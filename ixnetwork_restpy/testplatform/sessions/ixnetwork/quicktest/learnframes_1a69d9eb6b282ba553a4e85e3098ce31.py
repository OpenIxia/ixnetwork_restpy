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


class LearnFrames(Base):
    """The learning frames that IxNetwork sends during the test.
    The LearnFrames class encapsulates a required learnFrames resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'learnFrames'
    _SDM_ATT_MAP = {
        'LearnFrameSize': 'learnFrameSize',
        'LearnFrequency': 'learnFrequency',
        'LearnNumFrames': 'learnNumFrames',
        'LearnRate': 'learnRate',
        'LearnWaitTime': 'learnWaitTime',
        'LearnWaitTimeBeforeTransmit': 'learnWaitTimeBeforeTransmit',
        'LearningCountRandomFrameSize': 'learningCountRandomFrameSize',
        'LearningFrameSizeMode': 'learningFrameSizeMode',
        'LearningFramesizeFixedValue': 'learningFramesizeFixedValue',
        'LearningFramesizeList': 'learningFramesizeList',
        'LearningMaxIncrementFrameSize': 'learningMaxIncrementFrameSize',
        'LearningMaxRandomFrameSize': 'learningMaxRandomFrameSize',
        'LearningMinIncrementFrameSize': 'learningMinIncrementFrameSize',
        'LearningMinRandomFrameSize': 'learningMinRandomFrameSize',
        'LearningStepIncrementFrameSize': 'learningStepIncrementFrameSize',
    }

    def __init__(self, parent):
        super(LearnFrames, self).__init__(parent)

    @property
    def LearnFrameSize(self):
        """
        Returns
        -------
        - number: Specifies the size of the learning frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnFrameSize'])
    @LearnFrameSize.setter
    def LearnFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnFrameSize'], value)

    @property
    def LearnFrequency(self):
        """
        Returns
        -------
        - str(onBinaryIteration): Allows to choose how frequently IxNetwork sends learning frames during the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnFrequency'])
    @LearnFrequency.setter
    def LearnFrequency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnFrequency'], value)

    @property
    def LearnNumFrames(self):
        """
        Returns
        -------
        - number: Specifies the number of learning frames that IxNetwork sends for each address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnNumFrames'])
    @LearnNumFrames.setter
    def LearnNumFrames(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnNumFrames'], value)

    @property
    def LearnRate(self):
        """
        Returns
        -------
        - number: Specifies the rate at which IxNetwork sends learn frames to the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnRate'])
    @LearnRate.setter
    def LearnRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnRate'], value)

    @property
    def LearnWaitTime(self):
        """
        Returns
        -------
        - number: Specifies the length of time in ms that IxNetwork pauses before sending all the learning frames from all the ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnWaitTime'])
    @LearnWaitTime.setter
    def LearnWaitTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnWaitTime'], value)

    @property
    def LearnWaitTimeBeforeTransmit(self):
        """
        Returns
        -------
        - number: The time in ms that IxNetwork waits before sending all the learning frames from all the ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnWaitTimeBeforeTransmit'])
    @LearnWaitTimeBeforeTransmit.setter
    def LearnWaitTimeBeforeTransmit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnWaitTimeBeforeTransmit'], value)

    @property
    def LearningCountRandomFrameSize(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearningCountRandomFrameSize'])
    @LearningCountRandomFrameSize.setter
    def LearningCountRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearningCountRandomFrameSize'], value)

    @property
    def LearningFrameSizeMode(self):
        """
        Returns
        -------
        - str(custom | fixed | increment | random): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearningFrameSizeMode'])
    @LearningFrameSizeMode.setter
    def LearningFrameSizeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearningFrameSizeMode'], value)

    @property
    def LearningFramesizeFixedValue(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearningFramesizeFixedValue'])
    @LearningFramesizeFixedValue.setter
    def LearningFramesizeFixedValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearningFramesizeFixedValue'], value)

    @property
    def LearningFramesizeList(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearningFramesizeList'])
    @LearningFramesizeList.setter
    def LearningFramesizeList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearningFramesizeList'], value)

    @property
    def LearningMaxIncrementFrameSize(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearningMaxIncrementFrameSize'])
    @LearningMaxIncrementFrameSize.setter
    def LearningMaxIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearningMaxIncrementFrameSize'], value)

    @property
    def LearningMaxRandomFrameSize(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearningMaxRandomFrameSize'])
    @LearningMaxRandomFrameSize.setter
    def LearningMaxRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearningMaxRandomFrameSize'], value)

    @property
    def LearningMinIncrementFrameSize(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearningMinIncrementFrameSize'])
    @LearningMinIncrementFrameSize.setter
    def LearningMinIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearningMinIncrementFrameSize'], value)

    @property
    def LearningMinRandomFrameSize(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearningMinRandomFrameSize'])
    @LearningMinRandomFrameSize.setter
    def LearningMinRandomFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearningMinRandomFrameSize'], value)

    @property
    def LearningStepIncrementFrameSize(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearningStepIncrementFrameSize'])
    @LearningStepIncrementFrameSize.setter
    def LearningStepIncrementFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearningStepIncrementFrameSize'], value)

    def update(self, LearnFrameSize=None, LearnFrequency=None, LearnNumFrames=None, LearnRate=None, LearnWaitTime=None, LearnWaitTimeBeforeTransmit=None, LearningCountRandomFrameSize=None, LearningFrameSizeMode=None, LearningFramesizeFixedValue=None, LearningFramesizeList=None, LearningMaxIncrementFrameSize=None, LearningMaxRandomFrameSize=None, LearningMinIncrementFrameSize=None, LearningMinRandomFrameSize=None, LearningStepIncrementFrameSize=None):
        """Updates learnFrames resource on the server.

        Args
        ----
        - LearnFrameSize (number): Specifies the size of the learning frames.
        - LearnFrequency (str(onBinaryIteration)): Allows to choose how frequently IxNetwork sends learning frames during the test.
        - LearnNumFrames (number): Specifies the number of learning frames that IxNetwork sends for each address.
        - LearnRate (number): Specifies the rate at which IxNetwork sends learn frames to the DUT.
        - LearnWaitTime (number): Specifies the length of time in ms that IxNetwork pauses before sending all the learning frames from all the ports.
        - LearnWaitTimeBeforeTransmit (number): The time in ms that IxNetwork waits before sending all the learning frames from all the ports.
        - LearningCountRandomFrameSize (str): NOT DEFINED
        - LearningFrameSizeMode (str(custom | fixed | increment | random)): NOT DEFINED
        - LearningFramesizeFixedValue (number): NOT DEFINED
        - LearningFramesizeList (str): NOT DEFINED
        - LearningMaxIncrementFrameSize (str): NOT DEFINED
        - LearningMaxRandomFrameSize (str): NOT DEFINED
        - LearningMinIncrementFrameSize (str): NOT DEFINED
        - LearningMinRandomFrameSize (str): NOT DEFINED
        - LearningStepIncrementFrameSize (str): NOT DEFINED

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
