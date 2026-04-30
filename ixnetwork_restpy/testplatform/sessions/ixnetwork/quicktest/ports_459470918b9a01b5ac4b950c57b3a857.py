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
    """This object configures the ports.
    The Ports class encapsulates a list of ports resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ports.find() method.
    The list can be managed by using the Ports.add() and Ports.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "ports"
    _SDM_ATT_MAP = {
        "Id__": "__id__",
        "AssignedTo": "assignedTo",
        "Burdentraffictype": "burdentraffictype",
        "Cardtype": "cardtype",
        "InTest": "inTest",
        "Name": "name",
        "UseAsMonitor": "useAsMonitor",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Ports, self).__init__(parent, list_op)

    @property
    def SlavechassisConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.slavechassisconfig_602e2ee626ea498772ba394525f3f3e4.SlavechassisConfig): An instance of the SlavechassisConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.slavechassisconfig_602e2ee626ea498772ba394525f3f3e4 import (
            SlavechassisConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SlavechassisConfig", None) is not None:
                return self._properties.get("SlavechassisConfig")
        return SlavechassisConfig(self)._select()

    @property
    def Id__(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport): The unique identification of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Id__"])

    @Id__.setter
    def Id__(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Id__"], value)

    @property
    def AssignedTo(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The port to which the traffic is assigned.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssignedTo"])

    @AssignedTo.setter
    def AssignedTo(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AssignedTo"], value)

    @property
    def Burdentraffictype(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The traffic type is burden.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Burdentraffictype"])

    @Burdentraffictype.setter
    def Burdentraffictype(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Burdentraffictype"], value)

    @property
    def Cardtype(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The type of the traffic card.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Cardtype"])

    @Cardtype.setter
    def Cardtype(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Cardtype"], value)

    @property
    def InTest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the traffic item is included in the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InTest"])

    @InTest.setter
    def InTest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InTest"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def UseAsMonitor(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sets the port as a monitor port in order to capture flooded frames comming from the other ports included in the test
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseAsMonitor"])

    @UseAsMonitor.setter
    def UseAsMonitor(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseAsMonitor"], value)

    def update(
        self,
        Id__=None,
        AssignedTo=None,
        Burdentraffictype=None,
        Cardtype=None,
        InTest=None,
        Name=None,
        UseAsMonitor=None,
    ):
        # type: (str, str, str, str, bool, str, bool) -> Ports
        """Updates ports resource on the server.

        Args
        ----
        - Id__ (str(None | /api/v1/sessions/1/ixnetwork/vport)): The unique identification of the port.
        - AssignedTo (str): The port to which the traffic is assigned.
        - Burdentraffictype (str): The traffic type is burden.
        - Cardtype (str): The type of the traffic card.
        - InTest (bool): If true, the traffic item is included in the test.
        - Name (str): The name of the port.
        - UseAsMonitor (bool): Sets the port as a monitor port in order to capture flooded frames comming from the other ports included in the test

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Id__=None,
        AssignedTo=None,
        Burdentraffictype=None,
        Cardtype=None,
        InTest=None,
        Name=None,
        UseAsMonitor=None,
    ):
        # type: (str, str, str, str, bool, str, bool) -> Ports
        """Adds a new ports resource on the server and adds it to the container.

        Args
        ----
        - Id__ (str(None | /api/v1/sessions/1/ixnetwork/vport)): The unique identification of the port.
        - AssignedTo (str): The port to which the traffic is assigned.
        - Burdentraffictype (str): The traffic type is burden.
        - Cardtype (str): The type of the traffic card.
        - InTest (bool): If true, the traffic item is included in the test.
        - Name (str): The name of the port.
        - UseAsMonitor (bool): Sets the port as a monitor port in order to capture flooded frames comming from the other ports included in the test

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
        Id__=None,
        AssignedTo=None,
        Burdentraffictype=None,
        Cardtype=None,
        InTest=None,
        Name=None,
        UseAsMonitor=None,
    ):
        # type: (str, str, str, str, bool, str, bool) -> Ports
        """Finds and retrieves ports resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ports resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ports resources from the server.

        Args
        ----
        - Id__ (str(None | /api/v1/sessions/1/ixnetwork/vport)): The unique identification of the port.
        - AssignedTo (str): The port to which the traffic is assigned.
        - Burdentraffictype (str): The traffic type is burden.
        - Cardtype (str): The type of the traffic card.
        - InTest (bool): If true, the traffic item is included in the test.
        - Name (str): The name of the port.
        - UseAsMonitor (bool): Sets the port as a monitor port in order to capture flooded frames comming from the other ports included in the test

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
