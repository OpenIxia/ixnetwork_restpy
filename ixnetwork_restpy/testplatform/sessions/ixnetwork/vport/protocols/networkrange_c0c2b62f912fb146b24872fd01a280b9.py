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


class NetworkRange(Base):
    """A set of network ranges to be included for this router.
    The NetworkRange class encapsulates a list of networkRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetworkRange.find() method.
    The list can be managed by using the NetworkRange.add() and NetworkRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'networkRange'
    _SDM_ATT_MAP = {
        'BBit': 'bBit',
        'EBit': 'eBit',
        'EnableAdvertiseNetworkRange': 'enableAdvertiseNetworkRange',
        'EntryAddress': 'entryAddress',
        'EntryColumn': 'entryColumn',
        'EntryMaskLength': 'entryMaskLength',
        'EntryRow': 'entryRow',
        'IncrementByRid': 'incrementByRid',
        'LinkMetric': 'linkMetric',
        'LinkType': 'linkType',
        'NumCols': 'numCols',
        'NumRows': 'numRows',
        'PrefixAddress': 'prefixAddress',
        'PrefixMask': 'prefixMask',
        'Rid': 'rid',
    }

    def __init__(self, parent):
        super(NetworkRange, self).__init__(parent)

    @property
    def BBit(self):
        """
        Returns
        -------
        - bool: If enabled, the router LSAs will indicate that the router is acting as a Border Router (area border router/ABR). Disabled by default.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BBit'])
    @BBit.setter
    def BBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BBit'], value)

    @property
    def EBit(self):
        """
        Returns
        -------
        - bool: If enabled, the router LSAs will indicate that the router is acting as an AS Boundary Router (Autonomous System Boundary Router/ASBR). Disabled by default.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EBit'])
    @EBit.setter
    def EBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EBit'], value)

    @property
    def EnableAdvertiseNetworkRange(self):
        """
        Returns
        -------
        - bool: Enables the OSPFv3 network range grid and allows it to be advertised by the emulated OSPFv3 router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAdvertiseNetworkRange'])
    @EnableAdvertiseNetworkRange.setter
    def EnableAdvertiseNetworkRange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAdvertiseNetworkRange'], value)

    @property
    def EntryAddress(self):
        """
        Returns
        -------
        - str: The IPv6 address of the simulated OSPFv3 router that is the entry point into the network range grid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryAddress'])
    @EntryAddress.setter
    def EntryAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryAddress'], value)

    @property
    def EntryColumn(self):
        """
        Returns
        -------
        - number: The column where the entry point simulated OSPFv3 router is located in the network range grid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryColumn'])
    @EntryColumn.setter
    def EntryColumn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryColumn'], value)

    @property
    def EntryMaskLength(self):
        """
        Returns
        -------
        - number: (integer, range = 1 to 128) The length of the mask used with the IPv6 address of the entry point simulated OSPFv3 router in the grid. The default is 64.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryMaskLength'])
    @EntryMaskLength.setter
    def EntryMaskLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryMaskLength'], value)

    @property
    def EntryRow(self):
        """
        Returns
        -------
        - number: The row where the entry point simulated OSPFv3 router is located in the network range grid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EntryRow'])
    @EntryRow.setter
    def EntryRow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EntryRow'], value)

    @property
    def IncrementByRid(self):
        """
        Returns
        -------
        - str: The increment step to be added to the RID for each additional simulated OSPFv3 router in the grid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementByRid'])
    @IncrementByRid.setter
    def IncrementByRid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementByRid'], value)

    @property
    def LinkMetric(self):
        """
        Returns
        -------
        - number: The metric for the link connecting the grid with the emulated OSPFv3 router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkMetric'])
    @LinkMetric.setter
    def LinkMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkMetric'], value)

    @property
    def LinkType(self):
        """
        Returns
        -------
        - str(broadcast | pointToPoint): Sets the link type of the network range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkType'])
    @LinkType.setter
    def LinkType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkType'], value)

    @property
    def NumCols(self):
        """
        Returns
        -------
        - number: The number of columns in this network range grid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumCols'])
    @NumCols.setter
    def NumCols(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumCols'], value)

    @property
    def NumRows(self):
        """
        Returns
        -------
        - number: The number of rows in this network range grid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumRows'])
    @NumRows.setter
    def NumRows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumRows'], value)

    @property
    def PrefixAddress(self):
        """
        Returns
        -------
        - str: The IPv6 prefix address for the first subnet in the grid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixAddress'])
    @PrefixAddress.setter
    def PrefixAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PrefixAddress'], value)

    @property
    def PrefixMask(self):
        """
        Returns
        -------
        - number: (integer, range = 1 to 128) The length of the mask used with the IPv6 addresses of the subnets in the grid. The default is 64.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixMask'])
    @PrefixMask.setter
    def PrefixMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PrefixMask'], value)

    @property
    def Rid(self):
        """
        Returns
        -------
        - str: The identifier for the first simulated OSPFv3 router in the grid.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rid'])
    @Rid.setter
    def Rid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rid'], value)

    def update(self, BBit=None, EBit=None, EnableAdvertiseNetworkRange=None, EntryAddress=None, EntryColumn=None, EntryMaskLength=None, EntryRow=None, IncrementByRid=None, LinkMetric=None, LinkType=None, NumCols=None, NumRows=None, PrefixAddress=None, PrefixMask=None, Rid=None):
        """Updates networkRange resource on the server.

        Args
        ----
        - BBit (bool): If enabled, the router LSAs will indicate that the router is acting as a Border Router (area border router/ABR). Disabled by default.
        - EBit (bool): If enabled, the router LSAs will indicate that the router is acting as an AS Boundary Router (Autonomous System Boundary Router/ASBR). Disabled by default.
        - EnableAdvertiseNetworkRange (bool): Enables the OSPFv3 network range grid and allows it to be advertised by the emulated OSPFv3 router.
        - EntryAddress (str): The IPv6 address of the simulated OSPFv3 router that is the entry point into the network range grid.
        - EntryColumn (number): The column where the entry point simulated OSPFv3 router is located in the network range grid.
        - EntryMaskLength (number): (integer, range = 1 to 128) The length of the mask used with the IPv6 address of the entry point simulated OSPFv3 router in the grid. The default is 64.
        - EntryRow (number): The row where the entry point simulated OSPFv3 router is located in the network range grid.
        - IncrementByRid (str): The increment step to be added to the RID for each additional simulated OSPFv3 router in the grid.
        - LinkMetric (number): The metric for the link connecting the grid with the emulated OSPFv3 router.
        - LinkType (str(broadcast | pointToPoint)): Sets the link type of the network range.
        - NumCols (number): The number of columns in this network range grid.
        - NumRows (number): The number of rows in this network range grid.
        - PrefixAddress (str): The IPv6 prefix address for the first subnet in the grid.
        - PrefixMask (number): (integer, range = 1 to 128) The length of the mask used with the IPv6 addresses of the subnets in the grid. The default is 64.
        - Rid (str): The identifier for the first simulated OSPFv3 router in the grid.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, BBit=None, EBit=None, EnableAdvertiseNetworkRange=None, EntryAddress=None, EntryColumn=None, EntryMaskLength=None, EntryRow=None, IncrementByRid=None, LinkMetric=None, LinkType=None, NumCols=None, NumRows=None, PrefixAddress=None, PrefixMask=None, Rid=None):
        """Adds a new networkRange resource on the server and adds it to the container.

        Args
        ----
        - BBit (bool): If enabled, the router LSAs will indicate that the router is acting as a Border Router (area border router/ABR). Disabled by default.
        - EBit (bool): If enabled, the router LSAs will indicate that the router is acting as an AS Boundary Router (Autonomous System Boundary Router/ASBR). Disabled by default.
        - EnableAdvertiseNetworkRange (bool): Enables the OSPFv3 network range grid and allows it to be advertised by the emulated OSPFv3 router.
        - EntryAddress (str): The IPv6 address of the simulated OSPFv3 router that is the entry point into the network range grid.
        - EntryColumn (number): The column where the entry point simulated OSPFv3 router is located in the network range grid.
        - EntryMaskLength (number): (integer, range = 1 to 128) The length of the mask used with the IPv6 address of the entry point simulated OSPFv3 router in the grid. The default is 64.
        - EntryRow (number): The row where the entry point simulated OSPFv3 router is located in the network range grid.
        - IncrementByRid (str): The increment step to be added to the RID for each additional simulated OSPFv3 router in the grid.
        - LinkMetric (number): The metric for the link connecting the grid with the emulated OSPFv3 router.
        - LinkType (str(broadcast | pointToPoint)): Sets the link type of the network range.
        - NumCols (number): The number of columns in this network range grid.
        - NumRows (number): The number of rows in this network range grid.
        - PrefixAddress (str): The IPv6 prefix address for the first subnet in the grid.
        - PrefixMask (number): (integer, range = 1 to 128) The length of the mask used with the IPv6 addresses of the subnets in the grid. The default is 64.
        - Rid (str): The identifier for the first simulated OSPFv3 router in the grid.

        Returns
        -------
        - self: This instance with all currently retrieved networkRange resources using find and the newly added networkRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained networkRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BBit=None, EBit=None, EnableAdvertiseNetworkRange=None, EntryAddress=None, EntryColumn=None, EntryMaskLength=None, EntryRow=None, IncrementByRid=None, LinkMetric=None, LinkType=None, NumCols=None, NumRows=None, PrefixAddress=None, PrefixMask=None, Rid=None):
        """Finds and retrieves networkRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve networkRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all networkRange resources from the server.

        Args
        ----
        - BBit (bool): If enabled, the router LSAs will indicate that the router is acting as a Border Router (area border router/ABR). Disabled by default.
        - EBit (bool): If enabled, the router LSAs will indicate that the router is acting as an AS Boundary Router (Autonomous System Boundary Router/ASBR). Disabled by default.
        - EnableAdvertiseNetworkRange (bool): Enables the OSPFv3 network range grid and allows it to be advertised by the emulated OSPFv3 router.
        - EntryAddress (str): The IPv6 address of the simulated OSPFv3 router that is the entry point into the network range grid.
        - EntryColumn (number): The column where the entry point simulated OSPFv3 router is located in the network range grid.
        - EntryMaskLength (number): (integer, range = 1 to 128) The length of the mask used with the IPv6 address of the entry point simulated OSPFv3 router in the grid. The default is 64.
        - EntryRow (number): The row where the entry point simulated OSPFv3 router is located in the network range grid.
        - IncrementByRid (str): The increment step to be added to the RID for each additional simulated OSPFv3 router in the grid.
        - LinkMetric (number): The metric for the link connecting the grid with the emulated OSPFv3 router.
        - LinkType (str(broadcast | pointToPoint)): Sets the link type of the network range.
        - NumCols (number): The number of columns in this network range grid.
        - NumRows (number): The number of rows in this network range grid.
        - PrefixAddress (str): The IPv6 prefix address for the first subnet in the grid.
        - PrefixMask (number): (integer, range = 1 to 128) The length of the mask used with the IPv6 addresses of the subnets in the grid. The default is 64.
        - Rid (str): The identifier for the first simulated OSPFv3 router in the grid.

        Returns
        -------
        - self: This instance with matching networkRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of networkRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the networkRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
