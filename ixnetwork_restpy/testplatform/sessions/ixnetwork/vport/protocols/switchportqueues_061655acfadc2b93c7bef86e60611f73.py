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
    """A high level object that allows to define the Swicth Port Queues configuration. An OpenFlow switch provides limited Quality-of-Service support (QoS) through a simple queuing mechanism. One (or more) queues can attach to a port and be used to map flow entries on it. Flow entries mapped to a specific queue are treated according to that configuration of the queue.
    The SwitchPortQueues class encapsulates a list of switchPortQueues resources that is be managed by the user.
    A list of resources can be retrieved from the server using the SwitchPortQueues.find() method.
    The list can be managed by the user by using the SwitchPortQueues.add() and SwitchPortQueues.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switchPortQueues'

    def __init__(self, parent):
        super(SwitchPortQueues, self).__init__(parent)

    @property
    def QueueProperty(self):
        """An instance of the QueueProperty class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueproperty_6be0034beb04041ef5bfafdf6a15ea2d.QueueProperty)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueproperty_6be0034beb04041ef5bfafdf6a15ea2d import QueueProperty
        return QueueProperty(self)._select()

    @property
    def MaxRate(self):
        """Specify the maximum data rate guaranteed. The default value is 1. This field is available only when the Queue Property is Maximum data rate.

        Returns:
            str
        """
        return self._get_attribute('maxRate')
    @MaxRate.setter
    def MaxRate(self, value):
        self._set_attribute('maxRate', value)

    @property
    def MinRate(self):
        """Specify the minimum data rate guaranteed. The default value is 1. This field is available only when the Queue Property is Minimum data rate Guaranteed.

        Returns:
            str
        """
        return self._get_attribute('minRate')
    @MinRate.setter
    def MinRate(self, value):
        self._set_attribute('minRate', value)

    @property
    def NumberOfQueues(self):
        """Specify the number of port queues to be configured. The default value is 1.

        Returns:
            number
        """
        return self._get_attribute('numberOfQueues')
    @NumberOfQueues.setter
    def NumberOfQueues(self, value):
        self._set_attribute('numberOfQueues', value)

    @property
    def QueueId(self):
        """Specify the queue identifier for the packets.

        Returns:
            str
        """
        return self._get_attribute('queueId')
    @QueueId.setter
    def QueueId(self, value):
        self._set_attribute('queueId', value)

    def update(self, MaxRate=None, MinRate=None, NumberOfQueues=None, QueueId=None):
        """Updates a child instance of switchPortQueues on the server.

        Args:
            MaxRate (str): Specify the maximum data rate guaranteed. The default value is 1. This field is available only when the Queue Property is Maximum data rate.
            MinRate (str): Specify the minimum data rate guaranteed. The default value is 1. This field is available only when the Queue Property is Minimum data rate Guaranteed.
            NumberOfQueues (number): Specify the number of port queues to be configured. The default value is 1.
            QueueId (str): Specify the queue identifier for the packets.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, MaxRate=None, MinRate=None, NumberOfQueues=None, QueueId=None):
        """Adds a new switchPortQueues node on the server and retrieves it in this instance.

        Args:
            MaxRate (str): Specify the maximum data rate guaranteed. The default value is 1. This field is available only when the Queue Property is Maximum data rate.
            MinRate (str): Specify the minimum data rate guaranteed. The default value is 1. This field is available only when the Queue Property is Minimum data rate Guaranteed.
            NumberOfQueues (number): Specify the number of port queues to be configured. The default value is 1.
            QueueId (str): Specify the queue identifier for the packets.

        Returns:
            self: This instance with all currently retrieved switchPortQueues data using find and the newly added switchPortQueues data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the switchPortQueues data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, MaxRate=None, MinRate=None, NumberOfQueues=None, QueueId=None):
        """Finds and retrieves switchPortQueues data from the server.

        All named parameters support regex and can be used to selectively retrieve switchPortQueues data from the server.
        By default the find method takes no parameters and will retrieve all switchPortQueues data from the server.

        Args:
            MaxRate (str): Specify the maximum data rate guaranteed. The default value is 1. This field is available only when the Queue Property is Maximum data rate.
            MinRate (str): Specify the minimum data rate guaranteed. The default value is 1. This field is available only when the Queue Property is Minimum data rate Guaranteed.
            NumberOfQueues (number): Specify the number of port queues to be configured. The default value is 1.
            QueueId (str): Specify the queue identifier for the packets.

        Returns:
            self: This instance with matching switchPortQueues data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of switchPortQueues data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the switchPortQueues data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
