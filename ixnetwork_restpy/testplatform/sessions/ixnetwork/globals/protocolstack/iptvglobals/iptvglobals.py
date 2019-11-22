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


class IptvGlobals(Base):
    """
    The IptvGlobals class encapsulates a list of iptvGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the IptvGlobals.find() method.
    The list can be managed by the user by using the IptvGlobals.add() and IptvGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'iptvGlobals'

    def __init__(self, parent):
        super(IptvGlobals, self).__init__(parent)

    @property
    def GlobalChannelList(self):
        """An instance of the GlobalChannelList class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.iptvglobals.globalchannellist.globalchannellist.GlobalChannelList)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.iptvglobals.globalchannellist.globalchannellist import GlobalChannelList
        return GlobalChannelList(self)

    @property
    def IgmpGroupRange(self):
        """An instance of the IgmpGroupRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.iptvglobals.igmpgrouprange.igmpgrouprange.IgmpGroupRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.iptvglobals.igmpgrouprange.igmpgrouprange import IgmpGroupRange
        return IgmpGroupRange(self)

    @property
    def IptvProfile(self):
        """An instance of the IptvProfile class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.iptvglobals.iptvprofile.iptvprofile.IptvProfile)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.iptvglobals.iptvprofile.iptvprofile import IptvProfile
        return IptvProfile(self)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    def add(self):
        """Adds a new iptvGlobals node on the server and retrieves it in this instance.

        Returns:
            self: This instance with all currently retrieved iptvGlobals data using find and the newly added iptvGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the iptvGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ObjectId=None):
        """Finds and retrieves iptvGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve iptvGlobals data from the server.
        By default the find method takes no parameters and will retrieve all iptvGlobals data from the server.

        Args:
            ObjectId (str): Unique identifier for this object

        Returns:
            self: This instance with matching iptvGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of iptvGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the iptvGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
