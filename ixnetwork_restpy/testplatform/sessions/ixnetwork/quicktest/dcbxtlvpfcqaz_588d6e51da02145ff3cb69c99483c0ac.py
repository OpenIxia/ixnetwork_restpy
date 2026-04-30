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


class DcbxTlvPfcQaz(Base):
    """This object helps to configure the options for the DCBX TLV PFC QAZ parameters.
    The DcbxTlvPfcQaz class encapsulates a list of dcbxTlvPfcQaz resources that are managed by the system.
    A list of resources can be retrieved from the server using the DcbxTlvPfcQaz.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "dcbxTlvPfcQaz"
    _SDM_ATT_MAP = {
        "Mbc": "mbc",
        "PfcCapability": "pfcCapability",
        "PfcEnableVector": "pfcEnableVector",
        "Willing": "willing",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DcbxTlvPfcQaz, self).__init__(parent, list_op)

    @property
    def Mbc(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the MACsec Bypass Capability Bit. Enabling MBC indicates that the station can bypass MACsec processing when MACsec is disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mbc"])

    @Mbc.setter
    def Mbc(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mbc"], value)

    @property
    def PfcCapability(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The priority based flow control capability.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcCapability"])

    @PfcCapability.setter
    def PfcCapability(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcCapability"], value)

    @property
    def PfcEnableVector(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If true, the priority based flow control vector is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcEnableVector"])

    @PfcEnableVector.setter
    def PfcEnableVector(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcEnableVector"], value)

    @property
    def Willing(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether or not this feature accepts its configuration from the peer. When the Willing flag is TRUE, the system uses the DesiredCfg supplied by apeer as the OperCfg. A system that sets Willing to TRUE must be capable ofaccepting any valid DesiredCfg for the feature from the peer. In general, for onepeer to use the configuration of another peer, one peer must be willing and theother not willing. If both local and remote systems have the same value for theWilling flag, then the local DesiredCfg is used and the operational outcome of theexchange is determined by the Compatible method of the feature.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Willing"])

    @Willing.setter
    def Willing(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Willing"], value)

    def update(self, Mbc=None, PfcCapability=None, PfcEnableVector=None, Willing=None):
        # type: (bool, int, str, bool) -> DcbxTlvPfcQaz
        """Updates dcbxTlvPfcQaz resource on the server.

        Args
        ----
        - Mbc (bool): This signifies the MACsec Bypass Capability Bit. Enabling MBC indicates that the station can bypass MACsec processing when MACsec is disabled.
        - PfcCapability (number): The priority based flow control capability.
        - PfcEnableVector (str): If true, the priority based flow control vector is enabled.
        - Willing (bool): Indicates whether or not this feature accepts its configuration from the peer. When the Willing flag is TRUE, the system uses the DesiredCfg supplied by apeer as the OperCfg. A system that sets Willing to TRUE must be capable ofaccepting any valid DesiredCfg for the feature from the peer. In general, for onepeer to use the configuration of another peer, one peer must be willing and theother not willing. If both local and remote systems have the same value for theWilling flag, then the local DesiredCfg is used and the operational outcome of theexchange is determined by the Compatible method of the feature.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Mbc=None, PfcCapability=None, PfcEnableVector=None, Willing=None):
        # type: (bool, int, str, bool) -> DcbxTlvPfcQaz
        """Adds a new dcbxTlvPfcQaz resource on the json, only valid with batch add utility

        Args
        ----
        - Mbc (bool): This signifies the MACsec Bypass Capability Bit. Enabling MBC indicates that the station can bypass MACsec processing when MACsec is disabled.
        - PfcCapability (number): The priority based flow control capability.
        - PfcEnableVector (str): If true, the priority based flow control vector is enabled.
        - Willing (bool): Indicates whether or not this feature accepts its configuration from the peer. When the Willing flag is TRUE, the system uses the DesiredCfg supplied by apeer as the OperCfg. A system that sets Willing to TRUE must be capable ofaccepting any valid DesiredCfg for the feature from the peer. In general, for onepeer to use the configuration of another peer, one peer must be willing and theother not willing. If both local and remote systems have the same value for theWilling flag, then the local DesiredCfg is used and the operational outcome of theexchange is determined by the Compatible method of the feature.

        Returns
        -------
        - self: This instance with all currently retrieved dcbxTlvPfcQaz resources using find and the newly added dcbxTlvPfcQaz resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Mbc=None, PfcCapability=None, PfcEnableVector=None, Willing=None):
        # type: (bool, int, str, bool) -> DcbxTlvPfcQaz
        """Finds and retrieves dcbxTlvPfcQaz resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dcbxTlvPfcQaz resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dcbxTlvPfcQaz resources from the server.

        Args
        ----
        - Mbc (bool): This signifies the MACsec Bypass Capability Bit. Enabling MBC indicates that the station can bypass MACsec processing when MACsec is disabled.
        - PfcCapability (number): The priority based flow control capability.
        - PfcEnableVector (str): If true, the priority based flow control vector is enabled.
        - Willing (bool): Indicates whether or not this feature accepts its configuration from the peer. When the Willing flag is TRUE, the system uses the DesiredCfg supplied by apeer as the OperCfg. A system that sets Willing to TRUE must be capable ofaccepting any valid DesiredCfg for the feature from the peer. In general, for onepeer to use the configuration of another peer, one peer must be willing and theother not willing. If both local and remote systems have the same value for theWilling flag, then the local DesiredCfg is used and the operational outcome of theexchange is determined by the Compatible method of the feature.

        Returns
        -------
        - self: This instance with matching dcbxTlvPfcQaz resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dcbxTlvPfcQaz data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dcbxTlvPfcQaz resources from the server available through an iterator or index

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
