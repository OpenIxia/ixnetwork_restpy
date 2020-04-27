""" Demonstrates how to create a Linux API Server QuickTest Web session

"""
from ixnetwork_restpy import SessionAssistant


# create a linux api server quicktest session
session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    ApplicationType=SessionAssistant.APP_TYPE_QUICKTEST,
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
print(session_assistant.Session)
session_assistant.Session.remove()

# create a linux api server ixnetwork session
session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    ApplicationType=SessionAssistant.APP_TYPE_IXNETWORK,
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
print(session_assistant.Session)
session_assistant.Session.remove()
