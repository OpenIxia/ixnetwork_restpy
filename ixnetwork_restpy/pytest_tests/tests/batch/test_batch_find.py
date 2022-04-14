import pytest
from ixnetwork_restpy.assistants.batch.batchfind import BatchFind


def test_required_find(ixnetwork):
    """Batch find of a required node with property.

    The generator now adds a find for required nodes that can be used to reduce
    the returned results.
    """
    for _ in range(0, 5):
        vport = ixnetwork.Vport.add()
        for vlanid in range(0, 5):
            vport.Interface.add().Vlan.VlanEnable = vlanid % 2 == 0
    with BatchFind(ixnetwork) as ctx:
        ixnetwork.Vport.find().Interface.find().Vlan.find(VlanEnable=True)
    assert len(ctx.results.vport) == 5
    assert len(ctx.results.interface) == 25
    assert len(ctx.results.vlan) == 15


def test_multiple_from(ixnetwork):
    """Batch find where the from is a container that encapsulates multiple resources.

    The expectation is that all encapsulated resources in a container will
    be used in the batch find select.
    """
    for _ in range(0, 3):
        topology = ixnetwork.Topology.add()
        for _ in range(0, 3):
            topology.DeviceGroup.add().Ethernet.add().Ipv4.add()
    topology = ixnetwork.Topology.find()

    with BatchFind(topology) as ctx:
        topology.DeviceGroup.find().Ethernet.find().Ipv4.find()
    assert len(ctx.results.deviceGroup) == 9
    assert len(ctx.results.ethernet) == 9
    assert len(ctx.results.ipv4) == 9


def test_mix_of_required_and_primitive_nodes(ixnetwork):
    """Batch find of a required node in traffic item & other primitive nodes
    with some property.

    The generator now adds a find for required nodes that can be used to reduce
    the returned results.
    """
    vport1 = ixnetwork.Vport.add(Name="Port1")
    vport2 = ixnetwork.Vport.add(Name="Port2")

    ixnetwork.Topology.add(Ports=vport1)
    ixnetwork.Topology.add(Ports=vport2)

    topology = ixnetwork.Topology.find()

    for topo in topology:
        for dg_id in range(0, 3):
            if dg_id == 0:
                dg = topo.DeviceGroup.add(Multiplier=2)
            else:
                dg = topo.DeviceGroup.add(Multiplier=10)
            dg.Ethernet.add().Ipv4.add()
    for _ in range(0, 5):
        traffic_item = ixnetwork.Traffic.TrafficItem.add(TrafficType="raw")
        traffic_item.EndpointSet.add(
            Sources=vport1.Protocols.find(), Destinations=vport2.Protocols.find()
        )
    with BatchFind(ixnetwork) as ctx:
        ixnetwork.Vport.find()
        ixnetwork.Topology.find().DeviceGroup.find(Multiplier=10)
        traffic_item = ixnetwork.Traffic.TrafficItem.find()
        traffic_item.DynamicUpdate.find()
        traffic_item.Tracking.find()
        traffic_item.TransmissionDistribution.find()
    assert len(ctx.results.vport) == 2
    assert ctx.results.vport[0].Name == "Port1"
    assert len(ctx.results.topology) == 2
    assert len(ctx.results.deviceGroup) == 4
    assert len(ctx.results.dynamicUpdate) == 5
    assert len(ctx.results.tracking) == 5
    assert len(ctx.results.transmissionDistribution) == 5


def test_bath_find_on_mix_of_nodes_with_different_multiplicity(ixnetwork):
    """Batch find of vports, topologies, deviceGroups, networkGroups, ethernet, Ipv4, BgpIpv4Peers,
    BgpEthernetSegments & Ipv4PrefixPools.

    The expectation is that all encapsulated resources in a container will
    be used in the batch find select.
    """
    vp = [ixnetwork.Vport.add(Name="vp1"), ixnetwork.Vport.add(Name="vp2")]

    tp1 = ixnetwork.Topology.add(Vports=vp[0])
    tp2 = ixnetwork.Topology.add(Vports=vp[1])

    dg1 = tp1.DeviceGroup.add()
    eth1 = dg1.Ethernet.add()
    bgpv41 = eth1.Ipv4.add().BgpIpv4Peer.add()
    bgpv41.EthernetSegmentsCountV4 = 1
    bgpv41.BgpEthernetSegmentV4

    ng1 = dg1.NetworkGroup.add(Name="NG BgpIpv4Peer")
    ip_pool1 = ng1.Ipv4PrefixPools.add(NumberOfAddresses=10)
    ip_pool1.NetworkAddress.Increment("2.4.8.9", "1.2.3.4")
    connector = ip_pool1.Connector.find()
    connector.ConnectedTo = bgpv41.href

    ng11 = dg1.NetworkGroup.add(Name="NG Ethernet Topo1")
    ip_pool11 = ng11.Ipv4PrefixPools.add(NumberOfAddresses=10)
    ip_pool11.NetworkAddress.Increment("1.4.8.9", "1.2.3.4")
    connector = ip_pool11.Connector.find()
    connector.ConnectedTo = eth1.href

    dg2 = tp2.DeviceGroup.add()
    eth2 = dg2.Ethernet.add()
    ng2 = dg2.NetworkGroup.add(Name="NG Ethernet Topo2")
    ip_pool2 = ng2.Ipv4PrefixPools.add(NumberOfAddresses=10)
    ip_pool2.NetworkAddress.Increment("1.2.8.9", "1.2.3.4")
    connector = ip_pool2.Connector.find()
    connector.ConnectedTo = eth2.href

    with BatchFind(ixnetwork) as ctx:
        dgs = ixnetwork.Topology.find().DeviceGroup.find()
        dgs.NetworkGroup.find()
        dgs.Ethernet.find().Ipv4.find().BgpIpv4Peer.find().BgpEthernetSegmentV4.find()
        ixnetwork.Vport.find()
    assert len(ctx.results.vport) == 2
    assert len(ctx.results.topology) == 2
    assert len(ctx.results.deviceGroup) == 2
    assert len(ctx.results.networkGroup) == 3
    assert len(ctx.results.ethernet) == 2
    assert len(ctx.results.ipv4) == 1
    assert len(ctx.results.bgpIpv4Peer) == 1
    assert len(ctx.results.bgpEthernetSegmentV4) == 1

    ng1 = ctx.results.topology[0].DeviceGroup.find().NetworkGroup.find()
    assert len(ng1) == 2
    assert ctx.results.networkGroup[0].Name == "NG BgpIpv4Peer"
    assert ctx.results.networkGroup[1].Name == "NG Ethernet Topo1"

    ng2 = ctx.results.topology[1].DeviceGroup.find().NetworkGroup.find()
    assert len(ng2) == 1
    assert ctx.results.networkGroup[2].Name == "NG Ethernet Topo2"
    assert ctx.results.networkGroup[2].Ipv4PrefixPools.find()[0].NumberOfAddresses == 10


if __name__ == "__main__":
    pytest.main(
        [
            "-v",
            "-s",
            "--server",
            "localhost:11009:windows",
            # "-k",  # runs only the following test
            # "test_multiple_from",
            __file__,  # runs all tests in the file
        ]
    )
