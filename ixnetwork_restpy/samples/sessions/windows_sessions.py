""" Demonstrates standalone IxNetwork Windows GUI session management
"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
test_platform = session_assistant.TestPlatform

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