"""Demonstrates how to use the PortMapAssistant class

"""
from ixnetwork_restpy.testplatform.testplatform import TestPlatform
from ixnetwork_restpy.assistants.ports.portmapassistant import PortMapAssistant


test_platform = TestPlatform('127.0.0.1')
test_platform.Authenticate('admin', 'admin')
session = test_platform.Sessions.add()
ixnetwork = session.Ixnetwork
ixnetwork.NewConfig()

# create a port map assistant instance
port_map = PortMapAssistant(ixnetwork)

# demonstrate different ways to add mappings between test port locations and vport names
# if the vport name does not exist or is not supplied a new vport will be created using the system's default naming scheme 
port_map.Map('10.35.74.26', 2, 12)
port_map.Map('10.35.74.26', 2, 11, Name='Port 11')
port_map.Map(IpAddress='10.36.74.26', CardId=2, PortId=13, Name='Port 1')
port_map.Map(Port=('10.36.74.26', 2, 14))
port_map.Map(Port=('10.36.74.26', 2, 15), Name='A New Port Name')
print(port_map)

# using the map establish a hardware connection between test port locations and vports
port_map.Connect(ForceOwnership=True)
print(port_map)

# using the map disconnect the hardware connection between test port locations and vports
port_map.Disconnect()
print(port_map)
