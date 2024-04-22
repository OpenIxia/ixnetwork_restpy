# testing traffic nodes with batch add
from ixnetwork_restpy.assistants.batch.batchadd import BatchAdd
import pytest


def test_batch_add_with_traffic(ixnetwork):
    with BatchAdd(ixnetwork):
        virtual_ports = ixnetwork.Vport.add().add()
        virtual_ports[0].Name = "myVport_1"
        virtual_ports[0].RxMode = "captureAndMeasure"
        virtual_ports[1].Name = "myVport_2"
        tr = ixnetwork.Traffic.TrafficItem.add(
            Name="RAW TCP",
            AllowSelfDestined=True,
            TrafficType="raw",
            TrafficItemType="l2L3",
        )
        tr.BiDirectional = True
        tr.SrcDestMesh = "oneToOne"
        end = tr.EndpointSet.add(
            Sources=virtual_ports[0].Protocols.add(),
            Destinations=virtual_ports[1].Protocols.add(),
            ScalableSources=[],
            ScalableDestinations=[],
        )
    assert tr.href == "/api/v1/sessions/1/ixnetwork/traffic/trafficItem/1"
    assert end.Sources[0] == "/vport[1]/protocols"
    assert end.Destinations[0] == "/vport[2]/protocols"


def test_batch_add_with_traditional_traffic(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add().add()
        vport[0].Name = "myVport_1"
        vport[0].RxMode = "captureAndMeasure"
        vport[1].Name = "myVport_2"
        traffic = ixnetwork.Traffic.TrafficItem
        tr1 = traffic.add(
            Name="RAW TCP",
            BiDirectional=False,
            TrafficType="raw",
            TrafficItemType="l2L3",
        )
        tr1.EndpointSet.add(
            Sources=vport[0].Protocols.add(), Destinations=vport[1].Protocols.add()
        )

    traffic_config = tr1.ConfigElement.find()
    eth_st = traffic_config.Stack.find(DisplayName="Ethernet II")
    dhcpProtocolTemplate = ixnetwork.Traffic.ProtocolTemplate.find(
        StackTypeId=f"^dhcp$"
    )

    with BatchAdd(ixnetwork):
        src_addr = eth_st.Field.find(DisplayName="Source MAC Address")
        dst_addr = eth_st.Field.find(DisplayName="Destination MAC Address")
        src_addr.SingleValue = "00:11:00:00:22:00"
        dst_addr.SingleValue = "00:33:00:11:22:00"
        eth_st.Append(Arg2=dhcpProtocolTemplate)
        dhcp_st = traffic_config.Stack.find(DisplayName="DHCP")
        dhcp_opcode = dhcp_st.Field.find(DisplayName="Message op code")
        dhcp_server = dhcp_st.Field.find(DisplayName="Server IP address")
        dhcp_client = dhcp_st.Field.find(DisplayName="Client IP address")
        dhcp_opcode.SingleValue = 2
        dhcp_server.ValueType = "increment"
        dhcp_server.StartValue = "1.2.3.4"
        dhcp_server.StepValue = "0.2.1.0"
        dhcp_client.ValueType = "decrement"
        dhcp_client.StartValue = "12.13.14.15"
        dhcp_client.StepValue = "0.0.0.1"

    stacks = ixnetwork.Traffic.TrafficItem.find().ConfigElement.find().Stack.find()
    assert len(stacks) == 3
    assert stacks[0].DisplayName == "Ethernet II"
    assert stacks[1].DisplayName == "DHCP"


def test_batch_add_with_multicast_traffic(ixnetwork):
    with BatchAdd(ixnetwork):
        vports = ixnetwork.Vport.add().add()
        ipv4_1 = (
            ixnetwork.Topology.add(Vports=vports[0])
            .DeviceGroup.add(Name="dg1")
            .Ethernet.add(Name="eth1")
            .Ipv4.add(Name="ip1")
        )
        igmp_host = ipv4_1.IgmpHost.add(Name="igmp1")
        ipv4_2 = (
            ixnetwork.Topology.add(Vports=vports[1])
            .DeviceGroup.add(Name="dg2")
            .Ethernet.add(Name="eth2")
            .Ipv4.add(Name="ip2")
        )
        ipv4_2.IgmpQuerier.add(Name="igmpq1")
        traffic = ixnetwork.Traffic.TrafficItem
        scalable_sources = [
            {"arg1": ipv4_2, "arg2": "1", "arg3": "1", "arg4": "1", "arg5": "2"},
            {"arg1": ipv4_2, "arg2": "1", "arg3": "1", "arg4": "3", "arg5": "2"},
        ]
        multicast_receivers = [
            {
                "arg1": igmp_host.IgmpMcastIPv4GroupList,
                "arg2": "0",
                "arg3": "3",
                "arg4": "0",
            },
            {
                "arg1": igmp_host.IgmpMcastIPv4GroupList,
                "arg2": "0",
                "arg3": "4",
                "arg4": "0",
            },
            {
                "arg1": igmp_host.IgmpMcastIPv4GroupList,
                "arg2": "0",
                "arg3": "6",
                "arg4": "0",
            },
            {
                "arg1": igmp_host.IgmpMcastIPv4GroupList,
                "arg2": "0",
                "arg3": "9",
                "arg4": "0",
            },
        ]
        tr3 = traffic.add(Name="Multicast", TrafficType="ipv4", TrafficItemType="l2L3")
        endpoint_set = tr3.EndpointSet.add(
            ScalableSources=scalable_sources, MulticastReceivers=multicast_receivers
        )
        configElement = tr3.ConfigElement.add()
        configElement.FrameRate.Type = "percentLineRate"
        configElement.FrameRate.Rate = 50
        configElement.TransmissionControl.Type = "fixedFrameCount"
        configElement.TransmissionControl.FrameCount = 100000
        configElement.FrameRateDistribution.PortDistribution = "splitRateEvenly"
        configElement.FrameSize.FixedSize = 1280
        tr3.Tracking.add(TrackBy=["trafficGroupId0"])

    assert (
        endpoint_set.href
        == "/api/v1/sessions/1/ixnetwork/traffic/trafficItem/1/endpointSet/1"
    )
    end_point = ixnetwork.Traffic.TrafficItem.find().EndpointSet.find()
    assert end_point.ScalableSources[0]["arg1"] == ipv4_2.href
    assert end_point.ScalableSources[1]["arg1"] == ipv4_2.href
    assert (
        end_point.MulticastReceivers[0]["arg1"]
        == "/api/v1/sessions/1/ixnetwork/topology/1/deviceGroup/1/ethernet/1/ipv4/1/igmpHost/1/igmpMcastIPv4GroupList"
    )
    assert (
        end_point.MulticastReceivers[2]["arg1"]
        == "/api/v1/sessions/1/ixnetwork/topology/1/deviceGroup/1/ethernet/1/ipv4/1/igmpHost/1/igmpMcastIPv4GroupList"
    )


def test_batch_add_with_autogen_traffic_templates(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add().add()
        vport[0].Name = "myVport_1"
        vport[0].RxMode = "captureAndMeasure"
        vport[1].Name = "myVport_2"
        traffic = ixnetwork.Traffic.TrafficItem
        tr1 = traffic.add(
            Name="RAW TCP",
            BiDirectional=False,
            TrafficType="raw",
            TrafficItemType="l2L3",
        )
        tr1.EndpointSet.add(
            Sources=vport[0].Protocols.add(), Destinations=vport[1].Protocols.add()
        )
        stack = tr1.ConfigElement.add().Stack.add()
        eth_st = stack.Ethernet.add()
        eth_st.SourceAddress.Single("00:11:00:00:22:00")
        eth_st.DestinationAddress.Single("00:33:00:11:22:00")
        dhcp_st = stack.Dhcp.add()
        dhcp_st.OpCode.Single(2)
        dhcp_st.HwType.Single(5)
        dhcp_st.BroadcastFlag.Single(32768)
        dhcp_st.ServerIP.Increment("1.2.3.4", "0.2.1.0")
        dhcp_st.ClientIP.Decrement("12.13.14.15", "0.0.0.1")
        dhcp_st.ClientHwAddress.Single("0aaa")
        igmp_st = stack.Igmpv1.add()
        igmp_st.Type.Single(1)
        igmp_st.Unused.Single("0xcc")
        ip_list = ["1.2.3.4", "1.22.31.4", "1.12.3.4", "1.4.3.4"]
        igmp_st.GroupAddress.ValueList(ip_list)

    stacks = ixnetwork.Traffic.TrafficItem.find().ConfigElement.find().Stack.find()
    assert len(stacks) == 4
    assert stacks[0].DisplayName == "Ethernet II"
    assert stacks[1].DisplayName == "DHCP"
    assert stacks[2].DisplayName == "IGMPv1"


def test_batch_add_with_quick_flow_traffic(ixnetwork):
    vport1 = ixnetwork.Vport.add(Name="Port1")
    vport2 = ixnetwork.Vport.add(Name="Port2")
    with BatchAdd(ixnetwork):
        traffic_item = ixnetwork.Traffic.TrafficItem.add(
            TrafficType="raw", TrafficItemType="quick"
        )
        proto1 = vport1.Protocols.add()
        proto2 = vport2.Protocols.add()
        for i in range(2):
            traffic_item.EndpointSet.add(Sources=proto1, Destinations=proto2)
            hls = traffic_item.HighLevelStream.add()
            hls.Name = "hls" + str(i)
            hls.FrameRate.Type = "framesPerSecond"
            hls.FrameRate.Rate = 10
            hls.FrameSize.Type = "fixed"
            hls.FrameSize.FixedSize = 500
            hls.TransmissionControl.Type = "fixedFrameCount"
            hls.TransmissionControl.FrameCount = 10
            stack = hls.Stack.add()
            eth_st = stack.Ethernet.add()
            eth_st.SourceAddress.Single("00:00:29:68:05:1E")
            eth_st.DestinationAddress.Single("00:0c:29:68:05:1E")


def test_batch_add_with_traffic_having_href_objects(ixnetwork):
    vports = ixnetwork.Vport.add().add()
    ipv4_1 = (
        ixnetwork.Topology.add(Vports=vports[0])
        .DeviceGroup.add(Name="dg1")
        .Ethernet.add(Name="eth1")
        .Ipv4.add(Name="ip1")
    )
    ipv4_2 = (
        ixnetwork.Topology.add(Vports=vports[1])
        .DeviceGroup.add(Name="dg2")
        .Ethernet.add(Name="eth2")
        .Ipv4.add(Name="ip2")
    )

    with BatchAdd(ixnetwork):
        traffic = ixnetwork.Traffic.TrafficItem
        scalable_sources = [
            {"arg1": ipv4_2, "arg2": "1", "arg3": "1", "arg4": "1", "arg5": "2"},
            {"arg1": ipv4_2, "arg2": "1", "arg3": "1", "arg4": "3", "arg5": "2"},
        ]
        scalable_destinations = [
            {"arg1": ipv4_1, "arg2": "1", "arg3": "1", "arg4": "1", "arg5": "2"}
        ]
        tr3 = traffic.add(Name="Multicast", TrafficType="ipv4", TrafficItemType="l2L3")
        endpoint_set = tr3.EndpointSet.add(
            ScalableSources=scalable_sources, ScalableDestinations=scalable_destinations
        )

    assert (
        endpoint_set.href
        == "/api/v1/sessions/1/ixnetwork/traffic/trafficItem/1/endpointSet/1"
    )
    end_point = ixnetwork.Traffic.TrafficItem.find().EndpointSet.find()
    assert end_point.ScalableSources[0]["arg1"] == ipv4_2.href
    assert end_point.ScalableSources[1]["arg1"] == ipv4_2.href
    assert end_point.ScalableDestinations[0]["arg1"] == ipv4_1.href


def test_batch_add_traffic_for_non_active_fields(ixnetwork):
    with BatchAdd(ixnetwork):
        vport = ixnetwork.Vport.add().add()
        vport[0].Name = "myVport_1"
        vport[0].RxMode = "captureAndMeasure"
        vport[1].Name = "myVport_2"
        traffic = ixnetwork.Traffic.TrafficItem
        tr1 = traffic.add(
            Name="RAW TCP",
            BiDirectional=False,
            TrafficType="raw",
            TrafficItemType="l2L3",
        )
        tr1.EndpointSet.add(
            Sources=vport[0].Protocols.add(), Destinations=vport[1].Protocols.add()
        )
        stack = tr1.ConfigElement.add().Stack.add()
        eth_st = stack.Ethernet.add()
        eth_st.SourceAddress.Single("00:11:00:00:22:00")
        eth_st.DestinationAddress.Single("00:33:00:11:22:00")
        ipv4_st = stack.Ipv4.add()
        ipv4_st.SrcIp.Single("1.1.1.1")
        ipv4_st.PriorityRaw.Single("0xb5")

    stack.find()
    assert len(stack) == 3

    # check eth values
    eth_fields = stack[0].Field.find()
    for field in eth_fields:
        if field.DisplayName == "Destination MAC Address":
            assert field.Auto is False
            assert field.ValueType == "singleValue"
            assert field.SingleValue == "00:33:00:11:22:00"
        elif field.DisplayName == "Source MAC Address":
            assert field.Auto is False
            assert field.ValueType == "singleValue"
            assert field.SingleValue == "00:11:00:00:22:00"

    # check ip values
    ip_fields = stack[1].Field.find()
    for field in eth_fields:
        if field.DisplayName == "Raw priority":
            assert field.Auto is False
            assert field.OptionalEnabled is True
            assert field.ActiveChoiceField is True
            assert field.ValueType == "singleValue"
            assert field.SingleValue == "b5"
        elif field.DisplayName == "Source Address":
            assert field.Auto is False
            assert field.OptionalEnabled is True
            assert field.ActiveChoiceField is True
            assert field.ValueType == "singleValue"
            assert field.SingleValue == "1.1.1.1"


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
