""" Assistant class to simplify the task of virtual ports to test ports connections
"""
from ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork


class PortMapAssistant(object):
    def __init__(self, IxNetwork):
        """Create mappings between test port locations and virtual ports.

        Args
        ----
            IxNetwork (obj (ixnetwork_restpy.testplatform.sessions.ixnetwork.Ixnetwork)): An Ixnetwork object
        """
        assert(isinstance(IxNetwork, Ixnetwork))
        self._IxNetwork = IxNetwork
        self._vports = []
        self._locations = []

    def Map(self, *args, **kwargs):
        """Map a test port location to a virtual port
        
        Example
        -------
            Map(IpAddress='10.36.74.26', CardId=2, PortId=13, Name='Tx')
            Map(Port=('10.36.74.26', 2, 13), Name='Tx')
            Map('10.36.74.26', 2, 13, Name='Tx')

        Args
        ----
            IpAddress (str): The ip address of the platform that hosts the card/port combination.
                If the IpAddress is not specified the default value is 127.0.0.1
            CardId (number): The id of the card that hosts the port
                If the CardId is not specified the default value is 1
            PortId (number): The id of the port.
            Name (str): The name of the virtual port. 
                If the virtual port cannot be found using the Name parameter a default named virtual port will be created.
            Port (tuple(IpAddress,CardId,PortId)): A test port location tuple consisting of an IpAddress, CardId, PortId.
                Use this parameter instead of specifying the individual IpAddress, CardId, PortId parameters.
                If this parameter is present it will override any IpAddress, CardId, PortId parameters.
        
        Returns
        -------
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.vport.Vport): A Vport object

        Raises
        ------
            ValueError: a PortId was not provided
            ServerError: an unexpected error occurred on the server
        """	
        if len(args) >= 1:
            IpAddress = args[0]
        else:
            IpAddress = kwargs.get('IpAddress', '127.0.0.1')
        if len(args) >= 2:
            CardId = args[1]
        else:
            CardId = kwargs.get('CardId', 1)
        if len(args) >= 3:
            PortId = args[2]
        else:
            PortId = kwargs.get('PortId', None)
        Port = kwargs.get('Port', None)
        Name = kwargs.get('Name', None)
        if Port is not None:
            (IpAddress, CardId, PortId) = Port
        if PortId is None:
            raise ValueError('A PortId must be provided')
        vport = self._IxNetwork.Vport.find(Name='^%s$' % Name)
        if len(vport) == 0:
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
            Disconnect (bool): disconnect virtual ports from test ports
        """
        if Disconnect is True:
            self.Disconnect()
        self._vports = []
        self._locations = []
        return self

    def Connect(self, ForceOwnership=True):
        """Connect all mapped virtual ports to test port locations

        Args
        ----
            ForceOwnership (bool): Forcefully clear ownership of the test port
        """
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