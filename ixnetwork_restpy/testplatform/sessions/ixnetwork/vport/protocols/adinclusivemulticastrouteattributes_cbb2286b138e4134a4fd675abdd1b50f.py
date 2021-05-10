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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AdInclusiveMulticastRouteAttributes(Base):
    """Configures route attributes for EVIs. These attributes are carried in AD route per EVI/domain, Multicast route.
    The AdInclusiveMulticastRouteAttributes class encapsulates a required adInclusiveMulticastRouteAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'adInclusiveMulticastRouteAttributes'
    _SDM_ATT_MAP = {
        'AggregatorAs': 'aggregatorAs',
        'AggregatorId': 'aggregatorId',
        'AsPath': 'asPath',
        'AsSetMode': 'asSetMode',
        'Cluster': 'cluster',
        'Community': 'community',
        'EnableAggregator': 'enableAggregator',
        'EnableAsPath': 'enableAsPath',
        'EnableAtomicAggregate': 'enableAtomicAggregate',
        'EnableCluster': 'enableCluster',
        'EnableCommunity': 'enableCommunity',
        'EnableLocalPref': 'enableLocalPref',
        'EnableMultiExit': 'enableMultiExit',
        'EnableNextHop': 'enableNextHop',
        'EnableOrigin': 'enableOrigin',
        'EnableOriginator': 'enableOriginator',
        'ExtendedCommunity': 'extendedCommunity',
        'LocalPref': 'localPref',
        'MultiExit': 'multiExit',
        'NextHop': 'nextHop',
        'NextHopIpType': 'nextHopIpType',
        'NextHopMode': 'nextHopMode',
        'Origin': 'origin',
        'OriginatorId': 'originatorId',
        'SetNextHop': 'setNextHop',
    }

    def __init__(self, parent):
        super(AdInclusiveMulticastRouteAttributes, self).__init__(parent)

    @property
    def AggregatorAs(self):
        """
        Returns
        -------
        - number: The AS associated with the aggregator router ID in the AGGREGATOR attribute. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregatorAs'])
    @AggregatorAs.setter
    def AggregatorAs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregatorAs'], value)

    @property
    def AggregatorId(self):
        """
        Returns
        -------
        - str: The IP address of the router that aggregated two or more routes in the AGGREGATOR attribute. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregatorId'])
    @AggregatorId.setter
    def AggregatorId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregatorId'], value)

    @property
    def AsPath(self):
        """
        Returns
        -------
        - list(dict(arg1:bool,arg2:str[unknown | asSet | asSequence | asConfedSet | asConfedSequence],arg3:list[number])): Indicates the local IP address of the BGP router
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsPath'])
    @AsPath.setter
    def AsPath(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AsPath'], value)

    @property
    def AsSetMode(self):
        """
        Returns
        -------
        - str(includeAsSeq | includeAsSeqConf | includeAsSet | includeAsSetConf | noInclude | prependAs): The mode to set the AsPath. Possible values include:
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsSetMode'])
    @AsSetMode.setter
    def AsSetMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AsSetMode'], value)

    @property
    def Cluster(self):
        """
        Returns
        -------
        - list(number): The list of BGP clusters that a particular route has passed through
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cluster'])
    @Cluster.setter
    def Cluster(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Cluster'], value)

    @property
    def Community(self):
        """
        Returns
        -------
        - list(number): This object is used to construct an extended community attribute for a route item
        """
        return self._get_attribute(self._SDM_ATT_MAP['Community'])
    @Community.setter
    def Community(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Community'], value)

    @property
    def EnableAggregator(self):
        """
        Returns
        -------
        - bool: Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAggregator'])
    @EnableAggregator.setter
    def EnableAggregator(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAggregator'], value)

    @property
    def EnableAsPath(self):
        """
        Returns
        -------
        - bool: Enables the generation of AS Path related items.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsPath'])
    @EnableAsPath.setter
    def EnableAsPath(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsPath'], value)

    @property
    def EnableAtomicAggregate(self):
        """
        Returns
        -------
        - bool: Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAtomicAggregate'])
    @EnableAtomicAggregate.setter
    def EnableAtomicAggregate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAtomicAggregate'], value)

    @property
    def EnableCluster(self):
        """
        Returns
        -------
        - bool: Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCluster'])
    @EnableCluster.setter
    def EnableCluster(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCluster'], value)

    @property
    def EnableCommunity(self):
        """
        Returns
        -------
        - bool: Enables the generation of a COMMUNITY attribute list. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCommunity'])
    @EnableCommunity.setter
    def EnableCommunity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCommunity'], value)

    @property
    def EnableLocalPref(self):
        """
        Returns
        -------
        - bool: Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLocalPref'])
    @EnableLocalPref.setter
    def EnableLocalPref(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLocalPref'], value)

    @property
    def EnableMultiExit(self):
        """
        Returns
        -------
        - bool: Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMultiExit'])
    @EnableMultiExit.setter
    def EnableMultiExit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMultiExit'], value)

    @property
    def EnableNextHop(self):
        """
        Returns
        -------
        - bool: Enables the generation of a NEXT HOP attribute. (default = true)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableNextHop'])
    @EnableNextHop.setter
    def EnableNextHop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableNextHop'], value)

    @property
    def EnableOrigin(self):
        """
        Returns
        -------
        - bool: Enables the generation of an ORIGIN attribute. (default = true)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOrigin'])
    @EnableOrigin.setter
    def EnableOrigin(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOrigin'], value)

    @property
    def EnableOriginator(self):
        """
        Returns
        -------
        - bool: Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOriginator'])
    @EnableOriginator.setter
    def EnableOriginator(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOriginator'], value)

    @property
    def ExtendedCommunity(self):
        """
        Returns
        -------
        - list(dict(arg1:str[decimal | hex | ip | ieeeFloat],arg2:str[decimal | hex | ip | ieeeFloat],arg3:str[twoOctetAs | ip | fourOctetAs | opaque | administratorAsTwoOctetLinkBw],arg4:str[routeTarget | origin | extendedBandwidthSubType],arg5:str)): This object is used to construct an extended community attribute for a route item
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtendedCommunity'])
    @ExtendedCommunity.setter
    def ExtendedCommunity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExtendedCommunity'], value)

    @property
    def LocalPref(self):
        """
        Returns
        -------
        - number: The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalPref'])
    @LocalPref.setter
    def LocalPref(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LocalPref'], value)

    @property
    def MultiExit(self):
        """
        Returns
        -------
        - number: The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MultiExit'])
    @MultiExit.setter
    def MultiExit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MultiExit'], value)

    @property
    def NextHop(self):
        """
        Returns
        -------
        - str: The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHop'])
    @NextHop.setter
    def NextHop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHop'], value)

    @property
    def NextHopIpType(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): IP type of Next Hop. Default is IPv4.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopIpType'])
    @NextHopIpType.setter
    def NextHopIpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHopIpType'], value)

    @property
    def NextHopMode(self):
        """
        Returns
        -------
        - str(fixed | incrementPerPeer): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopMode'])
    @NextHopMode.setter
    def NextHopMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHopMode'], value)

    @property
    def Origin(self):
        """
        Returns
        -------
        - str(igp | egp | incomplete): (0x03) Route Origin Community. Identifies one or more routers injecting a set of routes with this extended community, into BGP
        """
        return self._get_attribute(self._SDM_ATT_MAP['Origin'])
    @Origin.setter
    def Origin(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Origin'], value)

    @property
    def OriginatorId(self):
        """
        Returns
        -------
        - str: The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginatorId'])
    @OriginatorId.setter
    def OriginatorId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OriginatorId'], value)

    @property
    def SetNextHop(self):
        """
        Returns
        -------
        - str(manually | sameAsLocalIp): Indicates now to set the next hop IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetNextHop'])
    @SetNextHop.setter
    def SetNextHop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetNextHop'], value)

    def update(self, AggregatorAs=None, AggregatorId=None, AsPath=None, AsSetMode=None, Cluster=None, Community=None, EnableAggregator=None, EnableAsPath=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableLocalPref=None, EnableMultiExit=None, EnableNextHop=None, EnableOrigin=None, EnableOriginator=None, ExtendedCommunity=None, LocalPref=None, MultiExit=None, NextHop=None, NextHopIpType=None, NextHopMode=None, Origin=None, OriginatorId=None, SetNextHop=None):
        """Updates adInclusiveMulticastRouteAttributes resource on the server.

        Args
        ----
        - AggregatorAs (number): The AS associated with the aggregator router ID in the AGGREGATOR attribute. (default = 0)
        - AggregatorId (str): The IP address of the router that aggregated two or more routes in the AGGREGATOR attribute. (default = 0.0.0.0)
        - AsPath (list(dict(arg1:bool,arg2:str[unknown | asSet | asSequence | asConfedSet | asConfedSequence],arg3:list[number]))): Indicates the local IP address of the BGP router
        - AsSetMode (str(includeAsSeq | includeAsSeqConf | includeAsSet | includeAsSetConf | noInclude | prependAs)): The mode to set the AsPath. Possible values include:
        - Cluster (list(number)): The list of BGP clusters that a particular route has passed through
        - Community (list(number)): This object is used to construct an extended community attribute for a route item
        - EnableAggregator (bool): Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        - EnableAsPath (bool): Enables the generation of AS Path related items.
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
        - Origin (str(igp | egp | incomplete)): (0x03) Route Origin Community. Identifies one or more routers injecting a set of routes with this extended community, into BGP
        - OriginatorId (str): The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        - SetNextHop (str(manually | sameAsLocalIp)): Indicates now to set the next hop IP address.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
