"""Demonstrates adding ipv4 devices
"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin', 
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)

ipv4 = session_assistant.Ixnetwork \
	.Topology.add() \
	.DeviceGroup.add() \
	.Ethernet.add() \
	.Ipv4.add()
print(ipv4)
