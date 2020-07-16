import unittest
try:
    from unittest.mock import Mock, patch
except:
    from mock import Mock, patch
from ixnetwork_restpy.tests.fixtures.mocks import Mocks
from ixnetwork_restpy.testplatform.testplatform import TestPlatform


class TestTestPlatform(unittest.TestCase):
    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request) 
    def test_windows_platform(self, mock_request):
        Mocks.set_platform('windows')
        testplatform = TestPlatform('127.0.0.1', platform='windows', rest_port=11009)
        print(testplatform)
        assert(testplatform.href == '/api/v1')
        assert(testplatform.Hostname == '127.0.0.1')
        assert(testplatform.Platform == 'windows')
        assert(testplatform.RestPort == 11009)

    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request) 
    def test_linux_platform(self, mock_request):
        Mocks.set_platform('linux')
        testplatform = TestPlatform('127.0.0.1', platform='linux')
        print(testplatform)
        assert(testplatform.href == '/api/v1')
        assert(testplatform.Hostname == '127.0.0.1')
        assert(testplatform.Platform == 'linux')
        assert(testplatform.RestPort == 443)

    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request) 
    def test_connection_manager_platform(self, mock_request):
        Mocks.set_platform('connection_manager')
        testplatform = TestPlatform('127.0.0.1', platform='connection_manager')
        print(testplatform)
        assert(testplatform.href == '/api/v1')
        assert(testplatform.Hostname == '127.0.0.1')
        assert(testplatform.Platform == 'connection_manager')
        assert(testplatform.RestPort == 443)

    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request) 
    def test_session_getter(self, mock_request):
        testplatform = TestPlatform('127.0.0.1')
        print(testplatform)
        from ixnetwork_restpy.testplatform.sessions.sessions import Sessions
        assert(isinstance(testplatform.Sessions, Sessions) is True)

if __name__ == '__main__':
    unittest.main()