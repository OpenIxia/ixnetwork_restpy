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
    """The test configuration.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "testConfig"
    _SDM_ATT_MAP = {
        "ApplyMode": "applyMode",
        "AssignGroupType": "assignGroupType",
        "BackoffIteration": "backoffIteration",
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
        "DelayAfterTransmit": "delayAfterTransmit",
        "Duration": "duration",
        "EnableBackoffIteration": "enableBackoffIteration",
        "EnableDataIntegrity": "enableDataIntegrity",
        "EnableExtraIterations": "enableExtraIterations",
        "EnableFastConvergence": "enableFastConvergence",
        "EnableLayer1Rate": "enableLayer1Rate",
        "EnableLeaveGroup": "enableLeaveGroup",
        "EnableMinFrameSize": "enableMinFrameSize",
        "EnableMulticastQuerier": "enableMulticastQuerier",
        "EnableOldStatsForReef": "enableOldStatsForReef",
        "EnableSaturationIteration": "enableSaturationIteration",
        "EnableStopTestOnHighLoss": "enableStopTestOnHighLoss",
        "ExtraIterationOffsets": "extraIterationOffsets",
        "FastConvergenceDuration": "fastConvergenceDuration",
        "FastConvergenceThreshold": "fastConvergenceThreshold",
        "FloodedFramesEnabled": "floodedFramesEnabled",
        "ForceRegenerate": "forceRegenerate",
        "FrameLossUnit": "frameLossUnit",
        "FrameSizeMode": "frameSizeMode",
        "FramelossPercentValue": "framelossPercentValue",
        "FramesPerBurstGap": "framesPerBurstGap",
        "FramesizeList": "framesizeList",
        "Gap": "gap",
        "GroupDistributionType": "groupDistributionType",
        "IgmpV1Timeout": "igmpV1Timeout",
        "IgmpVersion": "igmpVersion",
        "Igmpv3MessageType": "igmpv3MessageType",
        "Igmpv3SourceAddrList": "igmpv3SourceAddrList",
        "IncrAddresses": "incrAddresses",
        "InitialBinaryLoadRate": "initialBinaryLoadRate",
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
        "LoadType": "loadType",
        "MapType": "mapType",
        "MaxBinaryLoadRate": "maxBinaryLoadRate",
        "MaxIncrementFrameSize": "maxIncrementFrameSize",
        "MaxQuickSearchLoadRate": "maxQuickSearchLoadRate",
        "MaxRandomFrameSize": "maxRandomFrameSize",
        "MaxStepLoadRate": "maxStepLoadRate",
        "MinBinaryLoadRate": "minBinaryLoadRate",
        "MinIncrementFrameSize": "minIncrementFrameSize",
        "MinQuickSearchLoadRate": "minQuickSearchLoadRate",
        "MinRandomFrameSize": "minRandomFrameSize",
        "MldVersion": "mldVersion",
        "NumAddresses": "numAddresses",
        "NumIterations": "numIterations",
        "Numtrials": "numtrials",
        "PortDelayEnabled": "portDelayEnabled",
        "PortDelayUnit": "portDelayUnit",
        "PortDelayValue": "portDelayValue",
        "ProtocolItem": "protocolItem",
        "QuickSearchFrameLossUnit": "quickSearchFrameLossUnit",
        "QuickSearchLoadUnit": "quickSearchLoadUnit",
        "QuickSearchResolution": "quickSearchResolution",
        "QuickSearchSearchType": "quickSearchSearchType",
        "QuickSearchTolerance": "quickSearchTolerance",
        "ReportSequenceError": "reportSequenceError",
        "ReportTputRateUnit": "reportTputRateUnit",
        "RouterAlert": "routerAlert",
        "SaturationIteration": "saturationIteration",
        "ShowDetailedBinaryResults": "showDetailedBinaryResults",
        "StepFrameLossUnit": "stepFrameLossUnit",
        "StepIncrementFrameSize": "stepIncrementFrameSize",
        "StepLoadUnit": "stepLoadUnit",
        "StepStepLoadRate": "stepStepLoadRate",
        "StepTolerance": "stepTolerance",
        "StopTestOnHighLoss": "stopTestOnHighLoss",
        "SupportedTrafficTypes": "supportedTrafficTypes",
        "TestMapType": "testMapType",
        "TestTrafficType": "testTrafficType",
        "TxDelay": "txDelay",
        "UnchangedInitial": "unchangedInitial",
        "UsePercentOffsets": "usePercentOffsets",
    }
    _SDM_ENUM_MAP = {
        "assignGroupType": ["accumulated", "distributed"],
        "binaryFrameLossUnit": ["%", "frames"],
        "binaryLoadUnit": [
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
        "binarySearchType": ["linear"],
        "frameSizeMode": ["custom", "fixed", "increment", "random"],
        "groupDistributionType": ["acrossHosts", "acrossPorts"],
        "igmpv3MessageType": ["exclude", "include"],
        "latencyType": ["cutThrough", "storeForward"],
        "loadType": ["binary", "quickSearch", "step"],
        "portDelayUnit": ["bytes", "nanoseconds"],
        "quickSearchFrameLossUnit": ["%"],
        "quickSearchLoadUnit": [
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
        "quickSearchSearchType": ["linear"],
        "reportTputRateUnit": ["gbps", "gBps", "kbps", "kBps", "mbps", "mBps"],
        "stepFrameLossUnit": ["%", "frames"],
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
        "testMapType": ["fullymesh", "one2many"],
        "unchangedInitial": ["False", "True"],
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
        - str(accumulated | distributed): The assigned group type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssignGroupType"])

    @AssignGroupType.setter
    def AssignGroupType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AssignGroupType"], value)

    @property
    def BackoffIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: IF true, the iteration is backed off.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BackoffIteration"])

    @BackoffIteration.setter
    def BackoffIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BackoffIteration"], value)

    @property
    def BidirectionalOptionEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: if true, the bidirectional option is enabled.
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
        - number: The binary backoff.
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
        - str(% | frames): The binary frame loss unit.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The binary load unit.
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
        - number: The binary resolution.
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
        - str(linear): The binary search type.
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
        - number: The binary tolerance.
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
        - number: The burst size.
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
        - bool: The calculated jitter.
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
        - bool: The latency is calculated.
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
        - number: if true, the random frame size is counted.
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
        - number: The delay after transmit of test config.
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
        - number: The test configuration duration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Duration"])

    @Duration.setter
    def Duration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Duration"], value)

    @property
    def EnableBackoffIteration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the back off iteration is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableBackoffIteration"])

    @EnableBackoffIteration.setter
    def EnableBackoffIteration(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableBackoffIteration"], value)

    @property
    def EnableDataIntegrity(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, data integrity is enabled.
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
        - bool: If true, extra iterations are enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableExtraIterations"])

    @EnableExtraIterations.setter
    def EnableExtraIterations(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableExtraIterations"], value)

    @property
    def EnableFastConvergence(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, fast convergence is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableFastConvergence"])

    @EnableFastConvergence.setter
    def EnableFastConvergence(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableFastConvergence"], value)

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
        - bool: If true, the leave group is enabled.
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
        - bool: If true,the minimum frame size is enabled.
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
        - bool: If true, the old stats for reef is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOldStatsForReef"])

    @EnableOldStatsForReef.setter
    def EnableOldStatsForReef(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOldStatsForReef"], value)

    @property
    def EnableSaturationIteration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the saturation iteration us enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSaturationIteration"])

    @EnableSaturationIteration.setter
    def EnableSaturationIteration(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSaturationIteration"], value)

    @property
    def EnableStopTestOnHighLoss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the test is stopped on high loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableStopTestOnHighLoss"])

    @EnableStopTestOnHighLoss.setter
    def EnableStopTestOnHighLoss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableStopTestOnHighLoss"], value)

    @property
    def ExtraIterationOffsets(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The extra iteration offsets.
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
        - number: The fast convergence duration.
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
        - number: The fast convergence threshold.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastConvergenceThreshold"])

    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastConvergenceThreshold"], value)

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
        - bool: If true, the test configuration is forcefully regenerated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForceRegenerate"])

    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForceRegenerate"], value)

    @property
    def FrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The frame loss unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameLossUnit"])

    @FrameLossUnit.setter
    def FrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameLossUnit"], value)

    @property
    def FrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | fixed | increment | random): The frame size mode of test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameSizeMode"])

    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameSizeMode"], value)

    @property
    def FramelossPercentValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The frame loss percentage value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramelossPercentValue"])

    @FramelossPercentValue.setter
    def FramelossPercentValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramelossPercentValue"], value)

    @property
    def FramesPerBurstGap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The frames per burst gap.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesPerBurstGap"])

    @FramesPerBurstGap.setter
    def FramesPerBurstGap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesPerBurstGap"], value)

    @property
    def FramesizeList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The frame size list of the test configuration.
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
        - number: The test configuration gap.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Gap"])

    @Gap.setter
    def Gap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Gap"], value)

    @property
    def GroupDistributionType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(acrossHosts | acrossPorts): The group distribution type.
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
        - number: The igmp V1 timeout.
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
        - number: The igmp version of the test configuration.
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
    def IncrAddresses(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The incremented address of the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrAddresses"])

    @IncrAddresses.setter
    def IncrAddresses(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrAddresses"], value)

    @property
    def InitialBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The initial binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialBinaryLoadRate"])

    @InitialBinaryLoadRate.setter
    def InitialBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialBinaryLoadRate"], value)

    @property
    def InitialRate(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The initial rate of the test configuration.
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
        - number: The initial step of the load type.
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
        - str: The IPV4 address.
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
        - str: The IPV6 address.
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
        - str: The ipv6 address.
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
        - str: The Multicast automatic frame data.
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
        - number: The join and leave rate of the test configuration.
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
        - number: The join and leave wait time.
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
        - str(cutThrough | storeForward): The latency type.
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
    def LoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(binary | quickSearch | step): The load type.
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
        - str: The map type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapType"])

    @MapType.setter
    def MapType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapType"], value)

    @property
    def MaxBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxBinaryLoadRate"])

    @MaxBinaryLoadRate.setter
    def MaxBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxBinaryLoadRate"], value)

    @property
    def MaxIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum frame size incrememnt.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxIncrementFrameSize"])

    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxIncrementFrameSize"], value)

    @property
    def MaxQuickSearchLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the maximum QuickSearch load rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxQuickSearchLoadRate"])

    @MaxQuickSearchLoadRate.setter
    def MaxQuickSearchLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxQuickSearchLoadRate"], value)

    @property
    def MaxRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum random frame size.
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
        - number: The maximum step of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxStepLoadRate"])

    @MaxStepLoadRate.setter
    def MaxStepLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxStepLoadRate"], value)

    @property
    def MinBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinBinaryLoadRate"])

    @MinBinaryLoadRate.setter
    def MinBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinBinaryLoadRate"], value)

    @property
    def MinIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum frame size increment.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinIncrementFrameSize"])

    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinIncrementFrameSize"], value)

    @property
    def MinQuickSearchLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the minum Quick Search load rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinQuickSearchLoadRate"])

    @MinQuickSearchLoadRate.setter
    def MinQuickSearchLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinQuickSearchLoadRate"], value)

    @property
    def MinRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum random frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRandomFrameSize"])

    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRandomFrameSize"], value)

    @property
    def MldVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The mld version of the test configuration.
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
        - number: The number of addresses of the test configuration.
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
        - number: The number of trials for the test configuration.
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
    def QuickSearchFrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(%): Sets the quick search frame loss unit
        """
        return self._get_attribute(self._SDM_ATT_MAP["QuickSearchFrameLossUnit"])

    @QuickSearchFrameLossUnit.setter
    def QuickSearchFrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["QuickSearchFrameLossUnit"], value)

    @property
    def QuickSearchLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Sets the quick search load unit
        """
        return self._get_attribute(self._SDM_ATT_MAP["QuickSearchLoadUnit"])

    @QuickSearchLoadUnit.setter
    def QuickSearchLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["QuickSearchLoadUnit"], value)

    @property
    def QuickSearchResolution(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the quick search resolution
        """
        return self._get_attribute(self._SDM_ATT_MAP["QuickSearchResolution"])

    @QuickSearchResolution.setter
    def QuickSearchResolution(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QuickSearchResolution"], value)

    @property
    def QuickSearchSearchType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(linear): Sets the quick search type
        """
        return self._get_attribute(self._SDM_ATT_MAP["QuickSearchSearchType"])

    @QuickSearchSearchType.setter
    def QuickSearchSearchType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["QuickSearchSearchType"], value)

    @property
    def QuickSearchTolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the quick search tolerance
        """
        return self._get_attribute(self._SDM_ATT_MAP["QuickSearchTolerance"])

    @QuickSearchTolerance.setter
    def QuickSearchTolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QuickSearchTolerance"], value)

    @property
    def ReportSequenceError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The report of sequence error.
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
        - str(gbps | gBps | kbps | kBps | mbps | mBps): The report throughput rate unit.
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
        - bool: The router alert.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterAlert"])

    @RouterAlert.setter
    def RouterAlert(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterAlert"], value)

    @property
    def SaturationIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The saturation iteration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SaturationIteration"])

    @SaturationIteration.setter
    def SaturationIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SaturationIteration"], value)

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
        - str(% | frames): The step frame loss unit.
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
        - number: The step increment frame size.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The step load unit.
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
        - number: The step of the step load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepStepLoadRate"])

    @StepStepLoadRate.setter
    def StepStepLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepStepLoadRate"], value)

    @property
    def StepTolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The step tolerance.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepTolerance"])

    @StepTolerance.setter
    def StepTolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepTolerance"], value)

    @property
    def StopTestOnHighLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, the test is stopped at high loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StopTestOnHighLoss"])

    @StopTestOnHighLoss.setter
    def StopTestOnHighLoss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StopTestOnHighLoss"], value)

    @property
    def SupportedTrafficTypes(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The supported traffic types.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportedTrafficTypes"])

    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportedTrafficTypes"], value)

    @property
    def TestMapType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fullymesh | one2many): The test map type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestMapType"])

    @TestMapType.setter
    def TestMapType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestMapType"], value)

    @property
    def TestTrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The test traffic type.
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
        - number: The transmission delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxDelay"])

    @TxDelay.setter
    def TxDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxDelay"], value)

    @property
    def UnchangedInitial(self):
        # type: () -> str
        """
        Returns
        -------
        - str(False | True): If true, the initial is unchanged.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnchangedInitial"])

    @UnchangedInitial.setter
    def UnchangedInitial(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnchangedInitial"], value)

    @property
    def UsePercentOffsets(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The use percent offsets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UsePercentOffsets"])

    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UsePercentOffsets"], value)

    def update(
        self,
        ApplyMode=None,
        AssignGroupType=None,
        BackoffIteration=None,
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
        DelayAfterTransmit=None,
        Duration=None,
        EnableBackoffIteration=None,
        EnableDataIntegrity=None,
        EnableExtraIterations=None,
        EnableFastConvergence=None,
        EnableLayer1Rate=None,
        EnableLeaveGroup=None,
        EnableMinFrameSize=None,
        EnableMulticastQuerier=None,
        EnableOldStatsForReef=None,
        EnableSaturationIteration=None,
        EnableStopTestOnHighLoss=None,
        ExtraIterationOffsets=None,
        FastConvergenceDuration=None,
        FastConvergenceThreshold=None,
        FloodedFramesEnabled=None,
        ForceRegenerate=None,
        FrameLossUnit=None,
        FrameSizeMode=None,
        FramelossPercentValue=None,
        FramesPerBurstGap=None,
        FramesizeList=None,
        Gap=None,
        GroupDistributionType=None,
        IgmpV1Timeout=None,
        IgmpVersion=None,
        Igmpv3MessageType=None,
        Igmpv3SourceAddrList=None,
        IncrAddresses=None,
        InitialBinaryLoadRate=None,
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
        LoadType=None,
        MapType=None,
        MaxBinaryLoadRate=None,
        MaxIncrementFrameSize=None,
        MaxQuickSearchLoadRate=None,
        MaxRandomFrameSize=None,
        MaxStepLoadRate=None,
        MinBinaryLoadRate=None,
        MinIncrementFrameSize=None,
        MinQuickSearchLoadRate=None,
        MinRandomFrameSize=None,
        MldVersion=None,
        NumAddresses=None,
        NumIterations=None,
        Numtrials=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        ProtocolItem=None,
        QuickSearchFrameLossUnit=None,
        QuickSearchLoadUnit=None,
        QuickSearchResolution=None,
        QuickSearchSearchType=None,
        QuickSearchTolerance=None,
        ReportSequenceError=None,
        ReportTputRateUnit=None,
        RouterAlert=None,
        SaturationIteration=None,
        ShowDetailedBinaryResults=None,
        StepFrameLossUnit=None,
        StepIncrementFrameSize=None,
        StepLoadUnit=None,
        StepStepLoadRate=None,
        StepTolerance=None,
        StopTestOnHighLoss=None,
        SupportedTrafficTypes=None,
        TestMapType=None,
        TestTrafficType=None,
        TxDelay=None,
        UnchangedInitial=None,
        UsePercentOffsets=None,
    ):
        # type: (str, str, int, bool, int, str, str, int, str, int, int, bool, bool, int, int, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, int, int, bool, bool, str, str, int, int, List[str], int, str, int, int, str, str, int, int, str, int, str, str, str, str, int, int, int, str, bool, str, int, str, str, int, int, int, int, int, int, int, int, int, int, int, int, int, bool, str, int, List[str], str, str, int, str, int, bool, str, bool, int, bool, str, int, str, int, int, int, str, str, str, int, str, str) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): The assigned group type.
        - BackoffIteration (number): IF true, the iteration is backed off.
        - BidirectionalOptionEnabled (bool): if true, the bidirectional option is enabled.
        - BinaryBackoff (number): The binary backoff.
        - BinaryFrameLossUnit (str(% | frames)): The binary frame loss unit.
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The binary load unit.
        - BinaryResolution (number): The binary resolution.
        - BinarySearchType (str(linear)): The binary search type.
        - BinaryTolerance (number): The binary tolerance.
        - BurstSize (number): The burst size.
        - CalculateJitter (bool): The calculated jitter.
        - CalculateLatency (bool): The latency is calculated.
        - CountRandomFrameSize (number): if true, the random frame size is counted.
        - DelayAfterTransmit (number): The delay after transmit of test config.
        - Duration (number): The test configuration duration.
        - EnableBackoffIteration (bool): If true, the back off iteration is enabled.
        - EnableDataIntegrity (bool): If true, data integrity is enabled.
        - EnableExtraIterations (bool): If true, extra iterations are enabled.
        - EnableFastConvergence (bool): If true, fast convergence is enabled.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableLeaveGroup (bool): If true, the leave group is enabled.
        - EnableMinFrameSize (bool): If true,the minimum frame size is enabled.
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableOldStatsForReef (bool): If true, the old stats for reef is enabled.
        - EnableSaturationIteration (bool): If true, the saturation iteration us enabled.
        - EnableStopTestOnHighLoss (bool): If true, the test is stopped on high loss.
        - ExtraIterationOffsets (str): The extra iteration offsets.
        - FastConvergenceDuration (number): The fast convergence duration.
        - FastConvergenceThreshold (number): The fast convergence threshold.
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): If true, the test configuration is forcefully regenerated.
        - FrameLossUnit (str): The frame loss unit.
        - FrameSizeMode (str(custom | fixed | increment | random)): The frame size mode of test configuration.
        - FramelossPercentValue (number): The frame loss percentage value.
        - FramesPerBurstGap (number): The frames per burst gap.
        - FramesizeList (list(str)): The frame size list of the test configuration.
        - Gap (number): The test configuration gap.
        - GroupDistributionType (str(acrossHosts | acrossPorts)): The group distribution type.
        - IgmpV1Timeout (number): The igmp V1 timeout.
        - IgmpVersion (number): The igmp version of the test configuration.
        - Igmpv3MessageType (str(exclude | include)): It gives details about the igmpv3 message type in the test configuration
        - Igmpv3SourceAddrList (str): It gives details about the igmpv3 source address list in the test configuration
        - IncrAddresses (number): The incremented address of the test configuration.
        - InitialBinaryLoadRate (number): The initial binary load rate.
        - InitialRate (str): The initial rate of the test configuration.
        - InitialStepLoadRate (number): The initial step of the load type.
        - Ipv4Address (str): The IPV4 address.
        - Ipv6Address (str): The IPV6 address.
        - IsIPv6 (str): The ipv6 address.
        - IsMulticastAutomaticFrameData (str): The Multicast automatic frame data.
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): The join and leave rate of the test configuration.
        - JoinLeaveWaitTime (number): The join and leave wait time.
        - LatencyBins (str): Sets the latency bins statistics
        - LatencyBinsEnabled (bool): Enables the latency bins statistics
        - LatencyType (str(cutThrough | storeForward)): The latency type.
        - LoadInitialRate (number): The initial rate of the load.
        - LoadType (str(binary | quickSearch | step)): The load type.
        - MapType (str): The map type.
        - MaxBinaryLoadRate (number): The maximum binary load rate.
        - MaxIncrementFrameSize (number): The maximum frame size incrememnt.
        - MaxQuickSearchLoadRate (number): Sets the maximum QuickSearch load rate
        - MaxRandomFrameSize (number): The maximum random frame size.
        - MaxStepLoadRate (number): The maximum step of the load rate.
        - MinBinaryLoadRate (number): The minimum binary load rate.
        - MinIncrementFrameSize (number): The minimum frame size increment.
        - MinQuickSearchLoadRate (number): Sets the minum Quick Search load rate
        - MinRandomFrameSize (number): The minimum random frame size.
        - MldVersion (number): The mld version of the test configuration.
        - NumAddresses (number): The number of addresses of the test configuration.
        - NumIterations (number): The number of iterations.
        - Numtrials (number): The number of trials for the test configuration.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - QuickSearchFrameLossUnit (str(%)): Sets the quick search frame loss unit
        - QuickSearchLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Sets the quick search load unit
        - QuickSearchResolution (number): Sets the quick search resolution
        - QuickSearchSearchType (str(linear)): Sets the quick search type
        - QuickSearchTolerance (number): Sets the quick search tolerance
        - ReportSequenceError (bool): The report of sequence error.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The report throughput rate unit.
        - RouterAlert (bool): The router alert.
        - SaturationIteration (number): The saturation iteration.
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepFrameLossUnit (str(% | frames)): The step frame loss unit.
        - StepIncrementFrameSize (number): The step increment frame size.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The step load unit.
        - StepStepLoadRate (number): The step of the step load rate.
        - StepTolerance (number): The step tolerance.
        - StopTestOnHighLoss (number): If true, the test is stopped at high loss.
        - SupportedTrafficTypes (str): The supported traffic types.
        - TestMapType (str(fullymesh | one2many)): The test map type.
        - TestTrafficType (str): The test traffic type.
        - TxDelay (number): The transmission delay.
        - UnchangedInitial (str(False | True)): If true, the initial is unchanged.
        - UsePercentOffsets (str): The use percent offsets.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ApplyMode=None,
        AssignGroupType=None,
        BackoffIteration=None,
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
        DelayAfterTransmit=None,
        Duration=None,
        EnableBackoffIteration=None,
        EnableDataIntegrity=None,
        EnableExtraIterations=None,
        EnableFastConvergence=None,
        EnableLayer1Rate=None,
        EnableLeaveGroup=None,
        EnableMinFrameSize=None,
        EnableMulticastQuerier=None,
        EnableOldStatsForReef=None,
        EnableSaturationIteration=None,
        EnableStopTestOnHighLoss=None,
        ExtraIterationOffsets=None,
        FastConvergenceDuration=None,
        FastConvergenceThreshold=None,
        FloodedFramesEnabled=None,
        ForceRegenerate=None,
        FrameLossUnit=None,
        FrameSizeMode=None,
        FramelossPercentValue=None,
        FramesPerBurstGap=None,
        FramesizeList=None,
        Gap=None,
        GroupDistributionType=None,
        IgmpV1Timeout=None,
        IgmpVersion=None,
        Igmpv3MessageType=None,
        Igmpv3SourceAddrList=None,
        IncrAddresses=None,
        InitialBinaryLoadRate=None,
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
        LoadType=None,
        MapType=None,
        MaxBinaryLoadRate=None,
        MaxIncrementFrameSize=None,
        MaxQuickSearchLoadRate=None,
        MaxRandomFrameSize=None,
        MaxStepLoadRate=None,
        MinBinaryLoadRate=None,
        MinIncrementFrameSize=None,
        MinQuickSearchLoadRate=None,
        MinRandomFrameSize=None,
        MldVersion=None,
        NumAddresses=None,
        NumIterations=None,
        Numtrials=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        ProtocolItem=None,
        QuickSearchFrameLossUnit=None,
        QuickSearchLoadUnit=None,
        QuickSearchResolution=None,
        QuickSearchSearchType=None,
        QuickSearchTolerance=None,
        ReportSequenceError=None,
        ReportTputRateUnit=None,
        RouterAlert=None,
        SaturationIteration=None,
        ShowDetailedBinaryResults=None,
        StepFrameLossUnit=None,
        StepIncrementFrameSize=None,
        StepLoadUnit=None,
        StepStepLoadRate=None,
        StepTolerance=None,
        StopTestOnHighLoss=None,
        SupportedTrafficTypes=None,
        TestMapType=None,
        TestTrafficType=None,
        TxDelay=None,
        UnchangedInitial=None,
        UsePercentOffsets=None,
    ):
        # type: (str, str, int, bool, int, str, str, int, str, int, int, bool, bool, int, int, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, int, int, bool, bool, str, str, int, int, List[str], int, str, int, int, str, str, int, int, str, int, str, str, str, str, int, int, int, str, bool, str, int, str, str, int, int, int, int, int, int, int, int, int, int, int, int, int, bool, str, int, List[str], str, str, int, str, int, bool, str, bool, int, bool, str, int, str, int, int, int, str, str, str, int, str, str) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): The assigned group type.
        - BackoffIteration (number): IF true, the iteration is backed off.
        - BidirectionalOptionEnabled (bool): if true, the bidirectional option is enabled.
        - BinaryBackoff (number): The binary backoff.
        - BinaryFrameLossUnit (str(% | frames)): The binary frame loss unit.
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The binary load unit.
        - BinaryResolution (number): The binary resolution.
        - BinarySearchType (str(linear)): The binary search type.
        - BinaryTolerance (number): The binary tolerance.
        - BurstSize (number): The burst size.
        - CalculateJitter (bool): The calculated jitter.
        - CalculateLatency (bool): The latency is calculated.
        - CountRandomFrameSize (number): if true, the random frame size is counted.
        - DelayAfterTransmit (number): The delay after transmit of test config.
        - Duration (number): The test configuration duration.
        - EnableBackoffIteration (bool): If true, the back off iteration is enabled.
        - EnableDataIntegrity (bool): If true, data integrity is enabled.
        - EnableExtraIterations (bool): If true, extra iterations are enabled.
        - EnableFastConvergence (bool): If true, fast convergence is enabled.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableLeaveGroup (bool): If true, the leave group is enabled.
        - EnableMinFrameSize (bool): If true,the minimum frame size is enabled.
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableOldStatsForReef (bool): If true, the old stats for reef is enabled.
        - EnableSaturationIteration (bool): If true, the saturation iteration us enabled.
        - EnableStopTestOnHighLoss (bool): If true, the test is stopped on high loss.
        - ExtraIterationOffsets (str): The extra iteration offsets.
        - FastConvergenceDuration (number): The fast convergence duration.
        - FastConvergenceThreshold (number): The fast convergence threshold.
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): If true, the test configuration is forcefully regenerated.
        - FrameLossUnit (str): The frame loss unit.
        - FrameSizeMode (str(custom | fixed | increment | random)): The frame size mode of test configuration.
        - FramelossPercentValue (number): The frame loss percentage value.
        - FramesPerBurstGap (number): The frames per burst gap.
        - FramesizeList (list(str)): The frame size list of the test configuration.
        - Gap (number): The test configuration gap.
        - GroupDistributionType (str(acrossHosts | acrossPorts)): The group distribution type.
        - IgmpV1Timeout (number): The igmp V1 timeout.
        - IgmpVersion (number): The igmp version of the test configuration.
        - Igmpv3MessageType (str(exclude | include)): It gives details about the igmpv3 message type in the test configuration
        - Igmpv3SourceAddrList (str): It gives details about the igmpv3 source address list in the test configuration
        - IncrAddresses (number): The incremented address of the test configuration.
        - InitialBinaryLoadRate (number): The initial binary load rate.
        - InitialRate (str): The initial rate of the test configuration.
        - InitialStepLoadRate (number): The initial step of the load type.
        - Ipv4Address (str): The IPV4 address.
        - Ipv6Address (str): The IPV6 address.
        - IsIPv6 (str): The ipv6 address.
        - IsMulticastAutomaticFrameData (str): The Multicast automatic frame data.
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): The join and leave rate of the test configuration.
        - JoinLeaveWaitTime (number): The join and leave wait time.
        - LatencyBins (str): Sets the latency bins statistics
        - LatencyBinsEnabled (bool): Enables the latency bins statistics
        - LatencyType (str(cutThrough | storeForward)): The latency type.
        - LoadInitialRate (number): The initial rate of the load.
        - LoadType (str(binary | quickSearch | step)): The load type.
        - MapType (str): The map type.
        - MaxBinaryLoadRate (number): The maximum binary load rate.
        - MaxIncrementFrameSize (number): The maximum frame size incrememnt.
        - MaxQuickSearchLoadRate (number): Sets the maximum QuickSearch load rate
        - MaxRandomFrameSize (number): The maximum random frame size.
        - MaxStepLoadRate (number): The maximum step of the load rate.
        - MinBinaryLoadRate (number): The minimum binary load rate.
        - MinIncrementFrameSize (number): The minimum frame size increment.
        - MinQuickSearchLoadRate (number): Sets the minum Quick Search load rate
        - MinRandomFrameSize (number): The minimum random frame size.
        - MldVersion (number): The mld version of the test configuration.
        - NumAddresses (number): The number of addresses of the test configuration.
        - NumIterations (number): The number of iterations.
        - Numtrials (number): The number of trials for the test configuration.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - QuickSearchFrameLossUnit (str(%)): Sets the quick search frame loss unit
        - QuickSearchLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Sets the quick search load unit
        - QuickSearchResolution (number): Sets the quick search resolution
        - QuickSearchSearchType (str(linear)): Sets the quick search type
        - QuickSearchTolerance (number): Sets the quick search tolerance
        - ReportSequenceError (bool): The report of sequence error.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The report throughput rate unit.
        - RouterAlert (bool): The router alert.
        - SaturationIteration (number): The saturation iteration.
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepFrameLossUnit (str(% | frames)): The step frame loss unit.
        - StepIncrementFrameSize (number): The step increment frame size.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The step load unit.
        - StepStepLoadRate (number): The step of the step load rate.
        - StepTolerance (number): The step tolerance.
        - StopTestOnHighLoss (number): If true, the test is stopped at high loss.
        - SupportedTrafficTypes (str): The supported traffic types.
        - TestMapType (str(fullymesh | one2many)): The test map type.
        - TestTrafficType (str): The test traffic type.
        - TxDelay (number): The transmission delay.
        - UnchangedInitial (str(False | True)): If true, the initial is unchanged.
        - UsePercentOffsets (str): The use percent offsets.

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
