"""Demonstrates how to use the underlying requests connection
to access an API that is not exposed in the python package 

Background
----------
every object has an internal _connection
the _connection has a .update .read .create .delete
those methods are raw requests access to the server so you need to 
use API browser property names in the payload

"""
from ixnetwork_restpy import SessionAssistant, Files


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

preferences = session_assistant.Ixnetwork.Globals.Preferences
url = '%s/debug/mw' % preferences.href
payload = {
    'debugLog': True,
    'traceLevel': 'all'
}
preferences._connection._update(url, payload)
