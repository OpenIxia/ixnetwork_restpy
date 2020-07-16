def test_can_configure_ngpf_ipv4(ixnetwork):

    vports = ixnetwork.Vport.add().add()


    topology = ixnetwork.Topology.add(Name='Topology 1', Ports=vports)
    assert(len(topology) == 1)

    device_group = topology.DeviceGroup.add(Name='Device 1', Multiplier='7')
    assert(len(device_group) == 1)
    device_group.Enabled.Alternate('False')
    assert (device_group.Enabled == 'Alt: False')
    
    ethernet = device_group.Ethernet.add()
    assert(len(ethernet) == 1)

    ethernet.Mac.Decrement(start_value='00:00:de:ad:be:ef', step_value='00:00:fa:ce:fa:ce')
    assert (ethernet.Mac == 'Dec: 00:00:de:ad:be:ef, 00:00:fa:ce:fa:ce')
    
    ipv4 = ethernet.Ipv4.add(Name='Ipv4 1')

    ipv4.Address.ValueList(['1.1.1.1', '1.1.1.2'])
    assert(ipv4.Address.Pattern.startswith('List:'))
    ipv4.Address.Increment(start_value='1.1.1.1', step_value='0.1.1.1')
    assert(ipv4.Address == 'Inc: 1.1.1.1, 0.1.1.1')
       




