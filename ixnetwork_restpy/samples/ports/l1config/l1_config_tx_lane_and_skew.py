"""
l1_config_aresone_800g_tx_lane_and_skew_checking.py:

    - Connect to the API server
    - In this test, do the following:
        - Add two real ports of AresOne 800G
        - Add two vports
        - Assign two the ports in to vports
        - Find the AresOneEightHundredGigLanQddC from the l1Config
        - Update TxLane and Skew attributes of AresOneEightHundredGigLanQddC
        - Verify the value of the attributes
     
Supports IxNetwork API servers:
   - Windows, Windows Connection Mgr and Linux
   
Requirements:
   - Minimum IxNetwork 9.30 Update 1
   - Python 2.7 and 3+
   - pip install requests
   - pip install ixnetwork_restpy (minimum version 1.1.9)
   
RestPy Doc:
    https://openixia.github.io/ixnetwork_restpy/#/overview

Usage:
   - Enter: python <script>
   
"""

from ixnetwork_restpy import SessionAssistant

session_assistant = SessionAssistant(
    IpAddress="<chassis-ip>",
    RestPort="<rest-port>",
    UserName="admin",
    Password="admin",
    LogLevel=SessionAssistant.LOGLEVEL_INFO,
    ClearConfig=True,
)

ixnetwork = session_assistant.Ixnetwork

# mapping the ports. Here we have used AresOne-800G for reference
port_map = session_assistant.PortMapAssistant()
port_map.Map(Location="<chassis-ip>;<card>;<port>", Name="Port 1")
port_map.Map(Location="<chassis-ip>;<card>;<port>", Name="Port 2")

# using the map connect test port locations and vports
port_map.Connect(ForceOwnership=True, HostReadyTimeout=20, LinkUpTimeout=60)
vport1 = ixnetwork.Vport.find(Name="Port 1")
vport2 = ixnetwork.Vport.find(Name="Port 2")

# Tx Lane and skew
v1_txLane = vport1.L1Config.AresOneEightHundredGigLanQddC.TxLane
print(v1_txLane)
v1_txLane.update(IsSkewSynchronized="true")
