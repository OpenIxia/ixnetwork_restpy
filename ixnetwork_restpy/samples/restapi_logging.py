"""The following demonstrates the logging features of this package

The different trace options are meant to expose the details of the request and response messages. 
The default output is to sys.stdout
To output to a log file, use the log_file_name param

The trace level can be specified in the TestPlatform constructor and subsequently modified using the TestPlatform.Trace property.
Trace='none' is no tracing of request and response messages with a logger level of CRITICAL
Trace='request' is DEBUG logging of request messages with a logger level of INFO
Trace='request_response' is DEBUG logging of request messages and response messages truncated to 132 bytes with a logger level of INFO
Trace='all' is DEBUG logging of the entire request and response messages with a logger level of INFO

"""
from ixnetwork_restpy.testplatform.testplatform import TestPlatform

test_platform = TestPlatform('127.0.0.1', log_file_name='test.log', trace='all')
test_platform.Authenticate('admin', 'admin')
sessions = test_platform.Sessions.add()

test_platform.info('Set the tracing to `request`so that truncated request messages are logged')
test_platform.Trace = 'request'
sessions.Ixnetwork.Vport.add()

test_platform.info('Set the tracing to `request_response`so that truncated request and response messages are logged')
test_platform.Trace = 'request_response'
sessions.Ixnetwork.Vport.add()

test_platform.info('Set the tracing to `all` so that entire request and response messages are logged')
test_platform.Trace = 'all'
sessions.Ixnetwork.Vport.add()

test_platform.info('Set the tracing `none` so that nothing is logged')
test_platform.Trace = 'none'
sessions.Ixnetwork.Vport.add()
