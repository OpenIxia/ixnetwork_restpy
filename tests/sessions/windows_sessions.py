""" Demonstrates standalone IxNetwork Windows GUI session management
"""

from ixnetwork_restpy.testplatform.testplatform import TestPlatform


# setup the connection information to a standalone windows gui test platform
# the session will always be defaulted to session id 1
# the session state is always active
test_platform=TestPlatform('127.0.0.1', rest_port=11009, platform='windows')
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

# get a valid session
sessions = test_platform.Sessions.find(Id=1)
assert(len(sessions) == 1)