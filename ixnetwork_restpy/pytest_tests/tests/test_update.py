"""Test the .update() functionality to ensure all
encapsulated resources are updated in a single call
"""

import pytest


def test_update(ixnetwork):
    # uncomment the following to see the full request and response
    # from ixnetwork_restpy import TestPlatform
    # ixnetwork.parent.parent.Trace = TestPlatform.TRACE_ALL

    # add two virtual ports
    vports = ixnetwork.Vport.add().add()
    assert len(vports) == 2

    # update the encapsulated virtual ports and verify the find() returns the
    # two updated virtual ports
    vports.update(TraceLevel="kDebug", TransmitIgnoreLinkStatus=True)
    vports = ixnetwork.Vport.find(TraceLevel="kDebug", TransmitIgnoreLinkStatus=True)
    assert len(vports) == 2


def test_update_for_classic_nodes(ixnetwork):
    # uncomment the following to see the full request and response
    # from ixnetwork_restpy import TestPlatform
    # ixnetwork.parent.parent.Trace = TestPlatform.TRACE_ALL

    # add two virtual ports
    vports = ixnetwork.Vport.add().add()
    assert len(vports) == 2

    # add classic Ethernet endpoints and range in respective vports
    vports[0].ProtocolStack.EthernetEndpoint.add().Range.add().add()
    vports[1].ProtocolStack.EthernetEndpoint.add().Range.add().add()
    eth_endpoint = vports.ProtocolStack.EthernetEndpoint.find()
    assert len(eth_endpoint) == 2
    eth_range = eth_endpoint.Range.find()
    assert len(eth_range) == 4

    # update the MacRange with certain values
    eth_range.MacRange.update(Enabled=False, Count=10)

    # finding the updated MacRanges and checking for updated values
    mac_ranges = (
        ixnetwork.Vport.find()
        .ProtocolStack.EthernetEndpoint.find()
        .Range.find()
        .MacRange
    )
    assert len(mac_ranges) == 4
    for mac_range in mac_ranges:
        assert mac_range.Enabled is False
        assert mac_range.Count == 10


def test_update_for_nodes_with_kwargs(ixnetwork):
    """
    update() functions which takes more than 255 arguments is changed to **kwargs
    This test basically checks those functions work properly with **kwargs
    """

    qt = ixnetwork.QuickTest.Rfc2544throughput.add()
    test_conf = qt.TestConfig
    framesize_list = ["68", "132", "256", "516", "1028", "1284", "1522"]
    test_conf.update(
        CalculateLatency=True,
        EnableMinFrameSize=True,
        FramesizeList=framesize_list,
        FrameSizeMode="custom",
    )

    test_conf.refresh()

    assert test_conf.CalculateLatency is True
    assert test_conf.EnableMinFrameSize is True
    assert test_conf.FrameSizeMode == "custom"
    for frame in test_conf.FramesizeList:
        assert frame in framesize_list


if __name__ == "__main__":
    pytest.main(["-s", "--server", "localhost:11009:windows", __file__])
