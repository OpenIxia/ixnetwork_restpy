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
    """
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "testConfig"
    _SDM_ATT_MAP = {
        "CalculateJitter": "calculateJitter",
        "CalculateLatency": "calculateLatency",
        "CustomLoadUnit": "customLoadUnit",
        "DetailedResultsEnabled": "detailedResultsEnabled",
        "Duration": "duration",
        "EnableDataIntegrity": "enableDataIntegrity",
        "EnableLayer1Rate": "enableLayer1Rate",
        "FixedFrameSize": "fixedFrameSize",
        "FloodedFramesEnabled": "floodedFramesEnabled",
        "ForceContinuosTraffic": "forceContinuosTraffic",
        "FrameSizeMode": "frameSizeMode",
        "Gap": "gap",
        "IncrementFramesizeFrom": "incrementFramesizeFrom",
        "IncrementFramesizeStep": "incrementFramesizeStep",
        "IncrementFramesizeTo": "incrementFramesizeTo",
        "IpRatioMode": "ipRatioMode",
        "Ipv4rate": "ipv4rate",
        "Ipv6rate": "ipv6rate",
        "LatencyType": "latencyType",
        "LoadRateValue": "loadRateValue",
        "LoadType": "loadType",
        "Numtrials": "numtrials",
        "ProtocolItem": "protocolItem",
        "ReportSequenceError": "reportSequenceError",
        "ReportTputRateUnit": "reportTputRateUnit",
        "TrafficType": "trafficType",
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
        "frameSizeMode": ["fixed", "increment"],
        "ipRatioMode": ["custom", "fixed", "increment", "random"],
        "latencyType": ["cutThrough", "forwardingDelay", "mef", "storeForward"],
        "loadType": [
            "binary",
            "combo",
            "custom",
            "fixed",
            "increment",
            "quickSearch",
            "random",
            "step",
            "unchanged",
        ],
        "reportTputRateUnit": ["gbps", "gBps", "kbps", "kBps", "mbps", "mBps"],
        "trafficType": ["burstyLoading", "constantLoading"],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

    @property
    def CalculateJitter(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["CalculateJitter"])

    @CalculateJitter.setter
    def CalculateJitter(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CalculateJitter"], value)

    @property
    def CalculateLatency(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["CalculateLatency"])

    @CalculateLatency.setter
    def CalculateLatency(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CalculateLatency"], value)

    @property
    def CustomLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate):
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomLoadUnit"])

    @CustomLoadUnit.setter
    def CustomLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomLoadUnit"], value)

    @property
    def DetailedResultsEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["DetailedResultsEnabled"])

    @DetailedResultsEnabled.setter
    def DetailedResultsEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DetailedResultsEnabled"], value)

    @property
    def Duration(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Duration"])

    @Duration.setter
    def Duration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Duration"], value)

    @property
    def EnableDataIntegrity(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDataIntegrity"])

    @EnableDataIntegrity.setter
    def EnableDataIntegrity(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDataIntegrity"], value)

    @property
    def EnableLayer1Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLayer1Rate"])

    @EnableLayer1Rate.setter
    def EnableLayer1Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLayer1Rate"], value)

    @property
    def FixedFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FixedFrameSize"])

    @FixedFrameSize.setter
    def FixedFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FixedFrameSize"], value)

    @property
    def FloodedFramesEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FloodedFramesEnabled"])

    @FloodedFramesEnabled.setter
    def FloodedFramesEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FloodedFramesEnabled"], value)

    @property
    def ForceContinuosTraffic(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
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
        - str(fixed | increment):
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
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Gap"])

    @Gap.setter
    def Gap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Gap"], value)

    @property
    def IncrementFramesizeFrom(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementFramesizeFrom"])

    @IncrementFramesizeFrom.setter
    def IncrementFramesizeFrom(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementFramesizeFrom"], value)

    @property
    def IncrementFramesizeStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementFramesizeStep"])

    @IncrementFramesizeStep.setter
    def IncrementFramesizeStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementFramesizeStep"], value)

    @property
    def IncrementFramesizeTo(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementFramesizeTo"])

    @IncrementFramesizeTo.setter
    def IncrementFramesizeTo(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementFramesizeTo"], value)

    @property
    def IpRatioMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | fixed | increment | random):
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpRatioMode"])

    @IpRatioMode.setter
    def IpRatioMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpRatioMode"], value)

    @property
    def Ipv4rate(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4rate"])

    @Ipv4rate.setter
    def Ipv4rate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4rate"], value)

    @property
    def Ipv6rate(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6rate"])

    @Ipv6rate.setter
    def Ipv6rate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6rate"], value)

    @property
    def LatencyType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cutThrough | forwardingDelay | mef | storeForward):
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyType"])

    @LatencyType.setter
    def LatencyType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyType"], value)

    @property
    def LoadRateValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadRateValue"])

    @LoadRateValue.setter
    def LoadRateValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadRateValue"], value)

    @property
    def LoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged):
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadType"])

    @LoadType.setter
    def LoadType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadType"], value)

    @property
    def Numtrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
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
    def ReportSequenceError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportSequenceError"])

    @ReportSequenceError.setter
    def ReportSequenceError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportSequenceError"], value)

    @property
    def ReportTputRateUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(gbps | gBps | kbps | kBps | mbps | mBps):
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportTputRateUnit"])

    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportTputRateUnit"], value)

    @property
    def TrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(burstyLoading | constantLoading):
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficType"])

    @TrafficType.setter
    def TrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficType"], value)

    def update(
        self,
        CalculateJitter=None,
        CalculateLatency=None,
        CustomLoadUnit=None,
        DetailedResultsEnabled=None,
        Duration=None,
        EnableDataIntegrity=None,
        EnableLayer1Rate=None,
        FixedFrameSize=None,
        FloodedFramesEnabled=None,
        ForceContinuosTraffic=None,
        FrameSizeMode=None,
        Gap=None,
        IncrementFramesizeFrom=None,
        IncrementFramesizeStep=None,
        IncrementFramesizeTo=None,
        IpRatioMode=None,
        Ipv4rate=None,
        Ipv6rate=None,
        LatencyType=None,
        LoadRateValue=None,
        LoadType=None,
        Numtrials=None,
        ProtocolItem=None,
        ReportSequenceError=None,
        ReportTputRateUnit=None,
        TrafficType=None,
    ):
        # type: (bool, bool, str, bool, int, bool, bool, int, bool, bool, str, int, int, int, int, str, int, int, str, int, str, int, List[str], bool, str, str) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - CalculateJitter (bool):
        - CalculateLatency (bool):
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)):
        - DetailedResultsEnabled (bool):
        - Duration (number):
        - EnableDataIntegrity (bool):
        - EnableLayer1Rate (bool):
        - FixedFrameSize (number):
        - FloodedFramesEnabled (bool):
        - ForceContinuosTraffic (bool):
        - FrameSizeMode (str(fixed | increment)):
        - Gap (number):
        - IncrementFramesizeFrom (number):
        - IncrementFramesizeStep (number):
        - IncrementFramesizeTo (number):
        - IpRatioMode (str(custom | fixed | increment | random)):
        - Ipv4rate (number):
        - Ipv6rate (number):
        - LatencyType (str(cutThrough | forwardingDelay | mef | storeForward)):
        - LoadRateValue (number):
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)):
        - Numtrials (number):
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - ReportSequenceError (bool):
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)):
        - TrafficType (str(burstyLoading | constantLoading)):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CalculateJitter=None,
        CalculateLatency=None,
        CustomLoadUnit=None,
        DetailedResultsEnabled=None,
        Duration=None,
        EnableDataIntegrity=None,
        EnableLayer1Rate=None,
        FixedFrameSize=None,
        FloodedFramesEnabled=None,
        ForceContinuosTraffic=None,
        FrameSizeMode=None,
        Gap=None,
        IncrementFramesizeFrom=None,
        IncrementFramesizeStep=None,
        IncrementFramesizeTo=None,
        IpRatioMode=None,
        Ipv4rate=None,
        Ipv6rate=None,
        LatencyType=None,
        LoadRateValue=None,
        LoadType=None,
        Numtrials=None,
        ProtocolItem=None,
        ReportSequenceError=None,
        ReportTputRateUnit=None,
        TrafficType=None,
    ):
        # type: (bool, bool, str, bool, int, bool, bool, int, bool, bool, str, int, int, int, int, str, int, int, str, int, str, int, List[str], bool, str, str) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - CalculateJitter (bool):
        - CalculateLatency (bool):
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)):
        - DetailedResultsEnabled (bool):
        - Duration (number):
        - EnableDataIntegrity (bool):
        - EnableLayer1Rate (bool):
        - FixedFrameSize (number):
        - FloodedFramesEnabled (bool):
        - ForceContinuosTraffic (bool):
        - FrameSizeMode (str(fixed | increment)):
        - Gap (number):
        - IncrementFramesizeFrom (number):
        - IncrementFramesizeStep (number):
        - IncrementFramesizeTo (number):
        - IpRatioMode (str(custom | fixed | increment | random)):
        - Ipv4rate (number):
        - Ipv6rate (number):
        - LatencyType (str(cutThrough | forwardingDelay | mef | storeForward)):
        - LoadRateValue (number):
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)):
        - Numtrials (number):
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - ReportSequenceError (bool):
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)):
        - TrafficType (str(burstyLoading | constantLoading)):

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
