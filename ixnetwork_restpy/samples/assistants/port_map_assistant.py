"""Demonstrates how to use the PortMapAssistant class

"""
from ixnetwork_restpy.testplatform.testplatform import TestPlatform
from ixnetwork_restpy.assistants.ports.portmapassistant import PortMapAssistant


test_platform = TestPlatform('127.0.0.1')
test_platform.Authenticate('admin', 'admin')
session = test_platform.Sessions.add()

# create a port map assistant instance
port_map = PortMapAssistant(session.Ixnetwork)

# add mappings between test port locations and vport names
# if the vport name does not exist or is not supplied a vport will be created
# the vport will be returned as part of the call 
for portId in range(1, 3):
	vport = port_map.Map(IpAddress='10.36.17.24;', CardId=1, PortId=portId, Name='Port %s' % x)
	print(vport.Name)
print(port_map)

port_map.Connect(ForceOwnership=True)
print(port_map)

port_map.Disconnect()
print(port_map)
