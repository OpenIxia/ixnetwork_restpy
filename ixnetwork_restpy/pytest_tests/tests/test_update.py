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
    mac_ranges = ixnetwork.Vport.find().ProtocolStack.EthernetEndpoint.find().Range.find().MacRange
    assert len(mac_ranges) == 4
    for mac_range in mac_ranges:
        assert mac_range.Enabled is False
        assert mac_range.Count == 10


if __name__ == "__main__":
    pytest.main(["-s", "--server", "localhost:11009:windows", __file__])
