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


class ManualIpv6(Base):
    """The IPV6 address assigned manually.
    The ManualIpv6 class encapsulates a list of manualIpv6 resources that are managed by the user.
    A list of resources can be retrieved from the server using the ManualIpv6.find() method.
    The list can be managed by using the ManualIpv6.add() and ManualIpv6.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "manualIpv6"
    _SDM_ATT_MAP = {
        "AddrPerPort": "addrPerPort",
        "AssignConfig": "assignConfig",
        "FirstSrcMacMv": "firstSrcMacMv",
        "InTest": "inTest",
        "PortId": "portId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(ManualIpv6, self).__init__(parent, list_op)

    @property
    def Ipv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv6_db0a3271a06dcebc8d93a7e3553775f7.Ipv6): An instance of the Ipv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ipv6_db0a3271a06dcebc8d93a7e3553775f7 import (
            Ipv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6", None) is not None:
                return self._properties.get("Ipv6")
        return Ipv6(self)._select()

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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.qos_6a2461650e537d2f7c0c98997ab178c3.Qos): An instance of the Qos class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.qos_6a2461650e537d2f7c0c98997ab178c3 import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.vlan_44d3989b43c9f2706cf994550bce0ff7.Vlan): An instance of the Vlan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.vlan_44d3989b43c9f2706cf994550bce0ff7 import (
            Vlan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Vlan", None) is not None:
                return self._properties.get("Vlan")
        return Vlan(self)._select()

    @property
    def AddrPerPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The gateway address per port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddrPerPort"])

    @AddrPerPort.setter
    def AddrPerPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddrPerPort"], value)

    @property
    def AssignConfig(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the configuration is assigned to ports that are excluded from the test in the Ports window.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssignConfig"])

    @AssignConfig.setter
    def AssignConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AssignConfig"], value)

    @property
    def FirstSrcMacMv(self):
        """
        Returns
        -------
        - dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str]): The first source MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirstSrcMacMv"])

    @FirstSrcMacMv.setter
    def FirstSrcMacMv(self, value):
        self._set_attribute(self._SDM_ATT_MAP["FirstSrcMacMv"], value)

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
    def PortId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport): The Port identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortId"])

    @PortId.setter
    def PortId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortId"], value)

    def update(
        self,
        AddrPerPort=None,
        AssignConfig=None,
        FirstSrcMacMv=None,
        InTest=None,
        PortId=None,
    ):
        """Updates manualIpv6 resource on the server.

        Args
        ----
        - AddrPerPort (number): The gateway address per port.
        - AssignConfig (bool): If true, the configuration is assigned to ports that are excluded from the test in the Ports window.
        - FirstSrcMacMv (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): The first source MAC address.
        - InTest (bool): If true, the traffic item is included in the test.
        - PortId (str(None | /api/v1/sessions/1/ixnetwork/vport)): The Port identifier.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AddrPerPort=None,
        AssignConfig=None,
        FirstSrcMacMv=None,
        InTest=None,
        PortId=None,
    ):
        """Adds a new manualIpv6 resource on the server and adds it to the container.

        Args
        ----
        - AddrPerPort (number): The gateway address per port.
        - AssignConfig (bool): If true, the configuration is assigned to ports that are excluded from the test in the Ports window.
        - FirstSrcMacMv (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): The first source MAC address.
        - InTest (bool): If true, the traffic item is included in the test.
        - PortId (str(None | /api/v1/sessions/1/ixnetwork/vport)): The Port identifier.

        Returns
        -------
        - self: This instance with all currently retrieved manualIpv6 resources using find and the newly added manualIpv6 resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained manualIpv6 resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AddrPerPort=None,
        AssignConfig=None,
        FirstSrcMacMv=None,
        InTest=None,
        PortId=None,
    ):
        """Finds and retrieves manualIpv6 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve manualIpv6 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all manualIpv6 resources from the server.

        Args
        ----
        - AddrPerPort (number): The gateway address per port.
        - AssignConfig (bool): If true, the configuration is assigned to ports that are excluded from the test in the Ports window.
        - FirstSrcMacMv (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): The first source MAC address.
        - InTest (bool): If true, the traffic item is included in the test.
        - PortId (str(None | /api/v1/sessions/1/ixnetwork/vport)): The Port identifier.

        Returns
        -------
        - self: This instance with matching manualIpv6 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of manualIpv6 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the manualIpv6 resources from the server available through an iterator or index

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
