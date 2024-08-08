"""Test the .refresh() functionality to ensure all
encapsulated resources are refreshed in a single call
"""

import pytest


def test_update(ixnetwork):
    # uncomment the following to see the full request and response
    # from ixnetwork_restpy import TestPlatform
    # ixnetwork.parent.parent.Trace = TestPlatform.TRACE_ALL

    # add two virtual ports
    vports = ixnetwork.Vport.add().add()
    assert len(vports) == 2

    # update some of the encapsulated virtual ports
    vports[0].TraceLevel = "kDebug"
    vports[1].TransmitIgnoreLinkStatus = True

    # refresh the encapsulated resources and verify the retrieved resources
    # match what was updated
    vports.refresh()
    assert vports[0].TraceLevel == "kDebug"
    assert vports[0].TransmitIgnoreLinkStatus == False
    assert vports[1].TraceLevel == "kInfo"
    assert vports[1].TransmitIgnoreLinkStatus == True


def test_refresh_for_classic_nodes(ixnetwork):
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

    # updating few parameter of MacRange
    eth_range[2].MacRange.Count = 20
    eth_range[3].MacRange.Enabled = False
    eth_range[0].MacRange.Mac = "7A:FD:FE:CF:00:AA"

    # refresh the encapsulated resources and verify the retrieved resources
    # match what was updated
    eth_range.refresh()
    assert eth_range[2].MacRange.Count == 20
    assert eth_range[3].MacRange.Enabled is False
    assert eth_range[0].MacRange.Mac == "7A:FD:FE:CF:00:AA"


if __name__ == "__main__":
    pytest.main(["-s", "--server", "localhost:11009:windows", __file__])
