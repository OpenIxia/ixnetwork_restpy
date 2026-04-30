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


class Dhcp6Page(Base):
    """Allows to configure dhcp verison 6.
    The Dhcp6Page class encapsulates a list of dhcp6Page resources that are managed by the system.
    A list of resources can be retrieved from the server using the Dhcp6Page.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "dhcp6Page"
    _SDM_ATT_MAP = {
        "Dhcp6DuidEnterpriseId": "dhcp6DuidEnterpriseId",
        "Dhcp6DuidType": "dhcp6DuidType",
        "Dhcp6DuidVendorId": "dhcp6DuidVendorId",
        "Dhcp6DuidVendorIdIncrement": "dhcp6DuidVendorIdIncrement",
        "Dhcp6IaId": "dhcp6IaId",
        "Dhcp6IaIdIncrement": "dhcp6IaIdIncrement",
        "Dhcp6IaT1": "dhcp6IaT1",
        "Dhcp6IaT2": "dhcp6IaT2",
        "Dhcp6IaType": "dhcp6IaType",
        "Dhcp6ParamRequestList": "dhcp6ParamRequestList",
        "DhcpPD": "dhcpPD",
        "UseRapidCommit": "useRapidCommit",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Dhcp6Page, self).__init__(parent, list_op)

    @property
    def Dhcp6DuidEnterpriseId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, the dhcp version 6 Duid Type is registered.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6DuidEnterpriseId"])

    @Dhcp6DuidEnterpriseId.setter
    def Dhcp6DuidEnterpriseId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6DuidEnterpriseId"], value)

    @property
    def Dhcp6DuidType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: DHCP Unique Identifier (DUID) Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6DuidType"])

    @Dhcp6DuidType.setter
    def Dhcp6DuidType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6DuidType"], value)

    @property
    def Dhcp6DuidVendorId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: A unique identifier defined by the vendor.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6DuidVendorId"])

    @Dhcp6DuidVendorId.setter
    def Dhcp6DuidVendorId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6DuidVendorId"], value)

    @property
    def Dhcp6DuidVendorIdIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Describes the incremental value of unique identifier defined by the vendor.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6DuidVendorIdIncrement"])

    @Dhcp6DuidVendorIdIncrement.setter
    def Dhcp6DuidVendorIdIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6DuidVendorIdIncrement"], value)

    @property
    def Dhcp6IaId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Unique Identifier for Identity Association (IA).
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6IaId"])

    @Dhcp6IaId.setter
    def Dhcp6IaId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6IaId"], value)

    @property
    def Dhcp6IaIdIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value by which the dhcp6IaId is incremented for each DHCP client.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6IaIdIncrement"])

    @Dhcp6IaIdIncrement.setter
    def Dhcp6IaIdIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6IaIdIncrement"], value)

    @property
    def Dhcp6IaT1(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Time, in seconds, at which the client contacts the server to extend the lifetimes of the assigned addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6IaT1"])

    @Dhcp6IaT1.setter
    def Dhcp6IaT1(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6IaT1"], value)

    @property
    def Dhcp6IaT2(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Time, in seconds, at which the client contacts any available server to extend the lifetimes of the addresses assigned.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6IaT2"])

    @Dhcp6IaT2.setter
    def Dhcp6IaT2(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6IaT2"], value)

    @property
    def Dhcp6IaType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Identity Association Type. An identify association is a construct through which a server and a client identify, group, and manage a set of related IPv6 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6IaType"])

    @Dhcp6IaType.setter
    def Dhcp6IaType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6IaType"], value)

    @property
    def Dhcp6ParamRequestList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the request list for dhcp version 6.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6ParamRequestList"])

    @Dhcp6ParamRequestList.setter
    def Dhcp6ParamRequestList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6ParamRequestList"], value)

    @property
    def DhcpPD(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Contains the global configuration parameters for DHCP Client Global Settings
        """
        return self._get_attribute(self._SDM_ATT_MAP["DhcpPD"])

    @DhcpPD.setter
    def DhcpPD(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DhcpPD"], value)

    @property
    def UseRapidCommit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, rapid commit is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseRapidCommit"])

    @UseRapidCommit.setter
    def UseRapidCommit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseRapidCommit"], value)

    def update(
        self,
        Dhcp6DuidEnterpriseId=None,
        Dhcp6DuidType=None,
        Dhcp6DuidVendorId=None,
        Dhcp6DuidVendorIdIncrement=None,
        Dhcp6IaId=None,
        Dhcp6IaIdIncrement=None,
        Dhcp6IaT1=None,
        Dhcp6IaT2=None,
        Dhcp6IaType=None,
        Dhcp6ParamRequestList=None,
        DhcpPD=None,
        UseRapidCommit=None,
    ):
        # type: (int, str, int, int, int, int, int, int, str, str, bool, bool) -> Dhcp6Page
        """Updates dhcp6Page resource on the server.

        Args
        ----
        - Dhcp6DuidEnterpriseId (number): If true, the dhcp version 6 Duid Type is registered.
        - Dhcp6DuidType (str): DHCP Unique Identifier (DUID) Type.
        - Dhcp6DuidVendorId (number): A unique identifier defined by the vendor.
        - Dhcp6DuidVendorIdIncrement (number): Describes the incremental value of unique identifier defined by the vendor.
        - Dhcp6IaId (number): Unique Identifier for Identity Association (IA).
        - Dhcp6IaIdIncrement (number): The value by which the dhcp6IaId is incremented for each DHCP client.
        - Dhcp6IaT1 (number): Time, in seconds, at which the client contacts the server to extend the lifetimes of the assigned addresses.
        - Dhcp6IaT2 (number): Time, in seconds, at which the client contacts any available server to extend the lifetimes of the addresses assigned.
        - Dhcp6IaType (str): The Identity Association Type. An identify association is a construct through which a server and a client identify, group, and manage a set of related IPv6 addresses.
        - Dhcp6ParamRequestList (str): Describes the request list for dhcp version 6.
        - DhcpPD (bool): Contains the global configuration parameters for DHCP Client Global Settings
        - UseRapidCommit (bool): If true, rapid commit is enabled.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Dhcp6DuidEnterpriseId=None,
        Dhcp6DuidType=None,
        Dhcp6DuidVendorId=None,
        Dhcp6DuidVendorIdIncrement=None,
        Dhcp6IaId=None,
        Dhcp6IaIdIncrement=None,
        Dhcp6IaT1=None,
        Dhcp6IaT2=None,
        Dhcp6IaType=None,
        Dhcp6ParamRequestList=None,
        DhcpPD=None,
        UseRapidCommit=None,
    ):
        # type: (int, str, int, int, int, int, int, int, str, str, bool, bool) -> Dhcp6Page
        """Adds a new dhcp6Page resource on the json, only valid with batch add utility

        Args
        ----
        - Dhcp6DuidEnterpriseId (number): If true, the dhcp version 6 Duid Type is registered.
        - Dhcp6DuidType (str): DHCP Unique Identifier (DUID) Type.
        - Dhcp6DuidVendorId (number): A unique identifier defined by the vendor.
        - Dhcp6DuidVendorIdIncrement (number): Describes the incremental value of unique identifier defined by the vendor.
        - Dhcp6IaId (number): Unique Identifier for Identity Association (IA).
        - Dhcp6IaIdIncrement (number): The value by which the dhcp6IaId is incremented for each DHCP client.
        - Dhcp6IaT1 (number): Time, in seconds, at which the client contacts the server to extend the lifetimes of the assigned addresses.
        - Dhcp6IaT2 (number): Time, in seconds, at which the client contacts any available server to extend the lifetimes of the addresses assigned.
        - Dhcp6IaType (str): The Identity Association Type. An identify association is a construct through which a server and a client identify, group, and manage a set of related IPv6 addresses.
        - Dhcp6ParamRequestList (str): Describes the request list for dhcp version 6.
        - DhcpPD (bool): Contains the global configuration parameters for DHCP Client Global Settings
        - UseRapidCommit (bool): If true, rapid commit is enabled.

        Returns
        -------
        - self: This instance with all currently retrieved dhcp6Page resources using find and the newly added dhcp6Page resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Dhcp6DuidEnterpriseId=None,
        Dhcp6DuidType=None,
        Dhcp6DuidVendorId=None,
        Dhcp6DuidVendorIdIncrement=None,
        Dhcp6IaId=None,
        Dhcp6IaIdIncrement=None,
        Dhcp6IaT1=None,
        Dhcp6IaT2=None,
        Dhcp6IaType=None,
        Dhcp6ParamRequestList=None,
        DhcpPD=None,
        UseRapidCommit=None,
    ):
        # type: (int, str, int, int, int, int, int, int, str, str, bool, bool) -> Dhcp6Page
        """Finds and retrieves dhcp6Page resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcp6Page resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcp6Page resources from the server.

        Args
        ----
        - Dhcp6DuidEnterpriseId (number): If true, the dhcp version 6 Duid Type is registered.
        - Dhcp6DuidType (str): DHCP Unique Identifier (DUID) Type.
        - Dhcp6DuidVendorId (number): A unique identifier defined by the vendor.
        - Dhcp6DuidVendorIdIncrement (number): Describes the incremental value of unique identifier defined by the vendor.
        - Dhcp6IaId (number): Unique Identifier for Identity Association (IA).
        - Dhcp6IaIdIncrement (number): The value by which the dhcp6IaId is incremented for each DHCP client.
        - Dhcp6IaT1 (number): Time, in seconds, at which the client contacts the server to extend the lifetimes of the assigned addresses.
        - Dhcp6IaT2 (number): Time, in seconds, at which the client contacts any available server to extend the lifetimes of the addresses assigned.
        - Dhcp6IaType (str): The Identity Association Type. An identify association is a construct through which a server and a client identify, group, and manage a set of related IPv6 addresses.
        - Dhcp6ParamRequestList (str): Describes the request list for dhcp version 6.
        - DhcpPD (bool): Contains the global configuration parameters for DHCP Client Global Settings
        - UseRapidCommit (bool): If true, rapid commit is enabled.

        Returns
        -------
        - self: This instance with matching dhcp6Page resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcp6Page data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcp6Page resources from the server available through an iterator or index

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
