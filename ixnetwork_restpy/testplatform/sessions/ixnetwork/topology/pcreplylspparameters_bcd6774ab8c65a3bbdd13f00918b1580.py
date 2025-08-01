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


class PcReplyLspParameters(Base):
    """PCReply LSP Parameters
    The PcReplyLspParameters class encapsulates a required pcReplyLspParameters resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "pcReplyLspParameters"
    _SDM_ATT_MAP = {
        "Active": "active",
        "Bandwidth": "bandwidth",
        "BiDirectional": "biDirectional",
        "BindingType": "bindingType",
        "Bos": "bos",
        "ComputationPriority": "computationPriority",
        "ComputationPriorityReserved": "computationPriorityReserved",
        "ConfigStateDFlag": "configStateDFlag",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "ENLP": "eNLP",
        "ENLPReserved": "eNLPReserved",
        "EnableCFlag": "enableCFlag",
        "EnableEro": "enableEro",
        "EnableLoose": "enableLoose",
        "EnableXro": "enableXro",
        "ExcludeAny": "excludeAny",
        "FailBit": "failBit",
        "HoldingPriority": "holdingPriority",
        "IncludeAll": "includeAll",
        "IncludeAny": "includeAny",
        "IncludeBandwidth": "includeBandwidth",
        "IncludeComputationPriorityTLV": "includeComputationPriorityTLV",
        "IncludeConfiguredERO": "includeConfiguredERO",
        "IncludeENLPTLV": "includeENLPTLV",
        "IncludeInvalidationTLV": "includeInvalidationTLV",
        "IncludeLsp": "includeLsp",
        "IncludeLspa": "includeLspa",
        "IncludeMetric": "includeMetric",
        "IncludeRp": "includeRp",
        "IncludeSymbolicPathNameTlv": "includeSymbolicPathNameTlv",
        "IncludeTEPathBindingTLV": "includeTEPathBindingTLV",
        "InvalidationReserved": "invalidationReserved",
        "LocalProtection": "localProtection",
        "LspAdminFlag": "lspAdminFlag",
        "MplsLabel": "mplsLabel",
        "Name": "name",
        "NatureOfIssue": "natureOfIssue",
        "NumberOfEroSubObjects": "numberOfEroSubObjects",
        "NumberOfMetricSubObject": "numberOfMetricSubObject",
        "NumberOfTEPathBindingTLV": "numberOfTEPathBindingTLV",
        "NumberOfXroSubObjects": "numberOfXroSubObjects",
        "OperStateDFlag": "operStateDFlag",
        "PlspId": "plspId",
        "PriorityValue": "priorityValue",
        "ProcessType": "processType",
        "ReceivedPLSPID": "receivedPLSPID",
        "ReceivedSymbolicPath": "receivedSymbolicPath",
        "ReflectLSP": "reflectLSP",
        "ReflectRP": "reflectRP",
        "ReflectedObjectNoPath": "reflectedObjectNoPath",
        "RequestId": "requestId",
        "ResponseOptions": "responseOptions",
        "ResponsePathType": "responsePathType",
        "SendEmptyTLV": "sendEmptyTLV",
        "SessionInfo": "sessionInfo",
        "SetupPriority": "setupPriority",
        "Srv6SID": "srv6SID",
        "SymbolicPathName": "symbolicPathName",
        "Tc": "tc",
        "Ttl": "ttl",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PcReplyLspParameters, self).__init__(parent, list_op)

    @property
    def PceXroSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcexrosubobjectslist_497bc286ebfb51b8813947a23cd5817a.PceXroSubObjectsList): An instance of the PceXroSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcexrosubobjectslist_497bc286ebfb51b8813947a23cd5817a import (
            PceXroSubObjectsList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PceXroSubObjectsList", None) is not None:
                return self._properties.get("PceXroSubObjectsList")
        return PceXroSubObjectsList(self)

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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceptepathbindingtlvlist_f4c1df238c92bb045645b2a65159e09e.PcepTEPATHBINDINGTLVList): An instance of the PcepTEPATHBINDINGTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceptepathbindingtlvlist_f4c1df238c92bb045645b2a65159e09e import (
            PcepTEPATHBINDINGTLVList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PcepTEPATHBINDINGTLVList", None) is not None:
                return self._properties.get("PcepTEPATHBINDINGTLVList")
        return PcepTEPATHBINDINGTLVList(self)

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
    def BiDirectional(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bi-directional
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BiDirectional"]))

    @property
    def BindingType(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the type of binding included in the TLV. Types are as follows: 20bit MPLS Label 32bit MPLS Label. SRv6 SID Default value is 20bit MPLS Label.
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
    def EnableCFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): C Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableCFlag"]))

    @property
    def EnableEro(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include ERO
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableEro"]))

    @property
    def EnableLoose(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Loose
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableLoose"]))

    @property
    def EnableXro(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include XRO
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableXro"]))

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
    def FailBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Fail Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FailBit"]))

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
    def IncludeBandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Bandwidth
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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeLsp"]))

    @property
    def IncludeLspa(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include LSPA
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeLspa"]))

    @property
    def IncludeMetric(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeMetric"]))

    @property
    def IncludeRp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include RP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IncludeRp"]))

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if TE-PATH-BINDING TLV is to be included in PCInitiate message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeTEPathBindingTLV"])
        )

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Protection
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalProtection"])
        )

    @property
    def LspAdminFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if A Flag in LSP object is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LspAdminFlag"]))

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
    def NatureOfIssue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Nature Of Issue
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NatureOfIssue"]))

    @property
    def NumberOfEroSubObjects(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of ERO Sub Objects
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
        - number: Number of Metric
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
    def NumberOfXroSubObjects(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of XRO Sub Objects
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfXroSubObjects"])

    @NumberOfXroSubObjects.setter
    def NumberOfXroSubObjects(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfXroSubObjects"], value)

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
    def PriorityValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PriorityValue"]))

    @property
    def ProcessType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates how the XRO is responded in the Path Request Response.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProcessType"]))

    @property
    def ReceivedPLSPID(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Received PLSP-ID in PcRequest
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceivedPLSPID"])

    @property
    def ReceivedSymbolicPath(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Received Symbolic Path Name in PcRequest
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceivedSymbolicPath"])

    @property
    def ReflectLSP(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reflect LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ReflectLSP"]))

    @property
    def ReflectRP(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reflect RP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ReflectRP"]))

    @property
    def ReflectedObjectNoPath(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reflected Object
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReflectedObjectNoPath"])
        )

    @property
    def RequestId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Request ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RequestId"]))

    @property
    def ResponseOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reply Options
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ResponseOptions"])
        )

    @property
    def ResponsePathType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates which type of LSP will be responsed in the Path Request Response.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ResponsePathType"])
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
    def SessionInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[delegatedActive | delegatedDown | delegatedGoingUp | delegatedUp | noLSPObjectInPCRequest | none | notDelegatedActive | notDelegatedDown | notDelegatedGoingUp | notDelegatedUp | pcErrorReceived | removedByPCC | replySent | replySentReportNotReceived]): Logs additional information about the LSP state
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionInfo"])

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
        Name=None,
        NumberOfEroSubObjects=None,
        NumberOfMetricSubObject=None,
        NumberOfTEPathBindingTLV=None,
        NumberOfXroSubObjects=None,
    ):
        # type: (str, int, int, int, int) -> PcReplyLspParameters
        """Updates pcReplyLspParameters resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfEroSubObjects (number): Number of ERO Sub Objects
        - NumberOfMetricSubObject (number): Number of Metric
        - NumberOfTEPathBindingTLV (number): Value that indicates the number of TE-PATH-BINDING TLV to be configured.
        - NumberOfXroSubObjects (number): Number of XRO Sub Objects

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        Name=None,
        NumberOfEroSubObjects=None,
        NumberOfMetricSubObject=None,
        NumberOfTEPathBindingTLV=None,
        NumberOfXroSubObjects=None,
        ReceivedPLSPID=None,
        ReceivedSymbolicPath=None,
        SessionInfo=None,
    ):
        # type: (int, str, str, int, int, int, int, List[int], List[str], List[str]) -> PcReplyLspParameters
        """Finds and retrieves pcReplyLspParameters resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pcReplyLspParameters resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pcReplyLspParameters resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfEroSubObjects (number): Number of ERO Sub Objects
        - NumberOfMetricSubObject (number): Number of Metric
        - NumberOfTEPathBindingTLV (number): Value that indicates the number of TE-PATH-BINDING TLV to be configured.
        - NumberOfXroSubObjects (number): Number of XRO Sub Objects
        - ReceivedPLSPID (list(number)): Received PLSP-ID in PcRequest
        - ReceivedSymbolicPath (list(str)): Received Symbolic Path Name in PcRequest
        - SessionInfo (list(str[delegatedActive | delegatedDown | delegatedGoingUp | delegatedUp | noLSPObjectInPCRequest | none | notDelegatedActive | notDelegatedDown | notDelegatedGoingUp | notDelegatedUp | pcErrorReceived | removedByPCC | replySent | replySentReportNotReceived])): Logs additional information about the LSP state

        Returns
        -------
        - self: This instance with matching pcReplyLspParameters resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pcReplyLspParameters data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pcReplyLspParameters resources from the server available through an iterator or index

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

    def ReturnDelegation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the returnDelegation operation on the server.

        Return Delegation of PCE-Replied LSPs

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        returnDelegation(async_operation=bool)
        --------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        returnDelegation(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        returnDelegation(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        returnDelegation(Arg2=list, async_operation=bool)list
        -----------------------------------------------------
        - Arg2 (list(number)): Return Delegation.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("returnDelegation", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        Bandwidth=None,
        BiDirectional=None,
        BindingType=None,
        Bos=None,
        ComputationPriority=None,
        ComputationPriorityReserved=None,
        ConfigStateDFlag=None,
        ENLP=None,
        ENLPReserved=None,
        EnableCFlag=None,
        EnableEro=None,
        EnableLoose=None,
        EnableXro=None,
        ExcludeAny=None,
        FailBit=None,
        HoldingPriority=None,
        IncludeAll=None,
        IncludeAny=None,
        IncludeBandwidth=None,
        IncludeComputationPriorityTLV=None,
        IncludeConfiguredERO=None,
        IncludeENLPTLV=None,
        IncludeInvalidationTLV=None,
        IncludeLsp=None,
        IncludeLspa=None,
        IncludeMetric=None,
        IncludeRp=None,
        IncludeSymbolicPathNameTlv=None,
        IncludeTEPathBindingTLV=None,
        InvalidationReserved=None,
        LocalProtection=None,
        LspAdminFlag=None,
        MplsLabel=None,
        NatureOfIssue=None,
        OperStateDFlag=None,
        PlspId=None,
        PriorityValue=None,
        ProcessType=None,
        ReflectLSP=None,
        ReflectRP=None,
        ReflectedObjectNoPath=None,
        RequestId=None,
        ResponseOptions=None,
        ResponsePathType=None,
        SendEmptyTLV=None,
        SetupPriority=None,
        Srv6SID=None,
        SymbolicPathName=None,
        Tc=None,
        Ttl=None,
    ):
        """Base class infrastructure that gets a list of pcReplyLspParameters device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - Bandwidth (str): optional regex of bandwidth
        - BiDirectional (str): optional regex of biDirectional
        - BindingType (str): optional regex of bindingType
        - Bos (str): optional regex of bos
        - ComputationPriority (str): optional regex of computationPriority
        - ComputationPriorityReserved (str): optional regex of computationPriorityReserved
        - ConfigStateDFlag (str): optional regex of configStateDFlag
        - ENLP (str): optional regex of eNLP
        - ENLPReserved (str): optional regex of eNLPReserved
        - EnableCFlag (str): optional regex of enableCFlag
        - EnableEro (str): optional regex of enableEro
        - EnableLoose (str): optional regex of enableLoose
        - EnableXro (str): optional regex of enableXro
        - ExcludeAny (str): optional regex of excludeAny
        - FailBit (str): optional regex of failBit
        - HoldingPriority (str): optional regex of holdingPriority
        - IncludeAll (str): optional regex of includeAll
        - IncludeAny (str): optional regex of includeAny
        - IncludeBandwidth (str): optional regex of includeBandwidth
        - IncludeComputationPriorityTLV (str): optional regex of includeComputationPriorityTLV
        - IncludeConfiguredERO (str): optional regex of includeConfiguredERO
        - IncludeENLPTLV (str): optional regex of includeENLPTLV
        - IncludeInvalidationTLV (str): optional regex of includeInvalidationTLV
        - IncludeLsp (str): optional regex of includeLsp
        - IncludeLspa (str): optional regex of includeLspa
        - IncludeMetric (str): optional regex of includeMetric
        - IncludeRp (str): optional regex of includeRp
        - IncludeSymbolicPathNameTlv (str): optional regex of includeSymbolicPathNameTlv
        - IncludeTEPathBindingTLV (str): optional regex of includeTEPathBindingTLV
        - InvalidationReserved (str): optional regex of invalidationReserved
        - LocalProtection (str): optional regex of localProtection
        - LspAdminFlag (str): optional regex of lspAdminFlag
        - MplsLabel (str): optional regex of mplsLabel
        - NatureOfIssue (str): optional regex of natureOfIssue
        - OperStateDFlag (str): optional regex of operStateDFlag
        - PlspId (str): optional regex of plspId
        - PriorityValue (str): optional regex of priorityValue
        - ProcessType (str): optional regex of processType
        - ReflectLSP (str): optional regex of reflectLSP
        - ReflectRP (str): optional regex of reflectRP
        - ReflectedObjectNoPath (str): optional regex of reflectedObjectNoPath
        - RequestId (str): optional regex of requestId
        - ResponseOptions (str): optional regex of responseOptions
        - ResponsePathType (str): optional regex of responsePathType
        - SendEmptyTLV (str): optional regex of sendEmptyTLV
        - SetupPriority (str): optional regex of setupPriority
        - Srv6SID (str): optional regex of srv6SID
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
