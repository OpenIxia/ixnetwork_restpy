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


class IpPage(Base):
    """If true, ip page is enabled.
    The IpPage class encapsulates a list of ipPage resources that are managed by the system.
    A list of resources can be retrieved from the server using the IpPage.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "ipPage"
    _SDM_ATT_MAP = {
        "Count": "count",
        "GatewayAddress": "gatewayAddress",
        "GatewayIncrement": "gatewayIncrement",
        "IncrementBy": "incrementBy",
        "IpAddress": "ipAddress",
        "IpType": "ipType",
        "IsOnlyIpv4": "isOnlyIpv4",
        "Mss": "mss",
        "PgIpIncrement": "pgIpIncrement",
        "Prefix": "prefix",
        "RangeIpIncrement": "rangeIpIncrement",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IpPage, self).__init__(parent, list_op)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of emulated access nodes for the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @Count.setter
    def Count(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Count"], value)

    @property
    def GatewayAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The gateway address for all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GatewayAddress"])

    @GatewayAddress.setter
    def GatewayAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GatewayAddress"], value)

    @property
    def GatewayIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Configures the address increment value that is used to generate each gateway address required in the network group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GatewayIncrement"])

    @GatewayIncrement.setter
    def GatewayIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GatewayIncrement"], value)

    @property
    def IncrementBy(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value that is used in conjunction with the base MAC address to create a range of multiple MAC addresses for ip page.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementBy"])

    @IncrementBy.setter
    def IncrementBy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementBy"], value)

    @property
    def IpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the ip address assigned for ip page.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddress"])

    @IpAddress.setter
    def IpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddress"], value)

    @property
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the type of ip for ip page.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpType"])

    @IpType.setter
    def IpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpType"], value)

    @property
    def IsOnlyIpv4(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, ipv4 can be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsOnlyIpv4"])

    @IsOnlyIpv4.setter
    def IsOnlyIpv4(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsOnlyIpv4"], value)

    @property
    def Mss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Describes the Maximum Segment Size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mss"])

    @Mss.setter
    def Mss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mss"], value)

    @property
    def PgIpIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the page ip increment.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PgIpIncrement"])

    @PgIpIncrement.setter
    def PgIpIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PgIpIncrement"], value)

    @property
    def Prefix(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of one bits in the subnet mask.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Prefix"])

    @Prefix.setter
    def Prefix(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Prefix"], value)

    @property
    def RangeIpIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the range of ip increment for ip page.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeIpIncrement"])

    @RangeIpIncrement.setter
    def RangeIpIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeIpIncrement"], value)

    def update(
        self,
        Count=None,
        GatewayAddress=None,
        GatewayIncrement=None,
        IncrementBy=None,
        IpAddress=None,
        IpType=None,
        IsOnlyIpv4=None,
        Mss=None,
        PgIpIncrement=None,
        Prefix=None,
        RangeIpIncrement=None,
    ):
        # type: (int, str, str, str, str, str, bool, int, str, int, str) -> IpPage
        """Updates ipPage resource on the server.

        Args
        ----
        - Count (number): Number of emulated access nodes for the range.
        - GatewayAddress (str): The gateway address for all the addresses in the range.
        - GatewayIncrement (str): Configures the address increment value that is used to generate each gateway address required in the network group.
        - IncrementBy (str): The value that is used in conjunction with the base MAC address to create a range of multiple MAC addresses for ip page.
        - IpAddress (str): Describes the ip address assigned for ip page.
        - IpType (str): Describes the type of ip for ip page.
        - IsOnlyIpv4 (bool): If true, ipv4 can be used.
        - Mss (number): Describes the Maximum Segment Size.
        - PgIpIncrement (str): Describes the page ip increment.
        - Prefix (number): The number of one bits in the subnet mask.
        - RangeIpIncrement (str): Describes the range of ip increment for ip page.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Count=None,
        GatewayAddress=None,
        GatewayIncrement=None,
        IncrementBy=None,
        IpAddress=None,
        IpType=None,
        IsOnlyIpv4=None,
        Mss=None,
        PgIpIncrement=None,
        Prefix=None,
        RangeIpIncrement=None,
    ):
        # type: (int, str, str, str, str, str, bool, int, str, int, str) -> IpPage
        """Adds a new ipPage resource on the json, only valid with batch add utility

        Args
        ----
        - Count (number): Number of emulated access nodes for the range.
        - GatewayAddress (str): The gateway address for all the addresses in the range.
        - GatewayIncrement (str): Configures the address increment value that is used to generate each gateway address required in the network group.
        - IncrementBy (str): The value that is used in conjunction with the base MAC address to create a range of multiple MAC addresses for ip page.
        - IpAddress (str): Describes the ip address assigned for ip page.
        - IpType (str): Describes the type of ip for ip page.
        - IsOnlyIpv4 (bool): If true, ipv4 can be used.
        - Mss (number): Describes the Maximum Segment Size.
        - PgIpIncrement (str): Describes the page ip increment.
        - Prefix (number): The number of one bits in the subnet mask.
        - RangeIpIncrement (str): Describes the range of ip increment for ip page.

        Returns
        -------
        - self: This instance with all currently retrieved ipPage resources using find and the newly added ipPage resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        GatewayAddress=None,
        GatewayIncrement=None,
        IncrementBy=None,
        IpAddress=None,
        IpType=None,
        IsOnlyIpv4=None,
        Mss=None,
        PgIpIncrement=None,
        Prefix=None,
        RangeIpIncrement=None,
    ):
        # type: (int, str, str, str, str, str, bool, int, str, int, str) -> IpPage
        """Finds and retrieves ipPage resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipPage resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipPage resources from the server.

        Args
        ----
        - Count (number): Number of emulated access nodes for the range.
        - GatewayAddress (str): The gateway address for all the addresses in the range.
        - GatewayIncrement (str): Configures the address increment value that is used to generate each gateway address required in the network group.
        - IncrementBy (str): The value that is used in conjunction with the base MAC address to create a range of multiple MAC addresses for ip page.
        - IpAddress (str): Describes the ip address assigned for ip page.
        - IpType (str): Describes the type of ip for ip page.
        - IsOnlyIpv4 (bool): If true, ipv4 can be used.
        - Mss (number): Describes the Maximum Segment Size.
        - PgIpIncrement (str): Describes the page ip increment.
        - Prefix (number): The number of one bits in the subnet mask.
        - RangeIpIncrement (str): Describes the range of ip increment for ip page.

        Returns
        -------
        - self: This instance with matching ipPage resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipPage data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipPage resources from the server available through an iterator or index

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
