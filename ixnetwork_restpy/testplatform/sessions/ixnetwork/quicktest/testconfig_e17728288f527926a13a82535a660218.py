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
    """Test configuration
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'CorrectionFactorMode': 'correctionFactorMode',
        'CorrectionFactorScale': 'correctionFactorScale',
        'Duration': 'duration',
        'EnableCorrectionFactorPassFail': 'enableCorrectionFactorPassFail',
        'MaxOutstanding': 'maxOutstanding',
        'MeasuredResidenceTime': 'measuredResidenceTime',
        'NumberCorrectionFactorPassFail': 'numberCorrectionFactorPassFail',
        'Numtrials': 'numtrials',
        'OffsetGraph': 'offsetGraph',
        'PathDelayGraphing': 'pathDelayGraphing',
        'ProtocolItem': 'protocolItem',
        'ResidenceTime': 'residenceTime',
        'Runmode': 'runmode',
        'SetupRate': 'setupRate',
        'StartTraffic': 'startTraffic',
        'TeardownRate': 'teardownRate',
        'TestConfiguration': 'testConfiguration',
        'UseExistingSetupRate': 'useExistingSetupRate',
    }

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def CorrectionFactorMode(self):
        """
        Returns
        -------
        - str: Correction Factor mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['CorrectionFactorMode'])
    @CorrectionFactorMode.setter
    def CorrectionFactorMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CorrectionFactorMode'], value)

    @property
    def CorrectionFactorScale(self):
        """
        Returns
        -------
        - str: Correction Factor Scale
        """
        return self._get_attribute(self._SDM_ATT_MAP['CorrectionFactorScale'])
    @CorrectionFactorScale.setter
    def CorrectionFactorScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CorrectionFactorScale'], value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: The wait time in hours, minutes, and seconds, that is required for the PTP protocol to negotiate
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])
    @Duration.setter
    def Duration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Duration'], value)

    @property
    def EnableCorrectionFactorPassFail(self):
        """
        Returns
        -------
        - str: If selected, a Pass/Fail criteria is applied to the Correction Factor Error test
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCorrectionFactorPassFail'])
    @EnableCorrectionFactorPassFail.setter
    def EnableCorrectionFactorPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCorrectionFactorPassFail'], value)

    @property
    def MaxOutstanding(self):
        """
        Returns
        -------
        - number: Maximum number of connection requests or tear down requests that can be pending at any one time
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOutstanding'])
    @MaxOutstanding.setter
    def MaxOutstanding(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxOutstanding'], value)

    @property
    def MeasuredResidenceTime(self):
        """
        Returns
        -------
        - str: The measured time taken by a packet to move from the ingress port to the egress port
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeasuredResidenceTime'])
    @MeasuredResidenceTime.setter
    def MeasuredResidenceTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MeasuredResidenceTime'], value)

    @property
    def NumberCorrectionFactorPassFail(self):
        """
        Returns
        -------
        - number: Number of criteria used for Pass/Fail
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberCorrectionFactorPassFail'])
    @NumberCorrectionFactorPassFail.setter
    def NumberCorrectionFactorPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberCorrectionFactorPassFail'], value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: The number of trials that can be run
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def OffsetGraph(self):
        """
        Returns
        -------
        - str: Offset graphing
        """
        return self._get_attribute(self._SDM_ATT_MAP['OffsetGraph'])
    @OffsetGraph.setter
    def OffsetGraph(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OffsetGraph'], value)

    @property
    def PathDelayGraphing(self):
        """
        Returns
        -------
        - str: Graphing of path delay
        """
        return self._get_attribute(self._SDM_ATT_MAP['PathDelayGraphing'])
    @PathDelayGraphing.setter
    def PathDelayGraphing(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PathDelayGraphing'], value)

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
    def ResidenceTime(self):
        """
        Returns
        -------
        - number: The time taken by a packet to move from the ingress port to the egress port
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResidenceTime'])
    @ResidenceTime.setter
    def ResidenceTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ResidenceTime'], value)

    @property
    def Runmode(self):
        """
        Returns
        -------
        - str(duration | noframes): Running mode used
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
        - number: The number of PTP connections to be initiated per second
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
        - str: All traffic configured in IxNetwork is initiated on running this test
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
        - number: The number of PTP connections to tear down per second
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRate'])
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRate'], value)

    @property
    def TestConfiguration(self):
        """
        Returns
        -------
        - str: Test configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestConfiguration'])
    @TestConfiguration.setter
    def TestConfiguration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestConfiguration'], value)

    @property
    def UseExistingSetupRate(self):
        """
        Returns
        -------
        - bool: The current setup rate value is used
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseExistingSetupRate'])
    @UseExistingSetupRate.setter
    def UseExistingSetupRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseExistingSetupRate'], value)

    def update(self, CorrectionFactorMode=None, CorrectionFactorScale=None, Duration=None, EnableCorrectionFactorPassFail=None, MaxOutstanding=None, MeasuredResidenceTime=None, NumberCorrectionFactorPassFail=None, Numtrials=None, OffsetGraph=None, PathDelayGraphing=None, ProtocolItem=None, ResidenceTime=None, Runmode=None, SetupRate=None, StartTraffic=None, TeardownRate=None, TestConfiguration=None, UseExistingSetupRate=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - CorrectionFactorMode (str): Correction Factor mode
        - CorrectionFactorScale (str): Correction Factor Scale
        - Duration (number): The wait time in hours, minutes, and seconds, that is required for the PTP protocol to negotiate
        - EnableCorrectionFactorPassFail (str): If selected, a Pass/Fail criteria is applied to the Correction Factor Error test
        - MaxOutstanding (number): Maximum number of connection requests or tear down requests that can be pending at any one time
        - MeasuredResidenceTime (str): The measured time taken by a packet to move from the ingress port to the egress port
        - NumberCorrectionFactorPassFail (number): Number of criteria used for Pass/Fail
        - Numtrials (number): The number of trials that can be run
        - OffsetGraph (str): Offset graphing
        - PathDelayGraphing (str): Graphing of path delay
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - ResidenceTime (number): The time taken by a packet to move from the ingress port to the egress port
        - Runmode (str(duration | noframes)): Running mode used
        - SetupRate (number): The number of PTP connections to be initiated per second
        - StartTraffic (str): All traffic configured in IxNetwork is initiated on running this test
        - TeardownRate (number): The number of PTP connections to tear down per second
        - TestConfiguration (str): Test configuration
        - UseExistingSetupRate (bool): The current setup rate value is used

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
