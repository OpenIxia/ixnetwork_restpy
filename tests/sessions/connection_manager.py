""" Demonstrates IxNetwork Connection Manager session management
"""

from ixnetwork_restpy.testplatform.testplatform import TestPlatform


# setup the connection information for a connection manager test platform 
test_platform=TestPlatform('10.113.9.116', rest_port=443, platform='connection_manager')
test_platform.Trace = 'request_response'

# get a list of sessions
for session in test_platform.Sessions.find():
    print(session)

# add a session and remove the session
sessions = test_platform.Sessions.add()
assert(len(sessions) == 1)
print(sessions)
sessions.remove()

# get an invalid session
sessions = test_platform.Sessions.find(Id=6)
assert(len(sessions) == 0)

# get a valid session, start it and remove it when finished
# use the state to determine if it can be stopped
sessions = test_platform.Sessions.find(Id=8022)
assert(len(sessions) == 1)
if sessions.State == 'STOPPED':
    sessions.Start()
    sessions.remove()
