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


class Bridge(Base):
    """This object contains the configuration for the CFM bridge.
    The Bridge class encapsulates a list of bridge resources that are managed by the user.
    A list of resources can be retrieved from the server using the Bridge.find() method.
    The list can be managed by using the Bridge.add() and Bridge.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bridge'
    _SDM_ATT_MAP = {
        'AisInterval': 'aisInterval',
        'AllowCfmMaidFormatsInY1731': 'allowCfmMaidFormatsInY1731',
        'BridgeId': 'bridgeId',
        'DelayLearnedErrorString': 'delayLearnedErrorString',
        'EnableAis': 'enableAis',
        'EnableOutOfSequenceDetection': 'enableOutOfSequenceDetection',
        'Enabled': 'enabled',
        'Encapsulation': 'encapsulation',
        'EtherType': 'etherType',
        'Function': 'function',
        'GarbageCollectTime': 'garbageCollectTime',
        'IsAisLearnedInfoRefreshed': 'isAisLearnedInfoRefreshed',
        'IsCcmLearnedInfoRefreshed': 'isCcmLearnedInfoRefreshed',
        'IsDelayLearnedConfigMep': 'isDelayLearnedConfigMep',
        'IsDelayLearnedPacketSent': 'isDelayLearnedPacketSent',
        'IsDelayMeasurementLearnedInfoRefreshed': 'isDelayMeasurementLearnedInfoRefreshed',
        'IsLbLearnedConfigMep': 'isLbLearnedConfigMep',
        'IsLbLearnedPacketSent': 'isLbLearnedPacketSent',
        'IsLckLearnedInfoRefreshed': 'isLckLearnedInfoRefreshed',
        'IsLinkTraceLearnedInfoRefreshed': 'isLinkTraceLearnedInfoRefreshed',
        'IsLoopbackLearnedInfoRefreshed': 'isLoopbackLearnedInfoRefreshed',
        'IsLossMeasurementLearnedInfoPacketSent': 'isLossMeasurementLearnedInfoPacketSent',
        'IsLossMeasurementLearnedInfoRefreshed': 'isLossMeasurementLearnedInfoRefreshed',
        'IsLtLearnedConfigMep': 'isLtLearnedConfigMep',
        'IsLtLearnedPacketSent': 'isLtLearnedPacketSent',
        'IsPbbTeCcmLearnedInfoRefreshed': 'isPbbTeCcmLearnedInfoRefreshed',
        'IsPbbTeDelayLearnedConfigMep': 'isPbbTeDelayLearnedConfigMep',
        'IsPbbTeDelayLearnedInfoRefreshed': 'isPbbTeDelayLearnedInfoRefreshed',
        'IsPbbTeDelayLearnedPacketSent': 'isPbbTeDelayLearnedPacketSent',
        'IsPbbTeLbLearnedConfigMep': 'isPbbTeLbLearnedConfigMep',
        'IsPbbTeLbLearnedInfoRefreshed': 'isPbbTeLbLearnedInfoRefreshed',
        'IsPbbTeLbLearnedPacketSent': 'isPbbTeLbLearnedPacketSent',
        'IsPeriodicOamLearnedInfoRefreshed': 'isPeriodicOamLearnedInfoRefreshed',
        'IsTstLearnedInfoRefreshed': 'isTstLearnedInfoRefreshed',
        'LbLearnedErrorString': 'lbLearnedErrorString',
        'LossMeasurementLearnedInfoErrorString': 'lossMeasurementLearnedInfoErrorString',
        'LtLearnedErrorString': 'ltLearnedErrorString',
        'OperationMode': 'operationMode',
        'PbbTeDelayLearnedErrorString': 'pbbTeDelayLearnedErrorString',
        'PbbTeLbLearnedErrorString': 'pbbTeLbLearnedErrorString',
        'UserBvlan': 'userBvlan',
        'UserBvlanId': 'userBvlanId',
        'UserBvlanPriority': 'userBvlanPriority',
        'UserBvlanTpId': 'userBvlanTpId',
        'UserCvlan': 'userCvlan',
        'UserCvlanId': 'userCvlanId',
        'UserCvlanPriority': 'userCvlanPriority',
        'UserCvlanTpId': 'userCvlanTpId',
        'UserDelayMethod': 'userDelayMethod',
        'UserDelayType': 'userDelayType',
        'UserDstMacAddress': 'userDstMacAddress',
        'UserDstMepId': 'userDstMepId',
        'UserDstType': 'userDstType',
        'UserLearnedInfoTimeOut': 'userLearnedInfoTimeOut',
        'UserLossMethod': 'userLossMethod',
        'UserMdLevel': 'userMdLevel',
        'UserPbbTeDelayMethod': 'userPbbTeDelayMethod',
        'UserPbbTeDelayType': 'userPbbTeDelayType',
        'UserPeriodicOamType': 'userPeriodicOamType',
        'UserSelectDstMepById': 'userSelectDstMepById',
        'UserSelectSrcMepById': 'userSelectSrcMepById',
        'UserSendType': 'userSendType',
        'UserShortMaName': 'userShortMaName',
        'UserShortMaNameFormat': 'userShortMaNameFormat',
        'UserSrcMacAddress': 'userSrcMacAddress',
        'UserSrcMepId': 'userSrcMepId',
        'UserSrcType': 'userSrcType',
        'UserSvlan': 'userSvlan',
        'UserSvlanId': 'userSvlanId',
        'UserSvlanPriority': 'userSvlanPriority',
        'UserSvlanTpId': 'userSvlanTpId',
        'UserTransactionId': 'userTransactionId',
        'UserTtlInterval': 'userTtlInterval',
        'UserUsabilityOption': 'userUsabilityOption',
    }

    def __init__(self, parent):
        super(Bridge, self).__init__(parent)

    @property
    def AisLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.aislearnedinfo_9d4d1a1b3ec5fdeb4481cafe9a0bb262.AisLearnedInfo): An instance of the AisLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.aislearnedinfo_9d4d1a1b3ec5fdeb4481cafe9a0bb262 import AisLearnedInfo
        return AisLearnedInfo(self)

    @property
    def CcmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ccmlearnedinfo_c99d00ef89af4fbcf32feeec5fafa4f7.CcmLearnedInfo): An instance of the CcmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ccmlearnedinfo_c99d00ef89af4fbcf32feeec5fafa4f7 import CcmLearnedInfo
        return CcmLearnedInfo(self)

    @property
    def CustomTlvs(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtlvs_bd691d177945bac583502e55bd792b7e.CustomTlvs): An instance of the CustomTlvs class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtlvs_bd691d177945bac583502e55bd792b7e import CustomTlvs
        return CustomTlvs(self)

    @property
    def DelayLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.delaylearnedinfo_e8e77e74a384521713f2adb3148f7022.DelayLearnedInfo): An instance of the DelayLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.delaylearnedinfo_e8e77e74a384521713f2adb3148f7022 import DelayLearnedInfo
        return DelayLearnedInfo(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_628fdf0890417e234e9b9a33933fd6bf.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_628fdf0890417e234e9b9a33933fd6bf import Interface
        return Interface(self)

    @property
    def LbLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lblearnedinfo_4823f0af8cbdf6d47df16955c18ca8ce.LbLearnedInfo): An instance of the LbLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lblearnedinfo_4823f0af8cbdf6d47df16955c18ca8ce import LbLearnedInfo
        return LbLearnedInfo(self)

    @property
    def LckLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lcklearnedinfo_ee59f77921e9b47ea51da325dd2c139e.LckLearnedInfo): An instance of the LckLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lcklearnedinfo_ee59f77921e9b47ea51da325dd2c139e import LckLearnedInfo
        return LckLearnedInfo(self)

    @property
    def Link(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_d1c3e2cedfb63fb83d884a011b42535c.Link): An instance of the Link class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_d1c3e2cedfb63fb83d884a011b42535c import Link
        return Link(self)

    @property
    def LossLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.losslearnedinfo_1cec4b3ece3eda9fa67e657808f7e614.LossLearnedInfo): An instance of the LossLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.losslearnedinfo_1cec4b3ece3eda9fa67e657808f7e614 import LossLearnedInfo
        return LossLearnedInfo(self)

    @property
    def LtLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedinfo_10ac5d7b75e3dd7daf4fe0b262809d4b.LtLearnedInfo): An instance of the LtLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedinfo_10ac5d7b75e3dd7daf4fe0b262809d4b import LtLearnedInfo
        return LtLearnedInfo(self)

    @property
    def MdLevel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mdlevel_e4cee9102f603a069fe765a7d88962f7.MdLevel): An instance of the MdLevel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mdlevel_e4cee9102f603a069fe765a7d88962f7 import MdLevel
        return MdLevel(self)

    @property
    def Mp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mp_fdca92ca7688d207a32daf52e610fd90.Mp): An instance of the Mp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mp_fdca92ca7688d207a32daf52e610fd90 import Mp
        return Mp(self)

    @property
    def PbbTeCcmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteccmlearnedinfo_7c0c86eaac3f2e7074b3a921e77e6bb4.PbbTeCcmLearnedInfo): An instance of the PbbTeCcmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteccmlearnedinfo_7c0c86eaac3f2e7074b3a921e77e6bb4 import PbbTeCcmLearnedInfo
        return PbbTeCcmLearnedInfo(self)

    @property
    def PbbTeDelayLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbtedelaylearnedinfo_512d2783741599b833ac92de5dea3589.PbbTeDelayLearnedInfo): An instance of the PbbTeDelayLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbtedelaylearnedinfo_512d2783741599b833ac92de5dea3589 import PbbTeDelayLearnedInfo
        return PbbTeDelayLearnedInfo(self)

    @property
    def PbbTeLbLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbtelblearnedinfo_04eda79d986af811f8d758c15dc5e1a1.PbbTeLbLearnedInfo): An instance of the PbbTeLbLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbtelblearnedinfo_04eda79d986af811f8d758c15dc5e1a1 import PbbTeLbLearnedInfo
        return PbbTeLbLearnedInfo(self)

    @property
    def PbbTeLtLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteltlearnedinfo_610e30e3fd03ef63fef044cdd71d106f.PbbTeLtLearnedInfo): An instance of the PbbTeLtLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteltlearnedinfo_610e30e3fd03ef63fef044cdd71d106f import PbbTeLtLearnedInfo
        return PbbTeLtLearnedInfo(self)

    @property
    def PbbTePeriodicOamDmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamdmlearnedinfo_30859a22b472106375a906c016795ef4.PbbTePeriodicOamDmLearnedInfo): An instance of the PbbTePeriodicOamDmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamdmlearnedinfo_30859a22b472106375a906c016795ef4 import PbbTePeriodicOamDmLearnedInfo
        return PbbTePeriodicOamDmLearnedInfo(self)

    @property
    def PbbTePeriodicOamLbLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamlblearnedinfo_4d43822d094c1ac0c3a7742b050d3b92.PbbTePeriodicOamLbLearnedInfo): An instance of the PbbTePeriodicOamLbLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamlblearnedinfo_4d43822d094c1ac0c3a7742b050d3b92 import PbbTePeriodicOamLbLearnedInfo
        return PbbTePeriodicOamLbLearnedInfo(self)

    @property
    def PbbTePeriodicOamLtLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamltlearnedinfo_14fbffb76c1c6dda7d20b24a185c9b8b.PbbTePeriodicOamLtLearnedInfo): An instance of the PbbTePeriodicOamLtLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamltlearnedinfo_14fbffb76c1c6dda7d20b24a185c9b8b import PbbTePeriodicOamLtLearnedInfo
        return PbbTePeriodicOamLtLearnedInfo(self)

    @property
    def PeriodicOamDmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamdmlearnedinfo_31e7a62116d301ce1802b27ea0445657.PeriodicOamDmLearnedInfo): An instance of the PeriodicOamDmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamdmlearnedinfo_31e7a62116d301ce1802b27ea0445657 import PeriodicOamDmLearnedInfo
        return PeriodicOamDmLearnedInfo(self)

    @property
    def PeriodicOamLbLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamlblearnedinfo_af7787e7abe588d7e9ad7b393adc6874.PeriodicOamLbLearnedInfo): An instance of the PeriodicOamLbLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamlblearnedinfo_af7787e7abe588d7e9ad7b393adc6874 import PeriodicOamLbLearnedInfo
        return PeriodicOamLbLearnedInfo(self)

    @property
    def PeriodicOamLmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamlmlearnedinfo_ee2b776d335186db7b509aa54dc286c1.PeriodicOamLmLearnedInfo): An instance of the PeriodicOamLmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamlmlearnedinfo_ee2b776d335186db7b509aa54dc286c1 import PeriodicOamLmLearnedInfo
        return PeriodicOamLmLearnedInfo(self)

    @property
    def PeriodicOamLtLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamltlearnedinfo_6554ec0bf8935a19c2e174af8633dd1c.PeriodicOamLtLearnedInfo): An instance of the PeriodicOamLtLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamltlearnedinfo_6554ec0bf8935a19c2e174af8633dd1c import PeriodicOamLtLearnedInfo
        return PeriodicOamLtLearnedInfo(self)

    @property
    def Trunk(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trunk_147fd64b18a4a919a7b504ec774c3e79.Trunk): An instance of the Trunk class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trunk_147fd64b18a4a919a7b504ec774c3e79 import Trunk
        return Trunk(self)

    @property
    def TstLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tstlearnedinfo_08a667662f0e19344b814657abe79fc4.TstLearnedInfo): An instance of the TstLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tstlearnedinfo_08a667662f0e19344b814657abe79fc4 import TstLearnedInfo
        return TstLearnedInfo(self)

    @property
    def Vlans(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vlans_7edba6e68b5ca69b65bf3cbb911cf28b.Vlans): An instance of the Vlans class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vlans_7edba6e68b5ca69b65bf3cbb911cf28b import Vlans
        return Vlans(self)

    @property
    def AisInterval(self):
        """DEPRECATED 
        Returns
        -------
        - str(oneSec | oneMin): The interval between AIS messages sent from this CFM bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AisInterval'])
    @AisInterval.setter
    def AisInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AisInterval'], value)

    @property
    def AllowCfmMaidFormatsInY1731(self):
        """
        Returns
        -------
        - bool: If true, allows to use CFM's MD Name types and Short MA Name types when the Operation Mode is Y.1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllowCfmMaidFormatsInY1731'])
    @AllowCfmMaidFormatsInY1731.setter
    def AllowCfmMaidFormatsInY1731(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AllowCfmMaidFormatsInY1731'], value)

    @property
    def BridgeId(self):
        """
        Returns
        -------
        - str: The bridge MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BridgeId'])
    @BridgeId.setter
    def BridgeId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BridgeId'], value)

    @property
    def DelayLearnedErrorString(self):
        """
        Returns
        -------
        - str: (read only) The learned error string for the delay measurement.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayLearnedErrorString'])

    @property
    def EnableAis(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If true, enables the use of AIS messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAis'])
    @EnableAis.setter
    def EnableAis(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAis'], value)

    @property
    def EnableOutOfSequenceDetection(self):
        """
        Returns
        -------
        - bool: If true, enables the detection of out of sequence CCM messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOutOfSequenceDetection'])
    @EnableOutOfSequenceDetection.setter
    def EnableOutOfSequenceDetection(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOutOfSequenceDetection'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, enables the CFM bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Encapsulation(self):
        """
        Returns
        -------
        - str(ethernet | llcSnap): Sets the encapsulation type for the bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Encapsulation'])
    @Encapsulation.setter
    def Encapsulation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Encapsulation'], value)

    @property
    def EtherType(self):
        """
        Returns
        -------
        - number: Selects the ether type for the bridge. The options are 0x8902 and 0x88E6.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EtherType'])
    @EtherType.setter
    def EtherType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EtherType'], value)

    @property
    def Function(self):
        """DEPRECATED 
        Returns
        -------
        - str(faultManagement | performanceMeasurement): Determines the CFM function when operationMode is set to Y.1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Function'])
    @Function.setter
    def Function(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Function'], value)

    @property
    def GarbageCollectTime(self):
        """
        Returns
        -------
        - number: Integer value denotes the interval for holding the expired database. Default 10 seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GarbageCollectTime'])
    @GarbageCollectTime.setter
    def GarbageCollectTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GarbageCollectTime'], value)

    @property
    def IsAisLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsAisLearnedInfoRefreshed'])

    @property
    def IsCcmLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the CCM learned information is current.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsCcmLearnedInfoRefreshed'])

    @property
    def IsDelayLearnedConfigMep(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the delay measurement was found.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsDelayLearnedConfigMep'])

    @property
    def IsDelayLearnedPacketSent(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates the delay packet was sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsDelayLearnedPacketSent'])

    @property
    def IsDelayMeasurementLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the learned delay information is current.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsDelayMeasurementLearnedInfoRefreshed'])

    @property
    def IsLbLearnedConfigMep(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the loopback measurement was found.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLbLearnedConfigMep'])

    @property
    def IsLbLearnedPacketSent(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates the loopback packet was sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLbLearnedPacketSent'])

    @property
    def IsLckLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLckLearnedInfoRefreshed'])

    @property
    def IsLinkTraceLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the learned link trace information is current.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLinkTraceLearnedInfoRefreshed'])

    @property
    def IsLoopbackLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the learned loopback information is current.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLoopbackLearnedInfoRefreshed'])

    @property
    def IsLossMeasurementLearnedInfoPacketSent(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLossMeasurementLearnedInfoPacketSent'])

    @property
    def IsLossMeasurementLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLossMeasurementLearnedInfoRefreshed'])

    @property
    def IsLtLearnedConfigMep(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the link trace measurement was found.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLtLearnedConfigMep'])

    @property
    def IsLtLearnedPacketSent(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates the link trace packet was sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLtLearnedPacketSent'])

    @property
    def IsPbbTeCcmLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the learned PBB-TE CCM information is current.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPbbTeCcmLearnedInfoRefreshed'])

    @property
    def IsPbbTeDelayLearnedConfigMep(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the PBB-TE delay measurement was found.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPbbTeDelayLearnedConfigMep'])

    @property
    def IsPbbTeDelayLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the learned PBB-TE delay information is current.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPbbTeDelayLearnedInfoRefreshed'])

    @property
    def IsPbbTeDelayLearnedPacketSent(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates the PBB-TE delay packet was sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPbbTeDelayLearnedPacketSent'])

    @property
    def IsPbbTeLbLearnedConfigMep(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the PBB-TE loopback measurement was found.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPbbTeLbLearnedConfigMep'])

    @property
    def IsPbbTeLbLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the PBB-TE learned loopback information is current.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPbbTeLbLearnedInfoRefreshed'])

    @property
    def IsPbbTeLbLearnedPacketSent(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates the PBB-TE loopback packet was sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPbbTeLbLearnedPacketSent'])

    @property
    def IsPeriodicOamLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: If true, the periodic OAM learned information is up-to-date.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPeriodicOamLearnedInfoRefreshed'])

    @property
    def IsTstLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsTstLearnedInfoRefreshed'])

    @property
    def LbLearnedErrorString(self):
        """
        Returns
        -------
        - str: (read only) The learned error string for the loopback measurement.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LbLearnedErrorString'])

    @property
    def LossMeasurementLearnedInfoErrorString(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LossMeasurementLearnedInfoErrorString'])

    @property
    def LtLearnedErrorString(self):
        """
        Returns
        -------
        - str: (read only) The learned error string for the link trace measurement.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LtLearnedErrorString'])

    @property
    def OperationMode(self):
        """
        Returns
        -------
        - str(cfm | y1731 | pbbTe): Selects the type of CFM to enable.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OperationMode'])
    @OperationMode.setter
    def OperationMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OperationMode'], value)

    @property
    def PbbTeDelayLearnedErrorString(self):
        """
        Returns
        -------
        - str: (read only) The learned error string for the PBB-TE delay measurement.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbTeDelayLearnedErrorString'])

    @property
    def PbbTeLbLearnedErrorString(self):
        """
        Returns
        -------
        - str: (read only) The learned error string for the PBB-TE loopback measurement.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PbbTeLbLearnedErrorString'])

    @property
    def UserBvlan(self):
        """
        Returns
        -------
        - str(noVlanId | vlanId | allVlanId): Sets the bridge filter for PBB-TE learned information for the VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserBvlan'])
    @UserBvlan.setter
    def UserBvlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserBvlan'], value)

    @property
    def UserBvlanId(self):
        """
        Returns
        -------
        - number: Sets the PBB-TE VLAN identifier for filtering learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserBvlanId'])
    @UserBvlanId.setter
    def UserBvlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserBvlanId'], value)

    @property
    def UserBvlanPriority(self):
        """
        Returns
        -------
        - number: Sets the PBB-TE VLAN priority for filtering learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserBvlanPriority'])
    @UserBvlanPriority.setter
    def UserBvlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserBvlanPriority'], value)

    @property
    def UserBvlanTpId(self):
        """
        Returns
        -------
        - str: Sets the PBB-TE VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserBvlanTpId'])
    @UserBvlanTpId.setter
    def UserBvlanTpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserBvlanTpId'], value)

    @property
    def UserCvlan(self):
        """
        Returns
        -------
        - str(noVlanId | vlanId | allVlanId): Sets the bridge filter for learned information for a single VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserCvlan'])
    @UserCvlan.setter
    def UserCvlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserCvlan'], value)

    @property
    def UserCvlanId(self):
        """
        Returns
        -------
        - number: Sets the single VLAN identifier for filtering learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserCvlanId'])
    @UserCvlanId.setter
    def UserCvlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserCvlanId'], value)

    @property
    def UserCvlanPriority(self):
        """
        Returns
        -------
        - number: Sets the single VLAN priority for filtering learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserCvlanPriority'])
    @UserCvlanPriority.setter
    def UserCvlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserCvlanPriority'], value)

    @property
    def UserCvlanTpId(self):
        """
        Returns
        -------
        - str: Sets the single VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserCvlanTpId'])
    @UserCvlanTpId.setter
    def UserCvlanTpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserCvlanTpId'], value)

    @property
    def UserDelayMethod(self):
        """
        Returns
        -------
        - str(oneWay | twoWay): Sets the type of delay method to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserDelayMethod'])
    @UserDelayMethod.setter
    def UserDelayMethod(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserDelayMethod'], value)

    @property
    def UserDelayType(self):
        """
        Returns
        -------
        - str(dm | dvm): Sets the type of delay measurement to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserDelayType'])
    @UserDelayType.setter
    def UserDelayType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserDelayType'], value)

    @property
    def UserDstMacAddress(self):
        """
        Returns
        -------
        - str: Filters on the destination MAC address specified.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserDstMacAddress'])
    @UserDstMacAddress.setter
    def UserDstMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserDstMacAddress'], value)

    @property
    def UserDstMepId(self):
        """
        Returns
        -------
        - number: Sets the MEP identifier for use with userSelectDstMepById.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserDstMepId'])
    @UserDstMepId.setter
    def UserDstMepId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserDstMepId'], value)

    @property
    def UserDstType(self):
        """
        Returns
        -------
        - str(mepMac | mepId | mepMacAll | mepIdAll): The user destination type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserDstType'])
    @UserDstType.setter
    def UserDstType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserDstType'], value)

    @property
    def UserLearnedInfoTimeOut(self):
        """
        Returns
        -------
        - number: The interval in millisecond for the learned record to timeout. Default: 5000.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserLearnedInfoTimeOut'])
    @UserLearnedInfoTimeOut.setter
    def UserLearnedInfoTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserLearnedInfoTimeOut'], value)

    @property
    def UserLossMethod(self):
        """
        Returns
        -------
        - str(dualEnded | singleEnded): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserLossMethod'])
    @UserLossMethod.setter
    def UserLossMethod(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserLossMethod'], value)

    @property
    def UserMdLevel(self):
        """
        Returns
        -------
        - str(0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | allMd): Filters on the specified MD level.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserMdLevel'])
    @UserMdLevel.setter
    def UserMdLevel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserMdLevel'], value)

    @property
    def UserPbbTeDelayMethod(self):
        """
        Returns
        -------
        - str(twoWay | oneWay): Sets the PBB-TE type of delay method to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPbbTeDelayMethod'])
    @UserPbbTeDelayMethod.setter
    def UserPbbTeDelayMethod(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserPbbTeDelayMethod'], value)

    @property
    def UserPbbTeDelayType(self):
        """
        Returns
        -------
        - str(dm | dvm): Sets the PBB-TE type of delay measurement to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPbbTeDelayType'])
    @UserPbbTeDelayType.setter
    def UserPbbTeDelayType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserPbbTeDelayType'], value)

    @property
    def UserPeriodicOamType(self):
        """
        Returns
        -------
        - str(linkTrace | loopback | delayMeasurement | lossMeasurement): Sets the type of periodic OAM.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPeriodicOamType'])
    @UserPeriodicOamType.setter
    def UserPeriodicOamType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserPeriodicOamType'], value)

    @property
    def UserSelectDstMepById(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If true, filters on the MEP by destination MEP identifier rather than by the MAC address. The MEP identifier is set in userDstMepId.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserSelectDstMepById'])
    @UserSelectDstMepById.setter
    def UserSelectDstMepById(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserSelectDstMepById'], value)

    @property
    def UserSelectSrcMepById(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If true, filters on the MEP by source MEP identifier rather than by the MAC address. The MEP identifier is set in userSrcMepId.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserSelectSrcMepById'])
    @UserSelectSrcMepById.setter
    def UserSelectSrcMepById(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserSelectSrcMepById'], value)

    @property
    def UserSendType(self):
        """
        Returns
        -------
        - str(unicast | multicast): Filters on the the send type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserSendType'])
    @UserSendType.setter
    def UserSendType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserSendType'], value)

    @property
    def UserShortMaName(self):
        """
        Returns
        -------
        - str: Filters on the specified Short MA Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserShortMaName'])
    @UserShortMaName.setter
    def UserShortMaName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserShortMaName'], value)

    @property
    def UserShortMaNameFormat(self):
        """
        Returns
        -------
        - str(allFormats | primaryVid | characterString | twoOctetInteger | rfc2685VpnId): Filters on the Short MA Name Format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserShortMaNameFormat'])
    @UserShortMaNameFormat.setter
    def UserShortMaNameFormat(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserShortMaNameFormat'], value)

    @property
    def UserSrcMacAddress(self):
        """
        Returns
        -------
        - str: Filters on the specified source MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserSrcMacAddress'])
    @UserSrcMacAddress.setter
    def UserSrcMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserSrcMacAddress'], value)

    @property
    def UserSrcMepId(self):
        """
        Returns
        -------
        - number: Sets the MEP identifier for use with userSelectSrcMepById.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserSrcMepId'])
    @UserSrcMepId.setter
    def UserSrcMepId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserSrcMepId'], value)

    @property
    def UserSrcType(self):
        """
        Returns
        -------
        - str(mepMac | mepId | mepMacAll | mepIdAll): The user source type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserSrcType'])
    @UserSrcType.setter
    def UserSrcType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserSrcType'], value)

    @property
    def UserSvlan(self):
        """
        Returns
        -------
        - str(noVlanId | vlanId | allVlanId): Sets the bridge filter for learned information for a stacked VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserSvlan'])
    @UserSvlan.setter
    def UserSvlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserSvlan'], value)

    @property
    def UserSvlanId(self):
        """
        Returns
        -------
        - number: Sets the stacked VLAN identifier for filtering learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserSvlanId'])
    @UserSvlanId.setter
    def UserSvlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserSvlanId'], value)

    @property
    def UserSvlanPriority(self):
        """
        Returns
        -------
        - number: Sets the stacked VLAN priority for filtering learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserSvlanPriority'])
    @UserSvlanPriority.setter
    def UserSvlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserSvlanPriority'], value)

    @property
    def UserSvlanTpId(self):
        """
        Returns
        -------
        - str: Sets the stacked VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserSvlanTpId'])
    @UserSvlanTpId.setter
    def UserSvlanTpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserSvlanTpId'], value)

    @property
    def UserTransactionId(self):
        """
        Returns
        -------
        - number: The transaction identifier for the LTM packet if the configured MEP not found. Default: 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserTransactionId'])
    @UserTransactionId.setter
    def UserTransactionId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserTransactionId'], value)

    @property
    def UserTtlInterval(self):
        """
        Returns
        -------
        - number: Time to live value, in seconds. Default is 64.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserTtlInterval'])
    @UserTtlInterval.setter
    def UserTtlInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserTtlInterval'], value)

    @property
    def UserUsabilityOption(self):
        """
        Returns
        -------
        - str(manual | oneToOne | oneToAll | allToOne | allToAll): User Option, one of Manual, One-to-One, One-to-All, All-to-One, All-to-All.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserUsabilityOption'])
    @UserUsabilityOption.setter
    def UserUsabilityOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UserUsabilityOption'], value)

    def update(self, AisInterval=None, AllowCfmMaidFormatsInY1731=None, BridgeId=None, EnableAis=None, EnableOutOfSequenceDetection=None, Enabled=None, Encapsulation=None, EtherType=None, Function=None, GarbageCollectTime=None, OperationMode=None, UserBvlan=None, UserBvlanId=None, UserBvlanPriority=None, UserBvlanTpId=None, UserCvlan=None, UserCvlanId=None, UserCvlanPriority=None, UserCvlanTpId=None, UserDelayMethod=None, UserDelayType=None, UserDstMacAddress=None, UserDstMepId=None, UserDstType=None, UserLearnedInfoTimeOut=None, UserLossMethod=None, UserMdLevel=None, UserPbbTeDelayMethod=None, UserPbbTeDelayType=None, UserPeriodicOamType=None, UserSelectDstMepById=None, UserSelectSrcMepById=None, UserSendType=None, UserShortMaName=None, UserShortMaNameFormat=None, UserSrcMacAddress=None, UserSrcMepId=None, UserSrcType=None, UserSvlan=None, UserSvlanId=None, UserSvlanPriority=None, UserSvlanTpId=None, UserTransactionId=None, UserTtlInterval=None, UserUsabilityOption=None):
        """Updates bridge resource on the server.

        Args
        ----
        - AisInterval (str(oneSec | oneMin)): The interval between AIS messages sent from this CFM bridge.
        - AllowCfmMaidFormatsInY1731 (bool): If true, allows to use CFM's MD Name types and Short MA Name types when the Operation Mode is Y.1731.
        - BridgeId (str): The bridge MAC address.
        - EnableAis (bool): If true, enables the use of AIS messages.
        - EnableOutOfSequenceDetection (bool): If true, enables the detection of out of sequence CCM messages.
        - Enabled (bool): If true, enables the CFM bridge.
        - Encapsulation (str(ethernet | llcSnap)): Sets the encapsulation type for the bridge.
        - EtherType (number): Selects the ether type for the bridge. The options are 0x8902 and 0x88E6.
        - Function (str(faultManagement | performanceMeasurement)): Determines the CFM function when operationMode is set to Y.1731.
        - GarbageCollectTime (number): Integer value denotes the interval for holding the expired database. Default 10 seconds.
        - OperationMode (str(cfm | y1731 | pbbTe)): Selects the type of CFM to enable.
        - UserBvlan (str(noVlanId | vlanId | allVlanId)): Sets the bridge filter for PBB-TE learned information for the VLAN.
        - UserBvlanId (number): Sets the PBB-TE VLAN identifier for filtering learned information.
        - UserBvlanPriority (number): Sets the PBB-TE VLAN priority for filtering learned information.
        - UserBvlanTpId (str): Sets the PBB-TE VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        - UserCvlan (str(noVlanId | vlanId | allVlanId)): Sets the bridge filter for learned information for a single VLAN.
        - UserCvlanId (number): Sets the single VLAN identifier for filtering learned information.
        - UserCvlanPriority (number): Sets the single VLAN priority for filtering learned information.
        - UserCvlanTpId (str): Sets the single VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        - UserDelayMethod (str(oneWay | twoWay)): Sets the type of delay method to use.
        - UserDelayType (str(dm | dvm)): Sets the type of delay measurement to use.
        - UserDstMacAddress (str): Filters on the destination MAC address specified.
        - UserDstMepId (number): Sets the MEP identifier for use with userSelectDstMepById.
        - UserDstType (str(mepMac | mepId | mepMacAll | mepIdAll)): The user destination type.
        - UserLearnedInfoTimeOut (number): The interval in millisecond for the learned record to timeout. Default: 5000.
        - UserLossMethod (str(dualEnded | singleEnded)): NOT DEFINED
        - UserMdLevel (str(0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | allMd)): Filters on the specified MD level.
        - UserPbbTeDelayMethod (str(twoWay | oneWay)): Sets the PBB-TE type of delay method to use.
        - UserPbbTeDelayType (str(dm | dvm)): Sets the PBB-TE type of delay measurement to use.
        - UserPeriodicOamType (str(linkTrace | loopback | delayMeasurement | lossMeasurement)): Sets the type of periodic OAM.
        - UserSelectDstMepById (bool): If true, filters on the MEP by destination MEP identifier rather than by the MAC address. The MEP identifier is set in userDstMepId.
        - UserSelectSrcMepById (bool): If true, filters on the MEP by source MEP identifier rather than by the MAC address. The MEP identifier is set in userSrcMepId.
        - UserSendType (str(unicast | multicast)): Filters on the the send type.
        - UserShortMaName (str): Filters on the specified Short MA Name.
        - UserShortMaNameFormat (str(allFormats | primaryVid | characterString | twoOctetInteger | rfc2685VpnId)): Filters on the Short MA Name Format.
        - UserSrcMacAddress (str): Filters on the specified source MAC address.
        - UserSrcMepId (number): Sets the MEP identifier for use with userSelectSrcMepById.
        - UserSrcType (str(mepMac | mepId | mepMacAll | mepIdAll)): The user source type.
        - UserSvlan (str(noVlanId | vlanId | allVlanId)): Sets the bridge filter for learned information for a stacked VLAN.
        - UserSvlanId (number): Sets the stacked VLAN identifier for filtering learned information.
        - UserSvlanPriority (number): Sets the stacked VLAN priority for filtering learned information.
        - UserSvlanTpId (str): Sets the stacked VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        - UserTransactionId (number): The transaction identifier for the LTM packet if the configured MEP not found. Default: 1.
        - UserTtlInterval (number): Time to live value, in seconds. Default is 64.
        - UserUsabilityOption (str(manual | oneToOne | oneToAll | allToOne | allToAll)): User Option, one of Manual, One-to-One, One-to-All, All-to-One, All-to-All.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AisInterval=None, AllowCfmMaidFormatsInY1731=None, BridgeId=None, EnableAis=None, EnableOutOfSequenceDetection=None, Enabled=None, Encapsulation=None, EtherType=None, Function=None, GarbageCollectTime=None, OperationMode=None, UserBvlan=None, UserBvlanId=None, UserBvlanPriority=None, UserBvlanTpId=None, UserCvlan=None, UserCvlanId=None, UserCvlanPriority=None, UserCvlanTpId=None, UserDelayMethod=None, UserDelayType=None, UserDstMacAddress=None, UserDstMepId=None, UserDstType=None, UserLearnedInfoTimeOut=None, UserLossMethod=None, UserMdLevel=None, UserPbbTeDelayMethod=None, UserPbbTeDelayType=None, UserPeriodicOamType=None, UserSelectDstMepById=None, UserSelectSrcMepById=None, UserSendType=None, UserShortMaName=None, UserShortMaNameFormat=None, UserSrcMacAddress=None, UserSrcMepId=None, UserSrcType=None, UserSvlan=None, UserSvlanId=None, UserSvlanPriority=None, UserSvlanTpId=None, UserTransactionId=None, UserTtlInterval=None, UserUsabilityOption=None):
        """Adds a new bridge resource on the server and adds it to the container.

        Args
        ----
        - AisInterval (str(oneSec | oneMin)): The interval between AIS messages sent from this CFM bridge.
        - AllowCfmMaidFormatsInY1731 (bool): If true, allows to use CFM's MD Name types and Short MA Name types when the Operation Mode is Y.1731.
        - BridgeId (str): The bridge MAC address.
        - EnableAis (bool): If true, enables the use of AIS messages.
        - EnableOutOfSequenceDetection (bool): If true, enables the detection of out of sequence CCM messages.
        - Enabled (bool): If true, enables the CFM bridge.
        - Encapsulation (str(ethernet | llcSnap)): Sets the encapsulation type for the bridge.
        - EtherType (number): Selects the ether type for the bridge. The options are 0x8902 and 0x88E6.
        - Function (str(faultManagement | performanceMeasurement)): Determines the CFM function when operationMode is set to Y.1731.
        - GarbageCollectTime (number): Integer value denotes the interval for holding the expired database. Default 10 seconds.
        - OperationMode (str(cfm | y1731 | pbbTe)): Selects the type of CFM to enable.
        - UserBvlan (str(noVlanId | vlanId | allVlanId)): Sets the bridge filter for PBB-TE learned information for the VLAN.
        - UserBvlanId (number): Sets the PBB-TE VLAN identifier for filtering learned information.
        - UserBvlanPriority (number): Sets the PBB-TE VLAN priority for filtering learned information.
        - UserBvlanTpId (str): Sets the PBB-TE VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        - UserCvlan (str(noVlanId | vlanId | allVlanId)): Sets the bridge filter for learned information for a single VLAN.
        - UserCvlanId (number): Sets the single VLAN identifier for filtering learned information.
        - UserCvlanPriority (number): Sets the single VLAN priority for filtering learned information.
        - UserCvlanTpId (str): Sets the single VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        - UserDelayMethod (str(oneWay | twoWay)): Sets the type of delay method to use.
        - UserDelayType (str(dm | dvm)): Sets the type of delay measurement to use.
        - UserDstMacAddress (str): Filters on the destination MAC address specified.
        - UserDstMepId (number): Sets the MEP identifier for use with userSelectDstMepById.
        - UserDstType (str(mepMac | mepId | mepMacAll | mepIdAll)): The user destination type.
        - UserLearnedInfoTimeOut (number): The interval in millisecond for the learned record to timeout. Default: 5000.
        - UserLossMethod (str(dualEnded | singleEnded)): NOT DEFINED
        - UserMdLevel (str(0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | allMd)): Filters on the specified MD level.
        - UserPbbTeDelayMethod (str(twoWay | oneWay)): Sets the PBB-TE type of delay method to use.
        - UserPbbTeDelayType (str(dm | dvm)): Sets the PBB-TE type of delay measurement to use.
        - UserPeriodicOamType (str(linkTrace | loopback | delayMeasurement | lossMeasurement)): Sets the type of periodic OAM.
        - UserSelectDstMepById (bool): If true, filters on the MEP by destination MEP identifier rather than by the MAC address. The MEP identifier is set in userDstMepId.
        - UserSelectSrcMepById (bool): If true, filters on the MEP by source MEP identifier rather than by the MAC address. The MEP identifier is set in userSrcMepId.
        - UserSendType (str(unicast | multicast)): Filters on the the send type.
        - UserShortMaName (str): Filters on the specified Short MA Name.
        - UserShortMaNameFormat (str(allFormats | primaryVid | characterString | twoOctetInteger | rfc2685VpnId)): Filters on the Short MA Name Format.
        - UserSrcMacAddress (str): Filters on the specified source MAC address.
        - UserSrcMepId (number): Sets the MEP identifier for use with userSelectSrcMepById.
        - UserSrcType (str(mepMac | mepId | mepMacAll | mepIdAll)): The user source type.
        - UserSvlan (str(noVlanId | vlanId | allVlanId)): Sets the bridge filter for learned information for a stacked VLAN.
        - UserSvlanId (number): Sets the stacked VLAN identifier for filtering learned information.
        - UserSvlanPriority (number): Sets the stacked VLAN priority for filtering learned information.
        - UserSvlanTpId (str): Sets the stacked VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        - UserTransactionId (number): The transaction identifier for the LTM packet if the configured MEP not found. Default: 1.
        - UserTtlInterval (number): Time to live value, in seconds. Default is 64.
        - UserUsabilityOption (str(manual | oneToOne | oneToAll | allToOne | allToAll)): User Option, one of Manual, One-to-One, One-to-All, All-to-One, All-to-All.

        Returns
        -------
        - self: This instance with all currently retrieved bridge resources using find and the newly added bridge resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bridge resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AisInterval=None, AllowCfmMaidFormatsInY1731=None, BridgeId=None, DelayLearnedErrorString=None, EnableAis=None, EnableOutOfSequenceDetection=None, Enabled=None, Encapsulation=None, EtherType=None, Function=None, GarbageCollectTime=None, IsAisLearnedInfoRefreshed=None, IsCcmLearnedInfoRefreshed=None, IsDelayLearnedConfigMep=None, IsDelayLearnedPacketSent=None, IsDelayMeasurementLearnedInfoRefreshed=None, IsLbLearnedConfigMep=None, IsLbLearnedPacketSent=None, IsLckLearnedInfoRefreshed=None, IsLinkTraceLearnedInfoRefreshed=None, IsLoopbackLearnedInfoRefreshed=None, IsLossMeasurementLearnedInfoPacketSent=None, IsLossMeasurementLearnedInfoRefreshed=None, IsLtLearnedConfigMep=None, IsLtLearnedPacketSent=None, IsPbbTeCcmLearnedInfoRefreshed=None, IsPbbTeDelayLearnedConfigMep=None, IsPbbTeDelayLearnedInfoRefreshed=None, IsPbbTeDelayLearnedPacketSent=None, IsPbbTeLbLearnedConfigMep=None, IsPbbTeLbLearnedInfoRefreshed=None, IsPbbTeLbLearnedPacketSent=None, IsPeriodicOamLearnedInfoRefreshed=None, IsTstLearnedInfoRefreshed=None, LbLearnedErrorString=None, LossMeasurementLearnedInfoErrorString=None, LtLearnedErrorString=None, OperationMode=None, PbbTeDelayLearnedErrorString=None, PbbTeLbLearnedErrorString=None, UserBvlan=None, UserBvlanId=None, UserBvlanPriority=None, UserBvlanTpId=None, UserCvlan=None, UserCvlanId=None, UserCvlanPriority=None, UserCvlanTpId=None, UserDelayMethod=None, UserDelayType=None, UserDstMacAddress=None, UserDstMepId=None, UserDstType=None, UserLearnedInfoTimeOut=None, UserLossMethod=None, UserMdLevel=None, UserPbbTeDelayMethod=None, UserPbbTeDelayType=None, UserPeriodicOamType=None, UserSelectDstMepById=None, UserSelectSrcMepById=None, UserSendType=None, UserShortMaName=None, UserShortMaNameFormat=None, UserSrcMacAddress=None, UserSrcMepId=None, UserSrcType=None, UserSvlan=None, UserSvlanId=None, UserSvlanPriority=None, UserSvlanTpId=None, UserTransactionId=None, UserTtlInterval=None, UserUsabilityOption=None):
        """Finds and retrieves bridge resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bridge resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bridge resources from the server.

        Args
        ----
        - AisInterval (str(oneSec | oneMin)): The interval between AIS messages sent from this CFM bridge.
        - AllowCfmMaidFormatsInY1731 (bool): If true, allows to use CFM's MD Name types and Short MA Name types when the Operation Mode is Y.1731.
        - BridgeId (str): The bridge MAC address.
        - DelayLearnedErrorString (str): (read only) The learned error string for the delay measurement.
        - EnableAis (bool): If true, enables the use of AIS messages.
        - EnableOutOfSequenceDetection (bool): If true, enables the detection of out of sequence CCM messages.
        - Enabled (bool): If true, enables the CFM bridge.
        - Encapsulation (str(ethernet | llcSnap)): Sets the encapsulation type for the bridge.
        - EtherType (number): Selects the ether type for the bridge. The options are 0x8902 and 0x88E6.
        - Function (str(faultManagement | performanceMeasurement)): Determines the CFM function when operationMode is set to Y.1731.
        - GarbageCollectTime (number): Integer value denotes the interval for holding the expired database. Default 10 seconds.
        - IsAisLearnedInfoRefreshed (bool): NOT DEFINED
        - IsCcmLearnedInfoRefreshed (bool): (read only) If true, the CCM learned information is current.
        - IsDelayLearnedConfigMep (bool): (read only) If true, indicates if the configured MEP for the delay measurement was found.
        - IsDelayLearnedPacketSent (bool): (read only) If true, indicates the delay packet was sent.
        - IsDelayMeasurementLearnedInfoRefreshed (bool): (read only) If true, the learned delay information is current.
        - IsLbLearnedConfigMep (bool): (read only) If true, indicates if the configured MEP for the loopback measurement was found.
        - IsLbLearnedPacketSent (bool): (read only) If true, indicates the loopback packet was sent.
        - IsLckLearnedInfoRefreshed (bool): NOT DEFINED
        - IsLinkTraceLearnedInfoRefreshed (bool): (read only) If true, the learned link trace information is current.
        - IsLoopbackLearnedInfoRefreshed (bool): (read only) If true, the learned loopback information is current.
        - IsLossMeasurementLearnedInfoPacketSent (bool): NOT DEFINED
        - IsLossMeasurementLearnedInfoRefreshed (bool): NOT DEFINED
        - IsLtLearnedConfigMep (bool): (read only) If true, indicates if the configured MEP for the link trace measurement was found.
        - IsLtLearnedPacketSent (bool): (read only) If true, indicates the link trace packet was sent.
        - IsPbbTeCcmLearnedInfoRefreshed (bool): (read only) If true, the learned PBB-TE CCM information is current.
        - IsPbbTeDelayLearnedConfigMep (bool): (read only) If true, indicates if the configured MEP for the PBB-TE delay measurement was found.
        - IsPbbTeDelayLearnedInfoRefreshed (bool): (read only) If true, the learned PBB-TE delay information is current.
        - IsPbbTeDelayLearnedPacketSent (bool): (read only) If true, indicates the PBB-TE delay packet was sent.
        - IsPbbTeLbLearnedConfigMep (bool): (read only) If true, indicates if the configured MEP for the PBB-TE loopback measurement was found.
        - IsPbbTeLbLearnedInfoRefreshed (bool): (read only) If true, the PBB-TE learned loopback information is current.
        - IsPbbTeLbLearnedPacketSent (bool): (read only) If true, indicates the PBB-TE loopback packet was sent.
        - IsPeriodicOamLearnedInfoRefreshed (bool): If true, the periodic OAM learned information is up-to-date.
        - IsTstLearnedInfoRefreshed (bool): NOT DEFINED
        - LbLearnedErrorString (str): (read only) The learned error string for the loopback measurement.
        - LossMeasurementLearnedInfoErrorString (str): NOT DEFINED
        - LtLearnedErrorString (str): (read only) The learned error string for the link trace measurement.
        - OperationMode (str(cfm | y1731 | pbbTe)): Selects the type of CFM to enable.
        - PbbTeDelayLearnedErrorString (str): (read only) The learned error string for the PBB-TE delay measurement.
        - PbbTeLbLearnedErrorString (str): (read only) The learned error string for the PBB-TE loopback measurement.
        - UserBvlan (str(noVlanId | vlanId | allVlanId)): Sets the bridge filter for PBB-TE learned information for the VLAN.
        - UserBvlanId (number): Sets the PBB-TE VLAN identifier for filtering learned information.
        - UserBvlanPriority (number): Sets the PBB-TE VLAN priority for filtering learned information.
        - UserBvlanTpId (str): Sets the PBB-TE VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        - UserCvlan (str(noVlanId | vlanId | allVlanId)): Sets the bridge filter for learned information for a single VLAN.
        - UserCvlanId (number): Sets the single VLAN identifier for filtering learned information.
        - UserCvlanPriority (number): Sets the single VLAN priority for filtering learned information.
        - UserCvlanTpId (str): Sets the single VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        - UserDelayMethod (str(oneWay | twoWay)): Sets the type of delay method to use.
        - UserDelayType (str(dm | dvm)): Sets the type of delay measurement to use.
        - UserDstMacAddress (str): Filters on the destination MAC address specified.
        - UserDstMepId (number): Sets the MEP identifier for use with userSelectDstMepById.
        - UserDstType (str(mepMac | mepId | mepMacAll | mepIdAll)): The user destination type.
        - UserLearnedInfoTimeOut (number): The interval in millisecond for the learned record to timeout. Default: 5000.
        - UserLossMethod (str(dualEnded | singleEnded)): NOT DEFINED
        - UserMdLevel (str(0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | allMd)): Filters on the specified MD level.
        - UserPbbTeDelayMethod (str(twoWay | oneWay)): Sets the PBB-TE type of delay method to use.
        - UserPbbTeDelayType (str(dm | dvm)): Sets the PBB-TE type of delay measurement to use.
        - UserPeriodicOamType (str(linkTrace | loopback | delayMeasurement | lossMeasurement)): Sets the type of periodic OAM.
        - UserSelectDstMepById (bool): If true, filters on the MEP by destination MEP identifier rather than by the MAC address. The MEP identifier is set in userDstMepId.
        - UserSelectSrcMepById (bool): If true, filters on the MEP by source MEP identifier rather than by the MAC address. The MEP identifier is set in userSrcMepId.
        - UserSendType (str(unicast | multicast)): Filters on the the send type.
        - UserShortMaName (str): Filters on the specified Short MA Name.
        - UserShortMaNameFormat (str(allFormats | primaryVid | characterString | twoOctetInteger | rfc2685VpnId)): Filters on the Short MA Name Format.
        - UserSrcMacAddress (str): Filters on the specified source MAC address.
        - UserSrcMepId (number): Sets the MEP identifier for use with userSelectSrcMepById.
        - UserSrcType (str(mepMac | mepId | mepMacAll | mepIdAll)): The user source type.
        - UserSvlan (str(noVlanId | vlanId | allVlanId)): Sets the bridge filter for learned information for a stacked VLAN.
        - UserSvlanId (number): Sets the stacked VLAN identifier for filtering learned information.
        - UserSvlanPriority (number): Sets the stacked VLAN priority for filtering learned information.
        - UserSvlanTpId (str): Sets the stacked VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        - UserTransactionId (number): The transaction identifier for the LTM packet if the configured MEP not found. Default: 1.
        - UserTtlInterval (number): Time to live value, in seconds. Default is 64.
        - UserUsabilityOption (str(manual | oneToOne | oneToAll | allToOne | allToAll)): User Option, one of Manual, One-to-One, One-to-All, All-to-One, All-to-All.

        Returns
        -------
        - self: This instance with matching bridge resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bridge data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bridge resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshAisLearnedInfo(self):
        """Executes the refreshAisLearnedInfo operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshAisLearnedInfo', payload=payload, response_object=None)

    def RefreshCcmLearnedInfo(self):
        """Executes the refreshCcmLearnedInfo operation on the server.

        This command is used to refresh the learned CCM information on the bridge.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshCcmLearnedInfo', payload=payload, response_object=None)

    def RefreshLckLearnedInfo(self):
        """Executes the refreshLckLearnedInfo operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLckLearnedInfo', payload=payload, response_object=None)

    def RefreshTstLearnedInfo(self):
        """Executes the refreshTstLearnedInfo operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshTstLearnedInfo', payload=payload, response_object=None)

    def StartDelayMeasurement(self):
        """Executes the startDelayMeasurement operation on the server.

        This command is used to refresh the learned CFM ITU information on this bridge.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('startDelayMeasurement', payload=payload, response_object=None)

    def StartLinkTrace(self):
        """Executes the startLinkTrace operation on the server.

        This command is used to refresh the learned CFM LT information on this bridge.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('startLinkTrace', payload=payload, response_object=None)

    def StartLoopback(self):
        """Executes the startLoopback operation on the server.

        This command is used to refresh the learned CFM LB information on this bridge.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('startLoopback', payload=payload, response_object=None)

    def StartLossMeasurement(self):
        """Executes the startLossMeasurement operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('startLossMeasurement', payload=payload, response_object=None)

    def UpdatePeriodicOamLearnedInfo(self):
        """Executes the updatePeriodicOamLearnedInfo operation on the server.

        This command updates the periodic OAM learned information on this bridge.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('updatePeriodicOamLearnedInfo', payload=payload, response_object=None)
