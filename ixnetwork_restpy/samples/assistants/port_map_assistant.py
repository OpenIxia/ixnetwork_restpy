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
