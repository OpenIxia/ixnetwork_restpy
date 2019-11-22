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


class Ospf(Base):
    """This object simulates one or more OSPF routers in a network of routers.
    The Ospf class encapsulates a required ospf resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ospf'

    def __init__(self, parent):
        super(Ospf, self).__init__(parent)

    @property
    def Router(self):
        """An instance of the Router class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_527fd224df416456371158e8ee44dd5e.Router)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_527fd224df416456371158e8ee44dd5e import Router
        return Router(self)

    @property
    def EnableDrOrBdr(self):
        """If true, enables this router as the Designated (DR) or Backup Designated Router (BDR).

        Returns:
            bool
        """
        return self._get_attribute('enableDrOrBdr')
    @EnableDrOrBdr.setter
    def EnableDrOrBdr(self, value):
        self._set_attribute('enableDrOrBdr', value)

    @property
    def Enabled(self):
        """Enables this emulated OSPF router.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def FloodLinkStateUpdatesPerInterval(self):
        """Sets the number of Flood Link State Updates to be sent in each rate control interval.

        Returns:
            number
        """
        return self._get_attribute('floodLinkStateUpdatesPerInterval')
    @FloodLinkStateUpdatesPerInterval.setter
    def FloodLinkStateUpdatesPerInterval(self, value):
        self._set_attribute('floodLinkStateUpdatesPerInterval', value)

    @property
    def RateControlInterval(self):
        """Enables the option Rate Control Interval to define a value.

        Returns:
            number
        """
        return self._get_attribute('rateControlInterval')
    @RateControlInterval.setter
    def RateControlInterval(self, value):
        self._set_attribute('rateControlInterval', value)

    @property
    def RunningState(self):
        """The current state of the OSPF router.

        Returns:
            str(unknown|stopped|stopping|starting|started)
        """
        return self._get_attribute('runningState')

    def update(self, EnableDrOrBdr=None, Enabled=None, FloodLinkStateUpdatesPerInterval=None, RateControlInterval=None):
        """Updates a child instance of ospf on the server.

        Args:
            EnableDrOrBdr (bool): If true, enables this router as the Designated (DR) or Backup Designated Router (BDR).
            Enabled (bool): Enables this emulated OSPF router.
            FloodLinkStateUpdatesPerInterval (number): Sets the number of Flood Link State Updates to be sent in each rate control interval.
            RateControlInterval (number): Enables the option Rate Control Interval to define a value.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def Start(self):
        """Executes the start operation on the server.

        Starts the OSPF protocol on a port or group of ports simultaneously.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the MLD protocol on a port or group of ports simultaneously.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
