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
    """It signifies the configuration of the test.
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
        "CountRandomFrameSize": "countRandomFrameSize",
        "DelayAfterTransmit": "delayAfterTransmit",
        "Duration": "duration",
        "EnableDataIntegrity": "enableDataIntegrity",
        "EnableLayer1Rate": "enableLayer1Rate",
        "EnableLeaveGroup": "enableLeaveGroup",
        "EnableMinFrameSize": "enableMinFrameSize",
        "EnableMulticastQuerier": "enableMulticastQuerier",
        "EnableOldStatsForReef": "enableOldStatsForReef",
        "FirstMulticastDestMACAddress": "firstMulticastDestMACAddress",
        "FloodedFramesEnabled": "floodedFramesEnabled",
        "ForceRegenerate": "forceRegenerate",
        "FrameSizeMode": "frameSizeMode",
        "FramesizeList": "framesizeList",
        "Gap": "gap",
        "GroupCapacityGreaterThan": "groupCapacityGreaterThan",
        "GroupDistributionType": "groupDistributionType",
        "IgmpV1Timeout": "igmpV1Timeout",
        "IgmpVersion": "igmpVersion",
        "Igmpv3MessageType": "igmpv3MessageType",
        "Igmpv3SourceAddrList": "igmpv3SourceAddrList",
        "IncMulticastDestMACAddress": "incMulticastDestMACAddress",
        "IncPortMACAddress": "incPortMACAddress",
        "IncrAddresses": "incrAddresses",
        "InitialRate": "initialRate",
        "InitialStepLoadRate": "initialStepLoadRate",
        "Ipv4Address": "ipv4Address",
        "Ipv6Address": "ipv6Address",
        "IsIPv6": "isIPv6",
        "IsMulticastAutomaticFrameData": "isMulticastAutomaticFrameData",
        "JoinLeaveMultiplier": "joinLeaveMultiplier",
        "JoinLeaveRate": "joinLeaveRate",
        "JoinLeaveWaitTime": "joinLeaveWaitTime",
        "LatencyBins": "latencyBins",
        "LatencyBinsEnabled": "latencyBinsEnabled",
        "LatencyType": "latencyType",
        "LoadInitialRate": "loadInitialRate",
        "LoadRateList": "loadRateList",
        "LoadType": "loadType",
        "MapType": "mapType",
        "MaxIncrementFrameSize": "maxIncrementFrameSize",
        "MaxRandomFrameSize": "maxRandomFrameSize",
        "MaxStepLoadRate": "maxStepLoadRate",
        "MinIncrementFrameSize": "minIncrementFrameSize",
        "MinRandomFrameSize": "minRandomFrameSize",
        "MixedClassMulticast": "mixedClassMulticast",
        "MldVersion": "mldVersion",
        "NumAddresses": "numAddresses",
        "NumIterations": "numIterations",
        "Numtrials": "numtrials",
        "PortDelayEnabled": "portDelayEnabled",
        "PortDelayUnit": "portDelayUnit",
        "PortDelayValue": "portDelayValue",
        "PortMACAddress": "portMACAddress",
        "ProtocolItem": "protocolItem",
        "ReportSequenceError": "reportSequenceError",
        "ReportTputRateUnit": "reportTputRateUnit",
        "RouterAlert": "routerAlert",
        "StepIncrementFrameSize": "stepIncrementFrameSize",
        "StepLoadUnit": "stepLoadUnit",
        "StepStepLoadRate": "stepStepLoadRate",
        "SupportedTrafficTypes": "supportedTrafficTypes",
        "TestTrafficType": "testTrafficType",
        "TxDelay": "txDelay",
    }
    _SDM_ENUM_MAP = {
        "assignGroupType": ["accumulated", "distributed"],
        "frameSizeMode": ["custom", "fixed", "increment", "random"],
        "groupDistributionType": ["acrossHosts", "acrossPorts"],
        "igmpv3MessageType": ["exclude", "include"],
        "latencyType": ["cutThrough", "storeForward"],
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
        "portDelayUnit": ["bytes", "nanoseconds"],
        "reportTputRateUnit": ["gbps", "gBps", "kbps", "kBps", "mbps", "mBps"],
        "stepLoadUnit": [
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
        - str(accumulated | distributed): It assigns the group type.
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
        - bool: If true, the bidirectional option is enabled.
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
        - number: The number of packets that are sent in a burst.
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
        - bool: If true, the jitter is calculated.
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
        - bool: If true, the latency is calculated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CalculateLatency"])

    @CalculateLatency.setter
    def CalculateLatency(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CalculateLatency"], value)

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
        - number: The amount of delay after every transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"])

    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"], value)

    @property
    def Duration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The duration of the test in hours, which is used to calculate the number of frames to transmit.
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
    def EnableLayer1Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLayer1Rate"])

    @EnableLayer1Rate.setter
    def EnableLayer1Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLayer1Rate"], value)

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
    def EnableOldStatsForReef(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: It enables the old statistics for reef.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOldStatsForReef"])

    @EnableOldStatsForReef.setter
    def EnableOldStatsForReef(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOldStatsForReef"], value)

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
        - str(custom | fixed | increment | random): This attribute is the frame size mode for the Quad Gaussian. The Quad Gaussian is the superposition of four Gaussian distributions.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameSizeMode"])

    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameSizeMode"], value)

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
    def Gap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The gap in transmission of frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Gap"])

    @Gap.setter
    def Gap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Gap"], value)

    @property
    def GroupCapacityGreaterThan(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The integer that distinguishes the group capacity that could be greater than the specified integer.
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
        - str(acrossHosts | acrossPorts): It signifies group distribution type.
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
        - number: It signifies the timeout of version 1 of IGMP.
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
        - number: It signifies the version of IGMP.
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
        - str(exclude | include): It gives details about the igmpv3 message type in the test configuration
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
        - str: It gives details about the igmpv3 source address list in the test configuration
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
        - number: If true, the MAC address is incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrAddresses"])

    @IncrAddresses.setter
    def IncrAddresses(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrAddresses"], value)

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
    def InitialStepLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The initial step value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialStepLoadRate"])

    @InitialStepLoadRate.setter
    def InitialStepLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialStepLoadRate"], value)

    @property
    def Ipv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the IP address for version 4.
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
        - str: It signifies the IP address for version 6.
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
        - str: If true, configures IPv6 address.
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
        - str: If true, configures multicast automatic frame data.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsMulticastAutomaticFrameData"])

    @IsMulticastAutomaticFrameData.setter
    def IsMulticastAutomaticFrameData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsMulticastAutomaticFrameData"], value)

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
        - number: It signifies the join and leave rate.
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
        - number: The wait time for the leave.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinLeaveWaitTime"])

    @JoinLeaveWaitTime.setter
    def JoinLeaveWaitTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinLeaveWaitTime"], value)

    @property
    def LatencyBins(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Sets the latency bins statistics
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyBins"])

    @LatencyBins.setter
    def LatencyBins(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyBins"], value)

    @property
    def LatencyBinsEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the latency bins statistics
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyBinsEnabled"])

    @LatencyBinsEnabled.setter
    def LatencyBinsEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyBinsEnabled"], value)

    @property
    def LatencyType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cutThrough | storeForward): The type of latency required by the DUT to forward frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyType"])

    @LatencyType.setter
    def LatencyType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyType"], value)

    @property
    def LoadInitialRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The initial rate of the load.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadInitialRate"])

    @LoadInitialRate.setter
    def LoadInitialRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadInitialRate"], value)

    @property
    def LoadRateList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The list of Load Rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadRateList"])

    @LoadRateList.setter
    def LoadRateList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadRateList"], value)

    @property
    def LoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged): The type of the payload setting.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadType"])

    @LoadType.setter
    def LoadType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadType"], value)

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
    def MaxStepLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum step load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxStepLoadRate"])

    @MaxStepLoadRate.setter
    def MaxStepLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxStepLoadRate"], value)

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
        - number: It signifies the MLD version.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MldVersion"])

    @MldVersion.setter
    def MldVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MldVersion"], value)

    @property
    def NumAddresses(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The integer value for the number of addresses.
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
    def Numtrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The integer value that states the number of trials permitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Numtrials"])

    @Numtrials.setter
    def Numtrials(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Numtrials"], value)

    @property
    def PortDelayEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDelayEnabled"])

    @PortDelayEnabled.setter
    def PortDelayEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDelayEnabled"], value)

    @property
    def PortDelayUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDelayUnit"])

    @PortDelayUnit.setter
    def PortDelayUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDelayUnit"], value)

    @property
    def PortDelayValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the port delay value
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDelayValue"])

    @PortDelayValue.setter
    def PortDelayValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDelayValue"], value)

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
    def ReportSequenceError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Reports sequence errors in the test result
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportSequenceError"])

    @ReportSequenceError.setter
    def ReportSequenceError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportSequenceError"], value)

    @property
    def ReportTputRateUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(gbps | gBps | kbps | kBps | mbps | mBps): Report identifying the unit for measuring the throughput rate in frames per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportTputRateUnit"])

    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportTputRateUnit"], value)

    @property
    def RouterAlert(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The router alert selected from the Hop-by-hop Options.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterAlert"])

    @RouterAlert.setter
    def RouterAlert(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterAlert"], value)

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
    def StepLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the step rate of the load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepLoadUnit"])

    @StepLoadUnit.setter
    def StepLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepLoadUnit"], value)

    @property
    def StepStepLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The incremental step value of load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepStepLoadRate"])

    @StepStepLoadRate.setter
    def StepStepLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepStepLoadRate"], value)

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

    def update(
        self,
        ApplyMode=None,
        AssignGroupType=None,
        BidirectionalOptionEnabled=None,
        BurstSize=None,
        CalculateJitter=None,
        CalculateLatency=None,
        CountRandomFrameSize=None,
        DelayAfterTransmit=None,
        Duration=None,
        EnableDataIntegrity=None,
        EnableLayer1Rate=None,
        EnableLeaveGroup=None,
        EnableMinFrameSize=None,
        EnableMulticastQuerier=None,
        EnableOldStatsForReef=None,
        FirstMulticastDestMACAddress=None,
        FloodedFramesEnabled=None,
        ForceRegenerate=None,
        FrameSizeMode=None,
        FramesizeList=None,
        Gap=None,
        GroupCapacityGreaterThan=None,
        GroupDistributionType=None,
        IgmpV1Timeout=None,
        IgmpVersion=None,
        Igmpv3MessageType=None,
        Igmpv3SourceAddrList=None,
        IncMulticastDestMACAddress=None,
        IncPortMACAddress=None,
        IncrAddresses=None,
        InitialRate=None,
        InitialStepLoadRate=None,
        Ipv4Address=None,
        Ipv6Address=None,
        IsIPv6=None,
        IsMulticastAutomaticFrameData=None,
        JoinLeaveMultiplier=None,
        JoinLeaveRate=None,
        JoinLeaveWaitTime=None,
        LatencyBins=None,
        LatencyBinsEnabled=None,
        LatencyType=None,
        LoadInitialRate=None,
        LoadRateList=None,
        LoadType=None,
        MapType=None,
        MaxIncrementFrameSize=None,
        MaxRandomFrameSize=None,
        MaxStepLoadRate=None,
        MinIncrementFrameSize=None,
        MinRandomFrameSize=None,
        MixedClassMulticast=None,
        MldVersion=None,
        NumAddresses=None,
        NumIterations=None,
        Numtrials=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        PortMACAddress=None,
        ProtocolItem=None,
        ReportSequenceError=None,
        ReportTputRateUnit=None,
        RouterAlert=None,
        StepIncrementFrameSize=None,
        StepLoadUnit=None,
        StepStepLoadRate=None,
        SupportedTrafficTypes=None,
        TestTrafficType=None,
        TxDelay=None,
    ):
        # type: (str, str, bool, int, bool, bool, int, int, int, bool, bool, bool, bool, bool, bool, str, bool, bool, str, List[str], int, int, str, int, int, str, str, str, str, int, str, int, str, str, str, str, int, int, int, str, bool, str, int, str, str, str, int, int, int, int, int, str, int, int, int, int, bool, str, int, str, List[str], bool, str, bool, int, str, int, str, str, int) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): It assigns the group type.
        - BidirectionalOptionEnabled (bool): If true, the bidirectional option is enabled.
        - BurstSize (number): The number of packets that are sent in a burst.
        - CalculateJitter (bool): If true, the jitter is calculated.
        - CalculateLatency (bool): If true, the latency is calculated.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - DelayAfterTransmit (number): The amount of delay after every transmit.
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableLeaveGroup (bool): If true, enables leave group.
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableOldStatsForReef (bool): It enables the old statistics for reef.
        - FirstMulticastDestMACAddress (str): The first multicast destination MAC address.
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameSizeMode (str(custom | fixed | increment | random)): This attribute is the frame size mode for the Quad Gaussian. The Quad Gaussian is the superposition of four Gaussian distributions.
        - FramesizeList (list(str)): The list of the available frame size.
        - Gap (number): The gap in transmission of frames.
        - GroupCapacityGreaterThan (number): The integer that distinguishes the group capacity that could be greater than the specified integer.
        - GroupDistributionType (str(acrossHosts | acrossPorts)): It signifies group distribution type.
        - IgmpV1Timeout (number): It signifies the timeout of version 1 of IGMP.
        - IgmpVersion (number): It signifies the version of IGMP.
        - Igmpv3MessageType (str(exclude | include)): It gives details about the igmpv3 message type in the test configuration
        - Igmpv3SourceAddrList (str): It gives details about the igmpv3 source address list in the test configuration
        - IncMulticastDestMACAddress (str): The incrementing multicast destination MAC address.
        - IncPortMACAddress (str): The incrementing MAC address of the port.
        - IncrAddresses (number): If true, the MAC address is incremented.
        - InitialRate (str): The first rate of transmission.
        - InitialStepLoadRate (number): The initial step value of the load rate.
        - Ipv4Address (str): It signifies the IP address for version 4.
        - Ipv6Address (str): It signifies the IP address for version 6.
        - IsIPv6 (str): If true, configures IPv6 address.
        - IsMulticastAutomaticFrameData (str): If true, configures multicast automatic frame data.
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): It signifies the join and leave rate.
        - JoinLeaveWaitTime (number): The wait time for the leave.
        - LatencyBins (str): Sets the latency bins statistics
        - LatencyBinsEnabled (bool): Enables the latency bins statistics
        - LatencyType (str(cutThrough | storeForward)): The type of latency required by the DUT to forward frames.
        - LoadInitialRate (number): The initial rate of the load.
        - LoadRateList (str): The list of Load Rate.
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)): The type of the payload setting.
        - MapType (str): The POS traffic map type.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxStepLoadRate (number): The maximum step load rate.
        - MinIncrementFrameSize (number): The minimum incremental value of the frame size.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - MixedClassMulticast (str): The mixed multicast class.
        - MldVersion (number): It signifies the MLD version.
        - NumAddresses (number): The integer value for the number of addresses.
        - NumIterations (number): The number of iterations.
        - Numtrials (number): The integer value that states the number of trials permitted.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - PortMACAddress (str): The MAC address of the port.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - ReportSequenceError (bool): Reports sequence errors in the test result
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): Report identifying the unit for measuring the throughput rate in frames per second.
        - RouterAlert (bool): The router alert selected from the Hop-by-hop Options.
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the step rate of the load unit.
        - StepStepLoadRate (number): The incremental step value of load rate.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TestTrafficType (str): It signifies the test traffic type value.
        - TxDelay (number): Specifies the amount of delay after every transmit.

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
        CountRandomFrameSize=None,
        DelayAfterTransmit=None,
        Duration=None,
        EnableDataIntegrity=None,
        EnableLayer1Rate=None,
        EnableLeaveGroup=None,
        EnableMinFrameSize=None,
        EnableMulticastQuerier=None,
        EnableOldStatsForReef=None,
        FirstMulticastDestMACAddress=None,
        FloodedFramesEnabled=None,
        ForceRegenerate=None,
        FrameSizeMode=None,
        FramesizeList=None,
        Gap=None,
        GroupCapacityGreaterThan=None,
        GroupDistributionType=None,
        IgmpV1Timeout=None,
        IgmpVersion=None,
        Igmpv3MessageType=None,
        Igmpv3SourceAddrList=None,
        IncMulticastDestMACAddress=None,
        IncPortMACAddress=None,
        IncrAddresses=None,
        InitialRate=None,
        InitialStepLoadRate=None,
        Ipv4Address=None,
        Ipv6Address=None,
        IsIPv6=None,
        IsMulticastAutomaticFrameData=None,
        JoinLeaveMultiplier=None,
        JoinLeaveRate=None,
        JoinLeaveWaitTime=None,
        LatencyBins=None,
        LatencyBinsEnabled=None,
        LatencyType=None,
        LoadInitialRate=None,
        LoadRateList=None,
        LoadType=None,
        MapType=None,
        MaxIncrementFrameSize=None,
        MaxRandomFrameSize=None,
        MaxStepLoadRate=None,
        MinIncrementFrameSize=None,
        MinRandomFrameSize=None,
        MixedClassMulticast=None,
        MldVersion=None,
        NumAddresses=None,
        NumIterations=None,
        Numtrials=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        PortMACAddress=None,
        ProtocolItem=None,
        ReportSequenceError=None,
        ReportTputRateUnit=None,
        RouterAlert=None,
        StepIncrementFrameSize=None,
        StepLoadUnit=None,
        StepStepLoadRate=None,
        SupportedTrafficTypes=None,
        TestTrafficType=None,
        TxDelay=None,
    ):
        # type: (str, str, bool, int, bool, bool, int, int, int, bool, bool, bool, bool, bool, bool, str, bool, bool, str, List[str], int, int, str, int, int, str, str, str, str, int, str, int, str, str, str, str, int, int, int, str, bool, str, int, str, str, str, int, int, int, int, int, str, int, int, int, int, bool, str, int, str, List[str], bool, str, bool, int, str, int, str, str, int) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): It assigns the group type.
        - BidirectionalOptionEnabled (bool): If true, the bidirectional option is enabled.
        - BurstSize (number): The number of packets that are sent in a burst.
        - CalculateJitter (bool): If true, the jitter is calculated.
        - CalculateLatency (bool): If true, the latency is calculated.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - DelayAfterTransmit (number): The amount of delay after every transmit.
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableLeaveGroup (bool): If true, enables leave group.
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableOldStatsForReef (bool): It enables the old statistics for reef.
        - FirstMulticastDestMACAddress (str): The first multicast destination MAC address.
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameSizeMode (str(custom | fixed | increment | random)): This attribute is the frame size mode for the Quad Gaussian. The Quad Gaussian is the superposition of four Gaussian distributions.
        - FramesizeList (list(str)): The list of the available frame size.
        - Gap (number): The gap in transmission of frames.
        - GroupCapacityGreaterThan (number): The integer that distinguishes the group capacity that could be greater than the specified integer.
        - GroupDistributionType (str(acrossHosts | acrossPorts)): It signifies group distribution type.
        - IgmpV1Timeout (number): It signifies the timeout of version 1 of IGMP.
        - IgmpVersion (number): It signifies the version of IGMP.
        - Igmpv3MessageType (str(exclude | include)): It gives details about the igmpv3 message type in the test configuration
        - Igmpv3SourceAddrList (str): It gives details about the igmpv3 source address list in the test configuration
        - IncMulticastDestMACAddress (str): The incrementing multicast destination MAC address.
        - IncPortMACAddress (str): The incrementing MAC address of the port.
        - IncrAddresses (number): If true, the MAC address is incremented.
        - InitialRate (str): The first rate of transmission.
        - InitialStepLoadRate (number): The initial step value of the load rate.
        - Ipv4Address (str): It signifies the IP address for version 4.
        - Ipv6Address (str): It signifies the IP address for version 6.
        - IsIPv6 (str): If true, configures IPv6 address.
        - IsMulticastAutomaticFrameData (str): If true, configures multicast automatic frame data.
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): It signifies the join and leave rate.
        - JoinLeaveWaitTime (number): The wait time for the leave.
        - LatencyBins (str): Sets the latency bins statistics
        - LatencyBinsEnabled (bool): Enables the latency bins statistics
        - LatencyType (str(cutThrough | storeForward)): The type of latency required by the DUT to forward frames.
        - LoadInitialRate (number): The initial rate of the load.
        - LoadRateList (str): The list of Load Rate.
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)): The type of the payload setting.
        - MapType (str): The POS traffic map type.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxStepLoadRate (number): The maximum step load rate.
        - MinIncrementFrameSize (number): The minimum incremental value of the frame size.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - MixedClassMulticast (str): The mixed multicast class.
        - MldVersion (number): It signifies the MLD version.
        - NumAddresses (number): The integer value for the number of addresses.
        - NumIterations (number): The number of iterations.
        - Numtrials (number): The integer value that states the number of trials permitted.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - PortMACAddress (str): The MAC address of the port.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - ReportSequenceError (bool): Reports sequence errors in the test result
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): Report identifying the unit for measuring the throughput rate in frames per second.
        - RouterAlert (bool): The router alert selected from the Hop-by-hop Options.
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the step rate of the load unit.
        - StepStepLoadRate (number): The incremental step value of load rate.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TestTrafficType (str): It signifies the test traffic type value.
        - TxDelay (number): Specifies the amount of delay after every transmit.

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
