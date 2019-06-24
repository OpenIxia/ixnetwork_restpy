"""Sanity script
"""
import sys
import os
import json
from ixnetwork_restpy.testplatform.testplatform import TestPlatform
from ixnetwork_restpy.errors import IxNetworkError
from ixnetwork_restpy.files import Files

sessions = None

try:
    # test_platform = TestPlatform('10.36.78.53', platform='linux')
    test_platform = TestPlatform('127.0.0.1', rest_port=11009, platform='windows')
    test_platform.Trace = 'request_response'
    test_platform.Authenticate('admin', 'admin')
    print(test_platform)

    sessions = test_platform.Sessions.add()
    print(sessions)

    ixnetwork = sessions.Ixnetwork
    print(ixnetwork)
    ixnetwork.NewConfig()

    # create 2 ports
    vports = ixnetwork.Vport.add().add()

    # create a topology
    topology = ixnetwork.Topology.add(Name='Topology 1', Ports=vports)
    assert(len(topology) == 1)

    # create a device group
    device_group = topology.DeviceGroup.add(Name='Device 1', Multiplier='7')
    assert(len(device_group) == 1)
    device_group.Enabled.Alternate('False')
    assert (device_group.Enabled == 'Alt: False')
    
    # create and print ethernet information
    ethernet = device_group.Ethernet.add()
    assert(len(ethernet) == 1)

    # update multivalue on server immediately
    ethernet.Mac.Decrement(start_value='00:00:de:ad:be:ef', step_value='00:00:fa:ce:fa:ce')
    assert (ethernet.Mac == 'Dec: 00:00:de:ad:be:ef, 00:00:fa:ce:fa:ce')
    ethernet.Mac.Increment(start_value='00:00:fa:ce:fa:ce', step_value='00:00:de:ad:be:ef')
    assert (ethernet.Mac == 'Inc: 00:00:fa:ce:fa:ce, 00:00:de:ad:be:ef')
    ethernet.Mac.Random()
    assert (ethernet.Mac == 'Rand')
    ethernet.Mac.RandomRange()
    assert (ethernet.Mac.Pattern.startswith('Randr:'))
    ethernet.Mac.RandomMask()
    assert (ethernet.Mac.Pattern.startswith('Randb:'))
    ethernet.Mac.Distributed(algorithm='autoEven', mode='perPort', values=[('00:00:fa:ce:fa:ce', 60), ('0:00:de:ad:be:ef', 40)])
    assert (ethernet.Mac.Pattern.startswith('Dist:'))
    ethernet.Mac.ValueList(values=['00:00:fa:ce:fa:ce', '00:00:de:ad:be:ef'])
    assert (ethernet.Mac.Pattern.startswith('List:'))
    ethernet.Mac.Custom(start_value='00:00:fa:ce:fa:ce', step_value='00:00:de:ad:be:ef', increments=[('00:00:ab:ab:ab:ab', 6, [('00:00:01:01:01:01', 2, None)])])
    assert (ethernet.Mac.Pattern.startswith('Custom:'))
    print(ethernet.Mac.Values)
    
    ipv4 = ethernet.Ipv4.add(Name='Ipv4 1')
    print(ipv4)
    ipv4.Address.ValueList(['1.1.1.1', '1.1.1.2'])
    assert(ipv4.Address.Pattern.startswith('List:'))
    ipv4.Address.Increment(start_value='1.1.1.1', step_value='0.1.1.1')
    assert(ipv4.Address == 'Inc: 1.1.1.1, 0.1.1.1')
    
    ipv4.Start()
    
except IxNetworkError as e:
    print(e)

if sessions is not None:
    sessions.remove()


