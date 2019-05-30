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
	def FastPathEnable(self):
		"""If true, the fast path is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('fastPathEnable')
	@FastPathEnable.setter
	def FastPathEnable(self, value):
		self._set_attribute('fastPathEnable', value)

	@property
	def FastPathLearnFrameSize(self):
		"""Specifies the size of the learning frames in the fast path.

		Returns:
			number
		"""
		return self._get_attribute('fastPathLearnFrameSize')
	@FastPathLearnFrameSize.setter
	def FastPathLearnFrameSize(self, value):
		self._set_attribute('fastPathLearnFrameSize', value)

	@property
	def FastPathNumFrames(self):
		"""Specifies the number of learn frames that IxNetwork sends through fast path.

		Returns:
			number
		"""
		return self._get_attribute('fastPathNumFrames')
	@FastPathNumFrames.setter
	def FastPathNumFrames(self, value):
		self._set_attribute('fastPathNumFrames', value)

	@property
	def FastPathRate(self):
		"""The learnt information on the rate the data is to be transferred.

		Returns:
			number
		"""
		return self._get_attribute('fastPathRate')
	@FastPathRate.setter
	def FastPathRate(self, value):
		self._set_attribute('fastPathRate', value)

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
			str(never|onBinaryIteration|oncePerFramesize|oncePerTest|onTrial)
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
	def LearnSendMacOnly(self):
		"""If true, the learnt information on the MAC address is sent.

		Returns:
			bool
		"""
		return self._get_attribute('learnSendMacOnly')
	@LearnSendMacOnly.setter
	def LearnSendMacOnly(self, value):
		self._set_attribute('learnSendMacOnly', value)

	@property
	def LearnSendRouterSolicitation(self):
		"""If true, the learnt information on the router sends solicitation.

		Returns:
			bool
		"""
		return self._get_attribute('learnSendRouterSolicitation')
	@LearnSendRouterSolicitation.setter
	def LearnSendRouterSolicitation(self, value):
		self._set_attribute('learnSendRouterSolicitation', value)

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

	def update(self, FastPathEnable=None, FastPathLearnFrameSize=None, FastPathNumFrames=None, FastPathRate=None, LearnFrameSize=None, LearnFrequency=None, LearnNumFrames=None, LearnRate=None, LearnSendMacOnly=None, LearnSendRouterSolicitation=None, LearnWaitTime=None, LearnWaitTimeBeforeTransmit=None):
		"""Updates a child instance of learnFrames on the server.

		Args:
			FastPathEnable (bool): If true, the fast path is enabled.
			FastPathLearnFrameSize (number): Specifies the size of the learning frames in the fast path.
			FastPathNumFrames (number): Specifies the number of learn frames that IxNetwork sends through fast path.
			FastPathRate (number): The learnt information on the rate the data is to be transferred.
			LearnFrameSize (number): Specifies the size of the learning frames.
			LearnFrequency (str(never|onBinaryIteration|oncePerFramesize|oncePerTest|onTrial)): Allows to choose how frequently IxNetwork sends learning frames during the test.
			LearnNumFrames (number): Specifies the number of learning frames that IxNetwork sends for each address.
			LearnRate (number): Specifies the rate at which IxNetwork sends learn frames to the DUT.
			LearnSendMacOnly (bool): If true, the learnt information on the MAC address is sent.
			LearnSendRouterSolicitation (bool): If true, the learnt information on the router sends solicitation.
			LearnWaitTime (number): Specifies the length of time in ms that IxNetwork pauses before sending all the learning frames from all the ports.
			LearnWaitTimeBeforeTransmit (number): The time in ms that IxNetwork waits before sending all the learning frames from all the ports.

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
