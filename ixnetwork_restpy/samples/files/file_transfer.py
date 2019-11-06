"""Demonstrates how to upload and download files to a remote server.

"""

from ixnetwork_restpy.testplatform.testplatform import TestPlatform
from ixnetwork_restpy.files import Files


# connect to a test tool platform
test_platform = TestPlatform('127.0.0.1')
test_platform.Authenticate('admin', 'admin')
sessions = test_platform.Sessions.add()
ixnetwork = sessions.Ixnetwork
ixnetwork.NewConfig()

# add 4 vport objects
ixnetwork.Vport.add().add().add().add()

# save the configuration on the server
ixnetwork.SaveConfig(Files('sample.ixncfg'))

# get a list of remote files
print(sessions.GetFileList())

# download the remote saved configuration as some other local file
sessions.DownloadFile('sample.ixncfg', 'local.ixncfg')

# upload the local file
print(sessions.UploadFile('local.ixncfg'))

# load the remote local configuration
print(ixnetwork.LoadConfig(Files('local.ixncfg')))

# verify that the vport objects exist
assert(len(ixnetwork.Vport.find()) == 4)


