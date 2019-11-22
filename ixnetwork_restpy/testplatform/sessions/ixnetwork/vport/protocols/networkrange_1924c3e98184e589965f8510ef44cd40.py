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


class NetworkRange(Base):
    """A set of network ranges to be included for this router.
    The NetworkRange class encapsulates a list of networkRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the NetworkRange.find() method.
    The list can be managed by the user by using the NetworkRange.add() and NetworkRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'networkRange'

    def __init__(self, parent):
        super(NetworkRange, self).__init__(parent)

    @property
    def BBit(self):
        """If enabled, the router LSAs will indicate that the router is acting as a Border Router (area border router/ABR). Disabled by default.

        Returns:
            bool
        """
        return self._get_attribute('bBit')
    @BBit.setter
    def BBit(self, value):
        self._set_attribute('bBit', value)

    @property
    def EBit(self):
        """If enabled, the router LSAs will indicate that the router is acting as an AS Boundary Router (Autonomous System Boundary Router/ASBR). Disabled by default.

        Returns:
            bool
        """
        return self._get_attribute('eBit')
    @EBit.setter
    def EBit(self, value):
        self._set_attribute('eBit', value)

    @property
    def EnableAdvertiseNetworkRange(self):
        """Enables the OSPFv3 network range grid and allows it to be advertised by the emulated OSPFv3 router.

        Returns:
            bool
        """
        return self._get_attribute('enableAdvertiseNetworkRange')
    @EnableAdvertiseNetworkRange.setter
    def EnableAdvertiseNetworkRange(self, value):
        self._set_attribute('enableAdvertiseNetworkRange', value)

    @property
    def EntryAddress(self):
        """The IPv6 address of the simulated OSPFv3 router that is the entry point into the network range grid.

        Returns:
            str
        """
        return self._get_attribute('entryAddress')
    @EntryAddress.setter
    def EntryAddress(self, value):
        self._set_attribute('entryAddress', value)

    @property
    def EntryColumn(self):
        """The column where the entry point simulated OSPFv3 router is located in the network range grid.

        Returns:
            number
        """
        return self._get_attribute('entryColumn')
    @EntryColumn.setter
    def EntryColumn(self, value):
        self._set_attribute('entryColumn', value)

    @property
    def EntryMaskLength(self):
        """(integer, range = 1 to 128) The length of the mask used with the IPv6 address of the entry point simulated OSPFv3 router in the grid. The default is 64.

        Returns:
            number
        """
        return self._get_attribute('entryMaskLength')
    @EntryMaskLength.setter
    def EntryMaskLength(self, value):
        self._set_attribute('entryMaskLength', value)

    @property
    def EntryRow(self):
        """The row where the entry point simulated OSPFv3 router is located in the network range grid.

        Returns:
            number
        """
        return self._get_attribute('entryRow')
    @EntryRow.setter
    def EntryRow(self, value):
        self._set_attribute('entryRow', value)

    @property
    def IncrementByRid(self):
        """The increment step to be added to the RID for each additional simulated OSPFv3 router in the grid.

        Returns:
            str
        """
        return self._get_attribute('incrementByRid')
    @IncrementByRid.setter
    def IncrementByRid(self, value):
        self._set_attribute('incrementByRid', value)

    @property
    def LinkMetric(self):
        """The metric for the link connecting the grid with the emulated OSPFv3 router.

        Returns:
            number
        """
        return self._get_attribute('linkMetric')
    @LinkMetric.setter
    def LinkMetric(self, value):
        self._set_attribute('linkMetric', value)

    @property
    def LinkType(self):
        """Sets the link type of the network range.

        Returns:
            str(broadcast|pointToPoint)
        """
        return self._get_attribute('linkType')
    @LinkType.setter
    def LinkType(self, value):
        self._set_attribute('linkType', value)

    @property
    def NumCols(self):
        """The number of columns in this network range grid.

        Returns:
            number
        """
        return self._get_attribute('numCols')
    @NumCols.setter
    def NumCols(self, value):
        self._set_attribute('numCols', value)

    @property
    def NumRows(self):
        """The number of rows in this network range grid.

        Returns:
            number
        """
        return self._get_attribute('numRows')
    @NumRows.setter
    def NumRows(self, value):
        self._set_attribute('numRows', value)

    @property
    def PrefixAddress(self):
        """The IPv6 prefix address for the first subnet in the grid.

        Returns:
            str
        """
        return self._get_attribute('prefixAddress')
    @PrefixAddress.setter
    def PrefixAddress(self, value):
        self._set_attribute('prefixAddress', value)

    @property
    def PrefixMask(self):
        """(integer, range = 1 to 128) The length of the mask used with the IPv6 addresses of the subnets in the grid. The default is 64.

        Returns:
            number
        """
        return self._get_attribute('prefixMask')
    @PrefixMask.setter
    def PrefixMask(self, value):
        self._set_attribute('prefixMask', value)

    @property
    def Rid(self):
        """The identifier for the first simulated OSPFv3 router in the grid.

        Returns:
            str
        """
        return self._get_attribute('rid')
    @Rid.setter
    def Rid(self, value):
        self._set_attribute('rid', value)

    def update(self, BBit=None, EBit=None, EnableAdvertiseNetworkRange=None, EntryAddress=None, EntryColumn=None, EntryMaskLength=None, EntryRow=None, IncrementByRid=None, LinkMetric=None, LinkType=None, NumCols=None, NumRows=None, PrefixAddress=None, PrefixMask=None, Rid=None):
        """Updates a child instance of networkRange on the server.

        Args:
            BBit (bool): If enabled, the router LSAs will indicate that the router is acting as a Border Router (area border router/ABR). Disabled by default.
            EBit (bool): If enabled, the router LSAs will indicate that the router is acting as an AS Boundary Router (Autonomous System Boundary Router/ASBR). Disabled by default.
            EnableAdvertiseNetworkRange (bool): Enables the OSPFv3 network range grid and allows it to be advertised by the emulated OSPFv3 router.
            EntryAddress (str): The IPv6 address of the simulated OSPFv3 router that is the entry point into the network range grid.
            EntryColumn (number): The column where the entry point simulated OSPFv3 router is located in the network range grid.
            EntryMaskLength (number): (integer, range = 1 to 128) The length of the mask used with the IPv6 address of the entry point simulated OSPFv3 router in the grid. The default is 64.
            EntryRow (number): The row where the entry point simulated OSPFv3 router is located in the network range grid.
            IncrementByRid (str): The increment step to be added to the RID for each additional simulated OSPFv3 router in the grid.
            LinkMetric (number): The metric for the link connecting the grid with the emulated OSPFv3 router.
            LinkType (str(broadcast|pointToPoint)): Sets the link type of the network range.
            NumCols (number): The number of columns in this network range grid.
            NumRows (number): The number of rows in this network range grid.
            PrefixAddress (str): The IPv6 prefix address for the first subnet in the grid.
            PrefixMask (number): (integer, range = 1 to 128) The length of the mask used with the IPv6 addresses of the subnets in the grid. The default is 64.
            Rid (str): The identifier for the first simulated OSPFv3 router in the grid.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, BBit=None, EBit=None, EnableAdvertiseNetworkRange=None, EntryAddress=None, EntryColumn=None, EntryMaskLength=None, EntryRow=None, IncrementByRid=None, LinkMetric=None, LinkType=None, NumCols=None, NumRows=None, PrefixAddress=None, PrefixMask=None, Rid=None):
        """Adds a new networkRange node on the server and retrieves it in this instance.

        Args:
            BBit (bool): If enabled, the router LSAs will indicate that the router is acting as a Border Router (area border router/ABR). Disabled by default.
            EBit (bool): If enabled, the router LSAs will indicate that the router is acting as an AS Boundary Router (Autonomous System Boundary Router/ASBR). Disabled by default.
            EnableAdvertiseNetworkRange (bool): Enables the OSPFv3 network range grid and allows it to be advertised by the emulated OSPFv3 router.
            EntryAddress (str): The IPv6 address of the simulated OSPFv3 router that is the entry point into the network range grid.
            EntryColumn (number): The column where the entry point simulated OSPFv3 router is located in the network range grid.
            EntryMaskLength (number): (integer, range = 1 to 128) The length of the mask used with the IPv6 address of the entry point simulated OSPFv3 router in the grid. The default is 64.
            EntryRow (number): The row where the entry point simulated OSPFv3 router is located in the network range grid.
            IncrementByRid (str): The increment step to be added to the RID for each additional simulated OSPFv3 router in the grid.
            LinkMetric (number): The metric for the link connecting the grid with the emulated OSPFv3 router.
            LinkType (str(broadcast|pointToPoint)): Sets the link type of the network range.
            NumCols (number): The number of columns in this network range grid.
            NumRows (number): The number of rows in this network range grid.
            PrefixAddress (str): The IPv6 prefix address for the first subnet in the grid.
            PrefixMask (number): (integer, range = 1 to 128) The length of the mask used with the IPv6 addresses of the subnets in the grid. The default is 64.
            Rid (str): The identifier for the first simulated OSPFv3 router in the grid.

        Returns:
            self: This instance with all currently retrieved networkRange data using find and the newly added networkRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the networkRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BBit=None, EBit=None, EnableAdvertiseNetworkRange=None, EntryAddress=None, EntryColumn=None, EntryMaskLength=None, EntryRow=None, IncrementByRid=None, LinkMetric=None, LinkType=None, NumCols=None, NumRows=None, PrefixAddress=None, PrefixMask=None, Rid=None):
        """Finds and retrieves networkRange data from the server.

        All named parameters support regex and can be used to selectively retrieve networkRange data from the server.
        By default the find method takes no parameters and will retrieve all networkRange data from the server.

        Args:
            BBit (bool): If enabled, the router LSAs will indicate that the router is acting as a Border Router (area border router/ABR). Disabled by default.
            EBit (bool): If enabled, the router LSAs will indicate that the router is acting as an AS Boundary Router (Autonomous System Boundary Router/ASBR). Disabled by default.
            EnableAdvertiseNetworkRange (bool): Enables the OSPFv3 network range grid and allows it to be advertised by the emulated OSPFv3 router.
            EntryAddress (str): The IPv6 address of the simulated OSPFv3 router that is the entry point into the network range grid.
            EntryColumn (number): The column where the entry point simulated OSPFv3 router is located in the network range grid.
            EntryMaskLength (number): (integer, range = 1 to 128) The length of the mask used with the IPv6 address of the entry point simulated OSPFv3 router in the grid. The default is 64.
            EntryRow (number): The row where the entry point simulated OSPFv3 router is located in the network range grid.
            IncrementByRid (str): The increment step to be added to the RID for each additional simulated OSPFv3 router in the grid.
            LinkMetric (number): The metric for the link connecting the grid with the emulated OSPFv3 router.
            LinkType (str(broadcast|pointToPoint)): Sets the link type of the network range.
            NumCols (number): The number of columns in this network range grid.
            NumRows (number): The number of rows in this network range grid.
            PrefixAddress (str): The IPv6 prefix address for the first subnet in the grid.
            PrefixMask (number): (integer, range = 1 to 128) The length of the mask used with the IPv6 addresses of the subnets in the grid. The default is 64.
            Rid (str): The identifier for the first simulated OSPFv3 router in the grid.

        Returns:
            self: This instance with matching networkRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of networkRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the networkRange data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
