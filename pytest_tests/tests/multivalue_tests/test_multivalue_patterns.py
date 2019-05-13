from ipaddress import IPv4Address, ip_network
import pytest


@pytest.fixture
def multivalue(ixnetwork):
    vport_1 = ixnetwork.Vport.add(Name='ethernet-1')
    topology_1 = ixnetwork.Topology.add(Vports=vport_1)
    dg1 = topology_1.DeviceGroup.add()
    dg1.Multiplier = 50
    ipv4 = dg1.Ethernet.add().Ipv4.add()
    return ipv4.Address


def test_multivalue_can_retrieve_available_patterns(multivalue):
    patterns = multivalue.AvailablePatterns
    expected_patterns = ['singleValue', 'counter', 'custom', 'random', 'repeatableRandomRange', 'repeatableRandom',
                         'valueList', 'customDistributed']
    for pattern in expected_patterns:
        assert pattern in patterns


def test_multivalue_can_set_single_value(multivalue):
    multivalue.Single('1.1.1.1')
    # todo: ask how to retrieve pattern of multivalue
    # assert multivalue.Pattern.lower() == 'singlevalue'
    assert multivalue.Values[0] == '1.1.1.1'


def test_multivalue_can_set_increment_pattern(multivalue):
    base_ip = '1.1.1.1'
    multivalue.Increment(start_value=base_ip, step_value='0.0.0.1')
    ipv4_obj = IPv4Address(base_ip)
    for index, value in enumerate(multivalue.Values):
        assert value == str(ipv4_obj + index)


def test_multivalue_can_set_decrement_pattern(multivalue):
    base_ip = '1.1.1.1'
    multivalue.Decrement(start_value=base_ip, step_value='0.0.0.1')
    ipv4_obj = IPv4Address(base_ip)
    for index, value in enumerate(multivalue.Values):
        assert value == str(ipv4_obj - index)


def test_multivalue_can_set_value_list(multivalue):
    subnet = ip_network('1.1.1.0/24')
    hosts = [str(host) for host in subnet.hosts()][:50]
    multivalue.ValueList(values=hosts)
    for index, value in enumerate(multivalue.Values):
        assert value == hosts[index]


def test_multivalue_can_set_random(multivalue):
    multivalue.Random()
    # todo: improve this
    assert (multivalue == 'Rand')


def test_multivalue_can_set_random_range(multivalue):
    multivalue.RandomRange()
    # todo: improve this
    assert (multivalue.Pattern.startswith('Randr:'))


def test_multivalue_can_set_random_mask(multivalue):
    multivalue.RandomMask()
    assert (multivalue.Pattern.startswith('Randb:'))


def test_mulivalue_can_set_distributed(vports):
    vport_1, vport_2 = vports
    ixnetwork = vport_1._parent
    topo = ixnetwork.Topology.add(Vports=vports)
    dg_1 = topo.DeviceGroup.add(Multiplier=7)
    dg_1.Enabled.Alternate('False')
    ethernet = dg_1.Ethernet.add()
    ethernet.Mac.Distributed(algorithm='autoEven', mode='perPort',values=[('00:00:fa:ce:fa:ce', 60), ('0:00:de:ad:be:ef', 40)])
    # todo : improve this
    assert (ethernet.Mac.Pattern.startswith('Dist:'))


def test_multivalue_can_set_custom(ethernet_stacks):
    #todo: improve this
    eth_1, eth_2 = ethernet_stacks
    dg_1 = eth_1._parent
    dg_1.Multiplier = 7
    eth_1.Mac.Custom(start_value='00:00:fa:ce:fa:ce', step_value='00:00:de:ad:be:ef',
                      increments=[('00:00:ab:ab:ab:ab', 6, [('00:00:01:01:01:01', 2, None)])])
    assert (eth_1.Mac.Pattern.startswith('Custom:'))


def test_multivalue_can_set_overlay(multivalue):
    base_ip = '1.1.1.1'
    multivalue.Decrement(start_value=base_ip, step_value='0.0.0.1')
    multivalue.Overlay(2,'2.2.2.2')
    assert multivalue.Values[1] == '2.2.2.2'

def test_multivalue_can_clear_overlay(multivalue):
    base_ip = '1.1.1.1'
    multivalue.Decrement(start_value=base_ip, step_value='0.0.0.1')
    multivalue.Overlay(2,'2.2.2.2')
    multivalue.Overlay(3,'3.3.3.3')

    multivalue.ClearOverlays()
    values = multivalue.Values
    assert '2.2.2.2' not in values
    assert '3.3.3.3' not in values

def test_multivalue_can_retrieve_info(multivalue):
    info = multivalue.Info
    assert isinstance(info,str)

def test_multivalue_can_retrieve_source(multivalue):
    source = multivalue.Source
    assert source.split('/')[-1] == 'ipv4:1 -address'

def test_multivalue_can_retrieve_format(multivalue):
    format = multivalue.Format
    assert format == 'ipv4'

def test_multivalue_can_set_string(multivalue):
    ipv4 = multivalue._parent
    ospf=ipv4.Ospfv2.add()
    ospf.Authentication.Single('password')
    ospf.AuthenticationPassword.String('ixia123')
    assert all([x=='ixia123' for x in ospf.AuthenticationPassword.Values])

def test_can_check_available_enums_from_multivalue(multivalue):
    ipv4 = multivalue._parent
    ospf = ipv4.Ospfv2.add()
    enums = ospf.Authentication.AvailableEnums
    assert type(enums) == list
    assert len(enums) == 3
    assert all(enum in ['null','password','md5'] for enum in enums)

def test_multivalue_can_set_alternate_values(multivalue):
    ipv4 = multivalue._parent
    ipv4.ResolveGateway.Alternate(False)
    values = ipv4.ResolveGateway.Values
    # since device group multiplier is 50
    assert values.count('true') == 25
    assert values.count('false') == 25