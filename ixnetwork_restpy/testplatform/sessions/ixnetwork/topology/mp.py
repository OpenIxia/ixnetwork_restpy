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


class Mp(Base):
    """MP exposing network configuration
    The Mp class encapsulates a required mp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'mp'

    def __init__(self, parent):
        super(Mp, self).__init__(parent)

    @property
    def Active(self):
        """Activate/Deactivate Configuration

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('active')

    @property
    def AisEnableUnicastMac(self):
        """Enable the unicast MAC address of the remote MEP

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('aisEnableUnicastMac')

    @property
    def AisInterval(self):
        """AIS Interval

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('aisInterval')

    @property
    def AisMode(self):
        """AIS Mode (Auto Update)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('aisMode')

    @property
    def AisPriority(self):
        """AIS Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('aisPriority')

    @property
    def AisUnicastMac(self):
        """The MAC address of the remote MEP.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('aisUnicastMac')

    @property
    def AutoDmTimeout(self):
        """Auto DM Timeout (sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoDmTimeout')

    @property
    def AutoDmTimer(self):
        """Auto DM Timer (sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoDmTimer')

    @property
    def AutoLbIteration(self):
        """Auto LB Iteration

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoLbIteration')

    @property
    def AutoLbTimeoutInSec(self):
        """Auto LB Timeout (sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoLbTimeoutInSec')

    @property
    def AutoLbTimerInSec(self):
        """Auto LB Timer (sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoLbTimerInSec')

    @property
    def AutoLmIteration(self):
        """Auto LM Iteration

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoLmIteration')

    @property
    def AutoLmTimeout(self):
        """Auto LM Timeout (msec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoLmTimeout')

    @property
    def AutoLmTimer(self):
        """Auto LM Timer (msec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoLmTimer')

    @property
    def AutoLtIteration(self):
        """Auto LT Iteration

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoLtIteration')

    @property
    def AutoLtTimeoutInSec(self):
        """Auto LT Timeout (sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoLtTimeoutInSec')

    @property
    def AutoLtTimerInSec(self):
        """Auto LT Timer (sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoLtTimerInSec')

    @property
    def AutodmIteration(self):
        """Auto DM Iteration

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autodmIteration')

    @property
    def CVlanId(self):
        """C-VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanId')

    @property
    def CVlanPriority(self):
        """C-VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanPriority')

    @property
    def CVlanTpid(self):
        """C-VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanTpid')

    @property
    def CciInterval(self):
        """CCI Interval

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cciInterval')

    @property
    def CcmLmmTxFcf(self):
        """CCM/LMM TxFCf

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ccmLmmTxFcf')

    @property
    def CcmLmmTxFcfStepPer100mSec(self):
        """CCM/LMM TxFCf Step/100 msec

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ccmLmmTxFcfStepPer100mSec')

    @property
    def CcmPriority(self):
        """CCM Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ccmPriority')

    @property
    def CcmRxFcb(self):
        """CCM RxFCb

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ccmRxFcb')

    @property
    def CcmRxFcbStepPer100mSec(self):
        """CCM RxFCb Step/100 msec

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ccmRxFcbStepPer100mSec')

    @property
    def ChassisId(self):
        """Chassis ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('chassisId')

    @property
    def ChassisIdLength(self):
        """Chassis ID Length

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('chassisIdLength')

    @property
    def ChassisIdSubType(self):
        """Chassis ID SubType

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('chassisIdSubType')

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def DataTlvLength(self):
        """Data TLV Length

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dataTlvLength')

    @property
    def DataTlvValue(self):
        """Data TLV Value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dataTlvValue')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def DmAllRemoteMeps(self):
        """DM All Remote MEPS

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dmAllRemoteMeps')

    @property
    def DmDestinationMacAddress(self):
        """DM Destination MAC Address

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dmDestinationMacAddress')

    @property
    def DmMethod(self):
        """DM Method

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dmMethod')

    @property
    def DmPriority(self):
        """DM Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dmPriority')

    @property
    def EnableAisRx(self):
        """Enable AIS Rx (Auto Update)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableAisRx')

    @property
    def EnableAutoDm(self):
        """Enable Auto DM

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableAutoDm')

    @property
    def EnableAutoLb(self):
        """Enable Auto LB

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableAutoLb')

    @property
    def EnableAutoLm(self):
        """Enable Auto LM

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableAutoLm')

    @property
    def EnableAutoLt(self):
        """Enable Auto LT

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableAutoLt')

    @property
    def EnableDataTlv(self):
        """Enable Data TLV

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableDataTlv')

    @property
    def EnableInterfaceStatusTlv(self):
        """Enable Interface Status TLV

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableInterfaceStatusTlv')

    @property
    def EnableLckRx(self):
        """Enable LCK Rx (Auto Update)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableLckRx')

    @property
    def EnableLmCounterUpdate(self):
        """Enable LM Counter Update

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableLmCounterUpdate')

    @property
    def EnableOrganizationSpecificTlv(self):
        """Enable Organization Specific TLV

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableOrganizationSpecificTlv')

    @property
    def EnablePortStatusTlv(self):
        """Enable Port Status TLV

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enablePortStatusTlv')

    @property
    def EnableSenderIdTlv(self):
        """Enable Sender ID TLV

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableSenderIdTlv')

    @property
    def EnableTstRx(self):
        """Enable TST Rx (Auto Update)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableTstRx')

    @property
    def EnableVlan(self):
        """Enable VLAN

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableVlan')

    @property
    def IncludeTLVinCCM(self):
        """Include Custom TLV in CCM

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeTLVinCCM')

    @property
    def IncludeTLVinLBM(self):
        """Include Custom TLV in LBM

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeTLVinLBM')

    @property
    def IncludeTLVinLBR(self):
        """Include Custom TLV in LBR

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeTLVinLBR')

    @property
    def IncludeTLVinLMM(self):
        """Include Custom TLV in LMM

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeTLVinLMM')

    @property
    def IncludeTLVinLMR(self):
        """Include Custom TLV in LMR

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeTLVinLMR')

    @property
    def IncludeTLVinLTM(self):
        """Include Custom TLV in LTM

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeTLVinLTM')

    @property
    def IncludeTLVinLTR(self):
        """Include Custom TLV in LTR

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeTLVinLTR')

    @property
    def InterRemoteMepRxIncrementStep(self):
        """Inter Remote MEP Rx Increment Step

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('interRemoteMepRxIncrementStep')

    @property
    def InterRemoteMepTxIncrementStep(self):
        """Inter Remote MEP Tx Increment Step

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('interRemoteMepTxIncrementStep')

    @property
    def LbAllRemoteMeps(self):
        """LB All Remote MEPS

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lbAllRemoteMeps')

    @property
    def LbDestinationMacAddress(self):
        """LB Destination MAC Address

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lbDestinationMacAddress')

    @property
    def LbmPriority(self):
        """LBM Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lbmPriority')

    @property
    def LckEnableUnicastMac(self):
        """LCK Enable Unicast MAC

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lckEnableUnicastMac')

    @property
    def LckInterval(self):
        """LCK Interval

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lckInterval')

    @property
    def LckMode(self):
        """LCK Mode (Auto Update)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lckMode')

    @property
    def LckPriority(self):
        """LCK Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lckPriority')

    @property
    def LckSupportAisGeneration(self):
        """LCK Support AIS Generation

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lckSupportAisGeneration')

    @property
    def LckUnicastMac(self):
        """LCK Unicast MAC

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lckUnicastMac')

    @property
    def LmAllRemoteMeps(self):
        """LM All Remote MEPS

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lmAllRemoteMeps')

    @property
    def LmDestinationMacAddress(self):
        """LM Destination MAC Address

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lmDestinationMacAddress')

    @property
    def LmMethodType(self):
        """LM Method

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lmMethodType')

    @property
    def LmmPriority(self):
        """LMM Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lmmPriority')

    @property
    def LmrPriority(self):
        """LMR Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lmrPriority')

    @property
    def LmrRxFcf(self):
        """LMR RxFCf

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lmrRxFcf')

    @property
    def LmrRxFcfStepPer100mSec(self):
        """LMR RxFCf Step/100 msec

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lmrRxFcfStepPer100mSec')

    @property
    def LmrTxFcb(self):
        """LMR TxFCb (CCM/LLM TxFCf)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lmrTxFcb')

    @property
    def LmrTxFcbStepPer100mSec(self):
        """LMR TxFCb Step/100 msec (CCM/LMM TxFCf Step / 100 msec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lmrTxFcbStepPer100mSec')

    @property
    def LtAllRemoteMeps(self):
        """LT All Remote MEPS

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ltAllRemoteMeps')

    @property
    def LtDestinationMacAddress(self):
        """LT Destination MAC Address

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ltDestinationMacAddress')

    @property
    def LtmPriority(self):
        """LTM Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ltmPriority')

    @property
    def MacAddress(self):
        """MAC Address

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('macAddress')

    @property
    def ManagementAddress(self):
        """Management Address

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('managementAddress')

    @property
    def ManagementAddressDomain(self):
        """Management Address Domain

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('managementAddressDomain')

    @property
    def ManagementAddressDomainLength(self):
        """Management Address Domain Length

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('managementAddressDomainLength')

    @property
    def ManagementAddressLength(self):
        """Management Address Length

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('managementAddressLength')

    @property
    def MdMegLevel(self):
        """MD/MEG Level

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mdMegLevel')

    @property
    def MdMegLevelIndex(self):
        """MD/MEG Level Index

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mdMegLevelIndex')

    @property
    def MegIdFormat(self):
        """MEG ID Format

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('megIdFormat')

    @property
    def MepId(self):
        """MP ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mepId')

    @property
    def MpIndex(self):
        """MP Index

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mpIndex')

    @property
    def Name(self):
        """Name of NGPF element, guaranteed to be unique in Scenario

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def OrganizationSpecificTlvLength(self):
        """Organization Specific TLV Length

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('organizationSpecificTlvLength')

    @property
    def OverrideVlanPriority(self):
        """Override VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('overrideVlanPriority')

    @property
    def Rdi(self):
        """RDI (Auto Update/On/Off)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('rdi')

    @property
    def SVlanId(self):
        """S-VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanId')

    @property
    def SVlanPriority(self):
        """S-VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanPriority')

    @property
    def SVlanTpid(self):
        """S-VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanTpid')

    @property
    def ShortMaName(self):
        """Short MA Name

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('shortMaName')

    @property
    def ShortMaNameFormat(self):
        """Short MA Name Format

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('shortMaNameFormat')

    @property
    def TstEnableUnicastMac(self):
        """TST Enable Unicast MAC

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstEnableUnicastMac')

    @property
    def TstIncrementPacketLength(self):
        """TST Increment Packet Length (Auto Update)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstIncrementPacketLength')

    @property
    def TstInitialPatternValue(self):
        """TST Initial Pattern Value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstInitialPatternValue')

    @property
    def TstInterval(self):
        """TST Interval (ms)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstInterval')

    @property
    def TstMode(self):
        """TST Mode (Auto Update)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstMode')

    @property
    def TstOverwriteSequenceNumber(self):
        """TST Overwrite Sequence Number (Auto Update)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstOverwriteSequenceNumber')

    @property
    def TstPacketLength(self):
        """TST Packet Length

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstPacketLength')

    @property
    def TstPacketLengthStep(self):
        """TST Increment Packet Length Step

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstPacketLengthStep')

    @property
    def TstPatternType(self):
        """TST Pattern Type

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstPatternType')

    @property
    def TstPriority(self):
        """TST Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstPriority')

    @property
    def TstSequenceNumber(self):
        """TST Sequence Number

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstSequenceNumber')

    @property
    def TstTestType(self):
        """TST Test Type (Auto Update)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstTestType')

    @property
    def TstUnicastMac(self):
        """TST Unicast MAC

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tstUnicastMac')

    @property
    def Type(self):
        """Type

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('type')

    @property
    def VlanId(self):
        """VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanId')

    @property
    def VlanPriority(self):
        """VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanPriority')

    @property
    def VlanStacking(self):
        """VLAN Stacking

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanStacking')

    @property
    def VlanTpid(self):
        """VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanTpid')

    def update(self, Name=None):
        """Updates a child instance of mp on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def get_device_ids(self, PortNames=None, Active=None, AisEnableUnicastMac=None, AisInterval=None, AisMode=None, AisPriority=None, AisUnicastMac=None, AutoDmTimeout=None, AutoDmTimer=None, AutoLbIteration=None, AutoLbTimeoutInSec=None, AutoLbTimerInSec=None, AutoLmIteration=None, AutoLmTimeout=None, AutoLmTimer=None, AutoLtIteration=None, AutoLtTimeoutInSec=None, AutoLtTimerInSec=None, AutodmIteration=None, CVlanId=None, CVlanPriority=None, CVlanTpid=None, CciInterval=None, CcmLmmTxFcf=None, CcmLmmTxFcfStepPer100mSec=None, CcmPriority=None, CcmRxFcb=None, CcmRxFcbStepPer100mSec=None, ChassisId=None, ChassisIdLength=None, ChassisIdSubType=None, DataTlvLength=None, DataTlvValue=None, DmAllRemoteMeps=None, DmDestinationMacAddress=None, DmMethod=None, DmPriority=None, EnableAisRx=None, EnableAutoDm=None, EnableAutoLb=None, EnableAutoLm=None, EnableAutoLt=None, EnableDataTlv=None, EnableInterfaceStatusTlv=None, EnableLckRx=None, EnableLmCounterUpdate=None, EnableOrganizationSpecificTlv=None, EnablePortStatusTlv=None, EnableSenderIdTlv=None, EnableTstRx=None, EnableVlan=None, IncludeTLVinCCM=None, IncludeTLVinLBM=None, IncludeTLVinLBR=None, IncludeTLVinLMM=None, IncludeTLVinLMR=None, IncludeTLVinLTM=None, IncludeTLVinLTR=None, InterRemoteMepRxIncrementStep=None, InterRemoteMepTxIncrementStep=None, LbAllRemoteMeps=None, LbDestinationMacAddress=None, LbmPriority=None, LckEnableUnicastMac=None, LckInterval=None, LckMode=None, LckPriority=None, LckSupportAisGeneration=None, LckUnicastMac=None, LmAllRemoteMeps=None, LmDestinationMacAddress=None, LmMethodType=None, LmmPriority=None, LmrPriority=None, LmrRxFcf=None, LmrRxFcfStepPer100mSec=None, LmrTxFcb=None, LmrTxFcbStepPer100mSec=None, LtAllRemoteMeps=None, LtDestinationMacAddress=None, LtmPriority=None, MacAddress=None, ManagementAddress=None, ManagementAddressDomain=None, ManagementAddressDomainLength=None, ManagementAddressLength=None, MdMegLevel=None, MdMegLevelIndex=None, MegIdFormat=None, MepId=None, MpIndex=None, OrganizationSpecificTlvLength=None, OverrideVlanPriority=None, Rdi=None, SVlanId=None, SVlanPriority=None, SVlanTpid=None, ShortMaName=None, ShortMaNameFormat=None, TstEnableUnicastMac=None, TstIncrementPacketLength=None, TstInitialPatternValue=None, TstInterval=None, TstMode=None, TstOverwriteSequenceNumber=None, TstPacketLength=None, TstPacketLengthStep=None, TstPatternType=None, TstPriority=None, TstSequenceNumber=None, TstTestType=None, TstUnicastMac=None, Type=None, VlanId=None, VlanPriority=None, VlanStacking=None, VlanTpid=None):
        """Base class infrastructure that gets a list of mp device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            Active (str): optional regex of active
            AisEnableUnicastMac (str): optional regex of aisEnableUnicastMac
            AisInterval (str): optional regex of aisInterval
            AisMode (str): optional regex of aisMode
            AisPriority (str): optional regex of aisPriority
            AisUnicastMac (str): optional regex of aisUnicastMac
            AutoDmTimeout (str): optional regex of autoDmTimeout
            AutoDmTimer (str): optional regex of autoDmTimer
            AutoLbIteration (str): optional regex of autoLbIteration
            AutoLbTimeoutInSec (str): optional regex of autoLbTimeoutInSec
            AutoLbTimerInSec (str): optional regex of autoLbTimerInSec
            AutoLmIteration (str): optional regex of autoLmIteration
            AutoLmTimeout (str): optional regex of autoLmTimeout
            AutoLmTimer (str): optional regex of autoLmTimer
            AutoLtIteration (str): optional regex of autoLtIteration
            AutoLtTimeoutInSec (str): optional regex of autoLtTimeoutInSec
            AutoLtTimerInSec (str): optional regex of autoLtTimerInSec
            AutodmIteration (str): optional regex of autodmIteration
            CVlanId (str): optional regex of cVlanId
            CVlanPriority (str): optional regex of cVlanPriority
            CVlanTpid (str): optional regex of cVlanTpid
            CciInterval (str): optional regex of cciInterval
            CcmLmmTxFcf (str): optional regex of ccmLmmTxFcf
            CcmLmmTxFcfStepPer100mSec (str): optional regex of ccmLmmTxFcfStepPer100mSec
            CcmPriority (str): optional regex of ccmPriority
            CcmRxFcb (str): optional regex of ccmRxFcb
            CcmRxFcbStepPer100mSec (str): optional regex of ccmRxFcbStepPer100mSec
            ChassisId (str): optional regex of chassisId
            ChassisIdLength (str): optional regex of chassisIdLength
            ChassisIdSubType (str): optional regex of chassisIdSubType
            DataTlvLength (str): optional regex of dataTlvLength
            DataTlvValue (str): optional regex of dataTlvValue
            DmAllRemoteMeps (str): optional regex of dmAllRemoteMeps
            DmDestinationMacAddress (str): optional regex of dmDestinationMacAddress
            DmMethod (str): optional regex of dmMethod
            DmPriority (str): optional regex of dmPriority
            EnableAisRx (str): optional regex of enableAisRx
            EnableAutoDm (str): optional regex of enableAutoDm
            EnableAutoLb (str): optional regex of enableAutoLb
            EnableAutoLm (str): optional regex of enableAutoLm
            EnableAutoLt (str): optional regex of enableAutoLt
            EnableDataTlv (str): optional regex of enableDataTlv
            EnableInterfaceStatusTlv (str): optional regex of enableInterfaceStatusTlv
            EnableLckRx (str): optional regex of enableLckRx
            EnableLmCounterUpdate (str): optional regex of enableLmCounterUpdate
            EnableOrganizationSpecificTlv (str): optional regex of enableOrganizationSpecificTlv
            EnablePortStatusTlv (str): optional regex of enablePortStatusTlv
            EnableSenderIdTlv (str): optional regex of enableSenderIdTlv
            EnableTstRx (str): optional regex of enableTstRx
            EnableVlan (str): optional regex of enableVlan
            IncludeTLVinCCM (str): optional regex of includeTLVinCCM
            IncludeTLVinLBM (str): optional regex of includeTLVinLBM
            IncludeTLVinLBR (str): optional regex of includeTLVinLBR
            IncludeTLVinLMM (str): optional regex of includeTLVinLMM
            IncludeTLVinLMR (str): optional regex of includeTLVinLMR
            IncludeTLVinLTM (str): optional regex of includeTLVinLTM
            IncludeTLVinLTR (str): optional regex of includeTLVinLTR
            InterRemoteMepRxIncrementStep (str): optional regex of interRemoteMepRxIncrementStep
            InterRemoteMepTxIncrementStep (str): optional regex of interRemoteMepTxIncrementStep
            LbAllRemoteMeps (str): optional regex of lbAllRemoteMeps
            LbDestinationMacAddress (str): optional regex of lbDestinationMacAddress
            LbmPriority (str): optional regex of lbmPriority
            LckEnableUnicastMac (str): optional regex of lckEnableUnicastMac
            LckInterval (str): optional regex of lckInterval
            LckMode (str): optional regex of lckMode
            LckPriority (str): optional regex of lckPriority
            LckSupportAisGeneration (str): optional regex of lckSupportAisGeneration
            LckUnicastMac (str): optional regex of lckUnicastMac
            LmAllRemoteMeps (str): optional regex of lmAllRemoteMeps
            LmDestinationMacAddress (str): optional regex of lmDestinationMacAddress
            LmMethodType (str): optional regex of lmMethodType
            LmmPriority (str): optional regex of lmmPriority
            LmrPriority (str): optional regex of lmrPriority
            LmrRxFcf (str): optional regex of lmrRxFcf
            LmrRxFcfStepPer100mSec (str): optional regex of lmrRxFcfStepPer100mSec
            LmrTxFcb (str): optional regex of lmrTxFcb
            LmrTxFcbStepPer100mSec (str): optional regex of lmrTxFcbStepPer100mSec
            LtAllRemoteMeps (str): optional regex of ltAllRemoteMeps
            LtDestinationMacAddress (str): optional regex of ltDestinationMacAddress
            LtmPriority (str): optional regex of ltmPriority
            MacAddress (str): optional regex of macAddress
            ManagementAddress (str): optional regex of managementAddress
            ManagementAddressDomain (str): optional regex of managementAddressDomain
            ManagementAddressDomainLength (str): optional regex of managementAddressDomainLength
            ManagementAddressLength (str): optional regex of managementAddressLength
            MdMegLevel (str): optional regex of mdMegLevel
            MdMegLevelIndex (str): optional regex of mdMegLevelIndex
            MegIdFormat (str): optional regex of megIdFormat
            MepId (str): optional regex of mepId
            MpIndex (str): optional regex of mpIndex
            OrganizationSpecificTlvLength (str): optional regex of organizationSpecificTlvLength
            OverrideVlanPriority (str): optional regex of overrideVlanPriority
            Rdi (str): optional regex of rdi
            SVlanId (str): optional regex of sVlanId
            SVlanPriority (str): optional regex of sVlanPriority
            SVlanTpid (str): optional regex of sVlanTpid
            ShortMaName (str): optional regex of shortMaName
            ShortMaNameFormat (str): optional regex of shortMaNameFormat
            TstEnableUnicastMac (str): optional regex of tstEnableUnicastMac
            TstIncrementPacketLength (str): optional regex of tstIncrementPacketLength
            TstInitialPatternValue (str): optional regex of tstInitialPatternValue
            TstInterval (str): optional regex of tstInterval
            TstMode (str): optional regex of tstMode
            TstOverwriteSequenceNumber (str): optional regex of tstOverwriteSequenceNumber
            TstPacketLength (str): optional regex of tstPacketLength
            TstPacketLengthStep (str): optional regex of tstPacketLengthStep
            TstPatternType (str): optional regex of tstPatternType
            TstPriority (str): optional regex of tstPriority
            TstSequenceNumber (str): optional regex of tstSequenceNumber
            TstTestType (str): optional regex of tstTestType
            TstUnicastMac (str): optional regex of tstUnicastMac
            Type (str): optional regex of type
            VlanId (str): optional regex of vlanId
            VlanPriority (str): optional regex of vlanPriority
            VlanStacking (str): optional regex of vlanStacking
            VlanTpid (str): optional regex of vlanTpid

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def ConnectMPToIxiaPort(self, *args, **kwargs):
        """Executes the connectMPToIxiaPort operation on the server.

        Please provide a proper help text here.

        connectMPToIxiaPort(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('connectMPToIxiaPort', payload=payload, response_object=None)
