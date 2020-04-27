"""Demonstrates creating ospfv2 devices 

"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

dg = ixnetwork \
    .Topology.add(Vports=ixnetwork.Vport.add()) \
    .DeviceGroup.add(Name='Dg West')
ospf1 = dg.Ethernet.add() \
    .Ipv4.add(Name='Ipv4 West') \
    .Ospfv2.add()
dg.NetworkGroup.add(Multiplier=20) \
    .Ipv4PrefixPools.add()

ospf2 = ixnetwork \
    .Topology.add(Vports=ixnetwork.Vport.add()) \
    .DeviceGroup.add(Name='Dg East') \
    .Ethernet.add() \
    .Ipv4.add(Name='Ipv4 East') \
    .Ospfv2.add()