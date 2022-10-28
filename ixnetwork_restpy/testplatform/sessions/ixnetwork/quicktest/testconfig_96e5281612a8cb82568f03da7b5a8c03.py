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
        "BidirectionalOptionEnabled": "bidirectionalOptionEnabled",
        "BinarySearchType": "binarySearchType",
        "BurstSize": "burstSize",
        "CountRandomFrameSize": "countRandomFrameSize",
        "DelayAfterTransmit": "delayAfterTransmit",
        "Duration": "duration",
        "EnableAlignmentErr": "enableAlignmentErr",
        "EnableBadCrcErr": "enableBadCrcErr",
        "EnableDribbleErr": "enableDribbleErr",
        "EnableFragmentErr": "enableFragmentErr",
        "EnableMinFrameSize": "enableMinFrameSize",
        "EnableOversizeErr": "enableOversizeErr",
        "EnableUndersizeErr": "enableUndersizeErr",
        "EnforceBidirectional": "enforceBidirectional",
        "ForceRegenerate": "forceRegenerate",
        "FragmentFramesizeList": "fragmentFramesizeList",
        "FrameSizeMode": "frameSizeMode",
        "FramesizeList": "framesizeList",
        "LoadRatePercent": "loadRatePercent",
        "LoadType": "loadType",
        "MapType": "mapType",
        "MaxIncrementFrameSize": "maxIncrementFrameSize",
        "MaxRandomFrameSize": "maxRandomFrameSize",
        "MinIncrementFrameSize": "minIncrementFrameSize",
        "MinRandomFrameSize": "minRandomFrameSize",
        "Numtrials": "numtrials",
        "OversizeFramesizeList": "oversizeFramesizeList",
        "PassFailNote": "passFailNote",
        "PortDelayEnabled": "portDelayEnabled",
        "PortDelayUnit": "portDelayUnit",
        "PortDelayValue": "portDelayValue",
        "ProtocolItem": "protocolItem",
        "SendFullyMeshed": "sendFullyMeshed",
        "StepIncrementFrameSize": "stepIncrementFrameSize",
        "SupportedTrafficTypes": "supportedTrafficTypes",
        "TrafficType": "trafficType",
        "TxDelay": "txDelay",
        "UndersizeFramesizeList": "undersizeFramesizeList",
    }
    _SDM_ENUM_MAP = {
        "binarySearchType": ["linear", "perFlow", "perPort"],
        "frameSizeMode": ["custom", "increment", "random"],
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
        "portDelayUnit": ["bytes", "nanoseconds"],
        "trafficType": ["burstyLoading", "constantLoading"],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

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
    def BinarySearchType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(linear | perFlow | perPort): The binary search type value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BinarySearchType"])

    @BinarySearchType.setter
    def BinarySearchType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BinarySearchType"], value)

    @property
    def BurstSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of packets that are sent in a burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BurstSize"])

    @BurstSize.setter
    def BurstSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BurstSize"], value)

    @property
    def CountRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, frame sizes are counted at random.
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
        - number: A delay that is inserted after transmit is complete, before it continues with the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"])

    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DelayAfterTransmit"], value)

    @property
    def Duration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The duration of the test in hours, which is used to calculate the number of frames to transmit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Duration"])

    @Duration.setter
    def Duration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Duration"], value)

    @property
    def EnableAlignmentErr(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, alignment error is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAlignmentErr"])

    @EnableAlignmentErr.setter
    def EnableAlignmentErr(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAlignmentErr"], value)

    @property
    def EnableBadCrcErr(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, BadCrc error is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableBadCrcErr"])

    @EnableBadCrcErr.setter
    def EnableBadCrcErr(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableBadCrcErr"], value)

    @property
    def EnableDribbleErr(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, dribble error. is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDribbleErr"])

    @EnableDribbleErr.setter
    def EnableDribbleErr(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDribbleErr"], value)

    @property
    def EnableFragmentErr(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, fragment error is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableFragmentErr"])

    @EnableFragmentErr.setter
    def EnableFragmentErr(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableFragmentErr"], value)

    @property
    def EnableMinFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, IxNetwork will allow the stream to use smaller packet sizes. In the case of IPv4 and Ethernet, 64 bytes will be allowed. This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMinFrameSize"])

    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMinFrameSize"], value)

    @property
    def EnableOversizeErr(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, oversize error is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOversizeErr"])

    @EnableOversizeErr.setter
    def EnableOversizeErr(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOversizeErr"], value)

    @property
    def EnableUndersizeErr(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, oversize error is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableUndersizeErr"])

    @EnableUndersizeErr.setter
    def EnableUndersizeErr(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableUndersizeErr"], value)

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
    def ForceRegenerate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Initiates a forced regeneration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForceRegenerate"])

    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForceRegenerate"], value)

    @property
    def FragmentFramesizeList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The list of fragmented framesize.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FragmentFramesizeList"])

    @FragmentFramesizeList.setter
    def FragmentFramesizeList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FragmentFramesizeList"], value)

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
    def LoadRatePercent(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The percent value of Load Rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadRatePercent"])

    @LoadRatePercent.setter
    def LoadRatePercent(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadRatePercent"], value)

    @property
    def LoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged): The type of the payload setting.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoadType"])

    @LoadType.setter
    def LoadType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoadType"], value)

    @property
    def MapType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The POS traffic map type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapType"])

    @MapType.setter
    def MapType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapType"], value)

    @property
    def MaxIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The integer that states the maximum amount to which the frame size can be incremented.
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
        - number: The integer that states the maximum random amount to which the frame size can be incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxRandomFrameSize"])

    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxRandomFrameSize"], value)

    @property
    def MinIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The integer that states the minimum amount to which the frame size can be incremented.
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
        - number: The integer that states the minimum random amount to which the frame size can be incremented.
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
    def OversizeFramesizeList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The list of oversized framesize.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OversizeFramesizeList"])

    @OversizeFramesizeList.setter
    def OversizeFramesizeList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OversizeFramesizeList"], value)

    @property
    def PassFailNote(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The note that indicates whether the test has cleared the pass/fail criterion or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PassFailNote"])

    @PassFailNote.setter
    def PassFailNote(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PassFailNote"], value)

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
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured
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
        - number: Sets the port delay value
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDelayValue"])

    @PortDelayValue.setter
    def PortDelayValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDelayValue"], value)

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
    def SendFullyMeshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sending fully meshed traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendFullyMeshed"])

    @SendFullyMeshed.setter
    def SendFullyMeshed(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendFullyMeshed"], value)

    @property
    def StepIncrementFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The step to increment the frame size.
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
    def TrafficType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(burstyLoading | constantLoading): The test based on the traffic type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficType"])

    @TrafficType.setter
    def TrafficType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficType"], value)

    @property
    def TxDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum delay between successive LLDP packets. The default value is 2, the minimum is 1, and the maximum is 8192. Note that Tx Delay must be lower than txInterval.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxDelay"])

    @TxDelay.setter
    def TxDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxDelay"], value)

    @property
    def UndersizeFramesizeList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The list of undersized framesize.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UndersizeFramesizeList"])

    @UndersizeFramesizeList.setter
    def UndersizeFramesizeList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UndersizeFramesizeList"], value)

    def update(
        self,
        BidirectionalOptionEnabled=None,
        BinarySearchType=None,
        BurstSize=None,
        CountRandomFrameSize=None,
        DelayAfterTransmit=None,
        Duration=None,
        EnableAlignmentErr=None,
        EnableBadCrcErr=None,
        EnableDribbleErr=None,
        EnableFragmentErr=None,
        EnableMinFrameSize=None,
        EnableOversizeErr=None,
        EnableUndersizeErr=None,
        EnforceBidirectional=None,
        ForceRegenerate=None,
        FragmentFramesizeList=None,
        FrameSizeMode=None,
        FramesizeList=None,
        LoadRatePercent=None,
        LoadType=None,
        MapType=None,
        MaxIncrementFrameSize=None,
        MaxRandomFrameSize=None,
        MinIncrementFrameSize=None,
        MinRandomFrameSize=None,
        Numtrials=None,
        OversizeFramesizeList=None,
        PassFailNote=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        ProtocolItem=None,
        SendFullyMeshed=None,
        StepIncrementFrameSize=None,
        SupportedTrafficTypes=None,
        TrafficType=None,
        TxDelay=None,
        UndersizeFramesizeList=None,
    ):
        # type: (bool, str, int, int, int, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, List[str], int, str, str, int, int, int, int, int, str, str, bool, str, int, List[str], bool, int, str, str, int, str) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - BidirectionalOptionEnabled (bool): If true, allows bidirectional traffic.
        - BinarySearchType (str(linear | perFlow | perPort)): The binary search type value.
        - BurstSize (number): The number of packets that are sent in a burst.
        - CountRandomFrameSize (number): If true, frame sizes are counted at random.
        - DelayAfterTransmit (number): A delay that is inserted after transmit is complete, before it continues with the test.
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - EnableAlignmentErr (bool): If true, alignment error is enabled.
        - EnableBadCrcErr (bool): If true, BadCrc error is enabled.
        - EnableDribbleErr (bool): If true, dribble error. is enabled.
        - EnableFragmentErr (bool): If true, fragment error is enabled.
        - EnableMinFrameSize (bool): If true, IxNetwork will allow the stream to use smaller packet sizes. In the case of IPv4 and Ethernet, 64 bytes will be allowed. This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.
        - EnableOversizeErr (bool): If true, oversize error is enabled.
        - EnableUndersizeErr (bool): If true, oversize error is enabled.
        - EnforceBidirectional (bool): If true, uses bidirectional traffic mapping.
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FragmentFramesizeList (str): The list of fragmented framesize.
        - FrameSizeMode (str(custom | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - FramesizeList (list(str)): List containing the frame sizes used in the test.
        - LoadRatePercent (number): The percent value of Load Rate.
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)): The type of the payload setting.
        - MapType (str): The POS traffic map type.
        - MaxIncrementFrameSize (number): The integer that states the maximum amount to which the frame size can be incremented.
        - MaxRandomFrameSize (number): The integer that states the maximum random amount to which the frame size can be incremented.
        - MinIncrementFrameSize (number): The integer that states the minimum amount to which the frame size can be incremented.
        - MinRandomFrameSize (number): The integer that states the minimum random amount to which the frame size can be incremented.
        - Numtrials (number): Defines how many times each frame size will be tested.
        - OversizeFramesizeList (str): The list of oversized framesize.
        - PassFailNote (str): The note that indicates whether the test has cleared the pass/fail criterion or not.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - SendFullyMeshed (bool): Sending fully meshed traffic.
        - StepIncrementFrameSize (number): The step to increment the frame size.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TrafficType (str(burstyLoading | constantLoading)): The test based on the traffic type.
        - TxDelay (number): The minimum delay between successive LLDP packets. The default value is 2, the minimum is 1, and the maximum is 8192. Note that Tx Delay must be lower than txInterval.
        - UndersizeFramesizeList (str): The list of undersized framesize.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BidirectionalOptionEnabled=None,
        BinarySearchType=None,
        BurstSize=None,
        CountRandomFrameSize=None,
        DelayAfterTransmit=None,
        Duration=None,
        EnableAlignmentErr=None,
        EnableBadCrcErr=None,
        EnableDribbleErr=None,
        EnableFragmentErr=None,
        EnableMinFrameSize=None,
        EnableOversizeErr=None,
        EnableUndersizeErr=None,
        EnforceBidirectional=None,
        ForceRegenerate=None,
        FragmentFramesizeList=None,
        FrameSizeMode=None,
        FramesizeList=None,
        LoadRatePercent=None,
        LoadType=None,
        MapType=None,
        MaxIncrementFrameSize=None,
        MaxRandomFrameSize=None,
        MinIncrementFrameSize=None,
        MinRandomFrameSize=None,
        Numtrials=None,
        OversizeFramesizeList=None,
        PassFailNote=None,
        PortDelayEnabled=None,
        PortDelayUnit=None,
        PortDelayValue=None,
        ProtocolItem=None,
        SendFullyMeshed=None,
        StepIncrementFrameSize=None,
        SupportedTrafficTypes=None,
        TrafficType=None,
        TxDelay=None,
        UndersizeFramesizeList=None,
    ):
        # type: (bool, str, int, int, int, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, List[str], int, str, str, int, int, int, int, int, str, str, bool, str, int, List[str], bool, int, str, str, int, str) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - BidirectionalOptionEnabled (bool): If true, allows bidirectional traffic.
        - BinarySearchType (str(linear | perFlow | perPort)): The binary search type value.
        - BurstSize (number): The number of packets that are sent in a burst.
        - CountRandomFrameSize (number): If true, frame sizes are counted at random.
        - DelayAfterTransmit (number): A delay that is inserted after transmit is complete, before it continues with the test.
        - Duration (number): The duration of the test in hours, which is used to calculate the number of frames to transmit.
        - EnableAlignmentErr (bool): If true, alignment error is enabled.
        - EnableBadCrcErr (bool): If true, BadCrc error is enabled.
        - EnableDribbleErr (bool): If true, dribble error. is enabled.
        - EnableFragmentErr (bool): If true, fragment error is enabled.
        - EnableMinFrameSize (bool): If true, IxNetwork will allow the stream to use smaller packet sizes. In the case of IPv4 and Ethernet, 64 bytes will be allowed. This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.
        - EnableOversizeErr (bool): If true, oversize error is enabled.
        - EnableUndersizeErr (bool): If true, oversize error is enabled.
        - EnforceBidirectional (bool): If true, uses bidirectional traffic mapping.
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FragmentFramesizeList (str): The list of fragmented framesize.
        - FrameSizeMode (str(custom | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - FramesizeList (list(str)): List containing the frame sizes used in the test.
        - LoadRatePercent (number): The percent value of Load Rate.
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)): The type of the payload setting.
        - MapType (str): The POS traffic map type.
        - MaxIncrementFrameSize (number): The integer that states the maximum amount to which the frame size can be incremented.
        - MaxRandomFrameSize (number): The integer that states the maximum random amount to which the frame size can be incremented.
        - MinIncrementFrameSize (number): The integer that states the minimum amount to which the frame size can be incremented.
        - MinRandomFrameSize (number): The integer that states the minimum random amount to which the frame size can be incremented.
        - Numtrials (number): Defines how many times each frame size will be tested.
        - OversizeFramesizeList (str): The list of oversized framesize.
        - PassFailNote (str): The note that indicates whether the test has cleared the pass/fail criterion or not.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/protocols/static/lan])): Protocol Items
        - SendFullyMeshed (bool): Sending fully meshed traffic.
        - StepIncrementFrameSize (number): The step to increment the frame size.
        - SupportedTrafficTypes (str): The traffic types supported.
        - TrafficType (str(burstyLoading | constantLoading)): The test based on the traffic type.
        - TxDelay (number): The minimum delay between successive LLDP packets. The default value is 2, the minimum is 1, and the maximum is 8192. Note that Tx Delay must be lower than txInterval.
        - UndersizeFramesizeList (str): The list of undersized framesize.

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
