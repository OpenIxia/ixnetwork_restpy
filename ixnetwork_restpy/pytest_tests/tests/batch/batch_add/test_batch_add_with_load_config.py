# testing load config with batch add
from ixnetwork_restpy.assistants.batch.batchadd import BatchAdd
from ixnetwork_restpy.files import Files
import pytest, os


def test_batch_add_with_load_config(ixnetwork):
    session = ixnetwork._parent
    file_name = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "sample.ixncfg"
    )
    session.UploadFile(file_name)
    ixnetwork.NewConfig()
    ixnetwork.LoadConfig(Files("sample.ixncfg", local_file=False))
    topo = ixnetwork.Topology.find()
    with BatchAdd(ixnetwork):
        topo[1].DeviceGroup.add(Multiplier=3, Name="my_dg")
        topo[1].DeviceGroup.add(Multiplier=3, Name="my_dg2").Ethernet.add()

    dgs = ixnetwork.Topology.find()[1].DeviceGroup.find()
    assert len(dgs) == 6
    assert len(dgs[-1].Ethernet.find()) == 1


def test_batch_add_with_multiple_nodes(ixnetwork):
    session = ixnetwork._parent
    file_name = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "sample.ixncfg"
    )
    session.UploadFile(file_name)
    ixnetwork.NewConfig()
    ixnetwork.LoadConfig(Files("sample.ixncfg", local_file=False))
    topo = ixnetwork.Topology.find()
    dgs = topo[1].DeviceGroup.find()
    with BatchAdd(ixnetwork):
        topo[1].DeviceGroup.add(Multiplier=3, Name="my_dg")
        topo[1].DeviceGroup.add(Multiplier=3, Name="my_dg2").Ethernet.add()
        dgs[3].Ethernet.add().Ipv6.add()

    dgs = ixnetwork.Topology.find()[1].DeviceGroup.find()
    assert len(dgs) == 6
    assert len(dgs[-1].Ethernet.find()) == 1
    assert len(dgs[3].Ethernet.find().Ipv6.find()) == 1
    assert (
        dgs[3].Ethernet.find().Ipv6.find().href
        == "/api/v1/sessions/1/ixnetwork/topology/2/deviceGroup/4/ethernet/1/ipv6/1"
    )


def test_batch_add_with_load_config_and_update_function(ixnetwork):
    session = ixnetwork._parent
    file_name = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "sample.ixncfg"
    )
    session.UploadFile(file_name)
    ixnetwork.NewConfig()
    ixnetwork.LoadConfig(Files("sample.ixncfg", local_file=False))
    topo = ixnetwork.Topology.find()
    dgs = topo[1].DeviceGroup.find()
    with BatchAdd(ixnetwork):
        topo[0].update(Name="new_name_1")
        topo[1].update(Name="new_name_2")
        dgs[2].update(Name="asdasd", Multiplier=100)
        dgs[3].update(Name="dg 3333 yeahhhh", Multiplier=1000)

    topo = ixnetwork.Topology.find()
    dgs = topo[1].DeviceGroup.find()
    assert topo[0].Name == "new_name_1"
    assert topo[1].Name == "new_name_2"
    assert dgs[2].Name == "asdasd" and dgs[2].Multiplier == 100
    assert dgs[3].Name == "dg 3333 yeahhhh" and dgs[3].Multiplier == 1000


def test_precedence_with_batch_add(ixnetwork):
    session = ixnetwork._parent
    file_name = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "sample2.ixncfg"
    )
    session.UploadFile(file_name)
    ixnetwork.NewConfig()
    ixnetwork.LoadConfig(Files("sample2.ixncfg", local_file=False))
    topo = ixnetwork.Topology.find()
    with BatchAdd(ixnetwork):
        topo[1].DeviceGroup.add(Multiplier=3, Name="my_dg")
        topo[1].DeviceGroup.add(Multiplier=3, Name="my_dg2").Ethernet.add()
        topo[0].DeviceGroup.add(Multiplier=3, Name="my_dg3").Ethernet.add().Ipv4.add()

    vports = ixnetwork.Vport.find()

    with BatchAdd(ixnetwork):
        topo[0].DeviceGroup.add(Multiplier=2, Name="my_dg4").Ethernet.add().add()
        tr1 = ixnetwork.Traffic.TrafficItem.add(
            Name="RAW traffic", BiDirectional=False, TrafficType="raw"
        )
        tr1.EndpointSet.add(
            Sources=vports[0].Protocols.add(), Destinations=vports[1].Protocols.add()
        )

    end_point = ixnetwork.Traffic.TrafficItem.find().EndpointSet.find()
    assert end_point.Sources[0] == "/api/v1/sessions/1/ixnetwork/vport/1/protocols"
    assert end_point.Destinations[0] == "/api/v1/sessions/1/ixnetwork/vport/2/protocols"


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
