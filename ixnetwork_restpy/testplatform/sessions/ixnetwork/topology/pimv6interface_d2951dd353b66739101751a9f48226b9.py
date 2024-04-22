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


class PimV6Interface(Base):
    """PIMv6 Interface level Configuration
    The PimV6Interface class encapsulates a list of pimV6Interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the PimV6Interface.find() method.
    The list can be managed by using the PimV6Interface.add() and PimV6Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "pimV6Interface"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AutoPickNeighbor": "autoPickNeighbor",
        "BootstrapHashMaskLength": "bootstrapHashMaskLength",
        "BootstrapInterval": "bootstrapInterval",
        "BootstrapPriority": "bootstrapPriority",
        "BootstrapTimeout": "bootstrapTimeout",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "CrpRanges": "crpRanges",
        "DescriptiveName": "descriptiveName",
        "DfElectionBackoffPeriod": "dfElectionBackoffPeriod",
        "DfElectionOfferPeriod": "dfElectionOfferPeriod",
        "DfElectionRobustness": "dfElectionRobustness",
        "DisableTriggered": "disableTriggered",
        "DiscardLearnedRpInfo": "discardLearnedRpInfo",
        "EnableBfdRegistration": "enableBfdRegistration",
        "EnableBootstrap": "enableBootstrap",
        "EnablePrune": "enablePrune",
        "Errors": "errors",
        "ForceSemantic": "forceSemantic",
        "HelloHoldTime": "helloHoldTime",
        "HelloInterval": "helloInterval",
        "JoinPrunes": "joinPrunes",
        "LanPruneTbit": "lanPruneTbit",
        "LearnSelectedRpSet": "learnSelectedRpSet",
        "LocalRouterId": "localRouterId",
        "Multiplier": "multiplier",
        "Name": "name",
        "NeighborV6Address": "neighborV6Address",
        "OverrideInterval": "overrideInterval",
        "PruneDelay": "pruneDelay",
        "SendBidirectional": "sendBidirectional",
        "SendGenerationIdOption": "sendGenerationIdOption",
        "SendGenerationMode": "sendGenerationMode",
        "SessionStatus": "sessionStatus",
        "Sources": "sources",
        "StackedLayers": "stackedLayers",
        "StateCounts": "stateCounts",
        "Status": "status",
        "SupportUnicastBsm": "supportUnicastBsm",
        "TriggeredHelloDelay": "triggeredHelloDelay",
    }
    _SDM_ENUM_MAP = {
        "status": [
            "configured",
            "error",
            "mixed",
            "notStarted",
            "started",
            "starting",
            "stopping",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(PimV6Interface, self).__init__(parent, list_op)

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import (
            LearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedInfo", None) is not None:
                return self._properties.get("LearnedInfo")
        return LearnedInfo(self)

    @property
    def PimV6BIDIRRPMetricList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6bidirrpmetriclist_59a6cb26d48051aa410b9da38e0ae74c.PimV6BIDIRRPMetricList): An instance of the PimV6BIDIRRPMetricList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6bidirrpmetriclist_59a6cb26d48051aa410b9da38e0ae74c import (
            PimV6BIDIRRPMetricList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PimV6BIDIRRPMetricList", None) is not None:
                return self._properties.get("PimV6BIDIRRPMetricList")
        return PimV6BIDIRRPMetricList(self)._select()

    @property
    def PimV6CandidateRPsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6candidaterpslist_844aa043d76dc15890b467e44e8f739e.PimV6CandidateRPsList): An instance of the PimV6CandidateRPsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6candidaterpslist_844aa043d76dc15890b467e44e8f739e import (
            PimV6CandidateRPsList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PimV6CandidateRPsList", None) is not None:
                return self._properties.get("PimV6CandidateRPsList")
        return PimV6CandidateRPsList(self)._select()

    @property
    def PimV6JoinPruneList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6joinprunelist_45b4e701e80080858668a0625c9a948b.PimV6JoinPruneList): An instance of the PimV6JoinPruneList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6joinprunelist_45b4e701e80080858668a0625c9a948b import (
            PimV6JoinPruneList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PimV6JoinPruneList", None) is not None:
                return self._properties.get("PimV6JoinPruneList")
        return PimV6JoinPruneList(self)._select()

    @property
    def PimV6SourcesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6sourceslist_7c181c77974667394bfee5e6920a7772.PimV6SourcesList): An instance of the PimV6SourcesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6sourceslist_7c181c77974667394bfee5e6920a7772 import (
            PimV6SourcesList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PimV6SourcesList", None) is not None:
                return self._properties.get("PimV6SourcesList")
        return PimV6SourcesList(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import (
            Tag,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Tag", None) is not None:
                return self._properties.get("Tag")
        return Tag(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AutoPickNeighbor(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the time-saving Auto Pick feature is enabled-and the Upstream Neighbor field is not available for use. The Upstream Neighbor address used in the Join/Prune message is determined automatically from received Hello messages. The first time a Hello message is received-containing a Source (link-local) address that does not belong to this interface, that source address will be used as the Upstream Neighbor address. If not selected, the user can type in the link-local address in the Upstream Neighbor IP field (see Neighbor field below)-to be used for the upstream neighbor address field in the Join/Prune message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoPickNeighbor"])
        )

    @property
    def BootstrapHashMaskLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hash Mask Length of the Bootstrap Router (BSR) that is set with the same name in all Bootstrap Messages sent by this BSR.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BootstrapHashMaskLength"])
        )

    @property
    def BootstrapInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The time interval (in seconds) between two consecutive bootstrap messages sent by the BSR.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BootstrapInterval"])
        )

    @property
    def BootstrapPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Priority of the Bootstrap Router (BSR) that is set with the same name in all Bootstrap Messages sent by this BSR.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BootstrapPriority"])
        )

    @property
    def BootstrapTimeout(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Amount of time (in seconds) of not receiving any Bootstrap Messages, after which, the BSR if candidate at that point of time will decide that the currently elected BSR has gone down and will restart BSR election procedure.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BootstrapTimeout"])
        )

    @property
    def ConnectedVia(self):
        # type: () -> List[str]
        """DEPRECATED
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectedVia"])

    @ConnectedVia.setter
    def ConnectedVia(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectedVia"], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def CrpRanges(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of C-RP Ranges
        """
        return self._get_attribute(self._SDM_ATT_MAP["CrpRanges"])

    @CrpRanges.setter
    def CrpRanges(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CrpRanges"], value)

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def DfElectionBackoffPeriod(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Backoff Period for DF Election. It is the interval that the current acting DF waits between receiving a better Offer and sending the Pass message to transfer DF responsibility.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DfElectionBackoffPeriod"])
        )

    @property
    def DfElectionOfferPeriod(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Offer Period for DF Election. It is the waiting interval between repeated Offer and Winner messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DfElectionOfferPeriod"])
        )

    @property
    def DfElectionRobustness(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DF Election Robustness. This is the minimum number of election messages that must be lost in order for election to fail.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DfElectionRobustness"])
        )

    @property
    def DisableTriggered(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, the triggered hello delay function is disabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DisableTriggered"])
        )

    @property
    def DiscardLearnedRpInfo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, disregards group mappings learnt from Bootstrap Message (in case not acting as elected BSR) or from Candidate RP Advertisement (in case of elected BSR).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DiscardLearnedRpInfo"])
        )

    @property
    def EnableBfdRegistration(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable BFD Registration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableBfdRegistration"])
        )

    @property
    def EnableBootstrap(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, enables the PIM-SM interface to participate in Bootstrap Router election procedure.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableBootstrap"])
        )

    @property
    def EnablePrune(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the LAN Prune (propagation) Delay is enabled for this PIM-SM interface. (This Indicates that this option is present in the Hello message.)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnablePrune"]))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def ForceSemantic(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, this forces the BSR to send only one group specific RP list per bootstrap message, even if there is space in the packet to push in more RP list information pertaining to a different group.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ForceSemantic"]))

    @property
    def HelloHoldTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The timeout period in seconds specified in Hello messages. It is the length of time the receiver of this message must keep the neighbor reachable. The default is 3.5 times the Hello Interval (105 seconds).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HelloHoldTime"]))

    @property
    def HelloInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The PIM-SM Hello Interval is the length of time in seconds between the transmissions of Hello messages. The default is 30 seconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HelloInterval"]))

    @property
    def JoinPrunes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Join/Prunes
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinPrunes"])

    @JoinPrunes.setter
    def JoinPrunes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinPrunes"], value)

    @property
    def LanPruneTbit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the T flag bit in the LAN Prune Delay option of the Hello message is set (= 1). Setting this bit specifies that the sending PIM-SM router has the ability to disable Join message suppression
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LanPruneTbit"]))

    @property
    def LearnSelectedRpSet(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, displays the best RP per group (member of selected RP set).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LearnSelectedRpSet"])
        )

    @property
    def LocalRouterId(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The PIM-SM Router ID value, in IPv4 format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalRouterId"])

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Multiplier"])

    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Multiplier"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NeighborV6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): (Auto Pick Neighbor must be disabled/not selected to make this field active) The user can manually type in the link-local address to be used for the Upstream Neighbor address field in the Join/Prune message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NeighborV6Address"])
        )

    @property
    def OverrideInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): (in ms) The delay interval for randomizing the transmission time for override messages-when scheduling a delayed Join message. The default value is 2,500 milliseconds (ms). The valid range is 100 to 7FFF msec. (This is part of the LAN Prune Delay option included in Hello messages).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OverrideInterval"])
        )

    @property
    def PruneDelay(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): (in ms) The value of the LAN Prune (propagation) Delay for this PIM-SM interface. The expected delay for messages propagated on the link. It indicates to an upstream router how long to wait for a Join override message before it prunes an interface. The default value is 500 msec. The valid range is 100 to 0x7FFF msec. (LAN Prune Delay is an Option included in Hello messages.)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PruneDelay"]))

    @property
    def SendBidirectional(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, sets the bi-directional PIM-SM flag bit (= 1) in Hello Message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendBidirectional"])
        )

    @property
    def SendGenerationIdOption(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, enables the Send Generation ID Option, and the Generation ID Mode field will become available to make a mode selection.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendGenerationIdOption"])
        )

    @property
    def SendGenerationMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The mode for creating the 32-bit value for the Generation Identifier (GenID) option in the Hello message. A new GenID is created each time an interface (or router) starts or restarts PIM-SM forwarding. A change in this value indicates to the neighbor(s) that a change of state may have occurred, and that the old PIM-SM states information received from those interfaces should be discarded. Choose one of: Incremental-the GenID increases by 1 for each successive Hello Message sent from this emulated PIM-SM router. Random-each Hello message sent from this emulated PIM-SM router will have a randomly-generated GenID. Constant (the default)-the GenID remains the same in all of the Hello Messages sent from this emulated. PIM-SM router.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendGenerationMode"])
        )

    @property
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionStatus"])

    @property
    def Sources(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Sources
        """
        return self._get_attribute(self._SDM_ATT_MAP["Sources"])

    @Sources.setter
    def Sources(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Sources"], value)

    @property
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP["StackedLayers"])

    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["StackedLayers"], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP["StateCounts"])

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Status"])

    @property
    def SupportUnicastBsm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, this supports the sending and processing of Unicast bootstrap messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SupportUnicastBsm"])
        )

    @property
    def TriggeredHelloDelay(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The time (in seconds) after which the router senses a delay in sending or receiving PIM-SM hello message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TriggeredHelloDelay"])
        )

    def update(
        self,
        ConnectedVia=None,
        CrpRanges=None,
        JoinPrunes=None,
        Multiplier=None,
        Name=None,
        Sources=None,
        StackedLayers=None,
    ):
        # type: (List[str], int, int, int, str, int, List[str]) -> PimV6Interface
        """Updates pimV6Interface resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - CrpRanges (number): Number of C-RP Ranges
        - JoinPrunes (number): Number of Join/Prunes
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - Sources (number): Number of Sources
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ConnectedVia=None,
        CrpRanges=None,
        JoinPrunes=None,
        Multiplier=None,
        Name=None,
        Sources=None,
        StackedLayers=None,
    ):
        # type: (List[str], int, int, int, str, int, List[str]) -> PimV6Interface
        """Adds a new pimV6Interface resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - CrpRanges (number): Number of C-RP Ranges
        - JoinPrunes (number): Number of Join/Prunes
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - Sources (number): Number of Sources
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved pimV6Interface resources using find and the newly added pimV6Interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained pimV6Interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ConnectedVia=None,
        Count=None,
        CrpRanges=None,
        DescriptiveName=None,
        Errors=None,
        JoinPrunes=None,
        LocalRouterId=None,
        Multiplier=None,
        Name=None,
        SessionStatus=None,
        Sources=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
    ):
        """Finds and retrieves pimV6Interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pimV6Interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pimV6Interface resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - CrpRanges (number): Number of C-RP Ranges
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - JoinPrunes (number): Number of Join/Prunes
        - LocalRouterId (list(str)): The PIM-SM Router ID value, in IPv4 format.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - Sources (number): Number of Sources
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching pimV6Interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pimV6Interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pimV6Interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
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
        return self._execute("abort", payload=payload, response_object=None)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def ClearLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the clearLearnedInfo operation on the server.

        Clear Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearLearnedInfo(async_operation=bool)
        --------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearLearnedInfo(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearLearnedInfo(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearLearnedInfo(Arg2=list, async_operation=bool)list
        -----------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("clearLearnedInfo", payload=payload, response_object=None)

    def GetLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getLearnedInfo operation on the server.

        Get Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getLearnedInfo(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("getLearnedInfo", payload=payload, response_object=None)

    def IncrementGenID(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the incrementGenID operation on the server.

        Increment GenID

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        incrementGenID(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        incrementGenID(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        incrementGenID(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
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
        return self._execute("incrementGenID", payload=payload, response_object=None)

    def IncrementGenId(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the incrementGenId operation on the server.

        Stops the protocol state machine for the given protocol session instances.

        incrementGenId(Arg2=list, async_operation=bool)list
        ---------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("incrementGenId", payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
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
        return self._execute("restartDown", payload=payload, response_object=None)

    def ResumeBSM(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the resumeBSM operation on the server.

        Resume Bootstrap

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumeBSM(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeBSM(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeBSM(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeBSM(Arg2=list, async_operation=bool)list
        ----------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("resumeBSM", payload=payload, response_object=None)

    def ResumeHello(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the resumeHello operation on the server.

        Resume Hello

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumeHello(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeHello(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeHello(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeHello(Arg2=list, async_operation=bool)list
        ------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("resumeHello", payload=payload, response_object=None)

    def SendBSM(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendBSM operation on the server.

        Stop Bootstrap

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendBSM(async_operation=bool)
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendBSM(SessionIndices=list, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendBSM(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendBSM(Arg2=list, async_operation=bool)list
        --------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("sendBSM", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
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
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=list, async_operation=bool)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=string, async_operation=bool)
        -------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
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
        return self._execute("stop", payload=payload, response_object=None)

    def StopBSM(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the stopBSM operation on the server.

        Stop Bootstrap

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopBSM(async_operation=bool)
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopBSM(SessionIndices=list, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopBSM(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopBSM(Arg2=list, async_operation=bool)list
        --------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("stopBSM", payload=payload, response_object=None)

    def StopHello(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopHello operation on the server.

        Stop Hello

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopHello(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopHello(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopHello(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
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
        return self._execute("stopHello", payload=payload, response_object=None)

    def Stophello(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the stophello operation on the server.

        Stops the protocol state machine for the given protocol session instances.

        stophello(Arg2=list, async_operation=bool)list
        ----------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("stophello", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        AutoPickNeighbor=None,
        BootstrapHashMaskLength=None,
        BootstrapInterval=None,
        BootstrapPriority=None,
        BootstrapTimeout=None,
        DfElectionBackoffPeriod=None,
        DfElectionOfferPeriod=None,
        DfElectionRobustness=None,
        DisableTriggered=None,
        DiscardLearnedRpInfo=None,
        EnableBfdRegistration=None,
        EnableBootstrap=None,
        EnablePrune=None,
        ForceSemantic=None,
        HelloHoldTime=None,
        HelloInterval=None,
        LanPruneTbit=None,
        LearnSelectedRpSet=None,
        NeighborV6Address=None,
        OverrideInterval=None,
        PruneDelay=None,
        SendBidirectional=None,
        SendGenerationIdOption=None,
        SendGenerationMode=None,
        SupportUnicastBsm=None,
        TriggeredHelloDelay=None,
    ):
        """Base class infrastructure that gets a list of pimV6Interface device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AutoPickNeighbor (str): optional regex of autoPickNeighbor
        - BootstrapHashMaskLength (str): optional regex of bootstrapHashMaskLength
        - BootstrapInterval (str): optional regex of bootstrapInterval
        - BootstrapPriority (str): optional regex of bootstrapPriority
        - BootstrapTimeout (str): optional regex of bootstrapTimeout
        - DfElectionBackoffPeriod (str): optional regex of dfElectionBackoffPeriod
        - DfElectionOfferPeriod (str): optional regex of dfElectionOfferPeriod
        - DfElectionRobustness (str): optional regex of dfElectionRobustness
        - DisableTriggered (str): optional regex of disableTriggered
        - DiscardLearnedRpInfo (str): optional regex of discardLearnedRpInfo
        - EnableBfdRegistration (str): optional regex of enableBfdRegistration
        - EnableBootstrap (str): optional regex of enableBootstrap
        - EnablePrune (str): optional regex of enablePrune
        - ForceSemantic (str): optional regex of forceSemantic
        - HelloHoldTime (str): optional regex of helloHoldTime
        - HelloInterval (str): optional regex of helloInterval
        - LanPruneTbit (str): optional regex of lanPruneTbit
        - LearnSelectedRpSet (str): optional regex of learnSelectedRpSet
        - NeighborV6Address (str): optional regex of neighborV6Address
        - OverrideInterval (str): optional regex of overrideInterval
        - PruneDelay (str): optional regex of pruneDelay
        - SendBidirectional (str): optional regex of sendBidirectional
        - SendGenerationIdOption (str): optional regex of sendGenerationIdOption
        - SendGenerationMode (str): optional regex of sendGenerationMode
        - SupportUnicastBsm (str): optional regex of supportUnicastBsm
        - TriggeredHelloDelay (str): optional regex of triggeredHelloDelay

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
