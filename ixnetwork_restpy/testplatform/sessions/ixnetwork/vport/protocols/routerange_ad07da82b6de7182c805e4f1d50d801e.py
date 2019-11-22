# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class RouteRange(Base):
    """A set of routes to be included in this OSPFv3 router.
    The RouteRange class encapsulates a list of routeRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the RouteRange.find() method.
    The list can be managed by the user by using the RouteRange.add() and RouteRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'routeRange'

    def __init__(self, parent):
        super(RouteRange, self).__init__(parent)

    @property
    def AddressFamily(self):
        """Indiacates the Address Family type - Unicast or Multicast

        Returns:
            str(unicast|multicast)
        """
        return self._get_attribute('addressFamily')
    @AddressFamily.setter
    def AddressFamily(self, value):
        self._set_attribute('addressFamily', value)

    @property
    def Enabled(self):
        """Enables the use of this route range for the simulated router.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def FirstRoute(self):
        """The first route in this range of routes/network addresses. Note: Multicast addresses are not supported in this route range implementation.

        Returns:
            str
        """
        return self._get_attribute('firstRoute')
    @FirstRoute.setter
    def FirstRoute(self, value):
        self._set_attribute('firstRoute', value)

    @property
    def IpType(self):
        """Indicates the IP Type - IPv4 or IPv6

        Returns:
            str(ipV4|ipV6)
        """
        return self._get_attribute('ipType')
    @IpType.setter
    def IpType(self, value):
        self._set_attribute('ipType', value)

    @property
    def Mask(self):
        """The number of bits in the prefixes to be advertised.

        Returns:
            number
        """
        return self._get_attribute('mask')
    @Mask.setter
    def Mask(self, value):
        self._set_attribute('mask', value)

    @property
    def Metric(self):
        """The user-assigned routing metric associated with the route range.

        Returns:
            number
        """
        return self._get_attribute('metric')
    @Metric.setter
    def Metric(self, value):
        self._set_attribute('metric', value)

    @property
    def NumberOfRoutes(self):
        """The number of routes/network addresses to be created, based on the first route plus the mask.

        Returns:
            number
        """
        return self._get_attribute('numberOfRoutes')
    @NumberOfRoutes.setter
    def NumberOfRoutes(self, value):
        self._set_attribute('numberOfRoutes', value)

    @property
    def Step(self):
        """The step value to use for incrementing the network mask.

        Returns:
            number
        """
        return self._get_attribute('step')
    @Step.setter
    def Step(self, value):
        self._set_attribute('step', value)

    @property
    def Type(self):
        """The type of route origin.

        Returns:
            str(anotherArea|asExternal1|asExternal2|sameArea)
        """
        return self._get_attribute('type')
    @Type.setter
    def Type(self, value):
        self._set_attribute('type', value)

    def update(self, AddressFamily=None, Enabled=None, FirstRoute=None, IpType=None, Mask=None, Metric=None, NumberOfRoutes=None, Step=None, Type=None):
        """Updates a child instance of routeRange on the server.

        Args:
            AddressFamily (str(unicast|multicast)): Indiacates the Address Family type - Unicast or Multicast
            Enabled (bool): Enables the use of this route range for the simulated router.
            FirstRoute (str): The first route in this range of routes/network addresses. Note: Multicast addresses are not supported in this route range implementation.
            IpType (str(ipV4|ipV6)): Indicates the IP Type - IPv4 or IPv6
            Mask (number): The number of bits in the prefixes to be advertised.
            Metric (number): The user-assigned routing metric associated with the route range.
            NumberOfRoutes (number): The number of routes/network addresses to be created, based on the first route plus the mask.
            Step (number): The step value to use for incrementing the network mask.
            Type (str(anotherArea|asExternal1|asExternal2|sameArea)): The type of route origin.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AddressFamily=None, Enabled=None, FirstRoute=None, IpType=None, Mask=None, Metric=None, NumberOfRoutes=None, Step=None, Type=None):
        """Adds a new routeRange node on the server and retrieves it in this instance.

        Args:
            AddressFamily (str(unicast|multicast)): Indiacates the Address Family type - Unicast or Multicast
            Enabled (bool): Enables the use of this route range for the simulated router.
            FirstRoute (str): The first route in this range of routes/network addresses. Note: Multicast addresses are not supported in this route range implementation.
            IpType (str(ipV4|ipV6)): Indicates the IP Type - IPv4 or IPv6
            Mask (number): The number of bits in the prefixes to be advertised.
            Metric (number): The user-assigned routing metric associated with the route range.
            NumberOfRoutes (number): The number of routes/network addresses to be created, based on the first route plus the mask.
            Step (number): The step value to use for incrementing the network mask.
            Type (str(anotherArea|asExternal1|asExternal2|sameArea)): The type of route origin.

        Returns:
            self: This instance with all currently retrieved routeRange data using find and the newly added routeRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the routeRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AddressFamily=None, Enabled=None, FirstRoute=None, IpType=None, Mask=None, Metric=None, NumberOfRoutes=None, Step=None, Type=None):
        """Finds and retrieves routeRange data from the server.

        All named parameters support regex and can be used to selectively retrieve routeRange data from the server.
        By default the find method takes no parameters and will retrieve all routeRange data from the server.

        Args:
            AddressFamily (str(unicast|multicast)): Indiacates the Address Family type - Unicast or Multicast
            Enabled (bool): Enables the use of this route range for the simulated router.
            FirstRoute (str): The first route in this range of routes/network addresses. Note: Multicast addresses are not supported in this route range implementation.
            IpType (str(ipV4|ipV6)): Indicates the IP Type - IPv4 or IPv6
            Mask (number): The number of bits in the prefixes to be advertised.
            Metric (number): The user-assigned routing metric associated with the route range.
            NumberOfRoutes (number): The number of routes/network addresses to be created, based on the first route plus the mask.
            Step (number): The step value to use for incrementing the network mask.
            Type (str(anotherArea|asExternal1|asExternal2|sameArea)): The type of route origin.

        Returns:
            self: This instance with matching routeRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of routeRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the routeRange data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
