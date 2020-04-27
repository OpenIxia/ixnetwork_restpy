"""Demonstrates file handling.

The Files object determines how file content is uploaded.
Prior to an operation if local_file=True is specified the content will be pushed to the server 
if the content exists locally.
If the file does not exist locally an empty file using only the file name will be created on the server. 

"""
from ixnetwork_restpy import SessionAssistant, Files


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# add 4 vport objects
ixnetwork.Vport.add().add().add().add()

# save the configuration on the server
ixnetwork.SaveConfig(Files('sample.ixncfg'))

# create an empty configuration
ixnetwork.NewConfig()
assert(len(ixnetwork.Vport.find()) == 0)

# load the saved configuration
ixnetwork.LoadConfig(Files('sample.ixncfg'))

# verify that the vport objects exist
assert(len(ixnetwork.Vport.find()) == 4)


