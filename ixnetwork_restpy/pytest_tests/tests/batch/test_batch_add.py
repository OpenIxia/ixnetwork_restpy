# import pytest
# from ixnetwork_restpy import BatchAdd, Files
#
#
# # @pytest.mark.skip(reason="not implemented")
# def test_simple_batch_add(ixnetwork):
#     with BatchAdd(ixnetwork):
#         for i in range(0, 100):
#             ixnetwork.Vport.add(Name="Batch Add {}".format(i))
#
#     assert ixnetwork.Vport.find()[6].Name == "Batch Add 6"
#
#
# # @pytest.mark.skip(reason="not implemented")
# def test_batch_add_with_indexing(ixnetwork):
#     with BatchAdd(ixnetwork):
#         vp = ixnetwork.Vport.add(Name='vp1').add(Name='vp2')
#         ixnetwork.Topology.add(Vports=vp[0]).add(Vports=vp[1])
#         dg = ixnetwork.Topology[0].DeviceGroup.add().add()
#         dg[0].Ethernet.add().Ipv4.add()
#         dg[1].Ethernet.add().Ipv6.add()
#         dg = ixnetwork.Topology[1].DeviceGroup.add().add()
#         dg[0].Ethernet.add().Ipv4.add().BgpIpv4Peer.add(Name="Bgp1")
#         dg[1].Ethernet.add().Ipv4.add().Ospfv2.add(Name="ospf-100.1.0.2")
#
#     assert len(ixnetwork.Vport.find()) == 2
#     topo = ixnetwork.Topology.find()
#     assert len(topo) == 2
#     assert len(topo[0].DeviceGroup.find()) == 2
#     assert len(topo[1].DeviceGroup.find()) == 2
#     dgs = topo.DeviceGroup.find()
#     assert dgs[3].Ethernet.find().Ipv4.find().Ospfv2.find().Name == "ospf-100.1.0.2"
#
#
# # @pytest.mark.skip(reason="not implemented")
# def test_multiple_batch_add_calls(ixnetwork):
#     with BatchAdd(ixnetwork):
#         vp = ixnetwork.Vport.add(Name='vp1').add(Name='vp2')
#         ixnetwork.Topology.add(Vports=vp[0]).add(Vports=vp[1])
#         dg = ixnetwork.Topology[0].DeviceGroup.add().add()
#
#     assert len(ixnetwork.Vport.find()) == 2
#     topo = ixnetwork.Topology.find()
#     assert len(topo) == 2
#     assert len(topo[0].DeviceGroup.find()) == 2
#
#     with BatchAdd(ixnetwork):
#         ixnetwork.Vport.add(Name='vp3').add(Name='vp4')
#         ixnetwork.Topology.DeviceGroup.add(Multiplier=12, Name='new').add(Multiplier=12, Name='latest')
#
#     vp = ixnetwork.Vport.find()
#     assert len(vp) == 4
#     assert vp[2].Name == "vp3"
#     assert ixnetwork.Topology.find().DeviceGroup.find()[-1].Name == "latest"
#
#
# # @pytest.mark.skip(reason="not implemented")
# def test_batch_add_with_load_config(ixnetwork):
#     ixnetwork.LoadConfig(Files(r'C:\pycharm_projs\restpy_bitbucket\src\sample.ixncfg'))
#     topo = ixnetwork.Topology.find()
#     with BatchAdd(ixnetwork):
#         topo[1].DeviceGroup.add(Multiplier=3, Name="my_dg")
#         topo[1].DeviceGroup.add(Multiplier=3, Name="my_dg2").Ethernet.add()
#
#     dgs = ixnetwork.Topology.find()[1].DeviceGroup.find()
#     assert len(dgs) == 6
#     assert len(dgs[-1].Ethernet.find()) == 1
#
#
# # @pytest.mark.skip(reason="not implemented")
# def test_batch_add_with_multiple_nodes(ixnetwork):
#     ixnetwork.LoadConfig(Files(r'C:\pycharm_projs\restpy_bitbucket\src\sample.ixncfg'))
#     topo = ixnetwork.Topology.find()
#     dgs = topo[1].DeviceGroup.find()
#     with BatchAdd(ixnetwork):
#         topo[1].DeviceGroup.add(Multiplier=3, Name="my_dg")
#         topo[1].DeviceGroup.add(Multiplier=3, Name="my_dg2").Ethernet.add()
#         dgs[3].Ethernet.add().Ipv6.add()
#
#     dgs = ixnetwork.Topology.find()[1].DeviceGroup.find()
#     assert len(dgs) == 6
#     assert len(dgs[-1].Ethernet.find()) == 1
#     assert len(dgs[3].Ethernet.find().Ipv6.find()) == 1
#     assert dgs[3].Ethernet.find().Ipv6.find().href == \
#            '/api/v1/sessions/1/ixnetwork/topology/2/deviceGroup/4/ethernet/1/ipv6/1'
#
#
# # @pytest.mark.skip(reason="not implemented")
# def test_batch_add_with_multivalues(ixnetwork):
#     with BatchAdd(ixnetwork):
#         vport = ixnetwork.Vport.add().add()
#         topo = ixnetwork.Topology.add(Name='Topology 1', Vports=vport[0]).add(Name='Topology 2', Vports=vport[1])
#
#         # testing out increment multivalue
#         eth1 = topo[0].DeviceGroup.add(Name='Increment', Multiplier='10').Ethernet.add()
#         eth1.Mac.Increment(start_value='00:11:22:33:44:55', step_value='00:11:01:00:00:01')
#         eth1.Mtu.Single('1670')
#         ipv41 = eth1.Ipv4.add(Name='Ipv4 East')
#         ipv41.Address.Increment(start_value='1.1.1.1', step_value='0.1.0.0')
#
#         # testing out decrement multivalue
#         eth2 = topo[0].DeviceGroup.add(Name='Decrement', Multiplier='10').Ethernet.add()
#         eth2.Mac.Decrement(start_value='22:11:22:33:44:55', step_value='00:11:01:00:00:01')
#         eth2.Mtu.Single('1670')
#         ipv42 = eth2.Ipv4.add(Name='Ipv4 East')
#         ipv42.Address.Decrement(start_value='10.10.1.1', step_value='0.1.0.0')
#
#         # testing out valueList multivalue
#         eth3 = topo[0].DeviceGroup.add(Name='ValueList', Multiplier='4').Ethernet.add()
#         eth_list = ['00:11:22:33:44:55', '00:00:22:33:44:55', '00:77:22:33:44:55', '00:aa:22:33:44:55']
#         eth3.Mac.ValueList(eth_list)
#         eth3.Mtu.Single('1670')
#         ipv43 = eth3.Ipv4.add(Name='Ipv4 East')
#         ip_list = ['1.1.1.1', '1.1.1.11', '1.1.11.1', '1.11.1.1']
#         ipv43.Address.ValueList(ip_list)
#
#         # testing out overlay multivalue
#         eth4 = topo[0].DeviceGroup.add(Name='Overlay', Multiplier='10').Ethernet.add()
#         eth4.Mac.Increment(start_value='22:11:22:33:44:55', step_value='00:11:01:00:00:01')
#         eth4.Mac.Overlay(4, '22:11:00:00:00:55')
#         eth4.Mac.Overlay(7, '00:11:00:00:00:55')
#         eth4.Mtu.Single('1670')
#         ipv44 = eth4.Ipv4.add(Name='Ipv4 East')
#         ipv44.Address.Increment(start_value='10.10.1.1', step_value='0.1.0.0')
#         ipv44.Address.Overlay(5, '4.4.4.4')
#         ipv44.Address.Overlay(7, '10.10.10.10')
#         ipv44.Address.Overlay(3, '99.33.66.77')
#         ipv44.Address.Overlay(9, '1.45.67.89')
#
#         # testing alternate and string multivalue
#         eth1 = topo[0].DeviceGroup.add(Name='String/Alternate', Multiplier='10').Ethernet.add()
#         eth1.Mac.Increment(start_value='00:11:22:33:44:55', step_value='00:11:01:00:00:01')
#         eth1.Mtu.Single('1670')
#         ipv41 = eth1.Ipv4.add(Name='Ipv4 East')
#         ipv41.Address.Increment(start_value='1.1.1.1', step_value='0.1.0.0')
#         ipv41.ResolveGateway.Alternate(False)
#         ospf = ipv41.Ospfv2.add()
#         ospf.AuthenticationPassword.String('{"ixia", "Keysight"}')
#
#         # testing out random multivalue
#         eth1 = topo[1].DeviceGroup.add(Name='Random', Multiplier='10').Ethernet.add()
#         eth1.Mac.Random()
#         eth1.Mtu.Single('1670')
#         ipv41 = eth1.Ipv4.add(Name='Ipv4 East')
#         ipv41.Address.Random()
#
#         # testing out custom multivalue
#         eth2 = topo[1].DeviceGroup.add(Name='Custom', Multiplier='10').Ethernet.add()
#         eth2.Mac.Random()
#         eth2.Mtu.Single('1670')
#         ipv42 = eth2.Ipv4.add(Name='Ipv4 East')
#         increment = [('1.1.1.1', 10, [('1.1.3.1', 3, []), ('1.3.3.1', 2, []), ('1.2.3.1', 1, [])]),
#                      ('1.1.2.1', 5, [('1.1.4.1', 4, [('1.1.5.1', 4, [])])])]
#         ipv42.Address.Custom(start_value='0.0.1.1', step_value='1.0.1.0', increments=increment)
#
#         # testing out distributed multivalue
#         eth3 = topo[1].DeviceGroup.add(Name='Distributed', Multiplier='10').Ethernet.add()
#         eth3.Mac.Random()
#         eth3.Mtu.Single('1670')
#         ipv43 = eth3.Ipv4.add(Name='Ipv4 East')
#         ipv43.Address.Distributed('percentage', 'perTopology', [('1.0.0.0', 16), ('0.0.0.1', 17), ('0.0.1.0', 17),
#                                                                 ('0.1.0.0', 16), ('2.0.0.0', 17), ('0.0.0.2', 17)])
#
#         # testing out RandomRange multivalue
#         eth4 = topo[1].DeviceGroup.add(Name='RandomRange', Multiplier='10').Ethernet.add()
#         eth4.Mac.RandomRange('00:01:02:00:00:00', 'ff:ff:ff:ff:ff:ff', '00:00:00:00:00:01', 6)
#         eth4.Mtu.Single('1670')
#         ipv44 = eth4.Ipv4.add(Name='Ipv4 East')
#         ipv44.Address.RandomRange('1.2.3.4', '255.255.255.255', '0.1.3.0', 5)
#
#         # testing out RandomRange multivalue
#         eth5 = topo[1].DeviceGroup.add(Name='RandomMask', Multiplier='10').Ethernet.add()
#         eth5.Mac.RandomMask('00:01:02:00:00:00', '00:00:ff:ff:ff:ff', 5, 55)
#         eth5.Mtu.Single('1670')
#         ipv45 = eth5.Ipv4.add(Name='Ipv4 East')
#         ipv45.Address.RandomMask('1.2.3.4', '0.255.255.255', 5, 55)
#
#
# # @pytest.mark.skip(reason="not implemented")
# def test_batch_add_with_only_updates(ixnetwork):
#     vp = ixnetwork.Vport.add().add()
#     topo = ixnetwork.Topology.add(Name="topo1", Vports=vp[0]).add(Name="topo2", Vports=vp[1])
#     dg = topo[1].DeviceGroup.add(Name="dg1").add(Name="dg2").add(Name="dg3").add(Name="dg4")
#     with BatchAdd(ixnetwork):
#         topo[0].Name = "updated_topo1"
#         topo[1].Name = "updated_topo2"
#         dg[2].Name = "updated_dg3"
#         dg[3].Name = "updated_dg4"
#     topo = ixnetwork.Topology.find()
#     assert topo[0].Name == "updated_topo1"
#     assert topo[1].Name == "updated_topo2"
#     dgs = topo.DeviceGroup.find()
#     assert dg[2].Name == "updated_dg3"
#     assert dg[3].Name == "updated_dg4"
#
#
# # @pytest.mark.skip(reason="not implemented")
# def test_batch_add_with_dependent_attr(ixnetwork):
#     with BatchAdd(ixnetwork):
#         vport = ixnetwork.Vport.add().add()
#         vport[0].RxMode = 'captureAndMeasure'
#         vport[1].Name = 'myVport_2'
#         topo = ixnetwork.Topology.add(Name='Topology 1', Vports=vport[0]).add(Name='Topology 2', Vports=vport[1])
#         eth1 = topo[0].DeviceGroup.add(Name='Device Group 1', Multiplier='4').Ethernet.add()
#         eth1.Mac.Increment(start_value='00:11:22:33:44:55', step_value='00:11:01:00:00:01')
#         eth1.Mtu.Single('1670')
#         eth1.EnableVlans.Single(True)
#         eth1.VlanCount = 3
#         vlan = eth1.Vlan.add().add().add()
#         vlan[0].VlanId.Increment(10, 4)
#         vlan[1].VlanId.Increment(34, 1)
#         vlan[2].VlanId.Increment(46, 3)
#
#     vlan = ixnetwork.Topology.find()[0].DeviceGroup.find().Ethernet.find().Vlan.find()
#     assert len(vlan) == 3
#     assert vlan.parent.VlanCount == 3
#     assert vlan[0].href == '/api/v1/sessions/1/ixnetwork/topology/1/deviceGroup/1/ethernet/1/vlan/1'
#     assert vlan[0].VlanId.Values[0] == '10'
#     assert vlan[1].href == '/api/v1/sessions/1/ixnetwork/topology/1/deviceGroup/1/ethernet/1/vlan/2'
#     assert vlan[1].VlanId.Values[0] == '34'
#     assert vlan[2].href == '/api/v1/sessions/1/ixnetwork/topology/1/deviceGroup/1/ethernet/1/vlan/3'
#     assert vlan[2].VlanId.Values[0] == '46'
#
#
# # @pytest.mark.skip(reason="not implemented")
# def test_batch_add_with_traffic(ixnetwork):
#     with BatchAdd(ixnetwork):
#         virtual_ports = ixnetwork.Vport.add().add()
#         virtual_ports[0].Name = 'myVport_1'
#         virtual_ports[0].RxMode = 'captureAndMeasure'
#         virtual_ports[1].Name = 'myVport_2'
#         tr = ixnetwork.Traffic.TrafficItem.add(Name='RAW TCP', AllowSelfDestined=True, TrafficType='raw',
#                                                TrafficItemType='l2L3')
#         tr.BiDirectional = True
#         tr.SrcDestMesh = "oneToOne"
#         end = tr.EndpointSet.add(Sources=virtual_ports[0].Protocols.add(), Destinations=virtual_ports[1].Protocols.add(),
#                            ScalableSources=[], ScalableDestinations=[])
#     assert tr.href == '/api/v1/sessions/1/ixnetwork/traffic/trafficItem/1'
#     assert end.Sources[0] == '/vport[1]/protocols'
#     assert end.Destinations[0] == '/vport[2]/protocols'
#
#
# # @pytest.mark.skip(reason="not implemented")
# def test_batch_add_with_classic_config(ixnetwork):
#     with BatchAdd(ixnetwork):
#         for i in range(0, 2):
#             vport = ixnetwork.Vport.add()
#             bgp = vport.Protocols.add().Bgp
#             for j in range(0, 4):
#                 int1 = vport.Interface.add(Enabled=True)
#                 int1.Ipv4.add(Ip='1.1.1.1', Gateway='1.1.1.2')
#                 bgp.Enabled = True
#                 neighbor_range1 = bgp.NeighborRange.add(Interfaces=int1, Enabled=True, EnableBgpId=True)
#
#     interfaces = ixnetwork.Vport.find().Interface.find()
#     assert interfaces[2].href == '/api/v1/sessions/1/ixnetwork/vport/1/interface/3'
#     assert interfaces[3].href == '/api/v1/sessions/1/ixnetwork/vport/1/interface/4'
#     bgp = ixnetwork.Vport.find().Protocols.find().Bgp.NeighborRange.find()
#     assert bgp[3].href == '/api/v1/sessions/1/ixnetwork/vport/1/protocols/bgp/neighborRange/4'
#     assert bgp[7].href == '/api/v1/sessions/1/ixnetwork/vport/2/protocols/bgp/neighborRange/4'
#
#     with BatchAdd(ixnetwork):
#         for bgp_peer in bgp:
#             bgp_peer.Enabled = False
#
#     bgp = ixnetwork.Vport.find().Protocols.find().Bgp.NeighborRange.find()
#     for bgp_peer in bgp:
#         assert bgp_peer.Enabled == False
#
#
# # @pytest.mark.skip(reason="not implemented")
# def test_batch_add_with_autogen_traffic_templates(ixnetwork):
#     with BatchAdd(ixnetwork):
#         vport = ixnetwork.Vport.add().add()
#         vport[0].Name = 'myVport_1'
#         vport[0].RxMode = 'captureAndMeasure'
#         vport[1].Name = 'myVport_2'
#         traffic = ixnetwork.Traffic.TrafficItem
#         tr1 = traffic.add(Name='RAW TCP', BiDirectional=False, TrafficType='raw', TrafficItemType='l2L3')
#         tr1.EndpointSet.add(Sources=vport[0].Protocols.add(), Destinations=vport[1].Protocols.add())
#         stack = tr1.ConfigElement.add().Stack.add()
#         eth_st = stack.Ethernet.add()
#         eth_st.SourceAddress.Single('00:11:00:00:22:00')
#         eth_st.DestinationAddress.Single('00:33:00:11:22:00')
#         dhcp_st = stack.Dhcp.add()
#         dhcp_st.OpCode.Single(2)
#         dhcp_st.HwType.Single(5)
#         dhcp_st.BroadcastFlag.Single(32768)
#         dhcp_st.ServerIP.Increment('1.2.3.4', '0.2.1.0')
#         dhcp_st.ClientIP.Decrement('12.13.14.15', '0.0.0.1')
#         dhcp_st.ClientHwAddress.Single('0aaa')
#         mld_st = stack.Mldv1.add()
#         mld_st.Type.Single(131)
#         mld_st.Code.Single(23)
#         # mld_st.MaximumResponseDelayValue.Single(15)
#         mld_st.Reserved.Single(2)
#         mld_st.MulticastAddress.Increment('22::ff')
#         igmp_st = stack.Igmpv1.add()
#         igmp_st.Type.Single(1)
#         igmp_st.Unused.Single('0xcc')
#         ip_list = ['1.2.3.4', '1.22.31.4', '1.12.3.4', '1.4.3.4']
#         igmp_st.GroupAddress.ValueList(ip_list)
#
#     stacks = ixnetwork.Traffic.TrafficItem.find().ConfigElement.find().Stack.find()
#     assert len(stacks) == 5
#     assert stacks[0].DisplayName == "Ethernet II"
#     assert stacks[1].DisplayName == "DHCP"
#     assert stacks[2].DisplayName == "MLDv1 "
#     assert stacks[3].DisplayName == "IGMPv1"
#
#
# if __name__ == "__main__":
#     pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
