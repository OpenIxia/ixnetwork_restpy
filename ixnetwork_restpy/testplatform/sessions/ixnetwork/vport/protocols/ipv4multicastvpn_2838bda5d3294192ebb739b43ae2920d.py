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
from typing import List, Any, Union


class Ipv4MulticastVpn(Base):
    """If enabled, this BGP router/peer supports the IPv4 Multicast/VPN address
family..
    The Ipv4MulticastVpn class encapsulates a list of ipv4MulticastVpn resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ipv4MulticastVpn.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv4MulticastVpn'
    _SDM_ATT_MAP = {
        'AddressFamily': 'addressFamily',
        'AddressLength': 'addressLength',
        'CMcastRouteType': 'cMcastRouteType',
        'GroupAddress': 'groupAddress',
        'Neighbor': 'neighbor',
        'OpaqueLength': 'opaqueLength',
        'OriginatingRouter': 'originatingRouter',
        'RootAddress': 'rootAddress',
        'RouteDistinguisher': 'routeDistinguisher',
        'RouteKeyGroupAddress': 'routeKeyGroupAddress',
        'RouteKeyOriginatingRouter': 'routeKeyOriginatingRouter',
        'RouteKeyRouteDistinguisher': 'routeKeyRouteDistinguisher',
        'RouteKeyRsvpP2mpExtendedTunnelId': 'routeKeyRsvpP2mpExtendedTunnelId',
        'RouteKeyRsvpP2mpId': 'routeKeyRsvpP2mpId',
        'RouteKeyRsvpP2mpTunnelId': 'routeKeyRsvpP2mpTunnelId',
        'RouteKeySourceAddress': 'routeKeySourceAddress',
        'RouteKeyTunnelType': 'routeKeyTunnelType',
        'RouteKeyUpstreamLabel': 'routeKeyUpstreamLabel',
        'RouteType': 'routeType',
        'RsvpP2mpExtendedTunnelId': 'rsvpP2mpExtendedTunnelId',
        'RsvpP2mpId': 'rsvpP2mpId',
        'RsvpP2mpTunnelId': 'rsvpP2mpTunnelId',
        'SourceAddress': 'sourceAddress',
        'SourceAs': 'sourceAs',
        'TunnelType': 'tunnelType',
        'UpstreamLabel': 'upstreamLabel',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Ipv4MulticastVpn, self).__init__(parent, list_op)

    @property
    def OpaqueValueElement(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_d49e7d4c8b0df2f382492278f34bd590.OpaqueValueElement): An instance of the OpaqueValueElement class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_d49e7d4c8b0df2f382492278f34bd590 import OpaqueValueElement
        if self._properties.get('OpaqueValueElement', None) is not None:
            return self._properties.get('OpaqueValueElement')
        else:
            return OpaqueValueElement(self)

    @property
    def AddressFamily(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The address family identifier value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressFamily'])

    @property
    def AddressLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The length of the address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressLength'])

    @property
    def CMcastRouteType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The c-multicast route type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CMcastRouteType'])

    @property
    def GroupAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IPv4 Multicast group address in the range of group addresses included in this Register message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupAddress'])

    @property
    def Neighbor(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The neighbor address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Neighbor'])

    @property
    def OpaqueLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) Indicates the opaque length.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OpaqueLength'])

    @property
    def OriginatingRouter(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The originating router address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OriginatingRouter'])

    @property
    def RootAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) Indicates the root address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootAddress'])

    @property
    def RouteDistinguisher(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The route distinguisher for the route, for use with IPv4 multicast VPN address types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteDistinguisher'])

    @property
    def RouteKeyGroupAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The key group address of the route.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyGroupAddress'])

    @property
    def RouteKeyOriginatingRouter(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The key originating address of the router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyOriginatingRouter'])

    @property
    def RouteKeyRouteDistinguisher(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The key route distinguisher for the route, for use with IPv4 multicast VPN address types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyRouteDistinguisher'])

    @property
    def RouteKeyRsvpP2mpExtendedTunnelId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The key rsvp p2mp extended tunnel id for the route, for use with IPv4 multicast VPN address types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyRsvpP2mpExtendedTunnelId'])

    @property
    def RouteKeyRsvpP2mpId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The key rsvp p2mp id for the route, for use with IPv4 multicast VPN address types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyRsvpP2mpId'])

    @property
    def RouteKeyRsvpP2mpTunnelId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The key rsvp p2mp tunnel id for the route, for use with IPv4 multicast VPN address types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyRsvpP2mpTunnelId'])

    @property
    def RouteKeySourceAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The key source address for the route, for use with IPv4 multicast VPN address types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeySourceAddress'])

    @property
    def RouteKeyTunnelType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The key tunnel type for the route, for use with IPv4 multicast VPN address types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyTunnelType'])

    @property
    def RouteKeyUpstreamLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The key upstream label for the route, for use with IPv4 multicast VPN address types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteKeyUpstreamLabel'])

    @property
    def RouteType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The route type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteType'])

    @property
    def RsvpP2mpExtendedTunnelId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The rsvp p2mp extended tunnel id.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsvpP2mpExtendedTunnelId'])

    @property
    def RsvpP2mpId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The rsvp p2mp id.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsvpP2mpId'])

    @property
    def RsvpP2mpTunnelId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The rsvp p2mp tunnel id.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsvpP2mpTunnelId'])

    @property
    def SourceAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAddress'])

    @property
    def SourceAs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The source AS number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAs'])

    @property
    def TunnelType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The tunnel type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelType'])

    @property
    def UpstreamLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The upstream label.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLabel'])

    def add(self):
        """Adds a new ipv4MulticastVpn resource on the json, only valid with config assistant

        Returns
        -------
        - self: This instance with all currently retrieved ipv4MulticastVpn resources using find and the newly added ipv4MulticastVpn resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AddressFamily=None, AddressLength=None, CMcastRouteType=None, GroupAddress=None, Neighbor=None, OpaqueLength=None, OriginatingRouter=None, RootAddress=None, RouteDistinguisher=None, RouteKeyGroupAddress=None, RouteKeyOriginatingRouter=None, RouteKeyRouteDistinguisher=None, RouteKeyRsvpP2mpExtendedTunnelId=None, RouteKeyRsvpP2mpId=None, RouteKeyRsvpP2mpTunnelId=None, RouteKeySourceAddress=None, RouteKeyTunnelType=None, RouteKeyUpstreamLabel=None, RouteType=None, RsvpP2mpExtendedTunnelId=None, RsvpP2mpId=None, RsvpP2mpTunnelId=None, SourceAddress=None, SourceAs=None, TunnelType=None, UpstreamLabel=None):
        # type: (int, int, str, str, str, int, str, str, str, str, str, str, str, int, int, str, str, int, str, str, int, int, str, int, str, int) -> Ipv4MulticastVpn
        """Finds and retrieves ipv4MulticastVpn resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv4MulticastVpn resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv4MulticastVpn resources from the server.

        Args
        ----
        - AddressFamily (number): (read only) The address family identifier value.
        - AddressLength (number): (read only) The length of the address.
        - CMcastRouteType (str): The c-multicast route type.
        - GroupAddress (str): The IPv4 Multicast group address in the range of group addresses included in this Register message.
        - Neighbor (str): The neighbor address.
        - OpaqueLength (number): (read only) Indicates the opaque length.
        - OriginatingRouter (str): The originating router address.
        - RootAddress (str): (read only) Indicates the root address.
        - RouteDistinguisher (str): The route distinguisher for the route, for use with IPv4 multicast VPN address types.
        - RouteKeyGroupAddress (str): The key group address of the route.
        - RouteKeyOriginatingRouter (str): The key originating address of the router.
        - RouteKeyRouteDistinguisher (str): The key route distinguisher for the route, for use with IPv4 multicast VPN address types.
        - RouteKeyRsvpP2mpExtendedTunnelId (str): The key rsvp p2mp extended tunnel id for the route, for use with IPv4 multicast VPN address types.
        - RouteKeyRsvpP2mpId (number): The key rsvp p2mp id for the route, for use with IPv4 multicast VPN address types.
        - RouteKeyRsvpP2mpTunnelId (number): The key rsvp p2mp tunnel id for the route, for use with IPv4 multicast VPN address types.
        - RouteKeySourceAddress (str): The key source address for the route, for use with IPv4 multicast VPN address types.
        - RouteKeyTunnelType (str): The key tunnel type for the route, for use with IPv4 multicast VPN address types.
        - RouteKeyUpstreamLabel (number): The key upstream label for the route, for use with IPv4 multicast VPN address types.
        - RouteType (str): The route type.
        - RsvpP2mpExtendedTunnelId (str): The rsvp p2mp extended tunnel id.
        - RsvpP2mpId (number): The rsvp p2mp id.
        - RsvpP2mpTunnelId (number): The rsvp p2mp tunnel id.
        - SourceAddress (str): The source address.
        - SourceAs (number): The source AS number.
        - TunnelType (str): The tunnel type.
        - UpstreamLabel (number): The upstream label.

        Returns
        -------
        - self: This instance with matching ipv4MulticastVpn resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv4MulticastVpn data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv4MulticastVpn resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
