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


class Rfc2889partiallyMeshed(Base):
    """The RFC 2889Partially Meshed test determines the maximum throughput of the DUT while transmitting and receiving traffic on multiple ports.
    The Rfc2889partiallyMeshed class encapsulates a list of rfc2889partiallyMeshed resources that are managed by the user.
    A list of resources can be retrieved from the server using the Rfc2889partiallyMeshed.find() method.
    The list can be managed by using the Rfc2889partiallyMeshed.add() and Rfc2889partiallyMeshed.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "rfc2889partiallyMeshed"
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
        super(Rfc2889partiallyMeshed, self).__init__(parent, list_op)

    @property
    def CpfFrameData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cpfframedata_fa910c381a377e4bf2649a04d940a7e2.CpfFrameData): An instance of the CpfFrameData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cpfframedata_fa910c381a377e4bf2649a04d940a7e2 import (
            CpfFrameData,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CpfFrameData", None) is not None:
                return self._properties.get("CpfFrameData")
        return CpfFrameData(self)

    @property
    def EndpointMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.endpointmode_17c8bc2d1c5049ba8e6298e774994909.EndpointMode): An instance of the EndpointMode class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.endpointmode_17c8bc2d1c5049ba8e6298e774994909 import (
            EndpointMode,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EndpointMode", None) is not None:
                return self._properties.get("EndpointMode")
        return EndpointMode(self)

    @property
    def EthernetWizard(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ethernetwizard_84a96b4a565b7d16d8357ccef8173ec8.EthernetWizard): An instance of the EthernetWizard class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ethernetwizard_84a96b4a565b7d16d8357ccef8173ec8 import (
            EthernetWizard,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EthernetWizard", None) is not None:
                return self._properties.get("EthernetWizard")
        return EthernetWizard(self)._select()

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
    def IpmixWizard(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipmixwizard_6329ba5794c6429ccd5bf27bfdf158a6.IpmixWizard): An instance of the IpmixWizard class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipmixwizard_6329ba5794c6429ccd5bf27bfdf158a6 import (
            IpmixWizard,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IpmixWizard", None) is not None:
                return self._properties.get("IpmixWizard")
        return IpmixWizard(self)._select()

    @property
    def Ipv4Wizard(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv4wizard_91a927f614356e9f0b94b89798006948.Ipv4Wizard): An instance of the Ipv4Wizard class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv4wizard_91a927f614356e9f0b94b89798006948 import (
            Ipv4Wizard,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4Wizard", None) is not None:
                return self._properties.get("Ipv4Wizard")
        return Ipv4Wizard(self)._select()

    @property
    def Ipv6Wizard(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv6wizard_69e9a4de10dd12f0cbaad0edf0105169.Ipv6Wizard): An instance of the Ipv6Wizard class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv6wizard_69e9a4de10dd12f0cbaad0edf0105169 import (
            Ipv6Wizard,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6Wizard", None) is not None:
                return self._properties.get("Ipv6Wizard")
        return Ipv6Wizard(self)._select()

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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.passcriteria_2f84ada625563113d3ef4f44b25dd7e2.PassCriteria): An instance of the PassCriteria class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.passcriteria_2f84ada625563113d3ef4f44b25dd7e2 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ports_efcfda96caaf36de660944ce80de4ead.Ports): An instance of the Ports class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ports_efcfda96caaf36de660944ce80de4ead import (
            Ports,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ports", None) is not None:
                return self._properties.get("Ports")
        return Ports(self)

    @property
    def ProtocolSettings(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.protocolsettings_9e9d742e3a23cbc20a6e857cc5199d20.ProtocolSettings): An instance of the ProtocolSettings class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.protocolsettings_9e9d742e3a23cbc20a6e857cc5199d20 import (
            ProtocolSettings,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ProtocolSettings", None) is not None:
                return self._properties.get("ProtocolSettings")
        return ProtocolSettings(self)

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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.testconfig_42106b603a8d7271cf49ddaa967ae740.TestConfig): An instance of the TestConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.testconfig_42106b603a8d7271cf49ddaa967ae740 import (
            TestConfig,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TestConfig", None) is not None:
                return self._properties.get("TestConfig")
        return TestConfig(self)._select()

    @property
    def TrafficMapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficmapping_2d3494e619a86bce8bf8c64253f5a31d.TrafficMapping): An instance of the TrafficMapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficmapping_2d3494e619a86bce8bf8c64253f5a31d import (
            TrafficMapping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficMapping", None) is not None:
                return self._properties.get("TrafficMapping")
        return TrafficMapping(self)

    @property
    def TrafficSelection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficselection_e70293c1d497ca3a4de220ed6cf2ab95.TrafficSelection): An instance of the TrafficSelection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.trafficselection_e70293c1d497ca3a4de220ed6cf2ab95 import (
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
        # type: (bool, str, str, str) -> Rfc2889partiallyMeshed
        """Updates rfc2889partiallyMeshed resource on the server.

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
        # type: (bool, str, str, str) -> Rfc2889partiallyMeshed
        """Adds a new rfc2889partiallyMeshed resource on the server and adds it to the container.

        Args
        ----
        - ForceApplyQTConfig (bool): Apply QT config
        - InputParameters (str): Input Parameters
        - Mode (str(existingMode | newMode)): Test mode
        - Name (str): Test name

        Returns
        -------
        - self: This instance with all currently retrieved rfc2889partiallyMeshed resources using find and the newly added rfc2889partiallyMeshed resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained rfc2889partiallyMeshed resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ForceApplyQTConfig=None, InputParameters=None, Mode=None, Name=None):
        # type: (bool, str, str, str) -> Rfc2889partiallyMeshed
        """Finds and retrieves rfc2889partiallyMeshed resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rfc2889partiallyMeshed resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rfc2889partiallyMeshed resources from the server.

        Args
        ----
        - ForceApplyQTConfig (bool): Apply QT config
        - InputParameters (str): Input Parameters
        - Mode (str(existingMode | newMode)): Test mode
        - Name (str): Test name

        Returns
        -------
        - self: This instance with matching rfc2889partiallyMeshed resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rfc2889partiallyMeshed data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rfc2889partiallyMeshed resources from the server available through an iterator or index

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
