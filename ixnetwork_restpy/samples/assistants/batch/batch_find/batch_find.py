"""
batch_find.py:

    - Connect to the API server
    - Add 5 vports
    - Add 5 interfaces for each vport with enabled Vlan for some
    - Use BatchFind call to find all the vports, interfaces and vlans with enabled vlan
    - Update few attributes using the result found by BatchFind
    - Update attributes for the parent of any node found
    - Add two topologies
    - Add 5 device groups in each topology
    - Use BatchFind call to find the device groups of second topology only
    - Update attributes for the result found by the BatchFind
        
Supports IxNetwork API servers:
   - Windows, Windows Connection Mgr and Linux
   
Requirements:
   - Minimum IxNetwork 9.00
   - Python 2.7 and 3+
   - pip install requests
   - pip install ixnetwork_restpy (minimum version 1.1.5)
   
RestPy Doc:
    https://openixia.github.io/ixnetwork_restpy/#/overview

Usage:
   - Enter: python <script>
   
"""

from ixnetwork_restpy import SessionAssistant, BatchFind


# create a test tool session
session_assistant = SessionAssistant(
    IpAddress="127.0.0.1",
    UserName="admin",
    Password="admin",
    LogLevel=SessionAssistant.LOGLEVEL_INFO,
    ClearConfig=True,
)
ixnetwork = session_assistant.Ixnetwork

# adding certain vports and interfaces underneath them
for _ in range(0, 5):
    vport = ixnetwork.Vport.add()
    for vlan_id in range(0, 5):
        vport.Interface.add(Enabled=True).Vlan.VlanEnable = vlan_id % 2 == 0

# when you have a huge config with a lot of nodes, batch find will actually help to find nodes ver quickly,
# hence giving better performance result than normal find
# using batch find to find the respective restPy nodes
with BatchFind(ixnetwork) as bf:
    ixnetwork.Vport.find().Interface.find().Vlan.find(VlanEnable=True)

# the batch find object bf has a results object which has a list of restPy nodes with their names
# here we are changing the some attributes of the found nodes.
bf.results.vport[1].Name = "my_vport"
bf.results.interface[2].Description = "my_interface_description"
bf.results.vlan[3].VlanId = 100

# the restPy nodes maintains the same hierarchy when batch find is used.
# here we will be disabling the parent interface for a vlan node condition.
bf.results.vlan[6].parent.Enabled = False

topologies = ixnetwork.Topology.add().add()
for topology in topologies:
    for _ in range(0, 5):
        topology.DeviceGroup.add()

# one point to note.
# You need to pass the parent node in batchFind for which you want to find the children of.
with BatchFind(topologies[1]) as bf:
    topologies[1].DeviceGroup.find()

bf.results.deviceGroup[3].Multiplier = 100
