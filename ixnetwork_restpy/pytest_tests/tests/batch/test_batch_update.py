from ixnetwork_restpy.assistants.batch.batchupdate import BatchUpdate


def test_batch_update_for_primitive_attributes(ixnetwork):
    """BatchUpdate of various primitive attributes.

    This is expected to update the values of many primitive attributes in batch.
    """
    vports = ixnetwork.Vport
    for i in range(0, 10):
        vports.add()
    with BatchUpdate(ixnetwork):
        for vport in vports:
            vport.Name = vport.href
            vport.TxMode = "sequential"
            vport.RxMode = "captureAndMeasure"
            vport.TraceEnabled = False
            vport.TraceLevel = "kError"
            vport.TransmitIgnoreLinkStatus = True
            vport.Type = "novusHundredGigLan"
    with BatchUpdate(ixnetwork):
        for vport in vports:
            interface = vport.L1Config.NovusHundredGigLan
            interface.EnablePPM = False
            interface.AutoInstrumentation = "floating"
            interface.EnablePPM = False
            interface.EnableRsFec = False
            interface.EnableRsFecStats = False
            interface.RsFecAdvertise = True


def test_batch_update_for_multivalue_attributes(ixnetwork):
    """BatchUpdate of all types of multivalue attributes.

    This is expected to update the values of many mutivalue attributes in one go.
    """
    vport = ixnetwork.Vport.add().add()

    # adding two topologies
    topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0]).add(
        Name="Topology 2", Vports=vport[1]
    )

    # testing out increment multivalue
    eth1 = topo[0].DeviceGroup.add(Name="Increment", Multiplier="10").Ethernet.add()
    eth1.Mtu.Single("1650")
    eth1.Mac.Increment(start_value="00:11:22:33:44:55", step_value="00:11:01:00:00:01")
    ipv41 = eth1.Ipv4.add(Name="Ipv4 East")
    ipv41.Address.Increment(start_value="1.1.1.1", step_value="0.0.1.0")

    # testing out decrement multivalue
    eth2 = topo[0].DeviceGroup.add(Name="Decrement", Multiplier="10").Ethernet.add()
    eth2.Mtu.Single("1670")
    eth2.Mac.Decrement(start_value="22:22:22:33:44:55", step_value="00:11:01:00:00:01")
    ipv42 = eth2.Ipv4.add(Name="Ipv4 East")
    ipv42.Address.Decrement(start_value="10.10.1.1", step_value="0.1.0.0")

    # testing out valueList multivalue
    eth3 = topo[0].DeviceGroup.add(Name="ValueList", Multiplier="4").Ethernet.add()
    eth3.Mtu.Single("1670")
    ipv43 = eth3.Ipv4.add(Name="Ipv4 East")
    ip_list = ["1.1.1.1", "1.1.1.11", "1.1.11.1", "1.11.1.1"]
    ipv43.Address.ValueList(ip_list)

    with BatchUpdate(ixnetwork):
        # updating Single
        eth1.Mtu.Single("1670")
        # updating Increment
        ipv41.Address.Increment(start_value="1.1.1.1", step_value="0.1.0.0")
        # updating Decrement
        eth2.Mac.Decrement(
            start_value="22:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        # updating ValueList
        eth_list = [
            "00:11:22:33:44:55",
            "00:00:22:33:44:55",
            "00:77:22:33:44:55",
            "00:aa:22:33:44:55",
        ]
        eth3.Mac.ValueList(eth_list)
    topos = ixnetwork.Topology.find()

    dg1 = topos[0].DeviceGroup.find()
    assert len(dg1) == 3
    eth11 = dg1[0].Ethernet.find()
    mac_list = eth11.Mac.Pattern.split()
    assert (
        mac_list[0] == "Inc:"
        and mac_list[1] == "00:11:22:33:44:55,"
        and mac_list[2] == "00:11:01:00:00:01"
    )
    addr_list = eth11.Ipv4.find().Address.Pattern.split()
    assert (
        addr_list[0] == "Inc:"
        and addr_list[1] == "1.1.1.1,"
        and addr_list[2] == "0.1.0.0"
    )

    eth12 = dg1[1].Ethernet.find()
    mac_list = eth12.Mac.Pattern.split()
    assert (
        mac_list[0] == "Dec:"
        and mac_list[1] == "22:11:22:33:44:55,"
        and mac_list[2] == "00:11:01:00:00:01"
    )
    addr_list = eth12.Ipv4.find().Address.Pattern.split()
    assert (
        addr_list[0] == "Dec:"
        and addr_list[1] == "10.10.1.1,"
        and addr_list[2] == "0.1.0.0"
    )

    eth13 = dg1[2].Ethernet.find()
    mac_list = eth13.Mac.Pattern.split()
    assert (
        mac_list[0] == "List:"
        and mac_list[1] == "00:11:22:33:44:55,"
        and mac_list[2] == "00:00:22:33:44:55,"
        and mac_list[3] == "00:77:22:33:44:55,"
        and mac_list[4] == "00:aa:22:33:44:55"
    )
    addr_list = eth13.Ipv4.find().Address.Pattern.split()
    assert (
        addr_list[0] == "List:"
        and addr_list[1] == "1.1.1.1,"
        and addr_list[2] == "1.1.1.11,"
        and addr_list[3] == "1.1.11.1,"
        and addr_list[4] == "1.11.1.1"
    )


def test_batch_update_mix_of_multivalue_and_primitive_attributes(ixnetwork):
    """BatchUpdate of all types of multivalue and primitive attributes.

    This is expected to update the values of many mutivalue & primitive attributes in one go.
    """
    vport = ixnetwork.Vport.add().add()

    # adding two topologies
    topo = ixnetwork.Topology.add(Name="Topology 1", Vports=vport[0]).add(
        Name="Topology 2", Vports=vport[1]
    )

    # testing out increment multivalue
    eth1 = topo[0].DeviceGroup.add(Name="Increment1", Multiplier="10").Ethernet.add()
    eth1.Mtu.Single("1650")
    eth1.Mac.Increment(start_value="00:11:22:33:44:55", step_value="00:11:01:00:00:01")
    ipv41 = eth1.Ipv4.add(Name="Ipv4 East")
    ipv41.Address.Increment(start_value="1.1.1.1", step_value="0.0.1.0")

    # testing out decrement multivalue
    eth2 = topo[0].DeviceGroup.add(Name="Decrement", Multiplier="10").Ethernet.add()
    eth2.Mtu.Single("1670")
    eth2.Mac.Decrement(start_value="22:22:22:33:44:55", step_value="00:11:01:00:00:01")
    ipv42 = eth2.Ipv4.add(Name="Ipv4 East")
    ipv42.Address.Decrement(start_value="10.10.1.1", step_value="0.1.0.0")

    with BatchUpdate(ixnetwork):
        eth1.Mtu.Single("1670")
        eth1.Name = "Inc"
        ipv41.Name = "Inc_Ipv4"
        ipv41.Address.Increment(start_value="1.1.1.1", step_value="0.1.0.0")
        eth2.Mac.Decrement(
            start_value="22:11:22:33:44:55", step_value="00:11:01:00:00:01"
        )
        topo[0].DeviceGroup.find()[-1].Multiplier = 2
    topos = ixnetwork.Topology.find()

    dg1 = topos[0].DeviceGroup.find()
    assert len(dg1) == 2
    eth11 = dg1[0].Ethernet.find()
    assert dg1[-1].Multiplier == 2
    assert eth11.Name == "Inc"
    mac_list = eth11.Mac.Pattern.split()
    assert (
        mac_list[0] == "Inc:"
        and mac_list[1] == "00:11:22:33:44:55,"
        and mac_list[2] == "00:11:01:00:00:01"
    )
    ipv411 = eth11.Ipv4.find()
    assert ipv411.Name == "Inc_Ipv4"
    addr_list = ipv411.Address.Pattern.split()
    assert (
        addr_list[0] == "Inc:"
        and addr_list[1] == "1.1.1.1,"
        and addr_list[2] == "0.1.0.0"
    )

    eth12 = dg1[1].Ethernet.find()
    mac_list = eth12.Mac.Pattern.split()
    assert (
        mac_list[0] == "Dec:"
        and mac_list[1] == "22:11:22:33:44:55,"
        and mac_list[2] == "00:11:01:00:00:01"
    )
    addr_list = eth12.Ipv4.find().Address.Pattern.split()
    assert (
        addr_list[0] == "Dec:"
        and addr_list[1] == "10.10.1.1,"
        and addr_list[2] == "0.1.0.0"
    )


def test_batch_update_with_nodes_of_multiplicity_one(ixnetwork):
    vport = ixnetwork.Vport.add().add()
    traffic = ixnetwork.Traffic.TrafficItem
    for i in range(10):
        tr1 = traffic.add(
            Name="RAW TCP " + str(i),
            BiDirectional=False,
            TrafficType="raw",
            TrafficItemType="l2L3",
        )
        tr1.EndpointSet.add(
            Sources=vport[0].Protocols.find(), Destinations=vport[1].Protocols.find()
        )
    ixia_mac_space = "11 22 33 44 55 66"
    with BatchUpdate(ixnetwork):
        for item in ixnetwork.Traffic.TrafficItem.find():
            config_element = item.ConfigElement.find()
            config_element.FramePayload.update(
                Type="custom",
                CustomRepeat=False,
                CustomPattern=f'{"11 " * 40}ff ee 22 11 {ixia_mac_space}',
            )
            config_element.FrameRate.update(Type="framesPerSecond", Rate=99)
            config_element.FrameRateDistribution.update(
                StreamDistribution="applyRateToAll"
            )
            config_element.FrameSize.update(Type="fixed", FixedSize="900")
            config_element.TransmissionControl.update(
                Type="fixedFrameCount", FrameCount=99
            )  # was 2
            config_element.TransmissionDistribution.find().update(
                Distributions=["ipv4SourceIp0", "ipv4DestIp0", "vlanVlanId0"]
            )

    for item in ixnetwork.Traffic.TrafficItem.find():
        ce = item.ConfigElement.find()
        assert ce.FramePayload.Type == "custom"
        assert (
            config_element.FrameRateDistribution.StreamDistribution == "applyRateToAll"
        )


if __name__ == "__main__":
    import pytest

    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
