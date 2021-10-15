from __future__ import unicode_literals
from ipaddress import IPv4Address, ip_network
import pytest
import sys


@pytest.fixture
def multivalue(config_assistant):
    """Returns a tuple of a multivalue object and the config_assistant"""
    config = config_assistant.config
    vport_1 = config.Vport.add(Name="ethernet-1")
    topology_1 = config.Topology.add(Vports=vport_1)
    dg1 = topology_1.DeviceGroup.add()
    dg1.Multiplier = 50
    ipv4 = dg1.Ethernet.add().Ipv4.add()
    config_assistant.commit()

    return config.Topology.find()[0].DeviceGroup.find()[0].Ethernet.find()[0].Ipv4.find()[0].Address, config_assistant


def test_multivalue_can_retrieve_available_patterns(multivalue):
    patterns = multivalue[0].AvailablePatterns
    expected_patterns = [
        "singleValue",
        "counter",
        "custom",
        "random",
        "repeatableRandomRange",
        "repeatableRandom",
        "valueList",
        "customDistributed",
    ]
    for pattern in expected_patterns:
        assert pattern in patterns


def test_multivalue_can_set_single_value(multivalue):
    multivalue[0].Single("1.1.1.1")

    assert multivalue[0].Pattern == "1.1.1.1"


def test_multivalue_can_set_increment_pattern(multivalue):
    base_ip = "1.1.1.1"
    multivalue[0].Increment(start_value=base_ip, step_value="0.0.0.1")
    ipv4_obj = IPv4Address(base_ip)
    for index, value in enumerate(multivalue[0].Values):
        assert value == str(ipv4_obj + index)


def test_multivalue_can_set_decrement_pattern(multivalue):
    base_ip = "1.1.1.1"
    multivalue[0].Decrement(start_value=base_ip, step_value="0.0.0.1")
    ipv4_obj = IPv4Address(base_ip)
    for index, value in enumerate(multivalue[0].Values):
        assert value == str(ipv4_obj - index)


def test_multivalue_can_set_value_list(multivalue):
    subnet = ip_network("1.1.1.0/24")
    hosts = [str(host) for host in subnet.hosts()][:50]
    multivalue[0].ValueList(values=hosts)
    for index, value in enumerate(multivalue[0].Values):
        assert value == hosts[index]


def test_set_random_multivalue(multivalue):
    multivalue[0].Overlay(3, "1.2.3.4")
    multivalue[0].Overlay(6, "4.3.2.1")
    multivalue[0].Random()
    assert multivalue[0].Pattern.startswith("Rand") is True


def test_multivalue_can_set_random_range(multivalue):
    multivalue[0].Overlay(3, "1.2.3.4")
    multivalue[0].Overlay(6, "4.3.2.1")
    # set repeatable random range multivalue
    multivalue[0].RandomRange(min_value="1.1.1.1", max_value="2.2.2.2", step_value="0.0.0.1", seed=7)
    assert multivalue[0].Pattern.startswith("Randr:") is True


def test_multivalue_can_set_random_mask(multivalue):
    multivalue[0].Overlay(3, "1.2.3.4")
    multivalue[0].Overlay(6, "4.3.2.1")
    # set repeatable random multivalue
    multivalue[0].RandomMask(fixed_value="1.1.1.1", mask_value="0.0.0.1", seed=7, count=6)
    assert multivalue[0].Pattern.startswith("Randb:") is True


def test_mulivalue_can_set_distributed(multivalue):
    multivalue[0].Distributed(algorithm="autoEven", mode="perPort", values=[("1.1.1.1", 60), ("2.2.2.2", 40)])
    assert multivalue[0].Pattern.startswith("Dist:")


def test_multivalue_can_set_custom(multivalue):
    multivalue[0].Custom(start_value="1.1.1.1", step_value="1.1.1.2", increments=[("1.1.1.3", 6, [("1.1.1.4", 2, None)])])
    assert multivalue[0].Pattern.startswith("Custom:")


def test_multivalue_can_set_overlay(multivalue):
    base_ip = "1.1.1.1"
    multivalue[0].Decrement(start_value=base_ip, step_value="0.0.0.1")
    multivalue[0].Overlay(2, "2.2.2.2")
    assert multivalue[0].Values[1] == "2.2.2.2"


def test_multivalue_can_clear_overlay(multivalue):
    base_ip = "1.1.1.1"
    multivalue[0].Decrement(start_value=base_ip, step_value="0.0.0.1")
    multivalue[0].Overlay(2, "2.2.2.2")
    multivalue[0].Overlay(3, "3.3.3.3")

    multivalue[0].ClearOverlays()
    values = multivalue[0].Values
    assert "2.2.2.2" not in values
    assert "3.3.3.3" not in values


def test_multivalue_can_retrieve_info(multivalue):
    info = multivalue[0].Info
    assert info is not None


def test_multivalue_can_retrieve_source(multivalue):
    source = multivalue[0].Source
    assert source.split("/")[-1] == "ipv4:1 -address"


def test_multivalue_can_retrieve_format(multivalue):
    format = multivalue[0].Format
    assert format == "ipv4"


def test_multivalue_can_set_string(multivalue):
    ipv4 = multivalue[0]._parent
    ospf = ipv4.Ospfv2.add()
    ospf.Authentication.Single("password")
    ospf.AuthenticationPassword.String("ixia123")
    multivalue[1].commit()
    ospf = ospf.find()[0]
    assert all([x == "ixia123" for x in ospf.AuthenticationPassword.Values])


def test_can_check_available_enums_from_multivalue(multivalue):
    ipv4 = multivalue[0]._parent
    ospf = ipv4.Ospfv2.add()
    multivalue[1].commit()
    ospf = ospf.find()[0]
    enums = ospf.Authentication.AvailableEnums
    assert type(enums) == list
    assert len(enums) == 3
    assert all(enum in ["null", "password", "md5"] for enum in enums)


def test_multivalue_can_set_alternate_values(multivalue):
    ipv4 = multivalue[0]._parent
    ipv4.ResolveGateway.Alternate(False)
    values = ipv4.ResolveGateway.Values
    # since device group multiplier is 50
    assert values.count("true") == 25
    assert values.count("false") == 25


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
