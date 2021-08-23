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


class UserDefinedAfiSafi(Base):
    """Configures the user defined afi/safi values.
    The UserDefinedAfiSafi class encapsulates a list of userDefinedAfiSafi resources that are managed by the user.
    A list of resources can be retrieved from the server using the UserDefinedAfiSafi.find() method.
    The list can be managed by using the UserDefinedAfiSafi.add() and UserDefinedAfiSafi.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'userDefinedAfiSafi'
    _SDM_ATT_MAP = {
        'Afi': 'afi',
        'Safi': 'safi',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(UserDefinedAfiSafi, self).__init__(parent, list_op)

    @property
    def UserDefinedAfiSafiRoutes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userdefinedafisafiroutes_e29273deea974c8bb208222a3d127a0e.UserDefinedAfiSafiRoutes): An instance of the UserDefinedAfiSafiRoutes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userdefinedafisafiroutes_e29273deea974c8bb208222a3d127a0e import UserDefinedAfiSafiRoutes
        if self._properties.get('UserDefinedAfiSafiRoutes', None) is not None:
            return self._properties.get('UserDefinedAfiSafiRoutes')
        else:
            return UserDefinedAfiSafiRoutes(self)

    @property
    def Afi(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The 2 byte AFI value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Afi'])
    @Afi.setter
    def Afi(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Afi'], value)

    @property
    def Safi(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The 1 byte SAFI value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Safi'])
    @Safi.setter
    def Safi(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Safi'], value)

    def update(self, Afi=None, Safi=None):
        # type: (int, int) -> UserDefinedAfiSafi
        """Updates userDefinedAfiSafi resource on the server.

        Args
        ----
        - Afi (number): The 2 byte AFI value.
        - Safi (number): The 1 byte SAFI value.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Afi=None, Safi=None):
        # type: (int, int) -> UserDefinedAfiSafi
        """Adds a new userDefinedAfiSafi resource on the server and adds it to the container.

        Args
        ----
        - Afi (number): The 2 byte AFI value.
        - Safi (number): The 1 byte SAFI value.

        Returns
        -------
        - self: This instance with all currently retrieved userDefinedAfiSafi resources using find and the newly added userDefinedAfiSafi resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained userDefinedAfiSafi resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Afi=None, Safi=None):
        # type: (int, int) -> UserDefinedAfiSafi
        """Finds and retrieves userDefinedAfiSafi resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve userDefinedAfiSafi resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all userDefinedAfiSafi resources from the server.

        Args
        ----
        - Afi (number): The 2 byte AFI value.
        - Safi (number): The 1 byte SAFI value.

        Returns
        -------
        - self: This instance with matching userDefinedAfiSafi resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of userDefinedAfiSafi data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the userDefinedAfiSafi resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
