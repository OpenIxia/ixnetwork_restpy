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
        "BackoffIteration": "backoffIteration",
        "CalculateJitter": "calculateJitter",
        "CalculateLatency": "calculateLatency",
        "ContentInformation": "contentInformation",
        "CountRandomLoadRate": "countRandomLoadRate",
        "DelayAfterTransmit": "delayAfterTransmit",
        "Duration": "duration",
        "DynamicRateList": "dynamicRateList",
        "EnableBackoffIteration": "enableBackoffIteration",
        "EnableDataIntegrity": "enableDataIntegrity",
        "EnableExtraIterations": "enableExtraIterations",
        "EnableFastConvergence": "enableFastConvergence",
        "EnableLayer1Rate": "enableLayer1Rate",
        "EnableMinFrameSize": "enableMinFrameSize",
        "EnableOldStatsForReef": "enableOldStatsForReef",
        "EnableSaturationIteration": "enableSaturationIteration",
        "EnableStopTestOnHighLoss": "enableStopTestOnHighLoss",
        "ExtraIterationOffsets": "extraIterationOffsets",
        "FastConvergenceDuration": "fastConvergenceDuration",
        "FastConvergenceThreshold": "fastConvergenceThreshold",
        "FixedIteration": "fixedIteration",
        "FixedLoadUnit": "fixedLoadUnit",
        "ForceRegenerate": "forceRegenerate",
        "FrameLossUnit": "frameLossUnit",
        "FramesPerBurstGap": "framesPerBurstGap",
        "Framesize": "framesize",
        "FramesizeFixedValue": "framesizeFixedValue",
        "FramesizeList": "framesizeList",
        "Gap": "gap",
        "GenerateTrackingOptionAggregationFiles": "generateTrackingOptionAggregationFiles",
        "IncrementLoadUnit": "incrementLoadUnit",
        "InitialIncrementLoadRate": "initialIncrementLoadRate",
        "InitialStepLoadRate": "initialStepLoadRate",
        "Ipv4rate": "ipv4rate",
        "Ipv6rate": "ipv6rate",
        "LatencyBins": "latencyBins",
        "LatencyBinsEnabled": "latencyBinsEnabled",
        "LatencyType": "latencyType",
        "LoadRateList": "loadRateList",
        "LoadRateValue": "loadRateValue",
        "LoadType": "loadType",
        "MapType": "mapType",
        "MaxIncrementLoadRate": "maxIncrementLoadRate",
        "MaxRandomLoadRate": "maxRandomLoadRate",
        "MaxStepLoadRate": "maxStepLoadRate",
        "MinFpsRate": "minFpsRate",
        "MinKbpsRate": "minKbpsRate",
        "MinRandomLoadRate": "minRandomLoadRate",
        "Numtrials": "numtrials",
        "PercentMaxRate": "percentMaxRate",
        "PortDelayEnabled": "portDelayEnabled",
        "PortDelayUnit": "portDelayUnit",
        "PortDelayValue": "portDelayValue",
        "ProtocolItem": "protocolItem",
        "RandomLoadUnit": "randomLoadUnit",
        "RateSelect": "rateSelect",
        "ReportSequenceError": "reportSequenceError",
        "ReportTputRateUnit": "reportTputRateUnit",
        "Resolution": "resolution",
        "Rfc2889ordering": "rfc2889ordering",
        "SaturationIteration": "saturationIteration",
        "SkipDefaultPassFailEvaluation": "skipDefaultPassFailEvaluation",
        "StaggeredStart": "staggeredStart",
        "StepFrameLossUnit": "stepFrameLossUnit",
        "StepIncrementLoadRate": "stepIncrementLoadRate",
        "StepLoadUnit": "stepLoadUnit",
        "StepStepLoadRate": "stepStepLoadRate",
        "StepTolerance": "stepTolerance",
        "StopTestOnHighLoss": "stopTestOnHighLoss",
        "SupportedTrafficTypes": "supportedTrafficTypes",
        "TestTrafficType": "testTrafficType",
        "TimelineRateList": "timelineRateList",
        "Tolerance": "tolerance",
        "TxDelay": "txDelay",
        "UsePercentOffsets": "usePercentOffsets",
    }
    _SDM_ENUM_MAP = {
        "fixedLoadUnit": [
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
        "incrementLoadUnit": [
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
        "latencyType": ["cutThrough", "storeForward"],
        "loadType": ["dynamic", "step", "timeline"],
        "portDelayUnit": ["bytes", "nanoseconds"],
        "randomLoadUnit": [
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
        "rateSelect": ["fpsRate", "kbpsRate", "percentMaxRate"],
        "reportTputRateUnit": ["gbps", "gBps", "kbps", "kBps", "mbps", "mBps"],
        "rfc2889ordering": ["noOrdering", "unchanged", "val2889Ordering"],
        "stepFrameLossUnit": ["%"],
        "stepLoadUnit": ["percentMaxRate"],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

    @property
    def BackoffIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This enables the test to run an extra iteration for calculating the Backoff Latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BackoffIteration"])

    @BackoffIteration.setter
    def BackoffIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BackoffIteration"], value)

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
        - bool: If true, calculates the latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CalculateLatency"])

    @CalculateLatency.setter
    def CalculateLatency(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CalculateLatency"], value)

    @property
    def ContentInformation(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ContentInformation"])

    @ContentInformation.setter
    def ContentInformation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ContentInformation"], value)

    @property
    def CountRandomLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The random count of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CountRandomLoadRate"])

    @CountRandomLoadRate.setter
    def CountRandomLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CountRandomLoadRate"], value)

    @property
    def DelayAfterTransmit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the amount of delay after every transmit.
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
    def DynamicRateList(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DynamicRateList"])

    @DynamicRateList.setter
    def DynamicRateList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DynamicRateList"], value)

    @property
    def EnableBackoffIteration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables back off iteration test.
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
        - bool: If true, enables the checking of data integrity for the pass or fail of the trial.
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
        - bool: If true, more iterations are performed.
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
        - bool: If true, the test perform iterations using the fast convergence duration configured.
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
    def EnableOldStatsForReef(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables old statistics for reef load module.
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
        - bool: If true, enables the test to run an extra iteration for calculating the Saturation Latency.
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
        - bool: The test stops in case of a high loss.
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
        - str: This enables the test to run an extra iteration.
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
        - number: This enables the test to perform iterations using the fast convergence duration configured.
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
        - number: This enables the test to perform iterations using the fast convergence threshold configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastConvergenceThreshold"])

    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastConvergenceThreshold"], value)

    @property
    def FixedIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["FixedIteration"])

    @FixedIteration.setter
    def FixedIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FixedIteration"], value)

    @property
    def FixedLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The fixed load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FixedLoadUnit"])

    @FixedLoadUnit.setter
    def FixedLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FixedLoadUnit"], value)

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
    def FrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Frame loss measurement unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameLossUnit"])

    @FrameLossUnit.setter
    def FrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameLossUnit"], value)

    @property
    def FramesPerBurstGap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of frames to be sent after each burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesPerBurstGap"])

    @FramesPerBurstGap.setter
    def FramesPerBurstGap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesPerBurstGap"], value)

    @property
    def Framesize(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The frame size to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Framesize"])

    @Framesize.setter
    def Framesize(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Framesize"], value)

    @property
    def FramesizeFixedValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The fixed value of frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesizeFixedValue"])

    @FramesizeFixedValue.setter
    def FramesizeFixedValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesizeFixedValue"], value)

    @property
    def FramesizeList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The list of the available frame sizes.
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
    def GenerateTrackingOptionAggregationFiles(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the tracking option in aggregation files.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["GenerateTrackingOptionAggregationFiles"]
        )

    @GenerateTrackingOptionAggregationFiles.setter
    def GenerateTrackingOptionAggregationFiles(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["GenerateTrackingOptionAggregationFiles"], value
        )

    @property
    def IncrementLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The unit increment for the load.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementLoadUnit"])

    @IncrementLoadUnit.setter
    def IncrementLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementLoadUnit"], value)

    @property
    def InitialIncrementLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The initial incremental value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialIncrementLoadRate"])

    @InitialIncrementLoadRate.setter
    def InitialIncrementLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialIncrementLoadRate"], value)

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
    def Ipv4rate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The rate at which IPv4 traffic is sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4rate"])

    @Ipv4rate.setter
    def Ipv4rate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4rate"], value)

    @property
    def Ipv6rate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The rate at which IPv6 traffic is sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6rate"])

    @Ipv6rate.setter
    def Ipv6rate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6rate"], value)

    @property
    def LatencyBins(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: Sets the latency bins statistics.
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
        - bool: Enables the latency bins statistics.
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
        - str(cutThrough | storeForward): The type of latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyType"])

    @LatencyType.setter
    def LatencyType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyType"], value)

    @property
    def LoadRateList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Enters the Load Rate List.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadRateList"])

    @LoadRateList.setter
    def LoadRateList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadRateList"], value)

    @property
    def LoadRateValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadRateValue"])

    @LoadRateValue.setter
    def LoadRateValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadRateValue"], value)

    @property
    def LoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(dynamic | step | timeline): The type of the payload setting.
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
        - str: The mapping type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapType"])

    @MapType.setter
    def MapType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapType"], value)

    @property
    def MaxIncrementLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum incremental value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxIncrementLoadRate"])

    @MaxIncrementLoadRate.setter
    def MaxIncrementLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxIncrementLoadRate"], value)

    @property
    def MaxRandomLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum random value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxRandomLoadRate"])

    @MaxRandomLoadRate.setter
    def MaxRandomLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxRandomLoadRate"], value)

    @property
    def MaxStepLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum step value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxStepLoadRate"])

    @MaxStepLoadRate.setter
    def MaxStepLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxStepLoadRate"], value)

    @property
    def MinFpsRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The rate at which minimum frames are sent per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinFpsRate"])

    @MinFpsRate.setter
    def MinFpsRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinFpsRate"], value)

    @property
    def MinKbpsRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The rate at which minimum frames are sent per kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinKbpsRate"])

    @MinKbpsRate.setter
    def MinKbpsRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinKbpsRate"], value)

    @property
    def MinRandomLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum random value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRandomLoadRate"])

    @MinRandomLoadRate.setter
    def MinRandomLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRandomLoadRate"], value)

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
    def PercentMaxRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The rate selected in percentMax.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PercentMaxRate"])

    @PercentMaxRate.setter
    def PercentMaxRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PercentMaxRate"], value)

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
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured.
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
        - number: Sets the port delay value.
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
    def RandomLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The random values of the load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RandomLoadUnit"])

    @RandomLoadUnit.setter
    def RandomLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RandomLoadUnit"], value)

    @property
    def RateSelect(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fpsRate | kbpsRate | percentMaxRate): The rate selected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RateSelect"])

    @RateSelect.setter
    def RateSelect(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RateSelect"], value)

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
    def ReportTputRateUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(gbps | gBps | kbps | kBps | mbps | mBps): The unit of rate for throughput.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportTputRateUnit"])

    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportTputRateUnit"], value)

    @property
    def Resolution(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Resolution"])

    @Resolution.setter
    def Resolution(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Resolution"], value)

    @property
    def Rfc2889ordering(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noOrdering | unchanged | val2889Ordering): If true, indicates frame ordering by Rfc2889.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Rfc2889ordering"])

    @Rfc2889ordering.setter
    def Rfc2889ordering(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Rfc2889ordering"], value)

    @property
    def SaturationIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This enables the test to run an extra iteration for calculating the Saturation latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SaturationIteration"])

    @SaturationIteration.setter
    def SaturationIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SaturationIteration"], value)

    @property
    def SkipDefaultPassFailEvaluation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it skips the default pass fail evaluation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SkipDefaultPassFailEvaluation"])

    @SkipDefaultPassFailEvaluation.setter
    def SkipDefaultPassFailEvaluation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SkipDefaultPassFailEvaluation"], value)

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
    def StepFrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(%): Signifies the step frame loss unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepFrameLossUnit"])

    @StepFrameLossUnit.setter
    def StepFrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepFrameLossUnit"], value)

    @property
    def StepIncrementLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The step incremental value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepIncrementLoadRate"])

    @StepIncrementLoadRate.setter
    def StepIncrementLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepIncrementLoadRate"], value)

    @property
    def StepLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(percentMaxRate): Specifies the step rate of the load unit.
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
    def StepTolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The step value of the tolerance level.
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
        - number: It stops test on high loss.
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
    def TimelineRateList(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["TimelineRateList"])

    @TimelineRateList.setter
    def TimelineRateList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TimelineRateList"], value)

    @property
    def Tolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value set for the tolerance level.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Tolerance"])

    @Tolerance.setter
    def Tolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Tolerance"], value)

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
    def UsePercentOffsets(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If true, sets the offset value in percentage.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UsePercentOffsets"])

    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UsePercentOffsets"], value)

    def update(
        self,
        BackoffIteration=None,
        CalculateJitter=None,
        CalculateLatency=None,
        ContentInformation=None,
        CountRandomLoadRate=None,
        DelayAfterTransmit=None,
        Duration=None,
        DynamicRateList=None,
        EnableBackoffIteration=None,
        EnableDataIntegrity=None,
        EnableExtraIterations=None,
        EnableFastConvergence=None,
        EnableLayer1Rate=None,
        EnableMinFrameSize=None,
        EnableOldStatsForReef=None,
        EnableSaturationIteration=None,
        EnableStopTestOnHighLoss=None,
        ExtraIterationOffsets=None,
        FastConvergenceDuration=None,
        FastConvergenceThreshold=None,
        FixedIteration=None,
        FixedLoadUnit=None,
        ForceRegenerate=None,
        FrameLossUnit=None,
        FramesPerBurstGap=None,
        Framesize=None,
        FramesizeFixedValue=None,
        FramesizeList=None,
        Gap=None,
        GenerateTrackingOptionAggregationFiles=None,
        IncrementLoadUnit=None,
        InitialIncrementLoadRate=None,
        InitialStepLoadRate=None,
        Ipv4rate=None,
        Ipv6rate=None,
        LatencyBins=None,
        LatencyBinsEnabled=None,
        LatencyType=None,
        LoadRateList=None,
        LoadRateValue=None,
        LoadType=None,
        MapType=None,
        MaxIncrementLoadRate=None,
        MaxRandomLoadRate=None,
        MaxStepLoadRate=None,
        MinFpsRate=None,
        MinKbpsRate=None,
        MinRandomLoadRate=None,
        Numtrials=None,
        PercentMaxRate=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        ProtocolItem=None,
        RandomLoadUnit=None,
        RateSelect=None,
        ReportSequenceError=None,
        ReportTputRateUnit=None,
        Resolution=None,
        Rfc2889ordering=None,
        SaturationIteration=None,
        SkipDefaultPassFailEvaluation=None,
        StaggeredStart=None,
        StepFrameLossUnit=None,
        StepIncrementLoadRate=None,
        StepLoadUnit=None,
        StepStepLoadRate=None,
        StepTolerance=None,
        StopTestOnHighLoss=None,
        SupportedTrafficTypes=None,
        TestTrafficType=None,
        TimelineRateList=None,
        Tolerance=None,
        TxDelay=None,
        UsePercentOffsets=None,
    ):
        # type: (int, bool, bool, str, int, int, int, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, int, int, int, str, bool, str, int, str, int, List[str], int, bool, str, int, int, int, int, str, bool, str, str, int, str, str, int, int, int, int, int, int, int, int, bool, str, int, List[str], str, str, bool, str, int, str, int, bool, bool, str, int, str, int, int, int, str, str, str, int, int, str) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - BackoffIteration (number): This enables the test to run an extra iteration for calculating the Backoff Latency.
        - CalculateJitter (bool): If true, the jitter is calculated.
        - CalculateLatency (bool): If true, calculates the latency.
        - ContentInformation (str): NOT DEFINED
        - CountRandomLoadRate (number): The random count of the load rate.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - DynamicRateList (str): NOT DEFINED
        - EnableBackoffIteration (bool): If true, enables back off iteration test.
        - EnableDataIntegrity (bool): If true, enables the checking of data integrity for the pass or fail of the trial.
        - EnableExtraIterations (bool): If true, more iterations are performed.
        - EnableFastConvergence (bool): If true, the test perform iterations using the fast convergence duration configured.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableOldStatsForReef (bool): If true, enables old statistics for reef load module.
        - EnableSaturationIteration (bool): If true, enables the test to run an extra iteration for calculating the Saturation Latency.
        - EnableStopTestOnHighLoss (bool): The test stops in case of a high loss.
        - ExtraIterationOffsets (str): This enables the test to run an extra iteration.
        - FastConvergenceDuration (number): This enables the test to perform iterations using the fast convergence duration configured.
        - FastConvergenceThreshold (number): This enables the test to perform iterations using the fast convergence threshold configured.
        - FixedIteration (number): NOT DEFINED
        - FixedLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The fixed load unit.
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameLossUnit (str): Frame loss measurement unit.
        - FramesPerBurstGap (number): The number of frames to be sent after each burst.
        - Framesize (str): The frame size to be used.
        - FramesizeFixedValue (number): The fixed value of frame size.
        - FramesizeList (list(str)): The list of the available frame sizes.
        - Gap (number): The gap in transmission of frames.
        - GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The unit increment for the load.
        - InitialIncrementLoadRate (number): The initial incremental value of the load rate.
        - InitialStepLoadRate (number): The initial step value of the load rate.
        - Ipv4rate (number): The rate at which IPv4 traffic is sent.
        - Ipv6rate (number): The rate at which IPv6 traffic is sent.
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LatencyType (str(cutThrough | storeForward)): The type of latency.
        - LoadRateList (str): Enters the Load Rate List.
        - LoadRateValue (number): The value of the load rate.
        - LoadType (str(dynamic | step | timeline)): The type of the payload setting.
        - MapType (str): The mapping type.
        - MaxIncrementLoadRate (number): The maximum incremental value of the load rate.
        - MaxRandomLoadRate (number): The maximum random value of the load rate.
        - MaxStepLoadRate (number): The maximum step value of the load rate.
        - MinFpsRate (number): The rate at which minimum frames are sent per second.
        - MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
        - MinRandomLoadRate (number): The minimum random value of the load rate.
        - Numtrials (number): The integer value that states the number of trials permitted.
        - PercentMaxRate (number): The rate selected in percentMax.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - RandomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The random values of the load unit.
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): The rate selected.
        - ReportSequenceError (bool): Reports sequence errors in the test result.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The unit of rate for throughput.
        - Resolution (number): Specify the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
        - Rfc2889ordering (str(noOrdering | unchanged | val2889Ordering)): If true, indicates frame ordering by Rfc2889.
        - SaturationIteration (number): This enables the test to run an extra iteration for calculating the Saturation latency.
        - SkipDefaultPassFailEvaluation (bool): If true, it skips the default pass fail evaluation.
        - StaggeredStart (bool): Starts test with a stagger.
        - StepFrameLossUnit (str(%)): Signifies the step frame loss unit.
        - StepIncrementLoadRate (number): The step incremental value of the load rate.
        - StepLoadUnit (str(percentMaxRate)): Specifies the step rate of the load unit.
        - StepStepLoadRate (number): The incremental step value of load rate.
        - StepTolerance (number): The step value of the tolerance level.
        - StopTestOnHighLoss (number): It stops test on high loss.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TestTrafficType (str): It signifies the test traffic type value.
        - TimelineRateList (str): NOT DEFINED
        - Tolerance (number): The value set for the tolerance level.
        - TxDelay (number): Specifies the amount of delay after every transmit.
        - UsePercentOffsets (str): If true, sets the offset value in percentage.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BackoffIteration=None,
        CalculateJitter=None,
        CalculateLatency=None,
        ContentInformation=None,
        CountRandomLoadRate=None,
        DelayAfterTransmit=None,
        Duration=None,
        DynamicRateList=None,
        EnableBackoffIteration=None,
        EnableDataIntegrity=None,
        EnableExtraIterations=None,
        EnableFastConvergence=None,
        EnableLayer1Rate=None,
        EnableMinFrameSize=None,
        EnableOldStatsForReef=None,
        EnableSaturationIteration=None,
        EnableStopTestOnHighLoss=None,
        ExtraIterationOffsets=None,
        FastConvergenceDuration=None,
        FastConvergenceThreshold=None,
        FixedIteration=None,
        FixedLoadUnit=None,
        ForceRegenerate=None,
        FrameLossUnit=None,
        FramesPerBurstGap=None,
        Framesize=None,
        FramesizeFixedValue=None,
        FramesizeList=None,
        Gap=None,
        GenerateTrackingOptionAggregationFiles=None,
        IncrementLoadUnit=None,
        InitialIncrementLoadRate=None,
        InitialStepLoadRate=None,
        Ipv4rate=None,
        Ipv6rate=None,
        LatencyBins=None,
        LatencyBinsEnabled=None,
        LatencyType=None,
        LoadRateList=None,
        LoadRateValue=None,
        LoadType=None,
        MapType=None,
        MaxIncrementLoadRate=None,
        MaxRandomLoadRate=None,
        MaxStepLoadRate=None,
        MinFpsRate=None,
        MinKbpsRate=None,
        MinRandomLoadRate=None,
        Numtrials=None,
        PercentMaxRate=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        ProtocolItem=None,
        RandomLoadUnit=None,
        RateSelect=None,
        ReportSequenceError=None,
        ReportTputRateUnit=None,
        Resolution=None,
        Rfc2889ordering=None,
        SaturationIteration=None,
        SkipDefaultPassFailEvaluation=None,
        StaggeredStart=None,
        StepFrameLossUnit=None,
        StepIncrementLoadRate=None,
        StepLoadUnit=None,
        StepStepLoadRate=None,
        StepTolerance=None,
        StopTestOnHighLoss=None,
        SupportedTrafficTypes=None,
        TestTrafficType=None,
        TimelineRateList=None,
        Tolerance=None,
        TxDelay=None,
        UsePercentOffsets=None,
    ):
        # type: (int, bool, bool, str, int, int, int, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, int, int, int, str, bool, str, int, str, int, List[str], int, bool, str, int, int, int, int, str, bool, str, str, int, str, str, int, int, int, int, int, int, int, int, bool, str, int, List[str], str, str, bool, str, int, str, int, bool, bool, str, int, str, int, int, int, str, str, str, int, int, str) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - BackoffIteration (number): This enables the test to run an extra iteration for calculating the Backoff Latency.
        - CalculateJitter (bool): If true, the jitter is calculated.
        - CalculateLatency (bool): If true, calculates the latency.
        - ContentInformation (str): NOT DEFINED
        - CountRandomLoadRate (number): The random count of the load rate.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - DynamicRateList (str): NOT DEFINED
        - EnableBackoffIteration (bool): If true, enables back off iteration test.
        - EnableDataIntegrity (bool): If true, enables the checking of data integrity for the pass or fail of the trial.
        - EnableExtraIterations (bool): If true, more iterations are performed.
        - EnableFastConvergence (bool): If true, the test perform iterations using the fast convergence duration configured.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableOldStatsForReef (bool): If true, enables old statistics for reef load module.
        - EnableSaturationIteration (bool): If true, enables the test to run an extra iteration for calculating the Saturation Latency.
        - EnableStopTestOnHighLoss (bool): The test stops in case of a high loss.
        - ExtraIterationOffsets (str): This enables the test to run an extra iteration.
        - FastConvergenceDuration (number): This enables the test to perform iterations using the fast convergence duration configured.
        - FastConvergenceThreshold (number): This enables the test to perform iterations using the fast convergence threshold configured.
        - FixedIteration (number): NOT DEFINED
        - FixedLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The fixed load unit.
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameLossUnit (str): Frame loss measurement unit.
        - FramesPerBurstGap (number): The number of frames to be sent after each burst.
        - Framesize (str): The frame size to be used.
        - FramesizeFixedValue (number): The fixed value of frame size.
        - FramesizeList (list(str)): The list of the available frame sizes.
        - Gap (number): The gap in transmission of frames.
        - GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The unit increment for the load.
        - InitialIncrementLoadRate (number): The initial incremental value of the load rate.
        - InitialStepLoadRate (number): The initial step value of the load rate.
        - Ipv4rate (number): The rate at which IPv4 traffic is sent.
        - Ipv6rate (number): The rate at which IPv6 traffic is sent.
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LatencyType (str(cutThrough | storeForward)): The type of latency.
        - LoadRateList (str): Enters the Load Rate List.
        - LoadRateValue (number): The value of the load rate.
        - LoadType (str(dynamic | step | timeline)): The type of the payload setting.
        - MapType (str): The mapping type.
        - MaxIncrementLoadRate (number): The maximum incremental value of the load rate.
        - MaxRandomLoadRate (number): The maximum random value of the load rate.
        - MaxStepLoadRate (number): The maximum step value of the load rate.
        - MinFpsRate (number): The rate at which minimum frames are sent per second.
        - MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
        - MinRandomLoadRate (number): The minimum random value of the load rate.
        - Numtrials (number): The integer value that states the number of trials permitted.
        - PercentMaxRate (number): The rate selected in percentMax.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - RandomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The random values of the load unit.
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): The rate selected.
        - ReportSequenceError (bool): Reports sequence errors in the test result.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The unit of rate for throughput.
        - Resolution (number): Specify the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
        - Rfc2889ordering (str(noOrdering | unchanged | val2889Ordering)): If true, indicates frame ordering by Rfc2889.
        - SaturationIteration (number): This enables the test to run an extra iteration for calculating the Saturation latency.
        - SkipDefaultPassFailEvaluation (bool): If true, it skips the default pass fail evaluation.
        - StaggeredStart (bool): Starts test with a stagger.
        - StepFrameLossUnit (str(%)): Signifies the step frame loss unit.
        - StepIncrementLoadRate (number): The step incremental value of the load rate.
        - StepLoadUnit (str(percentMaxRate)): Specifies the step rate of the load unit.
        - StepStepLoadRate (number): The incremental step value of load rate.
        - StepTolerance (number): The step value of the tolerance level.
        - StopTestOnHighLoss (number): It stops test on high loss.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TestTrafficType (str): It signifies the test traffic type value.
        - TimelineRateList (str): NOT DEFINED
        - Tolerance (number): The value set for the tolerance level.
        - TxDelay (number): Specifies the amount of delay after every transmit.
        - UsePercentOffsets (str): If true, sets the offset value in percentage.

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
