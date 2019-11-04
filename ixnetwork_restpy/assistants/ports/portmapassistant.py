""" Assistant class to simplify connecting virtual ports to test ports
"""
from ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork
from ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork


class PortMapAssistant(object):
    def __init__(self, IxNetwork):
        """
        Args:
            IxNetwork (obj (ixnetwork_restpy.testplatform.sessions.ixnetwork.Ixnetwork)): An Ixnetwork object
        """
        assert(isinstance(IxNetwork, Ixnetwork))
        self._IxNetwork = IxNetwork
        self._vports = []
        self._locations = []
        self._groups = {}

    def Map(self, IpAddress, CardId, PortId, Name=None):
        """
        Args:
            IpAddress (str): The ip address of the platform that hosts the card/port combination.
            CardId (number): The id of the card that hosts the port
            PortId (number): The id of the port
            Name (str): The name of the virtual port. 
                If the Name=None then a default named Vport will be created.
                If the Name is not None and the Vport exists then that Vport will be used
        
        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.vport.Vport): A Vport object

        Raises:
            ServerError: an unexpected error occurred on the server
        """	
        vport = self._IxNetwork.Vport.find(Name='^%s$' % Name)
        if len(vport) == 0:
            vport = self._IxNetwork.Vport.add(Name=Name)
        self._vports.append(vport.href)
        self._locations.append(
            {
                'arg1': IpAddress,
                'arg2': CardId,
                'arg3': PortId
            }
        )
        return vport

    def Clear(self):
        """Clears the internal map of vports to test port locations
        """
        self._vports = []
        self._locations = []
        return self

    def Connect(self, ForceOwnership=True):
        self._IxNetwork.AssignPorts(self._locations, [], self._vports, ForceOwnership)
        return self
