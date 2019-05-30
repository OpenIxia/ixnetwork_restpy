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


class PassCriteria(Base):
	"""The PassCriteria class encapsulates a required passCriteria node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the PassCriteria property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'passCriteria'

	def __init__(self, parent):
		super(PassCriteria, self).__init__(parent)

	@property
	def DownstreamDataErrorThresholdMode(self):
		"""The downstream Data Error Threshold mode.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('downstreamDataErrorThresholdMode')
	@DownstreamDataErrorThresholdMode.setter
	def DownstreamDataErrorThresholdMode(self, value):
		self._set_attribute('downstreamDataErrorThresholdMode', value)

	@property
	def DownstreamDataErrorThresholdValue(self):
		"""The downstream data error threshold value.

		Returns:
			number
		"""
		return self._get_attribute('downstreamDataErrorThresholdValue')
	@DownstreamDataErrorThresholdValue.setter
	def DownstreamDataErrorThresholdValue(self, value):
		self._set_attribute('downstreamDataErrorThresholdValue', value)

	@property
	def DownstreamEnableDataIntegrityPassFail(self):
		"""Enables downstream data integrity pass or fail criteria.

		Returns:
			bool
		"""
		return self._get_attribute('downstreamEnableDataIntegrityPassFail')
	@DownstreamEnableDataIntegrityPassFail.setter
	def DownstreamEnableDataIntegrityPassFail(self, value):
		self._set_attribute('downstreamEnableDataIntegrityPassFail', value)

	@property
	def DownstreamEnableLatencyPassFail(self):
		"""Enable downstream traffic latency pass or fail criteria.

		Returns:
			bool
		"""
		return self._get_attribute('downstreamEnableLatencyPassFail')
	@DownstreamEnableLatencyPassFail.setter
	def DownstreamEnableLatencyPassFail(self, value):
		self._set_attribute('downstreamEnableLatencyPassFail', value)

	@property
	def DownstreamEnableRatePassFail(self):
		"""Enables to check downstream pass or fail rate.

		Returns:
			bool
		"""
		return self._get_attribute('downstreamEnableRatePassFail')
	@DownstreamEnableRatePassFail.setter
	def DownstreamEnableRatePassFail(self, value):
		self._set_attribute('downstreamEnableRatePassFail', value)

	@property
	def DownstreamEnableSequenceErrorsPassFail(self):
		"""Enables downstream sequence errors pass or fail criteria.

		Returns:
			bool
		"""
		return self._get_attribute('downstreamEnableSequenceErrorsPassFail')
	@DownstreamEnableSequenceErrorsPassFail.setter
	def DownstreamEnableSequenceErrorsPassFail(self, value):
		self._set_attribute('downstreamEnableSequenceErrorsPassFail', value)

	@property
	def DownstreamEnableStandardDeviationPassFail(self):
		"""Enables downstream standard deviation pass or fail criteria.

		Returns:
			bool
		"""
		return self._get_attribute('downstreamEnableStandardDeviationPassFail')
	@DownstreamEnableStandardDeviationPassFail.setter
	def DownstreamEnableStandardDeviationPassFail(self, value):
		self._set_attribute('downstreamEnableStandardDeviationPassFail', value)

	@property
	def DownstreamLatencyThresholdMode(self):
		"""The latency threshold mode for downstream traffic.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('downstreamLatencyThresholdMode')
	@DownstreamLatencyThresholdMode.setter
	def DownstreamLatencyThresholdMode(self, value):
		self._set_attribute('downstreamLatencyThresholdMode', value)

	@property
	def DownstreamLatencyThresholdScale(self):
		"""The latency threshold scale for downstream trafic.

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('downstreamLatencyThresholdScale')
	@DownstreamLatencyThresholdScale.setter
	def DownstreamLatencyThresholdScale(self, value):
		self._set_attribute('downstreamLatencyThresholdScale', value)

	@property
	def DownstreamLatencyThresholdValue(self):
		"""The latency threshold value for downstream traffic.

		Returns:
			number
		"""
		return self._get_attribute('downstreamLatencyThresholdValue')
	@DownstreamLatencyThresholdValue.setter
	def DownstreamLatencyThresholdValue(self, value):
		self._set_attribute('downstreamLatencyThresholdValue', value)

	@property
	def DownstreamLatencyVarThresholdMode(self):
		"""The latency variation threshold mode for downstream traffic.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('downstreamLatencyVarThresholdMode')
	@DownstreamLatencyVarThresholdMode.setter
	def DownstreamLatencyVarThresholdMode(self, value):
		self._set_attribute('downstreamLatencyVarThresholdMode', value)

	@property
	def DownstreamLatencyVariationThresholdScale(self):
		"""The latency variation threshold scale for downstream traffic.

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('downstreamLatencyVariationThresholdScale')
	@DownstreamLatencyVariationThresholdScale.setter
	def DownstreamLatencyVariationThresholdScale(self, value):
		self._set_attribute('downstreamLatencyVariationThresholdScale', value)

	@property
	def DownstreamLatencyVariationThresholdValue(self):
		"""The latency variation threshold value for downstream traffic.

		Returns:
			number
		"""
		return self._get_attribute('downstreamLatencyVariationThresholdValue')
	@DownstreamLatencyVariationThresholdValue.setter
	def DownstreamLatencyVariationThresholdValue(self, value):
		self._set_attribute('downstreamLatencyVariationThresholdValue', value)

	@property
	def DownstreamPassCriteriaLoadRateMode(self):
		"""The downstream traffic pass criteria for load rate mode.

		Returns:
			str(average|minimum)
		"""
		return self._get_attribute('downstreamPassCriteriaLoadRateMode')
	@DownstreamPassCriteriaLoadRateMode.setter
	def DownstreamPassCriteriaLoadRateMode(self, value):
		self._set_attribute('downstreamPassCriteriaLoadRateMode', value)

	@property
	def DownstreamPassCriteriaLoadRateScale(self):
		"""The downstream traffic pass criteria for load rate scale.

		Returns:
			str(fps|gbps|kbps|mbps|percent)
		"""
		return self._get_attribute('downstreamPassCriteriaLoadRateScale')
	@DownstreamPassCriteriaLoadRateScale.setter
	def DownstreamPassCriteriaLoadRateScale(self, value):
		self._set_attribute('downstreamPassCriteriaLoadRateScale', value)

	@property
	def DownstreamPassCriteriaLoadRateValue(self):
		"""The downstream traffic pass criteria load rate value.

		Returns:
			number
		"""
		return self._get_attribute('downstreamPassCriteriaLoadRateValue')
	@DownstreamPassCriteriaLoadRateValue.setter
	def DownstreamPassCriteriaLoadRateValue(self, value):
		self._set_attribute('downstreamPassCriteriaLoadRateValue', value)

	@property
	def DownstreamSeqErrorsThresholdMode(self):
		"""The downstream traffic sequence error threshold mode.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('downstreamSeqErrorsThresholdMode')
	@DownstreamSeqErrorsThresholdMode.setter
	def DownstreamSeqErrorsThresholdMode(self, value):
		self._set_attribute('downstreamSeqErrorsThresholdMode', value)

	@property
	def DownstreamSeqErrorsThresholdValue(self):
		"""The downstream traffic sequence error threshold value.

		Returns:
			number
		"""
		return self._get_attribute('downstreamSeqErrorsThresholdValue')
	@DownstreamSeqErrorsThresholdValue.setter
	def DownstreamSeqErrorsThresholdValue(self, value):
		self._set_attribute('downstreamSeqErrorsThresholdValue', value)

	@property
	def Downstream_passFailFrequency(self):
		"""NOT DEFINED

		Returns:
			str(framesizes|trials)
		"""
		return self._get_attribute('downstream_passFailFrequency')
	@Downstream_passFailFrequency.setter
	def Downstream_passFailFrequency(self, value):
		self._set_attribute('downstream_passFailFrequency', value)

	@property
	def UpstreamDataErrorThresholdMode(self):
		"""The upstream Data Error Threshold mode.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('upstreamDataErrorThresholdMode')
	@UpstreamDataErrorThresholdMode.setter
	def UpstreamDataErrorThresholdMode(self, value):
		self._set_attribute('upstreamDataErrorThresholdMode', value)

	@property
	def UpstreamDataErrorThresholdValue(self):
		"""The upstream Data Error Threshold value.

		Returns:
			number
		"""
		return self._get_attribute('upstreamDataErrorThresholdValue')
	@UpstreamDataErrorThresholdValue.setter
	def UpstreamDataErrorThresholdValue(self, value):
		self._set_attribute('upstreamDataErrorThresholdValue', value)

	@property
	def UpstreamEnableDataIntegrityPassFail(self):
		"""Enables data integrity pass or fail criteria for upstream traffic.

		Returns:
			bool
		"""
		return self._get_attribute('upstreamEnableDataIntegrityPassFail')
	@UpstreamEnableDataIntegrityPassFail.setter
	def UpstreamEnableDataIntegrityPassFail(self, value):
		self._set_attribute('upstreamEnableDataIntegrityPassFail', value)

	@property
	def UpstreamEnableLatencyPassFail(self):
		"""Enables latency pass fail criteria for upstream traffic.

		Returns:
			bool
		"""
		return self._get_attribute('upstreamEnableLatencyPassFail')
	@UpstreamEnableLatencyPassFail.setter
	def UpstreamEnableLatencyPassFail(self, value):
		self._set_attribute('upstreamEnableLatencyPassFail', value)

	@property
	def UpstreamEnableRatePassFail(self):
		"""Enables pass or fail rate for upstream traffic.

		Returns:
			bool
		"""
		return self._get_attribute('upstreamEnableRatePassFail')
	@UpstreamEnableRatePassFail.setter
	def UpstreamEnableRatePassFail(self, value):
		self._set_attribute('upstreamEnableRatePassFail', value)

	@property
	def UpstreamEnableSequenceErrorsPassFail(self):
		"""Enables sequence error pass or fail criteria for upstream traffic.

		Returns:
			bool
		"""
		return self._get_attribute('upstreamEnableSequenceErrorsPassFail')
	@UpstreamEnableSequenceErrorsPassFail.setter
	def UpstreamEnableSequenceErrorsPassFail(self, value):
		self._set_attribute('upstreamEnableSequenceErrorsPassFail', value)

	@property
	def UpstreamEnableStandardDeviationPassFail(self):
		"""Enables upstream traffic standard deviation pass or fail.

		Returns:
			bool
		"""
		return self._get_attribute('upstreamEnableStandardDeviationPassFail')
	@UpstreamEnableStandardDeviationPassFail.setter
	def UpstreamEnableStandardDeviationPassFail(self, value):
		self._set_attribute('upstreamEnableStandardDeviationPassFail', value)

	@property
	def UpstreamLatencyThresholdMode(self):
		"""The upstream latency threshold mode.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('upstreamLatencyThresholdMode')
	@UpstreamLatencyThresholdMode.setter
	def UpstreamLatencyThresholdMode(self, value):
		self._set_attribute('upstreamLatencyThresholdMode', value)

	@property
	def UpstreamLatencyThresholdScale(self):
		"""The upstream latency threshold scale.

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('upstreamLatencyThresholdScale')
	@UpstreamLatencyThresholdScale.setter
	def UpstreamLatencyThresholdScale(self, value):
		self._set_attribute('upstreamLatencyThresholdScale', value)

	@property
	def UpstreamLatencyThresholdValue(self):
		"""The upstream latency threshold value.

		Returns:
			number
		"""
		return self._get_attribute('upstreamLatencyThresholdValue')
	@UpstreamLatencyThresholdValue.setter
	def UpstreamLatencyThresholdValue(self, value):
		self._set_attribute('upstreamLatencyThresholdValue', value)

	@property
	def UpstreamLatencyVarThresholdMode(self):
		"""The upstream latency variation threshold mode.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('upstreamLatencyVarThresholdMode')
	@UpstreamLatencyVarThresholdMode.setter
	def UpstreamLatencyVarThresholdMode(self, value):
		self._set_attribute('upstreamLatencyVarThresholdMode', value)

	@property
	def UpstreamLatencyVariationThresholdScale(self):
		"""The upstream latency variation threshold scale.

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('upstreamLatencyVariationThresholdScale')
	@UpstreamLatencyVariationThresholdScale.setter
	def UpstreamLatencyVariationThresholdScale(self, value):
		self._set_attribute('upstreamLatencyVariationThresholdScale', value)

	@property
	def UpstreamLatencyVariationThresholdValue(self):
		"""The upstream latency variation threshold value.

		Returns:
			number
		"""
		return self._get_attribute('upstreamLatencyVariationThresholdValue')
	@UpstreamLatencyVariationThresholdValue.setter
	def UpstreamLatencyVariationThresholdValue(self, value):
		self._set_attribute('upstreamLatencyVariationThresholdValue', value)

	@property
	def UpstreamPassCriteriaLoadRateMode(self):
		"""The upstream pass criteria load rate mode.

		Returns:
			str(average|minimum)
		"""
		return self._get_attribute('upstreamPassCriteriaLoadRateMode')
	@UpstreamPassCriteriaLoadRateMode.setter
	def UpstreamPassCriteriaLoadRateMode(self, value):
		self._set_attribute('upstreamPassCriteriaLoadRateMode', value)

	@property
	def UpstreamPassCriteriaLoadRateScale(self):
		"""The upstream pass criteria load rate scale.

		Returns:
			str(fps|gbps|kbps|mbps|percent)
		"""
		return self._get_attribute('upstreamPassCriteriaLoadRateScale')
	@UpstreamPassCriteriaLoadRateScale.setter
	def UpstreamPassCriteriaLoadRateScale(self, value):
		self._set_attribute('upstreamPassCriteriaLoadRateScale', value)

	@property
	def UpstreamPassCriteriaLoadRateValue(self):
		"""The upstream pass criteria load rate value.

		Returns:
			number
		"""
		return self._get_attribute('upstreamPassCriteriaLoadRateValue')
	@UpstreamPassCriteriaLoadRateValue.setter
	def UpstreamPassCriteriaLoadRateValue(self, value):
		self._set_attribute('upstreamPassCriteriaLoadRateValue', value)

	@property
	def UpstreamSeqErrorsThresholdMode(self):
		"""The upstream sequence error threshold mode.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('upstreamSeqErrorsThresholdMode')
	@UpstreamSeqErrorsThresholdMode.setter
	def UpstreamSeqErrorsThresholdMode(self, value):
		self._set_attribute('upstreamSeqErrorsThresholdMode', value)

	@property
	def UpstreamSeqErrorsThresholdValue(self):
		"""The upstream sequence error threshold value.

		Returns:
			number
		"""
		return self._get_attribute('upstreamSeqErrorsThresholdValue')
	@UpstreamSeqErrorsThresholdValue.setter
	def UpstreamSeqErrorsThresholdValue(self, value):
		self._set_attribute('upstreamSeqErrorsThresholdValue', value)

	@property
	def Upstream_passFailFrequency(self):
		"""NOT DEFINED

		Returns:
			str(framesizes|trials)
		"""
		return self._get_attribute('upstream_passFailFrequency')
	@Upstream_passFailFrequency.setter
	def Upstream_passFailFrequency(self, value):
		self._set_attribute('upstream_passFailFrequency', value)

	def update(self, DownstreamDataErrorThresholdMode=None, DownstreamDataErrorThresholdValue=None, DownstreamEnableDataIntegrityPassFail=None, DownstreamEnableLatencyPassFail=None, DownstreamEnableRatePassFail=None, DownstreamEnableSequenceErrorsPassFail=None, DownstreamEnableStandardDeviationPassFail=None, DownstreamLatencyThresholdMode=None, DownstreamLatencyThresholdScale=None, DownstreamLatencyThresholdValue=None, DownstreamLatencyVarThresholdMode=None, DownstreamLatencyVariationThresholdScale=None, DownstreamLatencyVariationThresholdValue=None, DownstreamPassCriteriaLoadRateMode=None, DownstreamPassCriteriaLoadRateScale=None, DownstreamPassCriteriaLoadRateValue=None, DownstreamSeqErrorsThresholdMode=None, DownstreamSeqErrorsThresholdValue=None, Downstream_passFailFrequency=None, UpstreamDataErrorThresholdMode=None, UpstreamDataErrorThresholdValue=None, UpstreamEnableDataIntegrityPassFail=None, UpstreamEnableLatencyPassFail=None, UpstreamEnableRatePassFail=None, UpstreamEnableSequenceErrorsPassFail=None, UpstreamEnableStandardDeviationPassFail=None, UpstreamLatencyThresholdMode=None, UpstreamLatencyThresholdScale=None, UpstreamLatencyThresholdValue=None, UpstreamLatencyVarThresholdMode=None, UpstreamLatencyVariationThresholdScale=None, UpstreamLatencyVariationThresholdValue=None, UpstreamPassCriteriaLoadRateMode=None, UpstreamPassCriteriaLoadRateScale=None, UpstreamPassCriteriaLoadRateValue=None, UpstreamSeqErrorsThresholdMode=None, UpstreamSeqErrorsThresholdValue=None, Upstream_passFailFrequency=None):
		"""Updates a child instance of passCriteria on the server.

		Args:
			DownstreamDataErrorThresholdMode (str(average|maximum)): The downstream Data Error Threshold mode.
			DownstreamDataErrorThresholdValue (number): The downstream data error threshold value.
			DownstreamEnableDataIntegrityPassFail (bool): Enables downstream data integrity pass or fail criteria.
			DownstreamEnableLatencyPassFail (bool): Enable downstream traffic latency pass or fail criteria.
			DownstreamEnableRatePassFail (bool): Enables to check downstream pass or fail rate.
			DownstreamEnableSequenceErrorsPassFail (bool): Enables downstream sequence errors pass or fail criteria.
			DownstreamEnableStandardDeviationPassFail (bool): Enables downstream standard deviation pass or fail criteria.
			DownstreamLatencyThresholdMode (str(average|maximum)): The latency threshold mode for downstream traffic.
			DownstreamLatencyThresholdScale (str(ms|ns|us)): The latency threshold scale for downstream trafic.
			DownstreamLatencyThresholdValue (number): The latency threshold value for downstream traffic.
			DownstreamLatencyVarThresholdMode (str(average|maximum)): The latency variation threshold mode for downstream traffic.
			DownstreamLatencyVariationThresholdScale (str(ms|ns|us)): The latency variation threshold scale for downstream traffic.
			DownstreamLatencyVariationThresholdValue (number): The latency variation threshold value for downstream traffic.
			DownstreamPassCriteriaLoadRateMode (str(average|minimum)): The downstream traffic pass criteria for load rate mode.
			DownstreamPassCriteriaLoadRateScale (str(fps|gbps|kbps|mbps|percent)): The downstream traffic pass criteria for load rate scale.
			DownstreamPassCriteriaLoadRateValue (number): The downstream traffic pass criteria load rate value.
			DownstreamSeqErrorsThresholdMode (str(average|maximum)): The downstream traffic sequence error threshold mode.
			DownstreamSeqErrorsThresholdValue (number): The downstream traffic sequence error threshold value.
			Downstream_passFailFrequency (str(framesizes|trials)): NOT DEFINED
			UpstreamDataErrorThresholdMode (str(average|maximum)): The upstream Data Error Threshold mode.
			UpstreamDataErrorThresholdValue (number): The upstream Data Error Threshold value.
			UpstreamEnableDataIntegrityPassFail (bool): Enables data integrity pass or fail criteria for upstream traffic.
			UpstreamEnableLatencyPassFail (bool): Enables latency pass fail criteria for upstream traffic.
			UpstreamEnableRatePassFail (bool): Enables pass or fail rate for upstream traffic.
			UpstreamEnableSequenceErrorsPassFail (bool): Enables sequence error pass or fail criteria for upstream traffic.
			UpstreamEnableStandardDeviationPassFail (bool): Enables upstream traffic standard deviation pass or fail.
			UpstreamLatencyThresholdMode (str(average|maximum)): The upstream latency threshold mode.
			UpstreamLatencyThresholdScale (str(ms|ns|us)): The upstream latency threshold scale.
			UpstreamLatencyThresholdValue (number): The upstream latency threshold value.
			UpstreamLatencyVarThresholdMode (str(average|maximum)): The upstream latency variation threshold mode.
			UpstreamLatencyVariationThresholdScale (str(ms|ns|us)): The upstream latency variation threshold scale.
			UpstreamLatencyVariationThresholdValue (number): The upstream latency variation threshold value.
			UpstreamPassCriteriaLoadRateMode (str(average|minimum)): The upstream pass criteria load rate mode.
			UpstreamPassCriteriaLoadRateScale (str(fps|gbps|kbps|mbps|percent)): The upstream pass criteria load rate scale.
			UpstreamPassCriteriaLoadRateValue (number): The upstream pass criteria load rate value.
			UpstreamSeqErrorsThresholdMode (str(average|maximum)): The upstream sequence error threshold mode.
			UpstreamSeqErrorsThresholdValue (number): The upstream sequence error threshold value.
			Upstream_passFailFrequency (str(framesizes|trials)): NOT DEFINED

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
