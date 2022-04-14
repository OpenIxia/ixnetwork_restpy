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


class CurrentPacket(Base):
    """This object specifies current packet properties.
    The CurrentPacket class encapsulates a required currentPacket resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "currentPacket"
    _SDM_ATT_MAP = {
        "PacketHex": "packetHex",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(CurrentPacket, self).__init__(parent, list_op)

    @property
    def Stack(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.currentpacket.stack.stack.Stack): An instance of the Stack class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.currentpacket.stack.stack import (
            Stack,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Stack", None) is not None:
                return self._properties.get("Stack")
        return Stack(self)

    @property
    def PacketHex(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Gets the packet hex of the current packet
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketHex"])

    def find(self, PacketHex=None):
        # type: (str) -> CurrentPacket
        """Finds and retrieves currentPacket resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve currentPacket resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all currentPacket resources from the server.

        Args
        ----
        - PacketHex (str): Gets the packet hex of the current packet

        Returns
        -------
        - self: This instance with matching currentPacket resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of currentPacket data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the currentPacket resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetPacketFromControlCapture(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the getPacketFromControlCapture operation on the server.

        The command retrieves a packet from the control capture started on a port.

        getPacketFromControlCapture(Arg2=number, async_operation=bool)
        --------------------------------------------------------------
        - Arg2 (number): The packet index.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getPacketFromControlCapture", payload=payload, response_object=None
        )

    def GetPacketFromDataCapture(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the getPacketFromDataCapture operation on the server.

        The command retrieves a packet from the data capture started on a port.

        getPacketFromDataCapture(Arg2=number, async_operation=bool)
        -----------------------------------------------------------
        - Arg2 (number): The packet index.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getPacketFromDataCapture", payload=payload, response_object=None
        )
