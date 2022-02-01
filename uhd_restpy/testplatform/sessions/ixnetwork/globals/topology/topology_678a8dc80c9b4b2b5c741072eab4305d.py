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
import sys
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Topology(Base):
    """Topology port level configuration
    The Topology class encapsulates a required topology resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'topology'
    _SDM_ATT_MAP = {
        'ApplyOnTheFlyState': 'applyOnTheFlyState',
        'NgpfProtocolRateMode': 'ngpfProtocolRateMode',
        'ProtocolActionsInProgress': 'protocolActionsInProgress',
        'ProtocolStackingMode': 'protocolStackingMode',
        'Status': 'status',
        'Vports': 'vports',
    }
    _SDM_ENUM_MAP = {
        'applyOnTheFlyState': ['allowed', 'notAllowed', 'nothingToApply'],
        'ngpfProtocolRateMode': ['basic', 'smooth'],
        'protocolStackingMode': ['parallel', 'sequential'],
        'status': ['configured', 'error', 'mixed', 'notStarted', 'started', 'starting', 'stopping'],
    }

    def __init__(self, parent, list_op=False):
        super(Topology, self).__init__(parent, list_op)

    @property
    def BgpIpv4Peer(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.bgpipv4peer_439a44dd340bf6fd724df996ab26569d.BgpIpv4Peer): An instance of the BgpIpv4Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.bgpipv4peer_439a44dd340bf6fd724df996ab26569d import BgpIpv4Peer
        if len(self._object_properties) > 0:
            if self._properties.get('BgpIpv4Peer', None) is not None:
                return self._properties.get('BgpIpv4Peer')
        return BgpIpv4Peer(self)._select()

    @property
    def BgpIpv6Peer(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv6peer.bgpipv6peer_7e5e36454dedaa483fd7dd20abef422b.BgpIpv6Peer): An instance of the BgpIpv6Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv6peer.bgpipv6peer_7e5e36454dedaa483fd7dd20abef422b import BgpIpv6Peer
        if len(self._object_properties) > 0:
            if self._properties.get('BgpIpv6Peer', None) is not None:
                return self._properties.get('BgpIpv6Peer')
        return BgpIpv6Peer(self)._select()

    @property
    def Esmc(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.esmc.esmc_a6e91ae9ab0a9252a7e1dbcd069fcc86.Esmc): An instance of the Esmc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.esmc.esmc_a6e91ae9ab0a9252a7e1dbcd069fcc86 import Esmc
        if len(self._object_properties) > 0:
            if self._properties.get('Esmc', None) is not None:
                return self._properties.get('Esmc')
        return Esmc(self)._select()

    @property
    def Ethernet(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.ethernet_ccd3a65106ab16a2364be51d1a412f05.Ethernet): An instance of the Ethernet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.ethernet_ccd3a65106ab16a2364be51d1a412f05 import Ethernet
        if len(self._object_properties) > 0:
            if self._properties.get('Ethernet', None) is not None:
                return self._properties.get('Ethernet')
        return Ethernet(self)._select()

    @property
    def Ipv4(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.ipv4_d3982d161b434ec799d31ef7237a4b96.Ipv4): An instance of the Ipv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.ipv4_d3982d161b434ec799d31ef7237a4b96 import Ipv4
        if len(self._object_properties) > 0:
            if self._properties.get('Ipv4', None) is not None:
                return self._properties.get('Ipv4')
        return Ipv4(self)._select()

    @property
    def Ipv6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6.ipv6_a9f2dfb33a5d9c10d60b9830b8455095.Ipv6): An instance of the Ipv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6.ipv6_a9f2dfb33a5d9c10d60b9830b8455095 import Ipv6
        if len(self._object_properties) > 0:
            if self._properties.get('Ipv6', None) is not None:
                return self._properties.get('Ipv6')
        return Ipv6(self)._select()

    @property
    def Ipv6Autoconfiguration(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.ipv6autoconfiguration_186fdf3eb8d47323f28ec9e4d4c3e927.Ipv6Autoconfiguration): An instance of the Ipv6Autoconfiguration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.ipv6autoconfiguration_186fdf3eb8d47323f28ec9e4d4c3e927 import Ipv6Autoconfiguration
        if len(self._object_properties) > 0:
            if self._properties.get('Ipv6Autoconfiguration', None) is not None:
                return self._properties.get('Ipv6Autoconfiguration')
        return Ipv6Autoconfiguration(self)._select()

    @property
    def IsisL3Router(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.isisl3router.isisl3router_b5c245f4973246022b20f2613546d45a.IsisL3Router): An instance of the IsisL3Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.isisl3router.isisl3router_b5c245f4973246022b20f2613546d45a import IsisL3Router
        if len(self._object_properties) > 0:
            if self._properties.get('IsisL3Router', None) is not None:
                return self._properties.get('IsisL3Router')
        return IsisL3Router(self)

    @property
    def Lac(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.lac.lac_8a6ae7a66f1fba21c9a7af820795ad38.Lac): An instance of the Lac class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.lac.lac_8a6ae7a66f1fba21c9a7af820795ad38 import Lac
        if len(self._object_properties) > 0:
            if self._properties.get('Lac', None) is not None:
                return self._properties.get('Lac')
        return Lac(self)._select()

    @property
    def Lacp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.lacp.lacp_8a53bc5dca056354ad9594ab602dbf11.Lacp): An instance of the Lacp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.lacp.lacp_8a53bc5dca056354ad9594ab602dbf11 import Lacp
        if len(self._object_properties) > 0:
            if self._properties.get('Lacp', None) is not None:
                return self._properties.get('Lacp')
        return Lacp(self)._select()

    @property
    def Lagportlacp(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.lagportlacp.lagportlacp_7a4a0d1aa284610bc44568a967d49355.Lagportlacp): An instance of the Lagportlacp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.lagportlacp.lagportlacp_7a4a0d1aa284610bc44568a967d49355 import Lagportlacp
        if len(self._object_properties) > 0:
            if self._properties.get('Lagportlacp', None) is not None:
                return self._properties.get('Lagportlacp')
        return Lagportlacp(self)._select()

    @property
    def Lagportstaticlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.lagportstaticlag.lagportstaticlag_e722ffdff0d9b2f5175aa99e8f6c6166.Lagportstaticlag): An instance of the Lagportstaticlag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.lagportstaticlag.lagportstaticlag_e722ffdff0d9b2f5175aa99e8f6c6166 import Lagportstaticlag
        if len(self._object_properties) > 0:
            if self._properties.get('Lagportstaticlag', None) is not None:
                return self._properties.get('Lagportstaticlag')
        return Lagportstaticlag(self)._select()

    @property
    def Macsec(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.macsec.macsec_8998c1b41f29384c2c688534cb45d85d.Macsec): An instance of the Macsec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.macsec.macsec_8998c1b41f29384c2c688534cb45d85d import Macsec
        if len(self._object_properties) > 0:
            if self._properties.get('Macsec', None) is not None:
                return self._properties.get('Macsec')
        return Macsec(self)._select()

    @property
    def Mka(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.mka.mka_aedde1a3ca5c00a7f6b976a4fce2c20d.Mka): An instance of the Mka class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.mka.mka_aedde1a3ca5c00a7f6b976a4fce2c20d import Mka
        if len(self._object_properties) > 0:
            if self._properties.get('Mka', None) is not None:
                return self._properties.get('Mka')
        return Mka(self)._select()

    @property
    def Ospfv2Router(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv2router.ospfv2router_74c05cad626e75b691d6431d3166eb2c.Ospfv2Router): An instance of the Ospfv2Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv2router.ospfv2router_74c05cad626e75b691d6431d3166eb2c import Ospfv2Router
        if len(self._object_properties) > 0:
            if self._properties.get('Ospfv2Router', None) is not None:
                return self._properties.get('Ospfv2Router')
        return Ospfv2Router(self)

    @property
    def Ospfv3Router(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv3router.ospfv3router_4c45a88f00fdf201bca989331894ee2f.Ospfv3Router): An instance of the Ospfv3Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv3router.ospfv3router_4c45a88f00fdf201bca989331894ee2f import Ospfv3Router
        if len(self._object_properties) > 0:
            if self._properties.get('Ospfv3Router', None) is not None:
                return self._properties.get('Ospfv3Router')
        return Ospfv3Router(self)._select()

    @property
    def Pce(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.pce.pce_5defd13c57ea406c73fd4b2cb010a30f.Pce): An instance of the Pce class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.pce.pce_5defd13c57ea406c73fd4b2cb010a30f import Pce
        if len(self._object_properties) > 0:
            if self._properties.get('Pce', None) is not None:
                return self._properties.get('Pce')
        return Pce(self)._select()

    @property
    def StaticLag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.staticlag.staticlag_bb394020ab7d7a51040dbbf42e2f75d1.StaticLag): An instance of the StaticLag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.staticlag.staticlag_bb394020ab7d7a51040dbbf42e2f75d1 import StaticLag
        if len(self._object_properties) > 0:
            if self._properties.get('StaticLag', None) is not None:
                return self._properties.get('StaticLag')
        return StaticLag(self)._select()

    @property
    def StaticMacsec(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.staticmacsec.staticmacsec_9ab47bdf2b3b33d22965d0aa28f2bb3d.StaticMacsec): An instance of the StaticMacsec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.staticmacsec.staticmacsec_9ab47bdf2b3b33d22965d0aa28f2bb3d import StaticMacsec
        if len(self._object_properties) > 0:
            if self._properties.get('StaticMacsec', None) is not None:
                return self._properties.get('StaticMacsec')
        return StaticMacsec(self)._select()

    @property
    def ApplyOnTheFlyState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(allowed | notAllowed | nothingToApply): Checks whether the apply changes operation is allowed
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyOnTheFlyState'])

    @property
    def NgpfProtocolRateMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(basic | smooth): Decides whether protocol's sessions will started in normal or smooth mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['NgpfProtocolRateMode'])
    @NgpfProtocolRateMode.setter
    def NgpfProtocolRateMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['NgpfProtocolRateMode'], value)

    @property
    def ProtocolActionsInProgress(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Lists all current protocol actions in progress
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolActionsInProgress'])

    @property
    def ProtocolStackingMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(parallel | sequential): Decides whether protocol's sessions will started sequentially or parallelly across the layers
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolStackingMode'])
    @ProtocolStackingMode.setter
    def ProtocolStackingMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ProtocolStackingMode'], value)

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): The current state of the scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def Vports(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport]): List of virtual ports included in the port level configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vports'])

    def update(self, NgpfProtocolRateMode=None, ProtocolStackingMode=None):
        # type: (str, str) -> Topology
        """Updates topology resource on the server.

        Args
        ----
        - NgpfProtocolRateMode (str(basic | smooth)): Decides whether protocol's sessions will started in normal or smooth mode
        - ProtocolStackingMode (str(parallel | sequential)): Decides whether protocol's sessions will started sequentially or parallelly across the layers

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, ApplyOnTheFlyState=None, NgpfProtocolRateMode=None, ProtocolActionsInProgress=None, ProtocolStackingMode=None, Status=None, Vports=None):
        # type: (str, str, List[str], str, str, List[str]) -> Topology
        """Finds and retrieves topology resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve topology resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all topology resources from the server.

        Args
        ----
        - ApplyOnTheFlyState (str(allowed | notAllowed | nothingToApply)): Checks whether the apply changes operation is allowed
        - NgpfProtocolRateMode (str(basic | smooth)): Decides whether protocol's sessions will started in normal or smooth mode
        - ProtocolActionsInProgress (list(str)): Lists all current protocol actions in progress
        - ProtocolStackingMode (str(parallel | sequential)): Decides whether protocol's sessions will started sequentially or parallelly across the layers
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): The current state of the scenario
        - Vports (list(str[None | /api/v1/sessions/1/ixnetwork/vport])): List of virtual ports included in the port level configuration

        Returns
        -------
        - self: This instance with matching topology resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of topology data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the topology resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AbortApplyOnTheFly(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abortApplyOnTheFly operation on the server.

        Aborts any on the fly changes that are outstanding

        abortApplyOnTheFly(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abortApplyOnTheFly', payload=payload, response_object=None)

    def ApplyOnTheFly(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the applyOnTheFly operation on the server.

        Apply any outstanding on the fly changes

        applyOnTheFly(async_operation=bool)string
        -----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Details about the operation's state.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyOnTheFly', payload=payload, response_object=None)

    def ConfigureAll(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the configureAll operation on the server.

        Configures all protocols in current scenario

        configureAll(async_operation=bool)
        ----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('configureAll', payload=payload, response_object=None)

    def FetchAndUpdateConfigFromCloud(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the fetchAndUpdateConfigFromCloud operation on the server.

        Learn MAC / IP address for a topology running on VM ports, deployed in AWS.

        fetchAndUpdateConfigFromCloud(Mode=string, async_operation=bool)
        ----------------------------------------------------------------
        - Mode (str): Mode. Options are: cmdrefreshall, cmdrefreshmac, cmdrefreshipv4
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('fetchAndUpdateConfigFromCloud', payload=payload, response_object=None)
