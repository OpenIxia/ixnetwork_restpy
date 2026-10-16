"""
traffic_with_batch_add.py:

    - Connect to the API server
    - In a BatchAdd call, do the following:
        - Add two vports
        - Update some attributes of the vports
        - Add a raw traffic item
        - Add endpoint set, config element and stack to it
        - Add Ethernet, DHCP, Ipv4 & Igmpv1 protocols to the stack
        - Update various attributes of each of these
        
Supports IxNetwork API servers:
   - Windows, Windows Connection Mgr and Linux
   
Requirements:
   - Minimum IxNetwork 9.10
   - Python 2.7 and 3+
   - pip install requests
   - pip install ixnetwork_restpy (minimum version 1.1.5)
   
RestPy Doc:
    https://openixia.github.io/ixnetwork_restpy/#/overview

Usage:
   - Enter: python <script>
   
"""

from ixnetwork_restpy import SessionAssistant, BatchAdd


# create a test tool session
session_assistant = SessionAssistant(
    IpAddress="127.0.0.1",
    UserName="admin",
    Password="admin",
    LogLevel=SessionAssistant.LOGLEVEL_INFO,
    ClearConfig=True,
)
ixnetwork = session_assistant.Ixnetwork

# we will be configuring traffic using batch add
# please note that its a bit different and easier from our regular traffic configuration
with BatchAdd(ixnetwork):
    vport = ixnetwork.Vport.add().add()
    vport[0].Name = "myVport_1"
    vport[0].RxMode = "captureAndMeasure"
    vport[1].Name = "myVport_2"
    traffic = ixnetwork.Traffic.TrafficItem
    tr1 = traffic.add(
        Name="RAW TCP", BiDirectional=False, TrafficType="raw", TrafficItemType="l2L3"
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
    ipv4_st = stack.Ipv4.add()
    ipv4_st.TosDelay.Single(1)
    ipv4_st.TosPrecedence.Single(3)
    ipv4_st.Checksum.Increment(2, 4)
    igmp_st = stack.Igmpv1.add()
    igmp_st.Type.Single(1)
    igmp_st.Unused.Single("0xcc")
    ip_list = ["1.2.3.4", "1.22.31.4", "1.12.3.4", "1.4.3.4"]
    igmp_st.GroupAddress.ValueList(ip_list)
