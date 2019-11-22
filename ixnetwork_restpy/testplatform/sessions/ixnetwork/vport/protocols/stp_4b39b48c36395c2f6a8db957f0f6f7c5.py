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


class Stp(Base):
    """This object simulates one or more STP/RSTP/MSTP/PVST+/RPVST+ bridges in a network of bridges.
    The Stp class encapsulates a required stp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'stp'

    def __init__(self, parent):
        super(Stp, self).__init__(parent)

    @property
    def Bridge(self):
        """An instance of the Bridge class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bridge_533d557d2921bcc4dd6f66f6a8b8182a.Bridge)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bridge_533d557d2921bcc4dd6f66f6a8b8182a import Bridge
        return Bridge(self)

    @property
    def Lan(self):
        """An instance of the Lan class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lan_9e659dabb5c20b22becaaf3de1a62277.Lan)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lan_9e659dabb5c20b22becaaf3de1a62277 import Lan
        return Lan(self)

    @property
    def Enabled(self):
        """Enables or disables the use of this emulated spanning-tree protocol (STP) router in the emulated STP network. (default = disabled) STP is used to resolve and eliminate loops in a network.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def RunningState(self):
        """The current running state of the STP server.

        Returns:
            str(unknown|stopped|stopping|starting|started)
        """
        return self._get_attribute('runningState')

    def update(self, Enabled=None):
        """Updates a child instance of stp on the server.

        Args:
            Enabled (bool): Enables or disables the use of this emulated spanning-tree protocol (STP) router in the emulated STP network. (default = disabled) STP is used to resolve and eliminate loops in a network.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def Start(self):
        """Executes the start operation on the server.

        Starts STP on a port or group of ports.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops STP on a port or group of ports.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
