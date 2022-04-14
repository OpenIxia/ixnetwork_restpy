# testing classic nodes with batch add
from ixnetwork_restpy.assistants.batch.batchadd import BatchAdd
import pytest


def test_batch_add_with_dependent_attr(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add().add()
        vport[0].RxMode = "captureAndMeasure"
        vport[1].Name = "myVport_2"
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0]).add(
            Name="Topology 2", Vports=vport[1]
        )
        eth1 = (
            topo[0]
            .DeviceGroup.add(Name="Device Group 1", Multiplier="4")
            .Ethernet.add()
        )
        eth1.Mac.Increment(
            start_value="00:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        eth1.Mtu.Single("1670")
        eth1.EnableVlans.Single(True)
        eth1.VlanCount = 3
        vlan = eth1.Vlan.add().add().add()
        vlan[0].VlanId.Increment(10, 4)
        vlan[1].VlanId.Increment(34, 1)
        vlan[2].VlanId.Increment(46, 3)

    vlan = ixnetwork.Topology.find()[0].DeviceGroup.find().Ethernet.find().Vlan.find()
    assert len(vlan) == 3
    assert vlan.parent.VlanCount == 3
    assert (
        vlan[0].href
        == "/api/v1/sessions/1/ixnetwork/topology/1/deviceGroup/1/ethernet/1/vlan/1"
    )
    assert vlan[0].VlanId.Values[0] == "10"
    assert (
        vlan[1].href
        == "/api/v1/sessions/1/ixnetwork/topology/1/deviceGroup/1/ethernet/1/vlan/2"
    )
    assert vlan[1].VlanId.Values[0] == "34"
    assert (
        vlan[2].href
        == "/api/v1/sessions/1/ixnetwork/topology/1/deviceGroup/1/ethernet/1/vlan/3"
    )
    assert vlan[2].VlanId.Values[0] == "46"


def test_batch_add_with_classic_config(ixnetwork):
    with BatchAdd(ixnetwork):
        for i in range(0, 2):
            vport = ixnetwork.Vport.add()
            bgp = vport.Protocols.add().Bgp
            for j in range(0, 4):
                int1 = vport.Interface.add(Enabled=True)
                int1.Ipv4.add(Ip="1.1.1.1", Gateway="1.1.1.2")
                bgp.Enabled = True
                neighbor_range1 = bgp.NeighborRange.add(
                    Interfaces=int1, Enabled=True, EnableBgpId=True
                )

    interfaces = ixnetwork.Vport.find().Interface.find()
    assert interfaces[2].href == "/api/v1/sessions/1/ixnetwork/vport/1/interface/3"
    assert interfaces[3].href == "/api/v1/sessions/1/ixnetwork/vport/1/interface/4"
    bgp = ixnetwork.Vport.find().Protocols.find().Bgp.NeighborRange.find()
    assert (
        bgp[3].href
        == "/api/v1/sessions/1/ixnetwork/vport/1/protocols/bgp/neighborRange/4"
    )
    assert (
        bgp[7].href
        == "/api/v1/sessions/1/ixnetwork/vport/2/protocols/bgp/neighborRange/4"
    )
    assert bgp[3].Interfaces == "/api/v1/sessions/1/ixnetwork/vport/1/interface/4"
    assert bgp[7].Interfaces == "/api/v1/sessions/1/ixnetwork/vport/2/interface/4"

    with BatchAdd(ixnetwork):
        for bgp_peer in bgp:
            bgp_peer.Enabled = False

    bgp = ixnetwork.Vport.find().Protocols.find().Bgp.NeighborRange.find()
    for bgp_peer in bgp:
        assert bgp_peer.Enabled is False


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
