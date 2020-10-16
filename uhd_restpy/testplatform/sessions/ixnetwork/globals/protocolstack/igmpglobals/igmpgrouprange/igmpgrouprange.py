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


class IgmpGroupRange(Base):
    """
    The IgmpGroupRange class encapsulates a list of igmpGroupRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the IgmpGroupRange.find() method.
    The list can be managed by using the IgmpGroupRange.add() and IgmpGroupRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'igmpGroupRange'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'FilterMode': 'filterMode',
        'Increment': 'increment',
        'IpAddress': 'ipAddress',
        'Name': 'name',
        'ObjectId': 'objectId',
        'SourceCount': 'sourceCount',
        'SourceIncrement': 'sourceIncrement',
        'SourceIpAddress': 'sourceIpAddress',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(IgmpGroupRange, self).__init__(parent)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The count of multicast groups in a range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def FilterMode(self):
        """
        Returns
        -------
        - str: Define the Group Record type included in the Report messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FilterMode'])
    @FilterMode.setter
    def FilterMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FilterMode'], value)

    @property
    def Increment(self):
        """
        Returns
        -------
        - str: The value used to enumerate all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Increment'])
    @Increment.setter
    def Increment(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Increment'], value)

    @property
    def IpAddress(self):
        """
        Returns
        -------
        - str: The IP address of the first multicast group in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpAddress'])
    @IpAddress.setter
    def IpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpAddress'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: -The name of the range containing multicast groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def SourceCount(self):
        """
        Returns
        -------
        - number: The count of sources in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceCount'])
    @SourceCount.setter
    def SourceCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceCount'], value)

    @property
    def SourceIncrement(self):
        """
        Returns
        -------
        - str: The value used to enumerate all the source addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceIncrement'])
    @SourceIncrement.setter
    def SourceIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceIncrement'], value)

    @property
    def SourceIpAddress(self):
        """
        Returns
        -------
        - str: The starting IP address of a range of sources.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceIpAddress'])
    @SourceIpAddress.setter
    def SourceIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceIpAddress'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str: The type of the multicast group range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    def update(self, Count=None, FilterMode=None, Increment=None, IpAddress=None, Name=None, SourceCount=None, SourceIncrement=None, SourceIpAddress=None, Type=None):
        """Updates igmpGroupRange resource on the server.

        Args
        ----
        - Count (number): The count of multicast groups in a range.
        - FilterMode (str): Define the Group Record type included in the Report messages.
        - Increment (str): The value used to enumerate all the addresses in the range.
        - IpAddress (str): The IP address of the first multicast group in the range.
        - Name (str): -The name of the range containing multicast groups.
        - SourceCount (number): The count of sources in the range.
        - SourceIncrement (str): The value used to enumerate all the source addresses in the range.
        - SourceIpAddress (str): The starting IP address of a range of sources.
        - Type (str): The type of the multicast group range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Count=None, FilterMode=None, Increment=None, IpAddress=None, Name=None, SourceCount=None, SourceIncrement=None, SourceIpAddress=None, Type=None):
        """Adds a new igmpGroupRange resource on the server and adds it to the container.

        Args
        ----
        - Count (number): The count of multicast groups in a range.
        - FilterMode (str): Define the Group Record type included in the Report messages.
        - Increment (str): The value used to enumerate all the addresses in the range.
        - IpAddress (str): The IP address of the first multicast group in the range.
        - Name (str): -The name of the range containing multicast groups.
        - SourceCount (number): The count of sources in the range.
        - SourceIncrement (str): The value used to enumerate all the source addresses in the range.
        - SourceIpAddress (str): The starting IP address of a range of sources.
        - Type (str): The type of the multicast group range.

        Returns
        -------
        - self: This instance with all currently retrieved igmpGroupRange resources using find and the newly added igmpGroupRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained igmpGroupRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, FilterMode=None, Increment=None, IpAddress=None, Name=None, ObjectId=None, SourceCount=None, SourceIncrement=None, SourceIpAddress=None, Type=None):
        """Finds and retrieves igmpGroupRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve igmpGroupRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all igmpGroupRange resources from the server.

        Args
        ----
        - Count (number): The count of multicast groups in a range.
        - FilterMode (str): Define the Group Record type included in the Report messages.
        - Increment (str): The value used to enumerate all the addresses in the range.
        - IpAddress (str): The IP address of the first multicast group in the range.
        - Name (str): -The name of the range containing multicast groups.
        - ObjectId (str): Unique identifier for this object
        - SourceCount (number): The count of sources in the range.
        - SourceIncrement (str): The value used to enumerate all the source addresses in the range.
        - SourceIpAddress (str): The starting IP address of a range of sources.
        - Type (str): The type of the multicast group range.

        Returns
        -------
        - self: This instance with matching igmpGroupRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of igmpGroupRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the igmpGroupRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
