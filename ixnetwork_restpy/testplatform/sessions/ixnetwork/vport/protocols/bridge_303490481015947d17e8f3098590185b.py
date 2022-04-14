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


class Bridge(Base):
    """This object contains the configuration for the CFM bridge.
    The Bridge class encapsulates a list of bridge resources that are managed by the user.
    A list of resources can be retrieved from the server using the Bridge.find() method.
    The list can be managed by using the Bridge.add() and Bridge.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "bridge"
    _SDM_ATT_MAP = {
        "AisInterval": "aisInterval",
        "AllowCfmMaidFormatsInY1731": "allowCfmMaidFormatsInY1731",
        "BridgeId": "bridgeId",
        "DelayLearnedErrorString": "delayLearnedErrorString",
        "EnableAis": "enableAis",
        "EnableOutOfSequenceDetection": "enableOutOfSequenceDetection",
        "Enabled": "enabled",
        "Encapsulation": "encapsulation",
        "EtherType": "etherType",
        "Function": "function",
        "GarbageCollectTime": "garbageCollectTime",
        "IsAisLearnedInfoRefreshed": "isAisLearnedInfoRefreshed",
        "IsCcmLearnedInfoRefreshed": "isCcmLearnedInfoRefreshed",
        "IsDelayLearnedConfigMep": "isDelayLearnedConfigMep",
        "IsDelayLearnedPacketSent": "isDelayLearnedPacketSent",
        "IsDelayMeasurementLearnedInfoRefreshed": "isDelayMeasurementLearnedInfoRefreshed",
        "IsLbLearnedConfigMep": "isLbLearnedConfigMep",
        "IsLbLearnedPacketSent": "isLbLearnedPacketSent",
        "IsLckLearnedInfoRefreshed": "isLckLearnedInfoRefreshed",
        "IsLinkTraceLearnedInfoRefreshed": "isLinkTraceLearnedInfoRefreshed",
        "IsLoopbackLearnedInfoRefreshed": "isLoopbackLearnedInfoRefreshed",
        "IsLossMeasurementLearnedInfoPacketSent": "isLossMeasurementLearnedInfoPacketSent",
        "IsLossMeasurementLearnedInfoRefreshed": "isLossMeasurementLearnedInfoRefreshed",
        "IsLtLearnedConfigMep": "isLtLearnedConfigMep",
        "IsLtLearnedPacketSent": "isLtLearnedPacketSent",
        "IsPbbTeCcmLearnedInfoRefreshed": "isPbbTeCcmLearnedInfoRefreshed",
        "IsPbbTeDelayLearnedConfigMep": "isPbbTeDelayLearnedConfigMep",
        "IsPbbTeDelayLearnedInfoRefreshed": "isPbbTeDelayLearnedInfoRefreshed",
        "IsPbbTeDelayLearnedPacketSent": "isPbbTeDelayLearnedPacketSent",
        "IsPbbTeLbLearnedConfigMep": "isPbbTeLbLearnedConfigMep",
        "IsPbbTeLbLearnedInfoRefreshed": "isPbbTeLbLearnedInfoRefreshed",
        "IsPbbTeLbLearnedPacketSent": "isPbbTeLbLearnedPacketSent",
        "IsPeriodicOamLearnedInfoRefreshed": "isPeriodicOamLearnedInfoRefreshed",
        "IsTstLearnedInfoRefreshed": "isTstLearnedInfoRefreshed",
        "LbLearnedErrorString": "lbLearnedErrorString",
        "LossMeasurementLearnedInfoErrorString": "lossMeasurementLearnedInfoErrorString",
        "LtLearnedErrorString": "ltLearnedErrorString",
        "OperationMode": "operationMode",
        "PbbTeDelayLearnedErrorString": "pbbTeDelayLearnedErrorString",
        "PbbTeLbLearnedErrorString": "pbbTeLbLearnedErrorString",
        "UserBvlan": "userBvlan",
        "UserBvlanId": "userBvlanId",
        "UserBvlanPriority": "userBvlanPriority",
        "UserBvlanTpId": "userBvlanTpId",
        "UserCvlan": "userCvlan",
        "UserCvlanId": "userCvlanId",
        "UserCvlanPriority": "userCvlanPriority",
        "UserCvlanTpId": "userCvlanTpId",
        "UserDelayMethod": "userDelayMethod",
        "UserDelayType": "userDelayType",
        "UserDstMacAddress": "userDstMacAddress",
        "UserDstMepId": "userDstMepId",
        "UserDstType": "userDstType",
        "UserLearnedInfoTimeOut": "userLearnedInfoTimeOut",
        "UserLossMethod": "userLossMethod",
        "UserMdLevel": "userMdLevel",
        "UserPbbTeDelayMethod": "userPbbTeDelayMethod",
        "UserPbbTeDelayType": "userPbbTeDelayType",
        "UserPeriodicOamType": "userPeriodicOamType",
        "UserSelectDstMepById": "userSelectDstMepById",
        "UserSelectSrcMepById": "userSelectSrcMepById",
        "UserSendType": "userSendType",
        "UserShortMaName": "userShortMaName",
        "UserShortMaNameFormat": "userShortMaNameFormat",
        "UserSrcMacAddress": "userSrcMacAddress",
        "UserSrcMepId": "userSrcMepId",
        "UserSrcType": "userSrcType",
        "UserSvlan": "userSvlan",
        "UserSvlanId": "userSvlanId",
        "UserSvlanPriority": "userSvlanPriority",
        "UserSvlanTpId": "userSvlanTpId",
        "UserTransactionId": "userTransactionId",
        "UserTtlInterval": "userTtlInterval",
        "UserUsabilityOption": "userUsabilityOption",
    }
    _SDM_ENUM_MAP = {
        "aisInterval": ["oneSec", "oneMin"],
        "encapsulation": ["ethernet", "llcSnap"],
        "function": ["faultManagement", "performanceMeasurement"],
        "operationMode": ["cfm", "y1731", "pbbTe"],
        "userBvlan": ["noVlanId", "vlanId", "allVlanId"],
        "userCvlan": ["noVlanId", "vlanId", "allVlanId"],
        "userDelayMethod": ["oneWay", "twoWay"],
        "userDelayType": ["dm", "dvm"],
        "userDstType": ["mepMac", "mepId", "mepMacAll", "mepIdAll"],
        "userLossMethod": ["dualEnded", "singleEnded"],
        "userMdLevel": ["0", "1", "2", "3", "4", "5", "6", "7", "allMd"],
        "userPbbTeDelayMethod": ["twoWay", "oneWay"],
        "userPbbTeDelayType": ["dm", "dvm"],
        "userPeriodicOamType": [
            "linkTrace",
            "loopback",
            "delayMeasurement",
            "lossMeasurement",
        ],
        "userSendType": ["unicast", "multicast"],
        "userShortMaNameFormat": [
            "allFormats",
            "primaryVid",
            "characterString",
            "twoOctetInteger",
            "rfc2685VpnId",
        ],
        "userSrcType": ["mepMac", "mepId", "mepMacAll", "mepIdAll"],
        "userSvlan": ["noVlanId", "vlanId", "allVlanId"],
        "userUsabilityOption": [
            "manual",
            "oneToOne",
            "oneToAll",
            "allToOne",
            "allToAll",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Bridge, self).__init__(parent, list_op)

    @property
    def AisLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.aislearnedinfo_1ef51d8a5d7e1d6f8b4577dd1a7a694e.AisLearnedInfo): An instance of the AisLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.aislearnedinfo_1ef51d8a5d7e1d6f8b4577dd1a7a694e import (
            AisLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AisLearnedInfo", None) is not None:
                return self._properties.get("AisLearnedInfo")
        return AisLearnedInfo(self)

    @property
    def CcmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ccmlearnedinfo_f04a632dd1f2d59cdba98ffe4c169328.CcmLearnedInfo): An instance of the CcmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ccmlearnedinfo_f04a632dd1f2d59cdba98ffe4c169328 import (
            CcmLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CcmLearnedInfo", None) is not None:
                return self._properties.get("CcmLearnedInfo")
        return CcmLearnedInfo(self)

    @property
    def CustomTlvs(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtlvs_a77b90defd4dc2a97e3440bbaabec5e1.CustomTlvs): An instance of the CustomTlvs class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtlvs_a77b90defd4dc2a97e3440bbaabec5e1 import (
            CustomTlvs,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CustomTlvs", None) is not None:
                return self._properties.get("CustomTlvs")
        return CustomTlvs(self)

    @property
    def DelayLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.delaylearnedinfo_bea460573dd9106bc998073489a0c2d0.DelayLearnedInfo): An instance of the DelayLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.delaylearnedinfo_bea460573dd9106bc998073489a0c2d0 import (
            DelayLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DelayLearnedInfo", None) is not None:
                return self._properties.get("DelayLearnedInfo")
        return DelayLearnedInfo(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_f5817c97c964b787c8c564bdf17f05ce.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_f5817c97c964b787c8c564bdf17f05ce import (
            Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Interface", None) is not None:
                return self._properties.get("Interface")
        return Interface(self)

    @property
    def LbLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lblearnedinfo_2c4c60ce204615b71f6b9313592f8557.LbLearnedInfo): An instance of the LbLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lblearnedinfo_2c4c60ce204615b71f6b9313592f8557 import (
            LbLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LbLearnedInfo", None) is not None:
                return self._properties.get("LbLearnedInfo")
        return LbLearnedInfo(self)

    @property
    def LckLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lcklearnedinfo_496dd52a33c2c0009b74a9bee972e99f.LckLearnedInfo): An instance of the LckLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lcklearnedinfo_496dd52a33c2c0009b74a9bee972e99f import (
            LckLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LckLearnedInfo", None) is not None:
                return self._properties.get("LckLearnedInfo")
        return LckLearnedInfo(self)

    @property
    def Link(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_7d58db94150539071d46c85f2377f76c.Link): An instance of the Link class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_7d58db94150539071d46c85f2377f76c import (
            Link,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Link", None) is not None:
                return self._properties.get("Link")
        return Link(self)

    @property
    def LossLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.losslearnedinfo_84309f8d1003b963cb497f04a53aba4c.LossLearnedInfo): An instance of the LossLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.losslearnedinfo_84309f8d1003b963cb497f04a53aba4c import (
            LossLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LossLearnedInfo", None) is not None:
                return self._properties.get("LossLearnedInfo")
        return LossLearnedInfo(self)

    @property
    def LtLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedinfo_4d824216eb258ad01e7165314c7ec9bb.LtLearnedInfo): An instance of the LtLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedinfo_4d824216eb258ad01e7165314c7ec9bb import (
            LtLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LtLearnedInfo", None) is not None:
                return self._properties.get("LtLearnedInfo")
        return LtLearnedInfo(self)

    @property
    def MdLevel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mdlevel_ebbac25168b7f1eb8e9c616327588e31.MdLevel): An instance of the MdLevel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mdlevel_ebbac25168b7f1eb8e9c616327588e31 import (
            MdLevel,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MdLevel", None) is not None:
                return self._properties.get("MdLevel")
        return MdLevel(self)

    @property
    def Mp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mp_27380643ca73dc91fb91d8f173d7c4b0.Mp): An instance of the Mp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mp_27380643ca73dc91fb91d8f173d7c4b0 import (
            Mp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Mp", None) is not None:
                return self._properties.get("Mp")
        return Mp(self)

    @property
    def PbbTeCcmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteccmlearnedinfo_be36c1d486826a7637c81a968538c581.PbbTeCcmLearnedInfo): An instance of the PbbTeCcmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteccmlearnedinfo_be36c1d486826a7637c81a968538c581 import (
            PbbTeCcmLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PbbTeCcmLearnedInfo", None) is not None:
                return self._properties.get("PbbTeCcmLearnedInfo")
        return PbbTeCcmLearnedInfo(self)

    @property
    def PbbTeDelayLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbtedelaylearnedinfo_afb05fa03db6811e7ae1c2a593ca6044.PbbTeDelayLearnedInfo): An instance of the PbbTeDelayLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbtedelaylearnedinfo_afb05fa03db6811e7ae1c2a593ca6044 import (
            PbbTeDelayLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PbbTeDelayLearnedInfo", None) is not None:
                return self._properties.get("PbbTeDelayLearnedInfo")
        return PbbTeDelayLearnedInfo(self)

    @property
    def PbbTeLbLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbtelblearnedinfo_f137629a0dcafa32f5fc4fd0827a09f1.PbbTeLbLearnedInfo): An instance of the PbbTeLbLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbtelblearnedinfo_f137629a0dcafa32f5fc4fd0827a09f1 import (
            PbbTeLbLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PbbTeLbLearnedInfo", None) is not None:
                return self._properties.get("PbbTeLbLearnedInfo")
        return PbbTeLbLearnedInfo(self)

    @property
    def PbbTeLtLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteltlearnedinfo_c55aae88e52b1e26bdfd4943fba601be.PbbTeLtLearnedInfo): An instance of the PbbTeLtLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteltlearnedinfo_c55aae88e52b1e26bdfd4943fba601be import (
            PbbTeLtLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PbbTeLtLearnedInfo", None) is not None:
                return self._properties.get("PbbTeLtLearnedInfo")
        return PbbTeLtLearnedInfo(self)

    @property
    def PbbTePeriodicOamDmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamdmlearnedinfo_795335039bdead8c63c9803d2ae3d6b7.PbbTePeriodicOamDmLearnedInfo): An instance of the PbbTePeriodicOamDmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamdmlearnedinfo_795335039bdead8c63c9803d2ae3d6b7 import (
            PbbTePeriodicOamDmLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PbbTePeriodicOamDmLearnedInfo", None) is not None:
                return self._properties.get("PbbTePeriodicOamDmLearnedInfo")
        return PbbTePeriodicOamDmLearnedInfo(self)

    @property
    def PbbTePeriodicOamLbLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamlblearnedinfo_e9d79ab2045ec30babf41733329db343.PbbTePeriodicOamLbLearnedInfo): An instance of the PbbTePeriodicOamLbLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamlblearnedinfo_e9d79ab2045ec30babf41733329db343 import (
            PbbTePeriodicOamLbLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PbbTePeriodicOamLbLearnedInfo", None) is not None:
                return self._properties.get("PbbTePeriodicOamLbLearnedInfo")
        return PbbTePeriodicOamLbLearnedInfo(self)

    @property
    def PbbTePeriodicOamLtLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamltlearnedinfo_e6b96e3d1f94decd2b892cc7a253c5ac.PbbTePeriodicOamLtLearnedInfo): An instance of the PbbTePeriodicOamLtLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pbbteperiodicoamltlearnedinfo_e6b96e3d1f94decd2b892cc7a253c5ac import (
            PbbTePeriodicOamLtLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PbbTePeriodicOamLtLearnedInfo", None) is not None:
                return self._properties.get("PbbTePeriodicOamLtLearnedInfo")
        return PbbTePeriodicOamLtLearnedInfo(self)

    @property
    def PeriodicOamDmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamdmlearnedinfo_5d0ee05ebe2d3358a6728bad2b1827e4.PeriodicOamDmLearnedInfo): An instance of the PeriodicOamDmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamdmlearnedinfo_5d0ee05ebe2d3358a6728bad2b1827e4 import (
            PeriodicOamDmLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PeriodicOamDmLearnedInfo", None) is not None:
                return self._properties.get("PeriodicOamDmLearnedInfo")
        return PeriodicOamDmLearnedInfo(self)

    @property
    def PeriodicOamLbLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamlblearnedinfo_7a9a25d94d97ca8cf93888312cab1e63.PeriodicOamLbLearnedInfo): An instance of the PeriodicOamLbLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamlblearnedinfo_7a9a25d94d97ca8cf93888312cab1e63 import (
            PeriodicOamLbLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PeriodicOamLbLearnedInfo", None) is not None:
                return self._properties.get("PeriodicOamLbLearnedInfo")
        return PeriodicOamLbLearnedInfo(self)

    @property
    def PeriodicOamLmLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamlmlearnedinfo_3875ae13eb2ca004c45550a58703214d.PeriodicOamLmLearnedInfo): An instance of the PeriodicOamLmLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamlmlearnedinfo_3875ae13eb2ca004c45550a58703214d import (
            PeriodicOamLmLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PeriodicOamLmLearnedInfo", None) is not None:
                return self._properties.get("PeriodicOamLmLearnedInfo")
        return PeriodicOamLmLearnedInfo(self)

    @property
    def PeriodicOamLtLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamltlearnedinfo_49a700a40a8546a87d3cdd281c3f012b.PeriodicOamLtLearnedInfo): An instance of the PeriodicOamLtLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.periodicoamltlearnedinfo_49a700a40a8546a87d3cdd281c3f012b import (
            PeriodicOamLtLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PeriodicOamLtLearnedInfo", None) is not None:
                return self._properties.get("PeriodicOamLtLearnedInfo")
        return PeriodicOamLtLearnedInfo(self)

    @property
    def Trunk(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trunk_da9c758dcc43a1e155e9aecc9fc92dcd.Trunk): An instance of the Trunk class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trunk_da9c758dcc43a1e155e9aecc9fc92dcd import (
            Trunk,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Trunk", None) is not None:
                return self._properties.get("Trunk")
        return Trunk(self)

    @property
    def TstLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tstlearnedinfo_ddb283fba5ef8dce5df59ea72cdd6e37.TstLearnedInfo): An instance of the TstLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tstlearnedinfo_ddb283fba5ef8dce5df59ea72cdd6e37 import (
            TstLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TstLearnedInfo", None) is not None:
                return self._properties.get("TstLearnedInfo")
        return TstLearnedInfo(self)

    @property
    def Vlans(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vlans_92287cc4b4083769c57758c6be9fc9e8.Vlans): An instance of the Vlans class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vlans_92287cc4b4083769c57758c6be9fc9e8 import (
            Vlans,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Vlans", None) is not None:
                return self._properties.get("Vlans")
        return Vlans(self)

    @property
    def AisInterval(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(oneSec | oneMin): The interval between AIS messages sent from this CFM bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AisInterval"])

    @AisInterval.setter
    def AisInterval(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AisInterval"], value)

    @property
    def AllowCfmMaidFormatsInY1731(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, allows to use CFM's MD Name types and Short MA Name types when the Operation Mode is Y.1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AllowCfmMaidFormatsInY1731"])

    @AllowCfmMaidFormatsInY1731.setter
    def AllowCfmMaidFormatsInY1731(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AllowCfmMaidFormatsInY1731"], value)

    @property
    def BridgeId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The bridge MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BridgeId"])

    @BridgeId.setter
    def BridgeId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BridgeId"], value)

    @property
    def DelayLearnedErrorString(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned error string for the delay measurement.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayLearnedErrorString"])

    @property
    def EnableAis(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If true, enables the use of AIS messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAis"])

    @EnableAis.setter
    def EnableAis(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAis"], value)

    @property
    def EnableOutOfSequenceDetection(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the detection of out of sequence CCM messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOutOfSequenceDetection"])

    @EnableOutOfSequenceDetection.setter
    def EnableOutOfSequenceDetection(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOutOfSequenceDetection"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the CFM bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def Encapsulation(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ethernet | llcSnap): Sets the encapsulation type for the bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Encapsulation"])

    @Encapsulation.setter
    def Encapsulation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Encapsulation"], value)

    @property
    def EtherType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Selects the ether type for the bridge. The options are 0x8902 and 0x88E6.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EtherType"])

    @EtherType.setter
    def EtherType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EtherType"], value)

    @property
    def Function(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(faultManagement | performanceMeasurement): Determines the CFM function when operationMode is set to Y.1731.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Function"])

    @Function.setter
    def Function(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Function"], value)

    @property
    def GarbageCollectTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Integer value denotes the interval for holding the expired database. Default 10 seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GarbageCollectTime"])

    @GarbageCollectTime.setter
    def GarbageCollectTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GarbageCollectTime"], value)

    @property
    def IsAisLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsAisLearnedInfoRefreshed"])

    @property
    def IsCcmLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, the CCM learned information is current.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsCcmLearnedInfoRefreshed"])

    @property
    def IsDelayLearnedConfigMep(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the delay measurement was found.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsDelayLearnedConfigMep"])

    @property
    def IsDelayLearnedPacketSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, indicates the delay packet was sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsDelayLearnedPacketSent"])

    @property
    def IsDelayMeasurementLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, the learned delay information is current.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsDelayMeasurementLearnedInfoRefreshed"]
        )

    @property
    def IsLbLearnedConfigMep(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the loopback measurement was found.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLbLearnedConfigMep"])

    @property
    def IsLbLearnedPacketSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, indicates the loopback packet was sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLbLearnedPacketSent"])

    @property
    def IsLckLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLckLearnedInfoRefreshed"])

    @property
    def IsLinkTraceLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, the learned link trace information is current.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLinkTraceLearnedInfoRefreshed"])

    @property
    def IsLoopbackLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, the learned loopback information is current.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLoopbackLearnedInfoRefreshed"])

    @property
    def IsLossMeasurementLearnedInfoPacketSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsLossMeasurementLearnedInfoPacketSent"]
        )

    @property
    def IsLossMeasurementLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsLossMeasurementLearnedInfoRefreshed"]
        )

    @property
    def IsLtLearnedConfigMep(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the link trace measurement was found.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLtLearnedConfigMep"])

    @property
    def IsLtLearnedPacketSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, indicates the link trace packet was sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLtLearnedPacketSent"])

    @property
    def IsPbbTeCcmLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, the learned PBB-TE CCM information is current.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsPbbTeCcmLearnedInfoRefreshed"])

    @property
    def IsPbbTeDelayLearnedConfigMep(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the PBB-TE delay measurement was found.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsPbbTeDelayLearnedConfigMep"])

    @property
    def IsPbbTeDelayLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, the learned PBB-TE delay information is current.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsPbbTeDelayLearnedInfoRefreshed"]
        )

    @property
    def IsPbbTeDelayLearnedPacketSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, indicates the PBB-TE delay packet was sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsPbbTeDelayLearnedPacketSent"])

    @property
    def IsPbbTeLbLearnedConfigMep(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, indicates if the configured MEP for the PBB-TE loopback measurement was found.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsPbbTeLbLearnedConfigMep"])

    @property
    def IsPbbTeLbLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, the PBB-TE learned loopback information is current.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsPbbTeLbLearnedInfoRefreshed"])

    @property
    def IsPbbTeLbLearnedPacketSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, indicates the PBB-TE loopback packet was sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsPbbTeLbLearnedPacketSent"])

    @property
    def IsPeriodicOamLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the periodic OAM learned information is up-to-date.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsPeriodicOamLearnedInfoRefreshed"]
        )

    @property
    def IsTstLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsTstLearnedInfoRefreshed"])

    @property
    def LbLearnedErrorString(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned error string for the loopback measurement.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LbLearnedErrorString"])

    @property
    def LossMeasurementLearnedInfoErrorString(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["LossMeasurementLearnedInfoErrorString"]
        )

    @property
    def LtLearnedErrorString(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned error string for the link trace measurement.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LtLearnedErrorString"])

    @property
    def OperationMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cfm | y1731 | pbbTe): Selects the type of CFM to enable.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OperationMode"])

    @OperationMode.setter
    def OperationMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OperationMode"], value)

    @property
    def PbbTeDelayLearnedErrorString(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned error string for the PBB-TE delay measurement.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbTeDelayLearnedErrorString"])

    @property
    def PbbTeLbLearnedErrorString(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned error string for the PBB-TE loopback measurement.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PbbTeLbLearnedErrorString"])

    @property
    def UserBvlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noVlanId | vlanId | allVlanId): Sets the bridge filter for PBB-TE learned information for the VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserBvlan"])

    @UserBvlan.setter
    def UserBvlan(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserBvlan"], value)

    @property
    def UserBvlanId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the PBB-TE VLAN identifier for filtering learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserBvlanId"])

    @UserBvlanId.setter
    def UserBvlanId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserBvlanId"], value)

    @property
    def UserBvlanPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the PBB-TE VLAN priority for filtering learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserBvlanPriority"])

    @UserBvlanPriority.setter
    def UserBvlanPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserBvlanPriority"], value)

    @property
    def UserBvlanTpId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the PBB-TE VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserBvlanTpId"])

    @UserBvlanTpId.setter
    def UserBvlanTpId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserBvlanTpId"], value)

    @property
    def UserCvlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noVlanId | vlanId | allVlanId): Sets the bridge filter for learned information for a single VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserCvlan"])

    @UserCvlan.setter
    def UserCvlan(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserCvlan"], value)

    @property
    def UserCvlanId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the single VLAN identifier for filtering learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserCvlanId"])

    @UserCvlanId.setter
    def UserCvlanId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserCvlanId"], value)

    @property
    def UserCvlanPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the single VLAN priority for filtering learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserCvlanPriority"])

    @UserCvlanPriority.setter
    def UserCvlanPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserCvlanPriority"], value)

    @property
    def UserCvlanTpId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the single VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserCvlanTpId"])

    @UserCvlanTpId.setter
    def UserCvlanTpId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserCvlanTpId"], value)

    @property
    def UserDelayMethod(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oneWay | twoWay): Sets the type of delay method to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDelayMethod"])

    @UserDelayMethod.setter
    def UserDelayMethod(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDelayMethod"], value)

    @property
    def UserDelayType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(dm | dvm): Sets the type of delay measurement to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDelayType"])

    @UserDelayType.setter
    def UserDelayType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDelayType"], value)

    @property
    def UserDstMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Filters on the destination MAC address specified.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDstMacAddress"])

    @UserDstMacAddress.setter
    def UserDstMacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDstMacAddress"], value)

    @property
    def UserDstMepId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the MEP identifier for use with userSelectDstMepById.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDstMepId"])

    @UserDstMepId.setter
    def UserDstMepId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDstMepId"], value)

    @property
    def UserDstType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(mepMac | mepId | mepMacAll | mepIdAll): The user destination type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDstType"])

    @UserDstType.setter
    def UserDstType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDstType"], value)

    @property
    def UserLearnedInfoTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The interval in millisecond for the learned record to timeout. Default: 5000.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserLearnedInfoTimeOut"])

    @UserLearnedInfoTimeOut.setter
    def UserLearnedInfoTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserLearnedInfoTimeOut"], value)

    @property
    def UserLossMethod(self):
        # type: () -> str
        """
        Returns
        -------
        - str(dualEnded | singleEnded): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserLossMethod"])

    @UserLossMethod.setter
    def UserLossMethod(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserLossMethod"], value)

    @property
    def UserMdLevel(self):
        # type: () -> str
        """
        Returns
        -------
        - str(0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | allMd): Filters on the specified MD level.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserMdLevel"])

    @UserMdLevel.setter
    def UserMdLevel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserMdLevel"], value)

    @property
    def UserPbbTeDelayMethod(self):
        # type: () -> str
        """
        Returns
        -------
        - str(twoWay | oneWay): Sets the PBB-TE type of delay method to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserPbbTeDelayMethod"])

    @UserPbbTeDelayMethod.setter
    def UserPbbTeDelayMethod(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserPbbTeDelayMethod"], value)

    @property
    def UserPbbTeDelayType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(dm | dvm): Sets the PBB-TE type of delay measurement to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserPbbTeDelayType"])

    @UserPbbTeDelayType.setter
    def UserPbbTeDelayType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserPbbTeDelayType"], value)

    @property
    def UserPeriodicOamType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(linkTrace | loopback | delayMeasurement | lossMeasurement): Sets the type of periodic OAM.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserPeriodicOamType"])

    @UserPeriodicOamType.setter
    def UserPeriodicOamType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserPeriodicOamType"], value)

    @property
    def UserSelectDstMepById(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If true, filters on the MEP by destination MEP identifier rather than by the MAC address. The MEP identifier is set in userDstMepId.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserSelectDstMepById"])

    @UserSelectDstMepById.setter
    def UserSelectDstMepById(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserSelectDstMepById"], value)

    @property
    def UserSelectSrcMepById(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If true, filters on the MEP by source MEP identifier rather than by the MAC address. The MEP identifier is set in userSrcMepId.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserSelectSrcMepById"])

    @UserSelectSrcMepById.setter
    def UserSelectSrcMepById(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserSelectSrcMepById"], value)

    @property
    def UserSendType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unicast | multicast): Filters on the the send type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserSendType"])

    @UserSendType.setter
    def UserSendType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserSendType"], value)

    @property
    def UserShortMaName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Filters on the specified Short MA Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserShortMaName"])

    @UserShortMaName.setter
    def UserShortMaName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserShortMaName"], value)

    @property
    def UserShortMaNameFormat(self):
        # type: () -> str
        """
        Returns
        -------
        - str(allFormats | primaryVid | characterString | twoOctetInteger | rfc2685VpnId): Filters on the Short MA Name Format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserShortMaNameFormat"])

    @UserShortMaNameFormat.setter
    def UserShortMaNameFormat(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserShortMaNameFormat"], value)

    @property
    def UserSrcMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Filters on the specified source MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserSrcMacAddress"])

    @UserSrcMacAddress.setter
    def UserSrcMacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserSrcMacAddress"], value)

    @property
    def UserSrcMepId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the MEP identifier for use with userSelectSrcMepById.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserSrcMepId"])

    @UserSrcMepId.setter
    def UserSrcMepId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserSrcMepId"], value)

    @property
    def UserSrcType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(mepMac | mepId | mepMacAll | mepIdAll): The user source type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserSrcType"])

    @UserSrcType.setter
    def UserSrcType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserSrcType"], value)

    @property
    def UserSvlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noVlanId | vlanId | allVlanId): Sets the bridge filter for learned information for a stacked VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserSvlan"])

    @UserSvlan.setter
    def UserSvlan(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserSvlan"], value)

    @property
    def UserSvlanId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the stacked VLAN identifier for filtering learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserSvlanId"])

    @UserSvlanId.setter
    def UserSvlanId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserSvlanId"], value)

    @property
    def UserSvlanPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the stacked VLAN priority for filtering learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserSvlanPriority"])

    @UserSvlanPriority.setter
    def UserSvlanPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserSvlanPriority"], value)

    @property
    def UserSvlanTpId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the stacked VLAN TPID for filtering learned information. One of 0x8100, 0x9100, 0x9200, or 0x88A8.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserSvlanTpId"])

    @UserSvlanTpId.setter
    def UserSvlanTpId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserSvlanTpId"], value)

    @property
    def UserTransactionId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The transaction identifier for the LTM packet if the configured MEP not found. Default: 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserTransactionId"])

    @UserTransactionId.setter
    def UserTransactionId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserTransactionId"], value)

    @property
    def UserTtlInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Time to live value, in seconds. Default is 64.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserTtlInterval"])

    @UserTtlInterval.setter
    def UserTtlInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserTtlInterval"], value)

    @property
    def UserUsabilityOption(self):
        # type: () -> str
        """
        Returns
        -------
        - str(manual | oneToOne | oneToAll | allToOne | allToAll): User Option, one of Manual, One-to-One, One-to-All, All-to-One, All-to-All.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserUsabilityOption"])

    @UserUsabilityOption.setter
    def UserUsabilityOption(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserUsabilityOption"], value)

    def update(
        self,
        AisInterval=None,
        AllowCfmMaidFormatsInY1731=None,
        BridgeId=None,
        EnableAis=None,
        EnableOutOfSequenceDetection=None,
        Enabled=None,
        Encapsulation=None,
        EtherType=None,
        Function=None,
        GarbageCollectTime=None,
        OperationMode=None,
        UserBvlan=None,
        UserBvlanId=None,
        UserBvlanPriority=None,
        UserBvlanTpId=None,
        UserCvlan=None,
        UserCvlanId=None,
        UserCvlanPriority=None,
        UserCvlanTpId=None,
        UserDelayMethod=None,
        UserDelayType=None,
        UserDstMacAddress=None,
        UserDstMepId=None,
        UserDstType=None,
        UserLearnedInfoTimeOut=None,
        UserLossMethod=None,
        UserMdLevel=None,
        UserPbbTeDelayMethod=None,
        UserPbbTeDelayType=None,
        UserPeriodicOamType=None,
        UserSelectDstMepById=None,
        UserSelectSrcMepById=None,
        UserSendType=None,
        UserShortMaName=None,
        UserShortMaNameFormat=None,
        UserSrcMacAddress=None,
        UserSrcMepId=None,
        UserSrcType=None,
        UserSvlan=None,
        UserSvlanId=None,
        UserSvlanPriority=None,
        UserSvlanTpId=None,
        UserTransactionId=None,
        UserTtlInterval=None,
        UserUsabilityOption=None,
    ):
        # type: (str, bool, str, bool, bool, bool, str, int, str, int, str, str, int, int, str, str, int, int, str, str, str, str, int, str, int, str, str, str, str, str, bool, bool, str, str, str, str, int, str, str, int, int, str, int, int, str) -> Bridge
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

    def add(
        self,
        AisInterval=None,
        AllowCfmMaidFormatsInY1731=None,
        BridgeId=None,
        EnableAis=None,
        EnableOutOfSequenceDetection=None,
        Enabled=None,
        Encapsulation=None,
        EtherType=None,
        Function=None,
        GarbageCollectTime=None,
        OperationMode=None,
        UserBvlan=None,
        UserBvlanId=None,
        UserBvlanPriority=None,
        UserBvlanTpId=None,
        UserCvlan=None,
        UserCvlanId=None,
        UserCvlanPriority=None,
        UserCvlanTpId=None,
        UserDelayMethod=None,
        UserDelayType=None,
        UserDstMacAddress=None,
        UserDstMepId=None,
        UserDstType=None,
        UserLearnedInfoTimeOut=None,
        UserLossMethod=None,
        UserMdLevel=None,
        UserPbbTeDelayMethod=None,
        UserPbbTeDelayType=None,
        UserPeriodicOamType=None,
        UserSelectDstMepById=None,
        UserSelectSrcMepById=None,
        UserSendType=None,
        UserShortMaName=None,
        UserShortMaNameFormat=None,
        UserSrcMacAddress=None,
        UserSrcMepId=None,
        UserSrcType=None,
        UserSvlan=None,
        UserSvlanId=None,
        UserSvlanPriority=None,
        UserSvlanTpId=None,
        UserTransactionId=None,
        UserTtlInterval=None,
        UserUsabilityOption=None,
    ):
        # type: (str, bool, str, bool, bool, bool, str, int, str, int, str, str, int, int, str, str, int, int, str, str, str, str, int, str, int, str, str, str, str, str, bool, bool, str, str, str, str, int, str, str, int, int, str, int, int, str) -> Bridge
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

    def find(
        self,
        AisInterval=None,
        AllowCfmMaidFormatsInY1731=None,
        BridgeId=None,
        DelayLearnedErrorString=None,
        EnableAis=None,
        EnableOutOfSequenceDetection=None,
        Enabled=None,
        Encapsulation=None,
        EtherType=None,
        Function=None,
        GarbageCollectTime=None,
        IsAisLearnedInfoRefreshed=None,
        IsCcmLearnedInfoRefreshed=None,
        IsDelayLearnedConfigMep=None,
        IsDelayLearnedPacketSent=None,
        IsDelayMeasurementLearnedInfoRefreshed=None,
        IsLbLearnedConfigMep=None,
        IsLbLearnedPacketSent=None,
        IsLckLearnedInfoRefreshed=None,
        IsLinkTraceLearnedInfoRefreshed=None,
        IsLoopbackLearnedInfoRefreshed=None,
        IsLossMeasurementLearnedInfoPacketSent=None,
        IsLossMeasurementLearnedInfoRefreshed=None,
        IsLtLearnedConfigMep=None,
        IsLtLearnedPacketSent=None,
        IsPbbTeCcmLearnedInfoRefreshed=None,
        IsPbbTeDelayLearnedConfigMep=None,
        IsPbbTeDelayLearnedInfoRefreshed=None,
        IsPbbTeDelayLearnedPacketSent=None,
        IsPbbTeLbLearnedConfigMep=None,
        IsPbbTeLbLearnedInfoRefreshed=None,
        IsPbbTeLbLearnedPacketSent=None,
        IsPeriodicOamLearnedInfoRefreshed=None,
        IsTstLearnedInfoRefreshed=None,
        LbLearnedErrorString=None,
        LossMeasurementLearnedInfoErrorString=None,
        LtLearnedErrorString=None,
        OperationMode=None,
        PbbTeDelayLearnedErrorString=None,
        PbbTeLbLearnedErrorString=None,
        UserBvlan=None,
        UserBvlanId=None,
        UserBvlanPriority=None,
        UserBvlanTpId=None,
        UserCvlan=None,
        UserCvlanId=None,
        UserCvlanPriority=None,
        UserCvlanTpId=None,
        UserDelayMethod=None,
        UserDelayType=None,
        UserDstMacAddress=None,
        UserDstMepId=None,
        UserDstType=None,
        UserLearnedInfoTimeOut=None,
        UserLossMethod=None,
        UserMdLevel=None,
        UserPbbTeDelayMethod=None,
        UserPbbTeDelayType=None,
        UserPeriodicOamType=None,
        UserSelectDstMepById=None,
        UserSelectSrcMepById=None,
        UserSendType=None,
        UserShortMaName=None,
        UserShortMaNameFormat=None,
        UserSrcMacAddress=None,
        UserSrcMepId=None,
        UserSrcType=None,
        UserSvlan=None,
        UserSvlanId=None,
        UserSvlanPriority=None,
        UserSvlanTpId=None,
        UserTransactionId=None,
        UserTtlInterval=None,
        UserUsabilityOption=None,
    ):
        # type: (str, bool, str, str, bool, bool, bool, str, int, str, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, str, str, str, str, str, int, int, str, str, int, int, str, str, str, str, int, str, int, str, str, str, str, str, bool, bool, str, str, str, str, int, str, str, int, int, str, int, int, str) -> Bridge
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

    def RefreshAisLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshAisLearnedInfo operation on the server.

        NOT DEFINED

        refreshAisLearnedInfo(async_operation=bool)bool
        -----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "refreshAisLearnedInfo", payload=payload, response_object=None
        )

    def RefreshCcmLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshCcmLearnedInfo operation on the server.

        This command is used to refresh the learned CCM information on the bridge.

        refreshCcmLearnedInfo(async_operation=bool)bool
        -----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "refreshCcmLearnedInfo", payload=payload, response_object=None
        )

    def RefreshLckLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshLckLearnedInfo operation on the server.

        NOT DEFINED

        refreshLckLearnedInfo(async_operation=bool)bool
        -----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "refreshLckLearnedInfo", payload=payload, response_object=None
        )

    def RefreshTstLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshTstLearnedInfo operation on the server.

        NOT DEFINED

        refreshTstLearnedInfo(async_operation=bool)bool
        -----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "refreshTstLearnedInfo", payload=payload, response_object=None
        )

    def StartDelayMeasurement(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the startDelayMeasurement operation on the server.

        This command is used to refresh the learned CFM ITU information on this bridge.

        startDelayMeasurement(async_operation=bool)bool
        -----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "startDelayMeasurement", payload=payload, response_object=None
        )

    def StartLinkTrace(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the startLinkTrace operation on the server.

        This command is used to refresh the learned CFM LT information on this bridge.

        startLinkTrace(async_operation=bool)bool
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
        return self._execute("startLinkTrace", payload=payload, response_object=None)

    def StartLoopback(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the startLoopback operation on the server.

        This command is used to refresh the learned CFM LB information on this bridge.

        startLoopback(async_operation=bool)bool
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
        return self._execute("startLoopback", payload=payload, response_object=None)

    def StartLossMeasurement(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the startLossMeasurement operation on the server.

        NOT DEFINED

        startLossMeasurement(async_operation=bool)bool
        ----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "startLossMeasurement", payload=payload, response_object=None
        )

    def UpdatePeriodicOamLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the updatePeriodicOamLearnedInfo operation on the server.

        This command updates the periodic OAM learned information on this bridge.

        updatePeriodicOamLearnedInfo(async_operation=bool)bool
        ------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "updatePeriodicOamLearnedInfo", payload=payload, response_object=None
        )
