# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class Container(Base):
    """Tlv container used to group multiple object containers
    The Container class encapsulates a list of container resources that is managed by the system.
    A list of resources can be retrieved from the server using the Container.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'container'

    def __init__(self, parent):
        super(Container, self).__init__(parent)

    @property
    def Object(self):
        """An instance of the Object class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.object.Object)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.object import Object
        return Object(self)

    @property
    def IsEnabled(self):
        """Enables/disables this field

        Returns:
            bool
        """
        return self._get_attribute('isEnabled')
    @IsEnabled.setter
    def IsEnabled(self, value):
        self._set_attribute('isEnabled', value)

    @property
    def Name(self):
        """Name of the tlv

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    def update(self, IsEnabled=None, Name=None):
        """Updates a child instance of container on the server.

        Args:
            IsEnabled (bool): Enables/disables this field
            Name (str): Name of the tlv

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, IsEnabled=None, Name=None):
        """Finds and retrieves container data from the server.

        All named parameters support regex and can be used to selectively retrieve container data from the server.
        By default the find method takes no parameters and will retrieve all container data from the server.

        Args:
            IsEnabled (bool): Enables/disables this field
            Name (str): Name of the tlv

        Returns:
            self: This instance with matching container data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of container data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the container data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
