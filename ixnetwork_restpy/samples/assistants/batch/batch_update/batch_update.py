"""
batch_update.py:

    - Connect to the API server
    - Add 10 vports
    - Update few attributes of all the vports using BatchUpdate
    - Add a topology
    - Add 5 device groups to this topology
    - Find the device groups
    - Update any multivalue attribute of the device groups using BatchUpdate
        
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

from ixnetwork_restpy import SessionAssistant, BatchUpdate


# create a test tool session
session_assistant = SessionAssistant(
    IpAddress="127.0.0.1",
    UserName="admin",
    Password="admin",
    LogLevel=SessionAssistant.LOGLEVEL_INFO,
    ClearConfig=True,
)
ixnetwork = session_assistant.Ixnetwork

vports = ixnetwork.Vport

# adding few vports
for i in range(0, 10):
    vports.add()

# updating properties of vports using batch update.
# batch update basically batches all the update operations and updates those in one go, thereby giving us a little better
# performance that the normal update function
with BatchUpdate(ixnetwork):
    for vport in vports:
        vport.Name = vport.href
        vport.TxMode = "sequential"
        vport.RxMode = "captureAndMeasure"
        vport.TraceEnabled = False
        vport.Type = "novusHundredGigLan"


# adding topology and a few device groups
topology = ixnetwork.Topology.add()
for _ in range(0, 5):
    topology.DeviceGroup.add()

# batch update also supports multivalue updates
# below example we are updating enable multiValue property in device groups
device_groups = topology.DeviceGroup.find()
with BatchUpdate(ixnetwork):
    for device_group in device_groups:
        device_group.Enabled.Single(False)
