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


class GlobalChannelList(Base):
    """
    The GlobalChannelList class encapsulates a list of globalChannelList resources that are managed by the user.
    A list of resources can be retrieved from the server using the GlobalChannelList.find() method.
    The list can be managed by using the GlobalChannelList.add() and GlobalChannelList.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'globalChannelList'
    _SDM_ATT_MAP = {
        'FirstChannel': 'firstChannel',
        'Increment': 'increment',
        'InitialChannel': 'initialChannel',
        'InitialIncrement': 'initialIncrement',
        'LastChannel': 'lastChannel',
        'MulticastGroup': 'multicastGroup',
        'Name': 'name',
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(GlobalChannelList, self).__init__(parent)

    @property
    def FirstChannel(self):
        """
        Returns
        -------
        - number: The first channel from the multicast group range included in the current list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstChannel'])
    @FirstChannel.setter
    def FirstChannel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstChannel'], value)

    @property
    def Increment(self):
        """
        Returns
        -------
        - number: The increment step between first and last channels describing available channels.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Increment'])
    @Increment.setter
    def Increment(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Increment'], value)

    @property
    def InitialChannel(self):
        """
        Returns
        -------
        - number: The first channel to be joined by the first host.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialChannel'])
    @InitialChannel.setter
    def InitialChannel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialChannel'], value)

    @property
    def InitialIncrement(self):
        """
        Returns
        -------
        - number: The increment step between consecutive hosts joining the channels.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialIncrement'])
    @InitialIncrement.setter
    def InitialIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialIncrement'], value)

    @property
    def LastChannel(self):
        """
        Returns
        -------
        - number: The last channel from the multicast group range included in the current list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastChannel'])
    @LastChannel.setter
    def LastChannel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LastChannel'], value)

    @property
    def MulticastGroup(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/globals/.../igmpGroupRange): The associated multicast group range for defining the channels.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastGroup'])
    @MulticastGroup.setter
    def MulticastGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastGroup'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: The name of the channel list.
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

    def update(self, FirstChannel=None, Increment=None, InitialChannel=None, InitialIncrement=None, LastChannel=None, MulticastGroup=None, Name=None):
        """Updates globalChannelList resource on the server.

        Args
        ----
        - FirstChannel (number): The first channel from the multicast group range included in the current list.
        - Increment (number): The increment step between first and last channels describing available channels.
        - InitialChannel (number): The first channel to be joined by the first host.
        - InitialIncrement (number): The increment step between consecutive hosts joining the channels.
        - LastChannel (number): The last channel from the multicast group range included in the current list.
        - MulticastGroup (str(None | /api/v1/sessions/1/ixnetwork/globals/.../igmpGroupRange)): The associated multicast group range for defining the channels.
        - Name (str): The name of the channel list.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, FirstChannel=None, Increment=None, InitialChannel=None, InitialIncrement=None, LastChannel=None, MulticastGroup=None, Name=None):
        """Adds a new globalChannelList resource on the server and adds it to the container.

        Args
        ----
        - FirstChannel (number): The first channel from the multicast group range included in the current list.
        - Increment (number): The increment step between first and last channels describing available channels.
        - InitialChannel (number): The first channel to be joined by the first host.
        - InitialIncrement (number): The increment step between consecutive hosts joining the channels.
        - LastChannel (number): The last channel from the multicast group range included in the current list.
        - MulticastGroup (str(None | /api/v1/sessions/1/ixnetwork/globals/.../igmpGroupRange)): The associated multicast group range for defining the channels.
        - Name (str): The name of the channel list.

        Returns
        -------
        - self: This instance with all currently retrieved globalChannelList resources using find and the newly added globalChannelList resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained globalChannelList resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, FirstChannel=None, Increment=None, InitialChannel=None, InitialIncrement=None, LastChannel=None, MulticastGroup=None, Name=None, ObjectId=None):
        """Finds and retrieves globalChannelList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve globalChannelList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all globalChannelList resources from the server.

        Args
        ----
        - FirstChannel (number): The first channel from the multicast group range included in the current list.
        - Increment (number): The increment step between first and last channels describing available channels.
        - InitialChannel (number): The first channel to be joined by the first host.
        - InitialIncrement (number): The increment step between consecutive hosts joining the channels.
        - LastChannel (number): The last channel from the multicast group range included in the current list.
        - MulticastGroup (str(None | /api/v1/sessions/1/ixnetwork/globals/.../igmpGroupRange)): The associated multicast group range for defining the channels.
        - Name (str): The name of the channel list.
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching globalChannelList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of globalChannelList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the globalChannelList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
