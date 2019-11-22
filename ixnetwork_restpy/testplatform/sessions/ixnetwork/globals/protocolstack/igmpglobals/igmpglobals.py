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


class IgmpGlobals(Base):
    """
    The IgmpGlobals class encapsulates a list of igmpGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the IgmpGlobals.find() method.
    The list can be managed by the user by using the IgmpGlobals.add() and IgmpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'igmpGlobals'

    def __init__(self, parent):
        super(IgmpGlobals, self).__init__(parent)

    @property
    def IgmpGroupRange(self):
        """An instance of the IgmpGroupRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.igmpglobals.igmpgrouprange.igmpgrouprange.IgmpGroupRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.igmpglobals.igmpgrouprange.igmpgrouprange import IgmpGroupRange
        return IgmpGroupRange(self)

    @property
    def MaxPacketsPerSecond(self):
        """The maximum number of requests transmitted in each second.

        Returns:
            number
        """
        return self._get_attribute('maxPacketsPerSecond')
    @MaxPacketsPerSecond.setter
    def MaxPacketsPerSecond(self, value):
        self._set_attribute('maxPacketsPerSecond', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    def update(self, MaxPacketsPerSecond=None):
        """Updates a child instance of igmpGlobals on the server.

        Args:
            MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, MaxPacketsPerSecond=None):
        """Adds a new igmpGlobals node on the server and retrieves it in this instance.

        Args:
            MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.

        Returns:
            self: This instance with all currently retrieved igmpGlobals data using find and the newly added igmpGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the igmpGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, MaxPacketsPerSecond=None, ObjectId=None):
        """Finds and retrieves igmpGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve igmpGlobals data from the server.
        By default the find method takes no parameters and will retrieve all igmpGlobals data from the server.

        Args:
            MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
            ObjectId (str): Unique identifier for this object

        Returns:
            self: This instance with matching igmpGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of igmpGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the igmpGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
