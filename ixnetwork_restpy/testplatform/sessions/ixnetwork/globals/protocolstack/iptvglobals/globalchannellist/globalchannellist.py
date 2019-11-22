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


class GlobalChannelList(Base):
    """
    The GlobalChannelList class encapsulates a list of globalChannelList resources that is be managed by the user.
    A list of resources can be retrieved from the server using the GlobalChannelList.find() method.
    The list can be managed by the user by using the GlobalChannelList.add() and GlobalChannelList.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'globalChannelList'

    def __init__(self, parent):
        super(GlobalChannelList, self).__init__(parent)

    @property
    def FirstChannel(self):
        """The first channel from the multicast group range included in the current list.

        Returns:
            number
        """
        return self._get_attribute('firstChannel')
    @FirstChannel.setter
    def FirstChannel(self, value):
        self._set_attribute('firstChannel', value)

    @property
    def Increment(self):
        """The increment step between first and last channels describing available channels.

        Returns:
            number
        """
        return self._get_attribute('increment')
    @Increment.setter
    def Increment(self, value):
        self._set_attribute('increment', value)

    @property
    def InitialChannel(self):
        """The first channel to be joined by the first host.

        Returns:
            number
        """
        return self._get_attribute('initialChannel')
    @InitialChannel.setter
    def InitialChannel(self, value):
        self._set_attribute('initialChannel', value)

    @property
    def InitialIncrement(self):
        """The increment step between consecutive hosts joining the channels.

        Returns:
            number
        """
        return self._get_attribute('initialIncrement')
    @InitialIncrement.setter
    def InitialIncrement(self, value):
        self._set_attribute('initialIncrement', value)

    @property
    def LastChannel(self):
        """The last channel from the multicast group range included in the current list.

        Returns:
            number
        """
        return self._get_attribute('lastChannel')
    @LastChannel.setter
    def LastChannel(self, value):
        self._set_attribute('lastChannel', value)

    @property
    def MulticastGroup(self):
        """The associated multicast group range for defining the channels.

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=igmpGroupRange)
        """
        return self._get_attribute('multicastGroup')
    @MulticastGroup.setter
    def MulticastGroup(self, value):
        self._set_attribute('multicastGroup', value)

    @property
    def Name(self):
        """The name of the channel list.

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

    def update(self, FirstChannel=None, Increment=None, InitialChannel=None, InitialIncrement=None, LastChannel=None, MulticastGroup=None, Name=None):
        """Updates a child instance of globalChannelList on the server.

        Args:
            FirstChannel (number): The first channel from the multicast group range included in the current list.
            Increment (number): The increment step between first and last channels describing available channels.
            InitialChannel (number): The first channel to be joined by the first host.
            InitialIncrement (number): The increment step between consecutive hosts joining the channels.
            LastChannel (number): The last channel from the multicast group range included in the current list.
            MulticastGroup (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=igmpGroupRange)): The associated multicast group range for defining the channels.
            Name (str): The name of the channel list.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, FirstChannel=None, Increment=None, InitialChannel=None, InitialIncrement=None, LastChannel=None, MulticastGroup=None, Name=None):
        """Adds a new globalChannelList node on the server and retrieves it in this instance.

        Args:
            FirstChannel (number): The first channel from the multicast group range included in the current list.
            Increment (number): The increment step between first and last channels describing available channels.
            InitialChannel (number): The first channel to be joined by the first host.
            InitialIncrement (number): The increment step between consecutive hosts joining the channels.
            LastChannel (number): The last channel from the multicast group range included in the current list.
            MulticastGroup (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=igmpGroupRange)): The associated multicast group range for defining the channels.
            Name (str): The name of the channel list.

        Returns:
            self: This instance with all currently retrieved globalChannelList data using find and the newly added globalChannelList data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the globalChannelList data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, FirstChannel=None, Increment=None, InitialChannel=None, InitialIncrement=None, LastChannel=None, MulticastGroup=None, Name=None, ObjectId=None):
        """Finds and retrieves globalChannelList data from the server.

        All named parameters support regex and can be used to selectively retrieve globalChannelList data from the server.
        By default the find method takes no parameters and will retrieve all globalChannelList data from the server.

        Args:
            FirstChannel (number): The first channel from the multicast group range included in the current list.
            Increment (number): The increment step between first and last channels describing available channels.
            InitialChannel (number): The first channel to be joined by the first host.
            InitialIncrement (number): The increment step between consecutive hosts joining the channels.
            LastChannel (number): The last channel from the multicast group range included in the current list.
            MulticastGroup (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=igmpGroupRange)): The associated multicast group range for defining the channels.
            Name (str): The name of the channel list.
            ObjectId (str): Unique identifier for this object

        Returns:
            self: This instance with matching globalChannelList data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of globalChannelList data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the globalChannelList data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
