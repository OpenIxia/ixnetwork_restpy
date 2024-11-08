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


class Traffic(Base):
    """The traffic object allows the user to create millions of traffic flows for validating emulated networks and hosts. This is the top-level object for traffic configuration.
    The Traffic class encapsulates a required traffic resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "traffic"
    _SDM_ATT_MAP = {
        "AutoCorrectL4HeaderChecksums": "autoCorrectL4HeaderChecksums",
        "CycleOffsetForScheduledStart": "cycleOffsetForScheduledStart",
        "CycleOffsetUnitForScheduledStart": "cycleOffsetUnitForScheduledStart",
        "CycleTimeForScheduledStart": "cycleTimeForScheduledStart",
        "CycleTimeUnitForScheduledStart": "cycleTimeUnitForScheduledStart",
        "DataPlaneJitterWindow": "dataPlaneJitterWindow",
        "DelayTimeForScheduledStart": "delayTimeForScheduledStart",
        "DestMacRetryCount": "destMacRetryCount",
        "DestMacRetryDelay": "destMacRetryDelay",
        "DetectMisdirectedOnAllPorts": "detectMisdirectedOnAllPorts",
        "DisablePortLevelMisdirected": "disablePortLevelMisdirected",
        "DisplayMplsCurrentLabelValue": "displayMplsCurrentLabelValue",
        "EgressOnlyTrafficItemName": "egressOnlyTrafficItemName",
        "ElapsedTransmitTime": "elapsedTransmitTime",
        "EnableDataIntegrityCheck": "enableDataIntegrityCheck",
        "EnableDestMacRetry": "enableDestMacRetry",
        "EnableEgressOnlyTracking": "enableEgressOnlyTracking",
        "EnableEgressOnlyTxStats": "enableEgressOnlyTxStats",
        "EnableInstantaneousStatsSupport": "enableInstantaneousStatsSupport",
        "EnableLagAutoRate": "enableLagAutoRate",
        "EnableLagFlowBalancing": "enableLagFlowBalancing",
        "EnableLagFlowFailoverMode": "enableLagFlowFailoverMode",
        "EnableLagRebalanceOnPortUp": "enableLagRebalanceOnPortUp",
        "EnableMinFrameSize": "enableMinFrameSize",
        "EnableMulticastScalingFactor": "enableMulticastScalingFactor",
        "EnablePortLevelMisdirectedRoCEv2": "enablePortLevelMisdirectedRoCEv2",
        "EnableSequenceChecking": "enableSequenceChecking",
        "EnableStaggeredStartDelay": "enableStaggeredStartDelay",
        "EnableStaggeredTransmit": "enableStaggeredTransmit",
        "EnableStreamOrdering": "enableStreamOrdering",
        "FrameOrderingMode": "frameOrderingMode",
        "GlobalStreamControl": "globalStreamControl",
        "GlobalStreamControlIterations": "globalStreamControlIterations",
        "IsApplicationTrafficRunning": "isApplicationTrafficRunning",
        "IsApplyOnTheFlyRequired": "isApplyOnTheFlyRequired",
        "IsTrafficRunning": "isTrafficRunning",
        "LargeErrorThreshhold": "largeErrorThreshhold",
        "LearningFrameSize": "learningFrameSize",
        "LearningFramesCount": "learningFramesCount",
        "LearningFramesRate": "learningFramesRate",
        "MacChangeOnFly": "macChangeOnFly",
        "MaxTrafficGenerationQueries": "maxTrafficGenerationQueries",
        "MinimumSignatureLength": "minimumSignatureLength",
        "MplsLabelLearningTimeout": "mplsLabelLearningTimeout",
        "PeakLoadingReplicationCount": "peakLoadingReplicationCount",
        "PreventDataPlaneToCpu": "preventDataPlaneToCpu",
        "RefreshLearnedInfoBeforeApply": "refreshLearnedInfoBeforeApply",
        "State": "state",
        "TrafficItemsChanged": "trafficItemsChanged",
        "UseRfc5952": "useRfc5952",
        "UseScheduledStartTransmit": "useScheduledStartTransmit",
        "UseTxRxSync": "useTxRxSync",
        "WaitTime": "waitTime",
    }
    _SDM_ENUM_MAP = {
        "cycleOffsetUnitForScheduledStart": [
            "microseconds",
            "milliseconds",
            "nanoseconds",
            "seconds",
        ],
        "cycleTimeUnitForScheduledStart": [
            "microseconds",
            "milliseconds",
            "nanoseconds",
            "seconds",
        ],
        "dataPlaneJitterWindow": [
            "0",
            "10485760",
            "1310720",
            "167772160",
            "20971520",
            "2621440",
            "335544320",
            "41943040",
            "5242880",
            "671088640",
            "83886080",
        ],
        "frameOrderingMode": ["flowGroupSetup", "none", "peakLoading", "RFC2889"],
        "globalStreamControl": ["continuous", "iterations"],
        "state": [
            "error",
            "locked",
            "started",
            "startedWaitingForStats",
            "startedWaitingForStreams",
            "stopped",
            "stoppedWaitingForStats",
            "txStopWatchExpected",
            "unapplied",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Traffic, self).__init__(parent, list_op)

    @property
    def DynamicFrameSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.dynamicframesize.dynamicframesize.DynamicFrameSize): An instance of the DynamicFrameSize class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.dynamicframesize.dynamicframesize import (
            DynamicFrameSize,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DynamicFrameSize", None) is not None:
                return self._properties.get("DynamicFrameSize")
        return DynamicFrameSize(self)

    @property
    def DynamicRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.dynamicrate.dynamicrate.DynamicRate): An instance of the DynamicRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.dynamicrate.dynamicrate import (
            DynamicRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DynamicRate", None) is not None:
                return self._properties.get("DynamicRate")
        return DynamicRate(self)

    @property
    def EgressOnlyTracking(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.egressonlytracking.egressonlytracking.EgressOnlyTracking): An instance of the EgressOnlyTracking class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.egressonlytracking.egressonlytracking import (
            EgressOnlyTracking,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EgressOnlyTracking", None) is not None:
                return self._properties.get("EgressOnlyTracking")
        return EgressOnlyTracking(self)

    @property
    def ProtocolTemplate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.protocoltemplate.protocoltemplate.ProtocolTemplate): An instance of the ProtocolTemplate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.protocoltemplate.protocoltemplate import (
            ProtocolTemplate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ProtocolTemplate", None) is not None:
                return self._properties.get("ProtocolTemplate")
        return ProtocolTemplate(self)

    @property
    def RoceV2Traffic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.rocev2traffic.rocev2traffic.RoceV2Traffic): An instance of the RoceV2Traffic class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.rocev2traffic.rocev2traffic import (
            RoceV2Traffic,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RoceV2Traffic", None) is not None:
                return self._properties.get("RoceV2Traffic")
        return RoceV2Traffic(self)._select()

    @property
    def Statistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.statistics.Statistics): An instance of the Statistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.statistics import (
            Statistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Statistics", None) is not None:
                return self._properties.get("Statistics")
        return Statistics(self)._select()

    @property
    def TrafficGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficgroup.trafficgroup.TrafficGroup): An instance of the TrafficGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficgroup.trafficgroup import (
            TrafficGroup,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficGroup", None) is not None:
                return self._properties.get("TrafficGroup")
        return TrafficGroup(self)

    @property
    def TrafficItem(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.trafficitem.TrafficItem): An instance of the TrafficItem class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.trafficitem import (
            TrafficItem,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficItem", None) is not None:
                return self._properties.get("TrafficItem")
        return TrafficItem(self)

    @property
    def AutoCorrectL4HeaderChecksums(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This is used for Multis and Xdensity as checksum is not calculated correctly when change on the fly operations are performed. When this option is enabled IxOS uses 2 bytes before CRC, that way ensuring the checksum is correct when change on the fly operations are performed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoCorrectL4HeaderChecksums"])

    @AutoCorrectL4HeaderChecksums.setter
    def AutoCorrectL4HeaderChecksums(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoCorrectL4HeaderChecksums"], value)

    @property
    def CycleOffsetForScheduledStart(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["CycleOffsetForScheduledStart"])

    @CycleOffsetForScheduledStart.setter
    def CycleOffsetForScheduledStart(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CycleOffsetForScheduledStart"], value)

    @property
    def CycleOffsetUnitForScheduledStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str(microseconds | milliseconds | nanoseconds | seconds):
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["CycleOffsetUnitForScheduledStart"]
        )

    @CycleOffsetUnitForScheduledStart.setter
    def CycleOffsetUnitForScheduledStart(self, value):
        # type: (str) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["CycleOffsetUnitForScheduledStart"], value
        )

    @property
    def CycleTimeForScheduledStart(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["CycleTimeForScheduledStart"])

    @CycleTimeForScheduledStart.setter
    def CycleTimeForScheduledStart(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CycleTimeForScheduledStart"], value)

    @property
    def CycleTimeUnitForScheduledStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str(microseconds | milliseconds | nanoseconds | seconds):
        """
        return self._get_attribute(self._SDM_ATT_MAP["CycleTimeUnitForScheduledStart"])

    @CycleTimeUnitForScheduledStart.setter
    def CycleTimeUnitForScheduledStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CycleTimeUnitForScheduledStart"], value)

    @property
    def DataPlaneJitterWindow(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(0 | 10485760 | 1310720 | 167772160 | 20971520 | 2621440 | 335544320 | 41943040 | 5242880 | 671088640 | 83886080): Indicates the number of packets received during a time interval. This is used for calculating the rate on the recieve side
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPlaneJitterWindow"])

    @DataPlaneJitterWindow.setter
    def DataPlaneJitterWindow(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataPlaneJitterWindow"], value)

    @property
    def DelayTimeForScheduledStart(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Delay Time For Scheduled Start Transmit in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayTimeForScheduledStart"])

    @DelayTimeForScheduledStart.setter
    def DelayTimeForScheduledStart(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayTimeForScheduledStart"], value)

    @property
    def DestMacRetryCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of time to attempt to obtain the destination MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestMacRetryCount"])

    @DestMacRetryCount.setter
    def DestMacRetryCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestMacRetryCount"], value)

    @property
    def DestMacRetryDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of seconds to wait between attempts to obtain the destination MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestMacRetryDelay"])

    @DestMacRetryDelay.setter
    def DestMacRetryDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestMacRetryDelay"], value)

    @property
    def DetectMisdirectedOnAllPorts(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["DetectMisdirectedOnAllPorts"])

    @DetectMisdirectedOnAllPorts.setter
    def DetectMisdirectedOnAllPorts(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DetectMisdirectedOnAllPorts"], value)

    @property
    def DisablePortLevelMisdirected(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisablePortLevelMisdirected"])

    @DisablePortLevelMisdirected.setter
    def DisablePortLevelMisdirected(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisablePortLevelMisdirected"], value)

    @property
    def DisplayMplsCurrentLabelValue(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Displays current label value for LSP Endpoints.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisplayMplsCurrentLabelValue"])

    @DisplayMplsCurrentLabelValue.setter
    def DisplayMplsCurrentLabelValue(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisplayMplsCurrentLabelValue"], value)

    @property
    def EgressOnlyTrafficItemName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Traffic Item name for egress only flows in statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EgressOnlyTrafficItemName"])

    @EgressOnlyTrafficItemName.setter
    def EgressOnlyTrafficItemName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EgressOnlyTrafficItemName"], value)

    @property
    def ElapsedTransmitTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the amount of time traffic is running in milliseconds. If the traffic state is unapplied or errored then the transmit time will be 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ElapsedTransmitTime"])

    @property
    def EnableDataIntegrityCheck(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enable data integrity check.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDataIntegrityCheck"])

    @EnableDataIntegrityCheck.setter
    def EnableDataIntegrityCheck(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDataIntegrityCheck"], value)

    @property
    def EnableDestMacRetry(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the destination MAC address retry function.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDestMacRetry"])

    @EnableDestMacRetry.setter
    def EnableDestMacRetry(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDestMacRetry"], value)

    @property
    def EnableEgressOnlyTracking(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This flags enables/disables egress only tracking. In this mode only traffic without ingress tracking is supported on ports with egress only settings, user will have only PGID stats and the packets will not contain any instrumentation block.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableEgressOnlyTracking"])

    @EnableEgressOnlyTracking.setter
    def EnableEgressOnlyTracking(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableEgressOnlyTracking"], value)

    @property
    def EnableEgressOnlyTxStats(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This flags enables/disables egress only tx stats. In this mode all traffic without ingress tracking is considered for tx stats.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableEgressOnlyTxStats"])

    @EnableEgressOnlyTxStats.setter
    def EnableEgressOnlyTxStats(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableEgressOnlyTxStats"], value)

    @property
    def EnableInstantaneousStatsSupport(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables instantaneous stats support
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableInstantaneousStatsSupport"])

    @EnableInstantaneousStatsSupport.setter
    def EnableInstantaneousStatsSupport(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableInstantaneousStatsSupport"], value)

    @property
    def EnableLagAutoRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLagAutoRate"])

    @EnableLagAutoRate.setter
    def EnableLagAutoRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLagAutoRate"], value)

    @property
    def EnableLagFlowBalancing(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLagFlowBalancing"])

    @EnableLagFlowBalancing.setter
    def EnableLagFlowBalancing(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLagFlowBalancing"], value)

    @property
    def EnableLagFlowFailoverMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLagFlowFailoverMode"])

    @EnableLagFlowFailoverMode.setter
    def EnableLagFlowFailoverMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLagFlowFailoverMode"], value)

    @property
    def EnableLagRebalanceOnPortUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLagRebalanceOnPortUp"])

    @EnableLagRebalanceOnPortUp.setter
    def EnableLagRebalanceOnPortUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLagRebalanceOnPortUp"], value)

    @property
    def EnableMinFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, IxNetwork allows the stream to use smaller packet sizes. (In the case of IPv4 and Ethernet, 64 bytes are allowed.) This is achieved by reducing the size of the instrumentation tag, which is identified by the receiving ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMinFrameSize"])

    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMinFrameSize"], value)

    @property
    def EnableMulticastScalingFactor(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, traffic items with the Merged Destination Ranges option selected have be to manually regenerated by the user.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMulticastScalingFactor"])

    @EnableMulticastScalingFactor.setter
    def EnableMulticastScalingFactor(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMulticastScalingFactor"], value)

    @property
    def EnablePortLevelMisdirectedRoCEv2(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Check this option to enable port level misdirection handling for RoCEv2 traffic
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnablePortLevelMisdirectedRoCEv2"]
        )

    @EnablePortLevelMisdirectedRoCEv2.setter
    def EnablePortLevelMisdirectedRoCEv2(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnablePortLevelMisdirectedRoCEv2"], value
        )

    @property
    def EnableSequenceChecking(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If true, this field enables sequence checking. The default is false.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSequenceChecking"])

    @EnableSequenceChecking.setter
    def EnableSequenceChecking(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSequenceChecking"], value)

    @property
    def EnableStaggeredStartDelay(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If checked, enables the staggered start delay function.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableStaggeredStartDelay"])

    @EnableStaggeredStartDelay.setter
    def EnableStaggeredStartDelay(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableStaggeredStartDelay"], value)

    @property
    def EnableStaggeredTransmit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the start of transmit is staggered across ports. A 25-30 ms delay is introduced between the time one port begins transmitting and the time next port begins transmitting.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableStaggeredTransmit"])

    @EnableStaggeredTransmit.setter
    def EnableStaggeredTransmit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableStaggeredTransmit"], value)

    @property
    def EnableStreamOrdering(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, IxNetwork will allow stream ordering per RFC 2889.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableStreamOrdering"])

    @EnableStreamOrdering.setter
    def EnableStreamOrdering(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableStreamOrdering"], value)

    @property
    def FrameOrderingMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(flowGroupSetup | none | peakLoading | RFC2889): If true, enables frame ordering.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameOrderingMode"])

    @FrameOrderingMode.setter
    def FrameOrderingMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameOrderingMode"], value)

    @property
    def GlobalStreamControl(self):
        # type: () -> str
        """
        Returns
        -------
        - str(continuous | iterations): The Global Stream Control parameters.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GlobalStreamControl"])

    @GlobalStreamControl.setter
    def GlobalStreamControl(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GlobalStreamControl"], value)

    @property
    def GlobalStreamControlIterations(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, the user can specify how many times each packet stream will be transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GlobalStreamControlIterations"])

    @GlobalStreamControlIterations.setter
    def GlobalStreamControlIterations(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GlobalStreamControlIterations"], value)

    @property
    def IsApplicationTrafficRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, application traffic is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsApplicationTrafficRunning"])

    @property
    def IsApplyOnTheFlyRequired(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsApplyOnTheFlyRequired"])

    @property
    def IsTrafficRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, non-application traffic is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsTrafficRunning"])

    @property
    def LargeErrorThreshhold(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The user-configurable threshold value used to determine error levels for out-of-sequence, received packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LargeErrorThreshhold"])

    @LargeErrorThreshhold.setter
    def LargeErrorThreshhold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LargeErrorThreshhold"], value)

    @property
    def LearningFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Learns frame size
        """
        return self._get_attribute(self._SDM_ATT_MAP["LearningFrameSize"])

    @LearningFrameSize.setter
    def LearningFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LearningFrameSize"], value)

    @property
    def LearningFramesCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Learns frames count
        """
        return self._get_attribute(self._SDM_ATT_MAP["LearningFramesCount"])

    @LearningFramesCount.setter
    def LearningFramesCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LearningFramesCount"], value)

    @property
    def LearningFramesRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Learns frames rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["LearningFramesRate"])

    @LearningFramesRate.setter
    def LearningFramesRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LearningFramesRate"], value)

    @property
    def MacChangeOnFly(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables IxNetwork's gratuitous ARP capability. When enabled, IxNetwork listens for gratuitous ARP messages from its neighbors.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacChangeOnFly"])

    @MacChangeOnFly.setter
    def MacChangeOnFly(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MacChangeOnFly"], value)

    @property
    def MaxTrafficGenerationQueries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum number of traffic generation queries. The default is 500.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxTrafficGenerationQueries"])

    @MaxTrafficGenerationQueries.setter
    def MaxTrafficGenerationQueries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxTrafficGenerationQueries"], value)

    @property
    def MinimumSignatureLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Allows to set the Minimum Signature Length (4B-11B), when the Minimum Frame Size is enabled and 4B signature is not sufficient to track a huge number of flows.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinimumSignatureLength"])

    @MinimumSignatureLength.setter
    def MinimumSignatureLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinimumSignatureLength"], value)

    @property
    def MplsLabelLearningTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The MPLS label learning timeout in seconds. The default is 30 seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsLabelLearningTimeout"])

    @MplsLabelLearningTimeout.setter
    def MplsLabelLearningTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsLabelLearningTimeout"], value)

    @property
    def PeakLoadingReplicationCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The peak loading replication count
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeakLoadingReplicationCount"])

    @PeakLoadingReplicationCount.setter
    def PeakLoadingReplicationCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PeakLoadingReplicationCount"], value)

    @property
    def PreventDataPlaneToCpu(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prevent all data plane packets from being forwarded to Port CPU (disabling this option requires Port CPU reboot)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PreventDataPlaneToCpu"])

    @PreventDataPlaneToCpu.setter
    def PreventDataPlaneToCpu(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PreventDataPlaneToCpu"], value)

    @property
    def RefreshLearnedInfoBeforeApply(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This field refreshes the learned information from the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RefreshLearnedInfoBeforeApply"])

    @RefreshLearnedInfoBeforeApply.setter
    def RefreshLearnedInfoBeforeApply(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RefreshLearnedInfoBeforeApply"], value)

    @property
    def State(self):
        # type: () -> str
        """
        Returns
        -------
        - str(error | locked | started | startedWaitingForStats | startedWaitingForStreams | stopped | stoppedWaitingForStats | txStopWatchExpected | unapplied): Denotes the current state of traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["State"])

    @property
    def TrafficItemsChanged(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Keeps track if traffic has changed
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficItemsChanged"])

    @property
    def UseRfc5952(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use RFC 5952 for formatting IPv6 addresses (:ffff:1.2.3.4)
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseRfc5952"])

    @UseRfc5952.setter
    def UseRfc5952(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseRfc5952"], value)

    @property
    def UseScheduledStartTransmit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use Scheduled Start Transmit
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseScheduledStartTransmit"])

    @UseScheduledStartTransmit.setter
    def UseScheduledStartTransmit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseScheduledStartTransmit"], value)

    @property
    def UseTxRxSync(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the transmit/receive port synchronization algorithm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseTxRxSync"])

    @UseTxRxSync.setter
    def UseTxRxSync(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseTxRxSync"], value)

    @property
    def WaitTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time (in seconds) to wait after Stop Transmit before stopping Latency Measurement.
        """
        return self._get_attribute(self._SDM_ATT_MAP["WaitTime"])

    @WaitTime.setter
    def WaitTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["WaitTime"], value)

    def update(
        self,
        AutoCorrectL4HeaderChecksums=None,
        CycleOffsetForScheduledStart=None,
        CycleOffsetUnitForScheduledStart=None,
        CycleTimeForScheduledStart=None,
        CycleTimeUnitForScheduledStart=None,
        DataPlaneJitterWindow=None,
        DelayTimeForScheduledStart=None,
        DestMacRetryCount=None,
        DestMacRetryDelay=None,
        DetectMisdirectedOnAllPorts=None,
        DisablePortLevelMisdirected=None,
        DisplayMplsCurrentLabelValue=None,
        EgressOnlyTrafficItemName=None,
        EnableDataIntegrityCheck=None,
        EnableDestMacRetry=None,
        EnableEgressOnlyTracking=None,
        EnableEgressOnlyTxStats=None,
        EnableInstantaneousStatsSupport=None,
        EnableLagAutoRate=None,
        EnableLagFlowBalancing=None,
        EnableLagFlowFailoverMode=None,
        EnableLagRebalanceOnPortUp=None,
        EnableMinFrameSize=None,
        EnableMulticastScalingFactor=None,
        EnablePortLevelMisdirectedRoCEv2=None,
        EnableSequenceChecking=None,
        EnableStaggeredStartDelay=None,
        EnableStaggeredTransmit=None,
        EnableStreamOrdering=None,
        FrameOrderingMode=None,
        GlobalStreamControl=None,
        GlobalStreamControlIterations=None,
        LargeErrorThreshhold=None,
        LearningFrameSize=None,
        LearningFramesCount=None,
        LearningFramesRate=None,
        MacChangeOnFly=None,
        MaxTrafficGenerationQueries=None,
        MinimumSignatureLength=None,
        MplsLabelLearningTimeout=None,
        PeakLoadingReplicationCount=None,
        PreventDataPlaneToCpu=None,
        RefreshLearnedInfoBeforeApply=None,
        UseRfc5952=None,
        UseScheduledStartTransmit=None,
        UseTxRxSync=None,
        WaitTime=None,
    ):
        # type: (bool, int, str, int, str, str, int, int, int, bool, bool, bool, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, int, int, int, int, int, bool, int, int, int, int, bool, bool, bool, bool, bool, int) -> Traffic
        """Updates traffic resource on the server.

        Args
        ----
        - AutoCorrectL4HeaderChecksums (bool): This is used for Multis and Xdensity as checksum is not calculated correctly when change on the fly operations are performed. When this option is enabled IxOS uses 2 bytes before CRC, that way ensuring the checksum is correct when change on the fly operations are performed.
        - CycleOffsetForScheduledStart (number):
        - CycleOffsetUnitForScheduledStart (str(microseconds | milliseconds | nanoseconds | seconds)):
        - CycleTimeForScheduledStart (number):
        - CycleTimeUnitForScheduledStart (str(microseconds | milliseconds | nanoseconds | seconds)):
        - DataPlaneJitterWindow (str(0 | 10485760 | 1310720 | 167772160 | 20971520 | 2621440 | 335544320 | 41943040 | 5242880 | 671088640 | 83886080)): Indicates the number of packets received during a time interval. This is used for calculating the rate on the recieve side
        - DelayTimeForScheduledStart (number): Delay Time For Scheduled Start Transmit in seconds
        - DestMacRetryCount (number): The number of time to attempt to obtain the destination MAC address.
        - DestMacRetryDelay (number): The number of seconds to wait between attempts to obtain the destination MAC address.
        - DetectMisdirectedOnAllPorts (bool):
        - DisablePortLevelMisdirected (bool):
        - DisplayMplsCurrentLabelValue (bool): Displays current label value for LSP Endpoints.
        - EgressOnlyTrafficItemName (str): Traffic Item name for egress only flows in statistics.
        - EnableDataIntegrityCheck (bool): If true, enable data integrity check.
        - EnableDestMacRetry (bool): If true, enables the destination MAC address retry function.
        - EnableEgressOnlyTracking (bool): This flags enables/disables egress only tracking. In this mode only traffic without ingress tracking is supported on ports with egress only settings, user will have only PGID stats and the packets will not contain any instrumentation block.
        - EnableEgressOnlyTxStats (bool): This flags enables/disables egress only tx stats. In this mode all traffic without ingress tracking is considered for tx stats.
        - EnableInstantaneousStatsSupport (bool): If true, enables instantaneous stats support
        - EnableLagAutoRate (bool):
        - EnableLagFlowBalancing (bool):
        - EnableLagFlowFailoverMode (bool):
        - EnableLagRebalanceOnPortUp (bool):
        - EnableMinFrameSize (bool): If true, IxNetwork allows the stream to use smaller packet sizes. (In the case of IPv4 and Ethernet, 64 bytes are allowed.) This is achieved by reducing the size of the instrumentation tag, which is identified by the receiving ports.
        - EnableMulticastScalingFactor (bool): If true, traffic items with the Merged Destination Ranges option selected have be to manually regenerated by the user.
        - EnablePortLevelMisdirectedRoCEv2 (bool): Check this option to enable port level misdirection handling for RoCEv2 traffic
        - EnableSequenceChecking (bool): If true, this field enables sequence checking. The default is false.
        - EnableStaggeredStartDelay (bool): If checked, enables the staggered start delay function.
        - EnableStaggeredTransmit (bool): If true, the start of transmit is staggered across ports. A 25-30 ms delay is introduced between the time one port begins transmitting and the time next port begins transmitting.
        - EnableStreamOrdering (bool): If true, IxNetwork will allow stream ordering per RFC 2889.
        - FrameOrderingMode (str(flowGroupSetup | none | peakLoading | RFC2889)): If true, enables frame ordering.
        - GlobalStreamControl (str(continuous | iterations)): The Global Stream Control parameters.
        - GlobalStreamControlIterations (number): If true, the user can specify how many times each packet stream will be transmitted.
        - LargeErrorThreshhold (number): The user-configurable threshold value used to determine error levels for out-of-sequence, received packets.
        - LearningFrameSize (number): Learns frame size
        - LearningFramesCount (number): Learns frames count
        - LearningFramesRate (number): Learns frames rate
        - MacChangeOnFly (bool): If true, enables IxNetwork's gratuitous ARP capability. When enabled, IxNetwork listens for gratuitous ARP messages from its neighbors.
        - MaxTrafficGenerationQueries (number): The maximum number of traffic generation queries. The default is 500.
        - MinimumSignatureLength (number): Allows to set the Minimum Signature Length (4B-11B), when the Minimum Frame Size is enabled and 4B signature is not sufficient to track a huge number of flows.
        - MplsLabelLearningTimeout (number): The MPLS label learning timeout in seconds. The default is 30 seconds.
        - PeakLoadingReplicationCount (number): The peak loading replication count
        - PreventDataPlaneToCpu (bool): Prevent all data plane packets from being forwarded to Port CPU (disabling this option requires Port CPU reboot)
        - RefreshLearnedInfoBeforeApply (bool): This field refreshes the learned information from the DUT.
        - UseRfc5952 (bool): Use RFC 5952 for formatting IPv6 addresses (:ffff:1.2.3.4)
        - UseScheduledStartTransmit (bool): Use Scheduled Start Transmit
        - UseTxRxSync (bool): If true, enables the transmit/receive port synchronization algorithm.
        - WaitTime (number): The time (in seconds) to wait after Stop Transmit before stopping Latency Measurement.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AutoCorrectL4HeaderChecksums=None,
        CycleOffsetForScheduledStart=None,
        CycleOffsetUnitForScheduledStart=None,
        CycleTimeForScheduledStart=None,
        CycleTimeUnitForScheduledStart=None,
        DataPlaneJitterWindow=None,
        DelayTimeForScheduledStart=None,
        DestMacRetryCount=None,
        DestMacRetryDelay=None,
        DetectMisdirectedOnAllPorts=None,
        DisablePortLevelMisdirected=None,
        DisplayMplsCurrentLabelValue=None,
        EgressOnlyTrafficItemName=None,
        ElapsedTransmitTime=None,
        EnableDataIntegrityCheck=None,
        EnableDestMacRetry=None,
        EnableEgressOnlyTracking=None,
        EnableEgressOnlyTxStats=None,
        EnableInstantaneousStatsSupport=None,
        EnableLagAutoRate=None,
        EnableLagFlowBalancing=None,
        EnableLagFlowFailoverMode=None,
        EnableLagRebalanceOnPortUp=None,
        EnableMinFrameSize=None,
        EnableMulticastScalingFactor=None,
        EnablePortLevelMisdirectedRoCEv2=None,
        EnableSequenceChecking=None,
        EnableStaggeredStartDelay=None,
        EnableStaggeredTransmit=None,
        EnableStreamOrdering=None,
        FrameOrderingMode=None,
        GlobalStreamControl=None,
        GlobalStreamControlIterations=None,
        IsApplicationTrafficRunning=None,
        IsApplyOnTheFlyRequired=None,
        IsTrafficRunning=None,
        LargeErrorThreshhold=None,
        LearningFrameSize=None,
        LearningFramesCount=None,
        LearningFramesRate=None,
        MacChangeOnFly=None,
        MaxTrafficGenerationQueries=None,
        MinimumSignatureLength=None,
        MplsLabelLearningTimeout=None,
        PeakLoadingReplicationCount=None,
        PreventDataPlaneToCpu=None,
        RefreshLearnedInfoBeforeApply=None,
        State=None,
        TrafficItemsChanged=None,
        UseRfc5952=None,
        UseScheduledStartTransmit=None,
        UseTxRxSync=None,
        WaitTime=None,
    ):
        # type: (bool, int, str, int, str, str, int, int, int, bool, bool, bool, str, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, int, bool, bool, bool, int, int, int, int, bool, int, int, int, int, bool, bool, str, int, bool, bool, bool, int) -> Traffic
        """Finds and retrieves traffic resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve traffic resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all traffic resources from the server.

        Args
        ----
        - AutoCorrectL4HeaderChecksums (bool): This is used for Multis and Xdensity as checksum is not calculated correctly when change on the fly operations are performed. When this option is enabled IxOS uses 2 bytes before CRC, that way ensuring the checksum is correct when change on the fly operations are performed.
        - CycleOffsetForScheduledStart (number):
        - CycleOffsetUnitForScheduledStart (str(microseconds | milliseconds | nanoseconds | seconds)):
        - CycleTimeForScheduledStart (number):
        - CycleTimeUnitForScheduledStart (str(microseconds | milliseconds | nanoseconds | seconds)):
        - DataPlaneJitterWindow (str(0 | 10485760 | 1310720 | 167772160 | 20971520 | 2621440 | 335544320 | 41943040 | 5242880 | 671088640 | 83886080)): Indicates the number of packets received during a time interval. This is used for calculating the rate on the recieve side
        - DelayTimeForScheduledStart (number): Delay Time For Scheduled Start Transmit in seconds
        - DestMacRetryCount (number): The number of time to attempt to obtain the destination MAC address.
        - DestMacRetryDelay (number): The number of seconds to wait between attempts to obtain the destination MAC address.
        - DetectMisdirectedOnAllPorts (bool):
        - DisablePortLevelMisdirected (bool):
        - DisplayMplsCurrentLabelValue (bool): Displays current label value for LSP Endpoints.
        - EgressOnlyTrafficItemName (str): Traffic Item name for egress only flows in statistics.
        - ElapsedTransmitTime (number): Specifies the amount of time traffic is running in milliseconds. If the traffic state is unapplied or errored then the transmit time will be 0.
        - EnableDataIntegrityCheck (bool): If true, enable data integrity check.
        - EnableDestMacRetry (bool): If true, enables the destination MAC address retry function.
        - EnableEgressOnlyTracking (bool): This flags enables/disables egress only tracking. In this mode only traffic without ingress tracking is supported on ports with egress only settings, user will have only PGID stats and the packets will not contain any instrumentation block.
        - EnableEgressOnlyTxStats (bool): This flags enables/disables egress only tx stats. In this mode all traffic without ingress tracking is considered for tx stats.
        - EnableInstantaneousStatsSupport (bool): If true, enables instantaneous stats support
        - EnableLagAutoRate (bool):
        - EnableLagFlowBalancing (bool):
        - EnableLagFlowFailoverMode (bool):
        - EnableLagRebalanceOnPortUp (bool):
        - EnableMinFrameSize (bool): If true, IxNetwork allows the stream to use smaller packet sizes. (In the case of IPv4 and Ethernet, 64 bytes are allowed.) This is achieved by reducing the size of the instrumentation tag, which is identified by the receiving ports.
        - EnableMulticastScalingFactor (bool): If true, traffic items with the Merged Destination Ranges option selected have be to manually regenerated by the user.
        - EnablePortLevelMisdirectedRoCEv2 (bool): Check this option to enable port level misdirection handling for RoCEv2 traffic
        - EnableSequenceChecking (bool): If true, this field enables sequence checking. The default is false.
        - EnableStaggeredStartDelay (bool): If checked, enables the staggered start delay function.
        - EnableStaggeredTransmit (bool): If true, the start of transmit is staggered across ports. A 25-30 ms delay is introduced between the time one port begins transmitting and the time next port begins transmitting.
        - EnableStreamOrdering (bool): If true, IxNetwork will allow stream ordering per RFC 2889.
        - FrameOrderingMode (str(flowGroupSetup | none | peakLoading | RFC2889)): If true, enables frame ordering.
        - GlobalStreamControl (str(continuous | iterations)): The Global Stream Control parameters.
        - GlobalStreamControlIterations (number): If true, the user can specify how many times each packet stream will be transmitted.
        - IsApplicationTrafficRunning (bool): If true, application traffic is running.
        - IsApplyOnTheFlyRequired (bool):
        - IsTrafficRunning (bool): If true, non-application traffic is running.
        - LargeErrorThreshhold (number): The user-configurable threshold value used to determine error levels for out-of-sequence, received packets.
        - LearningFrameSize (number): Learns frame size
        - LearningFramesCount (number): Learns frames count
        - LearningFramesRate (number): Learns frames rate
        - MacChangeOnFly (bool): If true, enables IxNetwork's gratuitous ARP capability. When enabled, IxNetwork listens for gratuitous ARP messages from its neighbors.
        - MaxTrafficGenerationQueries (number): The maximum number of traffic generation queries. The default is 500.
        - MinimumSignatureLength (number): Allows to set the Minimum Signature Length (4B-11B), when the Minimum Frame Size is enabled and 4B signature is not sufficient to track a huge number of flows.
        - MplsLabelLearningTimeout (number): The MPLS label learning timeout in seconds. The default is 30 seconds.
        - PeakLoadingReplicationCount (number): The peak loading replication count
        - PreventDataPlaneToCpu (bool): Prevent all data plane packets from being forwarded to Port CPU (disabling this option requires Port CPU reboot)
        - RefreshLearnedInfoBeforeApply (bool): This field refreshes the learned information from the DUT.
        - State (str(error | locked | started | startedWaitingForStats | startedWaitingForStreams | stopped | stoppedWaitingForStats | txStopWatchExpected | unapplied)): Denotes the current state of traffic.
        - TrafficItemsChanged (number): Keeps track if traffic has changed
        - UseRfc5952 (bool): Use RFC 5952 for formatting IPv6 addresses (:ffff:1.2.3.4)
        - UseScheduledStartTransmit (bool): Use Scheduled Start Transmit
        - UseTxRxSync (bool): If true, enables the transmit/receive port synchronization algorithm.
        - WaitTime (number): The time (in seconds) to wait after Stop Transmit before stopping Latency Measurement.

        Returns
        -------
        - self: This instance with matching traffic resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of traffic data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the traffic resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddRoCEv2FlowGroups(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addRoCEv2FlowGroups operation on the server.

        Generate traffic for a RoCEv2 traffic flow groups.

        addRoCEv2FlowGroups(async_operation=bool)
        -----------------------------------------
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
            "addRoCEv2FlowGroups", payload=payload, response_object=None
        )

    def AddRoCEv2FlowGroupsWithParams(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addRoCEv2FlowGroupsWithParams operation on the server.

        Generate traffic for a RoCEv2 traffic flow groups with custom Tx Mode and burst count.

        addRoCEv2FlowGroupsWithParams(Arg2=enum, Arg3=number, async_operation=bool)
        ---------------------------------------------------------------------------
        - Arg2 (str(continuous | fixed)): RoCEv2 Stream Tx Mode: continuous | fixed
        - Arg3 (number): RoCEv2 Stream Burst Count
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
            "addRoCEv2FlowGroupsWithParams", payload=payload, response_object=None
        )

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Apply the traffic configuration.

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

    def ApplyApplicationTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyApplicationTraffic operation on the server.

        Apply the stateful traffic configuration.

        DEPRECATED applyApplicationTraffic(async_operation=bool)
        --------------------------------------------------------
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
            "applyApplicationTraffic", payload=payload, response_object=None
        )

    def ApplyOnTheFlyTrafficChanges(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyOnTheFlyTrafficChanges operation on the server.

        Apply on the fly traffic changes.

        applyOnTheFlyTrafficChanges(async_operation=bool)
        -------------------------------------------------
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
            "applyOnTheFlyTrafficChanges", payload=payload, response_object=None
        )

    def ApplyStatefulTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyStatefulTraffic operation on the server.

        Apply the traffic configuration for stateful traffic items only.

        applyStatefulTraffic(async_operation=bool)
        ------------------------------------------
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
            "applyStatefulTraffic", payload=payload, response_object=None
        )

    def GetFrameCountForDuration(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[int], None]
        """Executes the getFrameCountForDuration operation on the server.

        Get the frame count for a specific duration.

        getFrameCountForDuration(Arg2=list, async_operation=bool)list
        -------------------------------------------------------------
        - Arg2 (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/traffic/trafficItem/highLevelStream],arg2:number))): An array of structures. Each structure is one valid highLevelStream object reference and the duration to get the frame count for.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(number): An array of frame counts.

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
            "getFrameCountForDuration", payload=payload, response_object=None
        )

    def MakeStatelessTrafficUnapplied(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the makeStatelessTrafficUnapplied operation on the server.

        Move stateless traffic to unapplied state.

        makeStatelessTrafficUnapplied(async_operation=bool)
        ---------------------------------------------------
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
            "makeStatelessTrafficUnapplied", payload=payload, response_object=None
        )

    def PauseStatelessTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the pauseStatelessTraffic operation on the server.

        Pause or Resume stateless traffic.

        pauseStatelessTraffic(Arg2=bool, async_operation=bool)
        ------------------------------------------------------
        - Arg2 (bool): If true, it will pause running traffic. If false, it will resume previously paused traffic.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "pauseStatelessTraffic", payload=payload, response_object=None
        )

    def SendL2L3Learning(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the sendL2L3Learning operation on the server.

        Send L2 and L3 learning frames.

        sendL2L3Learning(async_operation=bool)
        --------------------------------------
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
        return self._execute("sendL2L3Learning", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start the traffic configuration.

        start(async_operation=bool)
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
        return self._execute("start", payload=payload, response_object=None)

    def StartApplicationTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startApplicationTraffic operation on the server.

        Start the stateful traffic configuration.

        DEPRECATED startApplicationTraffic(async_operation=bool)
        --------------------------------------------------------
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
            "startApplicationTraffic", payload=payload, response_object=None
        )

    def StartStatefulTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startStatefulTraffic operation on the server.

        Start stateful traffic items only.

        startStatefulTraffic(async_operation=bool)
        ------------------------------------------
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
            "startStatefulTraffic", payload=payload, response_object=None
        )

    def StartStatelessTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startStatelessTraffic operation on the server.

        Start the traffic configuration for stateless traffic items only.

        startStatelessTraffic(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "startStatelessTraffic", payload=payload, response_object=None
        )

    def StartStatelessTrafficBlocking(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startStatelessTrafficBlocking operation on the server.

        Start the traffic configuration for stateless traffic items only. This will block until traffic is fully started.

        startStatelessTrafficBlocking(async_operation=bool)
        ---------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "startStatelessTrafficBlocking", payload=payload, response_object=None
        )

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop the traffic configuration.

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

    def StopApplicationTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopApplicationTraffic operation on the server.

        Stop the stateful traffic configuration.

        DEPRECATED stopApplicationTraffic(async_operation=bool)
        -------------------------------------------------------
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
            "stopApplicationTraffic", payload=payload, response_object=None
        )

    def StopStatefulTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopStatefulTraffic operation on the server.

        Stop stateful traffic items only.

        stopStatefulTraffic(async_operation=bool)
        -----------------------------------------
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
            "stopStatefulTraffic", payload=payload, response_object=None
        )

    def StopStatelessTraffic(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopStatelessTraffic operation on the server.

        Stop the stateless traffic items.

        stopStatelessTraffic(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "stopStatelessTraffic", payload=payload, response_object=None
        )

    def StopStatelessTrafficBlocking(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopStatelessTrafficBlocking operation on the server.

        Stop the traffic configuration for stateless traffic items only. This will block until traffic is fully stopped.

        stopStatelessTrafficBlocking(async_operation=bool)
        --------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "stopStatelessTrafficBlocking", payload=payload, response_object=None
        )
