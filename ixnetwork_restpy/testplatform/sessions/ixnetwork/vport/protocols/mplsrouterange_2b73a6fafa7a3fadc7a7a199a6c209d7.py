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


class MplsRouteRange(Base):
    """Represents a route range that also advertises an MPLS label and is associated with a route item.
    The MplsRouteRange class encapsulates a list of mplsRouteRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the MplsRouteRange.find() method.
    The list can be managed by using the MplsRouteRange.add() and MplsRouteRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'mplsRouteRange'
    _SDM_ATT_MAP = {
        'AdvertiseNextHopAsV4': 'advertiseNextHopAsV4',
        'AggregatorAsNum': 'aggregatorAsNum',
        'AggregatorIpAddress': 'aggregatorIpAddress',
        'AsPathSetMode': 'asPathSetMode',
        'EnableAggregator': 'enableAggregator',
        'EnableAggregatorIdIncrementMode': 'enableAggregatorIdIncrementMode',
        'EnableAsPath': 'enableAsPath',
        'EnableAtomicAttribute': 'enableAtomicAttribute',
        'EnableCluster': 'enableCluster',
        'EnableCommunity': 'enableCommunity',
        'EnableGenerateUniqueRoutes': 'enableGenerateUniqueRoutes',
        'EnableIncludeLoopback': 'enableIncludeLoopback',
        'EnableIncludeMulticast': 'enableIncludeMulticast',
        'EnableLocalPref': 'enableLocalPref',
        'EnableMed': 'enableMed',
        'EnableNextHop': 'enableNextHop',
        'EnableOrigin': 'enableOrigin',
        'EnableOriginatorId': 'enableOriginatorId',
        'EnableTraditionalNlriUpdate': 'enableTraditionalNlriUpdate',
        'Enabled': 'enabled',
        'EndOfRib': 'endOfRib',
        'FromPacking': 'fromPacking',
        'FromPrefix': 'fromPrefix',
        'IpType': 'ipType',
        'IterationStep': 'iterationStep',
        'LocalPref': 'localPref',
        'Med': 'med',
        'NetworkAddress': 'networkAddress',
        'NextHopIpAddress': 'nextHopIpAddress',
        'NextHopMode': 'nextHopMode',
        'NextHopSetMode': 'nextHopSetMode',
        'NumRoutes': 'numRoutes',
        'OriginProtocol': 'originProtocol',
        'OriginatorId': 'originatorId',
        'ThruPacking': 'thruPacking',
        'ThruPrefix': 'thruPrefix',
    }

    def __init__(self, parent):
        super(MplsRouteRange, self).__init__(parent)

    @property
    def AsSegment(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.assegment_77023b63251dc6667bdf6c21a3e43b82.AsSegment): An instance of the AsSegment class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.assegment_77023b63251dc6667bdf6c21a3e43b82 import AsSegment
        return AsSegment(self)._select()

    @property
    def Cluster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_d68b61bb2cd5e48de06e56c1bb4b9cfb.Cluster): An instance of the Cluster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_d68b61bb2cd5e48de06e56c1bb4b9cfb import Cluster
        return Cluster(self)._select()

    @property
    def Community(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.community_46f6c2c27e8a80b9e728ca3a28276bc2.Community): An instance of the Community class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.community_46f6c2c27e8a80b9e728ca3a28276bc2 import Community
        return Community(self)._select()

    @property
    def ExtendedCommunity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.extendedcommunity_9dbd9a94c067c10769a25642ca9a2116.ExtendedCommunity): An instance of the ExtendedCommunity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.extendedcommunity_9dbd9a94c067c10769a25642ca9a2116 import ExtendedCommunity
        return ExtendedCommunity(self)._select()

    @property
    def Flapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flapping_14ce629a4dbc4bd9b20c8fe1dc2a1e04.Flapping): An instance of the Flapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flapping_14ce629a4dbc4bd9b20c8fe1dc2a1e04 import Flapping
        return Flapping(self)._select()

    @property
    def LabelSpace(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelspace_6d08c054aa4a79300972f72fa46e7edd.LabelSpace): An instance of the LabelSpace class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelspace_6d08c054aa4a79300972f72fa46e7edd import LabelSpace
        return LabelSpace(self)._select()

    @property
    def AdvertiseNextHopAsV4(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdvertiseNextHopAsV4'])
    @AdvertiseNextHopAsV4.setter
    def AdvertiseNextHopAsV4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdvertiseNextHopAsV4'], value)

    @property
    def AggregatorAsNum(self):
        """
        Returns
        -------
        - number: If enabled, sets the AS associated with the aggregator router ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregatorAsNum'])
    @AggregatorAsNum.setter
    def AggregatorAsNum(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregatorAsNum'], value)

    @property
    def AggregatorIpAddress(self):
        """
        Returns
        -------
        - str: If enabled, generates an aggregator attribute that indicates the router ID of the router that aggregated two or more routes into one.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregatorIpAddress'])
    @AggregatorIpAddress.setter
    def AggregatorIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregatorIpAddress'], value)

    @property
    def AsPathSetMode(self):
        """
        Returns
        -------
        - str(noInclude | includeAsSeq | includeAsSet | includeAsSeqConf | includeAsSetConf | prependAs): The mode to set the AsPath. Possible values include:+ noInclude+ includeAsSeq+ includeAsSet+ includeAsSeqConf+ includeAsSetConf+ prependAs
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsPathSetMode'])
    @AsPathSetMode.setter
    def AsPathSetMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AsPathSetMode'], value)

    @property
    def EnableAggregator(self):
        """
        Returns
        -------
        - bool: If enabled, generates an aggregator attribute that indicates the router ID that aggregated two or more routes into one.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAggregator'])
    @EnableAggregator.setter
    def EnableAggregator(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAggregator'], value)

    @property
    def EnableAggregatorIdIncrementMode(self):
        """
        Returns
        -------
        - bool: If true, Causes the AS field to be incremented for each neighbor session generated for the range of neighbor addresses in the AGGREGATOR attribute. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAggregatorIdIncrementMode'])
    @EnableAggregatorIdIncrementMode.setter
    def EnableAggregatorIdIncrementMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAggregatorIdIncrementMode'], value)

    @property
    def EnableAsPath(self):
        """
        Returns
        -------
        - bool: If true, Enables the generation of AS Path related items.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAsPath'])
    @EnableAsPath.setter
    def EnableAsPath(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAsPath'], value)

    @property
    def EnableAtomicAttribute(self):
        """
        Returns
        -------
        - bool: If enabled, sets the attribute bit that indicates that the router has aggregated two or more prefixes together into one.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAtomicAttribute'])
    @EnableAtomicAttribute.setter
    def EnableAtomicAttribute(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAtomicAttribute'], value)

    @property
    def EnableCluster(self):
        """
        Returns
        -------
        - bool: If enabled, generates a list of BGP clusters that a particular route has passed through.
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
        - bool: If enabled, indicates that a community attribute should be added to the BGP entry.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCommunity'])
    @EnableCommunity.setter
    def EnableCommunity(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCommunity'], value)

    @property
    def EnableGenerateUniqueRoutes(self):
        """
        Returns
        -------
        - bool: When true, each router generates a different IP address range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableGenerateUniqueRoutes'])
    @EnableGenerateUniqueRoutes.setter
    def EnableGenerateUniqueRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableGenerateUniqueRoutes'], value)

    @property
    def EnableIncludeLoopback(self):
        """
        Returns
        -------
        - bool: If true, will include the loopback address (127.0.0.1) if it is in the generated network range. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIncludeLoopback'])
    @EnableIncludeLoopback.setter
    def EnableIncludeLoopback(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIncludeLoopback'], value)

    @property
    def EnableIncludeMulticast(self):
        """
        Returns
        -------
        - bool: If true, will include multicast addresses if they are in the generated network range. The SAFI used for multicast addresses is dictated by the setting of the enableProperSafi option. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIncludeMulticast'])
    @EnableIncludeMulticast.setter
    def EnableIncludeMulticast(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIncludeMulticast'], value)

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
    def EnableMed(self):
        """
        Returns
        -------
        - bool: Enables the generation of a MULTI EXIT DISCRIMINATOR attribute, based on the information in MED. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMed'])
    @EnableMed.setter
    def EnableMed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMed'], value)

    @property
    def EnableNextHop(self):
        """
        Returns
        -------
        - bool: Enables the generation of a NEXT HOP attribute, based on information in nextHopIpAddress and nextHopMode (default = true)
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
        - bool: Enables the generation of an ORIGIN attribute, based on information in originProtocol. (default = true)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOrigin'])
    @EnableOrigin.setter
    def EnableOrigin(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOrigin'], value)

    @property
    def EnableOriginatorId(self):
        """
        Returns
        -------
        - bool: Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOriginatorId'])
    @EnableOriginatorId.setter
    def EnableOriginatorId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOriginatorId'], value)

    @property
    def EnableTraditionalNlriUpdate(self):
        """
        Returns
        -------
        - bool: If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableTraditionalNlriUpdate'])
    @EnableTraditionalNlriUpdate.setter
    def EnableTraditionalNlriUpdate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableTraditionalNlriUpdate'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, enables the MPLS route range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EndOfRib(self):
        """
        Returns
        -------
        - bool: If true, enables end of rib
        """
        return self._get_attribute(self._SDM_ATT_MAP['EndOfRib'])
    @EndOfRib.setter
    def EndOfRib(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EndOfRib'], value)

    @property
    def FromPacking(self):
        """
        Returns
        -------
        - number: The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['FromPacking'])
    @FromPacking.setter
    def FromPacking(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FromPacking'], value)

    @property
    def FromPrefix(self):
        """
        Returns
        -------
        - number: The first prefix length to generate based on the networkAddress and numRanges. (default = 24)
        """
        return self._get_attribute(self._SDM_ATT_MAP['FromPrefix'])
    @FromPrefix.setter
    def FromPrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FromPrefix'], value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - str(ipAny | ipv4 | ipv6): The Internet Protocol type for the addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpType'])
    @IpType.setter
    def IpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpType'], value)

    @property
    def IterationStep(self):
        """
        Returns
        -------
        - number: During prefix generation, the increment between prefixes. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['IterationStep'])
    @IterationStep.setter
    def IterationStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IterationStep'], value)

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
    def Med(self):
        """
        Returns
        -------
        - number: The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Med'])
    @Med.setter
    def Med(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Med'], value)

    @property
    def NetworkAddress(self):
        """
        Returns
        -------
        - str: The network address used for the generated prefixes, in either IPv4 or IPv6 format. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkAddress'])
    @NetworkAddress.setter
    def NetworkAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkAddress'], value)

    @property
    def NextHopIpAddress(self):
        """
        Returns
        -------
        - str: The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopIpAddress'])
    @NextHopIpAddress.setter
    def NextHopIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHopIpAddress'], value)

    @property
    def NextHopMode(self):
        """
        Returns
        -------
        - str(fixed | nextHopIncrement | incrementPerPrefix): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopMode'])
    @NextHopMode.setter
    def NextHopMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHopMode'], value)

    @property
    def NextHopSetMode(self):
        """
        Returns
        -------
        - str(setManually | sameAsLocalIp): Indicates now to set the next hop IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopSetMode'])
    @NextHopSetMode.setter
    def NextHopSetMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHopSetMode'], value)

    @property
    def NumRoutes(self):
        """
        Returns
        -------
        - number: The number of prefixes (routes) to generate for this routeItem. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumRoutes'])
    @NumRoutes.setter
    def NumRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumRoutes'], value)

    @property
    def OriginProtocol(self):
        """
        Returns
        -------
        - str(igp | egp | incomplete): An indication of where the route entry originated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginProtocol'])
    @OriginProtocol.setter
    def OriginProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OriginProtocol'], value)

    @property
    def OriginatorId(self):
        """
        Returns
        -------
        - str: The ID for the router that originated the route.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginatorId'])
    @OriginatorId.setter
    def OriginatorId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OriginatorId'], value)

    @property
    def ThruPacking(self):
        """
        Returns
        -------
        - number: The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ThruPacking'])
    @ThruPacking.setter
    def ThruPacking(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ThruPacking'], value)

    @property
    def ThruPrefix(self):
        """
        Returns
        -------
        - number: The last prefix length to generate based on the networkAddress and numRanges. (default = 24)
        """
        return self._get_attribute(self._SDM_ATT_MAP['ThruPrefix'])
    @ThruPrefix.setter
    def ThruPrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ThruPrefix'], value)

    def update(self, AdvertiseNextHopAsV4=None, AggregatorAsNum=None, AggregatorIpAddress=None, AsPathSetMode=None, EnableAggregator=None, EnableAggregatorIdIncrementMode=None, EnableAsPath=None, EnableAtomicAttribute=None, EnableCluster=None, EnableCommunity=None, EnableGenerateUniqueRoutes=None, EnableIncludeLoopback=None, EnableIncludeMulticast=None, EnableLocalPref=None, EnableMed=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableTraditionalNlriUpdate=None, Enabled=None, EndOfRib=None, FromPacking=None, FromPrefix=None, IpType=None, IterationStep=None, LocalPref=None, Med=None, NetworkAddress=None, NextHopIpAddress=None, NextHopMode=None, NextHopSetMode=None, NumRoutes=None, OriginProtocol=None, OriginatorId=None, ThruPacking=None, ThruPrefix=None):
        """Updates mplsRouteRange resource on the server.

        Args
        ----
        - AdvertiseNextHopAsV4 (bool): NOT DEFINED
        - AggregatorAsNum (number): If enabled, sets the AS associated with the aggregator router ID.
        - AggregatorIpAddress (str): If enabled, generates an aggregator attribute that indicates the router ID of the router that aggregated two or more routes into one.
        - AsPathSetMode (str(noInclude | includeAsSeq | includeAsSet | includeAsSeqConf | includeAsSetConf | prependAs)): The mode to set the AsPath. Possible values include:+ noInclude+ includeAsSeq+ includeAsSet+ includeAsSeqConf+ includeAsSetConf+ prependAs
        - EnableAggregator (bool): If enabled, generates an aggregator attribute that indicates the router ID that aggregated two or more routes into one.
        - EnableAggregatorIdIncrementMode (bool): If true, Causes the AS field to be incremented for each neighbor session generated for the range of neighbor addresses in the AGGREGATOR attribute. (default = 1)
        - EnableAsPath (bool): If true, Enables the generation of AS Path related items.
        - EnableAtomicAttribute (bool): If enabled, sets the attribute bit that indicates that the router has aggregated two or more prefixes together into one.
        - EnableCluster (bool): If enabled, generates a list of BGP clusters that a particular route has passed through.
        - EnableCommunity (bool): If enabled, indicates that a community attribute should be added to the BGP entry.
        - EnableGenerateUniqueRoutes (bool): When true, each router generates a different IP address range.
        - EnableIncludeLoopback (bool): If true, will include the loopback address (127.0.0.1) if it is in the generated network range. (default = false)
        - EnableIncludeMulticast (bool): If true, will include multicast addresses if they are in the generated network range. The SAFI used for multicast addresses is dictated by the setting of the enableProperSafi option. (default = false)
        - EnableLocalPref (bool): Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        - EnableMed (bool): Enables the generation of a MULTI EXIT DISCRIMINATOR attribute, based on the information in MED. (default = false)
        - EnableNextHop (bool): Enables the generation of a NEXT HOP attribute, based on information in nextHopIpAddress and nextHopMode (default = true)
        - EnableOrigin (bool): Enables the generation of an ORIGIN attribute, based on information in originProtocol. (default = true)
        - EnableOriginatorId (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId.
        - EnableTraditionalNlriUpdate (bool): If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        - Enabled (bool): If true, enables the MPLS route range.
        - EndOfRib (bool): If true, enables end of rib
        - FromPacking (number): The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. (default = 0)
        - FromPrefix (number): The first prefix length to generate based on the networkAddress and numRanges. (default = 24)
        - IpType (str(ipAny | ipv4 | ipv6)): The Internet Protocol type for the addresses.
        - IterationStep (number): During prefix generation, the increment between prefixes. (default = 1)
        - LocalPref (number): The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        - Med (number): The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        - NetworkAddress (str): The network address used for the generated prefixes, in either IPv4 or IPv6 format. (default = 0.0.0.0)
        - NextHopIpAddress (str): The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        - NextHopMode (str(fixed | nextHopIncrement | incrementPerPrefix)): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
        - NextHopSetMode (str(setManually | sameAsLocalIp)): Indicates now to set the next hop IP address.
        - NumRoutes (number): The number of prefixes (routes) to generate for this routeItem. (default = 1)
        - OriginProtocol (str(igp | egp | incomplete)): An indication of where the route entry originated.
        - OriginatorId (str): The ID for the router that originated the route.
        - ThruPacking (number): The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking.
        - ThruPrefix (number): The last prefix length to generate based on the networkAddress and numRanges. (default = 24)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdvertiseNextHopAsV4=None, AggregatorAsNum=None, AggregatorIpAddress=None, AsPathSetMode=None, EnableAggregator=None, EnableAggregatorIdIncrementMode=None, EnableAsPath=None, EnableAtomicAttribute=None, EnableCluster=None, EnableCommunity=None, EnableGenerateUniqueRoutes=None, EnableIncludeLoopback=None, EnableIncludeMulticast=None, EnableLocalPref=None, EnableMed=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableTraditionalNlriUpdate=None, Enabled=None, EndOfRib=None, FromPacking=None, FromPrefix=None, IpType=None, IterationStep=None, LocalPref=None, Med=None, NetworkAddress=None, NextHopIpAddress=None, NextHopMode=None, NextHopSetMode=None, NumRoutes=None, OriginProtocol=None, OriginatorId=None, ThruPacking=None, ThruPrefix=None):
        """Adds a new mplsRouteRange resource on the server and adds it to the container.

        Args
        ----
        - AdvertiseNextHopAsV4 (bool): NOT DEFINED
        - AggregatorAsNum (number): If enabled, sets the AS associated with the aggregator router ID.
        - AggregatorIpAddress (str): If enabled, generates an aggregator attribute that indicates the router ID of the router that aggregated two or more routes into one.
        - AsPathSetMode (str(noInclude | includeAsSeq | includeAsSet | includeAsSeqConf | includeAsSetConf | prependAs)): The mode to set the AsPath. Possible values include:+ noInclude+ includeAsSeq+ includeAsSet+ includeAsSeqConf+ includeAsSetConf+ prependAs
        - EnableAggregator (bool): If enabled, generates an aggregator attribute that indicates the router ID that aggregated two or more routes into one.
        - EnableAggregatorIdIncrementMode (bool): If true, Causes the AS field to be incremented for each neighbor session generated for the range of neighbor addresses in the AGGREGATOR attribute. (default = 1)
        - EnableAsPath (bool): If true, Enables the generation of AS Path related items.
        - EnableAtomicAttribute (bool): If enabled, sets the attribute bit that indicates that the router has aggregated two or more prefixes together into one.
        - EnableCluster (bool): If enabled, generates a list of BGP clusters that a particular route has passed through.
        - EnableCommunity (bool): If enabled, indicates that a community attribute should be added to the BGP entry.
        - EnableGenerateUniqueRoutes (bool): When true, each router generates a different IP address range.
        - EnableIncludeLoopback (bool): If true, will include the loopback address (127.0.0.1) if it is in the generated network range. (default = false)
        - EnableIncludeMulticast (bool): If true, will include multicast addresses if they are in the generated network range. The SAFI used for multicast addresses is dictated by the setting of the enableProperSafi option. (default = false)
        - EnableLocalPref (bool): Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        - EnableMed (bool): Enables the generation of a MULTI EXIT DISCRIMINATOR attribute, based on the information in MED. (default = false)
        - EnableNextHop (bool): Enables the generation of a NEXT HOP attribute, based on information in nextHopIpAddress and nextHopMode (default = true)
        - EnableOrigin (bool): Enables the generation of an ORIGIN attribute, based on information in originProtocol. (default = true)
        - EnableOriginatorId (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId.
        - EnableTraditionalNlriUpdate (bool): If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        - Enabled (bool): If true, enables the MPLS route range.
        - EndOfRib (bool): If true, enables end of rib
        - FromPacking (number): The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. (default = 0)
        - FromPrefix (number): The first prefix length to generate based on the networkAddress and numRanges. (default = 24)
        - IpType (str(ipAny | ipv4 | ipv6)): The Internet Protocol type for the addresses.
        - IterationStep (number): During prefix generation, the increment between prefixes. (default = 1)
        - LocalPref (number): The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        - Med (number): The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        - NetworkAddress (str): The network address used for the generated prefixes, in either IPv4 or IPv6 format. (default = 0.0.0.0)
        - NextHopIpAddress (str): The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        - NextHopMode (str(fixed | nextHopIncrement | incrementPerPrefix)): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
        - NextHopSetMode (str(setManually | sameAsLocalIp)): Indicates now to set the next hop IP address.
        - NumRoutes (number): The number of prefixes (routes) to generate for this routeItem. (default = 1)
        - OriginProtocol (str(igp | egp | incomplete)): An indication of where the route entry originated.
        - OriginatorId (str): The ID for the router that originated the route.
        - ThruPacking (number): The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking.
        - ThruPrefix (number): The last prefix length to generate based on the networkAddress and numRanges. (default = 24)

        Returns
        -------
        - self: This instance with all currently retrieved mplsRouteRange resources using find and the newly added mplsRouteRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained mplsRouteRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdvertiseNextHopAsV4=None, AggregatorAsNum=None, AggregatorIpAddress=None, AsPathSetMode=None, EnableAggregator=None, EnableAggregatorIdIncrementMode=None, EnableAsPath=None, EnableAtomicAttribute=None, EnableCluster=None, EnableCommunity=None, EnableGenerateUniqueRoutes=None, EnableIncludeLoopback=None, EnableIncludeMulticast=None, EnableLocalPref=None, EnableMed=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableTraditionalNlriUpdate=None, Enabled=None, EndOfRib=None, FromPacking=None, FromPrefix=None, IpType=None, IterationStep=None, LocalPref=None, Med=None, NetworkAddress=None, NextHopIpAddress=None, NextHopMode=None, NextHopSetMode=None, NumRoutes=None, OriginProtocol=None, OriginatorId=None, ThruPacking=None, ThruPrefix=None):
        """Finds and retrieves mplsRouteRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mplsRouteRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mplsRouteRange resources from the server.

        Args
        ----
        - AdvertiseNextHopAsV4 (bool): NOT DEFINED
        - AggregatorAsNum (number): If enabled, sets the AS associated with the aggregator router ID.
        - AggregatorIpAddress (str): If enabled, generates an aggregator attribute that indicates the router ID of the router that aggregated two or more routes into one.
        - AsPathSetMode (str(noInclude | includeAsSeq | includeAsSet | includeAsSeqConf | includeAsSetConf | prependAs)): The mode to set the AsPath. Possible values include:+ noInclude+ includeAsSeq+ includeAsSet+ includeAsSeqConf+ includeAsSetConf+ prependAs
        - EnableAggregator (bool): If enabled, generates an aggregator attribute that indicates the router ID that aggregated two or more routes into one.
        - EnableAggregatorIdIncrementMode (bool): If true, Causes the AS field to be incremented for each neighbor session generated for the range of neighbor addresses in the AGGREGATOR attribute. (default = 1)
        - EnableAsPath (bool): If true, Enables the generation of AS Path related items.
        - EnableAtomicAttribute (bool): If enabled, sets the attribute bit that indicates that the router has aggregated two or more prefixes together into one.
        - EnableCluster (bool): If enabled, generates a list of BGP clusters that a particular route has passed through.
        - EnableCommunity (bool): If enabled, indicates that a community attribute should be added to the BGP entry.
        - EnableGenerateUniqueRoutes (bool): When true, each router generates a different IP address range.
        - EnableIncludeLoopback (bool): If true, will include the loopback address (127.0.0.1) if it is in the generated network range. (default = false)
        - EnableIncludeMulticast (bool): If true, will include multicast addresses if they are in the generated network range. The SAFI used for multicast addresses is dictated by the setting of the enableProperSafi option. (default = false)
        - EnableLocalPref (bool): Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        - EnableMed (bool): Enables the generation of a MULTI EXIT DISCRIMINATOR attribute, based on the information in MED. (default = false)
        - EnableNextHop (bool): Enables the generation of a NEXT HOP attribute, based on information in nextHopIpAddress and nextHopMode (default = true)
        - EnableOrigin (bool): Enables the generation of an ORIGIN attribute, based on information in originProtocol. (default = true)
        - EnableOriginatorId (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId.
        - EnableTraditionalNlriUpdate (bool): If enabled, use the traditional NLRI in the UPDATE message, instead of using the MP_REACH_NLRI Multi-protocol extension to advertise the routes. (Not applicable for MPLS and MPLS VPN Route Ranges.)
        - Enabled (bool): If true, enables the MPLS route range.
        - EndOfRib (bool): If true, enables end of rib
        - FromPacking (number): The minimum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking. (default = 0)
        - FromPrefix (number): The first prefix length to generate based on the networkAddress and numRanges. (default = 24)
        - IpType (str(ipAny | ipv4 | ipv6)): The Internet Protocol type for the addresses.
        - IterationStep (number): During prefix generation, the increment between prefixes. (default = 1)
        - LocalPref (number): The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        - Med (number): The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        - NetworkAddress (str): The network address used for the generated prefixes, in either IPv4 or IPv6 format. (default = 0.0.0.0)
        - NextHopIpAddress (str): The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        - NextHopMode (str(fixed | nextHopIncrement | incrementPerPrefix)): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses.
        - NextHopSetMode (str(setManually | sameAsLocalIp)): Indicates now to set the next hop IP address.
        - NumRoutes (number): The number of prefixes (routes) to generate for this routeItem. (default = 1)
        - OriginProtocol (str(igp | egp | incomplete)): An indication of where the route entry originated.
        - OriginatorId (str): The ID for the router that originated the route.
        - ThruPacking (number): The maximum number of routes to pack into an UPDATE message. Random numbers are chosen from the range fromPacking to toPacking.
        - ThruPrefix (number): The last prefix length to generate based on the networkAddress and numRanges. (default = 24)

        Returns
        -------
        - self: This instance with matching mplsRouteRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mplsRouteRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mplsRouteRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
