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
        "BinaryBackoff": "binaryBackoff",
        "BinaryFrameLossUnit": "binaryFrameLossUnit",
        "BinaryLoadUnit": "binaryLoadUnit",
        "BinaryResolution": "binaryResolution",
        "BinarySearchType": "binarySearchType",
        "BinaryTolerance": "binaryTolerance",
        "BurstSize": "burstSize",
        "CalculateJitter": "calculateJitter",
        "CalculateLatency": "calculateLatency",
        "ComboBackoff": "comboBackoff",
        "ComboFrameLossUnit": "comboFrameLossUnit",
        "ComboLoadUnit": "comboLoadUnit",
        "ComboResolution": "comboResolution",
        "ComboTolerance": "comboTolerance",
        "CountRandomFrameSize": "countRandomFrameSize",
        "CountRandomLoadRate": "countRandomLoadRate",
        "CustomLoadUnit": "customLoadUnit",
        "DelayAfterTransmit": "delayAfterTransmit",
        "DisableInheritedImix": "disableInheritedImix",
        "Duration": "duration",
        "EnableBackoffIteration": "enableBackoffIteration",
        "EnableDataIntegrity": "enableDataIntegrity",
        "EnableExtraIterations": "enableExtraIterations",
        "EnableFastConvergence": "enableFastConvergence",
        "EnableLayer1Rate": "enableLayer1Rate",
        "EnableMinFrameSize": "enableMinFrameSize",
        "EnableSaturationIteration": "enableSaturationIteration",
        "EnableStopTestOnHighLoss": "enableStopTestOnHighLoss",
        "ExtraIterationOffsets": "extraIterationOffsets",
        "FastConvergenceDuration": "fastConvergenceDuration",
        "FastConvergenceThreshold": "fastConvergenceThreshold",
        "FixedFramesize": "fixedFramesize",
        "FixedLoadUnit": "fixedLoadUnit",
        "FixedRate": "fixedRate",
        "ForceRegenerate": "forceRegenerate",
        "FrameLossUnit": "frameLossUnit",
        "FrameSizeMode": "frameSizeMode",
        "FramesPerBurstGap": "framesPerBurstGap",
        "Framesize": "framesize",
        "FramesizeFixedValue": "framesizeFixedValue",
        "FramesizeImixList": "framesizeImixList",
        "FramesizeList": "framesizeList",
        "Gap": "gap",
        "GenerateTrackingOptionAggregationFiles": "generateTrackingOptionAggregationFiles",
        "ImixAdd": "imixAdd",
        "ImixData": "imixData",
        "ImixDelete": "imixDelete",
        "ImixDistribution": "imixDistribution",
        "ImixEnabled": "imixEnabled",
        "ImixTemplates": "imixTemplates",
        "ImixTrafficType": "imixTrafficType",
        "IncrementLoadUnit": "incrementLoadUnit",
        "InitialBinaryLoadRate": "initialBinaryLoadRate",
        "InitialComboLoadRate": "initialComboLoadRate",
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
        "MaxBinaryLoadRate": "maxBinaryLoadRate",
        "MaxComboLoadRate": "maxComboLoadRate",
        "MaxFramesize": "maxFramesize",
        "MaxIncrementFrameSize": "maxIncrementFrameSize",
        "MaxIncrementLoadRate": "maxIncrementLoadRate",
        "MaxRandomFrameSize": "maxRandomFrameSize",
        "MaxRandomLoadRate": "maxRandomLoadRate",
        "MaxRate": "maxRate",
        "MaxStepLoadRate": "maxStepLoadRate",
        "MinBinaryLoadRate": "minBinaryLoadRate",
        "MinComboLoadRate": "minComboLoadRate",
        "MinFpsRate": "minFpsRate",
        "MinFramesize": "minFramesize",
        "MinIncrementFrameSize": "minIncrementFrameSize",
        "MinKbpsRate": "minKbpsRate",
        "MinRandomFrameSize": "minRandomFrameSize",
        "MinRandomLoadRate": "minRandomLoadRate",
        "MinRate": "minRate",
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
        "SaturationIteration": "saturationIteration",
        "StaggeredStart": "staggeredStart",
        "StepComboLoadRate": "stepComboLoadRate",
        "StepFrameLossUnit": "stepFrameLossUnit",
        "StepIncrementFrameSize": "stepIncrementFrameSize",
        "StepIncrementLoadRate": "stepIncrementLoadRate",
        "StepLoadUnit": "stepLoadUnit",
        "StepStepLoadRate": "stepStepLoadRate",
        "StepTolerance": "stepTolerance",
        "StopTestOnHighLoss": "stopTestOnHighLoss",
        "Tolerance": "tolerance",
        "TrafficType": "trafficType",
        "TxDelay": "txDelay",
        "UnchangedInitial": "unchangedInitial",
        "UnchangedValueList": "unchangedValueList",
        "UsePercentOffsets": "usePercentOffsets",
    }
    _SDM_ENUM_MAP = {
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
        "binarySearchType": ["linear", "perFlow", "perPort", "perTrafficItem"],
        "comboFrameLossUnit": ["%", "frames"],
        "comboLoadUnit": [
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
        "customLoadUnit": [
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
        "frameSizeMode": ["custom", "fixed", "increment", "random", "unchanged"],
        "imixDistribution": ["bwpercentage", "weight"],
        "imixTemplates": [
            "cisco",
            "imix",
            "ipsec",
            "ipv6",
            "none",
            "quadmodal",
            "standard",
            "tcp",
            "tolly",
            "trimodal",
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
        "loadType": ["custom", "fixed", "increment", "random", "unchanged"],
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
        "trafficType": ["burstyLoading", "constantLoading"],
        "unchangedInitial": ["False", "True"],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

    @property
    def BackoffIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The rate of iteration for the backoff.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BackoffIteration"])

    @BackoffIteration.setter
    def BackoffIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BackoffIteration"], value)

    @property
    def BinaryBackoff(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The binary search interval through which the next iteration's rate is obtained.
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
        - str(% | frames): It signifies the binary frame loss unit value.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the binary load unit.
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
        - number: Binary resolution of the test configuration.
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
        - str(linear | perFlow | perPort | perTrafficItem): It signifies the binary search type value.
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
        - number: It signifies the binary tolerance value.
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
        - number: The number of packets to send in a burst.
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
        - bool: If true, calculates latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CalculateLatency"])

    @CalculateLatency.setter
    def CalculateLatency(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CalculateLatency"], value)

    @property
    def ComboBackoff(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The backoff combination of the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ComboBackoff"])

    @ComboBackoff.setter
    def ComboBackoff(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ComboBackoff"], value)

    @property
    def ComboFrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(% | frames): It signifies the combo frame loss unit value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ComboFrameLossUnit"])

    @ComboFrameLossUnit.setter
    def ComboFrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ComboFrameLossUnit"], value)

    @property
    def ComboLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the combo load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ComboLoadUnit"])

    @ComboLoadUnit.setter
    def ComboLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ComboLoadUnit"], value)

    @property
    def ComboResolution(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Combo resolution of the test configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ComboResolution"])

    @ComboResolution.setter
    def ComboResolution(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ComboResolution"], value)

    @property
    def ComboTolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the combo tolerance value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ComboTolerance"])

    @ComboTolerance.setter
    def ComboTolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ComboTolerance"], value)

    @property
    def CountRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the count of random frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CountRandomFrameSize"])

    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CountRandomFrameSize"], value)

    @property
    def CountRandomLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the count of random load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CountRandomLoadRate"])

    @CountRandomLoadRate.setter
    def CountRandomLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CountRandomLoadRate"], value)

    @property
    def CustomLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the custom load unit.
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
        - number: It signifies the delay value after transmission.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"])

    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"], value)

    @property
    def DisableInheritedImix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Disabled inherited imix.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisableInheritedImix"])

    @DisableInheritedImix.setter
    def DisableInheritedImix(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisableInheritedImix"], value)

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
    def EnableBackoffIteration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables back of iteration.
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
        - bool: If true, enables data integrity.
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
        - bool: If true, enables extra iterations.
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
        - bool: If true, enables fast convergence.
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
    def EnableSaturationIteration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the test to run an extra iteration for calculating the SaturationLatency.
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
        - bool: If true, stops test on high loss.
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
        - str: It signifies extra offset alteration.
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
        - number: It signifies the fast convergence duration.
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
        - number: It signifies the fast convergence threshold.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastConvergenceThreshold"])

    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastConvergenceThreshold"], value)

    @property
    def FixedFramesize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Bytes
        """
        return self._get_attribute(self._SDM_ATT_MAP["FixedFramesize"])

    @FixedFramesize.setter
    def FixedFramesize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FixedFramesize"], value)

    @property
    def FixedLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the fixed load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FixedLoadUnit"])

    @FixedLoadUnit.setter
    def FixedLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FixedLoadUnit"], value)

    @property
    def FixedRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the fixed rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FixedRate"])

    @FixedRate.setter
    def FixedRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FixedRate"], value)

    @property
    def ForceRegenerate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, regenerates force.
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
        - str: Specifies frame loss unit value.
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
        - str(custom | fixed | increment | random | unchanged): Specifies the framesize mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameSizeMode"])

    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameSizeMode"], value)

    @property
    def FramesPerBurstGap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the frames per burst gap.
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
        - str: It signifies the frame size.
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
        - number: It signifies the framesize fixed value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesizeFixedValue"])

    @FramesizeFixedValue.setter
    def FramesizeFixedValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesizeFixedValue"], value)

    @property
    def FramesizeImixList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the framesize IMIX list.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesizeImixList"])

    @FramesizeImixList.setter
    def FramesizeImixList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesizeImixList"], value)

    @property
    def FramesizeList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Signifies the framesize list.
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
        - number: Specifies the gap value.
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
        - bool: If enabled, it generates the tracking option for aggregation files.
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
    def ImixAdd(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the IMIX address value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImixAdd"])

    @ImixAdd.setter
    def ImixAdd(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ImixAdd"], value)

    @property
    def ImixData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the IMIX data.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImixData"])

    @ImixData.setter
    def ImixData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ImixData"], value)

    @property
    def ImixDelete(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the IMIX deleted value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImixDelete"])

    @ImixDelete.setter
    def ImixDelete(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ImixDelete"], value)

    @property
    def ImixDistribution(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bwpercentage | weight): Signifies the IMIX distribution value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImixDistribution"])

    @ImixDistribution.setter
    def ImixDistribution(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ImixDistribution"], value)

    @property
    def ImixEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables IMIX.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImixEnabled"])

    @ImixEnabled.setter
    def ImixEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ImixEnabled"], value)

    @property
    def ImixTemplates(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal): Specifies IMIX templates.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImixTemplates"])

    @ImixTemplates.setter
    def ImixTemplates(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ImixTemplates"], value)

    @property
    def ImixTrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the traffic type of IMIX.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImixTrafficType"])

    @ImixTrafficType.setter
    def ImixTrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ImixTrafficType"], value)

    @property
    def IncrementLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies incremented value for load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementLoadUnit"])

    @IncrementLoadUnit.setter
    def IncrementLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementLoadUnit"], value)

    @property
    def InitialBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the initial binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialBinaryLoadRate"])

    @InitialBinaryLoadRate.setter
    def InitialBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialBinaryLoadRate"], value)

    @property
    def InitialComboLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the initial load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialComboLoadRate"])

    @InitialComboLoadRate.setter
    def InitialComboLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialComboLoadRate"], value)

    @property
    def InitialIncrementLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the initial increment value for load rate.
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
        - number: It signifies the initial step load rate.
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
        - number: Internet Protocol version 4 rate.
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
        - number: Internet Protocol version 6 rate.
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
        - str(cutThrough | storeForward): It signifies the latency type.
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
        - str: Signifies the load rate list.
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
        - number: Specifies the load rate value.
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
        - str(custom | fixed | increment | random | unchanged): Signifies the load type value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadType"])

    @LoadType.setter
    def LoadType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadType"], value)

    @property
    def MaxBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the maximum binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxBinaryLoadRate"])

    @MaxBinaryLoadRate.setter
    def MaxBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxBinaryLoadRate"], value)

    @property
    def MaxComboLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the maximum combo load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxComboLoadRate"])

    @MaxComboLoadRate.setter
    def MaxComboLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxComboLoadRate"], value)

    @property
    def MaxFramesize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Bytes
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxFramesize"])

    @MaxFramesize.setter
    def MaxFramesize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxFramesize"], value)

    @property
    def MaxIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the maximum increment framesize.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxIncrementFrameSize"])

    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxIncrementFrameSize"], value)

    @property
    def MaxIncrementLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the maximum increment of load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxIncrementLoadRate"])

    @MaxIncrementLoadRate.setter
    def MaxIncrementLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxIncrementLoadRate"], value)

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
    def MaxRandomLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum random load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxRandomLoadRate"])

    @MaxRandomLoadRate.setter
    def MaxRandomLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxRandomLoadRate"], value)

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
    def MinComboLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum combo load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinComboLoadRate"])

    @MinComboLoadRate.setter
    def MinComboLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinComboLoadRate"], value)

    @property
    def MinFpsRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the minimum FPS rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinFpsRate"])

    @MinFpsRate.setter
    def MinFpsRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinFpsRate"], value)

    @property
    def MinFramesize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Bytes
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinFramesize"])

    @MinFramesize.setter
    def MinFramesize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinFramesize"], value)

    @property
    def MinIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the minimum incremental value framesize.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinIncrementFrameSize"])

    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinIncrementFrameSize"], value)

    @property
    def MinKbpsRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies minimum KBPS rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinKbpsRate"])

    @MinKbpsRate.setter
    def MinKbpsRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinKbpsRate"], value)

    @property
    def MinRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the minimum random framesize.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRandomFrameSize"])

    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRandomFrameSize"], value)

    @property
    def MinRandomLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the minimum random load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRandomLoadRate"])

    @MinRandomLoadRate.setter
    def MinRandomLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRandomLoadRate"], value)

    @property
    def MinRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the minimum rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRate"])

    @MinRate.setter
    def MinRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRate"], value)

    @property
    def Numtrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the number of trials.
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
        - number: Signifies the maximum percent of rates.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the random load rate.
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
        - str(fpsRate | kbpsRate | percentMaxRate): Specifies the selected rate.
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
        - bool: If true, reports sequence error.
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
        - str(gbps | gBps | kbps | kBps | mbps | mBps): Specifies the TPUT rate unit report.
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
        - number: Specify the resolution of the iteration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Resolution"])

    @Resolution.setter
    def Resolution(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Resolution"], value)

    @property
    def SaturationIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the saturation level of iteration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SaturationIteration"])

    @SaturationIteration.setter
    def SaturationIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SaturationIteration"], value)

    @property
    def StaggeredStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, transmit start is staggered; if false, transmit starts on all ports at the same time.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StaggeredStart"])

    @StaggeredStart.setter
    def StaggeredStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StaggeredStart"], value)

    @property
    def StepComboLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the step combo load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepComboLoadRate"])

    @StepComboLoadRate.setter
    def StepComboLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepComboLoadRate"], value)

    @property
    def StepFrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(% | frames): Specifies the step frame loss unit.
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
        - number: Specifies the incremental value of frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepIncrementFrameSize"])

    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepIncrementFrameSize"], value)

    @property
    def StepIncrementLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the incremental value for load rate.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies the step load unit.
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
        - number: Signifies the step load rate.
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
        - number: Stops tolerance value.
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
        - number: The test stops in case of a high loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StopTestOnHighLoss"])

    @StopTestOnHighLoss.setter
    def StopTestOnHighLoss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StopTestOnHighLoss"], value)

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
    def TrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(burstyLoading | constantLoading): Specifies the traffic type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficType"])

    @TrafficType.setter
    def TrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficType"], value)

    @property
    def TxDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the transmission delay time.
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
        - str(False | True): Specifies the unchanged initial value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnchangedInitial"])

    @UnchangedInitial.setter
    def UnchangedInitial(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnchangedInitial"], value)

    @property
    def UnchangedValueList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the unchanged value list.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnchangedValueList"])

    @UnchangedValueList.setter
    def UnchangedValueList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnchangedValueList"], value)

    @property
    def UsePercentOffsets(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It uses percent offsets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UsePercentOffsets"])

    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UsePercentOffsets"], value)

    def update(
        self,
        BackoffIteration=None,
        BinaryBackoff=None,
        BinaryFrameLossUnit=None,
        BinaryLoadUnit=None,
        BinaryResolution=None,
        BinarySearchType=None,
        BinaryTolerance=None,
        BurstSize=None,
        CalculateJitter=None,
        CalculateLatency=None,
        ComboBackoff=None,
        ComboFrameLossUnit=None,
        ComboLoadUnit=None,
        ComboResolution=None,
        ComboTolerance=None,
        CountRandomFrameSize=None,
        CountRandomLoadRate=None,
        CustomLoadUnit=None,
        DelayAfterTransmit=None,
        DisableInheritedImix=None,
        Duration=None,
        EnableBackoffIteration=None,
        EnableDataIntegrity=None,
        EnableExtraIterations=None,
        EnableFastConvergence=None,
        EnableLayer1Rate=None,
        EnableMinFrameSize=None,
        EnableSaturationIteration=None,
        EnableStopTestOnHighLoss=None,
        ExtraIterationOffsets=None,
        FastConvergenceDuration=None,
        FastConvergenceThreshold=None,
        FixedFramesize=None,
        FixedLoadUnit=None,
        FixedRate=None,
        ForceRegenerate=None,
        FrameLossUnit=None,
        FrameSizeMode=None,
        FramesPerBurstGap=None,
        Framesize=None,
        FramesizeFixedValue=None,
        FramesizeImixList=None,
        FramesizeList=None,
        Gap=None,
        GenerateTrackingOptionAggregationFiles=None,
        ImixAdd=None,
        ImixData=None,
        ImixDelete=None,
        ImixDistribution=None,
        ImixEnabled=None,
        ImixTemplates=None,
        ImixTrafficType=None,
        IncrementLoadUnit=None,
        InitialBinaryLoadRate=None,
        InitialComboLoadRate=None,
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
        MaxBinaryLoadRate=None,
        MaxComboLoadRate=None,
        MaxFramesize=None,
        MaxIncrementFrameSize=None,
        MaxIncrementLoadRate=None,
        MaxRandomFrameSize=None,
        MaxRandomLoadRate=None,
        MaxRate=None,
        MaxStepLoadRate=None,
        MinBinaryLoadRate=None,
        MinComboLoadRate=None,
        MinFpsRate=None,
        MinFramesize=None,
        MinIncrementFrameSize=None,
        MinKbpsRate=None,
        MinRandomFrameSize=None,
        MinRandomLoadRate=None,
        MinRate=None,
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
        SaturationIteration=None,
        StaggeredStart=None,
        StepComboLoadRate=None,
        StepFrameLossUnit=None,
        StepIncrementFrameSize=None,
        StepIncrementLoadRate=None,
        StepLoadUnit=None,
        StepStepLoadRate=None,
        StepTolerance=None,
        StopTestOnHighLoss=None,
        Tolerance=None,
        TrafficType=None,
        TxDelay=None,
        UnchangedInitial=None,
        UnchangedValueList=None,
        UsePercentOffsets=None,
    ):
        # type: (int, int, str, str, int, str, int, int, bool, bool, int, str, str, int, int, int, int, str, int, str, int, bool, bool, bool, bool, bool, bool, bool, bool, str, int, int, int, str, int, bool, str, str, int, str, int, str, List[str], int, bool, str, str, str, str, bool, str, str, str, int, int, int, int, int, int, str, bool, str, str, int, str, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, bool, str, int, List[str], str, str, bool, str, int, int, bool, int, str, int, int, str, int, int, int, int, str, int, str, str, str) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - BackoffIteration (number): The rate of iteration for the backoff.
        - BinaryBackoff (number): The binary search interval through which the next iteration's rate is obtained.
        - BinaryFrameLossUnit (str(% | frames)): It signifies the binary frame loss unit value.
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the binary load unit.
        - BinaryResolution (number): Binary resolution of the test configuration.
        - BinarySearchType (str(linear | perFlow | perPort | perTrafficItem)): It signifies the binary search type value.
        - BinaryTolerance (number): It signifies the binary tolerance value.
        - BurstSize (number): The number of packets to send in a burst.
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calculates latency.
        - ComboBackoff (number): The backoff combination of the test configuration.
        - ComboFrameLossUnit (str(% | frames)): It signifies the combo frame loss unit value.
        - ComboLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the combo load unit.
        - ComboResolution (number): Combo resolution of the test configuration.
        - ComboTolerance (number): It signifies the combo tolerance value.
        - CountRandomFrameSize (number): It signifies the count of random frame size.
        - CountRandomLoadRate (number): It signifies the count of random load rate.
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the custom load unit.
        - DelayAfterTransmit (number): It signifies the delay value after transmission.
        - DisableInheritedImix (str): Disabled inherited imix.
        - Duration (number): sec
        - EnableBackoffIteration (bool): If true, enables back of iteration.
        - EnableDataIntegrity (bool): If true, enables data integrity.
        - EnableExtraIterations (bool): If true, enables extra iterations.
        - EnableFastConvergence (bool): If true, enables fast convergence.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableSaturationIteration (bool): If true, enables the test to run an extra iteration for calculating the SaturationLatency.
        - EnableStopTestOnHighLoss (bool): If true, stops test on high loss.
        - ExtraIterationOffsets (str): It signifies extra offset alteration.
        - FastConvergenceDuration (number): It signifies the fast convergence duration.
        - FastConvergenceThreshold (number): It signifies the fast convergence threshold.
        - FixedFramesize (number): Bytes
        - FixedLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the fixed load unit.
        - FixedRate (number): Specifies the fixed rate.
        - ForceRegenerate (bool): If true, regenerates force.
        - FrameLossUnit (str): Specifies frame loss unit value.
        - FrameSizeMode (str(custom | fixed | increment | random | unchanged)): Specifies the framesize mode.
        - FramesPerBurstGap (number): Specifies the frames per burst gap.
        - Framesize (str): It signifies the frame size.
        - FramesizeFixedValue (number): It signifies the framesize fixed value.
        - FramesizeImixList (str): Specifies the framesize IMIX list.
        - FramesizeList (list(str)): Signifies the framesize list.
        - Gap (number): Specifies the gap value.
        - GenerateTrackingOptionAggregationFiles (bool): If enabled, it generates the tracking option for aggregation files.
        - ImixAdd (str): It signifies the IMIX address value.
        - ImixData (str): Specifies the IMIX data.
        - ImixDelete (str): Specifies the IMIX deleted value.
        - ImixDistribution (str(bwpercentage | weight)): Signifies the IMIX distribution value.
        - ImixEnabled (bool): If true, enables IMIX.
        - ImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Specifies IMIX templates.
        - ImixTrafficType (str): Specifies the traffic type of IMIX.
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies incremented value for load unit.
        - InitialBinaryLoadRate (number): It signifies the initial binary load rate.
        - InitialComboLoadRate (number): Specifies the initial load rate.
        - InitialIncrementLoadRate (number): It signifies the initial increment value for load rate.
        - InitialStepLoadRate (number): It signifies the initial step load rate.
        - Ipv4rate (number): Internet Protocol version 4 rate.
        - Ipv6rate (number): Internet Protocol version 6 rate.
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LatencyType (str(cutThrough | storeForward)): It signifies the latency type.
        - LoadRateList (str): Signifies the load rate list.
        - LoadRateValue (number): Specifies the load rate value.
        - LoadType (str(custom | fixed | increment | random | unchanged)): Signifies the load type value.
        - MaxBinaryLoadRate (number): Specifies the maximum binary load rate.
        - MaxComboLoadRate (number): Signifies the maximum combo load rate.
        - MaxFramesize (number): Bytes
        - MaxIncrementFrameSize (number): Specifies the maximum increment framesize.
        - MaxIncrementLoadRate (number): Specifies the maximum increment of load rate.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxRandomLoadRate (number): The maximum random load rate.
        - MaxRate (number): The maximum rate.
        - MaxStepLoadRate (number): The maximum step load rate.
        - MinBinaryLoadRate (number): The minimum binary load rate.
        - MinComboLoadRate (number): The minimum combo load rate.
        - MinFpsRate (number): Specifies the minimum FPS rate.
        - MinFramesize (number): Bytes
        - MinIncrementFrameSize (number): Specifies the minimum incremental value framesize.
        - MinKbpsRate (number): Specifies minimum KBPS rate.
        - MinRandomFrameSize (number): Specifies the minimum random framesize.
        - MinRandomLoadRate (number): Specifies the minimum random load rate.
        - MinRate (number): Specifies the minimum rate.
        - Numtrials (number): Signifies the number of trials.
        - PercentMaxRate (number): Signifies the maximum percent of rates.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - RandomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the random load rate.
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): Specifies the selected rate.
        - ReportSequenceError (bool): If true, reports sequence error.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): Specifies the TPUT rate unit report.
        - Resolution (number): Specify the resolution of the iteration.
        - SaturationIteration (number): Specifies the saturation level of iteration.
        - StaggeredStart (bool): If true, transmit start is staggered; if false, transmit starts on all ports at the same time.
        - StepComboLoadRate (number): Signifies the step combo load rate.
        - StepFrameLossUnit (str(% | frames)): Specifies the step frame loss unit.
        - StepIncrementFrameSize (number): Specifies the incremental value of frame size.
        - StepIncrementLoadRate (number): Specifies the incremental value for load rate.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the step load unit.
        - StepStepLoadRate (number): Signifies the step load rate.
        - StepTolerance (number): Stops tolerance value.
        - StopTestOnHighLoss (number): The test stops in case of a high loss.
        - Tolerance (number): The value set for the tolerance level.
        - TrafficType (str(burstyLoading | constantLoading)): Specifies the traffic type.
        - TxDelay (number): Signifies the transmission delay time.
        - UnchangedInitial (str(False | True)): Specifies the unchanged initial value.
        - UnchangedValueList (str): Specifies the unchanged value list.
        - UsePercentOffsets (str): It uses percent offsets.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BackoffIteration=None,
        BinaryBackoff=None,
        BinaryFrameLossUnit=None,
        BinaryLoadUnit=None,
        BinaryResolution=None,
        BinarySearchType=None,
        BinaryTolerance=None,
        BurstSize=None,
        CalculateJitter=None,
        CalculateLatency=None,
        ComboBackoff=None,
        ComboFrameLossUnit=None,
        ComboLoadUnit=None,
        ComboResolution=None,
        ComboTolerance=None,
        CountRandomFrameSize=None,
        CountRandomLoadRate=None,
        CustomLoadUnit=None,
        DelayAfterTransmit=None,
        DisableInheritedImix=None,
        Duration=None,
        EnableBackoffIteration=None,
        EnableDataIntegrity=None,
        EnableExtraIterations=None,
        EnableFastConvergence=None,
        EnableLayer1Rate=None,
        EnableMinFrameSize=None,
        EnableSaturationIteration=None,
        EnableStopTestOnHighLoss=None,
        ExtraIterationOffsets=None,
        FastConvergenceDuration=None,
        FastConvergenceThreshold=None,
        FixedFramesize=None,
        FixedLoadUnit=None,
        FixedRate=None,
        ForceRegenerate=None,
        FrameLossUnit=None,
        FrameSizeMode=None,
        FramesPerBurstGap=None,
        Framesize=None,
        FramesizeFixedValue=None,
        FramesizeImixList=None,
        FramesizeList=None,
        Gap=None,
        GenerateTrackingOptionAggregationFiles=None,
        ImixAdd=None,
        ImixData=None,
        ImixDelete=None,
        ImixDistribution=None,
        ImixEnabled=None,
        ImixTemplates=None,
        ImixTrafficType=None,
        IncrementLoadUnit=None,
        InitialBinaryLoadRate=None,
        InitialComboLoadRate=None,
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
        MaxBinaryLoadRate=None,
        MaxComboLoadRate=None,
        MaxFramesize=None,
        MaxIncrementFrameSize=None,
        MaxIncrementLoadRate=None,
        MaxRandomFrameSize=None,
        MaxRandomLoadRate=None,
        MaxRate=None,
        MaxStepLoadRate=None,
        MinBinaryLoadRate=None,
        MinComboLoadRate=None,
        MinFpsRate=None,
        MinFramesize=None,
        MinIncrementFrameSize=None,
        MinKbpsRate=None,
        MinRandomFrameSize=None,
        MinRandomLoadRate=None,
        MinRate=None,
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
        SaturationIteration=None,
        StaggeredStart=None,
        StepComboLoadRate=None,
        StepFrameLossUnit=None,
        StepIncrementFrameSize=None,
        StepIncrementLoadRate=None,
        StepLoadUnit=None,
        StepStepLoadRate=None,
        StepTolerance=None,
        StopTestOnHighLoss=None,
        Tolerance=None,
        TrafficType=None,
        TxDelay=None,
        UnchangedInitial=None,
        UnchangedValueList=None,
        UsePercentOffsets=None,
    ):
        # type: (int, int, str, str, int, str, int, int, bool, bool, int, str, str, int, int, int, int, str, int, str, int, bool, bool, bool, bool, bool, bool, bool, bool, str, int, int, int, str, int, bool, str, str, int, str, int, str, List[str], int, bool, str, str, str, str, bool, str, str, str, int, int, int, int, int, int, str, bool, str, str, int, str, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, bool, str, int, List[str], str, str, bool, str, int, int, bool, int, str, int, int, str, int, int, int, int, str, int, str, str, str) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - BackoffIteration (number): The rate of iteration for the backoff.
        - BinaryBackoff (number): The binary search interval through which the next iteration's rate is obtained.
        - BinaryFrameLossUnit (str(% | frames)): It signifies the binary frame loss unit value.
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the binary load unit.
        - BinaryResolution (number): Binary resolution of the test configuration.
        - BinarySearchType (str(linear | perFlow | perPort | perTrafficItem)): It signifies the binary search type value.
        - BinaryTolerance (number): It signifies the binary tolerance value.
        - BurstSize (number): The number of packets to send in a burst.
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calculates latency.
        - ComboBackoff (number): The backoff combination of the test configuration.
        - ComboFrameLossUnit (str(% | frames)): It signifies the combo frame loss unit value.
        - ComboLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the combo load unit.
        - ComboResolution (number): Combo resolution of the test configuration.
        - ComboTolerance (number): It signifies the combo tolerance value.
        - CountRandomFrameSize (number): It signifies the count of random frame size.
        - CountRandomLoadRate (number): It signifies the count of random load rate.
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the custom load unit.
        - DelayAfterTransmit (number): It signifies the delay value after transmission.
        - DisableInheritedImix (str): Disabled inherited imix.
        - Duration (number): sec
        - EnableBackoffIteration (bool): If true, enables back of iteration.
        - EnableDataIntegrity (bool): If true, enables data integrity.
        - EnableExtraIterations (bool): If true, enables extra iterations.
        - EnableFastConvergence (bool): If true, enables fast convergence.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableSaturationIteration (bool): If true, enables the test to run an extra iteration for calculating the SaturationLatency.
        - EnableStopTestOnHighLoss (bool): If true, stops test on high loss.
        - ExtraIterationOffsets (str): It signifies extra offset alteration.
        - FastConvergenceDuration (number): It signifies the fast convergence duration.
        - FastConvergenceThreshold (number): It signifies the fast convergence threshold.
        - FixedFramesize (number): Bytes
        - FixedLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the fixed load unit.
        - FixedRate (number): Specifies the fixed rate.
        - ForceRegenerate (bool): If true, regenerates force.
        - FrameLossUnit (str): Specifies frame loss unit value.
        - FrameSizeMode (str(custom | fixed | increment | random | unchanged)): Specifies the framesize mode.
        - FramesPerBurstGap (number): Specifies the frames per burst gap.
        - Framesize (str): It signifies the frame size.
        - FramesizeFixedValue (number): It signifies the framesize fixed value.
        - FramesizeImixList (str): Specifies the framesize IMIX list.
        - FramesizeList (list(str)): Signifies the framesize list.
        - Gap (number): Specifies the gap value.
        - GenerateTrackingOptionAggregationFiles (bool): If enabled, it generates the tracking option for aggregation files.
        - ImixAdd (str): It signifies the IMIX address value.
        - ImixData (str): Specifies the IMIX data.
        - ImixDelete (str): Specifies the IMIX deleted value.
        - ImixDistribution (str(bwpercentage | weight)): Signifies the IMIX distribution value.
        - ImixEnabled (bool): If true, enables IMIX.
        - ImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Specifies IMIX templates.
        - ImixTrafficType (str): Specifies the traffic type of IMIX.
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies incremented value for load unit.
        - InitialBinaryLoadRate (number): It signifies the initial binary load rate.
        - InitialComboLoadRate (number): Specifies the initial load rate.
        - InitialIncrementLoadRate (number): It signifies the initial increment value for load rate.
        - InitialStepLoadRate (number): It signifies the initial step load rate.
        - Ipv4rate (number): Internet Protocol version 4 rate.
        - Ipv6rate (number): Internet Protocol version 6 rate.
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LatencyType (str(cutThrough | storeForward)): It signifies the latency type.
        - LoadRateList (str): Signifies the load rate list.
        - LoadRateValue (number): Specifies the load rate value.
        - LoadType (str(custom | fixed | increment | random | unchanged)): Signifies the load type value.
        - MaxBinaryLoadRate (number): Specifies the maximum binary load rate.
        - MaxComboLoadRate (number): Signifies the maximum combo load rate.
        - MaxFramesize (number): Bytes
        - MaxIncrementFrameSize (number): Specifies the maximum increment framesize.
        - MaxIncrementLoadRate (number): Specifies the maximum increment of load rate.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxRandomLoadRate (number): The maximum random load rate.
        - MaxRate (number): The maximum rate.
        - MaxStepLoadRate (number): The maximum step load rate.
        - MinBinaryLoadRate (number): The minimum binary load rate.
        - MinComboLoadRate (number): The minimum combo load rate.
        - MinFpsRate (number): Specifies the minimum FPS rate.
        - MinFramesize (number): Bytes
        - MinIncrementFrameSize (number): Specifies the minimum incremental value framesize.
        - MinKbpsRate (number): Specifies minimum KBPS rate.
        - MinRandomFrameSize (number): Specifies the minimum random framesize.
        - MinRandomLoadRate (number): Specifies the minimum random load rate.
        - MinRate (number): Specifies the minimum rate.
        - Numtrials (number): Signifies the number of trials.
        - PercentMaxRate (number): Signifies the maximum percent of rates.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - RandomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the random load rate.
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): Specifies the selected rate.
        - ReportSequenceError (bool): If true, reports sequence error.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): Specifies the TPUT rate unit report.
        - Resolution (number): Specify the resolution of the iteration.
        - SaturationIteration (number): Specifies the saturation level of iteration.
        - StaggeredStart (bool): If true, transmit start is staggered; if false, transmit starts on all ports at the same time.
        - StepComboLoadRate (number): Signifies the step combo load rate.
        - StepFrameLossUnit (str(% | frames)): Specifies the step frame loss unit.
        - StepIncrementFrameSize (number): Specifies the incremental value of frame size.
        - StepIncrementLoadRate (number): Specifies the incremental value for load rate.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies the step load unit.
        - StepStepLoadRate (number): Signifies the step load rate.
        - StepTolerance (number): Stops tolerance value.
        - StopTestOnHighLoss (number): The test stops in case of a high loss.
        - Tolerance (number): The value set for the tolerance level.
        - TrafficType (str(burstyLoading | constantLoading)): Specifies the traffic type.
        - TxDelay (number): Signifies the transmission delay time.
        - UnchangedInitial (str(False | True)): Specifies the unchanged initial value.
        - UnchangedValueList (str): Specifies the unchanged value list.
        - UsePercentOffsets (str): It uses percent offsets.

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
