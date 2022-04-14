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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class PppoxRange(Base):
    """The PPP range class
    The PppoxRange class encapsulates a required pppoxRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "pppoxRange"
    _SDM_ATT_MAP = {
        "AcName": "acName",
        "AcOptions": "acOptions",
        "ActualRateDownstream": "actualRateDownstream",
        "ActualRateUpstream": "actualRateUpstream",
        "AgentCircuitId": "agentCircuitId",
        "AgentRemoteId": "agentRemoteId",
        "AuthOptions": "authOptions",
        "AuthRetries": "authRetries",
        "AuthTimeout": "authTimeout",
        "AuthType": "authType",
        "ChapName": "chapName",
        "ChapSecret": "chapSecret",
        "ClientBaseIid": "clientBaseIid",
        "ClientBaseIp": "clientBaseIp",
        "ClientDnsOptions": "clientDnsOptions",
        "ClientIidIncr": "clientIidIncr",
        "ClientIpIncr": "clientIpIncr",
        "ClientNetmask": "clientNetmask",
        "ClientNetmaskOptions": "clientNetmaskOptions",
        "ClientPrimaryDnsAddress": "clientPrimaryDnsAddress",
        "ClientSecondaryDnsAddress": "clientSecondaryDnsAddress",
        "ClientSignalIwf": "clientSignalIwf",
        "ClientSignalLoopChar": "clientSignalLoopChar",
        "ClientSignalLoopEncapsulation": "clientSignalLoopEncapsulation",
        "ClientSignalLoopId": "clientSignalLoopId",
        "DataLink": "dataLink",
        "DnsServerList": "dnsServerList",
        "DomainList": "domainList",
        "EchoReqInterval": "echoReqInterval",
        "EnableDnsRa": "enableDnsRa",
        "EnableDomainGroups": "enableDomainGroups",
        "EnableEchoReq": "enableEchoReq",
        "EnableEchoRsp": "enableEchoRsp",
        "EnableIncludeTagInPadi": "enableIncludeTagInPadi",
        "EnableIncludeTagInPado": "enableIncludeTagInPado",
        "EnableIncludeTagInPadr": "enableIncludeTagInPadr",
        "EnableIncludeTagInPads": "enableIncludeTagInPads",
        "EnableIntermediateAgentTags": "enableIntermediateAgentTags",
        "EnableMaxPayload": "enableMaxPayload",
        "EnableMru": "enableMru",
        "EnableMruNegotiation": "enableMruNegotiation",
        "EnablePasswordCheck": "enablePasswordCheck",
        "EnableRedial": "enableRedial",
        "Enabled": "enabled",
        "Encaps1": "encaps1",
        "Encaps2": "encaps2",
        "Ipv6AddrPrefixLen": "ipv6AddrPrefixLen",
        "Ipv6PoolPrefix": "ipv6PoolPrefix",
        "Ipv6PoolPrefixLen": "ipv6PoolPrefixLen",
        "LcpOptions": "lcpOptions",
        "LcpRetries": "lcpRetries",
        "LcpTermRetries": "lcpTermRetries",
        "LcpTermTimeout": "lcpTermTimeout",
        "LcpTimeout": "lcpTimeout",
        "MaxPayload": "maxPayload",
        "Mtu": "mtu",
        "Name": "name",
        "NcpRetries": "ncpRetries",
        "NcpTimeout": "ncpTimeout",
        "NcpType": "ncpType",
        "NumSessions": "numSessions",
        "ObjectId": "objectId",
        "PadiRetries": "padiRetries",
        "PadiTimeout": "padiTimeout",
        "PadrRetries": "padrRetries",
        "PadrTimeout": "padrTimeout",
        "PapPassword": "papPassword",
        "PapUser": "papUser",
        "PppoeOptions": "pppoeOptions",
        "RedialMax": "redialMax",
        "RedialTimeout": "redialTimeout",
        "ServerBaseIid": "serverBaseIid",
        "ServerBaseIp": "serverBaseIp",
        "ServerDnsOptions": "serverDnsOptions",
        "ServerIidIncr": "serverIidIncr",
        "ServerIpIncr": "serverIpIncr",
        "ServerNetmask": "serverNetmask",
        "ServerNetmaskOptions": "serverNetmaskOptions",
        "ServerPrimaryDnsAddress": "serverPrimaryDnsAddress",
        "ServerSecondaryDnsAddress": "serverSecondaryDnsAddress",
        "ServerSignalIwf": "serverSignalIwf",
        "ServerSignalLoopChar": "serverSignalLoopChar",
        "ServerSignalLoopEncapsulation": "serverSignalLoopEncapsulation",
        "ServerSignalLoopId": "serverSignalLoopId",
        "ServiceName": "serviceName",
        "ServiceOptions": "serviceOptions",
        "UnlimitedRedialAttempts": "unlimitedRedialAttempts",
        "UseMagic": "useMagic",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PppoxRange, self).__init__(parent, list_op)

    @property
    def AcMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.acmac_9ec8a1134161cc7c671ff615cb166b39.AcMac): An instance of the AcMac class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.acmac_9ec8a1134161cc7c671ff615cb166b39 import (
            AcMac,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AcMac", None) is not None:
                return self._properties.get("AcMac")
        return AcMac(self)

    @property
    def AcName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.acname_caeea664ba02e01d2ce8d9be780cab83.AcName): An instance of the AcName class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.acname_caeea664ba02e01d2ce8d9be780cab83 import (
            AcName,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AcName", None) is not None:
                return self._properties.get("AcName")
        return AcName(self)

    @property
    def DomainGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.domaingroup_bc7289bb1262b1f7cbdbb433b1ac34a8.DomainGroup): An instance of the DomainGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.domaingroup_bc7289bb1262b1f7cbdbb433b1ac34a8 import (
            DomainGroup,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DomainGroup", None) is not None:
                return self._properties.get("DomainGroup")
        return DomainGroup(self)

    @property
    def AcName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Access Concentrator Name - this option is only available for PPP servers.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AcName"])

    @AcName.setter
    def AcName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AcName"], value)

    @property
    def AcOptions(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates PPPoE AC retrieval mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["AcOptions"])

    @AcOptions.setter
    def AcOptions(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AcOptions"], value)

    @property
    def ActualRateDownstream(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Actual Data Rate Downstream Value (TR-101 suboption 0x82)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActualRateDownstream"])

    @ActualRateDownstream.setter
    def ActualRateDownstream(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ActualRateDownstream"], value)

    @property
    def ActualRateUpstream(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Actual Data Rate Upstream Value (TR-101 suboption 0x81)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActualRateUpstream"])

    @ActualRateUpstream.setter
    def ActualRateUpstream(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ActualRateUpstream"], value)

    @property
    def AgentCircuitId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Agent Circuit ID (TR-101 suboption 0x01)
        """
        return self._get_attribute(self._SDM_ATT_MAP["AgentCircuitId"])

    @AgentCircuitId.setter
    def AgentCircuitId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AgentCircuitId"], value)

    @property
    def AgentRemoteId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Agent Remote ID (TR-101 suboption 0x02)
        """
        return self._get_attribute(self._SDM_ATT_MAP["AgentRemoteId"])

    @AgentRemoteId.setter
    def AgentRemoteId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AgentRemoteId"], value)

    @property
    def AuthOptions(self):
        # type: () -> str
        """
        Returns
        -------
        - str: For GUI grouping.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AuthOptions"])

    @AuthOptions.setter
    def AuthOptions(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AuthOptions"], value)

    @property
    def AuthRetries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of PPP authentication retries
        """
        return self._get_attribute(self._SDM_ATT_MAP["AuthRetries"])

    @AuthRetries.setter
    def AuthRetries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AuthRetries"], value)

    @property
    def AuthTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Timeout for PPP authentication, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AuthTimeout"])

    @AuthTimeout.setter
    def AuthTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AuthTimeout"], value)

    @property
    def AuthType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Authentication type
        """
        return self._get_attribute(self._SDM_ATT_MAP["AuthType"])

    @AuthType.setter
    def AuthType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AuthType"], value)

    @property
    def ChapName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: User name when CHAP Authentication is being used
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChapName"])

    @ChapName.setter
    def ChapName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChapName"], value)

    @property
    def ChapSecret(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Secret when CHAP Authentication is being used
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChapSecret"])

    @ChapSecret.setter
    def ChapSecret(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChapSecret"], value)

    @property
    def ClientBaseIid(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Base for IPv6CP interface identifiers assigned to clients.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientBaseIid"])

    @ClientBaseIid.setter
    def ClientBaseIid(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientBaseIid"], value)

    @property
    def ClientBaseIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Base for IPv4 PPP client address creation
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientBaseIp"])

    @ClientBaseIp.setter
    def ClientBaseIp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientBaseIp"], value)

    @property
    def ClientDnsOptions(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Client DNS options
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientDnsOptions"])

    @ClientDnsOptions.setter
    def ClientDnsOptions(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientDnsOptions"], value)

    @property
    def ClientIidIncr(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Increment for IPv6CP client interface identifiers.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientIidIncr"])

    @ClientIidIncr.setter
    def ClientIidIncr(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientIidIncr"], value)

    @property
    def ClientIpIncr(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Incrementor for IPv4 PPP client address creation
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientIpIncr"])

    @ClientIpIncr.setter
    def ClientIpIncr(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientIpIncr"], value)

    @property
    def ClientNetmask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Netmask that the client should request
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientNetmask"])

    @ClientNetmask.setter
    def ClientNetmask(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientNetmask"], value)

    @property
    def ClientNetmaskOptions(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Client netmask options
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientNetmaskOptions"])

    @ClientNetmaskOptions.setter
    def ClientNetmaskOptions(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientNetmaskOptions"], value)

    @property
    def ClientPrimaryDnsAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Primary DNS server address requested by client
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientPrimaryDnsAddress"])

    @ClientPrimaryDnsAddress.setter
    def ClientPrimaryDnsAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientPrimaryDnsAddress"], value)

    @property
    def ClientSecondaryDnsAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Secondary DNS server address requested by client
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientSecondaryDnsAddress"])

    @ClientSecondaryDnsAddress.setter
    def ClientSecondaryDnsAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientSecondaryDnsAddress"], value)

    @property
    def ClientSignalIwf(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the sending of the interworked session (0xFE) TR-101 suboption in client PPPoE messages (PADI/PADR/PADT)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientSignalIwf"])

    @ClientSignalIwf.setter
    def ClientSignalIwf(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientSignalIwf"], value)

    @property
    def ClientSignalLoopChar(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the sending of the access loop characteristics TR-101 suboptions in client PPPoE messages (PADI/PADR/PADT)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientSignalLoopChar"])

    @ClientSignalLoopChar.setter
    def ClientSignalLoopChar(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientSignalLoopChar"], value)

    @property
    def ClientSignalLoopEncapsulation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the sending of the loop encapsulation (0x90) TR-101 suboption in client PPPoE messages (PADI/PADR/PADT)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientSignalLoopEncapsulation"])

    @ClientSignalLoopEncapsulation.setter
    def ClientSignalLoopEncapsulation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientSignalLoopEncapsulation"], value)

    @property
    def ClientSignalLoopId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the sending of the remote ID and circuit ID TR-101 suboptions in client PPPoE messages (PADI/PADR/PADT)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientSignalLoopId"])

    @ClientSignalLoopId.setter
    def ClientSignalLoopId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientSignalLoopId"], value)

    @property
    def DataLink(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Data Link for TR-101 suboption 0x90
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataLink"])

    @DataLink.setter
    def DataLink(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataLink"], value)

    @property
    def DnsServerList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: DNS server list separacted by semicolon
        """
        return self._get_attribute(self._SDM_ATT_MAP["DnsServerList"])

    @DnsServerList.setter
    def DnsServerList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DnsServerList"], value)

    @property
    def DomainList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Configure domain group settings
        """
        return self._get_attribute(self._SDM_ATT_MAP["DomainList"])

    @DomainList.setter
    def DomainList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DomainList"], value)

    @property
    def EchoReqInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Keep alive interval
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoReqInterval"])

    @EchoReqInterval.setter
    def EchoReqInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoReqInterval"], value)

    @property
    def EnableDnsRa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable RDNSS routing advertisments
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDnsRa"])

    @EnableDnsRa.setter
    def EnableDnsRa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDnsRa"], value)

    @property
    def EnableDomainGroups(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable domain groups
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDomainGroups"])

    @EnableDomainGroups.setter
    def EnableDomainGroups(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDomainGroups"], value)

    @property
    def EnableEchoReq(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable Echo requests
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableEchoReq"])

    @EnableEchoReq.setter
    def EnableEchoReq(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableEchoReq"], value)

    @property
    def EnableEchoRsp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable Echo replies
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableEchoRsp"])

    @EnableEchoRsp.setter
    def EnableEchoRsp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableEchoRsp"], value)

    @property
    def EnableIncludeTagInPadi(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: OBSOLETE - If checked, PADI messages include Intermediate Agent Tags(only for PPP client)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableIncludeTagInPadi"])

    @EnableIncludeTagInPadi.setter
    def EnableIncludeTagInPadi(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableIncludeTagInPadi"], value)

    @property
    def EnableIncludeTagInPado(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: OBSOLETE - If checked, PADO messages include Intermediate Agent Tags(only for PPP server)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableIncludeTagInPado"])

    @EnableIncludeTagInPado.setter
    def EnableIncludeTagInPado(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableIncludeTagInPado"], value)

    @property
    def EnableIncludeTagInPadr(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: OBSOLETE - If checked, PADR messages include Intermediate Agent Tags(only for PPP client)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableIncludeTagInPadr"])

    @EnableIncludeTagInPadr.setter
    def EnableIncludeTagInPadr(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableIncludeTagInPadr"], value)

    @property
    def EnableIncludeTagInPads(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: OBSOLETE - If checked, PADs messages include Intermediate Agent Tags(only for PPP server)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableIncludeTagInPads"])

    @EnableIncludeTagInPads.setter
    def EnableIncludeTagInPads(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableIncludeTagInPads"], value)

    @property
    def EnableIntermediateAgentTags(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: OBSOLETE - If checked, Intermediate Agent Tags are enabled
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableIntermediateAgentTags"])

    @EnableIntermediateAgentTags.setter
    def EnableIntermediateAgentTags(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableIntermediateAgentTags"], value)

    @property
    def EnableMaxPayload(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable/Disable Max Payload
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMaxPayload"])

    @EnableMaxPayload.setter
    def EnableMaxPayload(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMaxPayload"], value)

    @property
    def EnableMru(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable/Disable MRU negotiation
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMru"])

    @EnableMru.setter
    def EnableMru(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMru"], value)

    @property
    def EnableMruNegotiation(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: Option is deprecated. Please use enableMaxPayload. If checked, MRU negotiation is enabled
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMruNegotiation"])

    @EnableMruNegotiation.setter
    def EnableMruNegotiation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMruNegotiation"], value)

    @property
    def EnablePasswordCheck(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable authentication credential checking on the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePasswordCheck"])

    @EnablePasswordCheck.setter
    def EnablePasswordCheck(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePasswordCheck"], value)

    @property
    def EnableRedial(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable/Disable PPPoE redial
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableRedial"])

    @EnableRedial.setter
    def EnableRedial(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableRedial"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def Encaps1(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Encapsulation 1 for TR-101 suboption 0x90
        """
        return self._get_attribute(self._SDM_ATT_MAP["Encaps1"])

    @Encaps1.setter
    def Encaps1(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Encaps1"], value)

    @property
    def Encaps2(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Encapsulation 2 for TR-101 suboption 0x90
        """
        return self._get_attribute(self._SDM_ATT_MAP["Encaps2"])

    @Encaps2.setter
    def Encaps2(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Encaps2"], value)

    @property
    def Ipv6AddrPrefixLen(self):
        # type: () -> int
        """
        Returns
        -------
        - number: IPv6 Address Prefix Length
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6AddrPrefixLen"])

    @Ipv6AddrPrefixLen.setter
    def Ipv6AddrPrefixLen(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6AddrPrefixLen"], value)

    @property
    def Ipv6PoolPrefix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Pool prefix for the IPv6 IP pool.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6PoolPrefix"])

    @Ipv6PoolPrefix.setter
    def Ipv6PoolPrefix(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6PoolPrefix"], value)

    @property
    def Ipv6PoolPrefixLen(self):
        # type: () -> int
        """
        Returns
        -------
        - number: IPv6 Pool Prefix Length
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6PoolPrefixLen"])

    @Ipv6PoolPrefixLen.setter
    def Ipv6PoolPrefixLen(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6PoolPrefixLen"], value)

    @property
    def LcpOptions(self):
        # type: () -> str
        """
        Returns
        -------
        - str: For GUI grouping.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LcpOptions"])

    @LcpOptions.setter
    def LcpOptions(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LcpOptions"], value)

    @property
    def LcpRetries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of LCP retries
        """
        return self._get_attribute(self._SDM_ATT_MAP["LcpRetries"])

    @LcpRetries.setter
    def LcpRetries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LcpRetries"], value)

    @property
    def LcpTermRetries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of LCP Termination Retries
        """
        return self._get_attribute(self._SDM_ATT_MAP["LcpTermRetries"])

    @LcpTermRetries.setter
    def LcpTermRetries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LcpTermRetries"], value)

    @property
    def LcpTermTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Timeout for LCP termination, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LcpTermTimeout"])

    @LcpTermTimeout.setter
    def LcpTermTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LcpTermTimeout"], value)

    @property
    def LcpTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Timeout for LCP phase, in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["LcpTimeout"])

    @LcpTimeout.setter
    def LcpTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LcpTimeout"], value)

    @property
    def MaxPayload(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Max Payload
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxPayload"])

    @MaxPayload.setter
    def MaxPayload(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxPayload"], value)

    @property
    def Mtu(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Max Transmit Unit for PPP
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mtu"])

    @Mtu.setter
    def Mtu(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mtu"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NcpRetries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of NCP retries
        """
        return self._get_attribute(self._SDM_ATT_MAP["NcpRetries"])

    @NcpRetries.setter
    def NcpRetries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NcpRetries"], value)

    @property
    def NcpTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Timeout for NCP phase, in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["NcpTimeout"])

    @NcpTimeout.setter
    def NcpTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NcpTimeout"], value)

    @property
    def NcpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: IP type (IPv4/IPv6) for Network Control Protocol
        """
        return self._get_attribute(self._SDM_ATT_MAP["NcpType"])

    @NcpType.setter
    def NcpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NcpType"], value)

    @property
    def NumSessions(self):
        # type: () -> int
        """
        Returns
        -------
        - number: No. of sessions to setup
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumSessions"])

    @NumSessions.setter
    def NumSessions(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumSessions"], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    @property
    def PadiRetries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of PADI Retries
        """
        return self._get_attribute(self._SDM_ATT_MAP["PadiRetries"])

    @PadiRetries.setter
    def PadiRetries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PadiRetries"], value)

    @property
    def PadiTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Timeout for PADI no response, in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["PadiTimeout"])

    @PadiTimeout.setter
    def PadiTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PadiTimeout"], value)

    @property
    def PadrRetries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of PADR Retries
        """
        return self._get_attribute(self._SDM_ATT_MAP["PadrRetries"])

    @PadrRetries.setter
    def PadrRetries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PadrRetries"], value)

    @property
    def PadrTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Timeout for PADR no response, in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["PadrTimeout"])

    @PadrTimeout.setter
    def PadrTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PadrTimeout"], value)

    @property
    def PapPassword(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Password when PAP Authentication is being used
        """
        return self._get_attribute(self._SDM_ATT_MAP["PapPassword"])

    @PapPassword.setter
    def PapPassword(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PapPassword"], value)

    @property
    def PapUser(self):
        # type: () -> str
        """
        Returns
        -------
        - str: User name when PAP Authentication is being used
        """
        return self._get_attribute(self._SDM_ATT_MAP["PapUser"])

    @PapUser.setter
    def PapUser(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PapUser"], value)

    @property
    def PppoeOptions(self):
        # type: () -> str
        """
        Returns
        -------
        - str: For GUI grouping.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PppoeOptions"])

    @PppoeOptions.setter
    def PppoeOptions(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PppoeOptions"], value)

    @property
    def RedialMax(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of PPPoE redials
        """
        return self._get_attribute(self._SDM_ATT_MAP["RedialMax"])

    @RedialMax.setter
    def RedialMax(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RedialMax"], value)

    @property
    def RedialTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: PPPoE redial timeout, in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["RedialTimeout"])

    @RedialTimeout.setter
    def RedialTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RedialTimeout"], value)

    @property
    def ServerBaseIid(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Base for IPv6CP interface identifiers assigned to servers.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerBaseIid"])

    @ServerBaseIid.setter
    def ServerBaseIid(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerBaseIid"], value)

    @property
    def ServerBaseIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Base for IPv4 PPP server address creation
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerBaseIp"])

    @ServerBaseIp.setter
    def ServerBaseIp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerBaseIp"], value)

    @property
    def ServerDnsOptions(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Server DNS options
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerDnsOptions"])

    @ServerDnsOptions.setter
    def ServerDnsOptions(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerDnsOptions"], value)

    @property
    def ServerIidIncr(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Increment for IPv6CP server interface identifiers.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerIidIncr"])

    @ServerIidIncr.setter
    def ServerIidIncr(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerIidIncr"], value)

    @property
    def ServerIpIncr(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: *For internal use only*. For PPP/IP v4 server plugins, exactly one server address is used. As a result, 0.0.0.0 is the only legal value for this property.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerIpIncr"])

    @ServerIpIncr.setter
    def ServerIpIncr(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerIpIncr"], value)

    @property
    def ServerNetmask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Netmask that the server should supply to clients
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerNetmask"])

    @ServerNetmask.setter
    def ServerNetmask(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerNetmask"], value)

    @property
    def ServerNetmaskOptions(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Server netmask options
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerNetmaskOptions"])

    @ServerNetmaskOptions.setter
    def ServerNetmaskOptions(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerNetmaskOptions"], value)

    @property
    def ServerPrimaryDnsAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Primary DNS server address supplied by server
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerPrimaryDnsAddress"])

    @ServerPrimaryDnsAddress.setter
    def ServerPrimaryDnsAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerPrimaryDnsAddress"], value)

    @property
    def ServerSecondaryDnsAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Secondary DNS server address supplied by server
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerSecondaryDnsAddress"])

    @ServerSecondaryDnsAddress.setter
    def ServerSecondaryDnsAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerSecondaryDnsAddress"], value)

    @property
    def ServerSignalIwf(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the PPPoE server echoes the interworked session TR-101 suboption received in messages from the client
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerSignalIwf"])

    @ServerSignalIwf.setter
    def ServerSignalIwf(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerSignalIwf"], value)

    @property
    def ServerSignalLoopChar(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the PPPoE server echoes the loop characteristics TR-101 suboptions received in messages from the client
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerSignalLoopChar"])

    @ServerSignalLoopChar.setter
    def ServerSignalLoopChar(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerSignalLoopChar"], value)

    @property
    def ServerSignalLoopEncapsulation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the PPPoE server echoes the loop encapsulation (0x90) TR-101 suboption received in messages from the client
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerSignalLoopEncapsulation"])

    @ServerSignalLoopEncapsulation.setter
    def ServerSignalLoopEncapsulation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerSignalLoopEncapsulation"], value)

    @property
    def ServerSignalLoopId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the PPPoE server echoes the remote ID and circuit ID TR-101 suboptions received in messages from the client
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerSignalLoopId"])

    @ServerSignalLoopId.setter
    def ServerSignalLoopId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerSignalLoopId"], value)

    @property
    def ServiceName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Access Concentrator Service Name - this option is only available for PPP servers.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServiceName"])

    @ServiceName.setter
    def ServiceName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServiceName"], value)

    @property
    def ServiceOptions(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates PPPoE service retrieval mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServiceOptions"])

    @ServiceOptions.setter
    def ServiceOptions(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServiceOptions"], value)

    @property
    def UnlimitedRedialAttempts(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable/Disable PPPoE unlimited redial attempts
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnlimitedRedialAttempts"])

    @UnlimitedRedialAttempts.setter
    def UnlimitedRedialAttempts(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnlimitedRedialAttempts"], value)

    @property
    def UseMagic(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: use magic
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseMagic"])

    @UseMagic.setter
    def UseMagic(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseMagic"], value)

    def update(
        self,
        AcName=None,
        AcOptions=None,
        ActualRateDownstream=None,
        ActualRateUpstream=None,
        AgentCircuitId=None,
        AgentRemoteId=None,
        AuthOptions=None,
        AuthRetries=None,
        AuthTimeout=None,
        AuthType=None,
        ChapName=None,
        ChapSecret=None,
        ClientBaseIid=None,
        ClientBaseIp=None,
        ClientDnsOptions=None,
        ClientIidIncr=None,
        ClientIpIncr=None,
        ClientNetmask=None,
        ClientNetmaskOptions=None,
        ClientPrimaryDnsAddress=None,
        ClientSecondaryDnsAddress=None,
        ClientSignalIwf=None,
        ClientSignalLoopChar=None,
        ClientSignalLoopEncapsulation=None,
        ClientSignalLoopId=None,
        DataLink=None,
        DnsServerList=None,
        DomainList=None,
        EchoReqInterval=None,
        EnableDnsRa=None,
        EnableDomainGroups=None,
        EnableEchoReq=None,
        EnableEchoRsp=None,
        EnableIncludeTagInPadi=None,
        EnableIncludeTagInPado=None,
        EnableIncludeTagInPadr=None,
        EnableIncludeTagInPads=None,
        EnableIntermediateAgentTags=None,
        EnableMaxPayload=None,
        EnableMru=None,
        EnableMruNegotiation=None,
        EnablePasswordCheck=None,
        EnableRedial=None,
        Enabled=None,
        Encaps1=None,
        Encaps2=None,
        Ipv6AddrPrefixLen=None,
        Ipv6PoolPrefix=None,
        Ipv6PoolPrefixLen=None,
        LcpOptions=None,
        LcpRetries=None,
        LcpTermRetries=None,
        LcpTermTimeout=None,
        LcpTimeout=None,
        MaxPayload=None,
        Mtu=None,
        Name=None,
        NcpRetries=None,
        NcpTimeout=None,
        NcpType=None,
        NumSessions=None,
        PadiRetries=None,
        PadiTimeout=None,
        PadrRetries=None,
        PadrTimeout=None,
        PapPassword=None,
        PapUser=None,
        PppoeOptions=None,
        RedialMax=None,
        RedialTimeout=None,
        ServerBaseIid=None,
        ServerBaseIp=None,
        ServerDnsOptions=None,
        ServerIidIncr=None,
        ServerIpIncr=None,
        ServerNetmask=None,
        ServerNetmaskOptions=None,
        ServerPrimaryDnsAddress=None,
        ServerSecondaryDnsAddress=None,
        ServerSignalIwf=None,
        ServerSignalLoopChar=None,
        ServerSignalLoopEncapsulation=None,
        ServerSignalLoopId=None,
        ServiceName=None,
        ServiceOptions=None,
        UnlimitedRedialAttempts=None,
        UseMagic=None,
    ):
        # type: (str, str, int, int, str, str, str, int, int, str, str, str, str, str, str, int, str, str, str, str, str, bool, bool, bool, bool, str, str, str, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, int, str, int, str, int, int, int, int, int, int, str, int, int, str, int, int, int, int, int, str, str, str, int, int, str, str, str, int, str, str, str, str, str, bool, bool, bool, bool, str, str, bool, bool) -> PppoxRange
        """Updates pppoxRange resource on the server.

        Args
        ----
        - AcName (str): Access Concentrator Name - this option is only available for PPP servers.
        - AcOptions (str): Indicates PPPoE AC retrieval mode
        - ActualRateDownstream (number): Actual Data Rate Downstream Value (TR-101 suboption 0x82)
        - ActualRateUpstream (number): Actual Data Rate Upstream Value (TR-101 suboption 0x81)
        - AgentCircuitId (str): Agent Circuit ID (TR-101 suboption 0x01)
        - AgentRemoteId (str): Agent Remote ID (TR-101 suboption 0x02)
        - AuthOptions (str): For GUI grouping.
        - AuthRetries (number): Number of PPP authentication retries
        - AuthTimeout (number): Timeout for PPP authentication, in seconds.
        - AuthType (str): Authentication type
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
        - ClientSignalIwf (bool): Enables the sending of the interworked session (0xFE) TR-101 suboption in client PPPoE messages (PADI/PADR/PADT)
        - ClientSignalLoopChar (bool): Enables the sending of the access loop characteristics TR-101 suboptions in client PPPoE messages (PADI/PADR/PADT)
        - ClientSignalLoopEncapsulation (bool): Enables the sending of the loop encapsulation (0x90) TR-101 suboption in client PPPoE messages (PADI/PADR/PADT)
        - ClientSignalLoopId (bool): Enables the sending of the remote ID and circuit ID TR-101 suboptions in client PPPoE messages (PADI/PADR/PADT)
        - DataLink (str): Data Link for TR-101 suboption 0x90
        - DnsServerList (str): DNS server list separacted by semicolon
        - DomainList (str): Configure domain group settings
        - EchoReqInterval (number): Keep alive interval
        - EnableDnsRa (bool): Enable RDNSS routing advertisments
        - EnableDomainGroups (bool): Enable domain groups
        - EnableEchoReq (bool): Enable Echo requests
        - EnableEchoRsp (bool): Enable Echo replies
        - EnableIncludeTagInPadi (bool): OBSOLETE - If checked, PADI messages include Intermediate Agent Tags(only for PPP client)
        - EnableIncludeTagInPado (bool): OBSOLETE - If checked, PADO messages include Intermediate Agent Tags(only for PPP server)
        - EnableIncludeTagInPadr (bool): OBSOLETE - If checked, PADR messages include Intermediate Agent Tags(only for PPP client)
        - EnableIncludeTagInPads (bool): OBSOLETE - If checked, PADs messages include Intermediate Agent Tags(only for PPP server)
        - EnableIntermediateAgentTags (bool): OBSOLETE - If checked, Intermediate Agent Tags are enabled
        - EnableMaxPayload (bool): Enable/Disable Max Payload
        - EnableMru (bool): Enable/Disable MRU negotiation
        - EnableMruNegotiation (bool): Option is deprecated. Please use enableMaxPayload. If checked, MRU negotiation is enabled
        - EnablePasswordCheck (bool): Enable authentication credential checking on the port.
        - EnableRedial (bool): Enable/Disable PPPoE redial
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Encaps1 (str): Encapsulation 1 for TR-101 suboption 0x90
        - Encaps2 (str): Encapsulation 2 for TR-101 suboption 0x90
        - Ipv6AddrPrefixLen (number): IPv6 Address Prefix Length
        - Ipv6PoolPrefix (str): Pool prefix for the IPv6 IP pool.
        - Ipv6PoolPrefixLen (number): IPv6 Pool Prefix Length
        - LcpOptions (str): For GUI grouping.
        - LcpRetries (number): Number of LCP retries
        - LcpTermRetries (number): Number of LCP Termination Retries
        - LcpTermTimeout (number): Timeout for LCP termination, in seconds.
        - LcpTimeout (number): Timeout for LCP phase, in seconds
        - MaxPayload (number): Max Payload
        - Mtu (number): Max Transmit Unit for PPP
        - Name (str): Name of range
        - NcpRetries (number): Number of NCP retries
        - NcpTimeout (number): Timeout for NCP phase, in seconds
        - NcpType (str): IP type (IPv4/IPv6) for Network Control Protocol
        - NumSessions (number): No. of sessions to setup
        - PadiRetries (number): Number of PADI Retries
        - PadiTimeout (number): Timeout for PADI no response, in seconds
        - PadrRetries (number): Number of PADR Retries
        - PadrTimeout (number): Timeout for PADR no response, in seconds
        - PapPassword (str): Password when PAP Authentication is being used
        - PapUser (str): User name when PAP Authentication is being used
        - PppoeOptions (str): For GUI grouping.
        - RedialMax (number): Maximum number of PPPoE redials
        - RedialTimeout (number): PPPoE redial timeout, in seconds
        - ServerBaseIid (str): Base for IPv6CP interface identifiers assigned to servers.
        - ServerBaseIp (str): Base for IPv4 PPP server address creation
        - ServerDnsOptions (str): Server DNS options
        - ServerIidIncr (number): Increment for IPv6CP server interface identifiers.
        - ServerIpIncr (str): *For internal use only*. For PPP/IP v4 server plugins, exactly one server address is used. As a result, 0.0.0.0 is the only legal value for this property.
        - ServerNetmask (str): Netmask that the server should supply to clients
        - ServerNetmaskOptions (str): Server netmask options
        - ServerPrimaryDnsAddress (str): Primary DNS server address supplied by server
        - ServerSecondaryDnsAddress (str): Secondary DNS server address supplied by server
        - ServerSignalIwf (bool): If enabled, the PPPoE server echoes the interworked session TR-101 suboption received in messages from the client
        - ServerSignalLoopChar (bool): If enabled, the PPPoE server echoes the loop characteristics TR-101 suboptions received in messages from the client
        - ServerSignalLoopEncapsulation (bool): If enabled, the PPPoE server echoes the loop encapsulation (0x90) TR-101 suboption received in messages from the client
        - ServerSignalLoopId (bool): If enabled, the PPPoE server echoes the remote ID and circuit ID TR-101 suboptions received in messages from the client
        - ServiceName (str): Access Concentrator Service Name - this option is only available for PPP servers.
        - ServiceOptions (str): Indicates PPPoE service retrieval mode
        - UnlimitedRedialAttempts (bool): Enable/Disable PPPoE unlimited redial attempts
        - UseMagic (bool): use magic

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AcName=None,
        AcOptions=None,
        ActualRateDownstream=None,
        ActualRateUpstream=None,
        AgentCircuitId=None,
        AgentRemoteId=None,
        AuthOptions=None,
        AuthRetries=None,
        AuthTimeout=None,
        AuthType=None,
        ChapName=None,
        ChapSecret=None,
        ClientBaseIid=None,
        ClientBaseIp=None,
        ClientDnsOptions=None,
        ClientIidIncr=None,
        ClientIpIncr=None,
        ClientNetmask=None,
        ClientNetmaskOptions=None,
        ClientPrimaryDnsAddress=None,
        ClientSecondaryDnsAddress=None,
        ClientSignalIwf=None,
        ClientSignalLoopChar=None,
        ClientSignalLoopEncapsulation=None,
        ClientSignalLoopId=None,
        DataLink=None,
        DnsServerList=None,
        DomainList=None,
        EchoReqInterval=None,
        EnableDnsRa=None,
        EnableDomainGroups=None,
        EnableEchoReq=None,
        EnableEchoRsp=None,
        EnableIncludeTagInPadi=None,
        EnableIncludeTagInPado=None,
        EnableIncludeTagInPadr=None,
        EnableIncludeTagInPads=None,
        EnableIntermediateAgentTags=None,
        EnableMaxPayload=None,
        EnableMru=None,
        EnableMruNegotiation=None,
        EnablePasswordCheck=None,
        EnableRedial=None,
        Enabled=None,
        Encaps1=None,
        Encaps2=None,
        Ipv6AddrPrefixLen=None,
        Ipv6PoolPrefix=None,
        Ipv6PoolPrefixLen=None,
        LcpOptions=None,
        LcpRetries=None,
        LcpTermRetries=None,
        LcpTermTimeout=None,
        LcpTimeout=None,
        MaxPayload=None,
        Mtu=None,
        Name=None,
        NcpRetries=None,
        NcpTimeout=None,
        NcpType=None,
        NumSessions=None,
        ObjectId=None,
        PadiRetries=None,
        PadiTimeout=None,
        PadrRetries=None,
        PadrTimeout=None,
        PapPassword=None,
        PapUser=None,
        PppoeOptions=None,
        RedialMax=None,
        RedialTimeout=None,
        ServerBaseIid=None,
        ServerBaseIp=None,
        ServerDnsOptions=None,
        ServerIidIncr=None,
        ServerIpIncr=None,
        ServerNetmask=None,
        ServerNetmaskOptions=None,
        ServerPrimaryDnsAddress=None,
        ServerSecondaryDnsAddress=None,
        ServerSignalIwf=None,
        ServerSignalLoopChar=None,
        ServerSignalLoopEncapsulation=None,
        ServerSignalLoopId=None,
        ServiceName=None,
        ServiceOptions=None,
        UnlimitedRedialAttempts=None,
        UseMagic=None,
    ):
        # type: (str, str, int, int, str, str, str, int, int, str, str, str, str, str, str, int, str, str, str, str, str, bool, bool, bool, bool, str, str, str, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, int, str, int, str, int, int, int, int, int, int, str, int, int, str, int, str, int, int, int, int, str, str, str, int, int, str, str, str, int, str, str, str, str, str, bool, bool, bool, bool, str, str, bool, bool) -> PppoxRange
        """Finds and retrieves pppoxRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pppoxRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pppoxRange resources from the server.

        Args
        ----
        - AcName (str): Access Concentrator Name - this option is only available for PPP servers.
        - AcOptions (str): Indicates PPPoE AC retrieval mode
        - ActualRateDownstream (number): Actual Data Rate Downstream Value (TR-101 suboption 0x82)
        - ActualRateUpstream (number): Actual Data Rate Upstream Value (TR-101 suboption 0x81)
        - AgentCircuitId (str): Agent Circuit ID (TR-101 suboption 0x01)
        - AgentRemoteId (str): Agent Remote ID (TR-101 suboption 0x02)
        - AuthOptions (str): For GUI grouping.
        - AuthRetries (number): Number of PPP authentication retries
        - AuthTimeout (number): Timeout for PPP authentication, in seconds.
        - AuthType (str): Authentication type
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
        - ClientSignalIwf (bool): Enables the sending of the interworked session (0xFE) TR-101 suboption in client PPPoE messages (PADI/PADR/PADT)
        - ClientSignalLoopChar (bool): Enables the sending of the access loop characteristics TR-101 suboptions in client PPPoE messages (PADI/PADR/PADT)
        - ClientSignalLoopEncapsulation (bool): Enables the sending of the loop encapsulation (0x90) TR-101 suboption in client PPPoE messages (PADI/PADR/PADT)
        - ClientSignalLoopId (bool): Enables the sending of the remote ID and circuit ID TR-101 suboptions in client PPPoE messages (PADI/PADR/PADT)
        - DataLink (str): Data Link for TR-101 suboption 0x90
        - DnsServerList (str): DNS server list separacted by semicolon
        - DomainList (str): Configure domain group settings
        - EchoReqInterval (number): Keep alive interval
        - EnableDnsRa (bool): Enable RDNSS routing advertisments
        - EnableDomainGroups (bool): Enable domain groups
        - EnableEchoReq (bool): Enable Echo requests
        - EnableEchoRsp (bool): Enable Echo replies
        - EnableIncludeTagInPadi (bool): OBSOLETE - If checked, PADI messages include Intermediate Agent Tags(only for PPP client)
        - EnableIncludeTagInPado (bool): OBSOLETE - If checked, PADO messages include Intermediate Agent Tags(only for PPP server)
        - EnableIncludeTagInPadr (bool): OBSOLETE - If checked, PADR messages include Intermediate Agent Tags(only for PPP client)
        - EnableIncludeTagInPads (bool): OBSOLETE - If checked, PADs messages include Intermediate Agent Tags(only for PPP server)
        - EnableIntermediateAgentTags (bool): OBSOLETE - If checked, Intermediate Agent Tags are enabled
        - EnableMaxPayload (bool): Enable/Disable Max Payload
        - EnableMru (bool): Enable/Disable MRU negotiation
        - EnableMruNegotiation (bool): Option is deprecated. Please use enableMaxPayload. If checked, MRU negotiation is enabled
        - EnablePasswordCheck (bool): Enable authentication credential checking on the port.
        - EnableRedial (bool): Enable/Disable PPPoE redial
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Encaps1 (str): Encapsulation 1 for TR-101 suboption 0x90
        - Encaps2 (str): Encapsulation 2 for TR-101 suboption 0x90
        - Ipv6AddrPrefixLen (number): IPv6 Address Prefix Length
        - Ipv6PoolPrefix (str): Pool prefix for the IPv6 IP pool.
        - Ipv6PoolPrefixLen (number): IPv6 Pool Prefix Length
        - LcpOptions (str): For GUI grouping.
        - LcpRetries (number): Number of LCP retries
        - LcpTermRetries (number): Number of LCP Termination Retries
        - LcpTermTimeout (number): Timeout for LCP termination, in seconds.
        - LcpTimeout (number): Timeout for LCP phase, in seconds
        - MaxPayload (number): Max Payload
        - Mtu (number): Max Transmit Unit for PPP
        - Name (str): Name of range
        - NcpRetries (number): Number of NCP retries
        - NcpTimeout (number): Timeout for NCP phase, in seconds
        - NcpType (str): IP type (IPv4/IPv6) for Network Control Protocol
        - NumSessions (number): No. of sessions to setup
        - ObjectId (str): Unique identifier for this object
        - PadiRetries (number): Number of PADI Retries
        - PadiTimeout (number): Timeout for PADI no response, in seconds
        - PadrRetries (number): Number of PADR Retries
        - PadrTimeout (number): Timeout for PADR no response, in seconds
        - PapPassword (str): Password when PAP Authentication is being used
        - PapUser (str): User name when PAP Authentication is being used
        - PppoeOptions (str): For GUI grouping.
        - RedialMax (number): Maximum number of PPPoE redials
        - RedialTimeout (number): PPPoE redial timeout, in seconds
        - ServerBaseIid (str): Base for IPv6CP interface identifiers assigned to servers.
        - ServerBaseIp (str): Base for IPv4 PPP server address creation
        - ServerDnsOptions (str): Server DNS options
        - ServerIidIncr (number): Increment for IPv6CP server interface identifiers.
        - ServerIpIncr (str): *For internal use only*. For PPP/IP v4 server plugins, exactly one server address is used. As a result, 0.0.0.0 is the only legal value for this property.
        - ServerNetmask (str): Netmask that the server should supply to clients
        - ServerNetmaskOptions (str): Server netmask options
        - ServerPrimaryDnsAddress (str): Primary DNS server address supplied by server
        - ServerSecondaryDnsAddress (str): Secondary DNS server address supplied by server
        - ServerSignalIwf (bool): If enabled, the PPPoE server echoes the interworked session TR-101 suboption received in messages from the client
        - ServerSignalLoopChar (bool): If enabled, the PPPoE server echoes the loop characteristics TR-101 suboptions received in messages from the client
        - ServerSignalLoopEncapsulation (bool): If enabled, the PPPoE server echoes the loop encapsulation (0x90) TR-101 suboption received in messages from the client
        - ServerSignalLoopId (bool): If enabled, the PPPoE server echoes the remote ID and circuit ID TR-101 suboptions received in messages from the client
        - ServiceName (str): Access Concentrator Service Name - this option is only available for PPP servers.
        - ServiceOptions (str): Indicates PPPoE service retrieval mode
        - UnlimitedRedialAttempts (bool): Enable/Disable PPPoE unlimited redial attempts
        - UseMagic (bool): use magic

        Returns
        -------
        - self: This instance with matching pppoxRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pppoxRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pppoxRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "customProtocolStack", payload=payload, response_object=None
        )

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "disableProtocolStack", payload=payload, response_object=None
        )

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "enableProtocolStack", payload=payload, response_object=None
        )
