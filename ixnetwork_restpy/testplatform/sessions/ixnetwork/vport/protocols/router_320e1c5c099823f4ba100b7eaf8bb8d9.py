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


class Router(Base):
    """The object represents a simulated router. In addition to some identifying options, it holds two lists for the router: (1) Route ranges-routes to be advertised by the simulated router. (2) Interfaces-router interface.
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "router"
    _SDM_ATT_MAP = {
        "AreaAddressList": "areaAddressList",
        "AreaAuthType": "areaAuthType",
        "AreaReceivedPasswordList": "areaReceivedPasswordList",
        "AreaTransmitPassword": "areaTransmitPassword",
        "BroadcastRootPriority": "broadcastRootPriority",
        "CapabilityRouterId": "capabilityRouterId",
        "DeviceId": "deviceId",
        "DevicePriority": "devicePriority",
        "DomainAuthType": "domainAuthType",
        "DomainReceivedPasswordList": "domainReceivedPasswordList",
        "DomainTransmitPassword": "domainTransmitPassword",
        "EnableAttached": "enableAttached",
        "EnableAutoLoopback": "enableAutoLoopback",
        "EnableDiscardLearnedLsps": "enableDiscardLearnedLsps",
        "EnableHelloPadding": "enableHelloPadding",
        "EnableHitlessRestart": "enableHitlessRestart",
        "EnableHostName": "enableHostName",
        "EnableIgnoreMtPortCapability": "enableIgnoreMtPortCapability",
        "EnableIgnoreRecvMd5": "enableIgnoreRecvMd5",
        "EnableMtIpv6": "enableMtIpv6",
        "EnableMtuProbe": "enableMtuProbe",
        "EnableMultiTopology": "enableMultiTopology",
        "EnableOverloaded": "enableOverloaded",
        "EnablePartitionRepair": "enablePartitionRepair",
        "EnableTrillOam": "enableTrillOam",
        "EnableWideMetric": "enableWideMetric",
        "Enabled": "enabled",
        "FTagValue": "fTagValue",
        "FilterIpv4MulticastTlvs": "filterIpv4MulticastTlvs",
        "FilterIpv6MulticastTlvs": "filterIpv6MulticastTlvs",
        "FilterLearnedIpv4Prefixes": "filterLearnedIpv4Prefixes",
        "FilterLearnedIpv6Prefixes": "filterLearnedIpv6Prefixes",
        "FilterLearnedRbridges": "filterLearnedRbridges",
        "FilterLearnedSpbRbridges": "filterLearnedSpbRbridges",
        "FilterLearnedTrillMacUnicast": "filterLearnedTrillMacUnicast",
        "FilterMacMulticastTlvs": "filterMacMulticastTlvs",
        "HostName": "hostName",
        "InterLspMgroupPduBurstGap": "interLspMgroupPduBurstGap",
        "LspLifeTime": "lspLifeTime",
        "LspMaxSize": "lspMaxSize",
        "LspMgroupPduMinTransmissionInterval": "lspMgroupPduMinTransmissionInterval",
        "LspRefreshRate": "lspRefreshRate",
        "MaxAreaAddresses": "maxAreaAddresses",
        "MaxLspMgroupPdusPerBurst": "maxLspMgroupPdusPerBurst",
        "NumberOfMtuProbes": "numberOfMtuProbes",
        "NumberOfMultiDestinationTrees": "numberOfMultiDestinationTrees",
        "OriginatingLspBufSize": "originatingLspBufSize",
        "PsnpInterval": "psnpInterval",
        "RestartMode": "restartMode",
        "RestartTime": "restartTime",
        "RestartVersion": "restartVersion",
        "StartFtagValue": "startFtagValue",
        "SwitchId": "switchId",
        "SwitchIdPriority": "switchIdPriority",
        "SystemId": "systemId",
        "TeEnable": "teEnable",
        "TeRouterId": "teRouterId",
        "TrafficGroupId": "trafficGroupId",
    }
    _SDM_ENUM_MAP = {
        "areaAuthType": ["none", "password", "md5"],
        "domainAuthType": ["none", "password", "md5"],
        "restartMode": [
            "normalRouter",
            "restartingRouter",
            "startingRouter",
            "helperRouter",
        ],
        "restartVersion": ["version3", "version4"],
    }

    def __init__(self, parent, list_op=False):
        super(Router, self).__init__(parent, list_op)

    @property
    def CustomTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtlv_9b3af0590ed159139a0d6ee63aafb653.CustomTlv): An instance of the CustomTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtlv_9b3af0590ed159139a0d6ee63aafb653 import (
            CustomTlv,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CustomTlv", None) is not None:
                return self._properties.get("CustomTlv")
        return CustomTlv(self)

    @property
    def CustomTopology(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopology_95c201c50eb168382a558d283f2bec6c.CustomTopology): An instance of the CustomTopology class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopology_95c201c50eb168382a558d283f2bec6c import (
            CustomTopology,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CustomTopology", None) is not None:
                return self._properties.get("CustomTopology")
        return CustomTopology(self)

    @property
    def DceMulticastIpv4GroupRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcemulticastipv4grouprange_137811bdde8c702243d4c46d844116e9.DceMulticastIpv4GroupRange): An instance of the DceMulticastIpv4GroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcemulticastipv4grouprange_137811bdde8c702243d4c46d844116e9 import (
            DceMulticastIpv4GroupRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DceMulticastIpv4GroupRange", None) is not None:
                return self._properties.get("DceMulticastIpv4GroupRange")
        return DceMulticastIpv4GroupRange(self)

    @property
    def DceMulticastIpv6GroupRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcemulticastipv6grouprange_ff34b9b498a42af784ac1d9e6870d89b.DceMulticastIpv6GroupRange): An instance of the DceMulticastIpv6GroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcemulticastipv6grouprange_ff34b9b498a42af784ac1d9e6870d89b import (
            DceMulticastIpv6GroupRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DceMulticastIpv6GroupRange", None) is not None:
                return self._properties.get("DceMulticastIpv6GroupRange")
        return DceMulticastIpv6GroupRange(self)

    @property
    def DceMulticastMacRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcemulticastmacrange_cc6bbd6d9c9c0e88f6e630afd3a84823.DceMulticastMacRange): An instance of the DceMulticastMacRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcemulticastmacrange_cc6bbd6d9c9c0e88f6e630afd3a84823 import (
            DceMulticastMacRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DceMulticastMacRange", None) is not None:
                return self._properties.get("DceMulticastMacRange")
        return DceMulticastMacRange(self)

    @property
    def DceNetworkRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenetworkrange_de592cf3e2529092f28b2f14e5282a24.DceNetworkRange): An instance of the DceNetworkRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenetworkrange_de592cf3e2529092f28b2f14e5282a24 import (
            DceNetworkRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DceNetworkRange", None) is not None:
                return self._properties.get("DceNetworkRange")
        return DceNetworkRange(self)

    @property
    def DceTopologyRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcetopologyrange_e13ee59af806de98161bf79b499b2a3b.DceTopologyRange): An instance of the DceTopologyRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcetopologyrange_e13ee59af806de98161bf79b499b2a3b import (
            DceTopologyRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DceTopologyRange", None) is not None:
                return self._properties.get("DceTopologyRange")
        return DceTopologyRange(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_54e892c04a4d57ef720d90ef82e8d6e6.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_54e892c04a4d57ef720d90ef82e8d6e6 import (
            Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Interface", None) is not None:
                return self._properties.get("Interface")
        return Interface(self)

    @property
    def LearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinformation_bc2e368143330cd32a96af7ea8b5bb3a.LearnedInformation): An instance of the LearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinformation_bc2e368143330cd32a96af7ea8b5bb3a import (
            LearnedInformation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedInformation", None) is not None:
                return self._properties.get("LearnedInformation")
        return LearnedInformation(self)._select()

    @property
    def NetworkRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.networkrange_13f65c2451ab57b34c6f824d4665d3ea.NetworkRange): An instance of the NetworkRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.networkrange_13f65c2451ab57b34c6f824d4665d3ea import (
            NetworkRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NetworkRange", None) is not None:
                return self._properties.get("NetworkRange")
        return NetworkRange(self)

    @property
    def RouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_f356b867b4b5aaa0b94fb4b00d34a328.RouteRange): An instance of the RouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_f356b867b4b5aaa0b94fb4b00d34a328 import (
            RouteRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RouteRange", None) is not None:
                return self._properties.get("RouteRange")
        return RouteRange(self)

    @property
    def SpbNetworkRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbnetworkrange_d4c634041e8e33458ec27f522c953b2a.SpbNetworkRange): An instance of the SpbNetworkRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbnetworkrange_d4c634041e8e33458ec27f522c953b2a import (
            SpbNetworkRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SpbNetworkRange", None) is not None:
                return self._properties.get("SpbNetworkRange")
        return SpbNetworkRange(self)

    @property
    def SpbTopologyRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbtopologyrange_922b3eacc2d72dd7a24481d9cb1ee831.SpbTopologyRange): An instance of the SpbTopologyRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbtopologyrange_922b3eacc2d72dd7a24481d9cb1ee831 import (
            SpbTopologyRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SpbTopologyRange", None) is not None:
                return self._properties.get("SpbTopologyRange")
        return SpbTopologyRange(self)

    @property
    def TrillPingOam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillpingoam_1ad2c6d3f05ae8ebfc87ba18f1512d39.TrillPingOam): An instance of the TrillPingOam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillpingoam_1ad2c6d3f05ae8ebfc87ba18f1512d39 import (
            TrillPingOam,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrillPingOam", None) is not None:
                return self._properties.get("TrillPingOam")
        return TrillPingOam(self)._select()

    @property
    def TrillUnicastMacRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillunicastmacrange_1a357144d008fb5372e816e033477ead.TrillUnicastMacRange): An instance of the TrillUnicastMacRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillunicastmacrange_1a357144d008fb5372e816e033477ead import (
            TrillUnicastMacRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrillUnicastMacRange", None) is not None:
                return self._properties.get("TrillUnicastMacRange")
        return TrillUnicastMacRange(self)

    @property
    def AreaAddressList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The list of area addresses to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AreaAddressList"])

    @AreaAddressList.setter
    def AreaAddressList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["AreaAddressList"], value)

    @property
    def AreaAuthType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(none | password | md5): Sets up authentication for Level 1 LSPs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AreaAuthType"])

    @AreaAuthType.setter
    def AreaAuthType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AreaAuthType"], value)

    @property
    def AreaReceivedPasswordList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): If areaAuthType is isisAuthTypePassword, then this is a list of passwords that the router will accept on received LSPs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AreaReceivedPasswordList"])

    @AreaReceivedPasswordList.setter
    def AreaReceivedPasswordList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["AreaReceivedPasswordList"], value)

    @property
    def AreaTransmitPassword(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If areaAuthType is isisAuthTypePassword, then this is the password (or MD5Key) that will be sent with transmitted LSPs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AreaTransmitPassword"])

    @AreaTransmitPassword.setter
    def AreaTransmitPassword(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AreaTransmitPassword"], value)

    @property
    def BroadcastRootPriority(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: The value of the Broadcast Root Priority of a particular DCE ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BroadcastRootPriority"])

    @BroadcastRootPriority.setter
    def BroadcastRootPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BroadcastRootPriority"], value)

    @property
    def CapabilityRouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IPv4 address format of the Capability Router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CapabilityRouterId"])

    @CapabilityRouterId.setter
    def CapabilityRouterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CapabilityRouterId"], value)

    @property
    def DeviceId(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: This is a deprecated attribute in DCE ISIS mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeviceId"])

    @DeviceId.setter
    def DeviceId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeviceId"], value)

    @property
    def DevicePriority(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: This is a deprecated attribute in DCE ISIS mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DevicePriority"])

    @DevicePriority.setter
    def DevicePriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DevicePriority"], value)

    @property
    def DomainAuthType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(none | password | md5): Sets up authentication for Level 2 LSPs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DomainAuthType"])

    @DomainAuthType.setter
    def DomainAuthType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DomainAuthType"], value)

    @property
    def DomainReceivedPasswordList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): If domainAuthType is isisAuthTypePassword, then this is a list of passwords that the router will accept on received LSPs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DomainReceivedPasswordList"])

    @DomainReceivedPasswordList.setter
    def DomainReceivedPasswordList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["DomainReceivedPasswordList"], value)

    @property
    def DomainTransmitPassword(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If domainAuthType is isisAuthTypePassword, then this is the password (or MD5Key) that will be sent with transmitted LSPs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DomainTransmitPassword"])

    @DomainTransmitPassword.setter
    def DomainTransmitPassword(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DomainTransmitPassword"], value)

    @property
    def EnableAttached(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the Attached Flag is set. It indicates that this ISIS router can use L2 routing to reach other areas.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAttached"])

    @EnableAttached.setter
    def EnableAttached(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAttached"], value)

    @property
    def EnableAutoLoopback(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, loopback addresses are allowed in the generated routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAutoLoopback"])

    @EnableAutoLoopback.setter
    def EnableAutoLoopback(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAutoLoopback"], value)

    @property
    def EnableDiscardLearnedLsps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, LSPs learned from this router's interfaces will be discarded.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDiscardLearnedLsps"])

    @EnableDiscardLearnedLsps.setter
    def EnableDiscardLearnedLsps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDiscardLearnedLsps"], value)

    @property
    def EnableHelloPadding(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables padding of hello messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableHelloPadding"])

    @EnableHelloPadding.setter
    def EnableHelloPadding(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableHelloPadding"], value)

    @property
    def EnableHitlessRestart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Hitless Restart is enabled for this emulated ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableHitlessRestart"])

    @EnableHitlessRestart.setter
    def EnableHitlessRestart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableHitlessRestart"], value)

    @property
    def EnableHostName(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the given dynamic host name is transmitted in all the packets sent from this router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableHostName"])

    @EnableHostName.setter
    def EnableHostName(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableHostName"], value)

    @property
    def EnableIgnoreMtPortCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableIgnoreMtPortCapability"])

    @EnableIgnoreMtPortCapability.setter
    def EnableIgnoreMtPortCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableIgnoreMtPortCapability"], value)

    @property
    def EnableIgnoreRecvMd5(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MD5 authentication will be disabled for incoming/received packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableIgnoreRecvMd5"])

    @EnableIgnoreRecvMd5.setter
    def EnableIgnoreRecvMd5(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableIgnoreRecvMd5"], value)

    @property
    def EnableMtIpv6(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If checked in L3, emulation type traffic group ID at router level is grayed out and unassigned.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMtIpv6"])

    @EnableMtIpv6.setter
    def EnableMtIpv6(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMtIpv6"], value)

    @property
    def EnableMtuProbe(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMtuProbe"])

    @EnableMtuProbe.setter
    def EnableMtuProbe(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMtuProbe"], value)

    @property
    def EnableMultiTopology(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables more than one topology (distribution tree) corresponding to the given R bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMultiTopology"])

    @EnableMultiTopology.setter
    def EnableMultiTopology(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMultiTopology"], value)

    @property
    def EnableOverloaded(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the LSP Database Overload Bit is set. It indicates that the LSP database on this router is overloaded and that there is not enough memory to store a received LSP. This router enters the Waiting State and floods an LSP (with LSP number = 0) with the overload bit set, so other routers will not forward ISIS packets to it.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOverloaded"])

    @EnableOverloaded.setter
    def EnableOverloaded(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOverloaded"], value)

    @property
    def EnablePartitionRepair(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the optional partition repair option specified in ISO/IEC 10589 and RFC 1195 for Level 1 areas.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePartitionRepair"])

    @EnablePartitionRepair.setter
    def EnablePartitionRepair(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePartitionRepair"], value)

    @property
    def EnableTrillOam(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableTrillOam"])

    @EnableTrillOam.setter
    def EnableTrillOam(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableTrillOam"], value)

    @property
    def EnableWideMetric(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of extended reachability (wide) metrics (defined to support TE): 32-bits wide for IP reachability (routes) and 24-bits wide for IS reachability (IS neighbors). If TE is enabled, wide metrics will be enabled automatically. The wide metrics may be used without enabling TE, however.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableWideMetric"])

    @EnableWideMetric.setter
    def EnableWideMetric(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableWideMetric"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables the simulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def FTagValue(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: This is a deprecated attribute in DCE ISIS mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FTagValue"])

    @FTagValue.setter
    def FTagValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FTagValue"], value)

    @property
    def FilterIpv4MulticastTlvs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, retrieves IPv4 Multicast learned information in the DCE ISIS mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterIpv4MulticastTlvs"])

    @FilterIpv4MulticastTlvs.setter
    def FilterIpv4MulticastTlvs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterIpv4MulticastTlvs"], value)

    @property
    def FilterIpv6MulticastTlvs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, retrieves IPv6 Multicast learned information in the DCE ISIS mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterIpv6MulticastTlvs"])

    @FilterIpv6MulticastTlvs.setter
    def FilterIpv6MulticastTlvs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterIpv6MulticastTlvs"], value)

    @property
    def FilterLearnedIpv4Prefixes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, retrieves IPv4 Unicast learned information in the ISIS L3 Routing mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterLearnedIpv4Prefixes"])

    @FilterLearnedIpv4Prefixes.setter
    def FilterLearnedIpv4Prefixes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterLearnedIpv4Prefixes"], value)

    @property
    def FilterLearnedIpv6Prefixes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, retrieves IPv6 Unicast learned information in the ISIS L3 Routing mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterLearnedIpv6Prefixes"])

    @FilterLearnedIpv6Prefixes.setter
    def FilterLearnedIpv6Prefixes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterLearnedIpv6Prefixes"], value)

    @property
    def FilterLearnedRbridges(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, retrieves RBridges learned information in the DCE ISIS mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterLearnedRbridges"])

    @FilterLearnedRbridges.setter
    def FilterLearnedRbridges(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterLearnedRbridges"], value)

    @property
    def FilterLearnedSpbRbridges(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterLearnedSpbRbridges"])

    @FilterLearnedSpbRbridges.setter
    def FilterLearnedSpbRbridges(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterLearnedSpbRbridges"], value)

    @property
    def FilterLearnedTrillMacUnicast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterLearnedTrillMacUnicast"])

    @FilterLearnedTrillMacUnicast.setter
    def FilterLearnedTrillMacUnicast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterLearnedTrillMacUnicast"], value)

    @property
    def FilterMacMulticastTlvs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, retrieves MAC Multicast learned information in the DCE ISIS mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterMacMulticastTlvs"])

    @FilterMacMulticastTlvs.setter
    def FilterMacMulticastTlvs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterMacMulticastTlvs"], value)

    @property
    def HostName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Allows to add a host name to this router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostName"])

    @HostName.setter
    def HostName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["HostName"], value)

    @property
    def InterLspMgroupPduBurstGap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the gap between each LSP MGROUP-PDUs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterLspMgroupPduBurstGap"])

    @InterLspMgroupPduBurstGap.setter
    def InterLspMgroupPduBurstGap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterLspMgroupPduBurstGap"], value)

    @property
    def LspLifeTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (in sec) The MaxAge for retaining a learned LSP on this router. The default value is 1,200 sec.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspLifeTime"])

    @LspLifeTime.setter
    def LspLifeTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspLifeTime"], value)

    @property
    def LspMaxSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (in bytes) The maximum allowable length of an ISIS LSP message. The default is 1,492 bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspMaxSize"])

    @LspMaxSize.setter
    def LspMaxSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspMaxSize"], value)

    @property
    def LspMgroupPduMinTransmissionInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the minimum wait time for each LSP MGROUP-PDU transmission.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["LspMgroupPduMinTransmissionInterval"]
        )

    @LspMgroupPduMinTransmissionInterval.setter
    def LspMgroupPduMinTransmissionInterval(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["LspMgroupPduMinTransmissionInterval"], value
        )

    @property
    def LspRefreshRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (in sec) The rate at which LSPs are resent. The default value is 900 sec.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspRefreshRate"])

    @LspRefreshRate.setter
    def LspRefreshRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LspRefreshRate"], value)

    @property
    def MaxAreaAddresses(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of area addresses permitted for this IS area.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxAreaAddresses"])

    @MaxAreaAddresses.setter
    def MaxAreaAddresses(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxAreaAddresses"], value)

    @property
    def MaxLspMgroupPdusPerBurst(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the maximum number of LSP MGROUP-PDUs for each burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxLspMgroupPdusPerBurst"])

    @MaxLspMgroupPdusPerBurst.setter
    def MaxLspMgroupPdusPerBurst(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxLspMgroupPdusPerBurst"], value)

    @property
    def NumberOfMtuProbes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfMtuProbes"])

    @NumberOfMtuProbes.setter
    def NumberOfMtuProbes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfMtuProbes"], value)

    @property
    def NumberOfMultiDestinationTrees(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: The number of Multi-Destination Trees for the emulated DCE ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfMultiDestinationTrees"])

    @NumberOfMultiDestinationTrees.setter
    def NumberOfMultiDestinationTrees(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfMultiDestinationTrees"], value)

    @property
    def OriginatingLspBufSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["OriginatingLspBufSize"])

    @OriginatingLspBufSize.setter
    def OriginatingLspBufSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OriginatingLspBufSize"], value)

    @property
    def PsnpInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The PSPN Interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PsnpInterval"])

    @PsnpInterval.setter
    def PsnpInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PsnpInterval"], value)

    @property
    def RestartMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(normalRouter | restartingRouter | startingRouter | helperRouter): If enableHitlessRestart is true, this indicates the mode in which this router is to operate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RestartMode"])

    @RestartMode.setter
    def RestartMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RestartMode"], value)

    @property
    def RestartTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Enter the restart time in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RestartTime"])

    @RestartTime.setter
    def RestartTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RestartTime"], value)

    @property
    def RestartVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str(version3 | version4): If enableHitlessRestart is true, this indicates the version of the draft-ietf-isis-restart-nn document that the router should conform to.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RestartVersion"])

    @RestartVersion.setter
    def RestartVersion(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RestartVersion"], value)

    @property
    def StartFtagValue(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: The starting FTAG value of the emulated DCE ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartFtagValue"])

    @StartFtagValue.setter
    def StartFtagValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartFtagValue"], value)

    @property
    def SwitchId(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: The Switch ID of the emulated DCE ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchId"])

    @SwitchId.setter
    def SwitchId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchId"], value)

    @property
    def SwitchIdPriority(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: The Switch ID priority of the emulated DCE ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchIdPriority"])

    @SwitchIdPriority.setter
    def SwitchIdPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchIdPriority"], value)

    @property
    def SystemId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The neighbor's system ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SystemId"])

    @SystemId.setter
    def SystemId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SystemId"], value)

    @property
    def TeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables traffic engineering (TE) on this emulated ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TeEnable"])

    @TeEnable.setter
    def TeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TeEnable"], value)

    @property
    def TeRouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The ID of the simulated router, expressed as an IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TeRouterId"])

    @TeRouterId.setter
    def TeRouterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TeRouterId"], value)

    @property
    def TrafficGroupId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficGroupId"])

    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficGroupId"], value)

    def update(
        self,
        AreaAddressList=None,
        AreaAuthType=None,
        AreaReceivedPasswordList=None,
        AreaTransmitPassword=None,
        BroadcastRootPriority=None,
        CapabilityRouterId=None,
        DeviceId=None,
        DevicePriority=None,
        DomainAuthType=None,
        DomainReceivedPasswordList=None,
        DomainTransmitPassword=None,
        EnableAttached=None,
        EnableAutoLoopback=None,
        EnableDiscardLearnedLsps=None,
        EnableHelloPadding=None,
        EnableHitlessRestart=None,
        EnableHostName=None,
        EnableIgnoreMtPortCapability=None,
        EnableIgnoreRecvMd5=None,
        EnableMtIpv6=None,
        EnableMtuProbe=None,
        EnableMultiTopology=None,
        EnableOverloaded=None,
        EnablePartitionRepair=None,
        EnableTrillOam=None,
        EnableWideMetric=None,
        Enabled=None,
        FTagValue=None,
        FilterIpv4MulticastTlvs=None,
        FilterIpv6MulticastTlvs=None,
        FilterLearnedIpv4Prefixes=None,
        FilterLearnedIpv6Prefixes=None,
        FilterLearnedRbridges=None,
        FilterLearnedSpbRbridges=None,
        FilterLearnedTrillMacUnicast=None,
        FilterMacMulticastTlvs=None,
        HostName=None,
        InterLspMgroupPduBurstGap=None,
        LspLifeTime=None,
        LspMaxSize=None,
        LspMgroupPduMinTransmissionInterval=None,
        LspRefreshRate=None,
        MaxAreaAddresses=None,
        MaxLspMgroupPdusPerBurst=None,
        NumberOfMtuProbes=None,
        NumberOfMultiDestinationTrees=None,
        OriginatingLspBufSize=None,
        PsnpInterval=None,
        RestartMode=None,
        RestartTime=None,
        RestartVersion=None,
        StartFtagValue=None,
        SwitchId=None,
        SwitchIdPriority=None,
        SystemId=None,
        TeEnable=None,
        TeRouterId=None,
        TrafficGroupId=None,
    ):
        # type: (List[str], str, List[str], str, int, str, int, int, str, List[str], str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, bool, bool, bool, bool, bool, bool, bool, bool, str, int, int, int, int, int, int, int, int, int, int, int, str, int, str, int, int, int, str, bool, str, str) -> Router
        """Updates router resource on the server.

        Args
        ----
        - AreaAddressList (list(str)): The list of area addresses to use.
        - AreaAuthType (str(none | password | md5)): Sets up authentication for Level 1 LSPs.
        - AreaReceivedPasswordList (list(str)): If areaAuthType is isisAuthTypePassword, then this is a list of passwords that the router will accept on received LSPs.
        - AreaTransmitPassword (str): If areaAuthType is isisAuthTypePassword, then this is the password (or MD5Key) that will be sent with transmitted LSPs.
        - BroadcastRootPriority (number): The value of the Broadcast Root Priority of a particular DCE ISIS router.
        - CapabilityRouterId (str): The IPv4 address format of the Capability Router.
        - DeviceId (number): This is a deprecated attribute in DCE ISIS mode.
        - DevicePriority (number): This is a deprecated attribute in DCE ISIS mode.
        - DomainAuthType (str(none | password | md5)): Sets up authentication for Level 2 LSPs.
        - DomainReceivedPasswordList (list(str)): If domainAuthType is isisAuthTypePassword, then this is a list of passwords that the router will accept on received LSPs.
        - DomainTransmitPassword (str): If domainAuthType is isisAuthTypePassword, then this is the password (or MD5Key) that will be sent with transmitted LSPs.
        - EnableAttached (bool): Indicates that the Attached Flag is set. It indicates that this ISIS router can use L2 routing to reach other areas.
        - EnableAutoLoopback (bool): If enabled, loopback addresses are allowed in the generated routes.
        - EnableDiscardLearnedLsps (bool): If enabled, LSPs learned from this router's interfaces will be discarded.
        - EnableHelloPadding (bool): If true, enables padding of hello messages.
        - EnableHitlessRestart (bool): Hitless Restart is enabled for this emulated ISIS router.
        - EnableHostName (bool): If true, the given dynamic host name is transmitted in all the packets sent from this router.
        - EnableIgnoreMtPortCapability (bool): NOT DEFINED
        - EnableIgnoreRecvMd5 (bool): MD5 authentication will be disabled for incoming/received packets.
        - EnableMtIpv6 (bool): If checked in L3, emulation type traffic group ID at router level is grayed out and unassigned.
        - EnableMtuProbe (bool): NOT DEFINED
        - EnableMultiTopology (bool): Enables more than one topology (distribution tree) corresponding to the given R bridge.
        - EnableOverloaded (bool): If enabled, the LSP Database Overload Bit is set. It indicates that the LSP database on this router is overloaded and that there is not enough memory to store a received LSP. This router enters the Waiting State and floods an LSP (with LSP number = 0) with the overload bit set, so other routers will not forward ISIS packets to it.
        - EnablePartitionRepair (bool): Enables the optional partition repair option specified in ISO/IEC 10589 and RFC 1195 for Level 1 areas.
        - EnableTrillOam (bool): NOT DEFINED
        - EnableWideMetric (bool): Enables the use of extended reachability (wide) metrics (defined to support TE): 32-bits wide for IP reachability (routes) and 24-bits wide for IS reachability (IS neighbors). If TE is enabled, wide metrics will be enabled automatically. The wide metrics may be used without enabling TE, however.
        - Enabled (bool): Enables or disables the simulated router.
        - FTagValue (number): This is a deprecated attribute in DCE ISIS mode.
        - FilterIpv4MulticastTlvs (bool): If true, retrieves IPv4 Multicast learned information in the DCE ISIS mode.
        - FilterIpv6MulticastTlvs (bool): If true, retrieves IPv6 Multicast learned information in the DCE ISIS mode.
        - FilterLearnedIpv4Prefixes (bool): If true, retrieves IPv4 Unicast learned information in the ISIS L3 Routing mode.
        - FilterLearnedIpv6Prefixes (bool): If true, retrieves IPv6 Unicast learned information in the ISIS L3 Routing mode.
        - FilterLearnedRbridges (bool): If true, retrieves RBridges learned information in the DCE ISIS mode.
        - FilterLearnedSpbRbridges (bool): NOT DEFINED
        - FilterLearnedTrillMacUnicast (bool): NOT DEFINED
        - FilterMacMulticastTlvs (bool): If true, retrieves MAC Multicast learned information in the DCE ISIS mode.
        - HostName (str): Allows to add a host name to this router.
        - InterLspMgroupPduBurstGap (number): Indicates the gap between each LSP MGROUP-PDUs.
        - LspLifeTime (number): (in sec) The MaxAge for retaining a learned LSP on this router. The default value is 1,200 sec.
        - LspMaxSize (number): (in bytes) The maximum allowable length of an ISIS LSP message. The default is 1,492 bytes.
        - LspMgroupPduMinTransmissionInterval (number): Indicates the minimum wait time for each LSP MGROUP-PDU transmission.
        - LspRefreshRate (number): (in sec) The rate at which LSPs are resent. The default value is 900 sec.
        - MaxAreaAddresses (number): The number of area addresses permitted for this IS area.
        - MaxLspMgroupPdusPerBurst (number): Indicates the maximum number of LSP MGROUP-PDUs for each burst.
        - NumberOfMtuProbes (number): NOT DEFINED
        - NumberOfMultiDestinationTrees (number): The number of Multi-Destination Trees for the emulated DCE ISIS router.
        - OriginatingLspBufSize (number): NOT DEFINED
        - PsnpInterval (number): The PSPN Interval.
        - RestartMode (str(normalRouter | restartingRouter | startingRouter | helperRouter)): If enableHitlessRestart is true, this indicates the mode in which this router is to operate.
        - RestartTime (number): Enter the restart time in seconds.
        - RestartVersion (str(version3 | version4)): If enableHitlessRestart is true, this indicates the version of the draft-ietf-isis-restart-nn document that the router should conform to.
        - StartFtagValue (number): The starting FTAG value of the emulated DCE ISIS router.
        - SwitchId (number): The Switch ID of the emulated DCE ISIS router.
        - SwitchIdPriority (number): The Switch ID priority of the emulated DCE ISIS router.
        - SystemId (str): The neighbor's system ID.
        - TeEnable (bool): Enables traffic engineering (TE) on this emulated ISIS router.
        - TeRouterId (str): The ID of the simulated router, expressed as an IP address.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AreaAddressList=None,
        AreaAuthType=None,
        AreaReceivedPasswordList=None,
        AreaTransmitPassword=None,
        BroadcastRootPriority=None,
        CapabilityRouterId=None,
        DeviceId=None,
        DevicePriority=None,
        DomainAuthType=None,
        DomainReceivedPasswordList=None,
        DomainTransmitPassword=None,
        EnableAttached=None,
        EnableAutoLoopback=None,
        EnableDiscardLearnedLsps=None,
        EnableHelloPadding=None,
        EnableHitlessRestart=None,
        EnableHostName=None,
        EnableIgnoreMtPortCapability=None,
        EnableIgnoreRecvMd5=None,
        EnableMtIpv6=None,
        EnableMtuProbe=None,
        EnableMultiTopology=None,
        EnableOverloaded=None,
        EnablePartitionRepair=None,
        EnableTrillOam=None,
        EnableWideMetric=None,
        Enabled=None,
        FTagValue=None,
        FilterIpv4MulticastTlvs=None,
        FilterIpv6MulticastTlvs=None,
        FilterLearnedIpv4Prefixes=None,
        FilterLearnedIpv6Prefixes=None,
        FilterLearnedRbridges=None,
        FilterLearnedSpbRbridges=None,
        FilterLearnedTrillMacUnicast=None,
        FilterMacMulticastTlvs=None,
        HostName=None,
        InterLspMgroupPduBurstGap=None,
        LspLifeTime=None,
        LspMaxSize=None,
        LspMgroupPduMinTransmissionInterval=None,
        LspRefreshRate=None,
        MaxAreaAddresses=None,
        MaxLspMgroupPdusPerBurst=None,
        NumberOfMtuProbes=None,
        NumberOfMultiDestinationTrees=None,
        OriginatingLspBufSize=None,
        PsnpInterval=None,
        RestartMode=None,
        RestartTime=None,
        RestartVersion=None,
        StartFtagValue=None,
        SwitchId=None,
        SwitchIdPriority=None,
        SystemId=None,
        TeEnable=None,
        TeRouterId=None,
        TrafficGroupId=None,
    ):
        # type: (List[str], str, List[str], str, int, str, int, int, str, List[str], str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, bool, bool, bool, bool, bool, bool, bool, bool, str, int, int, int, int, int, int, int, int, int, int, int, str, int, str, int, int, int, str, bool, str, str) -> Router
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - AreaAddressList (list(str)): The list of area addresses to use.
        - AreaAuthType (str(none | password | md5)): Sets up authentication for Level 1 LSPs.
        - AreaReceivedPasswordList (list(str)): If areaAuthType is isisAuthTypePassword, then this is a list of passwords that the router will accept on received LSPs.
        - AreaTransmitPassword (str): If areaAuthType is isisAuthTypePassword, then this is the password (or MD5Key) that will be sent with transmitted LSPs.
        - BroadcastRootPriority (number): The value of the Broadcast Root Priority of a particular DCE ISIS router.
        - CapabilityRouterId (str): The IPv4 address format of the Capability Router.
        - DeviceId (number): This is a deprecated attribute in DCE ISIS mode.
        - DevicePriority (number): This is a deprecated attribute in DCE ISIS mode.
        - DomainAuthType (str(none | password | md5)): Sets up authentication for Level 2 LSPs.
        - DomainReceivedPasswordList (list(str)): If domainAuthType is isisAuthTypePassword, then this is a list of passwords that the router will accept on received LSPs.
        - DomainTransmitPassword (str): If domainAuthType is isisAuthTypePassword, then this is the password (or MD5Key) that will be sent with transmitted LSPs.
        - EnableAttached (bool): Indicates that the Attached Flag is set. It indicates that this ISIS router can use L2 routing to reach other areas.
        - EnableAutoLoopback (bool): If enabled, loopback addresses are allowed in the generated routes.
        - EnableDiscardLearnedLsps (bool): If enabled, LSPs learned from this router's interfaces will be discarded.
        - EnableHelloPadding (bool): If true, enables padding of hello messages.
        - EnableHitlessRestart (bool): Hitless Restart is enabled for this emulated ISIS router.
        - EnableHostName (bool): If true, the given dynamic host name is transmitted in all the packets sent from this router.
        - EnableIgnoreMtPortCapability (bool): NOT DEFINED
        - EnableIgnoreRecvMd5 (bool): MD5 authentication will be disabled for incoming/received packets.
        - EnableMtIpv6 (bool): If checked in L3, emulation type traffic group ID at router level is grayed out and unassigned.
        - EnableMtuProbe (bool): NOT DEFINED
        - EnableMultiTopology (bool): Enables more than one topology (distribution tree) corresponding to the given R bridge.
        - EnableOverloaded (bool): If enabled, the LSP Database Overload Bit is set. It indicates that the LSP database on this router is overloaded and that there is not enough memory to store a received LSP. This router enters the Waiting State and floods an LSP (with LSP number = 0) with the overload bit set, so other routers will not forward ISIS packets to it.
        - EnablePartitionRepair (bool): Enables the optional partition repair option specified in ISO/IEC 10589 and RFC 1195 for Level 1 areas.
        - EnableTrillOam (bool): NOT DEFINED
        - EnableWideMetric (bool): Enables the use of extended reachability (wide) metrics (defined to support TE): 32-bits wide for IP reachability (routes) and 24-bits wide for IS reachability (IS neighbors). If TE is enabled, wide metrics will be enabled automatically. The wide metrics may be used without enabling TE, however.
        - Enabled (bool): Enables or disables the simulated router.
        - FTagValue (number): This is a deprecated attribute in DCE ISIS mode.
        - FilterIpv4MulticastTlvs (bool): If true, retrieves IPv4 Multicast learned information in the DCE ISIS mode.
        - FilterIpv6MulticastTlvs (bool): If true, retrieves IPv6 Multicast learned information in the DCE ISIS mode.
        - FilterLearnedIpv4Prefixes (bool): If true, retrieves IPv4 Unicast learned information in the ISIS L3 Routing mode.
        - FilterLearnedIpv6Prefixes (bool): If true, retrieves IPv6 Unicast learned information in the ISIS L3 Routing mode.
        - FilterLearnedRbridges (bool): If true, retrieves RBridges learned information in the DCE ISIS mode.
        - FilterLearnedSpbRbridges (bool): NOT DEFINED
        - FilterLearnedTrillMacUnicast (bool): NOT DEFINED
        - FilterMacMulticastTlvs (bool): If true, retrieves MAC Multicast learned information in the DCE ISIS mode.
        - HostName (str): Allows to add a host name to this router.
        - InterLspMgroupPduBurstGap (number): Indicates the gap between each LSP MGROUP-PDUs.
        - LspLifeTime (number): (in sec) The MaxAge for retaining a learned LSP on this router. The default value is 1,200 sec.
        - LspMaxSize (number): (in bytes) The maximum allowable length of an ISIS LSP message. The default is 1,492 bytes.
        - LspMgroupPduMinTransmissionInterval (number): Indicates the minimum wait time for each LSP MGROUP-PDU transmission.
        - LspRefreshRate (number): (in sec) The rate at which LSPs are resent. The default value is 900 sec.
        - MaxAreaAddresses (number): The number of area addresses permitted for this IS area.
        - MaxLspMgroupPdusPerBurst (number): Indicates the maximum number of LSP MGROUP-PDUs for each burst.
        - NumberOfMtuProbes (number): NOT DEFINED
        - NumberOfMultiDestinationTrees (number): The number of Multi-Destination Trees for the emulated DCE ISIS router.
        - OriginatingLspBufSize (number): NOT DEFINED
        - PsnpInterval (number): The PSPN Interval.
        - RestartMode (str(normalRouter | restartingRouter | startingRouter | helperRouter)): If enableHitlessRestart is true, this indicates the mode in which this router is to operate.
        - RestartTime (number): Enter the restart time in seconds.
        - RestartVersion (str(version3 | version4)): If enableHitlessRestart is true, this indicates the version of the draft-ietf-isis-restart-nn document that the router should conform to.
        - StartFtagValue (number): The starting FTAG value of the emulated DCE ISIS router.
        - SwitchId (number): The Switch ID of the emulated DCE ISIS router.
        - SwitchIdPriority (number): The Switch ID priority of the emulated DCE ISIS router.
        - SystemId (str): The neighbor's system ID.
        - TeEnable (bool): Enables traffic engineering (TE) on this emulated ISIS router.
        - TeRouterId (str): The ID of the simulated router, expressed as an IP address.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.

        Returns
        -------
        - self: This instance with all currently retrieved router resources using find and the newly added router resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained router resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AreaAddressList=None,
        AreaAuthType=None,
        AreaReceivedPasswordList=None,
        AreaTransmitPassword=None,
        BroadcastRootPriority=None,
        CapabilityRouterId=None,
        DeviceId=None,
        DevicePriority=None,
        DomainAuthType=None,
        DomainReceivedPasswordList=None,
        DomainTransmitPassword=None,
        EnableAttached=None,
        EnableAutoLoopback=None,
        EnableDiscardLearnedLsps=None,
        EnableHelloPadding=None,
        EnableHitlessRestart=None,
        EnableHostName=None,
        EnableIgnoreMtPortCapability=None,
        EnableIgnoreRecvMd5=None,
        EnableMtIpv6=None,
        EnableMtuProbe=None,
        EnableMultiTopology=None,
        EnableOverloaded=None,
        EnablePartitionRepair=None,
        EnableTrillOam=None,
        EnableWideMetric=None,
        Enabled=None,
        FTagValue=None,
        FilterIpv4MulticastTlvs=None,
        FilterIpv6MulticastTlvs=None,
        FilterLearnedIpv4Prefixes=None,
        FilterLearnedIpv6Prefixes=None,
        FilterLearnedRbridges=None,
        FilterLearnedSpbRbridges=None,
        FilterLearnedTrillMacUnicast=None,
        FilterMacMulticastTlvs=None,
        HostName=None,
        InterLspMgroupPduBurstGap=None,
        LspLifeTime=None,
        LspMaxSize=None,
        LspMgroupPduMinTransmissionInterval=None,
        LspRefreshRate=None,
        MaxAreaAddresses=None,
        MaxLspMgroupPdusPerBurst=None,
        NumberOfMtuProbes=None,
        NumberOfMultiDestinationTrees=None,
        OriginatingLspBufSize=None,
        PsnpInterval=None,
        RestartMode=None,
        RestartTime=None,
        RestartVersion=None,
        StartFtagValue=None,
        SwitchId=None,
        SwitchIdPriority=None,
        SystemId=None,
        TeEnable=None,
        TeRouterId=None,
        TrafficGroupId=None,
    ):
        # type: (List[str], str, List[str], str, int, str, int, int, str, List[str], str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, bool, bool, bool, bool, bool, bool, bool, bool, str, int, int, int, int, int, int, int, int, int, int, int, str, int, str, int, int, int, str, bool, str, str) -> Router
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - AreaAddressList (list(str)): The list of area addresses to use.
        - AreaAuthType (str(none | password | md5)): Sets up authentication for Level 1 LSPs.
        - AreaReceivedPasswordList (list(str)): If areaAuthType is isisAuthTypePassword, then this is a list of passwords that the router will accept on received LSPs.
        - AreaTransmitPassword (str): If areaAuthType is isisAuthTypePassword, then this is the password (or MD5Key) that will be sent with transmitted LSPs.
        - BroadcastRootPriority (number): The value of the Broadcast Root Priority of a particular DCE ISIS router.
        - CapabilityRouterId (str): The IPv4 address format of the Capability Router.
        - DeviceId (number): This is a deprecated attribute in DCE ISIS mode.
        - DevicePriority (number): This is a deprecated attribute in DCE ISIS mode.
        - DomainAuthType (str(none | password | md5)): Sets up authentication for Level 2 LSPs.
        - DomainReceivedPasswordList (list(str)): If domainAuthType is isisAuthTypePassword, then this is a list of passwords that the router will accept on received LSPs.
        - DomainTransmitPassword (str): If domainAuthType is isisAuthTypePassword, then this is the password (or MD5Key) that will be sent with transmitted LSPs.
        - EnableAttached (bool): Indicates that the Attached Flag is set. It indicates that this ISIS router can use L2 routing to reach other areas.
        - EnableAutoLoopback (bool): If enabled, loopback addresses are allowed in the generated routes.
        - EnableDiscardLearnedLsps (bool): If enabled, LSPs learned from this router's interfaces will be discarded.
        - EnableHelloPadding (bool): If true, enables padding of hello messages.
        - EnableHitlessRestart (bool): Hitless Restart is enabled for this emulated ISIS router.
        - EnableHostName (bool): If true, the given dynamic host name is transmitted in all the packets sent from this router.
        - EnableIgnoreMtPortCapability (bool): NOT DEFINED
        - EnableIgnoreRecvMd5 (bool): MD5 authentication will be disabled for incoming/received packets.
        - EnableMtIpv6 (bool): If checked in L3, emulation type traffic group ID at router level is grayed out and unassigned.
        - EnableMtuProbe (bool): NOT DEFINED
        - EnableMultiTopology (bool): Enables more than one topology (distribution tree) corresponding to the given R bridge.
        - EnableOverloaded (bool): If enabled, the LSP Database Overload Bit is set. It indicates that the LSP database on this router is overloaded and that there is not enough memory to store a received LSP. This router enters the Waiting State and floods an LSP (with LSP number = 0) with the overload bit set, so other routers will not forward ISIS packets to it.
        - EnablePartitionRepair (bool): Enables the optional partition repair option specified in ISO/IEC 10589 and RFC 1195 for Level 1 areas.
        - EnableTrillOam (bool): NOT DEFINED
        - EnableWideMetric (bool): Enables the use of extended reachability (wide) metrics (defined to support TE): 32-bits wide for IP reachability (routes) and 24-bits wide for IS reachability (IS neighbors). If TE is enabled, wide metrics will be enabled automatically. The wide metrics may be used without enabling TE, however.
        - Enabled (bool): Enables or disables the simulated router.
        - FTagValue (number): This is a deprecated attribute in DCE ISIS mode.
        - FilterIpv4MulticastTlvs (bool): If true, retrieves IPv4 Multicast learned information in the DCE ISIS mode.
        - FilterIpv6MulticastTlvs (bool): If true, retrieves IPv6 Multicast learned information in the DCE ISIS mode.
        - FilterLearnedIpv4Prefixes (bool): If true, retrieves IPv4 Unicast learned information in the ISIS L3 Routing mode.
        - FilterLearnedIpv6Prefixes (bool): If true, retrieves IPv6 Unicast learned information in the ISIS L3 Routing mode.
        - FilterLearnedRbridges (bool): If true, retrieves RBridges learned information in the DCE ISIS mode.
        - FilterLearnedSpbRbridges (bool): NOT DEFINED
        - FilterLearnedTrillMacUnicast (bool): NOT DEFINED
        - FilterMacMulticastTlvs (bool): If true, retrieves MAC Multicast learned information in the DCE ISIS mode.
        - HostName (str): Allows to add a host name to this router.
        - InterLspMgroupPduBurstGap (number): Indicates the gap between each LSP MGROUP-PDUs.
        - LspLifeTime (number): (in sec) The MaxAge for retaining a learned LSP on this router. The default value is 1,200 sec.
        - LspMaxSize (number): (in bytes) The maximum allowable length of an ISIS LSP message. The default is 1,492 bytes.
        - LspMgroupPduMinTransmissionInterval (number): Indicates the minimum wait time for each LSP MGROUP-PDU transmission.
        - LspRefreshRate (number): (in sec) The rate at which LSPs are resent. The default value is 900 sec.
        - MaxAreaAddresses (number): The number of area addresses permitted for this IS area.
        - MaxLspMgroupPdusPerBurst (number): Indicates the maximum number of LSP MGROUP-PDUs for each burst.
        - NumberOfMtuProbes (number): NOT DEFINED
        - NumberOfMultiDestinationTrees (number): The number of Multi-Destination Trees for the emulated DCE ISIS router.
        - OriginatingLspBufSize (number): NOT DEFINED
        - PsnpInterval (number): The PSPN Interval.
        - RestartMode (str(normalRouter | restartingRouter | startingRouter | helperRouter)): If enableHitlessRestart is true, this indicates the mode in which this router is to operate.
        - RestartTime (number): Enter the restart time in seconds.
        - RestartVersion (str(version3 | version4)): If enableHitlessRestart is true, this indicates the version of the draft-ietf-isis-restart-nn document that the router should conform to.
        - StartFtagValue (number): The starting FTAG value of the emulated DCE ISIS router.
        - SwitchId (number): The Switch ID of the emulated DCE ISIS router.
        - SwitchIdPriority (number): The Switch ID priority of the emulated DCE ISIS router.
        - SystemId (str): The neighbor's system ID.
        - TeEnable (bool): Enables traffic engineering (TE) on this emulated ISIS router.
        - TeRouterId (str): The ID of the simulated router, expressed as an IP address.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.

        Returns
        -------
        - self: This instance with matching router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshLearnedInformation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshLearnedInformation operation on the server.

        This option refreshes the learned information of ISIS router.

        refreshLearnedInformation(async_operation=bool)bool
        ---------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: Boolean.

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
            "refreshLearnedInformation", payload=payload, response_object=None
        )

    def SendTrillOamPing(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the sendTrillOamPing operation on the server.

        This option will send trill OAM ping.

        sendTrillOamPing(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: Boolean.

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
        return self._execute("sendTrillOamPing", payload=payload, response_object=None)
