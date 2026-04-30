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


class ManualMac(Base):
    """The MAC address assigned manually.
    The ManualMac class encapsulates a list of manualMac resources that are managed by the user.
    A list of resources can be retrieved from the server using the ManualMac.find() method.
    The list can be managed by using the ManualMac.add() and ManualMac.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "manualMac"
    _SDM_ATT_MAP = {
        "AddrPerPort": "addrPerPort",
        "AssignConfig": "assignConfig",
        "DestIpAddress": "destIpAddress",
        "EnableIpHeader": "enableIpHeader",
        "EnableRandomMac": "enableRandomMac",
        "EtherType": "etherType",
        "InTest": "inTest",
        "LastRandomSeed": "lastRandomSeed",
        "PortId": "portId",
        "SrcMacMv": "srcMacMv",
        "UseLastSeed": "useLastSeed",
        "ValidChecksum": "validChecksum",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(ManualMac, self).__init__(parent, list_op)

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
        - bool: If true, the configuration is assigned to ports that are excluded from the test in.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssignConfig"])

    @AssignConfig.setter
    def AssignConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AssignConfig"], value)

    @property
    def DestIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP Address of the destination port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestIpAddress"])

    @DestIpAddress.setter
    def DestIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestIpAddress"], value)

    @property
    def EnableIpHeader(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, The IP header is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableIpHeader"])

    @EnableIpHeader.setter
    def EnableIpHeader(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableIpHeader"], value)

    @property
    def EnableRandomMac(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, a random MAC address is assigned.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableRandomMac"])

    @EnableRandomMac.setter
    def EnableRandomMac(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableRandomMac"], value)

    @property
    def EtherType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The EtherType that identifies the protocol header that follows the VLAN header.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EtherType"])

    @EtherType.setter
    def EtherType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EtherType"], value)

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
    def LastRandomSeed(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, the random MAC addresses previously used is not changed after editing.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastRandomSeed"])

    @LastRandomSeed.setter
    def LastRandomSeed(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LastRandomSeed"], value)

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

    @property
    def SrcMacMv(self):
        """
        Returns
        -------
        - dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str]): The Source MAC value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcMacMv"])

    @SrcMacMv.setter
    def SrcMacMv(self, value):
        self._set_attribute(self._SDM_ATT_MAP["SrcMacMv"], value)

    @property
    def UseLastSeed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the random MAC addresses previously used is not changed after editing.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseLastSeed"])

    @UseLastSeed.setter
    def UseLastSeed(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseLastSeed"], value)

    @property
    def ValidChecksum(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The ethernet frame including a valid IP checksum calculated from the IP value
        """
        return self._get_attribute(self._SDM_ATT_MAP["ValidChecksum"])

    @ValidChecksum.setter
    def ValidChecksum(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ValidChecksum"], value)

    def update(
        self,
        AddrPerPort=None,
        AssignConfig=None,
        DestIpAddress=None,
        EnableIpHeader=None,
        EnableRandomMac=None,
        EtherType=None,
        InTest=None,
        LastRandomSeed=None,
        PortId=None,
        SrcMacMv=None,
        UseLastSeed=None,
        ValidChecksum=None,
    ):
        """Updates manualMac resource on the server.

        Args
        ----
        - AddrPerPort (number): The gateway address per port.
        - AssignConfig (bool): If true, the configuration is assigned to ports that are excluded from the test in.
        - DestIpAddress (str): The IP Address of the destination port.
        - EnableIpHeader (bool): If true, The IP header is enabled.
        - EnableRandomMac (bool): If true, a random MAC address is assigned.
        - EtherType (str): The EtherType that identifies the protocol header that follows the VLAN header.
        - InTest (bool): If true, the traffic item is included in the test.
        - LastRandomSeed (number): If true, the random MAC addresses previously used is not changed after editing.
        - PortId (str(None | /api/v1/sessions/1/ixnetwork/vport)): The Port identifier.
        - SrcMacMv (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): The Source MAC value.
        - UseLastSeed (bool): If true, the random MAC addresses previously used is not changed after editing.
        - ValidChecksum (bool): The ethernet frame including a valid IP checksum calculated from the IP value

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AddrPerPort=None,
        AssignConfig=None,
        DestIpAddress=None,
        EnableIpHeader=None,
        EnableRandomMac=None,
        EtherType=None,
        InTest=None,
        LastRandomSeed=None,
        PortId=None,
        SrcMacMv=None,
        UseLastSeed=None,
        ValidChecksum=None,
    ):
        """Adds a new manualMac resource on the server and adds it to the container.

        Args
        ----
        - AddrPerPort (number): The gateway address per port.
        - AssignConfig (bool): If true, the configuration is assigned to ports that are excluded from the test in.
        - DestIpAddress (str): The IP Address of the destination port.
        - EnableIpHeader (bool): If true, The IP header is enabled.
        - EnableRandomMac (bool): If true, a random MAC address is assigned.
        - EtherType (str): The EtherType that identifies the protocol header that follows the VLAN header.
        - InTest (bool): If true, the traffic item is included in the test.
        - LastRandomSeed (number): If true, the random MAC addresses previously used is not changed after editing.
        - PortId (str(None | /api/v1/sessions/1/ixnetwork/vport)): The Port identifier.
        - SrcMacMv (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): The Source MAC value.
        - UseLastSeed (bool): If true, the random MAC addresses previously used is not changed after editing.
        - ValidChecksum (bool): The ethernet frame including a valid IP checksum calculated from the IP value

        Returns
        -------
        - self: This instance with all currently retrieved manualMac resources using find and the newly added manualMac resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained manualMac resources in this instance from the server.

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
        DestIpAddress=None,
        EnableIpHeader=None,
        EnableRandomMac=None,
        EtherType=None,
        InTest=None,
        LastRandomSeed=None,
        PortId=None,
        SrcMacMv=None,
        UseLastSeed=None,
        ValidChecksum=None,
    ):
        """Finds and retrieves manualMac resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve manualMac resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all manualMac resources from the server.

        Args
        ----
        - AddrPerPort (number): The gateway address per port.
        - AssignConfig (bool): If true, the configuration is assigned to ports that are excluded from the test in.
        - DestIpAddress (str): The IP Address of the destination port.
        - EnableIpHeader (bool): If true, The IP header is enabled.
        - EnableRandomMac (bool): If true, a random MAC address is assigned.
        - EtherType (str): The EtherType that identifies the protocol header that follows the VLAN header.
        - InTest (bool): If true, the traffic item is included in the test.
        - LastRandomSeed (number): If true, the random MAC addresses previously used is not changed after editing.
        - PortId (str(None | /api/v1/sessions/1/ixnetwork/vport)): The Port identifier.
        - SrcMacMv (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): The Source MAC value.
        - UseLastSeed (bool): If true, the random MAC addresses previously used is not changed after editing.
        - ValidChecksum (bool): The ethernet frame including a valid IP checksum calculated from the IP value

        Returns
        -------
        - self: This instance with matching manualMac resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of manualMac data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the manualMac resources from the server available through an iterator or index

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
