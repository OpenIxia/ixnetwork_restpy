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


class BgpSRTEPoliciesSegmentsCollectionV6(Base):
    """
    The BgpSRTEPoliciesSegmentsCollectionV6 class encapsulates a required bgpSRTEPoliciesSegmentsCollectionV6 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "bgpSRTEPoliciesSegmentsCollectionV6"
    _SDM_ATT_MAP = {
        "Active": "active",
        "Aflag": "aflag",
        "Algorithm": "algorithm",
        "ArgLength": "argLength",
        "BFlag": "bFlag",
        "BitReserved16": "bitReserved16",
        "BitReserved8": "bitReserved8",
        "BottomOfStack": "bottomOfStack",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnableGSRv6SIDEncoding": "enableGSRv6SIDEncoding",
        "EndPointBehaviour": "endPointBehaviour",
        "FunLength": "funLength",
        "GSIDBlockLength": "gSIDBlockLength",
        "GSIDEncodingFlag": "gSIDEncodingFlag",
        "GSIDLength": "gSIDLength",
        "InterfaceIndex": "interfaceIndex",
        "Ipv4LocalAddress": "ipv4LocalAddress",
        "Ipv4NodeAddress": "ipv4NodeAddress",
        "Ipv4RemoteAddress": "ipv4RemoteAddress",
        "Ipv6LocalAddress": "ipv6LocalAddress",
        "Ipv6NodeAddress": "ipv6NodeAddress",
        "Ipv6RemoteAddress": "ipv6RemoteAddress",
        "Ipv6SID": "ipv6SID",
        "Label": "label",
        "LbLength": "lbLength",
        "LnLength": "lnLength",
        "Name": "name",
        "OptionalBottomOfStack": "optionalBottomOfStack",
        "OptionalIpv6SID": "optionalIpv6SID",
        "OptionalLabel": "optionalLabel",
        "OptionalTLVType": "optionalTLVType",
        "OptionalTimeToLive": "optionalTimeToLive",
        "OptionalTrafficClass": "optionalTrafficClass",
        "RemainingBits": "remainingBits",
        "RemoteInterfaceIndex": "remoteInterfaceIndex",
        "SFlag": "sFlag",
        "SegmentCustomEndPointBehaviour": "segmentCustomEndPointBehaviour",
        "SegmentFlagReserved": "segmentFlagReserved",
        "SegmentListNumber": "segmentListNumber",
        "SegmentType": "segmentType",
        "SrtepolicyName": "srtepolicyName",
        "Srv6SidEndpointBehaviourFlagReserved": "srv6SidEndpointBehaviourFlagReserved",
        "TimeToLive": "timeToLive",
        "TrafficClass": "trafficClass",
        "Vflag": "vflag",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BgpSRTEPoliciesSegmentsCollectionV6, self).__init__(parent, list_op)

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): This flag indicates the presence of SR Algorithm id in the SR Algorithm field applicable to various Segment Types.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Aflag"]))

    @property
    def Algorithm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 1 octet specifying SR Algorithm.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Algorithm"]))

    @property
    def ArgLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Argument Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ArgLength"]))

    @property
    def BFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This flag, when set, indicates the presence of the SRv6 Endpoint Behavior and SID Structure encoding.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BFlag"]))

    @property
    def BitReserved16(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved portion of SID Encoding Sub TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BitReserved16"]))

    @property
    def BitReserved8(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved portion of SID Encoding Sub TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BitReserved8"]))

    @property
    def BottomOfStack(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bottom Of Stack
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BottomOfStack"]))

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
    def EnableGSRv6SIDEncoding(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This flag indicates the presence of Sid Encoding Sub tlv whereever applicable in segments
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableGSRv6SIDEncoding"])
        )

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Function Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FunLength"]))

    @property
    def GSIDBlockLength(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Block Length portion of SID Encoding Sub TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GSIDBlockLength"])
        )

    @property
    def GSIDEncodingFlag(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flag portion of SID Encoding Sub TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GSIDEncodingFlag"])
        )

    @property
    def GSIDLength(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): G-Sid Length portion of SID Encoding Sub TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["GSIDLength"]))

    @property
    def InterfaceIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Index of the interface used to identify the link.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterfaceIndex"])
        )

    @property
    def Ipv4LocalAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Local Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4LocalAddress"])
        )

    @property
    def Ipv4NodeAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Node Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4NodeAddress"])
        )

    @property
    def Ipv4RemoteAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Address of the remote Node.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4RemoteAddress"])
        )

    @property
    def Ipv6LocalAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Address of the Local Node.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6LocalAddress"])
        )

    @property
    def Ipv6NodeAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Address representing a node.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6NodeAddress"])
        )

    @property
    def Ipv6RemoteAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Address of the remote Node.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6RemoteAddress"])
        )

    @property
    def Ipv6SID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SID only, in the form of IPv6 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv6SID"]))

    @property
    def Label(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Label"]))

    @property
    def LbLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Locator Block Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LbLength"]))

    @property
    def LnLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Locator Node Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LnLength"]))

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
    def OptionalBottomOfStack(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bottom Of Stack
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionalBottomOfStack"])
        )

    @property
    def OptionalIpv6SID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SID which can be optional, in the form of IPv6 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionalIpv6SID"])
        )

    @property
    def OptionalLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OptionalLabel"]))

    @property
    def OptionalTLVType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Optional TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionalTLVType"])
        )

    @property
    def OptionalTimeToLive(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TTL
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionalTimeToLive"])
        )

    @property
    def OptionalTrafficClass(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Traffic Class
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionalTrafficClass"])
        )

    @property
    def RemainingBits(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remaining Flag Bits takes the 8-bit flags value in Hex format. It ignores the bit position for flags exposed separately in GUI. For example, the 1st and 2nd bits are ignored since they are set using the V Flag and A Flag settings.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RemainingBits"]))

    @property
    def RemoteInterfaceIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remote Interface Index
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoteInterfaceIndex"])
        )

    @property
    def SFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This flag encodes the Specified-BSID-only behavior.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SFlag"]))

    @property
    def SegmentCustomEndPointBehaviour(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Custom End-Point Behaviour, Applicable when Endpoint behaviour is 256-Custom End Point.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SegmentCustomEndPointBehaviour"]),
        )

    @property
    def SegmentFlagReserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved portion of Segment Flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentFlagReserved"])
        )

    @property
    def SegmentListNumber(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Segment List Number For Reference
        """
        return self._get_attribute(self._SDM_ATT_MAP["SegmentListNumber"])

    @property
    def SegmentType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Segment Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SegmentType"]))

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
    def TimeToLive(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TTL
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TimeToLive"]))

    @property
    def TrafficClass(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Traffic Class
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TrafficClass"]))

    @property
    def Vflag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This flag is used by SRPM for the purpose of SID verification.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Vflag"]))

    def update(self, Name=None):
        # type: (str) -> BgpSRTEPoliciesSegmentsCollectionV6
        """Updates bgpSRTEPoliciesSegmentsCollectionV6 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

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
        SegmentListNumber=None,
        SrtepolicyName=None,
    ):
        # type: (int, str, str, List[str], List[str]) -> BgpSRTEPoliciesSegmentsCollectionV6
        """Finds and retrieves bgpSRTEPoliciesSegmentsCollectionV6 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpSRTEPoliciesSegmentsCollectionV6 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpSRTEPoliciesSegmentsCollectionV6 resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SegmentListNumber (list(str)): Segment List Number For Reference
        - SrtepolicyName (list(str)): Policy Name For Reference

        Returns
        -------
        - self: This instance with matching bgpSRTEPoliciesSegmentsCollectionV6 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpSRTEPoliciesSegmentsCollectionV6 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpSRTEPoliciesSegmentsCollectionV6 resources from the server available through an iterator or index

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
        Algorithm=None,
        ArgLength=None,
        BFlag=None,
        BitReserved16=None,
        BitReserved8=None,
        BottomOfStack=None,
        EnableGSRv6SIDEncoding=None,
        EndPointBehaviour=None,
        FunLength=None,
        GSIDBlockLength=None,
        GSIDEncodingFlag=None,
        GSIDLength=None,
        InterfaceIndex=None,
        Ipv4LocalAddress=None,
        Ipv4NodeAddress=None,
        Ipv4RemoteAddress=None,
        Ipv6LocalAddress=None,
        Ipv6NodeAddress=None,
        Ipv6RemoteAddress=None,
        Ipv6SID=None,
        Label=None,
        LbLength=None,
        LnLength=None,
        OptionalBottomOfStack=None,
        OptionalIpv6SID=None,
        OptionalLabel=None,
        OptionalTLVType=None,
        OptionalTimeToLive=None,
        OptionalTrafficClass=None,
        RemainingBits=None,
        RemoteInterfaceIndex=None,
        SFlag=None,
        SegmentCustomEndPointBehaviour=None,
        SegmentFlagReserved=None,
        SegmentType=None,
        Srv6SidEndpointBehaviourFlagReserved=None,
        TimeToLive=None,
        TrafficClass=None,
        Vflag=None,
    ):
        """Base class infrastructure that gets a list of bgpSRTEPoliciesSegmentsCollectionV6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - Aflag (str): optional regex of aflag
        - Algorithm (str): optional regex of algorithm
        - ArgLength (str): optional regex of argLength
        - BFlag (str): optional regex of bFlag
        - BitReserved16 (str): optional regex of bitReserved16
        - BitReserved8 (str): optional regex of bitReserved8
        - BottomOfStack (str): optional regex of bottomOfStack
        - EnableGSRv6SIDEncoding (str): optional regex of enableGSRv6SIDEncoding
        - EndPointBehaviour (str): optional regex of endPointBehaviour
        - FunLength (str): optional regex of funLength
        - GSIDBlockLength (str): optional regex of gSIDBlockLength
        - GSIDEncodingFlag (str): optional regex of gSIDEncodingFlag
        - GSIDLength (str): optional regex of gSIDLength
        - InterfaceIndex (str): optional regex of interfaceIndex
        - Ipv4LocalAddress (str): optional regex of ipv4LocalAddress
        - Ipv4NodeAddress (str): optional regex of ipv4NodeAddress
        - Ipv4RemoteAddress (str): optional regex of ipv4RemoteAddress
        - Ipv6LocalAddress (str): optional regex of ipv6LocalAddress
        - Ipv6NodeAddress (str): optional regex of ipv6NodeAddress
        - Ipv6RemoteAddress (str): optional regex of ipv6RemoteAddress
        - Ipv6SID (str): optional regex of ipv6SID
        - Label (str): optional regex of label
        - LbLength (str): optional regex of lbLength
        - LnLength (str): optional regex of lnLength
        - OptionalBottomOfStack (str): optional regex of optionalBottomOfStack
        - OptionalIpv6SID (str): optional regex of optionalIpv6SID
        - OptionalLabel (str): optional regex of optionalLabel
        - OptionalTLVType (str): optional regex of optionalTLVType
        - OptionalTimeToLive (str): optional regex of optionalTimeToLive
        - OptionalTrafficClass (str): optional regex of optionalTrafficClass
        - RemainingBits (str): optional regex of remainingBits
        - RemoteInterfaceIndex (str): optional regex of remoteInterfaceIndex
        - SFlag (str): optional regex of sFlag
        - SegmentCustomEndPointBehaviour (str): optional regex of segmentCustomEndPointBehaviour
        - SegmentFlagReserved (str): optional regex of segmentFlagReserved
        - SegmentType (str): optional regex of segmentType
        - Srv6SidEndpointBehaviourFlagReserved (str): optional regex of srv6SidEndpointBehaviourFlagReserved
        - TimeToLive (str): optional regex of timeToLive
        - TrafficClass (str): optional regex of trafficClass
        - Vflag (str): optional regex of vflag

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
