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


class IgmpHostPage1(Base):
    """NOT DEFINED
    The IgmpHostPage1 class encapsulates a list of igmpHostPage1 resources that are managed by the system.
    A list of resources can be retrieved from the server using the IgmpHostPage1.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "igmpHostPage1"
    _SDM_ATT_MAP = {
        "ConfigurationMode": "configurationMode",
        "JlMultiplier": "jlMultiplier",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IgmpHostPage1, self).__init__(parent, list_op)

    @property
    def CommitInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.commitinfo_0a244066cd566b5e740f2737e9479f44.CommitInfo): An instance of the CommitInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.commitinfo_0a244066cd566b5e740f2737e9479f44 import (
            CommitInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CommitInfo", None) is not None:
                return self._properties.get("CommitInfo")
        return CommitInfo(self)

    @property
    def EnableProxyReporting(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.enableproxyreporting_996266123042d476f81bfaa0ba4a6351.EnableProxyReporting): An instance of the EnableProxyReporting class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.enableproxyreporting_996266123042d476f81bfaa0ba4a6351 import (
            EnableProxyReporting,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EnableProxyReporting", None) is not None:
                return self._properties.get("EnableProxyReporting")
        return EnableProxyReporting(self)

    @property
    def IgmpMcastIPv4GroupList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.igmpmcastipv4grouplist_886a8be0602d7724c3a1b5a106ca8ad2.IgmpMcastIPv4GroupList): An instance of the IgmpMcastIPv4GroupList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.igmpmcastipv4grouplist_886a8be0602d7724c3a1b5a106ca8ad2 import (
            IgmpMcastIPv4GroupList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IgmpMcastIPv4GroupList", None) is not None:
                return self._properties.get("IgmpMcastIPv4GroupList")
        return IgmpMcastIPv4GroupList(self)

    @property
    def MvActive(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvactive_977c041881ea5558579933b13d41c861.MvActive): An instance of the MvActive class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvactive_977c041881ea5558579933b13d41c861 import (
            MvActive,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvActive", None) is not None:
                return self._properties.get("MvActive")
        return MvActive(self)

    @property
    def MvGQResponseMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvgqresponsemode_69771919d99ba53d6025e71b523008b4.MvGQResponseMode): An instance of the MvGQResponseMode class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvgqresponsemode_69771919d99ba53d6025e71b523008b4 import (
            MvGQResponseMode,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvGQResponseMode", None) is not None:
                return self._properties.get("MvGQResponseMode")
        return MvGQResponseMode(self)

    @property
    def MvGSResponseMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvgsresponsemode_3179852c72c594af5de61f34b2a80b00.MvGSResponseMode): An instance of the MvGSResponseMode class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvgsresponsemode_3179852c72c594af5de61f34b2a80b00 import (
            MvGSResponseMode,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvGSResponseMode", None) is not None:
                return self._properties.get("MvGSResponseMode")
        return MvGSResponseMode(self)

    @property
    def MvImResponse(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvimresponse_561ca02e3cb0ac9aa33e438100313857.MvImResponse): An instance of the MvImResponse class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvimresponse_561ca02e3cb0ac9aa33e438100313857 import (
            MvImResponse,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvImResponse", None) is not None:
                return self._properties.get("MvImResponse")
        return MvImResponse(self)

    @property
    def MvReportFreq(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvreportfreq_dbfc0067fd95b6dbb8db5825020b2335.MvReportFreq): An instance of the MvReportFreq class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvreportfreq_dbfc0067fd95b6dbb8db5825020b2335 import (
            MvReportFreq,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvReportFreq", None) is not None:
                return self._properties.get("MvReportFreq")
        return MvReportFreq(self)

    @property
    def MvRouterAlert(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvrouteralert_a52e9369112117f00836335a0c12fbb3.MvRouterAlert): An instance of the MvRouterAlert class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvrouteralert_a52e9369112117f00836335a0c12fbb3 import (
            MvRouterAlert,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvRouterAlert", None) is not None:
                return self._properties.get("MvRouterAlert")
        return MvRouterAlert(self)

    @property
    def MvUSResponseMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvusresponsemode_dd9f475ee5ae233ac9f34fe324d9d68c.MvUSResponseMode): An instance of the MvUSResponseMode class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvusresponsemode_dd9f475ee5ae233ac9f34fe324d9d68c import (
            MvUSResponseMode,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvUSResponseMode", None) is not None:
                return self._properties.get("MvUSResponseMode")
        return MvUSResponseMode(self)

    @property
    def MvVersionType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvversiontype_158c96f97e9d2dd3000ef6ddb2c9c2ec.MvVersionType): An instance of the MvVersionType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvversiontype_158c96f97e9d2dd3000ef6ddb2c9c2ec import (
            MvVersionType,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvVersionType", None) is not None:
                return self._properties.get("MvVersionType")
        return MvVersionType(self)

    @property
    def ConfigurationMode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConfigurationMode"])

    @ConfigurationMode.setter
    def ConfigurationMode(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConfigurationMode"], value)

    @property
    def JlMultiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["JlMultiplier"])

    @JlMultiplier.setter
    def JlMultiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JlMultiplier"], value)

    def update(self, ConfigurationMode=None, JlMultiplier=None):
        # type: (int, int) -> IgmpHostPage1
        """Updates igmpHostPage1 resource on the server.

        Args
        ----
        - ConfigurationMode (number): NOT DEFINED
        - JlMultiplier (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConfigurationMode=None, JlMultiplier=None):
        # type: (int, int) -> IgmpHostPage1
        """Adds a new igmpHostPage1 resource on the json, only valid with batch add utility

        Args
        ----
        - ConfigurationMode (number): NOT DEFINED
        - JlMultiplier (number): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved igmpHostPage1 resources using find and the newly added igmpHostPage1 resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, ConfigurationMode=None, JlMultiplier=None):
        # type: (int, int) -> IgmpHostPage1
        """Finds and retrieves igmpHostPage1 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve igmpHostPage1 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all igmpHostPage1 resources from the server.

        Args
        ----
        - ConfigurationMode (number): NOT DEFINED
        - JlMultiplier (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching igmpHostPage1 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of igmpHostPage1 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the igmpHostPage1 resources from the server available through an iterator or index

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
