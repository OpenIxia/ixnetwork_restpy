def test_can_configure_ngpf_ipv4(config_assistant):

    config = config_assistant.config
    vports = config.Vport.add().add()


    topology = config.Topology.add(Name='Topology 1', Ports=vports)

    device_group = topology.DeviceGroup.add(Name='Device 1', Multiplier='7')
    device_group.Enabled.Alternate(False)
    
    ethernet = device_group.Ethernet.add()

    ethernet.Mac.Decrement(start_value='00:00:de:ad:be:ef', step_value='00:00:fa:ce:fa:ce')
    
    ipv4 = ethernet.Ipv4.add(Name='Ipv4 1')

    ipv4.Address.Increment(start_value='1.1.1.1', step_value='0.1.1.1')
    config_assistant.commit()

    topology = config.Topology.find()
    device_group = topology[0].DeviceGroup.find()
    ethernet = device_group[0].Ethernet.find()
    ipv4 = ethernet[0].Ipv4.find()
    print(device_group.Enabled)
    assert(ipv4.Address == 'Inc: 1.1.1.1, 0.1.1.1')
    assert(len(topology) == 1)
    assert(len(device_group) == 1)
    assert (device_group.Enabled == 'Alt: False')
    assert(len(ethernet) == 1)
    assert (ethernet.Mac == 'Dec: 00:00:de:ad:be:ef, 00:00:fa:ce:fa:ce')
       




