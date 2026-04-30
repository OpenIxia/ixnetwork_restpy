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


class FcoeFwdGen(Base):
    """This object configures the options for FCoE Forwarder.
    The FcoeFwdGen class encapsulates a list of fcoeFwdGen resources that are managed by the system.
    A list of resources can be retrieved from the server using the FcoeFwdGen.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "fcoeFwdGen"
    _SDM_ATT_MAP = {
        "FabricNameIncrement": "fabricNameIncrement",
        "FabricNameStart": "fabricNameStart",
        "FcMapIncrement": "fcMapIncrement",
        "FcMapStart": "fcMapStart",
        "FipClearVLinkOnExpire": "fipClearVLinkOnExpire",
        "FipPriority": "fipPriority",
        "HasOnlyFcPorts": "hasOnlyFcPorts",
        "IsFcClientToFcf": "isFcClientToFcf",
        "IsFcoeClientToFport": "isFcoeClientToFport",
        "PortIdIncrement": "portIdIncrement",
        "PortIdStart": "portIdStart",
        "SwitchNameIncrement": "switchNameIncrement",
        "SwitchNameStart": "switchNameStart",
        "VlanIds": "vlanIds",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(FcoeFwdGen, self).__init__(parent, list_op)

    @property
    def FabricNameIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value by which fabric names are incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FabricNameIncrement"])

    @FabricNameIncrement.setter
    def FabricNameIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FabricNameIncrement"], value)

    @property
    def FabricNameStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the first FCoE fabric.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FabricNameStart"])

    @FabricNameStart.setter
    def FabricNameStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FabricNameStart"], value)

    @property
    def FcMapIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first FC port map increment.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcMapIncrement"])

    @FcMapIncrement.setter
    def FcMapIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcMapIncrement"], value)

    @property
    def FcMapStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first FC port map.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcMapStart"])

    @FcMapStart.setter
    def FcMapStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcMapStart"], value)

    @property
    def FipClearVLinkOnExpire(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, transmits virtual links to the expired VN ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipClearVLinkOnExpire"])

    @FipClearVLinkOnExpire.setter
    def FipClearVLinkOnExpire(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipClearVLinkOnExpire"], value)

    @property
    def FipPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The user priority for the FCoE Initialization Protocol.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FipPriority"])

    @FipPriority.setter
    def FipPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FipPriority"], value)

    @property
    def HasOnlyFcPorts(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["HasOnlyFcPorts"])

    @HasOnlyFcPorts.setter
    def HasOnlyFcPorts(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HasOnlyFcPorts"], value)

    @property
    def IsFcClientToFcf(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsFcClientToFcf"])

    @IsFcClientToFcf.setter
    def IsFcClientToFcf(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsFcClientToFcf"], value)

    @property
    def IsFcoeClientToFport(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsFcoeClientToFport"])

    @IsFcoeClientToFport.setter
    def IsFcoeClientToFport(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsFcoeClientToFport"], value)

    @property
    def PortIdIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value by which the FC port IDs are incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortIdIncrement"])

    @PortIdIncrement.setter
    def PortIdIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortIdIncrement"], value)

    @property
    def PortIdStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first assigned Id for the FC port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortIdStart"])

    @PortIdStart.setter
    def PortIdStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortIdStart"], value)

    @property
    def SwitchNameIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value by which switch names are incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchNameIncrement"])

    @SwitchNameIncrement.setter
    def SwitchNameIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchNameIncrement"], value)

    @property
    def SwitchNameStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the first switch device.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchNameStart"])

    @SwitchNameStart.setter
    def SwitchNameStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchNameStart"], value)

    @property
    def VlanIds(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The VLAN ID associated with the fabric.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanIds"])

    @VlanIds.setter
    def VlanIds(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanIds"], value)

    def update(
        self,
        FabricNameIncrement=None,
        FabricNameStart=None,
        FcMapIncrement=None,
        FcMapStart=None,
        FipClearVLinkOnExpire=None,
        FipPriority=None,
        HasOnlyFcPorts=None,
        IsFcClientToFcf=None,
        IsFcoeClientToFport=None,
        PortIdIncrement=None,
        PortIdStart=None,
        SwitchNameIncrement=None,
        SwitchNameStart=None,
        VlanIds=None,
    ):
        # type: (str, str, str, str, bool, int, bool, bool, bool, str, str, str, str, str) -> FcoeFwdGen
        """Updates fcoeFwdGen resource on the server.

        Args
        ----
        - FabricNameIncrement (str): The value by which fabric names are incremented.
        - FabricNameStart (str): The name of the first FCoE fabric.
        - FcMapIncrement (str): The first FC port map increment.
        - FcMapStart (str): The first FC port map.
        - FipClearVLinkOnExpire (bool): If selected, transmits virtual links to the expired VN ports.
        - FipPriority (number): The user priority for the FCoE Initialization Protocol.
        - HasOnlyFcPorts (bool): NOT DEFINED
        - IsFcClientToFcf (bool): NOT DEFINED
        - IsFcoeClientToFport (bool): NOT DEFINED
        - PortIdIncrement (str): The value by which the FC port IDs are incremented.
        - PortIdStart (str): The first assigned Id for the FC port.
        - SwitchNameIncrement (str): The value by which switch names are incremented.
        - SwitchNameStart (str): The name of the first switch device.
        - VlanIds (str): The VLAN ID associated with the fabric.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        FabricNameIncrement=None,
        FabricNameStart=None,
        FcMapIncrement=None,
        FcMapStart=None,
        FipClearVLinkOnExpire=None,
        FipPriority=None,
        HasOnlyFcPorts=None,
        IsFcClientToFcf=None,
        IsFcoeClientToFport=None,
        PortIdIncrement=None,
        PortIdStart=None,
        SwitchNameIncrement=None,
        SwitchNameStart=None,
        VlanIds=None,
    ):
        # type: (str, str, str, str, bool, int, bool, bool, bool, str, str, str, str, str) -> FcoeFwdGen
        """Adds a new fcoeFwdGen resource on the json, only valid with batch add utility

        Args
        ----
        - FabricNameIncrement (str): The value by which fabric names are incremented.
        - FabricNameStart (str): The name of the first FCoE fabric.
        - FcMapIncrement (str): The first FC port map increment.
        - FcMapStart (str): The first FC port map.
        - FipClearVLinkOnExpire (bool): If selected, transmits virtual links to the expired VN ports.
        - FipPriority (number): The user priority for the FCoE Initialization Protocol.
        - HasOnlyFcPorts (bool): NOT DEFINED
        - IsFcClientToFcf (bool): NOT DEFINED
        - IsFcoeClientToFport (bool): NOT DEFINED
        - PortIdIncrement (str): The value by which the FC port IDs are incremented.
        - PortIdStart (str): The first assigned Id for the FC port.
        - SwitchNameIncrement (str): The value by which switch names are incremented.
        - SwitchNameStart (str): The name of the first switch device.
        - VlanIds (str): The VLAN ID associated with the fabric.

        Returns
        -------
        - self: This instance with all currently retrieved fcoeFwdGen resources using find and the newly added fcoeFwdGen resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        FabricNameIncrement=None,
        FabricNameStart=None,
        FcMapIncrement=None,
        FcMapStart=None,
        FipClearVLinkOnExpire=None,
        FipPriority=None,
        HasOnlyFcPorts=None,
        IsFcClientToFcf=None,
        IsFcoeClientToFport=None,
        PortIdIncrement=None,
        PortIdStart=None,
        SwitchNameIncrement=None,
        SwitchNameStart=None,
        VlanIds=None,
    ):
        # type: (str, str, str, str, bool, int, bool, bool, bool, str, str, str, str, str) -> FcoeFwdGen
        """Finds and retrieves fcoeFwdGen resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcoeFwdGen resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcoeFwdGen resources from the server.

        Args
        ----
        - FabricNameIncrement (str): The value by which fabric names are incremented.
        - FabricNameStart (str): The name of the first FCoE fabric.
        - FcMapIncrement (str): The first FC port map increment.
        - FcMapStart (str): The first FC port map.
        - FipClearVLinkOnExpire (bool): If selected, transmits virtual links to the expired VN ports.
        - FipPriority (number): The user priority for the FCoE Initialization Protocol.
        - HasOnlyFcPorts (bool): NOT DEFINED
        - IsFcClientToFcf (bool): NOT DEFINED
        - IsFcoeClientToFport (bool): NOT DEFINED
        - PortIdIncrement (str): The value by which the FC port IDs are incremented.
        - PortIdStart (str): The first assigned Id for the FC port.
        - SwitchNameIncrement (str): The value by which switch names are incremented.
        - SwitchNameStart (str): The name of the first switch device.
        - VlanIds (str): The VLAN ID associated with the fabric.

        Returns
        -------
        - self: This instance with matching fcoeFwdGen resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcoeFwdGen data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcoeFwdGen resources from the server available through an iterator or index

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
