""" Demonstrates IxNetwork Linux API Server session management
"""

from ixnetwork_restpy.testplatform.testplatform import TestPlatform


# setup the connection information for a windows gui test platform that has a default session of 1
# platform='linux' forces the scheme to https
# if the default platform='windows' is used a ConnectionError will be raised
# as the Linux API Server does not redirect but closes the connection
test_platform=TestPlatform('10.36.82.185')
assert(test_platform.Platform == 'linux')
test_platform.Trace = 'request_response'

# authenticate with username and password
test_platform.Authenticate('admin', 'admin')
api_key = test_platform.ApiKey

# if username/password is not acceptable to the client due to the unencrypted password
# an api key can be specified instead
# the api key can be retrieved from the linux api server user settings and provided 
# to the TestPlatform.ApiKey property which will be used in subsequent server requests
test_platform.ApiKey = api_key

# get a list of sessions
for session in test_platform.Sessions.find():
    print(session)

# add a session
sessions = test_platform.Sessions.add(ApplicationType='ixnrest')
session_id = sessions.Id
print(sessions)

# change the name of a session
session_name = 'new session name'
sessions.Name = session_name
assert(sessions.Name == session_name)
print(sessions)

# find by session name
sessions = test_platform.Sessions.find(Name=session_name)
assert(len(sessions) == 1)

# remove the session
sessions.remove()
assert (len(sessions) == 0)

# attempt to get the removed session
sessions = test_platform.Sessions.find(session_id)
assert(len(sessions) == 0)
