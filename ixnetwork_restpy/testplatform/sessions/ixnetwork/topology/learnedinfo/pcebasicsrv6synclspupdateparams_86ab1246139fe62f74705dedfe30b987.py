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


class PceBasicSrv6SyncLspUpdateParams(Base):
    """PCE Learned LSPs Information Database
    The PceBasicSrv6SyncLspUpdateParams class encapsulates a list of pceBasicSrv6SyncLspUpdateParams resources that are managed by the system.
    A list of resources can be retrieved from the server using the PceBasicSrv6SyncLspUpdateParams.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "pceBasicSrv6SyncLspUpdateParams"
    _SDM_ATT_MAP = {
        "AssociationId": "associationId",
        "Bandwidth": "bandwidth",
        "BindingType": "bindingType",
        "Bos": "bos",
        "ConfigureAssociation": "configureAssociation",
        "ConfigureBandwidth": "configureBandwidth",
        "ConfigureEro": "configureEro",
        "ConfigureLsp": "configureLsp",
        "ConfigureLspa": "configureLspa",
        "ConfigureMetric": "configureMetric",
        "ExcludeAny": "excludeAny",
        "HoldingPriority": "holdingPriority",
        "IncludeAll": "includeAll",
        "IncludeAny": "includeAny",
        "IncludeAssociation": "includeAssociation",
        "IncludeConfiguredERO": "includeConfiguredERO",
        "IncludeSrp": "includeSrp",
        "IncludeSymbolicPathName": "includeSymbolicPathName",
        "IncludeTEPathBindingTLV": "includeTEPathBindingTLV",
        "IncludeXro": "includeXro",
        "LocalProtection": "localProtection",
        "MplsLabel": "mplsLabel",
        "NumberOfAssociationObjects": "numberOfAssociationObjects",
        "NumberOfEroSubObjects": "numberOfEroSubObjects",
        "NumberOfMetricSubObjects": "numberOfMetricSubObjects",
        "NumberOfTEPathBindingTLV": "numberOfTEPathBindingTLV",
        "NumberOfXroSubObjects": "numberOfXroSubObjects",
        "OverridePLSPID": "overridePLSPID",
        "OverrideSrpId": "overrideSrpId",
        "PceTriggersChoiceList": "pceTriggersChoiceList",
        "PlspIdTriggerParam": "plspIdTriggerParam",
        "ProtectionLsp": "protectionLsp",
        "RemoveAssociation": "removeAssociation",
        "SendEmptyTLV": "sendEmptyTLV",
        "SetupPriority": "setupPriority",
        "SrpId": "srpId",
        "Srv6SID": "srv6SID",
        "StandbyMode": "standbyMode",
        "Tc": "tc",
        "Ttl": "ttl",
        "XroFailBit": "xroFailBit",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PceBasicSrv6SyncLspUpdateParams, self).__init__(parent, list_op)

    @property
    def PceUpdateAssociationObjectList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdateassociationobjectlist_067a0a0a0d8b8dbf8239b459127bf201.PceUpdateAssociationObjectList): An instance of the PceUpdateAssociationObjectList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdateassociationobjectlist_067a0a0a0d8b8dbf8239b459127bf201 import (
            PceUpdateAssociationObjectList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PceUpdateAssociationObjectList", None) is not None:
                return self._properties.get("PceUpdateAssociationObjectList")
        return PceUpdateAssociationObjectList(self)

    @property
    def PceUpdateSrv6EroSubObjectList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatesrv6erosubobjectlist_bbcc97d115dea1f934b86dd3b1d0e7e2.PceUpdateSrv6EroSubObjectList): An instance of the PceUpdateSrv6EroSubObjectList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatesrv6erosubobjectlist_bbcc97d115dea1f934b86dd3b1d0e7e2 import (
            PceUpdateSrv6EroSubObjectList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PceUpdateSrv6EroSubObjectList", None) is not None:
                return self._properties.get("PceUpdateSrv6EroSubObjectList")
        return PceUpdateSrv6EroSubObjectList(self)

    @property
    def PceUpdateSrv6MetricSubObjectList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatesrv6metricsubobjectlist_39e8f2176cc00efc53dbcdedfed0385e.PceUpdateSrv6MetricSubObjectList): An instance of the PceUpdateSrv6MetricSubObjectList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatesrv6metricsubobjectlist_39e8f2176cc00efc53dbcdedfed0385e import (
            PceUpdateSrv6MetricSubObjectList,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("PceUpdateSrv6MetricSubObjectList", None)
                is not None
            ):
                return self._properties.get("PceUpdateSrv6MetricSubObjectList")
        return PceUpdateSrv6MetricSubObjectList(self)

    @property
    def PceUpdateXroSubObjectList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatexrosubobjectlist_3cb16b2513bf72ff7ee4a5e0387625cf.PceUpdateXroSubObjectList): An instance of the PceUpdateXroSubObjectList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatexrosubobjectlist_3cb16b2513bf72ff7ee4a5e0387625cf import (
            PceUpdateXroSubObjectList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PceUpdateXroSubObjectList", None) is not None:
                return self._properties.get("PceUpdateXroSubObjectList")
        return PceUpdateXroSubObjectList(self)

    @property
    def PcepTEPATHBINDINGTLVList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceptepathbindingtlvlist_12acfda98ab8bf91c183199c30f2f953.PcepTEPATHBINDINGTLVList): An instance of the PcepTEPATHBINDINGTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceptepathbindingtlvlist_12acfda98ab8bf91c183199c30f2f953 import (
            PcepTEPATHBINDINGTLVList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PcepTEPATHBINDINGTLVList", None) is not None:
                return self._properties.get("PcepTEPATHBINDINGTLVList")
        return PcepTEPATHBINDINGTLVList(self)

    @property
    def AssociationId(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Association ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AssociationId"]))

    @property
    def Bandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth (bps)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Bandwidth"]))

    @property
    def BindingType(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the type of binding included in the TLV. Types are as follows: 20bit MPLS Label 32bit MPLS Label SRv6 SID Default value is 20bit MPLS Label.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BindingType"]))

    @property
    def Bos(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This bit is set to True for the last entry in the label stack i.e., for the bottom of the stack, and False for all other label stack entries. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Bos"]))

    @property
    def ConfigureAssociation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure Association
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfigureAssociation"])
        )

    @property
    def ConfigureBandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure Bandwidth
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfigureBandwidth"])
        )

    @property
    def ConfigureEro(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure ERO
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ConfigureEro"]))

    @property
    def ConfigureLsp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ConfigureLsp"]))

    @property
    def ConfigureLspa(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure LSPA
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ConfigureLspa"]))

    @property
    def ConfigureMetric(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfigureMetric"])
        )

    @property
    def ExcludeAny(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Exclude Any
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ExcludeAny"]))

    @property
    def HoldingPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Holding Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HoldingPriority"])
        )

    @property
    def IncludeAll(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include All
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeAll"]))

    @property
    def IncludeAny(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Any
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeAny"]))

    @property
    def IncludeAssociation(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Association object will be included in a PcUpdate message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeAssociation"])
        )

    @property
    def IncludeConfiguredERO(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is enabled, entire ERO will be go out in packet even if there is Binding SID, meaning no SR-ERO/SRv6-ERO validation will be done.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeConfiguredERO"])
        )

    @property
    def IncludeSrp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether SRP object will be included in a PCInitiate message. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeSrp"]))

    @property
    def IncludeSymbolicPathName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if Symbolic-Path-Name TLV is to be included in PCUpate trigger message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeSymbolicPathName"])
        )

    @property
    def IncludeTEPathBindingTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if TE-PATH-BINDING TLV is to be included in PCUpate trigger message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeTEPathBindingTLV"])
        )

    @property
    def IncludeXro(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether XRO object will be included in a PcUpdate message. All other attributes in sub-tab Update XRO would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeXro"]))

    @property
    def LocalProtection(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Protection
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalProtection"])
        )

    @property
    def MplsLabel(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This control will be editable if the Binding Type is set to either 20bit or 32bit MPLS-Label. This field will take the 20bit value of the MPLS-Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MplsLabel"]))

    @property
    def NumberOfAssociationObjects(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value that indicates the number of Association Objects to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfAssociationObjects"])

    @NumberOfAssociationObjects.setter
    def NumberOfAssociationObjects(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfAssociationObjects"], value)

    @property
    def NumberOfEroSubObjects(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value that indicates the number of ERO Sub Objects to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfEroSubObjects"])

    @NumberOfEroSubObjects.setter
    def NumberOfEroSubObjects(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfEroSubObjects"], value)

    @property
    def NumberOfMetricSubObjects(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value that indicates the number of Metric Objects to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfMetricSubObjects"])

    @NumberOfMetricSubObjects.setter
    def NumberOfMetricSubObjects(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfMetricSubObjects"], value)

    @property
    def NumberOfTEPathBindingTLV(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value that indicates the number of TE-PATH-BINDING TLV to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfTEPathBindingTLV"])

    @NumberOfTEPathBindingTLV.setter
    def NumberOfTEPathBindingTLV(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfTEPathBindingTLV"], value)

    @property
    def NumberOfXroSubObjects(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value that indicates the number of XRO Sub Objects to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfXroSubObjects"])

    @NumberOfXroSubObjects.setter
    def NumberOfXroSubObjects(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfXroSubObjects"], value)

    @property
    def OverridePLSPID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Allows the user to Send PcUpdate with an unknown PLSP-ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OverridePLSPID"])
        )

    @property
    def OverrideSrpId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether SRP object will be included in a PCUpdate trigger parameters. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OverrideSrpId"]))

    @property
    def PceTriggersChoiceList(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Based on options selected, IxNetwork sends information to PCPU and refreshes the statistical data in the corresponding tab of Learned Information
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PceTriggersChoiceList"])
        )

    @property
    def PlspIdTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value of PLSP-ID that should be put in the PcUpdate Message
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PlspIdTriggerParam"])
        )

    @property
    def ProtectionLsp(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Protection LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProtectionLsp"]))

    @property
    def RemoveAssociation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remove Association
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoveAssociation"])
        )

    @property
    def SendEmptyTLV(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled all fields after Binding Type will be grayed out.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SendEmptyTLV"]))

    @property
    def SetupPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Setup Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SetupPriority"]))

    @property
    def SrpId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The SRP object is used to correlate between initiation requests sent by the PCE and the error reports and state reports sent by the PCC. This number is unique per PCEP session and is incremented per initiation.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrpId"]))

    @property
    def Srv6SID(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID with a format of a 16 byte IPv6 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6SID"]))

    @property
    def StandbyMode(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Standby Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StandbyMode"]))

    @property
    def Tc(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field is used to carry traffic class information. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tc"]))

    @property
    def Ttl(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field is used to encode a time-to-live value. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ttl"]))

    @property
    def XroFailBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): XRO Fail bit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["XroFailBit"]))

    def update(
        self,
        NumberOfAssociationObjects=None,
        NumberOfEroSubObjects=None,
        NumberOfMetricSubObjects=None,
        NumberOfTEPathBindingTLV=None,
        NumberOfXroSubObjects=None,
    ):
        # type: (int, int, int, int, int) -> PceBasicSrv6SyncLspUpdateParams
        """Updates pceBasicSrv6SyncLspUpdateParams resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - NumberOfAssociationObjects (number): Value that indicates the number of Association Objects to be configured.
        - NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfTEPathBindingTLV (number): Value that indicates the number of TE-PATH-BINDING TLV to be configured.
        - NumberOfXroSubObjects (number): Value that indicates the number of XRO Sub Objects to be configured.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        NumberOfAssociationObjects=None,
        NumberOfEroSubObjects=None,
        NumberOfMetricSubObjects=None,
        NumberOfTEPathBindingTLV=None,
        NumberOfXroSubObjects=None,
    ):
        # type: (int, int, int, int, int) -> PceBasicSrv6SyncLspUpdateParams
        """Adds a new pceBasicSrv6SyncLspUpdateParams resource on the json, only valid with batch add utility

        Args
        ----
        - NumberOfAssociationObjects (number): Value that indicates the number of Association Objects to be configured.
        - NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfTEPathBindingTLV (number): Value that indicates the number of TE-PATH-BINDING TLV to be configured.
        - NumberOfXroSubObjects (number): Value that indicates the number of XRO Sub Objects to be configured.

        Returns
        -------
        - self: This instance with all currently retrieved pceBasicSrv6SyncLspUpdateParams resources using find and the newly added pceBasicSrv6SyncLspUpdateParams resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        NumberOfAssociationObjects=None,
        NumberOfEroSubObjects=None,
        NumberOfMetricSubObjects=None,
        NumberOfTEPathBindingTLV=None,
        NumberOfXroSubObjects=None,
    ):
        # type: (int, int, int, int, int) -> PceBasicSrv6SyncLspUpdateParams
        """Finds and retrieves pceBasicSrv6SyncLspUpdateParams resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pceBasicSrv6SyncLspUpdateParams resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pceBasicSrv6SyncLspUpdateParams resources from the server.

        Args
        ----
        - NumberOfAssociationObjects (number): Value that indicates the number of Association Objects to be configured.
        - NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfTEPathBindingTLV (number): Value that indicates the number of TE-PATH-BINDING TLV to be configured.
        - NumberOfXroSubObjects (number): Value that indicates the number of XRO Sub Objects to be configured.

        Returns
        -------
        - self: This instance with matching pceBasicSrv6SyncLspUpdateParams resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pceBasicSrv6SyncLspUpdateParams data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pceBasicSrv6SyncLspUpdateParams resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def SendPcUpdate(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendPcUpdate operation on the server.

        Counts property changes created by the user.

        sendPcUpdate(Arg2=list, async_operation=bool)list
        -------------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("sendPcUpdate", payload=payload, response_object=None)

    def SendReturnDelegation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendReturnDelegation operation on the server.

        Counts property changes created by the user.

        sendReturnDelegation(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
            "sendReturnDelegation", payload=payload, response_object=None
        )

    def get_device_ids(
        self,
        PortNames=None,
        AssociationId=None,
        Bandwidth=None,
        BindingType=None,
        Bos=None,
        ConfigureAssociation=None,
        ConfigureBandwidth=None,
        ConfigureEro=None,
        ConfigureLsp=None,
        ConfigureLspa=None,
        ConfigureMetric=None,
        ExcludeAny=None,
        HoldingPriority=None,
        IncludeAll=None,
        IncludeAny=None,
        IncludeAssociation=None,
        IncludeConfiguredERO=None,
        IncludeSrp=None,
        IncludeSymbolicPathName=None,
        IncludeTEPathBindingTLV=None,
        IncludeXro=None,
        LocalProtection=None,
        MplsLabel=None,
        OverridePLSPID=None,
        OverrideSrpId=None,
        PceTriggersChoiceList=None,
        PlspIdTriggerParam=None,
        ProtectionLsp=None,
        RemoveAssociation=None,
        SendEmptyTLV=None,
        SetupPriority=None,
        SrpId=None,
        Srv6SID=None,
        StandbyMode=None,
        Tc=None,
        Ttl=None,
        XroFailBit=None,
    ):
        """Base class infrastructure that gets a list of pceBasicSrv6SyncLspUpdateParams device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AssociationId (str): optional regex of associationId
        - Bandwidth (str): optional regex of bandwidth
        - BindingType (str): optional regex of bindingType
        - Bos (str): optional regex of bos
        - ConfigureAssociation (str): optional regex of configureAssociation
        - ConfigureBandwidth (str): optional regex of configureBandwidth
        - ConfigureEro (str): optional regex of configureEro
        - ConfigureLsp (str): optional regex of configureLsp
        - ConfigureLspa (str): optional regex of configureLspa
        - ConfigureMetric (str): optional regex of configureMetric
        - ExcludeAny (str): optional regex of excludeAny
        - HoldingPriority (str): optional regex of holdingPriority
        - IncludeAll (str): optional regex of includeAll
        - IncludeAny (str): optional regex of includeAny
        - IncludeAssociation (str): optional regex of includeAssociation
        - IncludeConfiguredERO (str): optional regex of includeConfiguredERO
        - IncludeSrp (str): optional regex of includeSrp
        - IncludeSymbolicPathName (str): optional regex of includeSymbolicPathName
        - IncludeTEPathBindingTLV (str): optional regex of includeTEPathBindingTLV
        - IncludeXro (str): optional regex of includeXro
        - LocalProtection (str): optional regex of localProtection
        - MplsLabel (str): optional regex of mplsLabel
        - OverridePLSPID (str): optional regex of overridePLSPID
        - OverrideSrpId (str): optional regex of overrideSrpId
        - PceTriggersChoiceList (str): optional regex of pceTriggersChoiceList
        - PlspIdTriggerParam (str): optional regex of plspIdTriggerParam
        - ProtectionLsp (str): optional regex of protectionLsp
        - RemoveAssociation (str): optional regex of removeAssociation
        - SendEmptyTLV (str): optional regex of sendEmptyTLV
        - SetupPriority (str): optional regex of setupPriority
        - SrpId (str): optional regex of srpId
        - Srv6SID (str): optional regex of srv6SID
        - StandbyMode (str): optional regex of standbyMode
        - Tc (str): optional regex of tc
        - Ttl (str): optional regex of ttl
        - XroFailBit (str): optional regex of xroFailBit

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
