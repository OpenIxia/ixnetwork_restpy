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
    """A set of routes to be included in the RIPng router.
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
        'NumberOfRoute': 'numberOfRoute',
        'RouteTag': 'routeTag',
        'Step': 'step',
    }

    def __init__(self, parent):
        super(RouteRange, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the selected route range.
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
        - str: The IPv6 address of the first route/network to be generated for this RIPng route range.
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
        - number: The network mask to be used when generating routes This value indicates the number of bits, counting from the MSB (at the left end), that will comprise the network part of the IPv6 address. The remainder of the address will indicate the host part of the address. The default mask width is 64 bits.
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
        - number: The current metric cost to reach the destination. A value between 0 and 15. A value of 16 indicates that the destination is unreachable. (The RIPng Interface Metric is added to this value.)
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
        - str: (For use in the Next Hop RTE.)The link-local IPv6 address of the next hop router. The value 0:0:0:0:0:0:0:0 indicates that the next hop router should be the originator of the RIPng route advertisement. (This router is the Next Hop.)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHop'])
    @NextHop.setter
    def NextHop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHop'], value)

    @property
    def NumberOfRoute(self):
        """
        Returns
        -------
        - number: The total number of routes to be included in this route range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfRoute'])
    @NumberOfRoute.setter
    def NumberOfRoute(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfRoute'], value)

    @property
    def RouteTag(self):
        """
        Returns
        -------
        - number: A route attribute advertised with a route: internal vs. external. For external routes, the route tag can be the AS from which the routes were learned or an arbitrary, assigned integer value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteTag'])
    @RouteTag.setter
    def RouteTag(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteTag'], value)

    @property
    def Step(self):
        """
        Returns
        -------
        - number: The increment step value to be used when creating additional routes/network addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step'])
    @Step.setter
    def Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step'], value)

    def update(self, Enabled=None, FirstRoute=None, MaskWidth=None, Metric=None, NextHop=None, NumberOfRoute=None, RouteTag=None, Step=None):
        """Updates routeRange resource on the server.

        Args
        ----
        - Enabled (bool): Enables the selected route range.
        - FirstRoute (str): The IPv6 address of the first route/network to be generated for this RIPng route range.
        - MaskWidth (number): The network mask to be used when generating routes This value indicates the number of bits, counting from the MSB (at the left end), that will comprise the network part of the IPv6 address. The remainder of the address will indicate the host part of the address. The default mask width is 64 bits.
        - Metric (number): The current metric cost to reach the destination. A value between 0 and 15. A value of 16 indicates that the destination is unreachable. (The RIPng Interface Metric is added to this value.)
        - NextHop (str): (For use in the Next Hop RTE.)The link-local IPv6 address of the next hop router. The value 0:0:0:0:0:0:0:0 indicates that the next hop router should be the originator of the RIPng route advertisement. (This router is the Next Hop.)
        - NumberOfRoute (number): The total number of routes to be included in this route range.
        - RouteTag (number): A route attribute advertised with a route: internal vs. external. For external routes, the route tag can be the AS from which the routes were learned or an arbitrary, assigned integer value.
        - Step (number): The increment step value to be used when creating additional routes/network addresses.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, FirstRoute=None, MaskWidth=None, Metric=None, NextHop=None, NumberOfRoute=None, RouteTag=None, Step=None):
        """Adds a new routeRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Enables the selected route range.
        - FirstRoute (str): The IPv6 address of the first route/network to be generated for this RIPng route range.
        - MaskWidth (number): The network mask to be used when generating routes This value indicates the number of bits, counting from the MSB (at the left end), that will comprise the network part of the IPv6 address. The remainder of the address will indicate the host part of the address. The default mask width is 64 bits.
        - Metric (number): The current metric cost to reach the destination. A value between 0 and 15. A value of 16 indicates that the destination is unreachable. (The RIPng Interface Metric is added to this value.)
        - NextHop (str): (For use in the Next Hop RTE.)The link-local IPv6 address of the next hop router. The value 0:0:0:0:0:0:0:0 indicates that the next hop router should be the originator of the RIPng route advertisement. (This router is the Next Hop.)
        - NumberOfRoute (number): The total number of routes to be included in this route range.
        - RouteTag (number): A route attribute advertised with a route: internal vs. external. For external routes, the route tag can be the AS from which the routes were learned or an arbitrary, assigned integer value.
        - Step (number): The increment step value to be used when creating additional routes/network addresses.

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

    def find(self, Enabled=None, FirstRoute=None, MaskWidth=None, Metric=None, NextHop=None, NumberOfRoute=None, RouteTag=None, Step=None):
        """Finds and retrieves routeRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve routeRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all routeRange resources from the server.

        Args
        ----
        - Enabled (bool): Enables the selected route range.
        - FirstRoute (str): The IPv6 address of the first route/network to be generated for this RIPng route range.
        - MaskWidth (number): The network mask to be used when generating routes This value indicates the number of bits, counting from the MSB (at the left end), that will comprise the network part of the IPv6 address. The remainder of the address will indicate the host part of the address. The default mask width is 64 bits.
        - Metric (number): The current metric cost to reach the destination. A value between 0 and 15. A value of 16 indicates that the destination is unreachable. (The RIPng Interface Metric is added to this value.)
        - NextHop (str): (For use in the Next Hop RTE.)The link-local IPv6 address of the next hop router. The value 0:0:0:0:0:0:0:0 indicates that the next hop router should be the originator of the RIPng route advertisement. (This router is the Next Hop.)
        - NumberOfRoute (number): The total number of routes to be included in this route range.
        - RouteTag (number): A route attribute advertised with a route: internal vs. external. For external routes, the route tag can be the AS from which the routes were learned or an arbitrary, assigned integer value.
        - Step (number): The increment step value to be used when creating additional routes/network addresses.

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
