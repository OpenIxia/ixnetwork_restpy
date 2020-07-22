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
    """It gives the test configuration
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'BinaryResolutionSlaveNumber': 'binaryResolutionSlaveNumber',
        'Duration': 'duration',
        'EnableSlavesPassFail': 'enableSlavesPassFail',
        'IncrementStepSlaveNumber': 'incrementStepSlaveNumber',
        'InitialBinarySlaveNumber': 'initialBinarySlaveNumber',
        'InitialStepSlaveNumber': 'initialStepSlaveNumber',
        'LoadType': 'loadType',
        'MaxBinarySlaveNumber': 'maxBinarySlaveNumber',
        'MaxOutstanding': 'maxOutstanding',
        'MaxStepSlaveNumber': 'maxStepSlaveNumber',
        'MinBinarySlaveNumber': 'minBinarySlaveNumber',
        'NumberOfSlavesPassFail': 'numberOfSlavesPassFail',
        'Numtrials': 'numtrials',
        'ProtocolItem': 'protocolItem',
        'Runmode': 'runmode',
        'SetupRate': 'setupRate',
        'StartTraffic': 'startTraffic',
        'TeardownRate': 'teardownRate',
        'UseExistingSetupRate': 'useExistingSetupRate',
    }

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def BinaryResolutionSlaveNumber(self):
        """
        Returns
        -------
        - number: Specifies the binary resolution slave number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BinaryResolutionSlaveNumber'])
    @BinaryResolutionSlaveNumber.setter
    def BinaryResolutionSlaveNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BinaryResolutionSlaveNumber'], value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: The duration of the test in hours, minutes, or seconds, which is used to calculate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])
    @Duration.setter
    def Duration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Duration'], value)

    @property
    def EnableSlavesPassFail(self):
        """
        Returns
        -------
        - str: If true, enables slaves pass fail.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSlavesPassFail'])
    @EnableSlavesPassFail.setter
    def EnableSlavesPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSlavesPassFail'], value)

    @property
    def IncrementStepSlaveNumber(self):
        """
        Returns
        -------
        - number: The incremental step value for the slave number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementStepSlaveNumber'])
    @IncrementStepSlaveNumber.setter
    def IncrementStepSlaveNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementStepSlaveNumber'], value)

    @property
    def InitialBinarySlaveNumber(self):
        """
        Returns
        -------
        - number: The initial incremental value of the binary slave number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialBinarySlaveNumber'])
    @InitialBinarySlaveNumber.setter
    def InitialBinarySlaveNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialBinarySlaveNumber'], value)

    @property
    def InitialStepSlaveNumber(self):
        """
        Returns
        -------
        - number: The initial step value of the slave number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitialStepSlaveNumber'])
    @InitialStepSlaveNumber.setter
    def InitialStepSlaveNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitialStepSlaveNumber'], value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(binary | step): The type of the payload setting.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadType'])
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadType'], value)

    @property
    def MaxBinarySlaveNumber(self):
        """
        Returns
        -------
        - number: The maximum value of the binary slave number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxBinarySlaveNumber'])
    @MaxBinarySlaveNumber.setter
    def MaxBinarySlaveNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxBinarySlaveNumber'], value)

    @property
    def MaxOutstanding(self):
        """
        Returns
        -------
        - number: The maximum oustanding value of the slave scalability.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOutstanding'])
    @MaxOutstanding.setter
    def MaxOutstanding(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxOutstanding'], value)

    @property
    def MaxStepSlaveNumber(self):
        """
        Returns
        -------
        - number: The maximum step value of the slave number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxStepSlaveNumber'])
    @MaxStepSlaveNumber.setter
    def MaxStepSlaveNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxStepSlaveNumber'], value)

    @property
    def MinBinarySlaveNumber(self):
        """
        Returns
        -------
        - number: The minimum binary value of the slave number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinBinarySlaveNumber'])
    @MinBinarySlaveNumber.setter
    def MinBinarySlaveNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinBinarySlaveNumber'], value)

    @property
    def NumberOfSlavesPassFail(self):
        """
        Returns
        -------
        - number: The number of slaves pass fail.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfSlavesPassFail'])
    @NumberOfSlavesPassFail.setter
    def NumberOfSlavesPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfSlavesPassFail'], value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: The number of trials.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

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
    def Runmode(self):
        """
        Returns
        -------
        - str(duration | noframes): It gives the run mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['Runmode'])
    @Runmode.setter
    def Runmode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Runmode'], value)

    @property
    def SetupRate(self):
        """
        Returns
        -------
        - number: The setup rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRate'])
    @SetupRate.setter
    def SetupRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRate'], value)

    @property
    def StartTraffic(self):
        """
        Returns
        -------
        - str: It starts the traffic
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartTraffic'])
    @StartTraffic.setter
    def StartTraffic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartTraffic'], value)

    @property
    def TeardownRate(self):
        """
        Returns
        -------
        - number: The teardown rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRate'])
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRate'], value)

    @property
    def UseExistingSetupRate(self):
        """
        Returns
        -------
        - bool: If True, it uses the Existing Setup rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseExistingSetupRate'])
    @UseExistingSetupRate.setter
    def UseExistingSetupRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseExistingSetupRate'], value)

    def update(self, BinaryResolutionSlaveNumber=None, Duration=None, EnableSlavesPassFail=None, IncrementStepSlaveNumber=None, InitialBinarySlaveNumber=None, InitialStepSlaveNumber=None, LoadType=None, MaxBinarySlaveNumber=None, MaxOutstanding=None, MaxStepSlaveNumber=None, MinBinarySlaveNumber=None, NumberOfSlavesPassFail=None, Numtrials=None, ProtocolItem=None, Runmode=None, SetupRate=None, StartTraffic=None, TeardownRate=None, UseExistingSetupRate=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - BinaryResolutionSlaveNumber (number): Specifies the binary resolution slave number.
        - Duration (number): The duration of the test in hours, minutes, or seconds, which is used to calculate.
        - EnableSlavesPassFail (str): If true, enables slaves pass fail.
        - IncrementStepSlaveNumber (number): The incremental step value for the slave number.
        - InitialBinarySlaveNumber (number): The initial incremental value of the binary slave number.
        - InitialStepSlaveNumber (number): The initial step value of the slave number.
        - LoadType (str(binary | step)): The type of the payload setting.
        - MaxBinarySlaveNumber (number): The maximum value of the binary slave number.
        - MaxOutstanding (number): The maximum oustanding value of the slave scalability.
        - MaxStepSlaveNumber (number): The maximum step value of the slave number.
        - MinBinarySlaveNumber (number): The minimum binary value of the slave number.
        - NumberOfSlavesPassFail (number): The number of slaves pass fail.
        - Numtrials (number): The number of trials.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - Runmode (str(duration | noframes)): It gives the run mode
        - SetupRate (number): The setup rate.
        - StartTraffic (str): It starts the traffic
        - TeardownRate (number): The teardown rate.
        - UseExistingSetupRate (bool): If True, it uses the Existing Setup rate

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
