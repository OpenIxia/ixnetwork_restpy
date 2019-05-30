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
		"""Signifies threshold mode for downstream data error.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('downstreamDataErrorThresholdMode')
	@DownstreamDataErrorThresholdMode.setter
	def DownstreamDataErrorThresholdMode(self, value):
		self._set_attribute('downstreamDataErrorThresholdMode', value)

	@property
	def DownstreamDataErrorThresholdValue(self):
		"""Signifies the downstream data error threshold value.

		Returns:
			number
		"""
		return self._get_attribute('downstreamDataErrorThresholdValue')
	@DownstreamDataErrorThresholdValue.setter
	def DownstreamDataErrorThresholdValue(self, value):
		self._set_attribute('downstreamDataErrorThresholdValue', value)

	@property
	def DownstreamEnableDataIntegrityPassFail(self):
		"""if true, enables pass or faill of data integrity for downstream.

		Returns:
			bool
		"""
		return self._get_attribute('downstreamEnableDataIntegrityPassFail')
	@DownstreamEnableDataIntegrityPassFail.setter
	def DownstreamEnableDataIntegrityPassFail(self, value):
		self._set_attribute('downstreamEnableDataIntegrityPassFail', value)

	@property
	def DownstreamEnableLatencyPassFail(self):
		"""If true, enables latency pass fail for downstream.

		Returns:
			bool
		"""
		return self._get_attribute('downstreamEnableLatencyPassFail')
	@DownstreamEnableLatencyPassFail.setter
	def DownstreamEnableLatencyPassFail(self, value):
		self._set_attribute('downstreamEnableLatencyPassFail', value)

	@property
	def DownstreamEnableRatePassFail(self):
		"""If true, enables pass fail rate for downstream.

		Returns:
			bool
		"""
		return self._get_attribute('downstreamEnableRatePassFail')
	@DownstreamEnableRatePassFail.setter
	def DownstreamEnableRatePassFail(self, value):
		self._set_attribute('downstreamEnableRatePassFail', value)

	@property
	def DownstreamEnableSequenceErrorsPassFail(self):
		"""If true, enables the pass fail for sequence errors for downstream.

		Returns:
			bool
		"""
		return self._get_attribute('downstreamEnableSequenceErrorsPassFail')
	@DownstreamEnableSequenceErrorsPassFail.setter
	def DownstreamEnableSequenceErrorsPassFail(self, value):
		self._set_attribute('downstreamEnableSequenceErrorsPassFail', value)

	@property
	def DownstreamEnableStandardDeviationPassFail(self):
		"""If true, enables pass fail of standard deviation for downstream.

		Returns:
			bool
		"""
		return self._get_attribute('downstreamEnableStandardDeviationPassFail')
	@DownstreamEnableStandardDeviationPassFail.setter
	def DownstreamEnableStandardDeviationPassFail(self, value):
		self._set_attribute('downstreamEnableStandardDeviationPassFail', value)

	@property
	def DownstreamLatencyThresholdMode(self):
		"""Signifies the latency threshold mode for downstream.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('downstreamLatencyThresholdMode')
	@DownstreamLatencyThresholdMode.setter
	def DownstreamLatencyThresholdMode(self, value):
		self._set_attribute('downstreamLatencyThresholdMode', value)

	@property
	def DownstreamLatencyThresholdScale(self):
		"""Signifies the threshold scale for downstream latency.

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('downstreamLatencyThresholdScale')
	@DownstreamLatencyThresholdScale.setter
	def DownstreamLatencyThresholdScale(self, value):
		self._set_attribute('downstreamLatencyThresholdScale', value)

	@property
	def DownstreamLatencyThresholdValue(self):
		"""Signifies the latency threshold value for downstream.

		Returns:
			number
		"""
		return self._get_attribute('downstreamLatencyThresholdValue')
	@DownstreamLatencyThresholdValue.setter
	def DownstreamLatencyThresholdValue(self, value):
		self._set_attribute('downstreamLatencyThresholdValue', value)

	@property
	def DownstreamLatencyVarThresholdMode(self):
		"""Signifies latency variation threshold mode for downstream.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('downstreamLatencyVarThresholdMode')
	@DownstreamLatencyVarThresholdMode.setter
	def DownstreamLatencyVarThresholdMode(self, value):
		self._set_attribute('downstreamLatencyVarThresholdMode', value)

	@property
	def DownstreamLatencyVariationThresholdScale(self):
		"""Signifies latency variation threshold scale for downstream.

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('downstreamLatencyVariationThresholdScale')
	@DownstreamLatencyVariationThresholdScale.setter
	def DownstreamLatencyVariationThresholdScale(self, value):
		self._set_attribute('downstreamLatencyVariationThresholdScale', value)

	@property
	def DownstreamLatencyVariationThresholdValue(self):
		"""Signifies the latency variation threshold value for downstream.

		Returns:
			number
		"""
		return self._get_attribute('downstreamLatencyVariationThresholdValue')
	@DownstreamLatencyVariationThresholdValue.setter
	def DownstreamLatencyVariationThresholdValue(self, value):
		self._set_attribute('downstreamLatencyVariationThresholdValue', value)

	@property
	def DownstreamPassCriteriaLoadRateMode(self):
		"""Signifies the pass criteria load rate mode for downstream.

		Returns:
			str(average|minimum)
		"""
		return self._get_attribute('downstreamPassCriteriaLoadRateMode')
	@DownstreamPassCriteriaLoadRateMode.setter
	def DownstreamPassCriteriaLoadRateMode(self, value):
		self._set_attribute('downstreamPassCriteriaLoadRateMode', value)

	@property
	def DownstreamPassCriteriaLoadRateScale(self):
		"""Signifies the pass criteria load rate scale for downstream.

		Returns:
			str(fps|gbps|kbps|mbps|percent)
		"""
		return self._get_attribute('downstreamPassCriteriaLoadRateScale')
	@DownstreamPassCriteriaLoadRateScale.setter
	def DownstreamPassCriteriaLoadRateScale(self, value):
		self._set_attribute('downstreamPassCriteriaLoadRateScale', value)

	@property
	def DownstreamPassCriteriaLoadRateValue(self):
		"""Signifies pass criteria load rate value for downstream.

		Returns:
			number
		"""
		return self._get_attribute('downstreamPassCriteriaLoadRateValue')
	@DownstreamPassCriteriaLoadRateValue.setter
	def DownstreamPassCriteriaLoadRateValue(self, value):
		self._set_attribute('downstreamPassCriteriaLoadRateValue', value)

	@property
	def DownstreamSeqErrorsThresholdMode(self):
		"""Signifies the threshold mode for sequence errors for downstream.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('downstreamSeqErrorsThresholdMode')
	@DownstreamSeqErrorsThresholdMode.setter
	def DownstreamSeqErrorsThresholdMode(self, value):
		self._set_attribute('downstreamSeqErrorsThresholdMode', value)

	@property
	def DownstreamSeqErrorsThresholdValue(self):
		"""Signifies the threshold value for sequence errors for downstream.

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
		"""Signifies the data error threshold mode for upstream.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('upstreamDataErrorThresholdMode')
	@UpstreamDataErrorThresholdMode.setter
	def UpstreamDataErrorThresholdMode(self, value):
		self._set_attribute('upstreamDataErrorThresholdMode', value)

	@property
	def UpstreamDataErrorThresholdValue(self):
		"""Signifies data error threshold value for upstream.

		Returns:
			number
		"""
		return self._get_attribute('upstreamDataErrorThresholdValue')
	@UpstreamDataErrorThresholdValue.setter
	def UpstreamDataErrorThresholdValue(self, value):
		self._set_attribute('upstreamDataErrorThresholdValue', value)

	@property
	def UpstreamEnableDataIntegrityPassFail(self):
		"""If true, enables pass fail of data integrity for upstream.

		Returns:
			bool
		"""
		return self._get_attribute('upstreamEnableDataIntegrityPassFail')
	@UpstreamEnableDataIntegrityPassFail.setter
	def UpstreamEnableDataIntegrityPassFail(self, value):
		self._set_attribute('upstreamEnableDataIntegrityPassFail', value)

	@property
	def UpstreamEnableLatencyPassFail(self):
		"""If true, enables latency pass fail for upstream.

		Returns:
			bool
		"""
		return self._get_attribute('upstreamEnableLatencyPassFail')
	@UpstreamEnableLatencyPassFail.setter
	def UpstreamEnableLatencyPassFail(self, value):
		self._set_attribute('upstreamEnableLatencyPassFail', value)

	@property
	def UpstreamEnableRatePassFail(self):
		"""If true, enables the rate of pass fail for upstream.

		Returns:
			bool
		"""
		return self._get_attribute('upstreamEnableRatePassFail')
	@UpstreamEnableRatePassFail.setter
	def UpstreamEnableRatePassFail(self, value):
		self._set_attribute('upstreamEnableRatePassFail', value)

	@property
	def UpstreamEnableSequenceErrorsPassFail(self):
		"""If true, enables sequence errors pass fail for upstream.

		Returns:
			bool
		"""
		return self._get_attribute('upstreamEnableSequenceErrorsPassFail')
	@UpstreamEnableSequenceErrorsPassFail.setter
	def UpstreamEnableSequenceErrorsPassFail(self, value):
		self._set_attribute('upstreamEnableSequenceErrorsPassFail', value)

	@property
	def UpstreamEnableStandardDeviationPassFail(self):
		"""If true, enables standard deviation of pass and fail for upstream.

		Returns:
			bool
		"""
		return self._get_attribute('upstreamEnableStandardDeviationPassFail')
	@UpstreamEnableStandardDeviationPassFail.setter
	def UpstreamEnableStandardDeviationPassFail(self, value):
		self._set_attribute('upstreamEnableStandardDeviationPassFail', value)

	@property
	def UpstreamLatencyThresholdMode(self):
		"""Signifies the latency threshold mode for upstream.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('upstreamLatencyThresholdMode')
	@UpstreamLatencyThresholdMode.setter
	def UpstreamLatencyThresholdMode(self, value):
		self._set_attribute('upstreamLatencyThresholdMode', value)

	@property
	def UpstreamLatencyThresholdScale(self):
		"""Signifies the latency threshold scale for upstream.

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('upstreamLatencyThresholdScale')
	@UpstreamLatencyThresholdScale.setter
	def UpstreamLatencyThresholdScale(self, value):
		self._set_attribute('upstreamLatencyThresholdScale', value)

	@property
	def UpstreamLatencyThresholdValue(self):
		"""It is the latency threshold value for upstream.

		Returns:
			number
		"""
		return self._get_attribute('upstreamLatencyThresholdValue')
	@UpstreamLatencyThresholdValue.setter
	def UpstreamLatencyThresholdValue(self, value):
		self._set_attribute('upstreamLatencyThresholdValue', value)

	@property
	def UpstreamLatencyVarThresholdMode(self):
		"""Signifies the latency variation threshold mode for upstream.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('upstreamLatencyVarThresholdMode')
	@UpstreamLatencyVarThresholdMode.setter
	def UpstreamLatencyVarThresholdMode(self, value):
		self._set_attribute('upstreamLatencyVarThresholdMode', value)

	@property
	def UpstreamLatencyVariationThresholdScale(self):
		"""It is the latency variation threshold scale for upstream.

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('upstreamLatencyVariationThresholdScale')
	@UpstreamLatencyVariationThresholdScale.setter
	def UpstreamLatencyVariationThresholdScale(self, value):
		self._set_attribute('upstreamLatencyVariationThresholdScale', value)

	@property
	def UpstreamLatencyVariationThresholdValue(self):
		"""Signifies the latency variation threshold value for upstream.

		Returns:
			number
		"""
		return self._get_attribute('upstreamLatencyVariationThresholdValue')
	@UpstreamLatencyVariationThresholdValue.setter
	def UpstreamLatencyVariationThresholdValue(self, value):
		self._set_attribute('upstreamLatencyVariationThresholdValue', value)

	@property
	def UpstreamPassCriteriaLoadRateMode(self):
		"""Signifies the pass criteria load rate mode for upstream.

		Returns:
			str(average|minimum)
		"""
		return self._get_attribute('upstreamPassCriteriaLoadRateMode')
	@UpstreamPassCriteriaLoadRateMode.setter
	def UpstreamPassCriteriaLoadRateMode(self, value):
		self._set_attribute('upstreamPassCriteriaLoadRateMode', value)

	@property
	def UpstreamPassCriteriaLoadRateScale(self):
		"""Signifies pass criteria for load rate scale for upstream.

		Returns:
			str(fps|gbps|kbps|mbps|percent)
		"""
		return self._get_attribute('upstreamPassCriteriaLoadRateScale')
	@UpstreamPassCriteriaLoadRateScale.setter
	def UpstreamPassCriteriaLoadRateScale(self, value):
		self._set_attribute('upstreamPassCriteriaLoadRateScale', value)

	@property
	def UpstreamPassCriteriaLoadRateValue(self):
		"""Signifies the pass criteria load rate value for upstream.

		Returns:
			number
		"""
		return self._get_attribute('upstreamPassCriteriaLoadRateValue')
	@UpstreamPassCriteriaLoadRateValue.setter
	def UpstreamPassCriteriaLoadRateValue(self, value):
		self._set_attribute('upstreamPassCriteriaLoadRateValue', value)

	@property
	def UpstreamSeqErrorsThresholdMode(self):
		"""Signifies the sequence errors threshold mode for upstream.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('upstreamSeqErrorsThresholdMode')
	@UpstreamSeqErrorsThresholdMode.setter
	def UpstreamSeqErrorsThresholdMode(self, value):
		self._set_attribute('upstreamSeqErrorsThresholdMode', value)

	@property
	def UpstreamSeqErrorsThresholdValue(self):
		"""Signifies sequence errors threshold value for upstream.

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
			DownstreamDataErrorThresholdMode (str(average|maximum)): Signifies threshold mode for downstream data error.
			DownstreamDataErrorThresholdValue (number): Signifies the downstream data error threshold value.
			DownstreamEnableDataIntegrityPassFail (bool): if true, enables pass or faill of data integrity for downstream.
			DownstreamEnableLatencyPassFail (bool): If true, enables latency pass fail for downstream.
			DownstreamEnableRatePassFail (bool): If true, enables pass fail rate for downstream.
			DownstreamEnableSequenceErrorsPassFail (bool): If true, enables the pass fail for sequence errors for downstream.
			DownstreamEnableStandardDeviationPassFail (bool): If true, enables pass fail of standard deviation for downstream.
			DownstreamLatencyThresholdMode (str(average|maximum)): Signifies the latency threshold mode for downstream.
			DownstreamLatencyThresholdScale (str(ms|ns|us)): Signifies the threshold scale for downstream latency.
			DownstreamLatencyThresholdValue (number): Signifies the latency threshold value for downstream.
			DownstreamLatencyVarThresholdMode (str(average|maximum)): Signifies latency variation threshold mode for downstream.
			DownstreamLatencyVariationThresholdScale (str(ms|ns|us)): Signifies latency variation threshold scale for downstream.
			DownstreamLatencyVariationThresholdValue (number): Signifies the latency variation threshold value for downstream.
			DownstreamPassCriteriaLoadRateMode (str(average|minimum)): Signifies the pass criteria load rate mode for downstream.
			DownstreamPassCriteriaLoadRateScale (str(fps|gbps|kbps|mbps|percent)): Signifies the pass criteria load rate scale for downstream.
			DownstreamPassCriteriaLoadRateValue (number): Signifies pass criteria load rate value for downstream.
			DownstreamSeqErrorsThresholdMode (str(average|maximum)): Signifies the threshold mode for sequence errors for downstream.
			DownstreamSeqErrorsThresholdValue (number): Signifies the threshold value for sequence errors for downstream.
			Downstream_passFailFrequency (str(framesizes|trials)): NOT DEFINED
			UpstreamDataErrorThresholdMode (str(average|maximum)): Signifies the data error threshold mode for upstream.
			UpstreamDataErrorThresholdValue (number): Signifies data error threshold value for upstream.
			UpstreamEnableDataIntegrityPassFail (bool): If true, enables pass fail of data integrity for upstream.
			UpstreamEnableLatencyPassFail (bool): If true, enables latency pass fail for upstream.
			UpstreamEnableRatePassFail (bool): If true, enables the rate of pass fail for upstream.
			UpstreamEnableSequenceErrorsPassFail (bool): If true, enables sequence errors pass fail for upstream.
			UpstreamEnableStandardDeviationPassFail (bool): If true, enables standard deviation of pass and fail for upstream.
			UpstreamLatencyThresholdMode (str(average|maximum)): Signifies the latency threshold mode for upstream.
			UpstreamLatencyThresholdScale (str(ms|ns|us)): Signifies the latency threshold scale for upstream.
			UpstreamLatencyThresholdValue (number): It is the latency threshold value for upstream.
			UpstreamLatencyVarThresholdMode (str(average|maximum)): Signifies the latency variation threshold mode for upstream.
			UpstreamLatencyVariationThresholdScale (str(ms|ns|us)): It is the latency variation threshold scale for upstream.
			UpstreamLatencyVariationThresholdValue (number): Signifies the latency variation threshold value for upstream.
			UpstreamPassCriteriaLoadRateMode (str(average|minimum)): Signifies the pass criteria load rate mode for upstream.
			UpstreamPassCriteriaLoadRateScale (str(fps|gbps|kbps|mbps|percent)): Signifies pass criteria for load rate scale for upstream.
			UpstreamPassCriteriaLoadRateValue (number): Signifies the pass criteria load rate value for upstream.
			UpstreamSeqErrorsThresholdMode (str(average|maximum)): Signifies the sequence errors threshold mode for upstream.
			UpstreamSeqErrorsThresholdValue (number): Signifies sequence errors threshold value for upstream.
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
