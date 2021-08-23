def test_can_add_raw_traffic_over_lags(config_assistant):
    config = config_assistant.config
    vports = config.Vport.add().add().add().add()
    vports_1 = vports[0:2]
    lag_1 = config.Lag.add(Name='Lag 1', Vports=vports_1)[-1]
    lag_1.ProtocolStack.add().Ethernet.add().Lagportlacp.add()
    vports_2 = vports[2:4]
    lag_2 = config.Lag.add(Name='Lag 2', Vports=vports_2)[-1]
    lag_2.ProtocolStack.add().Ethernet.add().Lagportlacp.add()
    # a lag MUST be a part of a topology otherwise TrafficType=raw will fail
    ethernet1 = config.Topology.add(Ports=lag_1).DeviceGroup.add().Ethernet.add()    
    ethernet2 = config.Topology.add(Ports=lag_2).DeviceGroup.add().Ethernet.add()    
    traffic_item = config.Traffic.TrafficItem.add(Name='Lag Traffic Item Sample', TrafficType='raw')
    endpoint_set = traffic_item.EndpointSet.add(Destinations=lag_2, Sources=lag_1)
    config_assistant.commit()
    endpoint_set = endpoint_set.find()[0]
    assert (len(endpoint_set.Sources) == 1)
    assert (len(endpoint_set.Destinations) == 1)


def test_can_add_raw_traffic_over_vports(config_assistant):
    config = config_assistant.config
    config_assistant.commit()
    config.NewConfig()
    config_assistant.commit()
    vport_1 = config.Vport.add()[-1]
    vport_2 = config.Vport.add()[-1]
    traffic_item = config.Traffic.TrafficItem.add(Name='Raw Traffic Item Sample', TrafficType='raw', TrafficItemType='l2L3')
    endpoint_set = traffic_item.EndpointSet.add(Sources=vport_1.Protocols, Destinations=vport_2.Protocols)
    config_assistant.commit()

    endpoint_set = endpoint_set.find()[0]
    assert (len(endpoint_set.Sources) == 1)
    assert (len(endpoint_set.Destinations) == 1)


def test_can_add_ipv4_traffic_over_scalable_source_multicast_receivers(config_assistant):
    config = config_assistant.config
    config_assistant.commit()
    config.NewConfig()
    config_assistant.commit()

    vport = config.Vport.add().add().add().add()
    ipv4_1 = config.Topology.add(Vports=vport[0]).DeviceGroup.add().Ethernet.add().Ipv4.add()
    igmp_host = ipv4_1.IgmpHost.add(Name='Igmp Host')
    ipv4_2 = config.Topology.add(Vports=vport[1:4]).DeviceGroup.add().Ethernet.add().Ipv4.add()
    ipv4_2.IgmpQuerier.add(Name='Igmp Querier')
    scalable_sources = [
        {
            'arg1': ipv4_2.xpath,
            'arg2': 1,
            'arg3': 3,
            'arg4': 1,
            'arg5': 2
        },
        {
            'arg1': ipv4_2.xpath,
            'arg2': 1,
            'arg3': 3,
            'arg4': 9,
            'arg5': 2
        }
    ]
    multicast_receivers = [
        {
            'arg1': igmp_host.IgmpMcastIPv4GroupList.xpath,
            'arg2': 0,
            'arg3': 3,
            'arg4': 0
        },
        {
            'arg1': igmp_host.IgmpMcastIPv4GroupList.xpath,
            'arg2': 0,
            'arg3': 4,
            'arg4': 0
        },
        {
            'arg1': igmp_host.IgmpMcastIPv4GroupList.xpath,
            'arg2': 0,
            'arg3': 6,
            'arg4': 0
        },
        {
            'arg1': igmp_host.IgmpMcastIPv4GroupList.xpath,
            'arg2': 0,
            'arg3': 9,
            'arg4': 0
        }	
    ]
    traffic_item = config.Traffic.TrafficItem.add(Name='Ipv4 Traffic Item Sample', TrafficType='ipv4', TrafficItemType='l2L3')
    endpoint_set = traffic_item.EndpointSet.add(ScalableSources=scalable_sources, MulticastReceivers=multicast_receivers)
    config_assistant.commit()
    traffic_item = config.Traffic.TrafficItem.find()[0]
    endpoint_set = traffic_item.EndpointSet.find()[0]
    assert (len(endpoint_set.MulticastReceivers) == 4)
    assert (len(endpoint_set.ScalableSources) == 2)
    assert (len(traffic_item.ConfigElement.find().Stack.find(StackTypeId='ipv4')) == 1)


def test_can_add_ipv4_traffic_over_protocols(config_assistant):
    config = config_assistant.config
    config_assistant.commit()
    config.NewConfig()
    config_assistant.commit()
    ipv4_1 = config.Topology.add(Vports=config.Vport.add()[-1]).DeviceGroup.add().Ethernet.add().Ipv4.add(Name='Ipv4 West')[-1]
    ipv4_2 = config.Topology.add(Vports=config.Vport.add()[-1]).DeviceGroup.add().Ethernet.add().Ipv4.add(Name='Ipv4 East')[-1]
    traffic_item = config.Traffic.TrafficItem.add(Name='Ipv4 Traffic Item Sample', TrafficType='ipv4', TrafficItemType='l2L3')
    endpoint_set = traffic_item.EndpointSet.add(Sources=ipv4_1, Destinations=ipv4_2)
    errs = config_assistant.commit()
    endpoint_set = endpoint_set.find()[0]
    assert (len(endpoint_set.Sources) == 1)
    assert (len(endpoint_set.Destinations) == 1)
    assert (len(traffic_item.ConfigElement.find().Stack.find(StackTypeId='ipv4')) == 1)


def test_can_add_raw_traffic_over_custom_stack(config_assistant):
    config = config_assistant.config
    config_assistant.commit()
    config.NewConfig()
    config_assistant.commit()

    vport_1 = config.Vport.add()[-1]
    vport_2 = config.Vport.add()[-1]
    traffic_item = config.Traffic.TrafficItem.add(Name='Raw Traffic Item Sample', TrafficType='raw', TrafficItemType='l2L3')
    traffic_item.EndpointSet.add(Sources=vport_1.Protocols, Destinations=vport_2.Protocols)
    config_element = traffic_item.ConfigElement
    eth = config_element.Stack.Ethernet.add()
    eth.DestinationAddress.Single('00:11:00:00:22:00')
    vlan = config_element.Stack.Vlan.add()
    vlan.VlanTagVlanID.Single('34')
    ipv4 = config_element.Stack.Ipv4.add()
    ipv4.Identification.Single('1')
    udp = config_element.Stack.Udp.add()
    udp.SrcPort.Single('45')
    config_assistant.commit()

    config_element = config.Traffic.TrafficItem.find()[0].ConfigElement.find()[0]
    stacks = config_element.Stack.find()
    vlanStackTypeId = stacks[1].StackTypeId
    ipv4StackTypeId = stacks[2].StackTypeId
    udpStackTypeId = stacks[3].StackTypeId
    assert vlanStackTypeId == "vlan"
    assert ipv4StackTypeId == "ipv4"
    assert udpStackTypeId == "udp"
