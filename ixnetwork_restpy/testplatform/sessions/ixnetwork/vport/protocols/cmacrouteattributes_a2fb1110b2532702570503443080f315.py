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


class CmacRouteAttributes(Base):
    """Configures route attributes for C-MAC ranges. These attributes are carried in MAC routes.
    The CmacRouteAttributes class encapsulates a required cmacRouteAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "cmacRouteAttributes"
    _SDM_ATT_MAP = {
        "AggregatorAs": "aggregatorAs",
        "AggregatorId": "aggregatorId",
        "AsPath": "asPath",
        "AsSetMode": "asSetMode",
        "Cluster": "cluster",
        "Community": "community",
        "EnableAggregator": "enableAggregator",
        "EnableAsPath": "enableAsPath",
        "EnableAtomicAggregate": "enableAtomicAggregate",
        "EnableCluster": "enableCluster",
        "EnableCommunity": "enableCommunity",
        "EnableLocalPref": "enableLocalPref",
        "EnableMultiExit": "enableMultiExit",
        "EnableNextHop": "enableNextHop",
        "EnableOrigin": "enableOrigin",
        "EnableOriginator": "enableOriginator",
        "ExtendedCommunity": "extendedCommunity",
        "LocalPref": "localPref",
        "MultiExit": "multiExit",
        "NextHop": "nextHop",
        "NextHopIpType": "nextHopIpType",
        "NextHopMode": "nextHopMode",
        "Origin": "origin",
        "OriginatorId": "originatorId",
        "SetNextHop": "setNextHop",
    }
    _SDM_ENUM_MAP = {
        "asSetMode": [
            "includeAsSeq",
            "includeAsSeqConf",
            "includeAsSet",
            "includeAsSetConf",
            "noInclude",
            "prependAs",
        ],
        "nextHopIpType": ["ipv4", "ipv6"],
        "nextHopMode": ["fixed", "incrementPerPeer"],
        "origin": ["igp", "egp", "incomplete"],
        "setNextHop": ["manually", "sameAsLocalIp"],
    }

    def __init__(self, parent, list_op=False):
        super(CmacRouteAttributes, self).__init__(parent, list_op)

    @property
    def AggregatorAs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The AS associated with the aggregator router ID in the AGGREGATOR attribute. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregatorAs"])

    @AggregatorAs.setter
    def AggregatorAs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AggregatorAs"], value)

    @property
    def AggregatorId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address of the router that aggregated two or more routes in the AGGREGATOR attribute. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregatorId"])

    @AggregatorId.setter
    def AggregatorId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AggregatorId"], value)

    @property
    def AsPath(self):
        """
        Returns
        -------
        - list(dict(arg1:bool,arg2:str[unknown | asSet | asSequence | asConfedSet | asConfedSequence],arg3:list[number])): Indicates the local IP address of the BGP router
        """
        return self._get_attribute(self._SDM_ATT_MAP["AsPath"])

    @AsPath.setter
    def AsPath(self, value):
        self._set_attribute(self._SDM_ATT_MAP["AsPath"], value)

    @property
    def AsSetMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(includeAsSeq | includeAsSeqConf | includeAsSet | includeAsSetConf | noInclude | prependAs): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AsSetMode"])

    @AsSetMode.setter
    def AsSetMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AsSetMode"], value)

    @property
    def Cluster(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): The list of BGP clusters that a particular route has passed through
        """
        return self._get_attribute(self._SDM_ATT_MAP["Cluster"])

    @Cluster.setter
    def Cluster(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP["Cluster"], value)

    @property
    def Community(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): The BGP Community attribute to be added to the BGP entry
        """
        return self._get_attribute(self._SDM_ATT_MAP["Community"])

    @Community.setter
    def Community(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP["Community"], value)

    @property
    def EnableAggregator(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAggregator"])

    @EnableAggregator.setter
    def EnableAggregator(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAggregator"], value)

    @property
    def EnableAsPath(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates the local IP address of the BGP router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAsPath"])

    @EnableAsPath.setter
    def EnableAsPath(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAsPath"], value)

    @property
    def EnableAtomicAggregate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAtomicAggregate"])

    @EnableAtomicAggregate.setter
    def EnableAtomicAggregate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAtomicAggregate"], value)

    @property
    def EnableCluster(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCluster"])

    @EnableCluster.setter
    def EnableCluster(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCluster"], value)

    @property
    def EnableCommunity(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the generation of a COMMUNITY attribute list. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCommunity"])

    @EnableCommunity.setter
    def EnableCommunity(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCommunity"], value)

    @property
    def EnableLocalPref(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLocalPref"])

    @EnableLocalPref.setter
    def EnableLocalPref(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLocalPref"], value)

    @property
    def EnableMultiExit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMultiExit"])

    @EnableMultiExit.setter
    def EnableMultiExit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMultiExit"], value)

    @property
    def EnableNextHop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the generation of a NEXT HOP attribute. (default = true)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableNextHop"])

    @EnableNextHop.setter
    def EnableNextHop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableNextHop"], value)

    @property
    def EnableOrigin(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the generation of an ORIGIN attribute. (default = true)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOrigin"])

    @EnableOrigin.setter
    def EnableOrigin(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOrigin"], value)

    @property
    def EnableOriginator(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOriginator"])

    @EnableOriginator.setter
    def EnableOriginator(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOriginator"], value)

    @property
    def ExtendedCommunity(self):
        """
        Returns
        -------
        - list(dict(arg1:str[decimal | hex | ip | ieeeFloat],arg2:str[decimal | hex | ip | ieeeFloat],arg3:str[twoOctetAs | ip | fourOctetAs | opaque | administratorAsTwoOctetLinkBw],arg4:str[routeTarget | origin | extendedBandwidthSubType],arg5:str)): This object is used to construct an extended community attribute for a route item
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExtendedCommunity"])

    @ExtendedCommunity.setter
    def ExtendedCommunity(self, value):
        self._set_attribute(self._SDM_ATT_MAP["ExtendedCommunity"], value)

    @property
    def LocalPref(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalPref"])

    @LocalPref.setter
    def LocalPref(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LocalPref"], value)

    @property
    def MultiExit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["MultiExit"])

    @MultiExit.setter
    def MultiExit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MultiExit"], value)

    @property
    def NextHop(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextHop"])

    @NextHop.setter
    def NextHop(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextHop"], value)

    @property
    def NextHopIpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipv4 | ipv6): IP type of Next Hop. Default is IPv4.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextHopIpType"])

    @NextHopIpType.setter
    def NextHopIpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextHopIpType"], value)

    @property
    def NextHopMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fixed | incrementPerPeer): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextHopMode"])

    @NextHopMode.setter
    def NextHopMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NextHopMode"], value)

    @property
    def Origin(self):
        # type: () -> str
        """
        Returns
        -------
        - str(igp | egp | incomplete): An indication of where the route entry originated
        """
        return self._get_attribute(self._SDM_ATT_MAP["Origin"])

    @Origin.setter
    def Origin(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Origin"], value)

    @property
    def OriginatorId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["OriginatorId"])

    @OriginatorId.setter
    def OriginatorId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OriginatorId"], value)

    @property
    def SetNextHop(self):
        # type: () -> str
        """
        Returns
        -------
        - str(manually | sameAsLocalIp): Indicates now to set the next hop IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetNextHop"])

    @SetNextHop.setter
    def SetNextHop(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetNextHop"], value)

    def update(
        self,
        AggregatorAs=None,
        AggregatorId=None,
        AsPath=None,
        AsSetMode=None,
        Cluster=None,
        Community=None,
        EnableAggregator=None,
        EnableAsPath=None,
        EnableAtomicAggregate=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableLocalPref=None,
        EnableMultiExit=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginator=None,
        ExtendedCommunity=None,
        LocalPref=None,
        MultiExit=None,
        NextHop=None,
        NextHopIpType=None,
        NextHopMode=None,
        Origin=None,
        OriginatorId=None,
        SetNextHop=None,
    ):
        """Updates cmacRouteAttributes resource on the server.

        Args
        ----
        - AggregatorAs (number): The AS associated with the aggregator router ID in the AGGREGATOR attribute. (default = 0)
        - AggregatorId (str): The IP address of the router that aggregated two or more routes in the AGGREGATOR attribute. (default = 0.0.0.0)
        - AsPath (list(dict(arg1:bool,arg2:str[unknown | asSet | asSequence | asConfedSet | asConfedSequence],arg3:list[number]))): Indicates the local IP address of the BGP router
        - AsSetMode (str(includeAsSeq | includeAsSeqConf | includeAsSet | includeAsSetConf | noInclude | prependAs)): NOT DEFINED
        - Cluster (list(number)): The list of BGP clusters that a particular route has passed through
        - Community (list(number)): The BGP Community attribute to be added to the BGP entry
        - EnableAggregator (bool): Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        - EnableAsPath (bool): Indicates the local IP address of the BGP router.
        - EnableAtomicAggregate (bool): Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        - EnableCluster (bool): Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        - EnableCommunity (bool): Enables the generation of a COMMUNITY attribute list. (default = false)
        - EnableLocalPref (bool): Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        - EnableMultiExit (bool): Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        - EnableNextHop (bool): Enables the generation of a NEXT HOP attribute. (default = true)
        - EnableOrigin (bool): Enables the generation of an ORIGIN attribute. (default = true)
        - EnableOriginator (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        - ExtendedCommunity (list(dict(arg1:str[decimal | hex | ip | ieeeFloat],arg2:str[decimal | hex | ip | ieeeFloat],arg3:str[twoOctetAs | ip | fourOctetAs | opaque | administratorAsTwoOctetLinkBw],arg4:str[routeTarget | origin | extendedBandwidthSubType],arg5:str))): This object is used to construct an extended community attribute for a route item
        - LocalPref (number): The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        - MultiExit (number): The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        - NextHop (str): The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        - NextHopIpType (str(ipv4 | ipv6)): IP type of Next Hop. Default is IPv4.
        - NextHopMode (str(fixed | incrementPerPeer)): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses
        - Origin (str(igp | egp | incomplete)): An indication of where the route entry originated
        - OriginatorId (str): The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        - SetNextHop (str(manually | sameAsLocalIp)): Indicates now to set the next hop IP address.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AggregatorAs=None,
        AggregatorId=None,
        AsPath=None,
        AsSetMode=None,
        Cluster=None,
        Community=None,
        EnableAggregator=None,
        EnableAsPath=None,
        EnableAtomicAggregate=None,
        EnableCluster=None,
        EnableCommunity=None,
        EnableLocalPref=None,
        EnableMultiExit=None,
        EnableNextHop=None,
        EnableOrigin=None,
        EnableOriginator=None,
        ExtendedCommunity=None,
        LocalPref=None,
        MultiExit=None,
        NextHop=None,
        NextHopIpType=None,
        NextHopMode=None,
        Origin=None,
        OriginatorId=None,
        SetNextHop=None,
    ):
        """Finds and retrieves cmacRouteAttributes resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cmacRouteAttributes resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cmacRouteAttributes resources from the server.

        Args
        ----
        - AggregatorAs (number): The AS associated with the aggregator router ID in the AGGREGATOR attribute. (default = 0)
        - AggregatorId (str): The IP address of the router that aggregated two or more routes in the AGGREGATOR attribute. (default = 0.0.0.0)
        - AsPath (list(dict(arg1:bool,arg2:str[unknown | asSet | asSequence | asConfedSet | asConfedSequence],arg3:list[number]))): Indicates the local IP address of the BGP router
        - AsSetMode (str(includeAsSeq | includeAsSeqConf | includeAsSet | includeAsSetConf | noInclude | prependAs)): NOT DEFINED
        - Cluster (list(number)): The list of BGP clusters that a particular route has passed through
        - Community (list(number)): The BGP Community attribute to be added to the BGP entry
        - EnableAggregator (bool): Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        - EnableAsPath (bool): Indicates the local IP address of the BGP router.
        - EnableAtomicAggregate (bool): Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        - EnableCluster (bool): Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        - EnableCommunity (bool): Enables the generation of a COMMUNITY attribute list. (default = false)
        - EnableLocalPref (bool): Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        - EnableMultiExit (bool): Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        - EnableNextHop (bool): Enables the generation of a NEXT HOP attribute. (default = true)
        - EnableOrigin (bool): Enables the generation of an ORIGIN attribute. (default = true)
        - EnableOriginator (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        - ExtendedCommunity (list(dict(arg1:str[decimal | hex | ip | ieeeFloat],arg2:str[decimal | hex | ip | ieeeFloat],arg3:str[twoOctetAs | ip | fourOctetAs | opaque | administratorAsTwoOctetLinkBw],arg4:str[routeTarget | origin | extendedBandwidthSubType],arg5:str))): This object is used to construct an extended community attribute for a route item
        - LocalPref (number): The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        - MultiExit (number): The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        - NextHop (str): The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        - NextHopIpType (str(ipv4 | ipv6)): IP type of Next Hop. Default is IPv4.
        - NextHopMode (str(fixed | incrementPerPeer)): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses
        - Origin (str(igp | egp | incomplete)): An indication of where the route entry originated
        - OriginatorId (str): The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        - SetNextHop (str(manually | sameAsLocalIp)): Indicates now to set the next hop IP address.

        Returns
        -------
        - self: This instance with matching cmacRouteAttributes resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cmacRouteAttributes data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cmacRouteAttributes resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
