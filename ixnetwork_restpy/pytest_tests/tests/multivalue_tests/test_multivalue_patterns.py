from __future__ import unicode_literals
from ipaddress import IPv4Address, ip_network
import pytest
import sys

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
    
    assert multivalue.Pattern == '1.1.1.1'


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


def test_set_random_multivalue(multivalue):
    multivalue.Overlay(3, '1.2.3.4')
    multivalue.Overlay(6, '4.3.2.1')
    multivalue.Random()
    assert(multivalue.Pattern.startswith('Rand') is True)


def test_multivalue_can_set_random_range(multivalue):
    multivalue.Overlay(3, '1.2.3.4')
    multivalue.Overlay(6, '4.3.2.1')
    # set repeatable random range multivalue
    multivalue.RandomRange(min_value='1.1.1.1', max_value='2.2.2.2', step_value='0.0.0.1', seed=7)
    assert(multivalue.Pattern.startswith('Randr:') is True)


def test_multivalue_can_set_random_mask(multivalue):
    multivalue.Overlay(3, '1.2.3.4')
    multivalue.Overlay(6, '4.3.2.1')
    # set repeatable random multivalue
    multivalue.RandomMask(fixed_value='1.1.1.1', mask_value='0.0.0.1', seed=7, count=6)
    assert(multivalue.Pattern.startswith('Randb:') is True)


def test_mulivalue_can_set_distributed(multivalue):
    print(multivalue)
    multivalue.Distributed(algorithm='autoEven', mode='perPort', values=[('1.1.1.1', 60), ('2.2.2.2', 40)])
    assert(multivalue.Pattern.startswith('Dist:'))


def test_multivalue_can_set_custom(multivalue):
    multivalue.Custom(start_value='1.1.1.1', step_value='1.1.1.2', increments=[('1.1.1.3', 6, [('1.1.1.4', 2, None)])])
    assert(multivalue.Pattern.startswith('Custom:'))


def test_multivalue_can_set_overlay(multivalue):
    base_ip = '1.1.1.1'
    multivalue.Decrement(start_value=base_ip, step_value='0.0.0.1')
    multivalue.Overlay(2,'2.2.2.2')
    assert(multivalue.Values[1] == '2.2.2.2')

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
    assert info is not None

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