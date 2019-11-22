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


class L2tpRange(Base):
    """L2TP Range
    The L2tpRange class encapsulates a required l2tpRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'l2tpRange'

    def __init__(self, parent):
        super(L2tpRange, self).__init__(parent)

    @property
    def DomainGroup(self):
        """An instance of the DomainGroup class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.domaingroup_f6859cb671851d1c232346b1baeeae89.DomainGroup)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.domaingroup_f6859cb671851d1c232346b1baeeae89 import DomainGroup
        return DomainGroup(self)

    @property
    def LnsIp(self):
        """An instance of the LnsIp class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.lnsip_ec48a5dd0e5aa7799a7f283d3de4499d.LnsIp)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.lnsip_ec48a5dd0e5aa7799a7f283d3de4499d import LnsIp
        return LnsIp(self)

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
    def BaseLnsIp(self):
        """Defines the base address to be used by the L2TP tunnel

        Returns:
            str
        """
        return self._get_attribute('baseLnsIp')
    @BaseLnsIp.setter
    def BaseLnsIp(self, value):
        self._set_attribute('baseLnsIp', value)

    @property
    def BasicOptions(self):
        """

        Returns:
            str
        """
        return self._get_attribute('basicOptions')
    @BasicOptions.setter
    def BasicOptions(self, value):
        self._set_attribute('basicOptions', value)

    @property
    def BearerCapability(self):
        """Bearer capability

        Returns:
            str
        """
        return self._get_attribute('bearerCapability')
    @BearerCapability.setter
    def BearerCapability(self, value):
        self._set_attribute('bearerCapability', value)

    @property
    def BearerType(self):
        """Bearer Type

        Returns:
            str
        """
        return self._get_attribute('bearerType')
    @BearerType.setter
    def BearerType(self, value):
        self._set_attribute('bearerType', value)

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
    def ControlMsgsRetryCounter(self):
        """Number of L2TP retries

        Returns:
            number
        """
        return self._get_attribute('controlMsgsRetryCounter')
    @ControlMsgsRetryCounter.setter
    def ControlMsgsRetryCounter(self, value):
        self._set_attribute('controlMsgsRetryCounter', value)

    @property
    def ControlPlaneOptions(self):
        """

        Returns:
            str
        """
        return self._get_attribute('controlPlaneOptions')
    @ControlPlaneOptions.setter
    def ControlPlaneOptions(self, value):
        self._set_attribute('controlPlaneOptions', value)

    @property
    def DataPlaneOptions(self):
        """

        Returns:
            str
        """
        return self._get_attribute('dataPlaneOptions')
    @DataPlaneOptions.setter
    def DataPlaneOptions(self, value):
        self._set_attribute('dataPlaneOptions', value)

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
    def DomainToIpList(self):
        """Domain To LNS

        Returns:
            str
        """
        return self._get_attribute('domainToIpList')
    @DomainToIpList.setter
    def DomainToIpList(self, value):
        self._set_attribute('domainToIpList', value)

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
    def EnableControlChecksum(self):
        """Enable/Disable UDP checksums on control plane packets

        Returns:
            bool
        """
        return self._get_attribute('enableControlChecksum')
    @EnableControlChecksum.setter
    def EnableControlChecksum(self, value):
        self._set_attribute('enableControlChecksum', value)

    @property
    def EnableDataChecksum(self):
        """Enable/Disable UDP checksums on data plane packets

        Returns:
            bool
        """
        return self._get_attribute('enableDataChecksum')
    @EnableDataChecksum.setter
    def EnableDataChecksum(self, value):
        self._set_attribute('enableDataChecksum', value)

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
    def EnableHelloRequest(self):
        """If enabled, L2TP hello request is performed

        Returns:
            bool
        """
        return self._get_attribute('enableHelloRequest')
    @EnableHelloRequest.setter
    def EnableHelloRequest(self, value):
        self._set_attribute('enableHelloRequest', value)

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
        """If enabled, L2TP redial is activated

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
    def FramingCapability(self):
        """Designates sync or async framing

        Returns:
            str
        """
        return self._get_attribute('framingCapability')
    @FramingCapability.setter
    def FramingCapability(self, value):
        self._set_attribute('framingCapability', value)

    @property
    def HelloRequestInterval(self):
        """Timeout for L2TP hello request, in seconds

        Returns:
            number
        """
        return self._get_attribute('helloRequestInterval')
    @HelloRequestInterval.setter
    def HelloRequestInterval(self, value):
        self._set_attribute('helloRequestInterval', value)

    @property
    def IncrementBy(self):
        """Defines the increment to be used for enumerating all the addresses in the range.

        Returns:
            number
        """
        return self._get_attribute('incrementBy')
    @IncrementBy.setter
    def IncrementBy(self, value):
        self._set_attribute('incrementBy', value)

    @property
    def InitRetransmitInterval(self):
        """Initial L2TP timeout

        Returns:
            number
        """
        return self._get_attribute('initRetransmitInterval')
    @InitRetransmitInterval.setter
    def InitRetransmitInterval(self, value):
        self._set_attribute('initRetransmitInterval', value)

    @property
    def IpIncrementOctet(self):
        """IP increment octet

        Returns:
            number
        """
        return self._get_attribute('ipIncrementOctet')
    @IpIncrementOctet.setter
    def IpIncrementOctet(self, value):
        self._set_attribute('ipIncrementOctet', value)

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
    def L2tpAuthOptions(self):
        """

        Returns:
            str
        """
        return self._get_attribute('l2tpAuthOptions')
    @L2tpAuthOptions.setter
    def L2tpAuthOptions(self, value):
        self._set_attribute('l2tpAuthOptions', value)

    @property
    def LacHostName(self):
        """L2TP host name used during authentication on LAC, or authenticated against (on LNS).

        Returns:
            str
        """
        return self._get_attribute('lacHostName')
    @LacHostName.setter
    def LacHostName(self, value):
        self._set_attribute('lacHostName', value)

    @property
    def LacSecret(self):
        """L2TP secret used during authentication

        Returns:
            str
        """
        return self._get_attribute('lacSecret')
    @LacSecret.setter
    def LacSecret(self, value):
        self._set_attribute('lacSecret', value)

    @property
    def LacToLnsMapping(self):
        """LAC to LNS Mapping

        Returns:
            str
        """
        return self._get_attribute('lacToLnsMapping')
    @LacToLnsMapping.setter
    def LacToLnsMapping(self, value):
        self._set_attribute('lacToLnsMapping', value)

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
    def LnsHostName(self):
        """L2TP hostname sent by Ixia port when acting as LNS

        Returns:
            str
        """
        return self._get_attribute('lnsHostName')
    @LnsHostName.setter
    def LnsHostName(self, value):
        self._set_attribute('lnsHostName', value)

    @property
    def LnsIpList(self):
        """LNS IP Addresses

        Returns:
            str
        """
        return self._get_attribute('lnsIpList')
    @LnsIpList.setter
    def LnsIpList(self, value):
        self._set_attribute('lnsIpList', value)

    @property
    def LnsIpNumber(self):
        """LNS IP number

        Returns:
            number
        """
        return self._get_attribute('lnsIpNumber')
    @LnsIpNumber.setter
    def LnsIpNumber(self, value):
        self._set_attribute('lnsIpNumber', value)

    @property
    def MaxRedialAttempts(self):
        """Max number of L2TP redial attempts

        Returns:
            number
        """
        return self._get_attribute('maxRedialAttempts')
    @MaxRedialAttempts.setter
    def MaxRedialAttempts(self, value):
        self._set_attribute('maxRedialAttempts', value)

    @property
    def MaxRetransmitInterval(self):
        """Max. L2TP timeout

        Returns:
            number
        """
        return self._get_attribute('maxRetransmitInterval')
    @MaxRetransmitInterval.setter
    def MaxRetransmitInterval(self, value):
        self._set_attribute('maxRetransmitInterval', value)

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
    def NoCallTimeout(self):
        """Timeout for no call establishment, in seconds

        Returns:
            number
        """
        return self._get_attribute('noCallTimeout')
    @NoCallTimeout.setter
    def NoCallTimeout(self, value):
        self._set_attribute('noCallTimeout', value)

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
    def OffsetByte(self):
        """L2TP offset byte

        Returns:
            number
        """
        return self._get_attribute('offsetByte')
    @OffsetByte.setter
    def OffsetByte(self, value):
        self._set_attribute('offsetByte', value)

    @property
    def OffsetLength(self):
        """L2TP offset length in bytes

        Returns:
            number
        """
        return self._get_attribute('offsetLength')
    @OffsetLength.setter
    def OffsetLength(self, value):
        self._set_attribute('offsetLength', value)

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
    def ReceiveWindowSize(self):
        """L2TP Receive Window Size

        Returns:
            number
        """
        return self._get_attribute('receiveWindowSize')
    @ReceiveWindowSize.setter
    def ReceiveWindowSize(self, value):
        self._set_attribute('receiveWindowSize', value)

    @property
    def RedialInterval(self):
        """L2TP redial timeout, in seconds

        Returns:
            number
        """
        return self._get_attribute('redialInterval')
    @RedialInterval.setter
    def RedialInterval(self, value):
        self._set_attribute('redialInterval', value)

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
    def SessionAllocMethod(self):
        """

        Returns:
            str
        """
        return self._get_attribute('sessionAllocMethod')
    @SessionAllocMethod.setter
    def SessionAllocMethod(self, value):
        self._set_attribute('sessionAllocMethod', value)

    @property
    def SessionsPerTunnel(self):
        """Number of sessions per L2TP tunnel

        Returns:
            number
        """
        return self._get_attribute('sessionsPerTunnel')
    @SessionsPerTunnel.setter
    def SessionsPerTunnel(self, value):
        self._set_attribute('sessionsPerTunnel', value)

    @property
    def TunnelAuthentication(self):
        """Enable/Disable L2TP tunnel authentication

        Returns:
            str
        """
        return self._get_attribute('tunnelAuthentication')
    @TunnelAuthentication.setter
    def TunnelAuthentication(self, value):
        self._set_attribute('tunnelAuthentication', value)

    @property
    def TunnelDestinationIp(self):
        """Defines the base address to be used for L2TP tunnel destination in the range

        Returns:
            str
        """
        return self._get_attribute('tunnelDestinationIp')
    @TunnelDestinationIp.setter
    def TunnelDestinationIp(self, value):
        self._set_attribute('tunnelDestinationIp', value)

    @property
    def TunnelIncrementBy(self):
        """Defines the increment to be used between L2TP tunnels

        Returns:
            str
        """
        return self._get_attribute('tunnelIncrementBy')
    @TunnelIncrementBy.setter
    def TunnelIncrementBy(self, value):
        self._set_attribute('tunnelIncrementBy', value)

    @property
    def UdpDestinationPort(self):
        """UDP port to employ for tunneling destinations

        Returns:
            number
        """
        return self._get_attribute('udpDestinationPort')
    @UdpDestinationPort.setter
    def UdpDestinationPort(self, value):
        self._set_attribute('udpDestinationPort', value)

    @property
    def UdpSourcePort(self):
        """UDP port to employ for tunneling sources

        Returns:
            number
        """
        return self._get_attribute('udpSourcePort')
    @UdpSourcePort.setter
    def UdpSourcePort(self, value):
        self._set_attribute('udpSourcePort', value)

    @property
    def UseHiddenAvps(self):
        """Enable/Disable (A)ttribute (V)alue (P)air hiding

        Returns:
            bool
        """
        return self._get_attribute('useHiddenAvps')
    @UseHiddenAvps.setter
    def UseHiddenAvps(self, value):
        self._set_attribute('useHiddenAvps', value)

    @property
    def UseLengthBitInPayload(self):
        """If enabled, length bit set in L2TP data packets.

        Returns:
            bool
        """
        return self._get_attribute('useLengthBitInPayload')
    @UseLengthBitInPayload.setter
    def UseLengthBitInPayload(self, value):
        self._set_attribute('useLengthBitInPayload', value)

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

    @property
    def UseOffsetBitInPayload(self):
        """If enabled, offset bit is enabled in L2TP data packets

        Returns:
            bool
        """
        return self._get_attribute('useOffsetBitInPayload')
    @UseOffsetBitInPayload.setter
    def UseOffsetBitInPayload(self, value):
        self._set_attribute('useOffsetBitInPayload', value)

    @property
    def UseSequenceNoInPayload(self):
        """If enabled, sequence bit is set in L2TP data packets.

        Returns:
            bool
        """
        return self._get_attribute('useSequenceNoInPayload')
    @UseSequenceNoInPayload.setter
    def UseSequenceNoInPayload(self, value):
        self._set_attribute('useSequenceNoInPayload', value)

    def update(self, AuthOptions=None, AuthRetries=None, AuthTimeout=None, AuthType=None, BaseLnsIp=None, BasicOptions=None, BearerCapability=None, BearerType=None, ChapName=None, ChapSecret=None, ClientBaseIid=None, ClientBaseIp=None, ClientDnsOptions=None, ClientIidIncr=None, ClientIpIncr=None, ClientNetmask=None, ClientNetmaskOptions=None, ClientPrimaryDnsAddress=None, ClientSecondaryDnsAddress=None, ControlMsgsRetryCounter=None, ControlPlaneOptions=None, DataPlaneOptions=None, DnsServerList=None, DomainList=None, DomainToIpList=None, EchoReqInterval=None, EnableControlChecksum=None, EnableDataChecksum=None, EnableDnsRa=None, EnableDomainGroups=None, EnableEchoReq=None, EnableEchoRsp=None, EnableHelloRequest=None, EnableMru=None, EnablePasswordCheck=None, EnableRedial=None, Enabled=None, FramingCapability=None, HelloRequestInterval=None, IncrementBy=None, InitRetransmitInterval=None, IpIncrementOctet=None, Ipv6AddrPrefixLen=None, Ipv6PoolPrefix=None, Ipv6PoolPrefixLen=None, L2tpAuthOptions=None, LacHostName=None, LacSecret=None, LacToLnsMapping=None, LcpOptions=None, LcpRetries=None, LcpTermRetries=None, LcpTermTimeout=None, LcpTimeout=None, LnsHostName=None, LnsIpList=None, LnsIpNumber=None, MaxRedialAttempts=None, MaxRetransmitInterval=None, Mtu=None, Name=None, NcpRetries=None, NcpTimeout=None, NcpType=None, NoCallTimeout=None, NumSessions=None, OffsetByte=None, OffsetLength=None, PapPassword=None, PapUser=None, ReceiveWindowSize=None, RedialInterval=None, ServerBaseIid=None, ServerBaseIp=None, ServerDnsOptions=None, ServerIidIncr=None, ServerIpIncr=None, ServerNetmask=None, ServerNetmaskOptions=None, ServerPrimaryDnsAddress=None, ServerSecondaryDnsAddress=None, SessionAllocMethod=None, SessionsPerTunnel=None, TunnelAuthentication=None, TunnelDestinationIp=None, TunnelIncrementBy=None, UdpDestinationPort=None, UdpSourcePort=None, UseHiddenAvps=None, UseLengthBitInPayload=None, UseMagic=None, UseOffsetBitInPayload=None, UseSequenceNoInPayload=None):
        """Updates a child instance of l2tpRange on the server.

        Args:
            AuthOptions (str): For GUI grouping.
            AuthRetries (number): Number of PPP authentication retries
            AuthTimeout (number): Timeout for PPP authentication, in seconds.
            AuthType (str): Authentication type
            BaseLnsIp (str): Defines the base address to be used by the L2TP tunnel
            BasicOptions (str): 
            BearerCapability (str): Bearer capability
            BearerType (str): Bearer Type
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
            ControlMsgsRetryCounter (number): Number of L2TP retries
            ControlPlaneOptions (str): 
            DataPlaneOptions (str): 
            DnsServerList (str): DNS server list separacted by semicolon
            DomainList (str): Configure domain group settings
            DomainToIpList (str): Domain To LNS
            EchoReqInterval (number): Keep alive interval
            EnableControlChecksum (bool): Enable/Disable UDP checksums on control plane packets
            EnableDataChecksum (bool): Enable/Disable UDP checksums on data plane packets
            EnableDnsRa (bool): Enable RDNSS routing advertisments
            EnableDomainGroups (bool): Enable domain groups
            EnableEchoReq (bool): Enable Echo requests
            EnableEchoRsp (bool): Enable Echo replies
            EnableHelloRequest (bool): If enabled, L2TP hello request is performed
            EnableMru (bool): Enable/Disable MRU negotiation
            EnablePasswordCheck (bool): Enable authentication credential checking on the port.
            EnableRedial (bool): If enabled, L2TP redial is activated
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FramingCapability (str): Designates sync or async framing
            HelloRequestInterval (number): Timeout for L2TP hello request, in seconds
            IncrementBy (number): Defines the increment to be used for enumerating all the addresses in the range.
            InitRetransmitInterval (number): Initial L2TP timeout
            IpIncrementOctet (number): IP increment octet
            Ipv6AddrPrefixLen (number): IPv6 Address Prefix Length
            Ipv6PoolPrefix (str): Pool prefix for the IPv6 IP pool.
            Ipv6PoolPrefixLen (number): IPv6 Pool Prefix Length
            L2tpAuthOptions (str): 
            LacHostName (str): L2TP host name used during authentication on LAC, or authenticated against (on LNS).
            LacSecret (str): L2TP secret used during authentication
            LacToLnsMapping (str): LAC to LNS Mapping
            LcpOptions (str): For GUI grouping.
            LcpRetries (number): Number of LCP retries
            LcpTermRetries (number): Number of LCP Termination Retries
            LcpTermTimeout (number): Timeout for LCP termination, in seconds.
            LcpTimeout (number): Timeout for LCP phase, in seconds
            LnsHostName (str): L2TP hostname sent by Ixia port when acting as LNS
            LnsIpList (str): LNS IP Addresses
            LnsIpNumber (number): LNS IP number
            MaxRedialAttempts (number): Max number of L2TP redial attempts
            MaxRetransmitInterval (number): Max. L2TP timeout
            Mtu (number): Max Transmit Unit for PPP
            Name (str): Name of range
            NcpRetries (number): Number of NCP retries
            NcpTimeout (number): Timeout for NCP phase, in seconds
            NcpType (str): IP type (IPv4/IPv6) for Network Control Protocol
            NoCallTimeout (number): Timeout for no call establishment, in seconds
            NumSessions (number): No. of sessions to setup
            OffsetByte (number): L2TP offset byte
            OffsetLength (number): L2TP offset length in bytes
            PapPassword (str): Password when PAP Authentication is being used
            PapUser (str): User name when PAP Authentication is being used
            ReceiveWindowSize (number): L2TP Receive Window Size
            RedialInterval (number): L2TP redial timeout, in seconds
            ServerBaseIid (str): Base for IPv6CP interface identifiers assigned to servers.
            ServerBaseIp (str): Base for IPv4 PPP server address creation
            ServerDnsOptions (str): Server DNS options
            ServerIidIncr (number): Increment for IPv6CP server interface identifiers.
            ServerIpIncr (str): *For internal use only*. For PPP/IP v4 server plugins, exactly one server address is used. As a result, 0.0.0.0 is the only legal value for this property.
            ServerNetmask (str): Netmask that the server should supply to clients
            ServerNetmaskOptions (str): Server netmask options
            ServerPrimaryDnsAddress (str): Primary DNS server address supplied by server
            ServerSecondaryDnsAddress (str): Secondary DNS server address supplied by server
            SessionAllocMethod (str): 
            SessionsPerTunnel (number): Number of sessions per L2TP tunnel
            TunnelAuthentication (str): Enable/Disable L2TP tunnel authentication
            TunnelDestinationIp (str): Defines the base address to be used for L2TP tunnel destination in the range
            TunnelIncrementBy (str): Defines the increment to be used between L2TP tunnels
            UdpDestinationPort (number): UDP port to employ for tunneling destinations
            UdpSourcePort (number): UDP port to employ for tunneling sources
            UseHiddenAvps (bool): Enable/Disable (A)ttribute (V)alue (P)air hiding
            UseLengthBitInPayload (bool): If enabled, length bit set in L2TP data packets.
            UseMagic (bool): use magic
            UseOffsetBitInPayload (bool): If enabled, offset bit is enabled in L2TP data packets
            UseSequenceNoInPayload (bool): If enabled, sequence bit is set in L2TP data packets.

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
