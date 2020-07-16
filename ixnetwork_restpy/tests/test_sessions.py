import unittest
try:
	from unittest.mock import Mock, patch
except:
	from mock import Mock, patch
from ixnetwork_restpy.tests.fixtures.mocks import Mocks
from ixnetwork_restpy.testplatform.testplatform import TestPlatform


class TestSessions(unittest.TestCase):
    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request) 
    def test_sessions(self, mock_request):
        testplatform = TestPlatform('127.0.0.1')
        session = testplatform.Sessions.find()
        testplatform.info(session)
        assert(len(session) == 1)

    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request) 
    def test_ixnetwork_getter(self, mock_request):
        ixnetwork = TestPlatform('127.0.0.1').Sessions.find().Ixnetwork
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork
        assert(isinstance(ixnetwork, Ixnetwork) is True)

if __name__ == '__main__':
    unittest.main()