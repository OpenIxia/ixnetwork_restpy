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


class Igmp(Base):
    """This object sends and responds to IGMP messages.
    The Igmp class encapsulates a required igmp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'igmp'

    def __init__(self, parent):
        super(Igmp, self).__init__(parent)

    @property
    def Host(self):
        """An instance of the Host class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.host_8a5fc3b3985507e575b5c694b5f975b3.Host)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.host_8a5fc3b3985507e575b5c694b5f975b3 import Host
        return Host(self)

    @property
    def Querier(self):
        """An instance of the Querier class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.querier_c9823e61c46d8d472c4fca706c674044.Querier)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.querier_c9823e61c46d8d472c4fca706c674044 import Querier
        return Querier(self)

    @property
    def Enabled(self):
        """Enables or disables the use of this emulated EIGRP router in the emulated EIGRP network. (default = disabled)

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def NumberOfGroups(self):
        """Provides a means of throttling the amount of IGMP traffic generated by the port.

        Returns:
            number
        """
        return self._get_attribute('numberOfGroups')
    @NumberOfGroups.setter
    def NumberOfGroups(self, value):
        self._set_attribute('numberOfGroups', value)

    @property
    def NumberOfQueries(self):
        """Provides a means of throttling the amount of IGMP queries generated by the port.

        Returns:
            number
        """
        return self._get_attribute('numberOfQueries')
    @NumberOfQueries.setter
    def NumberOfQueries(self, value):
        self._set_attribute('numberOfQueries', value)

    @property
    def QueryTimePeriod(self):
        """The time, in milliseconds, between queries.

        Returns:
            number
        """
        return self._get_attribute('queryTimePeriod')
    @QueryTimePeriod.setter
    def QueryTimePeriod(self, value):
        self._set_attribute('queryTimePeriod', value)

    @property
    def RunningState(self):
        """The current running state of the IGMP server.

        Returns:
            str(unknown|stopped|stopping|starting|started)
        """
        return self._get_attribute('runningState')

    @property
    def SendLeaveOnHostDisable(self):
        """Send Leave On Host Disable

        Returns:
            bool
        """
        return self._get_attribute('sendLeaveOnHostDisable')
    @SendLeaveOnHostDisable.setter
    def SendLeaveOnHostDisable(self, value):
        self._set_attribute('sendLeaveOnHostDisable', value)

    @property
    def SendLeaveOnStop(self):
        """Send leaves on stop (v2 and v3 only).

        Returns:
            bool
        """
        return self._get_attribute('sendLeaveOnStop')
    @SendLeaveOnStop.setter
    def SendLeaveOnStop(self, value):
        self._set_attribute('sendLeaveOnStop', value)

    @property
    def StatsEnabled(self):
        """If true, this object enables the IGMP statistics.

        Returns:
            bool
        """
        return self._get_attribute('statsEnabled')
    @StatsEnabled.setter
    def StatsEnabled(self, value):
        self._set_attribute('statsEnabled', value)

    @property
    def TimePeriod(self):
        """Specifies the length of each time period during which the specified number of IGMP groups will be advertised.

        Returns:
            number
        """
        return self._get_attribute('timePeriod')
    @TimePeriod.setter
    def TimePeriod(self, value):
        self._set_attribute('timePeriod', value)

    def update(self, Enabled=None, NumberOfGroups=None, NumberOfQueries=None, QueryTimePeriod=None, SendLeaveOnHostDisable=None, SendLeaveOnStop=None, StatsEnabled=None, TimePeriod=None):
        """Updates a child instance of igmp on the server.

        Args:
            Enabled (bool): Enables or disables the use of this emulated EIGRP router in the emulated EIGRP network. (default = disabled)
            NumberOfGroups (number): Provides a means of throttling the amount of IGMP traffic generated by the port.
            NumberOfQueries (number): Provides a means of throttling the amount of IGMP queries generated by the port.
            QueryTimePeriod (number): The time, in milliseconds, between queries.
            SendLeaveOnHostDisable (bool): Send Leave On Host Disable
            SendLeaveOnStop (bool): Send leaves on stop (v2 and v3 only).
            StatsEnabled (bool): If true, this object enables the IGMP statistics.
            TimePeriod (number): Specifies the length of each time period during which the specified number of IGMP groups will be advertised.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def Join(self, *args, **kwargs):
        """Executes the join operation on the server.

        NOT DEFINED

        join(Arg2:string, Arg3:number)
            Args:
                args[0] is Arg2 (str): NOT DEFINED
                args[1] is Arg3 (number): NOT DEFINED

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('join', payload=payload, response_object=None)

    def Leave(self, *args, **kwargs):
        """Executes the leave operation on the server.

        NOT DEFINED

        leave(Arg2:string, Arg3:number)
            Args:
                args[0] is Arg2 (str): NOT DEFINED
                args[1] is Arg3 (number): NOT DEFINED

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('leave', payload=payload, response_object=None)

    def Start(self):
        """Executes the start operation on the server.

        Starts the EIGRP protocol on a port or group of ports simultaneously.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the IGMP protocol on a port or group of ports simultaneously.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
