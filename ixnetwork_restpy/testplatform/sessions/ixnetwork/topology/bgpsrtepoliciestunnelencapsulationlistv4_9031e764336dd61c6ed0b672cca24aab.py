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


class BgpSRTEPoliciesTunnelEncapsulationListV4(Base):
    """
    The BgpSRTEPoliciesTunnelEncapsulationListV4 class encapsulates a required bgpSRTEPoliciesTunnelEncapsulationListV4 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "bgpSRTEPoliciesTunnelEncapsulationListV4"
    _SDM_ATT_MAP = {
        "ENLPValue": "ENLPValue",
        "IPv6SID": "IPv6SID",
        "SID4Octet": "SID4Octet",
        "Active": "active",
        "AddressFamily": "addressFamily",
        "As4Number": "as4Number",
        "BindingSIDType": "bindingSIDType",
        "ColorCOBits": "colorCOBits",
        "ColorReservedBits": "colorReservedBits",
        "ColorValue": "colorValue",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnBindingTLV": "enBindingTLV",
        "EnColorTLV": "enColorTLV",
        "EnENLPTLV": "enENLPTLV",
        "EnPolicyNameTLV": "enPolicyNameTLV",
        "EnPolicyPathNameTLV": "enPolicyPathNameTLV",
        "EnPolicyPrioritySubTLV": "enPolicyPrioritySubTLV",
        "EnPrefTLV": "enPrefTLV",
        "EnRemoteEndPointTLV": "enRemoteEndPointTLV",
        "Iflag": "iflag",
        "Name": "name",
        "NumberOfActiveSegmentList": "numberOfActiveSegmentList",
        "NumberOfSegmentListV4": "numberOfSegmentListV4",
        "PolicyName": "policyName",
        "PolicyPathName": "policyPathName",
        "PrefValue": "prefValue",
        "Priority": "priority",
        "RemainingBits": "remainingBits",
        "RemoteEndpointIPv4": "remoteEndpointIPv4",
        "RemoteEndpointIPv6": "remoteEndpointIPv6",
        "Sflag": "sflag",
        "SrtepolicyName": "srtepolicyName",
        "TunnelType": "tunnelType",
        "UseAsMPLSLabel": "useAsMPLSLabel",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BgpSRTEPoliciesTunnelEncapsulationListV4, self).__init__(parent, list_op)

    @property
    def BgpSRTEPoliciesSegmentListV4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepoliciessegmentlistv4_6336750dadf06a61a8083b94d2a11d76.BgpSRTEPoliciesSegmentListV4): An instance of the BgpSRTEPoliciesSegmentListV4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepoliciessegmentlistv4_6336750dadf06a61a8083b94d2a11d76 import (
            BgpSRTEPoliciesSegmentListV4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpSRTEPoliciesSegmentListV4", None) is not None:
                return self._properties.get("BgpSRTEPoliciesSegmentListV4")
        return BgpSRTEPoliciesSegmentListV4(self)._select()

    @property
    def ENLPValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Explicit NULL Label Policy Value
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ENLPValue"]))

    @property
    def IPv6SID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IPv6SID"]))

    @property
    def SID4Octet(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 4 Octet SID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SID4Octet"]))

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AddressFamily(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Address Family
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AddressFamily"]))

    @property
    def As4Number(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS Number (4 Octects)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["As4Number"]))

    @property
    def BindingSIDType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Binding SID Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingSIDType"])
        )

    @property
    def ColorCOBits(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Color CO Bits
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ColorCOBits"]))

    @property
    def ColorReservedBits(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Color Reserved Bits
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ColorReservedBits"])
        )

    @property
    def ColorValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Color Value
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ColorValue"]))

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
    def EnBindingTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Binding Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnBindingTLV"]))

    @property
    def EnColorTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Color Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnColorTLV"]))

    @property
    def EnENLPTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Explicit NULL Label Policy Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnENLPTLV"]))

    @property
    def EnPolicyNameTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Policy Name Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnPolicyNameTLV"])
        )

    @property
    def EnPolicyPathNameTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable policy candidate path name for sub-TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnPolicyPathNameTLV"])
        )

    @property
    def EnPolicyPrioritySubTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Policy Priority Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnPolicyPrioritySubTLV"])
        )

    @property
    def EnPrefTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Preference Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnPrefTLV"]))

    @property
    def EnRemoteEndPointTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Remote Endpoint Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnRemoteEndPointTLV"])
        )

    @property
    def Iflag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This flag encodes the Drop Upon Invalid behavior.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Iflag"]))

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
    def NumberOfActiveSegmentList(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue):
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NumberOfActiveSegmentList"])
        )

    @property
    def NumberOfSegmentListV4(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Count of Segment Lists Per Tunnel
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfSegmentListV4"])

    @NumberOfSegmentListV4.setter
    def NumberOfSegmentListV4(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfSegmentListV4"], value)

    @property
    def PolicyName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Policy Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PolicyName"]))

    @property
    def PolicyPathName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Policy candidate path name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PolicyPathName"])
        )

    @property
    def PrefValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Preference
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrefValue"]))

    @property
    def Priority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Priority"]))

    @property
    def RemainingBits(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remaining Flag Bits takes the 8-bit flags value in Hex format. It ignores the bit position for flags exposed separately in GUI. For example, the 1st and 2nd bits are ignored since they are set using the S Flag and I Flag settings.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RemainingBits"]))

    @property
    def RemoteEndpointIPv4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteEndpointIPv4"])
        )

    @property
    def RemoteEndpointIPv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteEndpointIPv6"])
        )

    @property
    def Sflag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This flag encodes the Specified-BSID-only behavior.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Sflag"]))

    @property
    def SrtepolicyName(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Policy Name For Reference
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrtepolicyName"])

    @property
    def TunnelType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tunnel Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TunnelType"]))

    @property
    def UseAsMPLSLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): when Enanbled the BSID (SID 4 Octet) value will be treated as 3-Octet MPLS Label part of the BSID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseAsMPLSLabel"])
        )

    def update(self, Name=None, NumberOfSegmentListV4=None):
        # type: (str, int) -> BgpSRTEPoliciesTunnelEncapsulationListV4
        """Updates bgpSRTEPoliciesTunnelEncapsulationListV4 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfSegmentListV4 (number): Count of Segment Lists Per Tunnel

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
        NumberOfSegmentListV4=None,
        SrtepolicyName=None,
    ):
        # type: (int, str, str, int, List[str]) -> BgpSRTEPoliciesTunnelEncapsulationListV4
        """Finds and retrieves bgpSRTEPoliciesTunnelEncapsulationListV4 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpSRTEPoliciesTunnelEncapsulationListV4 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpSRTEPoliciesTunnelEncapsulationListV4 resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfSegmentListV4 (number): Count of Segment Lists Per Tunnel
        - SrtepolicyName (list(str)): Policy Name For Reference

        Returns
        -------
        - self: This instance with matching bgpSRTEPoliciesTunnelEncapsulationListV4 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpSRTEPoliciesTunnelEncapsulationListV4 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpSRTEPoliciesTunnelEncapsulationListV4 resources from the server available through an iterator or index

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

    def get_device_ids(
        self,
        PortNames=None,
        ENLPValue=None,
        IPv6SID=None,
        SID4Octet=None,
        Active=None,
        AddressFamily=None,
        As4Number=None,
        BindingSIDType=None,
        ColorCOBits=None,
        ColorReservedBits=None,
        ColorValue=None,
        EnBindingTLV=None,
        EnColorTLV=None,
        EnENLPTLV=None,
        EnPolicyNameTLV=None,
        EnPolicyPathNameTLV=None,
        EnPolicyPrioritySubTLV=None,
        EnPrefTLV=None,
        EnRemoteEndPointTLV=None,
        Iflag=None,
        NumberOfActiveSegmentList=None,
        PolicyName=None,
        PolicyPathName=None,
        PrefValue=None,
        Priority=None,
        RemainingBits=None,
        RemoteEndpointIPv4=None,
        RemoteEndpointIPv6=None,
        Sflag=None,
        TunnelType=None,
        UseAsMPLSLabel=None,
    ):
        """Base class infrastructure that gets a list of bgpSRTEPoliciesTunnelEncapsulationListV4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ENLPValue (str): optional regex of ENLPValue
        - IPv6SID (str): optional regex of IPv6SID
        - SID4Octet (str): optional regex of SID4Octet
        - Active (str): optional regex of active
        - AddressFamily (str): optional regex of addressFamily
        - As4Number (str): optional regex of as4Number
        - BindingSIDType (str): optional regex of bindingSIDType
        - ColorCOBits (str): optional regex of colorCOBits
        - ColorReservedBits (str): optional regex of colorReservedBits
        - ColorValue (str): optional regex of colorValue
        - EnBindingTLV (str): optional regex of enBindingTLV
        - EnColorTLV (str): optional regex of enColorTLV
        - EnENLPTLV (str): optional regex of enENLPTLV
        - EnPolicyNameTLV (str): optional regex of enPolicyNameTLV
        - EnPolicyPathNameTLV (str): optional regex of enPolicyPathNameTLV
        - EnPolicyPrioritySubTLV (str): optional regex of enPolicyPrioritySubTLV
        - EnPrefTLV (str): optional regex of enPrefTLV
        - EnRemoteEndPointTLV (str): optional regex of enRemoteEndPointTLV
        - Iflag (str): optional regex of iflag
        - NumberOfActiveSegmentList (str): optional regex of numberOfActiveSegmentList
        - PolicyName (str): optional regex of policyName
        - PolicyPathName (str): optional regex of policyPathName
        - PrefValue (str): optional regex of prefValue
        - Priority (str): optional regex of priority
        - RemainingBits (str): optional regex of remainingBits
        - RemoteEndpointIPv4 (str): optional regex of remoteEndpointIPv4
        - RemoteEndpointIPv6 (str): optional regex of remoteEndpointIPv6
        - Sflag (str): optional regex of sflag
        - TunnelType (str): optional regex of tunnelType
        - UseAsMPLSLabel (str): optional regex of useAsMPLSLabel

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
