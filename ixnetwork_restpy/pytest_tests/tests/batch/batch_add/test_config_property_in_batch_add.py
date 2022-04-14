import pytest
import os
import json
from ixnetwork_restpy.assistants.batch.batchadd import BatchAdd


# testing if batch add property returns proper json
def test_config_property(ixnetwork):
    with BatchAdd(ixnetwork) as batch:
        vp = ixnetwork.Vport.add(Name="vp1").add(Name="vp2")
        ixnetwork.Topology.add(Vports=vp[0]).add(Vports=vp[1])
        dg = ixnetwork.Topology[0].DeviceGroup.add().add()
        dg[0].Ethernet.add().Ipv4.add()
        dg[1].Ethernet.add().Ipv6.add()
        dg = ixnetwork.Topology[1].DeviceGroup.add().add()
        dg[0].Ethernet.add().Ipv4.add().BgpIpv4Peer.add(Name="Bgp1")
        dg[1].Ethernet.add().Ipv4.add().Ospfv2.add(Name="ospf-100.1.0.2")

    assert isinstance(batch.config, list)
    assert len(batch.config) > 0


# test that proper exception is thrown if a user is accessing config property in wrong way
def test_exception_for_config_property_in_batch_add(ixnetwork):
    try:
        with BatchAdd(ixnetwork) as batch:
            vp = ixnetwork.Vport.add(Name="vp1").add(Name="vp2")
            ixnetwork.Topology.add(Vports=vp[0]).add(Vports=vp[1])
            dg = ixnetwork.Topology[0].DeviceGroup.add().add()
            dg[0].Ethernet.add().Ipv4.add()
            dg[1].Ethernet.add().Ipv6.add()
            dg = ixnetwork.Topology[1].DeviceGroup.add().add()
            dg[0].Ethernet.add().Ipv4.add().BgpIpv4Peer.add(Name="Bgp1")
            dg[1].Ethernet.add().Ipv4.add().Ospfv2.add(Name="ospf-100.1.0.2")
            conf = batch.config
    except Exception as error:
        assert (
            str(error)
            == "you are only allowed to access the config property after BatchAdd context is over"
        )


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
