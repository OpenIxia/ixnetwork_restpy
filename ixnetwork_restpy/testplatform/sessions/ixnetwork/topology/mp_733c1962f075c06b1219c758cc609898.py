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
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AisEnableUnicastMac': 'aisEnableUnicastMac',
        'AisInterval': 'aisInterval',
        'AisMode': 'aisMode',
        'AisPriority': 'aisPriority',
        'AisUnicastMac': 'aisUnicastMac',
        'AutoDmTimeout': 'autoDmTimeout',
        'AutoDmTimer': 'autoDmTimer',
        'AutoLbIteration': 'autoLbIteration',
        'AutoLbTimeoutInSec': 'autoLbTimeoutInSec',
        'AutoLbTimerInSec': 'autoLbTimerInSec',
        'AutoLmIteration': 'autoLmIteration',
        'AutoLmTimeout': 'autoLmTimeout',
        'AutoLmTimer': 'autoLmTimer',
        'AutoLtIteration': 'autoLtIteration',
        'AutoLtTimeoutInSec': 'autoLtTimeoutInSec',
        'AutoLtTimerInSec': 'autoLtTimerInSec',
        'AutodmIteration': 'autodmIteration',
        'CVlanId': 'cVlanId',
        'CVlanPriority': 'cVlanPriority',
        'CVlanTpid': 'cVlanTpid',
        'CciInterval': 'cciInterval',
        'CcmLmmTxFcf': 'ccmLmmTxFcf',
        'CcmLmmTxFcfStepPer100mSec': 'ccmLmmTxFcfStepPer100mSec',
        'CcmPriority': 'ccmPriority',
        'CcmRxFcb': 'ccmRxFcb',
        'CcmRxFcbStepPer100mSec': 'ccmRxFcbStepPer100mSec',
        'ChassisId': 'chassisId',
        'ChassisIdLength': 'chassisIdLength',
        'ChassisIdSubType': 'chassisIdSubType',
        'Count': 'count',
        'DataTlvLength': 'dataTlvLength',
        'DataTlvValue': 'dataTlvValue',
        'DescriptiveName': 'descriptiveName',
        'DmAllRemoteMeps': 'dmAllRemoteMeps',
        'DmDestinationMacAddress': 'dmDestinationMacAddress',
        'DmMethod': 'dmMethod',
        'DmPriority': 'dmPriority',
        'EnableAisRx': 'enableAisRx',
        'EnableAutoDm': 'enableAutoDm',
        'EnableAutoLb': 'enableAutoLb',
        'EnableAutoLm': 'enableAutoLm',
        'EnableAutoLt': 'enableAutoLt',
        'EnableDataTlv': 'enableDataTlv',
        'EnableInterfaceStatusTlv': 'enableInterfaceStatusTlv',
        'EnableLckRx': 'enableLckRx',
        'EnableLmCounterUpdate': 'enableLmCounterUpdate',
        'EnableOrganizationSpecificTlv': 'enableOrganizationSpecificTlv',
        'EnablePortStatusTlv': 'enablePortStatusTlv',
        'EnableSenderIdTlv': 'enableSenderIdTlv',
        'EnableTstRx': 'enableTstRx',
        'EnableVlan': 'enableVlan',
        'IncludeTLVinCCM': 'includeTLVinCCM',
        'IncludeTLVinLBM': 'includeTLVinLBM',
        'IncludeTLVinLBR': 'includeTLVinLBR',
        'IncludeTLVinLMM': 'includeTLVinLMM',
        'IncludeTLVinLMR': 'includeTLVinLMR',
        'IncludeTLVinLTM': 'includeTLVinLTM',
        'IncludeTLVinLTR': 'includeTLVinLTR',
        'InterRemoteMepRxIncrementStep': 'interRemoteMepRxIncrementStep',
        'InterRemoteMepTxIncrementStep': 'interRemoteMepTxIncrementStep',
        'LbAllRemoteMeps': 'lbAllRemoteMeps',
        'LbDestinationMacAddress': 'lbDestinationMacAddress',
        'LbmPriority': 'lbmPriority',
        'LckEnableUnicastMac': 'lckEnableUnicastMac',
        'LckInterval': 'lckInterval',
        'LckMode': 'lckMode',
        'LckPriority': 'lckPriority',
        'LckSupportAisGeneration': 'lckSupportAisGeneration',
        'LckUnicastMac': 'lckUnicastMac',
        'LmAllRemoteMeps': 'lmAllRemoteMeps',
        'LmDestinationMacAddress': 'lmDestinationMacAddress',
        'LmMethodType': 'lmMethodType',
        'LmmPriority': 'lmmPriority',
        'LmrPriority': 'lmrPriority',
        'LmrRxFcf': 'lmrRxFcf',
        'LmrRxFcfStepPer100mSec': 'lmrRxFcfStepPer100mSec',
        'LmrTxFcb': 'lmrTxFcb',
        'LmrTxFcbStepPer100mSec': 'lmrTxFcbStepPer100mSec',
        'LtAllRemoteMeps': 'ltAllRemoteMeps',
        'LtDestinationMacAddress': 'ltDestinationMacAddress',
        'LtmPriority': 'ltmPriority',
        'MacAddress': 'macAddress',
        'ManagementAddress': 'managementAddress',
        'ManagementAddressDomain': 'managementAddressDomain',
        'ManagementAddressDomainLength': 'managementAddressDomainLength',
        'ManagementAddressLength': 'managementAddressLength',
        'MdMegLevel': 'mdMegLevel',
        'MdMegLevelIndex': 'mdMegLevelIndex',
        'MegIdFormat': 'megIdFormat',
        'MepId': 'mepId',
        'MpIndex': 'mpIndex',
        'Name': 'name',
        'OrganizationSpecificTlvLength': 'organizationSpecificTlvLength',
        'OverrideVlanPriority': 'overrideVlanPriority',
        'Rdi': 'rdi',
        'SVlanId': 'sVlanId',
        'SVlanPriority': 'sVlanPriority',
        'SVlanTpid': 'sVlanTpid',
        'ShortMaName': 'shortMaName',
        'ShortMaNameFormat': 'shortMaNameFormat',
        'TstEnableUnicastMac': 'tstEnableUnicastMac',
        'TstIncrementPacketLength': 'tstIncrementPacketLength',
        'TstInitialPatternValue': 'tstInitialPatternValue',
        'TstInterval': 'tstInterval',
        'TstMode': 'tstMode',
        'TstOverwriteSequenceNumber': 'tstOverwriteSequenceNumber',
        'TstPacketLength': 'tstPacketLength',
        'TstPacketLengthStep': 'tstPacketLengthStep',
        'TstPatternType': 'tstPatternType',
        'TstPriority': 'tstPriority',
        'TstSequenceNumber': 'tstSequenceNumber',
        'TstTestType': 'tstTestType',
        'TstUnicastMac': 'tstUnicastMac',
        'Type': 'type',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
        'VlanStacking': 'vlanStacking',
        'VlanTpid': 'vlanTpid',
    }

    def __init__(self, parent):
        super(Mp, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AisEnableUnicastMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable the unicast MAC address of the remote MEP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AisEnableUnicastMac']))

    @property
    def AisInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AIS Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AisInterval']))

    @property
    def AisMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AIS Mode (Auto Update)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AisMode']))

    @property
    def AisPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AIS Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AisPriority']))

    @property
    def AisUnicastMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The MAC address of the remote MEP.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AisUnicastMac']))

    @property
    def AutoDmTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto DM Timeout (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoDmTimeout']))

    @property
    def AutoDmTimer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto DM Timer (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoDmTimer']))

    @property
    def AutoLbIteration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto LB Iteration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLbIteration']))

    @property
    def AutoLbTimeoutInSec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto LB Timeout (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLbTimeoutInSec']))

    @property
    def AutoLbTimerInSec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto LB Timer (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLbTimerInSec']))

    @property
    def AutoLmIteration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto LM Iteration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLmIteration']))

    @property
    def AutoLmTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto LM Timeout (msec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLmTimeout']))

    @property
    def AutoLmTimer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto LM Timer (msec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLmTimer']))

    @property
    def AutoLtIteration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto LT Iteration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLtIteration']))

    @property
    def AutoLtTimeoutInSec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto LT Timeout (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLtTimeoutInSec']))

    @property
    def AutoLtTimerInSec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto LT Timer (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLtTimerInSec']))

    @property
    def AutodmIteration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto DM Iteration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutodmIteration']))

    @property
    def CVlanId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): C-VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanId']))

    @property
    def CVlanPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): C-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanPriority']))

    @property
    def CVlanTpid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): C-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanTpid']))

    @property
    def CciInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CCI Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CciInterval']))

    @property
    def CcmLmmTxFcf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CCM/LMM TxFCf
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CcmLmmTxFcf']))

    @property
    def CcmLmmTxFcfStepPer100mSec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CCM/LMM TxFCf Step/100 msec
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CcmLmmTxFcfStepPer100mSec']))

    @property
    def CcmPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CCM Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CcmPriority']))

    @property
    def CcmRxFcb(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CCM RxFCb
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CcmRxFcb']))

    @property
    def CcmRxFcbStepPer100mSec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CCM RxFCb Step/100 msec
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CcmRxFcbStepPer100mSec']))

    @property
    def ChassisId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Chassis ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ChassisId']))

    @property
    def ChassisIdLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Chassis ID Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ChassisIdLength']))

    @property
    def ChassisIdSubType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Chassis ID SubType
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ChassisIdSubType']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DataTlvLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Data TLV Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DataTlvLength']))

    @property
    def DataTlvValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Data TLV Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DataTlvValue']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DmAllRemoteMeps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DM All Remote MEPS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DmAllRemoteMeps']))

    @property
    def DmDestinationMacAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DM Destination MAC Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DmDestinationMacAddress']))

    @property
    def DmMethod(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DM Method
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DmMethod']))

    @property
    def DmPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DM Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DmPriority']))

    @property
    def EnableAisRx(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable AIS Rx (Auto Update)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAisRx']))

    @property
    def EnableAutoDm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Auto DM
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAutoDm']))

    @property
    def EnableAutoLb(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Auto LB
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAutoLb']))

    @property
    def EnableAutoLm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Auto LM
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAutoLm']))

    @property
    def EnableAutoLt(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Auto LT
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAutoLt']))

    @property
    def EnableDataTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Data TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableDataTlv']))

    @property
    def EnableInterfaceStatusTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Interface Status TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableInterfaceStatusTlv']))

    @property
    def EnableLckRx(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable LCK Rx (Auto Update)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLckRx']))

    @property
    def EnableLmCounterUpdate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable LM Counter Update
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLmCounterUpdate']))

    @property
    def EnableOrganizationSpecificTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Organization Specific TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOrganizationSpecificTlv']))

    @property
    def EnablePortStatusTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Port Status TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnablePortStatusTlv']))

    @property
    def EnableSenderIdTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Sender ID TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSenderIdTlv']))

    @property
    def EnableTstRx(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable TST Rx (Auto Update)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableTstRx']))

    @property
    def EnableVlan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable VLAN
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableVlan']))

    @property
    def IncludeTLVinCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Custom TLV in CCM
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinCCM']))

    @property
    def IncludeTLVinLBM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Custom TLV in LBM
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinLBM']))

    @property
    def IncludeTLVinLBR(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Custom TLV in LBR
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinLBR']))

    @property
    def IncludeTLVinLMM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Custom TLV in LMM
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinLMM']))

    @property
    def IncludeTLVinLMR(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Custom TLV in LMR
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinLMR']))

    @property
    def IncludeTLVinLTM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Custom TLV in LTM
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinLTM']))

    @property
    def IncludeTLVinLTR(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Custom TLV in LTR
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTLVinLTR']))

    @property
    def InterRemoteMepRxIncrementStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Inter Remote MEP Rx Increment Step
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InterRemoteMepRxIncrementStep']))

    @property
    def InterRemoteMepTxIncrementStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Inter Remote MEP Tx Increment Step
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InterRemoteMepTxIncrementStep']))

    @property
    def LbAllRemoteMeps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LB All Remote MEPS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LbAllRemoteMeps']))

    @property
    def LbDestinationMacAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LB Destination MAC Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LbDestinationMacAddress']))

    @property
    def LbmPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LBM Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LbmPriority']))

    @property
    def LckEnableUnicastMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LCK Enable Unicast MAC
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LckEnableUnicastMac']))

    @property
    def LckInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LCK Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LckInterval']))

    @property
    def LckMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LCK Mode (Auto Update)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LckMode']))

    @property
    def LckPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LCK Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LckPriority']))

    @property
    def LckSupportAisGeneration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LCK Support AIS Generation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LckSupportAisGeneration']))

    @property
    def LckUnicastMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LCK Unicast MAC
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LckUnicastMac']))

    @property
    def LmAllRemoteMeps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LM All Remote MEPS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmAllRemoteMeps']))

    @property
    def LmDestinationMacAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LM Destination MAC Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmDestinationMacAddress']))

    @property
    def LmMethodType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LM Method
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmMethodType']))

    @property
    def LmmPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LMM Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmmPriority']))

    @property
    def LmrPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LMR Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmrPriority']))

    @property
    def LmrRxFcf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LMR RxFCf
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmrRxFcf']))

    @property
    def LmrRxFcfStepPer100mSec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LMR RxFCf Step/100 msec
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmrRxFcfStepPer100mSec']))

    @property
    def LmrTxFcb(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LMR TxFCb (CCM/LLM TxFCf)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmrTxFcb']))

    @property
    def LmrTxFcbStepPer100mSec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LMR TxFCb Step/100 msec (CCM/LMM TxFCf Step / 100 msec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmrTxFcbStepPer100mSec']))

    @property
    def LtAllRemoteMeps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LT All Remote MEPS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LtAllRemoteMeps']))

    @property
    def LtDestinationMacAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LT Destination MAC Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LtDestinationMacAddress']))

    @property
    def LtmPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LTM Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LtmPriority']))

    @property
    def MacAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MAC Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MacAddress']))

    @property
    def ManagementAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Management Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ManagementAddress']))

    @property
    def ManagementAddressDomain(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Management Address Domain
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ManagementAddressDomain']))

    @property
    def ManagementAddressDomainLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Management Address Domain Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ManagementAddressDomainLength']))

    @property
    def ManagementAddressLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Management Address Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ManagementAddressLength']))

    @property
    def MdMegLevel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MD/MEG Level
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MdMegLevel']))

    @property
    def MdMegLevelIndex(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MD/MEG Level Index
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MdMegLevelIndex']))

    @property
    def MegIdFormat(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MEG ID Format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MegIdFormat']))

    @property
    def MepId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MP ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MepId']))

    @property
    def MpIndex(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MP Index
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MpIndex']))

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
    def OrganizationSpecificTlvLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Organization Specific TLV Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OrganizationSpecificTlvLength']))

    @property
    def OverrideVlanPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Override VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OverrideVlanPriority']))

    @property
    def Rdi(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RDI (Auto Update/On/Off)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Rdi']))

    @property
    def SVlanId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S-VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanId']))

    @property
    def SVlanPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanPriority']))

    @property
    def SVlanTpid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanTpid']))

    @property
    def ShortMaName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Short MA Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ShortMaName']))

    @property
    def ShortMaNameFormat(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Short MA Name Format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ShortMaNameFormat']))

    @property
    def TstEnableUnicastMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Enable Unicast MAC
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstEnableUnicastMac']))

    @property
    def TstIncrementPacketLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Increment Packet Length (Auto Update)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstIncrementPacketLength']))

    @property
    def TstInitialPatternValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Initial Pattern Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstInitialPatternValue']))

    @property
    def TstInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstInterval']))

    @property
    def TstMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Mode (Auto Update)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstMode']))

    @property
    def TstOverwriteSequenceNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Overwrite Sequence Number (Auto Update)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstOverwriteSequenceNumber']))

    @property
    def TstPacketLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Packet Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstPacketLength']))

    @property
    def TstPacketLengthStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Increment Packet Length Step
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstPacketLengthStep']))

    @property
    def TstPatternType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Pattern Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstPatternType']))

    @property
    def TstPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstPriority']))

    @property
    def TstSequenceNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Sequence Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstSequenceNumber']))

    @property
    def TstTestType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Test Type (Auto Update)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstTestType']))

    @property
    def TstUnicastMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TST Unicast MAC
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstUnicastMac']))

    @property
    def Type(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def VlanId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanId']))

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanPriority']))

    @property
    def VlanStacking(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VLAN Stacking
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanStacking']))

    @property
    def VlanTpid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanTpid']))

    def update(self, Name=None):
        """Updates mp resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, AisEnableUnicastMac=None, AisInterval=None, AisMode=None, AisPriority=None, AisUnicastMac=None, AutoDmTimeout=None, AutoDmTimer=None, AutoLbIteration=None, AutoLbTimeoutInSec=None, AutoLbTimerInSec=None, AutoLmIteration=None, AutoLmTimeout=None, AutoLmTimer=None, AutoLtIteration=None, AutoLtTimeoutInSec=None, AutoLtTimerInSec=None, AutodmIteration=None, CVlanId=None, CVlanPriority=None, CVlanTpid=None, CciInterval=None, CcmLmmTxFcf=None, CcmLmmTxFcfStepPer100mSec=None, CcmPriority=None, CcmRxFcb=None, CcmRxFcbStepPer100mSec=None, ChassisId=None, ChassisIdLength=None, ChassisIdSubType=None, DataTlvLength=None, DataTlvValue=None, DmAllRemoteMeps=None, DmDestinationMacAddress=None, DmMethod=None, DmPriority=None, EnableAisRx=None, EnableAutoDm=None, EnableAutoLb=None, EnableAutoLm=None, EnableAutoLt=None, EnableDataTlv=None, EnableInterfaceStatusTlv=None, EnableLckRx=None, EnableLmCounterUpdate=None, EnableOrganizationSpecificTlv=None, EnablePortStatusTlv=None, EnableSenderIdTlv=None, EnableTstRx=None, EnableVlan=None, IncludeTLVinCCM=None, IncludeTLVinLBM=None, IncludeTLVinLBR=None, IncludeTLVinLMM=None, IncludeTLVinLMR=None, IncludeTLVinLTM=None, IncludeTLVinLTR=None, InterRemoteMepRxIncrementStep=None, InterRemoteMepTxIncrementStep=None, LbAllRemoteMeps=None, LbDestinationMacAddress=None, LbmPriority=None, LckEnableUnicastMac=None, LckInterval=None, LckMode=None, LckPriority=None, LckSupportAisGeneration=None, LckUnicastMac=None, LmAllRemoteMeps=None, LmDestinationMacAddress=None, LmMethodType=None, LmmPriority=None, LmrPriority=None, LmrRxFcf=None, LmrRxFcfStepPer100mSec=None, LmrTxFcb=None, LmrTxFcbStepPer100mSec=None, LtAllRemoteMeps=None, LtDestinationMacAddress=None, LtmPriority=None, MacAddress=None, ManagementAddress=None, ManagementAddressDomain=None, ManagementAddressDomainLength=None, ManagementAddressLength=None, MdMegLevel=None, MdMegLevelIndex=None, MegIdFormat=None, MepId=None, MpIndex=None, OrganizationSpecificTlvLength=None, OverrideVlanPriority=None, Rdi=None, SVlanId=None, SVlanPriority=None, SVlanTpid=None, ShortMaName=None, ShortMaNameFormat=None, TstEnableUnicastMac=None, TstIncrementPacketLength=None, TstInitialPatternValue=None, TstInterval=None, TstMode=None, TstOverwriteSequenceNumber=None, TstPacketLength=None, TstPacketLengthStep=None, TstPatternType=None, TstPriority=None, TstSequenceNumber=None, TstTestType=None, TstUnicastMac=None, Type=None, VlanId=None, VlanPriority=None, VlanStacking=None, VlanTpid=None):
        """Base class infrastructure that gets a list of mp device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AisEnableUnicastMac (str): optional regex of aisEnableUnicastMac
        - AisInterval (str): optional regex of aisInterval
        - AisMode (str): optional regex of aisMode
        - AisPriority (str): optional regex of aisPriority
        - AisUnicastMac (str): optional regex of aisUnicastMac
        - AutoDmTimeout (str): optional regex of autoDmTimeout
        - AutoDmTimer (str): optional regex of autoDmTimer
        - AutoLbIteration (str): optional regex of autoLbIteration
        - AutoLbTimeoutInSec (str): optional regex of autoLbTimeoutInSec
        - AutoLbTimerInSec (str): optional regex of autoLbTimerInSec
        - AutoLmIteration (str): optional regex of autoLmIteration
        - AutoLmTimeout (str): optional regex of autoLmTimeout
        - AutoLmTimer (str): optional regex of autoLmTimer
        - AutoLtIteration (str): optional regex of autoLtIteration
        - AutoLtTimeoutInSec (str): optional regex of autoLtTimeoutInSec
        - AutoLtTimerInSec (str): optional regex of autoLtTimerInSec
        - AutodmIteration (str): optional regex of autodmIteration
        - CVlanId (str): optional regex of cVlanId
        - CVlanPriority (str): optional regex of cVlanPriority
        - CVlanTpid (str): optional regex of cVlanTpid
        - CciInterval (str): optional regex of cciInterval
        - CcmLmmTxFcf (str): optional regex of ccmLmmTxFcf
        - CcmLmmTxFcfStepPer100mSec (str): optional regex of ccmLmmTxFcfStepPer100mSec
        - CcmPriority (str): optional regex of ccmPriority
        - CcmRxFcb (str): optional regex of ccmRxFcb
        - CcmRxFcbStepPer100mSec (str): optional regex of ccmRxFcbStepPer100mSec
        - ChassisId (str): optional regex of chassisId
        - ChassisIdLength (str): optional regex of chassisIdLength
        - ChassisIdSubType (str): optional regex of chassisIdSubType
        - DataTlvLength (str): optional regex of dataTlvLength
        - DataTlvValue (str): optional regex of dataTlvValue
        - DmAllRemoteMeps (str): optional regex of dmAllRemoteMeps
        - DmDestinationMacAddress (str): optional regex of dmDestinationMacAddress
        - DmMethod (str): optional regex of dmMethod
        - DmPriority (str): optional regex of dmPriority
        - EnableAisRx (str): optional regex of enableAisRx
        - EnableAutoDm (str): optional regex of enableAutoDm
        - EnableAutoLb (str): optional regex of enableAutoLb
        - EnableAutoLm (str): optional regex of enableAutoLm
        - EnableAutoLt (str): optional regex of enableAutoLt
        - EnableDataTlv (str): optional regex of enableDataTlv
        - EnableInterfaceStatusTlv (str): optional regex of enableInterfaceStatusTlv
        - EnableLckRx (str): optional regex of enableLckRx
        - EnableLmCounterUpdate (str): optional regex of enableLmCounterUpdate
        - EnableOrganizationSpecificTlv (str): optional regex of enableOrganizationSpecificTlv
        - EnablePortStatusTlv (str): optional regex of enablePortStatusTlv
        - EnableSenderIdTlv (str): optional regex of enableSenderIdTlv
        - EnableTstRx (str): optional regex of enableTstRx
        - EnableVlan (str): optional regex of enableVlan
        - IncludeTLVinCCM (str): optional regex of includeTLVinCCM
        - IncludeTLVinLBM (str): optional regex of includeTLVinLBM
        - IncludeTLVinLBR (str): optional regex of includeTLVinLBR
        - IncludeTLVinLMM (str): optional regex of includeTLVinLMM
        - IncludeTLVinLMR (str): optional regex of includeTLVinLMR
        - IncludeTLVinLTM (str): optional regex of includeTLVinLTM
        - IncludeTLVinLTR (str): optional regex of includeTLVinLTR
        - InterRemoteMepRxIncrementStep (str): optional regex of interRemoteMepRxIncrementStep
        - InterRemoteMepTxIncrementStep (str): optional regex of interRemoteMepTxIncrementStep
        - LbAllRemoteMeps (str): optional regex of lbAllRemoteMeps
        - LbDestinationMacAddress (str): optional regex of lbDestinationMacAddress
        - LbmPriority (str): optional regex of lbmPriority
        - LckEnableUnicastMac (str): optional regex of lckEnableUnicastMac
        - LckInterval (str): optional regex of lckInterval
        - LckMode (str): optional regex of lckMode
        - LckPriority (str): optional regex of lckPriority
        - LckSupportAisGeneration (str): optional regex of lckSupportAisGeneration
        - LckUnicastMac (str): optional regex of lckUnicastMac
        - LmAllRemoteMeps (str): optional regex of lmAllRemoteMeps
        - LmDestinationMacAddress (str): optional regex of lmDestinationMacAddress
        - LmMethodType (str): optional regex of lmMethodType
        - LmmPriority (str): optional regex of lmmPriority
        - LmrPriority (str): optional regex of lmrPriority
        - LmrRxFcf (str): optional regex of lmrRxFcf
        - LmrRxFcfStepPer100mSec (str): optional regex of lmrRxFcfStepPer100mSec
        - LmrTxFcb (str): optional regex of lmrTxFcb
        - LmrTxFcbStepPer100mSec (str): optional regex of lmrTxFcbStepPer100mSec
        - LtAllRemoteMeps (str): optional regex of ltAllRemoteMeps
        - LtDestinationMacAddress (str): optional regex of ltDestinationMacAddress
        - LtmPriority (str): optional regex of ltmPriority
        - MacAddress (str): optional regex of macAddress
        - ManagementAddress (str): optional regex of managementAddress
        - ManagementAddressDomain (str): optional regex of managementAddressDomain
        - ManagementAddressDomainLength (str): optional regex of managementAddressDomainLength
        - ManagementAddressLength (str): optional regex of managementAddressLength
        - MdMegLevel (str): optional regex of mdMegLevel
        - MdMegLevelIndex (str): optional regex of mdMegLevelIndex
        - MegIdFormat (str): optional regex of megIdFormat
        - MepId (str): optional regex of mepId
        - MpIndex (str): optional regex of mpIndex
        - OrganizationSpecificTlvLength (str): optional regex of organizationSpecificTlvLength
        - OverrideVlanPriority (str): optional regex of overrideVlanPriority
        - Rdi (str): optional regex of rdi
        - SVlanId (str): optional regex of sVlanId
        - SVlanPriority (str): optional regex of sVlanPriority
        - SVlanTpid (str): optional regex of sVlanTpid
        - ShortMaName (str): optional regex of shortMaName
        - ShortMaNameFormat (str): optional regex of shortMaNameFormat
        - TstEnableUnicastMac (str): optional regex of tstEnableUnicastMac
        - TstIncrementPacketLength (str): optional regex of tstIncrementPacketLength
        - TstInitialPatternValue (str): optional regex of tstInitialPatternValue
        - TstInterval (str): optional regex of tstInterval
        - TstMode (str): optional regex of tstMode
        - TstOverwriteSequenceNumber (str): optional regex of tstOverwriteSequenceNumber
        - TstPacketLength (str): optional regex of tstPacketLength
        - TstPacketLengthStep (str): optional regex of tstPacketLengthStep
        - TstPatternType (str): optional regex of tstPatternType
        - TstPriority (str): optional regex of tstPriority
        - TstSequenceNumber (str): optional regex of tstSequenceNumber
        - TstTestType (str): optional regex of tstTestType
        - TstUnicastMac (str): optional regex of tstUnicastMac
        - Type (str): optional regex of type
        - VlanId (str): optional regex of vlanId
        - VlanPriority (str): optional regex of vlanPriority
        - VlanStacking (str): optional regex of vlanStacking
        - VlanTpid (str): optional regex of vlanTpid

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def ConnectMPToIxiaPort(self, *args, **kwargs):
        """Executes the connectMPToIxiaPort operation on the server.

        Please provide a proper help text here.

        connectMPToIxiaPort(Arg2=list)list
        ----------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('connectMPToIxiaPort', payload=payload, response_object=None)
