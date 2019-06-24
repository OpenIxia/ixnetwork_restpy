"""Demonstrates how to create traffic over a lag

NOTE: due to current limitations either a Lagportlacp or Lagportstaticlag must be added

"""

from ixnetwork_restpy.testplatform.testplatform import TestPlatform

test_platform = TestPlatform('127.0.0.1', rest_port=11009)
test_platform.Trace = 'request_response'

sessions = test_platform.Sessions.add()

ixnetwork = sessions.Ixnetwork
ixnetwork.NewConfig()

# add a source lag with multiple vports
vports_1 = ixnetwork.Vport.add().add()
lag_1 = ixnetwork.Lag.add(Name='Lag 1', Vports=vports_1)
lag_1.ProtocolStack.add().Ethernet.add().Lagportlacp.add()
assert(len(lag_1.Vports) == 2)

# add a destination lag with multiple vports
vports_2 = ixnetwork.Vport.add().add()
lag_2 = ixnetwork.Lag.add(Name='Lag 2', Vports=vports_2)
lag_2.ProtocolStack.add().Ethernet.add().Lagportlacp.add()
assert(len(lag_2.Vports) == 2)

# create a raw traffic item
traffic_item = ixnetwork.Traffic.TrafficItem.add(Name='Lag Traffic Item Sample', TrafficType='raw')

# add the lag objects as endpoints to the traffic item
endpoint_set = traffic_item.EndpointSet.add(Destinations=lag_2, Sources=lag_1)
assert (len(endpoint_set.Sources) == 1)
assert (len(endpoint_set.Destinations) == 1)