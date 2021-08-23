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


class Hex(Base):
    """This specifies the hexadecimal properties related to the parameter.
    The Hex class encapsulates a list of hex resources that are managed by the system.
    A list of resources can be retrieved from the server using the Hex.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'hex'
    _SDM_ATT_MAP = {
        'Default': 'default',
        'Value': 'value',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Hex, self).__init__(parent, list_op)

    @property
    def Default(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read only) Parameter default value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Default'])

    @property
    def Value(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Parameter hex value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Value=None):
        # type: (str) -> Hex
        """Updates hex resource on the server.

        Args
        ----
        - Value (str): Parameter hex value.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Value=None):
        # type: (str) -> Hex
        """Adds a new hex resource on the json, only valid with config assistant

        Args
        ----
        - Value (str): Parameter hex value.

        Returns
        -------
        - self: This instance with all currently retrieved hex resources using find and the newly added hex resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Default=None, Value=None):
        # type: (str, str) -> Hex
        """Finds and retrieves hex resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve hex resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all hex resources from the server.

        Args
        ----
        - Default (str): (Read only) Parameter default value.
        - Value (str): Parameter hex value.

        Returns
        -------
        - self: This instance with matching hex resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of hex data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the hex resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
