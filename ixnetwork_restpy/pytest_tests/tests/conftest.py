import pytest
from collections import namedtuple
from ixnetwork_restpy.testplatform.testplatform import TestPlatform


def pytest_addoption(parser):
    parser.addoption('--server',default=[],action='append',help='''server: <server_ip>:<server_port>:<server_platform>
    example--> 
    --server 10.39.37.24:443:connection_manager 
    --server 10.117.156.155:443:linux
    --server 127.0.0.1:11009:windows
    ''')


def pytest_generate_tests(metafunc):
    if "server" in metafunc.fixturenames:
        metafunc.parametrize("server", metafunc.config.getoption("server"))


@pytest.fixture
def test_platform(server):
    # setup phase
    # 1.Connect
    # 2.Return Testplatform
    ip, port, platform = server.split(':')
    if platform == 'windows':
        test_platform = TestPlatform(ip, rest_port=port)
    else:
        test_platform = TestPlatform(ip)
    return test_platform


@pytest.fixture
def ixnetwork(test_platform):
    # setup phase
    # 1.connecting to server
    # 2.create test platform
    # 3.Add session in test platform
    # 4.get ixnetwork object
    # 5.exec new config
    # 6.returning an ixnetwork object
    # todo: implement for connection manager

    # creating server obj from test platform
    Server = namedtuple('Server', ['ip', 'port', 'platform'])
    server_obj = Server(
        test_platform.Hostname,
        test_platform.RestPort,
        test_platform.Platform
    )

    # authenticate regardless of platform
    # platforms that do not support authentication should treat it as a null operation    
    test_platform.Authenticate('admin', 'admin')

    # getting sessions as per test platform
    if test_platform.Platform == 'windows':
        session = test_platform.Sessions.find(Id=1)
    elif test_platform.Platform == 'linux':
        sessions = test_platform.Sessions.find()
        if (len(sessions) > 0) :
            session = sessions[0]
        else:
            session = test_platform.Sessions.add()
    elif test_platform.Platform == 'connection_manager':
        sessions = test_platform.Sessions.find()
        if (len(sessions) > 0) :
            session = sessions[0]
            if session.State != 'ACTIVE':
                session = test_platform.Sessions.add()    
        else:
            session = test_platform.Sessions.add()
            
    # getting ixnetwork object from session and return it
    ixnetwork = session.Ixnetwork
    ixnetwork.NewConfig()
    return ixnetwork

    # teardown phase
    #if server_obj.platform != 'windows':
    #    session.remove()


@pytest.fixture
def vports(ixnetwork):
    # returns a couple of vports
    return ixnetwork.Vport.add(Name='ethernet-1').add(Name='ethernet-2')

@pytest.fixture
def topologies(vports):
    vport_1, vport_2 = vports
    ixnetwork=vport_1._parent
    topology_1, topology_2 = ixnetwork.Topology.add(Vports=vport_1).add(Vports=vport_2)
    return topology_1, topology_2

@pytest.fixture
def device_groups(topologies):
    topology_1, topology_2 = topologies
    dg1 = topology_1.DeviceGroup.add()
    dg2 = topology_2.DeviceGroup.add()
    return dg1, dg2

@pytest.fixture
def ethernet_stacks(device_groups):
    dg1, dg2 = device_groups
    eth_1 = dg1.Ethernet.add()
    eth_2 = dg2.Ethernet.add()
    return eth_1, eth_2

@pytest.fixture
def ipv4_stacks(ethernet_stacks):
    eth_1, eth_2 = ethernet_stacks
    ipv4_1 = eth_1.Ipv4.add()
    ipv4_2 = eth_2.Ipv4.add()
    return ipv4_1, ipv4_2
