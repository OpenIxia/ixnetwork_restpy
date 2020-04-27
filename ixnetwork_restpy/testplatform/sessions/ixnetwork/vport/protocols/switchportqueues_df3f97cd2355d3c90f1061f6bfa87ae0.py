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


class SwitchPortQueues(Base):
    """Indicates the Queue Range associated with a port range.
    The SwitchPortQueues class encapsulates a list of switchPortQueues resources that are managed by the user.
    A list of resources can be retrieved from the server using the SwitchPortQueues.find() method.
    The list can be managed by using the SwitchPortQueues.add() and SwitchPortQueues.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchPortQueues'

    def __init__(self, parent):
        super(SwitchPortQueues, self).__init__(parent)

    @property
    def QueueProperty(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueproperty_ca8559bf68a899ed1e84fdde441b0eeb.QueueProperty): An instance of the QueueProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueproperty_ca8559bf68a899ed1e84fdde441b0eeb import QueueProperty
        return QueueProperty(self)._select()

    @property
    def MinRate(self):
        """
        Returns
        -------
        - str: Indicates the minimum-rate, in 1/10 of a percent, applicable when queue property is OFPQT_MIN.
        """
        return self._get_attribute('minRate')
    @MinRate.setter
    def MinRate(self, value):
        self._set_attribute('minRate', value)

    @property
    def NumberOfQueues(self):
        """
        Returns
        -------
        - number: Specifies the number of entries in the queue range.
        """
        return self._get_attribute('numberOfQueues')
    @NumberOfQueues.setter
    def NumberOfQueues(self, value):
        self._set_attribute('numberOfQueues', value)

    @property
    def QueueId(self):
        """
        Returns
        -------
        - str: Indicates the ID for the specific queue.
        """
        return self._get_attribute('queueId')
    @QueueId.setter
    def QueueId(self, value):
        self._set_attribute('queueId', value)

    def update(self, MinRate=None, NumberOfQueues=None, QueueId=None):
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
        return self._update(locals())

    def add(self, MinRate=None, NumberOfQueues=None, QueueId=None):
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
        return self._create(locals())

    def remove(self):
        """Deletes all the contained switchPortQueues resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, MinRate=None, NumberOfQueues=None, QueueId=None):
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
        return self._select(locals())

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
