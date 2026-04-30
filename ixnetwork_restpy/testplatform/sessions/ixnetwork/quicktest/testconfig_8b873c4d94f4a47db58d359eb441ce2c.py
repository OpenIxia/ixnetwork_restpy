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
        "AddressRatePassCriteriaMode": "addressRatePassCriteriaMode",
        "AddressRatePassFailValue": "addressRatePassFailValue",
        "BinaryBackoff": "binaryBackoff",
        "BinaryLoadUnit": "binaryLoadUnit",
        "BinaryResolution": "binaryResolution",
        "BinarySearchType": "binarySearchType",
        "CacheTimeout": "cacheTimeout",
        "DelayAfterTransmit": "delayAfterTransmit",
        "EnableAddressRatePassFail": "enableAddressRatePassFail",
        "EnableCacheTimeout": "enableCacheTimeout",
        "EnableDaD": "enableDaD",
        "EnableDropLink": "enableDropLink",
        "EnableExtraIterations": "enableExtraIterations",
        "EnableMinFrameSize": "enableMinFrameSize",
        "ExtraIterationOffsets": "extraIterationOffsets",
        "FrameSizeMode": "frameSizeMode",
        "Framesize": "framesize",
        "FramesizeFixedValue": "framesizeFixedValue",
        "FramesizeList": "framesizeList",
        "InitialBinaryLoadRate": "initialBinaryLoadRate",
        "Layer3AddressCount": "layer3AddressCount",
        "LoadRateList": "loadRateList",
        "LoadType": "loadType",
        "LoadUnit": "loadUnit",
        "MapType": "mapType",
        "MaxBinaryLoadRate": "maxBinaryLoadRate",
        "MaxOutstandingRequests": "maxOutstandingRequests",
        "MinBinaryLoadRate": "minBinaryLoadRate",
        "Numtrials": "numtrials",
        "PortDelayEnabled": "portDelayEnabled",
        "PortDelayUnit": "portDelayUnit",
        "PortDelayValue": "portDelayValue",
        "PortDownTime": "portDownTime",
        "ProtocolItem": "protocolItem",
        "StaggeredStart": "staggeredStart",
        "SupportedTrafficTypes": "supportedTrafficTypes",
        "TxDelay": "txDelay",
    }
    _SDM_ENUM_MAP = {
        "addrRateValidationRateUnit": ["fps", "percentMaxRate"],
        "binaryLoadUnit": ["fpsRate"],
        "binarySearchType": ["linear"],
        "frameSizeMode": ["fixed"],
        "loadType": ["binary"],
        "loadUnit": ["fpsRate"],
        "portDelayUnit": ["bytes", "nanoseconds"],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

    @property
    def AddrRateNumFrames(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the address rate in number of frames.
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
        - str: Indicates that the step rate of the load unit is fpsRate.
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
        - number: Indicates the address rate validation rate.
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
        - str(fps | percentMaxRate): Indicates the address rate validation rate unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddrRateValidationRateUnit"])

    @AddrRateValidationRateUnit.setter
    def AddrRateValidationRateUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddrRateValidationRateUnit"], value)

    @property
    def AddressRatePassCriteriaMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the address rate pass criteria mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddressRatePassCriteriaMode"])

    @AddressRatePassCriteriaMode.setter
    def AddressRatePassCriteriaMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddressRatePassCriteriaMode"], value)

    @property
    def AddressRatePassFailValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the Address Rate value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AddressRatePassFailValue"])

    @AddressRatePassFailValue.setter
    def AddressRatePassFailValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AddressRatePassFailValue"], value)

    @property
    def BinaryBackoff(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The binary search interval through which the next iteration's rate is obtained.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryBackoff"])

    @BinaryBackoff.setter
    def BinaryBackoff(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryBackoff"], value)

    @property
    def BinaryLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fpsRate): Indicates the binary load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinaryLoadUnit"])

    @BinaryLoadUnit.setter
    def BinaryLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinaryLoadUnit"], value)

    @property
    def BinaryResolution(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the resolution during the binary search.
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
        - str(linear): Indicates the search type for a Binary search.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinarySearchType"])

    @BinarySearchType.setter
    def BinarySearchType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinarySearchType"], value)

    @property
    def CacheTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates cache time out.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CacheTimeout"])

    @CacheTimeout.setter
    def CacheTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CacheTimeout"], value)

    @property
    def DelayAfterTransmit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: A delay that is inserted after transmit is complete, before it continues with the test.
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
        - bool: If true, allows Address Rate to be used as a Pass/Fail criteria.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAddressRatePassFail"])

    @EnableAddressRatePassFail.setter
    def EnableAddressRatePassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAddressRatePassFail"], value)

    @property
    def EnableCacheTimeout(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables cache time out.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCacheTimeout"])

    @EnableCacheTimeout.setter
    def EnableCacheTimeout(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCacheTimeout"], value)

    @property
    def EnableDaD(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, a Neighbor Solicitation is sent from the interface for Duplicate Address Detection (DAD), to confirm that no other node on the link has the same address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDaD"])

    @EnableDaD.setter
    def EnableDaD(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDaD"], value)

    @property
    def EnableDropLink(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, allows Route Range to be dropped.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDropLink"])

    @EnableDropLink.setter
    def EnableDropLink(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDropLink"], value)

    @property
    def EnableExtraIterations(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables extra iterations. Sets extra iteration offset values.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableExtraIterations"])

    @EnableExtraIterations.setter
    def EnableExtraIterations(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableExtraIterations"], value)

    @property
    def EnableMinFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, allows to set minimum frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMinFrameSize"])

    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMinFrameSize"], value)

    @property
    def ExtraIterationOffsets(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets extra iteration offset values.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExtraIterationOffsets"])

    @ExtraIterationOffsets.setter
    def ExtraIterationOffsets(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExtraIterationOffsets"], value)

    @property
    def FrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fixed): Indicates the frame size mode.
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
        - str: The frame size used by the service.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Framesize"])

    @Framesize.setter
    def Framesize(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Framesize"], value)

    @property
    def FramesizeFixedValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the frame size fixed value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesizeFixedValue"])

    @FramesizeFixedValue.setter
    def FramesizeFixedValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesizeFixedValue"], value)

    @property
    def FramesizeList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The list of the available frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesizeList"])

    @FramesizeList.setter
    def FramesizeList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesizeList"], value)

    @property
    def InitialBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the initial binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitialBinaryLoadRate"])

    @InitialBinaryLoadRate.setter
    def InitialBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitialBinaryLoadRate"], value)

    @property
    def Layer3AddressCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the Layer 3 address count.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Layer3AddressCount"])

    @Layer3AddressCount.setter
    def Layer3AddressCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Layer3AddressCount"], value)

    @property
    def LoadRateList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Enter the Load Rate List.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadRateList"])

    @LoadRateList.setter
    def LoadRateList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadRateList"], value)

    @property
    def LoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(binary): Indicates the load type.
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
        - str(fpsRate): Indicates the load unit.
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
        - str: Indicates the traffic map type.
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
        - number: Indicates the maximum binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxBinaryLoadRate"])

    @MaxBinaryLoadRate.setter
    def MaxBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxBinaryLoadRate"], value)

    @property
    def MaxOutstandingRequests(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates maximum outstanding request.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxOutstandingRequests"])

    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxOutstandingRequests"], value)

    @property
    def MinBinaryLoadRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the minimum binary load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinBinaryLoadRate"])

    @MinBinaryLoadRate.setter
    def MinBinaryLoadRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinBinaryLoadRate"], value)

    @property
    def Numtrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of trials that can be run.
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
        - number: During flapping, the amount of time during which the routes in the Route Range are withdrawn/down.
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
    def StaggeredStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables a staggered start to traffic transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StaggeredStart"])

    @StaggeredStart.setter
    def StaggeredStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StaggeredStart"], value)

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
    def TxDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the amount of delay after every transmit.
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
        AddressRatePassCriteriaMode=None,
        AddressRatePassFailValue=None,
        BinaryBackoff=None,
        BinaryLoadUnit=None,
        BinaryResolution=None,
        BinarySearchType=None,
        CacheTimeout=None,
        DelayAfterTransmit=None,
        EnableAddressRatePassFail=None,
        EnableCacheTimeout=None,
        EnableDaD=None,
        EnableDropLink=None,
        EnableExtraIterations=None,
        EnableMinFrameSize=None,
        ExtraIterationOffsets=None,
        FrameSizeMode=None,
        Framesize=None,
        FramesizeFixedValue=None,
        FramesizeList=None,
        InitialBinaryLoadRate=None,
        Layer3AddressCount=None,
        LoadRateList=None,
        LoadType=None,
        LoadUnit=None,
        MapType=None,
        MaxBinaryLoadRate=None,
        MaxOutstandingRequests=None,
        MinBinaryLoadRate=None,
        Numtrials=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        PortDownTime=None,
        ProtocolItem=None,
        StaggeredStart=None,
        SupportedTrafficTypes=None,
        TxDelay=None,
    ):
        # type: (int, str, int, str, str, int, int, str, int, str, int, int, bool, bool, bool, bool, bool, bool, str, str, str, int, List[str], int, int, str, str, str, str, int, int, int, int, bool, str, int, int, List[str], bool, str, int) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - AddrRateNumFrames (number): Indicates the address rate in number of frames.
        - AddrRateValidationFpsRate (str): Indicates that the step rate of the load unit is fpsRate.
        - AddrRateValidationRate (number): Indicates the address rate validation rate.
        - AddrRateValidationRateUnit (str(fps | percentMaxRate)): Indicates the address rate validation rate unit.
        - AddressRatePassCriteriaMode (str): Indicates the address rate pass criteria mode.
        - AddressRatePassFailValue (number): Indicates the Address Rate value.
        - BinaryBackoff (number): The binary search interval through which the next iteration's rate is obtained.
        - BinaryLoadUnit (str(fpsRate)): Indicates the binary load unit.
        - BinaryResolution (number): Indicates the resolution during the binary search.
        - BinarySearchType (str(linear)): Indicates the search type for a Binary search.
        - CacheTimeout (number): Indicates cache time out.
        - DelayAfterTransmit (number): A delay that is inserted after transmit is complete, before it continues with the test.
        - EnableAddressRatePassFail (bool): If true, allows Address Rate to be used as a Pass/Fail criteria.
        - EnableCacheTimeout (bool): If true, enables cache time out.
        - EnableDaD (bool): If true, a Neighbor Solicitation is sent from the interface for Duplicate Address Detection (DAD), to confirm that no other node on the link has the same address.
        - EnableDropLink (bool): If true, allows Route Range to be dropped.
        - EnableExtraIterations (bool): If true, enables extra iterations. Sets extra iteration offset values.
        - EnableMinFrameSize (bool): If true, allows to set minimum frame size.
        - ExtraIterationOffsets (str): Sets extra iteration offset values.
        - FrameSizeMode (str(fixed)): Indicates the frame size mode.
        - Framesize (str): The frame size used by the service.
        - FramesizeFixedValue (number): It signifies the frame size fixed value.
        - FramesizeList (list(str)): The list of the available frame size.
        - InitialBinaryLoadRate (number): Indicates the initial binary load rate.
        - Layer3AddressCount (number): Indicates the Layer 3 address count.
        - LoadRateList (str): Enter the Load Rate List.
        - LoadType (str(binary)): Indicates the load type.
        - LoadUnit (str(fpsRate)): Indicates the load unit.
        - MapType (str): Indicates the traffic map type.
        - MaxBinaryLoadRate (number): Indicates the maximum binary load rate.
        - MaxOutstandingRequests (number): Indicates maximum outstanding request.
        - MinBinaryLoadRate (number): Indicates the minimum binary load rate.
        - Numtrials (number): Number of trials that can be run.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - PortDownTime (number): During flapping, the amount of time during which the routes in the Route Range are withdrawn/down.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - StaggeredStart (bool): Enables a staggered start to traffic transmit.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TxDelay (number): Specifies the amount of delay after every transmit.

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
        AddressRatePassCriteriaMode=None,
        AddressRatePassFailValue=None,
        BinaryBackoff=None,
        BinaryLoadUnit=None,
        BinaryResolution=None,
        BinarySearchType=None,
        CacheTimeout=None,
        DelayAfterTransmit=None,
        EnableAddressRatePassFail=None,
        EnableCacheTimeout=None,
        EnableDaD=None,
        EnableDropLink=None,
        EnableExtraIterations=None,
        EnableMinFrameSize=None,
        ExtraIterationOffsets=None,
        FrameSizeMode=None,
        Framesize=None,
        FramesizeFixedValue=None,
        FramesizeList=None,
        InitialBinaryLoadRate=None,
        Layer3AddressCount=None,
        LoadRateList=None,
        LoadType=None,
        LoadUnit=None,
        MapType=None,
        MaxBinaryLoadRate=None,
        MaxOutstandingRequests=None,
        MinBinaryLoadRate=None,
        Numtrials=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        PortDownTime=None,
        ProtocolItem=None,
        StaggeredStart=None,
        SupportedTrafficTypes=None,
        TxDelay=None,
    ):
        # type: (int, str, int, str, str, int, int, str, int, str, int, int, bool, bool, bool, bool, bool, bool, str, str, str, int, List[str], int, int, str, str, str, str, int, int, int, int, bool, str, int, int, List[str], bool, str, int) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - AddrRateNumFrames (number): Indicates the address rate in number of frames.
        - AddrRateValidationFpsRate (str): Indicates that the step rate of the load unit is fpsRate.
        - AddrRateValidationRate (number): Indicates the address rate validation rate.
        - AddrRateValidationRateUnit (str(fps | percentMaxRate)): Indicates the address rate validation rate unit.
        - AddressRatePassCriteriaMode (str): Indicates the address rate pass criteria mode.
        - AddressRatePassFailValue (number): Indicates the Address Rate value.
        - BinaryBackoff (number): The binary search interval through which the next iteration's rate is obtained.
        - BinaryLoadUnit (str(fpsRate)): Indicates the binary load unit.
        - BinaryResolution (number): Indicates the resolution during the binary search.
        - BinarySearchType (str(linear)): Indicates the search type for a Binary search.
        - CacheTimeout (number): Indicates cache time out.
        - DelayAfterTransmit (number): A delay that is inserted after transmit is complete, before it continues with the test.
        - EnableAddressRatePassFail (bool): If true, allows Address Rate to be used as a Pass/Fail criteria.
        - EnableCacheTimeout (bool): If true, enables cache time out.
        - EnableDaD (bool): If true, a Neighbor Solicitation is sent from the interface for Duplicate Address Detection (DAD), to confirm that no other node on the link has the same address.
        - EnableDropLink (bool): If true, allows Route Range to be dropped.
        - EnableExtraIterations (bool): If true, enables extra iterations. Sets extra iteration offset values.
        - EnableMinFrameSize (bool): If true, allows to set minimum frame size.
        - ExtraIterationOffsets (str): Sets extra iteration offset values.
        - FrameSizeMode (str(fixed)): Indicates the frame size mode.
        - Framesize (str): The frame size used by the service.
        - FramesizeFixedValue (number): It signifies the frame size fixed value.
        - FramesizeList (list(str)): The list of the available frame size.
        - InitialBinaryLoadRate (number): Indicates the initial binary load rate.
        - Layer3AddressCount (number): Indicates the Layer 3 address count.
        - LoadRateList (str): Enter the Load Rate List.
        - LoadType (str(binary)): Indicates the load type.
        - LoadUnit (str(fpsRate)): Indicates the load unit.
        - MapType (str): Indicates the traffic map type.
        - MaxBinaryLoadRate (number): Indicates the maximum binary load rate.
        - MaxOutstandingRequests (number): Indicates maximum outstanding request.
        - MinBinaryLoadRate (number): Indicates the minimum binary load rate.
        - Numtrials (number): Number of trials that can be run.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured.
        - PortDelayValue (number): Sets the port delay value.
        - PortDownTime (number): During flapping, the amount of time during which the routes in the Route Range are withdrawn/down.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - StaggeredStart (bool): Enables a staggered start to traffic transmit.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TxDelay (number): Specifies the amount of delay after every transmit.

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
