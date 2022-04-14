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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Interfaces(Base):
    """This object contains the globally configurable parameters for created interfaces.
    The Interfaces class encapsulates a required interfaces resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "interfaces"
    _SDM_ATT_MAP = {
        "ArpOnLinkup": "arpOnLinkup",
        "NsOnLinkup": "nsOnLinkup",
        "SendSingleArpPerGateway": "sendSingleArpPerGateway",
        "SendSingleNsPerGateway": "sendSingleNsPerGateway",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Interfaces, self).__init__(parent, list_op)

    @property
    def ArpOnLinkup(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, automatically enables ARP and PING when the interfaces is associated with a port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpOnLinkup"])

    @ArpOnLinkup.setter
    def ArpOnLinkup(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpOnLinkup"], value)

    @property
    def NsOnLinkup(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, automatically enables NS when the interfaces is associated with a port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NsOnLinkup"])

    @NsOnLinkup.setter
    def NsOnLinkup(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NsOnLinkup"], value)

    @property
    def SendSingleArpPerGateway(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, only a single ARP is sent via each defined gateway address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendSingleArpPerGateway"])

    @SendSingleArpPerGateway.setter
    def SendSingleArpPerGateway(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendSingleArpPerGateway"], value)

    @property
    def SendSingleNsPerGateway(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, only a single NS is sent via each defined gateway address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendSingleNsPerGateway"])

    @SendSingleNsPerGateway.setter
    def SendSingleNsPerGateway(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendSingleNsPerGateway"], value)

    def update(
        self,
        ArpOnLinkup=None,
        NsOnLinkup=None,
        SendSingleArpPerGateway=None,
        SendSingleNsPerGateway=None,
    ):
        # type: (bool, bool, bool, bool) -> Interfaces
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

    def find(
        self,
        ArpOnLinkup=None,
        NsOnLinkup=None,
        SendSingleArpPerGateway=None,
        SendSingleNsPerGateway=None,
    ):
        # type: (bool, bool, bool, bool) -> Interfaces
        """Finds and retrieves interfaces resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interfaces resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interfaces resources from the server.

        Args
        ----
        - ArpOnLinkup (bool): If true, automatically enables ARP and PING when the interfaces is associated with a port.
        - NsOnLinkup (bool): If true, automatically enables NS when the interfaces is associated with a port.
        - SendSingleArpPerGateway (bool): If true, only a single ARP is sent via each defined gateway address.
        - SendSingleNsPerGateway (bool): If true, only a single NS is sent via each defined gateway address.

        Returns
        -------
        - self: This instance with matching interfaces resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interfaces data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interfaces resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
