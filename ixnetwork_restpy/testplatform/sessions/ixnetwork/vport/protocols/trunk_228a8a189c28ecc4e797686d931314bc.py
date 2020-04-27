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


class Trunk(Base):
    """This object contains the PBB-TE trunk configuration.
    The Trunk class encapsulates a list of trunk resources that are managed by the user.
    A list of resources can be retrieved from the server using the Trunk.find() method.
    The list can be managed by using the Trunk.add() and Trunk.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'trunk'

    def __init__(self, parent):
        super(Trunk, self).__init__(parent)

    @property
    def MacRanges(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macranges_5e98259ec7671f12dfbd5199259d7bb2.MacRanges): An instance of the MacRanges class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macranges_5e98259ec7671f12dfbd5199259d7bb2 import MacRanges
        return MacRanges(self)

    @property
    def AddCcmCustomTlvs(self):
        """
        Returns
        -------
        - bool: If true, adds a custom CCM TLV to bridge messages.
        """
        return self._get_attribute('addCcmCustomTlvs')
    @AddCcmCustomTlvs.setter
    def AddCcmCustomTlvs(self, value):
        self._set_attribute('addCcmCustomTlvs', value)

    @property
    def AddDataTlv(self):
        """
        Returns
        -------
        - bool: If true, adds a data TLV to bridge messages.
        """
        return self._get_attribute('addDataTlv')
    @AddDataTlv.setter
    def AddDataTlv(self, value):
        self._set_attribute('addDataTlv', value)

    @property
    def AddInterfaceStatusTlv(self):
        """
        Returns
        -------
        - bool: If true, adds an interface status TLV to bridge messages.
        """
        return self._get_attribute('addInterfaceStatusTlv')
    @AddInterfaceStatusTlv.setter
    def AddInterfaceStatusTlv(self, value):
        self._set_attribute('addInterfaceStatusTlv', value)

    @property
    def AddLbmCustomTlvs(self):
        """
        Returns
        -------
        - bool: If true, adds a custom loopback message TLV to bridge messages.
        """
        return self._get_attribute('addLbmCustomTlvs')
    @AddLbmCustomTlvs.setter
    def AddLbmCustomTlvs(self, value):
        self._set_attribute('addLbmCustomTlvs', value)

    @property
    def AddLbrCustomTlvs(self):
        """
        Returns
        -------
        - bool: If true, adds a custom loopback response message TLV to bridge messages.
        """
        return self._get_attribute('addLbrCustomTlvs')
    @AddLbrCustomTlvs.setter
    def AddLbrCustomTlvs(self, value):
        self._set_attribute('addLbrCustomTlvs', value)

    @property
    def AddLmmCustomTlvs(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('addLmmCustomTlvs')
    @AddLmmCustomTlvs.setter
    def AddLmmCustomTlvs(self, value):
        self._set_attribute('addLmmCustomTlvs', value)

    @property
    def AddLmrCustomTlvs(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('addLmrCustomTlvs')
    @AddLmrCustomTlvs.setter
    def AddLmrCustomTlvs(self, value):
        self._set_attribute('addLmrCustomTlvs', value)

    @property
    def AddLtmCustomTlvs(self):
        """
        Returns
        -------
        - bool: If true, adds a custom link trace message TLV to bridge messages.
        """
        return self._get_attribute('addLtmCustomTlvs')
    @AddLtmCustomTlvs.setter
    def AddLtmCustomTlvs(self, value):
        self._set_attribute('addLtmCustomTlvs', value)

    @property
    def AddLtrCustomTlvs(self):
        """
        Returns
        -------
        - bool: If true, adds a custom link trace response message.
        """
        return self._get_attribute('addLtrCustomTlvs')
    @AddLtrCustomTlvs.setter
    def AddLtrCustomTlvs(self, value):
        self._set_attribute('addLtrCustomTlvs', value)

    @property
    def AddOrganizationSpecificTlv(self):
        """
        Returns
        -------
        - bool: If true, adds a custom organization specific message TLV to bridge messages.
        """
        return self._get_attribute('addOrganizationSpecificTlv')
    @AddOrganizationSpecificTlv.setter
    def AddOrganizationSpecificTlv(self, value):
        self._set_attribute('addOrganizationSpecificTlv', value)

    @property
    def AddPortStatusTlv(self):
        """
        Returns
        -------
        - bool: If true, adds a custom port status message TLV to bridge messages.
        """
        return self._get_attribute('addPortStatusTlv')
    @AddPortStatusTlv.setter
    def AddPortStatusTlv(self, value):
        self._set_attribute('addPortStatusTlv', value)

    @property
    def AddSenderIdTlv(self):
        """
        Returns
        -------
        - bool: If true, adds a custom sender ID message TLV to bridge messages.
        """
        return self._get_attribute('addSenderIdTlv')
    @AddSenderIdTlv.setter
    def AddSenderIdTlv(self, value):
        self._set_attribute('addSenderIdTlv', value)

    @property
    def AisInterval(self):
        """
        Returns
        -------
        - str(oneSec | oneMin): NOT DEFINED
        """
        return self._get_attribute('aisInterval')
    @AisInterval.setter
    def AisInterval(self, value):
        self._set_attribute('aisInterval', value)

    @property
    def AisMode(self):
        """
        Returns
        -------
        - str(auto | start | stop): NOT DEFINED
        """
        return self._get_attribute('aisMode')
    @AisMode.setter
    def AisMode(self, value):
        self._set_attribute('aisMode', value)

    @property
    def AisPriority(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('aisPriority')
    @AisPriority.setter
    def AisPriority(self, value):
        self._set_attribute('aisPriority', value)

    @property
    def AutoDmIteration(self):
        """
        Returns
        -------
        - number: The count for how many times DMMs will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        """
        return self._get_attribute('autoDmIteration')
    @AutoDmIteration.setter
    def AutoDmIteration(self, value):
        self._set_attribute('autoDmIteration', value)

    @property
    def AutoDmTimeout(self):
        """
        Returns
        -------
        - number: The timeout period in seconds to wait for a response to DMMs. This value should be less than the Auto LB Timer. Default is 30. Min: 1 Max: 65535
        """
        return self._get_attribute('autoDmTimeout')
    @AutoDmTimeout.setter
    def AutoDmTimeout(self, value):
        self._set_attribute('autoDmTimeout', value)

    @property
    def AutoDmTimer(self):
        """
        Returns
        -------
        - number: The time period in seconds between DMMs. Default is 60. Min: 1 Max: 65535
        """
        return self._get_attribute('autoDmTimer')
    @AutoDmTimer.setter
    def AutoDmTimer(self, value):
        self._set_attribute('autoDmTimer', value)

    @property
    def AutoLbIteration(self):
        """
        Returns
        -------
        - number: The count for how many times LBM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        """
        return self._get_attribute('autoLbIteration')
    @AutoLbIteration.setter
    def AutoLbIteration(self, value):
        self._set_attribute('autoLbIteration', value)

    @property
    def AutoLbTimeout(self):
        """
        Returns
        -------
        - number: The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        """
        return self._get_attribute('autoLbTimeout')
    @AutoLbTimeout.setter
    def AutoLbTimeout(self, value):
        self._set_attribute('autoLbTimeout', value)

    @property
    def AutoLbTimer(self):
        """
        Returns
        -------
        - number: The time period in seconds between LTMs. Default is 60. Min: 1 Max: 65535
        """
        return self._get_attribute('autoLbTimer')
    @AutoLbTimer.setter
    def AutoLbTimer(self, value):
        self._set_attribute('autoLbTimer', value)

    @property
    def AutoLmIteration(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('autoLmIteration')
    @AutoLmIteration.setter
    def AutoLmIteration(self, value):
        self._set_attribute('autoLmIteration', value)

    @property
    def AutoLmTimeout(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('autoLmTimeout')
    @AutoLmTimeout.setter
    def AutoLmTimeout(self, value):
        self._set_attribute('autoLmTimeout', value)

    @property
    def AutoLmTimer(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('autoLmTimer')
    @AutoLmTimer.setter
    def AutoLmTimer(self, value):
        self._set_attribute('autoLmTimer', value)

    @property
    def AutoLtIteration(self):
        """
        Returns
        -------
        - number: The count for how many times LTM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        """
        return self._get_attribute('autoLtIteration')
    @AutoLtIteration.setter
    def AutoLtIteration(self, value):
        self._set_attribute('autoLtIteration', value)

    @property
    def AutoLtTimeout(self):
        """
        Returns
        -------
        - number: The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        """
        return self._get_attribute('autoLtTimeout')
    @AutoLtTimeout.setter
    def AutoLtTimeout(self, value):
        self._set_attribute('autoLtTimeout', value)

    @property
    def AutoLtTimer(self):
        """
        Returns
        -------
        - number: The time period in seconds between LTMs. Default is 60. Min: 1 Max: 65535
        """
        return self._get_attribute('autoLtTimer')
    @AutoLtTimer.setter
    def AutoLtTimer(self, value):
        self._set_attribute('autoLtTimer', value)

    @property
    def BVlanId(self):
        """
        Returns
        -------
        - number: The VLAN identifier for the trunk.
        """
        return self._get_attribute('bVlanId')
    @BVlanId.setter
    def BVlanId(self, value):
        self._set_attribute('bVlanId', value)

    @property
    def BVlanPriority(self):
        """
        Returns
        -------
        - number: The VLAN priority for the trunk.
        """
        return self._get_attribute('bVlanPriority')
    @BVlanPriority.setter
    def BVlanPriority(self, value):
        self._set_attribute('bVlanPriority', value)

    @property
    def BVlanTpId(self):
        """
        Returns
        -------
        - str: The VLAN TPID for the trunk. EtherTypes identify the protocol that follows the VLAN header. Select from a list of hex options: 0x8100, 0x9100, 0x9200, and 0x88A8.
        """
        return self._get_attribute('bVlanTpId')
    @BVlanTpId.setter
    def BVlanTpId(self, value):
        self._set_attribute('bVlanTpId', value)

    @property
    def CciInterval(self):
        """
        Returns
        -------
        - str(3.33msec | 10msec | 100msec | 1sec | 10sec | 1min | 10min): Sets the continuity check interval for the trunk.
        """
        return self._get_attribute('cciInterval')
    @CciInterval.setter
    def CciInterval(self, value):
        self._set_attribute('cciInterval', value)

    @property
    def CcmLmmTxFcf(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('ccmLmmTxFcf')
    @CcmLmmTxFcf.setter
    def CcmLmmTxFcf(self, value):
        self._set_attribute('ccmLmmTxFcf', value)

    @property
    def CcmLmmTxFcfStep(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('ccmLmmTxFcfStep')
    @CcmLmmTxFcfStep.setter
    def CcmLmmTxFcfStep(self, value):
        self._set_attribute('ccmLmmTxFcfStep', value)

    @property
    def CcmPriority(self):
        """
        Returns
        -------
        - number: Sets the priority for Continuity Check Messages. The default is 0. Min: 0 Max: 7
        """
        return self._get_attribute('ccmPriority')
    @CcmPriority.setter
    def CcmPriority(self, value):
        self._set_attribute('ccmPriority', value)

    @property
    def CcmRxFcb(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('ccmRxFcb')
    @CcmRxFcb.setter
    def CcmRxFcb(self, value):
        self._set_attribute('ccmRxFcb', value)

    @property
    def CcmRxFcbStep(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('ccmRxFcbStep')
    @CcmRxFcbStep.setter
    def CcmRxFcbStep(self, value):
        self._set_attribute('ccmRxFcbStep', value)

    @property
    def ChassisId(self):
        """
        Returns
        -------
        - str: Sets the chassis identification. Default is 00 00 00 00 00 00. This will take Hex value as input (0-255 byte).
        """
        return self._get_attribute('chassisId')
    @ChassisId.setter
    def ChassisId(self, value):
        self._set_attribute('chassisId', value)

    @property
    def ChassisIdLength(self):
        """
        Returns
        -------
        - number: Sets the length of the Chassis ID field. Default is 6. Min: 0 Max: 255.
        """
        return self._get_attribute('chassisIdLength')
    @ChassisIdLength.setter
    def ChassisIdLength(self, value):
        self._set_attribute('chassisIdLength', value)

    @property
    def ChassisIdSubType(self):
        """
        Returns
        -------
        - str(chassisComponent | interfaceAlias | portComponent | macAddress | networkAddress | interfaceName | locallyAssigned): Sets the chassis identifier sub-type for the optional TLV messages. Options are:
        """
        return self._get_attribute('chassisIdSubType')
    @ChassisIdSubType.setter
    def ChassisIdSubType(self, value):
        self._set_attribute('chassisIdSubType', value)

    @property
    def DataTlvLength(self):
        """
        Returns
        -------
        - number: Sets the length of the Data TLV field. Default is 4. Min: 0 Max: 1500.
        """
        return self._get_attribute('dataTlvLength')
    @DataTlvLength.setter
    def DataTlvLength(self, value):
        self._set_attribute('dataTlvLength', value)

    @property
    def DataTlvValue(self):
        """
        Returns
        -------
        - str: This attribute will take Hex value of data. This data TLV will be added both for periodic LBM and requested LBM transmit. Default is 44 61 74 61.
        """
        return self._get_attribute('dataTlvValue')
    @DataTlvValue.setter
    def DataTlvValue(self, value):
        self._set_attribute('dataTlvValue', value)

    @property
    def DmMethod(self):
        """
        Returns
        -------
        - str(twoWay | oneWay): The type of Delay Measurment support.
        """
        return self._get_attribute('dmMethod')
    @DmMethod.setter
    def DmMethod(self, value):
        self._set_attribute('dmMethod', value)

    @property
    def DmPriority(self):
        """
        Returns
        -------
        - number: Sets the priority for DM Messages. This priority will be used only for periodic DMMs one-way or two-way (for both type of DM Method for each MIP). The default is 0.
        """
        return self._get_attribute('dmPriority')
    @DmPriority.setter
    def DmPriority(self, value):
        self._set_attribute('dmPriority', value)

    @property
    def DmmPriority(self):
        """DEPRECATED 
        Returns
        -------
        - number: Sets the priority for DM Messages. This priority will be used only for periodic DMMs. The default is 0. Min: 0 Max: 7
        """
        return self._get_attribute('dmmPriority')
    @DmmPriority.setter
    def DmmPriority(self, value):
        self._set_attribute('dmmPriority', value)

    @property
    def DstMacAddress(self):
        """
        Returns
        -------
        - str: Sets the destination MAC address for the trunk.
        """
        return self._get_attribute('dstMacAddress')
    @DstMacAddress.setter
    def DstMacAddress(self, value):
        self._set_attribute('dstMacAddress', value)

    @property
    def EnableAisRx(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableAisRx')
    @EnableAisRx.setter
    def EnableAisRx(self, value):
        self._set_attribute('enableAisRx', value)

    @property
    def EnableAutoDm(self):
        """
        Returns
        -------
        - bool: If true, enables the automatic sending of DM Messages.
        """
        return self._get_attribute('enableAutoDm')
    @EnableAutoDm.setter
    def EnableAutoDm(self, value):
        self._set_attribute('enableAutoDm', value)

    @property
    def EnableAutoLb(self):
        """
        Returns
        -------
        - bool: If true, enables the automatic sending of Loopback messages.
        """
        return self._get_attribute('enableAutoLb')
    @EnableAutoLb.setter
    def EnableAutoLb(self, value):
        self._set_attribute('enableAutoLb', value)

    @property
    def EnableAutoLm(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableAutoLm')
    @EnableAutoLm.setter
    def EnableAutoLm(self, value):
        self._set_attribute('enableAutoLm', value)

    @property
    def EnableAutoLt(self):
        """
        Returns
        -------
        - bool: If true, enables the automatic sending of Link Trace messages.
        """
        return self._get_attribute('enableAutoLt')
    @EnableAutoLt.setter
    def EnableAutoLt(self, value):
        self._set_attribute('enableAutoLt', value)

    @property
    def EnableLckRx(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableLckRx')
    @EnableLckRx.setter
    def EnableLckRx(self, value):
        self._set_attribute('enableLckRx', value)

    @property
    def EnableLmCounterUpdate(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableLmCounterUpdate')
    @EnableLmCounterUpdate.setter
    def EnableLmCounterUpdate(self, value):
        self._set_attribute('enableLmCounterUpdate', value)

    @property
    def EnableReverseBvlan(self):
        """
        Returns
        -------
        - bool: If true, enables the use of reverse B-VLANs on this trunk. In some cases, a PBB-TE Trunk will require a different B-VID in the reversed path. This option allows the user to specify whether a reverse B-VID is same as forward direction or not.
        """
        return self._get_attribute('enableReverseBvlan')
    @EnableReverseBvlan.setter
    def EnableReverseBvlan(self, value):
        self._set_attribute('enableReverseBvlan', value)

    @property
    def EnableTstRx(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableTstRx')
    @EnableTstRx.setter
    def EnableTstRx(self, value):
        self._set_attribute('enableTstRx', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the trunk is enabled.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def LbmPriority(self):
        """
        Returns
        -------
        - number: Sets the priority for Loopback Messages. This priority will be used only for periodic LBMs. The default is 0. Min: 0 Max: 7
        """
        return self._get_attribute('lbmPriority')
    @LbmPriority.setter
    def LbmPriority(self, value):
        self._set_attribute('lbmPriority', value)

    @property
    def LckInterval(self):
        """
        Returns
        -------
        - str(oneSec | oneMin): NOT DEFINED
        """
        return self._get_attribute('lckInterval')
    @LckInterval.setter
    def LckInterval(self, value):
        self._set_attribute('lckInterval', value)

    @property
    def LckMode(self):
        """
        Returns
        -------
        - str(auto | start | stop): NOT DEFINED
        """
        return self._get_attribute('lckMode')
    @LckMode.setter
    def LckMode(self, value):
        self._set_attribute('lckMode', value)

    @property
    def LckPriority(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('lckPriority')
    @LckPriority.setter
    def LckPriority(self, value):
        self._set_attribute('lckPriority', value)

    @property
    def LckSupportAisGeneration(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('lckSupportAisGeneration')
    @LckSupportAisGeneration.setter
    def LckSupportAisGeneration(self, value):
        self._set_attribute('lckSupportAisGeneration', value)

    @property
    def LmMethod(self):
        """
        Returns
        -------
        - str(singleEnded | dualEnded): NOT DEFINED
        """
        return self._get_attribute('lmMethod')
    @LmMethod.setter
    def LmMethod(self, value):
        self._set_attribute('lmMethod', value)

    @property
    def LmmPriority(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('lmmPriority')
    @LmmPriority.setter
    def LmmPriority(self, value):
        self._set_attribute('lmmPriority', value)

    @property
    def LmrPriority(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('lmrPriority')
    @LmrPriority.setter
    def LmrPriority(self, value):
        self._set_attribute('lmrPriority', value)

    @property
    def LmrRxFcf(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('lmrRxFcf')
    @LmrRxFcf.setter
    def LmrRxFcf(self, value):
        self._set_attribute('lmrRxFcf', value)

    @property
    def LmrRxFcfStep(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('lmrRxFcfStep')
    @LmrRxFcfStep.setter
    def LmrRxFcfStep(self, value):
        self._set_attribute('lmrRxFcfStep', value)

    @property
    def LtmPriority(self):
        """
        Returns
        -------
        - number: Sets the priority for Link Trace Messages. This priority will be used only for periodic LTMs. The default is 0. Min: 0 Max: 7
        """
        return self._get_attribute('ltmPriority')
    @LtmPriority.setter
    def LtmPriority(self, value):
        self._set_attribute('ltmPriority', value)

    @property
    def ManagementAddress(self):
        """
        Returns
        -------
        - str: Sets the trunk management address. Input type is HEX (0-255 byte). Default is 01 02 03 03 04 05.
        """
        return self._get_attribute('managementAddress')
    @ManagementAddress.setter
    def ManagementAddress(self, value):
        self._set_attribute('managementAddress', value)

    @property
    def ManagementAddressDomain(self):
        """
        Returns
        -------
        - str: Sets the trunk management address domain. This will take HEX input (0-255 byte). Default is 4d 61 6e 61 67 65 6d 65 6e 74 20 41 64 64 72 20 44 6f 6d 61 69 6e (Management Addr Domain).
        """
        return self._get_attribute('managementAddressDomain')
    @ManagementAddressDomain.setter
    def ManagementAddressDomain(self, value):
        self._set_attribute('managementAddressDomain', value)

    @property
    def ManagementAddressDomainLength(self):
        """
        Returns
        -------
        - number: Sets the length of the Management address domain field. Default is 22. Min: 0 Max: 255.
        """
        return self._get_attribute('managementAddressDomainLength')
    @ManagementAddressDomainLength.setter
    def ManagementAddressDomainLength(self, value):
        self._set_attribute('managementAddressDomainLength', value)

    @property
    def ManagementAddressLength(self):
        """
        Returns
        -------
        - number: Sets the length of the Management address field. Default is 6. Min: 0 Max: 255.
        """
        return self._get_attribute('managementAddressLength')
    @ManagementAddressLength.setter
    def ManagementAddressLength(self, value):
        self._set_attribute('managementAddressLength', value)

    @property
    def MdLevelId(self):
        """
        Returns
        -------
        - number: Sets the MD level identification for the trunk.
        """
        return self._get_attribute('mdLevelId')
    @MdLevelId.setter
    def MdLevelId(self, value):
        self._set_attribute('mdLevelId', value)

    @property
    def MdName(self):
        """
        Returns
        -------
        - str: Sets the MD name for the trunk.
        """
        return self._get_attribute('mdName')
    @MdName.setter
    def MdName(self, value):
        self._set_attribute('mdName', value)

    @property
    def MdNameFormat(self):
        """
        Returns
        -------
        - str(noDomainName | domainNameBasedString | macAddress2OctetInteger | characterString): Sets the MD Name format for the trunk.
        """
        return self._get_attribute('mdNameFormat')
    @MdNameFormat.setter
    def MdNameFormat(self, value):
        self._set_attribute('mdNameFormat', value)

    @property
    def MepId(self):
        """
        Returns
        -------
        - number: Sets the MEP identifier for the trunk.
        """
        return self._get_attribute('mepId')
    @MepId.setter
    def MepId(self, value):
        self._set_attribute('mepId', value)

    @property
    def OrganizationSpecificTlvLength(self):
        """
        Returns
        -------
        - number: Sets the length of the organizational specific TLV field. Default is 4. Min: 4 Max: 1500
        """
        return self._get_attribute('organizationSpecificTlvLength')
    @OrganizationSpecificTlvLength.setter
    def OrganizationSpecificTlvLength(self, value):
        self._set_attribute('organizationSpecificTlvLength', value)

    @property
    def OrganizationSpecificTlvValue(self):
        """
        Returns
        -------
        - str: Sets the value of the organizational specific TLV field. This attribute will take Hex value. Default is NULL.
        """
        return self._get_attribute('organizationSpecificTlvValue')
    @OrganizationSpecificTlvValue.setter
    def OrganizationSpecificTlvValue(self, value):
        self._set_attribute('organizationSpecificTlvValue', value)

    @property
    def OverrideVlanPriority(self):
        """
        Returns
        -------
        - bool: If true, overrides the set VLAN priority for this bridge, and uses the advanced settings instead.
        """
        return self._get_attribute('overrideVlanPriority')
    @OverrideVlanPriority.setter
    def OverrideVlanPriority(self, value):
        self._set_attribute('overrideVlanPriority', value)

    @property
    def Rdi(self):
        """
        Returns
        -------
        - str(auto | on | off): The Remote Defect Identification.
        """
        return self._get_attribute('rdi')
    @Rdi.setter
    def Rdi(self, value):
        self._set_attribute('rdi', value)

    @property
    def ReverseBvlanId(self):
        """
        Returns
        -------
        - number: Specifies the B-VLAN identifier for the reverse path on this trunk.
        """
        return self._get_attribute('reverseBvlanId')
    @ReverseBvlanId.setter
    def ReverseBvlanId(self, value):
        self._set_attribute('reverseBvlanId', value)

    @property
    def ShortMaName(self):
        """
        Returns
        -------
        - str: Sets the Short MA Name for the trunk.
        """
        return self._get_attribute('shortMaName')
    @ShortMaName.setter
    def ShortMaName(self, value):
        self._set_attribute('shortMaName', value)

    @property
    def ShortMaNameFormat(self):
        """
        Returns
        -------
        - str(primaryVid | characterString | 2octetInteger | rfc2685VpnId): Sets the Short MA Name format for the trunk.
        """
        return self._get_attribute('shortMaNameFormat')
    @ShortMaNameFormat.setter
    def ShortMaNameFormat(self, value):
        self._set_attribute('shortMaNameFormat', value)

    @property
    def SrcMacAddress(self):
        """
        Returns
        -------
        - str: Sets the source MAC address for the trunk.
        """
        return self._get_attribute('srcMacAddress')
    @SrcMacAddress.setter
    def SrcMacAddress(self, value):
        self._set_attribute('srcMacAddress', value)

    @property
    def TstIncrPacketLength(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('tstIncrPacketLength')
    @TstIncrPacketLength.setter
    def TstIncrPacketLength(self, value):
        self._set_attribute('tstIncrPacketLength', value)

    @property
    def TstIncrPacketLengthStep(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('tstIncrPacketLengthStep')
    @TstIncrPacketLengthStep.setter
    def TstIncrPacketLengthStep(self, value):
        self._set_attribute('tstIncrPacketLengthStep', value)

    @property
    def TstInitialPatternValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('tstInitialPatternValue')
    @TstInitialPatternValue.setter
    def TstInitialPatternValue(self, value):
        self._set_attribute('tstInitialPatternValue', value)

    @property
    def TstInterval(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('tstInterval')
    @TstInterval.setter
    def TstInterval(self, value):
        self._set_attribute('tstInterval', value)

    @property
    def TstMode(self):
        """
        Returns
        -------
        - str(start | stop): NOT DEFINED
        """
        return self._get_attribute('tstMode')
    @TstMode.setter
    def TstMode(self, value):
        self._set_attribute('tstMode', value)

    @property
    def TstOverwriteSequenceNumber(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('tstOverwriteSequenceNumber')
    @TstOverwriteSequenceNumber.setter
    def TstOverwriteSequenceNumber(self, value):
        self._set_attribute('tstOverwriteSequenceNumber', value)

    @property
    def TstPacketLength(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('tstPacketLength')
    @TstPacketLength.setter
    def TstPacketLength(self, value):
        self._set_attribute('tstPacketLength', value)

    @property
    def TstPatternType(self):
        """
        Returns
        -------
        - str(nullSignalWithoutCrc32 | nullSignalWithCrc32 | prbs2311WithoutCrc32 | prbs2311WithCrc32): NOT DEFINED
        """
        return self._get_attribute('tstPatternType')
    @TstPatternType.setter
    def TstPatternType(self, value):
        self._set_attribute('tstPatternType', value)

    @property
    def TstPriority(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('tstPriority')
    @TstPriority.setter
    def TstPriority(self, value):
        self._set_attribute('tstPriority', value)

    @property
    def TstSequenceNumber(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('tstSequenceNumber')
    @TstSequenceNumber.setter
    def TstSequenceNumber(self, value):
        self._set_attribute('tstSequenceNumber', value)

    @property
    def TstTestType(self):
        """
        Returns
        -------
        - str(inService | outOfService): NOT DEFINED
        """
        return self._get_attribute('tstTestType')
    @TstTestType.setter
    def TstTestType(self, value):
        self._set_attribute('tstTestType', value)

    @property
    def Ttl(self):
        """
        Returns
        -------
        - number: Sets the trunk Time-to-live value. Default is 64. Min: 1 Max: 255
        """
        return self._get_attribute('ttl')
    @Ttl.setter
    def Ttl(self, value):
        self._set_attribute('ttl', value)

    def update(self, AddCcmCustomTlvs=None, AddDataTlv=None, AddInterfaceStatusTlv=None, AddLbmCustomTlvs=None, AddLbrCustomTlvs=None, AddLmmCustomTlvs=None, AddLmrCustomTlvs=None, AddLtmCustomTlvs=None, AddLtrCustomTlvs=None, AddOrganizationSpecificTlv=None, AddPortStatusTlv=None, AddSenderIdTlv=None, AisInterval=None, AisMode=None, AisPriority=None, AutoDmIteration=None, AutoDmTimeout=None, AutoDmTimer=None, AutoLbIteration=None, AutoLbTimeout=None, AutoLbTimer=None, AutoLmIteration=None, AutoLmTimeout=None, AutoLmTimer=None, AutoLtIteration=None, AutoLtTimeout=None, AutoLtTimer=None, BVlanId=None, BVlanPriority=None, BVlanTpId=None, CciInterval=None, CcmLmmTxFcf=None, CcmLmmTxFcfStep=None, CcmPriority=None, CcmRxFcb=None, CcmRxFcbStep=None, ChassisId=None, ChassisIdLength=None, ChassisIdSubType=None, DataTlvLength=None, DataTlvValue=None, DmMethod=None, DmPriority=None, DmmPriority=None, DstMacAddress=None, EnableAisRx=None, EnableAutoDm=None, EnableAutoLb=None, EnableAutoLm=None, EnableAutoLt=None, EnableLckRx=None, EnableLmCounterUpdate=None, EnableReverseBvlan=None, EnableTstRx=None, Enabled=None, LbmPriority=None, LckInterval=None, LckMode=None, LckPriority=None, LckSupportAisGeneration=None, LmMethod=None, LmmPriority=None, LmrPriority=None, LmrRxFcf=None, LmrRxFcfStep=None, LtmPriority=None, ManagementAddress=None, ManagementAddressDomain=None, ManagementAddressDomainLength=None, ManagementAddressLength=None, MdLevelId=None, MdName=None, MdNameFormat=None, MepId=None, OrganizationSpecificTlvLength=None, OrganizationSpecificTlvValue=None, OverrideVlanPriority=None, Rdi=None, ReverseBvlanId=None, ShortMaName=None, ShortMaNameFormat=None, SrcMacAddress=None, TstIncrPacketLength=None, TstIncrPacketLengthStep=None, TstInitialPatternValue=None, TstInterval=None, TstMode=None, TstOverwriteSequenceNumber=None, TstPacketLength=None, TstPatternType=None, TstPriority=None, TstSequenceNumber=None, TstTestType=None, Ttl=None):
        """Updates trunk resource on the server.

        Args
        ----
        - AddCcmCustomTlvs (bool): If true, adds a custom CCM TLV to bridge messages.
        - AddDataTlv (bool): If true, adds a data TLV to bridge messages.
        - AddInterfaceStatusTlv (bool): If true, adds an interface status TLV to bridge messages.
        - AddLbmCustomTlvs (bool): If true, adds a custom loopback message TLV to bridge messages.
        - AddLbrCustomTlvs (bool): If true, adds a custom loopback response message TLV to bridge messages.
        - AddLmmCustomTlvs (bool): NOT DEFINED
        - AddLmrCustomTlvs (bool): NOT DEFINED
        - AddLtmCustomTlvs (bool): If true, adds a custom link trace message TLV to bridge messages.
        - AddLtrCustomTlvs (bool): If true, adds a custom link trace response message.
        - AddOrganizationSpecificTlv (bool): If true, adds a custom organization specific message TLV to bridge messages.
        - AddPortStatusTlv (bool): If true, adds a custom port status message TLV to bridge messages.
        - AddSenderIdTlv (bool): If true, adds a custom sender ID message TLV to bridge messages.
        - AisInterval (str(oneSec | oneMin)): NOT DEFINED
        - AisMode (str(auto | start | stop)): NOT DEFINED
        - AisPriority (number): NOT DEFINED
        - AutoDmIteration (number): The count for how many times DMMs will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoDmTimeout (number): The timeout period in seconds to wait for a response to DMMs. This value should be less than the Auto LB Timer. Default is 30. Min: 1 Max: 65535
        - AutoDmTimer (number): The time period in seconds between DMMs. Default is 60. Min: 1 Max: 65535
        - AutoLbIteration (number): The count for how many times LBM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoLbTimeout (number): The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        - AutoLbTimer (number): The time period in seconds between LTMs. Default is 60. Min: 1 Max: 65535
        - AutoLmIteration (number): NOT DEFINED
        - AutoLmTimeout (number): NOT DEFINED
        - AutoLmTimer (number): NOT DEFINED
        - AutoLtIteration (number): The count for how many times LTM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoLtTimeout (number): The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        - AutoLtTimer (number): The time period in seconds between LTMs. Default is 60. Min: 1 Max: 65535
        - BVlanId (number): The VLAN identifier for the trunk.
        - BVlanPriority (number): The VLAN priority for the trunk.
        - BVlanTpId (str): The VLAN TPID for the trunk. EtherTypes identify the protocol that follows the VLAN header. Select from a list of hex options: 0x8100, 0x9100, 0x9200, and 0x88A8.
        - CciInterval (str(3.33msec | 10msec | 100msec | 1sec | 10sec | 1min | 10min)): Sets the continuity check interval for the trunk.
        - CcmLmmTxFcf (number): NOT DEFINED
        - CcmLmmTxFcfStep (number): NOT DEFINED
        - CcmPriority (number): Sets the priority for Continuity Check Messages. The default is 0. Min: 0 Max: 7
        - CcmRxFcb (number): NOT DEFINED
        - CcmRxFcbStep (number): NOT DEFINED
        - ChassisId (str): Sets the chassis identification. Default is 00 00 00 00 00 00. This will take Hex value as input (0-255 byte).
        - ChassisIdLength (number): Sets the length of the Chassis ID field. Default is 6. Min: 0 Max: 255.
        - ChassisIdSubType (str(chassisComponent | interfaceAlias | portComponent | macAddress | networkAddress | interfaceName | locallyAssigned)): Sets the chassis identifier sub-type for the optional TLV messages. Options are:
        - DataTlvLength (number): Sets the length of the Data TLV field. Default is 4. Min: 0 Max: 1500.
        - DataTlvValue (str): This attribute will take Hex value of data. This data TLV will be added both for periodic LBM and requested LBM transmit. Default is 44 61 74 61.
        - DmMethod (str(twoWay | oneWay)): The type of Delay Measurment support.
        - DmPriority (number): Sets the priority for DM Messages. This priority will be used only for periodic DMMs one-way or two-way (for both type of DM Method for each MIP). The default is 0.
        - DmmPriority (number): Sets the priority for DM Messages. This priority will be used only for periodic DMMs. The default is 0. Min: 0 Max: 7
        - DstMacAddress (str): Sets the destination MAC address for the trunk.
        - EnableAisRx (bool): NOT DEFINED
        - EnableAutoDm (bool): If true, enables the automatic sending of DM Messages.
        - EnableAutoLb (bool): If true, enables the automatic sending of Loopback messages.
        - EnableAutoLm (bool): NOT DEFINED
        - EnableAutoLt (bool): If true, enables the automatic sending of Link Trace messages.
        - EnableLckRx (bool): NOT DEFINED
        - EnableLmCounterUpdate (bool): NOT DEFINED
        - EnableReverseBvlan (bool): If true, enables the use of reverse B-VLANs on this trunk. In some cases, a PBB-TE Trunk will require a different B-VID in the reversed path. This option allows the user to specify whether a reverse B-VID is same as forward direction or not.
        - EnableTstRx (bool): NOT DEFINED
        - Enabled (bool): If true, the trunk is enabled.
        - LbmPriority (number): Sets the priority for Loopback Messages. This priority will be used only for periodic LBMs. The default is 0. Min: 0 Max: 7
        - LckInterval (str(oneSec | oneMin)): NOT DEFINED
        - LckMode (str(auto | start | stop)): NOT DEFINED
        - LckPriority (number): NOT DEFINED
        - LckSupportAisGeneration (bool): NOT DEFINED
        - LmMethod (str(singleEnded | dualEnded)): NOT DEFINED
        - LmmPriority (number): NOT DEFINED
        - LmrPriority (number): NOT DEFINED
        - LmrRxFcf (number): NOT DEFINED
        - LmrRxFcfStep (number): NOT DEFINED
        - LtmPriority (number): Sets the priority for Link Trace Messages. This priority will be used only for periodic LTMs. The default is 0. Min: 0 Max: 7
        - ManagementAddress (str): Sets the trunk management address. Input type is HEX (0-255 byte). Default is 01 02 03 03 04 05.
        - ManagementAddressDomain (str): Sets the trunk management address domain. This will take HEX input (0-255 byte). Default is 4d 61 6e 61 67 65 6d 65 6e 74 20 41 64 64 72 20 44 6f 6d 61 69 6e (Management Addr Domain).
        - ManagementAddressDomainLength (number): Sets the length of the Management address domain field. Default is 22. Min: 0 Max: 255.
        - ManagementAddressLength (number): Sets the length of the Management address field. Default is 6. Min: 0 Max: 255.
        - MdLevelId (number): Sets the MD level identification for the trunk.
        - MdName (str): Sets the MD name for the trunk.
        - MdNameFormat (str(noDomainName | domainNameBasedString | macAddress2OctetInteger | characterString)): Sets the MD Name format for the trunk.
        - MepId (number): Sets the MEP identifier for the trunk.
        - OrganizationSpecificTlvLength (number): Sets the length of the organizational specific TLV field. Default is 4. Min: 4 Max: 1500
        - OrganizationSpecificTlvValue (str): Sets the value of the organizational specific TLV field. This attribute will take Hex value. Default is NULL.
        - OverrideVlanPriority (bool): If true, overrides the set VLAN priority for this bridge, and uses the advanced settings instead.
        - Rdi (str(auto | on | off)): The Remote Defect Identification.
        - ReverseBvlanId (number): Specifies the B-VLAN identifier for the reverse path on this trunk.
        - ShortMaName (str): Sets the Short MA Name for the trunk.
        - ShortMaNameFormat (str(primaryVid | characterString | 2octetInteger | rfc2685VpnId)): Sets the Short MA Name format for the trunk.
        - SrcMacAddress (str): Sets the source MAC address for the trunk.
        - TstIncrPacketLength (bool): NOT DEFINED
        - TstIncrPacketLengthStep (number): NOT DEFINED
        - TstInitialPatternValue (number): NOT DEFINED
        - TstInterval (number): NOT DEFINED
        - TstMode (str(start | stop)): NOT DEFINED
        - TstOverwriteSequenceNumber (bool): NOT DEFINED
        - TstPacketLength (number): NOT DEFINED
        - TstPatternType (str(nullSignalWithoutCrc32 | nullSignalWithCrc32 | prbs2311WithoutCrc32 | prbs2311WithCrc32)): NOT DEFINED
        - TstPriority (number): NOT DEFINED
        - TstSequenceNumber (number): NOT DEFINED
        - TstTestType (str(inService | outOfService)): NOT DEFINED
        - Ttl (number): Sets the trunk Time-to-live value. Default is 64. Min: 1 Max: 255

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, AddCcmCustomTlvs=None, AddDataTlv=None, AddInterfaceStatusTlv=None, AddLbmCustomTlvs=None, AddLbrCustomTlvs=None, AddLmmCustomTlvs=None, AddLmrCustomTlvs=None, AddLtmCustomTlvs=None, AddLtrCustomTlvs=None, AddOrganizationSpecificTlv=None, AddPortStatusTlv=None, AddSenderIdTlv=None, AisInterval=None, AisMode=None, AisPriority=None, AutoDmIteration=None, AutoDmTimeout=None, AutoDmTimer=None, AutoLbIteration=None, AutoLbTimeout=None, AutoLbTimer=None, AutoLmIteration=None, AutoLmTimeout=None, AutoLmTimer=None, AutoLtIteration=None, AutoLtTimeout=None, AutoLtTimer=None, BVlanId=None, BVlanPriority=None, BVlanTpId=None, CciInterval=None, CcmLmmTxFcf=None, CcmLmmTxFcfStep=None, CcmPriority=None, CcmRxFcb=None, CcmRxFcbStep=None, ChassisId=None, ChassisIdLength=None, ChassisIdSubType=None, DataTlvLength=None, DataTlvValue=None, DmMethod=None, DmPriority=None, DmmPriority=None, DstMacAddress=None, EnableAisRx=None, EnableAutoDm=None, EnableAutoLb=None, EnableAutoLm=None, EnableAutoLt=None, EnableLckRx=None, EnableLmCounterUpdate=None, EnableReverseBvlan=None, EnableTstRx=None, Enabled=None, LbmPriority=None, LckInterval=None, LckMode=None, LckPriority=None, LckSupportAisGeneration=None, LmMethod=None, LmmPriority=None, LmrPriority=None, LmrRxFcf=None, LmrRxFcfStep=None, LtmPriority=None, ManagementAddress=None, ManagementAddressDomain=None, ManagementAddressDomainLength=None, ManagementAddressLength=None, MdLevelId=None, MdName=None, MdNameFormat=None, MepId=None, OrganizationSpecificTlvLength=None, OrganizationSpecificTlvValue=None, OverrideVlanPriority=None, Rdi=None, ReverseBvlanId=None, ShortMaName=None, ShortMaNameFormat=None, SrcMacAddress=None, TstIncrPacketLength=None, TstIncrPacketLengthStep=None, TstInitialPatternValue=None, TstInterval=None, TstMode=None, TstOverwriteSequenceNumber=None, TstPacketLength=None, TstPatternType=None, TstPriority=None, TstSequenceNumber=None, TstTestType=None, Ttl=None):
        """Adds a new trunk resource on the server and adds it to the container.

        Args
        ----
        - AddCcmCustomTlvs (bool): If true, adds a custom CCM TLV to bridge messages.
        - AddDataTlv (bool): If true, adds a data TLV to bridge messages.
        - AddInterfaceStatusTlv (bool): If true, adds an interface status TLV to bridge messages.
        - AddLbmCustomTlvs (bool): If true, adds a custom loopback message TLV to bridge messages.
        - AddLbrCustomTlvs (bool): If true, adds a custom loopback response message TLV to bridge messages.
        - AddLmmCustomTlvs (bool): NOT DEFINED
        - AddLmrCustomTlvs (bool): NOT DEFINED
        - AddLtmCustomTlvs (bool): If true, adds a custom link trace message TLV to bridge messages.
        - AddLtrCustomTlvs (bool): If true, adds a custom link trace response message.
        - AddOrganizationSpecificTlv (bool): If true, adds a custom organization specific message TLV to bridge messages.
        - AddPortStatusTlv (bool): If true, adds a custom port status message TLV to bridge messages.
        - AddSenderIdTlv (bool): If true, adds a custom sender ID message TLV to bridge messages.
        - AisInterval (str(oneSec | oneMin)): NOT DEFINED
        - AisMode (str(auto | start | stop)): NOT DEFINED
        - AisPriority (number): NOT DEFINED
        - AutoDmIteration (number): The count for how many times DMMs will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoDmTimeout (number): The timeout period in seconds to wait for a response to DMMs. This value should be less than the Auto LB Timer. Default is 30. Min: 1 Max: 65535
        - AutoDmTimer (number): The time period in seconds between DMMs. Default is 60. Min: 1 Max: 65535
        - AutoLbIteration (number): The count for how many times LBM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoLbTimeout (number): The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        - AutoLbTimer (number): The time period in seconds between LTMs. Default is 60. Min: 1 Max: 65535
        - AutoLmIteration (number): NOT DEFINED
        - AutoLmTimeout (number): NOT DEFINED
        - AutoLmTimer (number): NOT DEFINED
        - AutoLtIteration (number): The count for how many times LTM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoLtTimeout (number): The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        - AutoLtTimer (number): The time period in seconds between LTMs. Default is 60. Min: 1 Max: 65535
        - BVlanId (number): The VLAN identifier for the trunk.
        - BVlanPriority (number): The VLAN priority for the trunk.
        - BVlanTpId (str): The VLAN TPID for the trunk. EtherTypes identify the protocol that follows the VLAN header. Select from a list of hex options: 0x8100, 0x9100, 0x9200, and 0x88A8.
        - CciInterval (str(3.33msec | 10msec | 100msec | 1sec | 10sec | 1min | 10min)): Sets the continuity check interval for the trunk.
        - CcmLmmTxFcf (number): NOT DEFINED
        - CcmLmmTxFcfStep (number): NOT DEFINED
        - CcmPriority (number): Sets the priority for Continuity Check Messages. The default is 0. Min: 0 Max: 7
        - CcmRxFcb (number): NOT DEFINED
        - CcmRxFcbStep (number): NOT DEFINED
        - ChassisId (str): Sets the chassis identification. Default is 00 00 00 00 00 00. This will take Hex value as input (0-255 byte).
        - ChassisIdLength (number): Sets the length of the Chassis ID field. Default is 6. Min: 0 Max: 255.
        - ChassisIdSubType (str(chassisComponent | interfaceAlias | portComponent | macAddress | networkAddress | interfaceName | locallyAssigned)): Sets the chassis identifier sub-type for the optional TLV messages. Options are:
        - DataTlvLength (number): Sets the length of the Data TLV field. Default is 4. Min: 0 Max: 1500.
        - DataTlvValue (str): This attribute will take Hex value of data. This data TLV will be added both for periodic LBM and requested LBM transmit. Default is 44 61 74 61.
        - DmMethod (str(twoWay | oneWay)): The type of Delay Measurment support.
        - DmPriority (number): Sets the priority for DM Messages. This priority will be used only for periodic DMMs one-way or two-way (for both type of DM Method for each MIP). The default is 0.
        - DmmPriority (number): Sets the priority for DM Messages. This priority will be used only for periodic DMMs. The default is 0. Min: 0 Max: 7
        - DstMacAddress (str): Sets the destination MAC address for the trunk.
        - EnableAisRx (bool): NOT DEFINED
        - EnableAutoDm (bool): If true, enables the automatic sending of DM Messages.
        - EnableAutoLb (bool): If true, enables the automatic sending of Loopback messages.
        - EnableAutoLm (bool): NOT DEFINED
        - EnableAutoLt (bool): If true, enables the automatic sending of Link Trace messages.
        - EnableLckRx (bool): NOT DEFINED
        - EnableLmCounterUpdate (bool): NOT DEFINED
        - EnableReverseBvlan (bool): If true, enables the use of reverse B-VLANs on this trunk. In some cases, a PBB-TE Trunk will require a different B-VID in the reversed path. This option allows the user to specify whether a reverse B-VID is same as forward direction or not.
        - EnableTstRx (bool): NOT DEFINED
        - Enabled (bool): If true, the trunk is enabled.
        - LbmPriority (number): Sets the priority for Loopback Messages. This priority will be used only for periodic LBMs. The default is 0. Min: 0 Max: 7
        - LckInterval (str(oneSec | oneMin)): NOT DEFINED
        - LckMode (str(auto | start | stop)): NOT DEFINED
        - LckPriority (number): NOT DEFINED
        - LckSupportAisGeneration (bool): NOT DEFINED
        - LmMethod (str(singleEnded | dualEnded)): NOT DEFINED
        - LmmPriority (number): NOT DEFINED
        - LmrPriority (number): NOT DEFINED
        - LmrRxFcf (number): NOT DEFINED
        - LmrRxFcfStep (number): NOT DEFINED
        - LtmPriority (number): Sets the priority for Link Trace Messages. This priority will be used only for periodic LTMs. The default is 0. Min: 0 Max: 7
        - ManagementAddress (str): Sets the trunk management address. Input type is HEX (0-255 byte). Default is 01 02 03 03 04 05.
        - ManagementAddressDomain (str): Sets the trunk management address domain. This will take HEX input (0-255 byte). Default is 4d 61 6e 61 67 65 6d 65 6e 74 20 41 64 64 72 20 44 6f 6d 61 69 6e (Management Addr Domain).
        - ManagementAddressDomainLength (number): Sets the length of the Management address domain field. Default is 22. Min: 0 Max: 255.
        - ManagementAddressLength (number): Sets the length of the Management address field. Default is 6. Min: 0 Max: 255.
        - MdLevelId (number): Sets the MD level identification for the trunk.
        - MdName (str): Sets the MD name for the trunk.
        - MdNameFormat (str(noDomainName | domainNameBasedString | macAddress2OctetInteger | characterString)): Sets the MD Name format for the trunk.
        - MepId (number): Sets the MEP identifier for the trunk.
        - OrganizationSpecificTlvLength (number): Sets the length of the organizational specific TLV field. Default is 4. Min: 4 Max: 1500
        - OrganizationSpecificTlvValue (str): Sets the value of the organizational specific TLV field. This attribute will take Hex value. Default is NULL.
        - OverrideVlanPriority (bool): If true, overrides the set VLAN priority for this bridge, and uses the advanced settings instead.
        - Rdi (str(auto | on | off)): The Remote Defect Identification.
        - ReverseBvlanId (number): Specifies the B-VLAN identifier for the reverse path on this trunk.
        - ShortMaName (str): Sets the Short MA Name for the trunk.
        - ShortMaNameFormat (str(primaryVid | characterString | 2octetInteger | rfc2685VpnId)): Sets the Short MA Name format for the trunk.
        - SrcMacAddress (str): Sets the source MAC address for the trunk.
        - TstIncrPacketLength (bool): NOT DEFINED
        - TstIncrPacketLengthStep (number): NOT DEFINED
        - TstInitialPatternValue (number): NOT DEFINED
        - TstInterval (number): NOT DEFINED
        - TstMode (str(start | stop)): NOT DEFINED
        - TstOverwriteSequenceNumber (bool): NOT DEFINED
        - TstPacketLength (number): NOT DEFINED
        - TstPatternType (str(nullSignalWithoutCrc32 | nullSignalWithCrc32 | prbs2311WithoutCrc32 | prbs2311WithCrc32)): NOT DEFINED
        - TstPriority (number): NOT DEFINED
        - TstSequenceNumber (number): NOT DEFINED
        - TstTestType (str(inService | outOfService)): NOT DEFINED
        - Ttl (number): Sets the trunk Time-to-live value. Default is 64. Min: 1 Max: 255

        Returns
        -------
        - self: This instance with all currently retrieved trunk resources using find and the newly added trunk resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained trunk resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AddCcmCustomTlvs=None, AddDataTlv=None, AddInterfaceStatusTlv=None, AddLbmCustomTlvs=None, AddLbrCustomTlvs=None, AddLmmCustomTlvs=None, AddLmrCustomTlvs=None, AddLtmCustomTlvs=None, AddLtrCustomTlvs=None, AddOrganizationSpecificTlv=None, AddPortStatusTlv=None, AddSenderIdTlv=None, AisInterval=None, AisMode=None, AisPriority=None, AutoDmIteration=None, AutoDmTimeout=None, AutoDmTimer=None, AutoLbIteration=None, AutoLbTimeout=None, AutoLbTimer=None, AutoLmIteration=None, AutoLmTimeout=None, AutoLmTimer=None, AutoLtIteration=None, AutoLtTimeout=None, AutoLtTimer=None, BVlanId=None, BVlanPriority=None, BVlanTpId=None, CciInterval=None, CcmLmmTxFcf=None, CcmLmmTxFcfStep=None, CcmPriority=None, CcmRxFcb=None, CcmRxFcbStep=None, ChassisId=None, ChassisIdLength=None, ChassisIdSubType=None, DataTlvLength=None, DataTlvValue=None, DmMethod=None, DmPriority=None, DmmPriority=None, DstMacAddress=None, EnableAisRx=None, EnableAutoDm=None, EnableAutoLb=None, EnableAutoLm=None, EnableAutoLt=None, EnableLckRx=None, EnableLmCounterUpdate=None, EnableReverseBvlan=None, EnableTstRx=None, Enabled=None, LbmPriority=None, LckInterval=None, LckMode=None, LckPriority=None, LckSupportAisGeneration=None, LmMethod=None, LmmPriority=None, LmrPriority=None, LmrRxFcf=None, LmrRxFcfStep=None, LtmPriority=None, ManagementAddress=None, ManagementAddressDomain=None, ManagementAddressDomainLength=None, ManagementAddressLength=None, MdLevelId=None, MdName=None, MdNameFormat=None, MepId=None, OrganizationSpecificTlvLength=None, OrganizationSpecificTlvValue=None, OverrideVlanPriority=None, Rdi=None, ReverseBvlanId=None, ShortMaName=None, ShortMaNameFormat=None, SrcMacAddress=None, TstIncrPacketLength=None, TstIncrPacketLengthStep=None, TstInitialPatternValue=None, TstInterval=None, TstMode=None, TstOverwriteSequenceNumber=None, TstPacketLength=None, TstPatternType=None, TstPriority=None, TstSequenceNumber=None, TstTestType=None, Ttl=None):
        """Finds and retrieves trunk resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trunk resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trunk resources from the server.

        Args
        ----
        - AddCcmCustomTlvs (bool): If true, adds a custom CCM TLV to bridge messages.
        - AddDataTlv (bool): If true, adds a data TLV to bridge messages.
        - AddInterfaceStatusTlv (bool): If true, adds an interface status TLV to bridge messages.
        - AddLbmCustomTlvs (bool): If true, adds a custom loopback message TLV to bridge messages.
        - AddLbrCustomTlvs (bool): If true, adds a custom loopback response message TLV to bridge messages.
        - AddLmmCustomTlvs (bool): NOT DEFINED
        - AddLmrCustomTlvs (bool): NOT DEFINED
        - AddLtmCustomTlvs (bool): If true, adds a custom link trace message TLV to bridge messages.
        - AddLtrCustomTlvs (bool): If true, adds a custom link trace response message.
        - AddOrganizationSpecificTlv (bool): If true, adds a custom organization specific message TLV to bridge messages.
        - AddPortStatusTlv (bool): If true, adds a custom port status message TLV to bridge messages.
        - AddSenderIdTlv (bool): If true, adds a custom sender ID message TLV to bridge messages.
        - AisInterval (str(oneSec | oneMin)): NOT DEFINED
        - AisMode (str(auto | start | stop)): NOT DEFINED
        - AisPriority (number): NOT DEFINED
        - AutoDmIteration (number): The count for how many times DMMs will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoDmTimeout (number): The timeout period in seconds to wait for a response to DMMs. This value should be less than the Auto LB Timer. Default is 30. Min: 1 Max: 65535
        - AutoDmTimer (number): The time period in seconds between DMMs. Default is 60. Min: 1 Max: 65535
        - AutoLbIteration (number): The count for how many times LBM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoLbTimeout (number): The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        - AutoLbTimer (number): The time period in seconds between LTMs. Default is 60. Min: 1 Max: 65535
        - AutoLmIteration (number): NOT DEFINED
        - AutoLmTimeout (number): NOT DEFINED
        - AutoLmTimer (number): NOT DEFINED
        - AutoLtIteration (number): The count for how many times LTM will be transmitted. Default is 0 (no limit). Min: 0 Max: 2^32
        - AutoLtTimeout (number): The timeout period in seconds to wait for a response to LTMs. This value should be less than the Auto LT Timer. Default is 30. Min: 1 Max: 65535
        - AutoLtTimer (number): The time period in seconds between LTMs. Default is 60. Min: 1 Max: 65535
        - BVlanId (number): The VLAN identifier for the trunk.
        - BVlanPriority (number): The VLAN priority for the trunk.
        - BVlanTpId (str): The VLAN TPID for the trunk. EtherTypes identify the protocol that follows the VLAN header. Select from a list of hex options: 0x8100, 0x9100, 0x9200, and 0x88A8.
        - CciInterval (str(3.33msec | 10msec | 100msec | 1sec | 10sec | 1min | 10min)): Sets the continuity check interval for the trunk.
        - CcmLmmTxFcf (number): NOT DEFINED
        - CcmLmmTxFcfStep (number): NOT DEFINED
        - CcmPriority (number): Sets the priority for Continuity Check Messages. The default is 0. Min: 0 Max: 7
        - CcmRxFcb (number): NOT DEFINED
        - CcmRxFcbStep (number): NOT DEFINED
        - ChassisId (str): Sets the chassis identification. Default is 00 00 00 00 00 00. This will take Hex value as input (0-255 byte).
        - ChassisIdLength (number): Sets the length of the Chassis ID field. Default is 6. Min: 0 Max: 255.
        - ChassisIdSubType (str(chassisComponent | interfaceAlias | portComponent | macAddress | networkAddress | interfaceName | locallyAssigned)): Sets the chassis identifier sub-type for the optional TLV messages. Options are:
        - DataTlvLength (number): Sets the length of the Data TLV field. Default is 4. Min: 0 Max: 1500.
        - DataTlvValue (str): This attribute will take Hex value of data. This data TLV will be added both for periodic LBM and requested LBM transmit. Default is 44 61 74 61.
        - DmMethod (str(twoWay | oneWay)): The type of Delay Measurment support.
        - DmPriority (number): Sets the priority for DM Messages. This priority will be used only for periodic DMMs one-way or two-way (for both type of DM Method for each MIP). The default is 0.
        - DmmPriority (number): Sets the priority for DM Messages. This priority will be used only for periodic DMMs. The default is 0. Min: 0 Max: 7
        - DstMacAddress (str): Sets the destination MAC address for the trunk.
        - EnableAisRx (bool): NOT DEFINED
        - EnableAutoDm (bool): If true, enables the automatic sending of DM Messages.
        - EnableAutoLb (bool): If true, enables the automatic sending of Loopback messages.
        - EnableAutoLm (bool): NOT DEFINED
        - EnableAutoLt (bool): If true, enables the automatic sending of Link Trace messages.
        - EnableLckRx (bool): NOT DEFINED
        - EnableLmCounterUpdate (bool): NOT DEFINED
        - EnableReverseBvlan (bool): If true, enables the use of reverse B-VLANs on this trunk. In some cases, a PBB-TE Trunk will require a different B-VID in the reversed path. This option allows the user to specify whether a reverse B-VID is same as forward direction or not.
        - EnableTstRx (bool): NOT DEFINED
        - Enabled (bool): If true, the trunk is enabled.
        - LbmPriority (number): Sets the priority for Loopback Messages. This priority will be used only for periodic LBMs. The default is 0. Min: 0 Max: 7
        - LckInterval (str(oneSec | oneMin)): NOT DEFINED
        - LckMode (str(auto | start | stop)): NOT DEFINED
        - LckPriority (number): NOT DEFINED
        - LckSupportAisGeneration (bool): NOT DEFINED
        - LmMethod (str(singleEnded | dualEnded)): NOT DEFINED
        - LmmPriority (number): NOT DEFINED
        - LmrPriority (number): NOT DEFINED
        - LmrRxFcf (number): NOT DEFINED
        - LmrRxFcfStep (number): NOT DEFINED
        - LtmPriority (number): Sets the priority for Link Trace Messages. This priority will be used only for periodic LTMs. The default is 0. Min: 0 Max: 7
        - ManagementAddress (str): Sets the trunk management address. Input type is HEX (0-255 byte). Default is 01 02 03 03 04 05.
        - ManagementAddressDomain (str): Sets the trunk management address domain. This will take HEX input (0-255 byte). Default is 4d 61 6e 61 67 65 6d 65 6e 74 20 41 64 64 72 20 44 6f 6d 61 69 6e (Management Addr Domain).
        - ManagementAddressDomainLength (number): Sets the length of the Management address domain field. Default is 22. Min: 0 Max: 255.
        - ManagementAddressLength (number): Sets the length of the Management address field. Default is 6. Min: 0 Max: 255.
        - MdLevelId (number): Sets the MD level identification for the trunk.
        - MdName (str): Sets the MD name for the trunk.
        - MdNameFormat (str(noDomainName | domainNameBasedString | macAddress2OctetInteger | characterString)): Sets the MD Name format for the trunk.
        - MepId (number): Sets the MEP identifier for the trunk.
        - OrganizationSpecificTlvLength (number): Sets the length of the organizational specific TLV field. Default is 4. Min: 4 Max: 1500
        - OrganizationSpecificTlvValue (str): Sets the value of the organizational specific TLV field. This attribute will take Hex value. Default is NULL.
        - OverrideVlanPriority (bool): If true, overrides the set VLAN priority for this bridge, and uses the advanced settings instead.
        - Rdi (str(auto | on | off)): The Remote Defect Identification.
        - ReverseBvlanId (number): Specifies the B-VLAN identifier for the reverse path on this trunk.
        - ShortMaName (str): Sets the Short MA Name for the trunk.
        - ShortMaNameFormat (str(primaryVid | characterString | 2octetInteger | rfc2685VpnId)): Sets the Short MA Name format for the trunk.
        - SrcMacAddress (str): Sets the source MAC address for the trunk.
        - TstIncrPacketLength (bool): NOT DEFINED
        - TstIncrPacketLengthStep (number): NOT DEFINED
        - TstInitialPatternValue (number): NOT DEFINED
        - TstInterval (number): NOT DEFINED
        - TstMode (str(start | stop)): NOT DEFINED
        - TstOverwriteSequenceNumber (bool): NOT DEFINED
        - TstPacketLength (number): NOT DEFINED
        - TstPatternType (str(nullSignalWithoutCrc32 | nullSignalWithCrc32 | prbs2311WithoutCrc32 | prbs2311WithCrc32)): NOT DEFINED
        - TstPriority (number): NOT DEFINED
        - TstSequenceNumber (number): NOT DEFINED
        - TstTestType (str(inService | outOfService)): NOT DEFINED
        - Ttl (number): Sets the trunk Time-to-live value. Default is 64. Min: 1 Max: 255

        Returns
        -------
        - self: This instance with matching trunk resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of trunk data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trunk resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
