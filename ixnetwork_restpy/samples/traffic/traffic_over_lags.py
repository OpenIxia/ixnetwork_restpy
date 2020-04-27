"""Demonstrates how to create traffic over a lag

NOTE: due to current limitations either a Lagportlacp or Lagportstaticlag must be added

"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

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

# add lags to topologies
ethernet1 = ixnetwork.Topology.add(Ports=lag_1).DeviceGroup.add().Ethernet.add()    
ethernet2 = ixnetwork.Topology.add(Ports=lag_2).DeviceGroup.add().Ethernet.add()    

# create a raw traffic item
traffic_item = ixnetwork.Traffic.TrafficItem.add(Name='Lag Traffic Item Sample', TrafficType='raw')

# add the lag objects as endpoints to the traffic item
endpoint_set = traffic_item.EndpointSet.add(Destinations=lag_2, Sources=lag_1)
assert (len(endpoint_set.Sources) == 1)
assert (len(endpoint_set.Destinations) == 1)