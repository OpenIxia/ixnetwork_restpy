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


class String(Base):
    """This specifies the string properties related to the parameter.
    The String class encapsulates a list of string resources that are managed by the system.
    A list of resources can be retrieved from the server using the String.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'string'
    _SDM_ATT_MAP = {
        'Default': 'default',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(String, self).__init__(parent)

    @property
    def Default(self):
        """
        Returns
        -------
        - str: (Read only) Parameter default value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Default'])

    @property
    def Value(self):
        """
        Returns
        -------
        - str: Parameter string value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Value=None):
        """Updates string resource on the server.

        Args
        ----
        - Value (str): Parameter string value.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Default=None, Value=None):
        """Finds and retrieves string resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve string resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all string resources from the server.

        Args
        ----
        - Default (str): (Read only) Parameter default value.
        - Value (str): Parameter string value.

        Returns
        -------
        - self: This instance with matching string resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of string data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the string resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
