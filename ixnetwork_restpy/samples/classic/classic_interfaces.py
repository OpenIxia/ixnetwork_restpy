"""Demonstrates adding interfaces to virtual ports.

"""

from ixnetwork_restpy.testplatform.testplatform import TestPlatform

# connect to a test tool platform
test_platform = TestPlatform('127.0.0.1')
test_platform.Authenticate('admin', 'admin')
sessions = test_platform.Sessions.add()
ixnetwork = sessions.ixnetwork
ixnetwork.NewConfig()

# add a virtual port and get the interface object
interfaces = ixnetwork.Vport.add(Name='Test Port 1').Interface

# add 10 interfaces
for i in range(1, 11):
	interfaces.add(Description='Interface Demo %s' % i, Enabled=True)

# verify they have been added on the server
assert(len(interfaces.find()) == 10)
