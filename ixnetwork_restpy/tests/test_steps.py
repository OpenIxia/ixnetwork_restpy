import unittest
try:
    from unittest.mock import Mock, patch
except:
    from mock import Mock, patch
from ixnetwork_restpy.tests.fixtures.mocks import Mocks
from ixnetwork_restpy.testplatform.testplatform import TestPlatform


class TestSteps(unittest.TestCase):
    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request) 
    def test_steps(self, mock_request):
        testplatform = TestPlatform('127.0.0.1')
        session = testplatform.Sessions.find()
        # session.Ixnetwork.Topology.find().DeviceGroup.find().Ethernet.find().Ipv4.find().
        assert(len(session) == 1)

if __name__ == '__main__':
    unittest.main()