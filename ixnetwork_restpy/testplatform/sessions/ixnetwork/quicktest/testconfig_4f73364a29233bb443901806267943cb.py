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
        'AmountOfTraffic': 'amountOfTraffic',
        'BurstSize': 'burstSize',
        'CongestNumFrames': 'congestNumFrames',
        'CountRandomFrameSize': 'countRandomFrameSize',
        'CustomLoadUnit': 'customLoadUnit',
        'DelayAfterTransmit': 'delayAfterTransmit',
        'Duration': 'duration',
        'EnableBpPassFail': 'enableBpPassFail',
        'EnableHolbPassFail': 'enableHolbPassFail',
        'EnableMinFrameSize': 'enableMinFrameSize',
        'EnableOldStatsForReef': 'enableOldStatsForReef',
        'ForceRegenerate': 'forceRegenerate',
        'FrameSizeMode': 'frameSizeMode',
        'Framesize': 'framesize',
        'FramesizeList': 'framesizeList',
        'LoadRateList': 'loadRateList',
        'LoadType': 'loadType',
        'MapType': 'mapType',
        'MaxIncrementFrameSize': 'maxIncrementFrameSize',
        'MaxRandomFrameSize': 'maxRandomFrameSize',
        'MinFpsRate': 'minFpsRate',
        'MinIncrementFrameSize': 'minIncrementFrameSize',
        'MinKbpsRate': 'minKbpsRate',
        'MinRandomFrameSize': 'minRandomFrameSize',
        'Numtrials': 'numtrials',
        'PercentMaxRate': 'percentMaxRate',
        'PortDelayEnabled': 'portDelayEnabled',
        'PortDelayUnit': 'portDelayUnit',
        'PortDelayValue': 'portDelayValue',
        'ProtocolItem': 'protocolItem',
        'RateSelect': 'rateSelect',
        'ReportSequenceError': 'reportSequenceError',
        'Resolution': 'resolution',
        'StaggeredStart': 'staggeredStart',
        'StepIncrementFrameSize': 'stepIncrementFrameSize',
        'SupportedTrafficTypes': 'supportedTrafficTypes',
        'Tolerance': 'tolerance',
        'TrafficType': 'trafficType',
        'TxDelay': 'txDelay',
        'UsePercentOffsets': 'usePercentOffsets',
    }

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def AmountOfTraffic(self):
        """
        Returns
        -------
        - str(duration | numFrames): The amount of traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AmountOfTraffic'])
    @AmountOfTraffic.setter
    def AmountOfTraffic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AmountOfTraffic'], value)

    @property
    def BurstSize(self):
        """
        Returns
        -------
        - number: The number of packets that are sent in a burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurstSize'])
    @BurstSize.setter
    def BurstSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BurstSize'], value)

    @property
    def CongestNumFrames(self):
        """
        Returns
        -------
        - number: The number of frames that are congested.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CongestNumFrames'])
    @CongestNumFrames.setter
    def CongestNumFrames(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CongestNumFrames'], value)

    @property
    def CountRandomFrameSize(self):
        """
        Returns
        -------
        - number: If true, frame sizes are counted at random.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'])
    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountRandomFrameSize'], value)

    @property
    def CustomLoadUnit(self):
        """
        Returns
        -------
        - str(percentMaxRate): Specifies the custom load unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomLoadUnit'])
    @CustomLoadUnit.setter
    def CustomLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomLoadUnit'], value)

    @property
    def DelayAfterTransmit(self):
        """
        Returns
        -------
        - number: A delay that is inserted after transmit is complete, before it continues with the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'])
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DelayAfterTransmit'], value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: sec
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])
    @Duration.setter
    def Duration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Duration'], value)

    @property
    def EnableBpPassFail(self):
        """
        Returns
        -------
        - bool: If true, BP Pass/Fail criterion is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBpPassFail'])
    @EnableBpPassFail.setter
    def EnableBpPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBpPassFail'], value)

    @property
    def EnableHolbPassFail(self):
        """
        Returns
        -------
        - bool: If true, HOLB Pass/Fail criterion is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHolbPassFail'])
    @EnableHolbPassFail.setter
    def EnableHolbPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHolbPassFail'], value)

    @property
    def EnableMinFrameSize(self):
        """
        Returns
        -------
        - bool: If true, IxNetwork will allow the stream to use smaller packet sizes. In the case of IPv4 and Ethernet, 64 bytes will be allowed. This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'])
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMinFrameSize'], value)

    @property
    def EnableOldStatsForReef(self):
        """
        Returns
        -------
        - bool: If true, allows to get the old statistics for reef load module.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableOldStatsForReef'])
    @EnableOldStatsForReef.setter
    def EnableOldStatsForReef(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableOldStatsForReef'], value)

    @property
    def ForceRegenerate(self):
        """
        Returns
        -------
        - bool: Initiates a forced regeneration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceRegenerate'])
    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForceRegenerate'], value)

    @property
    def FrameSizeMode(self):
        """
        Returns
        -------
        - str(custom | fixed | increment | random): This attribute is the frame size mode for the Quad Gaussian.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeMode'])
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeMode'], value)

    @property
    def Framesize(self):
        """
        Returns
        -------
        - number: Bytes
        """
        return self._get_attribute(self._SDM_ATT_MAP['Framesize'])
    @Framesize.setter
    def Framesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Framesize'], value)

    @property
    def FramesizeList(self):
        """
        Returns
        -------
        - list(str): List containing the frame sizes used in the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FramesizeList'])
    @FramesizeList.setter
    def FramesizeList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FramesizeList'], value)

    @property
    def LoadRateList(self):
        """
        Returns
        -------
        - str: The rate list of the load item.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadRateList'])
    @LoadRateList.setter
    def LoadRateList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadRateList'], value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(custom): The type of the payload setting.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadType'])
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadType'], value)

    @property
    def MapType(self):
        """
        Returns
        -------
        - str: The POS traffic map type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MapType'])
    @MapType.setter
    def MapType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MapType'], value)

    @property
    def MaxIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The integer that states the maximum amount to which the frame size can be incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'])
    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxIncrementFrameSize'], value)

    @property
    def MaxRandomFrameSize(self):
        """
        Returns
        -------
        - number: The integer that states the maximum random amount to which the frame size can be incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'])
    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRandomFrameSize'], value)

    @property
    def MinFpsRate(self):
        """
        Returns
        -------
        - number: The rate at which minimum frames are sent per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinFpsRate'])
    @MinFpsRate.setter
    def MinFpsRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinFpsRate'], value)

    @property
    def MinIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The integer that states the minimum amount to which the frame size can be incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'])
    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinIncrementFrameSize'], value)

    @property
    def MinKbpsRate(self):
        """
        Returns
        -------
        - number: The rate at which minimum frames are sent per kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinKbpsRate'])
    @MinKbpsRate.setter
    def MinKbpsRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinKbpsRate'], value)

    @property
    def MinRandomFrameSize(self):
        """
        Returns
        -------
        - number: The integer that states the minimum random amount to which the frame size can be incremented.
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
        - number: Defines how many times each frame size will be tested.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def PercentMaxRate(self):
        """
        Returns
        -------
        - number: The percentage of the maximum rate that is specified.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PercentMaxRate'])
    @PercentMaxRate.setter
    def PercentMaxRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PercentMaxRate'], value)

    @property
    def PortDelayEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayEnabled'])
    @PortDelayEnabled.setter
    def PortDelayEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayEnabled'], value)

    @property
    def PortDelayUnit(self):
        """
        Returns
        -------
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayUnit'])
    @PortDelayUnit.setter
    def PortDelayUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayUnit'], value)

    @property
    def PortDelayValue(self):
        """
        Returns
        -------
        - number: Sets the port delay value
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortDelayValue'])
    @PortDelayValue.setter
    def PortDelayValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortDelayValue'], value)

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
    def RateSelect(self):
        """
        Returns
        -------
        - str(fpsRate | kbpsRate | percentMaxRate): Selects the rate list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RateSelect'])
    @RateSelect.setter
    def RateSelect(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RateSelect'], value)

    @property
    def ReportSequenceError(self):
        """
        Returns
        -------
        - bool: Reports sequence errors in the test result.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportSequenceError'])
    @ReportSequenceError.setter
    def ReportSequenceError(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReportSequenceError'], value)

    @property
    def Resolution(self):
        """
        Returns
        -------
        - number: Specify the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Resolution'])
    @Resolution.setter
    def Resolution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Resolution'], value)

    @property
    def StaggeredStart(self):
        """
        Returns
        -------
        - bool: Starts test with a stagger.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StaggeredStart'])
    @StaggeredStart.setter
    def StaggeredStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StaggeredStart'], value)

    @property
    def StepIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The step to increment the frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'])
    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepIncrementFrameSize'], value)

    @property
    def SupportedTrafficTypes(self):
        """
        Returns
        -------
        - str: The traffic types supported.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'])
    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportedTrafficTypes'], value)

    @property
    def Tolerance(self):
        """
        Returns
        -------
        - number: The level of acceptable threshold.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tolerance'])
    @Tolerance.setter
    def Tolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Tolerance'], value)

    @property
    def TrafficType(self):
        """
        Returns
        -------
        - str(burstyLoading | constantLoading): The test based on the traffic type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficType'])
    @TrafficType.setter
    def TrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficType'], value)

    @property
    def TxDelay(self):
        """
        Returns
        -------
        - number: The minimum delay between successive LLDP packets. The default value is 2, the minimum is 1, and the maximum is 8192. Note that Tx Delay must be lower than txInterval.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxDelay'])
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxDelay'], value)

    @property
    def UsePercentOffsets(self):
        """
        Returns
        -------
        - bool: Uses percentage offset value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UsePercentOffsets'])
    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UsePercentOffsets'], value)

    def update(self, AmountOfTraffic=None, BurstSize=None, CongestNumFrames=None, CountRandomFrameSize=None, CustomLoadUnit=None, DelayAfterTransmit=None, Duration=None, EnableBpPassFail=None, EnableHolbPassFail=None, EnableMinFrameSize=None, EnableOldStatsForReef=None, ForceRegenerate=None, FrameSizeMode=None, Framesize=None, FramesizeList=None, LoadRateList=None, LoadType=None, MapType=None, MaxIncrementFrameSize=None, MaxRandomFrameSize=None, MinFpsRate=None, MinIncrementFrameSize=None, MinKbpsRate=None, MinRandomFrameSize=None, Numtrials=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, RateSelect=None, ReportSequenceError=None, Resolution=None, StaggeredStart=None, StepIncrementFrameSize=None, SupportedTrafficTypes=None, Tolerance=None, TrafficType=None, TxDelay=None, UsePercentOffsets=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - AmountOfTraffic (str(duration | numFrames)): The amount of traffic.
        - BurstSize (number): The number of packets that are sent in a burst.
        - CongestNumFrames (number): The number of frames that are congested.
        - CountRandomFrameSize (number): If true, frame sizes are counted at random.
        - CustomLoadUnit (str(percentMaxRate)): Specifies the custom load unit.
        - DelayAfterTransmit (number): A delay that is inserted after transmit is complete, before it continues with the test.
        - Duration (number): sec
        - EnableBpPassFail (bool): If true, BP Pass/Fail criterion is enabled.
        - EnableHolbPassFail (bool): If true, HOLB Pass/Fail criterion is enabled.
        - EnableMinFrameSize (bool): If true, IxNetwork will allow the stream to use smaller packet sizes. In the case of IPv4 and Ethernet, 64 bytes will be allowed. This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.
        - EnableOldStatsForReef (bool): If true, allows to get the old statistics for reef load module.
        - ForceRegenerate (bool): Initiates a forced regeneration.
        - FrameSizeMode (str(custom | fixed | increment | random)): This attribute is the frame size mode for the Quad Gaussian.
        - Framesize (number): Bytes
        - FramesizeList (list(str)): List containing the frame sizes used in the test.
        - LoadRateList (str): The rate list of the load item.
        - LoadType (str(custom)): The type of the payload setting.
        - MapType (str): The POS traffic map type.
        - MaxIncrementFrameSize (number): The integer that states the maximum amount to which the frame size can be incremented.
        - MaxRandomFrameSize (number): The integer that states the maximum random amount to which the frame size can be incremented.
        - MinFpsRate (number): The rate at which minimum frames are sent per second.
        - MinIncrementFrameSize (number): The integer that states the minimum amount to which the frame size can be incremented.
        - MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
        - MinRandomFrameSize (number): The integer that states the minimum random amount to which the frame size can be incremented.
        - Numtrials (number): Defines how many times each frame size will be tested.
        - PercentMaxRate (number): The percentage of the maximum rate that is specified.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - RateSelect (str(fpsRate | kbpsRate | percentMaxRate)): Selects the rate list.
        - ReportSequenceError (bool): Reports sequence errors in the test result.
        - Resolution (number): Specify the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
        - StaggeredStart (bool): Starts test with a stagger.
        - StepIncrementFrameSize (number): The step to increment the frame size.
        - SupportedTrafficTypes (str): The traffic types supported.
        - Tolerance (number): The level of acceptable threshold.
        - TrafficType (str(burstyLoading | constantLoading)): The test based on the traffic type.
        - TxDelay (number): The minimum delay between successive LLDP packets. The default value is 2, the minimum is 1, and the maximum is 8192. Note that Tx Delay must be lower than txInterval.
        - UsePercentOffsets (bool): Uses percentage offset value.

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
