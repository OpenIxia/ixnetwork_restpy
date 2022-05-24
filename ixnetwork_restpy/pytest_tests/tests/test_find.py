import pytest


def test_find_classic(ixnetwork):
    """
    This test basically checks for find operations in restPy classic nodes,
    which did not have find function earlier
    """
    for _ in range(0, 5):
        vport = ixnetwork.Vport.add()
        for vlanid in range(0, 5):
            vport.Interface.add().Vlan.VlanEnable = vlanid % 2 == 0

    assert len(ixnetwork.Vport.find().Interface.find().Vlan.find(VlanEnable=True)) == 15


def test_find_ngpf(ixnetwork):
    """
    This test basically checks for find operations in restPy ngpf nodes,
    which did not have find function earlier
    """
    for i in range(0, 5):
        srte_v4 = (
            ixnetwork.Topology.add()
            .DeviceGroup.add()
            .Ethernet.add()
            .Ipv4.add()
            .BgpIpv4Peer.add(NumberSRTEPolicies=1)
            .BgpSRTEPoliciesListV4
        )
        if i % 2 == 0:
            srte_v4.NumberOfTunnelsV4 = 2
    assert (
        len(
            ixnetwork.Topology.find()
            .DeviceGroup.find()
            .Ethernet.find()
            .Ipv4.find()
            .BgpIpv4Peer.find()
            .BgpSRTEPoliciesListV4.find(NumberOfTunnelsV4=2)
        )
    ) == 3


def test_find_with_kwargs(ixnetwork):
    """
    find() functions which takes more than 255 arguments is changed to **kwargs
    This test basically checks those functions work properly with **kwargs
    """

    port_stats = ixnetwork.Globals.Statistics.StatFilter.PortStatistics
    port_stats.Aal5FramesRx = False
    port_stats.AtmCellsRx = True

    stats = ixnetwork.Globals.Statistics.StatFilter.PortStatistics.find(
        Aal5FramesRx=False, AtmCellsRx=True
    )

    assert len(stats) == 1


if __name__ == "__main__":
    pytest.main(
        [
            "-v",
            "-s",
            "--server",
            "localhost:11009:windows",
            # "-k",  # runs only the following test
            # "test_find_classic",
            __file__,  # runs all tests in the file
        ]
    )
