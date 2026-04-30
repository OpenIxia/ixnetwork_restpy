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


class Layer4(Base):
    """The application traffic of Layer 4.
    The Layer4 class encapsulates a required layer4 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "layer4"
    _SDM_ATT_MAP = {
        "DestPort": "destPort",
        "DestPortDistr": "destPortDistr",
        "DestPortMv": "destPortMv",
        "IdDistributionSupported": "idDistributionSupported",
        "IncrDestPortAcross": "incrDestPortAcross",
        "IncrDestPortSame": "incrDestPortSame",
        "IncrSrcPortAcross": "incrSrcPortAcross",
        "IncrSrcPortSame": "incrSrcPortSame",
        "L4Protocol": "l4Protocol",
        "SrcPort": "srcPort",
        "SrcPortDistr": "srcPortDistr",
        "SrcPortMv": "srcPortMv",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Layer4, self).__init__(parent, list_op)

    @property
    def DestPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the destination port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestPort"])

    @DestPort.setter
    def DestPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestPort"], value)

    @property
    def DestPortDistr(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If true, the destination port is distributed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestPortDistr"])

    @DestPortDistr.setter
    def DestPortDistr(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestPortDistr"], value)

    @property
    def DestPortMv(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value of the destination port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestPortMv"])

    @DestPortMv.setter
    def DestPortMv(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestPortMv"], value)

    @property
    def IdDistributionSupported(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IdDistributionSupported"])

    @IdDistributionSupported.setter
    def IdDistributionSupported(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IdDistributionSupported"], value)

    @property
    def IncrDestPortAcross(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the option Increment is selected under Use Destination Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrDestPortAcross"])

    @IncrDestPortAcross.setter
    def IncrDestPortAcross(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrDestPortAcross"], value)

    @property
    def IncrDestPortSame(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the selection of the relevant option to increment all destination ports included in the test with the same value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrDestPortSame"])

    @IncrDestPortSame.setter
    def IncrDestPortSame(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrDestPortSame"], value)

    @property
    def IncrSrcPortAcross(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the option Increment is selected under Use Source Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrSrcPortAcross"])

    @IncrSrcPortAcross.setter
    def IncrSrcPortAcross(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrSrcPortAcross"], value)

    @property
    def IncrSrcPortSame(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the selection of the relevant option to increment all source ports included in the test with the same value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrSrcPortSame"])

    @IncrSrcPortSame.setter
    def IncrSrcPortSame(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrSrcPortSame"], value)

    @property
    def L4Protocol(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the Layer 4 Protocol settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["L4Protocol"])

    @L4Protocol.setter
    def L4Protocol(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["L4Protocol"], value)

    @property
    def SrcPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the source port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcPort"])

    @SrcPort.setter
    def SrcPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcPort"], value)

    @property
    def SrcPortDistr(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If true, the source port is distributed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcPortDistr"])

    @SrcPortDistr.setter
    def SrcPortDistr(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcPortDistr"], value)

    @property
    def SrcPortMv(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value of the source port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcPortMv"])

    @SrcPortMv.setter
    def SrcPortMv(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcPortMv"], value)

    def update(
        self,
        DestPort=None,
        DestPortDistr=None,
        DestPortMv=None,
        IdDistributionSupported=None,
        IncrDestPortAcross=None,
        IncrDestPortSame=None,
        IncrSrcPortAcross=None,
        IncrSrcPortSame=None,
        L4Protocol=None,
        SrcPort=None,
        SrcPortDistr=None,
        SrcPortMv=None,
    ):
        # type: (int, str, str, str, bool, bool, bool, bool, str, int, str, str) -> Layer4
        """Updates layer4 resource on the server.

        Args
        ----
        - DestPort (number): Indicates the destination port.
        - DestPortDistr (str): If true, the destination port is distributed.
        - DestPortMv (str): The value of the destination port.
        - IdDistributionSupported (str): NOT DEFINED
        - IncrDestPortAcross (bool): This signifies the option Increment is selected under Use Destination Port.
        - IncrDestPortSame (bool): This signifies the selection of the relevant option to increment all destination ports included in the test with the same value.
        - IncrSrcPortAcross (bool): This signifies the option Increment is selected under Use Source Port.
        - IncrSrcPortSame (bool): This signifies the selection of the relevant option to increment all source ports included in the test with the same value.
        - L4Protocol (str): This signifies the Layer 4 Protocol settings.
        - SrcPort (number): Indicates the source port.
        - SrcPortDistr (str): If true, the source port is distributed.
        - SrcPortMv (str): The value of the source port.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        DestPort=None,
        DestPortDistr=None,
        DestPortMv=None,
        IdDistributionSupported=None,
        IncrDestPortAcross=None,
        IncrDestPortSame=None,
        IncrSrcPortAcross=None,
        IncrSrcPortSame=None,
        L4Protocol=None,
        SrcPort=None,
        SrcPortDistr=None,
        SrcPortMv=None,
    ):
        # type: (int, str, str, str, bool, bool, bool, bool, str, int, str, str) -> Layer4
        """Finds and retrieves layer4 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve layer4 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all layer4 resources from the server.

        Args
        ----
        - DestPort (number): Indicates the destination port.
        - DestPortDistr (str): If true, the destination port is distributed.
        - DestPortMv (str): The value of the destination port.
        - IdDistributionSupported (str): NOT DEFINED
        - IncrDestPortAcross (bool): This signifies the option Increment is selected under Use Destination Port.
        - IncrDestPortSame (bool): This signifies the selection of the relevant option to increment all destination ports included in the test with the same value.
        - IncrSrcPortAcross (bool): This signifies the option Increment is selected under Use Source Port.
        - IncrSrcPortSame (bool): This signifies the selection of the relevant option to increment all source ports included in the test with the same value.
        - L4Protocol (str): This signifies the Layer 4 Protocol settings.
        - SrcPort (number): Indicates the source port.
        - SrcPortDistr (str): If true, the source port is distributed.
        - SrcPortMv (str): The value of the source port.

        Returns
        -------
        - self: This instance with matching layer4 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of layer4 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the layer4 resources from the server available through an iterator or index

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
