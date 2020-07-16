import unittest
try:
	from unittest.mock import Mock, patch
except:
	from mock import Mock, patch
from ixnetwork_restpy.tests.fixtures.mocks import Mocks
from ixnetwork_restpy.testplatform.testplatform import TestPlatform

class TestPorts(unittest.TestCase):
    @patch('ixnetwork_restpy.connection.Connection._request', side_effect=Mocks.mocked_request)
    def test_assign_ports(self, mock_request):
        testp = TestPlatform('127.0.0.1')
        session = testp.Sessions.find()[0]
        ixnetwork = session.Ixnetwork
        testp.Trace = 'all'
        vport = ixnetwork.Vport.find()
        chassis_ip = '10.39.35.12'
        test_ports = [
            dict(Arg1=chassis_ip, Arg2=2, Arg3=9),
            dict(Arg1=chassis_ip, Arg2=2, Arg3=10)
        ]
        connected_ports = ixnetwork.AssignPorts(test_ports, [], vport, True)
        assert(len(connected_ports) == 2)
        
if __name__ == '__main__':
    unittest.main()