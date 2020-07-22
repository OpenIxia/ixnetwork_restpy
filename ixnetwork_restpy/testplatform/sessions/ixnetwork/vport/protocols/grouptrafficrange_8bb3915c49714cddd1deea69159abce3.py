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


class GroupTrafficRange(Base):
    """Configures the values for the group traffic range.
    The GroupTrafficRange class encapsulates a list of groupTrafficRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the GroupTrafficRange.find() method.
    The list can be managed by using the GroupTrafficRange.add() and GroupTrafficRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'groupTrafficRange'
    _SDM_ATT_MAP = {
        'AddrFamilyType': 'addrFamilyType',
        'GrpAddress': 'grpAddress',
        'GrpCount': 'grpCount',
    }

    def __init__(self, parent):
        super(GroupTrafficRange, self).__init__(parent)

    @property
    def AddrFamilyType(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): The address family of group address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddrFamilyType'])
    @AddrFamilyType.setter
    def AddrFamilyType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddrFamilyType'], value)

    @property
    def GrpAddress(self):
        """
        Returns
        -------
        - str: Group Address for traffic destination address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GrpAddress'])
    @GrpAddress.setter
    def GrpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GrpAddress'], value)

    @property
    def GrpCount(self):
        """
        Returns
        -------
        - number: The group address count per LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GrpCount'])
    @GrpCount.setter
    def GrpCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GrpCount'], value)

    def update(self, AddrFamilyType=None, GrpAddress=None, GrpCount=None):
        """Updates groupTrafficRange resource on the server.

        Args
        ----
        - AddrFamilyType (str(ipv4 | ipv6)): The address family of group address.
        - GrpAddress (str): Group Address for traffic destination address.
        - GrpCount (number): The group address count per LSP.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AddrFamilyType=None, GrpAddress=None, GrpCount=None):
        """Adds a new groupTrafficRange resource on the server and adds it to the container.

        Args
        ----
        - AddrFamilyType (str(ipv4 | ipv6)): The address family of group address.
        - GrpAddress (str): Group Address for traffic destination address.
        - GrpCount (number): The group address count per LSP.

        Returns
        -------
        - self: This instance with all currently retrieved groupTrafficRange resources using find and the newly added groupTrafficRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained groupTrafficRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AddrFamilyType=None, GrpAddress=None, GrpCount=None):
        """Finds and retrieves groupTrafficRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve groupTrafficRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all groupTrafficRange resources from the server.

        Args
        ----
        - AddrFamilyType (str(ipv4 | ipv6)): The address family of group address.
        - GrpAddress (str): Group Address for traffic destination address.
        - GrpCount (number): The group address count per LSP.

        Returns
        -------
        - self: This instance with matching groupTrafficRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of groupTrafficRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the groupTrafficRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
