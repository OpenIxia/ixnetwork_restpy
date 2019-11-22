# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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
    The PtpRangeOverMac class encapsulates a list of ptpRangeOverMac resources that is be managed by the user.
    A list of resources can be retrieved from the server using the PtpRangeOverMac.find() method.
    The list can be managed by the user by using the PtpRangeOverMac.add() and PtpRangeOverMac.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ptpRangeOverMac'

    def __init__(self, parent):
        super(PtpRangeOverMac, self).__init__(parent)

    @property
    def AnnounceCurrentUtcOffsetValid(self):
        """Set Announce currentUtcOffsetValid bit

        Returns:
            bool
        """
        return self._get_attribute('announceCurrentUtcOffsetValid')
    @AnnounceCurrentUtcOffsetValid.setter
    def AnnounceCurrentUtcOffsetValid(self, value):
        self._set_attribute('announceCurrentUtcOffsetValid', value)

    @property
    def AnnounceDropRate(self):
        """Percentage rate of the dropped Announce messages.

        Returns:
            number
        """
        return self._get_attribute('announceDropRate')
    @AnnounceDropRate.setter
    def AnnounceDropRate(self, value):
        self._set_attribute('announceDropRate', value)

    @property
    def AnnounceFrequencyTraceable(self):
        """Set Announce frequency traceable bit

        Returns:
            bool
        """
        return self._get_attribute('announceFrequencyTraceable')
    @AnnounceFrequencyTraceable.setter
    def AnnounceFrequencyTraceable(self, value):
        self._set_attribute('announceFrequencyTraceable', value)

    @property
    def AnnounceLeap59(self):
        """Set Announce leap59 bit

        Returns:
            bool
        """
        return self._get_attribute('announceLeap59')
    @AnnounceLeap59.setter
    def AnnounceLeap59(self, value):
        self._set_attribute('announceLeap59', value)

    @property
    def AnnounceLeap61(self):
        """Set Announce leap61 bit

        Returns:
            bool
        """
        return self._get_attribute('announceLeap61')
    @AnnounceLeap61.setter
    def AnnounceLeap61(self, value):
        self._set_attribute('announceLeap61', value)

    @property
    def AnnouncePtpTimescale(self):
        """Set Announce ptpTimescale bit

        Returns:
            bool
        """
        return self._get_attribute('announcePtpTimescale')
    @AnnouncePtpTimescale.setter
    def AnnouncePtpTimescale(self, value):
        self._set_attribute('announcePtpTimescale', value)

    @property
    def AnnounceReceiptTimeout(self):
        """the number of announceInterval that has to pass without receipt of an Announce message.

        Returns:
            number
        """
        return self._get_attribute('announceReceiptTimeout')
    @AnnounceReceiptTimeout.setter
    def AnnounceReceiptTimeout(self, value):
        self._set_attribute('announceReceiptTimeout', value)

    @property
    def AnnounceTimeTraceable(self):
        """Set Announce time traceable bit

        Returns:
            bool
        """
        return self._get_attribute('announceTimeTraceable')
    @AnnounceTimeTraceable.setter
    def AnnounceTimeTraceable(self, value):
        self._set_attribute('announceTimeTraceable', value)

    @property
    def ClientCount(self):
        """The total number of Unicast clients to be used for the range.

        Returns:
            number
        """
        return self._get_attribute('clientCount')
    @ClientCount.setter
    def ClientCount(self, value):
        self._set_attribute('clientCount', value)

    @property
    def ClientIpAddress(self):
        """Defines the base address to be used for enumerating all the addresses in the range.

        Returns:
            str
        """
        return self._get_attribute('clientIpAddress')
    @ClientIpAddress.setter
    def ClientIpAddress(self, value):
        self._set_attribute('clientIpAddress', value)

    @property
    def ClientIpIncrementBy(self):
        """Defines the increment to be used for enumerating all the addresses in the range.

        Returns:
            str
        """
        return self._get_attribute('clientIpIncrementBy')
    @ClientIpIncrementBy.setter
    def ClientIpIncrementBy(self, value):
        self._set_attribute('clientIpIncrementBy', value)

    @property
    def ClientMacAddress(self):
        """Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'clientMacIncrementBy' as an incrementor.

        Returns:
            str
        """
        return self._get_attribute('clientMacAddress')
    @ClientMacAddress.setter
    def ClientMacAddress(self, value):
        self._set_attribute('clientMacAddress', value)

    @property
    def ClientMacIncrementBy(self):
        """Defines the increment to be used for enumerating all the addresses in the range.

        Returns:
            str
        """
        return self._get_attribute('clientMacIncrementBy')
    @ClientMacIncrementBy.setter
    def ClientMacIncrementBy(self, value):
        self._set_attribute('clientMacIncrementBy', value)

    @property
    def ClockAccuracy(self):
        """Clock accuracy.

        Returns:
            str
        """
        return self._get_attribute('clockAccuracy')
    @ClockAccuracy.setter
    def ClockAccuracy(self, value):
        self._set_attribute('clockAccuracy', value)

    @property
    def ClockClass(self):
        """Traceability of the time or frequency distributed by the grandmaster clock.

        Returns:
            number
        """
        return self._get_attribute('clockClass')
    @ClockClass.setter
    def ClockClass(self, value):
        self._set_attribute('clockClass', value)

    @property
    def ClockIncrement(self):
        """Defines the ClockIdentity increment to be used in this range.

        Returns:
            str
        """
        return self._get_attribute('clockIncrement')
    @ClockIncrement.setter
    def ClockIncrement(self, value):
        self._set_attribute('clockIncrement', value)

    @property
    def CommunicationMode(self):
        """Communication mode (unicast/multicast).

        Returns:
            str
        """
        return self._get_attribute('communicationMode')
    @CommunicationMode.setter
    def CommunicationMode(self, value):
        self._set_attribute('communicationMode', value)

    @property
    def DelayMechanism(self):
        """Clock delay mechanism.

        Returns:
            str
        """
        return self._get_attribute('delayMechanism')
    @DelayMechanism.setter
    def DelayMechanism(self, value):
        self._set_attribute('delayMechanism', value)

    @property
    def DelayRespDropRate(self):
        """Percentage rate of the dropped Delay_Resp messages.

        Returns:
            number
        """
        return self._get_attribute('delayRespDropRate')
    @DelayRespDropRate.setter
    def DelayRespDropRate(self, value):
        self._set_attribute('delayRespDropRate', value)

    @property
    def DelayRespReceiptTimeout(self):
        """DelayResponse Receipt Timeout in seconds.

        Returns:
            number
        """
        return self._get_attribute('delayRespReceiptTimeout')
    @DelayRespReceiptTimeout.setter
    def DelayRespReceiptTimeout(self, value):
        self._set_attribute('delayRespReceiptTimeout', value)

    @property
    def DelayResponseDelay(self):
        """Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).

        Returns:
            number
        """
        return self._get_attribute('delayResponseDelay')
    @DelayResponseDelay.setter
    def DelayResponseDelay(self, value):
        self._set_attribute('delayResponseDelay', value)

    @property
    def DelayResponseDelayInsertionRate(self):
        """Percentage rate of the Delay_Resp messages in which the delay is introduced.

        Returns:
            number
        """
        return self._get_attribute('delayResponseDelayInsertionRate')
    @DelayResponseDelayInsertionRate.setter
    def DelayResponseDelayInsertionRate(self, value):
        self._set_attribute('delayResponseDelayInsertionRate', value)

    @property
    def Domain(self):
        """PTP Domain

        Returns:
            number
        """
        return self._get_attribute('domain')
    @Domain.setter
    def Domain(self, value):
        self._set_attribute('domain', value)

    @property
    def DropSignalReqAnnounce(self):
        """Select this check box to drop any Signal Request that contains Announce TLV.

        Returns:
            bool
        """
        return self._get_attribute('dropSignalReqAnnounce')
    @DropSignalReqAnnounce.setter
    def DropSignalReqAnnounce(self, value):
        self._set_attribute('dropSignalReqAnnounce', value)

    @property
    def DropSignalReqDelayResp(self):
        """Select this check box to drop any Signal Request that contains DelayResp TLV.

        Returns:
            bool
        """
        return self._get_attribute('dropSignalReqDelayResp')
    @DropSignalReqDelayResp.setter
    def DropSignalReqDelayResp(self, value):
        self._set_attribute('dropSignalReqDelayResp', value)

    @property
    def DropSignalReqSync(self):
        """Select this check box to drop any Signal Request that contains Sync TLV.

        Returns:
            bool
        """
        return self._get_attribute('dropSignalReqSync')
    @DropSignalReqSync.setter
    def DropSignalReqSync(self, value):
        self._set_attribute('dropSignalReqSync', value)

    @property
    def Enabled(self):
        """Disabled ranges won't be configured nor validated.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def FirstClock(self):
        """Defines the first ClockIdentity to be used in this range.

        Returns:
            str
        """
        return self._get_attribute('firstClock')
    @FirstClock.setter
    def FirstClock(self, value):
        self._set_attribute('firstClock', value)

    @property
    def FollowUpBadCrcRate(self):
        """Percentage rate of the bad crc Follow_Up messages.

        Returns:
            number
        """
        return self._get_attribute('followUpBadCrcRate')
    @FollowUpBadCrcRate.setter
    def FollowUpBadCrcRate(self, value):
        self._set_attribute('followUpBadCrcRate', value)

    @property
    def FollowUpDelay(self):
        """Additional delay introduced in the Follow_Up message timestamp (nanoseconds)

        Returns:
            number
        """
        return self._get_attribute('followUpDelay')
    @FollowUpDelay.setter
    def FollowUpDelay(self, value):
        self._set_attribute('followUpDelay', value)

    @property
    def FollowUpDelayInsertionRate(self):
        """Percentage rate of the Follow_Up messages in which the delay is introduced

        Returns:
            number
        """
        return self._get_attribute('followUpDelayInsertionRate')
    @FollowUpDelayInsertionRate.setter
    def FollowUpDelayInsertionRate(self, value):
        self._set_attribute('followUpDelayInsertionRate', value)

    @property
    def FollowUpDropRate(self):
        """Percentage rate of the dropped Follow_Up messages.

        Returns:
            number
        """
        return self._get_attribute('followUpDropRate')
    @FollowUpDropRate.setter
    def FollowUpDropRate(self, value):
        self._set_attribute('followUpDropRate', value)

    @property
    def GrantDelayRespDurationInterval(self):
        """Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for DelayResp messages.

        Returns:
            number
        """
        return self._get_attribute('grantDelayRespDurationInterval')
    @GrantDelayRespDurationInterval.setter
    def GrantDelayRespDurationInterval(self, value):
        self._set_attribute('grantDelayRespDurationInterval', value)

    @property
    def GrantSyncDurationInterval(self):
        """Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for Sync messages.

        Returns:
            number
        """
        return self._get_attribute('grantSyncDurationInterval')
    @GrantSyncDurationInterval.setter
    def GrantSyncDurationInterval(self, value):
        self._set_attribute('grantSyncDurationInterval', value)

    @property
    def GrantUnicastDurationInterval(self):
        """Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV.

        Returns:
            number
        """
        return self._get_attribute('grantUnicastDurationInterval')
    @GrantUnicastDurationInterval.setter
    def GrantUnicastDurationInterval(self, value):
        self._set_attribute('grantUnicastDurationInterval', value)

    @property
    def IpTos(self):
        """IP TOS or DS.

        Returns:
            number
        """
        return self._get_attribute('ipTos')
    @IpTos.setter
    def IpTos(self, value):
        self._set_attribute('ipTos', value)

    @property
    def LearnPortId(self):
        """Slave learns Master Port ID

        Returns:
            bool
        """
        return self._get_attribute('learnPortId')
    @LearnPortId.setter
    def LearnPortId(self, value):
        self._set_attribute('learnPortId', value)

    @property
    def LogAnnounceInterval(self):
        """The log mean time interval between successive Announce messages.

        Returns:
            number
        """
        return self._get_attribute('logAnnounceInterval')
    @LogAnnounceInterval.setter
    def LogAnnounceInterval(self, value):
        self._set_attribute('logAnnounceInterval', value)

    @property
    def LogDelayReqInterval(self):
        """The log mean time interval between successive Delay_Req messages.

        Returns:
            number
        """
        return self._get_attribute('logDelayReqInterval')
    @LogDelayReqInterval.setter
    def LogDelayReqInterval(self, value):
        self._set_attribute('logDelayReqInterval', value)

    @property
    def LogSyncInterval(self):
        """The log mean time interval between successive Sync messages.

        Returns:
            number
        """
        return self._get_attribute('logSyncInterval')
    @LogSyncInterval.setter
    def LogSyncInterval(self, value):
        self._set_attribute('logSyncInterval', value)

    @property
    def MasterCount(self):
        """The total number of Unicast masters to be used for the range.

        Returns:
            number
        """
        return self._get_attribute('masterCount')
    @MasterCount.setter
    def MasterCount(self, value):
        self._set_attribute('masterCount', value)

    @property
    def MasterIpAddress(self):
        """Defines the base address to be used for enumerating all the addresses in the range.

        Returns:
            str
        """
        return self._get_attribute('masterIpAddress')
    @MasterIpAddress.setter
    def MasterIpAddress(self, value):
        self._set_attribute('masterIpAddress', value)

    @property
    def MasterIpIncrementBy(self):
        """Defines the increment to be used for enumerating all the addresses in the range.

        Returns:
            str
        """
        return self._get_attribute('masterIpIncrementBy')
    @MasterIpIncrementBy.setter
    def MasterIpIncrementBy(self, value):
        self._set_attribute('masterIpIncrementBy', value)

    @property
    def MasterIpIncrementInterEntity(self):
        """Defines the increment to be used for the start address of Master

        Returns:
            str
        """
        return self._get_attribute('masterIpIncrementInterEntity')
    @MasterIpIncrementInterEntity.setter
    def MasterIpIncrementInterEntity(self, value):
        self._set_attribute('masterIpIncrementInterEntity', value)

    @property
    def MasterMacAddress(self):
        """Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'masterMacIncrementBy' as an incrementor.

        Returns:
            str
        """
        return self._get_attribute('masterMacAddress')
    @MasterMacAddress.setter
    def MasterMacAddress(self, value):
        self._set_attribute('masterMacAddress', value)

    @property
    def MasterMacIncrementBy(self):
        """Defines the increment to be used for enumerating all the addresses in the range.

        Returns:
            str
        """
        return self._get_attribute('masterMacIncrementBy')
    @MasterMacIncrementBy.setter
    def MasterMacIncrementBy(self, value):
        self._set_attribute('masterMacIncrementBy', value)

    @property
    def MasterMacIncrementInterEntity(self):
        """Defines the increment to be used for the start address of Master

        Returns:
            str
        """
        return self._get_attribute('masterMacIncrementInterEntity')
    @MasterMacIncrementInterEntity.setter
    def MasterMacIncrementInterEntity(self, value):
        self._set_attribute('masterMacIncrementInterEntity', value)

    @property
    def Name(self):
        """Name of range

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def PortNumber(self):
        """Port number

        Returns:
            number
        """
        return self._get_attribute('portNumber')
    @PortNumber.setter
    def PortNumber(self, value):
        self._set_attribute('portNumber', value)

    @property
    def PortNumberIncrement(self):
        """Port number increment

        Returns:
            number
        """
        return self._get_attribute('portNumberIncrement')
    @PortNumberIncrement.setter
    def PortNumberIncrement(self, value):
        self._set_attribute('portNumberIncrement', value)

    @property
    def Priority1(self):
        """PTP priority1.

        Returns:
            number
        """
        return self._get_attribute('priority1')
    @Priority1.setter
    def Priority1(self, value):
        self._set_attribute('priority1', value)

    @property
    def Priority2(self):
        """PTP priority2.

        Returns:
            number
        """
        return self._get_attribute('priority2')
    @Priority2.setter
    def Priority2(self, value):
        self._set_attribute('priority2', value)

    @property
    def RenewalInvited(self):
        """Set the Renewal Invited flag in Grant Unicast Transmission TLV

        Returns:
            bool
        """
        return self._get_attribute('renewalInvited')
    @RenewalInvited.setter
    def RenewalInvited(self, value):
        self._set_attribute('renewalInvited', value)

    @property
    def RequestAttempts(self):
        """How many succesive requests a client can request before entering into holddown.

        Returns:
            number
        """
        return self._get_attribute('requestAttempts')
    @RequestAttempts.setter
    def RequestAttempts(self, value):
        self._set_attribute('requestAttempts', value)

    @property
    def RequestHolddown(self):
        """Time between succesive requests if denied/timeout for Signal Request.

        Returns:
            number
        """
        return self._get_attribute('requestHolddown')
    @RequestHolddown.setter
    def RequestHolddown(self, value):
        self._set_attribute('requestHolddown', value)

    @property
    def RequestInterval(self):
        """Time between succesive requests if denied/timeout for Signal Request.

        Returns:
            number
        """
        return self._get_attribute('requestInterval')
    @RequestInterval.setter
    def RequestInterval(self, value):
        self._set_attribute('requestInterval', value)

    @property
    def ResidenceTime(self):
        """Master to slave residence time of the associated transparent clock

        Returns:
            number
        """
        return self._get_attribute('residenceTime')
    @ResidenceTime.setter
    def ResidenceTime(self, value):
        self._set_attribute('residenceTime', value)

    @property
    def RxCalibration(self):
        """The amount of time (in ns) that the Receive side timestamp needs to be offset to allow for error.

        Returns:
            number
        """
        return self._get_attribute('rxCalibration')
    @RxCalibration.setter
    def RxCalibration(self, value):
        self._set_attribute('rxCalibration', value)

    @property
    def SendAnnounceMulticast(self):
        """Send multicast Announce messages.

        Returns:
            bool
        """
        return self._get_attribute('sendAnnounceMulticast')
    @SendAnnounceMulticast.setter
    def SendAnnounceMulticast(self, value):
        self._set_attribute('sendAnnounceMulticast', value)

    @property
    def SendAnnounceTlv(self):
        """Send and respond to Announce TLV unicast requests in signal messages.

        Returns:
            bool
        """
        return self._get_attribute('sendAnnounceTlv')
    @SendAnnounceTlv.setter
    def SendAnnounceTlv(self, value):
        self._set_attribute('sendAnnounceTlv', value)

    @property
    def SendCancelTlv(self):
        """Send and respond to Cancel TLV unicast requests in signal messages.

        Returns:
            bool
        """
        return self._get_attribute('sendCancelTlv')
    @SendCancelTlv.setter
    def SendCancelTlv(self, value):
        self._set_attribute('sendCancelTlv', value)

    @property
    def SignalInterval(self):
        """Time between Signal Request messages, in seconds.

        Returns:
            number
        """
        return self._get_attribute('signalInterval')
    @SignalInterval.setter
    def SignalInterval(self, value):
        self._set_attribute('signalInterval', value)

    @property
    def SignalUnicastHandling(self):
        """

        Returns:
            str
        """
        return self._get_attribute('signalUnicastHandling')
    @SignalUnicastHandling.setter
    def SignalUnicastHandling(self, value):
        self._set_attribute('signalUnicastHandling', value)

    @property
    def StepMode(self):
        """Clock step mode.

        Returns:
            str
        """
        return self._get_attribute('stepMode')
    @StepMode.setter
    def StepMode(self, value):
        self._set_attribute('stepMode', value)

    @property
    def StepsRemoved(self):
        """The number of hops between the Grandmaster Clock and the emulated clock. Valid values: 0 to 65,535.

        Returns:
            number
        """
        return self._get_attribute('stepsRemoved')
    @StepsRemoved.setter
    def StepsRemoved(self, value):
        self._set_attribute('stepsRemoved', value)

    @property
    def StrictGrant(self):
        """If selected, server will not grant values that are above maximum offered values.

        Returns:
            bool
        """
        return self._get_attribute('strictGrant')
    @StrictGrant.setter
    def StrictGrant(self, value):
        self._set_attribute('strictGrant', value)

    @property
    def SyncDropRate(self):
        """Percentage rate of the dropped Sync messages.

        Returns:
            number
        """
        return self._get_attribute('syncDropRate')
    @SyncDropRate.setter
    def SyncDropRate(self, value):
        self._set_attribute('syncDropRate', value)

    @property
    def SyncReceiptTimeout(self):
        """Sync Receipt Timeout in seconds.

        Returns:
            number
        """
        return self._get_attribute('syncReceiptTimeout')
    @SyncReceiptTimeout.setter
    def SyncReceiptTimeout(self, value):
        self._set_attribute('syncReceiptTimeout', value)

    @property
    def TimeSource(self):
        """Time source for the PTP device.

        Returns:
            str
        """
        return self._get_attribute('timeSource')
    @TimeSource.setter
    def TimeSource(self, value):
        self._set_attribute('timeSource', value)

    @property
    def TimestampOffset(self):
        """Timestamp offset.

        Returns:
            number
        """
        return self._get_attribute('timestampOffset')
    @TimestampOffset.setter
    def TimestampOffset(self, value):
        self._set_attribute('timestampOffset', value)

    @property
    def TimestampOffsetVariation(self):
        """Timestamp offset variation.

        Returns:
            number
        """
        return self._get_attribute('timestampOffsetVariation')
    @TimestampOffsetVariation.setter
    def TimestampOffsetVariation(self, value):
        self._set_attribute('timestampOffsetVariation', value)

    @property
    def TxCalibration(self):
        """The amount of time (in ns) that the Transmit side timestamp needs to be offset to allow for error.

        Returns:
            number
        """
        return self._get_attribute('txCalibration')
    @TxCalibration.setter
    def TxCalibration(self, value):
        self._set_attribute('txCalibration', value)

    @property
    def UseAlternateMasterFlag(self):
        """Select this check box to set the Alternate Master flag in all Announce and Sync messages.

        Returns:
            bool
        """
        return self._get_attribute('useAlternateMasterFlag')
    @UseAlternateMasterFlag.setter
    def UseAlternateMasterFlag(self, value):
        self._set_attribute('useAlternateMasterFlag', value)

    @property
    def UseClockIdentity(self):
        """Use the ClockIdentity configured below.

        Returns:
            bool
        """
        return self._get_attribute('useClockIdentity')
    @UseClockIdentity.setter
    def UseClockIdentity(self, value):
        self._set_attribute('useClockIdentity', value)

    def update(self, AnnounceCurrentUtcOffsetValid=None, AnnounceDropRate=None, AnnounceFrequencyTraceable=None, AnnounceLeap59=None, AnnounceLeap61=None, AnnouncePtpTimescale=None, AnnounceReceiptTimeout=None, AnnounceTimeTraceable=None, ClientCount=None, ClientIpAddress=None, ClientIpIncrementBy=None, ClientMacAddress=None, ClientMacIncrementBy=None, ClockAccuracy=None, ClockClass=None, ClockIncrement=None, CommunicationMode=None, DelayMechanism=None, DelayRespDropRate=None, DelayRespReceiptTimeout=None, DelayResponseDelay=None, DelayResponseDelayInsertionRate=None, Domain=None, DropSignalReqAnnounce=None, DropSignalReqDelayResp=None, DropSignalReqSync=None, Enabled=None, FirstClock=None, FollowUpBadCrcRate=None, FollowUpDelay=None, FollowUpDelayInsertionRate=None, FollowUpDropRate=None, GrantDelayRespDurationInterval=None, GrantSyncDurationInterval=None, GrantUnicastDurationInterval=None, IpTos=None, LearnPortId=None, LogAnnounceInterval=None, LogDelayReqInterval=None, LogSyncInterval=None, MasterCount=None, MasterIpAddress=None, MasterIpIncrementBy=None, MasterIpIncrementInterEntity=None, MasterMacAddress=None, MasterMacIncrementBy=None, MasterMacIncrementInterEntity=None, Name=None, PortNumber=None, PortNumberIncrement=None, Priority1=None, Priority2=None, RenewalInvited=None, RequestAttempts=None, RequestHolddown=None, RequestInterval=None, ResidenceTime=None, RxCalibration=None, SendAnnounceMulticast=None, SendAnnounceTlv=None, SendCancelTlv=None, SignalInterval=None, SignalUnicastHandling=None, StepMode=None, StepsRemoved=None, StrictGrant=None, SyncDropRate=None, SyncReceiptTimeout=None, TimeSource=None, TimestampOffset=None, TimestampOffsetVariation=None, TxCalibration=None, UseAlternateMasterFlag=None, UseClockIdentity=None):
        """Updates a child instance of ptpRangeOverMac on the server.

        Args:
            AnnounceCurrentUtcOffsetValid (bool): Set Announce currentUtcOffsetValid bit
            AnnounceDropRate (number): Percentage rate of the dropped Announce messages.
            AnnounceFrequencyTraceable (bool): Set Announce frequency traceable bit
            AnnounceLeap59 (bool): Set Announce leap59 bit
            AnnounceLeap61 (bool): Set Announce leap61 bit
            AnnouncePtpTimescale (bool): Set Announce ptpTimescale bit
            AnnounceReceiptTimeout (number): the number of announceInterval that has to pass without receipt of an Announce message.
            AnnounceTimeTraceable (bool): Set Announce time traceable bit
            ClientCount (number): The total number of Unicast clients to be used for the range.
            ClientIpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
            ClientIpIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
            ClientMacAddress (str): Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'clientMacIncrementBy' as an incrementor.
            ClientMacIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
            ClockAccuracy (str): Clock accuracy.
            ClockClass (number): Traceability of the time or frequency distributed by the grandmaster clock.
            ClockIncrement (str): Defines the ClockIdentity increment to be used in this range.
            CommunicationMode (str): Communication mode (unicast/multicast).
            DelayMechanism (str): Clock delay mechanism.
            DelayRespDropRate (number): Percentage rate of the dropped Delay_Resp messages.
            DelayRespReceiptTimeout (number): DelayResponse Receipt Timeout in seconds.
            DelayResponseDelay (number): Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
            DelayResponseDelayInsertionRate (number): Percentage rate of the Delay_Resp messages in which the delay is introduced.
            Domain (number): PTP Domain
            DropSignalReqAnnounce (bool): Select this check box to drop any Signal Request that contains Announce TLV.
            DropSignalReqDelayResp (bool): Select this check box to drop any Signal Request that contains DelayResp TLV.
            DropSignalReqSync (bool): Select this check box to drop any Signal Request that contains Sync TLV.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FirstClock (str): Defines the first ClockIdentity to be used in this range.
            FollowUpBadCrcRate (number): Percentage rate of the bad crc Follow_Up messages.
            FollowUpDelay (number): Additional delay introduced in the Follow_Up message timestamp (nanoseconds)
            FollowUpDelayInsertionRate (number): Percentage rate of the Follow_Up messages in which the delay is introduced
            FollowUpDropRate (number): Percentage rate of the dropped Follow_Up messages.
            GrantDelayRespDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for DelayResp messages.
            GrantSyncDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for Sync messages.
            GrantUnicastDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV.
            IpTos (number): IP TOS or DS.
            LearnPortId (bool): Slave learns Master Port ID
            LogAnnounceInterval (number): The log mean time interval between successive Announce messages.
            LogDelayReqInterval (number): The log mean time interval between successive Delay_Req messages.
            LogSyncInterval (number): The log mean time interval between successive Sync messages.
            MasterCount (number): The total number of Unicast masters to be used for the range.
            MasterIpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
            MasterIpIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
            MasterIpIncrementInterEntity (str): Defines the increment to be used for the start address of Master
            MasterMacAddress (str): Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'masterMacIncrementBy' as an incrementor.
            MasterMacIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
            MasterMacIncrementInterEntity (str): Defines the increment to be used for the start address of Master
            Name (str): Name of range
            PortNumber (number): Port number
            PortNumberIncrement (number): Port number increment
            Priority1 (number): PTP priority1.
            Priority2 (number): PTP priority2.
            RenewalInvited (bool): Set the Renewal Invited flag in Grant Unicast Transmission TLV
            RequestAttempts (number): How many succesive requests a client can request before entering into holddown.
            RequestHolddown (number): Time between succesive requests if denied/timeout for Signal Request.
            RequestInterval (number): Time between succesive requests if denied/timeout for Signal Request.
            ResidenceTime (number): Master to slave residence time of the associated transparent clock
            RxCalibration (number): The amount of time (in ns) that the Receive side timestamp needs to be offset to allow for error.
            SendAnnounceMulticast (bool): Send multicast Announce messages.
            SendAnnounceTlv (bool): Send and respond to Announce TLV unicast requests in signal messages.
            SendCancelTlv (bool): Send and respond to Cancel TLV unicast requests in signal messages.
            SignalInterval (number): Time between Signal Request messages, in seconds.
            SignalUnicastHandling (str): 
            StepMode (str): Clock step mode.
            StepsRemoved (number): The number of hops between the Grandmaster Clock and the emulated clock. Valid values: 0 to 65,535.
            StrictGrant (bool): If selected, server will not grant values that are above maximum offered values.
            SyncDropRate (number): Percentage rate of the dropped Sync messages.
            SyncReceiptTimeout (number): Sync Receipt Timeout in seconds.
            TimeSource (str): Time source for the PTP device.
            TimestampOffset (number): Timestamp offset.
            TimestampOffsetVariation (number): Timestamp offset variation.
            TxCalibration (number): The amount of time (in ns) that the Transmit side timestamp needs to be offset to allow for error.
            UseAlternateMasterFlag (bool): Select this check box to set the Alternate Master flag in all Announce and Sync messages.
            UseClockIdentity (bool): Use the ClockIdentity configured below.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AnnounceCurrentUtcOffsetValid=None, AnnounceDropRate=None, AnnounceFrequencyTraceable=None, AnnounceLeap59=None, AnnounceLeap61=None, AnnouncePtpTimescale=None, AnnounceReceiptTimeout=None, AnnounceTimeTraceable=None, ClientCount=None, ClientIpAddress=None, ClientIpIncrementBy=None, ClientMacAddress=None, ClientMacIncrementBy=None, ClockAccuracy=None, ClockClass=None, ClockIncrement=None, CommunicationMode=None, DelayMechanism=None, DelayRespDropRate=None, DelayRespReceiptTimeout=None, DelayResponseDelay=None, DelayResponseDelayInsertionRate=None, Domain=None, DropSignalReqAnnounce=None, DropSignalReqDelayResp=None, DropSignalReqSync=None, Enabled=None, FirstClock=None, FollowUpBadCrcRate=None, FollowUpDelay=None, FollowUpDelayInsertionRate=None, FollowUpDropRate=None, GrantDelayRespDurationInterval=None, GrantSyncDurationInterval=None, GrantUnicastDurationInterval=None, IpTos=None, LearnPortId=None, LogAnnounceInterval=None, LogDelayReqInterval=None, LogSyncInterval=None, MasterCount=None, MasterIpAddress=None, MasterIpIncrementBy=None, MasterIpIncrementInterEntity=None, MasterMacAddress=None, MasterMacIncrementBy=None, MasterMacIncrementInterEntity=None, Name=None, PortNumber=None, PortNumberIncrement=None, Priority1=None, Priority2=None, RenewalInvited=None, RequestAttempts=None, RequestHolddown=None, RequestInterval=None, ResidenceTime=None, RxCalibration=None, SendAnnounceMulticast=None, SendAnnounceTlv=None, SendCancelTlv=None, SignalInterval=None, SignalUnicastHandling=None, StepMode=None, StepsRemoved=None, StrictGrant=None, SyncDropRate=None, SyncReceiptTimeout=None, TimeSource=None, TimestampOffset=None, TimestampOffsetVariation=None, TxCalibration=None, UseAlternateMasterFlag=None, UseClockIdentity=None):
        """Adds a new ptpRangeOverMac node on the server and retrieves it in this instance.

        Args:
            AnnounceCurrentUtcOffsetValid (bool): Set Announce currentUtcOffsetValid bit
            AnnounceDropRate (number): Percentage rate of the dropped Announce messages.
            AnnounceFrequencyTraceable (bool): Set Announce frequency traceable bit
            AnnounceLeap59 (bool): Set Announce leap59 bit
            AnnounceLeap61 (bool): Set Announce leap61 bit
            AnnouncePtpTimescale (bool): Set Announce ptpTimescale bit
            AnnounceReceiptTimeout (number): the number of announceInterval that has to pass without receipt of an Announce message.
            AnnounceTimeTraceable (bool): Set Announce time traceable bit
            ClientCount (number): The total number of Unicast clients to be used for the range.
            ClientIpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
            ClientIpIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
            ClientMacAddress (str): Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'clientMacIncrementBy' as an incrementor.
            ClientMacIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
            ClockAccuracy (str): Clock accuracy.
            ClockClass (number): Traceability of the time or frequency distributed by the grandmaster clock.
            ClockIncrement (str): Defines the ClockIdentity increment to be used in this range.
            CommunicationMode (str): Communication mode (unicast/multicast).
            DelayMechanism (str): Clock delay mechanism.
            DelayRespDropRate (number): Percentage rate of the dropped Delay_Resp messages.
            DelayRespReceiptTimeout (number): DelayResponse Receipt Timeout in seconds.
            DelayResponseDelay (number): Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
            DelayResponseDelayInsertionRate (number): Percentage rate of the Delay_Resp messages in which the delay is introduced.
            Domain (number): PTP Domain
            DropSignalReqAnnounce (bool): Select this check box to drop any Signal Request that contains Announce TLV.
            DropSignalReqDelayResp (bool): Select this check box to drop any Signal Request that contains DelayResp TLV.
            DropSignalReqSync (bool): Select this check box to drop any Signal Request that contains Sync TLV.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FirstClock (str): Defines the first ClockIdentity to be used in this range.
            FollowUpBadCrcRate (number): Percentage rate of the bad crc Follow_Up messages.
            FollowUpDelay (number): Additional delay introduced in the Follow_Up message timestamp (nanoseconds)
            FollowUpDelayInsertionRate (number): Percentage rate of the Follow_Up messages in which the delay is introduced
            FollowUpDropRate (number): Percentage rate of the dropped Follow_Up messages.
            GrantDelayRespDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for DelayResp messages.
            GrantSyncDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for Sync messages.
            GrantUnicastDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV.
            IpTos (number): IP TOS or DS.
            LearnPortId (bool): Slave learns Master Port ID
            LogAnnounceInterval (number): The log mean time interval between successive Announce messages.
            LogDelayReqInterval (number): The log mean time interval between successive Delay_Req messages.
            LogSyncInterval (number): The log mean time interval between successive Sync messages.
            MasterCount (number): The total number of Unicast masters to be used for the range.
            MasterIpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
            MasterIpIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
            MasterIpIncrementInterEntity (str): Defines the increment to be used for the start address of Master
            MasterMacAddress (str): Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'masterMacIncrementBy' as an incrementor.
            MasterMacIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
            MasterMacIncrementInterEntity (str): Defines the increment to be used for the start address of Master
            Name (str): Name of range
            PortNumber (number): Port number
            PortNumberIncrement (number): Port number increment
            Priority1 (number): PTP priority1.
            Priority2 (number): PTP priority2.
            RenewalInvited (bool): Set the Renewal Invited flag in Grant Unicast Transmission TLV
            RequestAttempts (number): How many succesive requests a client can request before entering into holddown.
            RequestHolddown (number): Time between succesive requests if denied/timeout for Signal Request.
            RequestInterval (number): Time between succesive requests if denied/timeout for Signal Request.
            ResidenceTime (number): Master to slave residence time of the associated transparent clock
            RxCalibration (number): The amount of time (in ns) that the Receive side timestamp needs to be offset to allow for error.
            SendAnnounceMulticast (bool): Send multicast Announce messages.
            SendAnnounceTlv (bool): Send and respond to Announce TLV unicast requests in signal messages.
            SendCancelTlv (bool): Send and respond to Cancel TLV unicast requests in signal messages.
            SignalInterval (number): Time between Signal Request messages, in seconds.
            SignalUnicastHandling (str): 
            StepMode (str): Clock step mode.
            StepsRemoved (number): The number of hops between the Grandmaster Clock and the emulated clock. Valid values: 0 to 65,535.
            StrictGrant (bool): If selected, server will not grant values that are above maximum offered values.
            SyncDropRate (number): Percentage rate of the dropped Sync messages.
            SyncReceiptTimeout (number): Sync Receipt Timeout in seconds.
            TimeSource (str): Time source for the PTP device.
            TimestampOffset (number): Timestamp offset.
            TimestampOffsetVariation (number): Timestamp offset variation.
            TxCalibration (number): The amount of time (in ns) that the Transmit side timestamp needs to be offset to allow for error.
            UseAlternateMasterFlag (bool): Select this check box to set the Alternate Master flag in all Announce and Sync messages.
            UseClockIdentity (bool): Use the ClockIdentity configured below.

        Returns:
            self: This instance with all currently retrieved ptpRangeOverMac data using find and the newly added ptpRangeOverMac data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the ptpRangeOverMac data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AnnounceCurrentUtcOffsetValid=None, AnnounceDropRate=None, AnnounceFrequencyTraceable=None, AnnounceLeap59=None, AnnounceLeap61=None, AnnouncePtpTimescale=None, AnnounceReceiptTimeout=None, AnnounceTimeTraceable=None, ClientCount=None, ClientIpAddress=None, ClientIpIncrementBy=None, ClientMacAddress=None, ClientMacIncrementBy=None, ClockAccuracy=None, ClockClass=None, ClockIncrement=None, CommunicationMode=None, DelayMechanism=None, DelayRespDropRate=None, DelayRespReceiptTimeout=None, DelayResponseDelay=None, DelayResponseDelayInsertionRate=None, Domain=None, DropSignalReqAnnounce=None, DropSignalReqDelayResp=None, DropSignalReqSync=None, Enabled=None, FirstClock=None, FollowUpBadCrcRate=None, FollowUpDelay=None, FollowUpDelayInsertionRate=None, FollowUpDropRate=None, GrantDelayRespDurationInterval=None, GrantSyncDurationInterval=None, GrantUnicastDurationInterval=None, IpTos=None, LearnPortId=None, LogAnnounceInterval=None, LogDelayReqInterval=None, LogSyncInterval=None, MasterCount=None, MasterIpAddress=None, MasterIpIncrementBy=None, MasterIpIncrementInterEntity=None, MasterMacAddress=None, MasterMacIncrementBy=None, MasterMacIncrementInterEntity=None, Name=None, ObjectId=None, PortNumber=None, PortNumberIncrement=None, Priority1=None, Priority2=None, RenewalInvited=None, RequestAttempts=None, RequestHolddown=None, RequestInterval=None, ResidenceTime=None, RxCalibration=None, SendAnnounceMulticast=None, SendAnnounceTlv=None, SendCancelTlv=None, SignalInterval=None, SignalUnicastHandling=None, StepMode=None, StepsRemoved=None, StrictGrant=None, SyncDropRate=None, SyncReceiptTimeout=None, TimeSource=None, TimestampOffset=None, TimestampOffsetVariation=None, TxCalibration=None, UseAlternateMasterFlag=None, UseClockIdentity=None):
        """Finds and retrieves ptpRangeOverMac data from the server.

        All named parameters support regex and can be used to selectively retrieve ptpRangeOverMac data from the server.
        By default the find method takes no parameters and will retrieve all ptpRangeOverMac data from the server.

        Args:
            AnnounceCurrentUtcOffsetValid (bool): Set Announce currentUtcOffsetValid bit
            AnnounceDropRate (number): Percentage rate of the dropped Announce messages.
            AnnounceFrequencyTraceable (bool): Set Announce frequency traceable bit
            AnnounceLeap59 (bool): Set Announce leap59 bit
            AnnounceLeap61 (bool): Set Announce leap61 bit
            AnnouncePtpTimescale (bool): Set Announce ptpTimescale bit
            AnnounceReceiptTimeout (number): the number of announceInterval that has to pass without receipt of an Announce message.
            AnnounceTimeTraceable (bool): Set Announce time traceable bit
            ClientCount (number): The total number of Unicast clients to be used for the range.
            ClientIpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
            ClientIpIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
            ClientMacAddress (str): Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'clientMacIncrementBy' as an incrementor.
            ClientMacIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
            ClockAccuracy (str): Clock accuracy.
            ClockClass (number): Traceability of the time or frequency distributed by the grandmaster clock.
            ClockIncrement (str): Defines the ClockIdentity increment to be used in this range.
            CommunicationMode (str): Communication mode (unicast/multicast).
            DelayMechanism (str): Clock delay mechanism.
            DelayRespDropRate (number): Percentage rate of the dropped Delay_Resp messages.
            DelayRespReceiptTimeout (number): DelayResponse Receipt Timeout in seconds.
            DelayResponseDelay (number): Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
            DelayResponseDelayInsertionRate (number): Percentage rate of the Delay_Resp messages in which the delay is introduced.
            Domain (number): PTP Domain
            DropSignalReqAnnounce (bool): Select this check box to drop any Signal Request that contains Announce TLV.
            DropSignalReqDelayResp (bool): Select this check box to drop any Signal Request that contains DelayResp TLV.
            DropSignalReqSync (bool): Select this check box to drop any Signal Request that contains Sync TLV.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FirstClock (str): Defines the first ClockIdentity to be used in this range.
            FollowUpBadCrcRate (number): Percentage rate of the bad crc Follow_Up messages.
            FollowUpDelay (number): Additional delay introduced in the Follow_Up message timestamp (nanoseconds)
            FollowUpDelayInsertionRate (number): Percentage rate of the Follow_Up messages in which the delay is introduced
            FollowUpDropRate (number): Percentage rate of the dropped Follow_Up messages.
            GrantDelayRespDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for DelayResp messages.
            GrantSyncDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for Sync messages.
            GrantUnicastDurationInterval (number): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV.
            IpTos (number): IP TOS or DS.
            LearnPortId (bool): Slave learns Master Port ID
            LogAnnounceInterval (number): The log mean time interval between successive Announce messages.
            LogDelayReqInterval (number): The log mean time interval between successive Delay_Req messages.
            LogSyncInterval (number): The log mean time interval between successive Sync messages.
            MasterCount (number): The total number of Unicast masters to be used for the range.
            MasterIpAddress (str): Defines the base address to be used for enumerating all the addresses in the range.
            MasterIpIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
            MasterIpIncrementInterEntity (str): Defines the increment to be used for the start address of Master
            MasterMacAddress (str): Defines the base address to be used for enumerating all the addresses in the range. This property is used in conjunction with 'masterMacIncrementBy' as an incrementor.
            MasterMacIncrementBy (str): Defines the increment to be used for enumerating all the addresses in the range.
            MasterMacIncrementInterEntity (str): Defines the increment to be used for the start address of Master
            Name (str): Name of range
            ObjectId (str): Unique identifier for this object
            PortNumber (number): Port number
            PortNumberIncrement (number): Port number increment
            Priority1 (number): PTP priority1.
            Priority2 (number): PTP priority2.
            RenewalInvited (bool): Set the Renewal Invited flag in Grant Unicast Transmission TLV
            RequestAttempts (number): How many succesive requests a client can request before entering into holddown.
            RequestHolddown (number): Time between succesive requests if denied/timeout for Signal Request.
            RequestInterval (number): Time between succesive requests if denied/timeout for Signal Request.
            ResidenceTime (number): Master to slave residence time of the associated transparent clock
            RxCalibration (number): The amount of time (in ns) that the Receive side timestamp needs to be offset to allow for error.
            SendAnnounceMulticast (bool): Send multicast Announce messages.
            SendAnnounceTlv (bool): Send and respond to Announce TLV unicast requests in signal messages.
            SendCancelTlv (bool): Send and respond to Cancel TLV unicast requests in signal messages.
            SignalInterval (number): Time between Signal Request messages, in seconds.
            SignalUnicastHandling (str): 
            StepMode (str): Clock step mode.
            StepsRemoved (number): The number of hops between the Grandmaster Clock and the emulated clock. Valid values: 0 to 65,535.
            StrictGrant (bool): If selected, server will not grant values that are above maximum offered values.
            SyncDropRate (number): Percentage rate of the dropped Sync messages.
            SyncReceiptTimeout (number): Sync Receipt Timeout in seconds.
            TimeSource (str): Time source for the PTP device.
            TimestampOffset (number): Timestamp offset.
            TimestampOffsetVariation (number): Timestamp offset variation.
            TxCalibration (number): The amount of time (in ns) that the Transmit side timestamp needs to be offset to allow for error.
            UseAlternateMasterFlag (bool): Select this check box to set the Alternate Master flag in all Announce and Sync messages.
            UseClockIdentity (bool): Use the ClockIdentity configured below.

        Returns:
            self: This instance with matching ptpRangeOverMac data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of ptpRangeOverMac data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the ptpRangeOverMac data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self):
        """Executes the apply operation on the server.

        Apply changes for on the fly configuration support.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('apply', payload=payload, response_object=None)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)

    def PtpChangeDropSignalParams(self, *args, **kwargs):
        """Executes the ptpChangeDropSignalParams operation on the server.

        Change Drop Signal Parameters

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        ptpChangeDropSignalParams(Arg2:bool, Arg3:bool, Arg4:bool)
            Args:
                args[0] is Arg2 (bool): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
                args[1] is Arg3 (bool): Drop any Signal Request received on a master side that contains one Announce TLV.
                args[2] is Arg4 (bool): Drop any Signal Request received on a master side that contains one Sync TLV.

        ptpChangeDropSignalParams(Arg2:bool, Arg3:bool, Arg4:bool, Arg5:enum)
            Args:
                args[0] is Arg2 (bool): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
                args[1] is Arg3 (bool): Drop any Signal Request received on a master side that contains one Announce TLV.
                args[2] is Arg4 (bool): Drop any Signal Request received on a master side that contains one Sync TLV.
                args[3] is Arg5 (str(async|sync)): Drop any Signal Request received on a master side that contains one DelayResp TLV.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpChangeDropSignalParams', payload=payload, response_object=None)

    def PtpChangeMiscParams(self, *args, **kwargs):
        """Executes the ptpChangeMiscParams operation on the server.

        Change Misc Parameters

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        ptpChangeMiscParams(Arg2:number, Arg3:number)
            Args:
                args[0] is Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
                args[1] is Arg3 (number): PTP Domain.

        ptpChangeMiscParams(Arg2:number, Arg3:number, Arg4:enum)
            Args:
                args[0] is Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
                args[1] is Arg3 (number): PTP Domain.
                args[2] is Arg4 (str(async|sync)): The number of announceInterval that has to pass without receipt of an Announce message.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpChangeMiscParams', payload=payload, response_object=None)

    def PtpChangeNegativeTesting(self, *args, **kwargs):
        """Executes the ptpChangeNegativeTesting operation on the server.

        Change Negative Testing Parameters

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        ptpChangeNegativeTesting(Arg2:number, Arg3:number, Arg4:number, Arg5:number, Arg6:number, Arg7:number, Arg8:number, Arg9:number, Arg10:number)
            Args:
                args[0] is Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
                args[1] is Arg3 (number): Additional delay introduced in the Follow_Up message timestamp (nanoseconds).
                args[2] is Arg4 (number): Percentage rate of the Follow_Up messages in which the delay is introduced.
                args[3] is Arg5 (number): Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
                args[4] is Arg6 (number): Percentage rate of the Delay_Resp messages in which the delay is introduced.
                args[5] is Arg7 (number): Percentage rate of the dropped Announce messages.
                args[6] is Arg8 (number): Percentage rate of the dropped Sync messages.
                args[7] is Arg9 (number): Percentage rate of the dropped Follow_Up messages.
                args[8] is Arg10 (number): Percentage rate of the dropped Delay_Resp messages.

        ptpChangeNegativeTesting(Arg2:number, Arg3:number, Arg4:number, Arg5:number, Arg6:number, Arg7:number, Arg8:number, Arg9:number, Arg10:number, Arg11:enum)
            Args:
                args[0] is Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]
                args[1] is Arg3 (number): Additional delay introduced in the Follow_Up message timestamp (nanoseconds).
                args[2] is Arg4 (number): Percentage rate of the Follow_Up messages in which the delay is introduced.
                args[3] is Arg5 (number): Additional delay introduced in the Delay_Resp message timestamp (nanoseconds).
                args[4] is Arg6 (number): Percentage rate of the Delay_Resp messages in which the delay is introduced.
                args[5] is Arg7 (number): Percentage rate of the dropped Announce messages.
                args[6] is Arg8 (number): Percentage rate of the dropped Sync messages.
                args[7] is Arg9 (number): Percentage rate of the dropped Follow_Up messages.
                args[8] is Arg10 (number): Percentage rate of the dropped Delay_Resp messages.
                args[9] is Arg11 (str(async|sync)): Percentage rate of the bad crc Follow_Up messages.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpChangeNegativeTesting', payload=payload, response_object=None)

    def PtpConfigure(self):
        """Executes the ptpConfigure operation on the server.

        Configure PTP protocol on selected ranges.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('ptpConfigure', payload=payload, response_object=None)

    def PtpPause(self):
        """Executes the ptpPause operation on the server.

        Pause negotiation of PTP for selected plugins and ranges

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('ptpPause', payload=payload, response_object=None)

    def PtpResume(self):
        """Executes the ptpResume operation on the server.

        Resume previously paused negotiation of PTP for selected plugins and ranges

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('ptpResume', payload=payload, response_object=None)

    def PtpStart(self, *args, **kwargs):
        """Executes the ptpStart operation on the server.

        Negotiate PTP for selected plugins and ranges

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        ptpStart()

        ptpStart(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpStart', payload=payload, response_object=None)

    def PtpStop(self, *args, **kwargs):
        """Executes the ptpStop operation on the server.

        Release PTP for selected plugins and ranges

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        ptpStop()

        ptpStop(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ip/ptp,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ip/ptp,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/atm/ipEndpoint/ptp,/vport/protocolStack/atm/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/dcbxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ip/ptp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ptp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ip/ptp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ipEndpoint/ptp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverIp,/vport/protocolStack/ethernet/ipEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/pppoxEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernet/ptp,/vport/protocolStack/ethernet/vepaEndpoint/range/ptpRangeOverMac,/vport/protocolStack/ethernetEndpoint/ptp,/vport/protocolStack/ethernetEndpoint/range/ptpRangeOverMac]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ptpStop', payload=payload, response_object=None)
