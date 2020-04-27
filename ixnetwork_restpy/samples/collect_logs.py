"""Demonstrates collecting diagnostic logs 

"""
from ixnetwork_restpy import SessionAssistant, Files


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

ixnetwork.CollectLogs(Arg1=Files('diagnostic_logs'), Arg2='currentInstance')
session_assistant.Session.DownloadFile('diagnostic_logs.zip')
