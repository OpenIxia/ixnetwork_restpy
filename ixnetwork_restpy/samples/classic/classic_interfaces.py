"""Demonstrates adding interfaces to virtual ports.

"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# add a virtual port and get the interface object
interfaces = ixnetwork.Vport.add(Name='Test Port 1').Interface

# add 10 interfaces
for i in range(1, 11):
	interfaces.add(Description='Interface Demo %s' % i, Enabled=True)

# verify they have been added on the server
assert(len(interfaces.find()) == 10)
