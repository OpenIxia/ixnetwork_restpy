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


class Bridge(Base):
    """This object contains the configuration for the CFM bridge.
    The Bridge class encapsulates a list of bridge resources that are managed by the user.
    A list of resources can be retrieved from the server using the Bridge.find() method.
    The list can be managed by using the Bridge.add() and Bridge.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bridge'

    def __init__(self, parent):
        super(Bridge, self).__init__(parent)

    @property
    def AisLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.aislearnedinfo_84ec55883717f43c98f87583a7ace177.AisLearnedInfo): An instance of the AisLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.aislearnedinfo_84ec55883717f43c98f87583a7ace177 import AisLearnedInfo
        return AisLearnedInfo(self)

    @property
    def CcmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ccmlearnedinfo_9baaacc2508aea99f5324e794c7430a0.CcmLearnedInfo): An instance of the CcmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ccmlearnedinfo_9baaacc2508aea99f5324e794c7430a0 import CcmLearnedInfo
        return CcmLearnedInfo(self)

    @property
    def CustomTlvs(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtlvs_b679b39bf7b4a713be28d7db7aa86bed.CustomTlvs): An instance of the CustomTlvs class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtlvs_b679b39bf7b4a713be28d7db7aa86bed import CustomTlvs
        return CustomTlvs(self)

    @property
    def DelayLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.delaylearnedinfo_79b4c3856835e73a34c390457efa6ad2.DelayLearnedInfo): An instance of the DelayLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.delaylearnedinfo_79b4c3856835e73a34c390457efa6ad2 import DelayLearnedInfo
        return DelayLearnedInfo(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_d0634a8f381feecfae06836434390e56.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_d0634a8f381feecfae06836434390e56 import Interface
        return Interface(self)

    @property
    def LbLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lblearnedinfo_ec56ce29319e76b0e1d8451951f052e6.LbLearnedInfo): An instance of the LbLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lblearnedinfo_ec56ce29319e76b0e1d8451951f052e6 import LbLearnedInfo
        return LbLearnedInfo(self)

    @property
    def LckLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lcklearnedinfo_64ce1c0413a6b36286c3aec03a316b5f.LckLearnedInfo): An instance of the LckLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lcklearnedinfo_64ce1c0413a6b36286c3aec03a316b5f import LckLearnedInfo
        return LckLearnedInfo(self)

    @property
    def Link(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_c8cd7dc0b25bdfc24496bef1811ac785.Link): An instance of the Link class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_c8cd7dc0b25bdfc24496bef1811ac785 import Link
        return Link(self)

    @property
    def LossLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.losslearnedinfo_c21d89e38fc50e907c08da07460ab8cb.LossLearnedInfo): An instance of the LossLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.losslearnedinfo_c21d89e38fc50e907c08da07460ab8cb import LossLearnedInfo
        return LossLearnedInfo(self)

    @property
    def LtLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedinfo_c11e1d991569cbe84098c437e3d8f560.LtLearnedInfo): An instance of the LtLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedinfo_c11e1d991569cbe84098c437e3d8f560 import LtLearnedInfo
        return LtLearnedInfo(self)

    @property
    def MdLevel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mdlevel_0dfd292e7b0b04015e11a57954a65648.MdLevel): An instance of the MdLevel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mdlevel_0dfd292e7b0b04015e11a57954a65648 import MdLevel
        return MdLevel(self)

    @property
    def Mp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mp_c258ba0d39201ea9310735882b0d66d6.Mp): An instance of the Mp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mp_c258ba0d39201ea9310735882b0d66d6 import Mp
        return Mp(self)

    @property
    def PbbTeCcmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteccmlearnedinfo_75bd8f81e009c34e0a3550002dd9b237.PbbTeCcmLearnedInfo): An instance of the PbbTeCcmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteccmlearnedinfo_75bd8f81e009c34e0a3550002dd9b237 import PbbTeCcmLearnedInfo
        return PbbTeCcmLearnedInfo(self)

    @property
    def PbbTeDelayLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbtedelaylearnedinfo_f3988daa95355a31c260690daaf605e5.PbbTeDelayLearnedInfo): An instance of the PbbTeDelayLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbtedelaylearnedinfo_f3988daa95355a31c260690daaf605e5 import PbbTeDelayLearnedInfo
        return PbbTeDelayLearnedInfo(self)

    @property
    def PbbTeLbLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbtelblearnedinfo_cedbd678dfd3ca6a787f0562fb5e7e27.PbbTeLbLearnedInfo): An instance of the PbbTeLbLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbtelblearnedinfo_cedbd678dfd3ca6a787f0562fb5e7e27 import PbbTeLbLearnedInfo
        return PbbTeLbLearnedInfo(self)

    @property
    def PbbTeLtLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteltlearnedinfo_93cf79776236c88ede7714d3c82d34f5.PbbTeLtLearnedInfo): An instance of the PbbTeLtLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteltlearnedinfo_93cf79776236c88ede7714d3c82d34f5 import PbbTeLtLearnedInfo
        return PbbTeLtLearnedInfo(self)

    @property
    def PbbTePeriodicOamDmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamdmlearnedinfo_99ec35e7a9f94b3f1e6b8ae45f1747df.PbbTePeriodicOamDmLearnedInfo): An instance of the PbbTePeriodicOamDmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamdmlearnedinfo_99ec35e7a9f94b3f1e6b8ae45f1747df import PbbTePeriodicOamDmLearnedInfo
        return PbbTePeriodicOamDmLearnedInfo(self)

    @property
    def PbbTePeriodicOamLbLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamlblearnedinfo_3f6ce689cc3a6b8f44b7cce003e299ac.PbbTePeriodicOamLbLearnedInfo): An instance of the PbbTePeriodicOamLbLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamlblearnedinfo_3f6ce689cc3a6b8f44b7cce003e299ac import PbbTePeriodicOamLbLearnedInfo
        return PbbTePeriodicOamLbLearnedInfo(self)

    @property
    def PbbTePeriodicOamLtLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamltlearnedinfo_ff71646600cf4e67f1a4415bd52f2eda.PbbTePeriodicOamLtLearnedInfo): An instance of the PbbTePeriodicOamLtLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamltlearnedinfo_ff71646600cf4e67f1a4415bd52f2eda import PbbTePeriodicOamLtLearnedInfo
        return PbbTePeriodicOamLtLearnedInfo(self)

    @property
    def PeriodicOamDmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamdmlearnedinfo_83bc258f0215cd29e5da43e42d96747e.PeriodicOamDmLearnedInfo): An instance of the PeriodicOamDmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamdmlearnedinfo_83bc258f0215cd29e5da43e42d96747e import PeriodicOamDmLearnedInfo
        return PeriodicOamDmLearnedInfo(self)

    @property
    def PeriodicOamLbLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamlblearnedinfo_684d1d460277cd2357b55dfd08d09a75.PeriodicOamLbLearnedInfo): An instance of the PeriodicOamLbLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamlblearnedinfo_684d1d460277cd2357b55dfd08d09a75 import PeriodicOamLbLearnedInfo
        return PeriodicOamLbLearnedInfo(self)

    @property
    def PeriodicOamLmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamlmlearnedinfo_3fc327b8fe3fa3de03d90b861d17730b.PeriodicOamLmLearnedInfo): An instance of the PeriodicOamLmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamlmlearnedinfo_3fc327b8fe3fa3de03d90b861d17730b import PeriodicOamLmLearnedInfo
        return PeriodicOamLmLearnedInfo(self)

    @property
    def PeriodicOamLtLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamltlearnedinfo_417818ba85e00c8d316815462a5a24ac.PeriodicOamLtLearnedInfo): An instance of the PeriodicOamLtLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamltlearnedinfo_417818ba85e00c8d316815462a5a24ac import PeriodicOamLtLearnedInfo
        return PeriodicOamLtLearnedInfo(self)

    @property
    def Trunk(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trunk_228a8a189c28ecc4e797686d931314bc.Trunk): An instance of the Trunk class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trunk_228a8a189c28ecc4e797686d931314bc import Trunk
        return Trunk(self)

    @property
    def TstLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tstlearnedinfo_dec6fd55f89d9eadf89ea66614d38b22.TstLearnedInfo): An instance of the TstLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tstlearnedinfo_dec6fd55f89d9eadf89ea66614d38b22 import TstLearnedInfo
        return TstLearnedInfo(self)

    @property
    def Vlans(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vlans_53ae5448a828df6c6fcd2f6b03f79ed9.Vlans): An instance of the Vlans class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vlans_53ae5448a828df6c6fcd2f6b03f79ed9 import Vlans
        return Vlans(self)

    @property
    def AisInterval(self):
        """DEPRECATED 
        Returns
        -------
        - str(oneSec | oneMin): The interval between AIS messages sent from this CFM bridge.
        """
        return self._get_attribute('aisInterval')
    @AisInterval.setter
    def AisInterval(self, value):
        self._set_attribute('aisInterval', value)

    @property
    def AllowCfmMaidFormatsInY1731(self):
        """
        Returns
        -------
        - bool: If true, allows to use CFM's MD Name types and Short MA Name types when the Operation Mode is Y.1731.
        """
        return self._get_attribute('allowCfmMaidFormatsInY1731')
    @AllowCfmMaidFormatsInY1731.setter
    def AllowCfmMaidFormatsInY1731(self, value):
        self._set_attribute('allowCfmMaidFormatsInY1731', value)

    @property
    def BridgeId(self):
        """
        Returns
        -------
        - str: The bridge MAC address.
        """
        return self._get_attribute('bridgeId')
    @BridgeId.setter
    def BridgeId(self, value):
        self._set_attribute('bridgeId', value)

    @property
    def DelayLearnedErrorString(self):
        """
        Returns
        -------
        - str: (read only) The learned error string for the delay measurement.
        """
        return self._get_attribute('delayLearnedErrorString')

    @property
    def EnableAis(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If true, enables the use of AIS messages.
        """
        return self._get_attribute('enableAis')
    @EnableAis.setter
    def EnableAis(self, value):
        self._set_attribute('enableAis', value)

    @property
    def EnableOutOfSequenceDetection(self):
        """
        Returns
        -------
        - bool: If true, enables the detection of out of sequence CCM messages.
        """
        return self._get_attribute('enableOutOfSequenceDetection')
    @EnableOutOfSequenceDetection.setter
    def EnableOutOfSequenceDetection(self, value):
        self._set_attribute('enableOutOfSequenceDetection', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, enables the CFM bridge.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def Encapsulation(self):
        """
        Returns
        -------
        - str(ethernet | llcSnap): Sets the encapsulation type for the bridge.
        """
        return self._get_attribute('encapsulation')
    @Encapsulation.setter
    def Encapsulation(self, value):
        self._set_attribute('encapsulation', value)

    @property
    def EtherType(self):
        """
        Returns
        -------
        - number: Selects the ether type for the bridge. The options are 0x8902 and 0x88E6.
        """
        return self._get_attribute('etherType')
    @EtherType.setter
    def EtherType(self, value):
        self._set_attribute('etherType', value)

    @property
    def Function(self):
        """DEPRECATED 
        Returns
        -------
        - str(faultManagement | performanceMeasurement): Determines the CFM function when operationMode is set to Y.1731.
        """
        return self._get_attribute('function')
    @Function.setter
    def Function(self, value):
        self._set_attribute('function', value)

    @property
    def GarbageCollectTime(self):
        """
        Returns
        -------
        - number: Integer value denotes the interval for holding the expired database. Default 10 seconds.
        """
        return self._get_attribute('garbageCollectTime')
    @GarbageCollectTime.setter
    def GarbageCollectTime(self, value):
        self._set_attribute('garbageCollectTime', value)

    @property
    def IsAisLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('isAisLearnedInfoRefreshed')

    @property
    def IsCcmLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the CCM learned information is current.
        """
        return self._get_attribute('isCcmLearnedInfoRefreshed')

    @property
    def IsDelayLearnedConfigMep(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the delay measurement was found.
        """
        return self._get_attribute('isDelayLearnedConfigMep')

    @property
    def IsDelayLearnedPacketSent(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates the delay packet was sent.
        """
        return self._get_attribute('isDelayLearnedPacketSent')

    @property
    def IsDelayMeasurementLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the learned delay information is current.
        """
        return self._get_attribute('isDelayMeasurementLearnedInfoRefreshed')

    @property
    def IsLbLearnedConfigMep(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the loopback measurement was found.
        """
        return self._get_attribute('isLbLearnedConfigMep')

    @property
    def IsLbLearnedPacketSent(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates the loopback packet was sent.
        """
        return self._get_attribute('isLbLearnedPacketSent')

    @property
    def IsLckLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('isLckLearnedInfoRefreshed')

    @property
    def IsLinkTraceLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the learned link trace information is current.
        """
        return self._get_attribute('isLinkTraceLearnedInfoRefreshed')

    @property
    def IsLoopbackLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the learned loopback information is current.
        """
        return self._get_attribute('isLoopbackLearnedInfoRefreshed')

    @property
    def IsLossMeasurementLearnedInfoPacketSent(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('isLossMeasurementLearnedInfoPacketSent')

    @property
    def IsLossMeasurementLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('isLossMeasurementLearnedInfoRefreshed')

    @property
    def IsLtLearnedConfigMep(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the link trace measurement was found.
        """
        return self._get_attribute('isLtLearnedConfigMep')

    @property
    def IsLtLearnedPacketSent(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates the link trace packet was sent.
        """
        return self._get_attribute('isLtLearnedPacketSent')

    @property
    def IsPbbTeCcmLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the learned PBB-TE CCM information is current.
        """
        return self._get_attribute('isPbbTeCcmLearnedInfoRefreshed')

    @property
    def IsPbbTeDelayLearnedConfigMep(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the PBB-TE delay measurement was found.
        """
        return self._get_attribute('isPbbTeDelayLearnedConfigMep')

    @property
    def IsPbbTeDelayLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the learned PBB-TE delay information is current.
        """
        return self._get_attribute('isPbbTeDelayLearnedInfoRefreshed')

    @property
    def IsPbbTeDelayLearnedPacketSent(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates the PBB-TE delay packet was sent.
        """
        return self._get_attribute('isPbbTeDelayLearnedPacketSent')

    @property
    def IsPbbTeLbLearnedConfigMep(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the PBB-TE loopback measurement was found.
        """
        return self._get_attribute('isPbbTeLbLearnedConfigMep')

    @property
    def IsPbbTeLbLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: (read only) If true, the PBB-TE learned loopback information is current.
        """
        return self._get_attribute('isPbbTeLbLearnedInfoRefreshed')

    @property
    def IsPbbTeLbLearnedPacketSent(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates the PBB-TE loopback packet was sent.
        """
        return self._get_attribute('isPbbTeLbLearnedPacketSent')

    @property
    def IsPeriodicOamLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: If true, the periodic OAM learned information is up-to-date.
        """
        return self._get_attribute('isPeriodicOamLearnedInfoRefreshed')

    @property
    def IsTstLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('isTstLearnedInfoRefreshed')

    @property
    def LbLearnedErrorString(self):
        """
        Returns
        -------
        - str: (read only) The learned error string for the loopback measurement.
        """
        return self._get_attribute('lbLearnedErrorString')

    @property
    def LossMeasurementLearnedInfoErrorString(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('lossMeasurementLearnedInfoErrorString')

    @property
    def LtLearnedErrorString(self):
        """
        Returns
        -------
        - str: (read only) The learned error string for the link trace measurement.
        """
        return self._get_attribute('ltLearnedErrorString')

    @property
    def OperationMode(self):
        """
        Returns
        -------
        - str(cfm | y1731 | pbbTe): Selects the type of CFM to enable.
        """
        return self._get_attribute('operationMode')
    @OperationMode.setter
    def OperationMode(self, value):
        self._set_attribute('operationMode', value)

    @property
    def PbbTeDelayLearnedErrorString(self):
        """
        Returns
        -------
        - str: (read only) The learned error string for the PBB-TE delay measurement.
        """
        return self._get_attribute('pbbTeDelayLearnedErrorString')

    @property
    def PbbTeLbLearnedErrorString(self):
        """
        Returns
        -------
        - str: (read only) The learned error string for the PBB-TE loopback measurement.
        """
        return self._get_attribute('pbbTeLbLearnedErrorString')

    @property
    def UserBvlan(self):
        """
        Returns
        -------
        - str(noVlanId | vlanId | allVlanId): Sets the bridge filter for PBB-TE learned information for the VLAN.
        """
        return self._get_attribute('userBvlan')
    @UserBvlan.setter
    def UserBvlan(self, value):
        self._set_attribute('userBvlan', value)

    @property
    def UserBvlanId(self):
        """
        Returns
        -------
        - number: Sets the PBB-TE VLAN identifier for filtering learned information.
        """
        return self._get_attribute('userBvlanId')
    @UserBvlanId.setter
    def UserBvlanId(self, value):
        self._set_attribute('userBvlanId', value)

    @property
    def UserBvlanPriority(self):
        """
        Returns
        -------
        - number: Sets the PBB-TE VLAN priority for filtering learned information.
        """
        return self._get_attribute('userBvlanPriority')
    @UserBvlanPriority.setter
    def UserBvlanPriority(self, value):
        self._set_attribute('userBvlanPriority', value)

    @property
    def UserBvlanTpId(self):
        """
        Returns
        -------
        - str: Sets the PBB-TE VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        """
        return self._get_attribute('userBvlanTpId')
    @UserBvlanTpId.setter
    def UserBvlanTpId(self, value):
        self._set_attribute('userBvlanTpId', value)

    @property
    def UserCvlan(self):
        """
        Returns
        -------
        - str(noVlanId | vlanId | allVlanId): Sets the bridge filter for learned information for a single VLAN.
        """
        return self._get_attribute('userCvlan')
    @UserCvlan.setter
    def UserCvlan(self, value):
        self._set_attribute('userCvlan', value)

    @property
    def UserCvlanId(self):
        """
        Returns
        -------
        - number: Sets the single VLAN identifier for filtering learned information.
        """
        return self._get_attribute('userCvlanId')
    @UserCvlanId.setter
    def UserCvlanId(self, value):
        self._set_attribute('userCvlanId', value)

    @property
    def UserCvlanPriority(self):
        """
        Returns
        -------
        - number: Sets the single VLAN priority for filtering learned information.
        """
        return self._get_attribute('userCvlanPriority')
    @UserCvlanPriority.setter
    def UserCvlanPriority(self, value):
        self._set_attribute('userCvlanPriority', value)

    @property
    def UserCvlanTpId(self):
        """
        Returns
        -------
        - str: Sets the single VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        """
        return self._get_attribute('userCvlanTpId')
    @UserCvlanTpId.setter
    def UserCvlanTpId(self, value):
        self._set_attribute('userCvlanTpId', value)

    @property
    def UserDelayMethod(self):
        """
        Returns
        -------
        - str(oneWay | twoWay): Sets the type of delay method to use.
        """
        return self._get_attribute('userDelayMethod')
    @UserDelayMethod.setter
    def UserDelayMethod(self, value):
        self._set_attribute('userDelayMethod', value)

    @property
    def UserDelayType(self):
        """
        Returns
        -------
        - str(dm | dvm): Sets the type of delay measurement to use.
        """
        return self._get_attribute('userDelayType')
    @UserDelayType.setter
    def UserDelayType(self, value):
        self._set_attribute('userDelayType', value)

    @property
    def UserDstMacAddress(self):
        """
        Returns
        -------
        - str: Filters on the destination MAC address specified.
        """
        return self._get_attribute('userDstMacAddress')
    @UserDstMacAddress.setter
    def UserDstMacAddress(self, value):
        self._set_attribute('userDstMacAddress', value)

    @property
    def UserDstMepId(self):
        """
        Returns
        -------
        - number: Sets the MEP identifier for use with userSelectDstMepById.
        """
        return self._get_attribute('userDstMepId')
    @UserDstMepId.setter
    def UserDstMepId(self, value):
        self._set_attribute('userDstMepId', value)

    @property
    def UserDstType(self):
        """
        Returns
        -------
        - str(mepMac | mepId | mepMacAll | mepIdAll): The user destination type.
        """
        return self._get_attribute('userDstType')
    @UserDstType.setter
    def UserDstType(self, value):
        self._set_attribute('userDstType', value)

    @property
    def UserLearnedInfoTimeOut(self):
        """
        Returns
        -------
        - number: The interval in millisecond for the learned record to timeout. Default: 5000.
        """
        return self._get_attribute('userLearnedInfoTimeOut')
    @UserLearnedInfoTimeOut.setter
    def UserLearnedInfoTimeOut(self, value):
        self._set_attribute('userLearnedInfoTimeOut', value)

    @property
    def UserLossMethod(self):
        """
        Returns
        -------
        - str(dualEnded | singleEnded): NOT DEFINED
        """
        return self._get_attribute('userLossMethod')
    @UserLossMethod.setter
    def UserLossMethod(self, value):
        self._set_attribute('userLossMethod', value)

    @property
    def UserMdLevel(self):
        """
        Returns
        -------
        - str(0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | allMd): Filters on the specified MD level.
        """
        return self._get_attribute('userMdLevel')
    @UserMdLevel.setter
    def UserMdLevel(self, value):
        self._set_attribute('userMdLevel', value)

    @property
    def UserPbbTeDelayMethod(self):
        """
        Returns
        -------
        - str(twoWay | oneWay): Sets the PBB-TE type of delay method to use.
        """
        return self._get_attribute('userPbbTeDelayMethod')
    @UserPbbTeDelayMethod.setter
    def UserPbbTeDelayMethod(self, value):
        self._set_attribute('userPbbTeDelayMethod', value)

    @property
    def UserPbbTeDelayType(self):
        """
        Returns
        -------
        - str(dm | dvm): Sets the PBB-TE type of delay measurement to use.
        """
        return self._get_attribute('userPbbTeDelayType')
    @UserPbbTeDelayType.setter
    def UserPbbTeDelayType(self, value):
        self._set_attribute('userPbbTeDelayType', value)

    @property
    def UserPeriodicOamType(self):
        """
        Returns
        -------
        - str(linkTrace | loopback | delayMeasurement | lossMeasurement): Sets the type of periodic OAM.
        """
        return self._get_attribute('userPeriodicOamType')
    @UserPeriodicOamType.setter
    def UserPeriodicOamType(self, value):
        self._set_attribute('userPeriodicOamType', value)

    @property
    def UserSelectDstMepById(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If true, filters on the MEP by destination MEP identifier rather than by the MAC address. The MEP identifier is set in userDstMepId.
        """
        return self._get_attribute('userSelectDstMepById')
    @UserSelectDstMepById.setter
    def UserSelectDstMepById(self, value):
        self._set_attribute('userSelectDstMepById', value)

    @property
    def UserSelectSrcMepById(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If true, filters on the MEP by source MEP identifier rather than by the MAC address. The MEP identifier is set in userSrcMepId.
        """
        return self._get_attribute('userSelectSrcMepById')
    @UserSelectSrcMepById.setter
    def UserSelectSrcMepById(self, value):
        self._set_attribute('userSelectSrcMepById', value)

    @property
    def UserSendType(self):
        """
        Returns
        -------
        - str(unicast | multicast): Filters on the the send type.
        """
        return self._get_attribute('userSendType')
    @UserSendType.setter
    def UserSendType(self, value):
        self._set_attribute('userSendType', value)

    @property
    def UserShortMaName(self):
        """
        Returns
        -------
        - str: Filters on the specified Short MA Name.
        """
        return self._get_attribute('userShortMaName')
    @UserShortMaName.setter
    def UserShortMaName(self, value):
        self._set_attribute('userShortMaName', value)

    @property
    def UserShortMaNameFormat(self):
        """
        Returns
        -------
        - str(allFormats | primaryVid | characterString | twoOctetInteger | rfc2685VpnId): Filters on the Short MA Name Format.
        """
        return self._get_attribute('userShortMaNameFormat')
    @UserShortMaNameFormat.setter
    def UserShortMaNameFormat(self, value):
        self._set_attribute('userShortMaNameFormat', value)

    @property
    def UserSrcMacAddress(self):
        """
        Returns
        -------
        - str: Filters on the specified source MAC address.
        """
        return self._get_attribute('userSrcMacAddress')
    @UserSrcMacAddress.setter
    def UserSrcMacAddress(self, value):
        self._set_attribute('userSrcMacAddress', value)

    @property
    def UserSrcMepId(self):
        """
        Returns
        -------
        - number: Sets the MEP identifier for use with userSelectSrcMepById.
        """
        return self._get_attribute('userSrcMepId')
    @UserSrcMepId.setter
    def UserSrcMepId(self, value):
        self._set_attribute('userSrcMepId', value)

    @property
    def UserSrcType(self):
        """
        Returns
        -------
        - str(mepMac | mepId | mepMacAll | mepIdAll): The user source type.
        """
        return self._get_attribute('userSrcType')
    @UserSrcType.setter
    def UserSrcType(self, value):
        self._set_attribute('userSrcType', value)

    @property
    def UserSvlan(self):
        """
        Returns
        -------
        - str(noVlanId | vlanId | allVlanId): Sets the bridge filter for learned information for a stacked VLAN.
        """
        return self._get_attribute('userSvlan')
    @UserSvlan.setter
    def UserSvlan(self, value):
        self._set_attribute('userSvlan', value)

    @property
    def UserSvlanId(self):
        """
        Returns
        -------
        - number: Sets the stacked VLAN identifier for filtering learned information.
        """
        return self._get_attribute('userSvlanId')
    @UserSvlanId.setter
    def UserSvlanId(self, value):
        self._set_attribute('userSvlanId', value)

    @property
    def UserSvlanPriority(self):
        """
        Returns
        -------
        - number: Sets the stacked VLAN priority for filtering learned information.
        """
        return self._get_attribute('userSvlanPriority')
    @UserSvlanPriority.setter
    def UserSvlanPriority(self, value):
        self._set_attribute('userSvlanPriority', value)

    @property
    def UserSvlanTpId(self):
        """
        Returns
        -------
        - str: Sets the stacked VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        """
        return self._get_attribute('userSvlanTpId')
    @UserSvlanTpId.setter
    def UserSvlanTpId(self, value):
        self._set_attribute('userSvlanTpId', value)

    @property
    def UserTransactionId(self):
        """
        Returns
        -------
        - number: The transaction identifier for the LTM packet if the configured MEP not found. Default: 1.
        """
        return self._get_attribute('userTransactionId')
    @UserTransactionId.setter
    def UserTransactionId(self, value):
        self._set_attribute('userTransactionId', value)

    @property
    def UserTtlInterval(self):
        """
        Returns
        -------
        - number: Time to live value, in seconds. Default is 64.
        """
        return self._get_attribute('userTtlInterval')
    @UserTtlInterval.setter
    def UserTtlInterval(self, value):
        self._set_attribute('userTtlInterval', value)

    @property
    def UserUsabilityOption(self):
        """
        Returns
        -------
        - str(manual | oneToOne | oneToAll | allToOne | allToAll): User Option, one of Manual, One-to-One, One-to-All, All-to-One, All-to-All.
        """
        return self._get_attribute('userUsabilityOption')
    @UserUsabilityOption.setter
    def UserUsabilityOption(self, value):
        self._set_attribute('userUsabilityOption', value)

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
        return self._update(locals())

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
        return self._create(locals())

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
        return self._select(locals())

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
