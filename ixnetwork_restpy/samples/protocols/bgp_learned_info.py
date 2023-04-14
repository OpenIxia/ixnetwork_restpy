"""
This sample actually demonstrates how call and see the learned information of a protocol.
The sample will be almost identical for rest of the protocols as well
In this test its assumed that bgp session is configured properly and is up and running
This test fetches the bgpv4 peer interface and calls the operation to get all learned info
After that it showcases from where we can get the learned info information for bgp.

Supports IxNetwork API servers:
   - Windows, Windows Connection Mgr and Linux

Requirements:
   - Minimum IxNetwork 8.50
   - Python 2.7 and 3+

RestPy Doc:
    https://openixia.github.io/ixnetwork_restpy/#/overview

"""

from ixnetwork_restpy import SessionAssistant

# connecting to an existing ixn session , note the clear config is false.
session_assistant = SessionAssistant(
    IpAddress="localhost",
    RestPort=11009,
    UserName="admin",
    Password="admin",
    LogLevel=SessionAssistant.LOGLEVEL_ALL,
    ClearConfig=False,
)

ixn = session_assistant.Ixnetwork

# finding the bgpv4 peer according to our need
bgp = (
    ixn.Topology.find()
    .DeviceGroup.find()
    .Ethernet.find()
    .Ipv4.find()
    .BgpIpv4Peer.find()
)

# calling the get all learned info operation
# note here we have showcased a simple call that fetches learned info of all bgp sessions
# if a particular session is required we can pass a list of session indices
# eg: bgp.GetAllLearnedInfo([1,5,9])
bgp.GetAllLearnedInfo()

# showcases from where we can retrieve the fetched learned info
learned_info_table = bgp.LearnedInfo.find().Table.find()
print(learned_info_table)
