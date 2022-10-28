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
        "AddrRateNumFrames": "addrRateNumFrames",
        "AddrRateValidationFpsRate": "addrRateValidationFpsRate",
        "AddrRateValidationRate": "addrRateValidationRate",
        "AddrRateValidationRateUnit": "addrRateValidationRateUnit",
        "AddressCachePassCriteriaMode": "addressCachePassCriteriaMode",
        "AddressRatePassFailValue": "addressRatePassFailValue",
        "Age": "age",
        "BidirectionalOptionEnabled": "bidirectionalOptionEnabled",
        "BinaryBackoff": "binaryBackoff",
        "BinaryResolution": "binaryResolution",
        "BinarySearchType": "binarySearchType",
        "BinaryTolerance": "binaryTolerance",
        "CalculateLatency": "calculateLatency",
        "CountRandomFrameSize": "countRandomFrameSize",
        "DelayAfterTransmit": "delayAfterTransmit",
        "EnableAddressRatePassFail": "enableAddressRatePassFail",
        "EnableDataIntegrity": "enableDataIntegrity",
        "EnableDropLink": "enableDropLink",
        "EnableMinFrameSize": "enableMinFrameSize",
        "EnforceBidirectional": "enforceBidirectional",
        "FrameSizeMode": "frameSizeMode",
        "FramesizeList": "framesizeList",
        "Gap": "gap",
        "InitialAddressNum": "initialAddressNum",
        "InitialBinaryLoadRate": "initialBinaryLoadRate",
        "LoadType": "loadType",
        "LoadUnit": "loadUnit",
        "MapType": "mapType",
        "MaxBinaryLoadRate": "maxBinaryLoadRate",
        "MaxIncrementFrameSize": "maxIncrementFrameSize",
        "MaxRandomFrameSize": "maxRandomFrameSize",
        "MinAddressNum": "minAddressNum",
        "MinBinaryLoadRate": "minBinaryLoadRate",
        "MinIncrementFrameSize": "minIncrementFrameSize",
        "MinRandomFrameSize": "minRandomFrameSize",
        "Numtrials": "numtrials",
        "PortDelayEnabled": "portDelayEnabled",
        "PortDelayUnit": "portDelayUnit",
        "PortDelayValue": "portDelayValue",
        "PortDownTime": "portDownTime",
        "ProtocolItem": "protocolItem",
        "Rfc2889ordering": "rfc2889ordering",
        "ShowDetailedBinaryResults": "showDetailedBinaryResults",
        "StepIncrementFrameSize": "stepIncrementFrameSize",
        "SupportedTrafficTypes": "supportedTrafficTypes",
        "Tablesize": "tablesize",
        "TxDelay": "txDelay",
    }
    _SDM_ENUM_MAP = {
        "addrRateValidationRateUnit": ["fps", "percentMaxRate"],
        "binarySearchType": ["linear"],
        "frameSizeMode": ["custom", "increment", "random"],
        "loadType": ["binary"],
        "loadUnit": ["fpsRate"],
        "portDelayUnit": ["bytes", "nanoseconds"],
        "rfc2889ordering": ["noOrdering", "unchanged", "val2889Ordering"],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

    @property
    def AddrRateNumFrames(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of addresses that are to be used for each port in the current configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddrRateNumFrames"])

    @AddrRateNumFrames.setter
    def AddrRateNumFrames(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddrRateNumFrames"], value)

    @property
    def AddrRateValidationFpsRate(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The rate at which validation frames are sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddrRateValidationFpsRate"])

    @AddrRateValidationFpsRate.setter
    def AddrRateValidationFpsRate(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddrRateValidationFpsRate"], value)

    @property
    def AddrRateValidationRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of validation frames that IxNetwork sends for each address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddrRateValidationRate"])

    @AddrRateValidationRate.setter
    def AddrRateValidationRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddrRateValidationRate"], value)

    @property
    def AddrRateValidationRateUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fps | percentMaxRate): The unit of rate at which validation frames are sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddrRateValidationRateUnit"])

    @AddrRateValidationRateUnit.setter
    def AddrRateValidationRateUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddrRateValidationRateUnit"], value)

    @property
    def AddressCachePassCriteriaMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the address cache pass criteria mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddressCachePassCriteriaMode"])

    @AddressCachePassCriteriaMode.setter
    def AddressCachePassCriteriaMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddressCachePassCriteriaMode"], value)

    @property
    def AddressRatePassFailValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the address pass and fail rate value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddressRatePassFailValue"])

    @AddressRatePassFailValue.setter
    def AddressRatePassFailValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddressRatePassFailValue"], value)

    @property
    def Age(self):
        # type: () -> int
        """
        Returns
        -------
        - number: New table size for each retry.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Age"])

    @Age.setter
    def Age(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Age"], value)

    @property
    def BidirectionalOptionEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, allows bidirectional traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BidirectionalOptionEnabled"])

    @BidirectionalOptionEnabled.setter
    def BidirectionalOptionEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BidirectionalOptionEnabled"], value)

    @property
    def BinaryBackoff(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the percentage of binary backoff.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryBackoff"])

    @BinaryBackoff.setter
    def BinaryBackoff(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryBackoff"], value)

    @property
    def BinaryResolution(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the resolution of the iteration. The difference between the real ratetransmission in two consecutive iterations, expressed as a percentage, iscompared with the resolution value. When the difference is smaller than thevalue specified for the resolution, the test stops.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryResolution"])

    @BinaryResolution.setter
    def BinaryResolution(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryResolution"], value)

    @property
    def BinarySearchType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(linear): Signifies the binary search type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinarySearchType"])

    @BinarySearchType.setter
    def BinarySearchType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinarySearchType"], value)

    @property
    def BinaryTolerance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The binary tolerance level.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryTolerance"])

    @BinaryTolerance.setter
    def BinaryTolerance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryTolerance"], value)

    @property
    def CalculateLatency(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the latency is calculated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CalculateLatency"])

    @CalculateLatency.setter
    def CalculateLatency(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CalculateLatency"], value)

    @property
    def CountRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, randomly counts the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CountRandomFrameSize"])

    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CountRandomFrameSize"], value)

    @property
    def DelayAfterTransmit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the amount of delay after every transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"])

    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"], value)

    @property
    def EnableAddressRatePassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the rate of pass and fail criteria is set.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAddressRatePassFail"])

    @EnableAddressRatePassFail.setter
    def EnableAddressRatePassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAddressRatePassFail"], value)

    @property
    def EnableDataIntegrity(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables data integrity test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDataIntegrity"])

    @EnableDataIntegrity.setter
    def EnableDataIntegrity(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDataIntegrity"], value)

    @property
    def EnableDropLink(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, allows to drop link.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDropLink"])

    @EnableDropLink.setter
    def EnableDropLink(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDropLink"], value)

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
    def EnforceBidirectional(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, uses bidirectional traffic mapping.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnforceBidirectional"])

    @EnforceBidirectional.setter
    def EnforceBidirectional(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnforceBidirectional"], value)

    @property
    def FrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | increment | random): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameSizeMode"])

    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameSizeMode"], value)

    @property
    def FramesizeList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): List containing the frame sizes used in the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesizeList"])

    @FramesizeList.setter
    def FramesizeList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesizeList"], value)

    @property
    def Gap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the gap value for the protocol.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Gap"])

    @Gap.setter
    def Gap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Gap"], value)

    @property
    def InitialAddressNum(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The initial number of addresses used in the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialAddressNum"])

    @InitialAddressNum.setter
    def InitialAddressNum(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialAddressNum"], value)

    @property
    def InitialBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the initial rate of the binary algorithm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialBinaryLoadRate"])

    @InitialBinaryLoadRate.setter
    def InitialBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialBinaryLoadRate"], value)

    @property
    def LoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(binary): The type of load used to modify the variable parameter value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadType"])

    @LoadType.setter
    def LoadType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadType"], value)

    @property
    def LoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fpsRate): The load unit value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadUnit"])

    @LoadUnit.setter
    def LoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadUnit"], value)

    @property
    def MapType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The mapping type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapType"])

    @MapType.setter
    def MapType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapType"], value)

    @property
    def MaxBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the maximum rate of the binary algorithm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxBinaryLoadRate"])

    @MaxBinaryLoadRate.setter
    def MaxBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxBinaryLoadRate"], value)

    @property
    def MaxIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum incremental value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxIncrementFrameSize"])

    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxIncrementFrameSize"], value)

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
    def MinAddressNum(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum number of addresses used in the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinAddressNum"])

    @MinAddressNum.setter
    def MinAddressNum(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinAddressNum"], value)

    @property
    def MinBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the minimum rate of the binary algorithm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinBinaryLoadRate"])

    @MinBinaryLoadRate.setter
    def MinBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinBinaryLoadRate"], value)

    @property
    def MinIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum incremental value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinIncrementFrameSize"])

    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinIncrementFrameSize"], value)

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
        - number: Defines how many times each frame size will be tested.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Numtrials"])

    @Numtrials.setter
    def Numtrials(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Numtrials"], value)

    @property
    def PortDelayEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDelayEnabled"])

    @PortDelayEnabled.setter
    def PortDelayEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDelayEnabled"], value)

    @property
    def PortDelayUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDelayUnit"])

    @PortDelayUnit.setter
    def PortDelayUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDelayUnit"], value)

    @property
    def PortDelayValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the port delay value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDelayValue"])

    @PortDelayValue.setter
    def PortDelayValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDelayValue"], value)

    @property
    def PortDownTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time interval during the port is down.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDownTime"])

    @PortDownTime.setter
    def PortDownTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDownTime"], value)

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
    def Rfc2889ordering(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noOrdering | unchanged | val2889Ordering): Enables ordering.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Rfc2889ordering"])

    @Rfc2889ordering.setter
    def Rfc2889ordering(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Rfc2889ordering"], value)

    @property
    def ShowDetailedBinaryResults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowDetailedBinaryResults"])

    @ShowDetailedBinaryResults.setter
    def ShowDetailedBinaryResults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowDetailedBinaryResults"], value)

    @property
    def StepIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The incremental step value of the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StepIncrementFrameSize"])

    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StepIncrementFrameSize"], value)

    @property
    def SupportedTrafficTypes(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The traffic types supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportedTrafficTypes"])

    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportedTrafficTypes"], value)

    @property
    def Tablesize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of addresses that are to be used for the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Tablesize"])

    @Tablesize.setter
    def Tablesize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Tablesize"], value)

    @property
    def TxDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the transmission delay time.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxDelay"])

    @TxDelay.setter
    def TxDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxDelay"], value)

    def update(
        self,
        AddrRateNumFrames=None,
        AddrRateValidationFpsRate=None,
        AddrRateValidationRate=None,
        AddrRateValidationRateUnit=None,
        AddressCachePassCriteriaMode=None,
        AddressRatePassFailValue=None,
        Age=None,
        BidirectionalOptionEnabled=None,
        BinaryBackoff=None,
        BinaryResolution=None,
        BinarySearchType=None,
        BinaryTolerance=None,
        CalculateLatency=None,
        CountRandomFrameSize=None,
        DelayAfterTransmit=None,
        EnableAddressRatePassFail=None,
        EnableDataIntegrity=None,
        EnableDropLink=None,
        EnableMinFrameSize=None,
        EnforceBidirectional=None,
        FrameSizeMode=None,
        FramesizeList=None,
        Gap=None,
        InitialAddressNum=None,
        InitialBinaryLoadRate=None,
        LoadType=None,
        LoadUnit=None,
        MapType=None,
        MaxBinaryLoadRate=None,
        MaxIncrementFrameSize=None,
        MaxRandomFrameSize=None,
        MinAddressNum=None,
        MinBinaryLoadRate=None,
        MinIncrementFrameSize=None,
        MinRandomFrameSize=None,
        Numtrials=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        PortDownTime=None,
        ProtocolItem=None,
        Rfc2889ordering=None,
        ShowDetailedBinaryResults=None,
        StepIncrementFrameSize=None,
        SupportedTrafficTypes=None,
        Tablesize=None,
        TxDelay=None,
    ):
        # type: (int, str, int, str, str, int, int, bool, int, int, str, int, bool, int, int, bool, bool, bool, bool, bool, str, List[str], int, int, int, str, str, str, int, int, int, int, int, int, int, int, bool, str, int, int, List[str], str, bool, int, str, int, int) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - AddrRateNumFrames (number): The number of addresses that are to be used for each port in the current configuration.
        - AddrRateValidationFpsRate (str): The rate at which validation frames are sent.
        - AddrRateValidationRate (number): The number of validation frames that IxNetwork sends for each address.
        - AddrRateValidationRateUnit (str(fps | percentMaxRate)): The unit of rate at which validation frames are sent.
        - AddressCachePassCriteriaMode (str): Signifies the address cache pass criteria mode.
        - AddressRatePassFailValue (number): Signifies the address pass and fail rate value.
        - Age (number): New table size for each retry.
        - BidirectionalOptionEnabled (bool): If true, allows bidirectional traffic.
        - BinaryBackoff (number): Specifies the percentage of binary backoff.
        - BinaryResolution (number): Specifies the resolution of the iteration. The difference between the real ratetransmission in two consecutive iterations, expressed as a percentage, iscompared with the resolution value. When the difference is smaller than thevalue specified for the resolution, the test stops.
        - BinarySearchType (str(linear)): Signifies the binary search type.
        - BinaryTolerance (number): The binary tolerance level.
        - CalculateLatency (bool): If true, the latency is calculated.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - EnableAddressRatePassFail (bool): If true, the rate of pass and fail criteria is set.
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableDropLink (bool): If true, allows to drop link.
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnforceBidirectional (bool): If true, uses bidirectional traffic mapping.
        - FrameSizeMode (str(custom | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - FramesizeList (list(str)): List containing the frame sizes used in the test.
        - Gap (number): It signifies the gap value for the protocol.
        - InitialAddressNum (number): The initial number of addresses used in the test.
        - InitialBinaryLoadRate (number): Specifies the initial rate of the binary algorithm.
        - LoadType (str(binary)): The type of load used to modify the variable parameter value.
        - LoadUnit (str(fpsRate)): The load unit value.
        - MapType (str): The mapping type.
        - MaxBinaryLoadRate (number): Specifies the maximum rate of the binary algorithm.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MinAddressNum (number): The minimum number of addresses used in the test.
        - MinBinaryLoadRate (number): Specifies the minimum rate of the binary algorithm.
        - MinIncrementFrameSize (number): The minimum incremental value of the frame size.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - Numtrials (number): Defines how many times each frame size will be tested.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - PortDownTime (number): The time interval during the port is down.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - Rfc2889ordering (str(noOrdering | unchanged | val2889Ordering)): Enables ordering.
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - SupportedTrafficTypes (str): The traffic types supported.
        - Tablesize (number): The number of addresses that are to be used for the test.
        - TxDelay (number): Signifies the transmission delay time.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AddrRateNumFrames=None,
        AddrRateValidationFpsRate=None,
        AddrRateValidationRate=None,
        AddrRateValidationRateUnit=None,
        AddressCachePassCriteriaMode=None,
        AddressRatePassFailValue=None,
        Age=None,
        BidirectionalOptionEnabled=None,
        BinaryBackoff=None,
        BinaryResolution=None,
        BinarySearchType=None,
        BinaryTolerance=None,
        CalculateLatency=None,
        CountRandomFrameSize=None,
        DelayAfterTransmit=None,
        EnableAddressRatePassFail=None,
        EnableDataIntegrity=None,
        EnableDropLink=None,
        EnableMinFrameSize=None,
        EnforceBidirectional=None,
        FrameSizeMode=None,
        FramesizeList=None,
        Gap=None,
        InitialAddressNum=None,
        InitialBinaryLoadRate=None,
        LoadType=None,
        LoadUnit=None,
        MapType=None,
        MaxBinaryLoadRate=None,
        MaxIncrementFrameSize=None,
        MaxRandomFrameSize=None,
        MinAddressNum=None,
        MinBinaryLoadRate=None,
        MinIncrementFrameSize=None,
        MinRandomFrameSize=None,
        Numtrials=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        PortDownTime=None,
        ProtocolItem=None,
        Rfc2889ordering=None,
        ShowDetailedBinaryResults=None,
        StepIncrementFrameSize=None,
        SupportedTrafficTypes=None,
        Tablesize=None,
        TxDelay=None,
    ):
        # type: (int, str, int, str, str, int, int, bool, int, int, str, int, bool, int, int, bool, bool, bool, bool, bool, str, List[str], int, int, int, str, str, str, int, int, int, int, int, int, int, int, bool, str, int, int, List[str], str, bool, int, str, int, int) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - AddrRateNumFrames (number): The number of addresses that are to be used for each port in the current configuration.
        - AddrRateValidationFpsRate (str): The rate at which validation frames are sent.
        - AddrRateValidationRate (number): The number of validation frames that IxNetwork sends for each address.
        - AddrRateValidationRateUnit (str(fps | percentMaxRate)): The unit of rate at which validation frames are sent.
        - AddressCachePassCriteriaMode (str): Signifies the address cache pass criteria mode.
        - AddressRatePassFailValue (number): Signifies the address pass and fail rate value.
        - Age (number): New table size for each retry.
        - BidirectionalOptionEnabled (bool): If true, allows bidirectional traffic.
        - BinaryBackoff (number): Specifies the percentage of binary backoff.
        - BinaryResolution (number): Specifies the resolution of the iteration. The difference between the real ratetransmission in two consecutive iterations, expressed as a percentage, iscompared with the resolution value. When the difference is smaller than thevalue specified for the resolution, the test stops.
        - BinarySearchType (str(linear)): Signifies the binary search type.
        - BinaryTolerance (number): The binary tolerance level.
        - CalculateLatency (bool): If true, the latency is calculated.
        - CountRandomFrameSize (number): If true, randomly counts the frame size.
        - DelayAfterTransmit (number): Specifies the amount of delay after every transmit.
        - EnableAddressRatePassFail (bool): If true, the rate of pass and fail criteria is set.
        - EnableDataIntegrity (bool): If true, enables data integrity test.
        - EnableDropLink (bool): If true, allows to drop link.
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnforceBidirectional (bool): If true, uses bidirectional traffic mapping.
        - FrameSizeMode (str(custom | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - FramesizeList (list(str)): List containing the frame sizes used in the test.
        - Gap (number): It signifies the gap value for the protocol.
        - InitialAddressNum (number): The initial number of addresses used in the test.
        - InitialBinaryLoadRate (number): Specifies the initial rate of the binary algorithm.
        - LoadType (str(binary)): The type of load used to modify the variable parameter value.
        - LoadUnit (str(fpsRate)): The load unit value.
        - MapType (str): The mapping type.
        - MaxBinaryLoadRate (number): Specifies the maximum rate of the binary algorithm.
        - MaxIncrementFrameSize (number): The maximum incremental value of the frame size.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MinAddressNum (number): The minimum number of addresses used in the test.
        - MinBinaryLoadRate (number): Specifies the minimum rate of the binary algorithm.
        - MinIncrementFrameSize (number): The minimum incremental value of the frame size.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - Numtrials (number): Defines how many times each frame size will be tested.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - PortDownTime (number): The time interval during the port is down.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - Rfc2889ordering (str(noOrdering | unchanged | val2889Ordering)): Enables ordering.
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepIncrementFrameSize (number): The incremental step value of the frame size.
        - SupportedTrafficTypes (str): The traffic types supported.
        - Tablesize (number): The number of addresses that are to be used for the test.
        - TxDelay (number): Signifies the transmission delay time.

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
