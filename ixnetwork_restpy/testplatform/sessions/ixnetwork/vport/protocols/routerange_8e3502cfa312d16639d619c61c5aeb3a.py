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


class RouteRange(Base):
    """A set of routes to be included in the router interface.
    The RouteRange class encapsulates a list of routeRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the RouteRange.find() method.
    The list can be managed by using the RouteRange.add() and RouteRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'routeRange'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'FirstRoute': 'firstRoute',
        'MaskWidth': 'maskWidth',
        'Metric': 'metric',
        'NextHop': 'nextHop',
        'NoOfRoutes': 'noOfRoutes',
        'RouteTag': 'routeTag',
    }

    def __init__(self, parent):
        super(RouteRange, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of this route range for the simulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def FirstRoute(self):
        """
        Returns
        -------
        - str: The first network address to be used in creating this route range. Note: Multicast and loopback addresses are not supported in this IPv4 route range implementation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstRoute'])
    @FirstRoute.setter
    def FirstRoute(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstRoute'], value)

    @property
    def MaskWidth(self):
        """
        Returns
        -------
        - number: The network mask to be applied to the networkIpAddress to yield the non-host part of the address. A value of 0 means there is no subnet address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaskWidth'])
    @MaskWidth.setter
    def MaskWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaskWidth'], value)

    @property
    def Metric(self):
        """
        Returns
        -------
        - number: The total metric cost for these routes. The valid range is from 1 to 16 (inclusive). A value of 16 means that the destination is not reachable, and that route will be removed from service.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metric'])
    @Metric.setter
    def Metric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Metric'], value)

    @property
    def NextHop(self):
        """
        Returns
        -------
        - str: The immediate next hop IP address on the way to the destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHop'])
    @NextHop.setter
    def NextHop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHop'], value)

    @property
    def NoOfRoutes(self):
        """
        Returns
        -------
        - number: The number of networks to be generated for this route range, based on the network address plus the network mask.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfRoutes'])
    @NoOfRoutes.setter
    def NoOfRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfRoutes'], value)

    @property
    def RouteTag(self):
        """
        Returns
        -------
        - number: An arbitrary value associated with the routes in this range. It is used to provide a means for distinguishing internal versus external RIP routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteTag'])
    @RouteTag.setter
    def RouteTag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteTag'], value)

    def update(self, Enabled=None, FirstRoute=None, MaskWidth=None, Metric=None, NextHop=None, NoOfRoutes=None, RouteTag=None):
        """Updates routeRange resource on the server.

        Args
        ----
        - Enabled (bool): Enables the use of this route range for the simulated router.
        - FirstRoute (str): The first network address to be used in creating this route range. Note: Multicast and loopback addresses are not supported in this IPv4 route range implementation.
        - MaskWidth (number): The network mask to be applied to the networkIpAddress to yield the non-host part of the address. A value of 0 means there is no subnet address.
        - Metric (number): The total metric cost for these routes. The valid range is from 1 to 16 (inclusive). A value of 16 means that the destination is not reachable, and that route will be removed from service.
        - NextHop (str): The immediate next hop IP address on the way to the destination address.
        - NoOfRoutes (number): The number of networks to be generated for this route range, based on the network address plus the network mask.
        - RouteTag (number): An arbitrary value associated with the routes in this range. It is used to provide a means for distinguishing internal versus external RIP routes.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, FirstRoute=None, MaskWidth=None, Metric=None, NextHop=None, NoOfRoutes=None, RouteTag=None):
        """Adds a new routeRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Enables the use of this route range for the simulated router.
        - FirstRoute (str): The first network address to be used in creating this route range. Note: Multicast and loopback addresses are not supported in this IPv4 route range implementation.
        - MaskWidth (number): The network mask to be applied to the networkIpAddress to yield the non-host part of the address. A value of 0 means there is no subnet address.
        - Metric (number): The total metric cost for these routes. The valid range is from 1 to 16 (inclusive). A value of 16 means that the destination is not reachable, and that route will be removed from service.
        - NextHop (str): The immediate next hop IP address on the way to the destination address.
        - NoOfRoutes (number): The number of networks to be generated for this route range, based on the network address plus the network mask.
        - RouteTag (number): An arbitrary value associated with the routes in this range. It is used to provide a means for distinguishing internal versus external RIP routes.

        Returns
        -------
        - self: This instance with all currently retrieved routeRange resources using find and the newly added routeRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained routeRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, FirstRoute=None, MaskWidth=None, Metric=None, NextHop=None, NoOfRoutes=None, RouteTag=None):
        """Finds and retrieves routeRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve routeRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all routeRange resources from the server.

        Args
        ----
        - Enabled (bool): Enables the use of this route range for the simulated router.
        - FirstRoute (str): The first network address to be used in creating this route range. Note: Multicast and loopback addresses are not supported in this IPv4 route range implementation.
        - MaskWidth (number): The network mask to be applied to the networkIpAddress to yield the non-host part of the address. A value of 0 means there is no subnet address.
        - Metric (number): The total metric cost for these routes. The valid range is from 1 to 16 (inclusive). A value of 16 means that the destination is not reachable, and that route will be removed from service.
        - NextHop (str): The immediate next hop IP address on the way to the destination address.
        - NoOfRoutes (number): The number of networks to be generated for this route range, based on the network address plus the network mask.
        - RouteTag (number): An arbitrary value associated with the routes in this range. It is used to provide a means for distinguishing internal versus external RIP routes.

        Returns
        -------
        - self: This instance with matching routeRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of routeRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the routeRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
