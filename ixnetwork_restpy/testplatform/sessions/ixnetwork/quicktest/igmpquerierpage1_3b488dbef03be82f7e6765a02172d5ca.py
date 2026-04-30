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


class IgmpQuerierPage1(Base):
    """
    The IgmpQuerierPage1 class encapsulates a list of igmpQuerierPage1 resources that are managed by the system.
    A list of resources can be retrieved from the server using the IgmpQuerierPage1.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "igmpQuerierPage1"
    _SDM_ATT_MAP = {
        "ConfigurationMode": "configurationMode",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IgmpQuerierPage1, self).__init__(parent, list_op)

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
    def MvDiscardLearntInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvdiscardlearntinfo_7d5b72f958d9ffed6532703aa7a75b7c.MvDiscardLearntInfo): An instance of the MvDiscardLearntInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvdiscardlearntinfo_7d5b72f958d9ffed6532703aa7a75b7c import (
            MvDiscardLearntInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvDiscardLearntInfo", None) is not None:
                return self._properties.get("MvDiscardLearntInfo")
        return MvDiscardLearntInfo(self)

    @property
    def MvGeneralQueryInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvgeneralqueryinterval_afbc0867224f49a29505651c79bb3692.MvGeneralQueryInterval): An instance of the MvGeneralQueryInterval class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvgeneralqueryinterval_afbc0867224f49a29505651c79bb3692 import (
            MvGeneralQueryInterval,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvGeneralQueryInterval", None) is not None:
                return self._properties.get("MvGeneralQueryInterval")
        return MvGeneralQueryInterval(self)

    @property
    def MvGeneralQueryResponseInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvgeneralqueryresponseinterval_3523bb8031a4ddab37624247b8e529ba.MvGeneralQueryResponseInterval): An instance of the MvGeneralQueryResponseInterval class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvgeneralqueryresponseinterval_3523bb8031a4ddab37624247b8e529ba import (
            MvGeneralQueryResponseInterval,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvGeneralQueryResponseInterval", None) is not None:
                return self._properties.get("MvGeneralQueryResponseInterval")
        return MvGeneralQueryResponseInterval(self)

    @property
    def MvProxyQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvproxyquerier_9643082ea8b1d9d56b7a6afc8aab79fd.MvProxyQuerier): An instance of the MvProxyQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvproxyquerier_9643082ea8b1d9d56b7a6afc8aab79fd import (
            MvProxyQuerier,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvProxyQuerier", None) is not None:
                return self._properties.get("MvProxyQuerier")
        return MvProxyQuerier(self)

    @property
    def MvRobustnessVariable(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvrobustnessvariable_739416276ef93e4fb3a81d1ec70455d5.MvRobustnessVariable): An instance of the MvRobustnessVariable class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvrobustnessvariable_739416276ef93e4fb3a81d1ec70455d5 import (
            MvRobustnessVariable,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvRobustnessVariable", None) is not None:
                return self._properties.get("MvRobustnessVariable")
        return MvRobustnessVariable(self)

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
    def MvSpecificQueryResponseInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvspecificqueryresponseinterval_85b2b061f0c08a4b378ec43c5f99d76d.MvSpecificQueryResponseInterval): An instance of the MvSpecificQueryResponseInterval class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvspecificqueryresponseinterval_85b2b061f0c08a4b378ec43c5f99d76d import (
            MvSpecificQueryResponseInterval,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("MvSpecificQueryResponseInterval", None)
                is not None
            ):
                return self._properties.get("MvSpecificQueryResponseInterval")
        return MvSpecificQueryResponseInterval(self)

    @property
    def MvSpecificQueryTransmissionCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvspecificquerytransmissioncount_5c1322e24e89583ea275210eaa96c753.MvSpecificQueryTransmissionCount): An instance of the MvSpecificQueryTransmissionCount class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvspecificquerytransmissioncount_5c1322e24e89583ea275210eaa96c753 import (
            MvSpecificQueryTransmissionCount,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("MvSpecificQueryTransmissionCount", None)
                is not None
            ):
                return self._properties.get("MvSpecificQueryTransmissionCount")
        return MvSpecificQueryTransmissionCount(self)

    @property
    def MvStartupQueryCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvstartupquerycount_3ad3762af9a59471d7edeaa077514cd7.MvStartupQueryCount): An instance of the MvStartupQueryCount class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvstartupquerycount_3ad3762af9a59471d7edeaa077514cd7 import (
            MvStartupQueryCount,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvStartupQueryCount", None) is not None:
                return self._properties.get("MvStartupQueryCount")
        return MvStartupQueryCount(self)

    @property
    def MvSupportElection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvsupportelection_28b45415c1cb516a0054aaec435ee738.MvSupportElection): An instance of the MvSupportElection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvsupportelection_28b45415c1cb516a0054aaec435ee738 import (
            MvSupportElection,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvSupportElection", None) is not None:
                return self._properties.get("MvSupportElection")
        return MvSupportElection(self)

    @property
    def MvSupportOlderVersionHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvsupportolderversionhost_d1f69860981f2c13385ab7d41a6b5273.MvSupportOlderVersionHost): An instance of the MvSupportOlderVersionHost class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvsupportolderversionhost_d1f69860981f2c13385ab7d41a6b5273 import (
            MvSupportOlderVersionHost,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvSupportOlderVersionHost", None) is not None:
                return self._properties.get("MvSupportOlderVersionHost")
        return MvSupportOlderVersionHost(self)

    @property
    def MvSupportOlderVersionQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvsupportolderversionquerier_c58c30cb43be827907a3774b289c876d.MvSupportOlderVersionQuerier): An instance of the MvSupportOlderVersionQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.mvsupportolderversionquerier_c58c30cb43be827907a3774b289c876d import (
            MvSupportOlderVersionQuerier,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MvSupportOlderVersionQuerier", None) is not None:
                return self._properties.get("MvSupportOlderVersionQuerier")
        return MvSupportOlderVersionQuerier(self)

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
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConfigurationMode"])

    @ConfigurationMode.setter
    def ConfigurationMode(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConfigurationMode"], value)

    def update(self, ConfigurationMode=None):
        # type: (int) -> IgmpQuerierPage1
        """Updates igmpQuerierPage1 resource on the server.

        Args
        ----
        - ConfigurationMode (number):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConfigurationMode=None):
        # type: (int) -> IgmpQuerierPage1
        """Adds a new igmpQuerierPage1 resource on the json, only valid with batch add utility

        Args
        ----
        - ConfigurationMode (number):

        Returns
        -------
        - self: This instance with all currently retrieved igmpQuerierPage1 resources using find and the newly added igmpQuerierPage1 resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, ConfigurationMode=None):
        # type: (int) -> IgmpQuerierPage1
        """Finds and retrieves igmpQuerierPage1 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve igmpQuerierPage1 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all igmpQuerierPage1 resources from the server.

        Args
        ----
        - ConfigurationMode (number):

        Returns
        -------
        - self: This instance with matching igmpQuerierPage1 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of igmpQuerierPage1 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the igmpQuerierPage1 resources from the server available through an iterator or index

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
