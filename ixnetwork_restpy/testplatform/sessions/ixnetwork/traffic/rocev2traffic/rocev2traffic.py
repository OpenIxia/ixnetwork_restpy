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


class RoceV2Traffic(Base):
    """This object specifies the particular RoCEv2 Traffic item related properties.
    The RoceV2Traffic class encapsulates a required roceV2Traffic resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "roceV2Traffic"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(RoceV2Traffic, self).__init__(parent, list_op)

    @property
    def RoceV2PortConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.rocev2traffic.rocev2portconfig.rocev2portconfig.RoceV2PortConfig): An instance of the RoceV2PortConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.rocev2traffic.rocev2portconfig.rocev2portconfig import (
            RoceV2PortConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RoceV2PortConfig", None) is not None:
                return self._properties.get("RoceV2PortConfig")
        return RoceV2PortConfig(self)

    @property
    def RoceV2Stream(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.rocev2traffic.rocev2stream.rocev2stream.RoceV2Stream): An instance of the RoceV2Stream class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.rocev2traffic.rocev2stream.rocev2stream import (
            RoceV2Stream,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RoceV2Stream", None) is not None:
                return self._properties.get("RoceV2Stream")
        return RoceV2Stream(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, this enables the selected RoCEv2 traffic item.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    def update(self, Enabled=None):
        # type: (bool) -> RoceV2Traffic
        """Updates roceV2Traffic resource on the server.

        Args
        ----
        - Enabled (bool): If true, this enables the selected RoCEv2 traffic item.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Enabled=None):
        # type: (bool) -> RoceV2Traffic
        """Finds and retrieves roceV2Traffic resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve roceV2Traffic resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all roceV2Traffic resources from the server.

        Args
        ----
        - Enabled (bool): If true, this enables the selected RoCEv2 traffic item.

        Returns
        -------
        - self: This instance with matching roceV2Traffic resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of roceV2Traffic data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the roceV2Traffic resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def BulkUpdateStreams(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the bulkUpdateStreams operation on the server.

        Takes a list of stream ids and properties to update

        bulkUpdateStreams(Arg2=list, async_operation=bool)
        --------------------------------------------------
        - Arg2 (list(dict(arg1:number,arg2:bool,arg3:str[continuous | fixed],arg4:number))): A list of stream properties to update: stream id, enabled (true/false), burst mode (continuous/fixed), burst count
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
        return self._execute("bulkUpdateStreams", payload=payload, response_object=None)

    def DeleteAllStreams(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the deleteAllStreams operation on the server.

        Deletes all RoCEv2 streams.

        deleteAllStreams(async_operation=bool)
        --------------------------------------
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
        return self._execute("deleteAllStreams", payload=payload, response_object=None)

    def Generate(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the generate operation on the server.

        Generate traffic for a specific traffic item.

        generate(async_operation=bool)
        ------------------------------
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
        return self._execute("generate", payload=payload, response_object=None)

    def GenerateWithParams(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the generateWithParams operation on the server.

        Generate traffic for a specific RoCEv2 traffic item with custom Tx Mode and burst count.

        generateWithParams(Arg2=enum, Arg3=number, async_operation=bool)
        ----------------------------------------------------------------
        - Arg2 (str(continuous | fixed)): RoCEv2 Stream Tx Mode: continuous | fixed
        - Arg3 (number): RoCEv2 Stream Burst Count
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
            "generateWithParams", payload=payload, response_object=None
        )
