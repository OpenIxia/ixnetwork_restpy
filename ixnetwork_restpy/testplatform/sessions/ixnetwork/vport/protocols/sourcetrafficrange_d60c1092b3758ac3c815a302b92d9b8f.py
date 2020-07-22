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


class SourceTrafficRange(Base):
    """Configures the source traffic range values.
    The SourceTrafficRange class encapsulates a list of sourceTrafficRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SourceTrafficRange.find() method.
    The list can be managed by using the SourceTrafficRange.add() and SourceTrafficRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'sourceTrafficRange'
    _SDM_ATT_MAP = {
        'AddrFamily': 'addrFamily',
        'FilterOnGroupAddress': 'filterOnGroupAddress',
        'GroupAddress': 'groupAddress',
        'GrpCountPerLsp': 'grpCountPerLsp',
        'SourceAddress': 'sourceAddress',
        'SrcCountPerLsp': 'srcCountPerLsp',
    }

    def __init__(self, parent):
        super(SourceTrafficRange, self).__init__(parent)

    @property
    def AddrFamily(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): The address familyt value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddrFamily'])
    @AddrFamily.setter
    def AddrFamily(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddrFamily'], value)

    @property
    def FilterOnGroupAddress(self):
        """
        Returns
        -------
        - bool: The available filters on group address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FilterOnGroupAddress'])
    @FilterOnGroupAddress.setter
    def FilterOnGroupAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FilterOnGroupAddress'], value)

    @property
    def GroupAddress(self):
        """
        Returns
        -------
        - str: The group address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupAddress'])
    @GroupAddress.setter
    def GroupAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupAddress'], value)

    @property
    def GrpCountPerLsp(self):
        """
        Returns
        -------
        - number: The total group count per LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GrpCountPerLsp'])
    @GrpCountPerLsp.setter
    def GrpCountPerLsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GrpCountPerLsp'], value)

    @property
    def SourceAddress(self):
        """
        Returns
        -------
        - str: The source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAddress'])
    @SourceAddress.setter
    def SourceAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceAddress'], value)

    @property
    def SrcCountPerLsp(self):
        """
        Returns
        -------
        - number: The total source count per LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrcCountPerLsp'])
    @SrcCountPerLsp.setter
    def SrcCountPerLsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SrcCountPerLsp'], value)

    def update(self, AddrFamily=None, FilterOnGroupAddress=None, GroupAddress=None, GrpCountPerLsp=None, SourceAddress=None, SrcCountPerLsp=None):
        """Updates sourceTrafficRange resource on the server.

        Args
        ----
        - AddrFamily (str(ipv4 | ipv6)): The address familyt value.
        - FilterOnGroupAddress (bool): The available filters on group address.
        - GroupAddress (str): The group address.
        - GrpCountPerLsp (number): The total group count per LSP.
        - SourceAddress (str): The source address.
        - SrcCountPerLsp (number): The total source count per LSP.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AddrFamily=None, FilterOnGroupAddress=None, GroupAddress=None, GrpCountPerLsp=None, SourceAddress=None, SrcCountPerLsp=None):
        """Adds a new sourceTrafficRange resource on the server and adds it to the container.

        Args
        ----
        - AddrFamily (str(ipv4 | ipv6)): The address familyt value.
        - FilterOnGroupAddress (bool): The available filters on group address.
        - GroupAddress (str): The group address.
        - GrpCountPerLsp (number): The total group count per LSP.
        - SourceAddress (str): The source address.
        - SrcCountPerLsp (number): The total source count per LSP.

        Returns
        -------
        - self: This instance with all currently retrieved sourceTrafficRange resources using find and the newly added sourceTrafficRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained sourceTrafficRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AddrFamily=None, FilterOnGroupAddress=None, GroupAddress=None, GrpCountPerLsp=None, SourceAddress=None, SrcCountPerLsp=None):
        """Finds and retrieves sourceTrafficRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve sourceTrafficRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all sourceTrafficRange resources from the server.

        Args
        ----
        - AddrFamily (str(ipv4 | ipv6)): The address familyt value.
        - FilterOnGroupAddress (bool): The available filters on group address.
        - GroupAddress (str): The group address.
        - GrpCountPerLsp (number): The total group count per LSP.
        - SourceAddress (str): The source address.
        - SrcCountPerLsp (number): The total source count per LSP.

        Returns
        -------
        - self: This instance with matching sourceTrafficRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of sourceTrafficRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the sourceTrafficRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
