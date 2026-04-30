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


class OpenFlowWizard(Base):
    """This object enables the selection of multiple ports and creation of multiple routers, interfaces, and instances on these ports.
    The OpenFlowWizard class encapsulates a required openFlowWizard resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "openFlowWizard"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(OpenFlowWizard, self).__init__(parent, list_op)

    @property
    def PageIdOpenFlowActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowactions_a9697470cb162a6f5d4b2539a4f7cd6f.PageIdOpenFlowActions): An instance of the PageIdOpenFlowActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowactions_a9697470cb162a6f5d4b2539a4f7cd6f import (
            PageIdOpenFlowActions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PageIdOpenFlowActions", None) is not None:
                return self._properties.get("PageIdOpenFlowActions")
        return PageIdOpenFlowActions(self)

    @property
    def PageIdOpenFlowController(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowcontroller_9c088e5c1e7bc02ab5fb66ab27af0a23.PageIdOpenFlowController): An instance of the PageIdOpenFlowController class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowcontroller_9c088e5c1e7bc02ab5fb66ab27af0a23 import (
            PageIdOpenFlowController,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PageIdOpenFlowController", None) is not None:
                return self._properties.get("PageIdOpenFlowController")
        return PageIdOpenFlowController(self)

    @property
    def PageIdOpenFlowFlowRanges(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowflowranges_0eda67754e9907095bc533295c59c8e6.PageIdOpenFlowFlowRanges): An instance of the PageIdOpenFlowFlowRanges class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowflowranges_0eda67754e9907095bc533295c59c8e6 import (
            PageIdOpenFlowFlowRanges,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PageIdOpenFlowFlowRanges", None) is not None:
                return self._properties.get("PageIdOpenFlowFlowRanges")
        return PageIdOpenFlowFlowRanges(self)

    @property
    def PageIdOpenFlowFlowRanges131(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowflowranges131_30019d39c75e0e494fbfb7683aba538d.PageIdOpenFlowFlowRanges131): An instance of the PageIdOpenFlowFlowRanges131 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowflowranges131_30019d39c75e0e494fbfb7683aba538d import (
            PageIdOpenFlowFlowRanges131,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PageIdOpenFlowFlowRanges131", None) is not None:
                return self._properties.get("PageIdOpenFlowFlowRanges131")
        return PageIdOpenFlowFlowRanges131(self)

    @property
    def PageIdOpenFlowGroup131(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowgroup131_6721876b510d675d789cf6c0c2a704dc.PageIdOpenFlowGroup131): An instance of the PageIdOpenFlowGroup131 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowgroup131_6721876b510d675d789cf6c0c2a704dc import (
            PageIdOpenFlowGroup131,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PageIdOpenFlowGroup131", None) is not None:
                return self._properties.get("PageIdOpenFlowGroup131")
        return PageIdOpenFlowGroup131(self)

    @property
    def PageIdOpenFlowInPortMapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowinportmapping_92adbdc91e1568219f5659ef0b74ebe0.PageIdOpenFlowInPortMapping): An instance of the PageIdOpenFlowInPortMapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowinportmapping_92adbdc91e1568219f5659ef0b74ebe0 import (
            PageIdOpenFlowInPortMapping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PageIdOpenFlowInPortMapping", None) is not None:
                return self._properties.get("PageIdOpenFlowInPortMapping")
        return PageIdOpenFlowInPortMapping(self)

    @property
    def PageIdOpenFlowInstructions131(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowinstructions131_0460be7a07714ee121aea1a8c6098cca.PageIdOpenFlowInstructions131): An instance of the PageIdOpenFlowInstructions131 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowinstructions131_0460be7a07714ee121aea1a8c6098cca import (
            PageIdOpenFlowInstructions131,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PageIdOpenFlowInstructions131", None) is not None:
                return self._properties.get("PageIdOpenFlowInstructions131")
        return PageIdOpenFlowInstructions131(self)

    @property
    def PageIdOpenFlowMeters131(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowmeters131_6c0d10373edc935f370a3601291db759.PageIdOpenFlowMeters131): An instance of the PageIdOpenFlowMeters131 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowmeters131_6c0d10373edc935f370a3601291db759 import (
            PageIdOpenFlowMeters131,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PageIdOpenFlowMeters131", None) is not None:
                return self._properties.get("PageIdOpenFlowMeters131")
        return PageIdOpenFlowMeters131(self)

    @property
    def PageIdOpenFlowOfChannel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowofchannel_256535b4ed48c0d801464bda733d18a8.PageIdOpenFlowOfChannel): An instance of the PageIdOpenFlowOfChannel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowofchannel_256535b4ed48c0d801464bda733d18a8 import (
            PageIdOpenFlowOfChannel,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PageIdOpenFlowOfChannel", None) is not None:
                return self._properties.get("PageIdOpenFlowOfChannel")
        return PageIdOpenFlowOfChannel(self)

    @property
    def PageIdOpenFlowOutPortMapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowoutportmapping_3b5fc90ddd803b62cc134610ffb7aad1.PageIdOpenFlowOutPortMapping): An instance of the PageIdOpenFlowOutPortMapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowoutportmapping_3b5fc90ddd803b62cc134610ffb7aad1 import (
            PageIdOpenFlowOutPortMapping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PageIdOpenFlowOutPortMapping", None) is not None:
                return self._properties.get("PageIdOpenFlowOutPortMapping")
        return PageIdOpenFlowOutPortMapping(self)

    @property
    def PageIdOpenFlowTrafficInterface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowtrafficinterface_ff6662e9ad5d5799a8604b5a248e49f8.PageIdOpenFlowTrafficInterface): An instance of the PageIdOpenFlowTrafficInterface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pageidopenflowtrafficinterface_ff6662e9ad5d5799a8604b5a248e49f8 import (
            PageIdOpenFlowTrafficInterface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PageIdOpenFlowTrafficInterface", None) is not None:
                return self._properties.get("PageIdOpenFlowTrafficInterface")
        return PageIdOpenFlowTrafficInterface(self)

    def find(self):
        """Finds and retrieves openFlowWizard resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve openFlowWizard resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all openFlowWizard resources from the server.

        Returns
        -------
        - self: This instance with matching openFlowWizard resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of openFlowWizard data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the openFlowWizard resources from the server available through an iterator or index

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
