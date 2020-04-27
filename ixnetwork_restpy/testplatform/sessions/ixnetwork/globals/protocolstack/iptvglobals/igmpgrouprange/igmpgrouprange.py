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
    The IgmpGroupRange class encapsulates a list of igmpGroupRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the IgmpGroupRange.find() method.
    The list can be managed by using the IgmpGroupRange.add() and IgmpGroupRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'igmpGroupRange'

    def __init__(self, parent):
        super(IgmpGroupRange, self).__init__(parent)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The count of multicast groups in a range.
        """
        return self._get_attribute('count')
    @Count.setter
    def Count(self, value):
        self._set_attribute('count', value)

    @property
    def FilterMode(self):
        """
        Returns
        -------
        - str: Define the Group Record type included in the Report messages.
        """
        return self._get_attribute('filterMode')
    @FilterMode.setter
    def FilterMode(self, value):
        self._set_attribute('filterMode', value)

    @property
    def Increment(self):
        """
        Returns
        -------
        - str: The value used to enumerate all the addresses in the range.
        """
        return self._get_attribute('increment')
    @Increment.setter
    def Increment(self, value):
        self._set_attribute('increment', value)

    @property
    def IpAddress(self):
        """
        Returns
        -------
        - str: The IP address of the first multicast group in the range.
        """
        return self._get_attribute('ipAddress')
    @IpAddress.setter
    def IpAddress(self, value):
        self._set_attribute('ipAddress', value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: -The name of the range containing multicast groups.
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute('objectId')

    @property
    def SourceCount(self):
        """
        Returns
        -------
        - number: The count of sources in the range.
        """
        return self._get_attribute('sourceCount')
    @SourceCount.setter
    def SourceCount(self, value):
        self._set_attribute('sourceCount', value)

    @property
    def SourceIncrement(self):
        """
        Returns
        -------
        - str: The value used to enumerate all the source addresses in the range.
        """
        return self._get_attribute('sourceIncrement')
    @SourceIncrement.setter
    def SourceIncrement(self, value):
        self._set_attribute('sourceIncrement', value)

    @property
    def SourceIpAddress(self):
        """
        Returns
        -------
        - str: The starting IP address of a range of sources.
        """
        return self._get_attribute('sourceIpAddress')
    @SourceIpAddress.setter
    def SourceIpAddress(self, value):
        self._set_attribute('sourceIpAddress', value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str: The type of the multicast group range.
        """
        return self._get_attribute('type')
    @Type.setter
    def Type(self, value):
        self._set_attribute('type', value)

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
        return self._update(locals())

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
        return self._create(locals())

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
        return self._select(locals())

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
