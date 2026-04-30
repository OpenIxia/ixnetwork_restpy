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


class TlvSettings(Base):
    """This object is used to configure the DCBX TLV settings.
    The TlvSettings class encapsulates a required tlvSettings resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "tlvSettings"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TlvSettings, self).__init__(parent, list_op)

    @property
    def DcbxTlvAppQaz(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvappqaz_819c8383811198034a3e35296c297b8d.DcbxTlvAppQaz): An instance of the DcbxTlvAppQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvappqaz_819c8383811198034a3e35296c297b8d import (
            DcbxTlvAppQaz,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvAppQaz", None) is not None:
                return self._properties.get("DcbxTlvAppQaz")
        return DcbxTlvAppQaz(self)

    @property
    def DcbxTlvBcn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvbcn_cadebd8ec0147d276cb7631123a5b7fa.DcbxTlvBcn): An instance of the DcbxTlvBcn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvbcn_cadebd8ec0147d276cb7631123a5b7fa import (
            DcbxTlvBcn,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvBcn", None) is not None:
                return self._properties.get("DcbxTlvBcn")
        return DcbxTlvBcn(self)

    @property
    def DcbxTlvCustom(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvcustom_dd1cce65eb6ad28bdec7fec2678e64ef.DcbxTlvCustom): An instance of the DcbxTlvCustom class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvcustom_dd1cce65eb6ad28bdec7fec2678e64ef import (
            DcbxTlvCustom,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvCustom", None) is not None:
                return self._properties.get("DcbxTlvCustom")
        return DcbxTlvCustom(self)

    @property
    def DcbxTlvEtsQaz(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvetsqaz_f30b1d71ebf33d60075fdd1d071280b6.DcbxTlvEtsQaz): An instance of the DcbxTlvEtsQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvetsqaz_f30b1d71ebf33d60075fdd1d071280b6 import (
            DcbxTlvEtsQaz,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvEtsQaz", None) is not None:
                return self._properties.get("DcbxTlvEtsQaz")
        return DcbxTlvEtsQaz(self)

    @property
    def DcbxTlvFcoeIeee(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvfcoeieee_23d7609075401f2287118df5ec92e55f.DcbxTlvFcoeIeee): An instance of the DcbxTlvFcoeIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvfcoeieee_23d7609075401f2287118df5ec92e55f import (
            DcbxTlvFcoeIeee,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvFcoeIeee", None) is not None:
                return self._properties.get("DcbxTlvFcoeIeee")
        return DcbxTlvFcoeIeee(self)

    @property
    def DcbxTlvFcoeIntel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvfcoeintel_33119795332388d1604783cd78b4f25f.DcbxTlvFcoeIntel): An instance of the DcbxTlvFcoeIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvfcoeintel_33119795332388d1604783cd78b4f25f import (
            DcbxTlvFcoeIntel,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvFcoeIntel", None) is not None:
                return self._properties.get("DcbxTlvFcoeIntel")
        return DcbxTlvFcoeIntel(self)

    @property
    def DcbxTlvLogicalLink(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvlogicallink_9635b2972bb6bd6a91cd215bbe72f4e1.DcbxTlvLogicalLink): An instance of the DcbxTlvLogicalLink class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvlogicallink_9635b2972bb6bd6a91cd215bbe72f4e1 import (
            DcbxTlvLogicalLink,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvLogicalLink", None) is not None:
                return self._properties.get("DcbxTlvLogicalLink")
        return DcbxTlvLogicalLink(self)

    @property
    def DcbxTlvNivIeee(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvnivieee_e75b1bbfff6941a7c7382afedc900d17.DcbxTlvNivIeee): An instance of the DcbxTlvNivIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvnivieee_e75b1bbfff6941a7c7382afedc900d17 import (
            DcbxTlvNivIeee,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvNivIeee", None) is not None:
                return self._properties.get("DcbxTlvNivIeee")
        return DcbxTlvNivIeee(self)

    @property
    def DcbxTlvNivIntel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvnivintel_90540adb9ebfec9c7611a9732a3e52db.DcbxTlvNivIntel): An instance of the DcbxTlvNivIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvnivintel_90540adb9ebfec9c7611a9732a3e52db import (
            DcbxTlvNivIntel,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvNivIntel", None) is not None:
                return self._properties.get("DcbxTlvNivIntel")
        return DcbxTlvNivIntel(self)

    @property
    def DcbxTlvPfcIeee(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvpfcieee_ce0377463578d2258be61b53c031f528.DcbxTlvPfcIeee): An instance of the DcbxTlvPfcIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvpfcieee_ce0377463578d2258be61b53c031f528 import (
            DcbxTlvPfcIeee,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvPfcIeee", None) is not None:
                return self._properties.get("DcbxTlvPfcIeee")
        return DcbxTlvPfcIeee(self)

    @property
    def DcbxTlvPfcIntel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvpfcintel_6969561f0b3561ab52aac963fc4de727.DcbxTlvPfcIntel): An instance of the DcbxTlvPfcIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvpfcintel_6969561f0b3561ab52aac963fc4de727 import (
            DcbxTlvPfcIntel,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvPfcIntel", None) is not None:
                return self._properties.get("DcbxTlvPfcIntel")
        return DcbxTlvPfcIntel(self)

    @property
    def DcbxTlvPfcQaz(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvpfcqaz_588d6e51da02145ff3cb69c99483c0ac.DcbxTlvPfcQaz): An instance of the DcbxTlvPfcQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvpfcqaz_588d6e51da02145ff3cb69c99483c0ac import (
            DcbxTlvPfcQaz,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvPfcQaz", None) is not None:
                return self._properties.get("DcbxTlvPfcQaz")
        return DcbxTlvPfcQaz(self)

    @property
    def DcbxTlvPgIeee(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvpgieee_9efdde3ce928917a47df57ed0f492144.DcbxTlvPgIeee): An instance of the DcbxTlvPgIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvpgieee_9efdde3ce928917a47df57ed0f492144 import (
            DcbxTlvPgIeee,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvPgIeee", None) is not None:
                return self._properties.get("DcbxTlvPgIeee")
        return DcbxTlvPgIeee(self)

    @property
    def DcbxTlvPgIntel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvpgintel_ab546fe8c19974710b92646daf3f3a38.DcbxTlvPgIntel): An instance of the DcbxTlvPgIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dcbxtlvpgintel_ab546fe8c19974710b92646daf3f3a38 import (
            DcbxTlvPgIntel,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvPgIntel", None) is not None:
                return self._properties.get("DcbxTlvPgIntel")
        return DcbxTlvPgIntel(self)

    def find(self):
        """Finds and retrieves tlvSettings resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tlvSettings resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tlvSettings resources from the server.

        Returns
        -------
        - self: This instance with matching tlvSettings resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tlvSettings data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tlvSettings resources from the server available through an iterator or index

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
