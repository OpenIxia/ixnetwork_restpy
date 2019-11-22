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


class PppoxRange(Base):
    """The PPP range class
    The PppoxRange class encapsulates a required pppoxRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'pppoxRange'

    def __init__(self, parent):
        super(PppoxRange, self).__init__(parent)

    @property
    def AcMac(self):
        """An instance of the AcMac class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.acmac_8e50169c78fa5a093fe398d8158a8ef0.AcMac)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.acmac_8e50169c78fa5a093fe398d8158a8ef0 import AcMac
        return AcMac(self)

    @property
    def AcName(self):
        """An instance of the AcName class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.acname_e6d0f33ce888fc287ef0d3fc7be325da.AcName)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.acname_e6d0f33ce888fc287ef0d3fc7be325da import AcName
        return AcName(self)

    @property
    def DomainGroup(self):
        """An instance of the DomainGroup class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.domaingroup_fb34cac83d1e1ce75a73d5c58208e8a6.DomainGroup)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.domaingroup_fb34cac83d1e1ce75a73d5c58208e8a6 import DomainGroup
        return DomainGroup(self)

    @property
    def AcName(self):
        """Access Concentrator Name - this option is only available for PPP servers.

        Returns:
            str
        """
        return self._get_attribute('acName')
    @AcName.setter
    def AcName(self, value):
        self._set_attribute('acName', value)

    @property
    def AcOptions(self):
        """Indicates PPPoE AC retrieval mode

        Returns:
            str
        """
        return self._get_attribute('acOptions')
    @AcOptions.setter
    def AcOptions(self, value):
        self._set_attribute('acOptions', value)

    @property
    def ActualRateDownstream(self):
        """Actual Data Rate Downstream Value (TR-101 suboption 0x82)

        Returns:
            number
        """
        return self._get_attribute('actualRateDownstream')
    @ActualRateDownstream.setter
    def ActualRateDownstream(self, value):
        self._set_attribute('actualRateDownstream', value)

    @property
    def ActualRateUpstream(self):
        """Actual Data Rate Upstream Value (TR-101 suboption 0x81)

        Returns:
            number
        """
        return self._get_attribute('actualRateUpstream')
    @ActualRateUpstream.setter
    def ActualRateUpstream(self, value):
        self._set_attribute('actualRateUpstream', value)

    @property
    def AgentCircuitId(self):
        """Agent Circuit ID (TR-101 suboption 0x01)

        Returns:
            str
        """
        return self._get_attribute('agentCircuitId')
    @AgentCircuitId.setter
    def AgentCircuitId(self, value):
        self._set_attribute('agentCircuitId', value)

    @property
    def AgentRemoteId(self):
        """Agent Remote ID (TR-101 suboption 0x02)

        Returns:
            str
        """
        return self._get_attribute('agentRemoteId')
    @AgentRemoteId.setter
    def AgentRemoteId(self, value):
        self._set_attribute('agentRemoteId', value)

    @property
    def AuthOptions(self):
        """For GUI grouping.

        Returns:
            str
        """
        return self._get_attribute('authOptions')
    @AuthOptions.setter
    def AuthOptions(self, value):
        self._set_attribute('authOptions', value)

    @property
    def AuthRetries(self):
        """Number of PPP authentication retries

        Returns:
            number
        """
        return self._get_attribute('authRetries')
    @AuthRetries.setter
    def AuthRetries(self, value):
        self._set_attribute('authRetries', value)

    @property
    def AuthTimeout(self):
        """Timeout for PPP authentication, in seconds.

        Returns:
            number
        """
        return self._get_attribute('authTimeout')
    @AuthTimeout.setter
    def AuthTimeout(self, value):
        self._set_attribute('authTimeout', value)

    @property
    def AuthType(self):
        """Authentication type

        Returns:
            str
        """
        return self._get_attribute('authType')
    @AuthType.setter
    def AuthType(self, value):
        self._set_attribute('authType', value)

    @property
    def ChapName(self):
        """User name when CHAP Authentication is being used

        Returns:
            str
        """
        return self._get_attribute('chapName')
    @ChapName.setter
    def ChapName(self, value):
        self._set_attribute('chapName', value)

    @property
    def ChapSecret(self):
        """Secret when CHAP Authentication is being used

        Returns:
            str
        """
        return self._get_attribute('chapSecret')
    @ChapSecret.setter
    def ChapSecret(self, value):
        self._set_attribute('chapSecret', value)

    @property
    def ClientBaseIid(self):
        """Base for IPv6CP interface identifiers assigned to clients.

        Returns:
            str
        """
        return self._get_attribute('clientBaseIid')
    @ClientBaseIid.setter
    def ClientBaseIid(self, value):
        self._set_attribute('clientBaseIid', value)

    @property
    def ClientBaseIp(self):
        """Base for IPv4 PPP client address creation

        Returns:
            str
        """
        return self._get_attribute('clientBaseIp')
    @ClientBaseIp.setter
    def ClientBaseIp(self, value):
        self._set_attribute('clientBaseIp', value)

    @property
    def ClientDnsOptions(self):
        """Client DNS options

        Returns:
            str
        """
        return self._get_attribute('clientDnsOptions')
    @ClientDnsOptions.setter
    def ClientDnsOptions(self, value):
        self._set_attribute('clientDnsOptions', value)

    @property
    def ClientIidIncr(self):
        """Increment for IPv6CP client interface identifiers.

        Returns:
            number
        """
        return self._get_attribute('clientIidIncr')
    @ClientIidIncr.setter
    def ClientIidIncr(self, value):
        self._set_attribute('clientIidIncr', value)

    @property
    def ClientIpIncr(self):
        """Incrementor for IPv4 PPP client address creation

        Returns:
            str
        """
        return self._get_attribute('clientIpIncr')
    @ClientIpIncr.setter
    def ClientIpIncr(self, value):
        self._set_attribute('clientIpIncr', value)

    @property
    def ClientNetmask(self):
        """Netmask that the client should request

        Returns:
            str
        """
        return self._get_attribute('clientNetmask')
    @ClientNetmask.setter
    def ClientNetmask(self, value):
        self._set_attribute('clientNetmask', value)

    @property
    def ClientNetmaskOptions(self):
        """Client netmask options

        Returns:
            str
        """
        return self._get_attribute('clientNetmaskOptions')
    @ClientNetmaskOptions.setter
    def ClientNetmaskOptions(self, value):
        self._set_attribute('clientNetmaskOptions', value)

    @property
    def ClientPrimaryDnsAddress(self):
        """Primary DNS server address requested by client

        Returns:
            str
        """
        return self._get_attribute('clientPrimaryDnsAddress')
    @ClientPrimaryDnsAddress.setter
    def ClientPrimaryDnsAddress(self, value):
        self._set_attribute('clientPrimaryDnsAddress', value)

    @property
    def ClientSecondaryDnsAddress(self):
        """Secondary DNS server address requested by client

        Returns:
            str
        """
        return self._get_attribute('clientSecondaryDnsAddress')
    @ClientSecondaryDnsAddress.setter
    def ClientSecondaryDnsAddress(self, value):
        self._set_attribute('clientSecondaryDnsAddress', value)

    @property
    def ClientSignalIwf(self):
        """Enables the sending of the interworked session (0xFE) TR-101 suboption in client PPPoE messages (PADI/PADR/PADT)

        Returns:
            bool
        """
        return self._get_attribute('clientSignalIwf')
    @ClientSignalIwf.setter
    def ClientSignalIwf(self, value):
        self._set_attribute('clientSignalIwf', value)

    @property
    def ClientSignalLoopChar(self):
        """Enables the sending of the access loop characteristics TR-101 suboptions in client PPPoE messages (PADI/PADR/PADT)

        Returns:
            bool
        """
        return self._get_attribute('clientSignalLoopChar')
    @ClientSignalLoopChar.setter
    def ClientSignalLoopChar(self, value):
        self._set_attribute('clientSignalLoopChar', value)

    @property
    def ClientSignalLoopEncapsulation(self):
        """Enables the sending of the loop encapsulation (0x90) TR-101 suboption in client PPPoE messages (PADI/PADR/PADT)

        Returns:
            bool
        """
        return self._get_attribute('clientSignalLoopEncapsulation')
    @ClientSignalLoopEncapsulation.setter
    def ClientSignalLoopEncapsulation(self, value):
        self._set_attribute('clientSignalLoopEncapsulation', value)

    @property
    def ClientSignalLoopId(self):
        """Enables the sending of the remote ID and circuit ID TR-101 suboptions in client PPPoE messages (PADI/PADR/PADT)

        Returns:
            bool
        """
        return self._get_attribute('clientSignalLoopId')
    @ClientSignalLoopId.setter
    def ClientSignalLoopId(self, value):
        self._set_attribute('clientSignalLoopId', value)

    @property
    def DataLink(self):
        """Data Link for TR-101 suboption 0x90

        Returns:
            str
        """
        return self._get_attribute('dataLink')
    @DataLink.setter
    def DataLink(self, value):
        self._set_attribute('dataLink', value)

    @property
    def DnsServerList(self):
        """DNS server list separacted by semicolon

        Returns:
            str
        """
        return self._get_attribute('dnsServerList')
    @DnsServerList.setter
    def DnsServerList(self, value):
        self._set_attribute('dnsServerList', value)

    @property
    def DomainList(self):
        """Configure domain group settings

        Returns:
            str
        """
        return self._get_attribute('domainList')
    @DomainList.setter
    def DomainList(self, value):
        self._set_attribute('domainList', value)

    @property
    def EchoReqInterval(self):
        """Keep alive interval

        Returns:
            number
        """
        return self._get_attribute('echoReqInterval')
    @EchoReqInterval.setter
    def EchoReqInterval(self, value):
        self._set_attribute('echoReqInterval', value)

    @property
    def EnableDnsRa(self):
        """Enable RDNSS routing advertisments

        Returns:
            bool
        """
        return self._get_attribute('enableDnsRa')
    @EnableDnsRa.setter
    def EnableDnsRa(self, value):
        self._set_attribute('enableDnsRa', value)

    @property
    def EnableDomainGroups(self):
        """Enable domain groups

        Returns:
            bool
        """
        return self._get_attribute('enableDomainGroups')
    @EnableDomainGroups.setter
    def EnableDomainGroups(self, value):
        self._set_attribute('enableDomainGroups', value)

    @property
    def EnableEchoReq(self):
        """Enable Echo requests

        Returns:
            bool
        """
        return self._get_attribute('enableEchoReq')
    @EnableEchoReq.setter
    def EnableEchoReq(self, value):
        self._set_attribute('enableEchoReq', value)

    @property
    def EnableEchoRsp(self):
        """Enable Echo replies

        Returns:
            bool
        """
        return self._get_attribute('enableEchoRsp')
    @EnableEchoRsp.setter
    def EnableEchoRsp(self, value):
        self._set_attribute('enableEchoRsp', value)

    @property
    def EnableIncludeTagInPadi(self):
        """DEPRECATED OBSOLETE - If checked, PADI messages include Intermediate Agent Tags(only for PPP client)

        Returns:
            bool
        """
        return self._get_attribute('enableIncludeTagInPadi')
    @EnableIncludeTagInPadi.setter
    def EnableIncludeTagInPadi(self, value):
        self._set_attribute('enableIncludeTagInPadi', value)

    @property
    def EnableIncludeTagInPado(self):
        """DEPRECATED OBSOLETE - If checked, PADO messages include Intermediate Agent Tags(only for PPP server)

        Returns:
            bool
        """
        return self._get_attribute('enableIncludeTagInPado')
    @EnableIncludeTagInPado.setter
    def EnableIncludeTagInPado(self, value):
        self._set_attribute('enableIncludeTagInPado', value)

    @property
    def EnableIncludeTagInPadr(self):
        """DEPRECATED OBSOLETE - If checked, PADR messages include Intermediate Agent Tags(only for PPP client)

        Returns:
            bool
        """
        return self._get_attribute('enableIncludeTagInPadr')
    @EnableIncludeTagInPadr.setter
    def EnableIncludeTagInPadr(self, value):
        self._set_attribute('enableIncludeTagInPadr', value)

    @property
    def EnableIncludeTagInPads(self):
        """DEPRECATED OBSOLETE - If checked, PADs messages include Intermediate Agent Tags(only for PPP server)

        Returns:
            bool
        """
        return self._get_attribute('enableIncludeTagInPads')
    @EnableIncludeTagInPads.setter
    def EnableIncludeTagInPads(self, value):
        self._set_attribute('enableIncludeTagInPads', value)

    @property
    def EnableIntermediateAgentTags(self):
        """DEPRECATED OBSOLETE - If checked, Intermediate Agent Tags are enabled

        Returns:
            bool
        """
        return self._get_attribute('enableIntermediateAgentTags')
    @EnableIntermediateAgentTags.setter
    def EnableIntermediateAgentTags(self, value):
        self._set_attribute('enableIntermediateAgentTags', value)

    @property
    def EnableMaxPayload(self):
        """Enable/Disable Max Payload

        Returns:
            bool
        """
        return self._get_attribute('enableMaxPayload')
    @EnableMaxPayload.setter
    def EnableMaxPayload(self, value):
        self._set_attribute('enableMaxPayload', value)

    @property
    def EnableMru(self):
        """Enable/Disable MRU negotiation

        Returns:
            bool
        """
        return self._get_attribute('enableMru')
    @EnableMru.setter
    def EnableMru(self, value):
        self._set_attribute('enableMru', value)

    @property
    def EnableMruNegotiation(self):
        """DEPRECATED Option is deprecated. Please use enableMaxPayload. If checked, MRU negotiation is enabled

        Returns:
            bool
        """
        return self._get_attribute('enableMruNegotiation')
    @EnableMruNegotiation.setter
    def EnableMruNegotiation(self, value):
        self._set_attribute('enableMruNegotiation', value)

    @property
    def EnablePasswordCheck(self):
        """Enable authentication credential checking on the port.

        Returns:
            bool
        """
        return self._get_attribute('enablePasswordCheck')
    @EnablePasswordCheck.setter
    def EnablePasswordCheck(self, value):
        self._set_attribute('enablePasswordCheck', value)

    @property
    def EnableRedial(self):
        """Enable/Disable PPPoE redial

        Returns:
            bool
        """
        return self._get_attribute('enableRedial')
    @EnableRedial.setter
    def EnableRedial(self, value):
        self._set_attribute('enableRedial', value)

    @property
    def Enabled(self):
        """Disabled ranges won't be configured nor validated.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def Encaps1(self):
        """Encapsulation 1 for TR-101 suboption 0x90

        Returns:
            str
        """
        return self._get_attribute('encaps1')
    @Encaps1.setter
    def Encaps1(self, value):
        self._set_attribute('encaps1', value)

    @property
    def Encaps2(self):
        """Encapsulation 2 for TR-101 suboption 0x90

        Returns:
            str
        """
        return self._get_attribute('encaps2')
    @Encaps2.setter
    def Encaps2(self, value):
        self._set_attribute('encaps2', value)

    @property
    def Ipv6AddrPrefixLen(self):
        """IPv6 Address Prefix Length

        Returns:
            number
        """
        return self._get_attribute('ipv6AddrPrefixLen')
    @Ipv6AddrPrefixLen.setter
    def Ipv6AddrPrefixLen(self, value):
        self._set_attribute('ipv6AddrPrefixLen', value)

    @property
    def Ipv6PoolPrefix(self):
        """Pool prefix for the IPv6 IP pool.

        Returns:
            str
        """
        return self._get_attribute('ipv6PoolPrefix')
    @Ipv6PoolPrefix.setter
    def Ipv6PoolPrefix(self, value):
        self._set_attribute('ipv6PoolPrefix', value)

    @property
    def Ipv6PoolPrefixLen(self):
        """IPv6 Pool Prefix Length

        Returns:
            number
        """
        return self._get_attribute('ipv6PoolPrefixLen')
    @Ipv6PoolPrefixLen.setter
    def Ipv6PoolPrefixLen(self, value):
        self._set_attribute('ipv6PoolPrefixLen', value)

    @property
    def LcpOptions(self):
        """For GUI grouping.

        Returns:
            str
        """
        return self._get_attribute('lcpOptions')
    @LcpOptions.setter
    def LcpOptions(self, value):
        self._set_attribute('lcpOptions', value)

    @property
    def LcpRetries(self):
        """Number of LCP retries

        Returns:
            number
        """
        return self._get_attribute('lcpRetries')
    @LcpRetries.setter
    def LcpRetries(self, value):
        self._set_attribute('lcpRetries', value)

    @property
    def LcpTermRetries(self):
        """Number of LCP Termination Retries

        Returns:
            number
        """
        return self._get_attribute('lcpTermRetries')
    @LcpTermRetries.setter
    def LcpTermRetries(self, value):
        self._set_attribute('lcpTermRetries', value)

    @property
    def LcpTermTimeout(self):
        """Timeout for LCP termination, in seconds.

        Returns:
            number
        """
        return self._get_attribute('lcpTermTimeout')
    @LcpTermTimeout.setter
    def LcpTermTimeout(self, value):
        self._set_attribute('lcpTermTimeout', value)

    @property
    def LcpTimeout(self):
        """Timeout for LCP phase, in seconds

        Returns:
            number
        """
        return self._get_attribute('lcpTimeout')
    @LcpTimeout.setter
    def LcpTimeout(self, value):
        self._set_attribute('lcpTimeout', value)

    @property
    def MaxPayload(self):
        """Max Payload

        Returns:
            number
        """
        return self._get_attribute('maxPayload')
    @MaxPayload.setter
    def MaxPayload(self, value):
        self._set_attribute('maxPayload', value)

    @property
    def Mtu(self):
        """Max Transmit Unit for PPP

        Returns:
            number
        """
        return self._get_attribute('mtu')
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute('mtu', value)

    @property
    def Name(self):
        """Name of range

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NcpRetries(self):
        """Number of NCP retries

        Returns:
            number
        """
        return self._get_attribute('ncpRetries')
    @NcpRetries.setter
    def NcpRetries(self, value):
        self._set_attribute('ncpRetries', value)

    @property
    def NcpTimeout(self):
        """Timeout for NCP phase, in seconds

        Returns:
            number
        """
        return self._get_attribute('ncpTimeout')
    @NcpTimeout.setter
    def NcpTimeout(self, value):
        self._set_attribute('ncpTimeout', value)

    @property
    def NcpType(self):
        """IP type (IPv4/IPv6) for Network Control Protocol

        Returns:
            str
        """
        return self._get_attribute('ncpType')
    @NcpType.setter
    def NcpType(self, value):
        self._set_attribute('ncpType', value)

    @property
    def NumSessions(self):
        """No. of sessions to setup

        Returns:
            number
        """
        return self._get_attribute('numSessions')
    @NumSessions.setter
    def NumSessions(self, value):
        self._set_attribute('numSessions', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def PadiRetries(self):
        """Number of PADI Retries

        Returns:
            number
        """
        return self._get_attribute('padiRetries')
    @PadiRetries.setter
    def PadiRetries(self, value):
        self._set_attribute('padiRetries', value)

    @property
    def PadiTimeout(self):
        """Timeout for PADI no response, in seconds

        Returns:
            number
        """
        return self._get_attribute('padiTimeout')
    @PadiTimeout.setter
    def PadiTimeout(self, value):
        self._set_attribute('padiTimeout', value)

    @property
    def PadrRetries(self):
        """Number of PADR Retries

        Returns:
            number
        """
        return self._get_attribute('padrRetries')
    @PadrRetries.setter
    def PadrRetries(self, value):
        self._set_attribute('padrRetries', value)

    @property
    def PadrTimeout(self):
        """Timeout for PADR no response, in seconds

        Returns:
            number
        """
        return self._get_attribute('padrTimeout')
    @PadrTimeout.setter
    def PadrTimeout(self, value):
        self._set_attribute('padrTimeout', value)

    @property
    def PapPassword(self):
        """Password when PAP Authentication is being used

        Returns:
            str
        """
        return self._get_attribute('papPassword')
    @PapPassword.setter
    def PapPassword(self, value):
        self._set_attribute('papPassword', value)

    @property
    def PapUser(self):
        """User name when PAP Authentication is being used

        Returns:
            str
        """
        return self._get_attribute('papUser')
    @PapUser.setter
    def PapUser(self, value):
        self._set_attribute('papUser', value)

    @property
    def PppoeOptions(self):
        """For GUI grouping.

        Returns:
            str
        """
        return self._get_attribute('pppoeOptions')
    @PppoeOptions.setter
    def PppoeOptions(self, value):
        self._set_attribute('pppoeOptions', value)

    @property
    def RedialMax(self):
        """Maximum number of PPPoE redials

        Returns:
            number
        """
        return self._get_attribute('redialMax')
    @RedialMax.setter
    def RedialMax(self, value):
        self._set_attribute('redialMax', value)

    @property
    def RedialTimeout(self):
        """PPPoE redial timeout, in seconds

        Returns:
            number
        """
        return self._get_attribute('redialTimeout')
    @RedialTimeout.setter
    def RedialTimeout(self, value):
        self._set_attribute('redialTimeout', value)

    @property
    def ServerBaseIid(self):
        """Base for IPv6CP interface identifiers assigned to servers.

        Returns:
            str
        """
        return self._get_attribute('serverBaseIid')
    @ServerBaseIid.setter
    def ServerBaseIid(self, value):
        self._set_attribute('serverBaseIid', value)

    @property
    def ServerBaseIp(self):
        """Base for IPv4 PPP server address creation

        Returns:
            str
        """
        return self._get_attribute('serverBaseIp')
    @ServerBaseIp.setter
    def ServerBaseIp(self, value):
        self._set_attribute('serverBaseIp', value)

    @property
    def ServerDnsOptions(self):
        """Server DNS options

        Returns:
            str
        """
        return self._get_attribute('serverDnsOptions')
    @ServerDnsOptions.setter
    def ServerDnsOptions(self, value):
        self._set_attribute('serverDnsOptions', value)

    @property
    def ServerIidIncr(self):
        """Increment for IPv6CP server interface identifiers.

        Returns:
            number
        """
        return self._get_attribute('serverIidIncr')
    @ServerIidIncr.setter
    def ServerIidIncr(self, value):
        self._set_attribute('serverIidIncr', value)

    @property
    def ServerIpIncr(self):
        """DEPRECATED *For internal use only*. For PPP/IP v4 server plugins, exactly one server address is used. As a result, 0.0.0.0 is the only legal value for this property.

        Returns:
            str
        """
        return self._get_attribute('serverIpIncr')
    @ServerIpIncr.setter
    def ServerIpIncr(self, value):
        self._set_attribute('serverIpIncr', value)

    @property
    def ServerNetmask(self):
        """Netmask that the server should supply to clients

        Returns:
            str
        """
        return self._get_attribute('serverNetmask')
    @ServerNetmask.setter
    def ServerNetmask(self, value):
        self._set_attribute('serverNetmask', value)

    @property
    def ServerNetmaskOptions(self):
        """Server netmask options

        Returns:
            str
        """
        return self._get_attribute('serverNetmaskOptions')
    @ServerNetmaskOptions.setter
    def ServerNetmaskOptions(self, value):
        self._set_attribute('serverNetmaskOptions', value)

    @property
    def ServerPrimaryDnsAddress(self):
        """Primary DNS server address supplied by server

        Returns:
            str
        """
        return self._get_attribute('serverPrimaryDnsAddress')
    @ServerPrimaryDnsAddress.setter
    def ServerPrimaryDnsAddress(self, value):
        self._set_attribute('serverPrimaryDnsAddress', value)

    @property
    def ServerSecondaryDnsAddress(self):
        """Secondary DNS server address supplied by server

        Returns:
            str
        """
        return self._get_attribute('serverSecondaryDnsAddress')
    @ServerSecondaryDnsAddress.setter
    def ServerSecondaryDnsAddress(self, value):
        self._set_attribute('serverSecondaryDnsAddress', value)

    @property
    def ServerSignalIwf(self):
        """If enabled, the PPPoE server echoes the interworked session TR-101 suboption received in messages from the client

        Returns:
            bool
        """
        return self._get_attribute('serverSignalIwf')
    @ServerSignalIwf.setter
    def ServerSignalIwf(self, value):
        self._set_attribute('serverSignalIwf', value)

    @property
    def ServerSignalLoopChar(self):
        """If enabled, the PPPoE server echoes the loop characteristics TR-101 suboptions received in messages from the client

        Returns:
            bool
        """
        return self._get_attribute('serverSignalLoopChar')
    @ServerSignalLoopChar.setter
    def ServerSignalLoopChar(self, value):
        self._set_attribute('serverSignalLoopChar', value)

    @property
    def ServerSignalLoopEncapsulation(self):
        """If enabled, the PPPoE server echoes the loop encapsulation (0x90) TR-101 suboption received in messages from the client

        Returns:
            bool
        """
        return self._get_attribute('serverSignalLoopEncapsulation')
    @ServerSignalLoopEncapsulation.setter
    def ServerSignalLoopEncapsulation(self, value):
        self._set_attribute('serverSignalLoopEncapsulation', value)

    @property
    def ServerSignalLoopId(self):
        """If enabled, the PPPoE server echoes the remote ID and circuit ID TR-101 suboptions received in messages from the client

        Returns:
            bool
        """
        return self._get_attribute('serverSignalLoopId')
    @ServerSignalLoopId.setter
    def ServerSignalLoopId(self, value):
        self._set_attribute('serverSignalLoopId', value)

    @property
    def ServiceName(self):
        """Access Concentrator Service Name - this option is only available for PPP servers.

        Returns:
            str
        """
        return self._get_attribute('serviceName')
    @ServiceName.setter
    def ServiceName(self, value):
        self._set_attribute('serviceName', value)

    @property
    def ServiceOptions(self):
        """Indicates PPPoE service retrieval mode

        Returns:
            str
        """
        return self._get_attribute('serviceOptions')
    @ServiceOptions.setter
    def ServiceOptions(self, value):
        self._set_attribute('serviceOptions', value)

    @property
    def UnlimitedRedialAttempts(self):
        """Enable/Disable PPPoE unlimited redial attempts

        Returns:
            bool
        """
        return self._get_attribute('unlimitedRedialAttempts')
    @UnlimitedRedialAttempts.setter
    def UnlimitedRedialAttempts(self, value):
        self._set_attribute('unlimitedRedialAttempts', value)

    @property
    def UseMagic(self):
        """use magic

        Returns:
            bool
        """
        return self._get_attribute('useMagic')
    @UseMagic.setter
    def UseMagic(self, value):
        self._set_attribute('useMagic', value)

    def update(self, AcName=None, AcOptions=None, ActualRateDownstream=None, ActualRateUpstream=None, AgentCircuitId=None, AgentRemoteId=None, AuthOptions=None, AuthRetries=None, AuthTimeout=None, AuthType=None, ChapName=None, ChapSecret=None, ClientBaseIid=None, ClientBaseIp=None, ClientDnsOptions=None, ClientIidIncr=None, ClientIpIncr=None, ClientNetmask=None, ClientNetmaskOptions=None, ClientPrimaryDnsAddress=None, ClientSecondaryDnsAddress=None, ClientSignalIwf=None, ClientSignalLoopChar=None, ClientSignalLoopEncapsulation=None, ClientSignalLoopId=None, DataLink=None, DnsServerList=None, DomainList=None, EchoReqInterval=None, EnableDnsRa=None, EnableDomainGroups=None, EnableEchoReq=None, EnableEchoRsp=None, EnableIncludeTagInPadi=None, EnableIncludeTagInPado=None, EnableIncludeTagInPadr=None, EnableIncludeTagInPads=None, EnableIntermediateAgentTags=None, EnableMaxPayload=None, EnableMru=None, EnableMruNegotiation=None, EnablePasswordCheck=None, EnableRedial=None, Enabled=None, Encaps1=None, Encaps2=None, Ipv6AddrPrefixLen=None, Ipv6PoolPrefix=None, Ipv6PoolPrefixLen=None, LcpOptions=None, LcpRetries=None, LcpTermRetries=None, LcpTermTimeout=None, LcpTimeout=None, MaxPayload=None, Mtu=None, Name=None, NcpRetries=None, NcpTimeout=None, NcpType=None, NumSessions=None, PadiRetries=None, PadiTimeout=None, PadrRetries=None, PadrTimeout=None, PapPassword=None, PapUser=None, PppoeOptions=None, RedialMax=None, RedialTimeout=None, ServerBaseIid=None, ServerBaseIp=None, ServerDnsOptions=None, ServerIidIncr=None, ServerIpIncr=None, ServerNetmask=None, ServerNetmaskOptions=None, ServerPrimaryDnsAddress=None, ServerSecondaryDnsAddress=None, ServerSignalIwf=None, ServerSignalLoopChar=None, ServerSignalLoopEncapsulation=None, ServerSignalLoopId=None, ServiceName=None, ServiceOptions=None, UnlimitedRedialAttempts=None, UseMagic=None):
        """Updates a child instance of pppoxRange on the server.

        Args:
            AcName (str): Access Concentrator Name - this option is only available for PPP servers.
            AcOptions (str): Indicates PPPoE AC retrieval mode
            ActualRateDownstream (number): Actual Data Rate Downstream Value (TR-101 suboption 0x82)
            ActualRateUpstream (number): Actual Data Rate Upstream Value (TR-101 suboption 0x81)
            AgentCircuitId (str): Agent Circuit ID (TR-101 suboption 0x01)
            AgentRemoteId (str): Agent Remote ID (TR-101 suboption 0x02)
            AuthOptions (str): For GUI grouping.
            AuthRetries (number): Number of PPP authentication retries
            AuthTimeout (number): Timeout for PPP authentication, in seconds.
            AuthType (str): Authentication type
            ChapName (str): User name when CHAP Authentication is being used
            ChapSecret (str): Secret when CHAP Authentication is being used
            ClientBaseIid (str): Base for IPv6CP interface identifiers assigned to clients.
            ClientBaseIp (str): Base for IPv4 PPP client address creation
            ClientDnsOptions (str): Client DNS options
            ClientIidIncr (number): Increment for IPv6CP client interface identifiers.
            ClientIpIncr (str): Incrementor for IPv4 PPP client address creation
            ClientNetmask (str): Netmask that the client should request
            ClientNetmaskOptions (str): Client netmask options
            ClientPrimaryDnsAddress (str): Primary DNS server address requested by client
            ClientSecondaryDnsAddress (str): Secondary DNS server address requested by client
            ClientSignalIwf (bool): Enables the sending of the interworked session (0xFE) TR-101 suboption in client PPPoE messages (PADI/PADR/PADT)
            ClientSignalLoopChar (bool): Enables the sending of the access loop characteristics TR-101 suboptions in client PPPoE messages (PADI/PADR/PADT)
            ClientSignalLoopEncapsulation (bool): Enables the sending of the loop encapsulation (0x90) TR-101 suboption in client PPPoE messages (PADI/PADR/PADT)
            ClientSignalLoopId (bool): Enables the sending of the remote ID and circuit ID TR-101 suboptions in client PPPoE messages (PADI/PADR/PADT)
            DataLink (str): Data Link for TR-101 suboption 0x90
            DnsServerList (str): DNS server list separacted by semicolon
            DomainList (str): Configure domain group settings
            EchoReqInterval (number): Keep alive interval
            EnableDnsRa (bool): Enable RDNSS routing advertisments
            EnableDomainGroups (bool): Enable domain groups
            EnableEchoReq (bool): Enable Echo requests
            EnableEchoRsp (bool): Enable Echo replies
            EnableIncludeTagInPadi (bool): OBSOLETE - If checked, PADI messages include Intermediate Agent Tags(only for PPP client)
            EnableIncludeTagInPado (bool): OBSOLETE - If checked, PADO messages include Intermediate Agent Tags(only for PPP server)
            EnableIncludeTagInPadr (bool): OBSOLETE - If checked, PADR messages include Intermediate Agent Tags(only for PPP client)
            EnableIncludeTagInPads (bool): OBSOLETE - If checked, PADs messages include Intermediate Agent Tags(only for PPP server)
            EnableIntermediateAgentTags (bool): OBSOLETE - If checked, Intermediate Agent Tags are enabled
            EnableMaxPayload (bool): Enable/Disable Max Payload
            EnableMru (bool): Enable/Disable MRU negotiation
            EnableMruNegotiation (bool): Option is deprecated. Please use enableMaxPayload. If checked, MRU negotiation is enabled
            EnablePasswordCheck (bool): Enable authentication credential checking on the port.
            EnableRedial (bool): Enable/Disable PPPoE redial
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Encaps1 (str): Encapsulation 1 for TR-101 suboption 0x90
            Encaps2 (str): Encapsulation 2 for TR-101 suboption 0x90
            Ipv6AddrPrefixLen (number): IPv6 Address Prefix Length
            Ipv6PoolPrefix (str): Pool prefix for the IPv6 IP pool.
            Ipv6PoolPrefixLen (number): IPv6 Pool Prefix Length
            LcpOptions (str): For GUI grouping.
            LcpRetries (number): Number of LCP retries
            LcpTermRetries (number): Number of LCP Termination Retries
            LcpTermTimeout (number): Timeout for LCP termination, in seconds.
            LcpTimeout (number): Timeout for LCP phase, in seconds
            MaxPayload (number): Max Payload
            Mtu (number): Max Transmit Unit for PPP
            Name (str): Name of range
            NcpRetries (number): Number of NCP retries
            NcpTimeout (number): Timeout for NCP phase, in seconds
            NcpType (str): IP type (IPv4/IPv6) for Network Control Protocol
            NumSessions (number): No. of sessions to setup
            PadiRetries (number): Number of PADI Retries
            PadiTimeout (number): Timeout for PADI no response, in seconds
            PadrRetries (number): Number of PADR Retries
            PadrTimeout (number): Timeout for PADR no response, in seconds
            PapPassword (str): Password when PAP Authentication is being used
            PapUser (str): User name when PAP Authentication is being used
            PppoeOptions (str): For GUI grouping.
            RedialMax (number): Maximum number of PPPoE redials
            RedialTimeout (number): PPPoE redial timeout, in seconds
            ServerBaseIid (str): Base for IPv6CP interface identifiers assigned to servers.
            ServerBaseIp (str): Base for IPv4 PPP server address creation
            ServerDnsOptions (str): Server DNS options
            ServerIidIncr (number): Increment for IPv6CP server interface identifiers.
            ServerIpIncr (str): *For internal use only*. For PPP/IP v4 server plugins, exactly one server address is used. As a result, 0.0.0.0 is the only legal value for this property.
            ServerNetmask (str): Netmask that the server should supply to clients
            ServerNetmaskOptions (str): Server netmask options
            ServerPrimaryDnsAddress (str): Primary DNS server address supplied by server
            ServerSecondaryDnsAddress (str): Secondary DNS server address supplied by server
            ServerSignalIwf (bool): If enabled, the PPPoE server echoes the interworked session TR-101 suboption received in messages from the client
            ServerSignalLoopChar (bool): If enabled, the PPPoE server echoes the loop characteristics TR-101 suboptions received in messages from the client
            ServerSignalLoopEncapsulation (bool): If enabled, the PPPoE server echoes the loop encapsulation (0x90) TR-101 suboption received in messages from the client
            ServerSignalLoopId (bool): If enabled, the PPPoE server echoes the remote ID and circuit ID TR-101 suboptions received in messages from the client
            ServiceName (str): Access Concentrator Service Name - this option is only available for PPP servers.
            ServiceOptions (str): Indicates PPPoE service retrieval mode
            UnlimitedRedialAttempts (bool): Enable/Disable PPPoE unlimited redial attempts
            UseMagic (bool): use magic

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
