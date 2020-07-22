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


class MulticastReceiverSite(Base):
    """Configures the values for the multicast receiver site.
    The MulticastReceiverSite class encapsulates a list of multicastReceiverSite resources that are managed by the user.
    A list of resources can be retrieved from the server using the MulticastReceiverSite.find() method.
    The list can be managed by using the MulticastReceiverSite.add() and MulticastReceiverSite.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'multicastReceiverSite'
    _SDM_ATT_MAP = {
        'AddressFamilyType': 'addressFamilyType',
        'CMcastRouteType': 'cMcastRouteType',
        'Enabled': 'enabled',
        'GroupAddressCount': 'groupAddressCount',
        'GroupMaskWidth': 'groupMaskWidth',
        'SendTriggeredCmulticastRoute': 'sendTriggeredCmulticastRoute',
        'SourceAddressCount': 'sourceAddressCount',
        'SourceGroupMapping': 'sourceGroupMapping',
        'SourceMaskWidth': 'sourceMaskWidth',
        'StartGroupAddress': 'startGroupAddress',
        'StartSourceAddress': 'startSourceAddress',
        'SupportLeafAdRoutesSending': 'supportLeafAdRoutesSending',
    }

    def __init__(self, parent):
        super(MulticastReceiverSite, self).__init__(parent)

    @property
    def AddressFamilyType(self):
        """
        Returns
        -------
        - str(addressFamilyIpv4 | addressFamilyIpv6): Indicates the IPv4/IPv6 interface id of the router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressFamilyType'])
    @AddressFamilyType.setter
    def AddressFamilyType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddressFamilyType'], value)

    @property
    def CMcastRouteType(self):
        """
        Returns
        -------
        - str(sourceTreeJoin | sharedTreeJoin): The C-Multicast Route Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CMcastRouteType'])
    @CMcastRouteType.setter
    def CMcastRouteType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CMcastRouteType'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables use of the multicast Sender site.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def GroupAddressCount(self):
        """
        Returns
        -------
        - number: The number of group addresses to be included in the Register message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupAddressCount'])
    @GroupAddressCount.setter
    def GroupAddressCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupAddressCount'], value)

    @property
    def GroupMaskWidth(self):
        """
        Returns
        -------
        - number: The number of bits in the network mask used with the Group Address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupMaskWidth'])
    @GroupMaskWidth.setter
    def GroupMaskWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupMaskWidth'], value)

    @property
    def SendTriggeredCmulticastRoute(self):
        """
        Returns
        -------
        - bool: This helps to send Source Tree Join C-Multicast route after receiving Source Active A-D route. This is also required by Shared Tree Join C-Multicast route to send Source Tree Join after receiving Source Active A-D Route.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendTriggeredCmulticastRoute'])
    @SendTriggeredCmulticastRoute.setter
    def SendTriggeredCmulticastRoute(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendTriggeredCmulticastRoute'], value)

    @property
    def SourceAddressCount(self):
        """
        Returns
        -------
        - number: The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values for the Source Address and the Source Mask Width. the default value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAddressCount'])
    @SourceAddressCount.setter
    def SourceAddressCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceAddressCount'], value)

    @property
    def SourceGroupMapping(self):
        """
        Returns
        -------
        - str(fullyMeshed | oneToOne): Indicates the source group mapping.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceGroupMapping'])
    @SourceGroupMapping.setter
    def SourceGroupMapping(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceGroupMapping'], value)

    @property
    def SourceMaskWidth(self):
        """
        Returns
        -------
        - number: The number of bits in the mask applied to the Source Address. (The masked bits in the Source Address form the address prefix.)The default value is 32. The valid range is 1 to 128, depending on address family type.Used for (S,G) Type and (S,G, rpt) only.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceMaskWidth'])
    @SourceMaskWidth.setter
    def SourceMaskWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceMaskWidth'], value)

    @property
    def StartGroupAddress(self):
        """
        Returns
        -------
        - str: The first IPv4 or IPv6 Multicast group address in the range of group addresses included in this Register message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartGroupAddress'])
    @StartGroupAddress.setter
    def StartGroupAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartGroupAddress'], value)

    @property
    def StartSourceAddress(self):
        """
        Returns
        -------
        - str: The first IPv4 or IPv6 source address to be included in this Register message.(IPv4 Multicast addresses are not valid for sources.).
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartSourceAddress'])
    @StartSourceAddress.setter
    def StartSourceAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartSourceAddress'], value)

    @property
    def SupportLeafAdRoutesSending(self):
        """
        Returns
        -------
        - bool: If true, helps IXIA to send Leaf A-D Route on receiving a S-PMSI A-D Route with the Leaf Information Required flag set. If false, IXIA shall not send the Leaf A-D Route even if such Update message is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportLeafAdRoutesSending'])
    @SupportLeafAdRoutesSending.setter
    def SupportLeafAdRoutesSending(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportLeafAdRoutesSending'], value)

    def update(self, AddressFamilyType=None, CMcastRouteType=None, Enabled=None, GroupAddressCount=None, GroupMaskWidth=None, SendTriggeredCmulticastRoute=None, SourceAddressCount=None, SourceGroupMapping=None, SourceMaskWidth=None, StartGroupAddress=None, StartSourceAddress=None, SupportLeafAdRoutesSending=None):
        """Updates multicastReceiverSite resource on the server.

        Args
        ----
        - AddressFamilyType (str(addressFamilyIpv4 | addressFamilyIpv6)): Indicates the IPv4/IPv6 interface id of the router.
        - CMcastRouteType (str(sourceTreeJoin | sharedTreeJoin)): The C-Multicast Route Type.
        - Enabled (bool): Enables or disables use of the multicast Sender site.
        - GroupAddressCount (number): The number of group addresses to be included in the Register message.
        - GroupMaskWidth (number): The number of bits in the network mask used with the Group Address.
        - SendTriggeredCmulticastRoute (bool): This helps to send Source Tree Join C-Multicast route after receiving Source Active A-D route. This is also required by Shared Tree Join C-Multicast route to send Source Tree Join after receiving Source Active A-D Route.
        - SourceAddressCount (number): The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values for the Source Address and the Source Mask Width. the default value is 0.
        - SourceGroupMapping (str(fullyMeshed | oneToOne)): Indicates the source group mapping.
        - SourceMaskWidth (number): The number of bits in the mask applied to the Source Address. (The masked bits in the Source Address form the address prefix.)The default value is 32. The valid range is 1 to 128, depending on address family type.Used for (S,G) Type and (S,G, rpt) only.
        - StartGroupAddress (str): The first IPv4 or IPv6 Multicast group address in the range of group addresses included in this Register message.
        - StartSourceAddress (str): The first IPv4 or IPv6 source address to be included in this Register message.(IPv4 Multicast addresses are not valid for sources.).
        - SupportLeafAdRoutesSending (bool): If true, helps IXIA to send Leaf A-D Route on receiving a S-PMSI A-D Route with the Leaf Information Required flag set. If false, IXIA shall not send the Leaf A-D Route even if such Update message is received.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AddressFamilyType=None, CMcastRouteType=None, Enabled=None, GroupAddressCount=None, GroupMaskWidth=None, SendTriggeredCmulticastRoute=None, SourceAddressCount=None, SourceGroupMapping=None, SourceMaskWidth=None, StartGroupAddress=None, StartSourceAddress=None, SupportLeafAdRoutesSending=None):
        """Adds a new multicastReceiverSite resource on the server and adds it to the container.

        Args
        ----
        - AddressFamilyType (str(addressFamilyIpv4 | addressFamilyIpv6)): Indicates the IPv4/IPv6 interface id of the router.
        - CMcastRouteType (str(sourceTreeJoin | sharedTreeJoin)): The C-Multicast Route Type.
        - Enabled (bool): Enables or disables use of the multicast Sender site.
        - GroupAddressCount (number): The number of group addresses to be included in the Register message.
        - GroupMaskWidth (number): The number of bits in the network mask used with the Group Address.
        - SendTriggeredCmulticastRoute (bool): This helps to send Source Tree Join C-Multicast route after receiving Source Active A-D route. This is also required by Shared Tree Join C-Multicast route to send Source Tree Join after receiving Source Active A-D Route.
        - SourceAddressCount (number): The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values for the Source Address and the Source Mask Width. the default value is 0.
        - SourceGroupMapping (str(fullyMeshed | oneToOne)): Indicates the source group mapping.
        - SourceMaskWidth (number): The number of bits in the mask applied to the Source Address. (The masked bits in the Source Address form the address prefix.)The default value is 32. The valid range is 1 to 128, depending on address family type.Used for (S,G) Type and (S,G, rpt) only.
        - StartGroupAddress (str): The first IPv4 or IPv6 Multicast group address in the range of group addresses included in this Register message.
        - StartSourceAddress (str): The first IPv4 or IPv6 source address to be included in this Register message.(IPv4 Multicast addresses are not valid for sources.).
        - SupportLeafAdRoutesSending (bool): If true, helps IXIA to send Leaf A-D Route on receiving a S-PMSI A-D Route with the Leaf Information Required flag set. If false, IXIA shall not send the Leaf A-D Route even if such Update message is received.

        Returns
        -------
        - self: This instance with all currently retrieved multicastReceiverSite resources using find and the newly added multicastReceiverSite resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained multicastReceiverSite resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AddressFamilyType=None, CMcastRouteType=None, Enabled=None, GroupAddressCount=None, GroupMaskWidth=None, SendTriggeredCmulticastRoute=None, SourceAddressCount=None, SourceGroupMapping=None, SourceMaskWidth=None, StartGroupAddress=None, StartSourceAddress=None, SupportLeafAdRoutesSending=None):
        """Finds and retrieves multicastReceiverSite resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve multicastReceiverSite resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all multicastReceiverSite resources from the server.

        Args
        ----
        - AddressFamilyType (str(addressFamilyIpv4 | addressFamilyIpv6)): Indicates the IPv4/IPv6 interface id of the router.
        - CMcastRouteType (str(sourceTreeJoin | sharedTreeJoin)): The C-Multicast Route Type.
        - Enabled (bool): Enables or disables use of the multicast Sender site.
        - GroupAddressCount (number): The number of group addresses to be included in the Register message.
        - GroupMaskWidth (number): The number of bits in the network mask used with the Group Address.
        - SendTriggeredCmulticastRoute (bool): This helps to send Source Tree Join C-Multicast route after receiving Source Active A-D route. This is also required by Shared Tree Join C-Multicast route to send Source Tree Join after receiving Source Active A-D Route.
        - SourceAddressCount (number): The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values for the Source Address and the Source Mask Width. the default value is 0.
        - SourceGroupMapping (str(fullyMeshed | oneToOne)): Indicates the source group mapping.
        - SourceMaskWidth (number): The number of bits in the mask applied to the Source Address. (The masked bits in the Source Address form the address prefix.)The default value is 32. The valid range is 1 to 128, depending on address family type.Used for (S,G) Type and (S,G, rpt) only.
        - StartGroupAddress (str): The first IPv4 or IPv6 Multicast group address in the range of group addresses included in this Register message.
        - StartSourceAddress (str): The first IPv4 or IPv6 source address to be included in this Register message.(IPv4 Multicast addresses are not valid for sources.).
        - SupportLeafAdRoutesSending (bool): If true, helps IXIA to send Leaf A-D Route on receiving a S-PMSI A-D Route with the Leaf Information Required flag set. If false, IXIA shall not send the Leaf A-D Route even if such Update message is received.

        Returns
        -------
        - self: This instance with matching multicastReceiverSite resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of multicastReceiverSite data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the multicastReceiverSite resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
