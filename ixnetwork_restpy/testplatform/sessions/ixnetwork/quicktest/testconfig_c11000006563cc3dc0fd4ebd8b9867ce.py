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


class TestConfig(Base):
    """The IxNetwork Test Configuration feature provides the ability to run predefined tests and allows the user to set some global test parameters for the individual test types.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "testConfig"
    _SDM_ATT_MAP = {
        "CpDpConvergenceFactorScale": "cpDpConvergenceFactorScale",
        "CpDpConvergenceTime": "cpDpConvergenceTime",
        "CustomFramesizeValue": "customFramesizeValue",
        "CustomLoadUnit": "customLoadUnit",
        "DelayAfterFailover": "delayAfterFailover",
        "DelayBeforeFailover": "delayBeforeFailover",
        "DeleteFlowsAtStartup": "deleteFlowsAtStartup",
        "DpDpConvergenceFactorScale": "dpDpConvergenceFactorScale",
        "DpDpConvergenceTime": "dpDpConvergenceTime",
        "EnableCpDpPassFail": "enableCpDpPassFail",
        "EnableDpDpPassFail": "enableDpDpPassFail",
        "EnableMinFrameSize": "enableMinFrameSize",
        "FailureMode": "failureMode",
        "FailureType": "failureType",
        "ForceContinuosTraffic": "forceContinuosTraffic",
        "FrameSizeMode": "frameSizeMode",
        "Gap": "gap",
        "LoadRateValue": "loadRateValue",
        "MaxRandomFrameSize": "maxRandomFrameSize",
        "MinRandomFrameSize": "minRandomFrameSize",
        "Numtrials": "numtrials",
        "ProtocolItem": "protocolItem",
        "ReportConvergenceUnit": "reportConvergenceUnit",
        "ReportTputRateUnit": "reportTputRateUnit",
        "SecondaryRxPort": "secondaryRxPort",
        "TestTrafficType": "testTrafficType",
    }
    _SDM_ENUM_MAP = {
        "customLoadUnit": [
            "bpsRate",
            "fpsRate",
            "gbpsRate",
            "gBpsRate",
            "kbpsRate",
            "kBpsRate",
            "mbpsRate",
            "mBpsRate",
            "percentMaxRate",
        ],
        "failureMode": ["delPrimaryFlow", "modifyRxPort"],
        "failureType": ["proactive"],
        "frameSizeMode": ["increment", "random"],
        "reportConvergenceUnit": ["ms", "ns", "us"],
        "reportTputRateUnit": ["gbps", "gBps", "kbps", "kBps", "mbps", "mBps"],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

    @property
    def CpDpConvergenceFactorScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the convergence factor scale.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpDpConvergenceFactorScale"])

    @CpDpConvergenceFactorScale.setter
    def CpDpConvergenceFactorScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpDpConvergenceFactorScale"], value)

    @property
    def CpDpConvergenceTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the convergence time.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpDpConvergenceTime"])

    @CpDpConvergenceTime.setter
    def CpDpConvergenceTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpDpConvergenceTime"], value)

    @property
    def CustomFramesizeValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the custom frame size value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomFramesizeValue"])

    @CustomFramesizeValue.setter
    def CustomFramesizeValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomFramesizeValue"], value)

    @property
    def CustomLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the custom load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomLoadUnit"])

    @CustomLoadUnit.setter
    def CustomLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomLoadUnit"], value)

    @property
    def DelayAfterFailover(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the delay after failover.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayAfterFailover"])

    @DelayAfterFailover.setter
    def DelayAfterFailover(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayAfterFailover"], value)

    @property
    def DelayBeforeFailover(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the delay before failover.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayBeforeFailover"])

    @DelayBeforeFailover.setter
    def DelayBeforeFailover(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayBeforeFailover"], value)

    @property
    def DeleteFlowsAtStartup(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the test will delete the flowgroups at startup.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeleteFlowsAtStartup"])

    @DeleteFlowsAtStartup.setter
    def DeleteFlowsAtStartup(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeleteFlowsAtStartup"], value)

    @property
    def DpDpConvergenceFactorScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the convergence factor scale.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DpDpConvergenceFactorScale"])

    @DpDpConvergenceFactorScale.setter
    def DpDpConvergenceFactorScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DpDpConvergenceFactorScale"], value)

    @property
    def DpDpConvergenceTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the convergence time.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DpDpConvergenceTime"])

    @DpDpConvergenceTime.setter
    def DpDpConvergenceTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DpDpConvergenceTime"], value)

    @property
    def EnableCpDpPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the CP DP pass fail.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCpDpPassFail"])

    @EnableCpDpPassFail.setter
    def EnableCpDpPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCpDpPassFail"], value)

    @property
    def EnableDpDpPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the DP DP pass fail
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDpDpPassFail"])

    @EnableDpDpPassFail.setter
    def EnableDpDpPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDpDpPassFail"], value)

    @property
    def EnableMinFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables minimum frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMinFrameSize"])

    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMinFrameSize"], value)

    @property
    def FailureMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(delPrimaryFlow | modifyRxPort): Sets the failure mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FailureMode"])

    @FailureMode.setter
    def FailureMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FailureMode"], value)

    @property
    def FailureType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(proactive): Sets the type of failure.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FailureType"])

    @FailureType.setter
    def FailureType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FailureType"], value)

    @property
    def ForceContinuosTraffic(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Forces continuous traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForceContinuosTraffic"])

    @ForceContinuosTraffic.setter
    def ForceContinuosTraffic(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForceContinuosTraffic"], value)

    @property
    def FrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(increment | random): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameSizeMode"])

    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameSizeMode"], value)

    @property
    def Gap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The gap in transmission of frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Gap"])

    @Gap.setter
    def Gap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Gap"], value)

    @property
    def LoadRateValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadRateValue"])

    @LoadRateValue.setter
    def LoadRateValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadRateValue"], value)

    @property
    def MaxRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxRandomFrameSize"])

    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxRandomFrameSize"], value)

    @property
    def MinRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRandomFrameSize"])

    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRandomFrameSize"], value)

    @property
    def Numtrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The integer value that states the number of trials permitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Numtrials"])

    @Numtrials.setter
    def Numtrials(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Numtrials"], value)

    @property
    def ProtocolItem(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan]): Protocol Items
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolItem"])

    @ProtocolItem.setter
    def ProtocolItem(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtocolItem"], value)

    @property
    def ReportConvergenceUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | ns | us): The unit in which convergence will be reported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportConvergenceUnit"])

    @ReportConvergenceUnit.setter
    def ReportConvergenceUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportConvergenceUnit"], value)

    @property
    def ReportTputRateUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(gbps | gBps | kbps | kBps | mbps | mBps): The unit of rate for throughput.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportTputRateUnit"])

    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportTputRateUnit"], value)

    @property
    def SecondaryRxPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the secondary receiving Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SecondaryRxPort"])

    @SecondaryRxPort.setter
    def SecondaryRxPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SecondaryRxPort"], value)

    @property
    def TestTrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the test traffic type value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestTrafficType"])

    @TestTrafficType.setter
    def TestTrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestTrafficType"], value)

    def update(
        self,
        CpDpConvergenceFactorScale=None,
        CpDpConvergenceTime=None,
        CustomFramesizeValue=None,
        CustomLoadUnit=None,
        DelayAfterFailover=None,
        DelayBeforeFailover=None,
        DeleteFlowsAtStartup=None,
        DpDpConvergenceFactorScale=None,
        DpDpConvergenceTime=None,
        EnableCpDpPassFail=None,
        EnableDpDpPassFail=None,
        EnableMinFrameSize=None,
        FailureMode=None,
        FailureType=None,
        ForceContinuosTraffic=None,
        FrameSizeMode=None,
        Gap=None,
        LoadRateValue=None,
        MaxRandomFrameSize=None,
        MinRandomFrameSize=None,
        Numtrials=None,
        ProtocolItem=None,
        ReportConvergenceUnit=None,
        ReportTputRateUnit=None,
        SecondaryRxPort=None,
        TestTrafficType=None,
    ):
        # type: (str, int, int, str, int, int, bool, str, int, bool, bool, bool, str, str, bool, str, int, int, int, int, int, List[str], str, str, int, str) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - CpDpConvergenceFactorScale (str): Indicates the convergence factor scale.
        - CpDpConvergenceTime (number): Indicates the convergence time.
        - CustomFramesizeValue (number): Sets the custom frame size value.
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the custom load unit.
        - DelayAfterFailover (number): Sets the delay after failover.
        - DelayBeforeFailover (number): Sets the delay before failover.
        - DeleteFlowsAtStartup (bool): If true, the test will delete the flowgroups at startup.
        - DpDpConvergenceFactorScale (str): Indicates the convergence factor scale.
        - DpDpConvergenceTime (number): Indicates the convergence time.
        - EnableCpDpPassFail (bool): Enables the CP DP pass fail.
        - EnableDpDpPassFail (bool): Enables the DP DP pass fail
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - FailureMode (str(delPrimaryFlow | modifyRxPort)): Sets the failure mode.
        - FailureType (str(proactive)): Sets the type of failure.
        - ForceContinuosTraffic (bool): Forces continuous traffic.
        - FrameSizeMode (str(increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - Gap (number): The gap in transmission of frames.
        - LoadRateValue (number): The value of the load rate.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - Numtrials (number): The integer value that states the number of trials permitted.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - ReportConvergenceUnit (str(ms | ns | us)): The unit in which convergence will be reported.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The unit of rate for throughput.
        - SecondaryRxPort (number): Sets the secondary receiving Port.
        - TestTrafficType (str): It signifies the test traffic type value.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CpDpConvergenceFactorScale=None,
        CpDpConvergenceTime=None,
        CustomFramesizeValue=None,
        CustomLoadUnit=None,
        DelayAfterFailover=None,
        DelayBeforeFailover=None,
        DeleteFlowsAtStartup=None,
        DpDpConvergenceFactorScale=None,
        DpDpConvergenceTime=None,
        EnableCpDpPassFail=None,
        EnableDpDpPassFail=None,
        EnableMinFrameSize=None,
        FailureMode=None,
        FailureType=None,
        ForceContinuosTraffic=None,
        FrameSizeMode=None,
        Gap=None,
        LoadRateValue=None,
        MaxRandomFrameSize=None,
        MinRandomFrameSize=None,
        Numtrials=None,
        ProtocolItem=None,
        ReportConvergenceUnit=None,
        ReportTputRateUnit=None,
        SecondaryRxPort=None,
        TestTrafficType=None,
    ):
        # type: (str, int, int, str, int, int, bool, str, int, bool, bool, bool, str, str, bool, str, int, int, int, int, int, List[str], str, str, int, str) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - CpDpConvergenceFactorScale (str): Indicates the convergence factor scale.
        - CpDpConvergenceTime (number): Indicates the convergence time.
        - CustomFramesizeValue (number): Sets the custom frame size value.
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the custom load unit.
        - DelayAfterFailover (number): Sets the delay after failover.
        - DelayBeforeFailover (number): Sets the delay before failover.
        - DeleteFlowsAtStartup (bool): If true, the test will delete the flowgroups at startup.
        - DpDpConvergenceFactorScale (str): Indicates the convergence factor scale.
        - DpDpConvergenceTime (number): Indicates the convergence time.
        - EnableCpDpPassFail (bool): Enables the CP DP pass fail.
        - EnableDpDpPassFail (bool): Enables the DP DP pass fail
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - FailureMode (str(delPrimaryFlow | modifyRxPort)): Sets the failure mode.
        - FailureType (str(proactive)): Sets the type of failure.
        - ForceContinuosTraffic (bool): Forces continuous traffic.
        - FrameSizeMode (str(increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - Gap (number): The gap in transmission of frames.
        - LoadRateValue (number): The value of the load rate.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - Numtrials (number): The integer value that states the number of trials permitted.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - ReportConvergenceUnit (str(ms | ns | us)): The unit in which convergence will be reported.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The unit of rate for throughput.
        - SecondaryRxPort (number): Sets the secondary receiving Port.
        - TestTrafficType (str): It signifies the test traffic type value.

        Returns
        -------
        - self: This instance with matching testConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of testConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the testConfig resources from the server available through an iterator or index

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
