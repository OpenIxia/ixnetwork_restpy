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


class MulticastJoinLeaveConfig(Base):
    """The join leave configurations of the multicast are described here
    The MulticastJoinLeaveConfig class encapsulates a list of multicastJoinLeaveConfig resources that are managed by the user.
    A list of resources can be retrieved from the server using the MulticastJoinLeaveConfig.find() method.
    The list can be managed by using the MulticastJoinLeaveConfig.add() and MulticastJoinLeaveConfig.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "multicastJoinLeaveConfig"
    _SDM_ATT_MAP = {
        "NumTxInterfaces": "numTxInterfaces",
        "RxPortForJoinExisting": "rxPortForJoinExisting",
        "TrafficType": "trafficType",
    }
    _SDM_ENUM_MAP = {
        "trafficType": ["ipmix", "ipv4", "ipv6", "mac"],
    }

    def __init__(self, parent, list_op=False):
        super(MulticastJoinLeaveConfig, self).__init__(parent, list_op)

    @property
    def JoinLeaveTraffic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.joinleavetraffic_6f7db97bc390adf0da32128fde214db7.JoinLeaveTraffic): An instance of the JoinLeaveTraffic class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.joinleavetraffic_6f7db97bc390adf0da32128fde214db7 import (
            JoinLeaveTraffic,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("JoinLeaveTraffic", None) is not None:
                return self._properties.get("JoinLeaveTraffic")
        return JoinLeaveTraffic(self)

    @property
    def MulticastGroups(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastgroups_33c9cd16c19c214df07bb10f94712303.MulticastGroups): An instance of the MulticastGroups class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.multicastgroups_33c9cd16c19c214df07bb10f94712303 import (
            MulticastGroups,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastGroups", None) is not None:
                return self._properties.get("MulticastGroups")
        return MulticastGroups(self)

    @property
    def RxPortsToInterfaces(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rxportstointerfaces_b514fe5f8385baadfa5c6276729669b5.RxPortsToInterfaces): An instance of the RxPortsToInterfaces class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rxportstointerfaces_b514fe5f8385baadfa5c6276729669b5 import (
            RxPortsToInterfaces,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RxPortsToInterfaces", None) is not None:
                return self._properties.get("RxPortsToInterfaces")
        return RxPortsToInterfaces(self)

    @property
    def RxPortsToMultipleInterfaces(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rxportstomultipleinterfaces_5655144d5564e2464eb8c7db539d0683.RxPortsToMultipleInterfaces): An instance of the RxPortsToMultipleInterfaces class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rxportstomultipleinterfaces_5655144d5564e2464eb8c7db539d0683 import (
            RxPortsToMultipleInterfaces,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RxPortsToMultipleInterfaces", None) is not None:
                return self._properties.get("RxPortsToMultipleInterfaces")
        return RxPortsToMultipleInterfaces(self)

    @property
    def TimingTraffic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.timingtraffic_aef27a6ca722468a6fed89317c41c951.TimingTraffic): An instance of the TimingTraffic class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.timingtraffic_aef27a6ca722468a6fed89317c41c951 import (
            TimingTraffic,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TimingTraffic", None) is not None:
                return self._properties.get("TimingTraffic")
        return TimingTraffic(self)

    @property
    def ValidationTraffic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.validationtraffic_84a8b304c9ca433b408621510572cf33.ValidationTraffic): An instance of the ValidationTraffic class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.validationtraffic_84a8b304c9ca433b408621510572cf33 import (
            ValidationTraffic,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ValidationTraffic", None) is not None:
                return self._properties.get("ValidationTraffic")
        return ValidationTraffic(self)

    @property
    def NumTxInterfaces(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the transmission of numbers to user interface
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumTxInterfaces"])

    @NumTxInterfaces.setter
    def NumTxInterfaces(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumTxInterfaces"], value)

    @property
    def RxPortForJoinExisting(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport): The receiving port for joining the existing protocols are described here
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPortForJoinExisting"])

    @RxPortForJoinExisting.setter
    def RxPortForJoinExisting(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPortForJoinExisting"], value)

    @property
    def TrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipmix | ipv4 | ipv6 | mac): It signifies the traffic type
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficType"])

    @TrafficType.setter
    def TrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficType"], value)

    def update(
        self, NumTxInterfaces=None, RxPortForJoinExisting=None, TrafficType=None
    ):
        # type: (int, str, str) -> MulticastJoinLeaveConfig
        """Updates multicastJoinLeaveConfig resource on the server.

        Args
        ----
        - NumTxInterfaces (number): It signifies the transmission of numbers to user interface
        - RxPortForJoinExisting (str(None | /api/v1/sessions/1/ixnetwork/vport)): The receiving port for joining the existing protocols are described here
        - TrafficType (str(ipmix | ipv4 | ipv6 | mac)): It signifies the traffic type

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, NumTxInterfaces=None, RxPortForJoinExisting=None, TrafficType=None):
        # type: (int, str, str) -> MulticastJoinLeaveConfig
        """Adds a new multicastJoinLeaveConfig resource on the server and adds it to the container.

        Args
        ----
        - NumTxInterfaces (number): It signifies the transmission of numbers to user interface
        - RxPortForJoinExisting (str(None | /api/v1/sessions/1/ixnetwork/vport)): The receiving port for joining the existing protocols are described here
        - TrafficType (str(ipmix | ipv4 | ipv6 | mac)): It signifies the traffic type

        Returns
        -------
        - self: This instance with all currently retrieved multicastJoinLeaveConfig resources using find and the newly added multicastJoinLeaveConfig resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained multicastJoinLeaveConfig resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, NumTxInterfaces=None, RxPortForJoinExisting=None, TrafficType=None):
        # type: (int, str, str) -> MulticastJoinLeaveConfig
        """Finds and retrieves multicastJoinLeaveConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve multicastJoinLeaveConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all multicastJoinLeaveConfig resources from the server.

        Args
        ----
        - NumTxInterfaces (number): It signifies the transmission of numbers to user interface
        - RxPortForJoinExisting (str(None | /api/v1/sessions/1/ixnetwork/vport)): The receiving port for joining the existing protocols are described here
        - TrafficType (str(ipmix | ipv4 | ipv6 | mac)): It signifies the traffic type

        Returns
        -------
        - self: This instance with matching multicastJoinLeaveConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of multicastJoinLeaveConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the multicastJoinLeaveConfig resources from the server available through an iterator or index

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
