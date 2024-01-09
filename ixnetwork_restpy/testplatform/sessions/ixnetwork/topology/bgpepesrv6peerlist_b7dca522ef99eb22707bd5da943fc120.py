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


class BgpEpeSrv6PeerList(Base):
    """EPE SRv6 Peers
    The BgpEpeSrv6PeerList class encapsulates a required bgpEpeSrv6PeerList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "bgpEpeSrv6PeerList"
    _SDM_ATT_MAP = {
        "Active": "active",
        "ArgumentLengthSRv6": "argumentLengthSRv6",
        "BBitSRv6": "bBitSRv6",
        "BgpLocalRouterId": "bgpLocalRouterId",
        "BgpRemoteRouterId": "bgpRemoteRouterId",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnableSRv6EndpointBehaviorSubTlv": "enableSRv6EndpointBehaviorSubTlv",
        "EnableSRv6PeerNodeSid": "enableSRv6PeerNodeSid",
        "EnableSRv6PeerNodeSidTlv": "enableSRv6PeerNodeSidTlv",
        "EnableSRv6SIDStructureTLV": "enableSRv6SIDStructureTLV",
        "EndPointFunctionSRv6": "endPointFunctionSRv6",
        "EndpointBehaviorAlgorithmSRv6": "endpointBehaviorAlgorithmSRv6",
        "EndpointBehaviorFlagsSRv6": "endpointBehaviorFlagsSRv6",
        "FunctionLengthSRv6": "functionLengthSRv6",
        "LocalAsn": "localAsn",
        "LocatorBlockLengthSRv6": "locatorBlockLengthSRv6",
        "LocatorNodeLengthSRv6": "locatorNodeLengthSRv6",
        "Name": "name",
        "NoOflinks": "noOflinks",
        "PBitSRv6": "pBitSRv6",
        "PeerName": "peerName",
        "RemoteAsn": "remoteAsn",
        "Reserved": "reserved",
        "RsvdBitsSRv6": "rsvdBitsSRv6",
        "SBitSRv6": "sBitSRv6",
        "Srv6EPESID": "srv6EPESID",
        "UseLocalConfedId": "useLocalConfedId",
        "UseRemoteConfedId": "useRemoteConfedId",
        "Weight": "weight",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BgpEpeSrv6PeerList, self).__init__(parent, list_op)

    @property
    def BgpEpePeerLinkList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeerlinklist_763f9e1a55aa38eb16e9aa15af5fbd00.BgpEpePeerLinkList): An instance of the BgpEpePeerLinkList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeerlinklist_763f9e1a55aa38eb16e9aa15af5fbd00 import (
            BgpEpePeerLinkList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpEpePeerLinkList", None) is not None:
                return self._properties.get("BgpEpePeerLinkList")
        return BgpEpePeerLinkList(self)._select()

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
    def ArgumentLengthSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Argument length in bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ArgumentLengthSRv6"])
        )

    @property
    def BBitSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B-Flag: Backup Flag. If set, the SID is eligible for protection.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BBitSRv6"]))

    @property
    def BgpLocalRouterId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BGP Router ID for Local Node Descriptor
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BgpLocalRouterId"])
        )

    @property
    def BgpRemoteRouterId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BGP Router ID for Remote Node Descriptor
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BgpRemoteRouterId"])
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
    def EnableSRv6EndpointBehaviorSubTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables SRv6 Endpoint Behavior Sub TLV in BGP-LS.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EnableSRv6EndpointBehaviorSubTlv"]),
        )

    @property
    def EnableSRv6PeerNodeSid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables SRv6 SID Information TLV in Link State IPv6 SID NLRI.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableSRv6PeerNodeSid"])
        )

    @property
    def EnableSRv6PeerNodeSidTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables SRv6 Peer-Node SID TLV inside BGP-LS Attribute.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableSRv6PeerNodeSidTlv"])
        )

    @property
    def EnableSRv6SIDStructureTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables SRv6 SID Structure TLV in BGP-LS.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableSRv6SIDStructureTLV"])
        )

    @property
    def EndPointFunctionSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Choose any End-Point Function from the list, or enter any value. More details: https:/www.iana.org/assignments/segment-routing/segment-routing.xhtml
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndPointFunctionSRv6"])
        )

    @property
    def EndpointBehaviorAlgorithmSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 0: SPF, 1: Strict SPF, 2-127: Reserved, 128-255: Flexible Algorithms More Info: https:/www.iana.org/assignments/igp-parameters/igp-parameters.xhtml
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EndpointBehaviorAlgorithmSRv6"]),
        )

    @property
    def EndpointBehaviorFlagsSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Endpoint Behavior Flags value in Hex (1 Octet).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointBehaviorFlagsSRv6"])
        )

    @property
    def FunctionLengthSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Function length in bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FunctionLengthSRv6"])
        )

    @property
    def LocalAsn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS# of Egress node
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LocalAsn"]))

    @property
    def LocatorBlockLengthSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Block length in bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocatorBlockLengthSRv6"])
        )

    @property
    def LocatorNodeLengthSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Node length in bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocatorNodeLengthSRv6"])
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
    def NoOflinks(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Links
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOflinks"])

    @NoOflinks.setter
    def NoOflinks(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOflinks"], value)

    @property
    def PBitSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): P-Flag: Persistent Flag: When set, the P-Flag indicates that the SID is persistently allocated.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PBitSRv6"]))

    @property
    def PeerName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peer Name For Reference
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PeerName"]))

    @property
    def RemoteAsn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS# of Peer Node
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RemoteAsn"]))

    @property
    def Reserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 2 Byte Reserved field of Peer Node SID TLV. The value MUST be set to 0 and ignored on receipt.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved"]))

    @property
    def RsvdBitsSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved for future use and MUST be zero when originated and ignored when received.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RsvdBitsSRv6"]))

    @property
    def SBitSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S-Flag: Set Flag. When set, the S-Flag indicates that the SID refers to a set of BGP peering sessions.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SBitSRv6"]))

    @property
    def Srv6EPESID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Information, part of mandatory TLV of SRv6 SID NLRI. Acts as Node SID or Peer-Set SID depending upon S-Flag of Peer Node SID TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6EPESID"]))

    @property
    def UseLocalConfedId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Local Confederation identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseLocalConfedId"])
        )

    @property
    def UseRemoteConfedId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Remote Confederation identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseRemoteConfedId"])
        )

    @property
    def Weight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Weight of SID for Load Balancing.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Weight"]))

    def update(self, Name=None, NoOflinks=None):
        # type: (str, int) -> BgpEpeSrv6PeerList
        """Updates bgpEpeSrv6PeerList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOflinks (number): Number of Links

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, NoOflinks=None):
        # type: (int, str, str, int) -> BgpEpeSrv6PeerList
        """Finds and retrieves bgpEpeSrv6PeerList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpEpeSrv6PeerList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpEpeSrv6PeerList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOflinks (number): Number of Links

        Returns
        -------
        - self: This instance with matching bgpEpeSrv6PeerList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpEpeSrv6PeerList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpEpeSrv6PeerList resources from the server available through an iterator or index

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
        ArgumentLengthSRv6=None,
        BBitSRv6=None,
        BgpLocalRouterId=None,
        BgpRemoteRouterId=None,
        EnableSRv6EndpointBehaviorSubTlv=None,
        EnableSRv6PeerNodeSid=None,
        EnableSRv6PeerNodeSidTlv=None,
        EnableSRv6SIDStructureTLV=None,
        EndPointFunctionSRv6=None,
        EndpointBehaviorAlgorithmSRv6=None,
        EndpointBehaviorFlagsSRv6=None,
        FunctionLengthSRv6=None,
        LocalAsn=None,
        LocatorBlockLengthSRv6=None,
        LocatorNodeLengthSRv6=None,
        PBitSRv6=None,
        PeerName=None,
        RemoteAsn=None,
        Reserved=None,
        RsvdBitsSRv6=None,
        SBitSRv6=None,
        Srv6EPESID=None,
        UseLocalConfedId=None,
        UseRemoteConfedId=None,
        Weight=None,
    ):
        """Base class infrastructure that gets a list of bgpEpeSrv6PeerList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ArgumentLengthSRv6 (str): optional regex of argumentLengthSRv6
        - BBitSRv6 (str): optional regex of bBitSRv6
        - BgpLocalRouterId (str): optional regex of bgpLocalRouterId
        - BgpRemoteRouterId (str): optional regex of bgpRemoteRouterId
        - EnableSRv6EndpointBehaviorSubTlv (str): optional regex of enableSRv6EndpointBehaviorSubTlv
        - EnableSRv6PeerNodeSid (str): optional regex of enableSRv6PeerNodeSid
        - EnableSRv6PeerNodeSidTlv (str): optional regex of enableSRv6PeerNodeSidTlv
        - EnableSRv6SIDStructureTLV (str): optional regex of enableSRv6SIDStructureTLV
        - EndPointFunctionSRv6 (str): optional regex of endPointFunctionSRv6
        - EndpointBehaviorAlgorithmSRv6 (str): optional regex of endpointBehaviorAlgorithmSRv6
        - EndpointBehaviorFlagsSRv6 (str): optional regex of endpointBehaviorFlagsSRv6
        - FunctionLengthSRv6 (str): optional regex of functionLengthSRv6
        - LocalAsn (str): optional regex of localAsn
        - LocatorBlockLengthSRv6 (str): optional regex of locatorBlockLengthSRv6
        - LocatorNodeLengthSRv6 (str): optional regex of locatorNodeLengthSRv6
        - PBitSRv6 (str): optional regex of pBitSRv6
        - PeerName (str): optional regex of peerName
        - RemoteAsn (str): optional regex of remoteAsn
        - Reserved (str): optional regex of reserved
        - RsvdBitsSRv6 (str): optional regex of rsvdBitsSRv6
        - SBitSRv6 (str): optional regex of sBitSRv6
        - Srv6EPESID (str): optional regex of srv6EPESID
        - UseLocalConfedId (str): optional regex of useLocalConfedId
        - UseRemoteConfedId (str): optional regex of useRemoteConfedId
        - Weight (str): optional regex of weight

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
