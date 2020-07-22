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


class RouteImportOptions(Base):
    """This object holds the available options for the imported routes.
    The RouteImportOptions class encapsulates a list of routeImportOptions resources that are managed by the user.
    A list of resources can be retrieved from the server using the RouteImportOptions.find() method.
    The list can be managed by using the RouteImportOptions.add() and RouteImportOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'routeImportOptions'
    _SDM_ATT_MAP = {
        'AdverstiseBestRoutes': 'adverstiseBestRoutes',
        'NextHopAsIs': 'nextHopAsIs',
        'NumberOfRoutesPerBlock': 'numberOfRoutesPerBlock',
        'RouteFileType': 'routeFileType',
        'SendMultiExitDiscValue': 'sendMultiExitDiscValue',
    }

    def __init__(self, parent):
        super(RouteImportOptions, self).__init__(parent)

    @property
    def AdverstiseBestRoutes(self):
        """
        Returns
        -------
        - bool: If checked, only the best routes are imbibed and advertised. The sub-optimal routes are ignored.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdverstiseBestRoutes'])
    @AdverstiseBestRoutes.setter
    def AdverstiseBestRoutes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdverstiseBestRoutes'], value)

    @property
    def NextHopAsIs(self):
        """
        Returns
        -------
        - bool: If true, it takes the next Hop AsIs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopAsIs'])
    @NextHopAsIs.setter
    def NextHopAsIs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NextHopAsIs'], value)

    @property
    def NumberOfRoutesPerBlock(self):
        """
        Returns
        -------
        - number: Represents the maximum number of routes that can be forwared in a block.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfRoutesPerBlock'])
    @NumberOfRoutesPerBlock.setter
    def NumberOfRoutesPerBlock(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfRoutesPerBlock'], value)

    @property
    def RouteFileType(self):
        """
        Returns
        -------
        - str: The route file type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteFileType'])
    @RouteFileType.setter
    def RouteFileType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouteFileType'], value)

    @property
    def SendMultiExitDiscValue(self):
        """
        Returns
        -------
        - bool: If enabled, the BGP router sends the MED value of the attribute.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendMultiExitDiscValue'])
    @SendMultiExitDiscValue.setter
    def SendMultiExitDiscValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendMultiExitDiscValue'], value)

    def update(self, AdverstiseBestRoutes=None, NextHopAsIs=None, NumberOfRoutesPerBlock=None, RouteFileType=None, SendMultiExitDiscValue=None):
        """Updates routeImportOptions resource on the server.

        Args
        ----
        - AdverstiseBestRoutes (bool): If checked, only the best routes are imbibed and advertised. The sub-optimal routes are ignored.
        - NextHopAsIs (bool): If true, it takes the next Hop AsIs.
        - NumberOfRoutesPerBlock (number): Represents the maximum number of routes that can be forwared in a block.
        - RouteFileType (str): The route file type.
        - SendMultiExitDiscValue (bool): If enabled, the BGP router sends the MED value of the attribute.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdverstiseBestRoutes=None, NextHopAsIs=None, NumberOfRoutesPerBlock=None, RouteFileType=None, SendMultiExitDiscValue=None):
        """Adds a new routeImportOptions resource on the server and adds it to the container.

        Args
        ----
        - AdverstiseBestRoutes (bool): If checked, only the best routes are imbibed and advertised. The sub-optimal routes are ignored.
        - NextHopAsIs (bool): If true, it takes the next Hop AsIs.
        - NumberOfRoutesPerBlock (number): Represents the maximum number of routes that can be forwared in a block.
        - RouteFileType (str): The route file type.
        - SendMultiExitDiscValue (bool): If enabled, the BGP router sends the MED value of the attribute.

        Returns
        -------
        - self: This instance with all currently retrieved routeImportOptions resources using find and the newly added routeImportOptions resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained routeImportOptions resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdverstiseBestRoutes=None, NextHopAsIs=None, NumberOfRoutesPerBlock=None, RouteFileType=None, SendMultiExitDiscValue=None):
        """Finds and retrieves routeImportOptions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve routeImportOptions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all routeImportOptions resources from the server.

        Args
        ----
        - AdverstiseBestRoutes (bool): If checked, only the best routes are imbibed and advertised. The sub-optimal routes are ignored.
        - NextHopAsIs (bool): If true, it takes the next Hop AsIs.
        - NumberOfRoutesPerBlock (number): Represents the maximum number of routes that can be forwared in a block.
        - RouteFileType (str): The route file type.
        - SendMultiExitDiscValue (bool): If enabled, the BGP router sends the MED value of the attribute.

        Returns
        -------
        - self: This instance with matching routeImportOptions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of routeImportOptions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the routeImportOptions resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetSupportedBGPRouteFileTypes(self):
        """Executes the getSupportedBGPRouteFileTypes operation on the server.

        This function allows to Get supported BGP router.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('getSupportedBGPRouteFileTypes', payload=payload, response_object=None)

    def ImportOpaqueRouteRangeFromFile(self, *args, **kwargs):
        """Executes the importOpaqueRouteRangeFromFile operation on the server.

        This function allows to import opaque route range from file.

        importOpaqueRouteRangeFromFile(Arg2=href)
        -----------------------------------------
        - Arg2 (obj(ixnetwork_restpy.files.Files)): NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('importOpaqueRouteRangeFromFile', payload=payload, response_object=None)
