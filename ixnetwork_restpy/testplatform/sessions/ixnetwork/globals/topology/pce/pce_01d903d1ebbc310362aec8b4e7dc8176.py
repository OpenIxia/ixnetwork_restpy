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


class Pce(Base):
    """PCE Port Specific Data
    The Pce class encapsulates a required pce resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "pce"
    _SDM_ATT_MAP = {
        "BindingSIDDraftVersion": "bindingSIDDraftVersion",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "ErrorValueAttemptedSRv6WithoutCapabilityAdvertise": "errorValueAttemptedSRv6WithoutCapabilityAdvertise",
        "ErrorValueInvalidSRv6SIDStructure": "errorValueInvalidSRv6SIDStructure",
        "ErrorValueMissingSRv6PCECapSubTlv": "errorValueMissingSRv6PCECapSubTlv",
        "ErrorValueRROContainsSRv6WithOtherSubobjects": "errorValueRROContainsSRv6WithOtherSubobjects",
        "ErrorValueSIDAndNAIAbsentInSRv6RROSubobject": "errorValueSIDAndNAIAbsentInSRv6RROSubobject",
        "Name": "name",
        "PathSetupTypeForSRv6": "pathSetupTypeForSRv6",
        "RowNames": "rowNames",
        "Srv6EROSubobjectType": "srv6EROSubobjectType",
        "Srv6PceCapabilitySubTLVType": "srv6PceCapabilitySubTLVType",
        "Srv6RROSubobjectType": "srv6RROSubobjectType",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Pce, self).__init__(parent, list_op)

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0 import (
            StartRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StartRate", None) is not None:
                return self._properties.get("StartRate")
        return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04 import (
            StopRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StopRate", None) is not None:
                return self._properties.get("StopRate")
        return StopRate(self)._select()

    @property
    def BindingSIDDraftVersion(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Depending on this field backward compatibility will be given. All draft versions before IETF draft will follow existing implementation. New IETF draft will be using new implementation and TLV structure.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingSIDDraftVersion"])
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
    def ErrorValueAttemptedSRv6WithoutCapabilityAdvertise(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Denotes the SRv6 Attempt w/o Capability Advertisement error value when PCEP Peer tries to send SRv6 ERO without SRv6 capability advertisement.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErrorValueAttemptedSRv6WithoutCapabilityAdvertise"]
        )

    @ErrorValueAttemptedSRv6WithoutCapabilityAdvertise.setter
    def ErrorValueAttemptedSRv6WithoutCapabilityAdvertise(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErrorValueAttemptedSRv6WithoutCapabilityAdvertise"],
            value,
        )

    @property
    def ErrorValueInvalidSRv6SIDStructure(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This error value is sent when the sum of all four sizes advertised in the SID structure is larger than 128 bits.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErrorValueInvalidSRv6SIDStructure"]
        )

    @ErrorValueInvalidSRv6SIDStructure.setter
    def ErrorValueInvalidSRv6SIDStructure(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErrorValueInvalidSRv6SIDStructure"], value
        )

    @property
    def ErrorValueMissingSRv6PCECapSubTlv(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Denotes the Missing SRv6-PCE-CAPABILITY Sub-TLV error value when the SRv6-PCE-CAPABILITY sub-TLV is missing from the PATH-SETUP-TYPE-CAPABILITY TLV in the OPEN object.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErrorValueMissingSRv6PCECapSubTlv"]
        )

    @ErrorValueMissingSRv6PCECapSubTlv.setter
    def ErrorValueMissingSRv6PCECapSubTlv(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErrorValueMissingSRv6PCECapSubTlv"], value
        )

    @property
    def ErrorValueRROContainsSRv6WithOtherSubobjects(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This error value is sent when a PCE detects that the subobjects of an RRO are a combination of SRv6-RRO and other types of subobjects.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErrorValueRROContainsSRv6WithOtherSubobjects"]
        )

    @ErrorValueRROContainsSRv6WithOtherSubobjects.setter
    def ErrorValueRROContainsSRv6WithOtherSubobjects(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErrorValueRROContainsSRv6WithOtherSubobjects"], value
        )

    @property
    def ErrorValueSIDAndNAIAbsentInSRv6RROSubobject(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This error value is sent when a PCEP speaker receives an SRv6-RRO subobject where both SRv6 SID and NAI are absent.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ErrorValueSIDAndNAIAbsentInSRv6RROSubobject"]
        )

    @ErrorValueSIDAndNAIAbsentInSRv6RROSubobject.setter
    def ErrorValueSIDAndNAIAbsentInSRv6RROSubobject(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ErrorValueSIDAndNAIAbsentInSRv6RROSubobject"], value
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
    def PathSetupTypeForSRv6(self):
        # type: () -> int
        """
        Returns
        -------
        - number: SRv6 Path Setup Type specifies PCE's capability of interpreting this type of Path.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathSetupTypeForSRv6"])

    @PathSetupTypeForSRv6.setter
    def PathSetupTypeForSRv6(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathSetupTypeForSRv6"], value)

    @property
    def RowNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP["RowNames"])

    @property
    def Srv6EROSubobjectType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Code Point For SRv6 ERO Subobject Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Srv6EROSubobjectType"])

    @Srv6EROSubobjectType.setter
    def Srv6EROSubobjectType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Srv6EROSubobjectType"], value)

    @property
    def Srv6PceCapabilitySubTLVType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: SRv6 PCE Capability Sub-TLV Type specifies PCE's capability of interpreting this type of sub-TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Srv6PceCapabilitySubTLVType"])

    @Srv6PceCapabilitySubTLVType.setter
    def Srv6PceCapabilitySubTLVType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Srv6PceCapabilitySubTLVType"], value)

    @property
    def Srv6RROSubobjectType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Code Point For SRv6 RRO Subobject Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Srv6RROSubobjectType"])

    @Srv6RROSubobjectType.setter
    def Srv6RROSubobjectType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Srv6RROSubobjectType"], value)

    def update(
        self,
        ErrorValueAttemptedSRv6WithoutCapabilityAdvertise=None,
        ErrorValueInvalidSRv6SIDStructure=None,
        ErrorValueMissingSRv6PCECapSubTlv=None,
        ErrorValueRROContainsSRv6WithOtherSubobjects=None,
        ErrorValueSIDAndNAIAbsentInSRv6RROSubobject=None,
        Name=None,
        PathSetupTypeForSRv6=None,
        Srv6EROSubobjectType=None,
        Srv6PceCapabilitySubTLVType=None,
        Srv6RROSubobjectType=None,
    ):
        # type: (int, int, int, int, int, str, int, int, int, int) -> Pce
        """Updates pce resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ErrorValueAttemptedSRv6WithoutCapabilityAdvertise (number): Denotes the SRv6 Attempt w/o Capability Advertisement error value when PCEP Peer tries to send SRv6 ERO without SRv6 capability advertisement.
        - ErrorValueInvalidSRv6SIDStructure (number): This error value is sent when the sum of all four sizes advertised in the SID structure is larger than 128 bits.
        - ErrorValueMissingSRv6PCECapSubTlv (number): Denotes the Missing SRv6-PCE-CAPABILITY Sub-TLV error value when the SRv6-PCE-CAPABILITY sub-TLV is missing from the PATH-SETUP-TYPE-CAPABILITY TLV in the OPEN object.
        - ErrorValueRROContainsSRv6WithOtherSubobjects (number): This error value is sent when a PCE detects that the subobjects of an RRO are a combination of SRv6-RRO and other types of subobjects.
        - ErrorValueSIDAndNAIAbsentInSRv6RROSubobject (number): This error value is sent when a PCEP speaker receives an SRv6-RRO subobject where both SRv6 SID and NAI are absent.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PathSetupTypeForSRv6 (number): SRv6 Path Setup Type specifies PCE's capability of interpreting this type of Path.
        - Srv6EROSubobjectType (number): Code Point For SRv6 ERO Subobject Type.
        - Srv6PceCapabilitySubTLVType (number): SRv6 PCE Capability Sub-TLV Type specifies PCE's capability of interpreting this type of sub-TLV.
        - Srv6RROSubobjectType (number): Code Point For SRv6 RRO Subobject Type.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        ErrorValueAttemptedSRv6WithoutCapabilityAdvertise=None,
        ErrorValueInvalidSRv6SIDStructure=None,
        ErrorValueMissingSRv6PCECapSubTlv=None,
        ErrorValueRROContainsSRv6WithOtherSubobjects=None,
        ErrorValueSIDAndNAIAbsentInSRv6RROSubobject=None,
        Name=None,
        PathSetupTypeForSRv6=None,
        RowNames=None,
        Srv6EROSubobjectType=None,
        Srv6PceCapabilitySubTLVType=None,
        Srv6RROSubobjectType=None,
    ):
        # type: (int, str, int, int, int, int, int, str, int, List[str], int, int, int) -> Pce
        """Finds and retrieves pce resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pce resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pce resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - ErrorValueAttemptedSRv6WithoutCapabilityAdvertise (number): Denotes the SRv6 Attempt w/o Capability Advertisement error value when PCEP Peer tries to send SRv6 ERO without SRv6 capability advertisement.
        - ErrorValueInvalidSRv6SIDStructure (number): This error value is sent when the sum of all four sizes advertised in the SID structure is larger than 128 bits.
        - ErrorValueMissingSRv6PCECapSubTlv (number): Denotes the Missing SRv6-PCE-CAPABILITY Sub-TLV error value when the SRv6-PCE-CAPABILITY sub-TLV is missing from the PATH-SETUP-TYPE-CAPABILITY TLV in the OPEN object.
        - ErrorValueRROContainsSRv6WithOtherSubobjects (number): This error value is sent when a PCE detects that the subobjects of an RRO are a combination of SRv6-RRO and other types of subobjects.
        - ErrorValueSIDAndNAIAbsentInSRv6RROSubobject (number): This error value is sent when a PCEP speaker receives an SRv6-RRO subobject where both SRv6 SID and NAI are absent.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PathSetupTypeForSRv6 (number): SRv6 Path Setup Type specifies PCE's capability of interpreting this type of Path.
        - RowNames (list(str)): Name of rows
        - Srv6EROSubobjectType (number): Code Point For SRv6 ERO Subobject Type.
        - Srv6PceCapabilitySubTLVType (number): SRv6 PCE Capability Sub-TLV Type specifies PCE's capability of interpreting this type of sub-TLV.
        - Srv6RROSubobjectType (number): Code Point For SRv6 RRO Subobject Type.

        Returns
        -------
        - self: This instance with matching pce resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pce data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pce resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, BindingSIDDraftVersion=None):
        """Base class infrastructure that gets a list of pce device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BindingSIDDraftVersion (str): optional regex of bindingSIDDraftVersion

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
