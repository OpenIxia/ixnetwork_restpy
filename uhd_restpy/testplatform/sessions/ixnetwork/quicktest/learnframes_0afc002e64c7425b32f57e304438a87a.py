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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class LearnFrames(Base):
    """The learning frames that IxNetwork sends during the test.
    The LearnFrames class encapsulates a required learnFrames resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'learnFrames'
    _SDM_ATT_MAP = {
        'FastPathEnable': 'fastPathEnable',
        'FastPathLearnFrameSize': 'fastPathLearnFrameSize',
        'FastPathNumFrames': 'fastPathNumFrames',
        'FastPathRate': 'fastPathRate',
        'LearnFrameSize': 'learnFrameSize',
        'LearnFrequency': 'learnFrequency',
        'LearnNumFrames': 'learnNumFrames',
        'LearnRate': 'learnRate',
        'LearnSendMacOnly': 'learnSendMacOnly',
        'LearnSendRouterSolicitation': 'learnSendRouterSolicitation',
        'LearnWaitTime': 'learnWaitTime',
        'LearnWaitTimeBeforeTransmit': 'learnWaitTimeBeforeTransmit',
    }

    def __init__(self, parent):
        super(LearnFrames, self).__init__(parent)

    @property
    def FastPathEnable(self):
        """
        Returns
        -------
        - bool: If true, the fast path is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastPathEnable'])
    @FastPathEnable.setter
    def FastPathEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastPathEnable'], value)

    @property
    def FastPathLearnFrameSize(self):
        """
        Returns
        -------
        - number: The path in which the learnt frame sizes are saved.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastPathLearnFrameSize'])
    @FastPathLearnFrameSize.setter
    def FastPathLearnFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastPathLearnFrameSize'], value)

    @property
    def FastPathNumFrames(self):
        """
        Returns
        -------
        - number: The learnt information on the number of frames to be tramsferred.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastPathNumFrames'])
    @FastPathNumFrames.setter
    def FastPathNumFrames(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastPathNumFrames'], value)

    @property
    def FastPathRate(self):
        """
        Returns
        -------
        - number: The learnt inofrmation on the rate the data is to be transferred.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FastPathRate'])
    @FastPathRate.setter
    def FastPathRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FastPathRate'], value)

    @property
    def LearnFrameSize(self):
        """
        Returns
        -------
        - number: The learnt information on frame size.
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
        - str(never | onBinaryIteration | oncePerFramesize | oncePerTest | onTrial): Allows to choose how frequently IxNetwork sends learning frames during the test.
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
        - number: The frequency at which number of frames are to be learnt.
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
        - number: The rate at which the data is to be learnt.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnRate'])
    @LearnRate.setter
    def LearnRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnRate'], value)

    @property
    def LearnSendMacOnly(self):
        """
        Returns
        -------
        - bool: The learnt information on the MAC address sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnSendMacOnly'])
    @LearnSendMacOnly.setter
    def LearnSendMacOnly(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnSendMacOnly'], value)

    @property
    def LearnSendRouterSolicitation(self):
        """
        Returns
        -------
        - bool: The learnt information on the router sent solicitation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnSendRouterSolicitation'])
    @LearnSendRouterSolicitation.setter
    def LearnSendRouterSolicitation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnSendRouterSolicitation'], value)

    @property
    def LearnWaitTime(self):
        """
        Returns
        -------
        - number: The learnt information on the wait time.
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
        - number: The learnt wait time before transmitting.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnWaitTimeBeforeTransmit'])
    @LearnWaitTimeBeforeTransmit.setter
    def LearnWaitTimeBeforeTransmit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LearnWaitTimeBeforeTransmit'], value)

    def update(self, FastPathEnable=None, FastPathLearnFrameSize=None, FastPathNumFrames=None, FastPathRate=None, LearnFrameSize=None, LearnFrequency=None, LearnNumFrames=None, LearnRate=None, LearnSendMacOnly=None, LearnSendRouterSolicitation=None, LearnWaitTime=None, LearnWaitTimeBeforeTransmit=None):
        """Updates learnFrames resource on the server.

        Args
        ----
        - FastPathEnable (bool): If true, the fast path is enabled.
        - FastPathLearnFrameSize (number): The path in which the learnt frame sizes are saved.
        - FastPathNumFrames (number): The learnt information on the number of frames to be tramsferred.
        - FastPathRate (number): The learnt inofrmation on the rate the data is to be transferred.
        - LearnFrameSize (number): The learnt information on frame size.
        - LearnFrequency (str(never | onBinaryIteration | oncePerFramesize | oncePerTest | onTrial)): Allows to choose how frequently IxNetwork sends learning frames during the test.
        - LearnNumFrames (number): The frequency at which number of frames are to be learnt.
        - LearnRate (number): The rate at which the data is to be learnt.
        - LearnSendMacOnly (bool): The learnt information on the MAC address sent.
        - LearnSendRouterSolicitation (bool): The learnt information on the router sent solicitation.
        - LearnWaitTime (number): The learnt information on the wait time.
        - LearnWaitTimeBeforeTransmit (number): The learnt wait time before transmitting.

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
