"""This script demonstrates how to get started with ixnetwork_restpy scripting.

The script demonstrates the following:
    - connect to an IxNetwork test platform, authenticate, add a new session and clear the config
    - create 1 tx port and 1 rx port
    - create traffic from the tx port to the rx port
    - start traffic
    - print statistics
    - stop traffic
"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# create tx and rx port resources
port_map = session_assistant.PortMapAssistant()
port_map.Map('10.36.74.26', 2, 13, Name='Tx')
port_map.Map('10.36.74.26', 2, 14, Name='Rx')

# create a TrafficItem resource
# TrafficItem acts a a high level container for ConfigElement resources
# ConfigElement is a high level container for individual HighLevelStream resources
traffic_item = ixnetwork.Traffic.TrafficItem.add(Name='Traffic Test', TrafficType='raw')
traffic_item.EndpointSet.add(
    Sources=ixnetwork.Vport.find(Name='^Tx').Protocols.find(), 
    Destinations=ixnetwork.Vport.find(Name='^Rx').Protocols.find())

# using the traffic ConfigElement resource
# update the frame rate
# update the transmission control
traffic_config = traffic_item.ConfigElement.find()
traffic_config.FrameRate.update(Type='percentLineRate', Rate='100')
traffic_config.TransmissionControl.update(Type='continuous')

# adjust Ethernet stack fields
destination_mac = traffic_config.Stack.find(StackTypeId='ethernet').Field.find(FieldTypeId='ethernet.header.destinationAddress')
destination_mac.update(ValueType='valueList', ValueList=['00:00:fa:ce:fa:ce', '00:00:de:ad:be:ef'], TrackingEnabled=True)

# push ConfigElement settings down to HighLevelStream resources
traffic_item.Generate()

# connect ports to hardware test ports
# apply traffic to hardware
# start traffic
port_map.Connect(ForceOwnership=True)
ixnetwork.Traffic.Apply()
ixnetwork.Traffic.StartStatelessTrafficBlocking()

# print statistics
print(session_assistant.StatViewAssistant('Port Statistics'))
print(session_assistant.StatViewAssistant('Traffic Item Statistics'))
print(session_assistant.StatViewAssistant('Flow Statistics'))

# stop traffic
ixnetwork.Traffic.StopStatelessTrafficBlocking()
