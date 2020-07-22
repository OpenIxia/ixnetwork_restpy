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


class PtpRangeOverMac(Base):
    """Manages a range of PTP clocks.
    The PtpRangeOverMac class encapsulates a list of ptpRangeOverMac resources that are managed by the user.
    A list of resources can be retrieved from the server using the PtpRangeOverMac.find() method.
    The list can be managed by using the PtpRangeOverMac.add() and PtpRangeOverMac.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ptpRangeOverMac'
    _SDM_ATT_MAP = {
        'AnnounceCurrentUtcOffsetValid': 'announceCurrentUtcOffsetValid',
        'AnnounceDropRate': 'announceDropRate',
        'AnnounceFrequencyTraceable': 'announceFrequencyTraceable',
        'AnnounceLeap59': 'announceLeap59',
        'AnnounceLeap61': 'announceLeap61',
        'AnnouncePtpTimescale': 'announcePtpTimescale',
        'AnnounceReceiptTimeout': 'announceReceiptTimeout',
        'AnnounceTimeTraceable': 'announceTimeTraceable',
        'ClientCount': 'clientCount',
        'ClientIpAddress': 'clientIpAddress',
        'ClientIpIncrementBy': 'clientIpIncrementBy',
        'ClientMacAddress': 'clientMacAddress',
        'ClientMacIncrementBy': 'clientMacIncrementBy',
        'ClockAccuracy': 'clockAccuracy',
        'ClockClass': 'clockClass',
        'ClockIncrement': 'clockIncrement',
        'CommunicationMode': 'communicationMode',
        'DelayMechanism': 'delayMechanism',
        'DelayRespDropRate': 'delayRespDropRate',
        'DelayRespReceiptTimeout': 'delayRespReceiptTimeout',
        'DelayResponseDelay': 'delayResponseDelay',
        'DelayResponseDelayInsertionRate': 'delayResponseDelayInsertionRate',
        'Domain': 'domain',
        'DropSignalReqAnnounce': 'dropSignalReqAnnounce',
        'DropSignalReqDelayResp': 'dropSignalReqDelayResp',
        'DropSignalReqSync': 'dropSignalReqSync',
        'Enabled': 'enabled',
        'FirstClock': 'firstClock',
        'FollowUpBadCrcRate': 'followUpBadCrcRate',
        'FollowUpDelay': 'followUpDelay',
        'FollowUpDelayInsertionRate': 'followUpDelayInsertionRate',
        'FollowUpDropRate': 'followUpDropRate',
        'GrantDelayRespDurationInterval': 'grantDelayRespDurationInterval',
        'GrantSyncDurationInterval': 'grantSyncDurationInterval',
        'GrantUnicastDurationInterval': 'grantUnicastDurationInterval',
        'IpTos': 'ipTos',
        'LearnPortId': 'learnPortId',
        'LogAnnounceInterval': 'logAnnounceInterval',
        'LogDelayReqInterval': 'logDelayReqInterval',
        'LogSyncInterval': 'logSyncInterval',
        'MasterCount': 'masterCount',
        'MasterIpAddress': 'masterIpAddress',
        'MasterIpIncrementBy': 'masterIpIncrementBy',
        'MasterIpIncrementInterEntity': 'masterIpIncrementInterEntity',
        'MasterMacAddress': 'masterMacAddress',
        'MasterMacIncrementBy': 'masterMacIncrementBy',
        'MasterMacIncrementInterEntity': 'masterMacIncrementInterEntity',
        'Name': 'name',
        'ObjectId': 'objectId',
        'PortNumber': 'portNumber',
        'PortNumberIncrement': 'portNumberIncrement',
        'Priority1': 'priority1',
        'Priority2': 'priority2',
        'RenewalInvited': 'renewalInvited',
        'RequestAttempts': 'requestAttempts',
        'RequestHolddown': 'requestHolddown',
        'RequestInterval': 'requestInterval',
        'ResidenceTime': 'residenceTime',
        'RxCalibration': 'rxCalibration',
        'SendAnnounceMulticast': 'sendAnnounceMulticast',
        'SendAnnounceTlv': 'sendAnnounceTlv',
        'SendCancelTlv': 'sendCancelTlv',
        'SignalInterval': 'signalInterval',
        'SignalUnicastHandling': 'signalUnicastHandling',
        'StepMode': 'stepMode',
        'StepsRemoved': 'stepsRemoved',
        'StrictGrant': 'strictGrant',
        'SyncDropRate': 'syncDropRate',
        'SyncReceiptTimeout': 'syncReceiptTimeout',
        'TimeSource': 'timeSource',
        'TimestampOffset': 'timestampOffset',
        'TimestampOffsetVariation': 'timestampOffsetVariation',
        'TxCalibration': 'txCalibration',
        'UseAlternateMasterFlag': 'useAlternateMasterFlag',
        'UseClockIdentity': 'useClockIdentity',
    }

    def __init__(self, parent):
        super(PtpRangeOverMac, self).__init__(parent)

    @property
    def AnnounceCurrentUtcOffsetValid(self):
        """
        Returns
        -------
        - bool: Set Announce currentUtcOffsetValid bit
        """
        return self._get_attribute(self._SDM_ATT_MAP['AnnounceCurrentUtcOffsetValid'])
    @AnnounceCurrentUtcOffsetValid.setter
    def AnnounceCurrentUtcOffsetValid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AnnounceCurrentUtcOffsetValid'], value)

    @property
    def AnnounceDropRate(self):
        """
        Returns
        -------
        - number: Percentage rate of the dropped Announce messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AnnounceDropRate'])
    @AnnounceDropRate.setter
    def AnnounceDropRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AnnounceDropRate'], value)

    @property
    def AnnounceFrequencyTraceable(self):
        """
        Returns
        -------
        - bool: Set Announce frequency traceable bit
        """
        return self._get_attribute(self._SDM_ATT_MAP['AnnounceFrequencyTraceable'])
    @AnnounceFrequencyTraceable.setter
    def AnnounceFrequencyTraceable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AnnounceFrequencyTraceable'], value)

    @property
    def AnnounceLeap59(self):
        """
        Returns
        -------
        - bool: Set Announce leap59 bit
        """
        return self._get_attribute(self._SDM_ATT_MAP['AnnounceLeap59'])
    @AnnounceLeap59.setter
    def AnnounceLeap59(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AnnounceLeap59'], value)

    @property
    def AnnounceLeap61(self):
        """
        Returns
        -------
        - bool: Set Announce leap61 bit
        """
        return self._get_attribute(self._SDM_ATT_MAP['AnnounceLeap61'])
    @AnnounceLeap61.setter
    def AnnounceLeap61(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AnnounceLeap61'], value)

    @property
    def AnnouncePtpTimescale(self):
        """
        Returns
        -------
        - bool: Set Announce ptpTimescale bit
        """
        return self._get_attribute(self._SDM_ATT_MAP['AnnouncePtpTimescale'])
    @AnnouncePtpTimescale.setter
    def AnnouncePtpTimescale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AnnouncePtpTimescale'], value)

    @property
    def AnnounceReceiptTimeout(self):
        """
        Returns
        -------
        - number: the number of announceInterval that has to pass without receipt of an Announce message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AnnounceReceiptTimeout'])
    @AnnounceReceiptTimeout.setter
    def AnnounceReceiptTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AnnounceReceiptTimeout'], value)

    @property
    def AnnounceTimeTraceable(self):
        """
        Returns
        -------
        - bool: Set Announce time traceable bit
        """
        return self._get_attribute(self._SDM_ATT_MAP['AnnounceTimeTraceable'])
    @AnnounceTimeTraceable.setter
    def AnnounceTimeTraceable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AnnounceTimeTraceable'], value)

    @property
    def ClientCount(self):
        """
        Returns
        -------
        - number: The total number of Unicast clients to be used for the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientCount'])
    @ClientCount.setter
    def ClientCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientCount'], value)

    @property
    def ClientIpAddress(self):
        """
        Returns
        -------
        - str: Defines the base address to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientIpAddress'])
    @ClientIpAddress.setter
    def ClientIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientIpAddress'], value)

    @property
    def ClientIpIncrementBy(self):
        """
        Returns
        -------
        - str: Defines the increment to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientIpIncrementBy'])
    @ClientIpIncrementBy.setter
    def ClientIpIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientIpIncrementBy'], value)

    @property
    def ClientMacAddress(self):
        """
        Returns
        -------
        - str: Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'clientMacIncrementBy' as an incrementor.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientMacAddress'])
    @ClientMacAddress.setter
    def ClientMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientMacAddress'], value)

    @property
    def ClientMacIncrementBy(self):
        """
        Returns
        -------
        - str: Defines the increment to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientMacIncrementBy'])
    @ClientMacIncrementBy.setter
    def ClientMacIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientMacIncrementBy'], value)

    @property
    def ClockAccuracy(self):
        """
        Returns
        -------
        - str: Clock accuracy.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClockAccuracy'])
    @ClockAccuracy.setter
    def ClockAccuracy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClockAccuracy'], value)

    @property
    def ClockClass(self):
        """
        Returns
        -------
        - number: Traceability of the time or frequency distributed by the grandmaster clock.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClockClass'])
    @ClockClass.setter
    def ClockClass(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClockClass'], value)

    @property
    def ClockIncrement(self):
        """
        Returns
        -------
        - str: Defines the ClockIdentity increment to be used in this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClockIncrement'])
    @ClockIncrement.setter
    def ClockIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClockIncrement'], value)

    @property
    def CommunicationMode(self):
        """
        Returns
        -------
        - str: Communication mode (unicast/multicast).
        """
        return self._get_attribute(self._SDM_ATT_MAP['CommunicationMode'])
    @CommunicationMode.setter
    def CommunicationMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CommunicationMode'], value)

    @property
    def DelayMechanism(self):
        """
        Returns
        -------
        - str: Clock delay mechanism.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayMechanism'])
    @DelayMechanism.setter
    def DelayMechanism(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayMechanism'], value)

    @property
    def DelayRespDropRate(self):
        """
        Returns
        -------
        - number: Percentage rate of the dropped Delay_Resp messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayRespDropRate'])
    @DelayRespDropRate.setter
    def DelayRespDropRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayRespDropRate'], value)

    @property
    def DelayRespReceiptTimeout(self):
        """
        Returns
        -------
        - number: DelayResponse Receipt Timeout in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayRespReceiptTimeout'])
    @DelayRespReceiptTimeout.setter
    def DelayRespReceiptTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayRespReceiptTimeout'], value)

    @property
    def DelayResponseDelay(self):
        """
        Returns
        -------
        - number: Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayResponseDelay'])
    @DelayResponseDelay.setter
    def DelayResponseDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayResponseDelay'], value)

    @property
    def DelayResponseDelayInsertionRate(self):
        """
        Returns
        -------
        - number: Percentage rate of the Delay_Resp messages in which the delay is introduced.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayResponseDelayInsertionRate'])
    @DelayResponseDelayInsertionRate.setter
    def DelayResponseDelayInsertionRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayResponseDelayInsertionRate'], value)

    @property
    def Domain(self):
        """
        Returns
        -------
        - number: PTP Domain
        """
        return self._get_attribute(self._SDM_ATT_MAP['Domain'])
    @Domain.setter
    def Domain(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Domain'], value)

    @property
    def DropSignalReqAnnounce(self):
        """
        Returns
        -------
        - bool: Select this check box to drop any Signal Request that contains Announce TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DropSignalReqAnnounce'])
    @DropSignalReqAnnounce.setter
    def DropSignalReqAnnounce(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DropSignalReqAnnounce'], value)

    @property
    def DropSignalReqDelayResp(self):
        """
        Returns
        -------
        - bool: Select this check box to drop any Signal Request that contains DelayResp TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DropSignalReqDelayResp'])
    @DropSignalReqDelayResp.setter
    def DropSignalReqDelayResp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DropSignalReqDelayResp'], value)

    @property
    def DropSignalReqSync(self):
        """
        Returns
        -------
        - bool: Select this check box to drop any Signal Request that contains Sync TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DropSignalReqSync'])
    @DropSignalReqSync.setter
    def DropSignalReqSync(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DropSignalReqSync'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def FirstClock(self):
        """
        Returns
        -------
        - str: Defines the first ClockIdentity to be used in this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstClock'])
    @FirstClock.setter
    def FirstClock(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstClock'], value)

    @property
    def FollowUpBadCrcRate(self):
        """
        Returns
        -------
        - number: Percentage rate of the bad crc Follow_Up messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FollowUpBadCrcRate'])
    @FollowUpBadCrcRate.setter
    def FollowUpBadCrcRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FollowUpBadCrcRate'], value)

    @property
    def FollowUpDelay(self):
        """
        Returns
        -------
        - number: Additional delay introduced in the Follow_Up message timestamp (nanoseconds)
        """
        return self._get_attribute(self._SDM_ATT_MAP['FollowUpDelay'])
    @FollowUpDelay.setter
    def FollowUpDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FollowUpDelay'], value)

    @property
    def FollowUpDelayInsertionRate(self):
        """
        Returns
        -------
        - number: Percentage rate of the Follow_Up messages in which the delay is introduced
        """
        return self._get_attribute(self._SDM_ATT_MAP['FollowUpDelayInsertionRate'])
    @FollowUpDelayInsertionRate.setter
    def FollowUpDelayInsertionRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FollowUpDelayInsertionRate'], value)

    @property
    def FollowUpDropRate(self):
        """
        Returns
        -------
        - number: Percentage rate of the dropped Follow_Up messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FollowUpDropRate'])
    @FollowUpDropRate.setter
    def FollowUpDropRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FollowUpDropRate'], value)

    @property
    def GrantDelayRespDurationInterval(self):
        """
        Returns
        -------
        - number: Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for DelayResp messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GrantDelayRespDurationInterval'])
    @GrantDelayRespDurationInterval.setter
    def GrantDelayRespDurationInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GrantDelayRespDurationInterval'], value)

    @property
    def GrantSyncDurationInterval(self):
        """
        Returns
        -------
        - number: Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for Sync messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GrantSyncDurationInterval'])
    @GrantSyncDurationInterval.setter
    def GrantSyncDurationInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GrantSyncDurationInterval'], value)

    @property
    def GrantUnicastDurationInterval(self):
        """
        Returns
        -------
        - number: Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GrantUnicastDurationInterval'])
    @GrantUnicastDurationInterval.setter
    def GrantUnicastDurationInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GrantUnicastDurationInterval'], value)

    @property
    def IpTos(self):
        """
        Returns
        -------
        - number: IP TOS or DS.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpTos'])
    @IpTos.setter
    def IpTos(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpTos'], value)

    @property
    def LearnPortId(self):
        """
        Returns
        -------
        - bool: Slave learns Master Port ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnPortId'])
    @LearnPortId.setter
    def LearnPortId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnPortId'], value)

    @property
    def LogAnnounceInterval(self):
        """
        Returns
        -------
        - number: The log mean time interval between successive Announce messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LogAnnounceInterval'])
    @LogAnnounceInterval.setter
    def LogAnnounceInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LogAnnounceInterval'], value)

    @property
    def LogDelayReqInterval(self):
        """
        Returns
        -------
        - number: The log mean time interval between successive Delay_Req messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LogDelayReqInterval'])
    @LogDelayReqInterval.setter
    def LogDelayReqInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LogDelayReqInterval'], value)

    @property
    def LogSyncInterval(self):
        """
        Returns
        -------
        - number: The log mean time interval between successive Sync messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LogSyncInterval'])
    @LogSyncInterval.setter
    def LogSyncInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LogSyncInterval'], value)

    @property
    def MasterCount(self):
        """
        Returns
        -------
        - number: The total number of Unicast masters to be used for the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterCount'])
    @MasterCount.setter
    def MasterCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MasterCount'], value)

    @property
    def MasterIpAddress(self):
        """
        Returns
        -------
        - str: Defines the base address to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterIpAddress'])
    @MasterIpAddress.setter
    def MasterIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MasterIpAddress'], value)

    @property
    def MasterIpIncrementBy(self):
        """
        Returns
        -------
        - str: Defines the increment to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterIpIncrementBy'])
    @MasterIpIncrementBy.setter
    def MasterIpIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MasterIpIncrementBy'], value)

    @property
    def MasterIpIncrementInterEntity(self):
        """
        Returns
        -------
        - str: Defines the increment to be used for the start address of Master
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterIpIncrementInterEntity'])
    @MasterIpIncrementInterEntity.setter
    def MasterIpIncrementInterEntity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MasterIpIncrementInterEntity'], value)

    @property
    def MasterMacAddress(self):
        """
        Returns
        -------
        - str: Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'masterMacIncrementBy' as an incrementor.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterMacAddress'])
    @MasterMacAddress.setter
    def MasterMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MasterMacAddress'], value)

    @property
    def MasterMacIncrementBy(self):
        """
        Returns
        -------
        - str: Defines the increment to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterMacIncrementBy'])
    @MasterMacIncrementBy.setter
    def MasterMacIncrementBy(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MasterMacIncrementBy'], value)

    @property
    def MasterMacIncrementInterEntity(self):
        """
        Returns
        -------
        - str: Defines the increment to be used for the start address of Master
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterMacIncrementInterEntity'])
    @MasterMacIncrementInterEntity.setter
    def MasterMacIncrementInterEntity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MasterMacIncrementInterEntity'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def PortNumber(self):
        """
        Returns
        -------
        - number: Port number
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortNumber'])
    @PortNumber.setter
    def PortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortNumber'], value)

    @property
    def PortNumberIncrement(self):
        """
        Returns
        -------
        - number: Port number increment
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortNumberIncrement'])
    @PortNumberIncrement.setter
    def PortNumberIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortNumberIncrement'], value)

    @property
    def Priority1(self):
        """
        Returns
        -------
        - number: PTP priority1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority1'])
    @Priority1.setter
    def Priority1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Priority1'], value)

    @property
    def Priority2(self):
        """
        Returns
        -------
        - number: PTP priority2.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority2'])
    @Priority2.setter
    def Priority2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Priority2'], value)

    @property
    def RenewalInvited(self):
        """
        Returns
        -------
        - bool: Set the Renewal Invited flag in Grant Unicast Transmission TLV
        """
        return self._get_attribute(self._SDM_ATT_MAP['RenewalInvited'])
    @RenewalInvited.setter
    def RenewalInvited(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RenewalInvited'], value)

    @property
    def RequestAttempts(self):
        """
        Returns
        -------
        - number: How many succesive requests a client can request before entering into holddown.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RequestAttempts'])
    @RequestAttempts.setter
    def RequestAttempts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RequestAttempts'], value)

    @property
    def RequestHolddown(self):
        """
        Returns
        -------
        - number: Time between succesive requests if denied/timeout for Signal Request.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RequestHolddown'])
    @RequestHolddown.setter
    def RequestHolddown(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RequestHolddown'], value)

    @property
    def RequestInterval(self):
        """
        Returns
        -------
        - number: Time between succesive requests if denied/timeout for Signal Request.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RequestInterval'])
    @RequestInterval.setter
    def RequestInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RequestInterval'], value)

    @property
    def ResidenceTime(self):
        """
        Returns
        -------
        - number: Master to slave residence time of the associated transparent clock
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResidenceTime'])
    @ResidenceTime.setter
    def ResidenceTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ResidenceTime'], value)

    @property
    def RxCalibration(self):
        """
        Returns
        -------
        - number: The amount of time (in ns) that the Receive side timestamp needs to be offset to allow for error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RxCalibration'])
    @RxCalibration.setter
    def RxCalibration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RxCalibration'], value)

    @property
    def SendAnnounceMulticast(self):
        """
        Returns
        -------
        - bool: Send multicast Announce messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendAnnounceMulticast'])
    @SendAnnounceMulticast.setter
    def SendAnnounceMulticast(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendAnnounceMulticast'], value)

    @property
    def SendAnnounceTlv(self):
        """
        Returns
        -------
        - bool: Send and respond to Announce TLV unicast requests in signal messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendAnnounceTlv'])
    @SendAnnounceTlv.setter
    def SendAnnounceTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendAnnounceTlv'], value)

    @property
    def SendCancelTlv(self):
        """
        Returns
        -------
        - bool: Send and respond to Cancel TLV unicast requests in signal messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendCancelTlv'])
    @SendCancelTlv.setter
    def SendCancelTlv(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendCancelTlv'], value)

    @property
    def SignalInterval(self):
        """
        Returns
        -------
        - number: Time between Signal Request messages, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SignalInterval'])
    @SignalInterval.setter
    def SignalInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SignalInterval'], value)

    @property
    def SignalUnicastHandling(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SignalUnicastHandling'])
    @SignalUnicastHandling.setter
    def SignalUnicastHandling(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SignalUnicastHandling'], value)

    @property
    def StepMode(self):
        """
        Returns
        -------
        - str: Clock step mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepMode'])
    @StepMode.setter
    def StepMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepMode'], value)

    @property
    def StepsRemoved(self):
        """
        Returns
        -------
        - number: The number of hops between the Grandmaster Clock and the emulated clock. Valid values: 0 to 65,535.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepsRemoved'])
    @StepsRemoved.setter
    def StepsRemoved(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepsRemoved'], value)

    @property
    def StrictGrant(self):
        """
        Returns
        -------
        - bool: If selected, server will not grant values that are above maximum offered values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StrictGrant'])
    @StrictGrant.setter
    def StrictGrant(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StrictGrant'], value)

    @property
    def SyncDropRate(self):
        """
        Returns
        -------
        - number: Percentage rate of the dropped Sync messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SyncDropRate'])
    @SyncDropRate.setter
    def SyncDropRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SyncDropRate'], value)

    @property
    def SyncReceiptTimeout(self):
        """
        Returns
        -------
        - number: Sync Receipt Timeout in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SyncReceiptTimeout'])
    @SyncReceiptTimeout.setter
    def SyncReceiptTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SyncReceiptTimeout'], value)

    @property
    def TimeSource(self):
        """
        Returns
        -------
        - str: Time source for the PTP device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeSource'])
    @TimeSource.setter
    def TimeSource(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimeSource'], value)

    @property
    def TimestampOffset(self):
        """
        Returns
        -------
        - number: Timestamp offset.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimestampOffset'])
    @TimestampOffset.setter
    def TimestampOffset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimestampOffset'], value)

    @property
    def TimestampOffsetVariation(self):
        """
        Returns
        -------
        - number: Timestamp offset variation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimestampOffsetVariation'])
    @TimestampOffsetVariation.setter
    def TimestampOffsetVariation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimestampOffsetVariation'], value)

    @property
    def TxCalibration(self):
        """
        Returns
        -------
        - number: The amount of time (in ns) that the Transmit side timestamp needs to be offset to allow for error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxCalibration'])
    @TxCalibration.setter
    def TxCalibration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxCalibration'], value)

    @property
    def UseAlternateMasterFlag(self):
        """
        Returns
        -------
        - bool: Select this check box to set the Alternate Master flag in all Announce and Sync messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseAlternateMasterFlag'])
    @UseAlternateMasterFlag.setter
    def UseAlternateMasterFlag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseAlternateMasterFlag'], value)

    @property
    def UseClockIdentity(self):
        """
        Returns
        -------
        - bool: Use the ClockIdentity configured below.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseClockIdentity'])
    @UseClockIdentity.setter
    def UseClockIdentity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseClockIdentity'], value)

    def update(self, AnnounceCurrentUtcOffsetValid=None, AnnounceDropRate=None, AnnounceFrequencyTraceable=None, AnnounceLeap59=None, AnnounceLeap61=None, AnnouncePtpTimescale=None, AnnounceReceiptTimeout=None, AnnounceTimeTraceable=None, ClientCount=None, ClientIpAddress=None, ClientIpIncrementBy=None, ClientMacAddress=None, ClientMacIncrementBy=None, ClockAccuracy=None, ClockClass=None, ClockIncrement=None, CommunicationMode=None, DelayMechanism=None, DelayRespDropRate=None, DelayRespReceiptTimeout=None, DelayResponseDelay=None, DelayResponseDelayInsertionRate=None, Domain=None, DropSignalReqAnnounce=None, DropSignalReqDelayResp=None, DropSignalReqSync=None, Enabled=None, FirstClock=None, FollowUpBadCrcRate=None, FollowUpDelay=None, FollowUpDelayInsertionRate=None, FollowUpDropRate=None, GrantDelayRespDurationInterval=None, GrantSyncDurationInterval=None, GrantUnicastDurationInterval=None, IpTos=None, LearnPortId=None, LogAnnounceInterval=None, LogDelayReqInterval=None, LogSyncInterval=None, MasterCount=None, MasterIpAddress=None, MasterIpIncrementBy=None, MasterIpIncrementInterEntity=None, MasterMacAddress=None, MasterMacIncrementBy=None, MasterMacIncrementInterEntity=None, Name=None, PortNumber=None, PortNumberIncrement=None, Priority1=None, Priority2=None, RenewalInvited=None, RequestAttempts=None, RequestHolddown=None, RequestInterval=None, ResidenceTime=None, RxCalibration=None, SendAnnounceMulticast=None, SendAnnounceTlv=None, SendCancelTlv=None, SignalInterval=None, SignalUnicastHandling=None, StepMode=None, StepsRemoved=None, StrictGrant=None, SyncDropRate=None, SyncReceiptTimeout=None, TimeSource=None, TimestampOffset=None, TimestampOffsetVariation=None, TxCalibration=None, UseAlternateMasterFlag=None, UseClockIdentity=None):
        """Updates ptpRangeOverMac resource on the server.

        Args
        ----
        - AnnounceCurrentUtcOffsetValid (bool): Set Announce currentUtcOffsetValid bit
        - AnnounceDropRate (number): Percentage rate of the dropped Announce messages.
        - AnnounceFrequencyTraceable (bool): Set Announce frequency traceable bit
        - AnnounceLeap59 (bool): Set Announce leap59 bit
        - AnnounceLeap61 (bool): Set Announce leap61 bit
        - AnnouncePtpTimescale (bool): Set Announce ptpTimescale bit
        - AnnounceReceiptTimeout (number): the number of announceInterval that has to pass without receipt of an Announce message.
        - AnnounceTimeTraceable (bool): Set Announce time traceable bit
        - ClientCount (number): The total number of Unicast clients to be used for the range.
        - ClientIpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
        - ClientIpIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - ClientMacAddress (str): Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'clientMacIncrementBy' as an incrementor.
        - ClientMacIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - ClockAccuracy (str): Clock accuracy.
        - ClockClass (number): Traceability of the time or frequency distributed by the grandmaster clock.
        - ClockIncrement (str): Defines the ClockIdentity increment to be used in this range.
        - CommunicationMode (str): Communication mode (unicast/multicast).
        - DelayMechanism (str): Clock delay mechanism.
        - DelayRespDropRate (number): Percentage rate of the dropped Delay_Resp messages.
        - DelayRespReceiptTimeout (number): DelayResponse Receipt Timeout in seconds.
        - DelayResponseDelay (number): Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
        - DelayResponseDelayInsertionRate (number): Percentage rate of the Delay_Resp messages in which the delay is introduced.
        - Domain (number): PTP Domain
        - DropSignalReqAnnounce (bool): Select this check box to drop any Signal Request that contains Announce TLV.
        - DropSignalReqDelayResp (bool): Select this check box to drop any Signal Request that contains DelayResp TLV.
        - DropSignalReqSync (bool): Select this check box to drop any Signal Request that contains Sync TLV.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FirstClock (str): Defines the first ClockIdentity to be used in this range.
        - FollowUpBadCrcRate (number): Percentage rate of the bad crc Follow_Up messages.
        - FollowUpDelay (number): Additional delay introduced in the Follow_Up message timestamp (nanoseconds)
        - FollowUpDelayInsertionRate (number): Percentage rate of the Follow_Up messages in which the delay is introduced
        - FollowUpDropRate (number): Percentage rate of the dropped Follow_Up messages.
        - GrantDelayRespDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for DelayResp messages.
        - GrantSyncDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for Sync messages.
        - GrantUnicastDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV.
        - IpTos (number): IP TOS or DS.
        - LearnPortId (bool): Slave learns Master Port ID
        - LogAnnounceInterval (number): The log mean time interval between successive Announce messages.
        - LogDelayReqInterval (number): The log mean time interval between successive Delay_Req messages.
        - LogSyncInterval (number): The log mean time interval between successive Sync messages.
        - MasterCount (number): The total number of Unicast masters to be used for the range.
        - MasterIpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
        - MasterIpIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - MasterIpIncrementInterEntity (str): Defines the increment to be used for the start address of Master
        - MasterMacAddress (str): Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'masterMacIncrementBy' as an incrementor.
        - MasterMacIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - MasterMacIncrementInterEntity (str): Defines the increment to be used for the start address of Master
        - Name (str): Name of range
        - PortNumber (number): Port number
        - PortNumberIncrement (number): Port number increment
        - Priority1 (number): PTP priority1.
        - Priority2 (number): PTP priority2.
        - RenewalInvited (bool): Set the Renewal Invited flag in Grant Unicast Transmission TLV
        - RequestAttempts (number): How many succesive requests a client can request before entering into holddown.
        - RequestHolddown (number): Time between succesive requests if denied/timeout for Signal Request.
        - RequestInterval (number): Time between succesive requests if denied/timeout for Signal Request.
        - ResidenceTime (number): Master to slave residence time of the associated transparent clock
        - RxCalibration (number): The amount of time (in ns) that the Receive side timestamp needs to be offset to allow for error.
        - SendAnnounceMulticast (bool): Send multicast Announce messages.
        - SendAnnounceTlv (bool): Send and respond to Announce TLV unicast requests in signal messages.
        - SendCancelTlv (bool): Send and respond to Cancel TLV unicast requests in signal messages.
        - SignalInterval (number): Time between Signal Request messages, in seconds.
        - SignalUnicastHandling (str): 
        - StepMode (str): Clock step mode.
        - StepsRemoved (number): The number of hops between the Grandmaster Clock and the emulated clock. Valid values: 0 to 65,535.
        - StrictGrant (bool): If selected, server will not grant values that are above maximum offered values.
        - SyncDropRate (number): Percentage rate of the dropped Sync messages.
        - SyncReceiptTimeout (number): Sync Receipt Timeout in seconds.
        - TimeSource (str): Time source for the PTP device.
        - TimestampOffset (number): Timestamp offset.
        - TimestampOffsetVariation (number): Timestamp offset variation.
        - TxCalibration (number): The amount of time (in ns) that the Transmit side timestamp needs to be offset to allow for error.
        - UseAlternateMasterFlag (bool): Select this check box to set the Alternate Master flag in all Announce and Sync messages.
        - UseClockIdentity (bool): Use the ClockIdentity configured below.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AnnounceCurrentUtcOffsetValid=None, AnnounceDropRate=None, AnnounceFrequencyTraceable=None, AnnounceLeap59=None, AnnounceLeap61=None, AnnouncePtpTimescale=None, AnnounceReceiptTimeout=None, AnnounceTimeTraceable=None, ClientCount=None, ClientIpAddress=None, ClientIpIncrementBy=None, ClientMacAddress=None, ClientMacIncrementBy=None, ClockAccuracy=None, ClockClass=None, ClockIncrement=None, CommunicationMode=None, DelayMechanism=None, DelayRespDropRate=None, DelayRespReceiptTimeout=None, DelayResponseDelay=None, DelayResponseDelayInsertionRate=None, Domain=None, DropSignalReqAnnounce=None, DropSignalReqDelayResp=None, DropSignalReqSync=None, Enabled=None, FirstClock=None, FollowUpBadCrcRate=None, FollowUpDelay=None, FollowUpDelayInsertionRate=None, FollowUpDropRate=None, GrantDelayRespDurationInterval=None, GrantSyncDurationInterval=None, GrantUnicastDurationInterval=None, IpTos=None, LearnPortId=None, LogAnnounceInterval=None, LogDelayReqInterval=None, LogSyncInterval=None, MasterCount=None, MasterIpAddress=None, MasterIpIncrementBy=None, MasterIpIncrementInterEntity=None, MasterMacAddress=None, MasterMacIncrementBy=None, MasterMacIncrementInterEntity=None, Name=None, PortNumber=None, PortNumberIncrement=None, Priority1=None, Priority2=None, RenewalInvited=None, RequestAttempts=None, RequestHolddown=None, RequestInterval=None, ResidenceTime=None, RxCalibration=None, SendAnnounceMulticast=None, SendAnnounceTlv=None, SendCancelTlv=None, SignalInterval=None, SignalUnicastHandling=None, StepMode=None, StepsRemoved=None, StrictGrant=None, SyncDropRate=None, SyncReceiptTimeout=None, TimeSource=None, TimestampOffset=None, TimestampOffsetVariation=None, TxCalibration=None, UseAlternateMasterFlag=None, UseClockIdentity=None):
        """Adds a new ptpRangeOverMac resource on the server and adds it to the container.

        Args
        ----
        - AnnounceCurrentUtcOffsetValid (bool): Set Announce currentUtcOffsetValid bit
        - AnnounceDropRate (number): Percentage rate of the dropped Announce messages.
        - AnnounceFrequencyTraceable (bool): Set Announce frequency traceable bit
        - AnnounceLeap59 (bool): Set Announce leap59 bit
        - AnnounceLeap61 (bool): Set Announce leap61 bit
        - AnnouncePtpTimescale (bool): Set Announce ptpTimescale bit
        - AnnounceReceiptTimeout (number): the number of announceInterval that has to pass without receipt of an Announce message.
        - AnnounceTimeTraceable (bool): Set Announce time traceable bit
        - ClientCount (number): The total number of Unicast clients to be used for the range.
        - ClientIpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
        - ClientIpIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - ClientMacAddress (str): Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'clientMacIncrementBy' as an incrementor.
        - ClientMacIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - ClockAccuracy (str): Clock accuracy.
        - ClockClass (number): Traceability of the time or frequency distributed by the grandmaster clock.
        - ClockIncrement (str): Defines the ClockIdentity increment to be used in this range.
        - CommunicationMode (str): Communication mode (unicast/multicast).
        - DelayMechanism (str): Clock delay mechanism.
        - DelayRespDropRate (number): Percentage rate of the dropped Delay_Resp messages.
        - DelayRespReceiptTimeout (number): DelayResponse Receipt Timeout in seconds.
        - DelayResponseDelay (number): Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
        - DelayResponseDelayInsertionRate (number): Percentage rate of the Delay_Resp messages in which the delay is introduced.
        - Domain (number): PTP Domain
        - DropSignalReqAnnounce (bool): Select this check box to drop any Signal Request that contains Announce TLV.
        - DropSignalReqDelayResp (bool): Select this check box to drop any Signal Request that contains DelayResp TLV.
        - DropSignalReqSync (bool): Select this check box to drop any Signal Request that contains Sync TLV.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FirstClock (str): Defines the first ClockIdentity to be used in this range.
        - FollowUpBadCrcRate (number): Percentage rate of the bad crc Follow_Up messages.
        - FollowUpDelay (number): Additional delay introduced in the Follow_Up message timestamp (nanoseconds)
        - FollowUpDelayInsertionRate (number): Percentage rate of the Follow_Up messages in which the delay is introduced
        - FollowUpDropRate (number): Percentage rate of the dropped Follow_Up messages.
        - GrantDelayRespDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for DelayResp messages.
        - GrantSyncDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for Sync messages.
        - GrantUnicastDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV.
        - IpTos (number): IP TOS or DS.
        - LearnPortId (bool): Slave learns Master Port ID
        - LogAnnounceInterval (number): The log mean time interval between successive Announce messages.
        - LogDelayReqInterval (number): The log mean time interval between successive Delay_Req messages.
        - LogSyncInterval (number): The log mean time interval between successive Sync messages.
        - MasterCount (number): The total number of Unicast masters to be used for the range.
        - MasterIpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
        - MasterIpIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - MasterIpIncrementInterEntity (str): Defines the increment to be used for the start address of Master
        - MasterMacAddress (str): Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'masterMacIncrementBy' as an incrementor.
        - MasterMacIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - MasterMacIncrementInterEntity (str): Defines the increment to be used for the start address of Master
        - Name (str): Name of range
        - PortNumber (number): Port number
        - PortNumberIncrement (number): Port number increment
        - Priority1 (number): PTP priority1.
        - Priority2 (number): PTP priority2.
        - RenewalInvited (bool): Set the Renewal Invited flag in Grant Unicast Transmission TLV
        - RequestAttempts (number): How many succesive requests a client can request before entering into holddown.
        - RequestHolddown (number): Time between succesive requests if denied/timeout for Signal Request.
        - RequestInterval (number): Time between succesive requests if denied/timeout for Signal Request.
        - ResidenceTime (number): Master to slave residence time of the associated transparent clock
        - RxCalibration (number): The amount of time (in ns) that the Receive side timestamp needs to be offset to allow for error.
        - SendAnnounceMulticast (bool): Send multicast Announce messages.
        - SendAnnounceTlv (bool): Send and respond to Announce TLV unicast requests in signal messages.
        - SendCancelTlv (bool): Send and respond to Cancel TLV unicast requests in signal messages.
        - SignalInterval (number): Time between Signal Request messages, in seconds.
        - SignalUnicastHandling (str): 
        - StepMode (str): Clock step mode.
        - StepsRemoved (number): The number of hops between the Grandmaster Clock and the emulated clock. Valid values: 0 to 65,535.
        - StrictGrant (bool): If selected, server will not grant values that are above maximum offered values.
        - SyncDropRate (number): Percentage rate of the dropped Sync messages.
        - SyncReceiptTimeout (number): Sync Receipt Timeout in seconds.
        - TimeSource (str): Time source for the PTP device.
        - TimestampOffset (number): Timestamp offset.
        - TimestampOffsetVariation (number): Timestamp offset variation.
        - TxCalibration (number): The amount of time (in ns) that the Transmit side timestamp needs to be offset to allow for error.
        - UseAlternateMasterFlag (bool): Select this check box to set the Alternate Master flag in all Announce and Sync messages.
        - UseClockIdentity (bool): Use the ClockIdentity configured below.

        Returns
        -------
        - self: This instance with all currently retrieved ptpRangeOverMac resources using find and the newly added ptpRangeOverMac resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ptpRangeOverMac resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AnnounceCurrentUtcOffsetValid=None, AnnounceDropRate=None, AnnounceFrequencyTraceable=None, AnnounceLeap59=None, AnnounceLeap61=None, AnnouncePtpTimescale=None, AnnounceReceiptTimeout=None, AnnounceTimeTraceable=None, ClientCount=None, ClientIpAddress=None, ClientIpIncrementBy=None, ClientMacAddress=None, ClientMacIncrementBy=None, ClockAccuracy=None, ClockClass=None, ClockIncrement=None, CommunicationMode=None, DelayMechanism=None, DelayRespDropRate=None, DelayRespReceiptTimeout=None, DelayResponseDelay=None, DelayResponseDelayInsertionRate=None, Domain=None, DropSignalReqAnnounce=None, DropSignalReqDelayResp=None, DropSignalReqSync=None, Enabled=None, FirstClock=None, FollowUpBadCrcRate=None, FollowUpDelay=None, FollowUpDelayInsertionRate=None, FollowUpDropRate=None, GrantDelayRespDurationInterval=None, GrantSyncDurationInterval=None, GrantUnicastDurationInterval=None, IpTos=None, LearnPortId=None, LogAnnounceInterval=None, LogDelayReqInterval=None, LogSyncInterval=None, MasterCount=None, MasterIpAddress=None, MasterIpIncrementBy=None, MasterIpIncrementInterEntity=None, MasterMacAddress=None, MasterMacIncrementBy=None, MasterMacIncrementInterEntity=None, Name=None, ObjectId=None, PortNumber=None, PortNumberIncrement=None, Priority1=None, Priority2=None, RenewalInvited=None, RequestAttempts=None, RequestHolddown=None, RequestInterval=None, ResidenceTime=None, RxCalibration=None, SendAnnounceMulticast=None, SendAnnounceTlv=None, SendCancelTlv=None, SignalInterval=None, SignalUnicastHandling=None, StepMode=None, StepsRemoved=None, StrictGrant=None, SyncDropRate=None, SyncReceiptTimeout=None, TimeSource=None, TimestampOffset=None, TimestampOffsetVariation=None, TxCalibration=None, UseAlternateMasterFlag=None, UseClockIdentity=None):
        """Finds and retrieves ptpRangeOverMac resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ptpRangeOverMac resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ptpRangeOverMac resources from the server.

        Args
        ----
        - AnnounceCurrentUtcOffsetValid (bool): Set Announce currentUtcOffsetValid bit
        - AnnounceDropRate (number): Percentage rate of the dropped Announce messages.
        - AnnounceFrequencyTraceable (bool): Set Announce frequency traceable bit
        - AnnounceLeap59 (bool): Set Announce leap59 bit
        - AnnounceLeap61 (bool): Set Announce leap61 bit
        - AnnouncePtpTimescale (bool): Set Announce ptpTimescale bit
        - AnnounceReceiptTimeout (number): the number of announceInterval that has to pass without receipt of an Announce message.
        - AnnounceTimeTraceable (bool): Set Announce time traceable bit
        - ClientCount (number): The total number of Unicast clients to be used for the range.
        - ClientIpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
        - ClientIpIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - ClientMacAddress (str): Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'clientMacIncrementBy' as an incrementor.
        - ClientMacIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - ClockAccuracy (str): Clock accuracy.
        - ClockClass (number): Traceability of the time or frequency distributed by the grandmaster clock.
        - ClockIncrement (str): Defines the ClockIdentity increment to be used in this range.
        - CommunicationMode (str): Communication mode (unicast/multicast).
        - DelayMechanism (str): Clock delay mechanism.
        - DelayRespDropRate (number): Percentage rate of the dropped Delay_Resp messages.
        - DelayRespReceiptTimeout (number): DelayResponse Receipt Timeout in seconds.
        - DelayResponseDelay (number): Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
        - DelayResponseDelayInsertionRate (number): Percentage rate of the Delay_Resp messages in which the delay is introduced.
        - Domain (number): PTP Domain
        - DropSignalReqAnnounce (bool): Select this check box to drop any Signal Request that contains Announce TLV.
        - DropSignalReqDelayResp (bool): Select this check box to drop any Signal Request that contains DelayResp TLV.
        - DropSignalReqSync (bool): Select this check box to drop any Signal Request that contains Sync TLV.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FirstClock (str): Defines the first ClockIdentity to be used in this range.
        - FollowUpBadCrcRate (number): Percentage rate of the bad crc Follow_Up messages.
        - FollowUpDelay (number): Additional delay introduced in the Follow_Up message timestamp (nanoseconds)
        - FollowUpDelayInsertionRate (number): Percentage rate of the Follow_Up messages in which the delay is introduced
        - FollowUpDropRate (number): Percentage rate of the dropped Follow_Up messages.
        - GrantDelayRespDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for DelayResp messages.
        - GrantSyncDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for Sync messages.
        - GrantUnicastDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV.
        - IpTos (number): IP TOS or DS.
        - LearnPortId (bool): Slave learns Master Port ID
        - LogAnnounceInterval (number): The log mean time interval between successive Announce messages.
        - LogDelayReqInterval (number): The log mean time interval between successive Delay_Req messages.
        - LogSyncInterval (number): The log mean time interval between successive Sync messages.
        - MasterCount (number): The total number of Unicast masters to be used for the range.
        - MasterIpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
        - MasterIpIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - MasterIpIncrementInterEntity (str): Defines the increment to be used for the start address of Master
        - MasterMacAddress (str): Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'masterMacIncrementBy' as an incrementor.
        - MasterMacIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
        - MasterMacIncrementInterEntity (str): Defines the increment to be used for the start address of Master
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - PortNumber (number): Port number
        - PortNumberIncrement (number): Port number increment
        - Priority1 (number): PTP priority1.
        - Priority2 (number): PTP priority2.
        - RenewalInvited (bool): Set the Renewal Invited flag in Grant Unicast Transmission TLV
        - RequestAttempts (number): How many succesive requests a client can request before entering into holddown.
        - RequestHolddown (number): Time between succesive requests if denied/timeout for Signal Request.
        - RequestInterval (number): Time between succesive requests if denied/timeout for Signal Request.
        - ResidenceTime (number): Master to slave residence time of the associated transparent clock
        - RxCalibration (number): The amount of time (in ns) that the Receive side timestamp needs to be offset to allow for error.
        - SendAnnounceMulticast (bool): Send multicast Announce messages.
        - SendAnnounceTlv (bool): Send and respond to Announce TLV unicast requests in signal messages.
        - SendCancelTlv (bool): Send and respond to Cancel TLV unicast requests in signal messages.
        - SignalInterval (number): Time between Signal Request messages, in seconds.
        - SignalUnicastHandling (str): 
        - StepMode (str): Clock step mode.
        - StepsRemoved (number): The number of hops between the Grandmaster Clock and the emulated clock. Valid values: 0 to 65,535.
        - StrictGrant (bool): If selected, server will not grant values that are above maximum offered values.
        - SyncDropRate (number): Percentage rate of the dropped Sync messages.
        - SyncReceiptTimeout (number): Sync Receipt Timeout in seconds.
        - TimeSource (str): Time source for the PTP device.
        - TimestampOffset (number): Timestamp offset.
        - TimestampOffsetVariation (number): Timestamp offset variation.
        - TxCalibration (number): The amount of time (in ns) that the Transmit side timestamp needs to be offset to allow for error.
        - UseAlternateMasterFlag (bool): Select this check box to set the Alternate Master flag in all Announce and Sync messages.
        - UseClockIdentity (bool): Use the ClockIdentity configured below.

        Returns
        -------
        - self: This instance with matching ptpRangeOverMac resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ptpRangeOverMac data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ptpRangeOverMac resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self):
        """Executes the apply operation on the server.

        Apply changes for on the fly configuration support.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('apply', payload=payload, response_object=None)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)

    def PtpChangeDropSignalParams(self, *args, **kwargs):
        """Executes the ptpChangeDropSignalParams operation on the server.

        Change Drop Signal Parameters

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ptpChangeDropSignalParams(Arg2=bool, Arg3=bool, Arg4=bool)
        ----------------------------------------------------------
        - Arg2 (bool): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - Arg3 (bool): Drop any Signal Request received on a master side that contains one Announce TLV.
        - Arg4 (bool): Drop any Signal Request received on a master side that contains one Sync TLV.

        ptpChangeDropSignalParams(Arg2=bool, Arg3=bool, Arg4=bool, Arg5=enum)
        ---------------------------------------------------------------------
        - Arg2 (bool): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - Arg3 (bool): Drop any Signal Request received on a master side that contains one Announce TLV.
        - Arg4 (bool): Drop any Signal Request received on a master side that contains one Sync TLV.
        - Arg5 (str(async | sync)): Drop any Signal Request received on a master side that contains one DelayResp TLV.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpChangeDropSignalParams', payload=payload, response_object=None)

    def PtpChangeMiscParams(self, *args, **kwargs):
        """Executes the ptpChangeMiscParams operation on the server.

        Change Misc Parameters

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ptpChangeMiscParams(Arg2=number, Arg3=number)
        ---------------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - Arg3 (number): PTP Domain.

        ptpChangeMiscParams(Arg2=number, Arg3=number, Arg4=enum)
        --------------------------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - Arg3 (number): PTP Domain.
        - Arg4 (str(async | sync)): The number of announceInterval that has to pass without receipt of an Announce message.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpChangeMiscParams', payload=payload, response_object=None)

    def PtpChangeNegativeTesting(self, *args, **kwargs):
        """Executes the ptpChangeNegativeTesting operation on the server.

        Change Negative Testing Parameters

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ptpChangeNegativeTesting(Arg2=number, Arg3=number, Arg4=number, Arg5=number, Arg6=number, Arg7=number, Arg8=number, Arg9=number, Arg10=number)
        ----------------------------------------------------------------------------------------------------------------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - Arg3 (number): Additional delay introduced in the Follow_Up message timestamp (nanoseconds).
        - Arg4 (number): Percentage rate of the Follow_Up messages in which the delay is introduced.
        - Arg5 (number): Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
        - Arg6 (number): Percentage rate of the Delay_Resp messages in which the delay is introduced.
        - Arg7 (number): Percentage rate of the dropped Announce messages.
        - Arg8 (number): Percentage rate of the dropped Sync messages.
        - Arg9 (number): Percentage rate of the dropped Follow_Up messages.
        - Arg10 (number): Percentage rate of the dropped Delay_Resp messages.

        ptpChangeNegativeTesting(Arg2=number, Arg3=number, Arg4=number, Arg5=number, Arg6=number, Arg7=number, Arg8=number, Arg9=number, Arg10=number, Arg11=enum)
        ----------------------------------------------------------------------------------------------------------------------------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
        - Arg3 (number): Additional delay introduced in the Follow_Up message timestamp (nanoseconds).
        - Arg4 (number): Percentage rate of the Follow_Up messages in which the delay is introduced.
        - Arg5 (number): Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
        - Arg6 (number): Percentage rate of the Delay_Resp messages in which the delay is introduced.
        - Arg7 (number): Percentage rate of the dropped Announce messages.
        - Arg8 (number): Percentage rate of the dropped Sync messages.
        - Arg9 (number): Percentage rate of the dropped Follow_Up messages.
        - Arg10 (number): Percentage rate of the dropped Delay_Resp messages.
        - Arg11 (str(async | sync)): Percentage rate of the bad crc Follow_Up messages.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpChangeNegativeTesting', payload=payload, response_object=None)

    def PtpConfigure(self):
        """Executes the ptpConfigure operation on the server.

        Configure PTP protocol on selected ranges.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('ptpConfigure', payload=payload, response_object=None)

    def PtpPause(self):
        """Executes the ptpPause operation on the server.

        Pause negotiation of PTP for selected plugins and ranges

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('ptpPause', payload=payload, response_object=None)

    def PtpResume(self):
        """Executes the ptpResume operation on the server.

        Resume previously paused negotiation of PTP for selected plugins and ranges

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('ptpResume', payload=payload, response_object=None)

    def PtpStart(self, *args, **kwargs):
        """Executes the ptpStart operation on the server.

        Negotiate PTP for selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ptpStart(Arg2=enum)
        -------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpStart', payload=payload, response_object=None)

    def PtpStop(self, *args, **kwargs):
        """Executes the ptpStop operation on the server.

        Release PTP for selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ptpStop(Arg2=enum)
        ------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpStop', payload=payload, response_object=None)
