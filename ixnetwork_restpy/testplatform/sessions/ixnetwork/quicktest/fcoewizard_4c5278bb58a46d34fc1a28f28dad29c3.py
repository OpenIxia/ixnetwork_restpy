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


class FcoeWizard(Base):
    """Allows the user to define the FCoE/FC client protocols.
    The FcoeWizard class encapsulates a required fcoeWizard resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "fcoeWizard"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(FcoeWizard, self).__init__(parent, list_op)

    @property
    def DcbxPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxpage_661c2e4fa775cf199879845907fdc7d6.DcbxPage): An instance of the DcbxPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxpage_661c2e4fa775cf199879845907fdc7d6 import (
            DcbxPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxPage", None) is not None:
                return self._properties.get("DcbxPage")
        return DcbxPage(self)

    @property
    def DcbxTlvPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvpage_1e99d31b77ed42d29abf5effb59e1fc7.DcbxTlvPage): An instance of the DcbxTlvPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvpage_1e99d31b77ed42d29abf5effb59e1fc7 import (
            DcbxTlvPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvPage", None) is not None:
                return self._properties.get("DcbxTlvPage")
        return DcbxTlvPage(self)

    @property
    def FcVnportLeft(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcvnportleft_f5465390fdf8c9a7cfe277b07e51fdc9.FcVnportLeft): An instance of the FcVnportLeft class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcvnportleft_f5465390fdf8c9a7cfe277b07e51fdc9 import (
            FcVnportLeft,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcVnportLeft", None) is not None:
                return self._properties.get("FcVnportLeft")
        return FcVnportLeft(self)

    @property
    def FcVnportRight(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcvnportright_40ecedb233f83d6d95160d8090324c54.FcVnportRight): An instance of the FcVnportRight class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcvnportright_40ecedb233f83d6d95160d8090324c54 import (
            FcVnportRight,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcVnportRight", None) is not None:
                return self._properties.get("FcVnportRight")
        return FcVnportRight(self)

    @property
    def FcoeFipGen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoefipgen_072c28286a6487bcc41f860a6b3a67c0.FcoeFipGen): An instance of the FcoeFipGen class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoefipgen_072c28286a6487bcc41f860a6b3a67c0 import (
            FcoeFipGen,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeFipGen", None) is not None:
                return self._properties.get("FcoeFipGen")
        return FcoeFipGen(self)

    @property
    def FcoeFlowControl(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoeflowcontrol_75e2b8602a28859d2a93e40cb865ea44.FcoeFlowControl): An instance of the FcoeFlowControl class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoeflowcontrol_75e2b8602a28859d2a93e40cb865ea44 import (
            FcoeFlowControl,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeFlowControl", None) is not None:
                return self._properties.get("FcoeFlowControl")
        return FcoeFlowControl(self)

    @property
    def FcoeFwdGen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoefwdgen_a6cc67887087df4bd7af99877b80a915.FcoeFwdGen): An instance of the FcoeFwdGen class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoefwdgen_a6cc67887087df4bd7af99877b80a915 import (
            FcoeFwdGen,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeFwdGen", None) is not None:
                return self._properties.get("FcoeFwdGen")
        return FcoeFwdGen(self)

    @property
    def FcoeMacPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemacpage_b146845808a7d64b1e5ccd1c1de70600.FcoeMacPage): An instance of the FcoeMacPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemacpage_b146845808a7d64b1e5ccd1c1de70600 import (
            FcoeMacPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeMacPage", None) is not None:
                return self._properties.get("FcoeMacPage")
        return FcoeMacPage(self)

    @property
    def FcoePortSelection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoeportselection_565f34db41f3624f1367bb0321e2ea63.FcoePortSelection): An instance of the FcoePortSelection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoeportselection_565f34db41f3624f1367bb0321e2ea63 import (
            FcoePortSelection,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoePortSelection", None) is not None:
                return self._properties.get("FcoePortSelection")
        return FcoePortSelection(self)

    @property
    def FcoeVlanPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoevlanpage_46a5407afb298532d116cdf69f061a5b.FcoeVlanPage): An instance of the FcoeVlanPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoevlanpage_46a5407afb298532d116cdf69f061a5b import (
            FcoeVlanPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeVlanPage", None) is not None:
                return self._properties.get("FcoeVlanPage")
        return FcoeVlanPage(self)

    @property
    def FcoeVnportLeft(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoevnportleft_841a5965ea34fa1d0d019972121cae57.FcoeVnportLeft): An instance of the FcoeVnportLeft class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoevnportleft_841a5965ea34fa1d0d019972121cae57 import (
            FcoeVnportLeft,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeVnportLeft", None) is not None:
                return self._properties.get("FcoeVnportLeft")
        return FcoeVnportLeft(self)

    @property
    def FcoeVnportRight(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoevnportright_1457ce432044531e33e7253a13dab77f.FcoeVnportRight): An instance of the FcoeVnportRight class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoevnportright_1457ce432044531e33e7253a13dab77f import (
            FcoeVnportRight,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeVnportRight", None) is not None:
                return self._properties.get("FcoeVnportRight")
        return FcoeVnportRight(self)

    @property
    def LldpTlvPage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.lldptlvpage_60cb5df24a6aa440c1c2b1ca4b02b9bc.LldpTlvPage): An instance of the LldpTlvPage class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.lldptlvpage_60cb5df24a6aa440c1c2b1ca4b02b9bc import (
            LldpTlvPage,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LldpTlvPage", None) is not None:
                return self._properties.get("LldpTlvPage")
        return LldpTlvPage(self)

    def find(self):
        """Finds and retrieves fcoeWizard resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcoeWizard resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcoeWizard resources from the server.

        Returns
        -------
        - self: This instance with matching fcoeWizard resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcoeWizard data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcoeWizard resources from the server available through an iterator or index

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
