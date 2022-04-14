import pytest
from ixnetwork_restpy.files import Files
from ixnetwork_restpy.assistants.batch.batchadd import BatchAdd
from ixnetwork_restpy.assistants.batch.batchfind import BatchFind


def test_simple_batch_add(ixnetwork):
    with BatchAdd(ixnetwork):
        for i in range(0, 100):
            ixnetwork.Vport.add(Name="Batch Add {}".format(i))

    assert ixnetwork.Vport.find()[6].Name == "Batch Add 6"


def test_batch_add_with_indexing(ixnetwork):
    with BatchAdd(ixnetwork):
        vp = ixnetwork.Vport.add(Name="vp1").add(Name="vp2")
        ixnetwork.Topology.add(Vports=vp[0]).add(Vports=vp[1])
        dg = ixnetwork.Topology[0].DeviceGroup.add().add()
        dg[0].Ethernet.add().Ipv4.add()
        dg[1].Ethernet.add().Ipv6.add()
        dg = ixnetwork.Topology[1].DeviceGroup.add().add()
        dg[0].Ethernet.add().Ipv4.add().BgpIpv4Peer.add(Name="Bgp1")
        dg[1].Ethernet.add().Ipv4.add().Ospfv2.add(Name="ospf-100.1.0.2")

    assert len(ixnetwork.Vport.find()) == 2
    topo = ixnetwork.Topology.find()
    assert len(topo) == 2
    assert len(topo[0].DeviceGroup.find()) == 2
    assert len(topo[1].DeviceGroup.find()) == 2
    dgs = topo.DeviceGroup.find()
    assert dgs[3].Ethernet.find().Ipv4.find().Ospfv2.find().Name == "ospf-100.1.0.2"


def test_multiple_batch_add_calls(ixnetwork):
    with BatchAdd(ixnetwork):
        vp = ixnetwork.Vport.add(Name="vp1").add(Name="vp2")
        ixnetwork.Topology.add(Vports=vp[0]).add(Vports=vp[1])
        dg = ixnetwork.Topology[0].DeviceGroup.add().add()

    assert len(ixnetwork.Vport.find()) == 2
    topo = ixnetwork.Topology.find()
    assert len(topo) == 2
    assert len(topo[0].DeviceGroup.find()) == 2

    with BatchAdd(ixnetwork):
        ixnetwork.Vport.add(Name="vp3").add(Name="vp4")
        ixnetwork.Topology.DeviceGroup.add(Multiplier=12, Name="new").add(
            Multiplier=12, Name="latest"
        )

    vp = ixnetwork.Vport.find()
    assert len(vp) == 4
    assert vp[2].Name == "vp3"
    assert ixnetwork.Topology.find().DeviceGroup.find()[-1].Name == "latest"


def test_batch_add_with_only_updates(ixnetwork):
    vp = ixnetwork.Vport.add().add()
    topo = ixnetwork.Topology.add(Name="topo1", Vports=vp[0]).add(
        Name="topo2", Vports=vp[1]
    )
    dg = (
        topo[1]
        .DeviceGroup.add(Name="dg1")
        .add(Name="dg2")
        .add(Name="dg3")
        .add(Name="dg4")
    )
    with BatchAdd(ixnetwork):
        topo[0].Name = "updated_topo1"
        topo[1].Name = "updated_topo2"
        dg[2].Name = "updated_dg3"
        dg[3].Name = "updated_dg4"
    topo = ixnetwork.Topology.find()
    assert topo[0].Name == "updated_topo1"
    assert topo[1].Name == "updated_topo2"
    dgs = topo.DeviceGroup.find()
    assert dg[2].Name == "updated_dg3"
    assert dg[3].Name == "updated_dg4"


def test_batch_add_with_update_function(ixnetwork):
    with BatchAdd(ixnetwork):
        vp = ixnetwork.Vport.add().add()
        vp[0].update(Name="vp1", RxMode="captureAndMeasure")
        vp[1].update(Name="vp2", RxMode="captureAndMeasure")
        topo = ixnetwork.Topology.add().add()
        topo[0].update(Name="topo1", Vports=vp[0])
        topo[1].update(Name="topo2", Vports=vp[1])

    vports = ixnetwork.Vport.find()
    assert vports[0].Name == "vp1" and vports[0].RxMode == "captureAndMeasure"
    assert vports[1].Name == "vp2" and vports[1].RxMode == "captureAndMeasure"
    topo = ixnetwork.Topology.find()
    assert topo[0].Name == "topo1" and topo[0].Vports[0] == vports[0].href
    assert topo[1].Name == "topo2" and topo[1].Vports[0] == vports[1].href


def test_batch_add_with_batch_find(ixnetwork):
    for i in range(0, 5):
        ixnetwork.Vport.add(Name="Batch Add {}".format(i))

    with BatchFind(ixnetwork) as ctx:
        ixnetwork.Vport.find()

    assert len(ctx.results.vport) == 5

    with BatchAdd(ixnetwork):
        ixnetwork.Topology.add(Vports=ctx.results.vport[0]).add(
            Vports=ctx.results.vport[1]
        ).add(Vports=ctx.results.vport[2]).add(Vports=ctx.results.vport[4])

    topo = ixnetwork.Topology.find()
    assert len(topo) == 4
    assert topo[0].Vports[0] == ctx.results.vport[0].href
    assert topo[3].Vports[0] == ctx.results.vport[4].href


def test_batch_add_with_delete_operation(ixnetwork):
    with BatchAdd(ixnetwork):
        ixnetwork.Vport.add().add().add().add()
        ixnetwork.Vport.remove()
        ixnetwork.Vport.add().add()

    assert len(ixnetwork.Vport.find()) == 2


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
