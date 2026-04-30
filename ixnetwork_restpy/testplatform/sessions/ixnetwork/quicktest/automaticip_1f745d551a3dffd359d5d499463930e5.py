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


class AutomaticIp(Base):
    """It signifies the automatic IP.
    The AutomaticIp class encapsulates a list of automaticIp resources that are managed by the system.
    A list of resources can be retrieved from the server using the AutomaticIp.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "automaticIp"
    _SDM_ATT_MAP = {
        "AssignExcludedPorts": "assignExcludedPorts",
        "EnableGwAddrIncr": "enableGwAddrIncr",
        "FirstSrcMac": "firstSrcMac",
        "IncludeValidationTraffic": "includeValidationTraffic",
        "ShowAssignExcludedPorts": "showAssignExcludedPorts",
        "ShowQoS": "showQoS",
        "SrcMacIncr": "srcMacIncr",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(AutomaticIp, self).__init__(parent, list_op)

    @property
    def AddrCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.addrcount_8103ec82d99ac7930132cbaee0daaaec.AddrCount): An instance of the AddrCount class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.addrcount_8103ec82d99ac7930132cbaee0daaaec import (
            AddrCount,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AddrCount", None) is not None:
                return self._properties.get("AddrCount")
        return AddrCount(self)._select()

    @property
    def Ip(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ip_fecc22879d751d7128036791d1081cc6.Ip): An instance of the Ip class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ip_fecc22879d751d7128036791d1081cc6 import (
            Ip,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ip", None) is not None:
                return self._properties.get("Ip")
        return Ip(self)._select()

    @property
    def Layer4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.layer4_57d0c461b9b738380fa0354ebc4ee8e9.Layer4): An instance of the Layer4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.layer4_57d0c461b9b738380fa0354ebc4ee8e9 import (
            Layer4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Layer4", None) is not None:
                return self._properties.get("Layer4")
        return Layer4(self)._select()

    @property
    def Payload(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.payload_1f6bf4eefe3df9197d5c83a3ddfd3925.Payload): An instance of the Payload class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.payload_1f6bf4eefe3df9197d5c83a3ddfd3925 import (
            Payload,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Payload", None) is not None:
                return self._properties.get("Payload")
        return Payload(self)._select()

    @property
    def Qos(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.qos_425a54915e652b80adb6171f7b4705aa.Qos): An instance of the Qos class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.qos_425a54915e652b80adb6171f7b4705aa import (
            Qos,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Qos", None) is not None:
                return self._properties.get("Qos")
        return Qos(self)._select()

    @property
    def Vlan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.vlan_36ee717c0e34f96e3957d47f76e2715e.Vlan): An instance of the Vlan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.vlan_36ee717c0e34f96e3957d47f76e2715e import (
            Vlan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Vlan", None) is not None:
                return self._properties.get("Vlan")
        return Vlan(self)._select()

    @property
    def AssignExcludedPorts(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, assigns excluded ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssignExcludedPorts"])

    @AssignExcludedPorts.setter
    def AssignExcludedPorts(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AssignExcludedPorts"], value)

    @property
    def EnableGwAddrIncr(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables increment of Gateway address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableGwAddrIncr"])

    @EnableGwAddrIncr.setter
    def EnableGwAddrIncr(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableGwAddrIncr"], value)

    @property
    def FirstSrcMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the first source MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirstSrcMac"])

    @FirstSrcMac.setter
    def FirstSrcMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirstSrcMac"], value)

    @property
    def IncludeValidationTraffic(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, includes validation traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeValidationTraffic"])

    @IncludeValidationTraffic.setter
    def IncludeValidationTraffic(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeValidationTraffic"], value)

    @property
    def ShowAssignExcludedPorts(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, shows assigned excluded ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowAssignExcludedPorts"])

    @ShowAssignExcludedPorts.setter
    def ShowAssignExcludedPorts(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowAssignExcludedPorts"], value)

    @property
    def ShowQoS(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, shows the quality of service.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowQoS"])

    @ShowQoS.setter
    def ShowQoS(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowQoS"], value)

    @property
    def SrcMacIncr(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the Increment of source MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcMacIncr"])

    @SrcMacIncr.setter
    def SrcMacIncr(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrcMacIncr"], value)

    def update(
        self,
        AssignExcludedPorts=None,
        EnableGwAddrIncr=None,
        FirstSrcMac=None,
        IncludeValidationTraffic=None,
        ShowAssignExcludedPorts=None,
        ShowQoS=None,
        SrcMacIncr=None,
    ):
        # type: (bool, bool, str, bool, bool, bool, str) -> AutomaticIp
        """Updates automaticIp resource on the server.

        Args
        ----
        - AssignExcludedPorts (bool): If true, assigns excluded ports.
        - EnableGwAddrIncr (bool): If true, enables increment of Gateway address.
        - FirstSrcMac (str): Signifies the first source MAC address.
        - IncludeValidationTraffic (bool): If true, includes validation traffic.
        - ShowAssignExcludedPorts (bool): If true, shows assigned excluded ports.
        - ShowQoS (bool): If true, shows the quality of service.
        - SrcMacIncr (str): Signifies the Increment of source MAC address.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AssignExcludedPorts=None,
        EnableGwAddrIncr=None,
        FirstSrcMac=None,
        IncludeValidationTraffic=None,
        ShowAssignExcludedPorts=None,
        ShowQoS=None,
        SrcMacIncr=None,
    ):
        # type: (bool, bool, str, bool, bool, bool, str) -> AutomaticIp
        """Adds a new automaticIp resource on the json, only valid with batch add utility

        Args
        ----
        - AssignExcludedPorts (bool): If true, assigns excluded ports.
        - EnableGwAddrIncr (bool): If true, enables increment of Gateway address.
        - FirstSrcMac (str): Signifies the first source MAC address.
        - IncludeValidationTraffic (bool): If true, includes validation traffic.
        - ShowAssignExcludedPorts (bool): If true, shows assigned excluded ports.
        - ShowQoS (bool): If true, shows the quality of service.
        - SrcMacIncr (str): Signifies the Increment of source MAC address.

        Returns
        -------
        - self: This instance with all currently retrieved automaticIp resources using find and the newly added automaticIp resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AssignExcludedPorts=None,
        EnableGwAddrIncr=None,
        FirstSrcMac=None,
        IncludeValidationTraffic=None,
        ShowAssignExcludedPorts=None,
        ShowQoS=None,
        SrcMacIncr=None,
    ):
        # type: (bool, bool, str, bool, bool, bool, str) -> AutomaticIp
        """Finds and retrieves automaticIp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve automaticIp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all automaticIp resources from the server.

        Args
        ----
        - AssignExcludedPorts (bool): If true, assigns excluded ports.
        - EnableGwAddrIncr (bool): If true, enables increment of Gateway address.
        - FirstSrcMac (str): Signifies the first source MAC address.
        - IncludeValidationTraffic (bool): If true, includes validation traffic.
        - ShowAssignExcludedPorts (bool): If true, shows assigned excluded ports.
        - ShowQoS (bool): If true, shows the quality of service.
        - SrcMacIncr (str): Signifies the Increment of source MAC address.

        Returns
        -------
        - self: This instance with matching automaticIp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of automaticIp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the automaticIp resources from the server available through an iterator or index

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
