"""Demonstrates creating a raw traffic item over vport endpoints.

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

# raw traffic endpoints must be Vport.Protocols objects
# create an endpoint set using the Vport.Protocols objects
endpoint_set = traffic_item.EndpointSet.add(Sources=vport_1.Protocols.find(), Destinations=vport_2.Protocols.find())
assert (len(endpoint_set.Sources) == 1)
assert (len(endpoint_set.Destinations) == 1)
