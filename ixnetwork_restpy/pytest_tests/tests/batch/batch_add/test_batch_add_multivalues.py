# testing the multivalues functionality with batch add
from ixnetwork_restpy.assistants.batch.batchadd import BatchAdd
import pytest


def test_only_update_multivalues_with_batch_add(ixnetwork):
    vp = ixnetwork.Vport.add(Name="vp1").add(Name="vp2")
    ixnetwork.Topology.add(Vports=vp[0]).add(Vports=vp[1])
    dg = ixnetwork.Topology.find()[0].DeviceGroup.add().add()
    dg[0].Ethernet.add().Ipv4.add()
    dg[1].Ethernet.add().Ipv6.add()
    dg = ixnetwork.Topology.find()[1].DeviceGroup.add().add()
    dg[0].Ethernet.add().Ipv4.add().BgpIpv4Peer.add(Name="Bgp1")
    dg[1].Ethernet.add().Ipv4.add().Ospfv2.add(Name="ospf-100.1.0.2")

    with BatchAdd(ixnetwork):
        ip = dg[0].Ethernet.find().Ipv4.find()
        ip.Address.Increment(start_value="1.1.1.1", step_value="0.1.0.0")
        ip.GatewayIp.Increment(start_value="1.1.1.0", step_value="0.1.0.0")


def test_batch_add_with_combination_of_multivalue_pattern(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add().add()
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0]).add(
            Name="Topology 2", Vports=vport[1]
        )

        # testing out increment multivalue
        eth1 = topo[0].DeviceGroup.add(Name="Increment", Multiplier="10").Ethernet.add()
        eth1.Mac.Increment(
            start_value="00:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        eth1.Mtu.Single("1670")
        ipv41 = eth1.Ipv4.add(Name="Ipv4 East")
        ipv41.Address.Increment(start_value="1.1.1.1", step_value="0.1.0.0")

        # testing out decrement multivalue
        eth2 = topo[0].DeviceGroup.add(Name="Decrement", Multiplier="10").Ethernet.add()
        eth2.Mac.Decrement(
            start_value="22:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        eth2.Mtu.Single("1670")
        ipv42 = eth2.Ipv4.add(Name="Ipv4 East")
        ipv42.Address.Decrement(start_value="10.10.1.1", step_value="0.1.0.0")

        # testing out valueList multivalue
        eth3 = topo[0].DeviceGroup.add(Name="ValueList", Multiplier="4").Ethernet.add()
        eth_list = [
            "00:11:22:33:44:55",
            "00:00:22:33:44:55",
            "00:77:22:33:44:55",
            "00:aa:22:33:44:55",
        ]
        eth3.Mac.ValueList(eth_list)
        eth3.Mtu.Single("1670")
        ipv43 = eth3.Ipv4.add(Name="Ipv4 East")
        ip_list = ["1.1.1.1", "1.1.1.11", "1.1.11.1", "1.11.1.1"]
        ipv43.Address.ValueList(ip_list)

        # testing out overlay multivalue
        eth4 = topo[0].DeviceGroup.add(Name="Overlay", Multiplier="10").Ethernet.add()
        eth4.Mac.Increment(
            start_value="22:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        eth4.Mac.Overlay(4, "22:11:00:00:00:55")
        eth4.Mac.Overlay(7, "00:11:00:00:00:55")
        eth4.Mtu.Single("1670")
        ipv44 = eth4.Ipv4.add(Name="Ipv4 East")
        ipv44.Address.Increment(start_value="10.10.1.1", step_value="0.1.0.0")
        ipv44.Address.Overlay(5, "4.4.4.4")
        ipv44.Address.Overlay(7, "10.10.10.10")
        ipv44.Address.Overlay(3, "99.33.66.77")
        ipv44.Address.Overlay(9, "1.45.67.89")

        # testing alternate and string multivalue
        eth1 = (
            topo[0]
            .DeviceGroup.add(Name="String/Alternate", Multiplier="10")
            .Ethernet.add()
        )
        eth1.Mac.Increment(
            start_value="00:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        eth1.Mtu.Single("1670")
        ipv41 = eth1.Ipv4.add(Name="Ipv4 East")
        ipv41.Address.Increment(start_value="1.1.1.1", step_value="0.1.0.0")
        ipv41.ResolveGateway.Alternate(False)
        ospf = ipv41.Ospfv2.add()
        ospf.AuthenticationPassword.String('{"ixia", "Keysight"}')

        # testing out random multivalue
        eth1 = topo[1].DeviceGroup.add(Name="Random", Multiplier="10").Ethernet.add()
        eth1.Mac.Random()
        eth1.Mtu.Single("1670")
        ipv41 = eth1.Ipv4.add(Name="Ipv4 East")
        ipv41.Address.Random()

        # testing out custom multivalue
        eth2 = topo[1].DeviceGroup.add(Name="Custom", Multiplier="10").Ethernet.add()
        eth2.Mac.Random()
        eth2.Mtu.Single("1670")
        ipv42 = eth2.Ipv4.add(Name="Ipv4 East")
        increment = [
            (
                "1.1.1.1",
                10,
                [("1.1.3.1", 3, []), ("1.3.3.1", 2, []), ("1.2.3.1", 1, [])],
            ),
            ("1.1.2.1", 5, [("1.1.4.1", 4, [("1.1.5.1", 4, [])])]),
        ]
        ipv42.Address.Custom(
            start_value="0.0.1.1", step_value="1.0.1.0", increments=increment
        )

        # testing out distributed multivalue
        eth3 = (
            topo[1].DeviceGroup.add(Name="Distributed", Multiplier="10").Ethernet.add()
        )
        eth3.Mac.Random()
        eth3.Mtu.Single("1670")
        ipv43 = eth3.Ipv4.add(Name="Ipv4 East")
        ipv43.Address.Distributed(
            "percentage",
            "perTopology",
            [
                ("1.0.0.0", 16),
                ("0.0.0.1", 17),
                ("0.0.1.0", 17),
                ("0.1.0.0", 16),
                ("2.0.0.0", 17),
                ("0.0.0.2", 17),
            ],
        )

        # testing out RandomRange multivalue
        eth4 = (
            topo[1].DeviceGroup.add(Name="RandomRange", Multiplier="10").Ethernet.add()
        )
        eth4.Mac.RandomRange(
            "00:01:02:00:00:00", "ff:ff:ff:ff:ff:ff", "00:00:00:00:00:01", 6
        )
        eth4.Mtu.Single("1670")
        ipv44 = eth4.Ipv4.add(Name="Ipv4 East")
        ipv44.Address.RandomRange("1.2.3.4", "255.255.255.255", "0.1.3.0", 5)

        # testing out RandomRange multivalue
        eth5 = (
            topo[1].DeviceGroup.add(Name="RandomMask", Multiplier="10").Ethernet.add()
        )
        eth5.Mac.RandomMask("00:01:02:00:00:00", "00:00:ff:ff:ff:ff", 5, 55)
        eth5.Mtu.Single("1670")
        ipv45 = eth5.Ipv4.add(Name="Ipv4 East")
        ipv45.Address.RandomMask("1.2.3.4", "0.255.255.255", 5, 55)


def test_batch_add_with_single_multivalue_pattern(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add()
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0])
        eth1 = topo[0].DeviceGroup.add(Name="Single", Multiplier="10").Ethernet.add()
        eth1.Mtu.Single("1670")

    assert eth1.refresh().Mtu.Pattern == "1670"


def test_batch_add_with_increment_multivalue_pattern(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add()
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0])
        eth1 = topo[0].DeviceGroup.add(Name="Single", Multiplier="10").Ethernet.add()
        eth1.Mac.Increment(
            start_value="00:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )

    assert eth1.refresh().Mac.Pattern == "Inc: 00:11:22:33:44:55, 00:11:01:00:00:01"


def test_batch_add_with_decrement_multivalue_pattern(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add()
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0])
        eth1 = topo[0].DeviceGroup.add(Name="Single", Multiplier="10").Ethernet.add()
        eth1.Mac.Decrement(
            start_value="00:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )

    assert eth1.refresh().Mac.Pattern == "Dec: 00:11:22:33:44:55, 00:11:01:00:00:01"


def test_batch_add_with_value_list_multivalue_pattern(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add()
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0])
        ip = (
            topo[0]
            .DeviceGroup.add(Name="Single", Multiplier="10")
            .Ethernet.add()
            .Ipv4.add()
        )
        ip_list = ["1.1.1.1", "1.1.1.11", "1.1.11.1", "1.11.1.1"]
        ip.Address.ValueList(ip_list)

    assert ip.refresh().Address.Pattern == "List: 1.1.1.1, 1.1.1.11, 1.1.11.1, 1.11.1.1"


def test_batch_add_with_random_multivalue_pattern(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add()
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0])
        eth = topo[0].DeviceGroup.add(Name="Single", Multiplier="10").Ethernet.add()
        eth.Mac.Random()

    assert eth.refresh().Mac.Pattern == "Rand"


def test_batch_add_with_random_range_multivalue_pattern(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add()
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0])
        eth = topo[0].DeviceGroup.add(Name="Single", Multiplier="10").Ethernet.add()
        eth.Mac.RandomRange(
            "00:01:02:00:00:00", "ff:ff:ff:ff:ff:ff", "00:00:00:00:00:01", 6
        )

    assert (
        eth.refresh().Mac.Pattern
        == "Randr: 00:01:02:00:00:00, ff:ff:ff:ff:ff:ff, 00:00:00:00:00:01, 6"
    )


def test_batch_add_with_random_mask_multivalue_pattern(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add()
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0])
        eth = topo[0].DeviceGroup.add(Name="Single", Multiplier="10").Ethernet.add()
        eth.Mac.RandomMask("00:01:02:00:00:00", "00:00:ff:ff:ff:ff", 5, 55)

    assert (
        eth.refresh().Mac.Pattern
        == "Randb: 00:01:02:00:00:00, 00:00:ff:ff:ff:ff, 5, 55"
    )


def test_batch_add_with_overlay_multivalue_pattern(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add()
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0])
        eth = topo[0].DeviceGroup.add(Name="Single", Multiplier="10").Ethernet.add()
        eth.Mac.Increment(
            start_value="22:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        eth.Mac.Overlay(4, "22:11:00:00:00:55")
        eth.Mac.Overlay(7, "00:11:00:00:00:55")

    assert eth.refresh().Mac.Pattern == "Inc: 22:11:22:33:44:55, 00:11:01:00:00:01"
    values = eth.Mac.Values
    assert values[3] == "22:11:00:00:00:55"
    assert values[6] == "00:11:00:00:00:55"


def test_batch_add_with_custom_multivalue_pattern(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add()
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0])
        ip = (
            topo[0]
            .DeviceGroup.add(Name="Single", Multiplier="10")
            .Ethernet.add()
            .Ipv4.add()
        )
        increment = [
            (
                "1.1.1.1",
                10,
                [("1.1.3.1", 3, []), ("1.3.3.1", 2, []), ("1.2.3.1", 1, [])],
            ),
            ("1.1.2.1", 5, [("1.1.4.1", 4, [("1.1.5.1", 4, [])])]),
        ]
        ip.Address.Custom(
            start_value="0.0.1.1", step_value="1.0.1.0", increments=increment
        )

    assert (
        ip.refresh().Address.Pattern
        == "Custom: 1.0.1.0, 1.0.1.0, [(1.1.1.1, 10, [(1.1.3.1, 3, []),(1.3.3.1, 2, []),(1.2.3.1, 1, [])]),(1.1.2.1, 5, [(1.1.4.1, 4, [(1.1.5.1, 4, [])])])]"
    )


def test_batch_add_with_custom_distributed_multivalue_pattern(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add()
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0])
        ip = (
            topo[0]
            .DeviceGroup.add(Name="Single", Multiplier="10")
            .Ethernet.add()
            .Ipv4.add()
        )
        ip.Address.Distributed(
            "percentage",
            "perTopology",
            [
                ("1.0.0.0", 16),
                ("0.0.0.1", 17),
                ("0.0.1.0", 17),
                ("0.1.0.0", 16),
                ("2.0.0.0", 17),
                ("0.0.0.2", 17),
            ],
        )

    assert (
        ip.refresh().Address.Pattern
        == "Dist: percentage, perTopology, [(1.0.0.0, 16.0),(0.0.0.1, 17.0),(0.0.1.0, 17.0),(0.1.0.0, 16.0),(2.0.0.0, 17.0),(0.0.0.2, 17.0)]"
    )


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
