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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


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

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def BinaryLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The load unit value in binary. Possible values include:
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryLoadUnit'])
    @BinaryLoadUnit.setter
    def BinaryLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryLoadUnit'], value)

    @property
    def BinaryResolution(self):
        """
        Returns
        -------
        - number: Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryResolution'])
    @BinaryResolution.setter
    def BinaryResolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryResolution'], value)

    @property
    def CalculateLatency(self):
        """
        Returns
        -------
        - bool: If true, calculates the latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateLatency'])
    @CalculateLatency.setter
    def CalculateLatency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CalculateLatency'], value)

    @property
    def CustomFramesizeValue(self):
        """
        Returns
        -------
        - number: Sets the custom framesize value
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomFramesizeValue'])
    @CustomFramesizeValue.setter
    def CustomFramesizeValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomFramesizeValue'], value)

    @property
    def CustomLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the custom load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomLoadUnit'])
    @CustomLoadUnit.setter
    def CustomLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomLoadUnit'], value)

    @property
    def DelayBeforeStartTransmit(self):
        """
        Returns
        -------
        - number: If true, a delay is introduced before transmission is started.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayBeforeStartTransmit'])
    @DelayBeforeStartTransmit.setter
    def DelayBeforeStartTransmit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayBeforeStartTransmit'], value)

    @property
    def DeleteFlowsAtStartup(self):
        """
        Returns
        -------
        - bool: If true, the test will delete the flowgroups at startup
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeleteFlowsAtStartup'])
    @DeleteFlowsAtStartup.setter
    def DeleteFlowsAtStartup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DeleteFlowsAtStartup'], value)

    @property
    def EnableMinFrameSize(self):
        """
        Returns
        -------
        - bool: If true, enables minimum frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'])
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'], value)

    @property
    def EnableTrafficValidation(self):
        """
        Returns
        -------
        - bool: If true, traffic validation is performed. It provides a high level view of the errors detected in each traffic item and flow group. With the help of this option you can easily identify the various categories of errors detected in each traffic item and flow group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableTrafficValidation'])
    @EnableTrafficValidation.setter
    def EnableTrafficValidation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableTrafficValidation'], value)

    @property
    def FrameSizeMode(self):
        """
        Returns
        -------
        - str(increment | random): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeMode'])
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeMode'], value)

    @property
    def Gap(self):
        """
        Returns
        -------
        - number: The gap in transmission of frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Gap'])
    @Gap.setter
    def Gap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Gap'], value)

    @property
    def InitialBinaryLoadIntegerValues(self):
        """
        Returns
        -------
        - number: Indicates the initial binary load integer values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialBinaryLoadIntegerValues'])
    @InitialBinaryLoadIntegerValues.setter
    def InitialBinaryLoadIntegerValues(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialBinaryLoadIntegerValues'], value)

    @property
    def InitialStepIntegerValues(self):
        """
        Returns
        -------
        - number: Indicates the initial step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialStepIntegerValues'])
    @InitialStepIntegerValues.setter
    def InitialStepIntegerValues(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialStepIntegerValues'], value)

    @property
    def LatencyType(self):
        """
        Returns
        -------
        - str(cutThrough | forwardingDelay | mef | storeForward): Indicate the type of latency that needs to be measured. Can be Cut-Through, Store-Forward and so on.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyType'])
    @LatencyType.setter
    def LatencyType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyType'], value)

    @property
    def LoadRateValue(self):
        """
        Returns
        -------
        - number: The value of the load rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadRateValue'])
    @LoadRateValue.setter
    def LoadRateValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadRateValue'], value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(binary | step): Indicates the load type. Can be any of the following:
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadType'])
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadType'], value)

    @property
    def MaxBinaryLoadIntegerValue(self):
        """
        Returns
        -------
        - number: Indicates the maximum load integer values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxBinaryLoadIntegerValue'])
    @MaxBinaryLoadIntegerValue.setter
    def MaxBinaryLoadIntegerValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxBinaryLoadIntegerValue'], value)

    @property
    def MaxRandomFrameSize(self):
        """
        Returns
        -------
        - number: The maximum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'])
    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'], value)

    @property
    def MaxStepIntegerValues(self):
        """
        Returns
        -------
        - number: Indicates the maximum step value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxStepIntegerValues'])
    @MaxStepIntegerValues.setter
    def MaxStepIntegerValues(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxStepIntegerValues'], value)

    @property
    def MinAddressTableSize(self):
        """
        Returns
        -------
        - number: Indicates the minimum size of the address table.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinAddressTableSize'])
    @MinAddressTableSize.setter
    def MinAddressTableSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinAddressTableSize'], value)

    @property
    def MinBinaryLoadIntegerValues(self):
        """
        Returns
        -------
        - number: Indicates the minimum binary load integer values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinBinaryLoadIntegerValues'])
    @MinBinaryLoadIntegerValues.setter
    def MinBinaryLoadIntegerValues(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinBinaryLoadIntegerValues'], value)

    @property
    def MinRandomFrameSize(self):
        """
        Returns
        -------
        - number: The minimum random frame size to be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'])
    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinRandomFrameSize'], value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: Number of trials that can be run
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def PacketsPerFlow(self):
        """
        Returns
        -------
        - number: Indicates the number of packets per flow.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketsPerFlow'])
    @PacketsPerFlow.setter
    def PacketsPerFlow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketsPerFlow'], value)

    @property
    def ProtocolItem(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan]): Protocol Items
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolItem'])
    @ProtocolItem.setter
    def ProtocolItem(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolItem'], value)

    @property
    def RangeCount(self):
        """
        Returns
        -------
        - number: Indicates the range count.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RangeCount'])
    @RangeCount.setter
    def RangeCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RangeCount'], value)

    @property
    def StepLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Specifies the step rate of the load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepLoadUnit'])
    @StepLoadUnit.setter
    def StepLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepLoadUnit'], value)

    @property
    def StepStepIntegerValues(self):
        """
        Returns
        -------
        - number: Indicates the step integer value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepStepIntegerValues'])
    @StepStepIntegerValues.setter
    def StepStepIntegerValues(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepStepIntegerValues'], value)

    @property
    def WaitAffterFlowAdd(self):
        """
        Returns
        -------
        - number: If true, the traffic is paused after flowdetection is added.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WaitAffterFlowAdd'])
    @WaitAffterFlowAdd.setter
    def WaitAffterFlowAdd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WaitAffterFlowAdd'], value)

    def update(self, BinaryLoadUnit=None, BinaryResolution=None, CalculateLatency=None, CustomFramesizeValue=None, CustomLoadUnit=None, DelayBeforeStartTransmit=None, DeleteFlowsAtStartup=None, EnableMinFrameSize=None, EnableTrafficValidation=None, FrameSizeMode=None, Gap=None, InitialBinaryLoadIntegerValues=None, InitialStepIntegerValues=None, LatencyType=None, LoadRateValue=None, LoadType=None, MaxBinaryLoadIntegerValue=None, MaxRandomFrameSize=None, MaxStepIntegerValues=None, MinAddressTableSize=None, MinBinaryLoadIntegerValues=None, MinRandomFrameSize=None, Numtrials=None, PacketsPerFlow=None, ProtocolItem=None, RangeCount=None, StepLoadUnit=None, StepStepIntegerValues=None, WaitAffterFlowAdd=None):
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

    def Apply(self):
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('apply', payload=payload, response_object=None)

    def ApplyAsync(self):
        """Executes the applyAsync operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsync', payload=payload, response_object=None)

    def ApplyAsyncResult(self):
        """Executes the applyAsyncResult operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsyncResult', payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self):
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

    def GenerateReport(self):
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('generateReport', payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(InputParameters=string)list
        -------------------------------
        - InputParameters (str): The input arguments of the test.
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
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(InputParameters=string)
        -----------------------------
        - InputParameters (str): The input arguments of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)

    def WaitForTest(self):
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('waitForTest', payload=payload, response_object=None)
