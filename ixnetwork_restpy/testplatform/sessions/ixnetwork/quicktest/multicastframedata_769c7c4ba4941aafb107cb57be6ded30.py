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


class MulticastFrameData(Base):
    """This helps to configure the frame data protocol.
    The MulticastFrameData class encapsulates a list of multicastFrameData resources that are managed by the system.
    A list of resources can be retrieved from the server using the MulticastFrameData.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "multicastFrameData"
    _SDM_ATT_MAP = {
        "Automatic": "automatic",
        "CreatedSdmObjects": "createdSdmObjects",
        "ShowManualPriorityMv": "showManualPriorityMv",
        "ShowManualQoS": "showManualQoS",
        "TrafficType": "trafficType",
    }
    _SDM_ENUM_MAP = {
        "trafficType": ["ipmix", "ipv4", "ipv6", "mac"],
    }

    def __init__(self, parent, list_op=False):
        super(MulticastFrameData, self).__init__(parent, list_op)

    @property
    def AutomaticIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.automaticip_159bc06d8b901f26547ada50bf8c77a7.AutomaticIp): An instance of the AutomaticIp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.automaticip_159bc06d8b901f26547ada50bf8c77a7 import (
            AutomaticIp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AutomaticIp", None) is not None:
                return self._properties.get("AutomaticIp")
        return AutomaticIp(self)._select()

    @property
    def AutomaticIpMix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.automaticipmix_0533d2c1be9c329c52397080ecf1a26e.AutomaticIpMix): An instance of the AutomaticIpMix class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.automaticipmix_0533d2c1be9c329c52397080ecf1a26e import (
            AutomaticIpMix,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AutomaticIpMix", None) is not None:
                return self._properties.get("AutomaticIpMix")
        return AutomaticIpMix(self)._select()

    @property
    def AutomaticIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.automaticipv6_3b48cf6b2555671a22117f9ec3dfc4bf.AutomaticIpv6): An instance of the AutomaticIpv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.automaticipv6_3b48cf6b2555671a22117f9ec3dfc4bf import (
            AutomaticIpv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AutomaticIpv6", None) is not None:
                return self._properties.get("AutomaticIpv6")
        return AutomaticIpv6(self)._select()

    @property
    def AutomaticMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.automaticmac_960c10e45a5852f17d2f05d13753b90f.AutomaticMac): An instance of the AutomaticMac class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.automaticmac_960c10e45a5852f17d2f05d13753b90f import (
            AutomaticMac,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AutomaticMac", None) is not None:
                return self._properties.get("AutomaticMac")
        return AutomaticMac(self)._select()

    @property
    def ManualIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.manualip_3a4cbee3b37ba41c0e763fefa70769d5.ManualIp): An instance of the ManualIp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.manualip_3a4cbee3b37ba41c0e763fefa70769d5 import (
            ManualIp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ManualIp", None) is not None:
                return self._properties.get("ManualIp")
        return ManualIp(self)

    @property
    def ManualIpMix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.manualipmix_d7e7c2304d0256f973a65d58c849d73b.ManualIpMix): An instance of the ManualIpMix class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.manualipmix_d7e7c2304d0256f973a65d58c849d73b import (
            ManualIpMix,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ManualIpMix", None) is not None:
                return self._properties.get("ManualIpMix")
        return ManualIpMix(self)

    @property
    def ManualIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.manualipv6_7085e0ac650e1d91ef95d2e21f1c5616.ManualIpv6): An instance of the ManualIpv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.manualipv6_7085e0ac650e1d91ef95d2e21f1c5616 import (
            ManualIpv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ManualIpv6", None) is not None:
                return self._properties.get("ManualIpv6")
        return ManualIpv6(self)

    @property
    def ManualMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.manualmac_62cc69789c4646637018001269e17a0f.ManualMac): An instance of the ManualMac class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.manualmac_62cc69789c4646637018001269e17a0f import (
            ManualMac,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ManualMac", None) is not None:
                return self._properties.get("ManualMac")
        return ManualMac(self)

    @property
    def Automatic(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The test based on automatic parameters.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Automatic"])

    @Automatic.setter
    def Automatic(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Automatic"], value)

    @property
    def CreatedSdmObjects(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan]): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CreatedSdmObjects"])

    @CreatedSdmObjects.setter
    def CreatedSdmObjects(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["CreatedSdmObjects"], value)

    @property
    def ShowManualPriorityMv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, Enables Manual Priority.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowManualPriorityMv"])

    @ShowManualPriorityMv.setter
    def ShowManualPriorityMv(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowManualPriorityMv"], value)

    @property
    def ShowManualQoS(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, Enables Manual QoS.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowManualQoS"])

    @ShowManualQoS.setter
    def ShowManualQoS(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowManualQoS"], value)

    @property
    def TrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipmix | ipv4 | ipv6 | mac): Traffic type for the frame data
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficType"])

    @TrafficType.setter
    def TrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficType"], value)

    def update(
        self,
        Automatic=None,
        CreatedSdmObjects=None,
        ShowManualPriorityMv=None,
        ShowManualQoS=None,
        TrafficType=None,
    ):
        # type: (bool, List[str], bool, bool, str) -> MulticastFrameData
        """Updates multicastFrameData resource on the server.

        Args
        ----
        - Automatic (bool): The test based on automatic parameters.
        - CreatedSdmObjects (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): NOT DEFINED
        - ShowManualPriorityMv (bool): If true, Enables Manual Priority.
        - ShowManualQoS (bool): If true, Enables Manual QoS.
        - TrafficType (str(ipmix | ipv4 | ipv6 | mac)): Traffic type for the frame data

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Automatic=None,
        CreatedSdmObjects=None,
        ShowManualPriorityMv=None,
        ShowManualQoS=None,
        TrafficType=None,
    ):
        # type: (bool, List[str], bool, bool, str) -> MulticastFrameData
        """Adds a new multicastFrameData resource on the json, only valid with batch add utility

        Args
        ----
        - Automatic (bool): The test based on automatic parameters.
        - CreatedSdmObjects (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): NOT DEFINED
        - ShowManualPriorityMv (bool): If true, Enables Manual Priority.
        - ShowManualQoS (bool): If true, Enables Manual QoS.
        - TrafficType (str(ipmix | ipv4 | ipv6 | mac)): Traffic type for the frame data

        Returns
        -------
        - self: This instance with all currently retrieved multicastFrameData resources using find and the newly added multicastFrameData resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Automatic=None,
        CreatedSdmObjects=None,
        ShowManualPriorityMv=None,
        ShowManualQoS=None,
        TrafficType=None,
    ):
        # type: (bool, List[str], bool, bool, str) -> MulticastFrameData
        """Finds and retrieves multicastFrameData resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve multicastFrameData resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all multicastFrameData resources from the server.

        Args
        ----
        - Automatic (bool): The test based on automatic parameters.
        - CreatedSdmObjects (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): NOT DEFINED
        - ShowManualPriorityMv (bool): If true, Enables Manual Priority.
        - ShowManualQoS (bool): If true, Enables Manual QoS.
        - TrafficType (str(ipmix | ipv4 | ipv6 | mac)): Traffic type for the frame data

        Returns
        -------
        - self: This instance with matching multicastFrameData resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of multicastFrameData data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the multicastFrameData resources from the server available through an iterator or index

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
