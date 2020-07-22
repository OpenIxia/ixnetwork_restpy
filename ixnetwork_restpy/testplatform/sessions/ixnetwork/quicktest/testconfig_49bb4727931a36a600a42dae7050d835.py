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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TestConfig(Base):
    """This object holds the attributes for Test Configuration parameters.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'BurstSize': 'burstSize',
        'CalculateJitter': 'calculateJitter',
        'CalculateLatency': 'calculateLatency',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'DownstreamGrain': 'downstreamGrain',
        'DownstreamImixAdd': 'downstreamImixAdd',
        'DownstreamImixData': 'downstreamImixData',
        'DownstreamImixDataQoS': 'downstreamImixDataQoS',
        'DownstreamImixDelete': 'downstreamImixDelete',
        'DownstreamImixDistribution': 'downstreamImixDistribution',
        'DownstreamImixEnabled': 'downstreamImixEnabled',
        'DownstreamImixTemplates': 'downstreamImixTemplates',
        'DownstreamInitialStepLoadRate': 'downstreamInitialStepLoadRate',
        'DownstreamLoadType': 'downstreamLoadType',
        'DownstreamStepLoadUnit': 'downstreamStepLoadUnit',
        'DownstreamStepStepLoadRate': 'downstreamStepStepLoadRate',
        'DownstreamStepTolerance': 'downstreamStepTolerance',
        'Duration': 'duration',
        'EnableDataIntegrity': 'enableDataIntegrity',
        'EnableLayer1Rate': 'enableLayer1Rate',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'ForceRegenerate': 'forceRegenerate',
        'FramesPerBurstGap': 'framesPerBurstGap',
        'Gap': 'gap',
        'GenerateTrackingOptionAggregationFiles': 'generateTrackingOptionAggregationFiles',
        'GranularityLabel': 'granularityLabel',
        'ImixTrafficType': 'imixTrafficType',
        'InitialRateLabel': 'initialRateLabel',
        'LatencyBins': 'latencyBins',
        'LatencyBinsEnabled': 'latencyBinsEnabled',
        'LatencyType': 'latencyType',
        'LoadType': 'loadType',
        'LoadUnitLabel': 'loadUnitLabel',
        'MapType': 'mapType',
        'NumFrames': 'numFrames',
        'Numtrials': 'numtrials',
        'PortDelayEnabled': 'portDelayEnabled',
        'PortDelayUnit': 'portDelayUnit',
        'PortDelayValue': 'portDelayValue',
        'ProtocolItem': 'protocolItem',
        'ReportSequenceError': 'reportSequenceError',
        'ReportTputRateUnit': 'reportTputRateUnit',
        'Runmode': 'runmode',
        'StaggeredStart': 'staggeredStart',
        'SupportedTrafficTypes': 'supportedTrafficTypes',
        'TestType': 'testType',
        'TestTypeTemp': 'testTypeTemp',
        'TestTypeTemp2': 'testTypeTemp2',
        'TrafficType': 'trafficType',
        'TxDelay': 'txDelay',
        'UpstreamGrain': 'upstreamGrain',
        'UpstreamImixAdd': 'upstreamImixAdd',
        'UpstreamImixData': 'upstreamImixData',
        'UpstreamImixDataQoS': 'upstreamImixDataQoS',
        'UpstreamImixDelete': 'upstreamImixDelete',
        'UpstreamImixDistribution': 'upstreamImixDistribution',
        'UpstreamImixEnabled': 'upstreamImixEnabled',
        'UpstreamImixTemplates': 'upstreamImixTemplates',
        'UpstreamInitialStepLoadRate': 'upstreamInitialStepLoadRate',
        'UpstreamLoadType': 'upstreamLoadType',
        'UpstreamStepLoadUnit': 'upstreamStepLoadUnit',
        'UpstreamStepStepLoadRate': 'upstreamStepStepLoadRate',
        'UpstreamStepTolerance': 'upstreamStepTolerance',
    }

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def BurstSize(self):
        """
        Returns
        -------
        - number: The number of packets to send in a burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurstSize'])
    @BurstSize.setter
    def BurstSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BurstSize'], value)

    @property
    def CalculateJitter(self):
        """
        Returns
        -------
        - bool: If true, calculates jitter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateJitter'])
    @CalculateJitter.setter
    def CalculateJitter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CalculateJitter'], value)

    @property
    def CalculateLatency(self):
        """
        Returns
        -------
        - bool: If true, calibrates the latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateLatency'])
    @CalculateLatency.setter
    def CalculateLatency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CalculateLatency'], value)

    @property
    def DelayAfterTransmit(self):
        """
        Returns
        -------
        - number: Specifies the amount of delay after every transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'])
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'], value)

    @property
    def DownstreamGrain(self):
        """
        Returns
        -------
        - str(coarse | fine): The type downstream grain.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamGrain'])
    @DownstreamGrain.setter
    def DownstreamGrain(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamGrain'], value)

    @property
    def DownstreamImixAdd(self):
        """
        Returns
        -------
        - str: Adds the IMIX for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamImixAdd'])
    @DownstreamImixAdd.setter
    def DownstreamImixAdd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamImixAdd'], value)

    @property
    def DownstreamImixData(self):
        """
        Returns
        -------
        - str: Signifies the downstream IMIX data
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamImixData'])
    @DownstreamImixData.setter
    def DownstreamImixData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamImixData'], value)

    @property
    def DownstreamImixDataQoS(self):
        """
        Returns
        -------
        - bool: Signifies the quality of service for downstream IMIX data
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamImixDataQoS'])
    @DownstreamImixDataQoS.setter
    def DownstreamImixDataQoS(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamImixDataQoS'], value)

    @property
    def DownstreamImixDelete(self):
        """
        Returns
        -------
        - str: Deletes the downstream IMIX value
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamImixDelete'])
    @DownstreamImixDelete.setter
    def DownstreamImixDelete(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamImixDelete'], value)

    @property
    def DownstreamImixDistribution(self):
        """
        Returns
        -------
        - str(bwpercentage | weight): It gives details about the down stream Imix distribution.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamImixDistribution'])
    @DownstreamImixDistribution.setter
    def DownstreamImixDistribution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamImixDistribution'], value)

    @property
    def DownstreamImixEnabled(self):
        """
        Returns
        -------
        - bool: If true, enables downstream IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamImixEnabled'])
    @DownstreamImixEnabled.setter
    def DownstreamImixEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamImixEnabled'], value)

    @property
    def DownstreamImixTemplates(self):
        """
        Returns
        -------
        - str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal): Signifies the downstream IMIX templates.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamImixTemplates'])
    @DownstreamImixTemplates.setter
    def DownstreamImixTemplates(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamImixTemplates'], value)

    @property
    def DownstreamInitialStepLoadRate(self):
        """
        Returns
        -------
        - number: Signifies downstream initial step load rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamInitialStepLoadRate'])
    @DownstreamInitialStepLoadRate.setter
    def DownstreamInitialStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamInitialStepLoadRate'], value)

    @property
    def DownstreamLoadType(self):
        """
        Returns
        -------
        - str(step): Signifies downstream load type
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLoadType'])
    @DownstreamLoadType.setter
    def DownstreamLoadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLoadType'], value)

    @property
    def DownstreamStepLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies downstream step load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamStepLoadUnit'])
    @DownstreamStepLoadUnit.setter
    def DownstreamStepLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamStepLoadUnit'], value)

    @property
    def DownstreamStepStepLoadRate(self):
        """
        Returns
        -------
        - str: Signifies downstream step load rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamStepStepLoadRate'])
    @DownstreamStepStepLoadRate.setter
    def DownstreamStepStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamStepStepLoadRate'], value)

    @property
    def DownstreamStepTolerance(self):
        """
        Returns
        -------
        - number: Signifies downstream step tolerance
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamStepTolerance'])
    @DownstreamStepTolerance.setter
    def DownstreamStepTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamStepTolerance'], value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: The duration of the test in hours, minutes, or seconds, which is used to calculate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])
    @Duration.setter
    def Duration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Duration'], value)

    @property
    def EnableDataIntegrity(self):
        """
        Returns
        -------
        - bool: Allows to do a data integrity check.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDataIntegrity'])
    @EnableDataIntegrity.setter
    def EnableDataIntegrity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDataIntegrity'], value)

    @property
    def EnableLayer1Rate(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLayer1Rate'])
    @EnableLayer1Rate.setter
    def EnableLayer1Rate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLayer1Rate'], value)

    @property
    def EnableMinFrameSize(self):
        """
        Returns
        -------
        - bool: If true, allows to set minimum frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'])
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'], value)

    @property
    def ForceRegenerate(self):
        """
        Returns
        -------
        - bool: Initiates a forced regeneration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceRegenerate'])
    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForceRegenerate'], value)

    @property
    def FramesPerBurstGap(self):
        """
        Returns
        -------
        - number: Specifies the per burst gap.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesPerBurstGap'])
    @FramesPerBurstGap.setter
    def FramesPerBurstGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FramesPerBurstGap'], value)

    @property
    def Gap(self):
        """
        Returns
        -------
        - number: The inter burst gap.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gap'])
    @Gap.setter
    def Gap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Gap'], value)

    @property
    def GenerateTrackingOptionAggregationFiles(self):
        """
        Returns
        -------
        - bool: Generates tracking option on aggregation files.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GenerateTrackingOptionAggregationFiles'])
    @GenerateTrackingOptionAggregationFiles.setter
    def GenerateTrackingOptionAggregationFiles(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GenerateTrackingOptionAggregationFiles'], value)

    @property
    def GranularityLabel(self):
        """
        Returns
        -------
        - str: Signifies the granulity label
        """
        return self._get_attribute(self._SDM_ATT_MAP['GranularityLabel'])
    @GranularityLabel.setter
    def GranularityLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GranularityLabel'], value)

    @property
    def ImixTrafficType(self):
        """
        Returns
        -------
        - str: Signifies the traffic type for IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP['ImixTrafficType'])
    @ImixTrafficType.setter
    def ImixTrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ImixTrafficType'], value)

    @property
    def InitialRateLabel(self):
        """
        Returns
        -------
        - str: Signifies the initial rate label
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialRateLabel'])
    @InitialRateLabel.setter
    def InitialRateLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialRateLabel'], value)

    @property
    def LatencyBins(self):
        """DEPRECATED 
        Returns
        -------
        - str: Sets the latency bins statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyBins'])
    @LatencyBins.setter
    def LatencyBins(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyBins'], value)

    @property
    def LatencyBinsEnabled(self):
        """
        Returns
        -------
        - bool: Enables the latency bins statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyBinsEnabled'])
    @LatencyBinsEnabled.setter
    def LatencyBinsEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyBinsEnabled'], value)

    @property
    def LatencyType(self):
        """
        Returns
        -------
        - str(cutThrough | storeForward): The latency type, either Cut Through or Store and Forward.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyType'])
    @LatencyType.setter
    def LatencyType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyType'], value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(step): The latency type, either Cut Through or Store and Forward.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadType'])
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadType'], value)

    @property
    def LoadUnitLabel(self):
        """
        Returns
        -------
        - str: Signifies the load unit label
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadUnitLabel'])
    @LoadUnitLabel.setter
    def LoadUnitLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadUnitLabel'], value)

    @property
    def MapType(self):
        """
        Returns
        -------
        - str: The map type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapType'])
    @MapType.setter
    def MapType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MapType'], value)

    @property
    def NumFrames(self):
        """
        Returns
        -------
        - number: Number of frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumFrames'])
    @NumFrames.setter
    def NumFrames(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumFrames'], value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: Number of trials.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def PortDelayEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayEnabled'])
    @PortDelayEnabled.setter
    def PortDelayEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayEnabled'], value)

    @property
    def PortDelayUnit(self):
        """
        Returns
        -------
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayUnit'])
    @PortDelayUnit.setter
    def PortDelayUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayUnit'], value)

    @property
    def PortDelayValue(self):
        """
        Returns
        -------
        - number: Sets the port delay value
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayValue'])
    @PortDelayValue.setter
    def PortDelayValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayValue'], value)

    @property
    def ProtocolItem(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan]): Protocol Items
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolItem'])
    @ProtocolItem.setter
    def ProtocolItem(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolItem'], value)

    @property
    def ReportSequenceError(self):
        """
        Returns
        -------
        - bool: Specifies to include the types of sequence errors in the results, such as Small.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportSequenceError'])
    @ReportSequenceError.setter
    def ReportSequenceError(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReportSequenceError'], value)

    @property
    def ReportTputRateUnit(self):
        """
        Returns
        -------
        - str(gbps | gBps | kbps | kBps | mbps | mBps): The throughput rate unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportTputRateUnit'])
    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReportTputRateUnit'], value)

    @property
    def Runmode(self):
        """
        Returns
        -------
        - str(duration | noframes): The running mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Runmode'])
    @Runmode.setter
    def Runmode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Runmode'], value)

    @property
    def StaggeredStart(self):
        """
        Returns
        -------
        - bool: Enable a staggered start to traffic transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StaggeredStart'])
    @StaggeredStart.setter
    def StaggeredStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StaggeredStart'], value)

    @property
    def SupportedTrafficTypes(self):
        """
        Returns
        -------
        - str: The supported traffic types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'])
    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'], value)

    @property
    def TestType(self):
        """
        Returns
        -------
        - str(downstreamOnly | upstreamDownstream | upstreamOnly): Signifies the test type
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestType'])
    @TestType.setter
    def TestType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestType'], value)

    @property
    def TestTypeTemp(self):
        """
        Returns
        -------
        - str(downstreamOnly | upstreamDownstream | upstreamOnly): Signifies the temporary test type
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestTypeTemp'])
    @TestTypeTemp.setter
    def TestTypeTemp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestTypeTemp'], value)

    @property
    def TestTypeTemp2(self):
        """
        Returns
        -------
        - str(downstreamOnly | upstreamDownstream | upstreamOnly): Signifies the second termorary version of test type
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestTypeTemp2'])
    @TestTypeTemp2.setter
    def TestTypeTemp2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestTypeTemp2'], value)

    @property
    def TrafficType(self):
        """
        Returns
        -------
        - str(burstyLoading | constantLoading): The type of traffic to be transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficType'])
    @TrafficType.setter
    def TrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficType'], value)

    @property
    def TxDelay(self):
        """
        Returns
        -------
        - number: The delay in transmission.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxDelay'])
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxDelay'], value)

    @property
    def UpstreamGrain(self):
        """
        Returns
        -------
        - str(coarse | fine): The upstream traffic grain type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamGrain'])
    @UpstreamGrain.setter
    def UpstreamGrain(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamGrain'], value)

    @property
    def UpstreamImixAdd(self):
        """
        Returns
        -------
        - str: Adds IMIX upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamImixAdd'])
    @UpstreamImixAdd.setter
    def UpstreamImixAdd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamImixAdd'], value)

    @property
    def UpstreamImixData(self):
        """
        Returns
        -------
        - str: Signifies the data of upstream IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamImixData'])
    @UpstreamImixData.setter
    def UpstreamImixData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamImixData'], value)

    @property
    def UpstreamImixDataQoS(self):
        """
        Returns
        -------
        - bool: Signifies the quality of service for upstream IMIX data
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamImixDataQoS'])
    @UpstreamImixDataQoS.setter
    def UpstreamImixDataQoS(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamImixDataQoS'], value)

    @property
    def UpstreamImixDelete(self):
        """
        Returns
        -------
        - str: Deletes upstream IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamImixDelete'])
    @UpstreamImixDelete.setter
    def UpstreamImixDelete(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamImixDelete'], value)

    @property
    def UpstreamImixDistribution(self):
        """
        Returns
        -------
        - str(bwpercentage | weight): Signifies the distribution of upstream IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamImixDistribution'])
    @UpstreamImixDistribution.setter
    def UpstreamImixDistribution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamImixDistribution'], value)

    @property
    def UpstreamImixEnabled(self):
        """
        Returns
        -------
        - bool: If true, enables upstream IMIX
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamImixEnabled'])
    @UpstreamImixEnabled.setter
    def UpstreamImixEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamImixEnabled'], value)

    @property
    def UpstreamImixTemplates(self):
        """
        Returns
        -------
        - str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal): Signifies the upstream IMIX templates.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamImixTemplates'])
    @UpstreamImixTemplates.setter
    def UpstreamImixTemplates(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamImixTemplates'], value)

    @property
    def UpstreamInitialStepLoadRate(self):
        """
        Returns
        -------
        - number: Signifies upstream initial step load rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamInitialStepLoadRate'])
    @UpstreamInitialStepLoadRate.setter
    def UpstreamInitialStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamInitialStepLoadRate'], value)

    @property
    def UpstreamLoadType(self):
        """
        Returns
        -------
        - str(step): Signifies upstream load type
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLoadType'])
    @UpstreamLoadType.setter
    def UpstreamLoadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLoadType'], value)

    @property
    def UpstreamStepLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Signifies upstream step load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamStepLoadUnit'])
    @UpstreamStepLoadUnit.setter
    def UpstreamStepLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamStepLoadUnit'], value)

    @property
    def UpstreamStepStepLoadRate(self):
        """
        Returns
        -------
        - str: Signifies the upstream step load rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamStepStepLoadRate'])
    @UpstreamStepStepLoadRate.setter
    def UpstreamStepStepLoadRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamStepStepLoadRate'], value)

    @property
    def UpstreamStepTolerance(self):
        """
        Returns
        -------
        - number: Signifies upstream step tolerance value
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamStepTolerance'])
    @UpstreamStepTolerance.setter
    def UpstreamStepTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamStepTolerance'], value)

    def update(self, BurstSize=None, CalculateJitter=None, CalculateLatency=None, DelayAfterTransmit=None, DownstreamGrain=None, DownstreamImixAdd=None, DownstreamImixData=None, DownstreamImixDataQoS=None, DownstreamImixDelete=None, DownstreamImixDistribution=None, DownstreamImixEnabled=None, DownstreamImixTemplates=None, DownstreamInitialStepLoadRate=None, DownstreamLoadType=None, DownstreamStepLoadUnit=None, DownstreamStepStepLoadRate=None, DownstreamStepTolerance=None, Duration=None, EnableDataIntegrity=None, EnableLayer1Rate=None, EnableMinFrameSize=None, ForceRegenerate=None, FramesPerBurstGap=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, GranularityLabel=None, ImixTrafficType=None, InitialRateLabel=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadType=None, LoadUnitLabel=None, MapType=None, NumFrames=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, ReportSequenceError=None, ReportTputRateUnit=None, Runmode=None, StaggeredStart=None, SupportedTrafficTypes=None, TestType=None, TestTypeTemp=None, TestTypeTemp2=None, TrafficType=None, TxDelay=None, UpstreamGrain=None, UpstreamImixAdd=None, UpstreamImixData=None, UpstreamImixDataQoS=None, UpstreamImixDelete=None, UpstreamImixDistribution=None, UpstreamImixEnabled=None, UpstreamImixTemplates=None, UpstreamInitialStepLoadRate=None, UpstreamLoadType=None, UpstreamStepLoadUnit=None, UpstreamStepStepLoadRate=None, UpstreamStepTolerance=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - BurstSize (number): The number of packets to send in a burst.
        - CalculateJitter (bool): If true, calculates jitter.
        - CalculateLatency (bool): If true, calibrates the latency.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - DownstreamGrain (str(coarse | fine)): The type downstream grain.
        - DownstreamImixAdd (str): Adds the IMIX for downstream.
        - DownstreamImixData (str): Signifies the downstream IMIX data
        - DownstreamImixDataQoS (bool): Signifies the quality of service for downstream IMIX data
        - DownstreamImixDelete (str): Deletes the downstream IMIX value
        - DownstreamImixDistribution (str(bwpercentage | weight)): It gives details about the down stream Imix distribution.
        - DownstreamImixEnabled (bool): If true, enables downstream IMIX
        - DownstreamImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Signifies the downstream IMIX templates.
        - DownstreamInitialStepLoadRate (number): Signifies downstream initial step load rate
        - DownstreamLoadType (str(step)): Signifies downstream load type
        - DownstreamStepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies downstream step load unit.
        - DownstreamStepStepLoadRate (str): Signifies downstream step load rate
        - DownstreamStepTolerance (number): Signifies downstream step tolerance
        - Duration (number): The duration of the test in hours, minutes, or seconds, which is used to calculate.
        - EnableDataIntegrity (bool): Allows to do a data integrity check.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableMinFrameSize (bool): If true, allows to set minimum frame size.
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FramesPerBurstGap (number): Specifies the per burst gap.
        - Gap (number): The inter burst gap.
        - GenerateTrackingOptionAggregationFiles (bool): Generates tracking option on aggregation files.
        - GranularityLabel (str): Signifies the granulity label
        - ImixTrafficType (str): Signifies the traffic type for IMIX
        - InitialRateLabel (str): Signifies the initial rate label
        - LatencyBins (str): Sets the latency bins statistics.
        - LatencyBinsEnabled (bool): Enables the latency bins statistics.
        - LatencyType (str(cutThrough | storeForward)): The latency type, either Cut Through or Store and Forward.
        - LoadType (str(step)): The latency type, either Cut Through or Store and Forward.
        - LoadUnitLabel (str): Signifies the load unit label
        - MapType (str): The map type.
        - NumFrames (number): Number of frames.
        - Numtrials (number): Number of trials.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - ReportSequenceError (bool): Specifies to include the types of sequence errors in the results, such as Small.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The throughput rate unit.
        - Runmode (str(duration | noframes)): The running mode.
        - StaggeredStart (bool): Enable a staggered start to traffic transmit.
        - SupportedTrafficTypes (str): The supported traffic types.
        - TestType (str(downstreamOnly | upstreamDownstream | upstreamOnly)): Signifies the test type
        - TestTypeTemp (str(downstreamOnly | upstreamDownstream | upstreamOnly)): Signifies the temporary test type
        - TestTypeTemp2 (str(downstreamOnly | upstreamDownstream | upstreamOnly)): Signifies the second termorary version of test type
        - TrafficType (str(burstyLoading | constantLoading)): The type of traffic to be transmitted.
        - TxDelay (number): The delay in transmission.
        - UpstreamGrain (str(coarse | fine)): The upstream traffic grain type.
        - UpstreamImixAdd (str): Adds IMIX upstream.
        - UpstreamImixData (str): Signifies the data of upstream IMIX
        - UpstreamImixDataQoS (bool): Signifies the quality of service for upstream IMIX data
        - UpstreamImixDelete (str): Deletes upstream IMIX
        - UpstreamImixDistribution (str(bwpercentage | weight)): Signifies the distribution of upstream IMIX
        - UpstreamImixEnabled (bool): If true, enables upstream IMIX
        - UpstreamImixTemplates (str(cisco | imix | ipsec | ipv6 | none | quadmodal | standard | tcp | tolly | trimodal)): Signifies the upstream IMIX templates.
        - UpstreamInitialStepLoadRate (number): Signifies upstream initial step load rate
        - UpstreamLoadType (str(step)): Signifies upstream load type
        - UpstreamStepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Signifies upstream step load unit.
        - UpstreamStepStepLoadRate (str): Signifies the upstream step load rate
        - UpstreamStepTolerance (number): Signifies upstream step tolerance value

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def Apply(self):
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('apply', payload=payload, response_object=None)

    def ApplyAsync(self):
        """Executes the applyAsync operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsync', payload=payload, response_object=None)

    def ApplyAsyncResult(self):
        """Executes the applyAsyncResult operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsyncResult', payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self):
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

    def GenerateReport(self):
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('generateReport', payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(InputParameters=string)list
        -------------------------------
        - InputParameters (str): The input arguments of the test.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('run', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(InputParameters=string)
        -----------------------------
        - InputParameters (str): The input arguments of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)

    def WaitForTest(self):
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('waitForTest', payload=payload, response_object=None)
