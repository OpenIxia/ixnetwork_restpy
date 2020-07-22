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


class Pppoxclient(Base):
    """PPPoX Client
    The Pppoxclient class encapsulates a list of pppoxclient resources that are managed by the user.
    A list of resources can be retrieved from the server using the Pppoxclient.find() method.
    The list can be managed by using the Pppoxclient.add() and Pppoxclient.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'pppoxclient'
    _SDM_ATT_MAP = {
        'AcMatchMac': 'acMatchMac',
        'AcMatchName': 'acMatchName',
        'AcOptions': 'acOptions',
        'ActualRateDownstream': 'actualRateDownstream',
        'ActualRateUpstream': 'actualRateUpstream',
        'AgentAccessAggregationCircuitId': 'agentAccessAggregationCircuitId',
        'AgentCircuitId': 'agentCircuitId',
        'AgentRemoteId': 'agentRemoteId',
        'AuthRetries': 'authRetries',
        'AuthTimeout': 'authTimeout',
        'AuthType': 'authType',
        'ChapName': 'chapName',
        'ChapSecret': 'chapSecret',
        'ClientDnsOptions': 'clientDnsOptions',
        'ClientLocalIp': 'clientLocalIp',
        'ClientLocalIpv6Iid': 'clientLocalIpv6Iid',
        'ClientNcpOptions': 'clientNcpOptions',
        'ClientNetmask': 'clientNetmask',
        'ClientNetmaskOptions': 'clientNetmaskOptions',
        'ClientPrimaryDnsAddress': 'clientPrimaryDnsAddress',
        'ClientSecondaryDnsAddress': 'clientSecondaryDnsAddress',
        'ClientSignalIWF': 'clientSignalIWF',
        'ClientSignalLoopChar': 'clientSignalLoopChar',
        'ClientSignalLoopEncapsulation': 'clientSignalLoopEncapsulation',
        'ClientSignalLoopId': 'clientSignalLoopId',
        'ClientV6NcpOptions': 'clientV6NcpOptions',
        'ClientWinsOptions': 'clientWinsOptions',
        'ClientWinsPrimaryAddress': 'clientWinsPrimaryAddress',
        'ClientWinsSecondaryAddress': 'clientWinsSecondaryAddress',
        'ConnectSpeedUpdateEnable': 'connectSpeedUpdateEnable',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DataLink': 'dataLink',
        'DescriptiveName': 'descriptiveName',
        'DiscoveredIpv4Addresses': 'discoveredIpv4Addresses',
        'DiscoveredIpv6Addresses': 'discoveredIpv6Addresses',
        'DiscoveredMacs': 'discoveredMacs',
        'DiscoveredRemoteSessionIds': 'discoveredRemoteSessionIds',
        'DiscoveredRemoteTunnelIds': 'discoveredRemoteTunnelIds',
        'DiscoveredSessionIds': 'discoveredSessionIds',
        'DiscoveredTunnelIPs': 'discoveredTunnelIPs',
        'DiscoveredTunnelIds': 'discoveredTunnelIds',
        'DomainList': 'domainList',
        'DslTypeTlv': 'dslTypeTlv',
        'EchoReqInterval': 'echoReqInterval',
        'EnableDomainGroups': 'enableDomainGroups',
        'EnableEchoReq': 'enableEchoReq',
        'EnableEchoRsp': 'enableEchoRsp',
        'EnableHostUniq': 'enableHostUniq',
        'EnableMaxPayload': 'enableMaxPayload',
        'EnableRedial': 'enableRedial',
        'Encaps1': 'encaps1',
        'Encaps2': 'encaps2',
        'EndpointDiscNegotiation': 'endpointDiscNegotiation',
        'EndpointDiscriminatorClass': 'endpointDiscriminatorClass',
        'Errors': 'errors',
        'HostUniq': 'hostUniq',
        'HostUniqLength': 'hostUniqLength',
        'LcpAccm': 'lcpAccm',
        'LcpEnableAccm': 'lcpEnableAccm',
        'LcpMaxFailure': 'lcpMaxFailure',
        'LcpRetries': 'lcpRetries',
        'LcpStartDelay': 'lcpStartDelay',
        'LcpTermRetries': 'lcpTermRetries',
        'LcpTimeout': 'lcpTimeout',
        'MaxPayload': 'maxPayload',
        'MlpppIPAddress': 'mlpppIPAddress',
        'MlpppMACAddress': 'mlpppMACAddress',
        'Mrru': 'mrru',
        'MrruNegotiation': 'mrruNegotiation',
        'MruNegotiation': 'mruNegotiation',
        'Mtu': 'mtu',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NcpRetries': 'ncpRetries',
        'NcpTimeout': 'ncpTimeout',
        'NcpType': 'ncpType',
        'PadiRetries': 'padiRetries',
        'PadiTimeout': 'padiTimeout',
        'PadrRetries': 'padrRetries',
        'PadrTimeout': 'padrTimeout',
        'PapPassword': 'papPassword',
        'PapUser': 'papUser',
        'PonTypeTlv': 'ponTypeTlv',
        'RedialMax': 'redialMax',
        'RedialTimeout': 'redialTimeout',
        'RxConnectSpeed': 'rxConnectSpeed',
        'ServiceName': 'serviceName',
        'ServiceOptions': 'serviceOptions',
        'SessionInfo': 'sessionInfo',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TxConnectSpeed': 'txConnectSpeed',
        'UnlimitedRedialAttempts': 'unlimitedRedialAttempts',
        'UserDefinedDslType': 'userDefinedDslType',
        'UserDefinedPonType': 'userDefinedPonType',
    }

    def __init__(self, parent):
        super(Pppoxclient, self).__init__(parent)

    @property
    def Bfdv4Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface_91b557a3f744baf442dbe21ac75e8f2e.Bfdv4Interface): An instance of the Bfdv4Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface_91b557a3f744baf442dbe21ac75e8f2e import Bfdv4Interface
        return Bfdv4Interface(self)

    @property
    def Bfdv6Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface_b9a91920db1b70c8c6410d2de0b438d3.Bfdv6Interface): An instance of the Bfdv6Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface_b9a91920db1b70c8c6410d2de0b438d3 import Bfdv6Interface
        return Bfdv6Interface(self)

    @property
    def BgpIpv4Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer_9dd9eddcf2bd784d82d8a016e392f035.BgpIpv4Peer): An instance of the BgpIpv4Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer_9dd9eddcf2bd784d82d8a016e392f035 import BgpIpv4Peer
        return BgpIpv4Peer(self)

    @property
    def BgpIpv6Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer_d4ac277d9da759fd5a152b8e6eb0ab20.BgpIpv6Peer): An instance of the BgpIpv6Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer_d4ac277d9da759fd5a152b8e6eb0ab20 import BgpIpv6Peer
        return BgpIpv6Peer(self)

    @property
    def Connector(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b.Connector): An instance of the Connector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b import Connector
        return Connector(self)

    @property
    def Dhcpv6client(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6client_355391ba11ab3c1555c827e2e4ac3c4c.Dhcpv6client): An instance of the Dhcpv6client class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6client_355391ba11ab3c1555c827e2e4ac3c4c import Dhcpv6client
        return Dhcpv6client(self)

    @property
    def ECpriRe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprire_51f1030cbafd2e567d3b517032a1b011.ECpriRe): An instance of the ECpriRe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprire_51f1030cbafd2e567d3b517032a1b011 import ECpriRe
        return ECpriRe(self)

    @property
    def ECpriRec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirec_129f1d43f285a4f806ade4e0df814255.ECpriRec): An instance of the ECpriRec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirec_129f1d43f285a4f806ade4e0df814255 import ECpriRec
        return ECpriRec(self)

    @property
    def Geneve(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve_14ab6f140956b4fc77d1d0f03c5e7514.Geneve): An instance of the Geneve class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve_14ab6f140956b4fc77d1d0f03c5e7514 import Geneve
        return Geneve(self)

    @property
    def IgmpHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost_8940887674c0387469423e8df3a33854.IgmpHost): An instance of the IgmpHost class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost_8940887674c0387469423e8df3a33854 import IgmpHost
        return IgmpHost(self)

    @property
    def IgmpQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier_38c883b0cec7ffb5405af90bf1b8cda5.IgmpQuerier): An instance of the IgmpQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier_38c883b0cec7ffb5405af90bf1b8cda5 import IgmpQuerier
        return IgmpQuerier(self)

    @property
    def MldHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost_824a1bed927138d4bb32f7d2631197a5.MldHost): An instance of the MldHost class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost_824a1bed927138d4bb32f7d2631197a5 import MldHost
        return MldHost(self)

    @property
    def MldQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier_e20671d730d138d65036e88d7cad63ac.MldQuerier): An instance of the MldQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier_e20671d730d138d65036e88d7cad63ac import MldQuerier
        return MldQuerier(self)

    @property
    def MplsOam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam_e01bb6affe899a4731aa60619f4aeadc.MplsOam): An instance of the MplsOam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam_e01bb6affe899a4731aa60619f4aeadc import MplsOam
        return MplsOam(self)

    @property
    def NetconfClient(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient_1eaa2ab0efacd988796bdc1f5fe4291c.NetconfClient): An instance of the NetconfClient class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient_1eaa2ab0efacd988796bdc1f5fe4291c import NetconfClient
        return NetconfClient(self)

    @property
    def NetconfServer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver_ad256f8ca38068f1eaff839ed40b1e30.NetconfServer): An instance of the NetconfServer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver_ad256f8ca38068f1eaff839ed40b1e30 import NetconfServer
        return NetconfServer(self)

    @property
    def Ospfv2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2_27b7a27a991a50e01e629b9de482a2f0.Ospfv2): An instance of the Ospfv2 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2_27b7a27a991a50e01e629b9de482a2f0 import Ospfv2
        return Ospfv2(self)

    @property
    def Ospfv3(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3_c029fd7cd4a9e9897b7b4e4547458751.Ospfv3): An instance of the Ospfv3 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3_c029fd7cd4a9e9897b7b4e4547458751 import Ospfv3
        return Ospfv3(self)

    @property
    def Pcc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc_9346785b55d17399fecd6fe36c418219.Pcc): An instance of the Pcc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc_9346785b55d17399fecd6fe36c418219 import Pcc
        return Pcc(self)

    @property
    def Pce(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce_bd5f6a11078a4f0deb5d56bef8e9674f.Pce): An instance of the Pce class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce_bd5f6a11078a4f0deb5d56bef8e9674f import Pce
        return Pce(self)

    @property
    def PimV4Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface_92603cbceaf153039f7575ed9bc4aa67.PimV4Interface): An instance of the PimV4Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface_92603cbceaf153039f7575ed9bc4aa67 import PimV4Interface
        return PimV4Interface(self)

    @property
    def PimV6Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface_74a3aa08a315ca50732e853e3e8cdc43.PimV6Interface): An instance of the PimV6Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface_74a3aa08a315ca50732e853e3e8cdc43 import PimV6Interface
        return PimV6Interface(self)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        return Tag(self)

    @property
    def TlvProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_69db000d3ef3b060f5edc387b878736c.TlvProfile): An instance of the TlvProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_69db000d3ef3b060f5edc387b878736c import TlvProfile
        return TlvProfile(self)

    @property
    def Vxlan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan_ed3df6fe7146492fc5fe0f77f53f9473.Vxlan): An instance of the Vxlan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan_ed3df6fe7146492fc5fe0f77f53f9473 import Vxlan
        return Vxlan(self)

    @property
    def Vxlanv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanv6_c18187deccae3db44b9e9de30ad538ec.Vxlanv6): An instance of the Vxlanv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanv6_c18187deccae3db44b9e9de30ad538ec import Vxlanv6
        return Vxlanv6(self)

    @property
    def AcMatchMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ?
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AcMatchMac']))

    @property
    def AcMatchName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ?
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AcMatchName']))

    @property
    def AcOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates PPPoE AC retrieval mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AcOptions']))

    @property
    def ActualRateDownstream(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter specifies the value to be included in the vendor specific PPPoE tag. It is the actual downstream data rate (sub-option 0x81), in kbps.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActualRateDownstream']))

    @property
    def ActualRateUpstream(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter specifies the value to be included in the vendor specific PPPoE tag. It is the actual upstream data rate (sub-option 0x82), in kbps.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActualRateUpstream']))

    @property
    def AgentAccessAggregationCircuitId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value to be inserted into the Agent Access-Aggregation-Circuit-ID-ASCII-Value field of the PPPoX tag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AgentAccessAggregationCircuitId']))

    @property
    def AgentCircuitId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value to be inserted into the Agent Circuit ID field of the PPPoX tag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AgentCircuitId']))

    @property
    def AgentRemoteId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value to be inserted into the Agent Remote ID field of the PPPoX tag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AgentRemoteId']))

    @property
    def AuthRetries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of PPP authentication retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuthRetries']))

    @property
    def AuthTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for PPP authentication, in seconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuthTimeout']))

    @property
    def AuthType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The authentication type to use during link setup.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuthType']))

    @property
    def ChapName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User name when CHAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ChapName']))

    @property
    def ChapSecret(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Secret when CHAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ChapSecret']))

    @property
    def ClientDnsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The client DNS options.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientDnsOptions']))

    @property
    def ClientLocalIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The requested IPv4 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientLocalIp']))

    @property
    def ClientLocalIpv6Iid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The requested IPv6 Interface Identifier (IID).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientLocalIpv6Iid']))

    @property
    def ClientNcpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The NCP configuration mode for IPv4 addressing.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientNcpOptions']))

    @property
    def ClientNetmask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The netmask that the client will use with the assigned IP address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientNetmask']))

    @property
    def ClientNetmaskOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The client netmask option.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientNetmaskOptions']))

    @property
    def ClientPrimaryDnsAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the primary DNS server address that the client requests from the server when the value of the Client DNS Options field is set to 'Request Primary only' or 'Request Primary and Secondary'.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientPrimaryDnsAddress']))

    @property
    def ClientSecondaryDnsAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the secondary DNS server address that the client requests from the server when the value of the Client DNS Options field is set to 'Request Primary and Secondary'.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientSecondaryDnsAddress']))

    @property
    def ClientSignalIWF(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-option 0xFE (signaling of interworked sessions) into the DSL tag in PADI and PADR packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientSignalIWF']))

    @property
    def ClientSignalLoopChar(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-options 0x81 and 0x82 into the DSL tag in PADI and PADR packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientSignalLoopChar']))

    @property
    def ClientSignalLoopEncapsulation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-option 0x90 into the DSL tag in PADI and PADR packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientSignalLoopEncapsulation']))

    @property
    def ClientSignalLoopId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-options 0x01 , 0x02, 0x03 (Remote ID,Circuit ID and Access Aggregation Circuit ID) into the DSL tag in PADI and PADR packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientSignalLoopId']))

    @property
    def ClientV6NcpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The NCP configuration mode for IPv6 addressing.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientV6NcpOptions']))

    @property
    def ClientWinsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the mode in which WINS host addresses are configured.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientWinsOptions']))

    @property
    def ClientWinsPrimaryAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the primary WINS address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientWinsPrimaryAddress']))

    @property
    def ClientWinsSecondaryAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the secondary WINS address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientWinsSecondaryAddress']))

    @property
    def ConnectSpeedUpdateEnable(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, LAC will send Connect Speed Update Enable AVP in ICRQ control message
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConnectSpeedUpdateEnable']))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer used to connect to the wire
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DataLink(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A one-byte field included with sub-option 0x90.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DataLink']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DiscoveredIpv4Addresses(self):
        """
        Returns
        -------
        - list(str): The discovered IPv4 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveredIpv4Addresses'])

    @property
    def DiscoveredIpv6Addresses(self):
        """
        Returns
        -------
        - list(str): The discovered IPv6 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveredIpv6Addresses'])

    @property
    def DiscoveredMacs(self):
        """
        Returns
        -------
        - list(str): The discovered remote MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveredMacs'])

    @property
    def DiscoveredRemoteSessionIds(self):
        """
        Returns
        -------
        - list(number): Remote session ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveredRemoteSessionIds'])

    @property
    def DiscoveredRemoteTunnelIds(self):
        """
        Returns
        -------
        - list(number): Remote tunnel ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveredRemoteTunnelIds'])

    @property
    def DiscoveredSessionIds(self):
        """
        Returns
        -------
        - list(number): The negotiated session ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveredSessionIds'])

    @property
    def DiscoveredTunnelIPs(self):
        """
        Returns
        -------
        - list(str): The discovered remote tunnel IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveredTunnelIPs'])

    @property
    def DiscoveredTunnelIds(self):
        """
        Returns
        -------
        - list(number): The negotiated tunnel ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveredTunnelIds'])

    @property
    def DomainList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure domain group settings
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DomainList']))

    @property
    def DslTypeTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DSL Type to be advertised in PPPoE VSA Tag. For undefined DSL type user has to select User-defined DSL Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DslTypeTlv']))

    @property
    def EchoReqInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Keep alive interval, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EchoReqInterval']))

    @property
    def EnableDomainGroups(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable domain groups
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableDomainGroups']))

    @property
    def EnableEchoReq(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ?
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableEchoReq']))

    @property
    def EnableEchoRsp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ?
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableEchoRsp']))

    @property
    def EnableHostUniq(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables PPPoE Host-Uniq tag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableHostUniq']))

    @property
    def EnableMaxPayload(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables PPPoE Max Payload tag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableMaxPayload']))

    @property
    def EnableRedial(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, PPPoE redial is enabled
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRedial']))

    @property
    def Encaps1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A one-byte field included with sub-option 0x90.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Encaps1']))

    @property
    def Encaps2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A one-byte field included with sub-option 0x90.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Encaps2']))

    @property
    def EndpointDiscNegotiation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Endpoint Discriminator Negotiation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EndpointDiscNegotiation']))

    @property
    def EndpointDiscriminatorClass(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Endpoint Discriminator for PPP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EndpointDiscriminatorClass']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def HostUniq(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates Host-Uniq Tag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HostUniq']))

    @property
    def HostUniqLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Host-Uniq Length, in bytes
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HostUniqLength']))

    @property
    def LcpAccm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Async-Control-Character-Map
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LcpAccm']))

    @property
    def LcpEnableAccm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Async-Control-Character-Map
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LcpEnableAccm']))

    @property
    def LcpMaxFailure(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of Configure-Nak packets sent without sending a Configure-Ack before assuming that configuration is not converging. Any further Configure-Nak packets for peer requested options are converted to Configure-Reject packets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LcpMaxFailure']))

    @property
    def LcpRetries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of LCP retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LcpRetries']))

    @property
    def LcpStartDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay time in milliseconds to wait before sending LCP Config Request packet
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LcpStartDelay']))

    @property
    def LcpTermRetries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of LCP Termination Retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LcpTermRetries']))

    @property
    def LcpTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for LCP phase, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LcpTimeout']))

    @property
    def MaxPayload(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max Payload
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxPayload']))

    @property
    def MlpppIPAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The IP address used in the ML-PPP endpoint discriminator option of the LCP configure request sent by PPP clients
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MlpppIPAddress']))

    @property
    def MlpppMACAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The MAC addresses are automatically derived from the local MAC address. An address in this class contains an IEEE 802.1 MAC address is canonical (802.3) format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MlpppMACAddress']))

    @property
    def Mrru(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max Receive Reconstructed Unit for PPP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Mrru']))

    @property
    def MrruNegotiation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MRRU Negotiation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MrruNegotiation']))

    @property
    def MruNegotiation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MRU Negotiation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MruNegotiation']))

    @property
    def Mtu(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max Transmit Unit for PPP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Mtu']))

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NcpRetries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of NCP retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NcpRetries']))

    @property
    def NcpTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for NCP phase, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NcpTimeout']))

    @property
    def NcpType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP address type (IPv4 or IPv6) for Network Control Protocol
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NcpType']))

    @property
    def PadiRetries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of PADI Retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PadiRetries']))

    @property
    def PadiTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for PADI no response, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PadiTimeout']))

    @property
    def PadrRetries(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of PADR Retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PadrRetries']))

    @property
    def PadrTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for PADR no response, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PadrTimeout']))

    @property
    def PapPassword(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Password when PAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PapPassword']))

    @property
    def PapUser(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User name when PAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PapUser']))

    @property
    def PonTypeTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PON Type to be advertised in PPPoE VSA Tag. For undefined PON type user has to select User-defined PON Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PonTypeTlv']))

    @property
    def RedialMax(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum number of PPPoE redials
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RedialMax']))

    @property
    def RedialTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PPPoE redial timeout, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RedialTimeout']))

    @property
    def RxConnectSpeed(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Rx Connection Speed
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RxConnectSpeed']))

    @property
    def ServiceName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Access Concentrator Service Name - this option is only available for PPP servers.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ServiceName']))

    @property
    def ServiceOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates PPPoE service retrieval mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ServiceOptions']))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[cLS_CFG_REJ_AUTH | cLS_CHAP_PEER_DET_FAIL | cLS_CHAP_PEER_RESP_BAD | cLS_CODE_REJ_IPCP | cLS_CODE_REJ_IPV6CP | cLS_CODE_REJ_LCP | cLS_ERR_PPP_NO_BUF | cLS_ERR_PPP_SEND_PKT | cLS_LINK_DISABLE | cLS_LOC_IPADDR_BROADCAST | cLS_LOC_IPADDR_CLASS_E | cLS_LOC_IPADDR_INVAL_ACKS_0 | cLS_LOC_IPADDR_INVAL_ACKS_DIFF | cLS_LOC_IPADDR_LOOPBACK | cLS_LOC_IPADDR_PEER_MATCH_LOC | cLS_LOC_IPADDR_PEER_NO_GIVE | cLS_LOC_IPADDR_PEER_NO_HELP | cLS_LOC_IPADDR_PEER_NO_TAKE | cLS_LOC_IPADDR_PEER_REJ | cLS_LOOPBACK_DETECT | cLS_NO_NCP | cLS_NONE | cLS_PAP_BAD_PASSWD | cLS_PEER_DISCONNECTED | cLS_PEER_DISCONNECTED_NEGO | cLS_PEER_IPADDR_MATCH_LOC | cLS_PEER_IPADDR_PEER_NO_SET | cLS_PPOE_AC_SYSTEM_ERROR | cLS_PPOE_GENERIC_ERROR | cLS_PPP_DISABLE | cLS_PPPOE_NO_HOST_UNIQ | cLS_PPPOE_PADI_TIMEOUT | cLS_PPPOE_PADO_TIMEOUT | cLS_PPPOE_PADR_TIMEOUT | cLS_PROTO_REJ_IPCP | cLS_PROTO_REJ_IPv6CP | cLS_TIMEOUT_CHAP_CHAL | cLS_TIMEOUT_CHAP_RESP | cLS_TIMEOUT_IPCP_CFG_REQ | cLS_TIMEOUT_IPV6CP_CFG_REQ | cLS_TIMEOUT_IPV6CP_RA | cLS_TIMEOUT_LCP_CFG_REQ | cLS_TIMEOUT_LCP_ECHO_REQ | cLS_TIMEOUT_PAP_AUTH_REQ | cLS_TUN_AUTH_FAILED | cLS_TUN_NO_RESOURCES | cLS_TUN_TIMEOUT_ICRQ | cLS_TUN_TIMEOUT_SCCRQ | cLS_TUN_VENDOR_SPECIFIC_ERR]): Logs additional information about the session state
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def StackedLayers(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StackedLayers'], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateCounts'])

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def TxConnectSpeed(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tx Connection Speed
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TxConnectSpeed']))

    @property
    def UnlimitedRedialAttempts(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, PPPoE unlimited redial attempts is enabled
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UnlimitedRedialAttempts']))

    @property
    def UserDefinedDslType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Defined DSL-Type Value.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UserDefinedDslType']))

    @property
    def UserDefinedPonType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Defined PON-Type Value.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UserDefinedPonType']))

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
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

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
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

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
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

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

    def get_device_ids(self, PortNames=None, AcMatchMac=None, AcMatchName=None, AcOptions=None, ActualRateDownstream=None, ActualRateUpstream=None, AgentAccessAggregationCircuitId=None, AgentCircuitId=None, AgentRemoteId=None, AuthRetries=None, AuthTimeout=None, AuthType=None, ChapName=None, ChapSecret=None, ClientDnsOptions=None, ClientLocalIp=None, ClientLocalIpv6Iid=None, ClientNcpOptions=None, ClientNetmask=None, ClientNetmaskOptions=None, ClientPrimaryDnsAddress=None, ClientSecondaryDnsAddress=None, ClientSignalIWF=None, ClientSignalLoopChar=None, ClientSignalLoopEncapsulation=None, ClientSignalLoopId=None, ClientV6NcpOptions=None, ClientWinsOptions=None, ClientWinsPrimaryAddress=None, ClientWinsSecondaryAddress=None, ConnectSpeedUpdateEnable=None, DataLink=None, DomainList=None, DslTypeTlv=None, EchoReqInterval=None, EnableDomainGroups=None, EnableEchoReq=None, EnableEchoRsp=None, EnableHostUniq=None, EnableMaxPayload=None, EnableRedial=None, Encaps1=None, Encaps2=None, EndpointDiscNegotiation=None, EndpointDiscriminatorClass=None, HostUniq=None, HostUniqLength=None, LcpAccm=None, LcpEnableAccm=None, LcpMaxFailure=None, LcpRetries=None, LcpStartDelay=None, LcpTermRetries=None, LcpTimeout=None, MaxPayload=None, MlpppIPAddress=None, MlpppMACAddress=None, Mrru=None, MrruNegotiation=None, MruNegotiation=None, Mtu=None, NcpRetries=None, NcpTimeout=None, NcpType=None, PadiRetries=None, PadiTimeout=None, PadrRetries=None, PadrTimeout=None, PapPassword=None, PapUser=None, PonTypeTlv=None, RedialMax=None, RedialTimeout=None, RxConnectSpeed=None, ServiceName=None, ServiceOptions=None, TxConnectSpeed=None, UnlimitedRedialAttempts=None, UserDefinedDslType=None, UserDefinedPonType=None):
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
        - ConnectSpeedUpdateEnable (str): optional regex of connectSpeedUpdateEnable
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
        - RxConnectSpeed (str): optional regex of rxConnectSpeed
        - ServiceName (str): optional regex of serviceName
        - ServiceOptions (str): optional regex of serviceOptions
        - TxConnectSpeed (str): optional regex of txConnectSpeed
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

    def Abort(self, *args, **kwargs):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        abort(SessionIndices=string)
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
        return self._execute('abort', payload=payload, response_object=None)

    def CloseIpcp(self, *args, **kwargs):
        """Executes the closeIpcp operation on the server.

        Close IPCP for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        closeIpcp(SessionIndices=list)list
        ----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
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
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
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
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
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
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
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
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

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
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
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
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
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

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

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

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

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
