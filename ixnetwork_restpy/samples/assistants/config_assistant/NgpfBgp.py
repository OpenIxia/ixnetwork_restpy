"""
bgpNgpf.py:
   Tested with two back-2-back Ixia ports...
   - Connect to the API server
   - Configure license server IP
   - Configure two Topology Groups: IPv4/BGP
   - Configure Network Group for each topology for route advertising
   - Configure a Traffic Item
   - Commit changes
   - Assign ports
   - Start all protocols
   - Verify all protocols
   - Start traffic
   - Get Traffic Item
   - Get Flow Statistics stats
Supports IxNetwork API servers:
   - Windows, Windows Connection Mgr and Linux
Requirements:
   - Minimum IxNetwork 8.50
   - Python 2.7 and 3+
   - pip install requests
   - pip install ixnetwork_restpy (minimum version 1.0.51)
RestPy Doc:
    https://www.openixia.github.io/ixnetwork_restpy
Usage:
   - Enter: python <script>
"""

import sys, os, time, traceback, json
from time import time
# Import the RestPy module
from ixnetwork_restpy import SessionAssistant

# For linux and connection_manager only. Set to True to leave the session alive for debugging.
debugMode = False

try:
    # LogLevel: none, info, warning, request, request_response, all
    session_assistant = SessionAssistant(IpAddress='127.0.0.1', UserName='admin', Password='admin',
                                         LogLevel=SessionAssistant.LOGLEVEL_INFO, ClearConfig=True)

    start = time()
    conf_assist = session_assistant.ConfigAssistant()
    config = conf_assist.config

    config.info('creating vport 1')
    vport1 = config.Vport.add()[-1]

    config.info('Creating Topology Group 1')
    topology1 = config.Topology.add(Name='Topo1', Ports=vport1)[-1]

    config.info('Creating Device Group 1')
    deviceGroup1 = topology1.DeviceGroup.add(Name='DG1', Multiplier='1')

    config.info('Creating Ethernet stack 1')
    ethernet1 = deviceGroup1.Ethernet.add(Name='Eth1')
    ethernet1.Mac.Increment(start_value='00:01:01:01:00:01', step_value='00:00:00:00:00:01')

    config.info('Enabling Vlan on Topology 1')
    ethernet1.EnableVlans.Single(True)

    config.info('Configuring vlanID')
    vlanObj1 = ethernet1.Vlan.add()
    vlanObj1.VlanId.Increment(start_value=103, step_value=0)

    config.info('Configuring IPv4')
    ipv4 = ethernet1.Ipv4.add(Name='Ipv4')
    ipv4.Address.Increment(start_value='1.1.1.1', step_value='0.0.0.1')
    ipv4.GatewayIp.Increment(start_value='1.1.1.2', step_value='0.0.0.0')

    config.info('Configuring BgpIpv4Peer 1')
    bgp1 = ipv4.BgpIpv4Peer.add(Name='Bgp1')
    bgp1.DutIp.Increment(start_value='1.1.1.2', step_value='0.0.0.0')
    bgp1.Type.Single('internal')
    bgp1.LocalAs2Bytes.Increment(start_value=101, step_value=0)

    config.info('Configuring Network Group 1')
    networkGroup1 = deviceGroup1.NetworkGroup.add(Name='BGP-Routes1', Multiplier='100')
    ipv4PrefixPool = networkGroup1.Ipv4PrefixPools.add(NumberOfAddresses='1')
    ipv4PrefixPool.NetworkAddress.Increment(start_value='10.10.0.1', step_value='0.0.0.1')
    ipv4PrefixPool.PrefixLength.Single(32)

    config.info('creating vport 2')
    vport2 = config.Vport.add()[-1]

    config.info('Creating Topology Group 2')
    topology2 = config.Topology.add(Name='Topo2', Ports=vport2)[-1]

    config.info('Creating Device Group 2')
    deviceGroup2 = topology2.DeviceGroup.add(Name='DG2', Multiplier='1')

    config.info('Creating Ethernet 2')
    ethernet2 = deviceGroup2.Ethernet.add(Name='Eth2')
    ethernet2.Mac.Increment(start_value='00:01:01:02:00:01', step_value='00:00:00:00:00:01')

    config.info('Enabling Vlan on Topology 2')
    ethernet2.EnableVlans.Single(True)

    config.info('Configuring vlanID')
    vlanObj2 = ethernet2.Vlan.add()
    vlanObj2.VlanId.Increment(start_value=103, step_value=0)

    config.info('Configuring IPv4 2')
    ipv4 = ethernet2.Ipv4.add(Name='Ipv4-2')
    ipv4.Address.Increment(start_value='1.1.1.2', step_value='0.0.0.1')
    ipv4.GatewayIp.Increment(start_value='1.1.1.1', step_value='0.0.0.0')

    config.info('Configuring BgpIpv4Peer 2')
    bgp2 = ipv4.BgpIpv4Peer.add(Name='Bgp2')
    bgp2.DutIp.Increment(start_value='1.1.1.1', step_value='0.0.0.0')
    bgp2.Type.Single('internal')
    bgp2.LocalAs2Bytes.Increment(start_value=101, step_value=0)

    config.info('Configuring Network Group 2')
    networkGroup2 = deviceGroup2.NetworkGroup.add(Name='BGP-Routes2', Multiplier='100')
    ipv4PrefixPool = networkGroup2.Ipv4PrefixPools.add(NumberOfAddresses='1')
    ipv4PrefixPool.NetworkAddress.Increment(start_value='20.20.0.1', step_value='0.0.0.1')
    ipv4PrefixPool.PrefixLength.Single(32)

    config.info('Create Traffic Item')
    trafficItem = config.Traffic.TrafficItem.add(Name='BGP Traffic', BiDirectional=False, TrafficType='ipv4')

    config.info('Add source/dest endpoints')
    trafficItem.EndpointSet.add(Sources=topology1, Destinations=topology2)

    config.info('Configuring config elements')
    configElement = trafficItem.ConfigElement
    configElement.FrameRate.Type = 'percentLineRate'
    configElement.FrameRate.Rate = 50
    configElement.TransmissionControl.Type = 'fixedFrameCount'
    configElement.TransmissionControl.FrameCount = 10000
    configElement.FrameRateDistribution.PortDistribution = 'splitRateEvenly'
    configElement.FrameSize.FixedSize = 128
    tracking = trafficItem.Tracking.add(TrackBy=['flowGroup0'])

    # generally its always advisable to configure everything first and then commit and do operation when using
    # config assistant so that the script execution is fast as well as creating the configuration at once as you can
    # see in this script everything configured then committing then all operation like start protocols and traffic

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
    config.AssignPorts(test_ports, [], config.Vport, True)

    config.info('Starting NGPF protocols')
    config.StartAllProtocols(Arg1='sync')

    config.info('Verify protocol sessions\n')
    protocolSummary = session_assistant.StatViewAssistant('Protocols Summary')
    protocolSummary.CheckCondition('Sessions Not Started', protocolSummary.EQUAL, 0)
    protocolSummary.CheckCondition('Sessions Down', protocolSummary.EQUAL, 0)

    config.info('generating traffic')
    trafficItem.Generate()
    config.info('Apply config')
    config.Traffic.Apply()

    config.info('Starting traffic')
    config.Traffic.StartStatelessTrafficBlocking()

    flowStatistics = session_assistant.StatViewAssistant('Flow Statistics')

    config.info('{}\n'.format(flowStatistics))

    for rowNumber, flowStat in enumerate(flowStatistics.Rows):
        config.info('\n\nSTATS: {}\n\n'.format(flowStat))
        config.info('\nRow:{}  TxPort:{}  RxPort:{}  TxFrames:{}  RxFrames:{}\n'.format(
            rowNumber, flowStat['Tx Port'], flowStat['Rx Port'],
            flowStat['Tx Frames'], flowStat['Rx Frames']))

    if not debugMode:
        # For linux and connection_manager only
        session_assistant.Session.remove()

    config.info('Test Case Passed !!!!!!!')

except Exception as errMsg:
    print('\n%s' % traceback.format_exc(None, errMsg))
    if not debugMode and 'session' in locals():
        session_assistant.Session.remove()
