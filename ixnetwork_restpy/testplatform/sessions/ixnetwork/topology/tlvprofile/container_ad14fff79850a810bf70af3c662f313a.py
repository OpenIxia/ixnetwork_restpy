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

    def __init__(self, parent):
        super(Container, self).__init__(parent)

    @property
    def Object(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.object_1ba6063c8cfb61359d0cafa499ed49e4.Object): An instance of the Object class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.object_1ba6063c8cfb61359d0cafa499ed49e4 import Object
        return Object(self)

    @property
    def IsEnabled(self):
        """
        Returns
        -------
        - bool: Enables/disables this field
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsEnabled'])
    @IsEnabled.setter
    def IsEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsEnabled'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of the tlv
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    def update(self, IsEnabled=None, Name=None):
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

    def find(self, IsEnabled=None, Name=None):
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
