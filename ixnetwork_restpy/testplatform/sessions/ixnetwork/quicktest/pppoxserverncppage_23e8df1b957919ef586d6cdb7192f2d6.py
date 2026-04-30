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


class PppoxServerNcpPage(Base):
    """If true, configure PPP Server as the multicast traffic source is enabled for the IPTV Channel Zapping Quick Test.
    The PppoxServerNcpPage class encapsulates a list of pppoxServerNcpPage resources that are managed by the system.
    A list of resources can be retrieved from the server using the PppoxServerNcpPage.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "pppoxServerNcpPage"
    _SDM_ATT_MAP = {
        "ClientBaseIID": "clientBaseIID",
        "ClientBaseIp": "clientBaseIp",
        "ClientIIDIncr": "clientIIDIncr",
        "ClientIpIncr": "clientIpIncr",
        "Ipv6PoolPrefix": "ipv6PoolPrefix",
        "IsServer": "isServer",
        "NcpType": "ncpType",
        "RangeClientIpIncrement": "rangeClientIpIncrement",
        "RangeClientIpv6Increment": "rangeClientIpv6Increment",
        "RangeServerIpIncrement": "rangeServerIpIncrement",
        "RangeServerIpv6Increment": "rangeServerIpv6Increment",
        "ServerBaseIID": "serverBaseIID",
        "ServerBaseIp": "serverBaseIp",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PppoxServerNcpPage, self).__init__(parent, list_op)

    @property
    def ClientBaseIID(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The base Interface-Identifier (IID) to be assigned to the ppox client.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientBaseIID"])

    @ClientBaseIID.setter
    def ClientBaseIID(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientBaseIID"], value)

    @property
    def ClientBaseIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The base IP address to be assigned to the ppox client.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientBaseIp"])

    @ClientBaseIp.setter
    def ClientBaseIp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientBaseIp"], value)

    @property
    def ClientIIDIncr(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Client IID increment value, used in conjunction with the client IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientIIDIncr"])

    @ClientIIDIncr.setter
    def ClientIIDIncr(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientIIDIncr"], value)

    @property
    def ClientIpIncr(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Client IID increment value, used in conjunction with the ip addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientIpIncr"])

    @ClientIpIncr.setter
    def ClientIpIncr(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientIpIncr"], value)

    @property
    def Ipv6PoolPrefix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Pool prefix for the IPv6 IP pool.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6PoolPrefix"])

    @Ipv6PoolPrefix.setter
    def Ipv6PoolPrefix(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6PoolPrefix"], value)

    @property
    def IsServer(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, ppox ncp server is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsServer"])

    @IsServer.setter
    def IsServer(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsServer"], value)

    @property
    def NcpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The type of NCP used for the ppox range
        """
        return self._get_attribute(self._SDM_ATT_MAP["NcpType"])

    @NcpType.setter
    def NcpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NcpType"], value)

    @property
    def RangeClientIpIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The base IP address to be assigned to the ppox server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeClientIpIncrement"])

    @RangeClientIpIncrement.setter
    def RangeClientIpIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeClientIpIncrement"], value)

    @property
    def RangeClientIpv6Increment(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the client range increment for ipv6.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeClientIpv6Increment"])

    @RangeClientIpv6Increment.setter
    def RangeClientIpv6Increment(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeClientIpv6Increment"], value)

    @property
    def RangeServerIpIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the server incremental range ip value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeServerIpIncrement"])

    @RangeServerIpIncrement.setter
    def RangeServerIpIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeServerIpIncrement"], value)

    @property
    def RangeServerIpv6Increment(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the server range increment for ipv6.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeServerIpv6Increment"])

    @RangeServerIpv6Increment.setter
    def RangeServerIpv6Increment(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeServerIpv6Increment"], value)

    @property
    def ServerBaseIID(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The base Link Local Identifier for the ppox server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerBaseIID"])

    @ServerBaseIID.setter
    def ServerBaseIID(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerBaseIID"], value)

    @property
    def ServerBaseIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The base IP address to be assigned to the Ppox NCP server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerBaseIp"])

    @ServerBaseIp.setter
    def ServerBaseIp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ServerBaseIp"], value)

    def update(
        self,
        ClientBaseIID=None,
        ClientBaseIp=None,
        ClientIIDIncr=None,
        ClientIpIncr=None,
        Ipv6PoolPrefix=None,
        IsServer=None,
        NcpType=None,
        RangeClientIpIncrement=None,
        RangeClientIpv6Increment=None,
        RangeServerIpIncrement=None,
        RangeServerIpv6Increment=None,
        ServerBaseIID=None,
        ServerBaseIp=None,
    ):
        # type: (str, str, int, str, str, bool, str, str, str, str, str, str, str) -> PppoxServerNcpPage
        """Updates pppoxServerNcpPage resource on the server.

        Args
        ----
        - ClientBaseIID (str): The base Interface-Identifier (IID) to be assigned to the ppox client.
        - ClientBaseIp (str): The base IP address to be assigned to the ppox client.
        - ClientIIDIncr (number): Client IID increment value, used in conjunction with the client IP address.
        - ClientIpIncr (str): Client IID increment value, used in conjunction with the ip addresses.
        - Ipv6PoolPrefix (str): Pool prefix for the IPv6 IP pool.
        - IsServer (bool): If true, ppox ncp server is enabled.
        - NcpType (str): The type of NCP used for the ppox range
        - RangeClientIpIncrement (str): The base IP address to be assigned to the ppox server.
        - RangeClientIpv6Increment (str): Describes the client range increment for ipv6.
        - RangeServerIpIncrement (str): Describes the server incremental range ip value.
        - RangeServerIpv6Increment (str): Describes the server range increment for ipv6.
        - ServerBaseIID (str): The base Link Local Identifier for the ppox server.
        - ServerBaseIp (str): The base IP address to be assigned to the Ppox NCP server.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ClientBaseIID=None,
        ClientBaseIp=None,
        ClientIIDIncr=None,
        ClientIpIncr=None,
        Ipv6PoolPrefix=None,
        IsServer=None,
        NcpType=None,
        RangeClientIpIncrement=None,
        RangeClientIpv6Increment=None,
        RangeServerIpIncrement=None,
        RangeServerIpv6Increment=None,
        ServerBaseIID=None,
        ServerBaseIp=None,
    ):
        # type: (str, str, int, str, str, bool, str, str, str, str, str, str, str) -> PppoxServerNcpPage
        """Adds a new pppoxServerNcpPage resource on the json, only valid with batch add utility

        Args
        ----
        - ClientBaseIID (str): The base Interface-Identifier (IID) to be assigned to the ppox client.
        - ClientBaseIp (str): The base IP address to be assigned to the ppox client.
        - ClientIIDIncr (number): Client IID increment value, used in conjunction with the client IP address.
        - ClientIpIncr (str): Client IID increment value, used in conjunction with the ip addresses.
        - Ipv6PoolPrefix (str): Pool prefix for the IPv6 IP pool.
        - IsServer (bool): If true, ppox ncp server is enabled.
        - NcpType (str): The type of NCP used for the ppox range
        - RangeClientIpIncrement (str): The base IP address to be assigned to the ppox server.
        - RangeClientIpv6Increment (str): Describes the client range increment for ipv6.
        - RangeServerIpIncrement (str): Describes the server incremental range ip value.
        - RangeServerIpv6Increment (str): Describes the server range increment for ipv6.
        - ServerBaseIID (str): The base Link Local Identifier for the ppox server.
        - ServerBaseIp (str): The base IP address to be assigned to the Ppox NCP server.

        Returns
        -------
        - self: This instance with all currently retrieved pppoxServerNcpPage resources using find and the newly added pppoxServerNcpPage resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ClientBaseIID=None,
        ClientBaseIp=None,
        ClientIIDIncr=None,
        ClientIpIncr=None,
        Ipv6PoolPrefix=None,
        IsServer=None,
        NcpType=None,
        RangeClientIpIncrement=None,
        RangeClientIpv6Increment=None,
        RangeServerIpIncrement=None,
        RangeServerIpv6Increment=None,
        ServerBaseIID=None,
        ServerBaseIp=None,
    ):
        # type: (str, str, int, str, str, bool, str, str, str, str, str, str, str) -> PppoxServerNcpPage
        """Finds and retrieves pppoxServerNcpPage resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pppoxServerNcpPage resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pppoxServerNcpPage resources from the server.

        Args
        ----
        - ClientBaseIID (str): The base Interface-Identifier (IID) to be assigned to the ppox client.
        - ClientBaseIp (str): The base IP address to be assigned to the ppox client.
        - ClientIIDIncr (number): Client IID increment value, used in conjunction with the client IP address.
        - ClientIpIncr (str): Client IID increment value, used in conjunction with the ip addresses.
        - Ipv6PoolPrefix (str): Pool prefix for the IPv6 IP pool.
        - IsServer (bool): If true, ppox ncp server is enabled.
        - NcpType (str): The type of NCP used for the ppox range
        - RangeClientIpIncrement (str): The base IP address to be assigned to the ppox server.
        - RangeClientIpv6Increment (str): Describes the client range increment for ipv6.
        - RangeServerIpIncrement (str): Describes the server incremental range ip value.
        - RangeServerIpv6Increment (str): Describes the server range increment for ipv6.
        - ServerBaseIID (str): The base Link Local Identifier for the ppox server.
        - ServerBaseIp (str): The base IP address to be assigned to the Ppox NCP server.

        Returns
        -------
        - self: This instance with matching pppoxServerNcpPage resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pppoxServerNcpPage data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pppoxServerNcpPage resources from the server available through an iterator or index

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
