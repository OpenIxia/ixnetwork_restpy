"""Demonstrates creating a traffic item that uses ipv4 endpoints.

"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# create 2 ipv4 endpoints
ipv4_1 = ixnetwork.Topology.add(Vports=ixnetwork.Vport.add()).DeviceGroup.add().Ethernet.add().Ipv4.add(Name='Ipv4 West')
ipv4_2 = ixnetwork.Topology.add(Vports=ixnetwork.Vport.add()).DeviceGroup.add().Ethernet.add().Ipv4.add(Name='Ipv4 East')

# create an ipv4 traffic item
traffic_item = ixnetwork.Traffic.TrafficItem.add(Name='Ipv4 Traffic Item Sample', TrafficType='ipv4', TrafficItemType='l2L3')

# create an endpoint set using the ipv4 objects
endpoint_set = traffic_item.EndpointSet.add(Sources=ipv4_1, Destinations=ipv4_2)
assert (len(endpoint_set.Sources) == 1)
assert (len(endpoint_set.Destinations) == 1)
assert (len(traffic_item.ConfigElement.find().Stack.find(StackTypeId='ipv4')) == 1)
