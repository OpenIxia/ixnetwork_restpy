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


class TrafficSettings(Base):
    """Describes the traffic settings for the IpTV Channel Zapping test.
    The TrafficSettings class encapsulates a list of trafficSettings resources that are managed by the user.
    A list of resources can be retrieved from the server using the TrafficSettings.find() method.
    The list can be managed by using the TrafficSettings.add() and TrafficSettings.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "trafficSettings"
    _SDM_ATT_MAP = {
        "Channels": "channels",
        "FrameSize": "frameSize",
        "Priority802Tag": "priority802Tag",
        "PriorityTosValue": "priorityTosValue",
        "PriorityTrafficClassValue": "priorityTrafficClassValue",
        "QuerierEnabled": "querierEnabled",
        "QuerierVersion": "querierVersion",
        "Rate": "rate",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TrafficSettings, self).__init__(parent, list_op)

    @property
    def RangeInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rangeinfo_df7f3d5900cc66da335343515e039a0a.RangeInfo): An instance of the RangeInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rangeinfo_df7f3d5900cc66da335343515e039a0a import (
            RangeInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RangeInfo", None) is not None:
                return self._properties.get("RangeInfo")
        return RangeInfo(self)._select()

    @property
    def Channels(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This attribute contains the globally configurable parameters for IPTV Channel Zapping.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Channels"])

    @Channels.setter
    def Channels(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Channels"], value)

    @property
    def FrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This attribute determines the frame size to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameSize"])

    @FrameSize.setter
    def FrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameSize"], value)

    @property
    def Priority802Tag(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This attribute defines the 802.1Q priority for the specified VLAN. The minimum value is zero and the maximum value is 7.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Priority802Tag"])

    @Priority802Tag.setter
    def Priority802Tag(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Priority802Tag"], value)

    @property
    def PriorityTosValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This attribute defines the priority specified for the ToS IP address
        """
        return self._get_attribute(self._SDM_ATT_MAP["PriorityTosValue"])

    @PriorityTosValue.setter
    def PriorityTosValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PriorityTosValue"], value)

    @property
    def PriorityTrafficClassValue(self):
        """
        Returns
        -------
        - dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str]): The priority traffic class value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PriorityTrafficClassValue"])

    @PriorityTrafficClassValue.setter
    def PriorityTrafficClassValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP["PriorityTrafficClassValue"], value)

    @property
    def QuerierEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, Enable Querier check box is selected for a specified server range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QuerierEnabled"])

    @QuerierEnabled.setter
    def QuerierEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QuerierEnabled"], value)

    @property
    def QuerierVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If true, Enable Querier check box is selected for choosing the querier version.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QuerierVersion"])

    @QuerierVersion.setter
    def QuerierVersion(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["QuerierVersion"], value)

    @property
    def Rate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This attribute describes the rate of traffic flow for the channel zapping test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Rate"])

    @Rate.setter
    def Rate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Rate"], value)

    def update(
        self,
        Channels=None,
        FrameSize=None,
        Priority802Tag=None,
        PriorityTosValue=None,
        PriorityTrafficClassValue=None,
        QuerierEnabled=None,
        QuerierVersion=None,
        Rate=None,
    ):
        """Updates trafficSettings resource on the server.

        Args
        ----
        - Channels (str): This attribute contains the globally configurable parameters for IPTV Channel Zapping.
        - FrameSize (number): This attribute determines the frame size to be used.
        - Priority802Tag (number): This attribute defines the 802.1Q priority for the specified VLAN. The minimum value is zero and the maximum value is 7.
        - PriorityTosValue (str): This attribute defines the priority specified for the ToS IP address
        - PriorityTrafficClassValue (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): The priority traffic class value.
        - QuerierEnabled (bool): If true, Enable Querier check box is selected for a specified server range.
        - QuerierVersion (str): If true, Enable Querier check box is selected for choosing the querier version.
        - Rate (number): This attribute describes the rate of traffic flow for the channel zapping test.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Channels=None,
        FrameSize=None,
        Priority802Tag=None,
        PriorityTosValue=None,
        PriorityTrafficClassValue=None,
        QuerierEnabled=None,
        QuerierVersion=None,
        Rate=None,
    ):
        """Adds a new trafficSettings resource on the server and adds it to the container.

        Args
        ----
        - Channels (str): This attribute contains the globally configurable parameters for IPTV Channel Zapping.
        - FrameSize (number): This attribute determines the frame size to be used.
        - Priority802Tag (number): This attribute defines the 802.1Q priority for the specified VLAN. The minimum value is zero and the maximum value is 7.
        - PriorityTosValue (str): This attribute defines the priority specified for the ToS IP address
        - PriorityTrafficClassValue (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): The priority traffic class value.
        - QuerierEnabled (bool): If true, Enable Querier check box is selected for a specified server range.
        - QuerierVersion (str): If true, Enable Querier check box is selected for choosing the querier version.
        - Rate (number): This attribute describes the rate of traffic flow for the channel zapping test.

        Returns
        -------
        - self: This instance with all currently retrieved trafficSettings resources using find and the newly added trafficSettings resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained trafficSettings resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Channels=None,
        FrameSize=None,
        Priority802Tag=None,
        PriorityTosValue=None,
        PriorityTrafficClassValue=None,
        QuerierEnabled=None,
        QuerierVersion=None,
        Rate=None,
    ):
        """Finds and retrieves trafficSettings resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trafficSettings resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trafficSettings resources from the server.

        Args
        ----
        - Channels (str): This attribute contains the globally configurable parameters for IPTV Channel Zapping.
        - FrameSize (number): This attribute determines the frame size to be used.
        - Priority802Tag (number): This attribute defines the 802.1Q priority for the specified VLAN. The minimum value is zero and the maximum value is 7.
        - PriorityTosValue (str): This attribute defines the priority specified for the ToS IP address
        - PriorityTrafficClassValue (dict(arg1:str[mvDecr | mvIncr | mvList | mvSingle],arg2:list[str])): The priority traffic class value.
        - QuerierEnabled (bool): If true, Enable Querier check box is selected for a specified server range.
        - QuerierVersion (str): If true, Enable Querier check box is selected for choosing the querier version.
        - Rate (number): This attribute describes the rate of traffic flow for the channel zapping test.

        Returns
        -------
        - self: This instance with matching trafficSettings resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of trafficSettings data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trafficSettings resources from the server available through an iterator or index

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
