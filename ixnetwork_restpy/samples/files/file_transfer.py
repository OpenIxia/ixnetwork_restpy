"""Demonstrates how to upload and download files to a remote server.

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

# get a list of remote files
print(session_assistant.Session.GetFileList())

# download the remote saved configuration as some other local file
session_assistant.Session.DownloadFile('sample.ixncfg', 'local.ixncfg')

# upload the local file
print(session_assistant.Session.UploadFile('local.ixncfg'))

# load the remote local configuration
print(ixnetwork.LoadConfig(Files('local.ixncfg')))

# verify that the vport objects exist
assert(len(ixnetwork.Vport.find()) == 4)


