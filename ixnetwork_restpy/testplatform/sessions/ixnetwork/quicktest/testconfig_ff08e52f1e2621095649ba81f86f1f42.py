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
    """NOT DEFINED
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "testConfig"
    _SDM_ATT_MAP = {
        "ApplyMode": "applyMode",
        "AssignGroupType": "assignGroupType",
        "AvgPassFailMode": "avgPassFailMode",
        "BidirectionalOptionEnabled": "bidirectionalOptionEnabled",
        "BinaryBackoff": "binaryBackoff",
        "BinaryFrameLossUnit": "binaryFrameLossUnit",
        "BinaryLoadUnit": "binaryLoadUnit",
        "BinaryResolution": "binaryResolution",
        "BinarySearchType": "binarySearchType",
        "BinaryTolerance": "binaryTolerance",
        "BurstSize": "burstSize",
        "CalculateJitter": "calculateJitter",
        "CalculateLatency": "calculateLatency",
        "CountRandomFrameSize": "countRandomFrameSize",
        "CustomLoadUnit": "customLoadUnit",
        "DelayAfterTransmit": "delayAfterTransmit",
        "DelayMode": "delayMode",
        "Duration": "duration",
        "EnableDataIntegrity": "enableDataIntegrity",
        "EnableDropLink": "enableDropLink",
        "EnableGroupJoinRatePassFail": "enableGroupJoinRatePassFail",
        "EnableLeaveGroup": "enableLeaveGroup",
        "EnableMinFrameSize": "enableMinFrameSize",
        "EnableMulticastLearning": "enableMulticastLearning",
        "EnableMulticastQuerier": "enableMulticastQuerier",
        "EnableOldStatsForReef": "enableOldStatsForReef",
        "FirstMulticastDestMACAddress": "firstMulticastDestMACAddress",
        "FloodedFramesEnabled": "floodedFramesEnabled",
        "FloodedFramesProcessing": "floodedFramesProcessing",
        "FloodedFramesTemp": "floodedFramesTemp",
        "ForceRegenerate": "forceRegenerate",
        "FrameSizeMode": "frameSizeMode",
        "FramesizeList": "framesizeList",
        "Gap": "gap",
        "GroupCapacityGreaterThan": "groupCapacityGreaterThan",
        "GroupDistributionType": "groupDistributionType",
        "GroupJoinRatePassFailValue": "groupJoinRatePassFailValue",
        "GroupJoinRateValidationFpsRate": "groupJoinRateValidationFpsRate",
        "GroupJoinRateValidationRate": "groupJoinRateValidationRate",
        "GroupJoinRateValidationRateUnit": "groupJoinRateValidationRateUnit",
        "GroupsDistribution": "groupsDistribution",
        "GroupsList": "groupsList",
        "GroupsMode": "groupsMode",
        "IgmpV1Timeout": "igmpV1Timeout",
        "IgmpVersion": "igmpVersion",
        "Igmpv3MessageType": "igmpv3MessageType",
        "Igmpv3SourceAddrList": "igmpv3SourceAddrList",
        "IncMulticastDestMACAddress": "incMulticastDestMACAddress",
        "IncPortMACAddress": "incPortMACAddress",
        "InitialBinaryLoadIntegerValues": "initialBinaryLoadIntegerValues",
        "InitialRate": "initialRate",
        "InitialStepJoinRate": "initialStepJoinRate",
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
        "LoadUnit": "loadUnit",
        "MapType": "mapType",
        "MaxBinaryLoadIntegerValue": "maxBinaryLoadIntegerValue",
        "MaxIncrementFrameSize": "maxIncrementFrameSize",
        "MaxIncrementGroups": "maxIncrementGroups",
        "MaxRandomFrameSize": "maxRandomFrameSize",
        "MaxStepJoinRate": "maxStepJoinRate",
        "MinBinaryLoadIntegerValues": "minBinaryLoadIntegerValues",
        "MinIncrementFrameSize": "minIncrementFrameSize",
        "MinIncrementGroups": "minIncrementGroups",
        "MinPassFailMode": "minPassFailMode",
        "MinRandomFrameSize": "minRandomFrameSize",
        "MixedClassMulticast": "mixedClassMulticast",
        "MldVersion": "mldVersion",
        "Numtrials": "numtrials",
        "PortDelayEnabled": "portDelayEnabled",
        "PortDelayUnit": "portDelayUnit",
        "PortDelayValue": "portDelayValue",
        "PortDownTime": "portDownTime",
        "PortMACAddress": "portMACAddress",
        "ProtocolItem": "protocolItem",
        "ReportSequenceError": "reportSequenceError",
        "RouterAlert": "routerAlert",
        "ShowDetailedBinaryResults": "showDetailedBinaryResults",
        "StepFrameLossUnit": "stepFrameLossUnit",
        "StepIncrementFrameSize": "stepIncrementFrameSize",
        "StepIncrementGroups": "stepIncrementGroups",
        "StepLoadUnit": "stepLoadUnit",
        "StepStepJoinRate": "stepStepJoinRate",
        "StepTolerance": "stepTolerance",
        "SupportedTrafficTypes": "supportedTrafficTypes",
        "TestTrafficType": "testTrafficType",
        "TxDelay": "txDelay",
    }
    _SDM_ENUM_MAP = {
        "assignGroupType": ["accumulated", "distributed"],
        "binaryFrameLossUnit": ["%"],
        "binaryLoadUnit": ["fpsRate", "percentMaxRate"],
        "binarySearchType": ["linear"],
        "customLoadUnit": ["fpsRate", "percentMaxRate"],
        "delayMode": ["average", "min"],
        "frameSizeMode": ["custom", "fixed", "increment", "random"],
        "groupDistributionType": ["acrossHosts", "acrossPorts"],
        "groupJoinRateValidationRateUnit": ["fpsRate", "percentMaxRate"],
        "groupsDistribution": [
            "accumulated",
            "distributedPerHost",
            "distributedPerPort",
        ],
        "groupsMode": ["custom", "increment", "unchanged"],
        "igmpv3MessageType": ["exclude", "include"],
        "latencyType": ["cutThrough", "storeForward"],
        "loadType": ["binary", "custom", "step", "unchanged"],
        "loadUnit": ["fpsRate", "percentMaxRate"],
        "portDelayUnit": ["bytes", "nanoseconds"],
        "stepFrameLossUnit": ["%"],
        "stepLoadUnit": ["fpsRate", "percentMaxRate"],
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
        - str(accumulated | distributed): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssignGroupType"])

    @AssignGroupType.setter
    def AssignGroupType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AssignGroupType"], value)

    @property
    def AvgPassFailMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvgPassFailMode"])

    @AvgPassFailMode.setter
    def AvgPassFailMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AvgPassFailMode"], value)

    @property
    def BidirectionalOptionEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BidirectionalOptionEnabled"])

    @BidirectionalOptionEnabled.setter
    def BidirectionalOptionEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BidirectionalOptionEnabled"], value)

    @property
    def BinaryBackoff(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryBackoff"])

    @BinaryBackoff.setter
    def BinaryBackoff(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryBackoff"], value)

    @property
    def BinaryFrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(%): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryFrameLossUnit"])

    @BinaryFrameLossUnit.setter
    def BinaryFrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryFrameLossUnit"], value)

    @property
    def BinaryLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryLoadUnit"])

    @BinaryLoadUnit.setter
    def BinaryLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryLoadUnit"], value)

    @property
    def BinaryResolution(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryResolution"])

    @BinaryResolution.setter
    def BinaryResolution(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryResolution"], value)

    @property
    def BinarySearchType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(linear): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinarySearchType"])

    @BinarySearchType.setter
    def BinarySearchType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinarySearchType"], value)

    @property
    def BinaryTolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryTolerance"])

    @BinaryTolerance.setter
    def BinaryTolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryTolerance"], value)

    @property
    def BurstSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CountRandomFrameSize"])

    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CountRandomFrameSize"], value)

    @property
    def CustomLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomLoadUnit"])

    @CustomLoadUnit.setter
    def CustomLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomLoadUnit"], value)

    @property
    def DelayAfterTransmit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"])

    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"], value)

    @property
    def DelayMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | min): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayMode"])

    @DelayMode.setter
    def DelayMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayMode"], value)

    @property
    def Duration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDataIntegrity"])

    @EnableDataIntegrity.setter
    def EnableDataIntegrity(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDataIntegrity"], value)

    @property
    def EnableDropLink(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDropLink"])

    @EnableDropLink.setter
    def EnableDropLink(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDropLink"], value)

    @property
    def EnableGroupJoinRatePassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableGroupJoinRatePassFail"])

    @EnableGroupJoinRatePassFail.setter
    def EnableGroupJoinRatePassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableGroupJoinRatePassFail"], value)

    @property
    def EnableLeaveGroup(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMinFrameSize"])

    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMinFrameSize"], value)

    @property
    def EnableMulticastLearning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMulticastLearning"])

    @EnableMulticastLearning.setter
    def EnableMulticastLearning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMulticastLearning"], value)

    @property
    def EnableMulticastQuerier(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - str: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["FloodedFramesEnabled"])

    @FloodedFramesEnabled.setter
    def FloodedFramesEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FloodedFramesEnabled"], value)

    @property
    def FloodedFramesProcessing(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["FloodedFramesProcessing"])

    @FloodedFramesProcessing.setter
    def FloodedFramesProcessing(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FloodedFramesProcessing"], value)

    @property
    def FloodedFramesTemp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["FloodedFramesTemp"])

    @FloodedFramesTemp.setter
    def FloodedFramesTemp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FloodedFramesTemp"], value)

    @property
    def ForceRegenerate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
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
        - str(custom | fixed | increment | random): NOT DEFINED
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
        - list(str): NOT DEFINED
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
        - number: NOT DEFINED
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
        - number: NOT DEFINED
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
        - str(acrossHosts | acrossPorts): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupDistributionType"])

    @GroupDistributionType.setter
    def GroupDistributionType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupDistributionType"], value)

    @property
    def GroupJoinRatePassFailValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupJoinRatePassFailValue"])

    @GroupJoinRatePassFailValue.setter
    def GroupJoinRatePassFailValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupJoinRatePassFailValue"], value)

    @property
    def GroupJoinRateValidationFpsRate(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupJoinRateValidationFpsRate"])

    @GroupJoinRateValidationFpsRate.setter
    def GroupJoinRateValidationFpsRate(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupJoinRateValidationFpsRate"], value)

    @property
    def GroupJoinRateValidationRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupJoinRateValidationRate"])

    @GroupJoinRateValidationRate.setter
    def GroupJoinRateValidationRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupJoinRateValidationRate"], value)

    @property
    def GroupJoinRateValidationRateUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupJoinRateValidationRateUnit"])

    @GroupJoinRateValidationRateUnit.setter
    def GroupJoinRateValidationRateUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupJoinRateValidationRateUnit"], value)

    @property
    def GroupsDistribution(self):
        # type: () -> str
        """
        Returns
        -------
        - str(accumulated | distributedPerHost | distributedPerPort): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupsDistribution"])

    @GroupsDistribution.setter
    def GroupsDistribution(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupsDistribution"], value)

    @property
    def GroupsList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupsList"])

    @GroupsList.setter
    def GroupsList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupsList"], value)

    @property
    def GroupsMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | increment | unchanged): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupsMode"])

    @GroupsMode.setter
    def GroupsMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupsMode"], value)

    @property
    def IgmpV1Timeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
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
        - number: NOT DEFINED
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
        - str(exclude | include): NOT DEFINED
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
        - str: NOT DEFINED
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
        - str: NOT DEFINED
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
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncPortMACAddress"])

    @IncPortMACAddress.setter
    def IncPortMACAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncPortMACAddress"], value)

    @property
    def InitialBinaryLoadIntegerValues(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialBinaryLoadIntegerValues"])

    @InitialBinaryLoadIntegerValues.setter
    def InitialBinaryLoadIntegerValues(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialBinaryLoadIntegerValues"], value)

    @property
    def InitialRate(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialRate"])

    @InitialRate.setter
    def InitialRate(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialRate"], value)

    @property
    def InitialStepJoinRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialStepJoinRate"])

    @InitialStepJoinRate.setter
    def InitialStepJoinRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialStepJoinRate"], value)

    @property
    def Ipv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
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
        - str: NOT DEFINED
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
        - str: NOT DEFINED
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
        - str: NOT DEFINED
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
        - number: NOT DEFINED
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
        - number: NOT DEFINED
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
        - str: NOT DEFINED
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
        - bool: NOT DEFINED
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
        - str(cutThrough | storeForward): NOT DEFINED
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
        - number: NOT DEFINED
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
        - str: NOT DEFINED
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
        - str(binary | custom | step | unchanged): NOT DEFINED
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
        - str(fpsRate | percentMaxRate): NOT DEFINED
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
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapType"])

    @MapType.setter
    def MapType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapType"], value)

    @property
    def MaxBinaryLoadIntegerValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxBinaryLoadIntegerValue"])

    @MaxBinaryLoadIntegerValue.setter
    def MaxBinaryLoadIntegerValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxBinaryLoadIntegerValue"], value)

    @property
    def MaxIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxIncrementFrameSize"])

    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxIncrementFrameSize"], value)

    @property
    def MaxIncrementGroups(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxIncrementGroups"])

    @MaxIncrementGroups.setter
    def MaxIncrementGroups(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxIncrementGroups"], value)

    @property
    def MaxRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxRandomFrameSize"])

    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxRandomFrameSize"], value)

    @property
    def MaxStepJoinRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxStepJoinRate"])

    @MaxStepJoinRate.setter
    def MaxStepJoinRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxStepJoinRate"], value)

    @property
    def MinBinaryLoadIntegerValues(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinBinaryLoadIntegerValues"])

    @MinBinaryLoadIntegerValues.setter
    def MinBinaryLoadIntegerValues(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinBinaryLoadIntegerValues"], value)

    @property
    def MinIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinIncrementFrameSize"])

    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinIncrementFrameSize"], value)

    @property
    def MinIncrementGroups(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinIncrementGroups"])

    @MinIncrementGroups.setter
    def MinIncrementGroups(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinIncrementGroups"], value)

    @property
    def MinPassFailMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinPassFailMode"])

    @MinPassFailMode.setter
    def MinPassFailMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinPassFailMode"], value)

    @property
    def MinRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
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
        - str: NOT DEFINED
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
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["MldVersion"])

    @MldVersion.setter
    def MldVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MldVersion"], value)

    @property
    def Numtrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
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
        - str(bytes | nanoseconds): NOT DEFINED
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
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDelayValue"])

    @PortDelayValue.setter
    def PortDelayValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDelayValue"], value)

    @property
    def PortDownTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDownTime"])

    @PortDownTime.setter
    def PortDownTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDownTime"], value)

    @property
    def PortMACAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportSequenceError"])

    @ReportSequenceError.setter
    def ReportSequenceError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportSequenceError"], value)

    @property
    def RouterAlert(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterAlert"])

    @RouterAlert.setter
    def RouterAlert(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterAlert"], value)

    @property
    def ShowDetailedBinaryResults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowDetailedBinaryResults"])

    @ShowDetailedBinaryResults.setter
    def ShowDetailedBinaryResults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowDetailedBinaryResults"], value)

    @property
    def StepFrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(%): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepFrameLossUnit"])

    @StepFrameLossUnit.setter
    def StepFrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepFrameLossUnit"], value)

    @property
    def StepIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepIncrementFrameSize"])

    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepIncrementFrameSize"], value)

    @property
    def StepIncrementGroups(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepIncrementGroups"])

    @StepIncrementGroups.setter
    def StepIncrementGroups(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepIncrementGroups"], value)

    @property
    def StepLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fpsRate | percentMaxRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepLoadUnit"])

    @StepLoadUnit.setter
    def StepLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepLoadUnit"], value)

    @property
    def StepStepJoinRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepStepJoinRate"])

    @StepStepJoinRate.setter
    def StepStepJoinRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepStepJoinRate"], value)

    @property
    def StepTolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepTolerance"])

    @StepTolerance.setter
    def StepTolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepTolerance"], value)

    @property
    def SupportedTrafficTypes(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
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
        - str: NOT DEFINED
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
        - number: NOT DEFINED
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
        AvgPassFailMode=None,
        BidirectionalOptionEnabled=None,
        BinaryBackoff=None,
        BinaryFrameLossUnit=None,
        BinaryLoadUnit=None,
        BinaryResolution=None,
        BinarySearchType=None,
        BinaryTolerance=None,
        BurstSize=None,
        CalculateJitter=None,
        CalculateLatency=None,
        CountRandomFrameSize=None,
        CustomLoadUnit=None,
        DelayAfterTransmit=None,
        DelayMode=None,
        Duration=None,
        EnableDataIntegrity=None,
        EnableDropLink=None,
        EnableGroupJoinRatePassFail=None,
        EnableLeaveGroup=None,
        EnableMinFrameSize=None,
        EnableMulticastLearning=None,
        EnableMulticastQuerier=None,
        EnableOldStatsForReef=None,
        FirstMulticastDestMACAddress=None,
        FloodedFramesEnabled=None,
        FloodedFramesProcessing=None,
        FloodedFramesTemp=None,
        ForceRegenerate=None,
        FrameSizeMode=None,
        FramesizeList=None,
        Gap=None,
        GroupCapacityGreaterThan=None,
        GroupDistributionType=None,
        GroupJoinRatePassFailValue=None,
        GroupJoinRateValidationFpsRate=None,
        GroupJoinRateValidationRate=None,
        GroupJoinRateValidationRateUnit=None,
        GroupsDistribution=None,
        GroupsList=None,
        GroupsMode=None,
        IgmpV1Timeout=None,
        IgmpVersion=None,
        Igmpv3MessageType=None,
        Igmpv3SourceAddrList=None,
        IncMulticastDestMACAddress=None,
        IncPortMACAddress=None,
        InitialBinaryLoadIntegerValues=None,
        InitialRate=None,
        InitialStepJoinRate=None,
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
        LoadUnit=None,
        MapType=None,
        MaxBinaryLoadIntegerValue=None,
        MaxIncrementFrameSize=None,
        MaxIncrementGroups=None,
        MaxRandomFrameSize=None,
        MaxStepJoinRate=None,
        MinBinaryLoadIntegerValues=None,
        MinIncrementFrameSize=None,
        MinIncrementGroups=None,
        MinPassFailMode=None,
        MinRandomFrameSize=None,
        MixedClassMulticast=None,
        MldVersion=None,
        Numtrials=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        PortDownTime=None,
        PortMACAddress=None,
        ProtocolItem=None,
        ReportSequenceError=None,
        RouterAlert=None,
        ShowDetailedBinaryResults=None,
        StepFrameLossUnit=None,
        StepIncrementFrameSize=None,
        StepIncrementGroups=None,
        StepLoadUnit=None,
        StepStepJoinRate=None,
        StepTolerance=None,
        SupportedTrafficTypes=None,
        TestTrafficType=None,
        TxDelay=None,
    ):
        # type: (str, str, bool, bool, int, str, str, int, str, int, int, bool, bool, int, str, int, str, int, bool, bool, bool, bool, bool, bool, bool, bool, str, bool, bool, str, bool, str, List[str], int, int, str, int, str, int, str, str, List[str], str, int, int, str, str, str, str, int, str, int, str, str, str, str, int, int, int, str, bool, str, int, str, str, str, str, int, int, int, int, int, int, int, int, bool, int, str, int, int, bool, str, int, int, str, List[str], bool, bool, bool, str, int, int, str, int, int, str, str, int) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): NOT DEFINED
        - AvgPassFailMode (bool): NOT DEFINED
        - BidirectionalOptionEnabled (bool): NOT DEFINED
        - BinaryBackoff (number): NOT DEFINED
        - BinaryFrameLossUnit (str(%)): NOT DEFINED
        - BinaryLoadUnit (str(fpsRate | percentMaxRate)): NOT DEFINED
        - BinaryResolution (number): NOT DEFINED
        - BinarySearchType (str(linear)): NOT DEFINED
        - BinaryTolerance (number): NOT DEFINED
        - BurstSize (number): NOT DEFINED
        - CalculateJitter (bool): NOT DEFINED
        - CalculateLatency (bool): NOT DEFINED
        - CountRandomFrameSize (number): NOT DEFINED
        - CustomLoadUnit (str(fpsRate | percentMaxRate)): NOT DEFINED
        - DelayAfterTransmit (number): NOT DEFINED
        - DelayMode (str(average | min)): NOT DEFINED
        - Duration (number): NOT DEFINED
        - EnableDataIntegrity (bool): NOT DEFINED
        - EnableDropLink (bool): NOT DEFINED
        - EnableGroupJoinRatePassFail (bool): NOT DEFINED
        - EnableLeaveGroup (bool): NOT DEFINED
        - EnableMinFrameSize (bool): NOT DEFINED
        - EnableMulticastLearning (bool): NOT DEFINED
        - EnableMulticastQuerier (bool): NOT DEFINED
        - EnableOldStatsForReef (bool): NOT DEFINED
        - FirstMulticastDestMACAddress (str): NOT DEFINED
        - FloodedFramesEnabled (bool): NOT DEFINED
        - FloodedFramesProcessing (bool): NOT DEFINED
        - FloodedFramesTemp (str): NOT DEFINED
        - ForceRegenerate (bool): NOT DEFINED
        - FrameSizeMode (str(custom | fixed | increment | random)): NOT DEFINED
        - FramesizeList (list(str)): NOT DEFINED
        - Gap (number): NOT DEFINED
        - GroupCapacityGreaterThan (number): NOT DEFINED
        - GroupDistributionType (str(acrossHosts | acrossPorts)): NOT DEFINED
        - GroupJoinRatePassFailValue (number): NOT DEFINED
        - GroupJoinRateValidationFpsRate (str): NOT DEFINED
        - GroupJoinRateValidationRate (number): NOT DEFINED
        - GroupJoinRateValidationRateUnit (str(fpsRate | percentMaxRate)): NOT DEFINED
        - GroupsDistribution (str(accumulated | distributedPerHost | distributedPerPort)): NOT DEFINED
        - GroupsList (list(str)): NOT DEFINED
        - GroupsMode (str(custom | increment | unchanged)): NOT DEFINED
        - IgmpV1Timeout (number): NOT DEFINED
        - IgmpVersion (number): NOT DEFINED
        - Igmpv3MessageType (str(exclude | include)): NOT DEFINED
        - Igmpv3SourceAddrList (str): NOT DEFINED
        - IncMulticastDestMACAddress (str): NOT DEFINED
        - IncPortMACAddress (str): NOT DEFINED
        - InitialBinaryLoadIntegerValues (number): NOT DEFINED
        - InitialRate (str): NOT DEFINED
        - InitialStepJoinRate (number): NOT DEFINED
        - Ipv4Address (str): NOT DEFINED
        - Ipv6Address (str): NOT DEFINED
        - IsIPv6 (str): NOT DEFINED
        - IsMulticastAutomaticFrameData (str): NOT DEFINED
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): NOT DEFINED
        - JoinLeaveWaitTime (number): NOT DEFINED
        - LatencyBins (str): NOT DEFINED
        - LatencyBinsEnabled (bool): NOT DEFINED
        - LatencyType (str(cutThrough | storeForward)): NOT DEFINED
        - LoadInitialRate (number): NOT DEFINED
        - LoadRateList (str): NOT DEFINED
        - LoadType (str(binary | custom | step | unchanged)): NOT DEFINED
        - LoadUnit (str(fpsRate | percentMaxRate)): NOT DEFINED
        - MapType (str): NOT DEFINED
        - MaxBinaryLoadIntegerValue (number): NOT DEFINED
        - MaxIncrementFrameSize (number): NOT DEFINED
        - MaxIncrementGroups (number): NOT DEFINED
        - MaxRandomFrameSize (number): NOT DEFINED
        - MaxStepJoinRate (number): NOT DEFINED
        - MinBinaryLoadIntegerValues (number): NOT DEFINED
        - MinIncrementFrameSize (number): NOT DEFINED
        - MinIncrementGroups (number): NOT DEFINED
        - MinPassFailMode (bool): NOT DEFINED
        - MinRandomFrameSize (number): NOT DEFINED
        - MixedClassMulticast (str): NOT DEFINED
        - MldVersion (number): NOT DEFINED
        - Numtrials (number): NOT DEFINED
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): NOT DEFINED
        - PortDelayValue (number): NOT DEFINED
        - PortDownTime (number): NOT DEFINED
        - PortMACAddress (str): NOT DEFINED
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - ReportSequenceError (bool): NOT DEFINED
        - RouterAlert (bool): NOT DEFINED
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepFrameLossUnit (str(%)): NOT DEFINED
        - StepIncrementFrameSize (number): NOT DEFINED
        - StepIncrementGroups (number): NOT DEFINED
        - StepLoadUnit (str(fpsRate | percentMaxRate)): NOT DEFINED
        - StepStepJoinRate (number): NOT DEFINED
        - StepTolerance (number): NOT DEFINED
        - SupportedTrafficTypes (str): NOT DEFINED
        - TestTrafficType (str): NOT DEFINED
        - TxDelay (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ApplyMode=None,
        AssignGroupType=None,
        AvgPassFailMode=None,
        BidirectionalOptionEnabled=None,
        BinaryBackoff=None,
        BinaryFrameLossUnit=None,
        BinaryLoadUnit=None,
        BinaryResolution=None,
        BinarySearchType=None,
        BinaryTolerance=None,
        BurstSize=None,
        CalculateJitter=None,
        CalculateLatency=None,
        CountRandomFrameSize=None,
        CustomLoadUnit=None,
        DelayAfterTransmit=None,
        DelayMode=None,
        Duration=None,
        EnableDataIntegrity=None,
        EnableDropLink=None,
        EnableGroupJoinRatePassFail=None,
        EnableLeaveGroup=None,
        EnableMinFrameSize=None,
        EnableMulticastLearning=None,
        EnableMulticastQuerier=None,
        EnableOldStatsForReef=None,
        FirstMulticastDestMACAddress=None,
        FloodedFramesEnabled=None,
        FloodedFramesProcessing=None,
        FloodedFramesTemp=None,
        ForceRegenerate=None,
        FrameSizeMode=None,
        FramesizeList=None,
        Gap=None,
        GroupCapacityGreaterThan=None,
        GroupDistributionType=None,
        GroupJoinRatePassFailValue=None,
        GroupJoinRateValidationFpsRate=None,
        GroupJoinRateValidationRate=None,
        GroupJoinRateValidationRateUnit=None,
        GroupsDistribution=None,
        GroupsList=None,
        GroupsMode=None,
        IgmpV1Timeout=None,
        IgmpVersion=None,
        Igmpv3MessageType=None,
        Igmpv3SourceAddrList=None,
        IncMulticastDestMACAddress=None,
        IncPortMACAddress=None,
        InitialBinaryLoadIntegerValues=None,
        InitialRate=None,
        InitialStepJoinRate=None,
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
        LoadUnit=None,
        MapType=None,
        MaxBinaryLoadIntegerValue=None,
        MaxIncrementFrameSize=None,
        MaxIncrementGroups=None,
        MaxRandomFrameSize=None,
        MaxStepJoinRate=None,
        MinBinaryLoadIntegerValues=None,
        MinIncrementFrameSize=None,
        MinIncrementGroups=None,
        MinPassFailMode=None,
        MinRandomFrameSize=None,
        MixedClassMulticast=None,
        MldVersion=None,
        Numtrials=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        PortDownTime=None,
        PortMACAddress=None,
        ProtocolItem=None,
        ReportSequenceError=None,
        RouterAlert=None,
        ShowDetailedBinaryResults=None,
        StepFrameLossUnit=None,
        StepIncrementFrameSize=None,
        StepIncrementGroups=None,
        StepLoadUnit=None,
        StepStepJoinRate=None,
        StepTolerance=None,
        SupportedTrafficTypes=None,
        TestTrafficType=None,
        TxDelay=None,
    ):
        # type: (str, str, bool, bool, int, str, str, int, str, int, int, bool, bool, int, str, int, str, int, bool, bool, bool, bool, bool, bool, bool, bool, str, bool, bool, str, bool, str, List[str], int, int, str, int, str, int, str, str, List[str], str, int, int, str, str, str, str, int, str, int, str, str, str, str, int, int, int, str, bool, str, int, str, str, str, str, int, int, int, int, int, int, int, int, bool, int, str, int, int, bool, str, int, int, str, List[str], bool, bool, bool, str, int, int, str, int, int, str, str, int) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): NOT DEFINED
        - AvgPassFailMode (bool): NOT DEFINED
        - BidirectionalOptionEnabled (bool): NOT DEFINED
        - BinaryBackoff (number): NOT DEFINED
        - BinaryFrameLossUnit (str(%)): NOT DEFINED
        - BinaryLoadUnit (str(fpsRate | percentMaxRate)): NOT DEFINED
        - BinaryResolution (number): NOT DEFINED
        - BinarySearchType (str(linear)): NOT DEFINED
        - BinaryTolerance (number): NOT DEFINED
        - BurstSize (number): NOT DEFINED
        - CalculateJitter (bool): NOT DEFINED
        - CalculateLatency (bool): NOT DEFINED
        - CountRandomFrameSize (number): NOT DEFINED
        - CustomLoadUnit (str(fpsRate | percentMaxRate)): NOT DEFINED
        - DelayAfterTransmit (number): NOT DEFINED
        - DelayMode (str(average | min)): NOT DEFINED
        - Duration (number): NOT DEFINED
        - EnableDataIntegrity (bool): NOT DEFINED
        - EnableDropLink (bool): NOT DEFINED
        - EnableGroupJoinRatePassFail (bool): NOT DEFINED
        - EnableLeaveGroup (bool): NOT DEFINED
        - EnableMinFrameSize (bool): NOT DEFINED
        - EnableMulticastLearning (bool): NOT DEFINED
        - EnableMulticastQuerier (bool): NOT DEFINED
        - EnableOldStatsForReef (bool): NOT DEFINED
        - FirstMulticastDestMACAddress (str): NOT DEFINED
        - FloodedFramesEnabled (bool): NOT DEFINED
        - FloodedFramesProcessing (bool): NOT DEFINED
        - FloodedFramesTemp (str): NOT DEFINED
        - ForceRegenerate (bool): NOT DEFINED
        - FrameSizeMode (str(custom | fixed | increment | random)): NOT DEFINED
        - FramesizeList (list(str)): NOT DEFINED
        - Gap (number): NOT DEFINED
        - GroupCapacityGreaterThan (number): NOT DEFINED
        - GroupDistributionType (str(acrossHosts | acrossPorts)): NOT DEFINED
        - GroupJoinRatePassFailValue (number): NOT DEFINED
        - GroupJoinRateValidationFpsRate (str): NOT DEFINED
        - GroupJoinRateValidationRate (number): NOT DEFINED
        - GroupJoinRateValidationRateUnit (str(fpsRate | percentMaxRate)): NOT DEFINED
        - GroupsDistribution (str(accumulated | distributedPerHost | distributedPerPort)): NOT DEFINED
        - GroupsList (list(str)): NOT DEFINED
        - GroupsMode (str(custom | increment | unchanged)): NOT DEFINED
        - IgmpV1Timeout (number): NOT DEFINED
        - IgmpVersion (number): NOT DEFINED
        - Igmpv3MessageType (str(exclude | include)): NOT DEFINED
        - Igmpv3SourceAddrList (str): NOT DEFINED
        - IncMulticastDestMACAddress (str): NOT DEFINED
        - IncPortMACAddress (str): NOT DEFINED
        - InitialBinaryLoadIntegerValues (number): NOT DEFINED
        - InitialRate (str): NOT DEFINED
        - InitialStepJoinRate (number): NOT DEFINED
        - Ipv4Address (str): NOT DEFINED
        - Ipv6Address (str): NOT DEFINED
        - IsIPv6 (str): NOT DEFINED
        - IsMulticastAutomaticFrameData (str): NOT DEFINED
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): NOT DEFINED
        - JoinLeaveWaitTime (number): NOT DEFINED
        - LatencyBins (str): NOT DEFINED
        - LatencyBinsEnabled (bool): NOT DEFINED
        - LatencyType (str(cutThrough | storeForward)): NOT DEFINED
        - LoadInitialRate (number): NOT DEFINED
        - LoadRateList (str): NOT DEFINED
        - LoadType (str(binary | custom | step | unchanged)): NOT DEFINED
        - LoadUnit (str(fpsRate | percentMaxRate)): NOT DEFINED
        - MapType (str): NOT DEFINED
        - MaxBinaryLoadIntegerValue (number): NOT DEFINED
        - MaxIncrementFrameSize (number): NOT DEFINED
        - MaxIncrementGroups (number): NOT DEFINED
        - MaxRandomFrameSize (number): NOT DEFINED
        - MaxStepJoinRate (number): NOT DEFINED
        - MinBinaryLoadIntegerValues (number): NOT DEFINED
        - MinIncrementFrameSize (number): NOT DEFINED
        - MinIncrementGroups (number): NOT DEFINED
        - MinPassFailMode (bool): NOT DEFINED
        - MinRandomFrameSize (number): NOT DEFINED
        - MixedClassMulticast (str): NOT DEFINED
        - MldVersion (number): NOT DEFINED
        - Numtrials (number): NOT DEFINED
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): NOT DEFINED
        - PortDelayValue (number): NOT DEFINED
        - PortDownTime (number): NOT DEFINED
        - PortMACAddress (str): NOT DEFINED
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - ReportSequenceError (bool): NOT DEFINED
        - RouterAlert (bool): NOT DEFINED
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepFrameLossUnit (str(%)): NOT DEFINED
        - StepIncrementFrameSize (number): NOT DEFINED
        - StepIncrementGroups (number): NOT DEFINED
        - StepLoadUnit (str(fpsRate | percentMaxRate)): NOT DEFINED
        - StepStepJoinRate (number): NOT DEFINED
        - StepTolerance (number): NOT DEFINED
        - SupportedTrafficTypes (str): NOT DEFINED
        - TestTrafficType (str): NOT DEFINED
        - TxDelay (number): NOT DEFINED

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
