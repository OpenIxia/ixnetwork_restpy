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


class SelectWatch(Base):
    """
    The SelectWatch class encapsulates a list of selectWatch resources that is be managed by the user.
    A list of resources can be retrieved from the server using the SelectWatch.find() method.
    The list can be managed by the user by using the SelectWatch.add() and SelectWatch.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'selectWatch'

    def __init__(self, parent):
        super(SelectWatch, self).__init__(parent)

    @property
    def AverageExecutionTime(self):
        """

        Returns:
            number
        """
        return self._get_attribute('averageExecutionTime')

    @property
    def IsDisabled(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('isDisabled')

    @property
    def LastExecutionTime(self):
        """

        Returns:
            number
        """
        return self._get_attribute('lastExecutionTime')

    @property
    def LastNotification(self):
        """

        Returns:
            str
        """
        return self._get_attribute('lastNotification')

    @property
    def MaxExecutionTime(self):
        """The maximum amount of time a watch can take in milliseconds. If the execution time exceeds this value the watch will be disabled.To bypass this check set the value to 0.

        Returns:
            number
        """
        return self._get_attribute('maxExecutionTime')
    @MaxExecutionTime.setter
    def MaxExecutionTime(self, value):
        self._set_attribute('maxExecutionTime', value)

    @property
    def PollInterval(self):
        """The interval in milliseconds the watch will be polled. Minimum value is 2000ms.

        Returns:
            number
        """
        return self._get_attribute('pollInterval')
    @PollInterval.setter
    def PollInterval(self, value):
        self._set_attribute('pollInterval', value)

    @property
    def Selects(self):
        """

        Returns:
            list(dict(from:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],properties:list[str],children:list[dict(child:str,properties:list[str],filters:list[dict(property:str,regex:str)])],inlines:list[dict(node:str,properties:list[str])]))
        """
        return self._get_attribute('selects')
    @Selects.setter
    def Selects(self, value):
        self._set_attribute('selects', value)

    @property
    def Token(self):
        """

        Returns:
            number
        """
        return self._get_attribute('token')

    @property
    def Topic(self):
        """

        Returns:
            str
        """
        return self._get_attribute('topic')
    @Topic.setter
    def Topic(self, value):
        self._set_attribute('topic', value)

    def update(self, MaxExecutionTime=None, PollInterval=None, Selects=None, Topic=None):
        """Updates a child instance of selectWatch on the server.

        Args:
            MaxExecutionTime (number): The maximum amount of time a watch can take in milliseconds. If the execution time exceeds this value the watch will be disabled.To bypass this check set the value to 0.
            PollInterval (number): The interval in milliseconds the watch will be polled. Minimum value is 2000ms.
            Selects (list(dict(from:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],properties:list[str],children:list[dict(child:str,properties:list[str],filters:list[dict(property:str,regex:str)])],inlines:list[dict(node:str,properties:list[str])]))): 
            Topic (str): 

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, MaxExecutionTime=None, PollInterval=None, Selects=None, Topic=None):
        """Adds a new selectWatch node on the server and retrieves it in this instance.

        Args:
            MaxExecutionTime (number): The maximum amount of time a watch can take in milliseconds. If the execution time exceeds this value the watch will be disabled.To bypass this check set the value to 0.
            PollInterval (number): The interval in milliseconds the watch will be polled. Minimum value is 2000ms.
            Selects (list(dict(from:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],properties:list[str],children:list[dict(child:str,properties:list[str],filters:list[dict(property:str,regex:str)])],inlines:list[dict(node:str,properties:list[str])]))): 
            Topic (str): 

        Returns:
            self: This instance with all currently retrieved selectWatch data using find and the newly added selectWatch data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the selectWatch data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AverageExecutionTime=None, IsDisabled=None, LastExecutionTime=None, LastNotification=None, MaxExecutionTime=None, PollInterval=None, Selects=None, Token=None, Topic=None):
        """Finds and retrieves selectWatch data from the server.

        All named parameters support regex and can be used to selectively retrieve selectWatch data from the server.
        By default the find method takes no parameters and will retrieve all selectWatch data from the server.

        Args:
            AverageExecutionTime (number): 
            IsDisabled (bool): 
            LastExecutionTime (number): 
            LastNotification (str): 
            MaxExecutionTime (number): The maximum amount of time a watch can take in milliseconds. If the execution time exceeds this value the watch will be disabled.To bypass this check set the value to 0.
            PollInterval (number): The interval in milliseconds the watch will be polled. Minimum value is 2000ms.
            Selects (list(dict(from:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],properties:list[str],children:list[dict(child:str,properties:list[str],filters:list[dict(property:str,regex:str)])],inlines:list[dict(node:str,properties:list[str])]))): 
            Token (number): 
            Topic (str): 

        Returns:
            self: This instance with matching selectWatch data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of selectWatch data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the selectWatch data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
