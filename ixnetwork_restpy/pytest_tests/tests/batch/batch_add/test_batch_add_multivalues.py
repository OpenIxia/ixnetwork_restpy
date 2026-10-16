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
        eth_inc = (
            topo[0].DeviceGroup.add(Name="Increment", Multiplier="10").Ethernet.add()
        )
        eth_inc.Mac.Increment(
            start_value="00:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        eth_inc.Mtu.Single("1670")
        ipv4_inc = eth_inc.Ipv4.add(Name="Ipv4 East")
        ipv4_inc.Address.Increment(start_value="1.1.1.1", step_value="0.1.0.0")

        # testing out decrement multivalue
        eth_dec = (
            topo[0].DeviceGroup.add(Name="Decrement", Multiplier="10").Ethernet.add()
        )
        eth_dec.Mac.Decrement(
            start_value="22:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        eth_dec.Mtu.Single("1670")
        ipv4_dec = eth_dec.Ipv4.add(Name="Ipv4 East")
        ipv4_dec.Address.Decrement(start_value="10.10.1.1", step_value="0.1.0.0")

        # testing out valueList multivalue
        eth_vl = (
            topo[0].DeviceGroup.add(Name="ValueList", Multiplier="4").Ethernet.add()
        )
        eth_list = [
            "00:11:22:33:44:55",
            "00:00:22:33:44:55",
            "00:77:22:33:44:55",
            "00:aa:22:33:44:55",
        ]
        eth_vl.Mac.ValueList(eth_list)
        eth_vl.Mtu.Single("1670")
        ipv4_vl = eth_vl.Ipv4.add(Name="Ipv4 East")
        ip_list = ["1.1.1.1", "1.1.1.11", "1.1.11.1", "1.11.1.1"]
        ipv4_vl.Address.ValueList(ip_list)

        # testing out overlay multivalue
        eth_ov = topo[0].DeviceGroup.add(Name="Overlay", Multiplier="10").Ethernet.add()
        eth_ov.Mac.Increment(
            start_value="22:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        eth_ov.Mac.Overlay(4, "22:11:00:00:00:55")
        eth_ov.Mac.Overlay(7, "00:11:00:00:00:55")
        eth_ov.Mtu.Single("1670")
        ipv4_ov = eth_ov.Ipv4.add(Name="Ipv4 East")
        ipv4_ov.Address.Increment(start_value="10.10.1.1", step_value="0.1.0.0")
        ipv4_ov.Address.Overlay(5, "4.4.4.4")
        ipv4_ov.Address.Overlay(7, "10.10.10.10")
        ipv4_ov.Address.Overlay(3, "99.33.66.77")
        ipv4_ov.Address.Overlay(9, "1.45.67.89")

        # testing out overlay multivalue with count
        eth_ovc = (
            topo[0].DeviceGroup.add(Name="OverlayCount", Multiplier="10").Ethernet.add()
        )
        eth_ovc.Mac.Increment(
            start_value="22:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        eth_ovc.Mac.Overlay(2, "22:11:00:00:00:55", count=3)
        eth_ovc.Mac.Overlay(8, "00:11:00:00:00:55", count=2)
        eth_ovc.Mtu.Single("1670")
        ipv4_ovc = eth_ovc.Ipv4.add(Name="Ipv4 East")
        ipv4_ovc.Address.Increment(start_value="10.10.1.1", step_value="0.1.0.0")
        ipv4_ovc.Address.Overlay(1, "4.4.4.4", count=2)
        ipv4_ovc.Address.Overlay(6, "10.10.10.10", count=4)

        # testing alternate and string multivalue
        eth_alt = (
            topo[0]
            .DeviceGroup.add(Name="String/Alternate", Multiplier="10")
            .Ethernet.add()
        )
        eth_alt.Mac.Increment(
            start_value="00:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        eth_alt.Mtu.Single("1670")
        ipv4_alt = eth_alt.Ipv4.add(Name="Ipv4 East")
        ipv4_alt.Address.Increment(start_value="1.1.1.1", step_value="0.1.0.0")
        ipv4_alt.ResolveGateway.Alternate(False)
        ospf = ipv4_alt.Ospfv2.add()
        ospf.AuthenticationPassword.String('{"ixia", "Keysight"}')

        # testing out random multivalue
        eth_rand = (
            topo[1].DeviceGroup.add(Name="Random", Multiplier="10").Ethernet.add()
        )
        eth_rand.Mac.Random()
        eth_rand.Mtu.Single("1670")
        ipv4_rand = eth_rand.Ipv4.add(Name="Ipv4 East")
        ipv4_rand.Address.Random()

        # testing out custom multivalue
        eth_cust = (
            topo[1].DeviceGroup.add(Name="Custom", Multiplier="10").Ethernet.add()
        )
        eth_cust.Mac.Random()
        eth_cust.Mtu.Single("1670")
        ipv4_cust = eth_cust.Ipv4.add(Name="Ipv4 East")
        increment = [
            (
                "1.1.1.1",
                10,
                [("1.1.3.1", 3, []), ("1.3.3.1", 2, []), ("1.2.3.1", 1, [])],
            ),
            ("1.1.2.1", 5, [("1.1.4.1", 4, [("1.1.5.1", 4, [])])]),
        ]
        ipv4_cust.Address.Custom(
            start_value="0.0.1.1", step_value="1.0.1.0", increments=increment
        )

        # testing out distributed multivalue
        eth_dist = (
            topo[1].DeviceGroup.add(Name="Distributed", Multiplier="10").Ethernet.add()
        )
        eth_dist.Mac.Random()
        eth_dist.Mtu.Single("1670")
        ipv4_dist = eth_dist.Ipv4.add(Name="Ipv4 East")
        ipv4_dist.Address.Distributed(
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
        eth_rr = (
            topo[1].DeviceGroup.add(Name="RandomRange", Multiplier="10").Ethernet.add()
        )
        eth_rr.Mac.RandomRange(
            "00:01:02:00:00:00", "ff:ff:ff:ff:ff:ff", "00:00:00:00:00:01", 6
        )
        eth_rr.Mtu.Single("1670")
        ipv4_rr = eth_rr.Ipv4.add(Name="Ipv4 East")
        ipv4_rr.Address.RandomRange("1.2.3.4", "255.255.255.255", "0.1.3.0", 5)

        # testing out RandomMask multivalue
        eth_rm = (
            topo[1].DeviceGroup.add(Name="RandomMask", Multiplier="10").Ethernet.add()
        )
        eth_rm.Mac.RandomMask("00:01:02:00:00:00", "00:00:ff:ff:ff:ff", 5, 55)
        eth_rm.Mtu.Single("1670")
        ipv4_rm = eth_rm.Ipv4.add(Name="Ipv4 East")
        ipv4_rm.Address.RandomMask("1.2.3.4", "0.255.255.255", 5, 55)

    # asserting the remaining multivalues
    mac_list = [
        "00:11:22:33:44:55",
        "00:00:22:33:44:55",
        "00:77:22:33:44:55",
        "00:aa:22:33:44:55",
    ]
    inc = eth_inc.refresh()
    assert inc.Mtu.Pattern == "1670"
    assert inc.Mac.Pattern == "Inc: 00:11:22:33:44:55, 00:11:01:00:00:01"
    assert ipv4_inc.refresh().Address.Pattern == "Inc: 1.1.1.1, 0.1.0.0"

    dec = eth_dec.refresh()
    assert dec.Mtu.Pattern == "1670"
    assert dec.Mac.Pattern == "Dec: 22:11:22:33:44:55, 00:11:01:00:00:01"
    assert ipv4_dec.refresh().Address.Pattern == "Dec: 10.10.1.1, 0.1.0.0"

    vl = eth_vl.refresh()
    assert vl.Mtu.Pattern == "1670"
    assert vl.Mac.Pattern == "List: " + ", ".join(mac_list)
    assert (
        ipv4_vl.refresh().Address.Pattern
        == "List: 1.1.1.1, 1.1.1.11, 1.1.11.1, 1.11.1.1"
    )

    alt = eth_alt.refresh()
    assert alt.Mtu.Pattern == "1670"
    assert alt.Mac.Pattern == "Inc: 00:11:22:33:44:55, 00:11:01:00:00:01"
    assert ipv4_alt.refresh().Address.Pattern == "Inc: 1.1.1.1, 0.1.0.0"

    rand = eth_rand.refresh()
    assert rand.Mtu.Pattern == "1670"
    assert rand.Mac.Pattern == "Rand"
    assert ipv4_rand.refresh().Address.Pattern == "Rand"

    cust = eth_cust.refresh()
    assert cust.Mtu.Pattern == "1670"
    assert cust.Mac.Pattern == "Rand"
    assert (
        ipv4_cust.refresh().Address.Pattern
        == "Custom: 0.0.1.1, 1.0.1.0, [(1.1.1.1, 10, [(1.1.3.1, 3, []),(1.3.3.1, 2, []),(1.2.3.1, 1, [])]),(1.1.2.1, 5, [(1.1.4.1, 4, [(1.1.5.1, 4, [])])])]"
    )

    dist = eth_dist.refresh()
    assert dist.Mtu.Pattern == "1670"
    assert dist.Mac.Pattern == "Rand"
    assert (
        ipv4_dist.refresh().Address.Pattern
        == "Dist: percentage, perTopology, [(1.0.0.0, 16.0),(0.0.0.1, 17.0),(0.0.1.0, 17.0),(0.1.0.0, 16.0),(2.0.0.0, 17.0),(0.0.0.2, 17.0)]"
    )

    rr = eth_rr.refresh()
    assert rr.Mtu.Pattern == "1670"
    assert (
        rr.Mac.Pattern
        == "Randr: 00:01:02:00:00:00, ff:ff:ff:ff:ff:ff, 00:00:00:00:00:01, 6"
    )
    assert ipv4_rr.refresh().Address.Pattern.startswith("Randr: 1.2.3.4")

    rm = eth_rm.refresh()
    assert rm.Mtu.Pattern == "1670"
    assert rm.Mac.Pattern == "Randb: 00:01:02:00:00:00, 00:00:ff:ff:ff:ff, 5, 55"
    assert ipv4_rm.refresh().Address.Pattern.startswith("Randb: 1.2.3.4")

    # asserting overlay multivalues
    mac = eth_ov.refresh().Mac
    assert mac.Pattern == "Inc: 22:11:22:33:44:55, 00:11:01:00:00:01"
    values = mac.Values
    assert values[3] == "22:11:00:00:00:55"
    assert values[6] == "00:11:00:00:00:55"
    values = ipv4_ov.refresh().Address.Values
    assert values[4] == "4.4.4.4"
    assert values[6] == "10.10.10.10"
    assert values[2] == "99.33.66.77"
    assert values[8] == "1.45.67.89"

    # asserting overlay multivalues with count
    mac = eth_ovc.refresh().Mac
    assert mac.Pattern == "Inc: 22:11:22:33:44:55, 00:11:01:00:00:01"
    values = mac.Values
    assert values[0] == "22:11:22:33:44:55"
    assert values[1:4] == ["22:11:00:00:00:55"] * 3
    assert values[4] != "22:11:00:00:00:55"
    assert values[7:9] == ["00:11:00:00:00:55"] * 2
    ip = ipv4_ovc.refresh().Address
    assert ip.Pattern == "Inc: 10.10.1.1, 0.1.0.0"
    values = ip.Values
    assert values[0:2] == ["4.4.4.4"] * 2
    assert values[2] != "4.4.4.4"
    assert values[5:9] == ["10.10.10.10"] * 4


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


def test_batch_add_with_overlay_count_multivalue_pattern(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add()
        topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0])
        eth = topo[0].DeviceGroup.add(Name="Single", Multiplier="10").Ethernet.add()
        eth.Mac.Increment(
            start_value="22:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        eth.Mac.Overlay(2, "22:11:00:00:00:55", count=3)
        eth.Mac.Overlay(8, "00:11:00:00:00:55", count=2)
        # overlay as the first multivalue operation, without a preceding pattern
        ipv4 = eth.Ipv4.add()
        ipv4.Address.Overlay(5, "4.4.4.4", count=4)

    assert eth.refresh().Mac.Pattern == "Inc: 22:11:22:33:44:55, 00:11:01:00:00:01"
    values = eth.Mac.Values
    assert values[1:4] == ["22:11:00:00:00:55"] * 3
    assert values[7:9] == ["00:11:00:00:00:55"] * 2
    assert values[0] == "22:11:22:33:44:55"
    assert values[4] != "22:11:00:00:00:55"
    assert ipv4.refresh().Address.Values[4:8] == ["4.4.4.4"] * 4


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
        == "Custom: 0.0.1.1, 1.0.1.0, [(1.1.1.1, 10, [(1.1.3.1, 3, []),(1.3.3.1, 2, []),(1.2.3.1, 1, [])]),(1.1.2.1, 5, [(1.1.4.1, 4, [(1.1.5.1, 4, [])])])]"
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
