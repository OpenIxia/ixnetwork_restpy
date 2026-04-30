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


class BackgroundMap(Base):
    """If true, enables background traffic settings in the traffic mapping and frame data wizard.
    The BackgroundMap class encapsulates a list of backgroundMap resources that are managed by the user.
    A list of resources can be retrieved from the server using the BackgroundMap.find() method.
    The list can be managed by using the BackgroundMap.add() and BackgroundMap.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "backgroundMap"
    _SDM_ATT_MAP = {
        "FrameSize": "frameSize",
        "PacketRate": "packetRate",
        "PacketRateLoadUnit": "packetRateLoadUnit",
        "Priority802Tag": "priority802Tag",
        "PriorityTosValue": "priorityTosValue",
        "PriorityTrafficClassValue": "priorityTrafficClassValue",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BackgroundMap, self).__init__(parent, list_op)

    @property
    def Destinations(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.destinations_37a3981ee4441a78beb7cf0c29547b26.Destinations): An instance of the Destinations class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.destinations_37a3981ee4441a78beb7cf0c29547b26 import (
            Destinations,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Destinations", None) is not None:
                return self._properties.get("Destinations")
        return Destinations(self)

    @property
    def Sources(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.sources_fdb45bf7b12f261f52837b53aafb520f.Sources): An instance of the Sources class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.sources_fdb45bf7b12f261f52837b53aafb520f import (
            Sources,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Sources", None) is not None:
                return self._properties.get("Sources")
        return Sources(self)

    @property
    def FrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It describes the packet size of the high level stream that is configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameSize"])

    @FrameSize.setter
    def FrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameSize"], value)

    @property
    def PacketRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Describes the interval of traffic packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketRate"])

    @PacketRate.setter
    def PacketRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketRate"], value)

    @property
    def PacketRateLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the interval of packet rate for load unit testing.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketRateLoadUnit"])

    @PacketRateLoadUnit.setter
    def PacketRateLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketRateLoadUnit"], value)

    @property
    def Priority802Tag(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The 802.1Q priority for the iptv channel zapping.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Priority802Tag"])

    @Priority802Tag.setter
    def Priority802Tag(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Priority802Tag"], value)

    @property
    def PriorityTosValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The priority specified for the IP address(ToS or DSCP).
        """
        return self._get_attribute(self._SDM_ATT_MAP["PriorityTosValue"])

    @PriorityTosValue.setter
    def PriorityTosValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PriorityTosValue"], value)

    @property
    def PriorityTrafficClassValue(self):
        """
        Returns
        -------
        - dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str]): The priority specified for the traffic class values.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PriorityTrafficClassValue"])

    @PriorityTrafficClassValue.setter
    def PriorityTrafficClassValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP["PriorityTrafficClassValue"], value)

    def update(
        self,
        FrameSize=None,
        PacketRate=None,
        PacketRateLoadUnit=None,
        Priority802Tag=None,
        PriorityTosValue=None,
        PriorityTrafficClassValue=None,
    ):
        """Updates backgroundMap resource on the server.

        Args
        ----
        - FrameSize (number): It describes the packet size of the high level stream that is configured.
        - PacketRate (number): Describes the interval of traffic packet.
        - PacketRateLoadUnit (str): Describes the interval of packet rate for load unit testing.
        - Priority802Tag (str): The 802.1Q priority for the iptv channel zapping.
        - PriorityTosValue (str): The priority specified for the IP address(ToS or DSCP).
        - PriorityTrafficClassValue (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): The priority specified for the traffic class values.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        FrameSize=None,
        PacketRate=None,
        PacketRateLoadUnit=None,
        Priority802Tag=None,
        PriorityTosValue=None,
        PriorityTrafficClassValue=None,
    ):
        """Adds a new backgroundMap resource on the server and adds it to the container.

        Args
        ----
        - FrameSize (number): It describes the packet size of the high level stream that is configured.
        - PacketRate (number): Describes the interval of traffic packet.
        - PacketRateLoadUnit (str): Describes the interval of packet rate for load unit testing.
        - Priority802Tag (str): The 802.1Q priority for the iptv channel zapping.
        - PriorityTosValue (str): The priority specified for the IP address(ToS or DSCP).
        - PriorityTrafficClassValue (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): The priority specified for the traffic class values.

        Returns
        -------
        - self: This instance with all currently retrieved backgroundMap resources using find and the newly added backgroundMap resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained backgroundMap resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        FrameSize=None,
        PacketRate=None,
        PacketRateLoadUnit=None,
        Priority802Tag=None,
        PriorityTosValue=None,
        PriorityTrafficClassValue=None,
    ):
        """Finds and retrieves backgroundMap resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve backgroundMap resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all backgroundMap resources from the server.

        Args
        ----
        - FrameSize (number): It describes the packet size of the high level stream that is configured.
        - PacketRate (number): Describes the interval of traffic packet.
        - PacketRateLoadUnit (str): Describes the interval of packet rate for load unit testing.
        - Priority802Tag (str): The 802.1Q priority for the iptv channel zapping.
        - PriorityTosValue (str): The priority specified for the IP address(ToS or DSCP).
        - PriorityTrafficClassValue (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): The priority specified for the traffic class values.

        Returns
        -------
        - self: This instance with matching backgroundMap resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of backgroundMap data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the backgroundMap resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
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
        return self._execute("apply", payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
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
        return self._execute("applyAsync", payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool:

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
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
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
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

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
        return self._execute("generateReport", payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

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
        return self._execute("run", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
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
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
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
        return self._execute("stop", payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

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
        return self._execute("waitForTest", payload=payload, response_object=None)
