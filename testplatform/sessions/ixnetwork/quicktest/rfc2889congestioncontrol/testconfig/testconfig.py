# Copyright 1997 - 2018 by IXIA Keysight
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
	"""The TestConfig class encapsulates a required testConfig node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the TestConfig property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'testConfig'

	def __init__(self, parent):
		super(TestConfig, self).__init__(parent)

	@property
	def AmountOfTraffic(self):
		"""The amount of traffic.

		Returns:
			str(duration|numFrames)
		"""
		return self._get_attribute('amountOfTraffic')
	@AmountOfTraffic.setter
	def AmountOfTraffic(self, value):
		self._set_attribute('amountOfTraffic', value)

	@property
	def BurstSize(self):
		"""The number of packets that are sent in a burst.

		Returns:
			number
		"""
		return self._get_attribute('burstSize')
	@BurstSize.setter
	def BurstSize(self, value):
		self._set_attribute('burstSize', value)

	@property
	def CongestNumFrames(self):
		"""The number of frames that are congested.

		Returns:
			number
		"""
		return self._get_attribute('congestNumFrames')
	@CongestNumFrames.setter
	def CongestNumFrames(self, value):
		self._set_attribute('congestNumFrames', value)

	@property
	def CountRandomFrameSize(self):
		"""If true, frame sizes are counted at random.

		Returns:
			number
		"""
		return self._get_attribute('countRandomFrameSize')
	@CountRandomFrameSize.setter
	def CountRandomFrameSize(self, value):
		self._set_attribute('countRandomFrameSize', value)

	@property
	def CustomLoadUnit(self):
		"""Specifies the custom load unit.

		Returns:
			str(percentMaxRate)
		"""
		return self._get_attribute('customLoadUnit')
	@CustomLoadUnit.setter
	def CustomLoadUnit(self, value):
		self._set_attribute('customLoadUnit', value)

	@property
	def DelayAfterTransmit(self):
		"""A delay that is inserted after transmit is complete, before it continues with the test.

		Returns:
			number
		"""
		return self._get_attribute('delayAfterTransmit')
	@DelayAfterTransmit.setter
	def DelayAfterTransmit(self, value):
		self._set_attribute('delayAfterTransmit', value)

	@property
	def Duration(self):
		"""sec

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableBpPassFail(self):
		"""If true, BP Pass/Fail criterion is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enableBpPassFail')
	@EnableBpPassFail.setter
	def EnableBpPassFail(self, value):
		self._set_attribute('enableBpPassFail', value)

	@property
	def EnableHolbPassFail(self):
		"""If true, HOLB Pass/Fail criterion is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enableHolbPassFail')
	@EnableHolbPassFail.setter
	def EnableHolbPassFail(self, value):
		self._set_attribute('enableHolbPassFail', value)

	@property
	def EnableMinFrameSize(self):
		"""If true, IxNetwork will allow the stream to use smaller packet sizes. In the case of IPv4 and Ethernet, 64 bytes will be allowed. This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

	@property
	def EnableOldStatsForReef(self):
		"""If true, allows to get the old statistics for reef load module.

		Returns:
			bool
		"""
		return self._get_attribute('enableOldStatsForReef')
	@EnableOldStatsForReef.setter
	def EnableOldStatsForReef(self, value):
		self._set_attribute('enableOldStatsForReef', value)

	@property
	def ForceRegenerate(self):
		"""Initiates a forced regeneration.

		Returns:
			bool
		"""
		return self._get_attribute('forceRegenerate')
	@ForceRegenerate.setter
	def ForceRegenerate(self, value):
		self._set_attribute('forceRegenerate', value)

	@property
	def FrameSizeMode(self):
		"""This attribute is the frame size mode for the Quad Gaussian.

		Returns:
			str(custom|customlist|increment|random)
		"""
		return self._get_attribute('frameSizeMode')
	@FrameSizeMode.setter
	def FrameSizeMode(self, value):
		self._set_attribute('frameSizeMode', value)

	@property
	def Framesize(self):
		"""Bytes

		Returns:
			number
		"""
		return self._get_attribute('framesize')
	@Framesize.setter
	def Framesize(self, value):
		self._set_attribute('framesize', value)

	@property
	def FramesizeList(self):
		"""List containing the frame sizes used in the test.

		Returns:
			list(str)
		"""
		return self._get_attribute('framesizeList')
	@FramesizeList.setter
	def FramesizeList(self, value):
		self._set_attribute('framesizeList', value)

	@property
	def LoadRateList(self):
		"""The rate list of the load item.

		Returns:
			str
		"""
		return self._get_attribute('loadRateList')
	@LoadRateList.setter
	def LoadRateList(self, value):
		self._set_attribute('loadRateList', value)

	@property
	def LoadType(self):
		"""The type of the payload setting.

		Returns:
			str(custom)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def MapType(self):
		"""The POS traffic map type.

		Returns:
			str
		"""
		return self._get_attribute('mapType')
	@MapType.setter
	def MapType(self, value):
		self._set_attribute('mapType', value)

	@property
	def MaxIncrementFrameSize(self):
		"""The integer that states the maximum amount to which the frame size can be incremented.

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementFrameSize')
	@MaxIncrementFrameSize.setter
	def MaxIncrementFrameSize(self, value):
		self._set_attribute('maxIncrementFrameSize', value)

	@property
	def MaxRandomFrameSize(self):
		"""The integer that states the maximum random amount to which the frame size can be incremented.

		Returns:
			number
		"""
		return self._get_attribute('maxRandomFrameSize')
	@MaxRandomFrameSize.setter
	def MaxRandomFrameSize(self, value):
		self._set_attribute('maxRandomFrameSize', value)

	@property
	def MinFpsRate(self):
		"""The rate at which minimum frames are sent per second.

		Returns:
			number
		"""
		return self._get_attribute('minFpsRate')
	@MinFpsRate.setter
	def MinFpsRate(self, value):
		self._set_attribute('minFpsRate', value)

	@property
	def MinIncrementFrameSize(self):
		"""The integer that states the minimum amount to which the frame size can be incremented.

		Returns:
			number
		"""
		return self._get_attribute('minIncrementFrameSize')
	@MinIncrementFrameSize.setter
	def MinIncrementFrameSize(self, value):
		self._set_attribute('minIncrementFrameSize', value)

	@property
	def MinKbpsRate(self):
		"""The rate at which minimum frames are sent per kbps.

		Returns:
			number
		"""
		return self._get_attribute('minKbpsRate')
	@MinKbpsRate.setter
	def MinKbpsRate(self, value):
		self._set_attribute('minKbpsRate', value)

	@property
	def MinRandomFrameSize(self):
		"""The integer that states the minimum random amount to which the frame size can be incremented.

		Returns:
			number
		"""
		return self._get_attribute('minRandomFrameSize')
	@MinRandomFrameSize.setter
	def MinRandomFrameSize(self, value):
		self._set_attribute('minRandomFrameSize', value)

	@property
	def Numtrials(self):
		"""Defines how many times each frame size will be tested.

		Returns:
			number
		"""
		return self._get_attribute('numtrials')
	@Numtrials.setter
	def Numtrials(self, value):
		self._set_attribute('numtrials', value)

	@property
	def PercentMaxRate(self):
		"""The percentage of the maximum rate that is specified.

		Returns:
			number
		"""
		return self._get_attribute('percentMaxRate')
	@PercentMaxRate.setter
	def PercentMaxRate(self, value):
		self._set_attribute('percentMaxRate', value)

	@property
	def PortDelayEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('portDelayEnabled')
	@PortDelayEnabled.setter
	def PortDelayEnabled(self, value):
		self._set_attribute('portDelayEnabled', value)

	@property
	def PortDelayUnit(self):
		"""Sets the port delay unit in which it will be measured

		Returns:
			str(bytes|nanoseconds)
		"""
		return self._get_attribute('portDelayUnit')
	@PortDelayUnit.setter
	def PortDelayUnit(self, value):
		self._set_attribute('portDelayUnit', value)

	@property
	def PortDelayValue(self):
		"""Sets the port delay value

		Returns:
			number
		"""
		return self._get_attribute('portDelayValue')
	@PortDelayValue.setter
	def PortDelayValue(self, value):
		self._set_attribute('portDelayValue', value)

	@property
	def ProtocolItem(self):
		"""Protocol Items

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])
		"""
		return self._get_attribute('protocolItem')
	@ProtocolItem.setter
	def ProtocolItem(self, value):
		self._set_attribute('protocolItem', value)

	@property
	def RateSelect(self):
		"""Selects the rate list.

		Returns:
			str(fpsRate|kbpsRate|percentMaxRate)
		"""
		return self._get_attribute('rateSelect')
	@RateSelect.setter
	def RateSelect(self, value):
		self._set_attribute('rateSelect', value)

	@property
	def ReportSequenceError(self):
		"""Reports sequence errors in the test result.

		Returns:
			bool
		"""
		return self._get_attribute('reportSequenceError')
	@ReportSequenceError.setter
	def ReportSequenceError(self, value):
		self._set_attribute('reportSequenceError', value)

	@property
	def Resolution(self):
		"""Specify the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.

		Returns:
			number
		"""
		return self._get_attribute('resolution')
	@Resolution.setter
	def Resolution(self, value):
		self._set_attribute('resolution', value)

	@property
	def StaggeredStart(self):
		"""Starts test with a stagger.

		Returns:
			bool
		"""
		return self._get_attribute('staggeredStart')
	@StaggeredStart.setter
	def StaggeredStart(self, value):
		self._set_attribute('staggeredStart', value)

	@property
	def StepIncrementFrameSize(self):
		"""The step to increment the frame size.

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementFrameSize')
	@StepIncrementFrameSize.setter
	def StepIncrementFrameSize(self, value):
		self._set_attribute('stepIncrementFrameSize', value)

	@property
	def SupportedTrafficTypes(self):
		"""The traffic types supported.

		Returns:
			str
		"""
		return self._get_attribute('supportedTrafficTypes')
	@SupportedTrafficTypes.setter
	def SupportedTrafficTypes(self, value):
		self._set_attribute('supportedTrafficTypes', value)

	@property
	def Tolerance(self):
		"""The level of acceptable threshold.

		Returns:
			number
		"""
		return self._get_attribute('tolerance')
	@Tolerance.setter
	def Tolerance(self, value):
		self._set_attribute('tolerance', value)

	@property
	def TrafficType(self):
		"""The test based on the traffic type.

		Returns:
			str(burstyLoading|constantLoading)
		"""
		return self._get_attribute('trafficType')
	@TrafficType.setter
	def TrafficType(self, value):
		self._set_attribute('trafficType', value)

	@property
	def TxDelay(self):
		"""The minimum delay between successive LLDP packets. The default value is 2, the minimum is 1, and the maximum is 8192. Note that Tx Delay must be lower than txInterval.

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	@property
	def UsePercentOffsets(self):
		"""Uses percentage offset value.

		Returns:
			bool
		"""
		return self._get_attribute('usePercentOffsets')
	@UsePercentOffsets.setter
	def UsePercentOffsets(self, value):
		self._set_attribute('usePercentOffsets', value)

	def update(self, AmountOfTraffic=None, BurstSize=None, CongestNumFrames=None, CountRandomFrameSize=None, CustomLoadUnit=None, DelayAfterTransmit=None, Duration=None, EnableBpPassFail=None, EnableHolbPassFail=None, EnableMinFrameSize=None, EnableOldStatsForReef=None, ForceRegenerate=None, FrameSizeMode=None, Framesize=None, FramesizeList=None, LoadRateList=None, LoadType=None, MapType=None, MaxIncrementFrameSize=None, MaxRandomFrameSize=None, MinFpsRate=None, MinIncrementFrameSize=None, MinKbpsRate=None, MinRandomFrameSize=None, Numtrials=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, RateSelect=None, ReportSequenceError=None, Resolution=None, StaggeredStart=None, StepIncrementFrameSize=None, SupportedTrafficTypes=None, Tolerance=None, TrafficType=None, TxDelay=None, UsePercentOffsets=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			AmountOfTraffic (str(duration|numFrames)): The amount of traffic.
			BurstSize (number): The number of packets that are sent in a burst.
			CongestNumFrames (number): The number of frames that are congested.
			CountRandomFrameSize (number): If true, frame sizes are counted at random.
			CustomLoadUnit (str(percentMaxRate)): Specifies the custom load unit.
			DelayAfterTransmit (number): A delay that is inserted after transmit is complete, before it continues with the test.
			Duration (number): sec
			EnableBpPassFail (bool): If true, BP Pass/Fail criterion is enabled.
			EnableHolbPassFail (bool): If true, HOLB Pass/Fail criterion is enabled.
			EnableMinFrameSize (bool): If true, IxNetwork will allow the stream to use smaller packet sizes. In the case of IPv4 and Ethernet, 64 bytes will be allowed. This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.
			EnableOldStatsForReef (bool): If true, allows to get the old statistics for reef load module.
			ForceRegenerate (bool): Initiates a forced regeneration.
			FrameSizeMode (str(custom|customlist|increment|random)): This attribute is the frame size mode for the Quad Gaussian.
			Framesize (number): Bytes
			FramesizeList (list(str)): List containing the frame sizes used in the test.
			LoadRateList (str): The rate list of the load item.
			LoadType (str(custom)): The type of the payload setting.
			MapType (str): The POS traffic map type.
			MaxIncrementFrameSize (number): The integer that states the maximum amount to which the frame size can be incremented.
			MaxRandomFrameSize (number): The integer that states the maximum random amount to which the frame size can be incremented.
			MinFpsRate (number): The rate at which minimum frames are sent per second.
			MinIncrementFrameSize (number): The integer that states the minimum amount to which the frame size can be incremented.
			MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
			MinRandomFrameSize (number): The integer that states the minimum random amount to which the frame size can be incremented.
			Numtrials (number): Defines how many times each frame size will be tested.
			PercentMaxRate (number): The percentage of the maximum rate that is specified.
			PortDelayEnabled (bool): NOT DEFINED
			PortDelayUnit (str(bytes|nanoseconds)): Sets the port delay unit in which it will be measured
			PortDelayValue (number): Sets the port delay value
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			RateSelect (str(fpsRate|kbpsRate|percentMaxRate)): Selects the rate list.
			ReportSequenceError (bool): Reports sequence errors in the test result.
			Resolution (number): Specify the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
			StaggeredStart (bool): Starts test with a stagger.
			StepIncrementFrameSize (number): The step to increment the frame size.
			SupportedTrafficTypes (str): The traffic types supported.
			Tolerance (number): The level of acceptable threshold.
			TrafficType (str(burstyLoading|constantLoading)): The test based on the traffic type.
			TxDelay (number): The minimum delay between successive LLDP packets. The default value is 2, the minimum is 1, and the maximum is 8192. Note that Tx Delay must be lower than txInterval.
			UsePercentOffsets (bool): Uses percentage offset value.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def Apply(self):
		"""Executes the apply operation on the server.

		Applies the specified Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('apply', payload=payload, response_object=None)

	def ApplyAsync(self):
		"""Executes the applyAsync operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyAsync', payload=payload, response_object=None)

	def ApplyAsyncResult(self):
		"""Executes the applyAsyncResult operation on the server.

			Returns:
				bool: 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyAsyncResult', payload=payload, response_object=None)

	def ApplyITWizardConfiguration(self):
		"""Executes the applyITWizardConfiguration operation on the server.

		Applies the specified Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

	def GenerateReport(self):
		"""Executes the generateReport operation on the server.

		Generate a PDF report for the last succesfull test run.

			Returns:
				str: This method is asynchronous and has no return value.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('generateReport', payload=payload, response_object=None)

	def Run(self, *args, **kwargs):
		"""Executes the run operation on the server.

		Starts the specified Quick Test and waits for its execution to finish.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		run()list

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		run(InputParameters:string)list
			Args:
				args[0] is InputParameters (str): The input arguments of the test.

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('run', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Starts the specified Quick Test.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(InputParameters:string)
			Args:
				args[0] is InputParameters (str): The input arguments of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stops the currently running Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)

	def WaitForTest(self):
		"""Executes the waitForTest operation on the server.

		Waits for the execution of the specified Quick Test to be completed.

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('waitForTest', payload=payload, response_object=None)
