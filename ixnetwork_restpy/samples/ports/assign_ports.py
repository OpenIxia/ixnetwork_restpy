"""Demonstrates the best practice for connecting vport(s) to hardware test ports.

AssignPorts is currently the optimal method for connecting hardware test ports to vport(s).

The AssignPorts method on the test platform does the following:
	- adds chassis to /availableHardware using Arg1
	- creates abstract ports if the abstract port list (Arg3) cannot meet the number of Arg1 test ports
	- clears ownership of test ports if Arg4 is True
	- waits until port statistic view for all test ports are ready
	- returns a list of abstract test ports that have not been connected to test ports
"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# setup test ports and virtual ports
chassis_ip = '10.36.74.26'
test_ports = [
	dict(Arg1=chassis_ip, Arg2=2, Arg3=13),
	dict(Arg1=chassis_ip, Arg2=2, Arg3=14)
]
virtual_ports = ixnetwork.Vport.add().add()

connected_ports = ixnetwork.AssignPorts(test_ports, [], virtual_ports, True)

