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


class Value(Base):
    """NOT DEFINED
    The Value class encapsulates a list of value resources that are managed by the user.
    A list of resources can be retrieved from the server using the Value.find() method.
    The list can be managed by using the Value.add() and Value.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "value"
    _SDM_ATT_MAP = {
        "AcceptableFramelossUnit": "acceptableFramelossUnit",
        "Group": "group",
        "ItemName": "itemName",
        "LoadUnit": "loadUnit",
        "StopSearchOnHighLoss": "stopSearchOnHighLoss",
    }
    _SDM_ENUM_MAP = {
        "acceptableFramelossUnit": ["frames", "percentage"],
        "loadUnit": [
            "bitsPerSecond",
            "framesPerSecond",
            "gbitsPerSecond",
            "gbytesPerSecond",
            "kbitsPerSecond",
            "kbytesPerSecond",
            "mbitsPerSecond",
            "mbytesPerSecond",
            "percentLineRate",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Value, self).__init__(parent, list_op)

    @property
    def AcceptableFramelossValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.acceptableframelossvalue_3d2b0f0b65bdb28d872d2c624e2f764c.AcceptableFramelossValue): An instance of the AcceptableFramelossValue class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.acceptableframelossvalue_3d2b0f0b65bdb28d872d2c624e2f764c import (
            AcceptableFramelossValue,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AcceptableFramelossValue", None) is not None:
                return self._properties.get("AcceptableFramelossValue")
        return AcceptableFramelossValue(self)

    @property
    def Backoff(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.backoff_a62e346e758e08a674f30e1a9db3a219.Backoff): An instance of the Backoff class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.backoff_a62e346e758e08a674f30e1a9db3a219 import (
            Backoff,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Backoff", None) is not None:
                return self._properties.get("Backoff")
        return Backoff(self)

    @property
    def InitialRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.initialrate_ab94ec0f92ed796e73a97aec1b2417f3.InitialRate): An instance of the InitialRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.initialrate_ab94ec0f92ed796e73a97aec1b2417f3 import (
            InitialRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("InitialRate", None) is not None:
                return self._properties.get("InitialRate")
        return InitialRate(self)

    @property
    def MaxRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.maxrate_1c23edd5256417052ed5b36f6f792cf4.MaxRate): An instance of the MaxRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.maxrate_1c23edd5256417052ed5b36f6f792cf4 import (
            MaxRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MaxRate", None) is not None:
                return self._properties.get("MaxRate")
        return MaxRate(self)

    @property
    def MinRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.minrate_398996be1d211debb2c73846070403f9.MinRate): An instance of the MinRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.minrate_398996be1d211debb2c73846070403f9 import (
            MinRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MinRate", None) is not None:
                return self._properties.get("MinRate")
        return MinRate(self)

    @property
    def Resolution(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.resolution_f7fbc853d99e3c4d0e8039d3cb501244.Resolution): An instance of the Resolution class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.resolution_f7fbc853d99e3c4d0e8039d3cb501244 import (
            Resolution,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Resolution", None) is not None:
                return self._properties.get("Resolution")
        return Resolution(self)

    @property
    def StepRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.steprate_c6ff6a6016b3cc7dfbe1bf62574cf56f.StepRate): An instance of the StepRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.steprate_c6ff6a6016b3cc7dfbe1bf62574cf56f import (
            StepRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StepRate", None) is not None:
                return self._properties.get("StepRate")
        return StepRate(self)

    @property
    def StopSearchOnHighLossValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.stopsearchonhighlossvalue_6e33a0ef082ec0d069012dfa380b102b.StopSearchOnHighLossValue): An instance of the StopSearchOnHighLossValue class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.stopsearchonhighlossvalue_6e33a0ef082ec0d069012dfa380b102b import (
            StopSearchOnHighLossValue,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StopSearchOnHighLossValue", None) is not None:
                return self._properties.get("StopSearchOnHighLossValue")
        return StopSearchOnHighLossValue(self)

    @property
    def AcceptableFramelossUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(frames | percentage): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AcceptableFramelossUnit"])

    @AcceptableFramelossUnit.setter
    def AcceptableFramelossUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AcceptableFramelossUnit"], value)

    @property
    def Group(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Group"])

    @Group.setter
    def Group(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Group"], value)

    @property
    def ItemName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ItemName"])

    @ItemName.setter
    def ItemName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ItemName"], value)

    @property
    def LoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bitsPerSecond | framesPerSecond | gbitsPerSecond | gbytesPerSecond | kbitsPerSecond | kbytesPerSecond | mbitsPerSecond | mbytesPerSecond | percentLineRate): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadUnit"])

    @LoadUnit.setter
    def LoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadUnit"], value)

    @property
    def StopSearchOnHighLoss(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["StopSearchOnHighLoss"])

    @StopSearchOnHighLoss.setter
    def StopSearchOnHighLoss(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StopSearchOnHighLoss"], value)

    def update(
        self,
        AcceptableFramelossUnit=None,
        Group=None,
        ItemName=None,
        LoadUnit=None,
        StopSearchOnHighLoss=None,
    ):
        # type: (str, str, str, str, bool) -> Value
        """Updates value resource on the server.

        Args
        ----
        - AcceptableFramelossUnit (str(frames | percentage)): NOT DEFINED
        - Group (str): NOT DEFINED
        - ItemName (str): NOT DEFINED
        - LoadUnit (str(bitsPerSecond | framesPerSecond | gbitsPerSecond | gbytesPerSecond | kbitsPerSecond | kbytesPerSecond | mbitsPerSecond | mbytesPerSecond | percentLineRate)): NOT DEFINED
        - StopSearchOnHighLoss (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AcceptableFramelossUnit=None,
        Group=None,
        ItemName=None,
        LoadUnit=None,
        StopSearchOnHighLoss=None,
    ):
        # type: (str, str, str, str, bool) -> Value
        """Adds a new value resource on the server and adds it to the container.

        Args
        ----
        - AcceptableFramelossUnit (str(frames | percentage)): NOT DEFINED
        - Group (str): NOT DEFINED
        - ItemName (str): NOT DEFINED
        - LoadUnit (str(bitsPerSecond | framesPerSecond | gbitsPerSecond | gbytesPerSecond | kbitsPerSecond | kbytesPerSecond | mbitsPerSecond | mbytesPerSecond | percentLineRate)): NOT DEFINED
        - StopSearchOnHighLoss (bool): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved value resources using find and the newly added value resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained value resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AcceptableFramelossUnit=None,
        Group=None,
        ItemName=None,
        LoadUnit=None,
        StopSearchOnHighLoss=None,
    ):
        # type: (str, str, str, str, bool) -> Value
        """Finds and retrieves value resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve value resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all value resources from the server.

        Args
        ----
        - AcceptableFramelossUnit (str(frames | percentage)): NOT DEFINED
        - Group (str): NOT DEFINED
        - ItemName (str): NOT DEFINED
        - LoadUnit (str(bitsPerSecond | framesPerSecond | gbitsPerSecond | gbytesPerSecond | kbitsPerSecond | kbytesPerSecond | mbitsPerSecond | mbytesPerSecond | percentLineRate)): NOT DEFINED
        - StopSearchOnHighLoss (bool): NOT DEFINED

        Returns
        -------
        - self: This instance with matching value resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of value data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the value resources from the server available through an iterator or index

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
