"""
batch_add.py:

    - Connect to the API server
    - In a BatchAdd call, do the following:
        - Add two vports
        - Add two topologies using these vports
        - Add two device groups in the first topology
        - Add Ethernet protocol to both the device groups
        - Add Ipv4 to the first device group, and Ipv6 to the second
        - Add two device groups in the second topology
        - Add Ethernet & Ipv4 protocols to both the device groups
        - Add BgpIpv4Peer to the first device group, and Ospfv2 to the second
    - In another BatchAdd call, do the following:
        - Add two more vports
        - Add two more topologies using these newly added vports
        - Add a device group in the last topology
        
Supports IxNetwork API servers:
   - Windows, Windows Connection Mgr and Linux
   
Requirements:
   - Minimum IxNetwork 9.10
   - Python 2.7 and 3+
   - pip install requests
   - pip install ixnetwork_restpy (minimum version 1.1.5)
   
RestPy Doc:
    https://openixia.github.io/ixnetwork_restpy/#/overview

Usage:
   - Enter: python <script>
   
"""

from ixnetwork_restpy import SessionAssistant, BatchAdd


# create a test tool session
session_assistant = SessionAssistant(
    IpAddress="127.0.0.1",
    UserName="admin",
    Password="admin",
    LogLevel=SessionAssistant.LOGLEVEL_INFO,
    ClearConfig=True,
)
ixnetwork = session_assistant.Ixnetwork

# Generally, BatchAdd is used to configure a bunch of resources in a single rest call
with BatchAdd(ixnetwork):
    vp = ixnetwork.Vport.add(Name="vp1").add(Name="vp2")
    ixnetwork.Topology.add(Vports=vp[0]).add(Vports=vp[1])
    dg = ixnetwork.Topology[0].DeviceGroup.add().add()
    dg[0].Ethernet.add().Ipv4.add()
    dg[1].Ethernet.add().Ipv6.add()
    dg = ixnetwork.Topology[1].DeviceGroup.add().add()
    dg[0].Ethernet.add().Ipv4.add().BgpIpv4Peer.add(Name="Bgp1")
    dg[1].Ethernet.add().Ipv4.add().Ospfv2.add(Name="ospf-100.1.0.2")


# Note: BatchAdd  can be used multiple times in the same script
with BatchAdd(ixnetwork):
    vp.add(Name="vp3").add(Name="vp4")
    topo = ixnetwork.Topology.add(Vports=vp[2]).add(Vports=vp[3])
    topo[-1].DeviceGroup.add(Name="my_dg")
