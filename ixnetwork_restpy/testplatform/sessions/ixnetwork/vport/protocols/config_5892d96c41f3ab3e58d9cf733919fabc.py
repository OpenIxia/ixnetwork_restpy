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


class Config(Base):
    """This object allow to define the settings for the current configuration of the physical port.
    The Config class encapsulates a required config resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "config"
    _SDM_ATT_MAP = {
        "NoFlood": "noFlood",
        "NoForward": "noForward",
        "NoPacketIn": "noPacketIn",
        "NoReceive": "noReceive",
        "NoReceiveStp": "noReceiveStp",
        "NoStp": "noStp",
        "PortDown": "portDown",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Config, self).__init__(parent, list_op)

    @property
    def NoFlood(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the port is not included when flooding.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoFlood"])

    @NoFlood.setter
    def NoFlood(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoFlood"], value)

    @property
    def NoForward(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the port drop all packets forwarded to it.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoForward"])

    @NoForward.setter
    def NoForward(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoForward"], value)

    @property
    def NoPacketIn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the port does not send packet-in messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoPacketIn"])

    @NoPacketIn.setter
    def NoPacketIn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoPacketIn"], value)

    @property
    def NoReceive(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the port drops all packets except 802.1D spanning tree packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoReceive"])

    @NoReceive.setter
    def NoReceive(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoReceive"], value)

    @property
    def NoReceiveStp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the port drops received 802.1D STP packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoReceiveStp"])

    @NoReceiveStp.setter
    def NoReceiveStp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoReceiveStp"], value)

    @property
    def NoStp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that 802.1D spanning tree on port is disable.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoStp"])

    @NoStp.setter
    def NoStp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoStp"], value)

    @property
    def PortDown(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the port is administratively down.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDown"])

    @PortDown.setter
    def PortDown(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDown"], value)

    def update(
        self,
        NoFlood=None,
        NoForward=None,
        NoPacketIn=None,
        NoReceive=None,
        NoReceiveStp=None,
        NoStp=None,
        PortDown=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool) -> Config
        """Updates config resource on the server.

        Args
        ----
        - NoFlood (bool): Indicates that the port is not included when flooding.
        - NoForward (bool): Indicates that the port drop all packets forwarded to it.
        - NoPacketIn (bool): Indicates that the port does not send packet-in messages.
        - NoReceive (bool): Indicates that the port drops all packets except 802.1D spanning tree packets.
        - NoReceiveStp (bool): Indicates that the port drops received 802.1D STP packets.
        - NoStp (bool): Indicates that 802.1D spanning tree on port is disable.
        - PortDown (bool): Indicates that the port is administratively down.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        NoFlood=None,
        NoForward=None,
        NoPacketIn=None,
        NoReceive=None,
        NoReceiveStp=None,
        NoStp=None,
        PortDown=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool) -> Config
        """Finds and retrieves config resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve config resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all config resources from the server.

        Args
        ----
        - NoFlood (bool): Indicates that the port is not included when flooding.
        - NoForward (bool): Indicates that the port drop all packets forwarded to it.
        - NoPacketIn (bool): Indicates that the port does not send packet-in messages.
        - NoReceive (bool): Indicates that the port drops all packets except 802.1D spanning tree packets.
        - NoReceiveStp (bool): Indicates that the port drops received 802.1D STP packets.
        - NoStp (bool): Indicates that 802.1D spanning tree on port is disable.
        - PortDown (bool): Indicates that the port is administratively down.

        Returns
        -------
        - self: This instance with matching config resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of config data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the config resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
