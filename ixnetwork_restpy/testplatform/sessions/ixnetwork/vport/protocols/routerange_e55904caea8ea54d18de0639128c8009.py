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
    """This object represents a set of routes.
    The RouteRange class encapsulates a list of routeRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the RouteRange.find() method.
    The list can be managed by using the RouteRange.add() and RouteRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'routeRange'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'FirstRoute': 'firstRoute',
        'IsRedistributed': 'isRedistributed',
        'MaskWidth': 'maskWidth',
        'Metric': 'metric',
        'NumberOfRoutes': 'numberOfRoutes',
        'RouteOrigin': 'routeOrigin',
        'Step': 'step',
        'Type': 'type',
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
        - str: The first route of the route range, in IPv4 dotted decimal format. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstRoute'])
    @FirstRoute.setter
    def FirstRoute(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstRoute'], value)

    @property
    def IsRedistributed(self):
        """
        Returns
        -------
        - bool: Sets the Up/Down (Redistribution) bit defined for TLVs 128 and 130 by RFC 2966. It is used for domain-wide advertisement of prefix information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRedistributed'])
    @IsRedistributed.setter
    def IsRedistributed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsRedistributed'], value)

    @property
    def MaskWidth(self):
        """
        Returns
        -------
        - number: The network mask width for the route range (in bits). The valid range is from 0 to 32 bits. (default = 24)
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
        - number: The user-defined metric associated with this route range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metric'])
    @Metric.setter
    def Metric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Metric'], value)

    @property
    def NumberOfRoutes(self):
        """
        Returns
        -------
        - number: The number of routes to be generated for this route range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfRoutes'])
    @NumberOfRoutes.setter
    def NumberOfRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfRoutes'], value)

    @property
    def RouteOrigin(self):
        """
        Returns
        -------
        - bool: The origin of the advertised route - internal or external to the ISIS area.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteOrigin'])
    @RouteOrigin.setter
    def RouteOrigin(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteOrigin'], value)

    @property
    def Step(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step'])

    @property
    def Type(self):
        """
        Returns
        -------
        - str(ipAny | ipv4 | ipv6): The IP type of the route range for the ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    def update(self, Enabled=None, FirstRoute=None, IsRedistributed=None, MaskWidth=None, Metric=None, NumberOfRoutes=None, RouteOrigin=None, Type=None):
        """Updates routeRange resource on the server.

        Args
        ----
        - Enabled (bool): Enables the use of this route range for the simulated router.
        - FirstRoute (str): The first route of the route range, in IPv4 dotted decimal format. (default = 0.0.0.0)
        - IsRedistributed (bool): Sets the Up/Down (Redistribution) bit defined for TLVs 128 and 130 by RFC 2966. It is used for domain-wide advertisement of prefix information.
        - MaskWidth (number): The network mask width for the route range (in bits). The valid range is from 0 to 32 bits. (default = 24)
        - Metric (number): The user-defined metric associated with this route range.
        - NumberOfRoutes (number): The number of routes to be generated for this route range.
        - RouteOrigin (bool): The origin of the advertised route - internal or external to the ISIS area.
        - Type (str(ipAny | ipv4 | ipv6)): The IP type of the route range for the ISIS router.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, FirstRoute=None, IsRedistributed=None, MaskWidth=None, Metric=None, NumberOfRoutes=None, RouteOrigin=None, Type=None):
        """Adds a new routeRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Enables the use of this route range for the simulated router.
        - FirstRoute (str): The first route of the route range, in IPv4 dotted decimal format. (default = 0.0.0.0)
        - IsRedistributed (bool): Sets the Up/Down (Redistribution) bit defined for TLVs 128 and 130 by RFC 2966. It is used for domain-wide advertisement of prefix information.
        - MaskWidth (number): The network mask width for the route range (in bits). The valid range is from 0 to 32 bits. (default = 24)
        - Metric (number): The user-defined metric associated with this route range.
        - NumberOfRoutes (number): The number of routes to be generated for this route range.
        - RouteOrigin (bool): The origin of the advertised route - internal or external to the ISIS area.
        - Type (str(ipAny | ipv4 | ipv6)): The IP type of the route range for the ISIS router.

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

    def find(self, Enabled=None, FirstRoute=None, IsRedistributed=None, MaskWidth=None, Metric=None, NumberOfRoutes=None, RouteOrigin=None, Step=None, Type=None):
        """Finds and retrieves routeRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve routeRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all routeRange resources from the server.

        Args
        ----
        - Enabled (bool): Enables the use of this route range for the simulated router.
        - FirstRoute (str): The first route of the route range, in IPv4 dotted decimal format. (default = 0.0.0.0)
        - IsRedistributed (bool): Sets the Up/Down (Redistribution) bit defined for TLVs 128 and 130 by RFC 2966. It is used for domain-wide advertisement of prefix information.
        - MaskWidth (number): The network mask width for the route range (in bits). The valid range is from 0 to 32 bits. (default = 24)
        - Metric (number): The user-defined metric associated with this route range.
        - NumberOfRoutes (number): The number of routes to be generated for this route range.
        - RouteOrigin (bool): The origin of the advertised route - internal or external to the ISIS area.
        - Step (number): 
        - Type (str(ipAny | ipv4 | ipv6)): The IP type of the route range for the ISIS router.

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
