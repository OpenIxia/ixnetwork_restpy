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
import sys
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Container(Base):
    """Tlv container used to group multiple object containers
    The Container class encapsulates a list of container resources that are managed by the system.
    A list of resources can be retrieved from the server using the Container.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'container'
    _SDM_ATT_MAP = {
        'IsEnabled': 'isEnabled',
        'Name': 'name',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Container, self).__init__(parent, list_op)

    @property
    def Object(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.object_1ba6063c8cfb61359d0cafa499ed49e4.Object): An instance of the Object class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.object_1ba6063c8cfb61359d0cafa499ed49e4 import Object
        if len(self._object_properties) > 0:
            if self._properties.get('Object', None) is not None:
                return self._properties.get('Object')
        return Object(self)

    @property
    def IsEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables/disables this field
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsEnabled'])
    @IsEnabled.setter
    def IsEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IsEnabled'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of the tlv
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    def update(self, IsEnabled=None, Name=None):
        # type: (bool, str) -> Container
        """Updates container resource on the server.

        Args
        ----
        - IsEnabled (bool): Enables/disables this field
        - Name (str): Name of the tlv

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IsEnabled=None, Name=None):
        # type: (bool, str) -> Container
        """Adds a new container resource on the json, only valid with batch add utility

        Args
        ----
        - IsEnabled (bool): Enables/disables this field
        - Name (str): Name of the tlv

        Returns
        -------
        - self: This instance with all currently retrieved container resources using find and the newly added container resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, IsEnabled=None, Name=None):
        # type: (bool, str) -> Container
        """Finds and retrieves container resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve container resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all container resources from the server.

        Args
        ----
        - IsEnabled (bool): Enables/disables this field
        - Name (str): Name of the tlv

        Returns
        -------
        - self: This instance with matching container resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of container data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the container resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
