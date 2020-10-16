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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class Interfaces(Base):
    """This object contains the globally configurable parameters for created interfaces.
    The Interfaces class encapsulates a required interfaces resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'interfaces'
    _SDM_ATT_MAP = {
        'ArpOnLinkup': 'arpOnLinkup',
        'NsOnLinkup': 'nsOnLinkup',
        'SendSingleArpPerGateway': 'sendSingleArpPerGateway',
        'SendSingleNsPerGateway': 'sendSingleNsPerGateway',
    }

    def __init__(self, parent):
        super(Interfaces, self).__init__(parent)

    @property
    def ArpOnLinkup(self):
        """
        Returns
        -------
        - bool: If true, automatically enables ARP and PING when the interfaces is associated with a port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpOnLinkup'])
    @ArpOnLinkup.setter
    def ArpOnLinkup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpOnLinkup'], value)

    @property
    def NsOnLinkup(self):
        """
        Returns
        -------
        - bool: If true, automatically enables NS when the interfaces is associated with a port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NsOnLinkup'])
    @NsOnLinkup.setter
    def NsOnLinkup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NsOnLinkup'], value)

    @property
    def SendSingleArpPerGateway(self):
        """
        Returns
        -------
        - bool: If true, only a single ARP is sent via each defined gateway address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendSingleArpPerGateway'])
    @SendSingleArpPerGateway.setter
    def SendSingleArpPerGateway(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendSingleArpPerGateway'], value)

    @property
    def SendSingleNsPerGateway(self):
        """
        Returns
        -------
        - bool: If true, only a single NS is sent via each defined gateway address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendSingleNsPerGateway'])
    @SendSingleNsPerGateway.setter
    def SendSingleNsPerGateway(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendSingleNsPerGateway'], value)

    def update(self, ArpOnLinkup=None, NsOnLinkup=None, SendSingleArpPerGateway=None, SendSingleNsPerGateway=None):
        """Updates interfaces resource on the server.

        Args
        ----
        - ArpOnLinkup (bool): If true, automatically enables ARP and PING when the interfaces is associated with a port.
        - NsOnLinkup (bool): If true, automatically enables NS when the interfaces is associated with a port.
        - SendSingleArpPerGateway (bool): If true, only a single ARP is sent via each defined gateway address.
        - SendSingleNsPerGateway (bool): If true, only a single NS is sent via each defined gateway address.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
