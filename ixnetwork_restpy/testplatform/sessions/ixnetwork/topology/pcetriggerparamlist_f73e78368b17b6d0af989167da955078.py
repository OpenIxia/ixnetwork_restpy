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


class PceTriggerParamList(Base):
    """PceLearnedInfoTriggerParam
    The PceTriggerParamList class encapsulates a list of pceTriggerParamList resources that are managed by the user.
    A list of resources can be retrieved from the server using the PceTriggerParamList.find() method.
    The list can be managed by using the PceTriggerParamList.add() and PceTriggerParamList.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "pceTriggerParamList"
    _SDM_ATT_MAP = {
        "AssociationIdForTriggerParam": "associationIdForTriggerParam",
        "Bandwidth": "bandwidth",
        "BindingTypeTriggerParam": "bindingTypeTriggerParam",
        "Bos_TriggerParam": "bos_TriggerParam",
        "ConfigureBandwidthForSendPcUpdateTriggerParam": "configureBandwidthForSendPcUpdateTriggerParam",
        "ConfigureEroForSendPcUpdateTriggerParam": "configureEroForSendPcUpdateTriggerParam",
        "ConfigureLspForSendPcUpdateTriggerParam": "configureLspForSendPcUpdateTriggerParam",
        "ConfigureLspaForSendPcUpdateTriggerParam": "configureLspaForSendPcUpdateTriggerParam",
        "ConfigureMetricForSendPcUpdateTriggerParam": "configureMetricForSendPcUpdateTriggerParam",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "DeviceIndex": "deviceIndex",
        "ExcludeAnyForTriggerParam": "excludeAnyForTriggerParam",
        "HoldingPriorityForTriggerParam": "holdingPriorityForTriggerParam",
        "IncludeAllForTriggerParam": "includeAllForTriggerParam",
        "IncludeAnyForTriggerParam": "includeAnyForTriggerParam",
        "IncludeAssociation": "includeAssociation",
        "IncludeConfiguredERO_TriggerParam": "includeConfiguredERO_TriggerParam",
        "IncludeSrp": "includeSrp",
        "IncludeSymbolicPathNameTlvTriggerParam": "includeSymbolicPathNameTlvTriggerParam",
        "IncludeTEPathBindingTLV": "includeTEPathBindingTLV",
        "IncludeXro": "includeXro",
        "LearnedPlspId": "learnedPlspId",
        "LearnedSymbolicPathName": "learnedSymbolicPathName",
        "LocalProtectionForTriggerParam": "localProtectionForTriggerParam",
        "Mpls_label_20_TriggerParam": "mpls_label_20_TriggerParam",
        "Name": "name",
        "NumberOfAssociationObjectsTriggerParam": "numberOfAssociationObjectsTriggerParam",
        "NumberOfEroSubObjectsTriggerParam": "numberOfEroSubObjectsTriggerParam",
        "NumberOfMetricSubObjectTriggerParam": "numberOfMetricSubObjectTriggerParam",
        "NumberOfTEPathBindingTLVTriggerParam": "numberOfTEPathBindingTLVTriggerParam",
        "NumberOfXroSubObjectsTriggerParam": "numberOfXroSubObjectsTriggerParam",
        "OverridePLSPID": "overridePLSPID",
        "OverrideSrpId": "overrideSrpId",
        "PlspIdTriggerParam": "plspIdTriggerParam",
        "ProtectionLspStatusForTriggerParam": "protectionLspStatusForTriggerParam",
        "RemoveAssociationStatusForTriggerParam": "removeAssociationStatusForTriggerParam",
        "SendEmptyTLVTriggerParam": "sendEmptyTLVTriggerParam",
        "SetupPriorityForTriggerParam": "setupPriorityForTriggerParam",
        "SrpId": "srpId",
        "Srv6SID_TriggerParam": "srv6SID_TriggerParam",
        "StandbyModeStatusForTriggerParam": "standbyModeStatusForTriggerParam",
        "Tos_TriggerParam": "tos_TriggerParam",
        "Ttl_TriggerParam": "ttl_TriggerParam",
        "XroFailBit": "xroFailBit",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PceTriggerParamList, self).__init__(parent, list_op)

    @property
    def PcepAssociationObjectsListTriggerParam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepassociationobjectslisttriggerparam_6b13018b4290569a0b0887965ecab0ca.PcepAssociationObjectsListTriggerParam): An instance of the PcepAssociationObjectsListTriggerParam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepassociationobjectslisttriggerparam_6b13018b4290569a0b0887965ecab0ca import (
            PcepAssociationObjectsListTriggerParam,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("PcepAssociationObjectsListTriggerParam", None)
                is not None
            ):
                return self._properties.get("PcepAssociationObjectsListTriggerParam")
        return PcepAssociationObjectsListTriggerParam(self)

    @property
    def PcepEROObjectsListTriggerParam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceperoobjectslisttriggerparam_7a5c524782bff6932bd99b311c55e9ad.PcepEROObjectsListTriggerParam): An instance of the PcepEROObjectsListTriggerParam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceperoobjectslisttriggerparam_7a5c524782bff6932bd99b311c55e9ad import (
            PcepEROObjectsListTriggerParam,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PcepEROObjectsListTriggerParam", None) is not None:
                return self._properties.get("PcepEROObjectsListTriggerParam")
        return PcepEROObjectsListTriggerParam(self)

    @property
    def PcepMetricSubObjectsListTriggerParam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepmetricsubobjectslisttriggerparam_de2e60079005ccd984641de408d76c7e.PcepMetricSubObjectsListTriggerParam): An instance of the PcepMetricSubObjectsListTriggerParam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepmetricsubobjectslisttriggerparam_de2e60079005ccd984641de408d76c7e import (
            PcepMetricSubObjectsListTriggerParam,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("PcepMetricSubObjectsListTriggerParam", None)
                is not None
            ):
                return self._properties.get("PcepMetricSubObjectsListTriggerParam")
        return PcepMetricSubObjectsListTriggerParam(self)

    @property
    def PcepTEPATHBINDINGTLVListTriggerParam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceptepathbindingtlvlisttriggerparam_73209d05e577378a56b9722352f1235b.PcepTEPATHBINDINGTLVListTriggerParam): An instance of the PcepTEPATHBINDINGTLVListTriggerParam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceptepathbindingtlvlisttriggerparam_73209d05e577378a56b9722352f1235b import (
            PcepTEPATHBINDINGTLVListTriggerParam,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("PcepTEPATHBINDINGTLVListTriggerParam", None)
                is not None
            ):
                return self._properties.get("PcepTEPATHBINDINGTLVListTriggerParam")
        return PcepTEPATHBINDINGTLVListTriggerParam(self)

    @property
    def PcepXROObjectsListTriggerParam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepxroobjectslisttriggerparam_5f7b6057618984dd647c0e901b41ccfc.PcepXROObjectsListTriggerParam): An instance of the PcepXROObjectsListTriggerParam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepxroobjectslisttriggerparam_5f7b6057618984dd647c0e901b41ccfc import (
            PcepXROObjectsListTriggerParam,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PcepXROObjectsListTriggerParam", None) is not None:
                return self._properties.get("PcepXROObjectsListTriggerParam")
        return PcepXROObjectsListTriggerParam(self)

    @property
    def AssociationIdForTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Association ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AssociationIdForTriggerParam"])
        )

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
    def BindingTypeTriggerParam(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the type of binding included in the TLV. Types are as follows: 20bit MPLS Label 32bit MPLS Label SRv6 SID Default value is 20bit MPLS Label.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingTypeTriggerParam"])
        )

    @property
    def Bos_TriggerParam(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This bit is set to True for the last entry in the label stack i.e., for the bottom of the stack, and False for all other label stack entries. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Bos_TriggerParam"])
        )

    @property
    def ConfigureBandwidthForSendPcUpdateTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure Bandwidth
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ConfigureBandwidthForSendPcUpdateTriggerParam"]
            ),
        )

    @property
    def ConfigureEroForSendPcUpdateTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure ERO
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ConfigureEroForSendPcUpdateTriggerParam"]
            ),
        )

    @property
    def ConfigureLspForSendPcUpdateTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ConfigureLspForSendPcUpdateTriggerParam"]
            ),
        )

    @property
    def ConfigureLspaForSendPcUpdateTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure LSPA
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ConfigureLspaForSendPcUpdateTriggerParam"]
            ),
        )

    @property
    def ConfigureMetricForSendPcUpdateTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ConfigureMetricForSendPcUpdateTriggerParam"]
            ),
        )

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def DeviceIndex(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Device Index of the parent PCCGroup Device
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeviceIndex"])

    @DeviceIndex.setter
    def DeviceIndex(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeviceIndex"], value)

    @property
    def ExcludeAnyForTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Exclude Any
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExcludeAnyForTriggerParam"])
        )

    @property
    def HoldingPriorityForTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Holding Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HoldingPriorityForTriggerParam"]),
        )

    @property
    def IncludeAllForTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include All
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeAllForTriggerParam"])
        )

    @property
    def IncludeAnyForTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Any
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeAnyForTriggerParam"])
        )

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
    def IncludeConfiguredERO_TriggerParam(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is enabled, entire ERO will be go out in packet even if there is Binding SID, meaning no SR-ERO/SRv6-ERO validation will be done.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IncludeConfiguredERO_TriggerParam"]),
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
    def IncludeSymbolicPathNameTlvTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if Symbolic-Path-Name TLV is to be included in PCUpate trigger message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IncludeSymbolicPathNameTlvTriggerParam"]
            ),
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
    def LearnedPlspId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PLSP-ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LearnedPlspId"]))

    @property
    def LearnedSymbolicPathName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Symbolic Path Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LearnedSymbolicPathName"])
        )

    @property
    def LocalProtectionForTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Protection
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LocalProtectionForTriggerParam"]),
        )

    @property
    def Mpls_label_20_TriggerParam(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This control will be editable if the Binding Type is set to either 20bit or 32bit MPLS-Label. This field will take the 20bit value of the MPLS-Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Mpls_label_20_TriggerParam"])
        )

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NumberOfAssociationObjectsTriggerParam(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value that indicates the number of Association Objects to be configured.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["NumberOfAssociationObjectsTriggerParam"]
        )

    @NumberOfAssociationObjectsTriggerParam.setter
    def NumberOfAssociationObjectsTriggerParam(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["NumberOfAssociationObjectsTriggerParam"], value
        )

    @property
    def NumberOfEroSubObjectsTriggerParam(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value that indicates the number of ERO Sub Objects to be configured.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["NumberOfEroSubObjectsTriggerParam"]
        )

    @NumberOfEroSubObjectsTriggerParam.setter
    def NumberOfEroSubObjectsTriggerParam(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["NumberOfEroSubObjectsTriggerParam"], value
        )

    @property
    def NumberOfMetricSubObjectTriggerParam(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value that indicates the number of Metric Objects to be configured.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["NumberOfMetricSubObjectTriggerParam"]
        )

    @NumberOfMetricSubObjectTriggerParam.setter
    def NumberOfMetricSubObjectTriggerParam(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["NumberOfMetricSubObjectTriggerParam"], value
        )

    @property
    def NumberOfTEPathBindingTLVTriggerParam(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value that indicates the number of TE-PATH-BINDING TLV to be configured.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["NumberOfTEPathBindingTLVTriggerParam"]
        )

    @NumberOfTEPathBindingTLVTriggerParam.setter
    def NumberOfTEPathBindingTLVTriggerParam(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["NumberOfTEPathBindingTLVTriggerParam"], value
        )

    @property
    def NumberOfXroSubObjectsTriggerParam(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value that indicates the number of XRO Sub Objects to be configured.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["NumberOfXroSubObjectsTriggerParam"]
        )

    @NumberOfXroSubObjectsTriggerParam.setter
    def NumberOfXroSubObjectsTriggerParam(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["NumberOfXroSubObjectsTriggerParam"], value
        )

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
    def ProtectionLspStatusForTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Protection LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProtectionLspStatusForTriggerParam"]
            ),
        )

    @property
    def RemoveAssociationStatusForTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remove Association
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RemoveAssociationStatusForTriggerParam"]
            ),
        )

    @property
    def SendEmptyTLVTriggerParam(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled all fields after Binding Type will be grayed out.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendEmptyTLVTriggerParam"])
        )

    @property
    def SetupPriorityForTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Setup Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SetupPriorityForTriggerParam"])
        )

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
    def Srv6SID_TriggerParam(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID with a format of a 16 byte IPv6 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6SID_TriggerParam"])
        )

    @property
    def StandbyModeStatusForTriggerParam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Standby Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["StandbyModeStatusForTriggerParam"]),
        )

    @property
    def Tos_TriggerParam(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field is used to carry traffic class information. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tos_TriggerParam"])
        )

    @property
    def Ttl_TriggerParam(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field is used to encode a time-to-live value. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ttl_TriggerParam"])
        )

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
        DeviceIndex=None,
        Name=None,
        NumberOfAssociationObjectsTriggerParam=None,
        NumberOfEroSubObjectsTriggerParam=None,
        NumberOfMetricSubObjectTriggerParam=None,
        NumberOfTEPathBindingTLVTriggerParam=None,
        NumberOfXroSubObjectsTriggerParam=None,
    ):
        # type: (int, str, int, int, int, int, int) -> PceTriggerParamList
        """Updates pceTriggerParamList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - DeviceIndex (number): Device Index of the parent PCCGroup Device
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAssociationObjectsTriggerParam (number): Value that indicates the number of Association Objects to be configured.
        - NumberOfEroSubObjectsTriggerParam (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObjectTriggerParam (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfTEPathBindingTLVTriggerParam (number): Value that indicates the number of TE-PATH-BINDING TLV to be configured.
        - NumberOfXroSubObjectsTriggerParam (number): Value that indicates the number of XRO Sub Objects to be configured.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        DeviceIndex=None,
        Name=None,
        NumberOfAssociationObjectsTriggerParam=None,
        NumberOfEroSubObjectsTriggerParam=None,
        NumberOfMetricSubObjectTriggerParam=None,
        NumberOfTEPathBindingTLVTriggerParam=None,
        NumberOfXroSubObjectsTriggerParam=None,
    ):
        # type: (int, str, int, int, int, int, int) -> PceTriggerParamList
        """Adds a new pceTriggerParamList resource on the server and adds it to the container.

        Args
        ----
        - DeviceIndex (number): Device Index of the parent PCCGroup Device
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAssociationObjectsTriggerParam (number): Value that indicates the number of Association Objects to be configured.
        - NumberOfEroSubObjectsTriggerParam (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObjectTriggerParam (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfTEPathBindingTLVTriggerParam (number): Value that indicates the number of TE-PATH-BINDING TLV to be configured.
        - NumberOfXroSubObjectsTriggerParam (number): Value that indicates the number of XRO Sub Objects to be configured.

        Returns
        -------
        - self: This instance with all currently retrieved pceTriggerParamList resources using find and the newly added pceTriggerParamList resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained pceTriggerParamList resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        DeviceIndex=None,
        Name=None,
        NumberOfAssociationObjectsTriggerParam=None,
        NumberOfEroSubObjectsTriggerParam=None,
        NumberOfMetricSubObjectTriggerParam=None,
        NumberOfTEPathBindingTLVTriggerParam=None,
        NumberOfXroSubObjectsTriggerParam=None,
    ):
        # type: (int, str, int, str, int, int, int, int, int) -> PceTriggerParamList
        """Finds and retrieves pceTriggerParamList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pceTriggerParamList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pceTriggerParamList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - DeviceIndex (number): Device Index of the parent PCCGroup Device
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAssociationObjectsTriggerParam (number): Value that indicates the number of Association Objects to be configured.
        - NumberOfEroSubObjectsTriggerParam (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObjectTriggerParam (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfTEPathBindingTLVTriggerParam (number): Value that indicates the number of TE-PATH-BINDING TLV to be configured.
        - NumberOfXroSubObjectsTriggerParam (number): Value that indicates the number of XRO Sub Objects to be configured.

        Returns
        -------
        - self: This instance with matching pceTriggerParamList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pceTriggerParamList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pceTriggerParamList resources from the server available through an iterator or index

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

    def get_device_ids(
        self,
        PortNames=None,
        AssociationIdForTriggerParam=None,
        Bandwidth=None,
        BindingTypeTriggerParam=None,
        Bos_TriggerParam=None,
        ConfigureBandwidthForSendPcUpdateTriggerParam=None,
        ConfigureEroForSendPcUpdateTriggerParam=None,
        ConfigureLspForSendPcUpdateTriggerParam=None,
        ConfigureLspaForSendPcUpdateTriggerParam=None,
        ConfigureMetricForSendPcUpdateTriggerParam=None,
        ExcludeAnyForTriggerParam=None,
        HoldingPriorityForTriggerParam=None,
        IncludeAllForTriggerParam=None,
        IncludeAnyForTriggerParam=None,
        IncludeAssociation=None,
        IncludeConfiguredERO_TriggerParam=None,
        IncludeSrp=None,
        IncludeSymbolicPathNameTlvTriggerParam=None,
        IncludeTEPathBindingTLV=None,
        IncludeXro=None,
        LearnedPlspId=None,
        LearnedSymbolicPathName=None,
        LocalProtectionForTriggerParam=None,
        Mpls_label_20_TriggerParam=None,
        OverridePLSPID=None,
        OverrideSrpId=None,
        PlspIdTriggerParam=None,
        ProtectionLspStatusForTriggerParam=None,
        RemoveAssociationStatusForTriggerParam=None,
        SendEmptyTLVTriggerParam=None,
        SetupPriorityForTriggerParam=None,
        SrpId=None,
        Srv6SID_TriggerParam=None,
        StandbyModeStatusForTriggerParam=None,
        Tos_TriggerParam=None,
        Ttl_TriggerParam=None,
        XroFailBit=None,
    ):
        """Base class infrastructure that gets a list of pceTriggerParamList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AssociationIdForTriggerParam (str): optional regex of associationIdForTriggerParam
        - Bandwidth (str): optional regex of bandwidth
        - BindingTypeTriggerParam (str): optional regex of bindingTypeTriggerParam
        - Bos_TriggerParam (str): optional regex of bos_TriggerParam
        - ConfigureBandwidthForSendPcUpdateTriggerParam (str): optional regex of configureBandwidthForSendPcUpdateTriggerParam
        - ConfigureEroForSendPcUpdateTriggerParam (str): optional regex of configureEroForSendPcUpdateTriggerParam
        - ConfigureLspForSendPcUpdateTriggerParam (str): optional regex of configureLspForSendPcUpdateTriggerParam
        - ConfigureLspaForSendPcUpdateTriggerParam (str): optional regex of configureLspaForSendPcUpdateTriggerParam
        - ConfigureMetricForSendPcUpdateTriggerParam (str): optional regex of configureMetricForSendPcUpdateTriggerParam
        - ExcludeAnyForTriggerParam (str): optional regex of excludeAnyForTriggerParam
        - HoldingPriorityForTriggerParam (str): optional regex of holdingPriorityForTriggerParam
        - IncludeAllForTriggerParam (str): optional regex of includeAllForTriggerParam
        - IncludeAnyForTriggerParam (str): optional regex of includeAnyForTriggerParam
        - IncludeAssociation (str): optional regex of includeAssociation
        - IncludeConfiguredERO_TriggerParam (str): optional regex of includeConfiguredERO_TriggerParam
        - IncludeSrp (str): optional regex of includeSrp
        - IncludeSymbolicPathNameTlvTriggerParam (str): optional regex of includeSymbolicPathNameTlvTriggerParam
        - IncludeTEPathBindingTLV (str): optional regex of includeTEPathBindingTLV
        - IncludeXro (str): optional regex of includeXro
        - LearnedPlspId (str): optional regex of learnedPlspId
        - LearnedSymbolicPathName (str): optional regex of learnedSymbolicPathName
        - LocalProtectionForTriggerParam (str): optional regex of localProtectionForTriggerParam
        - Mpls_label_20_TriggerParam (str): optional regex of mpls_label_20_TriggerParam
        - OverridePLSPID (str): optional regex of overridePLSPID
        - OverrideSrpId (str): optional regex of overrideSrpId
        - PlspIdTriggerParam (str): optional regex of plspIdTriggerParam
        - ProtectionLspStatusForTriggerParam (str): optional regex of protectionLspStatusForTriggerParam
        - RemoveAssociationStatusForTriggerParam (str): optional regex of removeAssociationStatusForTriggerParam
        - SendEmptyTLVTriggerParam (str): optional regex of sendEmptyTLVTriggerParam
        - SetupPriorityForTriggerParam (str): optional regex of setupPriorityForTriggerParam
        - SrpId (str): optional regex of srpId
        - Srv6SID_TriggerParam (str): optional regex of srv6SID_TriggerParam
        - StandbyModeStatusForTriggerParam (str): optional regex of standbyModeStatusForTriggerParam
        - Tos_TriggerParam (str): optional regex of tos_TriggerParam
        - Ttl_TriggerParam (str): optional regex of ttl_TriggerParam
        - XroFailBit (str): optional regex of xroFailBit

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
