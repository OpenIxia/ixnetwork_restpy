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


class AttributeWatch(Base):
    """
    The AttributeWatch class encapsulates a list of attributeWatch resources that are managed by the user.
    A list of resources can be retrieved from the server using the AttributeWatch.find() method.
    The list can be managed by using the AttributeWatch.add() and AttributeWatch.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'attributeWatch'
    _SDM_ATT_MAP = {
        'AttributesToWatch': 'attributesToWatch',
        'AverageExecutionTime': 'averageExecutionTime',
        'IsDisabled': 'isDisabled',
        'LastExecutionTime': 'lastExecutionTime',
        'LastNotification': 'lastNotification',
        'MaxExecutionTime': 'maxExecutionTime',
        'ObjectIdToWatch': 'objectIdToWatch',
        'PollInterval': 'pollInterval',
        'Token': 'token',
        'Topic': 'topic',
    }

    def __init__(self, parent):
        super(AttributeWatch, self).__init__(parent)

    @property
    def AttributesToWatch(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AttributesToWatch'])
    @AttributesToWatch.setter
    def AttributesToWatch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AttributesToWatch'], value)

    @property
    def AverageExecutionTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AverageExecutionTime'])

    @property
    def IsDisabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsDisabled'])

    @property
    def LastExecutionTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastExecutionTime'])

    @property
    def LastNotification(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastNotification'])

    @property
    def MaxExecutionTime(self):
        """
        Returns
        -------
        - number: The maximum amount of time a watch can take in milliseconds. If the execution time exceeds this value the watch will be disabled.To bypass this check set the value to 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxExecutionTime'])
    @MaxExecutionTime.setter
    def MaxExecutionTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxExecutionTime'], value)

    @property
    def ObjectIdToWatch(self):
        """
        Returns
        -------
        - str(None): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectIdToWatch'])
    @ObjectIdToWatch.setter
    def ObjectIdToWatch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ObjectIdToWatch'], value)

    @property
    def PollInterval(self):
        """
        Returns
        -------
        - number: The interval in milliseconds the watch will be polled. Minimum value is 100ms.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PollInterval'])
    @PollInterval.setter
    def PollInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PollInterval'], value)

    @property
    def Token(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Token'])

    @property
    def Topic(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Topic'])
    @Topic.setter
    def Topic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Topic'], value)

    def update(self, AttributesToWatch=None, MaxExecutionTime=None, ObjectIdToWatch=None, PollInterval=None, Topic=None):
        """Updates attributeWatch resource on the server.

        Args
        ----
        - AttributesToWatch (list(str)): 
        - MaxExecutionTime (number): The maximum amount of time a watch can take in milliseconds. If the execution time exceeds this value the watch will be disabled.To bypass this check set the value to 0.
        - ObjectIdToWatch (str(None)): 
        - PollInterval (number): The interval in milliseconds the watch will be polled. Minimum value is 100ms.
        - Topic (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AttributesToWatch=None, MaxExecutionTime=None, ObjectIdToWatch=None, PollInterval=None, Topic=None):
        """Adds a new attributeWatch resource on the server and adds it to the container.

        Args
        ----
        - AttributesToWatch (list(str)): 
        - MaxExecutionTime (number): The maximum amount of time a watch can take in milliseconds. If the execution time exceeds this value the watch will be disabled.To bypass this check set the value to 0.
        - ObjectIdToWatch (str(None)): 
        - PollInterval (number): The interval in milliseconds the watch will be polled. Minimum value is 100ms.
        - Topic (str): 

        Returns
        -------
        - self: This instance with all currently retrieved attributeWatch resources using find and the newly added attributeWatch resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained attributeWatch resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AttributesToWatch=None, AverageExecutionTime=None, IsDisabled=None, LastExecutionTime=None, LastNotification=None, MaxExecutionTime=None, ObjectIdToWatch=None, PollInterval=None, Token=None, Topic=None):
        """Finds and retrieves attributeWatch resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve attributeWatch resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all attributeWatch resources from the server.

        Args
        ----
        - AttributesToWatch (list(str)): 
        - AverageExecutionTime (number): 
        - IsDisabled (bool): 
        - LastExecutionTime (number): 
        - LastNotification (str): 
        - MaxExecutionTime (number): The maximum amount of time a watch can take in milliseconds. If the execution time exceeds this value the watch will be disabled.To bypass this check set the value to 0.
        - ObjectIdToWatch (str(None)): 
        - PollInterval (number): The interval in milliseconds the watch will be polled. Minimum value is 100ms.
        - Token (number): 
        - Topic (str): 

        Returns
        -------
        - self: This instance with matching attributeWatch resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of attributeWatch data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the attributeWatch resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
