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


class Bfd(Base):
    """Simulates one or more BFD routers in a network of routers.
    The Bfd class encapsulates a required bfd resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bfd'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'IntervalValue': 'intervalValue',
        'PacketsPerInterval': 'packetsPerInterval',
        'RunningState': 'runningState',
    }
    _SDM_ENUM_MAP = {
        'runningState': ['unknown', 'stopped', 'stopping', 'starting', 'started'],
    }

    def __init__(self, parent, list_op=False):
        super(Bfd, self).__init__(parent, list_op)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_8fefbefd4c6343cce300aae644040cd2.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_8fefbefd4c6343cce300aae644040cd2 import Router
        if self._properties.get('Router', None) is not None:
            return self._properties.get('Router')
        else:
            return Router(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables the use of this emulated BFD router in the emulated BFD network. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IntervalValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Interval Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['IntervalValue'])
    @IntervalValue.setter
    def IntervalValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['IntervalValue'], value)

    @property
    def PacketsPerInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of BFD control packets per interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketsPerInterval'])
    @PacketsPerInterval.setter
    def PacketsPerInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PacketsPerInterval'], value)

    @property
    def RunningState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of the BFD protocol.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningState'])

    def update(self, Enabled=None, IntervalValue=None, PacketsPerInterval=None):
        # type: (bool, int, int) -> Bfd
        """Updates bfd resource on the server.

        Args
        ----
        - Enabled (bool): Enables or disables the use of this emulated BFD router in the emulated BFD network. (default = disabled)
        - IntervalValue (number): Interval Value
        - PacketsPerInterval (number): Number of BFD control packets per interval.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the BFD protocol on a port or group of ports.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the BFD protocol on a port or group of ports.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
