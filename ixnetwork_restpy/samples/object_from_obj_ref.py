"""Demonstrates how to get an object given an href

The TestPlatform.Sessions class has a helper method that assists in returning an object given a valid href

"""

from ixnetwork_restpy.testplatform.testplatform import TestPlatform

test_platform = TestPlatform('127.0.0.1', rest_port=11009)
test_platform.Trace = 'request_response'

sessions = test_platform.Sessions.add()

ixnetwork = sessions.Ixnetwork
ixnetwork.NewConfig()

vport = ixnetwork.Vport.add()

# the following code is an attempt to get the object that the vport is connected to
# in this case the href that is returned from the .ConnectedTo property is null so the object returned is None
# if the vport was connected to an actual hardware port a valid /availableHardware/chassis/card/port object reference 
# would be returned from the Vport.ConnectedTo property
# this reference is then used to get an actual object
hardware_port = sessions.GetObjectFromHref(vport.ConnectedTo)
assert(hardware_port is None)