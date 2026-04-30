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


class CloudPerf(Base):
    """This measures the forwarding performance of data center top-of-rack switch or network by using simulated data center North-South and East-West traffic profiles.
    The CloudPerf class encapsulates a list of cloudPerf resources that are managed by the user.
    A list of resources can be retrieved from the server using the CloudPerf.find() method.
    The list can be managed by using the CloudPerf.add() and CloudPerf.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "cloudPerf"
    _SDM_ATT_MAP = {
        "ForceApplyQTConfig": "forceApplyQTConfig",
        "InputParameters": "inputParameters",
        "Mode": "mode",
        "Name": "name",
    }
    _SDM_ENUM_MAP = {
        "mode": ["existingMode", "newMode"],
    }

    def __init__(self, parent, list_op=False):
        super(CloudPerf, self).__init__(parent, list_op)

    @property
    def CapBackgroundTrafficSelection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.capbackgroundtrafficselection_3703ec9dbf26f3cb7f11ec8002934435.CapBackgroundTrafficSelection): An instance of the CapBackgroundTrafficSelection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.capbackgroundtrafficselection_3703ec9dbf26f3cb7f11ec8002934435 import (
            CapBackgroundTrafficSelection,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CapBackgroundTrafficSelection", None) is not None:
                return self._properties.get("CapBackgroundTrafficSelection")
        return CapBackgroundTrafficSelection(self)

    @property
    def FrameData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.framedata_5c34b7e3981fb5d7320658948cdcc1c1.FrameData): An instance of the FrameData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.framedata_5c34b7e3981fb5d7320658948cdcc1c1 import (
            FrameData,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FrameData", None) is not None:
                return self._properties.get("FrameData")
        return FrameData(self)

    @property
    def LearnFrames(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.learnframes_aff5042528d11d6e314f527665dc38f2.LearnFrames): An instance of the LearnFrames class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.learnframes_aff5042528d11d6e314f527665dc38f2 import (
            LearnFrames,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnFrames", None) is not None:
                return self._properties.get("LearnFrames")
        return LearnFrames(self)._select()

    @property
    def PassCriteria(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.passcriteria_f741c160036af93f7c679cb182075e56.PassCriteria): An instance of the PassCriteria class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.passcriteria_f741c160036af93f7c679cb182075e56 import (
            PassCriteria,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PassCriteria", None) is not None:
                return self._properties.get("PassCriteria")
        return PassCriteria(self)._select()

    @property
    def Ports(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ports_d1859f80b97a66f5939f9955bb32a229.Ports): An instance of the Ports class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ports_d1859f80b97a66f5939f9955bb32a229 import (
            Ports,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ports", None) is not None:
                return self._properties.get("Ports")
        return Ports(self)

    @property
    def Protocols(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.protocols_9a915e57e118f974c888001fce6e3692.Protocols): An instance of the Protocols class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.protocols_9a915e57e118f974c888001fce6e3692 import (
            Protocols,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Protocols", None) is not None:
                return self._properties.get("Protocols")
        return Protocols(self)

    @property
    def Results(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.results_23583c0cce1dabf7b75fe7d2ae18cfc4.Results): An instance of the Results class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.results_23583c0cce1dabf7b75fe7d2ae18cfc4 import (
            Results,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Results", None) is not None:
                return self._properties.get("Results")
        return Results(self)._select()

    @property
    def TestConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.testconfig_44c264bc2ea7f4205a6cb3d2991ce5ad.TestConfig): An instance of the TestConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.testconfig_44c264bc2ea7f4205a6cb3d2991ce5ad import (
            TestConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TestConfig", None) is not None:
                return self._properties.get("TestConfig")
        return TestConfig(self)._select()

    @property
    def TrafficConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficconfig_2bf6c23f622194f66aee1652ab9fdb19.TrafficConfig): An instance of the TrafficConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficconfig_2bf6c23f622194f66aee1652ab9fdb19 import (
            TrafficConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficConfig", None) is not None:
                return self._properties.get("TrafficConfig")
        return TrafficConfig(self)

    @property
    def TrafficSelection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficselection_4b9370a6ddada385ed5acebd896710e7.TrafficSelection): An instance of the TrafficSelection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficselection_4b9370a6ddada385ed5acebd896710e7 import (
            TrafficSelection,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficSelection", None) is not None:
                return self._properties.get("TrafficSelection")
        return TrafficSelection(self)

    @property
    def ForceApplyQTConfig(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Apply QT config
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForceApplyQTConfig"])

    @ForceApplyQTConfig.setter
    def ForceApplyQTConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForceApplyQTConfig"], value)

    @property
    def InputParameters(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Input Parameters
        """
        return self._get_attribute(self._SDM_ATT_MAP["InputParameters"])

    @InputParameters.setter
    def InputParameters(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InputParameters"], value)

    @property
    def Mode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(existingMode | newMode): Test mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mode"])

    @Mode.setter
    def Mode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mode"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Test name
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    def update(
        self, ForceApplyQTConfig=None, InputParameters=None, Mode=None, Name=None
    ):
        # type: (bool, str, str, str) -> CloudPerf
        """Updates cloudPerf resource on the server.

        Args
        ----
        - ForceApplyQTConfig (bool): Apply QT config
        - InputParameters (str): Input Parameters
        - Mode (str(existingMode | newMode)): Test mode
        - Name (str): Test name

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ForceApplyQTConfig=None, InputParameters=None, Mode=None, Name=None):
        # type: (bool, str, str, str) -> CloudPerf
        """Adds a new cloudPerf resource on the server and adds it to the container.

        Args
        ----
        - ForceApplyQTConfig (bool): Apply QT config
        - InputParameters (str): Input Parameters
        - Mode (str(existingMode | newMode)): Test mode
        - Name (str): Test name

        Returns
        -------
        - self: This instance with all currently retrieved cloudPerf resources using find and the newly added cloudPerf resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained cloudPerf resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ForceApplyQTConfig=None, InputParameters=None, Mode=None, Name=None):
        # type: (bool, str, str, str) -> CloudPerf
        """Finds and retrieves cloudPerf resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cloudPerf resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cloudPerf resources from the server.

        Args
        ----
        - ForceApplyQTConfig (bool): Apply QT config
        - InputParameters (str): Input Parameters
        - Mode (str(existingMode | newMode)): Test mode
        - Name (str): Test name

        Returns
        -------
        - self: This instance with matching cloudPerf resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cloudPerf data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cloudPerf resources from the server available through an iterator or index

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
