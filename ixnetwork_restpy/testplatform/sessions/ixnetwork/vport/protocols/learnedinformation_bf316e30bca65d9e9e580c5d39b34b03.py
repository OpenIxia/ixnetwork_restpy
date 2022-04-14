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


class LearnedInformation(Base):
    """This object displays the information learned from each router.
    The LearnedInformation class encapsulates a list of learnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "learnedInformation"
    _SDM_ATT_MAP = {
        "DestinationAddressIpv4": "destinationAddressIpv4",
        "DownstreamAddressType": "downstreamAddressType",
        "DownstreamInterfaceAddress": "downstreamInterfaceAddress",
        "DownstreamIpAddress": "downstreamIpAddress",
        "EchoResponseTimeoutMs": "echoResponseTimeoutMs",
        "EnableAdvance": "enableAdvance",
        "EnableDsiFlag": "enableDsiFlag",
        "EnableDsnFlag": "enableDsnFlag",
        "EnableFecValidation": "enableFecValidation",
        "EnableIncludeDownstreamMappingTlv": "enableIncludeDownstreamMappingTlv",
        "EnableIncludePadTlv": "enableIncludePadTlv",
        "EnableIncludeVendorEnterpriseNumberTlv": "enableIncludeVendorEnterpriseNumberTlv",
        "EnablePauseResumeBfdPduTrigger": "enablePauseResumeBfdPduTrigger",
        "EnablePauseResumeReplyTrigger": "enablePauseResumeReplyTrigger",
        "EnableSendTriggeredPing": "enableSendTriggeredPing",
        "EnableSendTriggeredTraceroute": "enableSendTriggeredTraceroute",
        "EnableSetResetEchoReplyCodeTrigger": "enableSetResetEchoReplyCodeTrigger",
        "IsGeneralLearnedInformationRefreshed": "isGeneralLearnedInformationRefreshed",
        "IsTriggeredPingLearnedInformationRefreshed": "isTriggeredPingLearnedInformationRefreshed",
        "IsTriggeredTraceRouteLearnedInformationRefreshed": "isTriggeredTraceRouteLearnedInformationRefreshed",
        "PadTlvFirstOctetOptions": "padTlvFirstOctetOptions",
        "PadTlvLength": "padTlvLength",
        "PauseResumeBfdPduTriggerOption": "pauseResumeBfdPduTriggerOption",
        "PauseResumeReplyTriggerOption": "pauseResumeReplyTriggerOption",
        "ReplyMode": "replyMode",
        "ReturnCodeOption": "returnCodeOption",
        "ReturnSubCode": "returnSubCode",
        "TriggerOptions": "triggerOptions",
        "TriggerType": "triggerType",
        "TtlLimit": "ttlLimit",
        "VendorEnterpriseNumber": "vendorEnterpriseNumber",
    }
    _SDM_ENUM_MAP = {
        "downstreamAddressType": ["ipv4Numbered", "ipv4UnNumbered"],
        "padTlvFirstOctetOptions": ["dropPadTlvFromReply", "copyPadTlvToReply"],
        "pauseResumeBfdPduTriggerOption": ["pause", "resume"],
        "pauseResumeReplyTriggerOption": ["pause", "resume"],
        "replyMode": [
            "doNotReply",
            "replyViaIpv4Ipv6UdpPacket",
            "replyViaIpv4Ipv6UdpPacketWithRouterAlert",
            "replyViaApplicationLevelControlChannel",
        ],
        "returnCodeOption": [
            "noReturnCode",
            "malformedEchoRequestReceived",
            "oneOrMoreOfTheTlvsWasNotUnderstood",
            "replyingRouterIsAnEgressForTheFecAtStackDepthRsc",
            "replyingRouterHasNoMappingForTheFecAtStackDepthRsc",
            "downstreamMappingMismatch",
            "upstreamInterfaceIndexUnknown",
            "lspPingReserved",
            "labelSwitchedAtStackDepthRsc",
            "labelSwitchedButNoMplsForwardingAtStackDepthRsc",
            "mappingForThisFecIsNotTheGivenLabelAtStackDepthRsc",
            "noLabelEntryAtStackDepthRsc",
            "protocolNotAssociatedWithInterfaceatFecStackDepthRsc",
            "prematureTerminationOfPingDueToLabelStackShrinkingToSingleLabel",
        ],
        "triggerOptions": ["tx", "rx", "txRx"],
        "triggerType": ["resetToNormalReply", "forceReplyCode"],
    }

    def __init__(self, parent, list_op=False):
        super(LearnedInformation, self).__init__(parent, list_op)

    @property
    def GeneralLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.generallearnedinfo_9cb8a8283663cc3094a8443009722083.GeneralLearnedInfo): An instance of the GeneralLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.generallearnedinfo_9cb8a8283663cc3094a8443009722083 import (
            GeneralLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("GeneralLearnedInfo", None) is not None:
                return self._properties.get("GeneralLearnedInfo")
        return GeneralLearnedInfo(self)

    @property
    def TriggeredPingLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.triggeredpinglearnedinfo_350be9d7c8dd6514556f2297763ef94b.TriggeredPingLearnedInfo): An instance of the TriggeredPingLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.triggeredpinglearnedinfo_350be9d7c8dd6514556f2297763ef94b import (
            TriggeredPingLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TriggeredPingLearnedInfo", None) is not None:
                return self._properties.get("TriggeredPingLearnedInfo")
        return TriggeredPingLearnedInfo(self)

    @property
    def TriggeredTracerouteLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.triggeredtraceroutelearnedinfo_abc82c355a1d42abb4a65edfe0c6864c.TriggeredTracerouteLearnedInfo): An instance of the TriggeredTracerouteLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.triggeredtraceroutelearnedinfo_abc82c355a1d42abb4a65edfe0c6864c import (
            TriggeredTracerouteLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TriggeredTracerouteLearnedInfo", None) is not None:
                return self._properties.get("TriggeredTracerouteLearnedInfo")
        return TriggeredTracerouteLearnedInfo(self)

    @property
    def DestinationAddressIpv4(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the destination IPv4 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationAddressIpv4"])

    @DestinationAddressIpv4.setter
    def DestinationAddressIpv4(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestinationAddressIpv4"], value)

    @property
    def DownstreamAddressType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipv4Numbered | ipv4UnNumbered): This signifies the address type of the downstream traffic. Possible values include Ipv4Numbered and Ipv4UnNumbered.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamAddressType"])

    @DownstreamAddressType.setter
    def DownstreamAddressType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamAddressType"], value)

    @property
    def DownstreamInterfaceAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the interface address of the downstream LSR.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamInterfaceAddress"])

    @DownstreamInterfaceAddress.setter
    def DownstreamInterfaceAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamInterfaceAddress"], value)

    @property
    def DownstreamIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the IPv4/IPv6 address of the downstream LSR.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamIpAddress"])

    @DownstreamIpAddress.setter
    def DownstreamIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamIpAddress"], value)

    @property
    def EchoResponseTimeoutMs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the minimum tiomeout interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoResponseTimeoutMs"])

    @EchoResponseTimeoutMs.setter
    def EchoResponseTimeoutMs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoResponseTimeoutMs"], value)

    @property
    def EnableAdvance(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of advance.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAdvance"])

    @EnableAdvance.setter
    def EnableAdvance(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAdvance"], value)

    @property
    def EnableDsiFlag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the activation of the DS I Flag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDsiFlag"])

    @EnableDsiFlag.setter
    def EnableDsiFlag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDsiFlag"], value)

    @property
    def EnableDsnFlag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the activation of the DN S Flag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDsnFlag"])

    @EnableDsnFlag.setter
    def EnableDsnFlag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDsnFlag"], value)

    @property
    def EnableFecValidation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the selection of the check box to enable FEC validation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableFecValidation"])

    @EnableFecValidation.setter
    def EnableFecValidation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableFecValidation"], value)

    @property
    def EnableIncludeDownstreamMappingTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the inclusion of the downstream mapping TLV in triggered Trace Route.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableIncludeDownstreamMappingTlv"]
        )

    @EnableIncludeDownstreamMappingTlv.setter
    def EnableIncludeDownstreamMappingTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableIncludeDownstreamMappingTlv"], value
        )

    @property
    def EnableIncludePadTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the selection of the check box to include Pad TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableIncludePadTlv"])

    @EnableIncludePadTlv.setter
    def EnableIncludePadTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableIncludePadTlv"], value)

    @property
    def EnableIncludeVendorEnterpriseNumberTlv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the selection of the checkbox to include the the TLV number of the vendor organization.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableIncludeVendorEnterpriseNumberTlv"]
        )

    @EnableIncludeVendorEnterpriseNumberTlv.setter
    def EnableIncludeVendorEnterpriseNumberTlv(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableIncludeVendorEnterpriseNumberTlv"], value
        )

    @property
    def EnablePauseResumeBfdPduTrigger(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the pausing of the BFD PDU trigger.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePauseResumeBfdPduTrigger"])

    @EnablePauseResumeBfdPduTrigger.setter
    def EnablePauseResumeBfdPduTrigger(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePauseResumeBfdPduTrigger"], value)

    @property
    def EnablePauseResumeReplyTrigger(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the pausing of the reply trigger.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePauseResumeReplyTrigger"])

    @EnablePauseResumeReplyTrigger.setter
    def EnablePauseResumeReplyTrigger(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePauseResumeReplyTrigger"], value)

    @property
    def EnableSendTriggeredPing(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the sending of the triggered ping.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSendTriggeredPing"])

    @EnableSendTriggeredPing.setter
    def EnableSendTriggeredPing(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSendTriggeredPing"], value)

    @property
    def EnableSendTriggeredTraceroute(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the enablement of the sending of triggered trace route.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSendTriggeredTraceroute"])

    @EnableSendTriggeredTraceroute.setter
    def EnableSendTriggeredTraceroute(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSendTriggeredTraceroute"], value)

    @property
    def EnableSetResetEchoReplyCodeTrigger(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the setting of the echo reply code trigger.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSetResetEchoReplyCodeTrigger"]
        )

    @EnableSetResetEchoReplyCodeTrigger.setter
    def EnableSetResetEchoReplyCodeTrigger(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSetResetEchoReplyCodeTrigger"], value
        )

    @property
    def IsGeneralLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the refreshing of the general learned information.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsGeneralLearnedInformationRefreshed"]
        )

    @property
    def IsTriggeredPingLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the checking of if the Triggered ping learned information is refreshed.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsTriggeredPingLearnedInformationRefreshed"]
        )

    @property
    def IsTriggeredTraceRouteLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the checking of if the Triggered Trace route information is refreshed.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsTriggeredTraceRouteLearnedInformationRefreshed"]
        )

    @property
    def PadTlvFirstOctetOptions(self):
        # type: () -> str
        """
        Returns
        -------
        - str(dropPadTlvFromReply | copyPadTlvToReply): This signifies the first octate of Pad TLV in triggered ping. Possible values include CopyPadTlvToReply and DropPadTlvFromReply.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PadTlvFirstOctetOptions"])

    @PadTlvFirstOctetOptions.setter
    def PadTlvFirstOctetOptions(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PadTlvFirstOctetOptions"], value)

    @property
    def PadTlvLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the specification of the length of the Pad TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PadTlvLength"])

    @PadTlvLength.setter
    def PadTlvLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PadTlvLength"], value)

    @property
    def PauseResumeBfdPduTriggerOption(self):
        # type: () -> str
        """
        Returns
        -------
        - str(pause | resume): This signifies the pausing of the BFD PDU trigger option.Possible values include Pause and Resume.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PauseResumeBfdPduTriggerOption"])

    @PauseResumeBfdPduTriggerOption.setter
    def PauseResumeBfdPduTriggerOption(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PauseResumeBfdPduTriggerOption"], value)

    @property
    def PauseResumeReplyTriggerOption(self):
        # type: () -> str
        """
        Returns
        -------
        - str(pause | resume): This signifies the pausing of the reply trigger option. Possible values include Pause and Resume.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PauseResumeReplyTriggerOption"])

    @PauseResumeReplyTriggerOption.setter
    def PauseResumeReplyTriggerOption(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PauseResumeReplyTriggerOption"], value)

    @property
    def ReplyMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel): This signifies the selection of the mode of reply. Possible values include:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReplyMode"])

    @ReplyMode.setter
    def ReplyMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReplyMode"], value)

    @property
    def ReturnCodeOption(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noReturnCode | malformedEchoRequestReceived | oneOrMoreOfTheTlvsWasNotUnderstood | replyingRouterIsAnEgressForTheFecAtStackDepthRsc | replyingRouterHasNoMappingForTheFecAtStackDepthRsc | downstreamMappingMismatch | upstreamInterfaceIndexUnknown | lspPingReserved | labelSwitchedAtStackDepthRsc | labelSwitchedButNoMplsForwardingAtStackDepthRsc | mappingForThisFecIsNotTheGivenLabelAtStackDepthRsc | noLabelEntryAtStackDepthRsc | protocolNotAssociatedWithInterfaceatFecStackDepthRsc | prematureTerminationOfPingDueToLabelStackShrinkingToSingleLabel): This signifies the return code option value. Possible values include:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReturnCodeOption"])

    @ReturnCodeOption.setter
    def ReturnCodeOption(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReturnCodeOption"], value)

    @property
    def ReturnSubCode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the return subcode value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReturnSubCode"])

    @ReturnSubCode.setter
    def ReturnSubCode(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReturnSubCode"], value)

    @property
    def TriggerOptions(self):
        # type: () -> str
        """
        Returns
        -------
        - str(tx | rx | txRx): This signifies the trigger option value. Possible values include:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerOptions"])

    @TriggerOptions.setter
    def TriggerOptions(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerOptions"], value)

    @property
    def TriggerType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(resetToNormalReply | forceReplyCode): This signifies the type of the trigger. Possible values include:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggerType"])

    @TriggerType.setter
    def TriggerType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggerType"], value)

    @property
    def TtlLimit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the maximum value of TTL up to which the TTL will be incremented while sending echo request packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TtlLimit"])

    @TtlLimit.setter
    def TtlLimit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TtlLimit"], value)

    @property
    def VendorEnterpriseNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the specification of the enterprise number of the vendor.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorEnterpriseNumber"])

    @VendorEnterpriseNumber.setter
    def VendorEnterpriseNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorEnterpriseNumber"], value)

    def update(
        self,
        DestinationAddressIpv4=None,
        DownstreamAddressType=None,
        DownstreamInterfaceAddress=None,
        DownstreamIpAddress=None,
        EchoResponseTimeoutMs=None,
        EnableAdvance=None,
        EnableDsiFlag=None,
        EnableDsnFlag=None,
        EnableFecValidation=None,
        EnableIncludeDownstreamMappingTlv=None,
        EnableIncludePadTlv=None,
        EnableIncludeVendorEnterpriseNumberTlv=None,
        EnablePauseResumeBfdPduTrigger=None,
        EnablePauseResumeReplyTrigger=None,
        EnableSendTriggeredPing=None,
        EnableSendTriggeredTraceroute=None,
        EnableSetResetEchoReplyCodeTrigger=None,
        PadTlvFirstOctetOptions=None,
        PadTlvLength=None,
        PauseResumeBfdPduTriggerOption=None,
        PauseResumeReplyTriggerOption=None,
        ReplyMode=None,
        ReturnCodeOption=None,
        ReturnSubCode=None,
        TriggerOptions=None,
        TriggerType=None,
        TtlLimit=None,
        VendorEnterpriseNumber=None,
    ):
        # type: (str, str, str, str, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, int, str, str, str, str, int, str, str, int, int) -> LearnedInformation
        """Updates learnedInformation resource on the server.

        Args
        ----
        - DestinationAddressIpv4 (str): This signifies the destination IPv4 address.
        - DownstreamAddressType (str(ipv4Numbered | ipv4UnNumbered)): This signifies the address type of the downstream traffic. Possible values include Ipv4Numbered and Ipv4UnNumbered.
        - DownstreamInterfaceAddress (str): This signifies the interface address of the downstream LSR.
        - DownstreamIpAddress (str): This signifies the IPv4/IPv6 address of the downstream LSR.
        - EchoResponseTimeoutMs (number): This signifies the minimum tiomeout interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
        - EnableAdvance (bool): This signifies the enablement of advance.
        - EnableDsiFlag (bool): This signifies the activation of the DS I Flag.
        - EnableDsnFlag (bool): This signifies the activation of the DN S Flag.
        - EnableFecValidation (bool): This signifies the selection of the check box to enable FEC validation.
        - EnableIncludeDownstreamMappingTlv (bool): This signifies the inclusion of the downstream mapping TLV in triggered Trace Route.
        - EnableIncludePadTlv (bool): This signifies the selection of the check box to include Pad TLV.
        - EnableIncludeVendorEnterpriseNumberTlv (bool): This signifies the selection of the checkbox to include the the TLV number of the vendor organization.
        - EnablePauseResumeBfdPduTrigger (bool): This signifies the pausing of the BFD PDU trigger.
        - EnablePauseResumeReplyTrigger (bool): This signifies the pausing of the reply trigger.
        - EnableSendTriggeredPing (bool): This signifies the sending of the triggered ping.
        - EnableSendTriggeredTraceroute (bool): This signifies the enablement of the sending of triggered trace route.
        - EnableSetResetEchoReplyCodeTrigger (bool): This signifies the setting of the echo reply code trigger.
        - PadTlvFirstOctetOptions (str(dropPadTlvFromReply | copyPadTlvToReply)): This signifies the first octate of Pad TLV in triggered ping. Possible values include CopyPadTlvToReply and DropPadTlvFromReply.
        - PadTlvLength (number): This signifies the specification of the length of the Pad TLV.
        - PauseResumeBfdPduTriggerOption (str(pause | resume)): This signifies the pausing of the BFD PDU trigger option.Possible values include Pause and Resume.
        - PauseResumeReplyTriggerOption (str(pause | resume)): This signifies the pausing of the reply trigger option. Possible values include Pause and Resume.
        - ReplyMode (str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel)): This signifies the selection of the mode of reply. Possible values include:
        - ReturnCodeOption (str(noReturnCode | malformedEchoRequestReceived | oneOrMoreOfTheTlvsWasNotUnderstood | replyingRouterIsAnEgressForTheFecAtStackDepthRsc | replyingRouterHasNoMappingForTheFecAtStackDepthRsc | downstreamMappingMismatch | upstreamInterfaceIndexUnknown | lspPingReserved | labelSwitchedAtStackDepthRsc | labelSwitchedButNoMplsForwardingAtStackDepthRsc | mappingForThisFecIsNotTheGivenLabelAtStackDepthRsc | noLabelEntryAtStackDepthRsc | protocolNotAssociatedWithInterfaceatFecStackDepthRsc | prematureTerminationOfPingDueToLabelStackShrinkingToSingleLabel)): This signifies the return code option value. Possible values include:
        - ReturnSubCode (number): This signifies the return subcode value.
        - TriggerOptions (str(tx | rx | txRx)): This signifies the trigger option value. Possible values include:
        - TriggerType (str(resetToNormalReply | forceReplyCode)): This signifies the type of the trigger. Possible values include:
        - TtlLimit (number): This signifies the maximum value of TTL up to which the TTL will be incremented while sending echo request packets.
        - VendorEnterpriseNumber (number): This signifies the specification of the enterprise number of the vendor.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        DestinationAddressIpv4=None,
        DownstreamAddressType=None,
        DownstreamInterfaceAddress=None,
        DownstreamIpAddress=None,
        EchoResponseTimeoutMs=None,
        EnableAdvance=None,
        EnableDsiFlag=None,
        EnableDsnFlag=None,
        EnableFecValidation=None,
        EnableIncludeDownstreamMappingTlv=None,
        EnableIncludePadTlv=None,
        EnableIncludeVendorEnterpriseNumberTlv=None,
        EnablePauseResumeBfdPduTrigger=None,
        EnablePauseResumeReplyTrigger=None,
        EnableSendTriggeredPing=None,
        EnableSendTriggeredTraceroute=None,
        EnableSetResetEchoReplyCodeTrigger=None,
        PadTlvFirstOctetOptions=None,
        PadTlvLength=None,
        PauseResumeBfdPduTriggerOption=None,
        PauseResumeReplyTriggerOption=None,
        ReplyMode=None,
        ReturnCodeOption=None,
        ReturnSubCode=None,
        TriggerOptions=None,
        TriggerType=None,
        TtlLimit=None,
        VendorEnterpriseNumber=None,
    ):
        # type: (str, str, str, str, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, int, str, str, str, str, int, str, str, int, int) -> LearnedInformation
        """Adds a new learnedInformation resource on the json, only valid with batch add utility

        Args
        ----
        - DestinationAddressIpv4 (str): This signifies the destination IPv4 address.
        - DownstreamAddressType (str(ipv4Numbered | ipv4UnNumbered)): This signifies the address type of the downstream traffic. Possible values include Ipv4Numbered and Ipv4UnNumbered.
        - DownstreamInterfaceAddress (str): This signifies the interface address of the downstream LSR.
        - DownstreamIpAddress (str): This signifies the IPv4/IPv6 address of the downstream LSR.
        - EchoResponseTimeoutMs (number): This signifies the minimum tiomeout interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
        - EnableAdvance (bool): This signifies the enablement of advance.
        - EnableDsiFlag (bool): This signifies the activation of the DS I Flag.
        - EnableDsnFlag (bool): This signifies the activation of the DN S Flag.
        - EnableFecValidation (bool): This signifies the selection of the check box to enable FEC validation.
        - EnableIncludeDownstreamMappingTlv (bool): This signifies the inclusion of the downstream mapping TLV in triggered Trace Route.
        - EnableIncludePadTlv (bool): This signifies the selection of the check box to include Pad TLV.
        - EnableIncludeVendorEnterpriseNumberTlv (bool): This signifies the selection of the checkbox to include the the TLV number of the vendor organization.
        - EnablePauseResumeBfdPduTrigger (bool): This signifies the pausing of the BFD PDU trigger.
        - EnablePauseResumeReplyTrigger (bool): This signifies the pausing of the reply trigger.
        - EnableSendTriggeredPing (bool): This signifies the sending of the triggered ping.
        - EnableSendTriggeredTraceroute (bool): This signifies the enablement of the sending of triggered trace route.
        - EnableSetResetEchoReplyCodeTrigger (bool): This signifies the setting of the echo reply code trigger.
        - PadTlvFirstOctetOptions (str(dropPadTlvFromReply | copyPadTlvToReply)): This signifies the first octate of Pad TLV in triggered ping. Possible values include CopyPadTlvToReply and DropPadTlvFromReply.
        - PadTlvLength (number): This signifies the specification of the length of the Pad TLV.
        - PauseResumeBfdPduTriggerOption (str(pause | resume)): This signifies the pausing of the BFD PDU trigger option.Possible values include Pause and Resume.
        - PauseResumeReplyTriggerOption (str(pause | resume)): This signifies the pausing of the reply trigger option. Possible values include Pause and Resume.
        - ReplyMode (str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel)): This signifies the selection of the mode of reply. Possible values include:
        - ReturnCodeOption (str(noReturnCode | malformedEchoRequestReceived | oneOrMoreOfTheTlvsWasNotUnderstood | replyingRouterIsAnEgressForTheFecAtStackDepthRsc | replyingRouterHasNoMappingForTheFecAtStackDepthRsc | downstreamMappingMismatch | upstreamInterfaceIndexUnknown | lspPingReserved | labelSwitchedAtStackDepthRsc | labelSwitchedButNoMplsForwardingAtStackDepthRsc | mappingForThisFecIsNotTheGivenLabelAtStackDepthRsc | noLabelEntryAtStackDepthRsc | protocolNotAssociatedWithInterfaceatFecStackDepthRsc | prematureTerminationOfPingDueToLabelStackShrinkingToSingleLabel)): This signifies the return code option value. Possible values include:
        - ReturnSubCode (number): This signifies the return subcode value.
        - TriggerOptions (str(tx | rx | txRx)): This signifies the trigger option value. Possible values include:
        - TriggerType (str(resetToNormalReply | forceReplyCode)): This signifies the type of the trigger. Possible values include:
        - TtlLimit (number): This signifies the maximum value of TTL up to which the TTL will be incremented while sending echo request packets.
        - VendorEnterpriseNumber (number): This signifies the specification of the enterprise number of the vendor.

        Returns
        -------
        - self: This instance with all currently retrieved learnedInformation resources using find and the newly added learnedInformation resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        DestinationAddressIpv4=None,
        DownstreamAddressType=None,
        DownstreamInterfaceAddress=None,
        DownstreamIpAddress=None,
        EchoResponseTimeoutMs=None,
        EnableAdvance=None,
        EnableDsiFlag=None,
        EnableDsnFlag=None,
        EnableFecValidation=None,
        EnableIncludeDownstreamMappingTlv=None,
        EnableIncludePadTlv=None,
        EnableIncludeVendorEnterpriseNumberTlv=None,
        EnablePauseResumeBfdPduTrigger=None,
        EnablePauseResumeReplyTrigger=None,
        EnableSendTriggeredPing=None,
        EnableSendTriggeredTraceroute=None,
        EnableSetResetEchoReplyCodeTrigger=None,
        IsGeneralLearnedInformationRefreshed=None,
        IsTriggeredPingLearnedInformationRefreshed=None,
        IsTriggeredTraceRouteLearnedInformationRefreshed=None,
        PadTlvFirstOctetOptions=None,
        PadTlvLength=None,
        PauseResumeBfdPduTriggerOption=None,
        PauseResumeReplyTriggerOption=None,
        ReplyMode=None,
        ReturnCodeOption=None,
        ReturnSubCode=None,
        TriggerOptions=None,
        TriggerType=None,
        TtlLimit=None,
        VendorEnterpriseNumber=None,
    ):
        # type: (str, str, str, str, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, int, str, str, str, str, int, str, str, int, int) -> LearnedInformation
        """Finds and retrieves learnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInformation resources from the server.

        Args
        ----
        - DestinationAddressIpv4 (str): This signifies the destination IPv4 address.
        - DownstreamAddressType (str(ipv4Numbered | ipv4UnNumbered)): This signifies the address type of the downstream traffic. Possible values include Ipv4Numbered and Ipv4UnNumbered.
        - DownstreamInterfaceAddress (str): This signifies the interface address of the downstream LSR.
        - DownstreamIpAddress (str): This signifies the IPv4/IPv6 address of the downstream LSR.
        - EchoResponseTimeoutMs (number): This signifies the minimum tiomeout interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
        - EnableAdvance (bool): This signifies the enablement of advance.
        - EnableDsiFlag (bool): This signifies the activation of the DS I Flag.
        - EnableDsnFlag (bool): This signifies the activation of the DN S Flag.
        - EnableFecValidation (bool): This signifies the selection of the check box to enable FEC validation.
        - EnableIncludeDownstreamMappingTlv (bool): This signifies the inclusion of the downstream mapping TLV in triggered Trace Route.
        - EnableIncludePadTlv (bool): This signifies the selection of the check box to include Pad TLV.
        - EnableIncludeVendorEnterpriseNumberTlv (bool): This signifies the selection of the checkbox to include the the TLV number of the vendor organization.
        - EnablePauseResumeBfdPduTrigger (bool): This signifies the pausing of the BFD PDU trigger.
        - EnablePauseResumeReplyTrigger (bool): This signifies the pausing of the reply trigger.
        - EnableSendTriggeredPing (bool): This signifies the sending of the triggered ping.
        - EnableSendTriggeredTraceroute (bool): This signifies the enablement of the sending of triggered trace route.
        - EnableSetResetEchoReplyCodeTrigger (bool): This signifies the setting of the echo reply code trigger.
        - IsGeneralLearnedInformationRefreshed (bool): This signifies the refreshing of the general learned information.
        - IsTriggeredPingLearnedInformationRefreshed (bool): This signifies the checking of if the Triggered ping learned information is refreshed.
        - IsTriggeredTraceRouteLearnedInformationRefreshed (bool): This signifies the checking of if the Triggered Trace route information is refreshed.
        - PadTlvFirstOctetOptions (str(dropPadTlvFromReply | copyPadTlvToReply)): This signifies the first octate of Pad TLV in triggered ping. Possible values include CopyPadTlvToReply and DropPadTlvFromReply.
        - PadTlvLength (number): This signifies the specification of the length of the Pad TLV.
        - PauseResumeBfdPduTriggerOption (str(pause | resume)): This signifies the pausing of the BFD PDU trigger option.Possible values include Pause and Resume.
        - PauseResumeReplyTriggerOption (str(pause | resume)): This signifies the pausing of the reply trigger option. Possible values include Pause and Resume.
        - ReplyMode (str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel)): This signifies the selection of the mode of reply. Possible values include:
        - ReturnCodeOption (str(noReturnCode | malformedEchoRequestReceived | oneOrMoreOfTheTlvsWasNotUnderstood | replyingRouterIsAnEgressForTheFecAtStackDepthRsc | replyingRouterHasNoMappingForTheFecAtStackDepthRsc | downstreamMappingMismatch | upstreamInterfaceIndexUnknown | lspPingReserved | labelSwitchedAtStackDepthRsc | labelSwitchedButNoMplsForwardingAtStackDepthRsc | mappingForThisFecIsNotTheGivenLabelAtStackDepthRsc | noLabelEntryAtStackDepthRsc | protocolNotAssociatedWithInterfaceatFecStackDepthRsc | prematureTerminationOfPingDueToLabelStackShrinkingToSingleLabel)): This signifies the return code option value. Possible values include:
        - ReturnSubCode (number): This signifies the return subcode value.
        - TriggerOptions (str(tx | rx | txRx)): This signifies the trigger option value. Possible values include:
        - TriggerType (str(resetToNormalReply | forceReplyCode)): This signifies the type of the trigger. Possible values include:
        - TtlLimit (number): This signifies the maximum value of TTL up to which the TTL will be incremented while sending echo request packets.
        - VendorEnterpriseNumber (number): This signifies the specification of the enterprise number of the vendor.

        Returns
        -------
        - self: This instance with matching learnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ClearRecordsForTrigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the clearRecordsForTrigger operation on the server.

        This signifies the record cleared for trigger settings.

        clearRecordsForTrigger(async_operation=bool)bool
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "clearRecordsForTrigger", payload=payload, response_object=None
        )

    def RefreshLearnedInformation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshLearnedInformation operation on the server.

        This signifies that the learned information is refreshed.

        refreshLearnedInformation(async_operation=bool)bool
        ---------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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

    def Trigger(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the trigger operation on the server.

        This signifies the learned info trigger settings.

        trigger(async_operation=bool)number
        -----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: NOT DEFINED

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
        return self._execute("trigger", payload=payload, response_object=None)
