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


class IgmpGlobals(Base):
    """
    The IgmpGlobals class encapsulates a list of igmpGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the IgmpGlobals.find() method.
    The list can be managed by using the IgmpGlobals.add() and IgmpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'igmpGlobals'
    _SDM_ATT_MAP = {
        'MaxPacketsPerSecond': 'maxPacketsPerSecond',
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(IgmpGlobals, self).__init__(parent)

    @property
    def IgmpGroupRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.igmpglobals.igmpgrouprange.igmpgrouprange.IgmpGroupRange): An instance of the IgmpGroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.igmpglobals.igmpgrouprange.igmpgrouprange import IgmpGroupRange
        return IgmpGroupRange(self)

    @property
    def MaxPacketsPerSecond(self):
        """
        Returns
        -------
        - number: The maximum number of requests transmitted in each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxPacketsPerSecond'])
    @MaxPacketsPerSecond.setter
    def MaxPacketsPerSecond(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxPacketsPerSecond'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    def update(self, MaxPacketsPerSecond=None):
        """Updates igmpGlobals resource on the server.

        Args
        ----
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, MaxPacketsPerSecond=None):
        """Adds a new igmpGlobals resource on the server and adds it to the container.

        Args
        ----
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.

        Returns
        -------
        - self: This instance with all currently retrieved igmpGlobals resources using find and the newly added igmpGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained igmpGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, MaxPacketsPerSecond=None, ObjectId=None):
        """Finds and retrieves igmpGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve igmpGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all igmpGlobals resources from the server.

        Args
        ----
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching igmpGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of igmpGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the igmpGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
