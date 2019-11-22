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


class IgmpGroupRange(Base):
    """
    The IgmpGroupRange class encapsulates a list of igmpGroupRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the IgmpGroupRange.find() method.
    The list can be managed by the user by using the IgmpGroupRange.add() and IgmpGroupRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'igmpGroupRange'

    def __init__(self, parent):
        super(IgmpGroupRange, self).__init__(parent)

    @property
    def Count(self):
        """The count of multicast groups in a range.

        Returns:
            number
        """
        return self._get_attribute('count')
    @Count.setter
    def Count(self, value):
        self._set_attribute('count', value)

    @property
    def FilterMode(self):
        """Define the Group Record type included in the Report messages.

        Returns:
            str
        """
        return self._get_attribute('filterMode')
    @FilterMode.setter
    def FilterMode(self, value):
        self._set_attribute('filterMode', value)

    @property
    def Increment(self):
        """The value used to enumerate all the addresses in the range.

        Returns:
            str
        """
        return self._get_attribute('increment')
    @Increment.setter
    def Increment(self, value):
        self._set_attribute('increment', value)

    @property
    def IpAddress(self):
        """The IP address of the first multicast group in the range.

        Returns:
            str
        """
        return self._get_attribute('ipAddress')
    @IpAddress.setter
    def IpAddress(self, value):
        self._set_attribute('ipAddress', value)

    @property
    def Name(self):
        """-The name of the range containing multicast groups.

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def SourceCount(self):
        """The count of sources in the range.

        Returns:
            number
        """
        return self._get_attribute('sourceCount')
    @SourceCount.setter
    def SourceCount(self, value):
        self._set_attribute('sourceCount', value)

    @property
    def SourceIncrement(self):
        """The value used to enumerate all the source addresses in the range.

        Returns:
            str
        """
        return self._get_attribute('sourceIncrement')
    @SourceIncrement.setter
    def SourceIncrement(self, value):
        self._set_attribute('sourceIncrement', value)

    @property
    def SourceIpAddress(self):
        """The starting IP address of a range of sources.

        Returns:
            str
        """
        return self._get_attribute('sourceIpAddress')
    @SourceIpAddress.setter
    def SourceIpAddress(self, value):
        self._set_attribute('sourceIpAddress', value)

    @property
    def Type(self):
        """The type of the multicast group range.

        Returns:
            str
        """
        return self._get_attribute('type')
    @Type.setter
    def Type(self, value):
        self._set_attribute('type', value)

    def update(self, Count=None, FilterMode=None, Increment=None, IpAddress=None, Name=None, SourceCount=None, SourceIncrement=None, SourceIpAddress=None, Type=None):
        """Updates a child instance of igmpGroupRange on the server.

        Args:
            Count (number): The count of multicast groups in a range.
            FilterMode (str): Define the Group Record type included in the Report messages.
            Increment (str): The value used to enumerate all the addresses in the range.
            IpAddress (str): The IP address of the first multicast group in the range.
            Name (str): -The name of the range containing multicast groups.
            SourceCount (number): The count of sources in the range.
            SourceIncrement (str): The value used to enumerate all the source addresses in the range.
            SourceIpAddress (str): The starting IP address of a range of sources.
            Type (str): The type of the multicast group range.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Count=None, FilterMode=None, Increment=None, IpAddress=None, Name=None, SourceCount=None, SourceIncrement=None, SourceIpAddress=None, Type=None):
        """Adds a new igmpGroupRange node on the server and retrieves it in this instance.

        Args:
            Count (number): The count of multicast groups in a range.
            FilterMode (str): Define the Group Record type included in the Report messages.
            Increment (str): The value used to enumerate all the addresses in the range.
            IpAddress (str): The IP address of the first multicast group in the range.
            Name (str): -The name of the range containing multicast groups.
            SourceCount (number): The count of sources in the range.
            SourceIncrement (str): The value used to enumerate all the source addresses in the range.
            SourceIpAddress (str): The starting IP address of a range of sources.
            Type (str): The type of the multicast group range.

        Returns:
            self: This instance with all currently retrieved igmpGroupRange data using find and the newly added igmpGroupRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the igmpGroupRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, FilterMode=None, Increment=None, IpAddress=None, Name=None, ObjectId=None, SourceCount=None, SourceIncrement=None, SourceIpAddress=None, Type=None):
        """Finds and retrieves igmpGroupRange data from the server.

        All named parameters support regex and can be used to selectively retrieve igmpGroupRange data from the server.
        By default the find method takes no parameters and will retrieve all igmpGroupRange data from the server.

        Args:
            Count (number): The count of multicast groups in a range.
            FilterMode (str): Define the Group Record type included in the Report messages.
            Increment (str): The value used to enumerate all the addresses in the range.
            IpAddress (str): The IP address of the first multicast group in the range.
            Name (str): -The name of the range containing multicast groups.
            ObjectId (str): Unique identifier for this object
            SourceCount (number): The count of sources in the range.
            SourceIncrement (str): The value used to enumerate all the source addresses in the range.
            SourceIpAddress (str): The starting IP address of a range of sources.
            Type (str): The type of the multicast group range.

        Returns:
            self: This instance with matching igmpGroupRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of igmpGroupRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the igmpGroupRange data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
