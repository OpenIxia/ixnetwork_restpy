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


class QuickTest(Base):
    """The IxNetwork QuickTests feature provides the ability to run predefined tests.
    The QuickTest class encapsulates a required quickTest resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'quickTest'
    _SDM_ATT_MAP = {
        'RunningTest': 'runningTest',
        'RunningTestObj': 'runningTestObj',
        'TestIds': 'testIds',
    }

    def __init__(self, parent):
        super(QuickTest, self).__init__(parent)

    @property
    def Globals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.globals_189e36988976210137e69f36458134c2.Globals): An instance of the Globals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.globals_189e36988976210137e69f36458134c2 import Globals
        return Globals(self)._select()

    @property
    def Rfc2544back2back(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_98477f12f665b89fbc05f63bb31ee827.Rfc2544back2back): An instance of the Rfc2544back2back class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_98477f12f665b89fbc05f63bb31ee827 import Rfc2544back2back
        return Rfc2544back2back(self)

    @property
    def Rfc2544frameLoss(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_f6a794f7d6a00f8572021fc418d8807f.Rfc2544frameLoss): An instance of the Rfc2544frameLoss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_f6a794f7d6a00f8572021fc418d8807f import Rfc2544frameLoss
        return Rfc2544frameLoss(self)

    @property
    def Rfc2544throughput(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_5a77c9a28f5fa2bb9ce9f4280eb5122f.Rfc2544throughput): An instance of the Rfc2544throughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_5a77c9a28f5fa2bb9ce9f4280eb5122f import Rfc2544throughput
        return Rfc2544throughput(self)

    @property
    def TrafficTest(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_9709f3566877e5d5fb6ae115268058c6.TrafficTest): An instance of the TrafficTest class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_9709f3566877e5d5fb6ae115268058c6 import TrafficTest
        return TrafficTest(self)

    @property
    def RunningTest(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/7/ixnetwork/quickTest/.../*]): Returns list containing the currently running QuickTest
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningTest'])

    @property
    def RunningTestObj(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/7/ixnetwork/quickTest/.../*]): Returns list containing the currently running QuickTest
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningTestObj'])

    @property
    def TestIds(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/7/ixnetwork/quickTest/.../*]): Returns list containing the QuickTest test in the configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestIds'])

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

    def LoadBatchFile(self, *args, **kwargs):
        """Executes the loadBatchFile operation on the server.

        Loads the given batch file with all the results of the old quick test.

        loadBatchFile(Arg2=string)
        --------------------------
        - Arg2 (str): Exact path to the batch xml.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('loadBatchFile', payload=payload, response_object=None)

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
