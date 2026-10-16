"""
The test explains how we can configure tap settings for different ports
"""

from ixnetwork_restpy import SessionAssistant, BatchUpdate


# create a test tool session
session_assistant = SessionAssistant(
    IpAddress="127.0.0.1",
    RestPort=11009,
    LogLevel=SessionAssistant.LOGLEVEL_ALL,
    ClearConfig=True,
)
ixnetwork = session_assistant.Ixnetwork
print(ixnetwork)

# Adding ports for which we want to update port setting
port_map = session_assistant.PortMapAssistant()
port_map.Map(Location="10.39.49.57;2;3", Name="Port 1")
port_map.Map(Location="10.39.49.57;2;4", Name="Port 2")
port_map.Map(Location="10.39.51.127;9;1", Name="Port 3")
port_map.Map(Location="10.39.51.127;9;2", Name="Port 4")

port_map.Connect(ForceOwnership=True, HostReadyTimeout=20, IgnoreLinkUp=True)

# fetch tap settings for all the ports
ixnetwork.GetTapSettings()

# get tap setting for each vport
vport = ixnetwork.Vport.find()
tapSet = vport.TapSettings.find()
# using batch update to update tap settings value
with BatchUpdate(ixnetwork):
    for ts in tapSet:
        params = ts.Parameter.find()
        man = None
        model = None
        paramToSet = None
        for param in params:
            if param.Name == "Manufacturer":
                man = param.CurrentValue
            elif param.Name == "Model":
                model = param.CurrentValue
            elif param.Name == "TxPreTapControl":
                paramToSet = param
        # Please update the conditions and parameters according to test criteria
        if (
            man == "FINISAR CORP."
            and model == "FTLX8571D3BCL"
            and paramToSet is not None
        ):
            paramToSet.CurrentValue = 7

# setting tap settings across all ports of different chassis
ixnetwork.SetTapSettings()
