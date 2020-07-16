"""Demonstrates creating ospfv2 devices 

"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant( 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

ipv41 = ixnetwork \
    .Topology.add(Vports=ixnetwork.Vport.add()) \
    .DeviceGroup.add(Name='Dg West') \
    .Ethernet.add() \
    .Ipv4.add(Name='Ipv4 West')

ipv42 = ixnetwork \
    .Topology.add(Vports=ixnetwork.Vport.add()) \
    .DeviceGroup.add(Name='Dg East') \
    .Ethernet.add() \
    .Ipv4.add(Name='Ipv4 East')

traffic = ixnetwork.Traffic.TrafficItem.add(Name='West -> East', TrafficType='ipv4')
traffic.EndpointSet.add(Sources=ipv41, Destinations=ipv42)

test_details = ixnetwork.Timeline.CreateTest(Arg2='rfc2544back2back', Arg3=None)
print(test_details)
test = ixnetwork.parent.GetObjectFromHref(test_details['arg1'])
test.TrafficItemIds = traffic

