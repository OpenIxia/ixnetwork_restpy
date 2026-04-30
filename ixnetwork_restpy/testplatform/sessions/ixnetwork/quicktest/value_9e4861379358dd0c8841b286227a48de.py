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
        "ClearOverlays": "clearOverlays",
        "CustomIsExtended": "customIsExtended",
        "OperationIndex": "operationIndex",
        "PerSessionOverlayIndices": "perSessionOverlayIndices",
        "PerSessionOverlayValues": "perSessionOverlayValues",
        "SingleValue": "singleValue",
        "StringApplyPatternExpression": "stringApplyPatternExpression",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Value, self).__init__(parent, list_op)

    @property
    def Pattern(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pattern_540a4fdfe12e4a603c4dcb3deb56f603.Pattern): An instance of the Pattern class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pattern_540a4fdfe12e4a603c4dcb3deb56f603 import (
            Pattern,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Pattern", None) is not None:
                return self._properties.get("Pattern")
        return Pattern(self)

    @property
    def ClearOverlays(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClearOverlays"])

    @ClearOverlays.setter
    def ClearOverlays(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClearOverlays"], value)

    @property
    def CustomIsExtended(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomIsExtended"])

    @CustomIsExtended.setter
    def CustomIsExtended(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomIsExtended"], value)

    @property
    def OperationIndex(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["OperationIndex"])

    @OperationIndex.setter
    def OperationIndex(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OperationIndex"], value)

    @property
    def PerSessionOverlayIndices(self):
        """
        Returns
        -------
        - dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str]): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PerSessionOverlayIndices"])

    @PerSessionOverlayIndices.setter
    def PerSessionOverlayIndices(self, value):
        self._set_attribute(self._SDM_ATT_MAP["PerSessionOverlayIndices"], value)

    @property
    def PerSessionOverlayValues(self):
        """
        Returns
        -------
        - dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str]): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PerSessionOverlayValues"])

    @PerSessionOverlayValues.setter
    def PerSessionOverlayValues(self, value):
        self._set_attribute(self._SDM_ATT_MAP["PerSessionOverlayValues"], value)

    @property
    def SingleValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SingleValue"])

    @SingleValue.setter
    def SingleValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SingleValue"], value)

    @property
    def StringApplyPatternExpression(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["StringApplyPatternExpression"])

    @StringApplyPatternExpression.setter
    def StringApplyPatternExpression(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StringApplyPatternExpression"], value)

    def update(
        self,
        ClearOverlays=None,
        CustomIsExtended=None,
        OperationIndex=None,
        PerSessionOverlayIndices=None,
        PerSessionOverlayValues=None,
        SingleValue=None,
        StringApplyPatternExpression=None,
    ):
        """Updates value resource on the server.

        Args
        ----
        - ClearOverlays (bool): NOT DEFINED
        - CustomIsExtended (bool): NOT DEFINED
        - OperationIndex (number): NOT DEFINED
        - PerSessionOverlayIndices (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): NOT DEFINED
        - PerSessionOverlayValues (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): NOT DEFINED
        - SingleValue (str): NOT DEFINED
        - StringApplyPatternExpression (str): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ClearOverlays=None,
        CustomIsExtended=None,
        OperationIndex=None,
        PerSessionOverlayIndices=None,
        PerSessionOverlayValues=None,
        SingleValue=None,
        StringApplyPatternExpression=None,
    ):
        """Adds a new value resource on the server and adds it to the container.

        Args
        ----
        - ClearOverlays (bool): NOT DEFINED
        - CustomIsExtended (bool): NOT DEFINED
        - OperationIndex (number): NOT DEFINED
        - PerSessionOverlayIndices (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): NOT DEFINED
        - PerSessionOverlayValues (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): NOT DEFINED
        - SingleValue (str): NOT DEFINED
        - StringApplyPatternExpression (str): NOT DEFINED

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
        ClearOverlays=None,
        CustomIsExtended=None,
        OperationIndex=None,
        PerSessionOverlayIndices=None,
        PerSessionOverlayValues=None,
        SingleValue=None,
        StringApplyPatternExpression=None,
    ):
        """Finds and retrieves value resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve value resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all value resources from the server.

        Args
        ----
        - ClearOverlays (bool): NOT DEFINED
        - CustomIsExtended (bool): NOT DEFINED
        - OperationIndex (number): NOT DEFINED
        - PerSessionOverlayIndices (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): NOT DEFINED
        - PerSessionOverlayValues (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): NOT DEFINED
        - SingleValue (str): NOT DEFINED
        - StringApplyPatternExpression (str): NOT DEFINED

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
