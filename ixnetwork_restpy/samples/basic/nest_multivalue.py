"""
nest_Multivalue.py:

   - Connect to the API server
   - Configure one Topology
   - Configure Device Group for topology
   - Configure Network Group connected to Device Group
   - From Network Group fetch all the nest for ipv4 prefix pools in multivalue network address
   - Set different values for Nest multivalues

RestPy Doc:
    https://www.openixia.github.io/ixnetwork_restpy/#/

Usage:
   - Enter: python <script>
"""

from ixnetwork_restpy import SessionAssistant

session = SessionAssistant(
    IpAddress="127.0.0.1",
    RestPort=11009,
    LogLevel=SessionAssistant.LOGLEVEL_INFO,
    ClearConfig=True,
)

ixNetwork = session.Ixnetwork

ixNetwork.info("Creating vport")
vport = ixNetwork.Vport.add()

ixNetwork.info("Creating Topology")
topology1 = ixNetwork.Topology.add(Name="Topo1", Ports=vport)
deviceGroup1 = topology1.DeviceGroup.add(Name="DG1", Multiplier="1")
ethernet1 = deviceGroup1.Ethernet.add(Name="Eth1")
ethernet1.Mac.Increment(start_value="00:01:01:01:00:01", step_value="00:00:00:00:00:01")

ixNetwork.info("Configuring IPv4 on Topology")
ipv4 = ethernet1.Ipv4.add(Name="Ipv4")
ipv4.Address.Increment(start_value="1.1.1.1", step_value="0.0.0.1")
ipv4.GatewayIp.Increment(start_value="1.1.1.4", step_value="0.0.0.0")

ixNetwork.info("Configuring Network group behind Topology")
networkGroup1 = deviceGroup1.NetworkGroup.add(Name="NG1", Multiplier="4")
ipv4PrefixPool = networkGroup1.Ipv4PrefixPools.add(NumberOfAddresses="1")
ipv4PrefixPool.NetworkAddress.Increment(start_value="20.10.0.1", step_value="0.0.0.1")

# Fetching all the Nest for multivalue network address
steps = ipv4PrefixPool.NetworkAddress.Steps
ixNetwork.info(steps)

# Setting values for different Nest multivalue
steps[1].Enabled = "True"
steps[1].Step = "0.0.0.4"

steps[0].Enabled = "True"
steps[0].Step = "1.0.0.4"
