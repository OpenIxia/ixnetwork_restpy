"""The following demonstrates the logging features of this package

The different trace options are meant to expose the details of the request and response messages. 
The default output is to sys.stdout
To output to a log file, use the log_file_name param
The trace level can be specified in the SessionAssistant constructor and subsequently modified using the TestPlatform.Trace property.
The default log level is SessionAssistant.LOGLEVEL_NONE which has a logging level of CRITICAL
"""
from ixnetwork_restpy import SessionAssistant, TestPlatform


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin', 
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
test_platform = session_assistant.TestPlatform
ixnetwork = session_assistant.Ixnetwork

# warn level messages logged
test_platform.Trace = TestPlatform.TRACE_WARNING
test_platform.warn('warn message')

# info level messages logged
test_platform.Trace = TestPlatform.TRACE_INFO
test_platform.info('info message')

# debug level messages showing only request
test_platform.Trace = TestPlatform.TRACE_REQUEST
ixnetwork.Vport.add()

# debug level messages showing request and response truncated
test_platform.Trace = TestPlatform.TRACE_REQUEST_RESPONSE
ixnetwork.Vport.add()

# debug level messages showing entire request and response
test_platform.Trace = TestPlatform.TRACE_ALL
ixnetwork.Vport.add()

# turn logging off
test_platform.Trace = TestPlatform.TRACE_NONE
test_platform.warn('warn message')
test_platform.info('info message')
ixnetwork.Vport.add()

