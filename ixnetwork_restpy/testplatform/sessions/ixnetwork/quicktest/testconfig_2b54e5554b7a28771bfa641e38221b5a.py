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
        "BurstSize": "burstSize",
        "CalculateJitter": "calculateJitter",
        "CalculateLatency": "calculateLatency",
        "CalibrateLatency": "calibrateLatency",
        "CountRandomFrameSize": "countRandomFrameSize",
        "CountRandomIpRatio": "countRandomIpRatio",
        "CountRandomLoadRate": "countRandomLoadRate",
        "CustomLoadUnit": "customLoadUnit",
        "DelayAfterTransmit": "delayAfterTransmit",
        "DetailedResultsEnabled": "detailedResultsEnabled",
        "Duration": "duration",
        "EnableDataIntegrity": "enableDataIntegrity",
        "EnableLayer1Rate": "enableLayer1Rate",
        "EnableMinFrameSize": "enableMinFrameSize",
        "EnableOldStatsForReef": "enableOldStatsForReef",
        "EnableTxRealRate": "enableTxRealRate",
        "FloodedFramesEnabled": "floodedFramesEnabled",
        "ForceRegenerate": "forceRegenerate",
        "FrameSizeMode": "frameSizeMode",
        "FramesPerBurstGap": "framesPerBurstGap",
        "Framesize": "framesize",
        "FramesizeImixList": "framesizeImixList",
        "FramesizeList": "framesizeList",
        "Gap": "gap",
        "GenerateTrackingOptionAggregationFiles": "generateTrackingOptionAggregationFiles",
        "Grain": "grain",
        "ImixAdd": "imixAdd",
        "ImixData": "imixData",
        "ImixDelete": "imixDelete",
        "ImixDistribution": "imixDistribution",
        "ImixEnabled": "imixEnabled",
        "ImixTemplates": "imixTemplates",
        "ImixTrafficType": "imixTrafficType",
        "IncrementLoadUnit": "incrementLoadUnit",
        "InitialIncrementLoadRate": "initialIncrementLoadRate",
        "InitialStepLoadRate": "initialStepLoadRate",
        "IpRatioMode": "ipRatioMode",
        "Ipv4RatioList": "ipv4RatioList",
        "Ipv4rate": "ipv4rate",
        "Ipv6RatioList": "ipv6RatioList",
        "Ipv6rate": "ipv6rate",
        "LatencyBins": "latencyBins",
        "LatencyBinsEnabled": "latencyBinsEnabled",
        "LatencyType": "latencyType",
        "LoadRateList": "loadRateList",
        "LoadType": "loadType",
        "LoadUnit": "loadUnit",
        "MapType": "mapType",
        "MaxIncrementFrameSize": "maxIncrementFrameSize",
        "MaxIncrementIpv4Ratio": "maxIncrementIpv4Ratio",
        "MaxIncrementIpv6Ratio": "maxIncrementIpv6Ratio",
        "MaxIncrementLoadRate": "maxIncrementLoadRate",
        "MaxRandomFrameSize": "maxRandomFrameSize",
        "MaxRandomIpv4Ratio": "maxRandomIpv4Ratio",
        "MaxRandomIpv6Ratio": "maxRandomIpv6Ratio",
        "MaxRandomLoadRate": "maxRandomLoadRate",
        "MaxStepLoadRate": "maxStepLoadRate",
        "MinFpsRate": "minFpsRate",
        "MinIncrementFrameSize": "minIncrementFrameSize",
        "MinIncrementIpv4Ratio": "minIncrementIpv4Ratio",
        "MinIncrementIpv6Ratio": "minIncrementIpv6Ratio",
        "MinKbpsRate": "minKbpsRate",
        "MinRandomFrameSize": "minRandomFrameSize",
        "MinRandomIpv4Ratio": "minRandomIpv4Ratio",
        "MinRandomIpv6Ratio": "minRandomIpv6Ratio",
        "MinRandomLoadRate": "minRandomLoadRate",
        "MinStepLoadRate": "minStepLoadRate",
        "NumFrames": "numFrames",
        "Numtrials": "numtrials",
        "PeakLoadingReplicationCount": "peakLoadingReplicationCount",
        "PerTrafficResults": "perTrafficResults",
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
        "Rfc2544ImixDataQoS": "rfc2544ImixDataQoS",
        "Rfc2889ordering": "rfc2889ordering",
        "Runmode": "runmode",
        "ScaleTxRealRate": "scaleTxRealRate",
        "SendFullyMeshed": "sendFullyMeshed",
        "ShowDetailedBinaryResults": "showDetailedBinaryResults",
        "SpyderFramesizeList": "spyderFramesizeList",
        "StaggeredStart": "staggeredStart",
        "StepIncrementFrameSize": "stepIncrementFrameSize",
        "StepIncrementIpv4Ratio": "stepIncrementIpv4Ratio",
        "StepIncrementIpv6Ratio": "stepIncrementIpv6Ratio",
        "StepIncrementLoadRate": "stepIncrementLoadRate",
        "StepLoadRateFormula": "stepLoadRateFormula",
        "StepLoadUnit": "stepLoadUnit",
        "StepStepLoadRate": "stepStepLoadRate",
        "StepTiLoss": "stepTiLoss",
        "StepTolerance": "stepTolerance",
        "SupportedTrafficTypes": "supportedTrafficTypes",
        "Tolerance": "tolerance",
        "ToleranceTxRealRate": "toleranceTxRealRate",
        "TrafficProportions": "trafficProportions",
        "TrafficType": "trafficType",
        "TxDelay": "txDelay",
        "UnchangedValueList": "unchangedValueList",
        "UseTiLoss": "useTiLoss",
    }
    _SDM_ENUM_MAP = {
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
        "frameSizeMode": ["custom", "customlist", "increment", "random", "unchanged"],
        "grain": ["coarse", "fine"],
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
        "ipRatioMode": ["custom", "fixed", "increment", "random"],
        "latencyType": ["cutThrough", "forwardingDelay", "mef", "storeForward"],
        "loadType": ["step"],
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
        "rfc2889ordering": [
            "noOrdering",
            "peakLoading",
            "unchanged",
            "val2889Ordering",
        ],
        "runmode": ["duration", "noframes"],
        "scaleTxRealRate": ["%"],
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
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

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
    def CountRandomIpRatio(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the count of the random ip ratio loop
        """
        return self._get_attribute(self._SDM_ATT_MAP["CountRandomIpRatio"])

    @CountRandomIpRatio.setter
    def CountRandomIpRatio(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CountRandomIpRatio"], value)

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
        - number: Specifies the amount of delay after every transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"])

    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"], value)

    @property
    def DetailedResultsEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it enables the detailed results for the fully meshed case
        """
        return self._get_attribute(self._SDM_ATT_MAP["DetailedResultsEnabled"])

    @DetailedResultsEnabled.setter
    def DetailedResultsEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DetailedResultsEnabled"], value)

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
        - bool: If true, enables the checking of data integrity for the pass or fail of the trial.
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
    def EnableTxRealRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableTxRealRate"])

    @EnableTxRealRate.setter
    def EnableTxRealRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableTxRealRate"], value)

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
        # type: () -> List[str]
        """
        Returns
        -------
        - str(custom | customlist | increment | random | unchanged): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameSizeMode"])

    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameSizeMode"], value)

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
    def FramesizeImixList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The list of the available lmix frame sizes.
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
    def Grain(self):
        # type: () -> str
        """
        Returns
        -------
        - str(coarse | fine): The granular value of the test parameter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Grain"])

    @Grain.setter
    def Grain(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Grain"], value)

    @property
    def ImixAdd(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Adds an imix data.
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
        - str: Displays imix data.
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
        - str: Deletes an imix data.
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
        - str(bwpercentage | weight): Shows the distribution of imix data.
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
        - bool: If True, Enables the imix value.
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
        - str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal): Specefies the imix templates.
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
        - str: Displays the imix traffic type.
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
    def IpRatioMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | fixed | increment | random): Sets the ip ratio mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpRatioMode"])

    @IpRatioMode.setter
    def IpRatioMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpRatioMode"], value)

    @property
    def Ipv4RatioList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the ipv4 ratio list
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4RatioList"])

    @Ipv4RatioList.setter
    def Ipv4RatioList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4RatioList"], value)

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
    def Ipv6RatioList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the ipv6 ratio list
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6RatioList"])

    @Ipv6RatioList.setter
    def Ipv6RatioList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6RatioList"], value)

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
        - str(cutThrough | forwardingDelay | mef | storeForward): The type of latency.
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
    def LoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(step): The type of the payload setting.
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
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The load unit value.
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
        - str: The mapping type.
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
    def MaxIncrementIpv4Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the maximum increment value for the ipv4 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxIncrementIpv4Ratio"])

    @MaxIncrementIpv4Ratio.setter
    def MaxIncrementIpv4Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxIncrementIpv4Ratio"], value)

    @property
    def MaxIncrementIpv6Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the maximum increment value for the ipv6 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxIncrementIpv6Ratio"])

    @MaxIncrementIpv6Ratio.setter
    def MaxIncrementIpv6Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxIncrementIpv6Ratio"], value)

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
    def MaxRandomIpv4Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the maximum radom value for the ipv4 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxRandomIpv4Ratio"])

    @MaxRandomIpv4Ratio.setter
    def MaxRandomIpv4Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxRandomIpv4Ratio"], value)

    @property
    def MaxRandomIpv6Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the maximum random value for the ipv6 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxRandomIpv6Ratio"])

    @MaxRandomIpv6Ratio.setter
    def MaxRandomIpv6Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxRandomIpv6Ratio"], value)

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
    def MinIncrementIpv4Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the minimum increment value for the ipv4 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinIncrementIpv4Ratio"])

    @MinIncrementIpv4Ratio.setter
    def MinIncrementIpv4Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinIncrementIpv4Ratio"], value)

    @property
    def MinIncrementIpv6Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the minimum increment value for the ipv6 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinIncrementIpv6Ratio"])

    @MinIncrementIpv6Ratio.setter
    def MinIncrementIpv6Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinIncrementIpv6Ratio"], value)

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
    def MinRandomIpv4Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the minimum random value for the ipv4 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRandomIpv4Ratio"])

    @MinRandomIpv4Ratio.setter
    def MinRandomIpv4Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRandomIpv4Ratio"], value)

    @property
    def MinRandomIpv6Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the minimum random value for the ipv6 ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRandomIpv6Ratio"])

    @MinRandomIpv6Ratio.setter
    def MinRandomIpv6Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRandomIpv6Ratio"], value)

    @property
    def MinRandomLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum random value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRandomLoadRate"])

    @MinRandomLoadRate.setter
    def MinRandomLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRandomLoadRate"], value)

    @property
    def MinStepLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum step value of load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinStepLoadRate"])

    @MinStepLoadRate.setter
    def MinStepLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinStepLoadRate"], value)

    @property
    def NumFrames(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of frames sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumFrames"])

    @NumFrames.setter
    def NumFrames(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumFrames"], value)

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
    def PeakLoadingReplicationCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeakLoadingReplicationCount"])

    @PeakLoadingReplicationCount.setter
    def PeakLoadingReplicationCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PeakLoadingReplicationCount"], value)

    @property
    def PerTrafficResults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["PerTrafficResults"])

    @PerTrafficResults.setter
    def PerTrafficResults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PerTrafficResults"], value)

    @property
    def PercentMaxRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum percentage rate.
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
        - bool: Enables the port delay.
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
    def Rfc2544ImixDataQoS(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it uses the same frame data qos
        """
        return self._get_attribute(self._SDM_ATT_MAP["Rfc2544ImixDataQoS"])

    @Rfc2544ImixDataQoS.setter
    def Rfc2544ImixDataQoS(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Rfc2544ImixDataQoS"], value)

    @property
    def Rfc2889ordering(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noOrdering | peakLoading | unchanged | val2889Ordering): If true, indicates frame ordering by Rfc2889.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Rfc2889ordering"])

    @Rfc2889ordering.setter
    def Rfc2889ordering(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Rfc2889ordering"], value)

    @property
    def Runmode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(duration | noframes): Specifies the number of frames that IxNetwork sends from each port in running mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Runmode"])

    @Runmode.setter
    def Runmode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Runmode"], value)

    @property
    def ScaleTxRealRate(self):
        # type: () -> str
        """
        Returns
        -------
        - str(%):
        """
        return self._get_attribute(self._SDM_ATT_MAP["ScaleTxRealRate"])

    @ScaleTxRealRate.setter
    def ScaleTxRealRate(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ScaleTxRealRate"], value)

    @property
    def SendFullyMeshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates the source group mapping type used for sending data.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendFullyMeshed"])

    @SendFullyMeshed.setter
    def SendFullyMeshed(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendFullyMeshed"], value)

    @property
    def ShowDetailedBinaryResults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowDetailedBinaryResults"])

    @ShowDetailedBinaryResults.setter
    def ShowDetailedBinaryResults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowDetailedBinaryResults"], value)

    @property
    def SpyderFramesizeList(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:str[None | /api/v1/sessions/1/ixnetwork/quickTest/globals/customImix | /api/v1/sessions/1/ixnetwork/quickTest/globals/imix])):
        """
        return self._get_attribute(self._SDM_ATT_MAP["SpyderFramesizeList"])

    @SpyderFramesizeList.setter
    def SpyderFramesizeList(self, value):
        self._set_attribute(self._SDM_ATT_MAP["SpyderFramesizeList"], value)

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
    def StepIncrementIpv4Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The step in which the ipv4 ratio loop is incremented
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepIncrementIpv4Ratio"])

    @StepIncrementIpv4Ratio.setter
    def StepIncrementIpv4Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepIncrementIpv4Ratio"], value)

    @property
    def StepIncrementIpv6Ratio(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The step in which the ipv6 ratio loop is incremented
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepIncrementIpv6Ratio"])

    @StepIncrementIpv6Ratio.setter
    def StepIncrementIpv6Ratio(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepIncrementIpv6Ratio"], value)

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
    def StepLoadRateFormula(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepLoadRateFormula"])

    @StepLoadRateFormula.setter
    def StepLoadRateFormula(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepLoadRateFormula"], value)

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
    def StepTiLoss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepTiLoss"])

    @StepTiLoss.setter
    def StepTiLoss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepTiLoss"], value)

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
    def ToleranceTxRealRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ToleranceTxRealRate"])

    @ToleranceTxRealRate.setter
    def ToleranceTxRealRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ToleranceTxRealRate"], value)

    @property
    def TrafficProportions(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficProportions"])

    @TrafficProportions.setter
    def TrafficProportions(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficProportions"], value)

    @property
    def TrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(burstyLoading | constantLoading): The test based on the traffic type.
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
        - number: Specifies the amount of delay after every transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxDelay"])

    @TxDelay.setter
    def TxDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxDelay"], value)

    @property
    def UnchangedValueList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The number of unchanged sessions.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnchangedValueList"])

    @UnchangedValueList.setter
    def UnchangedValueList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnchangedValueList"], value)

    @property
    def UseTiLoss(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseTiLoss"])

    @UseTiLoss.setter
    def UseTiLoss(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseTiLoss"], value)

    def update(
        self,
        BurstSize=None,
        CalculateJitter=None,
        CalculateLatency=None,
        CalibrateLatency=None,
        CountRandomFrameSize=None,
        CountRandomIpRatio=None,
        CountRandomLoadRate=None,
        CustomLoadUnit=None,
        DelayAfterTransmit=None,
        DetailedResultsEnabled=None,
        Duration=None,
        EnableDataIntegrity=None,
        EnableLayer1Rate=None,
        EnableMinFrameSize=None,
        EnableOldStatsForReef=None,
        EnableTxRealRate=None,
        FloodedFramesEnabled=None,
        ForceRegenerate=None,
        FrameSizeMode=None,
        FramesPerBurstGap=None,
        Framesize=None,
        FramesizeImixList=None,
        FramesizeList=None,
        Gap=None,
        GenerateTrackingOptionAggregationFiles=None,
        Grain=None,
        ImixAdd=None,
        ImixData=None,
        ImixDelete=None,
        ImixDistribution=None,
        ImixEnabled=None,
        ImixTemplates=None,
        ImixTrafficType=None,
        IncrementLoadUnit=None,
        InitialIncrementLoadRate=None,
        InitialStepLoadRate=None,
        IpRatioMode=None,
        Ipv4RatioList=None,
        Ipv4rate=None,
        Ipv6RatioList=None,
        Ipv6rate=None,
        LatencyBins=None,
        LatencyBinsEnabled=None,
        LatencyType=None,
        LoadRateList=None,
        LoadType=None,
        LoadUnit=None,
        MapType=None,
        MaxIncrementFrameSize=None,
        MaxIncrementIpv4Ratio=None,
        MaxIncrementIpv6Ratio=None,
        MaxIncrementLoadRate=None,
        MaxRandomFrameSize=None,
        MaxRandomIpv4Ratio=None,
        MaxRandomIpv6Ratio=None,
        MaxRandomLoadRate=None,
        MaxStepLoadRate=None,
        MinFpsRate=None,
        MinIncrementFrameSize=None,
        MinIncrementIpv4Ratio=None,
        MinIncrementIpv6Ratio=None,
        MinKbpsRate=None,
        MinRandomFrameSize=None,
        MinRandomIpv4Ratio=None,
        MinRandomIpv6Ratio=None,
        MinRandomLoadRate=None,
        MinStepLoadRate=None,
        NumFrames=None,
        Numtrials=None,
        PeakLoadingReplicationCount=None,
        PerTrafficResults=None,
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
        Rfc2544ImixDataQoS=None,
        Rfc2889ordering=None,
        Runmode=None,
        ScaleTxRealRate=None,
        SendFullyMeshed=None,
        ShowDetailedBinaryResults=None,
        SpyderFramesizeList=None,
        StaggeredStart=None,
        StepIncrementFrameSize=None,
        StepIncrementIpv4Ratio=None,
        StepIncrementIpv6Ratio=None,
        StepIncrementLoadRate=None,
        StepLoadRateFormula=None,
        StepLoadUnit=None,
        StepStepLoadRate=None,
        StepTiLoss=None,
        StepTolerance=None,
        SupportedTrafficTypes=None,
        Tolerance=None,
        ToleranceTxRealRate=None,
        TrafficProportions=None,
        TrafficType=None,
        TxDelay=None,
        UnchangedValueList=None,
        UseTiLoss=None,
    ):
        """Updates testConfig resource on the server.

        Args
        ----
        - BurstSize (number): The number of packets to send in a burst.
        - CalculateJitter (bool): If true, the jitter is calculated.
        - CalculateLatency (bool): If true, calculates the latency.
        - CalibrateLatency (bool): If true, calibrates the latency.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - CountRandomIpRatio (number): Sets the count of the random ip ratio loop
        - CountRandomLoadRate (number): The random count of the load rate.
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the custom load unit.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - DetailedResultsEnabled (bool): If true, it enables the detailed results for the fully meshed case
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - EnableDataIntegrity (bool): If true, enables the checking of data integrity for the pass or fail of the trial.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableOldStatsForReef (bool): If true, enables old statistics for reef load module.
        - EnableTxRealRate (bool):
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameSizeMode (str(custom | customlist | increment | random | unchanged)): This attribute is the frame size mode for the Quad Gaussian.
        - FramesPerBurstGap (number): The number of frames to be sent after each burst.
        - Framesize (str): The frame size to be used.
        - FramesizeImixList (str): The list of the available lmix frame sizes.
        - FramesizeList (list(str)): The list of the available frame sizes.
        - Gap (number): The gap in transmission of frames.
        - GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
        - Grain (str(coarse | fine)): The granular value of the test parameter.
        - ImixAdd (str): Adds an imix data.
        - ImixData (str): Displays imix data.
        - ImixDelete (str): Deletes an imix data.
        - ImixDistribution (str(bwpercentage | weight)): Shows the distribution of imix data.
        - ImixEnabled (bool): If True, Enables the imix value.
        - ImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Specefies the imix templates.
        - ImixTrafficType (str): Displays the imix traffic type.
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The unit increment for the load.
        - InitialIncrementLoadRate (number): The initial incremental value of the load rate.
        - InitialStepLoadRate (number): The initial step value of the load rate.
        - IpRatioMode (str(custom | fixed | increment | random)): Sets the ip ratio mode
        - Ipv4RatioList (str): Sets the ipv4 ratio list
        - Ipv4rate (number): The rate at which IPv4 traffic is sent.
        - Ipv6RatioList (str): Sets the ipv6 ratio list
        - Ipv6rate (number): The rate at which IPv6 traffic is sent.
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LatencyType (str(cutThrough | forwardingDelay | mef | storeForward)): The type of latency.
        - LoadRateList (str): Enters the Load Rate List.
        - LoadType (str(step)): The type of the payload setting.
        - LoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The load unit value.
        - MapType (str): The mapping type.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxIncrementIpv4Ratio (str): Sets the maximum increment value for the ipv4 ratio
        - MaxIncrementIpv6Ratio (str): Sets the maximum increment value for the ipv6 ratio
        - MaxIncrementLoadRate (number): The maximum incremental value of the load rate.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxRandomIpv4Ratio (str): Sets the maximum radom value for the ipv4 ratio
        - MaxRandomIpv6Ratio (str): Sets the maximum random value for the ipv6 ratio
        - MaxRandomLoadRate (number): The maximum random value of the load rate.
        - MaxStepLoadRate (number): The maximum step value of the load rate.
        - MinFpsRate (number): The rate at which minimum frames are sent per second.
        - MinIncrementFrameSize (number): The minimum incremental value of the frame size.
        - MinIncrementIpv4Ratio (str): Sets the minimum increment value for the ipv4 ratio
        - MinIncrementIpv6Ratio (str): Sets the minimum increment value for the ipv6 ratio
        - MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - MinRandomIpv4Ratio (str): Sets the minimum random value for the ipv4 ratio
        - MinRandomIpv6Ratio (str): Sets the minimum random value for the ipv6 ratio
        - MinRandomLoadRate (number): The maximum random value of the load rate.
        - MinStepLoadRate (number): The minimum step value of load rate.
        - NumFrames (number): The number of frames sent.
        - Numtrials (number): The integer value that states the number of trials permitted.
        - PeakLoadingReplicationCount (number): NOT DEFINED
        - PerTrafficResults (bool):
        - PercentMaxRate (number): The maximum percentage rate.
        - PortDelayEnabled (bool): Enables the port delay.
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - RandomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The random values of the load unit.
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): The rate selected.
        - ReportSequenceError (bool): Reports sequence errors in the test result.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The unit of rate for throughput.
        - Resolution (number): Specify the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
        - Rfc2544ImixDataQoS (bool): If true, it uses the same frame data qos
        - Rfc2889ordering (str(noOrdering | peakLoading | unchanged | val2889Ordering)): If true, indicates frame ordering by Rfc2889.
        - Runmode (str(duration | noframes)): Specifies the number of frames that IxNetwork sends from each port in running mode.
        - ScaleTxRealRate (str(%)):
        - SendFullyMeshed (bool): Indicates the source group mapping type used for sending data.
        - ShowDetailedBinaryResults (bool):
        - SpyderFramesizeList (list(dict(arg1:number,arg2:str[None | /api/v1/sessions/1/ixnetwork/quickTest/globals/customImix | /api/v1/sessions/1/ixnetwork/quickTest/globals/imix]))):
        - StaggeredStart (bool): Starts test with a stagger.
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - StepIncrementIpv4Ratio (str): The step in which the ipv4 ratio loop is incremented
        - StepIncrementIpv6Ratio (str): The step in which the ipv6 ratio loop is incremented
        - StepIncrementLoadRate (number): The step incremental value of the load rate.
        - StepLoadRateFormula (str):
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the step rate of the load unit.
        - StepStepLoadRate (number): The incremental step value of load rate.
        - StepTiLoss (bool): NOT DEFINED
        - StepTolerance (number): The step value of the tolerance level.
        - SupportedTrafficTypes (str): The traffic types supported.
        - Tolerance (number): The value set for the tolerance level.
        - ToleranceTxRealRate (number):
        - TrafficProportions (str):
        - TrafficType (str(burstyLoading | constantLoading)): The test based on the traffic type.
        - TxDelay (number): Specifies the amount of delay after every transmit.
        - UnchangedValueList (str): The number of unchanged sessions.
        - UseTiLoss (str): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BurstSize=None,
        CalculateJitter=None,
        CalculateLatency=None,
        CalibrateLatency=None,
        CountRandomFrameSize=None,
        CountRandomIpRatio=None,
        CountRandomLoadRate=None,
        CustomLoadUnit=None,
        DelayAfterTransmit=None,
        DetailedResultsEnabled=None,
        Duration=None,
        EnableDataIntegrity=None,
        EnableLayer1Rate=None,
        EnableMinFrameSize=None,
        EnableOldStatsForReef=None,
        EnableTxRealRate=None,
        FloodedFramesEnabled=None,
        ForceRegenerate=None,
        FrameSizeMode=None,
        FramesPerBurstGap=None,
        Framesize=None,
        FramesizeImixList=None,
        FramesizeList=None,
        Gap=None,
        GenerateTrackingOptionAggregationFiles=None,
        Grain=None,
        ImixAdd=None,
        ImixData=None,
        ImixDelete=None,
        ImixDistribution=None,
        ImixEnabled=None,
        ImixTemplates=None,
        ImixTrafficType=None,
        IncrementLoadUnit=None,
        InitialIncrementLoadRate=None,
        InitialStepLoadRate=None,
        IpRatioMode=None,
        Ipv4RatioList=None,
        Ipv4rate=None,
        Ipv6RatioList=None,
        Ipv6rate=None,
        LatencyBins=None,
        LatencyBinsEnabled=None,
        LatencyType=None,
        LoadRateList=None,
        LoadType=None,
        LoadUnit=None,
        MapType=None,
        MaxIncrementFrameSize=None,
        MaxIncrementIpv4Ratio=None,
        MaxIncrementIpv6Ratio=None,
        MaxIncrementLoadRate=None,
        MaxRandomFrameSize=None,
        MaxRandomIpv4Ratio=None,
        MaxRandomIpv6Ratio=None,
        MaxRandomLoadRate=None,
        MaxStepLoadRate=None,
        MinFpsRate=None,
        MinIncrementFrameSize=None,
        MinIncrementIpv4Ratio=None,
        MinIncrementIpv6Ratio=None,
        MinKbpsRate=None,
        MinRandomFrameSize=None,
        MinRandomIpv4Ratio=None,
        MinRandomIpv6Ratio=None,
        MinRandomLoadRate=None,
        MinStepLoadRate=None,
        NumFrames=None,
        Numtrials=None,
        PeakLoadingReplicationCount=None,
        PerTrafficResults=None,
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
        Rfc2544ImixDataQoS=None,
        Rfc2889ordering=None,
        Runmode=None,
        ScaleTxRealRate=None,
        SendFullyMeshed=None,
        ShowDetailedBinaryResults=None,
        SpyderFramesizeList=None,
        StaggeredStart=None,
        StepIncrementFrameSize=None,
        StepIncrementIpv4Ratio=None,
        StepIncrementIpv6Ratio=None,
        StepIncrementLoadRate=None,
        StepLoadRateFormula=None,
        StepLoadUnit=None,
        StepStepLoadRate=None,
        StepTiLoss=None,
        StepTolerance=None,
        SupportedTrafficTypes=None,
        Tolerance=None,
        ToleranceTxRealRate=None,
        TrafficProportions=None,
        TrafficType=None,
        TxDelay=None,
        UnchangedValueList=None,
        UseTiLoss=None,
    ):
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - BurstSize (number): The number of packets to send in a burst.
        - CalculateJitter (bool): If true, the jitter is calculated.
        - CalculateLatency (bool): If true, calculates the latency.
        - CalibrateLatency (bool): If true, calibrates the latency.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - CountRandomIpRatio (number): Sets the count of the random ip ratio loop
        - CountRandomLoadRate (number): The random count of the load rate.
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the custom load unit.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - DetailedResultsEnabled (bool): If true, it enables the detailed results for the fully meshed case
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - EnableDataIntegrity (bool): If true, enables the checking of data integrity for the pass or fail of the trial.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableOldStatsForReef (bool): If true, enables old statistics for reef load module.
        - EnableTxRealRate (bool):
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameSizeMode (str(custom | customlist | increment | random | unchanged)): This attribute is the frame size mode for the Quad Gaussian.
        - FramesPerBurstGap (number): The number of frames to be sent after each burst.
        - Framesize (str): The frame size to be used.
        - FramesizeImixList (str): The list of the available lmix frame sizes.
        - FramesizeList (list(str)): The list of the available frame sizes.
        - Gap (number): The gap in transmission of frames.
        - GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
        - Grain (str(coarse | fine)): The granular value of the test parameter.
        - ImixAdd (str): Adds an imix data.
        - ImixData (str): Displays imix data.
        - ImixDelete (str): Deletes an imix data.
        - ImixDistribution (str(bwpercentage | weight)): Shows the distribution of imix data.
        - ImixEnabled (bool): If True, Enables the imix value.
        - ImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Specefies the imix templates.
        - ImixTrafficType (str): Displays the imix traffic type.
        - IncrementLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The unit increment for the load.
        - InitialIncrementLoadRate (number): The initial incremental value of the load rate.
        - InitialStepLoadRate (number): The initial step value of the load rate.
        - IpRatioMode (str(custom | fixed | increment | random)): Sets the ip ratio mode
        - Ipv4RatioList (str): Sets the ipv4 ratio list
        - Ipv4rate (number): The rate at which IPv4 traffic is sent.
        - Ipv6RatioList (str): Sets the ipv6 ratio list
        - Ipv6rate (number): The rate at which IPv6 traffic is sent.
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LatencyType (str(cutThrough | forwardingDelay | mef | storeForward)): The type of latency.
        - LoadRateList (str): Enters the Load Rate List.
        - LoadType (str(step)): The type of the payload setting.
        - LoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The load unit value.
        - MapType (str): The mapping type.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxIncrementIpv4Ratio (str): Sets the maximum increment value for the ipv4 ratio
        - MaxIncrementIpv6Ratio (str): Sets the maximum increment value for the ipv6 ratio
        - MaxIncrementLoadRate (number): The maximum incremental value of the load rate.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxRandomIpv4Ratio (str): Sets the maximum radom value for the ipv4 ratio
        - MaxRandomIpv6Ratio (str): Sets the maximum random value for the ipv6 ratio
        - MaxRandomLoadRate (number): The maximum random value of the load rate.
        - MaxStepLoadRate (number): The maximum step value of the load rate.
        - MinFpsRate (number): The rate at which minimum frames are sent per second.
        - MinIncrementFrameSize (number): The minimum incremental value of the frame size.
        - MinIncrementIpv4Ratio (str): Sets the minimum increment value for the ipv4 ratio
        - MinIncrementIpv6Ratio (str): Sets the minimum increment value for the ipv6 ratio
        - MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - MinRandomIpv4Ratio (str): Sets the minimum random value for the ipv4 ratio
        - MinRandomIpv6Ratio (str): Sets the minimum random value for the ipv6 ratio
        - MinRandomLoadRate (number): The maximum random value of the load rate.
        - MinStepLoadRate (number): The minimum step value of load rate.
        - NumFrames (number): The number of frames sent.
        - Numtrials (number): The integer value that states the number of trials permitted.
        - PeakLoadingReplicationCount (number): NOT DEFINED
        - PerTrafficResults (bool):
        - PercentMaxRate (number): The maximum percentage rate.
        - PortDelayEnabled (bool): Enables the port delay.
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - RandomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The random values of the load unit.
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): The rate selected.
        - ReportSequenceError (bool): Reports sequence errors in the test result.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The unit of rate for throughput.
        - Resolution (number): Specify the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
        - Rfc2544ImixDataQoS (bool): If true, it uses the same frame data qos
        - Rfc2889ordering (str(noOrdering | peakLoading | unchanged | val2889Ordering)): If true, indicates frame ordering by Rfc2889.
        - Runmode (str(duration | noframes)): Specifies the number of frames that IxNetwork sends from each port in running mode.
        - ScaleTxRealRate (str(%)):
        - SendFullyMeshed (bool): Indicates the source group mapping type used for sending data.
        - ShowDetailedBinaryResults (bool):
        - SpyderFramesizeList (list(dict(arg1:number,arg2:str[None | /api/v1/sessions/1/ixnetwork/quickTest/globals/customImix | /api/v1/sessions/1/ixnetwork/quickTest/globals/imix]))):
        - StaggeredStart (bool): Starts test with a stagger.
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - StepIncrementIpv4Ratio (str): The step in which the ipv4 ratio loop is incremented
        - StepIncrementIpv6Ratio (str): The step in which the ipv6 ratio loop is incremented
        - StepIncrementLoadRate (number): The step incremental value of the load rate.
        - StepLoadRateFormula (str):
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the step rate of the load unit.
        - StepStepLoadRate (number): The incremental step value of load rate.
        - StepTiLoss (bool): NOT DEFINED
        - StepTolerance (number): The step value of the tolerance level.
        - SupportedTrafficTypes (str): The traffic types supported.
        - Tolerance (number): The value set for the tolerance level.
        - ToleranceTxRealRate (number):
        - TrafficProportions (str):
        - TrafficType (str(burstyLoading | constantLoading)): The test based on the traffic type.
        - TxDelay (number): Specifies the amount of delay after every transmit.
        - UnchangedValueList (str): The number of unchanged sessions.
        - UseTiLoss (str): NOT DEFINED

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
