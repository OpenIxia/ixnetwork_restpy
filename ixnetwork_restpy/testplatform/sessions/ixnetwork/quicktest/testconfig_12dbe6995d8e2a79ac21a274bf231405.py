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
        "CustomLoadUnit": "customLoadUnit",
        "DataPlaneJitterWindow": "dataPlaneJitterWindow",
        "Duration": "duration",
        "EnableBFD": "enableBFD",
        "EnableTolerance": "enableTolerance",
        "FixedFrameSize": "fixedFrameSize",
        "ForceContinuosTraffic": "forceContinuosTraffic",
        "FrameSizeMode": "frameSizeMode",
        "Framesize": "framesize",
        "HoldDownTimer": "holdDownTimer",
        "IpRatioMode": "ipRatioMode",
        "Ipv4rate": "ipv4rate",
        "Ipv6rate": "ipv6rate",
        "LoadRateValue": "loadRateValue",
        "LoadType": "loadType",
        "NetworkGroupRoutesType": "networkGroupRoutesType",
        "NetworkGroupSizeListIpv4": "networkGroupSizeListIpv4",
        "NetworkGroupSizeListIpv6": "networkGroupSizeListIpv6",
        "NetworkGroupSizeModeIpv4": "networkGroupSizeModeIpv4",
        "NetworkGroupSizeModeIpv6": "networkGroupSizeModeIpv6",
        "NumberOfIterations": "numberOfIterations",
        "Numtrials": "numtrials",
        "ProtocolItem": "protocolItem",
        "ReportConvergenceUnit": "reportConvergenceUnit",
        "ReportTputRateUnit": "reportTputRateUnit",
        "RoutesDistribution": "routesDistribution",
        "TestTrafficType": "testTrafficType",
        "Threshold": "threshold",
        "Tolerance": "tolerance",
        "TrafficType": "trafficType",
        "WaitAfterThresholdReached": "waitAfterThresholdReached",
        "WaitBeforeAdvertise": "waitBeforeAdvertise",
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
        "dataPlaneJitterWindow": [
            "k_10485760",
            "k_1310720",
            "k_167772160",
            "k_20971520",
            "k_2621440",
            "k_335544320",
            "k_41943040",
            "k_5242880",
            "k_671088640",
            "k_83886080",
        ],
        "frameSizeMode": ["fixed"],
        "ipRatioMode": ["custom", "fixed", "increment", "random"],
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
        "networkGroupRoutesType": ["ipv4", "ipv4/ipv6", "ipv6"],
        "networkGroupSizeModeIpv4": ["custom"],
        "networkGroupSizeModeIpv6": ["custom"],
        "reportConvergenceUnit": ["ms", "s", "us"],
        "reportTputRateUnit": ["gbps", "gBps", "kbps", "kBps", "mbps", "mBps"],
        "routesDistribution": ["distributedAcrossPorts", "equalCostOnEachPort"],
        "trafficType": ["burstyLoading", "constantLoading"],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

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
    def DataPlaneJitterWindow(self):
        # type: () -> str
        """
        Returns
        -------
        - str(k_10485760 | k_1310720 | k_167772160 | k_20971520 | k_2621440 | k_335544320 | k_41943040 | k_5242880 | k_671088640 | k_83886080):
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPlaneJitterWindow"])

    @DataPlaneJitterWindow.setter
    def DataPlaneJitterWindow(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataPlaneJitterWindow"], value)

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
    def EnableBFD(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableBFD"])

    @EnableBFD.setter
    def EnableBFD(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableBFD"], value)

    @property
    def EnableTolerance(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableTolerance"])

    @EnableTolerance.setter
    def EnableTolerance(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableTolerance"], value)

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
        - str(fixed):
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameSizeMode"])

    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameSizeMode"], value)

    @property
    def Framesize(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Framesize"])

    @Framesize.setter
    def Framesize(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Framesize"], value)

    @property
    def HoldDownTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["HoldDownTimer"])

    @HoldDownTimer.setter
    def HoldDownTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["HoldDownTimer"], value)

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
    def NetworkGroupRoutesType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipv4 | ipv4/ipv6 | ipv6):
        """
        return self._get_attribute(self._SDM_ATT_MAP["NetworkGroupRoutesType"])

    @NetworkGroupRoutesType.setter
    def NetworkGroupRoutesType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NetworkGroupRoutesType"], value)

    @property
    def NetworkGroupSizeListIpv4(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str):
        """
        return self._get_attribute(self._SDM_ATT_MAP["NetworkGroupSizeListIpv4"])

    @NetworkGroupSizeListIpv4.setter
    def NetworkGroupSizeListIpv4(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["NetworkGroupSizeListIpv4"], value)

    @property
    def NetworkGroupSizeListIpv6(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str):
        """
        return self._get_attribute(self._SDM_ATT_MAP["NetworkGroupSizeListIpv6"])

    @NetworkGroupSizeListIpv6.setter
    def NetworkGroupSizeListIpv6(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["NetworkGroupSizeListIpv6"], value)

    @property
    def NetworkGroupSizeModeIpv4(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom):
        """
        return self._get_attribute(self._SDM_ATT_MAP["NetworkGroupSizeModeIpv4"])

    @NetworkGroupSizeModeIpv4.setter
    def NetworkGroupSizeModeIpv4(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NetworkGroupSizeModeIpv4"], value)

    @property
    def NetworkGroupSizeModeIpv6(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom):
        """
        return self._get_attribute(self._SDM_ATT_MAP["NetworkGroupSizeModeIpv6"])

    @NetworkGroupSizeModeIpv6.setter
    def NetworkGroupSizeModeIpv6(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NetworkGroupSizeModeIpv6"], value)

    @property
    def NumberOfIterations(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfIterations"])

    @NumberOfIterations.setter
    def NumberOfIterations(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfIterations"], value)

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
    def ReportConvergenceUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | s | us):
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
        - str(gbps | gBps | kbps | kBps | mbps | mBps):
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportTputRateUnit"])

    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportTputRateUnit"], value)

    @property
    def RoutesDistribution(self):
        # type: () -> str
        """
        Returns
        -------
        - str(distributedAcrossPorts | equalCostOnEachPort):
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutesDistribution"])

    @RoutesDistribution.setter
    def RoutesDistribution(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutesDistribution"], value)

    @property
    def TestTrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestTrafficType"])

    @TestTrafficType.setter
    def TestTrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestTrafficType"], value)

    @property
    def Threshold(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Threshold"])

    @Threshold.setter
    def Threshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Threshold"], value)

    @property
    def Tolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Tolerance"])

    @Tolerance.setter
    def Tolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Tolerance"], value)

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

    @property
    def WaitAfterThresholdReached(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["WaitAfterThresholdReached"])

    @WaitAfterThresholdReached.setter
    def WaitAfterThresholdReached(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["WaitAfterThresholdReached"], value)

    @property
    def WaitBeforeAdvertise(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["WaitBeforeAdvertise"])

    @WaitBeforeAdvertise.setter
    def WaitBeforeAdvertise(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["WaitBeforeAdvertise"], value)

    def update(
        self,
        CustomLoadUnit=None,
        DataPlaneJitterWindow=None,
        Duration=None,
        EnableBFD=None,
        EnableTolerance=None,
        FixedFrameSize=None,
        ForceContinuosTraffic=None,
        FrameSizeMode=None,
        Framesize=None,
        HoldDownTimer=None,
        IpRatioMode=None,
        Ipv4rate=None,
        Ipv6rate=None,
        LoadRateValue=None,
        LoadType=None,
        NetworkGroupRoutesType=None,
        NetworkGroupSizeListIpv4=None,
        NetworkGroupSizeListIpv6=None,
        NetworkGroupSizeModeIpv4=None,
        NetworkGroupSizeModeIpv6=None,
        NumberOfIterations=None,
        Numtrials=None,
        ProtocolItem=None,
        ReportConvergenceUnit=None,
        ReportTputRateUnit=None,
        RoutesDistribution=None,
        TestTrafficType=None,
        Threshold=None,
        Tolerance=None,
        TrafficType=None,
        WaitAfterThresholdReached=None,
        WaitBeforeAdvertise=None,
    ):
        # type: (str, str, int, bool, bool, int, bool, str, str, int, str, int, int, int, str, str, List[str], List[str], str, str, int, int, List[str], str, str, str, str, int, int, str, int, int) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)):
        - DataPlaneJitterWindow (str(k_10485760 | k_1310720 | k_167772160 | k_20971520 | k_2621440 | k_335544320 | k_41943040 | k_5242880 | k_671088640 | k_83886080)):
        - Duration (number):
        - EnableBFD (bool):
        - EnableTolerance (bool):
        - FixedFrameSize (number):
        - ForceContinuosTraffic (bool):
        - FrameSizeMode (str(fixed)):
        - Framesize (str):
        - HoldDownTimer (number):
        - IpRatioMode (str(custom | fixed | increment | random)):
        - Ipv4rate (number):
        - Ipv6rate (number):
        - LoadRateValue (number):
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)):
        - NetworkGroupRoutesType (str(ipv4 | ipv4/ipv6 | ipv6)):
        - NetworkGroupSizeListIpv4 (list(str)):
        - NetworkGroupSizeListIpv6 (list(str)):
        - NetworkGroupSizeModeIpv4 (str(custom)):
        - NetworkGroupSizeModeIpv6 (str(custom)):
        - NumberOfIterations (number):
        - Numtrials (number):
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - ReportConvergenceUnit (str(ms | s | us)):
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)):
        - RoutesDistribution (str(distributedAcrossPorts | equalCostOnEachPort)):
        - TestTrafficType (str):
        - Threshold (number):
        - Tolerance (number):
        - TrafficType (str(burstyLoading | constantLoading)):
        - WaitAfterThresholdReached (number):
        - WaitBeforeAdvertise (number):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CustomLoadUnit=None,
        DataPlaneJitterWindow=None,
        Duration=None,
        EnableBFD=None,
        EnableTolerance=None,
        FixedFrameSize=None,
        ForceContinuosTraffic=None,
        FrameSizeMode=None,
        Framesize=None,
        HoldDownTimer=None,
        IpRatioMode=None,
        Ipv4rate=None,
        Ipv6rate=None,
        LoadRateValue=None,
        LoadType=None,
        NetworkGroupRoutesType=None,
        NetworkGroupSizeListIpv4=None,
        NetworkGroupSizeListIpv6=None,
        NetworkGroupSizeModeIpv4=None,
        NetworkGroupSizeModeIpv6=None,
        NumberOfIterations=None,
        Numtrials=None,
        ProtocolItem=None,
        ReportConvergenceUnit=None,
        ReportTputRateUnit=None,
        RoutesDistribution=None,
        TestTrafficType=None,
        Threshold=None,
        Tolerance=None,
        TrafficType=None,
        WaitAfterThresholdReached=None,
        WaitBeforeAdvertise=None,
    ):
        # type: (str, str, int, bool, bool, int, bool, str, str, int, str, int, int, int, str, str, List[str], List[str], str, str, int, int, List[str], str, str, str, str, int, int, str, int, int) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)):
        - DataPlaneJitterWindow (str(k_10485760 | k_1310720 | k_167772160 | k_20971520 | k_2621440 | k_335544320 | k_41943040 | k_5242880 | k_671088640 | k_83886080)):
        - Duration (number):
        - EnableBFD (bool):
        - EnableTolerance (bool):
        - FixedFrameSize (number):
        - ForceContinuosTraffic (bool):
        - FrameSizeMode (str(fixed)):
        - Framesize (str):
        - HoldDownTimer (number):
        - IpRatioMode (str(custom | fixed | increment | random)):
        - Ipv4rate (number):
        - Ipv6rate (number):
        - LoadRateValue (number):
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)):
        - NetworkGroupRoutesType (str(ipv4 | ipv4/ipv6 | ipv6)):
        - NetworkGroupSizeListIpv4 (list(str)):
        - NetworkGroupSizeListIpv6 (list(str)):
        - NetworkGroupSizeModeIpv4 (str(custom)):
        - NetworkGroupSizeModeIpv6 (str(custom)):
        - NumberOfIterations (number):
        - Numtrials (number):
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - ReportConvergenceUnit (str(ms | s | us)):
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)):
        - RoutesDistribution (str(distributedAcrossPorts | equalCostOnEachPort)):
        - TestTrafficType (str):
        - Threshold (number):
        - Tolerance (number):
        - TrafficType (str(burstyLoading | constantLoading)):
        - WaitAfterThresholdReached (number):
        - WaitBeforeAdvertise (number):

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
