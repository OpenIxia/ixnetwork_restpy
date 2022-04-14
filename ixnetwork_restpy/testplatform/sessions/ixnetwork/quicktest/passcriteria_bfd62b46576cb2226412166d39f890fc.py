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


class PassCriteria(Base):
    """NOT DEFINED
    The PassCriteria class encapsulates a required passCriteria resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "passCriteria"
    _SDM_ATT_MAP = {
        "EnableFrameLossPassFail": "enableFrameLossPassFail",
        "LossThresholdMode": "lossThresholdMode",
        "LossThresholdValue": "lossThresholdValue",
        "PassCriteriaLoadRateMode": "passCriteriaLoadRateMode",
        "PassCriteriaLoadRateScale": "passCriteriaLoadRateScale",
        "PassCriteriaLoadRateValue": "passCriteriaLoadRateValue",
        "PassFailFrequency": "passFailFrequency",
        "PassFailMeasureUnit": "passFailMeasureUnit",
    }
    _SDM_ENUM_MAP = {
        "lossThresholdMode": ["average", "maximum"],
        "passCriteriaLoadRateMode": ["average", "minimum"],
        "passCriteriaLoadRateScale": ["fps", "gbps", "kbps", "mbps", "percent"],
        "passFailFrequency": ["framesizes", "trials"],
        "passFailMeasureUnit": ["fps"],
    }

    def __init__(self, parent, list_op=False):
        super(PassCriteria, self).__init__(parent, list_op)

    @property
    def EnableFrameLossPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableFrameLossPassFail"])

    @EnableFrameLossPassFail.setter
    def EnableFrameLossPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableFrameLossPassFail"], value)

    @property
    def LossThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LossThresholdMode"])

    @LossThresholdMode.setter
    def LossThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LossThresholdMode"], value)

    @property
    def LossThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LossThresholdValue"])

    @LossThresholdValue.setter
    def LossThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LossThresholdValue"], value)

    @property
    def PassCriteriaLoadRateMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | minimum): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PassCriteriaLoadRateMode"])

    @PassCriteriaLoadRateMode.setter
    def PassCriteriaLoadRateMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PassCriteriaLoadRateMode"], value)

    @property
    def PassCriteriaLoadRateScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fps | gbps | kbps | mbps | percent): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PassCriteriaLoadRateScale"])

    @PassCriteriaLoadRateScale.setter
    def PassCriteriaLoadRateScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PassCriteriaLoadRateScale"], value)

    @property
    def PassCriteriaLoadRateValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PassCriteriaLoadRateValue"])

    @PassCriteriaLoadRateValue.setter
    def PassCriteriaLoadRateValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PassCriteriaLoadRateValue"], value)

    @property
    def PassFailFrequency(self):
        # type: () -> str
        """
        Returns
        -------
        - str(framesizes | trials): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PassFailFrequency"])

    @PassFailFrequency.setter
    def PassFailFrequency(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PassFailFrequency"], value)

    @property
    def PassFailMeasureUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fps): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PassFailMeasureUnit"])

    @PassFailMeasureUnit.setter
    def PassFailMeasureUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PassFailMeasureUnit"], value)

    def update(
        self,
        EnableFrameLossPassFail=None,
        LossThresholdMode=None,
        LossThresholdValue=None,
        PassCriteriaLoadRateMode=None,
        PassCriteriaLoadRateScale=None,
        PassCriteriaLoadRateValue=None,
        PassFailFrequency=None,
        PassFailMeasureUnit=None,
    ):
        # type: (bool, str, int, str, str, int, str, str) -> PassCriteria
        """Updates passCriteria resource on the server.

        Args
        ----
        - EnableFrameLossPassFail (bool): NOT DEFINED
        - LossThresholdMode (str(average | maximum)): NOT DEFINED
        - LossThresholdValue (number): NOT DEFINED
        - PassCriteriaLoadRateMode (str(average | minimum)): NOT DEFINED
        - PassCriteriaLoadRateScale (str(fps | gbps | kbps | mbps | percent)): NOT DEFINED
        - PassCriteriaLoadRateValue (number): NOT DEFINED
        - PassFailFrequency (str(framesizes | trials)): NOT DEFINED
        - PassFailMeasureUnit (str(fps)): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnableFrameLossPassFail=None,
        LossThresholdMode=None,
        LossThresholdValue=None,
        PassCriteriaLoadRateMode=None,
        PassCriteriaLoadRateScale=None,
        PassCriteriaLoadRateValue=None,
        PassFailFrequency=None,
        PassFailMeasureUnit=None,
    ):
        # type: (bool, str, int, str, str, int, str, str) -> PassCriteria
        """Finds and retrieves passCriteria resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve passCriteria resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all passCriteria resources from the server.

        Args
        ----
        - EnableFrameLossPassFail (bool): NOT DEFINED
        - LossThresholdMode (str(average | maximum)): NOT DEFINED
        - LossThresholdValue (number): NOT DEFINED
        - PassCriteriaLoadRateMode (str(average | minimum)): NOT DEFINED
        - PassCriteriaLoadRateScale (str(fps | gbps | kbps | mbps | percent)): NOT DEFINED
        - PassCriteriaLoadRateValue (number): NOT DEFINED
        - PassFailFrequency (str(framesizes | trials)): NOT DEFINED
        - PassFailMeasureUnit (str(fps)): NOT DEFINED

        Returns
        -------
        - self: This instance with matching passCriteria resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of passCriteria data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the passCriteria resources from the server available through an iterator or index

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
