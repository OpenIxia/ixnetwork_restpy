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


class PppoxClientAtmPage(Base):
    """It signifies the PPPOX client ATM page.
    The PppoxClientAtmPage class encapsulates a list of pppoxClientAtmPage resources that are managed by the system.
    A list of resources can be retrieved from the server using the PppoxClientAtmPage.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "pppoxClientAtmPage"
    _SDM_ATT_MAP = {
        "Encapsulation": "encapsulation",
        "IncrementBy": "incrementBy",
        "IncrementMode": "incrementMode",
        "Mac": "mac",
        "RangeMacIncrement": "rangeMacIncrement",
        "VciFirstId": "vciFirstId",
        "VciIncrement": "vciIncrement",
        "VciIncrementStep": "vciIncrementStep",
        "VciRangeIncrement": "vciRangeIncrement",
        "VciUniqueCount": "vciUniqueCount",
        "VpiFirstId": "vpiFirstId",
        "VpiIncrement": "vpiIncrement",
        "VpiIncrementStep": "vpiIncrementStep",
        "VpiRangeIncrement": "vpiRangeIncrement",
        "VpiUniqueCount": "vpiUniqueCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PppoxClientAtmPage, self).__init__(parent, list_op)

    @property
    def Encapsulation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The encapsulation for each traffic item.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Encapsulation"])

    @Encapsulation.setter
    def Encapsulation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Encapsulation"], value)

    @property
    def IncrementBy(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the increment value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementBy"])

    @IncrementBy.setter
    def IncrementBy(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementBy"], value)

    @property
    def IncrementMode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It increments the mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementMode"])

    @IncrementMode.setter
    def IncrementMode(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementMode"], value)

    @property
    def Mac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It is the MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mac"])

    @Mac.setter
    def Mac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mac"], value)

    @property
    def RangeMacIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It increments the range MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeMacIncrement"])

    @RangeMacIncrement.setter
    def RangeMacIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeMacIncrement"], value)

    @property
    def VciFirstId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the first ID of VCI.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VciFirstId"])

    @VciFirstId.setter
    def VciFirstId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VciFirstId"], value)

    @property
    def VciIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It increments the VCI.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VciIncrement"])

    @VciIncrement.setter
    def VciIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VciIncrement"], value)

    @property
    def VciIncrementStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It increments the step value for VCI.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VciIncrementStep"])

    @VciIncrementStep.setter
    def VciIncrementStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VciIncrementStep"], value)

    @property
    def VciRangeIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It increments the VCI range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VciRangeIncrement"])

    @VciRangeIncrement.setter
    def VciRangeIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VciRangeIncrement"], value)

    @property
    def VciUniqueCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the VCI unique count.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VciUniqueCount"])

    @VciUniqueCount.setter
    def VciUniqueCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VciUniqueCount"], value)

    @property
    def VpiFirstId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the first ID of VPI.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VpiFirstId"])

    @VpiFirstId.setter
    def VpiFirstId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VpiFirstId"], value)

    @property
    def VpiIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It increments the VPI.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VpiIncrement"])

    @VpiIncrement.setter
    def VpiIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VpiIncrement"], value)

    @property
    def VpiIncrementStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It increments the step value for VPI.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VpiIncrementStep"])

    @VpiIncrementStep.setter
    def VpiIncrementStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VpiIncrementStep"], value)

    @property
    def VpiRangeIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It increments the VPI range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VpiRangeIncrement"])

    @VpiRangeIncrement.setter
    def VpiRangeIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VpiRangeIncrement"], value)

    @property
    def VpiUniqueCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the VpI unique count.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VpiUniqueCount"])

    @VpiUniqueCount.setter
    def VpiUniqueCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VpiUniqueCount"], value)

    def update(
        self,
        Encapsulation=None,
        IncrementBy=None,
        IncrementMode=None,
        Mac=None,
        RangeMacIncrement=None,
        VciFirstId=None,
        VciIncrement=None,
        VciIncrementStep=None,
        VciRangeIncrement=None,
        VciUniqueCount=None,
        VpiFirstId=None,
        VpiIncrement=None,
        VpiIncrementStep=None,
        VpiRangeIncrement=None,
        VpiUniqueCount=None,
    ):
        # type: (str, str, int, str, str, int, int, int, int, int, int, int, int, int, int) -> PppoxClientAtmPage
        """Updates pppoxClientAtmPage resource on the server.

        Args
        ----
        - Encapsulation (str): The encapsulation for each traffic item.
        - IncrementBy (str): It signifies the increment value.
        - IncrementMode (number): It increments the mode.
        - Mac (str): It is the MAC address.
        - RangeMacIncrement (str): It increments the range MAC address.
        - VciFirstId (number): It signifies the first ID of VCI.
        - VciIncrement (number): It increments the VCI.
        - VciIncrementStep (number): It increments the step value for VCI.
        - VciRangeIncrement (number): It increments the VCI range.
        - VciUniqueCount (number): It signifies the VCI unique count.
        - VpiFirstId (number): It signifies the first ID of VPI.
        - VpiIncrement (number): It increments the VPI.
        - VpiIncrementStep (number): It increments the step value for VPI.
        - VpiRangeIncrement (number): It increments the VPI range.
        - VpiUniqueCount (number): It signifies the VpI unique count.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Encapsulation=None,
        IncrementBy=None,
        IncrementMode=None,
        Mac=None,
        RangeMacIncrement=None,
        VciFirstId=None,
        VciIncrement=None,
        VciIncrementStep=None,
        VciRangeIncrement=None,
        VciUniqueCount=None,
        VpiFirstId=None,
        VpiIncrement=None,
        VpiIncrementStep=None,
        VpiRangeIncrement=None,
        VpiUniqueCount=None,
    ):
        # type: (str, str, int, str, str, int, int, int, int, int, int, int, int, int, int) -> PppoxClientAtmPage
        """Adds a new pppoxClientAtmPage resource on the json, only valid with batch add utility

        Args
        ----
        - Encapsulation (str): The encapsulation for each traffic item.
        - IncrementBy (str): It signifies the increment value.
        - IncrementMode (number): It increments the mode.
        - Mac (str): It is the MAC address.
        - RangeMacIncrement (str): It increments the range MAC address.
        - VciFirstId (number): It signifies the first ID of VCI.
        - VciIncrement (number): It increments the VCI.
        - VciIncrementStep (number): It increments the step value for VCI.
        - VciRangeIncrement (number): It increments the VCI range.
        - VciUniqueCount (number): It signifies the VCI unique count.
        - VpiFirstId (number): It signifies the first ID of VPI.
        - VpiIncrement (number): It increments the VPI.
        - VpiIncrementStep (number): It increments the step value for VPI.
        - VpiRangeIncrement (number): It increments the VPI range.
        - VpiUniqueCount (number): It signifies the VpI unique count.

        Returns
        -------
        - self: This instance with all currently retrieved pppoxClientAtmPage resources using find and the newly added pppoxClientAtmPage resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Encapsulation=None,
        IncrementBy=None,
        IncrementMode=None,
        Mac=None,
        RangeMacIncrement=None,
        VciFirstId=None,
        VciIncrement=None,
        VciIncrementStep=None,
        VciRangeIncrement=None,
        VciUniqueCount=None,
        VpiFirstId=None,
        VpiIncrement=None,
        VpiIncrementStep=None,
        VpiRangeIncrement=None,
        VpiUniqueCount=None,
    ):
        # type: (str, str, int, str, str, int, int, int, int, int, int, int, int, int, int) -> PppoxClientAtmPage
        """Finds and retrieves pppoxClientAtmPage resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pppoxClientAtmPage resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pppoxClientAtmPage resources from the server.

        Args
        ----
        - Encapsulation (str): The encapsulation for each traffic item.
        - IncrementBy (str): It signifies the increment value.
        - IncrementMode (number): It increments the mode.
        - Mac (str): It is the MAC address.
        - RangeMacIncrement (str): It increments the range MAC address.
        - VciFirstId (number): It signifies the first ID of VCI.
        - VciIncrement (number): It increments the VCI.
        - VciIncrementStep (number): It increments the step value for VCI.
        - VciRangeIncrement (number): It increments the VCI range.
        - VciUniqueCount (number): It signifies the VCI unique count.
        - VpiFirstId (number): It signifies the first ID of VPI.
        - VpiIncrement (number): It increments the VPI.
        - VpiIncrementStep (number): It increments the step value for VPI.
        - VpiRangeIncrement (number): It increments the VPI range.
        - VpiUniqueCount (number): It signifies the VpI unique count.

        Returns
        -------
        - self: This instance with matching pppoxClientAtmPage resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pppoxClientAtmPage data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pppoxClientAtmPage resources from the server available through an iterator or index

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
