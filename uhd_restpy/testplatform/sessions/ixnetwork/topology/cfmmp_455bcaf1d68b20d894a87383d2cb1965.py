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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class CfmMp(Base):
    """MP exposing network configuration
    The CfmMp class encapsulates a required cfmMp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'cfmMp'
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
        'AutoLtTtl': 'autoLtTtl',
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
        'MdName': 'mdName',
        'MdNameFormat': 'mdNameFormat',
        'MegId': 'megId',
        'MegIdFormat': 'megIdFormat',
        'MepId': 'mepId',
        'MpType': 'mpType',
        'Name': 'name',
        'NumberOfCustomTLVs': 'numberOfCustomTLVs',
        'OrganizationSpecificTlvLength': 'organizationSpecificTlvLength',
        'OrganizationSpecificTlvValue': 'organizationSpecificTlvValue',
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
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
        'VlanStacking': 'vlanStacking',
        'VlanTpid': 'vlanTpid',
    }

    def __init__(self, parent):
        super(CfmMp, self).__init__(parent)

    @property
    def CfmCustomTLVList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.cfmcustomtlvlist_798bcbc04fddcff054434d56d2b00117.CfmCustomTLVList): An instance of the CfmCustomTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.cfmcustomtlvlist_798bcbc04fddcff054434d56d2b00117 import CfmCustomTLVList
        return CfmCustomTLVList(self)

    @property
    def StartCcmEmulatedMpParams(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.startccmemulatedmpparams_62b1a2be6189ae1e1aa5f0cee8254081.StartCcmEmulatedMpParams): An instance of the StartCcmEmulatedMpParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.startccmemulatedmpparams_62b1a2be6189ae1e1aa5f0cee8254081 import StartCcmEmulatedMpParams
        return StartCcmEmulatedMpParams(self)._select()

    @property
    def StopCcmEmulatedMpParams(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.stopccmemulatedmpparams_a24dfdb02ad9d3f95459876f02f9eff0.StopCcmEmulatedMpParams): An instance of the StopCcmEmulatedMpParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.stopccmemulatedmpparams_a24dfdb02ad9d3f95459876f02f9eff0 import StopCcmEmulatedMpParams
        return StopCcmEmulatedMpParams(self)._select()

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AisEnableUnicastMac(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable AIS in unicast mode to the specified MAC address of the remote MEP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AisEnableUnicastMac']))

    @property
    def AisInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interval between two AIS PDUs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AisInterval']))

    @property
    def AisMode(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Specifies Alarm Indication Signal Mode. Can be trigged from LCK only if set to Auto Mode. Manually Start or Stop otherwise.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AisMode']))

    @property
    def AisPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN Priority for AIS PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AisPriority']))

    @property
    def AisUnicastMac(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The MAC address of the remote MEP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AisUnicastMac']))

    @property
    def AutoDmTimeout(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Timeout value (in sec) of waiting for DMR of respective DMM.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoDmTimeout']))

    @property
    def AutoDmTimer(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interval (in sec) between two DMM PDUs to be sent.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoDmTimer']))

    @property
    def AutoLbIteration(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Number of LBM PDUs to be sent. 0 for infinite timer.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLbIteration']))

    @property
    def AutoLbTimeoutInSec(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Timeout value (in sec) of waiting for LBR of respective LBM.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLbTimeoutInSec']))

    @property
    def AutoLbTimerInSec(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interval (in sec) between two LBM PDUs to be sent.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLbTimerInSec']))

    @property
    def AutoLmIteration(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Number of LMM PDUs to be sent. 0 for infinite timer.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLmIteration']))

    @property
    def AutoLmTimeout(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Timeout value (in msec) of waiting for LMR of respective LMM. Must be multiple of 100.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLmTimeout']))

    @property
    def AutoLmTimer(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interval (in msec) between two LMM PDUs to be sent. Must be multiples of 100.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLmTimer']))

    @property
    def AutoLtIteration(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Number of LTM PDUs to be sent. 0 for infinite timer.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLtIteration']))

    @property
    def AutoLtTimeoutInSec(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Timeout value (in sec) of waiting for LTR of respective LTM.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLtTimeoutInSec']))

    @property
    def AutoLtTimerInSec(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interval (in sec) between two LTM PDUs to be sent.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLtTimerInSec']))

    @property
    def AutoLtTtl(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TTL for LBM PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoLtTtl']))

    @property
    def AutodmIteration(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Number of DMM PDUs to be sent. 0 for infinite timer.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutodmIteration']))

    @property
    def CVlanId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): C-VLAN ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanId']))

    @property
    def CVlanPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): C-VLAN Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanPriority']))

    @property
    def CVlanTpid(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): C-VLAN TPID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanTpid']))

    @property
    def CciInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interval between two CCM PDUs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CciInterval']))

    @property
    def CcmLmmTxFcf(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TxFCf value in CCM (dual mode) or LMM (single mode) PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CcmLmmTxFcf']))

    @property
    def CcmLmmTxFcfStepPer100mSec(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TxFCf step value per 100ms in CCM (dual mode) or LMM (single mode) PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CcmLmmTxFcfStepPer100mSec']))

    @property
    def CcmPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN Priority for CCM PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CcmPriority']))

    @property
    def CcmRxFcb(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): RxFCb value in CCM (dual mode) PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CcmRxFcb']))

    @property
    def CcmRxFcbStepPer100mSec(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): RxFCb step value per 100ms in CCM (dual mode) PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CcmRxFcbStepPer100mSec']))

    @property
    def ChassisId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Chassis ID for Sender ID TLV.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ChassisId']))

    @property
    def ChassisIdLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Chassis ID Length for Sender ID TLV.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ChassisIdLength']))

    @property
    def ChassisIdSubType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Chassis ID SubType for Sender ID TLV.
        """
        from uhd_restpy.multivalue import Multivalue
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
        - obj(uhd_restpy.multivalue.Multivalue): Data TLV Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DataTlvLength']))

    @property
    def DataTlvValue(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Data TLV Value
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DataTlvValue']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DmAllRemoteMeps(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enables DMM to be sent for all remote MEPs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DmAllRemoteMeps']))

    @property
    def DmDestinationMacAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MAC address of the remote MEP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DmDestinationMacAddress']))

    @property
    def DmMethod(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Specifies One Way or Two Way Delay Measurement Method.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DmMethod']))

    @property
    def DmPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN Priority for DMM PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DmPriority']))

    @property
    def EnableAisRx(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enables AIS PDUs to be processed in this MEP upon receiving at port.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAisRx']))

    @property
    def EnableAutoDm(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Periodic Delay Measurement.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAutoDm']))

    @property
    def EnableAutoLb(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Periodic Loopback.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAutoLb']))

    @property
    def EnableAutoLm(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Periodic Loss Measurement.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAutoLm']))

    @property
    def EnableAutoLt(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Periodic Link Trace.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAutoLt']))

    @property
    def EnableDataTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Data TLV for all applicable PDUs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableDataTlv']))

    @property
    def EnableInterfaceStatusTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Interface Status TLV for all applicable PDUs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableInterfaceStatusTlv']))

    @property
    def EnableLckRx(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enables LCK PDUs to be processed in this MEP upon receiving at port.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLckRx']))

    @property
    def EnableLmCounterUpdate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable updating the counter value for subsequent PDUs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLmCounterUpdate']))

    @property
    def EnableOrganizationSpecificTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Organization Specific TLV for all applicable PDUs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOrganizationSpecificTlv']))

    @property
    def EnablePortStatusTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Port Status TLV for all applicable PDUs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnablePortStatusTlv']))

    @property
    def EnableSenderIdTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Sender ID TLV for all applicable PDUs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSenderIdTlv']))

    @property
    def EnableTstRx(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enables TST PDUs to be processed in this MEP upon receiving at port.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableTstRx']))

    @property
    def EnableVlan(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable VLAN for this MP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableVlan']))

    @property
    def InterRemoteMepRxIncrementStep(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Inter Remote MEP Rx Increment Step.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InterRemoteMepRxIncrementStep']))

    @property
    def InterRemoteMepTxIncrementStep(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Inter Remote MEP Tx Increment Step.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InterRemoteMepTxIncrementStep']))

    @property
    def LbAllRemoteMeps(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enables LBM to be sent for all remote MEPs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LbAllRemoteMeps']))

    @property
    def LbDestinationMacAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MAC address of the remote MEP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LbDestinationMacAddress']))

    @property
    def LbmPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN Priority for LBM PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LbmPriority']))

    @property
    def LckEnableUnicastMac(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable LCK in unicast mode to the specified MAC address of the remote MEP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LckEnableUnicastMac']))

    @property
    def LckInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interval between two LCK PDUs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LckInterval']))

    @property
    def LckMode(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Specifies LCK Mode. Can be trigged from TST only if set to Auto Mode. Manually Start or Stop otherwise.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LckMode']))

    @property
    def LckPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN Priority for LCK PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LckPriority']))

    @property
    def LckSupportAisGeneration(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable or disable AIS PDU generation. Needs AIS mode to be set to Auto.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LckSupportAisGeneration']))

    @property
    def LckUnicastMac(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MAC Address of the remote MEP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LckUnicastMac']))

    @property
    def LmAllRemoteMeps(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enables LMM to be sent for all remote MEPs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmAllRemoteMeps']))

    @property
    def LmDestinationMacAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MAC address of the remote MEP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmDestinationMacAddress']))

    @property
    def LmMethodType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Loss Measurement Method - One Way or Two Way. For Two way, CCM PDUs are used. LMM & LMR otherwise.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmMethodType']))

    @property
    def LmmPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN Priority for LMM PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmmPriority']))

    @property
    def LmrPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN Priority for LMR PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmrPriority']))

    @property
    def LmrRxFcf(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): RxFCf value of LMR PDU (Single Mode).
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmrRxFcf']))

    @property
    def LmrRxFcfStepPer100mSec(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): RxFCf step value per 100ms of LMR PDU (Single Mode).
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmrRxFcfStepPer100mSec']))

    @property
    def LmrTxFcb(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TxFCb value in LMR PDU (Single mode) i.e. TxFCf of CCM or LMM.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmrTxFcb']))

    @property
    def LmrTxFcbStepPer100mSec(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TxFCb step value per 100ms in LMR PDU (Single mode).
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LmrTxFcbStepPer100mSec']))

    @property
    def LtAllRemoteMeps(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enables LTM to be sent for all remote MEPs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LtAllRemoteMeps']))

    @property
    def LtDestinationMacAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MAC address of the remote MEP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LtDestinationMacAddress']))

    @property
    def LtmPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN Priority for LTM PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LtmPriority']))

    @property
    def MacAddress(self):
        """
        Returns
        -------
        - list(str): MAC Address of MP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacAddress'])

    @property
    def ManagementAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Management Address for Sender ID TLV.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ManagementAddress']))

    @property
    def ManagementAddressDomain(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Management Address Domain for Sender ID TLV.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ManagementAddressDomain']))

    @property
    def ManagementAddressDomainLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Management Address Domain Length for Sender ID TLV.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ManagementAddressDomainLength']))

    @property
    def ManagementAddressLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Management Address Length for Sender ID TLV.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ManagementAddressLength']))

    @property
    def MdMegLevel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MD/MEG Level in which this MP belongs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MdMegLevel']))

    @property
    def MdName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MD Name for the selected MD Level. For MD Name Format MAC + Int, Please Use MAC-Int eg. 11:22:33:44:55:66-1. For Others, Use Any String.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MdName']))

    @property
    def MdNameFormat(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Format for Maintenance Domain Name.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MdNameFormat']))

    @property
    def MegId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MEG ID (Y.1731 Mode).
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MegId']))

    @property
    def MegIdFormat(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Format for MEG ID (Y.1731 Mode). Non-ICC formats are supported only if 'Allow CFM MAID Formats' is enabled.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MegIdFormat']))

    @property
    def MepId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MP Identifier. Must be unique in one MA.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MepId']))

    @property
    def MpType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Select MP type MIP or MEP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MpType']))

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
    def NumberOfCustomTLVs(self):
        """
        Returns
        -------
        - number: Number of Custom TLVs for PDUs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfCustomTLVs'])
    @NumberOfCustomTLVs.setter
    def NumberOfCustomTLVs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfCustomTLVs'], value)

    @property
    def OrganizationSpecificTlvLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Organization Specific TLV Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OrganizationSpecificTlvLength']))

    @property
    def OrganizationSpecificTlvValue(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Organization Specific TLV Value
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OrganizationSpecificTlvValue']))

    @property
    def OverrideVlanPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Override VLAN Priority value for PDUs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OverrideVlanPriority']))

    @property
    def Rdi(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Remote Defect Indication. Auto Update - RDI On if there is a defect in remote MEP. On or Off - Turn on or off RDI intentionally.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Rdi']))

    @property
    def SVlanId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): S-VLAN ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanId']))

    @property
    def SVlanPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): S-VLAN Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanPriority']))

    @property
    def SVlanTpid(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): S-VLAN TPID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanTpid']))

    @property
    def ShortMaName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Short Maintenance Association Name.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ShortMaName']))

    @property
    def ShortMaNameFormat(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Format for Maintenance Association Name.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ShortMaNameFormat']))

    @property
    def TstEnableUnicastMac(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable TST in unicast mode to the specified MAC address of the remote MEP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstEnableUnicastMac']))

    @property
    def TstIncrementPacketLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Increment Packet Length for subsequent TST PDUs.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstIncrementPacketLength']))

    @property
    def TstInitialPatternValue(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Initial Pattern Value of Test.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstInitialPatternValue']))

    @property
    def TstInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interval between two TST PDUs (in ms).
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstInterval']))

    @property
    def TstMode(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TST Mode On or Off.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstMode']))

    @property
    def TstOverwriteSequenceNumber(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Overwrite Sequence Number using specified value.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstOverwriteSequenceNumber']))

    @property
    def TstPacketLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Packet Length of TST PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstPacketLength']))

    @property
    def TstPacketLengthStep(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Increment for Packet Length Step.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstPacketLengthStep']))

    @property
    def TstPatternType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Pattern Type of Test.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstPatternType']))

    @property
    def TstPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN Priority for TST PDU.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstPriority']))

    @property
    def TstSequenceNumber(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Sequence Number of TST PDU. Effective only if overridden.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstSequenceNumber']))

    @property
    def TstTestType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Test Type In or Out Service.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstTestType']))

    @property
    def TstUnicastMac(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The MAC address of the remote MEP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TstUnicastMac']))

    @property
    def VlanId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanId']))

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanPriority']))

    @property
    def VlanStacking(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Single or Stacked VLAN Selection.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanStacking']))

    @property
    def VlanTpid(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VLAN TPID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanTpid']))

    def update(self, Name=None, NumberOfCustomTLVs=None):
        """Updates cfmMp resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfCustomTLVs (number): Number of Custom TLVs for PDUs.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, AisEnableUnicastMac=None, AisInterval=None, AisMode=None, AisPriority=None, AisUnicastMac=None, AutoDmTimeout=None, AutoDmTimer=None, AutoLbIteration=None, AutoLbTimeoutInSec=None, AutoLbTimerInSec=None, AutoLmIteration=None, AutoLmTimeout=None, AutoLmTimer=None, AutoLtIteration=None, AutoLtTimeoutInSec=None, AutoLtTimerInSec=None, AutoLtTtl=None, AutodmIteration=None, CVlanId=None, CVlanPriority=None, CVlanTpid=None, CciInterval=None, CcmLmmTxFcf=None, CcmLmmTxFcfStepPer100mSec=None, CcmPriority=None, CcmRxFcb=None, CcmRxFcbStepPer100mSec=None, ChassisId=None, ChassisIdLength=None, ChassisIdSubType=None, DataTlvLength=None, DataTlvValue=None, DmAllRemoteMeps=None, DmDestinationMacAddress=None, DmMethod=None, DmPriority=None, EnableAisRx=None, EnableAutoDm=None, EnableAutoLb=None, EnableAutoLm=None, EnableAutoLt=None, EnableDataTlv=None, EnableInterfaceStatusTlv=None, EnableLckRx=None, EnableLmCounterUpdate=None, EnableOrganizationSpecificTlv=None, EnablePortStatusTlv=None, EnableSenderIdTlv=None, EnableTstRx=None, EnableVlan=None, InterRemoteMepRxIncrementStep=None, InterRemoteMepTxIncrementStep=None, LbAllRemoteMeps=None, LbDestinationMacAddress=None, LbmPriority=None, LckEnableUnicastMac=None, LckInterval=None, LckMode=None, LckPriority=None, LckSupportAisGeneration=None, LckUnicastMac=None, LmAllRemoteMeps=None, LmDestinationMacAddress=None, LmMethodType=None, LmmPriority=None, LmrPriority=None, LmrRxFcf=None, LmrRxFcfStepPer100mSec=None, LmrTxFcb=None, LmrTxFcbStepPer100mSec=None, LtAllRemoteMeps=None, LtDestinationMacAddress=None, LtmPriority=None, ManagementAddress=None, ManagementAddressDomain=None, ManagementAddressDomainLength=None, ManagementAddressLength=None, MdMegLevel=None, MdName=None, MdNameFormat=None, MegId=None, MegIdFormat=None, MepId=None, MpType=None, OrganizationSpecificTlvLength=None, OrganizationSpecificTlvValue=None, OverrideVlanPriority=None, Rdi=None, SVlanId=None, SVlanPriority=None, SVlanTpid=None, ShortMaName=None, ShortMaNameFormat=None, TstEnableUnicastMac=None, TstIncrementPacketLength=None, TstInitialPatternValue=None, TstInterval=None, TstMode=None, TstOverwriteSequenceNumber=None, TstPacketLength=None, TstPacketLengthStep=None, TstPatternType=None, TstPriority=None, TstSequenceNumber=None, TstTestType=None, TstUnicastMac=None, VlanId=None, VlanPriority=None, VlanStacking=None, VlanTpid=None):
        """Base class infrastructure that gets a list of cfmMp device ids encapsulated by this object.

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
        - AutoLtTtl (str): optional regex of autoLtTtl
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
        - ManagementAddress (str): optional regex of managementAddress
        - ManagementAddressDomain (str): optional regex of managementAddressDomain
        - ManagementAddressDomainLength (str): optional regex of managementAddressDomainLength
        - ManagementAddressLength (str): optional regex of managementAddressLength
        - MdMegLevel (str): optional regex of mdMegLevel
        - MdName (str): optional regex of mdName
        - MdNameFormat (str): optional regex of mdNameFormat
        - MegId (str): optional regex of megId
        - MegIdFormat (str): optional regex of megIdFormat
        - MepId (str): optional regex of mepId
        - MpType (str): optional regex of mpType
        - OrganizationSpecificTlvLength (str): optional regex of organizationSpecificTlvLength
        - OrganizationSpecificTlvValue (str): optional regex of organizationSpecificTlvValue
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

    def ActivateMpEmulated(self, *args, **kwargs):
        """Executes the activateMpEmulated operation on the server.

        Activate Emulated MP

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        activateMpEmulated(SessionIndices=list)
        ---------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        activateMpEmulated(SessionIndices=string)
        -----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('activateMpEmulated', payload=payload, response_object=None)

    def ClearAllLearnedInfo(self, *args, **kwargs):
        """Executes the clearAllLearnedInfo operation on the server.

        Clears All Learned Info for the selected Root MP.

        clearAllLearnedInfo(Arg2=list)list
        ----------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearAllLearnedInfo', payload=payload, response_object=None)

    def DeactivateMpEmulated(self, *args, **kwargs):
        """Executes the deactivateMpEmulated operation on the server.

        Deactivate Emulated MP

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        deactivateMpEmulated(SessionIndices=list)
        -----------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        deactivateMpEmulated(SessionIndices=string)
        -------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('deactivateMpEmulated', payload=payload, response_object=None)

    def GetCfmAISDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmAISDbLearnedInformation operation on the server.

        Get Learned AIS Information

        getCfmAISDbLearnedInformation(Arg2=list)list
        --------------------------------------------
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
        return self._execute('getCfmAISDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmCcmLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmCcmLearnedInformation operation on the server.

        Please provide a proper help text here.

        getCfmCcmLearnedInformation(Arg2=list)list
        ------------------------------------------
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
        return self._execute('getCfmCcmLearnedInformation', payload=payload, response_object=None)

    def GetCfmDMDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmDMDbLearnedInformation operation on the server.

        Get Learned DM Information

        getCfmDMDbLearnedInformation(Arg2=list)list
        -------------------------------------------
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
        return self._execute('getCfmDMDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLCKDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLCKDbLearnedInformation operation on the server.

        Get Learned LCK Information

        getCfmLCKDbLearnedInformation(Arg2=list)list
        --------------------------------------------
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
        return self._execute('getCfmLCKDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLinkTraceDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLinkTraceDbLearnedInformation operation on the server.

        Please provide a proper help text here.

        getCfmLinkTraceDbLearnedInformation(Arg2=list)list
        --------------------------------------------------
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
        return self._execute('getCfmLinkTraceDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLMDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLMDbLearnedInformation operation on the server.

        Get Learned LM Information

        getCfmLMDbLearnedInformation(Arg2=list)list
        -------------------------------------------
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
        return self._execute('getCfmLMDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLoopbackDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLoopbackDbLearnedInformation operation on the server.

        Please provide a proper help text here.

        getCfmLoopbackDbLearnedInformation(Arg2=list)list
        -------------------------------------------------
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
        return self._execute('getCfmLoopbackDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmTSTDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmTSTDbLearnedInformation operation on the server.

        Get Learned TST Information

        getCfmTSTDbLearnedInformation(Arg2=list)list
        --------------------------------------------
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
        return self._execute('getCfmTSTDbLearnedInformation', payload=payload, response_object=None)

    def GetPeriodicDMLearnedInformation(self, *args, **kwargs):
        """Executes the getPeriodicDMLearnedInformation operation on the server.

        Please provide a proper help text here.

        getPeriodicDMLearnedInformation(Arg2=list)list
        ----------------------------------------------
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
        return self._execute('getPeriodicDMLearnedInformation', payload=payload, response_object=None)

    def GetPeriodicLBLearnedInformation(self, *args, **kwargs):
        """Executes the getPeriodicLBLearnedInformation operation on the server.

        Please provide a proper help text here.

        getPeriodicLBLearnedInformation(Arg2=list)list
        ----------------------------------------------
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
        return self._execute('getPeriodicLBLearnedInformation', payload=payload, response_object=None)

    def GetPeriodicLMLearnedInformation(self, *args, **kwargs):
        """Executes the getPeriodicLMLearnedInformation operation on the server.

        Please provide a proper help text here.

        getPeriodicLMLearnedInformation(Arg2=list)list
        ----------------------------------------------
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
        return self._execute('getPeriodicLMLearnedInformation', payload=payload, response_object=None)

    def GetPeriodicLTLearnedInformation(self, *args, **kwargs):
        """Executes the getPeriodicLTLearnedInformation operation on the server.

        Please provide a proper help text here.

        getPeriodicLTLearnedInformation(Arg2=list)list
        ----------------------------------------------
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
        return self._execute('getPeriodicLTLearnedInformation', payload=payload, response_object=None)

    def StartCcmEmulated(self, *args, **kwargs):
        """Executes the startCcmEmulated operation on the server.

        Start CCM

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        startCcmEmulated(SessionIndices=list)
        -------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        startCcmEmulated(SessionIndices=string)
        ---------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startCcmEmulated', payload=payload, response_object=None)

    def StartCcmEmulatedMp(self, *args, **kwargs):
        """Executes the startCcmEmulatedMp operation on the server.

        Start CCM PDU Transmission

        DEPRECATED startCcmEmulatedMp(Arg2=list)list
        --------------------------------------------
        - Arg2 (list(number)): List of indices into the network info. An empty list indicates all instances in the node specific data.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startCcmEmulatedMp', payload=payload, response_object=None)

    def StopCcmEmulated(self, *args, **kwargs):
        """Executes the stopCcmEmulated operation on the server.

        Stop CCM

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopCcmEmulated(SessionIndices=list)
        ------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stopCcmEmulated(SessionIndices=string)
        --------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopCcmEmulated', payload=payload, response_object=None)

    def StopCcmEmulatedMp(self, *args, **kwargs):
        """Executes the stopCcmEmulatedMp operation on the server.

        Stop CCM PDU Transmission

        DEPRECATED stopCcmEmulatedMp(Arg2=list)list
        -------------------------------------------
        - Arg2 (list(number)): List of indices into the network info. An empty list indicates all instances in the node specific data.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopCcmEmulatedMp', payload=payload, response_object=None)
