import unittest
try:
    from unittest.mock import Mock, patch
except:
    from mock import Mock, patch
from ixnetwork_restpy.tests.fixtures.mocks import Mocks
from ixnetwork_restpy.testplatform.testplatform import TestPlatform


class TestSlots(unittest.TestCase):
    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request) 
    def test_set_non_existent_property(self, mock_request):
        testplatform = TestPlatform('127.0.0.1')
        session = testplatform.Sessions.find()
        vport = session.Ixnetwork.Vport.find()
        vport.Name = 'Changed Vport Name'
        try:
            vport.Abcd = 'Dynamic property denied by __slots__'
            assert('Broken __slots__')
        except AttributeError as e:
            print('Successfully denied setting dynamic Abcd attribute')
        
    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request) 
    def test_get_non_existent_property(self, mock_request):
        testplatform = TestPlatform('127.0.0.1')
        session = testplatform.Sessions.find()
        vport = session.Ixnetwork.Vport.find()
        try:
            print(vport.Abcd)
            assert('Broken __slots__')
        except AttributeError as e:
            print('Successfully denied getting dynamic Abcd attribute')

if __name__ == '__main__':
    unittest.main()     