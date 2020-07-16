import unittest
try:
	from unittest.mock import Mock, patch
except:
	from mock import Mock, patch
from ixnetwork_restpy.tests.fixtures.mocks import Mocks
from ixnetwork_restpy.testplatform.testplatform import TestPlatform
from ixnetwork_restpy.assistants.statistics.statviewassistant import StatViewAssistant
from ixnetwork_restpy.errors import *

class TestStatistics(unittest.TestCase):
    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request)
    def test_can_get_view_names(self, mock_request):
        test_platform = TestPlatform('127.0.0.1', rest_port=11009, platform='windows')

        # use the default session and get the root node of the hierarchy
        ixnetwork = test_platform.Sessions.find().Ixnetwork
                
        #GetViewNames fetches all the available view on Ixnetwork server.
        statList  = StatViewAssistant.GetViewNames(ixnetwork)
        assert(len(statList) == 3)
    
    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request)
    def test_cannot_find_invalid_view_name(self, mock_request):
        test_platform = TestPlatform('127.0.0.1', rest_port=11009, platform='windows')

        # use the default session and get the root node of the hierarchy
        ixnetwork = test_platform.Sessions.find().Ixnetwork
        
        try:
            StatViewAssistant(ixnetwork, 'Port Stattics', Timeout=5)
        except NotFoundError as e:
            ixnetwork.info(e)

if __name__ == '__main__':
    unittest.main() 