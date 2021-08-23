"""
createTrafficItemAddPacketHeader.py
Description
   Configure custom packet headers in raw Traffic Item.

   - Create a Raw Traffic Items.
   - Example to show how to add packet header: Ethernet, PFC queue, PFC pause 802.1QBB, VLAN, IPv4 + DSCP, UDP, TCP and ICMP
   - Enable tracking to track the packet headers in Flow Statistics
Requirements
   - Minimum IxNetwork 8.50
   - Python 2.7 and 3+
   - pip install requests
   - pip install ixnetwork_restpy (minimum version 1.0.51)
RestPy Doc:
    https://www.openixia.github.io/ixnetwork_restpy/#/
Usage:
   - Enter: python <script>
"""

import os, sys, traceback
from pprint import pprint

# Import the RestPy module
from ixnetwork_restpy import SessionAssistant

# For linux and windowsConnectionMgr only. Set to True to leave the session alive for debugging.
debugMode = False

forceTakePortOwnership = True

try:
    # LogLevel: none, info, warning, request, request_response, all
    session = SessionAssistant(IpAddress='127.0.0.1', UserName='admin', Password='admin',
                                         LogLevel=SessionAssistant.LOGLEVEL_INFO, ClearConfig=True)

    conf_assist = session.ConfigAssistant()
    config = conf_assist.config

    config.info('configuring vports')
    vports = config.Vport.add().add()

    config.info('Create a raw traffic item')
    rawTrafficItemObj = config.Traffic.TrafficItem.add(Name='Raw packet', BiDirectional=False, TrafficType='raw')

    config.info('Add source and destination endpoints')
    rawTrafficItemObj.EndpointSet.add(Sources=vports[0].Protocols, Destinations=vports[1].Protocols)

    config.info('configuring rate and transmission control')
    configElement = rawTrafficItemObj.ConfigElement
    configElement.FrameRate.Type = 'percentLineRate'
    configElement.FrameRate.Rate = 50
    configElement.TransmissionControl.Type = 'fixedFrameCount'
    configElement.TransmissionControl.FrameCount = 10000
    configElement.FrameSize.FixedSize = 128

    config.info('adding ethernet stack')
    ethernetStackObj = configElement.Stack.Ethernet.add()

    config.info('Configuring Ethernet packet header')
    ethernetStackObj.DestinationAddress.Increment(start_value="00:0c:29:68:05:1E", step_value="00:00:00:00:00:00")
    ethernetStackObj.SourceAddress.Increment(start_value="00:0c:29:68:05:14", step_value="00:00:00:00:00:00")

    config.info('adding Vlan packet header')
    vlanFieldObj = configElement.Stack.Vlan.add()

    config.info('Configuring Vlan packet header')
    vlanFieldObj.VlanTagVlanID.Single(103)
    vlanFieldObj.VlanTagVlanUserPriority.Single(3)

    config.info('modifying pfc queue of ethernet stack')
    ethernetStackObj.PfcQueue.ValueList([1, 3, 5, 7])

    config.info('adding Pfc Pause packet header')
    pauseFrameObj = configElement.Stack.PfcPause.add()

    config.info('Configuring pfc pause packet header')
    pauseFrameObj.MacControlControlOpcode.Single(103)
    pauseFrameObj.PauseQuantaPfcQueue0.Single('abcd')

    config.info('adding ipv4 packet header')
    ipv4FieldObj = configElement.Stack.Ipv4.add()

    config.info('Configuring ipv4 packet header')
    ipv4FieldObj.SrcIp.Increment(start_value='1.1.1.1', step_value='0.0.0.1')
    ipv4FieldObj.DstIp.ValueList(['1.1.1.2', '1.1.1.3', '1.1.1.4', '1.1.1.5'])
    ipv4FieldObj.TosPrecedence.Single(3)
    ipv4FieldObj.DefaultPHBDefaultPHB.Single(56)

    config.info('adding udp packet header')
    udpFieldObj = configElement.Stack.Udp.add()

    config.info('Configuring udp packet header')
    udpFieldObj.SrcPort.Single(1000)
    udpFieldObj.DstPort.Single(1001)

    config.info('adding tcp packet header')
    tcpFieldObj = configElement.Stack.Tcp.add()

    config.info('Configuring tcp packet header')
    tcpFieldObj.SrcPort.ValueList(['1002', '1005', '1007'])
    tcpFieldObj.DstPort.Single(1003)

    # Optional: Enable tracking to track your packet headers:
    #
    #    Other trackings: udpUdpSrcPrt0, udpUdpDstPrt0,tcpTcpSrcPrt0, tcpTcpDstPrt0, vlanVlanId0, vlanVlanUserPriority0
    #    On an IxNetwork GUI (Windows or Web UI), add traffic item trackings.
    #    Then go on the API browser to view the tracking fields.
    tracking = rawTrafficItemObj.Tracking.add(TrackBy=['udpUdpSrcPrt0', 'udpUdpDstPrt0'])

    config.info('committing changes')
    errs = conf_assist.commit()
    if len(errs) > 0:
        raise Exception('json import has errors %s' % str(errs))

    chassis_ip = '10.39.51.187'
    test_ports = [
        dict(Arg1=chassis_ip, Arg2=1, Arg3=5),
        dict(Arg1=chassis_ip, Arg2=1, Arg3=6)
    ]

    config.info('Assigning Ports')
    config.AssignPorts(test_ports, [], vports, True)

    config.info('generating traffic')
    rawTrafficItemObj.Generate()

    config.info('Apply config')
    config.Traffic.Apply()

    config.info('Starting traffic')
    config.Traffic.StartStatelessTrafficBlocking()

    if not debugMode:
        # For Linux and WindowsConnectionMgr only
        if session.TestPlatform.Platform != 'windows':
            session.Session.remove()

    config.info('Test Case Passed !!!!!!!')

except Exception as errMsg:
    print(errMsg)
    config.debug('\n%s' % traceback.format_exc())
    if not debugMode and 'session' in locals():
        if session.TestPlatform.Platform != 'windows':
            session.Session.remove()
