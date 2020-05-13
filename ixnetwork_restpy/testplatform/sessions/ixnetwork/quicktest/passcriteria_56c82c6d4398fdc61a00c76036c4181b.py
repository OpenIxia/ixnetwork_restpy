# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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
    """
    The PassCriteria class encapsulates a required passCriteria resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'passCriteria'
    _SDM_ATT_MAP = {
        'CpDpConvergenceFactorScale': 'cpDpConvergenceFactorScale',
        'CpDpConvergenceTime': 'cpDpConvergenceTime',
        'EnableCpDpPassFail': 'enableCpDpPassFail',
        'EnablePacketLossDurationPassFail': 'enablePacketLossDurationPassFail',
        'EnablePassFail': 'enablePassFail',
        'PacketLossDurationConvergenceTime': 'packetLossDurationConvergenceTime',
        'PacketLossDurationFactorScale': 'packetLossDurationFactorScale',
        'PassFailFrequency': 'passFailFrequency',
    }

    def __init__(self, parent):
        super(PassCriteria, self).__init__(parent)

    @property
    def CpDpConvergenceFactorScale(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CpDpConvergenceFactorScale'])
    @CpDpConvergenceFactorScale.setter
    def CpDpConvergenceFactorScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CpDpConvergenceFactorScale'], value)

    @property
    def CpDpConvergenceTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CpDpConvergenceTime'])
    @CpDpConvergenceTime.setter
    def CpDpConvergenceTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CpDpConvergenceTime'], value)

    @property
    def EnableCpDpPassFail(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCpDpPassFail'])
    @EnableCpDpPassFail.setter
    def EnableCpDpPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCpDpPassFail'], value)

    @property
    def EnablePacketLossDurationPassFail(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePacketLossDurationPassFail'])
    @EnablePacketLossDurationPassFail.setter
    def EnablePacketLossDurationPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePacketLossDurationPassFail'], value)

    @property
    def EnablePassFail(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePassFail'])
    @EnablePassFail.setter
    def EnablePassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePassFail'], value)

    @property
    def PacketLossDurationConvergenceTime(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketLossDurationConvergenceTime'])
    @PacketLossDurationConvergenceTime.setter
    def PacketLossDurationConvergenceTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketLossDurationConvergenceTime'], value)

    @property
    def PacketLossDurationFactorScale(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketLossDurationFactorScale'])
    @PacketLossDurationFactorScale.setter
    def PacketLossDurationFactorScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketLossDurationFactorScale'], value)

    @property
    def PassFailFrequency(self):
        """
        Returns
        -------
        - str(iteration): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PassFailFrequency'])
    @PassFailFrequency.setter
    def PassFailFrequency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PassFailFrequency'], value)

    def update(self, CpDpConvergenceFactorScale=None, CpDpConvergenceTime=None, EnableCpDpPassFail=None, EnablePacketLossDurationPassFail=None, EnablePassFail=None, PacketLossDurationConvergenceTime=None, PacketLossDurationFactorScale=None, PassFailFrequency=None):
        """Updates passCriteria resource on the server.

        Args
        ----
        - CpDpConvergenceFactorScale (str): 
        - CpDpConvergenceTime (number): 
        - EnableCpDpPassFail (bool): 
        - EnablePacketLossDurationPassFail (bool): 
        - EnablePassFail (bool): 
        - PacketLossDurationConvergenceTime (number): 
        - PacketLossDurationFactorScale (str): 
        - PassFailFrequency (str(iteration)): 

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
