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
from typing import List, Any, Union


class SwitchPortQueues(Base):
    """Indicates the Queue Range associated with a port range.
    The SwitchPortQueues class encapsulates a list of switchPortQueues resources that are managed by the user.
    A list of resources can be retrieved from the server using the SwitchPortQueues.find() method.
    The list can be managed by using the SwitchPortQueues.add() and SwitchPortQueues.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchPortQueues'
    _SDM_ATT_MAP = {
        'MinRate': 'minRate',
        'NumberOfQueues': 'numberOfQueues',
        'QueueId': 'queueId',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(SwitchPortQueues, self).__init__(parent, list_op)

    @property
    def QueueProperty(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueproperty_28ede609f33dc123ae3579c11376d90b.QueueProperty): An instance of the QueueProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueproperty_28ede609f33dc123ae3579c11376d90b import QueueProperty
        if self._properties.get('QueueProperty', None) is not None:
            return self._properties.get('QueueProperty')
        else:
            return QueueProperty(self)._select()

    @property
    def MinRate(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the minimum-rate, in 1/10 of a percent, applicable when queue property is OFPQT_MIN.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRate'])
    @MinRate.setter
    def MinRate(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinRate'], value)

    @property
    def NumberOfQueues(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the number of entries in the queue range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfQueues'])
    @NumberOfQueues.setter
    def NumberOfQueues(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfQueues'], value)

    @property
    def QueueId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the ID for the specific queue.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueId'])
    @QueueId.setter
    def QueueId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['QueueId'], value)

    def update(self, MinRate=None, NumberOfQueues=None, QueueId=None):
        # type: (str, int, str) -> SwitchPortQueues
        """Updates switchPortQueues resource on the server.

        Args
        ----
        - MinRate (str): Indicates the minimum-rate, in 1/10 of a percent, applicable when queue property is OFPQT_MIN.
        - NumberOfQueues (number): Specifies the number of entries in the queue range.
        - QueueId (str): Indicates the ID for the specific queue.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, MinRate=None, NumberOfQueues=None, QueueId=None):
        # type: (str, int, str) -> SwitchPortQueues
        """Adds a new switchPortQueues resource on the server and adds it to the container.

        Args
        ----
        - MinRate (str): Indicates the minimum-rate, in 1/10 of a percent, applicable when queue property is OFPQT_MIN.
        - NumberOfQueues (number): Specifies the number of entries in the queue range.
        - QueueId (str): Indicates the ID for the specific queue.

        Returns
        -------
        - self: This instance with all currently retrieved switchPortQueues resources using find and the newly added switchPortQueues resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained switchPortQueues resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, MinRate=None, NumberOfQueues=None, QueueId=None):
        # type: (str, int, str) -> SwitchPortQueues
        """Finds and retrieves switchPortQueues resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchPortQueues resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchPortQueues resources from the server.

        Args
        ----
        - MinRate (str): Indicates the minimum-rate, in 1/10 of a percent, applicable when queue property is OFPQT_MIN.
        - NumberOfQueues (number): Specifies the number of entries in the queue range.
        - QueueId (str): Indicates the ID for the specific queue.

        Returns
        -------
        - self: This instance with matching switchPortQueues resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchPortQueues data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchPortQueues resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
