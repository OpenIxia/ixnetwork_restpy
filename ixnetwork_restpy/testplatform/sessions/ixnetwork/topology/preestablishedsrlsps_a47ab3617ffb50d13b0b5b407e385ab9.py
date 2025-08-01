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


class PreEstablishedSrLsps(Base):
    """Pre-Established SR LSPs
    The PreEstablishedSrLsps class encapsulates a required preEstablishedSrLsps resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "preEstablishedSrLsps"
    _SDM_ATT_MAP = {
        "Active": "active",
        "ActiveDataTrafficEndpoint": "activeDataTrafficEndpoint",
        "AssociationId": "associationId",
        "Bandwidth": "bandwidth",
        "BindingType": "bindingType",
        "Bos": "bos",
        "ComputationPriority": "computationPriority",
        "ComputationPriorityReserved": "computationPriorityReserved",
        "ConfigStateDFlag": "configStateDFlag",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "DestEndPointIpv4": "destEndPointIpv4",
        "DestinationIpv4Address": "destinationIpv4Address",
        "DestinationIpv6Address": "destinationIpv6Address",
        "ENLP": "eNLP",
        "ENLPReserved": "eNLPReserved",
        "ExcludeAny": "excludeAny",
        "HoldingPriority": "holdingPriority",
        "IncludeAll": "includeAll",
        "IncludeAny": "includeAny",
        "IncludeAssociation": "includeAssociation",
        "IncludeBandwidth": "includeBandwidth",
        "IncludeComputationPriorityTLV": "includeComputationPriorityTLV",
        "IncludeConfiguredERO": "includeConfiguredERO",
        "IncludeENLPTLV": "includeENLPTLV",
        "IncludeEro": "includeEro",
        "IncludeInvalidationTLV": "includeInvalidationTLV",
        "IncludeLsp": "includeLsp",
        "IncludeLspa": "includeLspa",
        "IncludeMetric": "includeMetric",
        "IncludePpag": "includePpag",
        "IncludeSrp": "includeSrp",
        "IncludeSymbolicPathNameTlv": "includeSymbolicPathNameTlv",
        "IncludeTEPathBindingTLV": "includeTEPathBindingTLV",
        "InitialDelegation": "initialDelegation",
        "InsertIpv6ExplicitNull": "insertIpv6ExplicitNull",
        "InvalidationReserved": "invalidationReserved",
        "LocalProtection": "localProtection",
        "LspDelegationState": "lspDelegationState",
        "MplsLabel": "mplsLabel",
        "Name": "name",
        "NumberOfAssociationObjects": "numberOfAssociationObjects",
        "NumberOfEroSubObjects": "numberOfEroSubObjects",
        "NumberOfMetricSubObject": "numberOfMetricSubObject",
        "NumberOfTEPathBindingTLV": "numberOfTEPathBindingTLV",
        "OperStateDFlag": "operStateDFlag",
        "OverridePlspId": "overridePlspId",
        "PathSetupType": "pathSetupType",
        "PlspId": "plspId",
        "ProtectionLspBit": "protectionLspBit",
        "ReDelegationTimerStatus": "reDelegationTimerStatus",
        "RedelegationTimeoutInterval": "redelegationTimeoutInterval",
        "SetupPriority": "setupPriority",
        "SrcEndPointIpv4": "srcEndPointIpv4",
        "SrcEndPointIpv6": "srcEndPointIpv6",
        "SrcIpv4": "srcIpv4",
        "Srv6SID": "srv6SID",
        "StandbyLspBit": "standbyLspBit",
        "SymbolicPathName": "symbolicPathName",
        "Tc": "tc",
        "Ttl": "ttl",
    }
    _SDM_ENUM_MAP = {
        "pathSetupType": ["sR", "sRv6"],
    }

    def __init__(self, parent, list_op=False):
        super(PreEstablishedSrLsps, self).__init__(parent, list_op)

    @property
    def PcepAssociationObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepassociationobjectslist_809d161eaa571fb4817c7358cc0e660c.PcepAssociationObjectsList): An instance of the PcepAssociationObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepassociationobjectslist_809d161eaa571fb4817c7358cc0e660c import (
            PcepAssociationObjectsList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PcepAssociationObjectsList", None) is not None:
                return self._properties.get("PcepAssociationObjectsList")
        return PcepAssociationObjectsList(self)

    @property
    def PcepEroSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceperosubobjectslist_86d5cc1708b448f03a004b8dddbd83d7.PcepEroSubObjectsList): An instance of the PcepEroSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceperosubobjectslist_86d5cc1708b448f03a004b8dddbd83d7 import (
            PcepEroSubObjectsList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PcepEroSubObjectsList", None) is not None:
                return self._properties.get("PcepEroSubObjectsList")
        return PcepEroSubObjectsList(self)

    @property
    def PcepMetricSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepmetricsubobjectslist_b1398d82dd25e8e98d50662ebf5ba3d1.PcepMetricSubObjectsList): An instance of the PcepMetricSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepmetricsubobjectslist_b1398d82dd25e8e98d50662ebf5ba3d1 import (
            PcepMetricSubObjectsList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PcepMetricSubObjectsList", None) is not None:
                return self._properties.get("PcepMetricSubObjectsList")
        return PcepMetricSubObjectsList(self)

    @property
    def PcepSRv6EROObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepsrv6eroobjectslist_205ff487307c7e9626812588ef2b6684.PcepSRv6EROObjectsList): An instance of the PcepSRv6EROObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepsrv6eroobjectslist_205ff487307c7e9626812588ef2b6684 import (
            PcepSRv6EROObjectsList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PcepSRv6EROObjectsList", None) is not None:
                return self._properties.get("PcepSRv6EROObjectsList")
        return PcepSRv6EROObjectsList(self)

    @property
    def PcepTEPATHBINDINGTLVList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceptepathbindingtlvlist_a446e2f09315dac50332432f39dfd53a.PcepTEPATHBINDINGTLVList): An instance of the PcepTEPATHBINDINGTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceptepathbindingtlvlist_a446e2f09315dac50332432f39dfd53a import (
            PcepTEPATHBINDINGTLVList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PcepTEPATHBINDINGTLVList", None) is not None:
                return self._properties.get("PcepTEPATHBINDINGTLVList")
        return PcepTEPATHBINDINGTLVList(self)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import (
            Tag,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Tag", None) is not None:
                return self._properties.get("Tag")
        return Tag(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def ActiveDataTrafficEndpoint(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies whether that specific Data Traffic Endpoint will generate data traffic
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActiveDataTrafficEndpoint"])
        )

    @property
    def AssociationId(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Association ID of this LSP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AssociationId"]))

    @property
    def Bandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth (bits/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Bandwidth"]))

    @property
    def BindingType(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the type of binding included in the TLV. Types are as follows:20bit MPLS Label32bit MPLS Label.SRv6 SIDSRv6 SID with SRv6 Endpoint Behavior and SID StructureDefault value is 20bit MPLS Label.
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
    def ComputationPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This TLV is used to signal the numerical computation priority.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ComputationPriority"])
        )

    @property
    def ComputationPriorityReserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved Field for Computation Priority TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ComputationPriorityReserved"])
        )

    @property
    def ConfigStateDFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): It encodes the current setting of the Drop-upon-invalid feature.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfigStateDFlag"])
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
    def DestEndPointIpv4(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination end point of the LSP, used to detect end point mismatch error if PCE changes association
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DestEndPointIpv4"])
        )

    @property
    def DestinationIpv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination IPv4 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DestinationIpv4Address"])
        )

    @property
    def DestinationIpv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination IPv6 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DestinationIpv6Address"])
        )

    @property
    def ENLP(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether an Explicit NULL Label must be pushed on an unlabeled IP packet before any other labels.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ENLP"]))

    @property
    def ENLPReserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved Field for ENLP TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ENLPReserved"]))

    @property
    def ExcludeAny(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a type of Resource Affinity Procedure that is used to validate a link. This control accepts a link only if the link carries all of the attributes in the set.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ExcludeAny"]))

    @property
    def HoldingPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The priority of the LSP with respect to holding resources. The value 0 is the highest priority. Holding Priority is used in deciding whether this session can be preempted by another session.
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
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a type of Resource Affinity Procedure that is used to validate a link. This control excludes a link from consideration if the link carries any of the attributes in the set.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeAll"]))

    @property
    def IncludeAny(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a type of Resource Affinity Procedure that is used to validate a link. This control accepts a link if the link carries any of the attributes in the set.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeAny"]))

    @property
    def IncludeAssociation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Association will be included in a Sync PCReport message. All other attributes in sub-tab-Association would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeAssociation"])
        )

    @property
    def IncludeBandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Bandwidth will be included in a PCInitiate message. All other attributes in sub-tab-Bandwidth would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeBandwidth"])
        )

    @property
    def IncludeComputationPriorityTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if Computation Priority TLV is to be included in PCInitiate message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IncludeComputationPriorityTLV"]),
        )

    @property
    def IncludeConfiguredERO(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is enabled, entire ERO will go out in packet even if there is Binding SID, which means no SR-ERO/SRv6-ERO validation will be done.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeConfiguredERO"])
        )

    @property
    def IncludeENLPTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if ENLP TLV is to be included in PCInitiate message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeENLPTLV"])
        )

    @property
    def IncludeEro(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies whether ERO is active or inactive. All subsequent attributes of the sub-tab-ERO would be editable only if this is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeEro"]))

    @property
    def IncludeInvalidationTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether the Invalidation TLV should be included in the PCEP message for controlling traffic steering when the LSP is down/invalid.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeInvalidationTLV"])
        )

    @property
    def IncludeLsp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether LSP will be included in a PCInitiate message. All other attributes in sub-tab-LSP would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeLsp"]))

    @property
    def IncludeLspa(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether LSPA will be included in a PCInitiate message. All other attributes in sub-tab-LSPA would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeLspa"]))

    @property
    def IncludeMetric(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether the PCInitiate message will have the metric list that is configured. All subsequent attributes of the sub-tab-Metric would be editable only if this is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeMetric"]))

    @property
    def IncludePpag(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Association will be included in a Sync PCReport message. All other attributes in sub-tab-PPAG would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludePpag"]))

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
    def IncludeSymbolicPathNameTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if Symbolic-Path-Name TLV is to be included in PCInitiate message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeSymbolicPathNameTlv"])
        )

    @property
    def IncludeTEPathBindingTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if TE-PATH-BINDING TLV is to be included in PCC Sync LSP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeTEPathBindingTLV"])
        )

    @property
    def InitialDelegation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Initial Delegation
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InitialDelegation"])
        )

    @property
    def InsertIpv6ExplicitNull(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Insert IPv6 Explicit Null MPLS header if the traffic type is of type IPv6
        """
        return self._get_attribute(self._SDM_ATT_MAP["InsertIpv6ExplicitNull"])

    @InsertIpv6ExplicitNull.setter
    def InsertIpv6ExplicitNull(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InsertIpv6ExplicitNull"], value)

    @property
    def InvalidationReserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved Field for Invalidation TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InvalidationReserved"])
        )

    @property
    def LocalProtection(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When set, this means that the path must include links protected with Fast Reroute
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalProtection"])
        )

    @property
    def LspDelegationState(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[delegated | delegationConfirmed | delegationRejected | delegationReturned | delegationRevoked | nonDelegated | none]): LSP Delegation State
        """
        return self._get_attribute(self._SDM_ATT_MAP["LspDelegationState"])

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
    def NumberOfMetricSubObject(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Value that indicates the number of Metric Objects to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfMetricSubObject"])

    @NumberOfMetricSubObject.setter
    def NumberOfMetricSubObject(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfMetricSubObject"], value)

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
    def OperStateDFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): It encodes the current state of the LSP, i.e., whether it is actively dropping traffic right now.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OperStateDFlag"])
        )

    @property
    def OverridePlspId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates if PLSP-ID will be set by the state machine or user. If disabled user wont have the control and state machine will set it.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverridePlspId"])

    @OverridePlspId.setter
    def OverridePlspId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverridePlspId"], value)

    @property
    def PathSetupType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(sR | sRv6): Indicates the type of LSP that will be sent in the PcReport for Pre-Established LSPs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathSetupType"])

    @PathSetupType.setter
    def PathSetupType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathSetupType"], value)

    @property
    def PlspId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): An identifier for the LSP. A PCC creates a unique PLSP-ID for each LSP that is constant for the lifetime of a PCEP session. The PCC will advertise the same PLSP-ID on all PCEP sessions it maintains at a given time.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PlspId"]))

    @property
    def ProtectionLspBit(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Protection LSP Bit is On.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtectionLspBit"])
        )

    @property
    def ReDelegationTimerStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[expired | none | notStarted | running | stopped]): Re-Delegation Timer Status
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReDelegationTimerStatus"])

    @property
    def RedelegationTimeoutInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The period of time a PCC waits for, when a PCEP session is terminated, before revoking LSP delegation to a PCE and attempting to redelegate LSPs associated with the terminated PCEP session to PCE.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RedelegationTimeoutInterval"])
        )

    @property
    def SetupPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The priority of the LSP with respect to taking resources.The value 0 is the highest priority.The Setup Priority is used in deciding whether this session can preempt another session.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SetupPriority"]))

    @property
    def SrcEndPointIpv4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source IPv4 address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcEndPointIpv4"])
        )

    @property
    def SrcEndPointIpv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source IPv6 address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcEndPointIpv6"])
        )

    @property
    def SrcIpv4(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source end point of the LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrcIpv4"]))

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
    def StandbyLspBit(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Standby LSP Bit is On.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StandbyLspBit"]))

    @property
    def SymbolicPathName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Each LSP (path) must have a symbolic name that is unique in the PCC. It must remain constant throughout a path's lifetime, which may span across multiple consecutive PCEP sessions and/or PCC restarts.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SymbolicPathName"])
        )

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

    def update(
        self,
        InsertIpv6ExplicitNull=None,
        Name=None,
        NumberOfAssociationObjects=None,
        NumberOfEroSubObjects=None,
        NumberOfMetricSubObject=None,
        NumberOfTEPathBindingTLV=None,
        OverridePlspId=None,
        PathSetupType=None,
    ):
        # type: (bool, str, int, int, int, int, bool, str) -> PreEstablishedSrLsps
        """Updates preEstablishedSrLsps resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - InsertIpv6ExplicitNull (bool): Insert IPv6 Explicit Null MPLS header if the traffic type is of type IPv6
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAssociationObjects (number): Value that indicates the number of Association Objects to be configured.
        - NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObject (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfTEPathBindingTLV (number): Value that indicates the number of TE-PATH-BINDING TLV to be configured.
        - OverridePlspId (bool): Indicates if PLSP-ID will be set by the state machine or user. If disabled user wont have the control and state machine will set it.
        - PathSetupType (str(sR | sRv6)): Indicates the type of LSP that will be sent in the PcReport for Pre-Established LSPs.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        InsertIpv6ExplicitNull=None,
        LspDelegationState=None,
        Name=None,
        NumberOfAssociationObjects=None,
        NumberOfEroSubObjects=None,
        NumberOfMetricSubObject=None,
        NumberOfTEPathBindingTLV=None,
        OverridePlspId=None,
        PathSetupType=None,
        ReDelegationTimerStatus=None,
    ):
        # type: (int, str, bool, List[str], str, int, int, int, int, bool, str, List[str]) -> PreEstablishedSrLsps
        """Finds and retrieves preEstablishedSrLsps resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve preEstablishedSrLsps resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all preEstablishedSrLsps resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - InsertIpv6ExplicitNull (bool): Insert IPv6 Explicit Null MPLS header if the traffic type is of type IPv6
        - LspDelegationState (list(str[delegated | delegationConfirmed | delegationRejected | delegationReturned | delegationRevoked | nonDelegated | none])): LSP Delegation State
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAssociationObjects (number): Value that indicates the number of Association Objects to be configured.
        - NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObject (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfTEPathBindingTLV (number): Value that indicates the number of TE-PATH-BINDING TLV to be configured.
        - OverridePlspId (bool): Indicates if PLSP-ID will be set by the state machine or user. If disabled user wont have the control and state machine will set it.
        - PathSetupType (str(sR | sRv6)): Indicates the type of LSP that will be sent in the PcReport for Pre-Established LSPs.
        - ReDelegationTimerStatus (list(str[expired | none | notStarted | running | stopped])): Re-Delegation Timer Status

        Returns
        -------
        - self: This instance with matching preEstablishedSrLsps resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of preEstablishedSrLsps data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the preEstablishedSrLsps resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (bool):
        - Arg3 (bool):
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

    def Delegate(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the delegate operation on the server.

        Delegate

        delegate(Arg2=list, async_operation=bool)list
        ---------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute("delegate", payload=payload, response_object=None)

    def PerformActionOnAllObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the performActionOnAllObjects operation on the server.

        Action on All Objects

        performActionOnAllObjects(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------------
        - Arg2 (str): Action Name
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

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
            "performActionOnAllObjects", payload=payload, response_object=None
        )

    def RevokeDelegation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the revokeDelegation operation on the server.

        Revoke Delegation

        revokeDelegation(Arg2=list, async_operation=bool)list
        -----------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute("revokeDelegation", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        ActiveDataTrafficEndpoint=None,
        AssociationId=None,
        Bandwidth=None,
        BindingType=None,
        Bos=None,
        ComputationPriority=None,
        ComputationPriorityReserved=None,
        ConfigStateDFlag=None,
        DestEndPointIpv4=None,
        DestinationIpv4Address=None,
        DestinationIpv6Address=None,
        ENLP=None,
        ENLPReserved=None,
        ExcludeAny=None,
        HoldingPriority=None,
        IncludeAll=None,
        IncludeAny=None,
        IncludeAssociation=None,
        IncludeBandwidth=None,
        IncludeComputationPriorityTLV=None,
        IncludeConfiguredERO=None,
        IncludeENLPTLV=None,
        IncludeEro=None,
        IncludeInvalidationTLV=None,
        IncludeLsp=None,
        IncludeLspa=None,
        IncludeMetric=None,
        IncludePpag=None,
        IncludeSrp=None,
        IncludeSymbolicPathNameTlv=None,
        IncludeTEPathBindingTLV=None,
        InitialDelegation=None,
        InvalidationReserved=None,
        LocalProtection=None,
        MplsLabel=None,
        OperStateDFlag=None,
        PlspId=None,
        ProtectionLspBit=None,
        RedelegationTimeoutInterval=None,
        SetupPriority=None,
        SrcEndPointIpv4=None,
        SrcEndPointIpv6=None,
        SrcIpv4=None,
        Srv6SID=None,
        StandbyLspBit=None,
        SymbolicPathName=None,
        Tc=None,
        Ttl=None,
    ):
        """Base class infrastructure that gets a list of preEstablishedSrLsps device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ActiveDataTrafficEndpoint (str): optional regex of activeDataTrafficEndpoint
        - AssociationId (str): optional regex of associationId
        - Bandwidth (str): optional regex of bandwidth
        - BindingType (str): optional regex of bindingType
        - Bos (str): optional regex of bos
        - ComputationPriority (str): optional regex of computationPriority
        - ComputationPriorityReserved (str): optional regex of computationPriorityReserved
        - ConfigStateDFlag (str): optional regex of configStateDFlag
        - DestEndPointIpv4 (str): optional regex of destEndPointIpv4
        - DestinationIpv4Address (str): optional regex of destinationIpv4Address
        - DestinationIpv6Address (str): optional regex of destinationIpv6Address
        - ENLP (str): optional regex of eNLP
        - ENLPReserved (str): optional regex of eNLPReserved
        - ExcludeAny (str): optional regex of excludeAny
        - HoldingPriority (str): optional regex of holdingPriority
        - IncludeAll (str): optional regex of includeAll
        - IncludeAny (str): optional regex of includeAny
        - IncludeAssociation (str): optional regex of includeAssociation
        - IncludeBandwidth (str): optional regex of includeBandwidth
        - IncludeComputationPriorityTLV (str): optional regex of includeComputationPriorityTLV
        - IncludeConfiguredERO (str): optional regex of includeConfiguredERO
        - IncludeENLPTLV (str): optional regex of includeENLPTLV
        - IncludeEro (str): optional regex of includeEro
        - IncludeInvalidationTLV (str): optional regex of includeInvalidationTLV
        - IncludeLsp (str): optional regex of includeLsp
        - IncludeLspa (str): optional regex of includeLspa
        - IncludeMetric (str): optional regex of includeMetric
        - IncludePpag (str): optional regex of includePpag
        - IncludeSrp (str): optional regex of includeSrp
        - IncludeSymbolicPathNameTlv (str): optional regex of includeSymbolicPathNameTlv
        - IncludeTEPathBindingTLV (str): optional regex of includeTEPathBindingTLV
        - InitialDelegation (str): optional regex of initialDelegation
        - InvalidationReserved (str): optional regex of invalidationReserved
        - LocalProtection (str): optional regex of localProtection
        - MplsLabel (str): optional regex of mplsLabel
        - OperStateDFlag (str): optional regex of operStateDFlag
        - PlspId (str): optional regex of plspId
        - ProtectionLspBit (str): optional regex of protectionLspBit
        - RedelegationTimeoutInterval (str): optional regex of redelegationTimeoutInterval
        - SetupPriority (str): optional regex of setupPriority
        - SrcEndPointIpv4 (str): optional regex of srcEndPointIpv4
        - SrcEndPointIpv6 (str): optional regex of srcEndPointIpv6
        - SrcIpv4 (str): optional regex of srcIpv4
        - Srv6SID (str): optional regex of srv6SID
        - StandbyLspBit (str): optional regex of standbyLspBit
        - SymbolicPathName (str): optional regex of symbolicPathName
        - Tc (str): optional regex of tc
        - Ttl (str): optional regex of ttl

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
