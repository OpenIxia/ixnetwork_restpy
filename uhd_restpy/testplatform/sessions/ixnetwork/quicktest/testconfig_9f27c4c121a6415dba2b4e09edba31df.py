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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class TestConfig(Base):
    """The IxNetwork Test Configuration feature provides the ability to run predefined tests and allows the user to set some global test parameters for the individual test types.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'BinaryLoadUnit': 'binaryLoadUnit',
        'BinaryResolution': 'binaryResolution',
        'CalculateLatency': 'calculateLatency',
        'CustomFramesizeValue': 'customFramesizeValue',
        'CustomLoadUnit': 'customLoadUnit',
        'DelayBeforeStartTransmit': 'delayBeforeStartTransmit',
        'DeleteFlowsAtStartup': 'deleteFlowsAtStartup',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableTrafficValidation': 'enableTrafficValidation',
        'FrameSizeMode': 'frameSizeMode',
        'Gap': 'gap',
        'InitialBinaryLoadIntegerValues': 'initialBinaryLoadIntegerValues',
        'InitialStepIntegerValues': 'initialStepIntegerValues',
        'LatencyType': 'latencyType',
        'LoadRateValue': 'loadRateValue',
        'LoadType': 'loadType',
        'MaxBinaryLoadIntegerValue': 'maxBinaryLoadIntegerValue',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MaxStepIntegerValues': 'maxStepIntegerValues',
        'MinAddressTableSize': 'minAddressTableSize',
        'MinBinaryLoadIntegerValues': 'minBinaryLoadIntegerValues',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'Numtrials': 'numtrials',
        'PacketsPerFlow': 'packetsPerFlow',
        'ProtocolItem': 'protocolItem',
        'RangeCount': 'rangeCount',
        'StepLoadUnit': 'stepLoadUnit',
        'StepStepIntegerValues': 'stepStepIntegerValues',
        'WaitAffterFlowAdd': 'waitAffterFlowAdd',
    }
    _SDM_ENUM_MAP = {
        'binaryLoadUnit': ['bpsRate', 'fpsRate', 'gbpsRate', 'gBpsRate', 'kbpsRate', 'kBpsRate', 'mbpsRate', 'mBpsRate', 'percentMaxRate'],
        'customLoadUnit': ['bpsRate', 'fpsRate', 'gbpsRate', 'gBpsRate', 'kbpsRate', 'kBpsRate', 'mbpsRate', 'mBpsRate', 'percentMaxRate'],
        'frameSizeMode': ['increment', 'random'],
        'latencyType': ['cutThrough', 'forwardingDelay', 'mef', 'storeForward'],
        'loadType': ['binary', 'step'],
        'stepLoadUnit': ['bpsRate', 'fpsRate', 'gbpsRate', 'gBpsRate', 'kbpsRate', 'kBpsRate', 'mbpsRate', 'mBpsRate', 'percentMaxRate'],
    }

    def __init__(self, parent, list_op=False):
        super(TestConfig, self).__init__(parent, list_op)

    @property
    def BinaryLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The load unit value in binary. Possible values include:
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryLoadUnit'])
    @BinaryLoadUnit.setter
    def BinaryLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['BinaryLoadUnit'], value)

    @property
    def BinaryResolution(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryResolution'])
    @BinaryResolution.setter
    def BinaryResolution(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['BinaryResolution'], value)

    @property
    def CalculateLatency(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, calculates the latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateLatency'])
    @CalculateLatency.setter
    def CalculateLatency(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CalculateLatency'], value)

    @property
    def CustomFramesizeValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the custom framesize value
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomFramesizeValue'])
    @CustomFramesizeValue.setter
    def CustomFramesizeValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['CustomFramesizeValue'], value)

    @property
    def CustomLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the custom load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomLoadUnit'])
    @CustomLoadUnit.setter
    def CustomLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CustomLoadUnit'], value)

    @property
    def DelayBeforeStartTransmit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, a delay is introduced before transmission is started.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayBeforeStartTransmit'])
    @DelayBeforeStartTransmit.setter
    def DelayBeforeStartTransmit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['DelayBeforeStartTransmit'], value)

    @property
    def DeleteFlowsAtStartup(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the test will delete the flowgroups at startup
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeleteFlowsAtStartup'])
    @DeleteFlowsAtStartup.setter
    def DeleteFlowsAtStartup(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['DeleteFlowsAtStartup'], value)

    @property
    def EnableMinFrameSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables minimum frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'])
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'], value)

    @property
    def EnableTrafficValidation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, traffic validation is performed. It provides a high level view of the errors detected in each traffic item and flow group. With the help of this option you can easily identify the various categories of errors detected in each traffic item and flow group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableTrafficValidation'])
    @EnableTrafficValidation.setter
    def EnableTrafficValidation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableTrafficValidation'], value)

    @property
    def FrameSizeMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(increment | random): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeMode'])
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeMode'], value)

    @property
    def Gap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The gap in transmission of frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gap'])
    @Gap.setter
    def Gap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Gap'], value)

    @property
    def InitialBinaryLoadIntegerValues(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the initial binary load integer values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialBinaryLoadIntegerValues'])
    @InitialBinaryLoadIntegerValues.setter
    def InitialBinaryLoadIntegerValues(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['InitialBinaryLoadIntegerValues'], value)

    @property
    def InitialStepIntegerValues(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the initial step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialStepIntegerValues'])
    @InitialStepIntegerValues.setter
    def InitialStepIntegerValues(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['InitialStepIntegerValues'], value)

    @property
    def LatencyType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cutThrough | forwardingDelay | mef | storeForward): Indicate the type of latency that needs to be measured. Can be Cut-Through, Store-Forward and so on.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyType'])
    @LatencyType.setter
    def LatencyType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LatencyType'], value)

    @property
    def LoadRateValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadRateValue'])
    @LoadRateValue.setter
    def LoadRateValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['LoadRateValue'], value)

    @property
    def LoadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(binary | step): Indicates the load type. Can be any of the following:
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadType'])
    @LoadType.setter
    def LoadType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LoadType'], value)

    @property
    def MaxBinaryLoadIntegerValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the maximum load integer values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxBinaryLoadIntegerValue'])
    @MaxBinaryLoadIntegerValue.setter
    def MaxBinaryLoadIntegerValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxBinaryLoadIntegerValue'], value)

    @property
    def MaxRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'])
    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'], value)

    @property
    def MaxStepIntegerValues(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the maximum step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxStepIntegerValues'])
    @MaxStepIntegerValues.setter
    def MaxStepIntegerValues(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxStepIntegerValues'], value)

    @property
    def MinAddressTableSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the minimum size of the address table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinAddressTableSize'])
    @MinAddressTableSize.setter
    def MinAddressTableSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinAddressTableSize'], value)

    @property
    def MinBinaryLoadIntegerValues(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the minimum binary load integer values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinBinaryLoadIntegerValues'])
    @MinBinaryLoadIntegerValues.setter
    def MinBinaryLoadIntegerValues(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinBinaryLoadIntegerValues'], value)

    @property
    def MinRandomFrameSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'])
    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'], value)

    @property
    def Numtrials(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of trials that can be run
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def PacketsPerFlow(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the number of packets per flow.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketsPerFlow'])
    @PacketsPerFlow.setter
    def PacketsPerFlow(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PacketsPerFlow'], value)

    @property
    def ProtocolItem(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan]): Protocol Items
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolItem'])
    @ProtocolItem.setter
    def ProtocolItem(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['ProtocolItem'], value)

    @property
    def RangeCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the range count.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RangeCount'])
    @RangeCount.setter
    def RangeCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['RangeCount'], value)

    @property
    def StepLoadUnit(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the step rate of the load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepLoadUnit'])
    @StepLoadUnit.setter
    def StepLoadUnit(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['StepLoadUnit'], value)

    @property
    def StepStepIntegerValues(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the step integer value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepStepIntegerValues'])
    @StepStepIntegerValues.setter
    def StepStepIntegerValues(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['StepStepIntegerValues'], value)

    @property
    def WaitAffterFlowAdd(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, the traffic is paused after flowdetection is added.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WaitAffterFlowAdd'])
    @WaitAffterFlowAdd.setter
    def WaitAffterFlowAdd(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['WaitAffterFlowAdd'], value)

    def update(self, BinaryLoadUnit=None, BinaryResolution=None, CalculateLatency=None, CustomFramesizeValue=None, CustomLoadUnit=None, DelayBeforeStartTransmit=None, DeleteFlowsAtStartup=None, EnableMinFrameSize=None, EnableTrafficValidation=None, FrameSizeMode=None, Gap=None, InitialBinaryLoadIntegerValues=None, InitialStepIntegerValues=None, LatencyType=None, LoadRateValue=None, LoadType=None, MaxBinaryLoadIntegerValue=None, MaxRandomFrameSize=None, MaxStepIntegerValues=None, MinAddressTableSize=None, MinBinaryLoadIntegerValues=None, MinRandomFrameSize=None, Numtrials=None, PacketsPerFlow=None, ProtocolItem=None, RangeCount=None, StepLoadUnit=None, StepStepIntegerValues=None, WaitAffterFlowAdd=None):
        # type: (str, int, bool, int, str, int, bool, bool, bool, str, int, int, int, str, int, str, int, int, int, int, int, int, int, int, List[str], int, str, int, int) -> TestConfig
        """Updates testConfig resource on the server.

        Args
        ----
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The load unit value in binary. Possible values include:
        - BinaryResolution (number): Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops
        - CalculateLatency (bool): If true, calculates the latency.
        - CustomFramesizeValue (number): Sets the custom framesize value
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the custom load unit.
        - DelayBeforeStartTransmit (number): If true, a delay is introduced before transmission is started.
        - DeleteFlowsAtStartup (bool): If true, the test will delete the flowgroups at startup
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableTrafficValidation (bool): If true, traffic validation is performed. It provides a high level view of the errors detected in each traffic item and flow group. With the help of this option you can easily identify the various categories of errors detected in each traffic item and flow group.
        - FrameSizeMode (str(increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - Gap (number): The gap in transmission of frames.
        - InitialBinaryLoadIntegerValues (number): Indicates the initial binary load integer values.
        - InitialStepIntegerValues (number): Indicates the initial step value.
        - LatencyType (str(cutThrough | forwardingDelay | mef | storeForward)): Indicate the type of latency that needs to be measured. Can be Cut-Through, Store-Forward and so on.
        - LoadRateValue (number): The value of the load rate.
        - LoadType (str(binary | step)): Indicates the load type. Can be any of the following:
        - MaxBinaryLoadIntegerValue (number): Indicates the maximum load integer values.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxStepIntegerValues (number): Indicates the maximum step value.
        - MinAddressTableSize (number): Indicates the minimum size of the address table.
        - MinBinaryLoadIntegerValues (number): Indicates the minimum binary load integer values.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - Numtrials (number): Number of trials that can be run
        - PacketsPerFlow (number): Indicates the number of packets per flow.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - RangeCount (number): Indicates the range count.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the step rate of the load unit.
        - StepStepIntegerValues (number): Indicates the step integer value.
        - WaitAffterFlowAdd (number): If true, the traffic is paused after flowdetection is added.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, BinaryLoadUnit=None, BinaryResolution=None, CalculateLatency=None, CustomFramesizeValue=None, CustomLoadUnit=None, DelayBeforeStartTransmit=None, DeleteFlowsAtStartup=None, EnableMinFrameSize=None, EnableTrafficValidation=None, FrameSizeMode=None, Gap=None, InitialBinaryLoadIntegerValues=None, InitialStepIntegerValues=None, LatencyType=None, LoadRateValue=None, LoadType=None, MaxBinaryLoadIntegerValue=None, MaxRandomFrameSize=None, MaxStepIntegerValues=None, MinAddressTableSize=None, MinBinaryLoadIntegerValues=None, MinRandomFrameSize=None, Numtrials=None, PacketsPerFlow=None, ProtocolItem=None, RangeCount=None, StepLoadUnit=None, StepStepIntegerValues=None, WaitAffterFlowAdd=None):
        # type: (str, int, bool, int, str, int, bool, bool, bool, str, int, int, int, str, int, str, int, int, int, int, int, int, int, int, List[str], int, str, int, int) -> TestConfig
        """Finds and retrieves testConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testConfig resources from the server.

        Args
        ----
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The load unit value in binary. Possible values include:
        - BinaryResolution (number): Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops
        - CalculateLatency (bool): If true, calculates the latency.
        - CustomFramesizeValue (number): Sets the custom framesize value
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the custom load unit.
        - DelayBeforeStartTransmit (number): If true, a delay is introduced before transmission is started.
        - DeleteFlowsAtStartup (bool): If true, the test will delete the flowgroups at startup
        - EnableMinFrameSize (bool): If true, enables minimum frame size.
        - EnableTrafficValidation (bool): If true, traffic validation is performed. It provides a high level view of the errors detected in each traffic item and flow group. With the help of this option you can easily identify the various categories of errors detected in each traffic item and flow group.
        - FrameSizeMode (str(increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - Gap (number): The gap in transmission of frames.
        - InitialBinaryLoadIntegerValues (number): Indicates the initial binary load integer values.
        - InitialStepIntegerValues (number): Indicates the initial step value.
        - LatencyType (str(cutThrough | forwardingDelay | mef | storeForward)): Indicate the type of latency that needs to be measured. Can be Cut-Through, Store-Forward and so on.
        - LoadRateValue (number): The value of the load rate.
        - LoadType (str(binary | step)): Indicates the load type. Can be any of the following:
        - MaxBinaryLoadIntegerValue (number): Indicates the maximum load integer values.
        - MaxRandomFrameSize (number): The maximum random frame size to be sent.
        - MaxStepIntegerValues (number): Indicates the maximum step value.
        - MinAddressTableSize (number): Indicates the minimum size of the address table.
        - MinBinaryLoadIntegerValues (number): Indicates the minimum binary load integer values.
        - MinRandomFrameSize (number): The minimum random frame size to be sent.
        - Numtrials (number): Number of trials that can be run
        - PacketsPerFlow (number): Indicates the number of packets per flow.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - RangeCount (number): Indicates the range count.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Specifies the step rate of the load unit.
        - StepStepIntegerValues (number): Indicates the step integer value.
        - WaitAffterFlowAdd (number): If true, the traffic is paused after flowdetection is added.

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('apply', payload=payload, response_object=None)

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyAsync', payload=payload, response_object=None)

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyAsyncResult', payload=payload, response_object=None)

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('generateReport', payload=payload, response_object=None)

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('run', payload=payload, response_object=None)

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('waitForTest', payload=payload, response_object=None)
