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


class Source(Base):
    """This object configures a set of IPv4 source addresses that a host wishes to receive multicast traffic from.
    The Source class encapsulates a list of source resources that are managed by the user.
    A list of resources can be retrieved from the server using the Source.find() method.
    The list can be managed by using the Source.add() and Source.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'source'
    _SDM_ATT_MAP = {
        'SourceRangeCount': 'sourceRangeCount',
        'SourceRangeStart': 'sourceRangeStart',
    }

    def __init__(self, parent):
        super(Source, self).__init__(parent)

    @property
    def SourceRangeCount(self):
        """
        Returns
        -------
        - number: The number of IP addresses in the source range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceRangeCount'])
    @SourceRangeCount.setter
    def SourceRangeCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceRangeCount'], value)

    @property
    def SourceRangeStart(self):
        """
        Returns
        -------
        - str: The first IP address in the source range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceRangeStart'])
    @SourceRangeStart.setter
    def SourceRangeStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceRangeStart'], value)

    def update(self, SourceRangeCount=None, SourceRangeStart=None):
        """Updates source resource on the server.

        Args
        ----
        - SourceRangeCount (number): The number of IP addresses in the source range.
        - SourceRangeStart (str): The first IP address in the source range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, SourceRangeCount=None, SourceRangeStart=None):
        """Adds a new source resource on the server and adds it to the container.

        Args
        ----
        - SourceRangeCount (number): The number of IP addresses in the source range.
        - SourceRangeStart (str): The first IP address in the source range.

        Returns
        -------
        - self: This instance with all currently retrieved source resources using find and the newly added source resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained source resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, SourceRangeCount=None, SourceRangeStart=None):
        """Finds and retrieves source resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve source resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all source resources from the server.

        Args
        ----
        - SourceRangeCount (number): The number of IP addresses in the source range.
        - SourceRangeStart (str): The first IP address in the source range.

        Returns
        -------
        - self: This instance with matching source resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of source data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the source resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
