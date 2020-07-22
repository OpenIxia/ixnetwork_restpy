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


class UserDefinedAfiSafiRoutes(Base):
    """Configures the user defined afi/safi routes.
    The UserDefinedAfiSafiRoutes class encapsulates a list of userDefinedAfiSafiRoutes resources that are managed by the user.
    A list of resources can be retrieved from the server using the UserDefinedAfiSafiRoutes.find() method.
    The list can be managed by using the UserDefinedAfiSafiRoutes.add() and UserDefinedAfiSafiRoutes.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'userDefinedAfiSafiRoutes'
    _SDM_ATT_MAP = {
        'Data': 'data',
        'Enabled': 'enabled',
        'Length': 'length',
    }

    def __init__(self, parent):
        super(UserDefinedAfiSafiRoutes, self).__init__(parent)

    @property
    def Data(self):
        """
        Returns
        -------
        - str: Data to be transmitted for AFI/SAFI, and regular enable-disable.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Data'])
    @Data.setter
    def Data(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Data'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the user-defined afi/safi is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Length(self):
        """
        Returns
        -------
        - number: The data is padded up to length with left alignment otherwise chopped till length.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Length'])
    @Length.setter
    def Length(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Length'], value)

    def update(self, Data=None, Enabled=None, Length=None):
        """Updates userDefinedAfiSafiRoutes resource on the server.

        Args
        ----
        - Data (str): Data to be transmitted for AFI/SAFI, and regular enable-disable.
        - Enabled (bool): If true, the user-defined afi/safi is enabled.
        - Length (number): The data is padded up to length with left alignment otherwise chopped till length.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Data=None, Enabled=None, Length=None):
        """Adds a new userDefinedAfiSafiRoutes resource on the server and adds it to the container.

        Args
        ----
        - Data (str): Data to be transmitted for AFI/SAFI, and regular enable-disable.
        - Enabled (bool): If true, the user-defined afi/safi is enabled.
        - Length (number): The data is padded up to length with left alignment otherwise chopped till length.

        Returns
        -------
        - self: This instance with all currently retrieved userDefinedAfiSafiRoutes resources using find and the newly added userDefinedAfiSafiRoutes resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained userDefinedAfiSafiRoutes resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Data=None, Enabled=None, Length=None):
        """Finds and retrieves userDefinedAfiSafiRoutes resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve userDefinedAfiSafiRoutes resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all userDefinedAfiSafiRoutes resources from the server.

        Args
        ----
        - Data (str): Data to be transmitted for AFI/SAFI, and regular enable-disable.
        - Enabled (bool): If true, the user-defined afi/safi is enabled.
        - Length (number): The data is padded up to length with left alignment otherwise chopped till length.

        Returns
        -------
        - self: This instance with matching userDefinedAfiSafiRoutes resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of userDefinedAfiSafiRoutes data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the userDefinedAfiSafiRoutes resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
