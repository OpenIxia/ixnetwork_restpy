import unittest
try:
    from unittest.mock import Mock, patch
except:
    from mock import Mock, patch
from ixnetwork_restpy.tests.fixtures.mocks import Mocks
from ixnetwork_restpy.testplatform.testplatform import TestPlatform


class TestConnect(unittest.TestCase):
    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request) 
    def test_ipv6_hostname(self, mock_request):
        for hostname in ['2620:10d:c0a8:21::2a', '[::1]']:
            testplatform = TestPlatform(hostname, rest_port='11009')
            assert('[' in testplatform.Hostname and ']' in testplatform.Hostname)

    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request) 
    def test_ipv4_hostname(self, mock_request):
        for hostname in ['127.0.0.1']:
            testplatform = TestPlatform(hostname, rest_port='11009')
            assert('[' not in testplatform.Hostname and ']' not in testplatform.Hostname)

    # @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request) 
    # def test_ipv6_redirect(self, mock_request):
    #     for hostname in ['2620:10d:c0a8:21::2a', '[::1]']:
    #         testplatform = TestPlatform(hostname, rest_port='11009')
    #         testplatform._connection._read('api/v1/redirect')
    #         assert('[' in testplatform.Hostname and ']' in testplatform.Hostname)

if __name__ == '__main__':
    unittest.main()