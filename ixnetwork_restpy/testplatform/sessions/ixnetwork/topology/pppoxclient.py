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


class Pppoxclient(Base):
    """PPPoX Client
    The Pppoxclient class encapsulates a list of pppoxclient resources that are managed by the user.
    A list of resources can be retrieved from the server using the Pppoxclient.find() method.
    The list can be managed by using the Pppoxclient.add() and Pppoxclient.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'pppoxclient'

    def __init__(self, parent):
        super(Pppoxclient, self).__init__(parent)

    @property
    def Bfdv4Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface.Bfdv4Interface): An instance of the Bfdv4Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface import Bfdv4Interface
        return Bfdv4Interface(self)

    @property
    def Bfdv6Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface.Bfdv6Interface): An instance of the Bfdv6Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface import Bfdv6Interface
        return Bfdv6Interface(self)

    @property
    def BgpIpv4Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer.BgpIpv4Peer): An instance of the BgpIpv4Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer import BgpIpv4Peer
        return BgpIpv4Peer(self)

    @property
    def BgpIpv6Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer.BgpIpv6Peer): An instance of the BgpIpv6Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer import BgpIpv6Peer
        return BgpIpv6Peer(self)

    @property
    def Connector(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector): An instance of the Connector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
        return Connector(self)

    @property
    def Dhcpv6client(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6client.Dhcpv6client): An instance of the Dhcpv6client class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6client import Dhcpv6client
        return Dhcpv6client(self)

    @property
    def ECpriRe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprire.ECpriRe): An instance of the ECpriRe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprire import ECpriRe
        return ECpriRe(self)

    @property
    def ECpriRec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirec.ECpriRec): An instance of the ECpriRec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirec import ECpriRec
        return ECpriRec(self)

    @property
    def Geneve(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve.Geneve): An instance of the Geneve class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve import Geneve
        return Geneve(self)

    @property
    def IgmpHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost.IgmpHost): An instance of the IgmpHost class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost import IgmpHost
        return IgmpHost(self)

    @property
    def IgmpQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier.IgmpQuerier): An instance of the IgmpQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier import IgmpQuerier
        return IgmpQuerier(self)

    @property
    def MldHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost.MldHost): An instance of the MldHost class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost import MldHost
        return MldHost(self)

    @property
    def MldQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier.MldQuerier): An instance of the MldQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier import MldQuerier
        return MldQuerier(self)

    @property
    def MplsOam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam.MplsOam): An instance of the MplsOam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam import MplsOam
        return MplsOam(self)

    @property
    def NetconfClient(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient.NetconfClient): An instance of the NetconfClient class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient import NetconfClient
        return NetconfClient(self)

    @property
    def NetconfServer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver.NetconfServer): An instance of the NetconfServer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver import NetconfServer
        return NetconfServer(self)

    @property
    def Ospfv2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2.Ospfv2): An instance of the Ospfv2 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2 import Ospfv2
        return Ospfv2(self)

    @property
    def Ospfv3(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3.Ospfv3): An instance of the Ospfv3 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3 import Ospfv3
        return Ospfv3(self)

    @property
    def Pcc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc.Pcc): An instance of the Pcc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc import Pcc
        return Pcc(self)

    @property
    def Pce(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce.Pce): An instance of the Pce class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce import Pce
        return Pce(self)

    @property
    def PimV4Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface.PimV4Interface): An instance of the PimV4Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface import PimV4Interface
        return PimV4Interface(self)

    @property
    def PimV6Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface.PimV6Interface): An instance of the PimV6Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface import PimV6Interface
        return PimV6Interface(self)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
        return Tag(self)

    @property
    def TlvProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile.TlvProfile): An instance of the TlvProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile import TlvProfile
        return TlvProfile(self)

    @property
    def Vxlan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan.Vxlan): An instance of the Vxlan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan import Vxlan
        return Vxlan(self)

    @property
    def Vxlanv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanv6.Vxlanv6): An instance of the Vxlanv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanv6 import Vxlanv6
        return Vxlanv6(self)

    @property
    def AcMatchMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ?
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('acMatchMac'))

    @property
    def AcMatchName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ?
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('acMatchName'))

    @property
    def AcOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates PPPoE AC retrieval mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('acOptions'))

    @property
    def ActualRateDownstream(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter specifies the value to be included in the vendor specific PPPoE tag. It is the actual downstream data rate (sub-option 0x81), in kbps.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('actualRateDownstream'))

    @property
    def ActualRateUpstream(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter specifies the value to be included in the vendor specific PPPoE tag. It is the actual upstream data rate (sub-option 0x82), in kbps.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('actualRateUpstream'))

    @property
    def AgentAccessAggregationCircuitId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value to be inserted into the Agent Access-Aggregation-Circuit-ID-ASCII-Value field of the PPPoX tag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('agentAccessAggregationCircuitId'))

    @property
    def AgentCircuitId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value to be inserted into the Agent Circuit ID field of the PPPoX tag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('agentCircuitId'))

    @property
    def AgentRemoteId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value to be inserted into the Agent Remote ID field of the PPPoX tag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('agentRemoteId'))

    @property
    def AuthRetries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of PPP authentication retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('authRetries'))

    @property
    def AuthTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for PPP authentication, in seconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('authTimeout'))

    @property
    def AuthType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The authentication type to use during link setup.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('authType'))

    @property
    def ChapName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User name when CHAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('chapName'))

    @property
    def ChapSecret(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Secret when CHAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('chapSecret'))

    @property
    def ClientDnsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The client DNS options.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientDnsOptions'))

    @property
    def ClientLocalIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The requested IPv4 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientLocalIp'))

    @property
    def ClientLocalIpv6Iid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The requested IPv6 Interface Identifier (IID).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientLocalIpv6Iid'))

    @property
    def ClientNcpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The NCP configuration mode for IPv4 addressing.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientNcpOptions'))

    @property
    def ClientNetmask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The netmask that the client will use with the assigned IP address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientNetmask'))

    @property
    def ClientNetmaskOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The client netmask option.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientNetmaskOptions'))

    @property
    def ClientPrimaryDnsAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the primary DNS server address that the client requests from the server when the value of the Client DNS Options field is set to 'Request Primary only' or 'Request Primary and Secondary'.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientPrimaryDnsAddress'))

    @property
    def ClientSecondaryDnsAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the secondary DNS server address that the client requests from the server when the value of the Client DNS Options field is set to 'Request Primary and Secondary'.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientSecondaryDnsAddress'))

    @property
    def ClientSignalIWF(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-option 0xFE (signaling of interworked sessions) into the DSL tag in PADI and PADR packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientSignalIWF'))

    @property
    def ClientSignalLoopChar(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-options 0x81 and 0x82 into the DSL tag in PADI and PADR packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientSignalLoopChar'))

    @property
    def ClientSignalLoopEncapsulation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-option 0x90 into the DSL tag in PADI and PADR packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientSignalLoopEncapsulation'))

    @property
    def ClientSignalLoopId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-options 0x01 , 0x02, 0x03 (Remote ID,Circuit ID and Access Aggregation Circuit ID) into the DSL tag in PADI and PADR packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientSignalLoopId'))

    @property
    def ClientV6NcpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The NCP configuration mode for IPv6 addressing.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientV6NcpOptions'))

    @property
    def ClientWinsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the mode in which WINS host addresses are configured.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientWinsOptions'))

    @property
    def ClientWinsPrimaryAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the primary WINS address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientWinsPrimaryAddress'))

    @property
    def ClientWinsSecondaryAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the secondary WINS address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('clientWinsSecondaryAddress'))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer used to connect to the wire
        """
        return self._get_attribute('connectedVia')
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute('connectedVia', value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute('count')

    @property
    def DataLink(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A one-byte field included with sub-option 0x90.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('dataLink'))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute('descriptiveName')

    @property
    def DiscoveredIpv4Addresses(self):
        """
        Returns
        -------
        - list(str): The discovered IPv4 addresses.
        """
        return self._get_attribute('discoveredIpv4Addresses')

    @property
    def DiscoveredIpv6Addresses(self):
        """
        Returns
        -------
        - list(str): The discovered IPv6 addresses.
        """
        return self._get_attribute('discoveredIpv6Addresses')

    @property
    def DiscoveredMacs(self):
        """
        Returns
        -------
        - list(str): The discovered remote MAC address.
        """
        return self._get_attribute('discoveredMacs')

    @property
    def DiscoveredRemoteSessionIds(self):
        """
        Returns
        -------
        - list(number): Remote session ID.
        """
        return self._get_attribute('discoveredRemoteSessionIds')

    @property
    def DiscoveredRemoteTunnelIds(self):
        """
        Returns
        -------
        - list(number): Remote tunnel ID.
        """
        return self._get_attribute('discoveredRemoteTunnelIds')

    @property
    def DiscoveredSessionIds(self):
        """
        Returns
        -------
        - list(number): The negotiated session ID.
        """
        return self._get_attribute('discoveredSessionIds')

    @property
    def DiscoveredTunnelIPs(self):
        """
        Returns
        -------
        - list(str): The discovered remote tunnel IP.
        """
        return self._get_attribute('discoveredTunnelIPs')

    @property
    def DiscoveredTunnelIds(self):
        """
        Returns
        -------
        - list(number): The negotiated tunnel ID.
        """
        return self._get_attribute('discoveredTunnelIds')

    @property
    def DomainList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure domain group settings
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('domainList'))

    @property
    def DslTypeTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DSL Type to be advertised in PPPoE VSA Tag. For undefined DSL type user has to select User-defined DSL Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('dslTypeTlv'))

    @property
    def EchoReqInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Keep alive interval, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('echoReqInterval'))

    @property
    def EnableDomainGroups(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable domain groups
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableDomainGroups'))

    @property
    def EnableEchoReq(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ?
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableEchoReq'))

    @property
    def EnableEchoRsp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ?
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableEchoRsp'))

    @property
    def EnableHostUniq(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables PPPoE Host-Uniq tag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableHostUniq'))

    @property
    def EnableMaxPayload(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables PPPoE Max Payload tag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableMaxPayload'))

    @property
    def EnableRedial(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, PPPoE redial is enabled
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableRedial'))

    @property
    def Encaps1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A one-byte field included with sub-option 0x90.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('encaps1'))

    @property
    def Encaps2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A one-byte field included with sub-option 0x90.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('encaps2'))

    @property
    def EndpointDiscNegotiation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Endpoint Discriminator Negotiation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('endpointDiscNegotiation'))

    @property
    def EndpointDiscriminatorClass(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Endpoint Discriminator for PPP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('endpointDiscriminatorClass'))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute('errors')

    @property
    def HostUniq(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates Host-Uniq Tag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('hostUniq'))

    @property
    def HostUniqLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Host-Uniq Length, in bytes
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('hostUniqLength'))

    @property
    def LcpAccm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Async-Control-Character-Map
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('lcpAccm'))

    @property
    def LcpEnableAccm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Async-Control-Character-Map
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('lcpEnableAccm'))

    @property
    def LcpMaxFailure(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of Configure-Nak packets sent without sending a Configure-Ack before assuming that configuration is not converging. Any further Configure-Nak packets for peer requested options are converted to Configure-Reject packets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('lcpMaxFailure'))

    @property
    def LcpRetries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of LCP retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('lcpRetries'))

    @property
    def LcpStartDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay time in milliseconds to wait before sending LCP Config Request packet
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('lcpStartDelay'))

    @property
    def LcpTermRetries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of LCP Termination Retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('lcpTermRetries'))

    @property
    def LcpTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for LCP phase, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('lcpTimeout'))

    @property
    def MaxPayload(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max Payload
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('maxPayload'))

    @property
    def MlpppIPAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The IP address used in the ML-PPP endpoint discriminator option of the LCP configure request sent by PPP clients
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mlpppIPAddress'))

    @property
    def MlpppMACAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The MAC addresses are automatically derived from the local MAC address. An address in this class contains an IEEE 802.1 MAC address is canonical (802.3) format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mlpppMACAddress'))

    @property
    def Mrru(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max Receive Reconstructed Unit for PPP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mrru'))

    @property
    def MrruNegotiation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MRRU Negotiation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mrruNegotiation'))

    @property
    def MruNegotiation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MRU Negotiation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mruNegotiation'))

    @property
    def Mtu(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max Transmit Unit for PPP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mtu'))

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute('multiplier')
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute('multiplier', value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NcpRetries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of NCP retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ncpRetries'))

    @property
    def NcpTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for NCP phase, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ncpTimeout'))

    @property
    def NcpType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP address type (IPv4 or IPv6) for Network Control Protocol
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ncpType'))

    @property
    def PadiRetries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of PADI Retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('padiRetries'))

    @property
    def PadiTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for PADI no response, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('padiTimeout'))

    @property
    def PadrRetries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of PADR Retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('padrRetries'))

    @property
    def PadrTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for PADR no response, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('padrTimeout'))

    @property
    def PapPassword(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Password when PAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('papPassword'))

    @property
    def PapUser(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User name when PAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('papUser'))

    @property
    def PonTypeTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PON Type to be advertised in PPPoE VSA Tag. For undefined PON type user has to select User-defined PON Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ponTypeTlv'))

    @property
    def RedialMax(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum number of PPPoE redials
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('redialMax'))

    @property
    def RedialTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PPPoE redial timeout, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('redialTimeout'))

    @property
    def ServiceName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Access Concentrator Service Name - this option is only available for PPP servers.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('serviceName'))

    @property
    def ServiceOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates PPPoE service retrieval mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('serviceOptions'))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[cLS_CFG_REJ_AUTH | cLS_CHAP_PEER_DET_FAIL | cLS_CHAP_PEER_RESP_BAD | cLS_CODE_REJ_IPCP | cLS_CODE_REJ_IPV6CP | cLS_CODE_REJ_LCP | cLS_ERR_PPP_NO_BUF | cLS_ERR_PPP_SEND_PKT | cLS_LINK_DISABLE | cLS_LOC_IPADDR_BROADCAST | cLS_LOC_IPADDR_CLASS_E | cLS_LOC_IPADDR_INVAL_ACKS_0 | cLS_LOC_IPADDR_INVAL_ACKS_DIFF | cLS_LOC_IPADDR_LOOPBACK | cLS_LOC_IPADDR_PEER_MATCH_LOC | cLS_LOC_IPADDR_PEER_NO_GIVE | cLS_LOC_IPADDR_PEER_NO_HELP | cLS_LOC_IPADDR_PEER_NO_TAKE | cLS_LOC_IPADDR_PEER_REJ | cLS_LOOPBACK_DETECT | cLS_NO_NCP | cLS_NONE | cLS_PAP_BAD_PASSWD | cLS_PEER_DISCONNECTED | cLS_PEER_DISCONNECTED_NEGO | cLS_PEER_IPADDR_MATCH_LOC | cLS_PEER_IPADDR_PEER_NO_SET | cLS_PPOE_AC_SYSTEM_ERROR | cLS_PPOE_GENERIC_ERROR | cLS_PPP_DISABLE | cLS_PPPOE_NO_HOST_UNIQ | cLS_PPPOE_PADI_TIMEOUT | cLS_PPPOE_PADO_TIMEOUT | cLS_PPPOE_PADR_TIMEOUT | cLS_PROTO_REJ_IPCP | cLS_PROTO_REJ_IPv6CP | cLS_TIMEOUT_CHAP_CHAL | cLS_TIMEOUT_CHAP_RESP | cLS_TIMEOUT_IPCP_CFG_REQ | cLS_TIMEOUT_IPV6CP_CFG_REQ | cLS_TIMEOUT_IPV6CP_RA | cLS_TIMEOUT_LCP_CFG_REQ | cLS_TIMEOUT_LCP_ECHO_REQ | cLS_TIMEOUT_PAP_AUTH_REQ | cLS_TUN_AUTH_FAILED | cLS_TUN_NO_RESOURCES | cLS_TUN_TIMEOUT_ICRQ | cLS_TUN_TIMEOUT_SCCRQ | cLS_TUN_VENDOR_SPECIFIC_ERR]): Logs additional information about the session state
        """
        return self._get_attribute('sessionInfo')

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute('sessionStatus')

    @property
    def StackedLayers(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute('stackedLayers')
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute('stackedLayers', value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute('stateCounts')

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute('status')

    @property
    def UnlimitedRedialAttempts(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, PPPoE unlimited redial attempts is enabled
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('unlimitedRedialAttempts'))

    @property
    def UserDefinedDslType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Defined DSL-Type Value.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('userDefinedDslType'))

    @property
    def UserDefinedPonType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Defined PON-Type Value.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('userDefinedPonType'))

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Updates pppoxclient resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Adds a new pppoxclient resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved pppoxclient resources using find and the newly added pppoxclient resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained pppoxclient resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, DiscoveredIpv4Addresses=None, DiscoveredIpv6Addresses=None, DiscoveredMacs=None, DiscoveredRemoteSessionIds=None, DiscoveredRemoteTunnelIds=None, DiscoveredSessionIds=None, DiscoveredTunnelIPs=None, DiscoveredTunnelIds=None, Errors=None, Multiplier=None, Name=None, SessionInfo=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves pppoxclient resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pppoxclient resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pppoxclient resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - DiscoveredIpv4Addresses (list(str)): The discovered IPv4 addresses.
        - DiscoveredIpv6Addresses (list(str)): The discovered IPv6 addresses.
        - DiscoveredMacs (list(str)): The discovered remote MAC address.
        - DiscoveredRemoteSessionIds (list(number)): Remote session ID.
        - DiscoveredRemoteTunnelIds (list(number)): Remote tunnel ID.
        - DiscoveredSessionIds (list(number)): The negotiated session ID.
        - DiscoveredTunnelIPs (list(str)): The discovered remote tunnel IP.
        - DiscoveredTunnelIds (list(number)): The negotiated tunnel ID.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionInfo (list(str[cLS_CFG_REJ_AUTH | cLS_CHAP_PEER_DET_FAIL | cLS_CHAP_PEER_RESP_BAD | cLS_CODE_REJ_IPCP | cLS_CODE_REJ_IPV6CP | cLS_CODE_REJ_LCP | cLS_ERR_PPP_NO_BUF | cLS_ERR_PPP_SEND_PKT | cLS_LINK_DISABLE | cLS_LOC_IPADDR_BROADCAST | cLS_LOC_IPADDR_CLASS_E | cLS_LOC_IPADDR_INVAL_ACKS_0 | cLS_LOC_IPADDR_INVAL_ACKS_DIFF | cLS_LOC_IPADDR_LOOPBACK | cLS_LOC_IPADDR_PEER_MATCH_LOC | cLS_LOC_IPADDR_PEER_NO_GIVE | cLS_LOC_IPADDR_PEER_NO_HELP | cLS_LOC_IPADDR_PEER_NO_TAKE | cLS_LOC_IPADDR_PEER_REJ | cLS_LOOPBACK_DETECT | cLS_NO_NCP | cLS_NONE | cLS_PAP_BAD_PASSWD | cLS_PEER_DISCONNECTED | cLS_PEER_DISCONNECTED_NEGO | cLS_PEER_IPADDR_MATCH_LOC | cLS_PEER_IPADDR_PEER_NO_SET | cLS_PPOE_AC_SYSTEM_ERROR | cLS_PPOE_GENERIC_ERROR | cLS_PPP_DISABLE | cLS_PPPOE_NO_HOST_UNIQ | cLS_PPPOE_PADI_TIMEOUT | cLS_PPPOE_PADO_TIMEOUT | cLS_PPPOE_PADR_TIMEOUT | cLS_PROTO_REJ_IPCP | cLS_PROTO_REJ_IPv6CP | cLS_TIMEOUT_CHAP_CHAL | cLS_TIMEOUT_CHAP_RESP | cLS_TIMEOUT_IPCP_CFG_REQ | cLS_TIMEOUT_IPV6CP_CFG_REQ | cLS_TIMEOUT_IPV6CP_RA | cLS_TIMEOUT_LCP_CFG_REQ | cLS_TIMEOUT_LCP_ECHO_REQ | cLS_TIMEOUT_PAP_AUTH_REQ | cLS_TUN_AUTH_FAILED | cLS_TUN_NO_RESOURCES | cLS_TUN_TIMEOUT_ICRQ | cLS_TUN_TIMEOUT_SCCRQ | cLS_TUN_VENDOR_SPECIFIC_ERR])): Logs additional information about the session state
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching pppoxclient resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of pppoxclient data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pppoxclient resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, AcMatchMac=None, AcMatchName=None, AcOptions=None, ActualRateDownstream=None, ActualRateUpstream=None, AgentAccessAggregationCircuitId=None, AgentCircuitId=None, AgentRemoteId=None, AuthRetries=None, AuthTimeout=None, AuthType=None, ChapName=None, ChapSecret=None, ClientDnsOptions=None, ClientLocalIp=None, ClientLocalIpv6Iid=None, ClientNcpOptions=None, ClientNetmask=None, ClientNetmaskOptions=None, ClientPrimaryDnsAddress=None, ClientSecondaryDnsAddress=None, ClientSignalIWF=None, ClientSignalLoopChar=None, ClientSignalLoopEncapsulation=None, ClientSignalLoopId=None, ClientV6NcpOptions=None, ClientWinsOptions=None, ClientWinsPrimaryAddress=None, ClientWinsSecondaryAddress=None, DataLink=None, DomainList=None, DslTypeTlv=None, EchoReqInterval=None, EnableDomainGroups=None, EnableEchoReq=None, EnableEchoRsp=None, EnableHostUniq=None, EnableMaxPayload=None, EnableRedial=None, Encaps1=None, Encaps2=None, EndpointDiscNegotiation=None, EndpointDiscriminatorClass=None, HostUniq=None, HostUniqLength=None, LcpAccm=None, LcpEnableAccm=None, LcpMaxFailure=None, LcpRetries=None, LcpStartDelay=None, LcpTermRetries=None, LcpTimeout=None, MaxPayload=None, MlpppIPAddress=None, MlpppMACAddress=None, Mrru=None, MrruNegotiation=None, MruNegotiation=None, Mtu=None, NcpRetries=None, NcpTimeout=None, NcpType=None, PadiRetries=None, PadiTimeout=None, PadrRetries=None, PadrTimeout=None, PapPassword=None, PapUser=None, PonTypeTlv=None, RedialMax=None, RedialTimeout=None, ServiceName=None, ServiceOptions=None, UnlimitedRedialAttempts=None, UserDefinedDslType=None, UserDefinedPonType=None):
        """Base class infrastructure that gets a list of pppoxclient device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AcMatchMac (str): optional regex of acMatchMac
        - AcMatchName (str): optional regex of acMatchName
        - AcOptions (str): optional regex of acOptions
        - ActualRateDownstream (str): optional regex of actualRateDownstream
        - ActualRateUpstream (str): optional regex of actualRateUpstream
        - AgentAccessAggregationCircuitId (str): optional regex of agentAccessAggregationCircuitId
        - AgentCircuitId (str): optional regex of agentCircuitId
        - AgentRemoteId (str): optional regex of agentRemoteId
        - AuthRetries (str): optional regex of authRetries
        - AuthTimeout (str): optional regex of authTimeout
        - AuthType (str): optional regex of authType
        - ChapName (str): optional regex of chapName
        - ChapSecret (str): optional regex of chapSecret
        - ClientDnsOptions (str): optional regex of clientDnsOptions
        - ClientLocalIp (str): optional regex of clientLocalIp
        - ClientLocalIpv6Iid (str): optional regex of clientLocalIpv6Iid
        - ClientNcpOptions (str): optional regex of clientNcpOptions
        - ClientNetmask (str): optional regex of clientNetmask
        - ClientNetmaskOptions (str): optional regex of clientNetmaskOptions
        - ClientPrimaryDnsAddress (str): optional regex of clientPrimaryDnsAddress
        - ClientSecondaryDnsAddress (str): optional regex of clientSecondaryDnsAddress
        - ClientSignalIWF (str): optional regex of clientSignalIWF
        - ClientSignalLoopChar (str): optional regex of clientSignalLoopChar
        - ClientSignalLoopEncapsulation (str): optional regex of clientSignalLoopEncapsulation
        - ClientSignalLoopId (str): optional regex of clientSignalLoopId
        - ClientV6NcpOptions (str): optional regex of clientV6NcpOptions
        - ClientWinsOptions (str): optional regex of clientWinsOptions
        - ClientWinsPrimaryAddress (str): optional regex of clientWinsPrimaryAddress
        - ClientWinsSecondaryAddress (str): optional regex of clientWinsSecondaryAddress
        - DataLink (str): optional regex of dataLink
        - DomainList (str): optional regex of domainList
        - DslTypeTlv (str): optional regex of dslTypeTlv
        - EchoReqInterval (str): optional regex of echoReqInterval
        - EnableDomainGroups (str): optional regex of enableDomainGroups
        - EnableEchoReq (str): optional regex of enableEchoReq
        - EnableEchoRsp (str): optional regex of enableEchoRsp
        - EnableHostUniq (str): optional regex of enableHostUniq
        - EnableMaxPayload (str): optional regex of enableMaxPayload
        - EnableRedial (str): optional regex of enableRedial
        - Encaps1 (str): optional regex of encaps1
        - Encaps2 (str): optional regex of encaps2
        - EndpointDiscNegotiation (str): optional regex of endpointDiscNegotiation
        - EndpointDiscriminatorClass (str): optional regex of endpointDiscriminatorClass
        - HostUniq (str): optional regex of hostUniq
        - HostUniqLength (str): optional regex of hostUniqLength
        - LcpAccm (str): optional regex of lcpAccm
        - LcpEnableAccm (str): optional regex of lcpEnableAccm
        - LcpMaxFailure (str): optional regex of lcpMaxFailure
        - LcpRetries (str): optional regex of lcpRetries
        - LcpStartDelay (str): optional regex of lcpStartDelay
        - LcpTermRetries (str): optional regex of lcpTermRetries
        - LcpTimeout (str): optional regex of lcpTimeout
        - MaxPayload (str): optional regex of maxPayload
        - MlpppIPAddress (str): optional regex of mlpppIPAddress
        - MlpppMACAddress (str): optional regex of mlpppMACAddress
        - Mrru (str): optional regex of mrru
        - MrruNegotiation (str): optional regex of mrruNegotiation
        - MruNegotiation (str): optional regex of mruNegotiation
        - Mtu (str): optional regex of mtu
        - NcpRetries (str): optional regex of ncpRetries
        - NcpTimeout (str): optional regex of ncpTimeout
        - NcpType (str): optional regex of ncpType
        - PadiRetries (str): optional regex of padiRetries
        - PadiTimeout (str): optional regex of padiTimeout
        - PadrRetries (str): optional regex of padrRetries
        - PadrTimeout (str): optional regex of padrTimeout
        - PapPassword (str): optional regex of papPassword
        - PapUser (str): optional regex of papUser
        - PonTypeTlv (str): optional regex of ponTypeTlv
        - RedialMax (str): optional regex of redialMax
        - RedialTimeout (str): optional regex of redialTimeout
        - ServiceName (str): optional regex of serviceName
        - ServiceOptions (str): optional regex of serviceOptions
        - UnlimitedRedialAttempts (str): optional regex of unlimitedRedialAttempts
        - UserDefinedDslType (str): optional regex of userDefinedDslType
        - UserDefinedPonType (str): optional regex of userDefinedPonType

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def CloseIpcp(self, *args, **kwargs):
        """Executes the closeIpcp operation on the server.

        Close IPCP for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        closeIpcp(SessionIndices=list)list
        ----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        closeIpcp(SessionIndices=string)list
        ------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('closeIpcp', payload=payload, response_object=None)

    def CloseIpv6cp(self, *args, **kwargs):
        """Executes the closeIpv6cp operation on the server.

        Close IPv6CP for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        closeIpv6cp(SessionIndices=list)list
        ------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        closeIpv6cp(SessionIndices=string)list
        --------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('closeIpv6cp', payload=payload, response_object=None)

    def OpenIpcp(self, *args, **kwargs):
        """Executes the openIpcp operation on the server.

        Open IPCP for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        openIpcp(SessionIndices=list)list
        ---------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        openIpcp(SessionIndices=string)list
        -----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('openIpcp', payload=payload, response_object=None)

    def OpenIpv6cp(self, *args, **kwargs):
        """Executes the openIpv6cp operation on the server.

        Open IPv6CP for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        openIpv6cp(SessionIndices=list)list
        -----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        openIpv6cp(SessionIndices=string)list
        -------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('openIpv6cp', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        restartDown(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def SendPing(self, *args, **kwargs):
        """Executes the sendPing operation on the server.

        Send Ping IPv4 for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPing(DestIp=string)list
        ---------------------------
        - DestIp (str): This parameter requires a destIp of type kString
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing(DestIp=string, SessionIndices=list)list
        ------------------------------------------------
        - DestIp (str): This parameter requires a destIp of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing(SessionIndices=string, DestIp=string)list
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a destIp of type kString
        - DestIp (str): This parameter requires a string of session numbers 1-4;6;7-12
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendPing', payload=payload, response_object=None)

    def SendPing6(self, *args, **kwargs):
        """Executes the sendPing6 operation on the server.

        Send Ping IPv6 for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPing6(DestIp=string)list
        ----------------------------
        - DestIp (str): This parameter requires a destIp of type kString
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing6(DestIp=string, SessionIndices=list)list
        -------------------------------------------------
        - DestIp (str): This parameter requires a destIp of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing6(SessionIndices=string, DestIp=string)list
        ---------------------------------------------------
        - SessionIndices (str): This parameter requires a destIp of type kString
        - DestIp (str): This parameter requires a string of session numbers 1-4;6;7-12
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendPing6', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start selected protocols.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop selected protocols.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
