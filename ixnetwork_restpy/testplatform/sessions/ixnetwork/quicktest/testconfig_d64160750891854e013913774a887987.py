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


class TestConfig(Base):
    """The IxNetwork Test Configuration feature provides the ability to run predefined tests and allows the user to set some global test parameters for the individual test types.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "testConfig"
    _SDM_ATT_MAP = {
        "ApplyMode": "applyMode",
        "AssignGroupType": "assignGroupType",
        "BidirectionalOptionEnabled": "bidirectionalOptionEnabled",
        "BurstSize": "burstSize",
        "CalculateJitter": "calculateJitter",
        "CalculateLatency": "calculateLatency",
        "CalibrateLatency": "calibrateLatency",
        "CountRandomFrameSize": "countRandomFrameSize",
        "DelayAfterTransmit": "delayAfterTransmit",
        "DelayBetweenIterations": "delayBetweenIterations",
        "DelayMode": "delayMode",
        "DummyTrafficId": "dummyTrafficId",
        "Duration": "duration",
        "EnableDataIntegrity": "enableDataIntegrity",
        "EnableExtraIterations": "enableExtraIterations",
        "EnableExtraJoinFrames": "enableExtraJoinFrames",
        "EnableFastConvergence": "enableFastConvergence",
        "EnableLayer2": "enableLayer2",
        "EnableLeaveGroup": "enableLeaveGroup",
        "EnableMinFrameSize": "enableMinFrameSize",
        "EnableMulticastQuerier": "enableMulticastQuerier",
        "EnableRouterAlert": "enableRouterAlert",
        "ExtraFramesFirstGroupAddress": "extraFramesFirstGroupAddress",
        "ExtraFramesFirstGroupAddressIPv6": "extraFramesFirstGroupAddressIPv6",
        "ExtraFramesTotalGroupAddresses": "extraFramesTotalGroupAddresses",
        "ExtraIterationOffsets": "extraIterationOffsets",
        "FastConvergenceDuration": "fastConvergenceDuration",
        "FastConvergenceThreshold": "fastConvergenceThreshold",
        "FirstMulticastDestMACAddress": "firstMulticastDestMACAddress",
        "FloodedFramesEnabled": "floodedFramesEnabled",
        "ForceRegenerate": "forceRegenerate",
        "FrameSizeMode": "frameSizeMode",
        "Framesize": "framesize",
        "FramesizeList": "framesizeList",
        "GroupCapacityGreaterThan": "groupCapacityGreaterThan",
        "GroupDistributionType": "groupDistributionType",
        "IgmpV1Timeout": "igmpV1Timeout",
        "IgmpVersion": "igmpVersion",
        "Igmpv3MessageType": "igmpv3MessageType",
        "Igmpv3SourceAddrList": "igmpv3SourceAddrList",
        "IncMulticastDestMACAddress": "incMulticastDestMACAddress",
        "IncPortMACAddress": "incPortMACAddress",
        "IncrAddresses": "incrAddresses",
        "IncrStep": "incrStep",
        "InitialRate": "initialRate",
        "Ipv4Address": "ipv4Address",
        "Ipv6Address": "ipv6Address",
        "IsIPv6": "isIPv6",
        "IsMulticastAutomaticFrameData": "isMulticastAutomaticFrameData",
        "JoinDelayRefUnit": "joinDelayRefUnit",
        "JoinDelayRefValue": "joinDelayRefValue",
        "JoinLeaveAlgorithm": "joinLeaveAlgorithm",
        "JoinLeaveFramesPerGroup": "joinLeaveFramesPerGroup",
        "JoinLeaveMode": "joinLeaveMode",
        "JoinLeaveMultiplier": "joinLeaveMultiplier",
        "JoinLeaveRate": "joinLeaveRate",
        "JoinLeaveWaitTime": "joinLeaveWaitTime",
        "LatencyType": "latencyType",
        "LeaveDelayRefUnit": "leaveDelayRefUnit",
        "LeaveDelayRefValue": "leaveDelayRefValue",
        "LoadInitialRate": "loadInitialRate",
        "LoadType": "loadType",
        "LoadUnit": "loadUnit",
        "MapType": "mapType",
        "MaxIncrementFrameSize": "maxIncrementFrameSize",
        "MaxRandomFrameSize": "maxRandomFrameSize",
        "MaxRate": "maxRate",
        "MinIncrementFrameSize": "minIncrementFrameSize",
        "MinRandomFrameSize": "minRandomFrameSize",
        "MixedClassMulticast": "mixedClassMulticast",
        "MldVersion": "mldVersion",
        "Mldv2MessageType": "mldv2MessageType",
        "Mldv2SourceAddrList": "mldv2SourceAddrList",
        "NumAddresses": "numAddresses",
        "NumIterations": "numIterations",
        "NumTrials": "numTrials",
        "NumberOfExtraJoins": "numberOfExtraJoins",
        "Numtrials": "numtrials",
        "OffsetTime": "offsetTime",
        "PercentMaxRate": "percentMaxRate",
        "PercentMulticastFrames": "percentMulticastFrames",
        "PercentUnicastFrames": "percentUnicastFrames",
        "PortMACAddress": "portMACAddress",
        "ProtocolItem": "protocolItem",
        "RatePass": "ratePass",
        "ReportSequenceError": "reportSequenceError",
        "SendJoinsBeforeLeave": "sendJoinsBeforeLeave",
        "StaggeredStart": "staggeredStart",
        "StepIncrementFrameSize": "stepIncrementFrameSize",
        "SupportedTrafficTypes": "supportedTrafficTypes",
        "TestTrafficType": "testTrafficType",
        "TrafficBeforeJoinLeave": "trafficBeforeJoinLeave",
        "TxDelay": "txDelay",
        "Use3376mode": "use3376mode",
        "UsePercentOffsets": "usePercentOffsets",
    }
    _SDM_ENUM_MAP = {
        "assignGroupType": ["accumulated", "distributed"],
        "delayMode": ["average", "max"],
        "frameSizeMode": ["custom", "increment", "random"],
        "groupDistributionType": ["acrossHosts", "acrossPorts"],
        "igmpv3MessageType": ["exclude", "include"],
        "joinDelayRefUnit": ["ms", "ns", "us"],
        "joinLeaveAlgorithm": ["joinExisting", "joinNew"],
        "joinLeaveMode": ["join", "joinLeave", "leave"],
        "latencyType": ["cutThrough", "storeForward"],
        "leaveDelayRefUnit": ["ms", "ns", "us"],
        "loadType": [
            "binary",
            "combo",
            "custom",
            "fixed",
            "increment",
            "quickSearch",
            "random",
            "step",
            "unchanged",
        ],
        "loadUnit": [
            "bpsRate",
            "fpsRate",
            "gbpsRate",
            "gBpsRate",
            "kbpsRate",
            "kBpsRate",
            "mbpsRate",
            "mBpsRate",
            "percentMaxRate",
        ],
        "mldv2MessageType": ["exclude", "include"],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

    @property
    def ApplyMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplyMode"])

    @ApplyMode.setter
    def ApplyMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApplyMode"], value)

    @property
    def AssignGroupType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(accumulated | distributed): The type assigned to the type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssignGroupType"])

    @AssignGroupType.setter
    def AssignGroupType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AssignGroupType"], value)

    @property
    def BidirectionalOptionEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it shows the outer VLAN connections.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BidirectionalOptionEnabled"])

    @BidirectionalOptionEnabled.setter
    def BidirectionalOptionEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BidirectionalOptionEnabled"], value)

    @property
    def BurstSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of packets to send in a burst .
        """
        return self._get_attribute(self._SDM_ATT_MAP["BurstSize"])

    @BurstSize.setter
    def BurstSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BurstSize"], value)

    @property
    def CalculateJitter(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, calculates jitter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CalculateJitter"])

    @CalculateJitter.setter
    def CalculateJitter(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CalculateJitter"], value)

    @property
    def CalculateLatency(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, calculates the latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CalculateLatency"])

    @CalculateLatency.setter
    def CalculateLatency(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CalculateLatency"], value)

    @property
    def CalibrateLatency(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, calibrates the latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CalibrateLatency"])

    @CalibrateLatency.setter
    def CalibrateLatency(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CalibrateLatency"], value)

    @property
    def CountRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, randomly counts the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CountRandomFrameSize"])

    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CountRandomFrameSize"], value)

    @property
    def DelayAfterTransmit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: A delay that is inserted after transmit is complete, before it continues with the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"])

    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"], value)

    @property
    def DelayBetweenIterations(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The delay in time between iterations of trasmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayBetweenIterations"])

    @DelayBetweenIterations.setter
    def DelayBetweenIterations(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayBetweenIterations"], value)

    @property
    def DelayMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | max): The mode of delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayMode"])

    @DelayMode.setter
    def DelayMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayMode"], value)

    @property
    def DummyTrafficId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The id of the monitor traffic item
        """
        return self._get_attribute(self._SDM_ATT_MAP["DummyTrafficId"])

    @DummyTrafficId.setter
    def DummyTrafficId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DummyTrafficId"], value)

    @property
    def Duration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: sec
        """
        return self._get_attribute(self._SDM_ATT_MAP["Duration"])

    @Duration.setter
    def Duration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Duration"], value)

    @property
    def EnableDataIntegrity(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables data integrity test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDataIntegrity"])

    @EnableDataIntegrity.setter
    def EnableDataIntegrity(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDataIntegrity"], value)

    @property
    def EnableExtraIterations(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables extra iterations.Sets extra iteration offset values.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableExtraIterations"])

    @EnableExtraIterations.setter
    def EnableExtraIterations(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableExtraIterations"], value)

    @property
    def EnableExtraJoinFrames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables extra join frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableExtraJoinFrames"])

    @EnableExtraJoinFrames.setter
    def EnableExtraJoinFrames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableExtraJoinFrames"], value)

    @property
    def EnableFastConvergence(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables fast convergence.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableFastConvergence"])

    @EnableFastConvergence.setter
    def EnableFastConvergence(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableFastConvergence"], value)

    @property
    def EnableLayer2(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables Layer2 protocols.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLayer2"])

    @EnableLayer2.setter
    def EnableLayer2(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLayer2"], value)

    @property
    def EnableLeaveGroup(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables leave group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLeaveGroup"])

    @EnableLeaveGroup.setter
    def EnableLeaveGroup(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLeaveGroup"], value)

    @property
    def EnableMinFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables minimum frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMinFrameSize"])

    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMinFrameSize"], value)

    @property
    def EnableMulticastQuerier(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable Multicast Querier Settings
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMulticastQuerier"])

    @EnableMulticastQuerier.setter
    def EnableMulticastQuerier(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMulticastQuerier"], value)

    @property
    def EnableRouterAlert(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables router alert.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableRouterAlert"])

    @EnableRouterAlert.setter
    def EnableRouterAlert(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableRouterAlert"], value)

    @property
    def ExtraFramesFirstGroupAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The extra frames first group IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExtraFramesFirstGroupAddress"])

    @ExtraFramesFirstGroupAddress.setter
    def ExtraFramesFirstGroupAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExtraFramesFirstGroupAddress"], value)

    @property
    def ExtraFramesFirstGroupAddressIPv6(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The extra frames first group IPv6 address.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ExtraFramesFirstGroupAddressIPv6"]
        )

    @ExtraFramesFirstGroupAddressIPv6.setter
    def ExtraFramesFirstGroupAddressIPv6(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ExtraFramesFirstGroupAddressIPv6"], value
        )

    @property
    def ExtraFramesTotalGroupAddresses(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The extra frames total group address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExtraFramesTotalGroupAddresses"])

    @ExtraFramesTotalGroupAddresses.setter
    def ExtraFramesTotalGroupAddresses(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExtraFramesTotalGroupAddresses"], value)

    @property
    def ExtraIterationOffsets(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets extra iteration offset values.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExtraIterationOffsets"])

    @ExtraIterationOffsets.setter
    def ExtraIterationOffsets(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExtraIterationOffsets"], value)

    @property
    def FastConvergenceDuration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: sec
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastConvergenceDuration"])

    @FastConvergenceDuration.setter
    def FastConvergenceDuration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastConvergenceDuration"], value)

    @property
    def FastConvergenceThreshold(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, enables fast convergence threshold value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastConvergenceThreshold"])

    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastConvergenceThreshold"], value)

    @property
    def FirstMulticastDestMACAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first multicast destination MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirstMulticastDestMACAddress"])

    @FirstMulticastDestMACAddress.setter
    def FirstMulticastDestMACAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirstMulticastDestMACAddress"], value)

    @property
    def FloodedFramesEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it enables the flooded frames statistics
        """
        return self._get_attribute(self._SDM_ATT_MAP["FloodedFramesEnabled"])

    @FloodedFramesEnabled.setter
    def FloodedFramesEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FloodedFramesEnabled"], value)

    @property
    def ForceRegenerate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Initiates a forced regeneration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForceRegenerate"])

    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForceRegenerate"], value)

    @property
    def FrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | increment | random): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameSizeMode"])

    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameSizeMode"], value)

    @property
    def Framesize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Bytes
        """
        return self._get_attribute(self._SDM_ATT_MAP["Framesize"])

    @Framesize.setter
    def Framesize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Framesize"], value)

    @property
    def FramesizeList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The list of the available frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesizeList"])

    @FramesizeList.setter
    def FramesizeList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesizeList"], value)

    @property
    def GroupCapacityGreaterThan(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The greater value of group capacity.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupCapacityGreaterThan"])

    @GroupCapacityGreaterThan.setter
    def GroupCapacityGreaterThan(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupCapacityGreaterThan"], value)

    @property
    def GroupDistributionType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(acrossHosts | acrossPorts): The type of group distribution.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupDistributionType"])

    @GroupDistributionType.setter
    def GroupDistributionType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupDistributionType"], value)

    @property
    def IgmpV1Timeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The IGMPv1 timeout value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IgmpV1Timeout"])

    @IgmpV1Timeout.setter
    def IgmpV1Timeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IgmpV1Timeout"], value)

    @property
    def IgmpVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The version of IGMP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IgmpVersion"])

    @IgmpVersion.setter
    def IgmpVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IgmpVersion"], value)

    @property
    def Igmpv3MessageType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(exclude | include): The message type of IGMPv3.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Igmpv3MessageType"])

    @Igmpv3MessageType.setter
    def Igmpv3MessageType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Igmpv3MessageType"], value)

    @property
    def Igmpv3SourceAddrList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The source address list of IGMPv3.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Igmpv3SourceAddrList"])

    @Igmpv3SourceAddrList.setter
    def Igmpv3SourceAddrList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Igmpv3SourceAddrList"], value)

    @property
    def IncMulticastDestMACAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The incrementing multicast destination MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncMulticastDestMACAddress"])

    @IncMulticastDestMACAddress.setter
    def IncMulticastDestMACAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncMulticastDestMACAddress"], value)

    @property
    def IncPortMACAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The incrementing MAC address of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncPortMACAddress"])

    @IncPortMACAddress.setter
    def IncPortMACAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncPortMACAddress"], value)

    @property
    def IncrAddresses(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The incremental address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrAddresses"])

    @IncrAddresses.setter
    def IncrAddresses(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrAddresses"], value)

    @property
    def IncrStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The incremental step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrStep"])

    @IncrStep.setter
    def IncrStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrStep"], value)

    @property
    def InitialRate(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first rate of transmission.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialRate"])

    @InitialRate.setter
    def InitialRate(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialRate"], value)

    @property
    def Ipv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The allocated IPv4 address for this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Address"])

    @Ipv4Address.setter
    def Ipv4Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4Address"], value)

    @property
    def Ipv6Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The allocated IPv6address for this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Address"])

    @Ipv6Address.setter
    def Ipv6Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6Address"], value)

    @property
    def IsIPv6(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies if the address is an ipv6 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsIPv6"])

    @IsIPv6.setter
    def IsIPv6(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsIPv6"], value)

    @property
    def IsMulticastAutomaticFrameData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies automatic frameData for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsMulticastAutomaticFrameData"])

    @IsMulticastAutomaticFrameData.setter
    def IsMulticastAutomaticFrameData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsMulticastAutomaticFrameData"], value)

    @property
    def JoinDelayRefUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | ns | us): The reference unit of join delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinDelayRefUnit"])

    @JoinDelayRefUnit.setter
    def JoinDelayRefUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinDelayRefUnit"], value)

    @property
    def JoinDelayRefValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The reference value of join delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinDelayRefValue"])

    @JoinDelayRefValue.setter
    def JoinDelayRefValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinDelayRefValue"], value)

    @property
    def JoinLeaveAlgorithm(self):
        # type: () -> str
        """
        Returns
        -------
        - str(joinExisting | joinNew): The algorithm for join leave.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinLeaveAlgorithm"])

    @JoinLeaveAlgorithm.setter
    def JoinLeaveAlgorithm(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinLeaveAlgorithm"], value)

    @property
    def JoinLeaveFramesPerGroup(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The join leave frames per group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinLeaveFramesPerGroup"])

    @JoinLeaveFramesPerGroup.setter
    def JoinLeaveFramesPerGroup(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinLeaveFramesPerGroup"], value)

    @property
    def JoinLeaveMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(join | joinLeave | leave): The mode of join leave delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinLeaveMode"])

    @JoinLeaveMode.setter
    def JoinLeaveMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinLeaveMode"], value)

    @property
    def JoinLeaveMultiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinLeaveMultiplier"])

    @JoinLeaveMultiplier.setter
    def JoinLeaveMultiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinLeaveMultiplier"], value)

    @property
    def JoinLeaveRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The join leave rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinLeaveRate"])

    @JoinLeaveRate.setter
    def JoinLeaveRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinLeaveRate"], value)

    @property
    def JoinLeaveWaitTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The wait time for join delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinLeaveWaitTime"])

    @JoinLeaveWaitTime.setter
    def JoinLeaveWaitTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinLeaveWaitTime"], value)

    @property
    def LatencyType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cutThrough | storeForward): The type of latency
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyType"])

    @LatencyType.setter
    def LatencyType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyType"], value)

    @property
    def LeaveDelayRefUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | ns | us): The reference unit of leave delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LeaveDelayRefUnit"])

    @LeaveDelayRefUnit.setter
    def LeaveDelayRefUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LeaveDelayRefUnit"], value)

    @property
    def LeaveDelayRefValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The leave delay reference value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LeaveDelayRefValue"])

    @LeaveDelayRefValue.setter
    def LeaveDelayRefValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LeaveDelayRefValue"], value)

    @property
    def LoadInitialRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The initial load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadInitialRate"])

    @LoadInitialRate.setter
    def LoadInitialRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadInitialRate"], value)

    @property
    def LoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged): The type of the payload setting
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadType"])

    @LoadType.setter
    def LoadType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadType"], value)

    @property
    def LoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the step rate of the load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadUnit"])

    @LoadUnit.setter
    def LoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadUnit"], value)

    @property
    def MapType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The POS traffic map type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapType"])

    @MapType.setter
    def MapType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapType"], value)

    @property
    def MaxIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum incremental value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxIncrementFrameSize"])

    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxIncrementFrameSize"], value)

    @property
    def MaxRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxRandomFrameSize"])

    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxRandomFrameSize"], value)

    @property
    def MaxRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxRate"])

    @MaxRate.setter
    def MaxRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxRate"], value)

    @property
    def MinIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum incremental value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinIncrementFrameSize"])

    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinIncrementFrameSize"], value)

    @property
    def MinRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRandomFrameSize"])

    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRandomFrameSize"], value)

    @property
    def MixedClassMulticast(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The mixed multicast class.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MixedClassMulticast"])

    @MixedClassMulticast.setter
    def MixedClassMulticast(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MixedClassMulticast"], value)

    @property
    def MldVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The version of MLD.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MldVersion"])

    @MldVersion.setter
    def MldVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MldVersion"], value)

    @property
    def Mldv2MessageType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(exclude | include): Signifies the message type of mldv2.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mldv2MessageType"])

    @Mldv2MessageType.setter
    def Mldv2MessageType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mldv2MessageType"], value)

    @property
    def Mldv2SourceAddrList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The source address list of mldv2.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mldv2SourceAddrList"])

    @Mldv2SourceAddrList.setter
    def Mldv2SourceAddrList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mldv2SourceAddrList"], value)

    @property
    def NumAddresses(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumAddresses"])

    @NumAddresses.setter
    def NumAddresses(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumAddresses"], value)

    @property
    def NumIterations(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of iterations.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumIterations"])

    @NumIterations.setter
    def NumIterations(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumIterations"], value)

    @property
    def NumTrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number: %
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumTrials"])

    @NumTrials.setter
    def NumTrials(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumTrials"], value)

    @property
    def NumberOfExtraJoins(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of extra joins in the address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfExtraJoins"])

    @NumberOfExtraJoins.setter
    def NumberOfExtraJoins(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfExtraJoins"], value)

    @property
    def Numtrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Numtrials"])

    @Numtrials.setter
    def Numtrials(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Numtrials"], value)

    @property
    def OffsetTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The offset time value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OffsetTime"])

    @OffsetTime.setter
    def OffsetTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OffsetTime"], value)

    @property
    def PercentMaxRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the step rate of the load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PercentMaxRate"])

    @PercentMaxRate.setter
    def PercentMaxRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PercentMaxRate"], value)

    @property
    def PercentMulticastFrames(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The percentage of multicast frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PercentMulticastFrames"])

    @PercentMulticastFrames.setter
    def PercentMulticastFrames(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PercentMulticastFrames"], value)

    @property
    def PercentUnicastFrames(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The percentage of unicast frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PercentUnicastFrames"])

    @PercentUnicastFrames.setter
    def PercentUnicastFrames(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PercentUnicastFrames"], value)

    @property
    def PortMACAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The MAC address of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortMACAddress"])

    @PortMACAddress.setter
    def PortMACAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortMACAddress"], value)

    @property
    def ProtocolItem(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan]): Protocol Items
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolItem"])

    @ProtocolItem.setter
    def ProtocolItem(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtocolItem"], value)

    @property
    def RatePass(self):
        # type: () -> int
        """
        Returns
        -------
        - number: A Pass criteria applied to each trial in the test to determine whether the trialpassed or failed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RatePass"])

    @RatePass.setter
    def RatePass(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RatePass"], value)

    @property
    def ReportSequenceError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Reports sequence errors in the test result.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportSequenceError"])

    @ReportSequenceError.setter
    def ReportSequenceError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportSequenceError"], value)

    @property
    def SendJoinsBeforeLeave(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendJoinsBeforeLeave"])

    @SendJoinsBeforeLeave.setter
    def SendJoinsBeforeLeave(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendJoinsBeforeLeave"], value)

    @property
    def StaggeredStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Starts test with a stagger.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StaggeredStart"])

    @StaggeredStart.setter
    def StaggeredStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StaggeredStart"], value)

    @property
    def StepIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The incremental step value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepIncrementFrameSize"])

    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepIncrementFrameSize"], value)

    @property
    def SupportedTrafficTypes(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The traffic types supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportedTrafficTypes"])

    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportedTrafficTypes"], value)

    @property
    def TestTrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the test traffic type value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestTrafficType"])

    @TestTrafficType.setter
    def TestTrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestTrafficType"], value)

    @property
    def TrafficBeforeJoinLeave(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The traffic sent before join leave.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficBeforeJoinLeave"])

    @TrafficBeforeJoinLeave.setter
    def TrafficBeforeJoinLeave(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficBeforeJoinLeave"], value)

    @property
    def TxDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the amount of delay after every transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxDelay"])

    @TxDelay.setter
    def TxDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxDelay"], value)

    @property
    def Use3376mode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Use3376mode"])

    @Use3376mode.setter
    def Use3376mode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Use3376mode"], value)

    @property
    def UsePercentOffsets(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Uses percentage offset value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UsePercentOffsets"])

    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UsePercentOffsets"], value)

    def update(
        self,
        ApplyMode=None,
        AssignGroupType=None,
        BidirectionalOptionEnabled=None,
        BurstSize=None,
        CalculateJitter=None,
        CalculateLatency=None,
        CalibrateLatency=None,
        CountRandomFrameSize=None,
        DelayAfterTransmit=None,
        DelayBetweenIterations=None,
        DelayMode=None,
        DummyTrafficId=None,
        Duration=None,
        EnableDataIntegrity=None,
        EnableExtraIterations=None,
        EnableExtraJoinFrames=None,
        EnableFastConvergence=None,
        EnableLayer2=None,
        EnableLeaveGroup=None,
        EnableMinFrameSize=None,
        EnableMulticastQuerier=None,
        EnableRouterAlert=None,
        ExtraFramesFirstGroupAddress=None,
        ExtraFramesFirstGroupAddressIPv6=None,
        ExtraFramesTotalGroupAddresses=None,
        ExtraIterationOffsets=None,
        FastConvergenceDuration=None,
        FastConvergenceThreshold=None,
        FirstMulticastDestMACAddress=None,
        FloodedFramesEnabled=None,
        ForceRegenerate=None,
        FrameSizeMode=None,
        Framesize=None,
        FramesizeList=None,
        GroupCapacityGreaterThan=None,
        GroupDistributionType=None,
        IgmpV1Timeout=None,
        IgmpVersion=None,
        Igmpv3MessageType=None,
        Igmpv3SourceAddrList=None,
        IncMulticastDestMACAddress=None,
        IncPortMACAddress=None,
        IncrAddresses=None,
        IncrStep=None,
        InitialRate=None,
        Ipv4Address=None,
        Ipv6Address=None,
        IsIPv6=None,
        IsMulticastAutomaticFrameData=None,
        JoinDelayRefUnit=None,
        JoinDelayRefValue=None,
        JoinLeaveAlgorithm=None,
        JoinLeaveFramesPerGroup=None,
        JoinLeaveMode=None,
        JoinLeaveMultiplier=None,
        JoinLeaveRate=None,
        JoinLeaveWaitTime=None,
        LatencyType=None,
        LeaveDelayRefUnit=None,
        LeaveDelayRefValue=None,
        LoadInitialRate=None,
        LoadType=None,
        LoadUnit=None,
        MapType=None,
        MaxIncrementFrameSize=None,
        MaxRandomFrameSize=None,
        MaxRate=None,
        MinIncrementFrameSize=None,
        MinRandomFrameSize=None,
        MixedClassMulticast=None,
        MldVersion=None,
        Mldv2MessageType=None,
        Mldv2SourceAddrList=None,
        NumAddresses=None,
        NumIterations=None,
        NumTrials=None,
        NumberOfExtraJoins=None,
        Numtrials=None,
        OffsetTime=None,
        PercentMaxRate=None,
        PercentMulticastFrames=None,
        PercentUnicastFrames=None,
        PortMACAddress=None,
        ProtocolItem=None,
        RatePass=None,
        ReportSequenceError=None,
        SendJoinsBeforeLeave=None,
        StaggeredStart=None,
        StepIncrementFrameSize=None,
        SupportedTrafficTypes=None,
        TestTrafficType=None,
        TrafficBeforeJoinLeave=None,
        TxDelay=None,
        Use3376mode=None,
        UsePercentOffsets=None,
    ):
        # type: (str, str, bool, int, bool, bool, bool, int, int, int, str, str, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, int, str, int, int, str, bool, bool, str, int, List[str], int, str, int, int, str, str, str, str, int, int, str, str, str, str, str, str, int, str, int, str, int, int, int, str, str, int, int, str, str, str, int, int, int, int, int, str, int, str, str, int, int, int, int, int, int, int, int, int, str, List[str], int, bool, bool, bool, int, str, str, bool, int, bool, bool) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): The type assigned to the type.
        - BidirectionalOptionEnabled (bool): If enabled, it shows the outer VLAN connections.
        - BurstSize (number): The number of packets to send in a burst .
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calculates the latency.
        - CalibrateLatency (bool): If true, calibrates the latency.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - DelayAfterTransmit (number): A delay that is inserted after transmit is complete, before it continues with the test.
        - DelayBetweenIterations (number): The delay in time between iterations of trasmit.
        - DelayMode (str(average | max)): The mode of delay.
        - DummyTrafficId (str): The id of the monitor traffic item
        - Duration (number): sec
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableExtraIterations (bool): If true, enables extra iterations.Sets extra iteration offset values.
        - EnableExtraJoinFrames (bool): If true, enables extra join frames.
        - EnableFastConvergence (bool): If true, enables fast convergence.
        - EnableLayer2 (bool): If true, enables Layer2 protocols.
        - EnableLeaveGroup (bool): If true, enables leave group.
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableRouterAlert (bool): If true, enables router alert.
        - ExtraFramesFirstGroupAddress (str): The extra frames first group IP address.
        - ExtraFramesFirstGroupAddressIPv6 (str): The extra frames first group IPv6 address.
        - ExtraFramesTotalGroupAddresses (number): The extra frames total group address.
        - ExtraIterationOffsets (str): Sets extra iteration offset values.
        - FastConvergenceDuration (number): sec
        - FastConvergenceThreshold (number): If true, enables fast convergence threshold value.
        - FirstMulticastDestMACAddress (str): The first multicast destination MAC address.
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameSizeMode (str(custom | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - Framesize (number): Bytes
        - FramesizeList (list(str)): The list of the available frame size.
        - GroupCapacityGreaterThan (number): The greater value of group capacity.
        - GroupDistributionType (str(acrossHosts | acrossPorts)): The type of group distribution.
        - IgmpV1Timeout (number): The IGMPv1 timeout value.
        - IgmpVersion (number): The version of IGMP.
        - Igmpv3MessageType (str(exclude | include)): The message type of IGMPv3.
        - Igmpv3SourceAddrList (str): The source address list of IGMPv3.
        - IncMulticastDestMACAddress (str): The incrementing multicast destination MAC address.
        - IncPortMACAddress (str): The incrementing MAC address of the port.
        - IncrAddresses (number): The incremental address.
        - IncrStep (number): The incremental step value.
        - InitialRate (str): The first rate of transmission.
        - Ipv4Address (str): The allocated IPv4 address for this interface.
        - Ipv6Address (str): The allocated IPv6address for this interface.
        - IsIPv6 (str): Signifies if the address is an ipv6 address.
        - IsMulticastAutomaticFrameData (str): Signifies automatic frameData for multicast.
        - JoinDelayRefUnit (str(ms | ns | us)): The reference unit of join delay.
        - JoinDelayRefValue (number): The reference value of join delay.
        - JoinLeaveAlgorithm (str(joinExisting | joinNew)): The algorithm for join leave.
        - JoinLeaveFramesPerGroup (number): The join leave frames per group.
        - JoinLeaveMode (str(join | joinLeave | leave)): The mode of join leave delay.
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): The join leave rate.
        - JoinLeaveWaitTime (number): The wait time for join delay.
        - LatencyType (str(cutThrough | storeForward)): The type of latency
        - LeaveDelayRefUnit (str(ms | ns | us)): The reference unit of leave delay.
        - LeaveDelayRefValue (number): The leave delay reference value.
        - LoadInitialRate (number): The initial load rate.
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)): The type of the payload setting
        - LoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the step rate of the load unit.
        - MapType (str): The POS traffic map type.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxRate (number): The maximum rate.
        - MinIncrementFrameSize (number): The minimum incremental value of the frame size.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - MixedClassMulticast (str): The mixed multicast class.
        - MldVersion (number): The version of MLD.
        - Mldv2MessageType (str(exclude | include)): Signifies the message type of mldv2.
        - Mldv2SourceAddrList (str): The source address list of mldv2.
        - NumAddresses (number): The number address.
        - NumIterations (number): The number of iterations.
        - NumTrials (number): %
        - NumberOfExtraJoins (number): The number of extra joins in the address.
        - Numtrials (number): The number address.
        - OffsetTime (number): The offset time value.
        - PercentMaxRate (number): Specifies the step rate of the load unit.
        - PercentMulticastFrames (number): The percentage of multicast frames.
        - PercentUnicastFrames (number): The percentage of unicast frames.
        - PortMACAddress (str): The MAC address of the port.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - RatePass (number): A Pass criteria applied to each trial in the test to determine whether the trialpassed or failed.
        - ReportSequenceError (bool): Reports sequence errors in the test result.
        - SendJoinsBeforeLeave (bool):
        - StaggeredStart (bool): Starts test with a stagger.
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TestTrafficType (str): It signifies the test traffic type value.
        - TrafficBeforeJoinLeave (bool): The traffic sent before join leave.
        - TxDelay (number): Specifies the amount of delay after every transmit.
        - Use3376mode (bool):
        - UsePercentOffsets (bool): Uses percentage offset value.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ApplyMode=None,
        AssignGroupType=None,
        BidirectionalOptionEnabled=None,
        BurstSize=None,
        CalculateJitter=None,
        CalculateLatency=None,
        CalibrateLatency=None,
        CountRandomFrameSize=None,
        DelayAfterTransmit=None,
        DelayBetweenIterations=None,
        DelayMode=None,
        DummyTrafficId=None,
        Duration=None,
        EnableDataIntegrity=None,
        EnableExtraIterations=None,
        EnableExtraJoinFrames=None,
        EnableFastConvergence=None,
        EnableLayer2=None,
        EnableLeaveGroup=None,
        EnableMinFrameSize=None,
        EnableMulticastQuerier=None,
        EnableRouterAlert=None,
        ExtraFramesFirstGroupAddress=None,
        ExtraFramesFirstGroupAddressIPv6=None,
        ExtraFramesTotalGroupAddresses=None,
        ExtraIterationOffsets=None,
        FastConvergenceDuration=None,
        FastConvergenceThreshold=None,
        FirstMulticastDestMACAddress=None,
        FloodedFramesEnabled=None,
        ForceRegenerate=None,
        FrameSizeMode=None,
        Framesize=None,
        FramesizeList=None,
        GroupCapacityGreaterThan=None,
        GroupDistributionType=None,
        IgmpV1Timeout=None,
        IgmpVersion=None,
        Igmpv3MessageType=None,
        Igmpv3SourceAddrList=None,
        IncMulticastDestMACAddress=None,
        IncPortMACAddress=None,
        IncrAddresses=None,
        IncrStep=None,
        InitialRate=None,
        Ipv4Address=None,
        Ipv6Address=None,
        IsIPv6=None,
        IsMulticastAutomaticFrameData=None,
        JoinDelayRefUnit=None,
        JoinDelayRefValue=None,
        JoinLeaveAlgorithm=None,
        JoinLeaveFramesPerGroup=None,
        JoinLeaveMode=None,
        JoinLeaveMultiplier=None,
        JoinLeaveRate=None,
        JoinLeaveWaitTime=None,
        LatencyType=None,
        LeaveDelayRefUnit=None,
        LeaveDelayRefValue=None,
        LoadInitialRate=None,
        LoadType=None,
        LoadUnit=None,
        MapType=None,
        MaxIncrementFrameSize=None,
        MaxRandomFrameSize=None,
        MaxRate=None,
        MinIncrementFrameSize=None,
        MinRandomFrameSize=None,
        MixedClassMulticast=None,
        MldVersion=None,
        Mldv2MessageType=None,
        Mldv2SourceAddrList=None,
        NumAddresses=None,
        NumIterations=None,
        NumTrials=None,
        NumberOfExtraJoins=None,
        Numtrials=None,
        OffsetTime=None,
        PercentMaxRate=None,
        PercentMulticastFrames=None,
        PercentUnicastFrames=None,
        PortMACAddress=None,
        ProtocolItem=None,
        RatePass=None,
        ReportSequenceError=None,
        SendJoinsBeforeLeave=None,
        StaggeredStart=None,
        StepIncrementFrameSize=None,
        SupportedTrafficTypes=None,
        TestTrafficType=None,
        TrafficBeforeJoinLeave=None,
        TxDelay=None,
        Use3376mode=None,
        UsePercentOffsets=None,
    ):
        # type: (str, str, bool, int, bool, bool, bool, int, int, int, str, str, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, int, str, int, int, str, bool, bool, str, int, List[str], int, str, int, int, str, str, str, str, int, int, str, str, str, str, str, str, int, str, int, str, int, int, int, str, str, int, int, str, str, str, int, int, int, int, int, str, int, str, str, int, int, int, int, int, int, int, int, int, str, List[str], int, bool, bool, bool, int, str, str, bool, int, bool, bool) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): The type assigned to the type.
        - BidirectionalOptionEnabled (bool): If enabled, it shows the outer VLAN connections.
        - BurstSize (number): The number of packets to send in a burst .
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calculates the latency.
        - CalibrateLatency (bool): If true, calibrates the latency.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - DelayAfterTransmit (number): A delay that is inserted after transmit is complete, before it continues with the test.
        - DelayBetweenIterations (number): The delay in time between iterations of trasmit.
        - DelayMode (str(average | max)): The mode of delay.
        - DummyTrafficId (str): The id of the monitor traffic item
        - Duration (number): sec
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableExtraIterations (bool): If true, enables extra iterations.Sets extra iteration offset values.
        - EnableExtraJoinFrames (bool): If true, enables extra join frames.
        - EnableFastConvergence (bool): If true, enables fast convergence.
        - EnableLayer2 (bool): If true, enables Layer2 protocols.
        - EnableLeaveGroup (bool): If true, enables leave group.
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableRouterAlert (bool): If true, enables router alert.
        - ExtraFramesFirstGroupAddress (str): The extra frames first group IP address.
        - ExtraFramesFirstGroupAddressIPv6 (str): The extra frames first group IPv6 address.
        - ExtraFramesTotalGroupAddresses (number): The extra frames total group address.
        - ExtraIterationOffsets (str): Sets extra iteration offset values.
        - FastConvergenceDuration (number): sec
        - FastConvergenceThreshold (number): If true, enables fast convergence threshold value.
        - FirstMulticastDestMACAddress (str): The first multicast destination MAC address.
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameSizeMode (str(custom | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - Framesize (number): Bytes
        - FramesizeList (list(str)): The list of the available frame size.
        - GroupCapacityGreaterThan (number): The greater value of group capacity.
        - GroupDistributionType (str(acrossHosts | acrossPorts)): The type of group distribution.
        - IgmpV1Timeout (number): The IGMPv1 timeout value.
        - IgmpVersion (number): The version of IGMP.
        - Igmpv3MessageType (str(exclude | include)): The message type of IGMPv3.
        - Igmpv3SourceAddrList (str): The source address list of IGMPv3.
        - IncMulticastDestMACAddress (str): The incrementing multicast destination MAC address.
        - IncPortMACAddress (str): The incrementing MAC address of the port.
        - IncrAddresses (number): The incremental address.
        - IncrStep (number): The incremental step value.
        - InitialRate (str): The first rate of transmission.
        - Ipv4Address (str): The allocated IPv4 address for this interface.
        - Ipv6Address (str): The allocated IPv6address for this interface.
        - IsIPv6 (str): Signifies if the address is an ipv6 address.
        - IsMulticastAutomaticFrameData (str): Signifies automatic frameData for multicast.
        - JoinDelayRefUnit (str(ms | ns | us)): The reference unit of join delay.
        - JoinDelayRefValue (number): The reference value of join delay.
        - JoinLeaveAlgorithm (str(joinExisting | joinNew)): The algorithm for join leave.
        - JoinLeaveFramesPerGroup (number): The join leave frames per group.
        - JoinLeaveMode (str(join | joinLeave | leave)): The mode of join leave delay.
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): The join leave rate.
        - JoinLeaveWaitTime (number): The wait time for join delay.
        - LatencyType (str(cutThrough | storeForward)): The type of latency
        - LeaveDelayRefUnit (str(ms | ns | us)): The reference unit of leave delay.
        - LeaveDelayRefValue (number): The leave delay reference value.
        - LoadInitialRate (number): The initial load rate.
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)): The type of the payload setting
        - LoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the step rate of the load unit.
        - MapType (str): The POS traffic map type.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxRate (number): The maximum rate.
        - MinIncrementFrameSize (number): The minimum incremental value of the frame size.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - MixedClassMulticast (str): The mixed multicast class.
        - MldVersion (number): The version of MLD.
        - Mldv2MessageType (str(exclude | include)): Signifies the message type of mldv2.
        - Mldv2SourceAddrList (str): The source address list of mldv2.
        - NumAddresses (number): The number address.
        - NumIterations (number): The number of iterations.
        - NumTrials (number): %
        - NumberOfExtraJoins (number): The number of extra joins in the address.
        - Numtrials (number): The number address.
        - OffsetTime (number): The offset time value.
        - PercentMaxRate (number): Specifies the step rate of the load unit.
        - PercentMulticastFrames (number): The percentage of multicast frames.
        - PercentUnicastFrames (number): The percentage of unicast frames.
        - PortMACAddress (str): The MAC address of the port.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - RatePass (number): A Pass criteria applied to each trial in the test to determine whether the trialpassed or failed.
        - ReportSequenceError (bool): Reports sequence errors in the test result.
        - SendJoinsBeforeLeave (bool):
        - StaggeredStart (bool): Starts test with a stagger.
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TestTrafficType (str): It signifies the test traffic type value.
        - TrafficBeforeJoinLeave (bool): The traffic sent before join leave.
        - TxDelay (number): Specifies the amount of delay after every transmit.
        - Use3376mode (bool):
        - UsePercentOffsets (bool): Uses percentage offset value.

        Returns
        -------
        - self: This instance with matching testConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of testConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the testConfig resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
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
        return self._execute("apply", payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
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
        return self._execute("applyAsync", payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool:

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
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
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
        return self._execute(
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

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
        return self._execute("generateReport", payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

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
        return self._execute("run", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
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
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
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
        return self._execute("stop", payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

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
        return self._execute("waitForTest", payload=payload, response_object=None)
