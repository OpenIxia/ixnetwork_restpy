"""This sample demonstrates customizing a traffic item stack.

"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# create two vport objects
vport_1 = ixnetwork.Vport.add()
vport_2 = ixnetwork.Vport.add()

# create a raw traffic item
traffic_item = ixnetwork.Traffic.TrafficItem.add(Name='Raw Traffic Item Sample', TrafficType='raw', TrafficItemType='l2L3')
endpoint_set = traffic_item.EndpointSet.add(Sources=vport_1.Protocols.find(), Destinations=vport_2.Protocols.find())

# append protocol templates to the traffic item
config_element = traffic_item.ConfigElement.find(EndpointSetId=1)
ethernet_stack = config_element.Stack.find(StackTypeId='^ethernet$')

# get the protocol templates to be appended
vlan_protocol_template = ixnetwork.Traffic.ProtocolTemplate.find(StackTypeId='^vlan$')
ipv4_protocol_template = ixnetwork.Traffic.ProtocolTemplate.find(StackTypeId='^ipv4$')
udp_protocol_template = ixnetwork.Traffic.ProtocolTemplate.find(StackTypeId='^udp$')

# append the protocol templates and get the newly appended stack object using the returned href
vlan_stack = config_element.Stack.read(ethernet_stack.AppendProtocol(vlan_protocol_template))
ipv4_stack = config_element.Stack.read(vlan_stack.AppendProtocol(ipv4_protocol_template))
udp_stack = config_element.Stack.read(ipv4_stack.AppendProtocol(udp_protocol_template))

