"""Demonstrates how to use the PortMapAssistant class

"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# demonstrate different ways to add mappings between test port locations and vport names
# if the vport name does not exist a new vport using that name will be created and mapped
# if the vport name is None then a new vport will be created using the system's default naming scheme and mapped
port_map = session_assistant.PortMapAssistant()
port_map.Map(Location='10.36.74.26;2;11', Name='Port 1')
port_map.Map('10.36.74.26', 2, 12, Name='Port 2')
port_map.Map(IpAddress='10.36.74.26', CardId=2, PortId=13, Name='Port 3')
port_map.Map(Port=('10.36.74.26', 2, 14), Name='Port 4')
print(port_map)

# using the map connect test port locations and vports
port_map.Connect(ForceOwnership=True, HostReadyTimeout=20, LinkUpTimeout=60)
print(port_map)

# using the map disconnect test port locations and vports
port_map.Disconnect()
print(port_map)
