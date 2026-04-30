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


class Ports(Base):
    """Allows the user to define the port configuration.
    The Ports class encapsulates a list of ports resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ports.find() method.
    The list can be managed by using the Ports.add() and Ports.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "ports"
    _SDM_ATT_MAP = {
        "Description": "description",
        "Enabled": "enabled",
        "FlowControl": "flowControl",
        "LeftSide": "leftSide",
        "ProtocolSummary": "protocolSummary",
        "RightSide": "rightSide",
        "Type": "type",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Ports, self).__init__(parent, list_op)

    @property
    def Description(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the description for the port group lists.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Description"])

    @Description.setter
    def Description(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Description"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the outer VLAN range is included in the configuration. If disabled, the range is neither validated, nor configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def FlowControl(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/quickTest/fcoeMaxNoDropThroughput/fcoeWizard/fcoeFlowControl/profiles): If selected, enables the port's flow control mechanisms.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowControl"])

    @FlowControl.setter
    def FlowControl(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowControl"], value)

    @property
    def LeftSide(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Determines if the port is serving as the FCoE initiator in the test topology.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LeftSide"])

    @LeftSide.setter
    def LeftSide(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LeftSide"], value)

    @property
    def ProtocolSummary(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates which Data Center Bridging fibre channel protocol (FCoE, FC, DCBX) the wizard will configure on the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolSummary"])

    @ProtocolSummary.setter
    def ProtocolSummary(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtocolSummary"], value)

    @property
    def RightSide(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Determines if the port is serving as the FCoE target in the test topology.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RightSide"])

    @RightSide.setter
    def RightSide(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RightSide"], value)

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    @Type.setter
    def Type(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Type"], value)

    def update(
        self,
        Description=None,
        Enabled=None,
        FlowControl=None,
        LeftSide=None,
        ProtocolSummary=None,
        RightSide=None,
        Type=None,
    ):
        # type: (str, bool, str, bool, str, bool, str) -> Ports
        """Updates ports resource on the server.

        Args
        ----
        - Description (str): It signifies the description for the port group lists.
        - Enabled (bool): If true, the outer VLAN range is included in the configuration. If disabled, the range is neither validated, nor configured.
        - FlowControl (str(None | /api/v1/sessions/1/ixnetwork/quickTest/fcoeMaxNoDropThroughput/fcoeWizard/fcoeFlowControl/profiles)): If selected, enables the port's flow control mechanisms.
        - LeftSide (bool): Determines if the port is serving as the FCoE initiator in the test topology.
        - ProtocolSummary (str): Indicates which Data Center Bridging fibre channel protocol (FCoE, FC, DCBX) the wizard will configure on the port.
        - RightSide (bool): Determines if the port is serving as the FCoE target in the test topology.
        - Type (str): It signifies the type.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Description=None,
        Enabled=None,
        FlowControl=None,
        LeftSide=None,
        ProtocolSummary=None,
        RightSide=None,
        Type=None,
    ):
        # type: (str, bool, str, bool, str, bool, str) -> Ports
        """Adds a new ports resource on the server and adds it to the container.

        Args
        ----
        - Description (str): It signifies the description for the port group lists.
        - Enabled (bool): If true, the outer VLAN range is included in the configuration. If disabled, the range is neither validated, nor configured.
        - FlowControl (str(None | /api/v1/sessions/1/ixnetwork/quickTest/fcoeMaxNoDropThroughput/fcoeWizard/fcoeFlowControl/profiles)): If selected, enables the port's flow control mechanisms.
        - LeftSide (bool): Determines if the port is serving as the FCoE initiator in the test topology.
        - ProtocolSummary (str): Indicates which Data Center Bridging fibre channel protocol (FCoE, FC, DCBX) the wizard will configure on the port.
        - RightSide (bool): Determines if the port is serving as the FCoE target in the test topology.
        - Type (str): It signifies the type.

        Returns
        -------
        - self: This instance with all currently retrieved ports resources using find and the newly added ports resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ports resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Description=None,
        Enabled=None,
        FlowControl=None,
        LeftSide=None,
        ProtocolSummary=None,
        RightSide=None,
        Type=None,
    ):
        # type: (str, bool, str, bool, str, bool, str) -> Ports
        """Finds and retrieves ports resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ports resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ports resources from the server.

        Args
        ----
        - Description (str): It signifies the description for the port group lists.
        - Enabled (bool): If true, the outer VLAN range is included in the configuration. If disabled, the range is neither validated, nor configured.
        - FlowControl (str(None | /api/v1/sessions/1/ixnetwork/quickTest/fcoeMaxNoDropThroughput/fcoeWizard/fcoeFlowControl/profiles)): If selected, enables the port's flow control mechanisms.
        - LeftSide (bool): Determines if the port is serving as the FCoE initiator in the test topology.
        - ProtocolSummary (str): Indicates which Data Center Bridging fibre channel protocol (FCoE, FC, DCBX) the wizard will configure on the port.
        - RightSide (bool): Determines if the port is serving as the FCoE target in the test topology.
        - Type (str): It signifies the type.

        Returns
        -------
        - self: This instance with matching ports resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ports data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ports resources from the server available through an iterator or index

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
