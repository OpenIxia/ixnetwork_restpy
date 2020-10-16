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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class Container(Base):
    """Tlv container used to group multiple object containers
    The Container class encapsulates a list of container resources that are managed by the user.
    A list of resources can be retrieved from the server using the Container.find() method.
    The list can be managed by using the Container.add() and Container.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'container'
    _SDM_ATT_MAP = {
        'Description': 'description',
        'IsEditable': 'isEditable',
        'IsRepeatable': 'isRepeatable',
        'IsRequired': 'isRequired',
        'Name': 'name',
    }

    def __init__(self, parent):
        super(Container, self).__init__(parent)

    @property
    def Object(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.object_12e587bd6e412f6d3d8361017e8dcba9.Object): An instance of the Object class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.object_12e587bd6e412f6d3d8361017e8dcba9 import Object
        return Object(self)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: Description of the tlv
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def IsEditable(self):
        """
        Returns
        -------
        - bool: Indicates whether this is editable or not
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsEditable'])
    @IsEditable.setter
    def IsEditable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsEditable'], value)

    @property
    def IsRepeatable(self):
        """
        Returns
        -------
        - bool: Flag indicating whether this is repeatable or not
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRepeatable'])
    @IsRepeatable.setter
    def IsRepeatable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsRepeatable'], value)

    @property
    def IsRequired(self):
        """
        Returns
        -------
        - bool: Flag indicating whether this is required or not
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRequired'])
    @IsRequired.setter
    def IsRequired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsRequired'], value)

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

    def update(self, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
        """Updates container resource on the server.

        Args
        ----
        - Description (str): Description of the tlv
        - IsEditable (bool): Indicates whether this is editable or not
        - IsRepeatable (bool): Flag indicating whether this is repeatable or not
        - IsRequired (bool): Flag indicating whether this is required or not
        - Name (str): Name of the tlv

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
        """Adds a new container resource on the server and adds it to the container.

        Args
        ----
        - Description (str): Description of the tlv
        - IsEditable (bool): Indicates whether this is editable or not
        - IsRepeatable (bool): Flag indicating whether this is repeatable or not
        - IsRequired (bool): Flag indicating whether this is required or not
        - Name (str): Name of the tlv

        Returns
        -------
        - self: This instance with all currently retrieved container resources using find and the newly added container resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained container resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
        """Finds and retrieves container resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve container resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all container resources from the server.

        Args
        ----
        - Description (str): Description of the tlv
        - IsEditable (bool): Indicates whether this is editable or not
        - IsRepeatable (bool): Flag indicating whether this is repeatable or not
        - IsRequired (bool): Flag indicating whether this is required or not
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
