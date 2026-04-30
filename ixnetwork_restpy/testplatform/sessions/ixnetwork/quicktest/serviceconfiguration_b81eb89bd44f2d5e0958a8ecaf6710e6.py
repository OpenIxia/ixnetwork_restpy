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


class ServiceConfiguration(Base):
    """The service configuration parameters.
    The ServiceConfiguration class encapsulates a list of serviceConfiguration resources that are managed by the user.
    A list of resources can be retrieved from the server using the ServiceConfiguration.find() method.
    The list can be managed by using the ServiceConfiguration.add() and ServiceConfiguration.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "serviceConfiguration"
    _SDM_ATT_MAP = {
        "IsCirPerFlowGroup": "isCirPerFlowGroup",
        "IsColorAware": "isColorAware",
        "IsPerformance": "isPerformance",
        "RateUnit": "rateUnit",
        "TimeUnit": "timeUnit",
        "TrafficType": "trafficType",
    }
    _SDM_ENUM_MAP = {
        "rateUnit": ["bps", "Gbps", "Kbps", "Mbps"],
        "timeUnit": ["ms", "ns", "us"],
        "trafficType": ["ipv4", "ipv6", "mac"],
    }

    def __init__(self, parent, list_op=False):
        super(ServiceConfiguration, self).__init__(parent, list_op)

    @property
    def Services(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.services_1cc698de4909ad80b59855a5c2899c97.Services): An instance of the Services class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.services_1cc698de4909ad80b59855a5c2899c97 import (
            Services,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Services", None) is not None:
                return self._properties.get("Services")
        return Services(self)

    @property
    def IsCirPerFlowGroup(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true it enables the cir per flowgroup
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsCirPerFlowGroup"])

    @IsCirPerFlowGroup.setter
    def IsCirPerFlowGroup(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsCirPerFlowGroup"], value)

    @property
    def IsColorAware(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it becomes aware of the color.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsColorAware"])

    @IsColorAware.setter
    def IsColorAware(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsColorAware"], value)

    @property
    def IsPerformance(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it enables the performance.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsPerformance"])

    @IsPerformance.setter
    def IsPerformance(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsPerformance"], value)

    @property
    def RateUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bps | Gbps | Kbps | Mbps): The service configuration rate unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RateUnit"])

    @RateUnit.setter
    def RateUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RateUnit"], value)

    @property
    def TimeUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | ns | us): The service configuration time unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TimeUnit"])

    @TimeUnit.setter
    def TimeUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TimeUnit"], value)

    @property
    def TrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipv4 | ipv6 | mac): The traffic type in use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficType"])

    @TrafficType.setter
    def TrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficType"], value)

    def update(
        self,
        IsCirPerFlowGroup=None,
        IsColorAware=None,
        IsPerformance=None,
        RateUnit=None,
        TimeUnit=None,
        TrafficType=None,
    ):
        # type: (bool, bool, bool, str, str, str) -> ServiceConfiguration
        """Updates serviceConfiguration resource on the server.

        Args
        ----
        - IsCirPerFlowGroup (bool): If true it enables the cir per flowgroup
        - IsColorAware (bool): If true, it becomes aware of the color.
        - IsPerformance (bool): If true, it enables the performance.
        - RateUnit (str(bps | Gbps | Kbps | Mbps)): The service configuration rate unit.
        - TimeUnit (str(ms | ns | us)): The service configuration time unit.
        - TrafficType (str(ipv4 | ipv6 | mac)): The traffic type in use.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        IsCirPerFlowGroup=None,
        IsColorAware=None,
        IsPerformance=None,
        RateUnit=None,
        TimeUnit=None,
        TrafficType=None,
    ):
        # type: (bool, bool, bool, str, str, str) -> ServiceConfiguration
        """Adds a new serviceConfiguration resource on the server and adds it to the container.

        Args
        ----
        - IsCirPerFlowGroup (bool): If true it enables the cir per flowgroup
        - IsColorAware (bool): If true, it becomes aware of the color.
        - IsPerformance (bool): If true, it enables the performance.
        - RateUnit (str(bps | Gbps | Kbps | Mbps)): The service configuration rate unit.
        - TimeUnit (str(ms | ns | us)): The service configuration time unit.
        - TrafficType (str(ipv4 | ipv6 | mac)): The traffic type in use.

        Returns
        -------
        - self: This instance with all currently retrieved serviceConfiguration resources using find and the newly added serviceConfiguration resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained serviceConfiguration resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        IsCirPerFlowGroup=None,
        IsColorAware=None,
        IsPerformance=None,
        RateUnit=None,
        TimeUnit=None,
        TrafficType=None,
    ):
        # type: (bool, bool, bool, str, str, str) -> ServiceConfiguration
        """Finds and retrieves serviceConfiguration resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve serviceConfiguration resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all serviceConfiguration resources from the server.

        Args
        ----
        - IsCirPerFlowGroup (bool): If true it enables the cir per flowgroup
        - IsColorAware (bool): If true, it becomes aware of the color.
        - IsPerformance (bool): If true, it enables the performance.
        - RateUnit (str(bps | Gbps | Kbps | Mbps)): The service configuration rate unit.
        - TimeUnit (str(ms | ns | us)): The service configuration time unit.
        - TrafficType (str(ipv4 | ipv6 | mac)): The traffic type in use.

        Returns
        -------
        - self: This instance with matching serviceConfiguration resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of serviceConfiguration data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the serviceConfiguration resources from the server available through an iterator or index

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
