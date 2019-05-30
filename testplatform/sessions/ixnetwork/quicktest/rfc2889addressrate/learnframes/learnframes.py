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


class LearnFrames(Base):
	"""The LearnFrames class encapsulates a required learnFrames node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the LearnFrames property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'learnFrames'

	def __init__(self, parent):
		super(LearnFrames, self).__init__(parent)

	@property
	def LearnFrameSize(self):
		"""Specifies the size of the learning frames.

		Returns:
			number
		"""
		return self._get_attribute('learnFrameSize')
	@LearnFrameSize.setter
	def LearnFrameSize(self, value):
		self._set_attribute('learnFrameSize', value)

	@property
	def LearnFrequency(self):
		"""Allows to choose how frequently IxNetwork sends learning frames during the test.

		Returns:
			str(onBinaryIteration)
		"""
		return self._get_attribute('learnFrequency')
	@LearnFrequency.setter
	def LearnFrequency(self, value):
		self._set_attribute('learnFrequency', value)

	@property
	def LearnNumFrames(self):
		"""Specifies the number of learning frames that IxNetwork sends for each address.

		Returns:
			number
		"""
		return self._get_attribute('learnNumFrames')
	@LearnNumFrames.setter
	def LearnNumFrames(self, value):
		self._set_attribute('learnNumFrames', value)

	@property
	def LearnRate(self):
		"""Specifies the rate at which IxNetwork sends learn frames to the DUT.

		Returns:
			number
		"""
		return self._get_attribute('learnRate')
	@LearnRate.setter
	def LearnRate(self, value):
		self._set_attribute('learnRate', value)

	@property
	def LearnWaitTime(self):
		"""Specifies the length of time in ms that IxNetwork pauses before sending all the learning frames from all the ports.

		Returns:
			number
		"""
		return self._get_attribute('learnWaitTime')
	@LearnWaitTime.setter
	def LearnWaitTime(self, value):
		self._set_attribute('learnWaitTime', value)

	@property
	def LearnWaitTimeBeforeTransmit(self):
		"""The time in ms that IxNetwork waits before sending all the learning frames from all the ports.

		Returns:
			number
		"""
		return self._get_attribute('learnWaitTimeBeforeTransmit')
	@LearnWaitTimeBeforeTransmit.setter
	def LearnWaitTimeBeforeTransmit(self, value):
		self._set_attribute('learnWaitTimeBeforeTransmit', value)

	@property
	def LearningCountRandomFrameSize(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('learningCountRandomFrameSize')
	@LearningCountRandomFrameSize.setter
	def LearningCountRandomFrameSize(self, value):
		self._set_attribute('learningCountRandomFrameSize', value)

	@property
	def LearningFrameSizeMode(self):
		"""NOT DEFINED

		Returns:
			str(custom|fixed|increment|random)
		"""
		return self._get_attribute('learningFrameSizeMode')
	@LearningFrameSizeMode.setter
	def LearningFrameSizeMode(self, value):
		self._set_attribute('learningFrameSizeMode', value)

	@property
	def LearningFramesizeFixedValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('learningFramesizeFixedValue')
	@LearningFramesizeFixedValue.setter
	def LearningFramesizeFixedValue(self, value):
		self._set_attribute('learningFramesizeFixedValue', value)

	@property
	def LearningFramesizeList(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('learningFramesizeList')
	@LearningFramesizeList.setter
	def LearningFramesizeList(self, value):
		self._set_attribute('learningFramesizeList', value)

	@property
	def LearningMaxIncrementFrameSize(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('learningMaxIncrementFrameSize')
	@LearningMaxIncrementFrameSize.setter
	def LearningMaxIncrementFrameSize(self, value):
		self._set_attribute('learningMaxIncrementFrameSize', value)

	@property
	def LearningMaxRandomFrameSize(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('learningMaxRandomFrameSize')
	@LearningMaxRandomFrameSize.setter
	def LearningMaxRandomFrameSize(self, value):
		self._set_attribute('learningMaxRandomFrameSize', value)

	@property
	def LearningMinIncrementFrameSize(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('learningMinIncrementFrameSize')
	@LearningMinIncrementFrameSize.setter
	def LearningMinIncrementFrameSize(self, value):
		self._set_attribute('learningMinIncrementFrameSize', value)

	@property
	def LearningMinRandomFrameSize(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('learningMinRandomFrameSize')
	@LearningMinRandomFrameSize.setter
	def LearningMinRandomFrameSize(self, value):
		self._set_attribute('learningMinRandomFrameSize', value)

	@property
	def LearningStepIncrementFrameSize(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('learningStepIncrementFrameSize')
	@LearningStepIncrementFrameSize.setter
	def LearningStepIncrementFrameSize(self, value):
		self._set_attribute('learningStepIncrementFrameSize', value)

	def update(self, LearnFrameSize=None, LearnFrequency=None, LearnNumFrames=None, LearnRate=None, LearnWaitTime=None, LearnWaitTimeBeforeTransmit=None, LearningCountRandomFrameSize=None, LearningFrameSizeMode=None, LearningFramesizeFixedValue=None, LearningFramesizeList=None, LearningMaxIncrementFrameSize=None, LearningMaxRandomFrameSize=None, LearningMinIncrementFrameSize=None, LearningMinRandomFrameSize=None, LearningStepIncrementFrameSize=None):
		"""Updates a child instance of learnFrames on the server.

		Args:
			LearnFrameSize (number): Specifies the size of the learning frames.
			LearnFrequency (str(onBinaryIteration)): Allows to choose how frequently IxNetwork sends learning frames during the test.
			LearnNumFrames (number): Specifies the number of learning frames that IxNetwork sends for each address.
			LearnRate (number): Specifies the rate at which IxNetwork sends learn frames to the DUT.
			LearnWaitTime (number): Specifies the length of time in ms that IxNetwork pauses before sending all the learning frames from all the ports.
			LearnWaitTimeBeforeTransmit (number): The time in ms that IxNetwork waits before sending all the learning frames from all the ports.
			LearningCountRandomFrameSize (str): NOT DEFINED
			LearningFrameSizeMode (str(custom|fixed|increment|random)): NOT DEFINED
			LearningFramesizeFixedValue (number): NOT DEFINED
			LearningFramesizeList (str): NOT DEFINED
			LearningMaxIncrementFrameSize (str): NOT DEFINED
			LearningMaxRandomFrameSize (str): NOT DEFINED
			LearningMinIncrementFrameSize (str): NOT DEFINED
			LearningMinRandomFrameSize (str): NOT DEFINED
			LearningStepIncrementFrameSize (str): NOT DEFINED

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
