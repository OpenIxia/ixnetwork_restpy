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


class Ptp(Base):
    """Precision Time Protocol
    The Ptp class encapsulates a list of ptp resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ptp.find() method.
    The list can be managed by using the Ptp.add() and Ptp.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ptp'
    _SDM_ATT_MAP = {
        'AllowedFaults': 'allowedFaults',
        'AllowedLostResponse': 'allowedLostResponse',
        'AlternateMasterFlag': 'alternateMasterFlag',
        'AnnounceCurrentUtcOffsetValid': 'announceCurrentUtcOffsetValid',
        'AnnounceDropRate': 'announceDropRate',
        'AnnounceFrequencyTraceable': 'announceFrequencyTraceable',
        'AnnounceLeap59': 'announceLeap59',
        'AnnounceLeap61': 'announceLeap61',
        'AnnouncePtpTimescale': 'announcePtpTimescale',
        'AnnounceReceiptTimeout': 'announceReceiptTimeout',
        'AnnounceTimeTraceable': 'announceTimeTraceable',
        'AtoiTlvCount': 'atoiTlvCount',
        'AvnuMode': 'avnuMode',
        'Bmca': 'bmca',
        'ClockAccuracy': 'clockAccuracy',
        'ClockClass': 'clockClass',
        'ClockIdentity': 'clockIdentity',
        'CommunicationMode': 'communicationMode',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'CumulativeScaledRateOffset': 'cumulativeScaledRateOffset',
        'CurrentLocalOffset': 'currentLocalOffset',
        'CurrentUtcOffset': 'currentUtcOffset',
        'CustomClockId': 'customClockId',
        'DaylightSaving': 'daylightSaving',
        'DefaultSystemFrameRateDenominator': 'defaultSystemFrameRateDenominator',
        'DefaultSystemFrameRateNumerator': 'defaultSystemFrameRateNumerator',
        'DelayAsymmetry': 'delayAsymmetry',
        'DelayMechanism': 'delayMechanism',
        'DelayReqDropRate': 'delayReqDropRate',
        'DelayReqOffset': 'delayReqOffset',
        'DelayReqResidenceTime': 'delayReqResidenceTime',
        'DelayReqSpread': 'delayReqSpread',
        'DelayRespDropRate': 'delayRespDropRate',
        'DelayRespReceiptTimeout': 'delayRespReceiptTimeout',
        'DelayRespResidenceTime': 'delayRespResidenceTime',
        'DelayResponseDelay': 'delayResponseDelay',
        'DelayResponseDelayInsertionRate': 'delayResponseDelayInsertionRate',
        'DescriptiveName': 'descriptiveName',
        'Domain': 'domain',
        'DropMalformed': 'dropMalformed',
        'DropSignalReqAnnounce': 'dropSignalReqAnnounce',
        'DropSignalReqDelayResp': 'dropSignalReqDelayResp',
        'DropSignalReqSync': 'dropSignalReqSync',
        'EnableATOITlv': 'enableATOITlv',
        'EnableCmlds': 'enableCmlds',
        'EnableNegativeTesting': 'enableNegativeTesting',
        'Errors': 'errors',
        'FolderPath': 'folderPath',
        'FollowUpBadCrcRate': 'followUpBadCrcRate',
        'FollowUpDelay': 'followUpDelay',
        'FollowUpDelayInsertionRate': 'followUpDelayInsertionRate',
        'FollowUpDropRate': 'followUpDropRate',
        'FollowUpResidenceTime': 'followUpResidenceTime',
        'Frequency': 'frequency',
        'GPTPCapableReceiptTimeout': 'gPTPCapableReceiptTimeout',
        'GmTimeBaseIndicator': 'gmTimeBaseIndicator',
        'GrandmasterID': 'grandmasterID',
        'GrandmasterIdentity': 'grandmasterIdentity',
        'GrantDelayRespDurationInterval': 'grantDelayRespDurationInterval',
        'GrantSyncDurationInterval': 'grantSyncDurationInterval',
        'GrantUnicastDurationInterval': 'grantUnicastDurationInterval',
        'HandleAnnounceTlv': 'handleAnnounceTlv',
        'HandleCancelTlv': 'handleCancelTlv',
        'JumpSeconds': 'jumpSeconds',
        'LastGmPhaseChange': 'lastGmPhaseChange',
        'LeapSecondJump': 'leapSecondJump',
        'LearnPortId': 'learnPortId',
        'LogAnnounceInterval': 'logAnnounceInterval',
        'LogCleanUpOption': 'logCleanUpOption',
        'LogDelayReqInterval': 'logDelayReqInterval',
        'LogFileAge': 'logFileAge',
        'LogFuturePacketInfo': 'logFuturePacketInfo',
        'LogManagementMsgInterval': 'logManagementMsgInterval',
        'LogSignallingInterval': 'logSignallingInterval',
        'LogSyncInterval': 'logSyncInterval',
        'MasterClockId': 'masterClockId',
        'MasterCount': 'masterCount',
        'MasterIpAddress': 'masterIpAddress',
        'MasterIpIncrementBy': 'masterIpIncrementBy',
        'MasterIpv6Address': 'masterIpv6Address',
        'MasterIpv6IncrementBy': 'masterIpv6IncrementBy',
        'MasterLockingStatus': 'masterLockingStatus',
        'MasterMacAddress': 'masterMacAddress',
        'MasterMacIncrementBy': 'masterMacIncrementBy',
        'MeanLinkDelayThreshold': 'meanLinkDelayThreshold',
        'MulticastAddress': 'multicastAddress',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NanosecondsPerSecond': 'nanosecondsPerSecond',
        'NotSlave': 'notSlave',
        'NumRecords': 'numRecords',
        'NumberOFMsgs': 'numberOFMsgs',
        'OffsetBaseddebuggabilityEnabled': 'offsetBaseddebuggabilityEnabled',
        'OffsetLimit': 'offsetLimit',
        'OffsetScaledLogVariance': 'offsetScaledLogVariance',
        'OneWay': 'oneWay',
        'PDelayFollowUpDelay': 'pDelayFollowUpDelay',
        'PDelayFollowUpDelayInsertionRate': 'pDelayFollowUpDelayInsertionRate',
        'PDelayFollowUpDropRate': 'pDelayFollowUpDropRate',
        'PDelayFollowUpResidenceTime': 'pDelayFollowUpResidenceTime',
        'PathTraceTLV': 'pathTraceTLV',
        'PortNumber': 'portNumber',
        'PreviousJamLocalOffset': 'previousJamLocalOffset',
        'Priority1': 'priority1',
        'Priority2': 'priority2',
        'Profile': 'profile',
        'PtpState': 'ptpState',
        'RenewalInvited': 'renewalInvited',
        'RequestAttempts': 'requestAttempts',
        'RequestHolddown': 'requestHolddown',
        'RequestInterval': 'requestInterval',
        'Reserved': 'reserved',
        'ReverseSync': 'reverseSync',
        'ReverseSyncIntervalPercent': 'reverseSyncIntervalPercent',
        'Role': 'role',
        'RxCalibration': 'rxCalibration',
        'ScaledLastGmFreqChange': 'scaledLastGmFreqChange',
        'SendMulticastAnnounce': 'sendMulticastAnnounce',
        'SessionInfo': 'sessionInfo',
        'SessionStatus': 'sessionStatus',
        'SignalInterval': 'signalInterval',
        'SignalUnicastHandling': 'signalUnicastHandling',
        'SignallingDropRate': 'signallingDropRate',
        'SimulateBoundary': 'simulateBoundary',
        'SimulateTransparent': 'simulateTransparent',
        'SlaveCount': 'slaveCount',
        'SlaveIpAddress': 'slaveIpAddress',
        'SlaveIpIncrementBy': 'slaveIpIncrementBy',
        'SlaveIpv6Address': 'slaveIpv6Address',
        'SlaveIpv6IncrementBy': 'slaveIpv6IncrementBy',
        'SlaveMacAddress': 'slaveMacAddress',
        'SlaveMacIncrementBy': 'slaveMacIncrementBy',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'StepMode': 'stepMode',
        'StepsRemoved': 'stepsRemoved',
        'StrictGrant': 'strictGrant',
        'SyncDropRate': 'syncDropRate',
        'SyncReceiptTimeout': 'syncReceiptTimeout',
        'SyncReceiptTimeoutgPTP': 'syncReceiptTimeoutgPTP',
        'SyncResidenceTime': 'syncResidenceTime',
        'TimeAddressFlags': 'timeAddressFlags',
        'TimeOfNextJam': 'timeOfNextJam',
        'TimeOfNextJump': 'timeOfNextJump',
        'TimeOfPreviousJam': 'timeOfPreviousJam',
        'TimeSource': 'timeSource',
        'TimestampOffset': 'timestampOffset',
        'TotalTimeInaccuracy': 'totalTimeInaccuracy',
        'TxCalibration': 'txCalibration',
        'TxTwoStepCalibration': 'txTwoStepCalibration',
        'UpdateTime': 'updateTime',
    }

    def __init__(self, parent):
        super(Ptp, self).__init__(parent)

    @property
    def AtoiTLVList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.atoitlvlist_5c4e305687043a6232999175d09f7f65.AtoiTLVList): An instance of the AtoiTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.atoitlvlist_5c4e305687043a6232999175d09f7f65 import AtoiTLVList
        return AtoiTLVList(self)._select()

    @property
    def PtpNegBehaveList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptpnegbehavelist_95420ff08c49e28cbca41e3d66ac6215.PtpNegBehaveList): An instance of the PtpNegBehaveList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptpnegbehavelist_95420ff08c49e28cbca41e3d66ac6215 import PtpNegBehaveList
        return PtpNegBehaveList(self)._select()

    @property
    def AllowedFaults(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): It is the number of faults, above which asCapableAcrossDomains is set to FALSE, i.e., a LinkPort is considered to be not capable of interoperating with its neighbor via the IEEE 802.1AS protocol.The Value should be between 1 and 255.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllowedFaults']))

    @property
    def AllowedLostResponse(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): It is the number of Pdelay_Req messages for which a valid response is not received, above whicha Link Port is considered to be not exchanging peer delay messages with its neighbor.The Value should be between 1 and 255.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllowedLostResponse']))

    @property
    def AlternateMasterFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to set the 'Alternate Master flag' in all Announce and Sync messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AlternateMasterFlag']))

    @property
    def AnnounceCurrentUtcOffsetValid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to set the 'UTC Reasonable' flag in all Announce messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AnnounceCurrentUtcOffsetValid']))

    @property
    def AnnounceDropRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage rate of the dropped Announce messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AnnounceDropRate']))

    @property
    def AnnounceFrequencyTraceable(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to set the 'Frequency Traceable flag' in all Announce messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AnnounceFrequencyTraceable']))

    @property
    def AnnounceLeap59(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to set the 'Announce leap59 flag' in all Announce messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AnnounceLeap59']))

    @property
    def AnnounceLeap61(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to set the 'Announce leap61 flag' in all Announce messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AnnounceLeap61']))

    @property
    def AnnouncePtpTimescale(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to set the 'PTP Timescale flag' in all Announce messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AnnouncePtpTimescale']))

    @property
    def AnnounceReceiptTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of Announce Intervals that have to pass without receipt of an Announce message to trigger timeout
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AnnounceReceiptTimeout']))

    @property
    def AnnounceTimeTraceable(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to set the 'Time Traceable flag' in all Announce messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AnnounceTimeTraceable']))

    @property
    def AtoiTlvCount(self):
        """
        Returns
        -------
        - number: ATOI TLV Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['AtoiTlvCount'])
    @AtoiTlvCount.setter
    def AtoiTlvCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AtoiTlvCount'], value)

    @property
    def AvnuMode(self):
        """
        Returns
        -------
        - str(aVNU_NA | aVNU_GPTP): AVNU Mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvnuMode'])
    @AvnuMode.setter
    def AvnuMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AvnuMode'], value)

    @property
    def Bmca(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Run the Best Master Clock Algorithm for gPTP (if disabled can use a pre-defined Master or accept messages from any source)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Bmca']))

    @property
    def ClockAccuracy(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Master clock accuracy that need to be conveyed via Announce Message.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClockAccuracy']))

    @property
    def ClockClass(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Traceability of the time or frequency distributed by the grandmaster clock
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClockClass']))

    @property
    def ClockIdentity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the ClockIdentity to be used by this device
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClockIdentity']))

    @property
    def CommunicationMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option to choose PTP Protocol Communication mode (unicast/multicast/mixed).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CommunicationMode']))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer used to connect to the wire
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def CumulativeScaledRateOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Cumulative Scaled Rate Offset field set in the gPTP FollowUp TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CumulativeScaledRateOffset']))

    @property
    def CurrentLocalOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Offset in seconds of Local Time from grandmaster PTP time.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CurrentLocalOffset']))

    @property
    def CurrentUtcOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Current UTC Offset (seconds) to be sent via Announce Message.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CurrentUtcOffset']))

    @property
    def CustomClockId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use the ClockIdentity configured in the next column instead of MAC based generated one
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CustomClockId']))

    @property
    def DaylightSaving(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This filed will be used to encode Occurence of daylight saving.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DaylightSaving']))

    @property
    def DefaultSystemFrameRateDenominator(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Default video frame rate of the slave system as a lowest term rational. The Denominator value of Default System Frame Rate.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DefaultSystemFrameRateDenominator']))

    @property
    def DefaultSystemFrameRateNumerator(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Default video frame rate of the slave system as a lowest term rational. The Numerator value of Default System Frame Rate.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DefaultSystemFrameRateNumerator']))

    @property
    def DelayAsymmetry(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay Asymmetry between path
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayAsymmetry']))

    @property
    def DelayMechanism(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Mechanism to measure path delay between two ptp port.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayMechanism']))

    @property
    def DelayReqDropRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage rate of the dropped (P)DelayReq messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayReqDropRate']))

    @property
    def DelayReqOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage of the agreed (P)DelayReq Inter-arrival time to schedule between two subsequent DelayReq messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayReqOffset']))

    @property
    def DelayReqResidenceTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Residence time of (P)DelayReq messages through an associated one-step end-to-end transparent clock inserted in the correction field of (P)DelayReq messages sent by this clock
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayReqResidenceTime']))

    @property
    def DelayReqSpread(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Distribute (P)DelayReq messages in an interval around the targeted Inter-arrival mean time (expressed as a % of targeted mean)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayReqSpread']))

    @property
    def DelayRespDropRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage rate of the dropped DelayResp messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayRespDropRate']))

    @property
    def DelayRespReceiptTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DelayResponse Receipt Timeout in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayRespReceiptTimeout']))

    @property
    def DelayRespResidenceTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Residence time of DelayReq messages through an associated two-step end-to-end transparent clock inserted in the correction field of DelayResp messages sent by this clock, or the residence time of PdelayResp messages through an associated one-step end-to-end transparent clock inserted in the correction field of PdelayResp messages sent by this clock.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayRespResidenceTime']))

    @property
    def DelayResponseDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Additional delay introduced in the DelayResp message (nanoseconds)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayResponseDelay']))

    @property
    def DelayResponseDelayInsertionRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage rate of the DelayResp messages in which the delay is introduced
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayResponseDelayInsertionRate']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Domain(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PTP Domain
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Domain']))

    @property
    def DropMalformed(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Drop packets that for which fields like Domain, message rates, Clock Class, Clock Accuracy and Offset Scaled Log Variance are not respecting strict G8275.1 imposed intervals
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DropMalformed']))

    @property
    def DropSignalReqAnnounce(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to drop any Signal Request that contains Announce TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DropSignalReqAnnounce']))

    @property
    def DropSignalReqDelayResp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to drop any Signal Request that contains DelayResp TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DropSignalReqDelayResp']))

    @property
    def DropSignalReqSync(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this check box to drop any Signal Request that contains Sync TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DropSignalReqSync']))

    @property
    def EnableATOITlv(self):
        """
        Returns
        -------
        - bool: Enable ATOI TLV
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableATOITlv'])
    @EnableATOITlv.setter
    def EnableATOITlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableATOITlv'], value)

    @property
    def EnableCmlds(self):
        """
        Returns
        -------
        - bool: Enable Cmlds
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCmlds'])
    @EnableCmlds.setter
    def EnableCmlds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCmlds'], value)

    @property
    def EnableNegativeTesting(self):
        """
        Returns
        -------
        - bool: Enable Negative Conformance Test
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableNegativeTesting'])
    @EnableNegativeTesting.setter
    def EnableNegativeTesting(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableNegativeTesting'], value)

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def FolderPath(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Folder To Store Log Files
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FolderPath']))

    @property
    def FollowUpBadCrcRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage rate of the bad crc FollowUp messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FollowUpBadCrcRate']))

    @property
    def FollowUpDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Additional delay introduced in the FollowUp message timestamp (ns)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FollowUpDelay']))

    @property
    def FollowUpDelayInsertionRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage rate of the FollowUp messages in which the delay is introduced
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FollowUpDelayInsertionRate']))

    @property
    def FollowUpDropRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage rate of the dropped FollowUp messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FollowUpDropRate']))

    @property
    def FollowUpResidenceTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Master to slave residence of Sync messages through an associated two-step transparent clock inserted in the correction field of FollowUp messages sent by this clock
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FollowUpResidenceTime']))

    @property
    def Frequency(self):
        """
        Returns
        -------
        - number: Frequency(N)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Frequency'])
    @Frequency.setter
    def Frequency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Frequency'], value)

    @property
    def GPTPCapableReceiptTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of gPTP Capable Message Intervals that have to pass without receipt of a gPTP Capable Message to trigger timeout
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GPTPCapableReceiptTimeout']))

    @property
    def GmTimeBaseIndicator(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): GM Time Base Indicator field set in the gPTP FollowUp TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GmTimeBaseIndicator']))

    @property
    def GrandmasterID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tester should allow [0x0000 - 0xFFFF] value to be configured for grandmasterID.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GrandmasterID']))

    @property
    def GrandmasterIdentity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the ClockIdentity of the Grandmaster behind this device
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GrandmasterIdentity']))

    @property
    def GrantDelayRespDurationInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for DelayResp messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GrantDelayRespDurationInterval']))

    @property
    def GrantSyncDurationInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for Sync messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GrantSyncDurationInterval']))

    @property
    def GrantUnicastDurationInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GrantUnicastDurationInterval']))

    @property
    def HandleAnnounceTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send and respond to Announce TLV unicast requests in signal messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HandleAnnounceTlv']))

    @property
    def HandleCancelTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send and respond to Cancel TLV unicast requests in signal messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HandleCancelTlv']))

    @property
    def JumpSeconds(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The size of the next discontinuity, in seconds, of Local Time. A value of zero indicates that no discontinuity is expected.A positive value indicates that the discontinuity will cause the currentLocalOffset to increase.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['JumpSeconds']))

    @property
    def LastGmPhaseChange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Last GM Phase Change nanoseconds set in the gPTP FollowUp TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LastGmPhaseChange']))

    @property
    def LeapSecondJump(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The reason for the forthcoming discontinuity of currentLocalOffset indicated by timeOfNextJump.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LeapSecondJump']))

    @property
    def LearnPortId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Slave learns Master Port ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LearnPortId']))

    @property
    def LogAnnounceInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The log mean time interval between successive Announce messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LogAnnounceInterval']))

    @property
    def LogCleanUpOption(self):
        """
        Returns
        -------
        - str(notClean | clean): Debug Log Clean Up
        """
        return self._get_attribute(self._SDM_ATT_MAP['LogCleanUpOption'])
    @LogCleanUpOption.setter
    def LogCleanUpOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LogCleanUpOption'], value)

    @property
    def LogDelayReqInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The log mean time interval between successive (P)DelayReq messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LogDelayReqInterval']))

    @property
    def LogFileAge(self):
        """
        Returns
        -------
        - number: This field determines how old logs to be deleted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LogFileAge'])
    @LogFileAge.setter
    def LogFileAge(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LogFileAge'], value)

    @property
    def LogFuturePacketInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this option is enabled PTP will write next packet information if a user defined offset limit crosses
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LogFuturePacketInfo']))

    @property
    def LogManagementMsgInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The log mean time interval between successive Management messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LogManagementMsgInterval']))

    @property
    def LogSignallingInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The log mean time interval between successive Signaling messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LogSignallingInterval']))

    @property
    def LogSyncInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The log mean time interval between successive Sync messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LogSyncInterval']))

    @property
    def MasterClockId(self):
        """
        Returns
        -------
        - list(obj(ixnetwork_restpy.multivalue.Multivalue)): Displays the Clock ID of the directly connected master port (might not necessarily be the Grandmaster of the system). If simulating a Boundary port, it will show the configured Clock ID of the emulated Grandmaster.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MasterClockId']))

    @property
    def MasterCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The total number of Unicast masters to be used for this slave (at max 500).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MasterCount']))

    @property
    def MasterIpAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the base address to be used for enumerating all the addresses for this slave
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MasterIpAddress']))

    @property
    def MasterIpIncrementBy(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the increment to be used for enumerating all the addresses for this slave
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MasterIpIncrementBy']))

    @property
    def MasterIpv6Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the base address to be used for enumerating all the addresses for this slave
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MasterIpv6Address']))

    @property
    def MasterIpv6IncrementBy(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the increment to be used for enumerating all the addresses for this slave
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MasterIpv6IncrementBy']))

    @property
    def MasterLockingStatus(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Complementary information to clockClass
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MasterLockingStatus']))

    @property
    def MasterMacAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the base address to be used for enumerating all the addresses for this slave
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MasterMacAddress']))

    @property
    def MasterMacIncrementBy(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the increment to be used for enumerating all the addresses for this slave
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MasterMacIncrementBy']))

    @property
    def MeanLinkDelayThreshold(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The propagation time threshold, above which a port is not considered capable of participating in the IEEE 802.1AS protocol.The Value should be between 0 and 9223372036854775807.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MeanLinkDelayThreshold']))

    @property
    def MulticastAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The destination multicast address for G8275.1: non-forwardable (01:80:C2:00:00:0E, recommended) or forwardable (01:1B:19:00:00:00)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MulticastAddress']))

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NanosecondsPerSecond(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of nanoseconds the emulated clock should effectively count for one second of hardware ticks
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NanosecondsPerSecond']))

    @property
    def NotSlave(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When enabled for Master clocks it prevents a G8275.1 port from going into Slave state, by ignoring Announce messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NotSlave']))

    @property
    def NumRecords(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number Of Records To Be Logged if user defined offset limit is crossed.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumRecords']))

    @property
    def NumberOFMsgs(self):
        """
        Returns
        -------
        - number: Messages Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOFMsgs'])
    @NumberOFMsgs.setter
    def NumberOFMsgs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOFMsgs'], value)

    @property
    def OffsetBaseddebuggabilityEnabled(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this option is enabled PTP will write log if a user defined offset limit crosses
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OffsetBaseddebuggabilityEnabled']))

    @property
    def OffsetLimit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User defined offset limit in nanosecond. When offset crosses this limit PTP will generate a Log
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OffsetLimit']))

    @property
    def OffsetScaledLogVariance(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Static Offset Scaled Log Variance of this clock
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OffsetScaledLogVariance']))

    @property
    def OneWay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Do not send Delay Requests
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OneWay']))

    @property
    def PDelayFollowUpDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Additional delay introduced in the PdelayResp FollowUp message (ns)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PDelayFollowUpDelay']))

    @property
    def PDelayFollowUpDelayInsertionRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage rate of the PdelayResp FollowUp messages in which the delay is introduced
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PDelayFollowUpDelayInsertionRate']))

    @property
    def PDelayFollowUpDropRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage rate of the dropped PdelayResp FollowUp messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PDelayFollowUpDropRate']))

    @property
    def PDelayFollowUpResidenceTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Total residence time of PdelayReq and PdelayResp messages through an associated two-step end-to-end transparent clock inserted in the correction field of PdelayRespFollowUp messages sent by this clock.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PDelayFollowUpResidenceTime']))

    @property
    def PathTraceTLV(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the master will append a Path Trace TLV to Announce messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PathTraceTLV']))

    @property
    def PortNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value of the portNumber for a port on a PTP node supporting a single PTP port shall be 1. The values of the port numbers for the N ports on a PTP node supporting N PTP ports shall be 1, 2, N, respectively.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PortNumber']))

    @property
    def PreviousJamLocalOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value of currentLocalOffset at the time of the previous Daily Jam event.If a discontinuity of Local Time occurs at the jam time, this parameter reflects the offset after the discontinuity.The default value shall be the current value of currentLocalOffset.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PreviousJamLocalOffset']))

    @property
    def Priority1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PTP priority1.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Priority1']))

    @property
    def Priority2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PTP priority2
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Priority2']))

    @property
    def Profile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The profile used by this clock
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Profile']))

    @property
    def PtpState(self):
        """
        Returns
        -------
        - list(str[disabled | faulty | grandmaster | initializing | listening | master | passive | preMaster | slave | transparentGrandmaster | transparentMaster | uncalibrated]): Displays the current PTP State
        """
        return self._get_attribute(self._SDM_ATT_MAP['PtpState'])

    @property
    def RenewalInvited(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set the Renewal Invited flag in Grant Unicast Transmission TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RenewalInvited']))

    @property
    def RequestAttempts(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of succesive requests a slave can request before entering into holddown.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RequestAttempts']))

    @property
    def RequestHolddown(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time between succesive requests if denied/timeout for Signal Request
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RequestHolddown']))

    @property
    def RequestInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time between succesive requests if denied/timeout for Signal Request
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RequestInterval']))

    @property
    def Reserved(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IEEE_C37_238 TLV Reserved
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def ReverseSync(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): As a slave, periodically send Reverse Sync messages with recovered clock. As a master, calculate the Offset of the Slave reported time to master time
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReverseSync']))

    @property
    def ReverseSyncIntervalPercent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The percentage of incoming Sync interval to use for Reverse Sync interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReverseSyncIntervalPercent']))

    @property
    def Role(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The desired role of this clock (Masters may become Slave as per BMCA)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Role']))

    @property
    def RxCalibration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The amount of time (in ns) that the Receive side timestamp needs to be offset to allow for error
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RxCalibration']))

    @property
    def ScaledLastGmFreqChange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Scaled Last GM Freq Change field set in the gPTP FollowUp TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ScaledLastGmFreqChange']))

    @property
    def SendMulticastAnnounce(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send multicast Announce messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendMulticastAnnounce']))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[announceReceiptTimeout | aSCapable | delayRespReceiptTimeout | g82651Layer | g82751ClockAccuracy | g82751ClockClass | g82751Domain | g82751Layer | g82751LogVariance | g82751Priority1 | g82751Rates | g82751VLANs | gPTPCapable | gPTPLayer | handleAnnounceTlvUnckecked | multipleP2PResponses | noAnnounce | none | p2PMixedMode | pathTraceDropAnnounce | signalAnnounceTimeout | signalDelayRespTimeout | signalIntervalGrantDelayRespDuration | signalIntervalGrantDuration | signalIntervalGrantSyncDuration | signalSyncTimeout | sMPTELayer | syncReceiptTimeout | syncReceiptTimeoutgPTP]): Logs additional information about the session state
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def SignalInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time between Signal Request messages, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SignalInterval']))

    @property
    def SignalUnicastHandling(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies how signal messages are exchanged when unicast communication mode is in effect.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SignalUnicastHandling']))

    @property
    def SignallingDropRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage rate of the dropped Signalling messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SignallingDropRate']))

    @property
    def SimulateBoundary(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Simulate a Grandmaster port behind this clock acting as a Boundary clock
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SimulateBoundary']))

    @property
    def SimulateTransparent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Simulate a transparent clock in front of this master clock.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SimulateTransparent']))

    @property
    def SlaveCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The total number of Unicast slaves to be used for this master.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlaveCount']))

    @property
    def SlaveIpAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the base address to be used for enumerating all the addresses for this master
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlaveIpAddress']))

    @property
    def SlaveIpIncrementBy(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the increment to be used for enumerating all the addresses for this master
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlaveIpIncrementBy']))

    @property
    def SlaveIpv6Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the base address to be used for enumerating all the addresses for this master
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlaveIpv6Address']))

    @property
    def SlaveIpv6IncrementBy(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the increment to be used for enumerating all the addresses for this master
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlaveIpv6IncrementBy']))

    @property
    def SlaveMacAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the base address to be used for enumerating all the addresses for this master
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlaveMacAddress']))

    @property
    def SlaveMacIncrementBy(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the increment to be used for enumerating all the addresses for this master
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlaveMacIncrementBy']))

    @property
    def StackedLayers(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StackedLayers'], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateCounts'])

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def StepMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Clock step mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StepMode']))

    @property
    def StepsRemoved(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Steps Removed field advertised in Announce Messages, representing the number of hops between this emulated Boundary clock and the Grandmaster clock (including it). Valid values: 0 to 65,535.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StepsRemoved']))

    @property
    def StrictGrant(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the master will not grant values that are above maximum offered values
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StrictGrant']))

    @property
    def SyncDropRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage rate of the dropped Sync messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SyncDropRate']))

    @property
    def SyncReceiptTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of seconds that have to pass without receipt of a Sync message to trigger timeout.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SyncReceiptTimeout']))

    @property
    def SyncReceiptTimeoutgPTP(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of Sync Intervals that have to pass without receipt of a Sync message to trigger timeout.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SyncReceiptTimeoutgPTP']))

    @property
    def SyncResidenceTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Master to slave residence time of Sync messages through an associated one-step transparent clock inserted in the correction field of Sync messages sent by this clock
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SyncResidenceTime']))

    @property
    def TimeAddressFlags(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the intended SMPTE ST 12-1 flags.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeAddressFlags']))

    @property
    def TimeOfNextJam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value of the second portion of the PTP time corresponding to the next scheduled occurrence of the Daily Jam.If no Daily Jam is scheduled, the value of timeOfNextJam shall be zero.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeOfNextJam']))

    @property
    def TimeOfNextJump(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value of the second portion of the grandmaster PTP time at the time when the next discontinuity of the currentLocalOffset will occur.The discontinuity occurs at the start of the second indicated.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeOfNextJump']))

    @property
    def TimeOfPreviousJam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value of the second portion of the PTP time corresponding to the previous occurrence of the Daily Jam.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeOfPreviousJam']))

    @property
    def TimeSource(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time source for the PTP device
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeSource']))

    @property
    def TimestampOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The initial offset added to the local clock when starting the session
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimestampOffset']))

    @property
    def TotalTimeInaccuracy(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Total Time Inaccuracy
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TotalTimeInaccuracy']))

    @property
    def TxCalibration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The amount of time (in ns) that the transmit timestamp of one step messages (Sync, PdelayResp) needs to be adjusted for error
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TxCalibration']))

    @property
    def TxTwoStepCalibration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The amount of time (in ns) that the read transmit timestamp of sent messages (two-step Sync, DelayReq, PdelayReq, two-step PdelayResp) needs to be adjusted for error
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TxTwoStepCalibration']))

    @property
    def UpdateTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Clocks in Slave role will correct their time based on received Sync messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UpdateTime']))

    def update(self, AtoiTlvCount=None, AvnuMode=None, ConnectedVia=None, EnableATOITlv=None, EnableCmlds=None, EnableNegativeTesting=None, Frequency=None, LogCleanUpOption=None, LogFileAge=None, Multiplier=None, Name=None, NumberOFMsgs=None, StackedLayers=None):
        """Updates ptp resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - AtoiTlvCount (number): ATOI TLV Count
        - AvnuMode (str(aVNU_NA | aVNU_GPTP)): AVNU Mode
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - EnableATOITlv (bool): Enable ATOI TLV
        - EnableCmlds (bool): Enable Cmlds
        - EnableNegativeTesting (bool): Enable Negative Conformance Test
        - Frequency (number): Frequency(N)
        - LogCleanUpOption (str(notClean | clean)): Debug Log Clean Up
        - LogFileAge (number): This field determines how old logs to be deleted.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOFMsgs (number): Messages Count
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AtoiTlvCount=None, AvnuMode=None, ConnectedVia=None, EnableATOITlv=None, EnableCmlds=None, EnableNegativeTesting=None, Frequency=None, LogCleanUpOption=None, LogFileAge=None, Multiplier=None, Name=None, NumberOFMsgs=None, StackedLayers=None):
        """Adds a new ptp resource on the server and adds it to the container.

        Args
        ----
        - AtoiTlvCount (number): ATOI TLV Count
        - AvnuMode (str(aVNU_NA | aVNU_GPTP)): AVNU Mode
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - EnableATOITlv (bool): Enable ATOI TLV
        - EnableCmlds (bool): Enable Cmlds
        - EnableNegativeTesting (bool): Enable Negative Conformance Test
        - Frequency (number): Frequency(N)
        - LogCleanUpOption (str(notClean | clean)): Debug Log Clean Up
        - LogFileAge (number): This field determines how old logs to be deleted.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOFMsgs (number): Messages Count
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved ptp resources using find and the newly added ptp resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ptp resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AtoiTlvCount=None, AvnuMode=None, ConnectedVia=None, Count=None, DescriptiveName=None, EnableATOITlv=None, EnableCmlds=None, EnableNegativeTesting=None, Errors=None, Frequency=None, LogCleanUpOption=None, LogFileAge=None, Multiplier=None, Name=None, NumberOFMsgs=None, PtpState=None, SessionInfo=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves ptp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ptp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ptp resources from the server.

        Args
        ----
        - AtoiTlvCount (number): ATOI TLV Count
        - AvnuMode (str(aVNU_NA | aVNU_GPTP)): AVNU Mode
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - EnableATOITlv (bool): Enable ATOI TLV
        - EnableCmlds (bool): Enable Cmlds
        - EnableNegativeTesting (bool): Enable Negative Conformance Test
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Frequency (number): Frequency(N)
        - LogCleanUpOption (str(notClean | clean)): Debug Log Clean Up
        - LogFileAge (number): This field determines how old logs to be deleted.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOFMsgs (number): Messages Count
        - PtpState (list(str[disabled | faulty | grandmaster | initializing | listening | master | passive | preMaster | slave | transparentGrandmaster | transparentMaster | uncalibrated])): Displays the current PTP State
        - SessionInfo (list(str[announceReceiptTimeout | aSCapable | delayRespReceiptTimeout | g82651Layer | g82751ClockAccuracy | g82751ClockClass | g82751Domain | g82751Layer | g82751LogVariance | g82751Priority1 | g82751Rates | g82751VLANs | gPTPCapable | gPTPLayer | handleAnnounceTlvUnckecked | multipleP2PResponses | noAnnounce | none | p2PMixedMode | pathTraceDropAnnounce | signalAnnounceTimeout | signalDelayRespTimeout | signalIntervalGrantDelayRespDuration | signalIntervalGrantDuration | signalIntervalGrantSyncDuration | signalSyncTimeout | sMPTELayer | syncReceiptTimeout | syncReceiptTimeoutgPTP])): Logs additional information about the session state
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching ptp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ptp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ptp resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, AllowedFaults=None, AllowedLostResponse=None, AlternateMasterFlag=None, AnnounceCurrentUtcOffsetValid=None, AnnounceDropRate=None, AnnounceFrequencyTraceable=None, AnnounceLeap59=None, AnnounceLeap61=None, AnnouncePtpTimescale=None, AnnounceReceiptTimeout=None, AnnounceTimeTraceable=None, Bmca=None, ClockAccuracy=None, ClockClass=None, ClockIdentity=None, CommunicationMode=None, CumulativeScaledRateOffset=None, CurrentLocalOffset=None, CurrentUtcOffset=None, CustomClockId=None, DaylightSaving=None, DefaultSystemFrameRateDenominator=None, DefaultSystemFrameRateNumerator=None, DelayAsymmetry=None, DelayMechanism=None, DelayReqDropRate=None, DelayReqOffset=None, DelayReqResidenceTime=None, DelayReqSpread=None, DelayRespDropRate=None, DelayRespReceiptTimeout=None, DelayRespResidenceTime=None, DelayResponseDelay=None, DelayResponseDelayInsertionRate=None, Domain=None, DropMalformed=None, DropSignalReqAnnounce=None, DropSignalReqDelayResp=None, DropSignalReqSync=None, FolderPath=None, FollowUpBadCrcRate=None, FollowUpDelay=None, FollowUpDelayInsertionRate=None, FollowUpDropRate=None, FollowUpResidenceTime=None, GPTPCapableReceiptTimeout=None, GmTimeBaseIndicator=None, GrandmasterID=None, GrandmasterIdentity=None, GrantDelayRespDurationInterval=None, GrantSyncDurationInterval=None, GrantUnicastDurationInterval=None, HandleAnnounceTlv=None, HandleCancelTlv=None, JumpSeconds=None, LastGmPhaseChange=None, LeapSecondJump=None, LearnPortId=None, LogAnnounceInterval=None, LogDelayReqInterval=None, LogFuturePacketInfo=None, LogManagementMsgInterval=None, LogSignallingInterval=None, LogSyncInterval=None, MasterClockId=None, MasterCount=None, MasterIpAddress=None, MasterIpIncrementBy=None, MasterIpv6Address=None, MasterIpv6IncrementBy=None, MasterLockingStatus=None, MasterMacAddress=None, MasterMacIncrementBy=None, MeanLinkDelayThreshold=None, MulticastAddress=None, NanosecondsPerSecond=None, NotSlave=None, NumRecords=None, OffsetBaseddebuggabilityEnabled=None, OffsetLimit=None, OffsetScaledLogVariance=None, OneWay=None, PDelayFollowUpDelay=None, PDelayFollowUpDelayInsertionRate=None, PDelayFollowUpDropRate=None, PDelayFollowUpResidenceTime=None, PathTraceTLV=None, PortNumber=None, PreviousJamLocalOffset=None, Priority1=None, Priority2=None, Profile=None, RenewalInvited=None, RequestAttempts=None, RequestHolddown=None, RequestInterval=None, Reserved=None, ReverseSync=None, ReverseSyncIntervalPercent=None, Role=None, RxCalibration=None, ScaledLastGmFreqChange=None, SendMulticastAnnounce=None, SignalInterval=None, SignalUnicastHandling=None, SignallingDropRate=None, SimulateBoundary=None, SimulateTransparent=None, SlaveCount=None, SlaveIpAddress=None, SlaveIpIncrementBy=None, SlaveIpv6Address=None, SlaveIpv6IncrementBy=None, SlaveMacAddress=None, SlaveMacIncrementBy=None, StepMode=None, StepsRemoved=None, StrictGrant=None, SyncDropRate=None, SyncReceiptTimeout=None, SyncReceiptTimeoutgPTP=None, SyncResidenceTime=None, TimeAddressFlags=None, TimeOfNextJam=None, TimeOfNextJump=None, TimeOfPreviousJam=None, TimeSource=None, TimestampOffset=None, TotalTimeInaccuracy=None, TxCalibration=None, TxTwoStepCalibration=None, UpdateTime=None):
        """Base class infrastructure that gets a list of ptp device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AllowedFaults (str): optional regex of allowedFaults
        - AllowedLostResponse (str): optional regex of allowedLostResponse
        - AlternateMasterFlag (str): optional regex of alternateMasterFlag
        - AnnounceCurrentUtcOffsetValid (str): optional regex of announceCurrentUtcOffsetValid
        - AnnounceDropRate (str): optional regex of announceDropRate
        - AnnounceFrequencyTraceable (str): optional regex of announceFrequencyTraceable
        - AnnounceLeap59 (str): optional regex of announceLeap59
        - AnnounceLeap61 (str): optional regex of announceLeap61
        - AnnouncePtpTimescale (str): optional regex of announcePtpTimescale
        - AnnounceReceiptTimeout (str): optional regex of announceReceiptTimeout
        - AnnounceTimeTraceable (str): optional regex of announceTimeTraceable
        - Bmca (str): optional regex of bmca
        - ClockAccuracy (str): optional regex of clockAccuracy
        - ClockClass (str): optional regex of clockClass
        - ClockIdentity (str): optional regex of clockIdentity
        - CommunicationMode (str): optional regex of communicationMode
        - CumulativeScaledRateOffset (str): optional regex of cumulativeScaledRateOffset
        - CurrentLocalOffset (str): optional regex of currentLocalOffset
        - CurrentUtcOffset (str): optional regex of currentUtcOffset
        - CustomClockId (str): optional regex of customClockId
        - DaylightSaving (str): optional regex of daylightSaving
        - DefaultSystemFrameRateDenominator (str): optional regex of defaultSystemFrameRateDenominator
        - DefaultSystemFrameRateNumerator (str): optional regex of defaultSystemFrameRateNumerator
        - DelayAsymmetry (str): optional regex of delayAsymmetry
        - DelayMechanism (str): optional regex of delayMechanism
        - DelayReqDropRate (str): optional regex of delayReqDropRate
        - DelayReqOffset (str): optional regex of delayReqOffset
        - DelayReqResidenceTime (str): optional regex of delayReqResidenceTime
        - DelayReqSpread (str): optional regex of delayReqSpread
        - DelayRespDropRate (str): optional regex of delayRespDropRate
        - DelayRespReceiptTimeout (str): optional regex of delayRespReceiptTimeout
        - DelayRespResidenceTime (str): optional regex of delayRespResidenceTime
        - DelayResponseDelay (str): optional regex of delayResponseDelay
        - DelayResponseDelayInsertionRate (str): optional regex of delayResponseDelayInsertionRate
        - Domain (str): optional regex of domain
        - DropMalformed (str): optional regex of dropMalformed
        - DropSignalReqAnnounce (str): optional regex of dropSignalReqAnnounce
        - DropSignalReqDelayResp (str): optional regex of dropSignalReqDelayResp
        - DropSignalReqSync (str): optional regex of dropSignalReqSync
        - FolderPath (str): optional regex of folderPath
        - FollowUpBadCrcRate (str): optional regex of followUpBadCrcRate
        - FollowUpDelay (str): optional regex of followUpDelay
        - FollowUpDelayInsertionRate (str): optional regex of followUpDelayInsertionRate
        - FollowUpDropRate (str): optional regex of followUpDropRate
        - FollowUpResidenceTime (str): optional regex of followUpResidenceTime
        - GPTPCapableReceiptTimeout (str): optional regex of gPTPCapableReceiptTimeout
        - GmTimeBaseIndicator (str): optional regex of gmTimeBaseIndicator
        - GrandmasterID (str): optional regex of grandmasterID
        - GrandmasterIdentity (str): optional regex of grandmasterIdentity
        - GrantDelayRespDurationInterval (str): optional regex of grantDelayRespDurationInterval
        - GrantSyncDurationInterval (str): optional regex of grantSyncDurationInterval
        - GrantUnicastDurationInterval (str): optional regex of grantUnicastDurationInterval
        - HandleAnnounceTlv (str): optional regex of handleAnnounceTlv
        - HandleCancelTlv (str): optional regex of handleCancelTlv
        - JumpSeconds (str): optional regex of jumpSeconds
        - LastGmPhaseChange (str): optional regex of lastGmPhaseChange
        - LeapSecondJump (str): optional regex of leapSecondJump
        - LearnPortId (str): optional regex of learnPortId
        - LogAnnounceInterval (str): optional regex of logAnnounceInterval
        - LogDelayReqInterval (str): optional regex of logDelayReqInterval
        - LogFuturePacketInfo (str): optional regex of logFuturePacketInfo
        - LogManagementMsgInterval (str): optional regex of logManagementMsgInterval
        - LogSignallingInterval (str): optional regex of logSignallingInterval
        - LogSyncInterval (str): optional regex of logSyncInterval
        - MasterClockId (str): optional regex of masterClockId
        - MasterCount (str): optional regex of masterCount
        - MasterIpAddress (str): optional regex of masterIpAddress
        - MasterIpIncrementBy (str): optional regex of masterIpIncrementBy
        - MasterIpv6Address (str): optional regex of masterIpv6Address
        - MasterIpv6IncrementBy (str): optional regex of masterIpv6IncrementBy
        - MasterLockingStatus (str): optional regex of masterLockingStatus
        - MasterMacAddress (str): optional regex of masterMacAddress
        - MasterMacIncrementBy (str): optional regex of masterMacIncrementBy
        - MeanLinkDelayThreshold (str): optional regex of meanLinkDelayThreshold
        - MulticastAddress (str): optional regex of multicastAddress
        - NanosecondsPerSecond (str): optional regex of nanosecondsPerSecond
        - NotSlave (str): optional regex of notSlave
        - NumRecords (str): optional regex of numRecords
        - OffsetBaseddebuggabilityEnabled (str): optional regex of offsetBaseddebuggabilityEnabled
        - OffsetLimit (str): optional regex of offsetLimit
        - OffsetScaledLogVariance (str): optional regex of offsetScaledLogVariance
        - OneWay (str): optional regex of oneWay
        - PDelayFollowUpDelay (str): optional regex of pDelayFollowUpDelay
        - PDelayFollowUpDelayInsertionRate (str): optional regex of pDelayFollowUpDelayInsertionRate
        - PDelayFollowUpDropRate (str): optional regex of pDelayFollowUpDropRate
        - PDelayFollowUpResidenceTime (str): optional regex of pDelayFollowUpResidenceTime
        - PathTraceTLV (str): optional regex of pathTraceTLV
        - PortNumber (str): optional regex of portNumber
        - PreviousJamLocalOffset (str): optional regex of previousJamLocalOffset
        - Priority1 (str): optional regex of priority1
        - Priority2 (str): optional regex of priority2
        - Profile (str): optional regex of profile
        - RenewalInvited (str): optional regex of renewalInvited
        - RequestAttempts (str): optional regex of requestAttempts
        - RequestHolddown (str): optional regex of requestHolddown
        - RequestInterval (str): optional regex of requestInterval
        - Reserved (str): optional regex of reserved
        - ReverseSync (str): optional regex of reverseSync
        - ReverseSyncIntervalPercent (str): optional regex of reverseSyncIntervalPercent
        - Role (str): optional regex of role
        - RxCalibration (str): optional regex of rxCalibration
        - ScaledLastGmFreqChange (str): optional regex of scaledLastGmFreqChange
        - SendMulticastAnnounce (str): optional regex of sendMulticastAnnounce
        - SignalInterval (str): optional regex of signalInterval
        - SignalUnicastHandling (str): optional regex of signalUnicastHandling
        - SignallingDropRate (str): optional regex of signallingDropRate
        - SimulateBoundary (str): optional regex of simulateBoundary
        - SimulateTransparent (str): optional regex of simulateTransparent
        - SlaveCount (str): optional regex of slaveCount
        - SlaveIpAddress (str): optional regex of slaveIpAddress
        - SlaveIpIncrementBy (str): optional regex of slaveIpIncrementBy
        - SlaveIpv6Address (str): optional regex of slaveIpv6Address
        - SlaveIpv6IncrementBy (str): optional regex of slaveIpv6IncrementBy
        - SlaveMacAddress (str): optional regex of slaveMacAddress
        - SlaveMacIncrementBy (str): optional regex of slaveMacIncrementBy
        - StepMode (str): optional regex of stepMode
        - StepsRemoved (str): optional regex of stepsRemoved
        - StrictGrant (str): optional regex of strictGrant
        - SyncDropRate (str): optional regex of syncDropRate
        - SyncReceiptTimeout (str): optional regex of syncReceiptTimeout
        - SyncReceiptTimeoutgPTP (str): optional regex of syncReceiptTimeoutgPTP
        - SyncResidenceTime (str): optional regex of syncResidenceTime
        - TimeAddressFlags (str): optional regex of timeAddressFlags
        - TimeOfNextJam (str): optional regex of timeOfNextJam
        - TimeOfNextJump (str): optional regex of timeOfNextJump
        - TimeOfPreviousJam (str): optional regex of timeOfPreviousJam
        - TimeSource (str): optional regex of timeSource
        - TimestampOffset (str): optional regex of timestampOffset
        - TotalTimeInaccuracy (str): optional regex of totalTimeInaccuracy
        - TxCalibration (str): optional regex of txCalibration
        - TxTwoStepCalibration (str): optional regex of txTwoStepCalibration
        - UpdateTime (str): optional regex of updateTime

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self, *args, **kwargs):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        abort(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def GPtpSendSignaling(self, *args, **kwargs):
        """Executes the gPtpSendSignaling operation on the server.

        Send Signaling messages for the selected PTP IEEE 802.1AS items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        gPtpSendSignaling(LinkDelayInterval=enum, TimeSyncInterval=enum, AnnounceInterval=enum, ComputeNeighborRateRatio=bool, ComputeNeighborPropDelay=bool)list
        ---------------------------------------------------------------------------------------------------------------------------------------------------------
        - LinkDelayInterval (str(enumOpt-DoNotChange | enumOpt-Initial | enumOpt-Stop | enumOpt-V0_1_per_second_ | enumOpt-V1_1_per_2_seconds_ | enumOpt-V2_1_per_4_seconds_ | enumOpt-V3_1_per_8_seconds_ | enumOpt-V4_1_per_16_seconds_ | enumOpt-V5_1_per_32_seconds_ | enumOpt-V6_1_per_64_seconds_ | enumOpt-V7_1_per_128_seconds_ | enumOpt-V8_1_per_256_seconds_ | enumOpt-V9_1_per_512_seconds_ | enumOpt-Vneg1_2_per_second_ | enumOpt-Vneg2_4_per_second_ | enumOpt-Vneg3_8_per_second_ | enumOpt-Vneg4_16_per_second_ | enumOpt-Vneg5_32_per_second_ | enumOpt-Vneg6_64_per_second_ | enumOpt-Vneg7_128_per_second_ | enumOpt-Vneg8_256_per_second_ | enumOpt-Vneg9_512_per_second_)): This parameter requires a linkDelayInterval of type kEnumValue=enumOpt-DoNotChange,enumOpt-Initial,enumOpt-Stop,enumOpt-V0_1_per_second_,enumOpt-V1_1_per_2_seconds_,enumOpt-V2_1_per_4_seconds_,enumOpt-V3_1_per_8_seconds_,enumOpt-V4_1_per_16_seconds_,enumOpt-V5_1_per_32_seconds_,enumOpt-V6_1_per_64_seconds_,enumOpt-V7_1_per_128_seconds_,enumOpt-V8_1_per_256_seconds_,enumOpt-V9_1_per_512_seconds_,enumOpt-Vneg1_2_per_second_,enumOpt-Vneg2_4_per_second_,enumOpt-Vneg3_8_per_second_,enumOpt-Vneg4_16_per_second_,enumOpt-Vneg5_32_per_second_,enumOpt-Vneg6_64_per_second_,enumOpt-Vneg7_128_per_second_,enumOpt-Vneg8_256_per_second_,enumOpt-Vneg9_512_per_second_
        - TimeSyncInterval (str(enumOpt-DoNotChange | enumOpt-Initial | enumOpt-Stop | enumOpt-V0_1_per_second_ | enumOpt-V1_1_per_2_seconds_ | enumOpt-V2_1_per_4_seconds_ | enumOpt-V3_1_per_8_seconds_ | enumOpt-V4_1_per_16_seconds_ | enumOpt-V5_1_per_32_seconds_ | enumOpt-V6_1_per_64_seconds_ | enumOpt-V7_1_per_128_seconds_ | enumOpt-V8_1_per_256_seconds_ | enumOpt-V9_1_per_512_seconds_ | enumOpt-Vneg1_2_per_second_ | enumOpt-Vneg2_4_per_second_ | enumOpt-Vneg3_8_per_second_ | enumOpt-Vneg4_16_per_second_ | enumOpt-Vneg5_32_per_second_ | enumOpt-Vneg6_64_per_second_ | enumOpt-Vneg7_128_per_second_ | enumOpt-Vneg8_256_per_second_ | enumOpt-Vneg9_512_per_second_)): This parameter requires a timeSyncInterval of type kEnumValue=enumOpt-DoNotChange,enumOpt-Initial,enumOpt-Stop,enumOpt-V0_1_per_second_,enumOpt-V1_1_per_2_seconds_,enumOpt-V2_1_per_4_seconds_,enumOpt-V3_1_per_8_seconds_,enumOpt-V4_1_per_16_seconds_,enumOpt-V5_1_per_32_seconds_,enumOpt-V6_1_per_64_seconds_,enumOpt-V7_1_per_128_seconds_,enumOpt-V8_1_per_256_seconds_,enumOpt-V9_1_per_512_seconds_,enumOpt-Vneg1_2_per_second_,enumOpt-Vneg2_4_per_second_,enumOpt-Vneg3_8_per_second_,enumOpt-Vneg4_16_per_second_,enumOpt-Vneg5_32_per_second_,enumOpt-Vneg6_64_per_second_,enumOpt-Vneg7_128_per_second_,enumOpt-Vneg8_256_per_second_,enumOpt-Vneg9_512_per_second_
        - AnnounceInterval (str(enumOpt-DoNotChange | enumOpt-Initial | enumOpt-Stop | enumOpt-V0_1_per_second_ | enumOpt-V1_1_per_2_seconds_ | enumOpt-V2_1_per_4_seconds_ | enumOpt-V3_1_per_8_seconds_ | enumOpt-V4_1_per_16_seconds_ | enumOpt-V5_1_per_32_seconds_ | enumOpt-V6_1_per_64_seconds_ | enumOpt-V7_1_per_128_seconds_ | enumOpt-V8_1_per_256_seconds_ | enumOpt-V9_1_per_512_seconds_ | enumOpt-Vneg1_2_per_second_ | enumOpt-Vneg2_4_per_second_ | enumOpt-Vneg3_8_per_second_ | enumOpt-Vneg4_16_per_second_ | enumOpt-Vneg5_32_per_second_ | enumOpt-Vneg6_64_per_second_ | enumOpt-Vneg7_128_per_second_ | enumOpt-Vneg8_256_per_second_ | enumOpt-Vneg9_512_per_second_)): This parameter requires a announceInterval of type kEnumValue=enumOpt-DoNotChange,enumOpt-Initial,enumOpt-Stop,enumOpt-V0_1_per_second_,enumOpt-V1_1_per_2_seconds_,enumOpt-V2_1_per_4_seconds_,enumOpt-V3_1_per_8_seconds_,enumOpt-V4_1_per_16_seconds_,enumOpt-V5_1_per_32_seconds_,enumOpt-V6_1_per_64_seconds_,enumOpt-V7_1_per_128_seconds_,enumOpt-V8_1_per_256_seconds_,enumOpt-V9_1_per_512_seconds_,enumOpt-Vneg1_2_per_second_,enumOpt-Vneg2_4_per_second_,enumOpt-Vneg3_8_per_second_,enumOpt-Vneg4_16_per_second_,enumOpt-Vneg5_32_per_second_,enumOpt-Vneg6_64_per_second_,enumOpt-Vneg7_128_per_second_,enumOpt-Vneg8_256_per_second_,enumOpt-Vneg9_512_per_second_
        - ComputeNeighborRateRatio (bool): This parameter requires a computeNeighborRateRatio of type kBool
        - ComputeNeighborPropDelay (bool): This parameter requires a computeNeighborPropDelay of type kBool
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        gPtpSendSignaling(LinkDelayInterval=enum, TimeSyncInterval=enum, AnnounceInterval=enum, ComputeNeighborRateRatio=bool, ComputeNeighborPropDelay=bool, SessionIndices=list)list
        ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - LinkDelayInterval (str(enumOpt-DoNotChange | enumOpt-Initial | enumOpt-Stop | enumOpt-V0_1_per_second_ | enumOpt-V1_1_per_2_seconds_ | enumOpt-V2_1_per_4_seconds_ | enumOpt-V3_1_per_8_seconds_ | enumOpt-V4_1_per_16_seconds_ | enumOpt-V5_1_per_32_seconds_ | enumOpt-V6_1_per_64_seconds_ | enumOpt-V7_1_per_128_seconds_ | enumOpt-V8_1_per_256_seconds_ | enumOpt-V9_1_per_512_seconds_ | enumOpt-Vneg1_2_per_second_ | enumOpt-Vneg2_4_per_second_ | enumOpt-Vneg3_8_per_second_ | enumOpt-Vneg4_16_per_second_ | enumOpt-Vneg5_32_per_second_ | enumOpt-Vneg6_64_per_second_ | enumOpt-Vneg7_128_per_second_ | enumOpt-Vneg8_256_per_second_ | enumOpt-Vneg9_512_per_second_)): This parameter requires a linkDelayInterval of type kEnumValue=enumOpt-DoNotChange,enumOpt-Initial,enumOpt-Stop,enumOpt-V0_1_per_second_,enumOpt-V1_1_per_2_seconds_,enumOpt-V2_1_per_4_seconds_,enumOpt-V3_1_per_8_seconds_,enumOpt-V4_1_per_16_seconds_,enumOpt-V5_1_per_32_seconds_,enumOpt-V6_1_per_64_seconds_,enumOpt-V7_1_per_128_seconds_,enumOpt-V8_1_per_256_seconds_,enumOpt-V9_1_per_512_seconds_,enumOpt-Vneg1_2_per_second_,enumOpt-Vneg2_4_per_second_,enumOpt-Vneg3_8_per_second_,enumOpt-Vneg4_16_per_second_,enumOpt-Vneg5_32_per_second_,enumOpt-Vneg6_64_per_second_,enumOpt-Vneg7_128_per_second_,enumOpt-Vneg8_256_per_second_,enumOpt-Vneg9_512_per_second_
        - TimeSyncInterval (str(enumOpt-DoNotChange | enumOpt-Initial | enumOpt-Stop | enumOpt-V0_1_per_second_ | enumOpt-V1_1_per_2_seconds_ | enumOpt-V2_1_per_4_seconds_ | enumOpt-V3_1_per_8_seconds_ | enumOpt-V4_1_per_16_seconds_ | enumOpt-V5_1_per_32_seconds_ | enumOpt-V6_1_per_64_seconds_ | enumOpt-V7_1_per_128_seconds_ | enumOpt-V8_1_per_256_seconds_ | enumOpt-V9_1_per_512_seconds_ | enumOpt-Vneg1_2_per_second_ | enumOpt-Vneg2_4_per_second_ | enumOpt-Vneg3_8_per_second_ | enumOpt-Vneg4_16_per_second_ | enumOpt-Vneg5_32_per_second_ | enumOpt-Vneg6_64_per_second_ | enumOpt-Vneg7_128_per_second_ | enumOpt-Vneg8_256_per_second_ | enumOpt-Vneg9_512_per_second_)): This parameter requires a timeSyncInterval of type kEnumValue=enumOpt-DoNotChange,enumOpt-Initial,enumOpt-Stop,enumOpt-V0_1_per_second_,enumOpt-V1_1_per_2_seconds_,enumOpt-V2_1_per_4_seconds_,enumOpt-V3_1_per_8_seconds_,enumOpt-V4_1_per_16_seconds_,enumOpt-V5_1_per_32_seconds_,enumOpt-V6_1_per_64_seconds_,enumOpt-V7_1_per_128_seconds_,enumOpt-V8_1_per_256_seconds_,enumOpt-V9_1_per_512_seconds_,enumOpt-Vneg1_2_per_second_,enumOpt-Vneg2_4_per_second_,enumOpt-Vneg3_8_per_second_,enumOpt-Vneg4_16_per_second_,enumOpt-Vneg5_32_per_second_,enumOpt-Vneg6_64_per_second_,enumOpt-Vneg7_128_per_second_,enumOpt-Vneg8_256_per_second_,enumOpt-Vneg9_512_per_second_
        - AnnounceInterval (str(enumOpt-DoNotChange | enumOpt-Initial | enumOpt-Stop | enumOpt-V0_1_per_second_ | enumOpt-V1_1_per_2_seconds_ | enumOpt-V2_1_per_4_seconds_ | enumOpt-V3_1_per_8_seconds_ | enumOpt-V4_1_per_16_seconds_ | enumOpt-V5_1_per_32_seconds_ | enumOpt-V6_1_per_64_seconds_ | enumOpt-V7_1_per_128_seconds_ | enumOpt-V8_1_per_256_seconds_ | enumOpt-V9_1_per_512_seconds_ | enumOpt-Vneg1_2_per_second_ | enumOpt-Vneg2_4_per_second_ | enumOpt-Vneg3_8_per_second_ | enumOpt-Vneg4_16_per_second_ | enumOpt-Vneg5_32_per_second_ | enumOpt-Vneg6_64_per_second_ | enumOpt-Vneg7_128_per_second_ | enumOpt-Vneg8_256_per_second_ | enumOpt-Vneg9_512_per_second_)): This parameter requires a announceInterval of type kEnumValue=enumOpt-DoNotChange,enumOpt-Initial,enumOpt-Stop,enumOpt-V0_1_per_second_,enumOpt-V1_1_per_2_seconds_,enumOpt-V2_1_per_4_seconds_,enumOpt-V3_1_per_8_seconds_,enumOpt-V4_1_per_16_seconds_,enumOpt-V5_1_per_32_seconds_,enumOpt-V6_1_per_64_seconds_,enumOpt-V7_1_per_128_seconds_,enumOpt-V8_1_per_256_seconds_,enumOpt-V9_1_per_512_seconds_,enumOpt-Vneg1_2_per_second_,enumOpt-Vneg2_4_per_second_,enumOpt-Vneg3_8_per_second_,enumOpt-Vneg4_16_per_second_,enumOpt-Vneg5_32_per_second_,enumOpt-Vneg6_64_per_second_,enumOpt-Vneg7_128_per_second_,enumOpt-Vneg8_256_per_second_,enumOpt-Vneg9_512_per_second_
        - ComputeNeighborRateRatio (bool): This parameter requires a computeNeighborRateRatio of type kBool
        - ComputeNeighborPropDelay (bool): This parameter requires a computeNeighborPropDelay of type kBool
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        gPtpSendSignaling(SessionIndices=string, LinkDelayInterval=enum, TimeSyncInterval=enum, AnnounceInterval=enum, ComputeNeighborRateRatio=bool, ComputeNeighborPropDelay=bool)list
        --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a linkDelayInterval of type kEnumValue=enumOpt-DoNotChange,enumOpt-Initial,enumOpt-Stop,enumOpt-V0_1_per_second_,enumOpt-V1_1_per_2_seconds_,enumOpt-V2_1_per_4_seconds_,enumOpt-V3_1_per_8_seconds_,enumOpt-V4_1_per_16_seconds_,enumOpt-V5_1_per_32_seconds_,enumOpt-V6_1_per_64_seconds_,enumOpt-V7_1_per_128_seconds_,enumOpt-V8_1_per_256_seconds_,enumOpt-V9_1_per_512_seconds_,enumOpt-Vneg1_2_per_second_,enumOpt-Vneg2_4_per_second_,enumOpt-Vneg3_8_per_second_,enumOpt-Vneg4_16_per_second_,enumOpt-Vneg5_32_per_second_,enumOpt-Vneg6_64_per_second_,enumOpt-Vneg7_128_per_second_,enumOpt-Vneg8_256_per_second_,enumOpt-Vneg9_512_per_second_
        - LinkDelayInterval (str(enumOpt-DoNotChange | enumOpt-Initial | enumOpt-Stop | enumOpt-V0_1_per_second_ | enumOpt-V1_1_per_2_seconds_ | enumOpt-V2_1_per_4_seconds_ | enumOpt-V3_1_per_8_seconds_ | enumOpt-V4_1_per_16_seconds_ | enumOpt-V5_1_per_32_seconds_ | enumOpt-V6_1_per_64_seconds_ | enumOpt-V7_1_per_128_seconds_ | enumOpt-V8_1_per_256_seconds_ | enumOpt-V9_1_per_512_seconds_ | enumOpt-Vneg1_2_per_second_ | enumOpt-Vneg2_4_per_second_ | enumOpt-Vneg3_8_per_second_ | enumOpt-Vneg4_16_per_second_ | enumOpt-Vneg5_32_per_second_ | enumOpt-Vneg6_64_per_second_ | enumOpt-Vneg7_128_per_second_ | enumOpt-Vneg8_256_per_second_ | enumOpt-Vneg9_512_per_second_)): This parameter requires a timeSyncInterval of type kEnumValue=enumOpt-DoNotChange,enumOpt-Initial,enumOpt-Stop,enumOpt-V0_1_per_second_,enumOpt-V1_1_per_2_seconds_,enumOpt-V2_1_per_4_seconds_,enumOpt-V3_1_per_8_seconds_,enumOpt-V4_1_per_16_seconds_,enumOpt-V5_1_per_32_seconds_,enumOpt-V6_1_per_64_seconds_,enumOpt-V7_1_per_128_seconds_,enumOpt-V8_1_per_256_seconds_,enumOpt-V9_1_per_512_seconds_,enumOpt-Vneg1_2_per_second_,enumOpt-Vneg2_4_per_second_,enumOpt-Vneg3_8_per_second_,enumOpt-Vneg4_16_per_second_,enumOpt-Vneg5_32_per_second_,enumOpt-Vneg6_64_per_second_,enumOpt-Vneg7_128_per_second_,enumOpt-Vneg8_256_per_second_,enumOpt-Vneg9_512_per_second_
        - TimeSyncInterval (str(enumOpt-DoNotChange | enumOpt-Initial | enumOpt-Stop | enumOpt-V0_1_per_second_ | enumOpt-V1_1_per_2_seconds_ | enumOpt-V2_1_per_4_seconds_ | enumOpt-V3_1_per_8_seconds_ | enumOpt-V4_1_per_16_seconds_ | enumOpt-V5_1_per_32_seconds_ | enumOpt-V6_1_per_64_seconds_ | enumOpt-V7_1_per_128_seconds_ | enumOpt-V8_1_per_256_seconds_ | enumOpt-V9_1_per_512_seconds_ | enumOpt-Vneg1_2_per_second_ | enumOpt-Vneg2_4_per_second_ | enumOpt-Vneg3_8_per_second_ | enumOpt-Vneg4_16_per_second_ | enumOpt-Vneg5_32_per_second_ | enumOpt-Vneg6_64_per_second_ | enumOpt-Vneg7_128_per_second_ | enumOpt-Vneg8_256_per_second_ | enumOpt-Vneg9_512_per_second_)): This parameter requires a announceInterval of type kEnumValue=enumOpt-DoNotChange,enumOpt-Initial,enumOpt-Stop,enumOpt-V0_1_per_second_,enumOpt-V1_1_per_2_seconds_,enumOpt-V2_1_per_4_seconds_,enumOpt-V3_1_per_8_seconds_,enumOpt-V4_1_per_16_seconds_,enumOpt-V5_1_per_32_seconds_,enumOpt-V6_1_per_64_seconds_,enumOpt-V7_1_per_128_seconds_,enumOpt-V8_1_per_256_seconds_,enumOpt-V9_1_per_512_seconds_,enumOpt-Vneg1_2_per_second_,enumOpt-Vneg2_4_per_second_,enumOpt-Vneg3_8_per_second_,enumOpt-Vneg4_16_per_second_,enumOpt-Vneg5_32_per_second_,enumOpt-Vneg6_64_per_second_,enumOpt-Vneg7_128_per_second_,enumOpt-Vneg8_256_per_second_,enumOpt-Vneg9_512_per_second_
        - AnnounceInterval (str(enumOpt-DoNotChange | enumOpt-Initial | enumOpt-Stop | enumOpt-V0_1_per_second_ | enumOpt-V1_1_per_2_seconds_ | enumOpt-V2_1_per_4_seconds_ | enumOpt-V3_1_per_8_seconds_ | enumOpt-V4_1_per_16_seconds_ | enumOpt-V5_1_per_32_seconds_ | enumOpt-V6_1_per_64_seconds_ | enumOpt-V7_1_per_128_seconds_ | enumOpt-V8_1_per_256_seconds_ | enumOpt-V9_1_per_512_seconds_ | enumOpt-Vneg1_2_per_second_ | enumOpt-Vneg2_4_per_second_ | enumOpt-Vneg3_8_per_second_ | enumOpt-Vneg4_16_per_second_ | enumOpt-Vneg5_32_per_second_ | enumOpt-Vneg6_64_per_second_ | enumOpt-Vneg7_128_per_second_ | enumOpt-Vneg8_256_per_second_ | enumOpt-Vneg9_512_per_second_)): This parameter requires a computeNeighborRateRatio of type kBool
        - ComputeNeighborRateRatio (bool): This parameter requires a computeNeighborPropDelay of type kBool
        - ComputeNeighborPropDelay (bool): This parameter requires a string of session numbers 1-4;6;7-12
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('gPtpSendSignaling', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        restartDown(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def SendgPtpRevSignaling(self, *args, **kwargs):
        """Executes the sendgPtpRevSignaling operation on the server.

        Send Signaling messages for the selected PTP IEEE 802.1AS Rev sessions.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendgPtpRevSignaling(Arg2=list, Arg3=enum, Arg4=enum, Arg5=enum, Arg6=enum, Arg7=enum, Arg8=bool, Arg9=bool, Arg10=bool)list
        ----------------------------------------------------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group for the corresponding deviceinstances whose PTP sessions are used as the source of the signaling messages.
        - Arg3 (str(message_Interval_Request_Tlv | gPTP_Capable_Message_Interval_Request_Tlv | both)): Desired Type Of Signaling Message Tlv
        - Arg4 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired linkDelayInterval
        - Arg5 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired timeSyncInterval
        - Arg6 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired announceInterval
        - Arg7 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired gPTP Capable Message Interval
        - Arg8 (bool): computeNeighborRateRatio flag
        - Arg9 (bool): computeNeighborPropDelay flag
        - Arg10 (bool): oneStepReceiveCapable flag
        - Returns list(str): ID to associate each async action invocation

        sendgPtpRevSignaling(Arg2=enum, Arg3=enum, Arg4=enum, Arg5=enum, Arg6=enum, Arg7=bool, Arg8=bool, Arg9=bool)list
        ----------------------------------------------------------------------------------------------------------------
        - Arg2 (str(message_Interval_Request_Tlv | gPTP_Capable_Message_Interval_Request_Tlv | both)): Desired Type Of Signaling Message Tlv
        - Arg3 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired linkDelayInterval
        - Arg4 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired timeSyncInterval
        - Arg5 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired announceInterval
        - Arg6 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired gPTP Capable Message Interval
        - Arg7 (bool): computeNeighborRateRatio flag
        - Arg8 (bool): computeNeighborPropDelay flag
        - Arg9 (bool): oneStepReceiveCapable flag
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendgPtpRevSignaling', payload=payload, response_object=None)

    def SendgPtpSignaling(self, *args, **kwargs):
        """Executes the sendgPtpSignaling operation on the server.

        Send Signaling messages for the selected PTP IEEE 802.1AS sessions.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendgPtpSignaling(Arg2=list, Arg3=enum, Arg4=enum, Arg5=enum, Arg6=bool, Arg7=bool)list
        ---------------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group for the corresponding device instances whose PTP sessions are used as the source of the signaling messages.
        - Arg3 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired linkDelayInterval
        - Arg4 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired timeSyncInterval
        - Arg5 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired announceInterval
        - Arg6 (bool): computeNeighborRateRatio flag
        - Arg7 (bool): computeNeighborPropDelay flag
        - Returns list(str): ID to associate each async action invocation

        sendgPtpSignaling(Arg2=enum, Arg3=enum, Arg4=enum, Arg5=bool, Arg6=bool)list
        ----------------------------------------------------------------------------
        - Arg2 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired linkDelayInterval
        - Arg3 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired timeSyncInterval
        - Arg4 (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired announceInterval
        - Arg5 (bool): computeNeighborRateRatio flag
        - Arg6 (bool): computeNeighborPropDelay flag
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendgPtpSignaling', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
