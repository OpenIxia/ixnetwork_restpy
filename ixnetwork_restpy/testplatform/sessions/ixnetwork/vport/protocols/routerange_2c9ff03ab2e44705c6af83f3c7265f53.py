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
    """If true enables the route range.
    The RouteRange class encapsulates a list of routeRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the RouteRange.find() method.
    The list can be managed by using the RouteRange.add() and RouteRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'routeRange'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'Mask': 'mask',
        'Metric': 'metric',
        'NetworkNumber': 'networkNumber',
        'NumberOfRoutes': 'numberOfRoutes',
        'Origin': 'origin',
        'Propagate': 'propagate',
        'Step': 'step',
    }

    def __init__(self, parent):
        super(RouteRange, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the router range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Mask(self):
        """
        Returns
        -------
        - number: The number of bits in the network mask.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mask'])
    @Mask.setter
    def Mask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mask'], value)

    @property
    def Metric(self):
        """
        Returns
        -------
        - number: The user-assigned routing metric associated with the route range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metric'])
    @Metric.setter
    def Metric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Metric'], value)

    @property
    def NetworkNumber(self):
        """
        Returns
        -------
        - str: The number of prefixes to be advertised.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkNumber'])
    @NetworkNumber.setter
    def NetworkNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkNumber'], value)

    @property
    def NumberOfRoutes(self):
        """
        Returns
        -------
        - number: The number of routes/network addresses to be created, based on the first route plus the mask.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfRoutes'])
    @NumberOfRoutes.setter
    def NumberOfRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfRoutes'], value)

    @property
    def Origin(self):
        """
        Returns
        -------
        - str(area | externalType1 | externalType2 | nssa | sameArea): The origin of the advertised route.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Origin'])
    @Origin.setter
    def Origin(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Origin'], value)

    @property
    def Propagate(self):
        """
        Returns
        -------
        - bool: Enables emulation of NSSA-LSA propagation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Propagate'])
    @Propagate.setter
    def Propagate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Propagate'], value)

    @property
    def Step(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step'])

    def update(self, Enabled=None, Mask=None, Metric=None, NetworkNumber=None, NumberOfRoutes=None, Origin=None, Propagate=None):
        """Updates routeRange resource on the server.

        Args
        ----
        - Enabled (bool): Enables the router range.
        - Mask (number): The number of bits in the network mask.
        - Metric (number): The user-assigned routing metric associated with the route range.
        - NetworkNumber (str): The number of prefixes to be advertised.
        - NumberOfRoutes (number): The number of routes/network addresses to be created, based on the first route plus the mask.
        - Origin (str(area | externalType1 | externalType2 | nssa | sameArea)): The origin of the advertised route.
        - Propagate (bool): Enables emulation of NSSA-LSA propagation.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, Mask=None, Metric=None, NetworkNumber=None, NumberOfRoutes=None, Origin=None, Propagate=None):
        """Adds a new routeRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Enables the router range.
        - Mask (number): The number of bits in the network mask.
        - Metric (number): The user-assigned routing metric associated with the route range.
        - NetworkNumber (str): The number of prefixes to be advertised.
        - NumberOfRoutes (number): The number of routes/network addresses to be created, based on the first route plus the mask.
        - Origin (str(area | externalType1 | externalType2 | nssa | sameArea)): The origin of the advertised route.
        - Propagate (bool): Enables emulation of NSSA-LSA propagation.

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

    def find(self, Enabled=None, Mask=None, Metric=None, NetworkNumber=None, NumberOfRoutes=None, Origin=None, Propagate=None, Step=None):
        """Finds and retrieves routeRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve routeRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all routeRange resources from the server.

        Args
        ----
        - Enabled (bool): Enables the router range.
        - Mask (number): The number of bits in the network mask.
        - Metric (number): The user-assigned routing metric associated with the route range.
        - NetworkNumber (str): The number of prefixes to be advertised.
        - NumberOfRoutes (number): The number of routes/network addresses to be created, based on the first route plus the mask.
        - Origin (str(area | externalType1 | externalType2 | nssa | sameArea)): The origin of the advertised route.
        - Propagate (bool): Enables emulation of NSSA-LSA propagation.
        - Step (number): 

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
