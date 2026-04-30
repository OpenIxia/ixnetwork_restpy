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


class ViewingProfile(Base):
    """A template describing the behavior of clients viewing the lists of channels.
    The ViewingProfile class encapsulates a required viewingProfile resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "viewingProfile"
    _SDM_ATT_MAP = {
        "ChangesBeforeView": "changesBeforeView",
        "Name": "name",
        "ViewDuration": "viewDuration",
        "ZapBehavior": "zapBehavior",
        "ZapDirection": "zapDirection",
        "ZapInterval": "zapInterval",
        "ZapIntervalType": "zapIntervalType",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(ViewingProfile, self).__init__(parent, list_op)

    @property
    def ChangesBeforeView(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of channels to change before stopping on a channel and watching it for the View Duration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChangesBeforeView"])

    @ChangesBeforeView.setter
    def ChangesBeforeView(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChangesBeforeView"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique name for this Viewing Profile. IxNetwork assigns a default name to each profile. It is user-editable.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def ViewDuration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The length of time, in milliseconds, that users of this profile will view the last channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ViewDuration"])

    @ViewDuration.setter
    def ViewDuration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ViewDuration"], value)

    @property
    def ZapBehavior(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The zapping behavior for this profile. Zapping describes the behavior of a television view using a remote control device (RCD) to quickly switch from one channel to another.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ZapBehavior"])

    @ZapBehavior.setter
    def ZapBehavior(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ZapBehavior"], value)

    @property
    def ZapDirection(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The direction of changing channels.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ZapDirection"])

    @ZapDirection.setter
    def ZapDirection(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ZapDirection"], value)

    @property
    def ZapInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Interval in milliseconds between channel changes, based on the selected type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ZapInterval"])

    @ZapInterval.setter
    def ZapInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ZapInterval"], value)

    @property
    def ZapIntervalType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The wait-interval type before changing channels.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ZapIntervalType"])

    @ZapIntervalType.setter
    def ZapIntervalType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ZapIntervalType"], value)

    def update(
        self,
        ChangesBeforeView=None,
        Name=None,
        ViewDuration=None,
        ZapBehavior=None,
        ZapDirection=None,
        ZapInterval=None,
        ZapIntervalType=None,
    ):
        # type: (int, str, int, str, str, int, str) -> ViewingProfile
        """Updates viewingProfile resource on the server.

        Args
        ----
        - ChangesBeforeView (number): The number of channels to change before stopping on a channel and watching it for the View Duration.
        - Name (str): Unique name for this Viewing Profile. IxNetwork assigns a default name to each profile. It is user-editable.
        - ViewDuration (number): The length of time, in milliseconds, that users of this profile will view the last channel.
        - ZapBehavior (str): The zapping behavior for this profile. Zapping describes the behavior of a television view using a remote control device (RCD) to quickly switch from one channel to another.
        - ZapDirection (str): The direction of changing channels.
        - ZapInterval (number): Interval in milliseconds between channel changes, based on the selected type.
        - ZapIntervalType (str): The wait-interval type before changing channels.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ChangesBeforeView=None,
        Name=None,
        ViewDuration=None,
        ZapBehavior=None,
        ZapDirection=None,
        ZapInterval=None,
        ZapIntervalType=None,
    ):
        # type: (int, str, int, str, str, int, str) -> ViewingProfile
        """Finds and retrieves viewingProfile resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve viewingProfile resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all viewingProfile resources from the server.

        Args
        ----
        - ChangesBeforeView (number): The number of channels to change before stopping on a channel and watching it for the View Duration.
        - Name (str): Unique name for this Viewing Profile. IxNetwork assigns a default name to each profile. It is user-editable.
        - ViewDuration (number): The length of time, in milliseconds, that users of this profile will view the last channel.
        - ZapBehavior (str): The zapping behavior for this profile. Zapping describes the behavior of a television view using a remote control device (RCD) to quickly switch from one channel to another.
        - ZapDirection (str): The direction of changing channels.
        - ZapInterval (number): Interval in milliseconds between channel changes, based on the selected type.
        - ZapIntervalType (str): The wait-interval type before changing channels.

        Returns
        -------
        - self: This instance with matching viewingProfile resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of viewingProfile data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the viewingProfile resources from the server available through an iterator or index

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
