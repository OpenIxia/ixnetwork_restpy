def test_can_add_raw_traffic_over_lags(ixnetwork):
    vports_1 = ixnetwork.Vport.add().add()
    lag_1 = ixnetwork.Lag.add(Name='Lag 1', Vports=vports_1)
    lag_1.ProtocolStack.add().Ethernet.add().Lagportlacp.add()
    vports_2 = ixnetwork.Vport.add().add()
    lag_2 = ixnetwork.Lag.add(Name='Lag 2', Vports=vports_2)
    lag_2.ProtocolStack.add().Ethernet.add().Lagportlacp.add()
    # a lag MUST be a part of a topology otherwise TrafficType=raw will fail
    ethernet1 = ixnetwork.Topology.add(Ports=lag_1).DeviceGroup.add().Ethernet.add()    
    ethernet2 = ixnetwork.Topology.add(Ports=lag_2).DeviceGroup.add().Ethernet.add()    
    traffic_item = ixnetwork.Traffic.TrafficItem.add(Name='Lag Traffic Item Sample', TrafficType='raw')
    endpoint_set = traffic_item.EndpointSet.add(Destinations=lag_2, Sources=lag_1)
    assert (len(endpoint_set.Sources) == 1)
    assert (len(endpoint_set.Destinations) == 1)


def test_can_add_raw_traffic_over_vports(ixnetwork):
    vport_1 = ixnetwork.Vport.add()
    vport_2 = ixnetwork.Vport.add()
    traffic_item = ixnetwork.Traffic.TrafficItem.add(Name='Raw Traffic Item Sample', TrafficType='raw', TrafficItemType='l2L3')
    endpoint_set = traffic_item.EndpointSet.add(Sources=vport_1.Protocols.find(), Destinations=vport_2.Protocols.find())
    assert (len(endpoint_set.Sources) == 1)
    assert (len(endpoint_set.Destinations) == 1)


def test_can_add_ipv4_traffic_over_scalable_source_multicast_receivers(ixnetwork):
    ipv4_1 = ixnetwork.Topology.add(Vports=ixnetwork.Vport.add()).DeviceGroup.add().Ethernet.add().Ipv4.add()
    igmp_host = ipv4_1.IgmpHost.add(Name='Igmp Host')
    ipv4_2 = ixnetwork.Topology.add(Vports=ixnetwork.Vport.add().add().add()).DeviceGroup.add().Ethernet.add().Ipv4.add()
    ipv4_2.IgmpQuerier.add(Name='Igmp Querier')
    scalable_sources = [
        {
            'arg1': ipv4_2.href,
            'arg2': 1,
            'arg3': 3,
            'arg4': 1,
            'arg5': 2
        },
        {
            'arg1': ipv4_2.href,
            'arg2': 1,
            'arg3': 3,
            'arg4': 9,
            'arg5': 2
        }
    ]
    multicast_receivers = [
        {
            'arg1': igmp_host.IgmpMcastIPv4GroupList.href,
            'arg2': 0,
            'arg3': 3,
            'arg4': 0
        },
        {
            'arg1': igmp_host.IgmpMcastIPv4GroupList.href,
            'arg2': 0,
            'arg3': 4,
            'arg4': 0
        },
        {
            'arg1': igmp_host.IgmpMcastIPv4GroupList.href,
            'arg2': 0,
            'arg3': 6,
            'arg4': 0
        },
        {
            'arg1': igmp_host.IgmpMcastIPv4GroupList.href,
            'arg2': 0,
            'arg3': 9,
            'arg4': 0
        }	
    ]
    traffic_item = ixnetwork.Traffic.TrafficItem.add(Name='Ipv4 Traffic Item Sample', TrafficType='ipv4', TrafficItemType='l2L3')
    endpoint_set = traffic_item.EndpointSet.add(ScalableSources=scalable_sources, MulticastReceivers=multicast_receivers)
    assert (len(endpoint_set.MulticastReceivers) == 4)
    assert (len(endpoint_set.ScalableSources) == 2)
    assert (len(traffic_item.ConfigElement.find().Stack.find(StackTypeId='ipv4')) == 1)


def test_can_add_ipv4_traffic_over_protocols(ixnetwork):
    ipv4_1 = ixnetwork.Topology.add(Vports=ixnetwork.Vport.add()).DeviceGroup.add().Ethernet.add().Ipv4.add(Name='Ipv4 West')
    ipv4_2 = ixnetwork.Topology.add(Vports=ixnetwork.Vport.add()).DeviceGroup.add().Ethernet.add().Ipv4.add(Name='Ipv4 East')
    traffic_item = ixnetwork.Traffic.TrafficItem.add(Name='Ipv4 Traffic Item Sample', TrafficType='ipv4', TrafficItemType='l2L3')
    endpoint_set = traffic_item.EndpointSet.add(Sources=ipv4_1, Destinations=ipv4_2)
    assert (len(endpoint_set.Sources) == 1)
    assert (len(endpoint_set.Destinations) == 1)
    assert (len(traffic_item.ConfigElement.find().Stack.find(StackTypeId='ipv4')) == 1)


def test_can_add_raw_traffic_over_custom_stack(ixnetwork):
    vport_1 = ixnetwork.Vport.add()
    vport_2 = ixnetwork.Vport.add()
    traffic_item = ixnetwork.Traffic.TrafficItem.add(Name='Raw Traffic Item Sample', TrafficType='raw', TrafficItemType='l2L3')
    traffic_item.EndpointSet.add(Sources=vport_1.Protocols.find(), Destinations=vport_2.Protocols.find())
    config_element = traffic_item.ConfigElement.find(EndpointSetId=1)
    ethernet_stack = config_element.Stack.find(StackTypeId='^ethernet$')
    vlan_protocol_template = ixnetwork.Traffic.ProtocolTemplate.find(StackTypeId='^vlan$')
    ipv4_protocol_template = ixnetwork.Traffic.ProtocolTemplate.find(StackTypeId='^ipv4$')
    udp_protocol_template = ixnetwork.Traffic.ProtocolTemplate.find(StackTypeId='^udp$')
    vlan_stack = config_element.Stack.read(ethernet_stack.AppendProtocol(vlan_protocol_template))
    ipv4_stack = config_element.Stack.read(vlan_stack.AppendProtocol(ipv4_protocol_template))
    udp_stack = config_element.Stack.read(ipv4_stack.AppendProtocol(udp_protocol_template))
    vlanStackTypeId =  vlan_stack.StackTypeId
    ipv4StackTypeId =  ipv4_stack.StackTypeId
    udpStackTypeId =  udp_stack.StackTypeId
    assert vlanStackTypeId == "vlan"
    assert ipv4StackTypeId == "ipv4"
    assert udpStackTypeId == "udp"