"""A simple script that demonstrates how to get started with ixnetwork_restpy scripting.

"""

from ixnetwork_restpy.testplatform.testplatform import TestPlatform


# connect to a test tool platform
test_platform = TestPlatform('127.0.0.1')
test_platform.Authenticate('admin', 'admin')
sessions = test_platform.Sessions.add()
ixnetwork = sessions.ixnetwork
ixnetwork.NewConfig()

# add a virtual port
vport = ixnetwork.Vport.add(Name='Abstract Test Port 1')

# add 10 ipv4 devices
ipv4_devices = ixnetwork.Topology.add(Ports=vport).DeviceGroup.add(Multiplier=10).Ethernet.add().Ipv4.add()
