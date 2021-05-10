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


class DceOutsideLinks(Base):
    """Sets the Outside Links of a particular DCE ISIS Network Range.
    The DceOutsideLinks class encapsulates a list of dceOutsideLinks resources that are managed by the user.
    A list of resources can be retrieved from the server using the DceOutsideLinks.find() method.
    The list can be managed by using the DceOutsideLinks.add() and DceOutsideLinks.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dceOutsideLinks'
    _SDM_ATT_MAP = {
        'ConnectionCol': 'connectionCol',
        'ConnectionRow': 'connectionRow',
        'LinkedRid': 'linkedRid',
    }

    def __init__(self, parent):
        super(DceOutsideLinks, self).__init__(parent)

    @property
    def ConnectionCol(self):
        """
        Returns
        -------
        - number: Used with the Connection Row value to specify the particular network range router that is the endpoint of the Outside Link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectionCol'])
    @ConnectionCol.setter
    def ConnectionCol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectionCol'], value)

    @property
    def ConnectionRow(self):
        """
        Returns
        -------
        - number: Used with the Connection Col value to specify the particular network range router that is the endpoint of the Outside Link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectionRow'])
    @ConnectionRow.setter
    def ConnectionRow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectionRow'], value)

    @property
    def LinkedRid(self):
        """
        Returns
        -------
        - str: The Router ID of the emulated DCE ISIS router at the far end of the Outside Link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkedRid'])
    @LinkedRid.setter
    def LinkedRid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkedRid'], value)

    def update(self, ConnectionCol=None, ConnectionRow=None, LinkedRid=None):
        """Updates dceOutsideLinks resource on the server.

        Args
        ----
        - ConnectionCol (number): Used with the Connection Row value to specify the particular network range router that is the endpoint of the Outside Link.
        - ConnectionRow (number): Used with the Connection Col value to specify the particular network range router that is the endpoint of the Outside Link.
        - LinkedRid (str): The Router ID of the emulated DCE ISIS router at the far end of the Outside Link.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectionCol=None, ConnectionRow=None, LinkedRid=None):
        """Adds a new dceOutsideLinks resource on the server and adds it to the container.

        Args
        ----
        - ConnectionCol (number): Used with the Connection Row value to specify the particular network range router that is the endpoint of the Outside Link.
        - ConnectionRow (number): Used with the Connection Col value to specify the particular network range router that is the endpoint of the Outside Link.
        - LinkedRid (str): The Router ID of the emulated DCE ISIS router at the far end of the Outside Link.

        Returns
        -------
        - self: This instance with all currently retrieved dceOutsideLinks resources using find and the newly added dceOutsideLinks resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dceOutsideLinks resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectionCol=None, ConnectionRow=None, LinkedRid=None):
        """Finds and retrieves dceOutsideLinks resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dceOutsideLinks resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dceOutsideLinks resources from the server.

        Args
        ----
        - ConnectionCol (number): Used with the Connection Row value to specify the particular network range router that is the endpoint of the Outside Link.
        - ConnectionRow (number): Used with the Connection Col value to specify the particular network range router that is the endpoint of the Outside Link.
        - LinkedRid (str): The Router ID of the emulated DCE ISIS router at the far end of the Outside Link.

        Returns
        -------
        - self: This instance with matching dceOutsideLinks resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dceOutsideLinks data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dceOutsideLinks resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
