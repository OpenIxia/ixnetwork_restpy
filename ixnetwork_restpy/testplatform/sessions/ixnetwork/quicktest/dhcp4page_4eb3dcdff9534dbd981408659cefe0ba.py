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


class Dhcp4Page(Base):
    """If true, dhcp 4 is enabled.
    The Dhcp4Page class encapsulates a list of dhcp4Page resources that are managed by the system.
    A list of resources can be retrieved from the server using the Dhcp4Page.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "dhcp4Page"
    _SDM_ATT_MAP = {
        "Dhcp4ParamRequestList": "dhcp4ParamRequestList",
        "Dhcp4ServerAddress": "dhcp4ServerAddress",
        "Dhcp4UseFirstServer": "dhcp4UseFirstServer",
        "UseRapidCommit": "useRapidCommit",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Dhcp4Page, self).__init__(parent, list_op)

    @property
    def Dhcp4ParamRequestList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the dhcp 4 paramenter request list.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp4ParamRequestList"])

    @Dhcp4ParamRequestList.setter
    def Dhcp4ParamRequestList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp4ParamRequestList"], value)

    @property
    def Dhcp4ServerAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the dhcp4 server address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp4ServerAddress"])

    @Dhcp4ServerAddress.setter
    def Dhcp4ServerAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp4ServerAddress"], value)

    @property
    def Dhcp4UseFirstServer(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Describes the first dhcp4 server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp4UseFirstServer"])

    @Dhcp4UseFirstServer.setter
    def Dhcp4UseFirstServer(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp4UseFirstServer"], value)

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
        Dhcp4ParamRequestList=None,
        Dhcp4ServerAddress=None,
        Dhcp4UseFirstServer=None,
        UseRapidCommit=None,
    ):
        # type: (str, str, bool, bool) -> Dhcp4Page
        """Updates dhcp4Page resource on the server.

        Args
        ----
        - Dhcp4ParamRequestList (str): Describes the dhcp 4 paramenter request list.
        - Dhcp4ServerAddress (str): Describes the dhcp4 server address.
        - Dhcp4UseFirstServer (bool): Describes the first dhcp4 server.
        - UseRapidCommit (bool): If true, rapid commit is enabled.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Dhcp4ParamRequestList=None,
        Dhcp4ServerAddress=None,
        Dhcp4UseFirstServer=None,
        UseRapidCommit=None,
    ):
        # type: (str, str, bool, bool) -> Dhcp4Page
        """Adds a new dhcp4Page resource on the json, only valid with batch add utility

        Args
        ----
        - Dhcp4ParamRequestList (str): Describes the dhcp 4 paramenter request list.
        - Dhcp4ServerAddress (str): Describes the dhcp4 server address.
        - Dhcp4UseFirstServer (bool): Describes the first dhcp4 server.
        - UseRapidCommit (bool): If true, rapid commit is enabled.

        Returns
        -------
        - self: This instance with all currently retrieved dhcp4Page resources using find and the newly added dhcp4Page resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Dhcp4ParamRequestList=None,
        Dhcp4ServerAddress=None,
        Dhcp4UseFirstServer=None,
        UseRapidCommit=None,
    ):
        # type: (str, str, bool, bool) -> Dhcp4Page
        """Finds and retrieves dhcp4Page resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcp4Page resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcp4Page resources from the server.

        Args
        ----
        - Dhcp4ParamRequestList (str): Describes the dhcp 4 paramenter request list.
        - Dhcp4ServerAddress (str): Describes the dhcp4 server address.
        - Dhcp4UseFirstServer (bool): Describes the first dhcp4 server.
        - UseRapidCommit (bool): If true, rapid commit is enabled.

        Returns
        -------
        - self: This instance with matching dhcp4Page resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcp4Page data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcp4Page resources from the server available through an iterator or index

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
