# this test basically test quick test traffic and also a check whether timeline node is working properly or not
import pytest


def test_timeline_node(ixnetwork):
    ipv41 = (
        ixnetwork.Topology.add(Vports=ixnetwork.Vport.add())
        .DeviceGroup.add(Name="Dg West")
        .Ethernet.add()
        .Ipv4.add(Name="Ipv4 West")
    )

    ipv42 = (
        ixnetwork.Topology.add(Vports=ixnetwork.Vport.add())
        .DeviceGroup.add(Name="Dg East")
        .Ethernet.add()
        .Ipv4.add(Name="Ipv4 East")
    )

    traffic = ixnetwork.Traffic.TrafficItem.add(Name="West -> East", TrafficType="ipv4")
    traffic.EndpointSet.add(Sources=ipv41, Destinations=ipv42)

    test_details = ixnetwork.Timeline.CreateTest(Arg2="rfc2544back2back", Arg3="none")
    assert "timeline/test/1" in test_details["arg1"]
    assert "quickTest/rfc2544back2back/1" in test_details["arg2"]
    assert len(test_details["arg3"]) == 0


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
