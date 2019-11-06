"""A simple script that demonstrates how to get started with ixnetwork_restpy scripting.

The script does the following:
    - Establishes a connection with an IxNetwork test platform
    - Authenticates
    - Adds (creates) a test session
    - Gets the root IxNetwork node 
    - Clears any configuration information
    - Adds a virtual port
    - Adds 10 ipv4 emulated devices
"""

from ixnetwork_restpy.testplatform.testplatform import TestPlatform


# connect to a test tool platform
test_platform = TestPlatform('127.0.0.1')
test_platform.Authenticate('admin', 'admin')
sessions = test_platform.Sessions.add()
ixnetwork = sessions.Ixnetwork

ixnetwork.NewConfig()

# add virtual port
vport = ixnetwork.Vport.add(Name='Virtual Test Port 1')

# add ipv4 devices
ipv4_devices = ixnetwork.Topology.add(Ports=vport) \
    .DeviceGroup.add(Multiplier=10) \
    .Ethernet.add() \
    .Ipv4.add()
