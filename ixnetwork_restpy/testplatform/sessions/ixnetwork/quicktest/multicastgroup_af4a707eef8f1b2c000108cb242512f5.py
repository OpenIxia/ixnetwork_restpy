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


class MulticastGroup(Base):
    """The channel list multicast group ranges.
    The MulticastGroup class encapsulates a required multicastGroup resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "multicastGroup"
    _SDM_ATT_MAP = {
        "Count": "count",
        "FilterMode": "filterMode",
        "FirstChannelNumber": "firstChannelNumber",
        "Increment": "increment",
        "IpAddress": "ipAddress",
        "Name": "name",
        "SourceCount": "sourceCount",
        "SourceIncrement": "sourceIncrement",
        "SourceIpAddress": "sourceIpAddress",
        "Type": "type",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(MulticastGroup, self).__init__(parent, list_op)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The count of multicast groups in a range. Default value is 2, minimum value is 1, and maximum value is 4294967295.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @Count.setter
    def Count(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Count"], value)

    @property
    def FilterMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The source filter mode. This value defines the Group Record type included in the Report messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterMode"])

    @FilterMode.setter
    def FilterMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FilterMode"], value)

    @property
    def FirstChannelNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: First channel number in the range of multicast groups. Default value is 1, minimum value is 1, and maximum value is the count of multicast groups in a range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirstChannelNumber"])

    @FirstChannelNumber.setter
    def FirstChannelNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirstChannelNumber"], value)

    @property
    def Increment(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value used to enumerate all addresses in the range. Default is 0.0.0.1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Increment"])

    @Increment.setter
    def Increment(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Increment"], value)

    @property
    def IpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address of the first multicast group in the range. Default is 225.0.0.1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddress"])

    @IpAddress.setter
    def IpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddress"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A unique name for a Multicast Group Range. A default name is assigned to each range. It is user-editable.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def SourceCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The count of sources in the range. Default value is 0, minimum value is 0, while maximum value is 4294967295.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceCount"])

    @SourceCount.setter
    def SourceCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SourceCount"], value)

    @property
    def SourceIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value used to enumerate all source addresses in the range. Default is 0.0.0.1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceIncrement"])

    @SourceIncrement.setter
    def SourceIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SourceIncrement"], value)

    @property
    def SourceIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The starting IP address of a range of sources. Default is 10.10.10.1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceIpAddress"])

    @SourceIpAddress.setter
    def SourceIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SourceIpAddress"], value)

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Type of multicast group range. The options are IPv4 (default) and IPv6.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    @Type.setter
    def Type(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Type"], value)

    def update(
        self,
        Count=None,
        FilterMode=None,
        FirstChannelNumber=None,
        Increment=None,
        IpAddress=None,
        Name=None,
        SourceCount=None,
        SourceIncrement=None,
        SourceIpAddress=None,
        Type=None,
    ):
        # type: (int, str, int, str, str, str, int, str, str, str) -> MulticastGroup
        """Updates multicastGroup resource on the server.

        Args
        ----
        - Count (number): The count of multicast groups in a range. Default value is 2, minimum value is 1, and maximum value is 4294967295.
        - FilterMode (str): The source filter mode. This value defines the Group Record type included in the Report messages.
        - FirstChannelNumber (number): First channel number in the range of multicast groups. Default value is 1, minimum value is 1, and maximum value is the count of multicast groups in a range.
        - Increment (str): The value used to enumerate all addresses in the range. Default is 0.0.0.1.
        - IpAddress (str): The IP address of the first multicast group in the range. Default is 225.0.0.1.
        - Name (str): A unique name for a Multicast Group Range. A default name is assigned to each range. It is user-editable.
        - SourceCount (number): The count of sources in the range. Default value is 0, minimum value is 0, while maximum value is 4294967295.
        - SourceIncrement (str): The value used to enumerate all source addresses in the range. Default is 0.0.0.1.
        - SourceIpAddress (str): The starting IP address of a range of sources. Default is 10.10.10.1.
        - Type (str): Type of multicast group range. The options are IPv4 (default) and IPv6.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        FilterMode=None,
        FirstChannelNumber=None,
        Increment=None,
        IpAddress=None,
        Name=None,
        SourceCount=None,
        SourceIncrement=None,
        SourceIpAddress=None,
        Type=None,
    ):
        # type: (int, str, int, str, str, str, int, str, str, str) -> MulticastGroup
        """Finds and retrieves multicastGroup resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve multicastGroup resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all multicastGroup resources from the server.

        Args
        ----
        - Count (number): The count of multicast groups in a range. Default value is 2, minimum value is 1, and maximum value is 4294967295.
        - FilterMode (str): The source filter mode. This value defines the Group Record type included in the Report messages.
        - FirstChannelNumber (number): First channel number in the range of multicast groups. Default value is 1, minimum value is 1, and maximum value is the count of multicast groups in a range.
        - Increment (str): The value used to enumerate all addresses in the range. Default is 0.0.0.1.
        - IpAddress (str): The IP address of the first multicast group in the range. Default is 225.0.0.1.
        - Name (str): A unique name for a Multicast Group Range. A default name is assigned to each range. It is user-editable.
        - SourceCount (number): The count of sources in the range. Default value is 0, minimum value is 0, while maximum value is 4294967295.
        - SourceIncrement (str): The value used to enumerate all source addresses in the range. Default is 0.0.0.1.
        - SourceIpAddress (str): The starting IP address of a range of sources. Default is 10.10.10.1.
        - Type (str): Type of multicast group range. The options are IPv4 (default) and IPv6.

        Returns
        -------
        - self: This instance with matching multicastGroup resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of multicastGroup data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the multicastGroup resources from the server available through an iterator or index

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
