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


class L2tpRange(Base):
    """L2TP Range
    The L2tpRange class encapsulates a required l2tpRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'l2tpRange'
    _SDM_ATT_MAP = {
        'AuthOptions': 'authOptions',
        'AuthRetries': 'authRetries',
        'AuthTimeout': 'authTimeout',
        'AuthType': 'authType',
        'BaseLnsIp': 'baseLnsIp',
        'BasicOptions': 'basicOptions',
        'BearerCapability': 'bearerCapability',
        'BearerType': 'bearerType',
        'ChapName': 'chapName',
        'ChapSecret': 'chapSecret',
        'ClientBaseIid': 'clientBaseIid',
        'ClientBaseIp': 'clientBaseIp',
        'ClientDnsOptions': 'clientDnsOptions',
        'ClientIidIncr': 'clientIidIncr',
        'ClientIpIncr': 'clientIpIncr',
        'ClientNetmask': 'clientNetmask',
        'ClientNetmaskOptions': 'clientNetmaskOptions',
        'ClientPrimaryDnsAddress': 'clientPrimaryDnsAddress',
        'ClientSecondaryDnsAddress': 'clientSecondaryDnsAddress',
        'ControlMsgsRetryCounter': 'controlMsgsRetryCounter',
        'ControlPlaneOptions': 'controlPlaneOptions',
        'DataPlaneOptions': 'dataPlaneOptions',
        'DnsServerList': 'dnsServerList',
        'DomainList': 'domainList',
        'DomainToIpList': 'domainToIpList',
        'EchoReqInterval': 'echoReqInterval',
        'EnableControlChecksum': 'enableControlChecksum',
        'EnableDataChecksum': 'enableDataChecksum',
        'EnableDnsRa': 'enableDnsRa',
        'EnableDomainGroups': 'enableDomainGroups',
        'EnableEchoReq': 'enableEchoReq',
        'EnableEchoRsp': 'enableEchoRsp',
        'EnableHelloRequest': 'enableHelloRequest',
        'EnableMru': 'enableMru',
        'EnablePasswordCheck': 'enablePasswordCheck',
        'EnableRedial': 'enableRedial',
        'Enabled': 'enabled',
        'FramingCapability': 'framingCapability',
        'HelloRequestInterval': 'helloRequestInterval',
        'IncrementBy': 'incrementBy',
        'InitRetransmitInterval': 'initRetransmitInterval',
        'IpIncrementOctet': 'ipIncrementOctet',
        'Ipv6AddrPrefixLen': 'ipv6AddrPrefixLen',
        'Ipv6PoolPrefix': 'ipv6PoolPrefix',
        'Ipv6PoolPrefixLen': 'ipv6PoolPrefixLen',
        'L2tpAuthOptions': 'l2tpAuthOptions',
        'LacHostName': 'lacHostName',
        'LacSecret': 'lacSecret',
        'LacToLnsMapping': 'lacToLnsMapping',
        'LcpOptions': 'lcpOptions',
        'LcpRetries': 'lcpRetries',
        'LcpTermRetries': 'lcpTermRetries',
        'LcpTermTimeout': 'lcpTermTimeout',
        'LcpTimeout': 'lcpTimeout',
        'LnsHostName': 'lnsHostName',
        'LnsIpList': 'lnsIpList',
        'LnsIpNumber': 'lnsIpNumber',
        'MaxRedialAttempts': 'maxRedialAttempts',
        'MaxRetransmitInterval': 'maxRetransmitInterval',
        'Mtu': 'mtu',
        'Name': 'name',
        'NcpRetries': 'ncpRetries',
        'NcpTimeout': 'ncpTimeout',
        'NcpType': 'ncpType',
        'NoCallTimeout': 'noCallTimeout',
        'NumSessions': 'numSessions',
        'ObjectId': 'objectId',
        'OffsetByte': 'offsetByte',
        'OffsetLength': 'offsetLength',
        'PapPassword': 'papPassword',
        'PapUser': 'papUser',
        'ReceiveWindowSize': 'receiveWindowSize',
        'RedialInterval': 'redialInterval',
        'ServerBaseIid': 'serverBaseIid',
        'ServerBaseIp': 'serverBaseIp',
        'ServerDnsOptions': 'serverDnsOptions',
        'ServerIidIncr': 'serverIidIncr',
        'ServerIpIncr': 'serverIpIncr',
        'ServerNetmask': 'serverNetmask',
        'ServerNetmaskOptions': 'serverNetmaskOptions',
        'ServerPrimaryDnsAddress': 'serverPrimaryDnsAddress',
        'ServerSecondaryDnsAddress': 'serverSecondaryDnsAddress',
        'SessionAllocMethod': 'sessionAllocMethod',
        'SessionsPerTunnel': 'sessionsPerTunnel',
        'TunnelAuthentication': 'tunnelAuthentication',
        'TunnelDestinationIp': 'tunnelDestinationIp',
        'TunnelIncrementBy': 'tunnelIncrementBy',
        'UdpDestinationPort': 'udpDestinationPort',
        'UdpSourcePort': 'udpSourcePort',
        'UseHiddenAvps': 'useHiddenAvps',
        'UseLengthBitInPayload': 'useLengthBitInPayload',
        'UseMagic': 'useMagic',
        'UseOffsetBitInPayload': 'useOffsetBitInPayload',
        'UseSequenceNoInPayload': 'useSequenceNoInPayload',
    }

    def __init__(self, parent):
        super(L2tpRange, self).__init__(parent)

    @property
    def DomainGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.domaingroup_695770cefa25f4649b6c1b5bdc5c2b4d.DomainGroup): An instance of the DomainGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.domaingroup_695770cefa25f4649b6c1b5bdc5c2b4d import DomainGroup
        return DomainGroup(self)

    @property
    def LnsIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.lnsip_d4eb5af3e3a70d8e85283c6e7758faa8.LnsIp): An instance of the LnsIp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.lnsip_d4eb5af3e3a70d8e85283c6e7758faa8 import LnsIp
        return LnsIp(self)

    @property
    def AuthOptions(self):
        """
        Returns
        -------
        - str: For GUI grouping.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthOptions'])
    @AuthOptions.setter
    def AuthOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuthOptions'], value)

    @property
    def AuthRetries(self):
        """
        Returns
        -------
        - number: Number of PPP authentication retries
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthRetries'])
    @AuthRetries.setter
    def AuthRetries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuthRetries'], value)

    @property
    def AuthTimeout(self):
        """
        Returns
        -------
        - number: Timeout for PPP authentication, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthTimeout'])
    @AuthTimeout.setter
    def AuthTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuthTimeout'], value)

    @property
    def AuthType(self):
        """
        Returns
        -------
        - str: Authentication type
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthType'])
    @AuthType.setter
    def AuthType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuthType'], value)

    @property
    def BaseLnsIp(self):
        """
        Returns
        -------
        - str: Defines the base address to be used by the L2TP tunnel
        """
        return self._get_attribute(self._SDM_ATT_MAP['BaseLnsIp'])
    @BaseLnsIp.setter
    def BaseLnsIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BaseLnsIp'], value)

    @property
    def BasicOptions(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BasicOptions'])
    @BasicOptions.setter
    def BasicOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BasicOptions'], value)

    @property
    def BearerCapability(self):
        """
        Returns
        -------
        - str: Bearer capability
        """
        return self._get_attribute(self._SDM_ATT_MAP['BearerCapability'])
    @BearerCapability.setter
    def BearerCapability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BearerCapability'], value)

    @property
    def BearerType(self):
        """
        Returns
        -------
        - str: Bearer Type
        """
        return self._get_attribute(self._SDM_ATT_MAP['BearerType'])
    @BearerType.setter
    def BearerType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BearerType'], value)

    @property
    def ChapName(self):
        """
        Returns
        -------
        - str: User name when CHAP Authentication is being used
        """
        return self._get_attribute(self._SDM_ATT_MAP['ChapName'])
    @ChapName.setter
    def ChapName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ChapName'], value)

    @property
    def ChapSecret(self):
        """
        Returns
        -------
        - str: Secret when CHAP Authentication is being used
        """
        return self._get_attribute(self._SDM_ATT_MAP['ChapSecret'])
    @ChapSecret.setter
    def ChapSecret(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ChapSecret'], value)

    @property
    def ClientBaseIid(self):
        """
        Returns
        -------
        - str: Base for IPv6CP interface identifiers assigned to clients.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientBaseIid'])
    @ClientBaseIid.setter
    def ClientBaseIid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientBaseIid'], value)

    @property
    def ClientBaseIp(self):
        """
        Returns
        -------
        - str: Base for IPv4 PPP client address creation
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientBaseIp'])
    @ClientBaseIp.setter
    def ClientBaseIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientBaseIp'], value)

    @property
    def ClientDnsOptions(self):
        """
        Returns
        -------
        - str: Client DNS options
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientDnsOptions'])
    @ClientDnsOptions.setter
    def ClientDnsOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientDnsOptions'], value)

    @property
    def ClientIidIncr(self):
        """
        Returns
        -------
        - number: Increment for IPv6CP client interface identifiers.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientIidIncr'])
    @ClientIidIncr.setter
    def ClientIidIncr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientIidIncr'], value)

    @property
    def ClientIpIncr(self):
        """
        Returns
        -------
        - str: Incrementor for IPv4 PPP client address creation
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientIpIncr'])
    @ClientIpIncr.setter
    def ClientIpIncr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientIpIncr'], value)

    @property
    def ClientNetmask(self):
        """
        Returns
        -------
        - str: Netmask that the client should request
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientNetmask'])
    @ClientNetmask.setter
    def ClientNetmask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientNetmask'], value)

    @property
    def ClientNetmaskOptions(self):
        """
        Returns
        -------
        - str: Client netmask options
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientNetmaskOptions'])
    @ClientNetmaskOptions.setter
    def ClientNetmaskOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientNetmaskOptions'], value)

    @property
    def ClientPrimaryDnsAddress(self):
        """
        Returns
        -------
        - str: Primary DNS server address requested by client
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientPrimaryDnsAddress'])
    @ClientPrimaryDnsAddress.setter
    def ClientPrimaryDnsAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientPrimaryDnsAddress'], value)

    @property
    def ClientSecondaryDnsAddress(self):
        """
        Returns
        -------
        - str: Secondary DNS server address requested by client
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientSecondaryDnsAddress'])
    @ClientSecondaryDnsAddress.setter
    def ClientSecondaryDnsAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientSecondaryDnsAddress'], value)

    @property
    def ControlMsgsRetryCounter(self):
        """
        Returns
        -------
        - number: Number of L2TP retries
        """
        return self._get_attribute(self._SDM_ATT_MAP['ControlMsgsRetryCounter'])
    @ControlMsgsRetryCounter.setter
    def ControlMsgsRetryCounter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ControlMsgsRetryCounter'], value)

    @property
    def ControlPlaneOptions(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ControlPlaneOptions'])
    @ControlPlaneOptions.setter
    def ControlPlaneOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ControlPlaneOptions'], value)

    @property
    def DataPlaneOptions(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPlaneOptions'])
    @DataPlaneOptions.setter
    def DataPlaneOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DataPlaneOptions'], value)

    @property
    def DnsServerList(self):
        """
        Returns
        -------
        - str: DNS server list separacted by semicolon
        """
        return self._get_attribute(self._SDM_ATT_MAP['DnsServerList'])
    @DnsServerList.setter
    def DnsServerList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DnsServerList'], value)

    @property
    def DomainList(self):
        """
        Returns
        -------
        - str: Configure domain group settings
        """
        return self._get_attribute(self._SDM_ATT_MAP['DomainList'])
    @DomainList.setter
    def DomainList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DomainList'], value)

    @property
    def DomainToIpList(self):
        """
        Returns
        -------
        - str: Domain To LNS
        """
        return self._get_attribute(self._SDM_ATT_MAP['DomainToIpList'])
    @DomainToIpList.setter
    def DomainToIpList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DomainToIpList'], value)

    @property
    def EchoReqInterval(self):
        """
        Returns
        -------
        - number: Keep alive interval
        """
        return self._get_attribute(self._SDM_ATT_MAP['EchoReqInterval'])
    @EchoReqInterval.setter
    def EchoReqInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EchoReqInterval'], value)

    @property
    def EnableControlChecksum(self):
        """
        Returns
        -------
        - bool: Enable/Disable UDP checksums on control plane packets
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableControlChecksum'])
    @EnableControlChecksum.setter
    def EnableControlChecksum(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableControlChecksum'], value)

    @property
    def EnableDataChecksum(self):
        """
        Returns
        -------
        - bool: Enable/Disable UDP checksums on data plane packets
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDataChecksum'])
    @EnableDataChecksum.setter
    def EnableDataChecksum(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDataChecksum'], value)

    @property
    def EnableDnsRa(self):
        """
        Returns
        -------
        - bool: Enable RDNSS routing advertisments
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDnsRa'])
    @EnableDnsRa.setter
    def EnableDnsRa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDnsRa'], value)

    @property
    def EnableDomainGroups(self):
        """
        Returns
        -------
        - bool: Enable domain groups
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDomainGroups'])
    @EnableDomainGroups.setter
    def EnableDomainGroups(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDomainGroups'], value)

    @property
    def EnableEchoReq(self):
        """
        Returns
        -------
        - bool: Enable Echo requests
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableEchoReq'])
    @EnableEchoReq.setter
    def EnableEchoReq(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableEchoReq'], value)

    @property
    def EnableEchoRsp(self):
        """
        Returns
        -------
        - bool: Enable Echo replies
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableEchoRsp'])
    @EnableEchoRsp.setter
    def EnableEchoRsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableEchoRsp'], value)

    @property
    def EnableHelloRequest(self):
        """
        Returns
        -------
        - bool: If enabled, L2TP hello request is performed
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHelloRequest'])
    @EnableHelloRequest.setter
    def EnableHelloRequest(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHelloRequest'], value)

    @property
    def EnableMru(self):
        """
        Returns
        -------
        - bool: Enable/Disable MRU negotiation
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMru'])
    @EnableMru.setter
    def EnableMru(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMru'], value)

    @property
    def EnablePasswordCheck(self):
        """
        Returns
        -------
        - bool: Enable authentication credential checking on the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePasswordCheck'])
    @EnablePasswordCheck.setter
    def EnablePasswordCheck(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePasswordCheck'], value)

    @property
    def EnableRedial(self):
        """
        Returns
        -------
        - bool: If enabled, L2TP redial is activated
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRedial'])
    @EnableRedial.setter
    def EnableRedial(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRedial'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def FramingCapability(self):
        """
        Returns
        -------
        - str: Designates sync or async framing
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramingCapability'])
    @FramingCapability.setter
    def FramingCapability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FramingCapability'], value)

    @property
    def HelloRequestInterval(self):
        """
        Returns
        -------
        - number: Timeout for L2TP hello request, in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloRequestInterval'])
    @HelloRequestInterval.setter
    def HelloRequestInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloRequestInterval'], value)

    @property
    def IncrementBy(self):
        """
        Returns
        -------
        - number: Defines the increment to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementBy'])
    @IncrementBy.setter
    def IncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementBy'], value)

    @property
    def InitRetransmitInterval(self):
        """
        Returns
        -------
        - number: Initial L2TP timeout
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitRetransmitInterval'])
    @InitRetransmitInterval.setter
    def InitRetransmitInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitRetransmitInterval'], value)

    @property
    def IpIncrementOctet(self):
        """
        Returns
        -------
        - number: IP increment octet
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpIncrementOctet'])
    @IpIncrementOctet.setter
    def IpIncrementOctet(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpIncrementOctet'], value)

    @property
    def Ipv6AddrPrefixLen(self):
        """
        Returns
        -------
        - number: IPv6 Address Prefix Length
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6AddrPrefixLen'])
    @Ipv6AddrPrefixLen.setter
    def Ipv6AddrPrefixLen(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6AddrPrefixLen'], value)

    @property
    def Ipv6PoolPrefix(self):
        """
        Returns
        -------
        - str: Pool prefix for the IPv6 IP pool.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6PoolPrefix'])
    @Ipv6PoolPrefix.setter
    def Ipv6PoolPrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6PoolPrefix'], value)

    @property
    def Ipv6PoolPrefixLen(self):
        """
        Returns
        -------
        - number: IPv6 Pool Prefix Length
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6PoolPrefixLen'])
    @Ipv6PoolPrefixLen.setter
    def Ipv6PoolPrefixLen(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6PoolPrefixLen'], value)

    @property
    def L2tpAuthOptions(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['L2tpAuthOptions'])
    @L2tpAuthOptions.setter
    def L2tpAuthOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['L2tpAuthOptions'], value)

    @property
    def LacHostName(self):
        """
        Returns
        -------
        - str: L2TP host name used during authentication on LAC, or authenticated against (on LNS).
        """
        return self._get_attribute(self._SDM_ATT_MAP['LacHostName'])
    @LacHostName.setter
    def LacHostName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LacHostName'], value)

    @property
    def LacSecret(self):
        """
        Returns
        -------
        - str: L2TP secret used during authentication
        """
        return self._get_attribute(self._SDM_ATT_MAP['LacSecret'])
    @LacSecret.setter
    def LacSecret(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LacSecret'], value)

    @property
    def LacToLnsMapping(self):
        """
        Returns
        -------
        - str: LAC to LNS Mapping
        """
        return self._get_attribute(self._SDM_ATT_MAP['LacToLnsMapping'])
    @LacToLnsMapping.setter
    def LacToLnsMapping(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LacToLnsMapping'], value)

    @property
    def LcpOptions(self):
        """
        Returns
        -------
        - str: For GUI grouping.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LcpOptions'])
    @LcpOptions.setter
    def LcpOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LcpOptions'], value)

    @property
    def LcpRetries(self):
        """
        Returns
        -------
        - number: Number of LCP retries
        """
        return self._get_attribute(self._SDM_ATT_MAP['LcpRetries'])
    @LcpRetries.setter
    def LcpRetries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LcpRetries'], value)

    @property
    def LcpTermRetries(self):
        """
        Returns
        -------
        - number: Number of LCP Termination Retries
        """
        return self._get_attribute(self._SDM_ATT_MAP['LcpTermRetries'])
    @LcpTermRetries.setter
    def LcpTermRetries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LcpTermRetries'], value)

    @property
    def LcpTermTimeout(self):
        """
        Returns
        -------
        - number: Timeout for LCP termination, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LcpTermTimeout'])
    @LcpTermTimeout.setter
    def LcpTermTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LcpTermTimeout'], value)

    @property
    def LcpTimeout(self):
        """
        Returns
        -------
        - number: Timeout for LCP phase, in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['LcpTimeout'])
    @LcpTimeout.setter
    def LcpTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LcpTimeout'], value)

    @property
    def LnsHostName(self):
        """
        Returns
        -------
        - str: L2TP hostname sent by Ixia port when acting as LNS
        """
        return self._get_attribute(self._SDM_ATT_MAP['LnsHostName'])
    @LnsHostName.setter
    def LnsHostName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LnsHostName'], value)

    @property
    def LnsIpList(self):
        """
        Returns
        -------
        - str: LNS IP Addresses
        """
        return self._get_attribute(self._SDM_ATT_MAP['LnsIpList'])
    @LnsIpList.setter
    def LnsIpList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LnsIpList'], value)

    @property
    def LnsIpNumber(self):
        """
        Returns
        -------
        - number: LNS IP number
        """
        return self._get_attribute(self._SDM_ATT_MAP['LnsIpNumber'])
    @LnsIpNumber.setter
    def LnsIpNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LnsIpNumber'], value)

    @property
    def MaxRedialAttempts(self):
        """
        Returns
        -------
        - number: Max number of L2TP redial attempts
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRedialAttempts'])
    @MaxRedialAttempts.setter
    def MaxRedialAttempts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRedialAttempts'], value)

    @property
    def MaxRetransmitInterval(self):
        """
        Returns
        -------
        - number: Max. L2TP timeout
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRetransmitInterval'])
    @MaxRetransmitInterval.setter
    def MaxRetransmitInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRetransmitInterval'], value)

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: Max Transmit Unit for PPP
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mtu'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of range
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
        - number: Number of NCP retries
        """
        return self._get_attribute(self._SDM_ATT_MAP['NcpRetries'])
    @NcpRetries.setter
    def NcpRetries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NcpRetries'], value)

    @property
    def NcpTimeout(self):
        """
        Returns
        -------
        - number: Timeout for NCP phase, in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['NcpTimeout'])
    @NcpTimeout.setter
    def NcpTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NcpTimeout'], value)

    @property
    def NcpType(self):
        """
        Returns
        -------
        - str: IP type (IPv4/IPv6) for Network Control Protocol
        """
        return self._get_attribute(self._SDM_ATT_MAP['NcpType'])
    @NcpType.setter
    def NcpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NcpType'], value)

    @property
    def NoCallTimeout(self):
        """
        Returns
        -------
        - number: Timeout for no call establishment, in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoCallTimeout'])
    @NoCallTimeout.setter
    def NoCallTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoCallTimeout'], value)

    @property
    def NumSessions(self):
        """
        Returns
        -------
        - number: No. of sessions to setup
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumSessions'])
    @NumSessions.setter
    def NumSessions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumSessions'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def OffsetByte(self):
        """
        Returns
        -------
        - number: L2TP offset byte
        """
        return self._get_attribute(self._SDM_ATT_MAP['OffsetByte'])
    @OffsetByte.setter
    def OffsetByte(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OffsetByte'], value)

    @property
    def OffsetLength(self):
        """
        Returns
        -------
        - number: L2TP offset length in bytes
        """
        return self._get_attribute(self._SDM_ATT_MAP['OffsetLength'])
    @OffsetLength.setter
    def OffsetLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OffsetLength'], value)

    @property
    def PapPassword(self):
        """
        Returns
        -------
        - str: Password when PAP Authentication is being used
        """
        return self._get_attribute(self._SDM_ATT_MAP['PapPassword'])
    @PapPassword.setter
    def PapPassword(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PapPassword'], value)

    @property
    def PapUser(self):
        """
        Returns
        -------
        - str: User name when PAP Authentication is being used
        """
        return self._get_attribute(self._SDM_ATT_MAP['PapUser'])
    @PapUser.setter
    def PapUser(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PapUser'], value)

    @property
    def ReceiveWindowSize(self):
        """
        Returns
        -------
        - number: L2TP Receive Window Size
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceiveWindowSize'])
    @ReceiveWindowSize.setter
    def ReceiveWindowSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReceiveWindowSize'], value)

    @property
    def RedialInterval(self):
        """
        Returns
        -------
        - number: L2TP redial timeout, in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['RedialInterval'])
    @RedialInterval.setter
    def RedialInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RedialInterval'], value)

    @property
    def ServerBaseIid(self):
        """
        Returns
        -------
        - str: Base for IPv6CP interface identifiers assigned to servers.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerBaseIid'])
    @ServerBaseIid.setter
    def ServerBaseIid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerBaseIid'], value)

    @property
    def ServerBaseIp(self):
        """
        Returns
        -------
        - str: Base for IPv4 PPP server address creation
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerBaseIp'])
    @ServerBaseIp.setter
    def ServerBaseIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerBaseIp'], value)

    @property
    def ServerDnsOptions(self):
        """
        Returns
        -------
        - str: Server DNS options
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerDnsOptions'])
    @ServerDnsOptions.setter
    def ServerDnsOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerDnsOptions'], value)

    @property
    def ServerIidIncr(self):
        """
        Returns
        -------
        - number: Increment for IPv6CP server interface identifiers.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerIidIncr'])
    @ServerIidIncr.setter
    def ServerIidIncr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerIidIncr'], value)

    @property
    def ServerIpIncr(self):
        """DEPRECATED 
        Returns
        -------
        - str: *For internal use only*. For PPP/IP v4 server plugins, exactly one server address is used. As a result, 0.0.0.0 is the only legal value for this property.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerIpIncr'])
    @ServerIpIncr.setter
    def ServerIpIncr(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerIpIncr'], value)

    @property
    def ServerNetmask(self):
        """
        Returns
        -------
        - str: Netmask that the server should supply to clients
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerNetmask'])
    @ServerNetmask.setter
    def ServerNetmask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerNetmask'], value)

    @property
    def ServerNetmaskOptions(self):
        """
        Returns
        -------
        - str: Server netmask options
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerNetmaskOptions'])
    @ServerNetmaskOptions.setter
    def ServerNetmaskOptions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerNetmaskOptions'], value)

    @property
    def ServerPrimaryDnsAddress(self):
        """
        Returns
        -------
        - str: Primary DNS server address supplied by server
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerPrimaryDnsAddress'])
    @ServerPrimaryDnsAddress.setter
    def ServerPrimaryDnsAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerPrimaryDnsAddress'], value)

    @property
    def ServerSecondaryDnsAddress(self):
        """
        Returns
        -------
        - str: Secondary DNS server address supplied by server
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerSecondaryDnsAddress'])
    @ServerSecondaryDnsAddress.setter
    def ServerSecondaryDnsAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerSecondaryDnsAddress'], value)

    @property
    def SessionAllocMethod(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionAllocMethod'])
    @SessionAllocMethod.setter
    def SessionAllocMethod(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SessionAllocMethod'], value)

    @property
    def SessionsPerTunnel(self):
        """
        Returns
        -------
        - number: Number of sessions per L2TP tunnel
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionsPerTunnel'])
    @SessionsPerTunnel.setter
    def SessionsPerTunnel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SessionsPerTunnel'], value)

    @property
    def TunnelAuthentication(self):
        """
        Returns
        -------
        - str: Enable/Disable L2TP tunnel authentication
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelAuthentication'])
    @TunnelAuthentication.setter
    def TunnelAuthentication(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelAuthentication'], value)

    @property
    def TunnelDestinationIp(self):
        """
        Returns
        -------
        - str: Defines the base address to be used for L2TP tunnel destination in the range
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelDestinationIp'])
    @TunnelDestinationIp.setter
    def TunnelDestinationIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelDestinationIp'], value)

    @property
    def TunnelIncrementBy(self):
        """
        Returns
        -------
        - str: Defines the increment to be used between L2TP tunnels
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelIncrementBy'])
    @TunnelIncrementBy.setter
    def TunnelIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelIncrementBy'], value)

    @property
    def UdpDestinationPort(self):
        """
        Returns
        -------
        - number: UDP port to employ for tunneling destinations
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpDestinationPort'])
    @UdpDestinationPort.setter
    def UdpDestinationPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UdpDestinationPort'], value)

    @property
    def UdpSourcePort(self):
        """
        Returns
        -------
        - number: UDP port to employ for tunneling sources
        """
        return self._get_attribute(self._SDM_ATT_MAP['UdpSourcePort'])
    @UdpSourcePort.setter
    def UdpSourcePort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UdpSourcePort'], value)

    @property
    def UseHiddenAvps(self):
        """
        Returns
        -------
        - bool: Enable/Disable (A)ttribute (V)alue (P)air hiding
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseHiddenAvps'])
    @UseHiddenAvps.setter
    def UseHiddenAvps(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseHiddenAvps'], value)

    @property
    def UseLengthBitInPayload(self):
        """
        Returns
        -------
        - bool: If enabled, length bit set in L2TP data packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseLengthBitInPayload'])
    @UseLengthBitInPayload.setter
    def UseLengthBitInPayload(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseLengthBitInPayload'], value)

    @property
    def UseMagic(self):
        """
        Returns
        -------
        - bool: use magic
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseMagic'])
    @UseMagic.setter
    def UseMagic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseMagic'], value)

    @property
    def UseOffsetBitInPayload(self):
        """
        Returns
        -------
        - bool: If enabled, offset bit is enabled in L2TP data packets
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseOffsetBitInPayload'])
    @UseOffsetBitInPayload.setter
    def UseOffsetBitInPayload(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseOffsetBitInPayload'], value)

    @property
    def UseSequenceNoInPayload(self):
        """
        Returns
        -------
        - bool: If enabled, sequence bit is set in L2TP data packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseSequenceNoInPayload'])
    @UseSequenceNoInPayload.setter
    def UseSequenceNoInPayload(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseSequenceNoInPayload'], value)

    def update(self, AuthOptions=None, AuthRetries=None, AuthTimeout=None, AuthType=None, BaseLnsIp=None, BasicOptions=None, BearerCapability=None, BearerType=None, ChapName=None, ChapSecret=None, ClientBaseIid=None, ClientBaseIp=None, ClientDnsOptions=None, ClientIidIncr=None, ClientIpIncr=None, ClientNetmask=None, ClientNetmaskOptions=None, ClientPrimaryDnsAddress=None, ClientSecondaryDnsAddress=None, ControlMsgsRetryCounter=None, ControlPlaneOptions=None, DataPlaneOptions=None, DnsServerList=None, DomainList=None, DomainToIpList=None, EchoReqInterval=None, EnableControlChecksum=None, EnableDataChecksum=None, EnableDnsRa=None, EnableDomainGroups=None, EnableEchoReq=None, EnableEchoRsp=None, EnableHelloRequest=None, EnableMru=None, EnablePasswordCheck=None, EnableRedial=None, Enabled=None, FramingCapability=None, HelloRequestInterval=None, IncrementBy=None, InitRetransmitInterval=None, IpIncrementOctet=None, Ipv6AddrPrefixLen=None, Ipv6PoolPrefix=None, Ipv6PoolPrefixLen=None, L2tpAuthOptions=None, LacHostName=None, LacSecret=None, LacToLnsMapping=None, LcpOptions=None, LcpRetries=None, LcpTermRetries=None, LcpTermTimeout=None, LcpTimeout=None, LnsHostName=None, LnsIpList=None, LnsIpNumber=None, MaxRedialAttempts=None, MaxRetransmitInterval=None, Mtu=None, Name=None, NcpRetries=None, NcpTimeout=None, NcpType=None, NoCallTimeout=None, NumSessions=None, OffsetByte=None, OffsetLength=None, PapPassword=None, PapUser=None, ReceiveWindowSize=None, RedialInterval=None, ServerBaseIid=None, ServerBaseIp=None, ServerDnsOptions=None, ServerIidIncr=None, ServerIpIncr=None, ServerNetmask=None, ServerNetmaskOptions=None, ServerPrimaryDnsAddress=None, ServerSecondaryDnsAddress=None, SessionAllocMethod=None, SessionsPerTunnel=None, TunnelAuthentication=None, TunnelDestinationIp=None, TunnelIncrementBy=None, UdpDestinationPort=None, UdpSourcePort=None, UseHiddenAvps=None, UseLengthBitInPayload=None, UseMagic=None, UseOffsetBitInPayload=None, UseSequenceNoInPayload=None):
        """Updates l2tpRange resource on the server.

        Args
        ----
        - AuthOptions (str): For GUI grouping.
        - AuthRetries (number): Number of PPP authentication retries
        - AuthTimeout (number): Timeout for PPP authentication, in seconds.
        - AuthType (str): Authentication type
        - BaseLnsIp (str): Defines the base address to be used by the L2TP tunnel
        - BasicOptions (str): 
        - BearerCapability (str): Bearer capability
        - BearerType (str): Bearer Type
        - ChapName (str): User name when CHAP Authentication is being used
        - ChapSecret (str): Secret when CHAP Authentication is being used
        - ClientBaseIid (str): Base for IPv6CP interface identifiers assigned to clients.
        - ClientBaseIp (str): Base for IPv4 PPP client address creation
        - ClientDnsOptions (str): Client DNS options
        - ClientIidIncr (number): Increment for IPv6CP client interface identifiers.
        - ClientIpIncr (str): Incrementor for IPv4 PPP client address creation
        - ClientNetmask (str): Netmask that the client should request
        - ClientNetmaskOptions (str): Client netmask options
        - ClientPrimaryDnsAddress (str): Primary DNS server address requested by client
        - ClientSecondaryDnsAddress (str): Secondary DNS server address requested by client
        - ControlMsgsRetryCounter (number): Number of L2TP retries
        - ControlPlaneOptions (str): 
        - DataPlaneOptions (str): 
        - DnsServerList (str): DNS server list separacted by semicolon
        - DomainList (str): Configure domain group settings
        - DomainToIpList (str): Domain To LNS
        - EchoReqInterval (number): Keep alive interval
        - EnableControlChecksum (bool): Enable/Disable UDP checksums on control plane packets
        - EnableDataChecksum (bool): Enable/Disable UDP checksums on data plane packets
        - EnableDnsRa (bool): Enable RDNSS routing advertisments
        - EnableDomainGroups (bool): Enable domain groups
        - EnableEchoReq (bool): Enable Echo requests
        - EnableEchoRsp (bool): Enable Echo replies
        - EnableHelloRequest (bool): If enabled, L2TP hello request is performed
        - EnableMru (bool): Enable/Disable MRU negotiation
        - EnablePasswordCheck (bool): Enable authentication credential checking on the port.
        - EnableRedial (bool): If enabled, L2TP redial is activated
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FramingCapability (str): Designates sync or async framing
        - HelloRequestInterval (number): Timeout for L2TP hello request, in seconds
        - IncrementBy (number): Defines the increment to be used for enumerating all the addresses in the range.
        - InitRetransmitInterval (number): Initial L2TP timeout
        - IpIncrementOctet (number): IP increment octet
        - Ipv6AddrPrefixLen (number): IPv6 Address Prefix Length
        - Ipv6PoolPrefix (str): Pool prefix for the IPv6 IP pool.
        - Ipv6PoolPrefixLen (number): IPv6 Pool Prefix Length
        - L2tpAuthOptions (str): 
        - LacHostName (str): L2TP host name used during authentication on LAC, or authenticated against (on LNS).
        - LacSecret (str): L2TP secret used during authentication
        - LacToLnsMapping (str): LAC to LNS Mapping
        - LcpOptions (str): For GUI grouping.
        - LcpRetries (number): Number of LCP retries
        - LcpTermRetries (number): Number of LCP Termination Retries
        - LcpTermTimeout (number): Timeout for LCP termination, in seconds.
        - LcpTimeout (number): Timeout for LCP phase, in seconds
        - LnsHostName (str): L2TP hostname sent by Ixia port when acting as LNS
        - LnsIpList (str): LNS IP Addresses
        - LnsIpNumber (number): LNS IP number
        - MaxRedialAttempts (number): Max number of L2TP redial attempts
        - MaxRetransmitInterval (number): Max. L2TP timeout
        - Mtu (number): Max Transmit Unit for PPP
        - Name (str): Name of range
        - NcpRetries (number): Number of NCP retries
        - NcpTimeout (number): Timeout for NCP phase, in seconds
        - NcpType (str): IP type (IPv4/IPv6) for Network Control Protocol
        - NoCallTimeout (number): Timeout for no call establishment, in seconds
        - NumSessions (number): No. of sessions to setup
        - OffsetByte (number): L2TP offset byte
        - OffsetLength (number): L2TP offset length in bytes
        - PapPassword (str): Password when PAP Authentication is being used
        - PapUser (str): User name when PAP Authentication is being used
        - ReceiveWindowSize (number): L2TP Receive Window Size
        - RedialInterval (number): L2TP redial timeout, in seconds
        - ServerBaseIid (str): Base for IPv6CP interface identifiers assigned to servers.
        - ServerBaseIp (str): Base for IPv4 PPP server address creation
        - ServerDnsOptions (str): Server DNS options
        - ServerIidIncr (number): Increment for IPv6CP server interface identifiers.
        - ServerIpIncr (str): *For internal use only*. For PPP/IP v4 server plugins, exactly one server address is used. As a result, 0.0.0.0 is the only legal value for this property.
        - ServerNetmask (str): Netmask that the server should supply to clients
        - ServerNetmaskOptions (str): Server netmask options
        - ServerPrimaryDnsAddress (str): Primary DNS server address supplied by server
        - ServerSecondaryDnsAddress (str): Secondary DNS server address supplied by server
        - SessionAllocMethod (str): 
        - SessionsPerTunnel (number): Number of sessions per L2TP tunnel
        - TunnelAuthentication (str): Enable/Disable L2TP tunnel authentication
        - TunnelDestinationIp (str): Defines the base address to be used for L2TP tunnel destination in the range
        - TunnelIncrementBy (str): Defines the increment to be used between L2TP tunnels
        - UdpDestinationPort (number): UDP port to employ for tunneling destinations
        - UdpSourcePort (number): UDP port to employ for tunneling sources
        - UseHiddenAvps (bool): Enable/Disable (A)ttribute (V)alue (P)air hiding
        - UseLengthBitInPayload (bool): If enabled, length bit set in L2TP data packets.
        - UseMagic (bool): use magic
        - UseOffsetBitInPayload (bool): If enabled, offset bit is enabled in L2TP data packets
        - UseSequenceNoInPayload (bool): If enabled, sequence bit is set in L2TP data packets.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
