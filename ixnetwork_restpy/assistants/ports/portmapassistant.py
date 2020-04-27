""" Assistant class to simplify the task of virtual ports to test ports connections
"""
import time
from ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork


class PortMapAssistant(object):
    def __init__(self, IxNetwork):
        """Create mappings between test port locations and virtual ports.

        Args
        ----
        - IxNetwork (obj (ixnetwork_restpy.testplatform.sessions.ixnetwork.Ixnetwork)): An Ixnetwork object
        """
        assert(isinstance(IxNetwork, Ixnetwork))
        self._IxNetwork = IxNetwork
        self._vports = []
        self._locations = []

    def Map(self, IpAddress='127.0.0.1', CardId=1, PortId=1, Name=None, Port=None):
        """Map a test port to a virtual port
        
        Examples
        --------
            Map(IpAddress='10.36.74.26', CardId=2, PortId=13, Name='Tx')
            Map(Name='Tx', Port=('10.36.74.26', 2, 13))
            Map('10.36.74.26', 2, 13, Name='Tx')
            Map('10.36.74.26', 2, 14, Name=vport.Name)

        Args
        ----
        - IpAddress (str): The ip address of the platform that hosts the card/port combination.
            If the IpAddress is not specified the default value is 127.0.0.1
        - CardId (number): The id of the card that hosts the port
            If the CardId is not specified the default value is 1
        - PortId (number): The id of the port.
        - Name (str): The name of a virtual port. 
            If the Name is not specified a default named virtual port will be created.
            If the Name is specified an attempt to find it will be made. 
            If it does not exist a virtual port with that name will be created.
            The found or created vport will then be mapped.
        - Port (tuple(IpAddress,CardId,PortId)): A test port location tuple consisting of an IpAddress, CardId, PortId.
            Use this parameter instead of specifying the individual IpAddress, CardId, PortId parameters.
            If this parameter is present it will override any IpAddress, CardId, PortId parameters.
        
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.vport.Vport): A Vport object

        Raises
        ------
        - ValueError: a PortId was not provided
        - ServerError: an unexpected error occurred on the server
        """	
        if Port is not None:
            (IpAddress, CardId, PortId) = Port
        if PortId is None:
            raise ValueError('A PortId must be provided')
        if Name is not None:
            vport = self._IxNetwork.Vport.find(Name='^%s$' % Name)
        if Name is None or len(vport) == 0:
            vport = self._IxNetwork.Vport.add(Name=Name)
        self._vports.append(vport)
        self._locations.append(
            {
                'arg1': IpAddress,
                'arg2': CardId,
                'arg3': PortId
            }
        )
        return vport

    def Clear(self, Disconnect=False):
        """Clears the map of virtual ports to test port locations

        Args
        ----
        - Disconnect (bool): disconnect virtual ports from test ports
        """
        if Disconnect is True:
            self.Disconnect()
        self._vports = []
        self._locations = []
        return self

    def Connect(self, ForceOwnership=True, ChassisTimeout=60):
        """Connect mapped test ports to virtual ports

        The server method that connects test ports to virtual ports does the following:
        - connects to each unique chassis in the map
        - checks that the Ixnetwork.AvailableHardware.Chassis.State is 'ready' (timeout for all chassis is 16 minutes)
        - for each map pair, sets the Ixnetwork.Vport.ConnectedTo property to an AvailableHardware.Chassis.Card.Port
        - checks that the IxNetwork.Vport.ConnectionState is in ['connectedLinkUp', 'connectedLinkDown'] (timeout for all ports is 10 minutes) 
        - checks that the Port Statistics view is ready and all test ports are present as row labels in the view (timeout for all ports is 90 seconds)

        Args
        ----
        - ForceOwnership (bool): Forcefully clear ownership of the test port
        - ChassisTimeout (int): The amount of seconds to wait for all unique chassis to be in a 'ready' state
            The default is None which will use the server timeout of 16 minutes

        Raises
        ------
        - BadRequestError:
        - RuntimeError: when the ChassisTimeout value has been execeeded 
        - ServerError: 
        """
        if ChassisTimeout is not None:
            chassis = self._IxNetwork.AvailableHardware.Chassis
            ip_addresses = []
            for location in self._locations:
                ip_addresses.append(location['arg1'])
            ip_addresses = set(ip_addresses)
            for ip_address in ip_addresses:
                chassis.add(Hostname=ip_address)
            start_time = time.time()
            hostname_pattern = '^(%s)$' % '|'.join(ip_addresses)
            while True:
                matches = chassis.find(Hostname=hostname_pattern, State='ready')
                if len(matches) == len(ip_addresses):
                    break
                if time.time() - start_time > ChassisTimeout:
                    not_ready = []
                    for match in chassis.find(State='^(?!ready).*$'):
                        not_ready.append(match.Hostname)
                    raise RuntimeError('After %s seconds, chassis [%s] are not in a ready state' % (ChassisTimeout, ', '.join(not_ready)))
                time.sleep(3)
        self._IxNetwork.AssignPorts(self._locations, [], self._vports, ForceOwnership)
        return self

    def Disconnect(self):
        """Disconnect all mapped virtual ports from test port locations
        """
        for vport in self._vports:
            vport.ReleasePort()
        return self

    def __str__(self):
        map = ''
        for vport, location in zip(self._vports, self._locations):
            vport.refresh()
            map += 'Vport.Name[%s] -> location[%s;%s;%s] -> Vport.ConnectionState[%s]\n' % \
                (vport.Name, location['arg1'], location['arg2'], location['arg3'], vport.ConnectionState)
        return map