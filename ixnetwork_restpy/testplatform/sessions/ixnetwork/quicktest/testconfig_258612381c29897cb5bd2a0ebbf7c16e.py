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
    """signifies the test configuration.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "testConfig"
    _SDM_ATT_MAP = {
        "AggregateByDirection": "aggregateByDirection",
        "AggregateByFlowgroup": "aggregateByFlowgroup",
        "AggregateByPort": "aggregateByPort",
        "BackoffIteration": "backoffIteration",
        "BinaryAcceptableFrameLossLabel": "binaryAcceptableFrameLossLabel",
        "BinaryBackoffLabel": "binaryBackoffLabel",
        "BinaryInitialRateLabel": "binaryInitialRateLabel",
        "BinaryLoadUnitLabel": "binaryLoadUnitLabel",
        "BinaryMaxRateLabel": "binaryMaxRateLabel",
        "BinaryMinRateLabel": "binaryMinRateLabel",
        "BinaryResolutionLabel": "binaryResolutionLabel",
        "BurstSize": "burstSize",
        "CalculateJitter": "calculateJitter",
        "CalculateLatency": "calculateLatency",
        "DelayAfterTransmit": "delayAfterTransmit",
        "DownstreamBinaryBackoff": "downstreamBinaryBackoff",
        "DownstreamBinaryFrameLossUnit": "downstreamBinaryFrameLossUnit",
        "DownstreamBinaryLoadUnit": "downstreamBinaryLoadUnit",
        "DownstreamBinaryResolution": "downstreamBinaryResolution",
        "DownstreamBinarySearchType": "downstreamBinarySearchType",
        "DownstreamBinaryTolerance": "downstreamBinaryTolerance",
        "DownstreamImixAdd": "downstreamImixAdd",
        "DownstreamImixData": "downstreamImixData",
        "DownstreamImixDataQoS": "downstreamImixDataQoS",
        "DownstreamImixDelete": "downstreamImixDelete",
        "DownstreamImixDistribution": "downstreamImixDistribution",
        "DownstreamImixEnabled": "downstreamImixEnabled",
        "DownstreamImixTemplates": "downstreamImixTemplates",
        "DownstreamInitialBinaryLoadRate": "downstreamInitialBinaryLoadRate",
        "DownstreamInitialStepLoadRate": "downstreamInitialStepLoadRate",
        "DownstreamLoadType": "downstreamLoadType",
        "DownstreamMaxBinaryLoadRate": "downstreamMaxBinaryLoadRate",
        "DownstreamMaxStepLoadRate": "downstreamMaxStepLoadRate",
        "DownstreamMinBinaryLoadRate": "downstreamMinBinaryLoadRate",
        "DownstreamStepFrameLossUnit": "downstreamStepFrameLossUnit",
        "DownstreamStepLoadUnit": "downstreamStepLoadUnit",
        "DownstreamStepStepLoadRate": "downstreamStepStepLoadRate",
        "DownstreamStepTolerance": "downstreamStepTolerance",
        "DownstreamStopTestOnHighLoss": "downstreamStopTestOnHighLoss",
        "Duration": "duration",
        "EnableBackoffIteration": "enableBackoffIteration",
        "EnableDataIntegrity": "enableDataIntegrity",
        "EnableFastConvergence": "enableFastConvergence",
        "EnableLayer1Rate": "enableLayer1Rate",
        "EnableMinFrameSize": "enableMinFrameSize",
        "EnableSaturationIteration": "enableSaturationIteration",
        "EnableStopTestOnHighLoss": "enableStopTestOnHighLoss",
        "FastConvergenceDuration": "fastConvergenceDuration",
        "FastConvergenceThreshold": "fastConvergenceThreshold",
        "ForceRegenerate": "forceRegenerate",
        "FramesPerBurstGap": "framesPerBurstGap",
        "Gap": "gap",
        "GenerateTrackingOptionAggregationFiles": "generateTrackingOptionAggregationFiles",
        "ImixTrafficType": "imixTrafficType",
        "IterationParameters": "iterationParameters",
        "LatencyBins": "latencyBins",
        "LatencyBinsEnabled": "latencyBinsEnabled",
        "LatencyType": "latencyType",
        "LoadType": "loadType",
        "MapType": "mapType",
        "Numtrials": "numtrials",
        "PortDelayEnabled": "portDelayEnabled",
        "PortDelayUnit": "portDelayUnit",
        "PortDelayValue": "portDelayValue",
        "ProtocolItem": "protocolItem",
        "ReportSequenceError": "reportSequenceError",
        "ReportTputRateUnit": "reportTputRateUnit",
        "SaturationIteration": "saturationIteration",
        "StaggeredStart": "staggeredStart",
        "StepAcceptableFrameLossLabel": "stepAcceptableFrameLossLabel",
        "StepEndRateLabel": "stepEndRateLabel",
        "StepInitialRateLabel": "stepInitialRateLabel",
        "StepLoadUnitLabel": "stepLoadUnitLabel",
        "StepStepRateLabel": "stepStepRateLabel",
        "SupportedTrafficTypes": "supportedTrafficTypes",
        "TestType": "testType",
        "TestTypeTemp": "testTypeTemp",
        "TestTypeTemp2": "testTypeTemp2",
        "Tolerance": "tolerance",
        "TrafficType": "trafficType",
        "TxDelay": "txDelay",
        "UpstreamBinaryBackoff": "upstreamBinaryBackoff",
        "UpstreamBinaryFrameLossUnit": "upstreamBinaryFrameLossUnit",
        "UpstreamBinaryLoadUnit": "upstreamBinaryLoadUnit",
        "UpstreamBinaryResolution": "upstreamBinaryResolution",
        "UpstreamBinarySearchType": "upstreamBinarySearchType",
        "UpstreamBinaryTolerance": "upstreamBinaryTolerance",
        "UpstreamEnableExtraIterations": "upstreamEnableExtraIterations",
        "UpstreamExtraIterationOffsets": "upstreamExtraIterationOffsets",
        "UpstreamImixAdd": "upstreamImixAdd",
        "UpstreamImixData": "upstreamImixData",
        "UpstreamImixDataQoS": "upstreamImixDataQoS",
        "UpstreamImixDelete": "upstreamImixDelete",
        "UpstreamImixDistribution": "upstreamImixDistribution",
        "UpstreamImixEnabled": "upstreamImixEnabled",
        "UpstreamImixTemplates": "upstreamImixTemplates",
        "UpstreamInitialBinaryLoadRate": "upstreamInitialBinaryLoadRate",
        "UpstreamInitialStepLoadRate": "upstreamInitialStepLoadRate",
        "UpstreamLoadType": "upstreamLoadType",
        "UpstreamMaxBinaryLoadRate": "upstreamMaxBinaryLoadRate",
        "UpstreamMaxStepLoadRate": "upstreamMaxStepLoadRate",
        "UpstreamMinBinaryLoadRate": "upstreamMinBinaryLoadRate",
        "UpstreamStepFrameLossUnit": "upstreamStepFrameLossUnit",
        "UpstreamStepLoadUnit": "upstreamStepLoadUnit",
        "UpstreamStepStepLoadRate": "upstreamStepStepLoadRate",
        "UpstreamStepTolerance": "upstreamStepTolerance",
        "UpstreamStopTestOnHighLoss": "upstreamStopTestOnHighLoss",
        "UpstreamUsePercentOffsets": "upstreamUsePercentOffsets",
    }
    _SDM_ENUM_MAP = {
        "downstreamBinaryFrameLossUnit": ["%", "frames"],
        "downstreamBinaryLoadUnit": [
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
        "downstreamImixDistribution": ["bwpercentage", "weight"],
        "downstreamImixTemplates": [
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
        "downstreamStepFrameLossUnit": ["%", "frames"],
        "downstreamStepLoadUnit": [
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
        "testType": ["downstreamOnly", "upstreamDownstream", "upstreamOnly"],
        "testTypeTemp": ["downstreamOnly", "upstreamDownstream", "upstreamOnly"],
        "testTypeTemp2": ["downstreamOnly", "upstreamDownstream", "upstreamOnly"],
        "trafficType": ["burstyLoading", "constantLoading"],
        "upstreamBinaryFrameLossUnit": ["%", "frames"],
        "upstreamBinaryLoadUnit": [
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
        "upstreamImixDistribution": ["bwpercentage", "weight"],
        "upstreamImixTemplates": [
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
        "upstreamLoadType": ["binary"],
        "upstreamStepFrameLossUnit": ["%", "frames"],
        "upstreamStepLoadUnit": [
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
    def AggregateByDirection(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregateByDirection"])

    @AggregateByDirection.setter
    def AggregateByDirection(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AggregateByDirection"], value)

    @property
    def AggregateByFlowgroup(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregateByFlowgroup"])

    @AggregateByFlowgroup.setter
    def AggregateByFlowgroup(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AggregateByFlowgroup"], value)

    @property
    def AggregateByPort(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregateByPort"])

    @AggregateByPort.setter
    def AggregateByPort(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AggregateByPort"], value)

    @property
    def BackoffIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the back of iteration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BackoffIteration"])

    @BackoffIteration.setter
    def BackoffIteration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BackoffIteration"], value)

    @property
    def BinaryAcceptableFrameLossLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the binary value of acceptable frame loss label
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryAcceptableFrameLossLabel"])

    @BinaryAcceptableFrameLossLabel.setter
    def BinaryAcceptableFrameLossLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryAcceptableFrameLossLabel"], value)

    @property
    def BinaryBackoffLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the binary backoff label
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryBackoffLabel"])

    @BinaryBackoffLabel.setter
    def BinaryBackoffLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryBackoffLabel"], value)

    @property
    def BinaryInitialRateLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies initial rate label
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryInitialRateLabel"])

    @BinaryInitialRateLabel.setter
    def BinaryInitialRateLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryInitialRateLabel"], value)

    @property
    def BinaryLoadUnitLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the binary load unit label
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryLoadUnitLabel"])

    @BinaryLoadUnitLabel.setter
    def BinaryLoadUnitLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryLoadUnitLabel"], value)

    @property
    def BinaryMaxRateLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the binary maximum rate label
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryMaxRateLabel"])

    @BinaryMaxRateLabel.setter
    def BinaryMaxRateLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryMaxRateLabel"], value)

    @property
    def BinaryMinRateLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the binary minimum rte label
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryMinRateLabel"])

    @BinaryMinRateLabel.setter
    def BinaryMinRateLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryMinRateLabel"], value)

    @property
    def BinaryResolutionLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the binary resolution label
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryResolutionLabel"])

    @BinaryResolutionLabel.setter
    def BinaryResolutionLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryResolutionLabel"], value)

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
    def DelayAfterTransmit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the delay time after transmit of the packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"])

    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"], value)

    @property
    def DownstreamBinaryBackoff(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the downstream binary backoff
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamBinaryBackoff"])

    @DownstreamBinaryBackoff.setter
    def DownstreamBinaryBackoff(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamBinaryBackoff"], value)

    @property
    def DownstreamBinaryFrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(% | frames): Signifies the downstream binary frame loss unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamBinaryFrameLossUnit"])

    @DownstreamBinaryFrameLossUnit.setter
    def DownstreamBinaryFrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamBinaryFrameLossUnit"], value)

    @property
    def DownstreamBinaryLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies downstream binary load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamBinaryLoadUnit"])

    @DownstreamBinaryLoadUnit.setter
    def DownstreamBinaryLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamBinaryLoadUnit"], value)

    @property
    def DownstreamBinaryResolution(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the downstream binary resolution.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamBinaryResolution"])

    @DownstreamBinaryResolution.setter
    def DownstreamBinaryResolution(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamBinaryResolution"], value)

    @property
    def DownstreamBinarySearchType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the downstream binary search type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamBinarySearchType"])

    @DownstreamBinarySearchType.setter
    def DownstreamBinarySearchType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamBinarySearchType"], value)

    @property
    def DownstreamBinaryTolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the downstream binary tolerance.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamBinaryTolerance"])

    @DownstreamBinaryTolerance.setter
    def DownstreamBinaryTolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamBinaryTolerance"], value)

    @property
    def DownstreamImixAdd(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Adds downstream IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamImixAdd"])

    @DownstreamImixAdd.setter
    def DownstreamImixAdd(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamImixAdd"], value)

    @property
    def DownstreamImixData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the downstream IMIX data
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamImixData"])

    @DownstreamImixData.setter
    def DownstreamImixData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamImixData"], value)

    @property
    def DownstreamImixDataQoS(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the quality of service for downstream IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamImixDataQoS"])

    @DownstreamImixDataQoS.setter
    def DownstreamImixDataQoS(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamImixDataQoS"], value)

    @property
    def DownstreamImixDelete(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Deletes downstream IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamImixDelete"])

    @DownstreamImixDelete.setter
    def DownstreamImixDelete(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamImixDelete"], value)

    @property
    def DownstreamImixDistribution(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bwpercentage | weight): signifies the downstream imix distribution.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamImixDistribution"])

    @DownstreamImixDistribution.setter
    def DownstreamImixDistribution(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamImixDistribution"], value)

    @property
    def DownstreamImixEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables downstream IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamImixEnabled"])

    @DownstreamImixEnabled.setter
    def DownstreamImixEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamImixEnabled"], value)

    @property
    def DownstreamImixTemplates(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal): Signifies downstream IMIX templates.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamImixTemplates"])

    @DownstreamImixTemplates.setter
    def DownstreamImixTemplates(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamImixTemplates"], value)

    @property
    def DownstreamInitialBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies downstream initial binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamInitialBinaryLoadRate"])

    @DownstreamInitialBinaryLoadRate.setter
    def DownstreamInitialBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamInitialBinaryLoadRate"], value)

    @property
    def DownstreamInitialStepLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies downstream initial step load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamInitialStepLoadRate"])

    @DownstreamInitialStepLoadRate.setter
    def DownstreamInitialStepLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamInitialStepLoadRate"], value)

    @property
    def DownstreamLoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies downstream load type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamLoadType"])

    @DownstreamLoadType.setter
    def DownstreamLoadType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamLoadType"], value)

    @property
    def DownstreamMaxBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies maximum downstream binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamMaxBinaryLoadRate"])

    @DownstreamMaxBinaryLoadRate.setter
    def DownstreamMaxBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamMaxBinaryLoadRate"], value)

    @property
    def DownstreamMaxStepLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies downstream maximum step load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamMaxStepLoadRate"])

    @DownstreamMaxStepLoadRate.setter
    def DownstreamMaxStepLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamMaxStepLoadRate"], value)

    @property
    def DownstreamMinBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies minimum downstream binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamMinBinaryLoadRate"])

    @DownstreamMinBinaryLoadRate.setter
    def DownstreamMinBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamMinBinaryLoadRate"], value)

    @property
    def DownstreamStepFrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(% | frames): Signifies downstream step frame loss unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamStepFrameLossUnit"])

    @DownstreamStepFrameLossUnit.setter
    def DownstreamStepFrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamStepFrameLossUnit"], value)

    @property
    def DownstreamStepLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies downstream step load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamStepLoadUnit"])

    @DownstreamStepLoadUnit.setter
    def DownstreamStepLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamStepLoadUnit"], value)

    @property
    def DownstreamStepStepLoadRate(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies downstream step load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamStepStepLoadRate"])

    @DownstreamStepStepLoadRate.setter
    def DownstreamStepStepLoadRate(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamStepStepLoadRate"], value)

    @property
    def DownstreamStepTolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies downstream step tolerance.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamStepTolerance"])

    @DownstreamStepTolerance.setter
    def DownstreamStepTolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamStepTolerance"], value)

    @property
    def DownstreamStopTestOnHighLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This stops the downstream test on high loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownstreamStopTestOnHighLoss"])

    @DownstreamStopTestOnHighLoss.setter
    def DownstreamStopTestOnHighLoss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownstreamStopTestOnHighLoss"], value)

    @property
    def Duration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the duration.
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
        - bool: If true, enables backoff iteration.
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
        - bool: If true, enables stop test on high loss option.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableStopTestOnHighLoss"])

    @EnableStopTestOnHighLoss.setter
    def EnableStopTestOnHighLoss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableStopTestOnHighLoss"], value)

    @property
    def FastConvergenceDuration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies fast convergence duration.
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
        - number: Signifies the threshold for fast convergence.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastConvergenceThreshold"])

    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastConvergenceThreshold"], value)

    @property
    def ForceRegenerate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables force regenerate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForceRegenerate"])

    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForceRegenerate"], value)

    @property
    def FramesPerBurstGap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the frames sent per burst gap
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesPerBurstGap"])

    @FramesPerBurstGap.setter
    def FramesPerBurstGap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesPerBurstGap"], value)

    @property
    def Gap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the burst gap
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
        - bool: If true, generates tracking option of aggregation files.
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
    def ImixTrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the type of IMIX traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImixTrafficType"])

    @ImixTrafficType.setter
    def ImixTrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ImixTrafficType"], value)

    @property
    def IterationParameters(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: This signifies the Iteration Parameters.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IterationParameters"])

    @IterationParameters.setter
    def IterationParameters(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IterationParameters"], value)

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
        - str(cutThrough | storeForward): Signifies the latency type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyType"])

    @LatencyType.setter
    def LatencyType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyType"], value)

    @property
    def LoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged): Signifies the load type.
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
        - str: Signifies the map type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapType"])

    @MapType.setter
    def MapType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapType"], value)

    @property
    def Numtrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the numeric trials.
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
        - str(gbps | gBps | kbps | kBps | mbps | mBps): Reports throughput rate unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportTputRateUnit"])

    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportTputRateUnit"], value)

    @property
    def SaturationIteration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies saturation iteration.
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
        - bool: If true, staggers start.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StaggeredStart"])

    @StaggeredStart.setter
    def StaggeredStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StaggeredStart"], value)

    @property
    def StepAcceptableFrameLossLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies step acceptable frame loss label
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepAcceptableFrameLossLabel"])

    @StepAcceptableFrameLossLabel.setter
    def StepAcceptableFrameLossLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepAcceptableFrameLossLabel"], value)

    @property
    def StepEndRateLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies step end rate label
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepEndRateLabel"])

    @StepEndRateLabel.setter
    def StepEndRateLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepEndRateLabel"], value)

    @property
    def StepInitialRateLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies step initial rate label
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepInitialRateLabel"])

    @StepInitialRateLabel.setter
    def StepInitialRateLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepInitialRateLabel"], value)

    @property
    def StepLoadUnitLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the step load unit label
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepLoadUnitLabel"])

    @StepLoadUnitLabel.setter
    def StepLoadUnitLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepLoadUnitLabel"], value)

    @property
    def StepStepRateLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the step rate label
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepStepRateLabel"])

    @StepStepRateLabel.setter
    def StepStepRateLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepStepRateLabel"], value)

    @property
    def SupportedTrafficTypes(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the traffic types supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportedTrafficTypes"])

    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportedTrafficTypes"], value)

    @property
    def TestType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(downstreamOnly | upstreamDownstream | upstreamOnly): Signifies th test type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestType"])

    @TestType.setter
    def TestType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestType"], value)

    @property
    def TestTypeTemp(self):
        # type: () -> str
        """
        Returns
        -------
        - str(downstreamOnly | upstreamDownstream | upstreamOnly): Signifies the temporary test type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestTypeTemp"])

    @TestTypeTemp.setter
    def TestTypeTemp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestTypeTemp"], value)

    @property
    def TestTypeTemp2(self):
        # type: () -> str
        """
        Returns
        -------
        - str(downstreamOnly | upstreamDownstream | upstreamOnly): Signifies the second temporary test type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestTypeTemp2"])

    @TestTypeTemp2.setter
    def TestTypeTemp2(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestTypeTemp2"], value)

    @property
    def Tolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the tolerance.
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
        - str(burstyLoading | constantLoading): Signifies the traffic type.
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
        - number: Signifies the delay time during the transmission of data
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxDelay"])

    @TxDelay.setter
    def TxDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxDelay"], value)

    @property
    def UpstreamBinaryBackoff(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies upstream binary backoff
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamBinaryBackoff"])

    @UpstreamBinaryBackoff.setter
    def UpstreamBinaryBackoff(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamBinaryBackoff"], value)

    @property
    def UpstreamBinaryFrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(% | frames): Signifies the upstream binary frame loss unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamBinaryFrameLossUnit"])

    @UpstreamBinaryFrameLossUnit.setter
    def UpstreamBinaryFrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamBinaryFrameLossUnit"], value)

    @property
    def UpstreamBinaryLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): This signifies the upstream binary load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamBinaryLoadUnit"])

    @UpstreamBinaryLoadUnit.setter
    def UpstreamBinaryLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamBinaryLoadUnit"], value)

    @property
    def UpstreamBinaryResolution(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies upstream binary resolution.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamBinaryResolution"])

    @UpstreamBinaryResolution.setter
    def UpstreamBinaryResolution(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamBinaryResolution"], value)

    @property
    def UpstreamBinarySearchType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the upstream binary search type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamBinarySearchType"])

    @UpstreamBinarySearchType.setter
    def UpstreamBinarySearchType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamBinarySearchType"], value)

    @property
    def UpstreamBinaryTolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the upstream binary tolerance.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamBinaryTolerance"])

    @UpstreamBinaryTolerance.setter
    def UpstreamBinaryTolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamBinaryTolerance"], value)

    @property
    def UpstreamEnableExtraIterations(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables extra iterations upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamEnableExtraIterations"])

    @UpstreamEnableExtraIterations.setter
    def UpstreamEnableExtraIterations(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamEnableExtraIterations"], value)

    @property
    def UpstreamExtraIterationOffsets(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies extra iteration offsets upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamExtraIterationOffsets"])

    @UpstreamExtraIterationOffsets.setter
    def UpstreamExtraIterationOffsets(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamExtraIterationOffsets"], value)

    @property
    def UpstreamImixAdd(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Adds upstream IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamImixAdd"])

    @UpstreamImixAdd.setter
    def UpstreamImixAdd(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamImixAdd"], value)

    @property
    def UpstreamImixData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies upstream IMIX data
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamImixData"])

    @UpstreamImixData.setter
    def UpstreamImixData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamImixData"], value)

    @property
    def UpstreamImixDataQoS(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables quality of service for upstream IMIX data
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamImixDataQoS"])

    @UpstreamImixDataQoS.setter
    def UpstreamImixDataQoS(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamImixDataQoS"], value)

    @property
    def UpstreamImixDelete(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Deletes upstream IMIX data
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamImixDelete"])

    @UpstreamImixDelete.setter
    def UpstreamImixDelete(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamImixDelete"], value)

    @property
    def UpstreamImixDistribution(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bwpercentage | weight): Distributes upstream IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamImixDistribution"])

    @UpstreamImixDistribution.setter
    def UpstreamImixDistribution(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamImixDistribution"], value)

    @property
    def UpstreamImixEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables upstream IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamImixEnabled"])

    @UpstreamImixEnabled.setter
    def UpstreamImixEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamImixEnabled"], value)

    @property
    def UpstreamImixTemplates(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal): Signifies upstream IMIX templates.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamImixTemplates"])

    @UpstreamImixTemplates.setter
    def UpstreamImixTemplates(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamImixTemplates"], value)

    @property
    def UpstreamInitialBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the uptream initial binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamInitialBinaryLoadRate"])

    @UpstreamInitialBinaryLoadRate.setter
    def UpstreamInitialBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamInitialBinaryLoadRate"], value)

    @property
    def UpstreamInitialStepLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies upstream initial step load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamInitialStepLoadRate"])

    @UpstreamInitialStepLoadRate.setter
    def UpstreamInitialStepLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamInitialStepLoadRate"], value)

    @property
    def UpstreamLoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(binary): Signifies upstream load type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamLoadType"])

    @UpstreamLoadType.setter
    def UpstreamLoadType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamLoadType"], value)

    @property
    def UpstreamMaxBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies upstream maximum binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamMaxBinaryLoadRate"])

    @UpstreamMaxBinaryLoadRate.setter
    def UpstreamMaxBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamMaxBinaryLoadRate"], value)

    @property
    def UpstreamMaxStepLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies upstream maximum step load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamMaxStepLoadRate"])

    @UpstreamMaxStepLoadRate.setter
    def UpstreamMaxStepLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamMaxStepLoadRate"], value)

    @property
    def UpstreamMinBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the upstream binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamMinBinaryLoadRate"])

    @UpstreamMinBinaryLoadRate.setter
    def UpstreamMinBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamMinBinaryLoadRate"], value)

    @property
    def UpstreamStepFrameLossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(% | frames): Signifies the upstream step frame loss unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamStepFrameLossUnit"])

    @UpstreamStepFrameLossUnit.setter
    def UpstreamStepFrameLossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamStepFrameLossUnit"], value)

    @property
    def UpstreamStepLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies upstream step load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamStepLoadUnit"])

    @UpstreamStepLoadUnit.setter
    def UpstreamStepLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamStepLoadUnit"], value)

    @property
    def UpstreamStepStepLoadRate(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the upstream step load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamStepStepLoadRate"])

    @UpstreamStepStepLoadRate.setter
    def UpstreamStepStepLoadRate(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamStepStepLoadRate"], value)

    @property
    def UpstreamStepTolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies upstream step tolerance value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamStepTolerance"])

    @UpstreamStepTolerance.setter
    def UpstreamStepTolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamStepTolerance"], value)

    @property
    def UpstreamStopTestOnHighLoss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies upstream stop test on high loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamStopTestOnHighLoss"])

    @UpstreamStopTestOnHighLoss.setter
    def UpstreamStopTestOnHighLoss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamStopTestOnHighLoss"], value)

    @property
    def UpstreamUsePercentOffsets(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies upstream use percent offsets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpstreamUsePercentOffsets"])

    @UpstreamUsePercentOffsets.setter
    def UpstreamUsePercentOffsets(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpstreamUsePercentOffsets"], value)

    def update(
        self,
        AggregateByDirection=None,
        AggregateByFlowgroup=None,
        AggregateByPort=None,
        BackoffIteration=None,
        BinaryAcceptableFrameLossLabel=None,
        BinaryBackoffLabel=None,
        BinaryInitialRateLabel=None,
        BinaryLoadUnitLabel=None,
        BinaryMaxRateLabel=None,
        BinaryMinRateLabel=None,
        BinaryResolutionLabel=None,
        BurstSize=None,
        CalculateJitter=None,
        CalculateLatency=None,
        DelayAfterTransmit=None,
        DownstreamBinaryBackoff=None,
        DownstreamBinaryFrameLossUnit=None,
        DownstreamBinaryLoadUnit=None,
        DownstreamBinaryResolution=None,
        DownstreamBinarySearchType=None,
        DownstreamBinaryTolerance=None,
        DownstreamImixAdd=None,
        DownstreamImixData=None,
        DownstreamImixDataQoS=None,
        DownstreamImixDelete=None,
        DownstreamImixDistribution=None,
        DownstreamImixEnabled=None,
        DownstreamImixTemplates=None,
        DownstreamInitialBinaryLoadRate=None,
        DownstreamInitialStepLoadRate=None,
        DownstreamLoadType=None,
        DownstreamMaxBinaryLoadRate=None,
        DownstreamMaxStepLoadRate=None,
        DownstreamMinBinaryLoadRate=None,
        DownstreamStepFrameLossUnit=None,
        DownstreamStepLoadUnit=None,
        DownstreamStepStepLoadRate=None,
        DownstreamStepTolerance=None,
        DownstreamStopTestOnHighLoss=None,
        Duration=None,
        EnableBackoffIteration=None,
        EnableDataIntegrity=None,
        EnableFastConvergence=None,
        EnableLayer1Rate=None,
        EnableMinFrameSize=None,
        EnableSaturationIteration=None,
        EnableStopTestOnHighLoss=None,
        FastConvergenceDuration=None,
        FastConvergenceThreshold=None,
        ForceRegenerate=None,
        FramesPerBurstGap=None,
        Gap=None,
        GenerateTrackingOptionAggregationFiles=None,
        ImixTrafficType=None,
        IterationParameters=None,
        LatencyBins=None,
        LatencyBinsEnabled=None,
        LatencyType=None,
        LoadType=None,
        MapType=None,
        Numtrials=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        ProtocolItem=None,
        ReportSequenceError=None,
        ReportTputRateUnit=None,
        SaturationIteration=None,
        StaggeredStart=None,
        StepAcceptableFrameLossLabel=None,
        StepEndRateLabel=None,
        StepInitialRateLabel=None,
        StepLoadUnitLabel=None,
        StepStepRateLabel=None,
        SupportedTrafficTypes=None,
        TestType=None,
        TestTypeTemp=None,
        TestTypeTemp2=None,
        Tolerance=None,
        TrafficType=None,
        TxDelay=None,
        UpstreamBinaryBackoff=None,
        UpstreamBinaryFrameLossUnit=None,
        UpstreamBinaryLoadUnit=None,
        UpstreamBinaryResolution=None,
        UpstreamBinarySearchType=None,
        UpstreamBinaryTolerance=None,
        UpstreamEnableExtraIterations=None,
        UpstreamExtraIterationOffsets=None,
        UpstreamImixAdd=None,
        UpstreamImixData=None,
        UpstreamImixDataQoS=None,
        UpstreamImixDelete=None,
        UpstreamImixDistribution=None,
        UpstreamImixEnabled=None,
        UpstreamImixTemplates=None,
        UpstreamInitialBinaryLoadRate=None,
        UpstreamInitialStepLoadRate=None,
        UpstreamLoadType=None,
        UpstreamMaxBinaryLoadRate=None,
        UpstreamMaxStepLoadRate=None,
        UpstreamMinBinaryLoadRate=None,
        UpstreamStepFrameLossUnit=None,
        UpstreamStepLoadUnit=None,
        UpstreamStepStepLoadRate=None,
        UpstreamStepTolerance=None,
        UpstreamStopTestOnHighLoss=None,
        UpstreamUsePercentOffsets=None,
    ):
        # type: (bool, bool, bool, int, str, str, str, str, str, str, str, int, bool, bool, int, int, str, str, int, str, int, str, str, bool, str, str, bool, str, int, int, str, int, int, int, str, str, str, int, int, int, bool, bool, bool, bool, bool, bool, bool, int, int, bool, int, int, bool, str, str, str, bool, str, str, str, int, bool, str, int, List[str], bool, str, int, bool, str, str, str, str, str, str, str, str, str, int, str, int, int, str, str, int, str, int, bool, str, str, str, bool, str, str, bool, str, int, int, str, int, int, int, str, str, str, int, int, str) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - AggregateByDirection (bool): NOT DEFINED
        - AggregateByFlowgroup (bool): NOT DEFINED
        - AggregateByPort (bool): NOT DEFINED
        - BackoffIteration (number): Signifies the back of iteration.
        - BinaryAcceptableFrameLossLabel (str): Signifies the binary value of acceptable frame loss label
        - BinaryBackoffLabel (str): Signifies the binary backoff label
        - BinaryInitialRateLabel (str): Signifies initial rate label
        - BinaryLoadUnitLabel (str): Signifies the binary load unit label
        - BinaryMaxRateLabel (str): Signifies the binary maximum rate label
        - BinaryMinRateLabel (str): Signifies the binary minimum rte label
        - BinaryResolutionLabel (str): Signifies the binary resolution label
        - BurstSize (number): The number of packets to send in a burst.
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calculates latency.
        - DelayAfterTransmit (number): Signifies the delay time after transmit of the packet.
        - DownstreamBinaryBackoff (number): Signifies the downstream binary backoff
        - DownstreamBinaryFrameLossUnit (str(% | frames)): Signifies the downstream binary frame loss unit.
        - DownstreamBinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies downstream binary load unit.
        - DownstreamBinaryResolution (number): Signifies the downstream binary resolution.
        - DownstreamBinarySearchType (str): This signifies the downstream binary search type.
        - DownstreamBinaryTolerance (number): Signifies the downstream binary tolerance.
        - DownstreamImixAdd (str): Adds downstream IMIX
        - DownstreamImixData (str): Signifies the downstream IMIX data
        - DownstreamImixDataQoS (bool): If true, enables the quality of service for downstream IMIX
        - DownstreamImixDelete (str): Deletes downstream IMIX
        - DownstreamImixDistribution (str(bwpercentage | weight)): signifies the downstream imix distribution.
        - DownstreamImixEnabled (bool): If true, enables downstream IMIX
        - DownstreamImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Signifies downstream IMIX templates.
        - DownstreamInitialBinaryLoadRate (number): This signifies downstream initial binary load rate.
        - DownstreamInitialStepLoadRate (number): This signifies downstream initial step load rate.
        - DownstreamLoadType (str): Signifies downstream load type.
        - DownstreamMaxBinaryLoadRate (number): Signifies maximum downstream binary load rate.
        - DownstreamMaxStepLoadRate (number): Signifies downstream maximum step load rate.
        - DownstreamMinBinaryLoadRate (number): Signifies minimum downstream binary load rate.
        - DownstreamStepFrameLossUnit (str(% | frames)): Signifies downstream step frame loss unit.
        - DownstreamStepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies downstream step load unit.
        - DownstreamStepStepLoadRate (str): This signifies downstream step load rate.
        - DownstreamStepTolerance (number): Signifies downstream step tolerance.
        - DownstreamStopTestOnHighLoss (number): This stops the downstream test on high loss.
        - Duration (number): Signifies the duration.
        - EnableBackoffIteration (bool): If true, enables backoff iteration.
        - EnableDataIntegrity (bool): If true, enables data integrity.
        - EnableFastConvergence (bool): If true, enables fast convergence.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableSaturationIteration (bool): If true, enables the test to run an extra iteration for calculating the SaturationLatency.
        - EnableStopTestOnHighLoss (bool): If true, enables stop test on high loss option.
        - FastConvergenceDuration (number): Signifies fast convergence duration.
        - FastConvergenceThreshold (number): Signifies the threshold for fast convergence.
        - ForceRegenerate (bool): If true, enables force regenerate.
        - FramesPerBurstGap (number): Signifies the frames sent per burst gap
        - Gap (number): Signifies the burst gap
        - GenerateTrackingOptionAggregationFiles (bool): If true, generates tracking option of aggregation files.
        - ImixTrafficType (str): Signifies the type of IMIX traffic.
        - IterationParameters (str): This signifies the Iteration Parameters.
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LatencyType (str(cutThrough | storeForward)): Signifies the latency type.
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)): Signifies the load type.
        - MapType (str): Signifies the map type.
        - Numtrials (number): Signifies the numeric trials.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - ReportSequenceError (bool): If true, reports sequence error.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): Reports throughput rate unit.
        - SaturationIteration (number): Signifies saturation iteration.
        - StaggeredStart (bool): If true, staggers start.
        - StepAcceptableFrameLossLabel (str): Signifies step acceptable frame loss label
        - StepEndRateLabel (str): Signifies step end rate label
        - StepInitialRateLabel (str): Signifies step initial rate label
        - StepLoadUnitLabel (str): Signifies the step load unit label
        - StepStepRateLabel (str): Signifies the step rate label
        - SupportedTrafficTypes (str): Signifies the traffic types supported.
        - TestType (str(downstreamOnly | upstreamDownstream | upstreamOnly)): Signifies th test type.
        - TestTypeTemp (str(downstreamOnly | upstreamDownstream | upstreamOnly)): Signifies the temporary test type.
        - TestTypeTemp2 (str(downstreamOnly | upstreamDownstream | upstreamOnly)): Signifies the second temporary test type.
        - Tolerance (number): Signifies the tolerance.
        - TrafficType (str(burstyLoading | constantLoading)): Signifies the traffic type.
        - TxDelay (number): Signifies the delay time during the transmission of data
        - UpstreamBinaryBackoff (number): Signifies upstream binary backoff
        - UpstreamBinaryFrameLossUnit (str(% | frames)): Signifies the upstream binary frame loss unit.
        - UpstreamBinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): This signifies the upstream binary load unit.
        - UpstreamBinaryResolution (number): Signifies upstream binary resolution.
        - UpstreamBinarySearchType (str): Signifies the upstream binary search type.
        - UpstreamBinaryTolerance (number): Signifies the upstream binary tolerance.
        - UpstreamEnableExtraIterations (bool): If true, enables extra iterations upstream.
        - UpstreamExtraIterationOffsets (str): Signifies extra iteration offsets upstream.
        - UpstreamImixAdd (str): Adds upstream IMIX
        - UpstreamImixData (str): Signifies upstream IMIX data
        - UpstreamImixDataQoS (bool): If true, enables quality of service for upstream IMIX data
        - UpstreamImixDelete (str): Deletes upstream IMIX data
        - UpstreamImixDistribution (str(bwpercentage | weight)): Distributes upstream IMIX
        - UpstreamImixEnabled (bool): If true, enables upstream IMIX
        - UpstreamImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Signifies upstream IMIX templates.
        - UpstreamInitialBinaryLoadRate (number): Signifies the uptream initial binary load rate.
        - UpstreamInitialStepLoadRate (number): This signifies upstream initial step load rate.
        - UpstreamLoadType (str(binary)): Signifies upstream load type.
        - UpstreamMaxBinaryLoadRate (number): Signifies upstream maximum binary load rate.
        - UpstreamMaxStepLoadRate (number): Signifies upstream maximum step load rate.
        - UpstreamMinBinaryLoadRate (number): Signifies the upstream binary load rate.
        - UpstreamStepFrameLossUnit (str(% | frames)): Signifies the upstream step frame loss unit.
        - UpstreamStepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies upstream step load unit.
        - UpstreamStepStepLoadRate (str): Signifies the upstream step load rate.
        - UpstreamStepTolerance (number): Signifies upstream step tolerance value.
        - UpstreamStopTestOnHighLoss (number): Signifies upstream stop test on high loss.
        - UpstreamUsePercentOffsets (str): Signifies upstream use percent offsets.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AggregateByDirection=None,
        AggregateByFlowgroup=None,
        AggregateByPort=None,
        BackoffIteration=None,
        BinaryAcceptableFrameLossLabel=None,
        BinaryBackoffLabel=None,
        BinaryInitialRateLabel=None,
        BinaryLoadUnitLabel=None,
        BinaryMaxRateLabel=None,
        BinaryMinRateLabel=None,
        BinaryResolutionLabel=None,
        BurstSize=None,
        CalculateJitter=None,
        CalculateLatency=None,
        DelayAfterTransmit=None,
        DownstreamBinaryBackoff=None,
        DownstreamBinaryFrameLossUnit=None,
        DownstreamBinaryLoadUnit=None,
        DownstreamBinaryResolution=None,
        DownstreamBinarySearchType=None,
        DownstreamBinaryTolerance=None,
        DownstreamImixAdd=None,
        DownstreamImixData=None,
        DownstreamImixDataQoS=None,
        DownstreamImixDelete=None,
        DownstreamImixDistribution=None,
        DownstreamImixEnabled=None,
        DownstreamImixTemplates=None,
        DownstreamInitialBinaryLoadRate=None,
        DownstreamInitialStepLoadRate=None,
        DownstreamLoadType=None,
        DownstreamMaxBinaryLoadRate=None,
        DownstreamMaxStepLoadRate=None,
        DownstreamMinBinaryLoadRate=None,
        DownstreamStepFrameLossUnit=None,
        DownstreamStepLoadUnit=None,
        DownstreamStepStepLoadRate=None,
        DownstreamStepTolerance=None,
        DownstreamStopTestOnHighLoss=None,
        Duration=None,
        EnableBackoffIteration=None,
        EnableDataIntegrity=None,
        EnableFastConvergence=None,
        EnableLayer1Rate=None,
        EnableMinFrameSize=None,
        EnableSaturationIteration=None,
        EnableStopTestOnHighLoss=None,
        FastConvergenceDuration=None,
        FastConvergenceThreshold=None,
        ForceRegenerate=None,
        FramesPerBurstGap=None,
        Gap=None,
        GenerateTrackingOptionAggregationFiles=None,
        ImixTrafficType=None,
        IterationParameters=None,
        LatencyBins=None,
        LatencyBinsEnabled=None,
        LatencyType=None,
        LoadType=None,
        MapType=None,
        Numtrials=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        ProtocolItem=None,
        ReportSequenceError=None,
        ReportTputRateUnit=None,
        SaturationIteration=None,
        StaggeredStart=None,
        StepAcceptableFrameLossLabel=None,
        StepEndRateLabel=None,
        StepInitialRateLabel=None,
        StepLoadUnitLabel=None,
        StepStepRateLabel=None,
        SupportedTrafficTypes=None,
        TestType=None,
        TestTypeTemp=None,
        TestTypeTemp2=None,
        Tolerance=None,
        TrafficType=None,
        TxDelay=None,
        UpstreamBinaryBackoff=None,
        UpstreamBinaryFrameLossUnit=None,
        UpstreamBinaryLoadUnit=None,
        UpstreamBinaryResolution=None,
        UpstreamBinarySearchType=None,
        UpstreamBinaryTolerance=None,
        UpstreamEnableExtraIterations=None,
        UpstreamExtraIterationOffsets=None,
        UpstreamImixAdd=None,
        UpstreamImixData=None,
        UpstreamImixDataQoS=None,
        UpstreamImixDelete=None,
        UpstreamImixDistribution=None,
        UpstreamImixEnabled=None,
        UpstreamImixTemplates=None,
        UpstreamInitialBinaryLoadRate=None,
        UpstreamInitialStepLoadRate=None,
        UpstreamLoadType=None,
        UpstreamMaxBinaryLoadRate=None,
        UpstreamMaxStepLoadRate=None,
        UpstreamMinBinaryLoadRate=None,
        UpstreamStepFrameLossUnit=None,
        UpstreamStepLoadUnit=None,
        UpstreamStepStepLoadRate=None,
        UpstreamStepTolerance=None,
        UpstreamStopTestOnHighLoss=None,
        UpstreamUsePercentOffsets=None,
    ):
        # type: (bool, bool, bool, int, str, str, str, str, str, str, str, int, bool, bool, int, int, str, str, int, str, int, str, str, bool, str, str, bool, str, int, int, str, int, int, int, str, str, str, int, int, int, bool, bool, bool, bool, bool, bool, bool, int, int, bool, int, int, bool, str, str, str, bool, str, str, str, int, bool, str, int, List[str], bool, str, int, bool, str, str, str, str, str, str, str, str, str, int, str, int, int, str, str, int, str, int, bool, str, str, str, bool, str, str, bool, str, int, int, str, int, int, int, str, str, str, int, int, str) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - AggregateByDirection (bool): NOT DEFINED
        - AggregateByFlowgroup (bool): NOT DEFINED
        - AggregateByPort (bool): NOT DEFINED
        - BackoffIteration (number): Signifies the back of iteration.
        - BinaryAcceptableFrameLossLabel (str): Signifies the binary value of acceptable frame loss label
        - BinaryBackoffLabel (str): Signifies the binary backoff label
        - BinaryInitialRateLabel (str): Signifies initial rate label
        - BinaryLoadUnitLabel (str): Signifies the binary load unit label
        - BinaryMaxRateLabel (str): Signifies the binary maximum rate label
        - BinaryMinRateLabel (str): Signifies the binary minimum rte label
        - BinaryResolutionLabel (str): Signifies the binary resolution label
        - BurstSize (number): The number of packets to send in a burst.
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calculates latency.
        - DelayAfterTransmit (number): Signifies the delay time after transmit of the packet.
        - DownstreamBinaryBackoff (number): Signifies the downstream binary backoff
        - DownstreamBinaryFrameLossUnit (str(% | frames)): Signifies the downstream binary frame loss unit.
        - DownstreamBinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies downstream binary load unit.
        - DownstreamBinaryResolution (number): Signifies the downstream binary resolution.
        - DownstreamBinarySearchType (str): This signifies the downstream binary search type.
        - DownstreamBinaryTolerance (number): Signifies the downstream binary tolerance.
        - DownstreamImixAdd (str): Adds downstream IMIX
        - DownstreamImixData (str): Signifies the downstream IMIX data
        - DownstreamImixDataQoS (bool): If true, enables the quality of service for downstream IMIX
        - DownstreamImixDelete (str): Deletes downstream IMIX
        - DownstreamImixDistribution (str(bwpercentage | weight)): signifies the downstream imix distribution.
        - DownstreamImixEnabled (bool): If true, enables downstream IMIX
        - DownstreamImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Signifies downstream IMIX templates.
        - DownstreamInitialBinaryLoadRate (number): This signifies downstream initial binary load rate.
        - DownstreamInitialStepLoadRate (number): This signifies downstream initial step load rate.
        - DownstreamLoadType (str): Signifies downstream load type.
        - DownstreamMaxBinaryLoadRate (number): Signifies maximum downstream binary load rate.
        - DownstreamMaxStepLoadRate (number): Signifies downstream maximum step load rate.
        - DownstreamMinBinaryLoadRate (number): Signifies minimum downstream binary load rate.
        - DownstreamStepFrameLossUnit (str(% | frames)): Signifies downstream step frame loss unit.
        - DownstreamStepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies downstream step load unit.
        - DownstreamStepStepLoadRate (str): This signifies downstream step load rate.
        - DownstreamStepTolerance (number): Signifies downstream step tolerance.
        - DownstreamStopTestOnHighLoss (number): This stops the downstream test on high loss.
        - Duration (number): Signifies the duration.
        - EnableBackoffIteration (bool): If true, enables backoff iteration.
        - EnableDataIntegrity (bool): If true, enables data integrity.
        - EnableFastConvergence (bool): If true, enables fast convergence.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableSaturationIteration (bool): If true, enables the test to run an extra iteration for calculating the SaturationLatency.
        - EnableStopTestOnHighLoss (bool): If true, enables stop test on high loss option.
        - FastConvergenceDuration (number): Signifies fast convergence duration.
        - FastConvergenceThreshold (number): Signifies the threshold for fast convergence.
        - ForceRegenerate (bool): If true, enables force regenerate.
        - FramesPerBurstGap (number): Signifies the frames sent per burst gap
        - Gap (number): Signifies the burst gap
        - GenerateTrackingOptionAggregationFiles (bool): If true, generates tracking option of aggregation files.
        - ImixTrafficType (str): Signifies the type of IMIX traffic.
        - IterationParameters (str): This signifies the Iteration Parameters.
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LatencyType (str(cutThrough | storeForward)): Signifies the latency type.
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)): Signifies the load type.
        - MapType (str): Signifies the map type.
        - Numtrials (number): Signifies the numeric trials.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - ReportSequenceError (bool): If true, reports sequence error.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): Reports throughput rate unit.
        - SaturationIteration (number): Signifies saturation iteration.
        - StaggeredStart (bool): If true, staggers start.
        - StepAcceptableFrameLossLabel (str): Signifies step acceptable frame loss label
        - StepEndRateLabel (str): Signifies step end rate label
        - StepInitialRateLabel (str): Signifies step initial rate label
        - StepLoadUnitLabel (str): Signifies the step load unit label
        - StepStepRateLabel (str): Signifies the step rate label
        - SupportedTrafficTypes (str): Signifies the traffic types supported.
        - TestType (str(downstreamOnly | upstreamDownstream | upstreamOnly)): Signifies th test type.
        - TestTypeTemp (str(downstreamOnly | upstreamDownstream | upstreamOnly)): Signifies the temporary test type.
        - TestTypeTemp2 (str(downstreamOnly | upstreamDownstream | upstreamOnly)): Signifies the second temporary test type.
        - Tolerance (number): Signifies the tolerance.
        - TrafficType (str(burstyLoading | constantLoading)): Signifies the traffic type.
        - TxDelay (number): Signifies the delay time during the transmission of data
        - UpstreamBinaryBackoff (number): Signifies upstream binary backoff
        - UpstreamBinaryFrameLossUnit (str(% | frames)): Signifies the upstream binary frame loss unit.
        - UpstreamBinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): This signifies the upstream binary load unit.
        - UpstreamBinaryResolution (number): Signifies upstream binary resolution.
        - UpstreamBinarySearchType (str): Signifies the upstream binary search type.
        - UpstreamBinaryTolerance (number): Signifies the upstream binary tolerance.
        - UpstreamEnableExtraIterations (bool): If true, enables extra iterations upstream.
        - UpstreamExtraIterationOffsets (str): Signifies extra iteration offsets upstream.
        - UpstreamImixAdd (str): Adds upstream IMIX
        - UpstreamImixData (str): Signifies upstream IMIX data
        - UpstreamImixDataQoS (bool): If true, enables quality of service for upstream IMIX data
        - UpstreamImixDelete (str): Deletes upstream IMIX data
        - UpstreamImixDistribution (str(bwpercentage | weight)): Distributes upstream IMIX
        - UpstreamImixEnabled (bool): If true, enables upstream IMIX
        - UpstreamImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Signifies upstream IMIX templates.
        - UpstreamInitialBinaryLoadRate (number): Signifies the uptream initial binary load rate.
        - UpstreamInitialStepLoadRate (number): This signifies upstream initial step load rate.
        - UpstreamLoadType (str(binary)): Signifies upstream load type.
        - UpstreamMaxBinaryLoadRate (number): Signifies upstream maximum binary load rate.
        - UpstreamMaxStepLoadRate (number): Signifies upstream maximum step load rate.
        - UpstreamMinBinaryLoadRate (number): Signifies the upstream binary load rate.
        - UpstreamStepFrameLossUnit (str(% | frames)): Signifies the upstream step frame loss unit.
        - UpstreamStepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies upstream step load unit.
        - UpstreamStepStepLoadRate (str): Signifies the upstream step load rate.
        - UpstreamStepTolerance (number): Signifies upstream step tolerance value.
        - UpstreamStopTestOnHighLoss (number): Signifies upstream stop test on high loss.
        - UpstreamUsePercentOffsets (str): Signifies upstream use percent offsets.

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
