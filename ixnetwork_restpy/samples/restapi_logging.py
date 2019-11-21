"""The following demonstrates the logging features of this package

The different trace options are meant to expose the details of the request and response messages. 
The default output is to sys.stdout
To output to a log file, use the log_file_name param
The trace level can be specified in the TestPlatform constructor and subsequently modified using the TestPlatform.Trace property.
The default log level is TestPlatform.TRACE_NONE which has a logging level of CRITICAL
"""
from ixnetwork_restpy.testplatform.testplatform import TestPlatform

# by default nothing should be logged
# anything that is logged will be logged to the console and to a log file
test_platform = TestPlatform('127.0.0.1', log_file_name='test.log')
test_platform.Authenticate('admin', 'admin')
sessions = test_platform.Sessions.add()

# warn level messages logged
test_platform.Trace = TestPlatform.TRACE_WARNING
test_platform.warn('warn message')

# info level messages logged
test_platform.Trace = TestPlatform.TRACE_INFO
test_platform.info('info message')

# debug level messages showing only request
test_platform.Trace = TestPlatform.TRACE_REQUEST
sessions.Ixnetwork.Vport.add()

# debug level messages showing request and response truncated
test_platform.Trace = TestPlatform.TRACE_REQUEST_RESPONSE
sessions.Ixnetwork.Vport.add()

# debug level messages showing entire request and response
test_platform.Trace = TestPlatform.TRACE_ALL
sessions.Ixnetwork.Vport.add()

# turn logging off
test_platform.Trace = TestPlatform.TRACE_NONE
test_platform.warn('warn message')
test_platform.info('info message')
sessions.Ixnetwork.Vport.add()

