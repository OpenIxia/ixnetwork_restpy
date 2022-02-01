import pytest
import ixnetwork_restpy as ixn


def test_required_find(ixnetwork):
    """Batch find of a required node with property.

    The generator now adds a find for required nodes that can be used to reduce
    the returned results.
    """
    ixnetwork.parent.parent.Trace = ixn.TestPlatform.TRACE_INFO
    for _ in range(0, 5):
        vport = ixnetwork.Vport.add()
        for vlanid in range(0, 5):
            vport.Interface.add().Vlan.VlanEnable = vlanid % 2 == 0

    with ixn.BatchFind(ixnetwork) as ctx:
        ixnetwork.Vport.find().Interface.find().Vlan.find(VlanEnable=True)
    assert len(ctx.results.vport) == 5
    assert len(ctx.results.interface) == 25
    assert len(ctx.results.vlan) == 15


def test_multiple_from(ixnetwork):
    """Batch find where the from is a container that encapsulates multiple resources.

    The expectation is that all encapsulated resources in a container will
    be used in the batch find select.
    """
    ixnetwork.parent.parent.Trace = ixn.TestPlatform.TRACE_INFO
    for _ in range(0, 3):
        topology = ixnetwork.Topology.add()
        for _ in range(0, 3):
            topology.DeviceGroup.add().Ethernet.add().Ipv4.add()
    topology = ixnetwork.Topology.find()

    with ixn.BatchFind(topology) as ctx:
        topology.DeviceGroup.find().Ethernet.find().Ipv4.find()
    assert len(ctx.results.deviceGroup) == 9
    assert len(ctx.results.ethernet) == 9
    assert len(ctx.results.ipv4) == 9


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
