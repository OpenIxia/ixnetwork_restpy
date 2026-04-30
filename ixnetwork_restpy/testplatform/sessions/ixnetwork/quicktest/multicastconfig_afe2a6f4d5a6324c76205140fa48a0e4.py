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


class MulticastConfig(Base):
    """It signifies the configuration of multicast.
    The MulticastConfig class encapsulates a required multicastConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "multicastConfig"
    _SDM_ATT_MAP = {
        "AssignGroupType": "assignGroupType",
        "EnableLeaveGroup": "enableLeaveGroup",
        "IgmpV1Timeout": "igmpV1Timeout",
        "IgmpVersion": "igmpVersion",
        "Ipv4Address": "ipv4Address",
        "Ipv6Address": "ipv6Address",
        "JoinLeaveRate": "joinLeaveRate",
        "MldVersion": "mldVersion",
        "MulticastCountRandomFrameSize": "multicastCountRandomFrameSize",
        "MulticastEnableMinFrameSize": "multicastEnableMinFrameSize",
        "MulticastForceRegenerate": "multicastForceRegenerate",
        "MulticastFrameSizeMode": "multicastFrameSizeMode",
        "MulticastFramesizeFixedValue": "multicastFramesizeFixedValue",
        "MulticastFramesizeList": "multicastFramesizeList",
        "MulticastIpv6": "multicastIpv6",
        "MulticastMaxIncrementFrameSize": "multicastMaxIncrementFrameSize",
        "MulticastMaxRandomFrameSize": "multicastMaxRandomFrameSize",
        "MulticastMinIncrementFrameSize": "multicastMinIncrementFrameSize",
        "MulticastMinRandomFrameSize": "multicastMinRandomFrameSize",
        "MulticastStepIncrementFrameSize": "multicastStepIncrementFrameSize",
        "NumAddresses": "numAddresses",
        "RouterAlert": "routerAlert",
    }
    _SDM_ENUM_MAP = {
        "assignGroupType": ["accumulated", "distributed"],
        "multicastFrameSizeMode": ["custom", "fixed", "increment", "random"],
    }

    def __init__(self, parent, list_op=False):
        super(MulticastConfig, self).__init__(parent, list_op)

    @property
    def AssignGroupType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(accumulated | distributed): Assigns the group type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AssignGroupType"])

    @AssignGroupType.setter
    def AssignGroupType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AssignGroupType"], value)

    @property
    def EnableLeaveGroup(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates if leave group messages should be send at the end of the test. The hosts may prefer to send IGMP leave group messages to the DUT after the desired measurements are obtained.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLeaveGroup"])

    @EnableLeaveGroup.setter
    def EnableLeaveGroup(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLeaveGroup"], value)

    @property
    def IgmpV1Timeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The IGMPv1 timeout value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IgmpV1Timeout"])

    @IgmpV1Timeout.setter
    def IgmpV1Timeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IgmpV1Timeout"], value)

    @property
    def IgmpVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The IGMP version.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IgmpVersion"])

    @IgmpVersion.setter
    def IgmpVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IgmpVersion"], value)

    @property
    def Ipv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The allocated IPv4 address for this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4Address"])

    @Ipv4Address.setter
    def Ipv4Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4Address"], value)

    @property
    def Ipv6Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The allocated IPv6 address for this interface .
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6Address"])

    @Ipv6Address.setter
    def Ipv6Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6Address"], value)

    @property
    def JoinLeaveRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the join and leave rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinLeaveRate"])

    @JoinLeaveRate.setter
    def JoinLeaveRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinLeaveRate"], value)

    @property
    def MldVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The version of the MLD messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MldVersion"])

    @MldVersion.setter
    def MldVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MldVersion"], value)

    @property
    def MulticastCountRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the count random frame size value for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastCountRandomFrameSize"])

    @MulticastCountRandomFrameSize.setter
    def MulticastCountRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastCountRandomFrameSize"], value)

    @property
    def MulticastEnableMinFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables minimum frame size for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastEnableMinFrameSize"])

    @MulticastEnableMinFrameSize.setter
    def MulticastEnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastEnableMinFrameSize"], value)

    @property
    def MulticastForceRegenerate(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the multicast force regenerate value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastForceRegenerate"])

    @MulticastForceRegenerate.setter
    def MulticastForceRegenerate(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastForceRegenerate"], value)

    @property
    def MulticastFrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | fixed | increment | random): Indicates the frame size mode for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastFrameSizeMode"])

    @MulticastFrameSizeMode.setter
    def MulticastFrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastFrameSizeMode"], value)

    @property
    def MulticastFramesizeFixedValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the fixed value of multicast frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastFramesizeFixedValue"])

    @MulticastFramesizeFixedValue.setter
    def MulticastFramesizeFixedValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastFramesizeFixedValue"], value)

    @property
    def MulticastFramesizeList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): It lists the frame size for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastFramesizeList"])

    @MulticastFramesizeList.setter
    def MulticastFramesizeList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastFramesizeList"], value)

    @property
    def MulticastIpv6(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the IP version 6 for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastIpv6"])

    @MulticastIpv6.setter
    def MulticastIpv6(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastIpv6"], value)

    @property
    def MulticastMaxIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the maximum increment frame size value for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastMaxIncrementFrameSize"])

    @MulticastMaxIncrementFrameSize.setter
    def MulticastMaxIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastMaxIncrementFrameSize"], value)

    @property
    def MulticastMaxRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the maximum random frame size value for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastMaxRandomFrameSize"])

    @MulticastMaxRandomFrameSize.setter
    def MulticastMaxRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastMaxRandomFrameSize"], value)

    @property
    def MulticastMinIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the minimum increment frame size for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastMinIncrementFrameSize"])

    @MulticastMinIncrementFrameSize.setter
    def MulticastMinIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastMinIncrementFrameSize"], value)

    @property
    def MulticastMinRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the minimum random frame size value for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastMinRandomFrameSize"])

    @MulticastMinRandomFrameSize.setter
    def MulticastMinRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastMinRandomFrameSize"], value)

    @property
    def MulticastStepIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the step increment frame size value for multicast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastStepIncrementFrameSize"])

    @MulticastStepIncrementFrameSize.setter
    def MulticastStepIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastStepIncrementFrameSize"], value)

    @property
    def NumAddresses(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The integer value for the number of addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumAddresses"])

    @NumAddresses.setter
    def NumAddresses(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumAddresses"], value)

    @property
    def RouterAlert(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it alerts the router. The router alert selected from the Hop-by-hop Options.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterAlert"])

    @RouterAlert.setter
    def RouterAlert(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterAlert"], value)

    def update(
        self,
        AssignGroupType=None,
        EnableLeaveGroup=None,
        IgmpV1Timeout=None,
        IgmpVersion=None,
        Ipv4Address=None,
        Ipv6Address=None,
        JoinLeaveRate=None,
        MldVersion=None,
        MulticastCountRandomFrameSize=None,
        MulticastEnableMinFrameSize=None,
        MulticastForceRegenerate=None,
        MulticastFrameSizeMode=None,
        MulticastFramesizeFixedValue=None,
        MulticastFramesizeList=None,
        MulticastIpv6=None,
        MulticastMaxIncrementFrameSize=None,
        MulticastMaxRandomFrameSize=None,
        MulticastMinIncrementFrameSize=None,
        MulticastMinRandomFrameSize=None,
        MulticastStepIncrementFrameSize=None,
        NumAddresses=None,
        RouterAlert=None,
    ):
        # type: (str, bool, int, int, str, str, int, int, int, bool, str, str, int, List[str], str, int, int, int, int, int, int, bool) -> MulticastConfig
        """Updates multicastConfig resource on the server.

        Args
        ----
        - AssignGroupType (str(accumulated | distributed)): Assigns the group type.
        - EnableLeaveGroup (bool): Indicates if leave group messages should be send at the end of the test. The hosts may prefer to send IGMP leave group messages to the DUT after the desired measurements are obtained.
        - IgmpV1Timeout (number): The IGMPv1 timeout value.
        - IgmpVersion (number): The IGMP version.
        - Ipv4Address (str): The allocated IPv4 address for this interface.
        - Ipv6Address (str): The allocated IPv6 address for this interface .
        - JoinLeaveRate (number): It signifies the join and leave rate.
        - MldVersion (number): The version of the MLD messages.
        - MulticastCountRandomFrameSize (number): It signifies the count random frame size value for multicast.
        - MulticastEnableMinFrameSize (bool): If true, enables minimum frame size for multicast.
        - MulticastForceRegenerate (str): It signifies the multicast force regenerate value.
        - MulticastFrameSizeMode (str(custom | fixed | increment | random)): Indicates the frame size mode for multicast.
        - MulticastFramesizeFixedValue (number): Indicates the fixed value of multicast frame size.
        - MulticastFramesizeList (list(str)): It lists the frame size for multicast.
        - MulticastIpv6 (str): It signifies the IP version 6 for multicast.
        - MulticastMaxIncrementFrameSize (number): It signifies the maximum increment frame size value for multicast.
        - MulticastMaxRandomFrameSize (number): It signifies the maximum random frame size value for multicast.
        - MulticastMinIncrementFrameSize (number): It signifies the minimum increment frame size for multicast.
        - MulticastMinRandomFrameSize (number): It signifies the minimum random frame size value for multicast.
        - MulticastStepIncrementFrameSize (number): It signifies the step increment frame size value for multicast.
        - NumAddresses (number): The integer value for the number of addresses.
        - RouterAlert (bool): If enabled, it alerts the router. The router alert selected from the Hop-by-hop Options.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AssignGroupType=None,
        EnableLeaveGroup=None,
        IgmpV1Timeout=None,
        IgmpVersion=None,
        Ipv4Address=None,
        Ipv6Address=None,
        JoinLeaveRate=None,
        MldVersion=None,
        MulticastCountRandomFrameSize=None,
        MulticastEnableMinFrameSize=None,
        MulticastForceRegenerate=None,
        MulticastFrameSizeMode=None,
        MulticastFramesizeFixedValue=None,
        MulticastFramesizeList=None,
        MulticastIpv6=None,
        MulticastMaxIncrementFrameSize=None,
        MulticastMaxRandomFrameSize=None,
        MulticastMinIncrementFrameSize=None,
        MulticastMinRandomFrameSize=None,
        MulticastStepIncrementFrameSize=None,
        NumAddresses=None,
        RouterAlert=None,
    ):
        # type: (str, bool, int, int, str, str, int, int, int, bool, str, str, int, List[str], str, int, int, int, int, int, int, bool) -> MulticastConfig
        """Finds and retrieves multicastConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve multicastConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all multicastConfig resources from the server.

        Args
        ----
        - AssignGroupType (str(accumulated | distributed)): Assigns the group type.
        - EnableLeaveGroup (bool): Indicates if leave group messages should be send at the end of the test. The hosts may prefer to send IGMP leave group messages to the DUT after the desired measurements are obtained.
        - IgmpV1Timeout (number): The IGMPv1 timeout value.
        - IgmpVersion (number): The IGMP version.
        - Ipv4Address (str): The allocated IPv4 address for this interface.
        - Ipv6Address (str): The allocated IPv6 address for this interface .
        - JoinLeaveRate (number): It signifies the join and leave rate.
        - MldVersion (number): The version of the MLD messages.
        - MulticastCountRandomFrameSize (number): It signifies the count random frame size value for multicast.
        - MulticastEnableMinFrameSize (bool): If true, enables minimum frame size for multicast.
        - MulticastForceRegenerate (str): It signifies the multicast force regenerate value.
        - MulticastFrameSizeMode (str(custom | fixed | increment | random)): Indicates the frame size mode for multicast.
        - MulticastFramesizeFixedValue (number): Indicates the fixed value of multicast frame size.
        - MulticastFramesizeList (list(str)): It lists the frame size for multicast.
        - MulticastIpv6 (str): It signifies the IP version 6 for multicast.
        - MulticastMaxIncrementFrameSize (number): It signifies the maximum increment frame size value for multicast.
        - MulticastMaxRandomFrameSize (number): It signifies the maximum random frame size value for multicast.
        - MulticastMinIncrementFrameSize (number): It signifies the minimum increment frame size for multicast.
        - MulticastMinRandomFrameSize (number): It signifies the minimum random frame size value for multicast.
        - MulticastStepIncrementFrameSize (number): It signifies the step increment frame size value for multicast.
        - NumAddresses (number): The integer value for the number of addresses.
        - RouterAlert (bool): If enabled, it alerts the router. The router alert selected from the Hop-by-hop Options.

        Returns
        -------
        - self: This instance with matching multicastConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of multicastConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the multicastConfig resources from the server available through an iterator or index

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
