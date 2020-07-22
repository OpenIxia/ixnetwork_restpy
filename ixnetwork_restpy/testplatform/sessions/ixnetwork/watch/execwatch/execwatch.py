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


class ExecWatch(Base):
    """
    The ExecWatch class encapsulates a list of execWatch resources that are managed by the user.
    A list of resources can be retrieved from the server using the ExecWatch.find() method.
    The list can be managed by using the ExecWatch.add() and ExecWatch.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'execWatch'
    _SDM_ATT_MAP = {
        'AverageExecutionTime': 'averageExecutionTime',
        'ExecToWatch': 'execToWatch',
        'IsDisabled': 'isDisabled',
        'LastExecutionTime': 'lastExecutionTime',
        'LastNotification': 'lastNotification',
        'MaxExecutionTime': 'maxExecutionTime',
        'PollInterval': 'pollInterval',
        'Token': 'token',
        'Topic': 'topic',
    }

    def __init__(self, parent):
        super(ExecWatch, self).__init__(parent)

    @property
    def AverageExecutionTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AverageExecutionTime'])

    @property
    def ExecToWatch(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExecToWatch'])
    @ExecToWatch.setter
    def ExecToWatch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExecToWatch'], value)

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

    def update(self, ExecToWatch=None, MaxExecutionTime=None, PollInterval=None, Topic=None):
        """Updates execWatch resource on the server.

        Args
        ----
        - ExecToWatch (str): 
        - MaxExecutionTime (number): The maximum amount of time a watch can take in milliseconds. If the execution time exceeds this value the watch will be disabled.To bypass this check set the value to 0.
        - PollInterval (number): The interval in milliseconds the watch will be polled. Minimum value is 100ms.
        - Topic (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ExecToWatch=None, MaxExecutionTime=None, PollInterval=None, Topic=None):
        """Adds a new execWatch resource on the server and adds it to the container.

        Args
        ----
        - ExecToWatch (str): 
        - MaxExecutionTime (number): The maximum amount of time a watch can take in milliseconds. If the execution time exceeds this value the watch will be disabled.To bypass this check set the value to 0.
        - PollInterval (number): The interval in milliseconds the watch will be polled. Minimum value is 100ms.
        - Topic (str): 

        Returns
        -------
        - self: This instance with all currently retrieved execWatch resources using find and the newly added execWatch resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained execWatch resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AverageExecutionTime=None, ExecToWatch=None, IsDisabled=None, LastExecutionTime=None, LastNotification=None, MaxExecutionTime=None, PollInterval=None, Token=None, Topic=None):
        """Finds and retrieves execWatch resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve execWatch resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all execWatch resources from the server.

        Args
        ----
        - AverageExecutionTime (number): 
        - ExecToWatch (str): 
        - IsDisabled (bool): 
        - LastExecutionTime (number): 
        - LastNotification (str): 
        - MaxExecutionTime (number): The maximum amount of time a watch can take in milliseconds. If the execution time exceeds this value the watch will be disabled.To bypass this check set the value to 0.
        - PollInterval (number): The interval in milliseconds the watch will be polled. Minimum value is 100ms.
        - Token (number): 
        - Topic (str): 

        Returns
        -------
        - self: This instance with matching execWatch resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of execWatch data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the execWatch resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
