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


class Interface(Base):
    """This object represents a set of interfaces.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "interface"
    _SDM_ATT_MAP = {
        "AddressFamily": "addressFamily",
        "AutoPickUpstreamNeighbor": "autoPickUpstreamNeighbor",
        "BootstrapEnable": "bootstrapEnable",
        "BootstrapHashMaskLen": "bootstrapHashMaskLen",
        "BootstrapInterval": "bootstrapInterval",
        "BootstrapPriority": "bootstrapPriority",
        "BootstrapTimeout": "bootstrapTimeout",
        "DisableTriggeredHello": "disableTriggeredHello",
        "DiscardDataMdtTlv": "discardDataMdtTlv",
        "DiscardLearnedRpInfo": "discardLearnedRpInfo",
        "EnableBfdRegistration": "enableBfdRegistration",
        "EnableV4MappedV6Address": "enableV4MappedV6Address",
        "Enabled": "enabled",
        "ForceSemanticFragmentation": "forceSemanticFragmentation",
        "GenerationIdMode": "generationIdMode",
        "HelloHoldTime": "helloHoldTime",
        "HelloInterval": "helloInterval",
        "InterfaceId": "interfaceId",
        "InterfaceIndex": "interfaceIndex",
        "InterfaceType": "interfaceType",
        "Interfaces": "interfaces",
        "IsRefreshRpSetComplete": "isRefreshRpSetComplete",
        "LanPruneDelay": "lanPruneDelay",
        "LanPruneDelayTBit": "lanPruneDelayTBit",
        "LearnSelectedRpSet": "learnSelectedRpSet",
        "OverrideInterval": "overrideInterval",
        "SendBiDirCapableOption": "sendBiDirCapableOption",
        "SendGenIdOption": "sendGenIdOption",
        "SendHelloLanPruneDelayOption": "sendHelloLanPruneDelayOption",
        "ShowSelectedRpSetOnly": "showSelectedRpSetOnly",
        "SupportUnicastBootstrap": "supportUnicastBootstrap",
        "TrafficGroupId": "trafficGroupId",
        "TriggeredHelloDelay": "triggeredHelloDelay",
        "UpstreamNeighbor": "upstreamNeighbor",
    }
    _SDM_ENUM_MAP = {
        "addressFamily": ["ipv4", "ipv6"],
        "generationIdMode": ["incremental", "random", "constant"],
    }

    def __init__(self, parent, list_op=False):
        super(Interface, self).__init__(parent, list_op)

    @property
    def CrpRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.crprange_597167656c83f71e3e5a55938cb106a8.CrpRange): An instance of the CrpRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.crprange_597167656c83f71e3e5a55938cb106a8 import (
            CrpRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CrpRange", None) is not None:
                return self._properties.get("CrpRange")
        return CrpRange(self)

    @property
    def DataMdt(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.datamdt_79ed433986fc353fbd239fb7999ae1ee.DataMdt): An instance of the DataMdt class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.datamdt_79ed433986fc353fbd239fb7999ae1ee import (
            DataMdt,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DataMdt", None) is not None:
                return self._properties.get("DataMdt")
        return DataMdt(self)

    @property
    def JoinPrune(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.joinprune_9763e6279a674992cf71e86306c68672.JoinPrune): An instance of the JoinPrune class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.joinprune_9763e6279a674992cf71e86306c68672 import (
            JoinPrune,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("JoinPrune", None) is not None:
                return self._properties.get("JoinPrune")
        return JoinPrune(self)

    @property
    def LearnedBsrInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedbsrinfo_2b92bfaf7519829d075075f5c767de14.LearnedBsrInfo): An instance of the LearnedBsrInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedbsrinfo_2b92bfaf7519829d075075f5c767de14 import (
            LearnedBsrInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedBsrInfo", None) is not None:
                return self._properties.get("LearnedBsrInfo")
        return LearnedBsrInfo(self)

    @property
    def LearnedCrpInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedcrpinfo_60dd066e4b0de49ae66860f72856bd39.LearnedCrpInfo): An instance of the LearnedCrpInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedcrpinfo_60dd066e4b0de49ae66860f72856bd39 import (
            LearnedCrpInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedCrpInfo", None) is not None:
                return self._properties.get("LearnedCrpInfo")
        return LearnedCrpInfo(self)

    @property
    def LearnedMdtInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedmdtinfo_bbc54102507121c33244de8dacb03b19.LearnedMdtInfo): An instance of the LearnedMdtInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedmdtinfo_bbc54102507121c33244de8dacb03b19 import (
            LearnedMdtInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedMdtInfo", None) is not None:
                return self._properties.get("LearnedMdtInfo")
        return LearnedMdtInfo(self)

    @property
    def Source(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.source_f52e88433233160a4b212fd8bab440ba.Source): An instance of the Source class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.source_f52e88433233160a4b212fd8bab440ba import (
            Source,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Source", None) is not None:
                return self._properties.get("Source")
        return Source(self)

    @property
    def AddressFamily(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipv4 | ipv6): Choose an Address Family for this PIM-SM Interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddressFamily"])

    @AddressFamily.setter
    def AddressFamily(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddressFamily"], value)

    @property
    def AutoPickUpstreamNeighbor(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the time-saving Auto Pick feature and the Upstream Neighbor field is not available for use. The Upstream Neighbor address used in the Join/Prune message is determined automatically from received Hello messages. The first time a Hello message is received - containing a Source (link-local) address that does not belong to this interface, that source address will be used as the Upstream Neighbor address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoPickUpstreamNeighbor"])

    @AutoPickUpstreamNeighbor.setter
    def AutoPickUpstreamNeighbor(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoPickUpstreamNeighbor"], value)

    @property
    def BootstrapEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If checked, enables the PIM-SM interface to participate in Bootstrap Router election procedure.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BootstrapEnable"])

    @BootstrapEnable.setter
    def BootstrapEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BootstrapEnable"], value)

    @property
    def BootstrapHashMaskLen(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Hash Mask Length of the Bootstrap Router (BSR) that is set with the same name in all Bootstrap Messages sent by this BSR.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BootstrapHashMaskLen"])

    @BootstrapHashMaskLen.setter
    def BootstrapHashMaskLen(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BootstrapHashMaskLen"], value)

    @property
    def BootstrapInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time interval (in seconds) between two consecutive bootstrap messages sent by the BSR.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BootstrapInterval"])

    @BootstrapInterval.setter
    def BootstrapInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BootstrapInterval"], value)

    @property
    def BootstrapPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Priority of the Bootstrap Router (BSR) that is set with the same name in all Bootstrap Messages sent by this BSR.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BootstrapPriority"])

    @BootstrapPriority.setter
    def BootstrapPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BootstrapPriority"], value)

    @property
    def BootstrapTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Amount of time (in seconds) of not receiving any Bootstrap Messages, after which the BSR if candidate at that point of time will decide that the currently elected BSR has gone down and will restart BSR election procedure.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BootstrapTimeout"])

    @BootstrapTimeout.setter
    def BootstrapTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BootstrapTimeout"], value)

    @property
    def DisableTriggeredHello(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the triggered hello delay function is disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisableTriggeredHello"])

    @DisableTriggeredHello.setter
    def DisableTriggeredHello(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisableTriggeredHello"], value)

    @property
    def DiscardDataMdtTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, received Data MDT TLVs will be discarded.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscardDataMdtTlv"])

    @DiscardDataMdtTlv.setter
    def DiscardDataMdtTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DiscardDataMdtTlv"], value)

    @property
    def DiscardLearnedRpInfo(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If checked, disregards group mappings learnt from Bootstrap Message (in case not acting as elected BSR) or from Candidate RP Advertisement (in case of elected BSR).
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscardLearnedRpInfo"])

    @DiscardLearnedRpInfo.setter
    def DiscardLearnedRpInfo(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DiscardLearnedRpInfo"], value)

    @property
    def EnableBfdRegistration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates if a BFD session is to be created to the PIMSM peer IP address once the PIMSM session is established. This allows PIMSM to use BFD to maintain IPv4 connectivity the PIMSM peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableBfdRegistration"])

    @EnableBfdRegistration.setter
    def EnableBfdRegistration(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableBfdRegistration"], value)

    @property
    def EnableV4MappedV6Address(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use IpV4 mapped IpV6 address
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableV4MappedV6Address"])

    @EnableV4MappedV6Address.setter
    def EnableV4MappedV6Address(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableV4MappedV6Address"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables the use of the interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def ForceSemanticFragmentation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this forces the BSR to send only one group specific RP list per bootstrap message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForceSemanticFragmentation"])

    @ForceSemanticFragmentation.setter
    def ForceSemanticFragmentation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForceSemanticFragmentation"], value)

    @property
    def GenerationIdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(incremental | random | constant): The mode used for creating the 32-bit value for the Generation ID. This can either be incrementing, random or constant. (default = constant)
        """
        return self._get_attribute(self._SDM_ATT_MAP["GenerationIdMode"])

    @GenerationIdMode.setter
    def GenerationIdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GenerationIdMode"], value)

    @property
    def HelloHoldTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The amount of time that neighbor routers should hold the interface as reachable.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HelloHoldTime"])

    @HelloHoldTime.setter
    def HelloHoldTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["HelloHoldTime"], value)

    @property
    def HelloInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The interval between transmitted hello messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HelloInterval"])

    @HelloInterval.setter
    def HelloInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["HelloInterval"], value)

    @property
    def InterfaceId(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface): The identifier for this PIM-SM Interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceId"])

    @InterfaceId.setter
    def InterfaceId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterfaceId"], value)

    @property
    def InterfaceIndex(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The assigned protocol interface ID for this PIM-SM interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceIndex"])

    @InterfaceIndex.setter
    def InterfaceIndex(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterfaceIndex"], value)

    @property
    def InterfaceType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The type of interface to be selected for this PIM-SM interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceType"])

    @InterfaceType.setter
    def InterfaceType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterfaceType"], value)

    @property
    def Interfaces(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernetEndpoint/range): The interfaces that are associated with the selected interface type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Interfaces"])

    @Interfaces.setter
    def Interfaces(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Interfaces"], value)

    @property
    def IsRefreshRpSetComplete(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, shows the desired set of RPs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsRefreshRpSetComplete"])

    @property
    def LanPruneDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value of the LAN Prune (propagation) Delay for this PIM-SM interface. The expected delay for messages propagated on the link. It indicates to an upstream router how long to wait for a Join override message before it prunes an interface.The default value is 500 msec. The valid range is 100 to 0x7FFF msec. (LAN Prune Delay is an Option included in Hello messages.)
        """
        return self._get_attribute(self._SDM_ATT_MAP["LanPruneDelay"])

    @LanPruneDelay.setter
    def LanPruneDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LanPruneDelay"], value)

    @property
    def LanPruneDelayTBit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the T flag bit in the LAN Prune Delay option of the Hello message is set (= 1). Setting this bit specifies that the sending PIM-SM router has the ability to disable Join message suppression.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LanPruneDelayTBit"])

    @LanPruneDelayTBit.setter
    def LanPruneDelayTBit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LanPruneDelayTBit"], value)

    @property
    def LearnSelectedRpSet(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this displays only the best RP per group (member of selected RP set).
        """
        return self._get_attribute(self._SDM_ATT_MAP["LearnSelectedRpSet"])

    @LearnSelectedRpSet.setter
    def LearnSelectedRpSet(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LearnSelectedRpSet"], value)

    @property
    def OverrideInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The delay interval, in milliseconds, for randomizing the transmission time for override messages, which are used when scheduling a delayed Join message. This is part of the LAN Prune Delay option included in Hello messages. The valid range is 100 to 7FFF msec. (default = 2500)
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideInterval"])

    @OverrideInterval.setter
    def OverrideInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideInterval"], value)

    @property
    def SendBiDirCapableOption(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, sets the bidirectional PIM-SM flag bit (=1), per IETF DRAFT draft-ietf-pim-bidir-04.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendBiDirCapableOption"])

    @SendBiDirCapableOption.setter
    def SendBiDirCapableOption(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendBiDirCapableOption"], value)

    @property
    def SendGenIdOption(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the send generation ID option.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendGenIdOption"])

    @SendGenIdOption.setter
    def SendGenIdOption(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendGenIdOption"], value)

    @property
    def SendHelloLanPruneDelayOption(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If set, the LAN Prune propagation delay is enabled for this interface, as indicated in the pruneDelay option. The option is indicated in Hello messages from the interface. (default = true)
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendHelloLanPruneDelayOption"])

    @SendHelloLanPruneDelayOption.setter
    def SendHelloLanPruneDelayOption(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendHelloLanPruneDelayOption"], value)

    @property
    def ShowSelectedRpSetOnly(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If enabled, this displays only the best RP per group (member of selected RP set).
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowSelectedRpSetOnly"])

    @ShowSelectedRpSetOnly.setter
    def ShowSelectedRpSetOnly(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowSelectedRpSetOnly"], value)

    @property
    def SupportUnicastBootstrap(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this supports the sending and processing of Unicast bootstrap messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportUnicastBootstrap"])

    @SupportUnicastBootstrap.setter
    def SupportUnicastBootstrap(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportUnicastBootstrap"], value)

    @property
    def TrafficGroupId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup): The name of the group to which this emulated router is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficGroupId"])

    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficGroupId"], value)

    @property
    def TriggeredHelloDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time (in seconds) after which the router senses a delay in sending or receiving PIM-SM hello message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggeredHelloDelay"])

    @TriggeredHelloDelay.setter
    def TriggeredHelloDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggeredHelloDelay"], value)

    @property
    def UpstreamNeighbor(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address of the upstream neighbor.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamNeighbor"])

    @UpstreamNeighbor.setter
    def UpstreamNeighbor(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamNeighbor"], value)

    def update(
        self,
        AddressFamily=None,
        AutoPickUpstreamNeighbor=None,
        BootstrapEnable=None,
        BootstrapHashMaskLen=None,
        BootstrapInterval=None,
        BootstrapPriority=None,
        BootstrapTimeout=None,
        DisableTriggeredHello=None,
        DiscardDataMdtTlv=None,
        DiscardLearnedRpInfo=None,
        EnableBfdRegistration=None,
        EnableV4MappedV6Address=None,
        Enabled=None,
        ForceSemanticFragmentation=None,
        GenerationIdMode=None,
        HelloHoldTime=None,
        HelloInterval=None,
        InterfaceId=None,
        InterfaceIndex=None,
        InterfaceType=None,
        Interfaces=None,
        LanPruneDelay=None,
        LanPruneDelayTBit=None,
        LearnSelectedRpSet=None,
        OverrideInterval=None,
        SendBiDirCapableOption=None,
        SendGenIdOption=None,
        SendHelloLanPruneDelayOption=None,
        ShowSelectedRpSetOnly=None,
        SupportUnicastBootstrap=None,
        TrafficGroupId=None,
        TriggeredHelloDelay=None,
        UpstreamNeighbor=None,
    ):
        # type: (str, bool, bool, int, int, int, int, bool, bool, bool, bool, bool, bool, bool, str, int, int, str, int, str, str, int, bool, bool, int, bool, bool, bool, bool, bool, str, int, str) -> Interface
        """Updates interface resource on the server.

        Args
        ----
        - AddressFamily (str(ipv4 | ipv6)): Choose an Address Family for this PIM-SM Interface.
        - AutoPickUpstreamNeighbor (bool): Enables the time-saving Auto Pick feature and the Upstream Neighbor field is not available for use. The Upstream Neighbor address used in the Join/Prune message is determined automatically from received Hello messages. The first time a Hello message is received - containing a Source (link-local) address that does not belong to this interface, that source address will be used as the Upstream Neighbor address.
        - BootstrapEnable (bool): If checked, enables the PIM-SM interface to participate in Bootstrap Router election procedure.
        - BootstrapHashMaskLen (number): Hash Mask Length of the Bootstrap Router (BSR) that is set with the same name in all Bootstrap Messages sent by this BSR.
        - BootstrapInterval (number): The time interval (in seconds) between two consecutive bootstrap messages sent by the BSR.
        - BootstrapPriority (number): Priority of the Bootstrap Router (BSR) that is set with the same name in all Bootstrap Messages sent by this BSR.
        - BootstrapTimeout (number): Amount of time (in seconds) of not receiving any Bootstrap Messages, after which the BSR if candidate at that point of time will decide that the currently elected BSR has gone down and will restart BSR election procedure.
        - DisableTriggeredHello (bool): If enabled, the triggered hello delay function is disabled.
        - DiscardDataMdtTlv (bool): If enabled, received Data MDT TLVs will be discarded.
        - DiscardLearnedRpInfo (bool): If checked, disregards group mappings learnt from Bootstrap Message (in case not acting as elected BSR) or from Candidate RP Advertisement (in case of elected BSR).
        - EnableBfdRegistration (bool): Indicates if a BFD session is to be created to the PIMSM peer IP address once the PIMSM session is established. This allows PIMSM to use BFD to maintain IPv4 connectivity the PIMSM peer.
        - EnableV4MappedV6Address (bool): Use IpV4 mapped IpV6 address
        - Enabled (bool): Enables or disables the use of the interface.
        - ForceSemanticFragmentation (bool): If enabled, this forces the BSR to send only one group specific RP list per bootstrap message.
        - GenerationIdMode (str(incremental | random | constant)): The mode used for creating the 32-bit value for the Generation ID. This can either be incrementing, random or constant. (default = constant)
        - HelloHoldTime (number): The amount of time that neighbor routers should hold the interface as reachable.
        - HelloInterval (number): The interval between transmitted hello messages.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): The identifier for this PIM-SM Interface.
        - InterfaceIndex (number): The assigned protocol interface ID for this PIM-SM interface.
        - InterfaceType (str): The type of interface to be selected for this PIM-SM interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/interface | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernetEndpoint/range)): The interfaces that are associated with the selected interface type.
        - LanPruneDelay (number): The value of the LAN Prune (propagation) Delay for this PIM-SM interface. The expected delay for messages propagated on the link. It indicates to an upstream router how long to wait for a Join override message before it prunes an interface.The default value is 500 msec. The valid range is 100 to 0x7FFF msec. (LAN Prune Delay is an Option included in Hello messages.)
        - LanPruneDelayTBit (bool): If enabled, the T flag bit in the LAN Prune Delay option of the Hello message is set (= 1). Setting this bit specifies that the sending PIM-SM router has the ability to disable Join message suppression.
        - LearnSelectedRpSet (bool): If enabled, this displays only the best RP per group (member of selected RP set).
        - OverrideInterval (number): The delay interval, in milliseconds, for randomizing the transmission time for override messages, which are used when scheduling a delayed Join message. This is part of the LAN Prune Delay option included in Hello messages. The valid range is 100 to 7FFF msec. (default = 2500)
        - SendBiDirCapableOption (bool): If enabled, sets the bidirectional PIM-SM flag bit (=1), per IETF DRAFT draft-ietf-pim-bidir-04.
        - SendGenIdOption (bool): Enables the send generation ID option.
        - SendHelloLanPruneDelayOption (bool): If set, the LAN Prune propagation delay is enabled for this interface, as indicated in the pruneDelay option. The option is indicated in Hello messages from the interface. (default = true)
        - ShowSelectedRpSetOnly (bool): If enabled, this displays only the best RP per group (member of selected RP set).
        - SupportUnicastBootstrap (bool): If enabled, this supports the sending and processing of Unicast bootstrap messages.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): The name of the group to which this emulated router is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - TriggeredHelloDelay (number): The time (in seconds) after which the router senses a delay in sending or receiving PIM-SM hello message.
        - UpstreamNeighbor (str): The IP address of the upstream neighbor.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AddressFamily=None,
        AutoPickUpstreamNeighbor=None,
        BootstrapEnable=None,
        BootstrapHashMaskLen=None,
        BootstrapInterval=None,
        BootstrapPriority=None,
        BootstrapTimeout=None,
        DisableTriggeredHello=None,
        DiscardDataMdtTlv=None,
        DiscardLearnedRpInfo=None,
        EnableBfdRegistration=None,
        EnableV4MappedV6Address=None,
        Enabled=None,
        ForceSemanticFragmentation=None,
        GenerationIdMode=None,
        HelloHoldTime=None,
        HelloInterval=None,
        InterfaceId=None,
        InterfaceIndex=None,
        InterfaceType=None,
        Interfaces=None,
        LanPruneDelay=None,
        LanPruneDelayTBit=None,
        LearnSelectedRpSet=None,
        OverrideInterval=None,
        SendBiDirCapableOption=None,
        SendGenIdOption=None,
        SendHelloLanPruneDelayOption=None,
        ShowSelectedRpSetOnly=None,
        SupportUnicastBootstrap=None,
        TrafficGroupId=None,
        TriggeredHelloDelay=None,
        UpstreamNeighbor=None,
    ):
        # type: (str, bool, bool, int, int, int, int, bool, bool, bool, bool, bool, bool, bool, str, int, int, str, int, str, str, int, bool, bool, int, bool, bool, bool, bool, bool, str, int, str) -> Interface
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - AddressFamily (str(ipv4 | ipv6)): Choose an Address Family for this PIM-SM Interface.
        - AutoPickUpstreamNeighbor (bool): Enables the time-saving Auto Pick feature and the Upstream Neighbor field is not available for use. The Upstream Neighbor address used in the Join/Prune message is determined automatically from received Hello messages. The first time a Hello message is received - containing a Source (link-local) address that does not belong to this interface, that source address will be used as the Upstream Neighbor address.
        - BootstrapEnable (bool): If checked, enables the PIM-SM interface to participate in Bootstrap Router election procedure.
        - BootstrapHashMaskLen (number): Hash Mask Length of the Bootstrap Router (BSR) that is set with the same name in all Bootstrap Messages sent by this BSR.
        - BootstrapInterval (number): The time interval (in seconds) between two consecutive bootstrap messages sent by the BSR.
        - BootstrapPriority (number): Priority of the Bootstrap Router (BSR) that is set with the same name in all Bootstrap Messages sent by this BSR.
        - BootstrapTimeout (number): Amount of time (in seconds) of not receiving any Bootstrap Messages, after which the BSR if candidate at that point of time will decide that the currently elected BSR has gone down and will restart BSR election procedure.
        - DisableTriggeredHello (bool): If enabled, the triggered hello delay function is disabled.
        - DiscardDataMdtTlv (bool): If enabled, received Data MDT TLVs will be discarded.
        - DiscardLearnedRpInfo (bool): If checked, disregards group mappings learnt from Bootstrap Message (in case not acting as elected BSR) or from Candidate RP Advertisement (in case of elected BSR).
        - EnableBfdRegistration (bool): Indicates if a BFD session is to be created to the PIMSM peer IP address once the PIMSM session is established. This allows PIMSM to use BFD to maintain IPv4 connectivity the PIMSM peer.
        - EnableV4MappedV6Address (bool): Use IpV4 mapped IpV6 address
        - Enabled (bool): Enables or disables the use of the interface.
        - ForceSemanticFragmentation (bool): If enabled, this forces the BSR to send only one group specific RP list per bootstrap message.
        - GenerationIdMode (str(incremental | random | constant)): The mode used for creating the 32-bit value for the Generation ID. This can either be incrementing, random or constant. (default = constant)
        - HelloHoldTime (number): The amount of time that neighbor routers should hold the interface as reachable.
        - HelloInterval (number): The interval between transmitted hello messages.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): The identifier for this PIM-SM Interface.
        - InterfaceIndex (number): The assigned protocol interface ID for this PIM-SM interface.
        - InterfaceType (str): The type of interface to be selected for this PIM-SM interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/interface | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernetEndpoint/range)): The interfaces that are associated with the selected interface type.
        - LanPruneDelay (number): The value of the LAN Prune (propagation) Delay for this PIM-SM interface. The expected delay for messages propagated on the link. It indicates to an upstream router how long to wait for a Join override message before it prunes an interface.The default value is 500 msec. The valid range is 100 to 0x7FFF msec. (LAN Prune Delay is an Option included in Hello messages.)
        - LanPruneDelayTBit (bool): If enabled, the T flag bit in the LAN Prune Delay option of the Hello message is set (= 1). Setting this bit specifies that the sending PIM-SM router has the ability to disable Join message suppression.
        - LearnSelectedRpSet (bool): If enabled, this displays only the best RP per group (member of selected RP set).
        - OverrideInterval (number): The delay interval, in milliseconds, for randomizing the transmission time for override messages, which are used when scheduling a delayed Join message. This is part of the LAN Prune Delay option included in Hello messages. The valid range is 100 to 7FFF msec. (default = 2500)
        - SendBiDirCapableOption (bool): If enabled, sets the bidirectional PIM-SM flag bit (=1), per IETF DRAFT draft-ietf-pim-bidir-04.
        - SendGenIdOption (bool): Enables the send generation ID option.
        - SendHelloLanPruneDelayOption (bool): If set, the LAN Prune propagation delay is enabled for this interface, as indicated in the pruneDelay option. The option is indicated in Hello messages from the interface. (default = true)
        - ShowSelectedRpSetOnly (bool): If enabled, this displays only the best RP per group (member of selected RP set).
        - SupportUnicastBootstrap (bool): If enabled, this supports the sending and processing of Unicast bootstrap messages.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): The name of the group to which this emulated router is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - TriggeredHelloDelay (number): The time (in seconds) after which the router senses a delay in sending or receiving PIM-SM hello message.
        - UpstreamNeighbor (str): The IP address of the upstream neighbor.

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AddressFamily=None,
        AutoPickUpstreamNeighbor=None,
        BootstrapEnable=None,
        BootstrapHashMaskLen=None,
        BootstrapInterval=None,
        BootstrapPriority=None,
        BootstrapTimeout=None,
        DisableTriggeredHello=None,
        DiscardDataMdtTlv=None,
        DiscardLearnedRpInfo=None,
        EnableBfdRegistration=None,
        EnableV4MappedV6Address=None,
        Enabled=None,
        ForceSemanticFragmentation=None,
        GenerationIdMode=None,
        HelloHoldTime=None,
        HelloInterval=None,
        InterfaceId=None,
        InterfaceIndex=None,
        InterfaceType=None,
        Interfaces=None,
        IsRefreshRpSetComplete=None,
        LanPruneDelay=None,
        LanPruneDelayTBit=None,
        LearnSelectedRpSet=None,
        OverrideInterval=None,
        SendBiDirCapableOption=None,
        SendGenIdOption=None,
        SendHelloLanPruneDelayOption=None,
        ShowSelectedRpSetOnly=None,
        SupportUnicastBootstrap=None,
        TrafficGroupId=None,
        TriggeredHelloDelay=None,
        UpstreamNeighbor=None,
    ):
        # type: (str, bool, bool, int, int, int, int, bool, bool, bool, bool, bool, bool, bool, str, int, int, str, int, str, str, bool, int, bool, bool, int, bool, bool, bool, bool, bool, str, int, str) -> Interface
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - AddressFamily (str(ipv4 | ipv6)): Choose an Address Family for this PIM-SM Interface.
        - AutoPickUpstreamNeighbor (bool): Enables the time-saving Auto Pick feature and the Upstream Neighbor field is not available for use. The Upstream Neighbor address used in the Join/Prune message is determined automatically from received Hello messages. The first time a Hello message is received - containing a Source (link-local) address that does not belong to this interface, that source address will be used as the Upstream Neighbor address.
        - BootstrapEnable (bool): If checked, enables the PIM-SM interface to participate in Bootstrap Router election procedure.
        - BootstrapHashMaskLen (number): Hash Mask Length of the Bootstrap Router (BSR) that is set with the same name in all Bootstrap Messages sent by this BSR.
        - BootstrapInterval (number): The time interval (in seconds) between two consecutive bootstrap messages sent by the BSR.
        - BootstrapPriority (number): Priority of the Bootstrap Router (BSR) that is set with the same name in all Bootstrap Messages sent by this BSR.
        - BootstrapTimeout (number): Amount of time (in seconds) of not receiving any Bootstrap Messages, after which the BSR if candidate at that point of time will decide that the currently elected BSR has gone down and will restart BSR election procedure.
        - DisableTriggeredHello (bool): If enabled, the triggered hello delay function is disabled.
        - DiscardDataMdtTlv (bool): If enabled, received Data MDT TLVs will be discarded.
        - DiscardLearnedRpInfo (bool): If checked, disregards group mappings learnt from Bootstrap Message (in case not acting as elected BSR) or from Candidate RP Advertisement (in case of elected BSR).
        - EnableBfdRegistration (bool): Indicates if a BFD session is to be created to the PIMSM peer IP address once the PIMSM session is established. This allows PIMSM to use BFD to maintain IPv4 connectivity the PIMSM peer.
        - EnableV4MappedV6Address (bool): Use IpV4 mapped IpV6 address
        - Enabled (bool): Enables or disables the use of the interface.
        - ForceSemanticFragmentation (bool): If enabled, this forces the BSR to send only one group specific RP list per bootstrap message.
        - GenerationIdMode (str(incremental | random | constant)): The mode used for creating the 32-bit value for the Generation ID. This can either be incrementing, random or constant. (default = constant)
        - HelloHoldTime (number): The amount of time that neighbor routers should hold the interface as reachable.
        - HelloInterval (number): The interval between transmitted hello messages.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): The identifier for this PIM-SM Interface.
        - InterfaceIndex (number): The assigned protocol interface ID for this PIM-SM interface.
        - InterfaceType (str): The type of interface to be selected for this PIM-SM interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/interface | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernetEndpoint/range)): The interfaces that are associated with the selected interface type.
        - IsRefreshRpSetComplete (bool): If enabled, shows the desired set of RPs.
        - LanPruneDelay (number): The value of the LAN Prune (propagation) Delay for this PIM-SM interface. The expected delay for messages propagated on the link. It indicates to an upstream router how long to wait for a Join override message before it prunes an interface.The default value is 500 msec. The valid range is 100 to 0x7FFF msec. (LAN Prune Delay is an Option included in Hello messages.)
        - LanPruneDelayTBit (bool): If enabled, the T flag bit in the LAN Prune Delay option of the Hello message is set (= 1). Setting this bit specifies that the sending PIM-SM router has the ability to disable Join message suppression.
        - LearnSelectedRpSet (bool): If enabled, this displays only the best RP per group (member of selected RP set).
        - OverrideInterval (number): The delay interval, in milliseconds, for randomizing the transmission time for override messages, which are used when scheduling a delayed Join message. This is part of the LAN Prune Delay option included in Hello messages. The valid range is 100 to 7FFF msec. (default = 2500)
        - SendBiDirCapableOption (bool): If enabled, sets the bidirectional PIM-SM flag bit (=1), per IETF DRAFT draft-ietf-pim-bidir-04.
        - SendGenIdOption (bool): Enables the send generation ID option.
        - SendHelloLanPruneDelayOption (bool): If set, the LAN Prune propagation delay is enabled for this interface, as indicated in the pruneDelay option. The option is indicated in Hello messages from the interface. (default = true)
        - ShowSelectedRpSetOnly (bool): If enabled, this displays only the best RP per group (member of selected RP set).
        - SupportUnicastBootstrap (bool): If enabled, this supports the sending and processing of Unicast bootstrap messages.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): The name of the group to which this emulated router is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - TriggeredHelloDelay (number): The time (in seconds) after which the router senses a delay in sending or receiving PIM-SM hello message.
        - UpstreamNeighbor (str): The IP address of the upstream neighbor.

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetInterfaceAccessorIfaceList(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getInterfaceAccessorIfaceList operation on the server.

        Gets the interface accesor Iface list.

        getInterfaceAccessorIfaceList(async_operation=bool)string
        ---------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Return list of interface.

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
            "getInterfaceAccessorIfaceList", payload=payload, response_object=None
        )

    def RefreshCrpBsrLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshCrpBsrLearnedInfo operation on the server.

        If true, refreshes the Bsr learned information

        refreshCrpBsrLearnedInfo(async_operation=bool)bool
        --------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: Returns boolean value on success.

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
            "refreshCrpBsrLearnedInfo", payload=payload, response_object=None
        )
