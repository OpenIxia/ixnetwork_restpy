"""
load_config_with_batch_update.py:

    - Connect to the API server
    - Load a saved configuration
    - Find all the traffic items in the configuration
    - Update few attributes of all the traffic items & their config elements using BatchUpdate
        
Supports IxNetwork API servers:
   - Windows, Windows Connection Mgr and Linux
   
Requirements:
   - Minimum IxNetwork 9.20
   - Python 2.7 and 3+
   - pip install requests
   - pip install ixnetwork_restpy (minimum version 1.1.5)
   
RestPy Doc:
    https://openixia.github.io/ixnetwork_restpy/#/overview

Usage:
   - Enter: python <script>
   
"""

from ixnetwork_restpy import SessionAssistant, BatchUpdate, Files


# create a test tool session
session_assistant = SessionAssistant(
    IpAddress="127.0.0.1",
    UserName="admin",
    Password="admin",
    LogLevel=SessionAssistant.LOGLEVEL_INFO,
    ClearConfig=True,
)
ixnetwork = session_assistant.Ixnetwork

# loading a config to our ixnetwork server
ixnetwork.LoadConfig(Files(r"load.ixncfg"))

# finding all the traffic items in our config
traffic_items = ixnetwork.Traffic.TrafficItem.find()

# we are using batch update to update some traffic parameters and parameters of its sub child
with BatchUpdate(ixnetwork):
    for idx, traffic_item in enumerate(traffic_items):
        traffic_item.Name = "my_traffic_" + str(idx)
        configElement = traffic_item.ConfigElement.find()
        configElement.FrameRate.Type = "percentLineRate"
        configElement.FrameRate.Rate = 50
        configElement.TransmissionControl.Type = "fixedFrameCount"
        configElement.TransmissionControl.FrameCount = 100000
        configElement.FrameRateDistribution.PortDistribution = "splitRateEvenly"
        configElement.FrameSize.FixedSize = 1280
        traffic_item.Tracking.find().TrackBy = ["trafficGroupId0"]
