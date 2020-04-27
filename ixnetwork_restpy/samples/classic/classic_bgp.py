"""Demonstrates adding a bgp neighbor range to a virtual port.

"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# add a virtual port and get the interface object
vport = ixnetwork.Vport.add(Name='Test Port 1')

# add an interface
interface = vport.Interface.add(Enabled=True)
ipv4 = interface.Ipv4.add(Ip='1.1.1.1', Gateway='1.1.2.1')

# enable bgp
bgp = vport.Protocols.find().Bgp
bgp.Enabled = True

# add a bgp neighbor range
neighbor_range = bgp.NeighborRange.add(Interfaces=interface, Enabled=True, EnableBgpId=True)

# verify the neighbor range has been added on the server
assert(len(neighbor_range.find()) == 1)
