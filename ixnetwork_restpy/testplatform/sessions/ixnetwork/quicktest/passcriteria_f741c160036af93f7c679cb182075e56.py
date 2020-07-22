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


class PassCriteria(Base):
    """The pass criteria for the cloud performance.
    The PassCriteria class encapsulates a required passCriteria resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'passCriteria'
    _SDM_ATT_MAP = {
        'DataErrorThresholdValue': 'dataErrorThresholdValue',
        'EnableDataIntegrityPassFail': 'enableDataIntegrityPassFail',
        'EnableLatencyPassFail': 'enableLatencyPassFail',
        'EnablePassFail': 'enablePassFail',
        'EnableRatePassFail': 'enableRatePassFail',
        'EnableSequenceErrorsPassFail': 'enableSequenceErrorsPassFail',
        'EnableStandardDeviationPassFail': 'enableStandardDeviationPassFail',
        'LatencyThresholdMode': 'latencyThresholdMode',
        'LatencyThresholdScale': 'latencyThresholdScale',
        'LatencyThresholdValue': 'latencyThresholdValue',
        'LatencyVarThresholdMode': 'latencyVarThresholdMode',
        'LatencyVariationThresholdScale': 'latencyVariationThresholdScale',
        'LatencyVariationThresholdValue': 'latencyVariationThresholdValue',
        'PassCriteriaLoadRateScale': 'passCriteriaLoadRateScale',
        'PassCriteriaLoadRateValue': 'passCriteriaLoadRateValue',
        'SeqErrorsThresholdValue': 'seqErrorsThresholdValue',
    }

    def __init__(self, parent):
        super(PassCriteria, self).__init__(parent)

    @property
    def DataErrorThresholdValue(self):
        """
        Returns
        -------
        - number: The data error of the threshold value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataErrorThresholdValue'])
    @DataErrorThresholdValue.setter
    def DataErrorThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DataErrorThresholdValue'], value)

    @property
    def EnableDataIntegrityPassFail(self):
        """
        Returns
        -------
        - bool: If true, that data integrity of the pass or fail criteria is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDataIntegrityPassFail'])
    @EnableDataIntegrityPassFail.setter
    def EnableDataIntegrityPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDataIntegrityPassFail'], value)

    @property
    def EnableLatencyPassFail(self):
        """
        Returns
        -------
        - bool: If true, the latency is enabled for pass fail.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLatencyPassFail'])
    @EnableLatencyPassFail.setter
    def EnableLatencyPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLatencyPassFail'], value)

    @property
    def EnablePassFail(self):
        """
        Returns
        -------
        - bool: If true, IxNetwork applies the Pass Criteria to each trial in the test and determineswhether the trial passed or failed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePassFail'])
    @EnablePassFail.setter
    def EnablePassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePassFail'], value)

    @property
    def EnableRatePassFail(self):
        """
        Returns
        -------
        - bool: If true, the rate of pass fail is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRatePassFail'])
    @EnableRatePassFail.setter
    def EnableRatePassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRatePassFail'], value)

    @property
    def EnableSequenceErrorsPassFail(self):
        """
        Returns
        -------
        - bool: If true, the sequence errors for pass fail id enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSequenceErrorsPassFail'])
    @EnableSequenceErrorsPassFail.setter
    def EnableSequenceErrorsPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSequenceErrorsPassFail'], value)

    @property
    def EnableStandardDeviationPassFail(self):
        """
        Returns
        -------
        - bool: If true, the standard deviation for pass or failure is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableStandardDeviationPassFail'])
    @EnableStandardDeviationPassFail.setter
    def EnableStandardDeviationPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableStandardDeviationPassFail'], value)

    @property
    def LatencyThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): The latency threshold mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyThresholdMode'])
    @LatencyThresholdMode.setter
    def LatencyThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyThresholdMode'], value)

    @property
    def LatencyThresholdScale(self):
        """
        Returns
        -------
        - str(ms | ns | us): The scale by which the latency threshold is measured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyThresholdScale'])
    @LatencyThresholdScale.setter
    def LatencyThresholdScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyThresholdScale'], value)

    @property
    def LatencyThresholdValue(self):
        """
        Returns
        -------
        - number: The value for the latency threshold.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyThresholdValue'])
    @LatencyThresholdValue.setter
    def LatencyThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyThresholdValue'], value)

    @property
    def LatencyVarThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): The latency variation threshold mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyVarThresholdMode'])
    @LatencyVarThresholdMode.setter
    def LatencyVarThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyVarThresholdMode'], value)

    @property
    def LatencyVariationThresholdScale(self):
        """
        Returns
        -------
        - str(ms | ns | us): The scale in which latency variation threshold is measured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyVariationThresholdScale'])
    @LatencyVariationThresholdScale.setter
    def LatencyVariationThresholdScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyVariationThresholdScale'], value)

    @property
    def LatencyVariationThresholdValue(self):
        """
        Returns
        -------
        - number: The threshold value of the latency variation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyVariationThresholdValue'])
    @LatencyVariationThresholdValue.setter
    def LatencyVariationThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyVariationThresholdValue'], value)

    @property
    def PassCriteriaLoadRateScale(self):
        """
        Returns
        -------
        - str(fps | gbps | kbps | mbps | percent): The load rate scale for the pass criteria.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PassCriteriaLoadRateScale'])
    @PassCriteriaLoadRateScale.setter
    def PassCriteriaLoadRateScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PassCriteriaLoadRateScale'], value)

    @property
    def PassCriteriaLoadRateValue(self):
        """
        Returns
        -------
        - number: The load rate value for the pass criteria.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PassCriteriaLoadRateValue'])
    @PassCriteriaLoadRateValue.setter
    def PassCriteriaLoadRateValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PassCriteriaLoadRateValue'], value)

    @property
    def SeqErrorsThresholdValue(self):
        """
        Returns
        -------
        - number: The threshold value for the sequence errors.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SeqErrorsThresholdValue'])
    @SeqErrorsThresholdValue.setter
    def SeqErrorsThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SeqErrorsThresholdValue'], value)

    def update(self, DataErrorThresholdValue=None, EnableDataIntegrityPassFail=None, EnableLatencyPassFail=None, EnablePassFail=None, EnableRatePassFail=None, EnableSequenceErrorsPassFail=None, EnableStandardDeviationPassFail=None, LatencyThresholdMode=None, LatencyThresholdScale=None, LatencyThresholdValue=None, LatencyVarThresholdMode=None, LatencyVariationThresholdScale=None, LatencyVariationThresholdValue=None, PassCriteriaLoadRateScale=None, PassCriteriaLoadRateValue=None, SeqErrorsThresholdValue=None):
        """Updates passCriteria resource on the server.

        Args
        ----
        - DataErrorThresholdValue (number): The data error of the threshold value.
        - EnableDataIntegrityPassFail (bool): If true, that data integrity of the pass or fail criteria is enabled.
        - EnableLatencyPassFail (bool): If true, the latency is enabled for pass fail.
        - EnablePassFail (bool): If true, IxNetwork applies the Pass Criteria to each trial in the test and determineswhether the trial passed or failed.
        - EnableRatePassFail (bool): If true, the rate of pass fail is enabled.
        - EnableSequenceErrorsPassFail (bool): If true, the sequence errors for pass fail id enabled.
        - EnableStandardDeviationPassFail (bool): If true, the standard deviation for pass or failure is enabled.
        - LatencyThresholdMode (str(average | maximum)): The latency threshold mode.
        - LatencyThresholdScale (str(ms | ns | us)): The scale by which the latency threshold is measured.
        - LatencyThresholdValue (number): The value for the latency threshold.
        - LatencyVarThresholdMode (str(average | maximum)): The latency variation threshold mode.
        - LatencyVariationThresholdScale (str(ms | ns | us)): The scale in which latency variation threshold is measured.
        - LatencyVariationThresholdValue (number): The threshold value of the latency variation.
        - PassCriteriaLoadRateScale (str(fps | gbps | kbps | mbps | percent)): The load rate scale for the pass criteria.
        - PassCriteriaLoadRateValue (number): The load rate value for the pass criteria.
        - SeqErrorsThresholdValue (number): The threshold value for the sequence errors.

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
