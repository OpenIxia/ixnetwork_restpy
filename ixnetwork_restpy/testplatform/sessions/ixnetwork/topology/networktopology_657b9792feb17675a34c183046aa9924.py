# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
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
    _SDM_ATT_MAP = {
        'Count': 'count',
        'FromNodeIndex': 'fromNodeIndex',
        'LinksPerNetwork': 'linksPerNetwork',
        'NodesPerNetwork': 'nodesPerNetwork',
        'ToNodeIndex': 'toNodeIndex',
    }

    def __init__(self, parent):
        super(NetworkTopology, self).__init__(parent)

    @property
    def CfmSimulatedTopology(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmsimulatedtopology_dc7c77f2f0651bc2e9e2b4796e7969b8.CfmSimulatedTopology): An instance of the CfmSimulatedTopology class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmsimulatedtopology_dc7c77f2f0651bc2e9e2b4796e7969b8 import CfmSimulatedTopology
        return CfmSimulatedTopology(self)

    @property
    def ExternalLink(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.externallink_92dfe6bfe971a09aeb88dd947516d4b8.ExternalLink): An instance of the ExternalLink class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.externallink_92dfe6bfe971a09aeb88dd947516d4b8 import ExternalLink
        return ExternalLink(self)

    @property
    def IsisDceSimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcesimulatedtopologyconfig_4d88faaf0dcf92c0db3815f377d8e18d.IsisDceSimulatedTopologyConfig): An instance of the IsisDceSimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcesimulatedtopologyconfig_4d88faaf0dcf92c0db3815f377d8e18d import IsisDceSimulatedTopologyConfig
        return IsisDceSimulatedTopologyConfig(self)

    @property
    def IsisL3SimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3simulatedtopologyconfig_1890e701c5ec6fe1e10b65bd6dd71fb5.IsisL3SimulatedTopologyConfig): An instance of the IsisL3SimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3simulatedtopologyconfig_1890e701c5ec6fe1e10b65bd6dd71fb5 import IsisL3SimulatedTopologyConfig
        return IsisL3SimulatedTopologyConfig(self)

    @property
    def IsisSpbSimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbsimulatedtopologyconfig_768b370addc0695580bc7b46b573d5a7.IsisSpbSimulatedTopologyConfig): An instance of the IsisSpbSimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbsimulatedtopologyconfig_768b370addc0695580bc7b46b573d5a7 import IsisSpbSimulatedTopologyConfig
        return IsisSpbSimulatedTopologyConfig(self)

    @property
    def IsisTrillSimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillsimulatedtopologyconfig_75756af58887c54a1ba308c360c558c6.IsisTrillSimulatedTopologyConfig): An instance of the IsisTrillSimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillsimulatedtopologyconfig_75756af58887c54a1ba308c360c558c6 import IsisTrillSimulatedTopologyConfig
        return IsisTrillSimulatedTopologyConfig(self)

    @property
    def LdpSimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpsimulatedtopologyconfig_2643921a67ce50542ef3fd34b8bbaa14.LdpSimulatedTopologyConfig): An instance of the LdpSimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpsimulatedtopologyconfig_2643921a67ce50542ef3fd34b8bbaa14 import LdpSimulatedTopologyConfig
        return LdpSimulatedTopologyConfig(self)

    @property
    def NetTopologyCustom(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologycustom_bb47a11f6f5e815f215a8a6cd753c1de.NetTopologyCustom): An instance of the NetTopologyCustom class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologycustom_bb47a11f6f5e815f215a8a6cd753c1de import NetTopologyCustom
        return NetTopologyCustom(self)

    @property
    def NetTopologyFatTree(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologyfattree_da9d3b86dfd4429aea6fd83e55f04c9b.NetTopologyFatTree): An instance of the NetTopologyFatTree class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologyfattree_da9d3b86dfd4429aea6fd83e55f04c9b import NetTopologyFatTree
        return NetTopologyFatTree(self)

    @property
    def NetTopologyGrid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologygrid_83b3d6466db720e42f8941917ac35776.NetTopologyGrid): An instance of the NetTopologyGrid class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologygrid_83b3d6466db720e42f8941917ac35776 import NetTopologyGrid
        return NetTopologyGrid(self)

    @property
    def NetTopologyHubNSpoke(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologyhubnspoke_6bab635dca26252c93ca0fa925b87be2.NetTopologyHubNSpoke): An instance of the NetTopologyHubNSpoke class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologyhubnspoke_6bab635dca26252c93ca0fa925b87be2 import NetTopologyHubNSpoke
        return NetTopologyHubNSpoke(self)

    @property
    def NetTopologyLinear(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologylinear_293f26b1484d1839fe8dc0ad00ed2bd5.NetTopologyLinear): An instance of the NetTopologyLinear class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologylinear_293f26b1484d1839fe8dc0ad00ed2bd5 import NetTopologyLinear
        return NetTopologyLinear(self)

    @property
    def NetTopologyMesh(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologymesh_517b38131e86c1d1de945da2a10cb914.NetTopologyMesh): An instance of the NetTopologyMesh class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologymesh_517b38131e86c1d1de945da2a10cb914 import NetTopologyMesh
        return NetTopologyMesh(self)

    @property
    def NetTopologyRing(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologyring_53b30b7628c14a65021b6e4a332bfa7c.NetTopologyRing): An instance of the NetTopologyRing class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologyring_53b30b7628c14a65021b6e4a332bfa7c import NetTopologyRing
        return NetTopologyRing(self)

    @property
    def NetTopologyTree(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologytree_89d07e1ee9645fffc22bcedbb938f9f7.NetTopologyTree): An instance of the NetTopologyTree class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nettopologytree_89d07e1ee9645fffc22bcedbb938f9f7 import NetTopologyTree
        return NetTopologyTree(self)

    @property
    def OspfSimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsimulatedtopologyconfig_97e4d55091dcce69020c77d08e90eee0.OspfSimulatedTopologyConfig): An instance of the OspfSimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsimulatedtopologyconfig_97e4d55091dcce69020c77d08e90eee0 import OspfSimulatedTopologyConfig
        return OspfSimulatedTopologyConfig(self)

    @property
    def Ospfv3SimulatedTopologyConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3simulatedtopologyconfig_497060526b39fa396a89711564688ce1.Ospfv3SimulatedTopologyConfig): An instance of the Ospfv3SimulatedTopologyConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3simulatedtopologyconfig_497060526b39fa396a89711564688ce1 import Ospfv3SimulatedTopologyConfig
        return Ospfv3SimulatedTopologyConfig(self)

    @property
    def SimInterface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterface_c5ed266ee5e10544297ff85a7ebe3c50.SimInterface): An instance of the SimInterface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterface_c5ed266ee5e10544297ff85a7ebe3c50 import SimInterface
        return SimInterface(self)

    @property
    def SimRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.simrouter_6b838313b6104e3f157ae2656c6afbb1.SimRouter): An instance of the SimRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.simrouter_6b838313b6104e3f157ae2656c6afbb1 import SimRouter
        return SimRouter(self)

    @property
    def SimRouterBridge(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.simrouterbridge_7a0805a6e8bddd5a066f100c0b0a7df2.SimRouterBridge): An instance of the SimRouterBridge class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.simrouterbridge_7a0805a6e8bddd5a066f100c0b0a7df2 import SimRouterBridge
        return SimRouterBridge(self)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def FromNodeIndex(self):
        """
        Returns
        -------
        - list(str): Link From Node Index
        """
        return self._get_attribute(self._SDM_ATT_MAP['FromNodeIndex'])

    @property
    def LinksPerNetwork(self):
        """
        Returns
        -------
        - number: linksPerNetwork is controled by assigned topology
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinksPerNetwork'])

    @property
    def NodesPerNetwork(self):
        """
        Returns
        -------
        - number: Number of nodes in the Network Topology, including the root node defined in the parent Device Group
        """
        return self._get_attribute(self._SDM_ATT_MAP['NodesPerNetwork'])

    @property
    def ToNodeIndex(self):
        """
        Returns
        -------
        - list(str): Link To Node Index
        """
        return self._get_attribute(self._SDM_ATT_MAP['ToNodeIndex'])

    def add(self):
        """Adds a new networkTopology resource on the server and adds it to the container.

        Returns
        -------
        - self: This instance with all currently retrieved networkTopology resources using find and the newly added networkTopology resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

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
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

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
