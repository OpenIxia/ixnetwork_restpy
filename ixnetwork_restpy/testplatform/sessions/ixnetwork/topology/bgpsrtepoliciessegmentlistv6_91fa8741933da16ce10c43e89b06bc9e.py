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


class BgpSRTEPoliciesSegmentListV6(Base):
    """
    The BgpSRTEPoliciesSegmentListV6 class encapsulates a required bgpSRTEPoliciesSegmentListV6 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "bgpSRTEPoliciesSegmentListV6"
    _SDM_ATT_MAP = {
        "Active": "active",
        "Aflag": "aflag",
        "ArgLength": "argLength",
        "Bflag": "bflag",
        "Count": "count",
        "CustomEndPointBehaviour": "customEndPointBehaviour",
        "DescriptiveName": "descriptiveName",
        "EnBindingSID": "enBindingSID",
        "EnReverseBindingTLV": "enReverseBindingTLV",
        "EnWeight": "enWeight",
        "EndPointBehaviour": "endPointBehaviour",
        "FunLength": "funLength",
        "Ipv6SID": "ipv6SID",
        "LbLength": "lbLength",
        "LnLength": "lnLength",
        "MplsSID": "mplsSID",
        "Name": "name",
        "NumberOfActiveSegments": "numberOfActiveSegments",
        "NumberOfSegmentsV6": "numberOfSegmentsV6",
        "RemainingBits": "remainingBits",
        "ReverseArgLength": "reverseArgLength",
        "ReverseCustomEndPoint": "reverseCustomEndPoint",
        "ReverseEndPointBehaviour": "reverseEndPointBehaviour",
        "ReverseFunLength": "reverseFunLength",
        "ReverseIpv6SID": "reverseIpv6SID",
        "ReverseLbLength": "reverseLbLength",
        "ReverseLnLength": "reverseLnLength",
        "ReverseMPLSSID": "reverseMPLSSID",
        "SegmentListNumber": "segmentListNumber",
        "SrtepolicyName": "srtepolicyName",
        "Srv6ReverseSidEndpointBehaviourFlagReserved": "srv6ReverseSidEndpointBehaviourFlagReserved",
        "Srv6SidEndpointBehaviourFlagReserved": "srv6SidEndpointBehaviourFlagReserved",
        "UseAsMPLSLabel": "useAsMPLSLabel",
        "UseAsReverseMPLSLabel": "useAsReverseMPLSLabel",
        "Weight": "weight",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BgpSRTEPoliciesSegmentListV6, self).__init__(parent, list_op)

    @property
    def BgpSRTEPoliciesSegmentsCollectionV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepoliciessegmentscollectionv6_36fca517ef159515fd45af1719a56398.BgpSRTEPoliciesSegmentsCollectionV6): An instance of the BgpSRTEPoliciesSegmentsCollectionV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepoliciessegmentscollectionv6_36fca517ef159515fd45af1719a56398 import (
            BgpSRTEPoliciesSegmentsCollectionV6,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("BgpSRTEPoliciesSegmentsCollectionV6", None)
                is not None
            ):
                return self._properties.get("BgpSRTEPoliciesSegmentsCollectionV6")
        return BgpSRTEPoliciesSegmentsCollectionV6(self)._select()

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
    def Aflag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This flag encodes the SID type(MPLS or SRv6).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Aflag"]))

    @property
    def ArgLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Argument Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ArgLength"]))

    @property
    def Bflag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This flag encodes whether to carry SRv6 Endpoint behavior and SID structure or not.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Bflag"]))

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
    def CustomEndPointBehaviour(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Custom End-Point Behaviour, applicable when Endpoint behaviour is 256-Custom End Point.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CustomEndPointBehaviour"])
        )

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
    def EnBindingSID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Binding SID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnBindingSID"]))

    @property
    def EnReverseBindingTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): checkbox to enable Reverse Binding SID TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnReverseBindingTLV"])
        )

    @property
    def EnWeight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Weight Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnWeight"]))

    @property
    def EndPointBehaviour(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the behavior that can be associated with a SID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndPointBehaviour"])
        )

    @property
    def FunLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Function Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FunLength"]))

    @property
    def Ipv6SID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 SID, a 16 octet value to send out with Binding TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv6SID"]))

    @property
    def LbLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Block Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LbLength"]))

    @property
    def LnLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Node Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LnLength"]))

    @property
    def MplsSID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MPLS SID, a 32 bit value to sent out with Binding TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MplsSID"]))

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
    def NumberOfActiveSegments(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Count of Active Segments configured.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NumberOfActiveSegments"])
        )

    @property
    def NumberOfSegmentsV6(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Count of Segments Per Segment List.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfSegmentsV6"])

    @NumberOfSegmentsV6.setter
    def NumberOfSegmentsV6(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfSegmentsV6"], value)

    @property
    def RemainingBits(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remaining Flag Bits takes the 8-bit flags value in Hex format. It ignores the bit position for flags exposed separately in GUI. For example, the 1st and 2nd bits and 3rd bits are ignored since they are set using the A Flag and B Flag settings.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RemainingBits"]))

    @property
    def ReverseArgLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reverse Argument Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReverseArgLength"])
        )

    @property
    def ReverseCustomEndPoint(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Custom End-Point Behaviour, enabled when Endpoint behaviour is 256-Custom End Point.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReverseCustomEndPoint"])
        )

    @property
    def ReverseEndPointBehaviour(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the behavior that can be associated with a SID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReverseEndPointBehaviour"])
        )

    @property
    def ReverseFunLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reverse Function Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReverseFunLength"])
        )

    @property
    def ReverseIpv6SID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reverse IPv6 SID, a 16 octet value to sent out with Binding TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReverseIpv6SID"])
        )

    @property
    def ReverseLbLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reverse Locator Block Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReverseLbLength"])
        )

    @property
    def ReverseLnLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Reverse Locator Node Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReverseLnLength"])
        )

    @property
    def ReverseMPLSSID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reverse MPLS SID, a 32 bit value to sent out with Binding TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReverseMPLSSID"])
        )

    @property
    def SegmentListNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Segment List Number For Reference.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListNumber"])
        )

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
    def Srv6ReverseSidEndpointBehaviourFlagReserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 16 bits Reserved for SRv6 Sid Endpoint Behaviour and Structure Flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Srv6ReverseSidEndpointBehaviourFlagReserved"]
            ),
        )

    @property
    def Srv6SidEndpointBehaviourFlagReserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 16 bits Reserved for SRv6 Sid Endpoint Behaviour and Structure Flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Srv6SidEndpointBehaviourFlagReserved"]
            ),
        )

    @property
    def UseAsMPLSLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): when Enanbled the BSID (MPLS SID) value will be treated as 3-Octet MPLS Label part of the BSID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseAsMPLSLabel"])
        )

    @property
    def UseAsReverseMPLSLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): when Enanbled the BSID (Reverse MPLS SID) value will be treated as 3-Octet MPLS Label part of the BSID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseAsReverseMPLSLabel"])
        )

    @property
    def Weight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Weight Value
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Weight"]))

    def update(self, Name=None, NumberOfSegmentsV6=None):
        # type: (str, int) -> BgpSRTEPoliciesSegmentListV6
        """Updates bgpSRTEPoliciesSegmentListV6 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfSegmentsV6 (number): Count of Segments Per Segment List.

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
        NumberOfSegmentsV6=None,
        SrtepolicyName=None,
    ):
        # type: (int, str, str, int, List[str]) -> BgpSRTEPoliciesSegmentListV6
        """Finds and retrieves bgpSRTEPoliciesSegmentListV6 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpSRTEPoliciesSegmentListV6 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpSRTEPoliciesSegmentListV6 resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfSegmentsV6 (number): Count of Segments Per Segment List.
        - SrtepolicyName (list(str)): Policy Name For Reference

        Returns
        -------
        - self: This instance with matching bgpSRTEPoliciesSegmentListV6 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpSRTEPoliciesSegmentListV6 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpSRTEPoliciesSegmentListV6 resources from the server available through an iterator or index

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
        Active=None,
        Aflag=None,
        ArgLength=None,
        Bflag=None,
        CustomEndPointBehaviour=None,
        EnBindingSID=None,
        EnReverseBindingTLV=None,
        EnWeight=None,
        EndPointBehaviour=None,
        FunLength=None,
        Ipv6SID=None,
        LbLength=None,
        LnLength=None,
        MplsSID=None,
        NumberOfActiveSegments=None,
        RemainingBits=None,
        ReverseArgLength=None,
        ReverseCustomEndPoint=None,
        ReverseEndPointBehaviour=None,
        ReverseFunLength=None,
        ReverseIpv6SID=None,
        ReverseLbLength=None,
        ReverseLnLength=None,
        ReverseMPLSSID=None,
        SegmentListNumber=None,
        Srv6ReverseSidEndpointBehaviourFlagReserved=None,
        Srv6SidEndpointBehaviourFlagReserved=None,
        UseAsMPLSLabel=None,
        UseAsReverseMPLSLabel=None,
        Weight=None,
    ):
        """Base class infrastructure that gets a list of bgpSRTEPoliciesSegmentListV6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - Aflag (str): optional regex of aflag
        - ArgLength (str): optional regex of argLength
        - Bflag (str): optional regex of bflag
        - CustomEndPointBehaviour (str): optional regex of customEndPointBehaviour
        - EnBindingSID (str): optional regex of enBindingSID
        - EnReverseBindingTLV (str): optional regex of enReverseBindingTLV
        - EnWeight (str): optional regex of enWeight
        - EndPointBehaviour (str): optional regex of endPointBehaviour
        - FunLength (str): optional regex of funLength
        - Ipv6SID (str): optional regex of ipv6SID
        - LbLength (str): optional regex of lbLength
        - LnLength (str): optional regex of lnLength
        - MplsSID (str): optional regex of mplsSID
        - NumberOfActiveSegments (str): optional regex of numberOfActiveSegments
        - RemainingBits (str): optional regex of remainingBits
        - ReverseArgLength (str): optional regex of reverseArgLength
        - ReverseCustomEndPoint (str): optional regex of reverseCustomEndPoint
        - ReverseEndPointBehaviour (str): optional regex of reverseEndPointBehaviour
        - ReverseFunLength (str): optional regex of reverseFunLength
        - ReverseIpv6SID (str): optional regex of reverseIpv6SID
        - ReverseLbLength (str): optional regex of reverseLbLength
        - ReverseLnLength (str): optional regex of reverseLnLength
        - ReverseMPLSSID (str): optional regex of reverseMPLSSID
        - SegmentListNumber (str): optional regex of segmentListNumber
        - Srv6ReverseSidEndpointBehaviourFlagReserved (str): optional regex of srv6ReverseSidEndpointBehaviourFlagReserved
        - Srv6SidEndpointBehaviourFlagReserved (str): optional regex of srv6SidEndpointBehaviourFlagReserved
        - UseAsMPLSLabel (str): optional regex of useAsMPLSLabel
        - UseAsReverseMPLSLabel (str): optional regex of useAsReverseMPLSLabel
        - Weight (str): optional regex of weight

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
