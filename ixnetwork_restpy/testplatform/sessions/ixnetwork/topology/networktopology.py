# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class NetworkTopology(Base):
    """Container for Network Topology related objects
    The NetworkTopology class encapsulates a list of networkTopology resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetworkTopology.find() method.
    The list can be managed by using the NetworkTopology.add() and NetworkTopology.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'networkTopology'

    def __init__(self, parent):
        super(NetworkTopology, self).__init__(parent)

    @property
    def ExternalLink(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.externallink.ExternalLink): An instance of the ExternalLink class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.externallink import ExternalLink
        return ExternalLink(self)

    @property
    def IsisDceSimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcesimulatedtopologyconfig.IsisDceSimulatedTopologyConfig): An instance of the IsisDceSimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcesimulatedtopologyconfig import IsisDceSimulatedTopologyConfig
        return IsisDceSimulatedTopologyConfig(self)

    @property
    def IsisL3SimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3simulatedtopologyconfig.IsisL3SimulatedTopologyConfig): An instance of the IsisL3SimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3simulatedtopologyconfig import IsisL3SimulatedTopologyConfig
        return IsisL3SimulatedTopologyConfig(self)

    @property
    def IsisSpbSimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbsimulatedtopologyconfig.IsisSpbSimulatedTopologyConfig): An instance of the IsisSpbSimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbsimulatedtopologyconfig import IsisSpbSimulatedTopologyConfig
        return IsisSpbSimulatedTopologyConfig(self)

    @property
    def IsisTrillSimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillsimulatedtopologyconfig.IsisTrillSimulatedTopologyConfig): An instance of the IsisTrillSimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillsimulatedtopologyconfig import IsisTrillSimulatedTopologyConfig
        return IsisTrillSimulatedTopologyConfig(self)

    @property
    def LdpSimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpsimulatedtopologyconfig.LdpSimulatedTopologyConfig): An instance of the LdpSimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpsimulatedtopologyconfig import LdpSimulatedTopologyConfig
        return LdpSimulatedTopologyConfig(self)

    @property
    def NetTopologyCustom(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologycustom.NetTopologyCustom): An instance of the NetTopologyCustom class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologycustom import NetTopologyCustom
        return NetTopologyCustom(self)

    @property
    def NetTopologyFatTree(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologyfattree.NetTopologyFatTree): An instance of the NetTopologyFatTree class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologyfattree import NetTopologyFatTree
        return NetTopologyFatTree(self)

    @property
    def NetTopologyGrid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologygrid.NetTopologyGrid): An instance of the NetTopologyGrid class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologygrid import NetTopologyGrid
        return NetTopologyGrid(self)

    @property
    def NetTopologyHubNSpoke(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologyhubnspoke.NetTopologyHubNSpoke): An instance of the NetTopologyHubNSpoke class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologyhubnspoke import NetTopologyHubNSpoke
        return NetTopologyHubNSpoke(self)

    @property
    def NetTopologyLinear(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologylinear.NetTopologyLinear): An instance of the NetTopologyLinear class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologylinear import NetTopologyLinear
        return NetTopologyLinear(self)

    @property
    def NetTopologyMesh(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologymesh.NetTopologyMesh): An instance of the NetTopologyMesh class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologymesh import NetTopologyMesh
        return NetTopologyMesh(self)

    @property
    def NetTopologyRing(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologyring.NetTopologyRing): An instance of the NetTopologyRing class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologyring import NetTopologyRing
        return NetTopologyRing(self)

    @property
    def NetTopologyTree(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologytree.NetTopologyTree): An instance of the NetTopologyTree class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologytree import NetTopologyTree
        return NetTopologyTree(self)

    @property
    def OspfSimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsimulatedtopologyconfig.OspfSimulatedTopologyConfig): An instance of the OspfSimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsimulatedtopologyconfig import OspfSimulatedTopologyConfig
        return OspfSimulatedTopologyConfig(self)

    @property
    def Ospfv3SimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3simulatedtopologyconfig.Ospfv3SimulatedTopologyConfig): An instance of the Ospfv3SimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3simulatedtopologyconfig import Ospfv3SimulatedTopologyConfig
        return Ospfv3SimulatedTopologyConfig(self)

    @property
    def SimInterface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterface.SimInterface): An instance of the SimInterface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterface import SimInterface
        return SimInterface(self)

    @property
    def SimRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.simrouter.SimRouter): An instance of the SimRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.simrouter import SimRouter
        return SimRouter(self)

    @property
    def SimRouterBridge(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.simrouterbridge.SimRouterBridge): An instance of the SimRouterBridge class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.simrouterbridge import SimRouterBridge
        return SimRouterBridge(self)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute('count')

    @property
    def FromNodeIndex(self):
        """
        Returns
        -------
        - list(str): Link From Node Index
        """
        return self._get_attribute('fromNodeIndex')

    @property
    def LinksPerNetwork(self):
        """
        Returns
        -------
        - number: linksPerNetwork is controled by assigned topology
        """
        return self._get_attribute('linksPerNetwork')

    @property
    def NodesPerNetwork(self):
        """
        Returns
        -------
        - number: Number of nodes in the Network Topology, including the root node defined in the parent Device Group
        """
        return self._get_attribute('nodesPerNetwork')

    @property
    def ToNodeIndex(self):
        """
        Returns
        -------
        - list(str): Link To Node Index
        """
        return self._get_attribute('toNodeIndex')

    def add(self):
        """Adds a new networkTopology resource on the server and adds it to the container.

        Returns
        -------
        - self: This instance with all currently retrieved networkTopology resources using find and the newly added networkTopology resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained networkTopology resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, FromNodeIndex=None, LinksPerNetwork=None, NodesPerNetwork=None, ToNodeIndex=None):
        """Finds and retrieves networkTopology resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve networkTopology resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all networkTopology resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - FromNodeIndex (list(str)): Link From Node Index
        - LinksPerNetwork (number): linksPerNetwork is controled by assigned topology
        - NodesPerNetwork (number): Number of nodes in the Network Topology, including the root node defined in the parent Device Group
        - ToNodeIndex (list(str)): Link To Node Index

        Returns
        -------
        - self: This instance with matching networkTopology resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of networkTopology data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the networkTopology resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
