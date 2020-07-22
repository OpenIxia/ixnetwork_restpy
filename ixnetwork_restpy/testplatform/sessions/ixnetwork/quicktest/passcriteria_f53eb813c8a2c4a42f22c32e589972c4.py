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
    """This object, if true, enables IxNetwork to apply the Pass Criteria to each trial in the test and determines whether the trial passed or failed.
    The PassCriteria class encapsulates a required passCriteria resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'passCriteria'
    _SDM_ATT_MAP = {
        'DataErrorThresholdMode': 'dataErrorThresholdMode',
        'DataErrorThresholdValue': 'dataErrorThresholdValue',
        'EnableDataIntegrityPassFail': 'enableDataIntegrityPassFail',
        'EnableFrameLossPassFail': 'enableFrameLossPassFail',
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
        'LossThresholdMode': 'lossThresholdMode',
        'LossThresholdValue': 'lossThresholdValue',
        'PassCriteriaLoadRateMode': 'passCriteriaLoadRateMode',
        'PassCriteriaLoadRateScale': 'passCriteriaLoadRateScale',
        'PassCriteriaLoadRateValue': 'passCriteriaLoadRateValue',
        'PassFailFrequency': 'passFailFrequency',
        'SeqErrorsThresholdMode': 'seqErrorsThresholdMode',
        'SeqErrorsThresholdValue': 'seqErrorsThresholdValue',
    }

    def __init__(self, parent):
        super(PassCriteria, self).__init__(parent)

    @property
    def DataErrorThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): The threshold mode for the data error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataErrorThresholdMode'])
    @DataErrorThresholdMode.setter
    def DataErrorThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DataErrorThresholdMode'], value)

    @property
    def DataErrorThresholdValue(self):
        """
        Returns
        -------
        - number: The data error threshold value.
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
        - bool: If true, enables the checking of data integrity for the pass or fail of the trial.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableDataIntegrityPassFail'])
    @EnableDataIntegrityPassFail.setter
    def EnableDataIntegrityPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableDataIntegrityPassFail'], value)

    @property
    def EnableFrameLossPassFail(self):
        """
        Returns
        -------
        - bool: If true, enables the checking of frame loss for the pass or fail of the trial.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFrameLossPassFail'])
    @EnableFrameLossPassFail.setter
    def EnableFrameLossPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFrameLossPassFail'], value)

    @property
    def EnableLatencyPassFail(self):
        """
        Returns
        -------
        - bool: If true, enables latency at which trails pass or fail.
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
        - bool: If true, IxNetwork applies the Pass Criteria to each trial in the test and determines whether the trial passed or failed.
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
        - bool: If true, enables the rate of pass or failure of the trial.
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
        - bool: If true, sets the amount of time required by the DUT to forward frames and the sequence errors for the pass or fail of the trial.
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
        - bool: If true, enables standard deviation in the pass or failure of the trial.
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
        - str(average | maximum): The threshold latency mode value.
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
        - str(ms | ns | us): The latency threshold scale value.
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
        - number: The latency threshold value of the test.
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
        - str(average | maximum): The threshold mode for the latency variation.
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
        - str(ms | ns | us): signifies the latency variation in the threshold scale.
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
        - number: signifies the latency variation in the threshold value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyVariationThresholdValue'])
    @LatencyVariationThresholdValue.setter
    def LatencyVariationThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyVariationThresholdValue'], value)

    @property
    def LossThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): Signifies threshold mode of the frame loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LossThresholdMode'])
    @LossThresholdMode.setter
    def LossThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LossThresholdMode'], value)

    @property
    def LossThresholdValue(self):
        """
        Returns
        -------
        - number: Denotes the loss in threshold value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LossThresholdValue'])
    @LossThresholdValue.setter
    def LossThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LossThresholdValue'], value)

    @property
    def PassCriteriaLoadRateMode(self):
        """
        Returns
        -------
        - str(average | minimum): The Pass Criteria per trial rate at which the DUT should be able to transmit and receive, expressed as a percentage of the maximum theoretical line speed or in terms of frames per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PassCriteriaLoadRateMode'])
    @PassCriteriaLoadRateMode.setter
    def PassCriteriaLoadRateMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PassCriteriaLoadRateMode'], value)

    @property
    def PassCriteriaLoadRateScale(self):
        """
        Returns
        -------
        - str(fps | gbps | kbps | mbps | percent): The load rate scale for the Pass Criteria per trial.
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
        - number: The load rate value for the Pass Criteria per trial.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PassCriteriaLoadRateValue'])
    @PassCriteriaLoadRateValue.setter
    def PassCriteriaLoadRateValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PassCriteriaLoadRateValue'], value)

    @property
    def PassFailFrequency(self):
        """
        Returns
        -------
        - str(framesizes | trials): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PassFailFrequency'])
    @PassFailFrequency.setter
    def PassFailFrequency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PassFailFrequency'], value)

    @property
    def SeqErrorsThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): The sequence error value for the threshold mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SeqErrorsThresholdMode'])
    @SeqErrorsThresholdMode.setter
    def SeqErrorsThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SeqErrorsThresholdMode'], value)

    @property
    def SeqErrorsThresholdValue(self):
        """
        Returns
        -------
        - number: The value for the sequence error threshold.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SeqErrorsThresholdValue'])
    @SeqErrorsThresholdValue.setter
    def SeqErrorsThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SeqErrorsThresholdValue'], value)

    def update(self, DataErrorThresholdMode=None, DataErrorThresholdValue=None, EnableDataIntegrityPassFail=None, EnableFrameLossPassFail=None, EnableLatencyPassFail=None, EnablePassFail=None, EnableRatePassFail=None, EnableSequenceErrorsPassFail=None, EnableStandardDeviationPassFail=None, LatencyThresholdMode=None, LatencyThresholdScale=None, LatencyThresholdValue=None, LatencyVarThresholdMode=None, LatencyVariationThresholdScale=None, LatencyVariationThresholdValue=None, LossThresholdMode=None, LossThresholdValue=None, PassCriteriaLoadRateMode=None, PassCriteriaLoadRateScale=None, PassCriteriaLoadRateValue=None, PassFailFrequency=None, SeqErrorsThresholdMode=None, SeqErrorsThresholdValue=None):
        """Updates passCriteria resource on the server.

        Args
        ----
        - DataErrorThresholdMode (str(average | maximum)): The threshold mode for the data error.
        - DataErrorThresholdValue (number): The data error threshold value.
        - EnableDataIntegrityPassFail (bool): If true, enables the checking of data integrity for the pass or fail of the trial.
        - EnableFrameLossPassFail (bool): If true, enables the checking of frame loss for the pass or fail of the trial.
        - EnableLatencyPassFail (bool): If true, enables latency at which trails pass or fail.
        - EnablePassFail (bool): If true, IxNetwork applies the Pass Criteria to each trial in the test and determines whether the trial passed or failed.
        - EnableRatePassFail (bool): If true, enables the rate of pass or failure of the trial.
        - EnableSequenceErrorsPassFail (bool): If true, sets the amount of time required by the DUT to forward frames and the sequence errors for the pass or fail of the trial.
        - EnableStandardDeviationPassFail (bool): If true, enables standard deviation in the pass or failure of the trial.
        - LatencyThresholdMode (str(average | maximum)): The threshold latency mode value.
        - LatencyThresholdScale (str(ms | ns | us)): The latency threshold scale value.
        - LatencyThresholdValue (number): The latency threshold value of the test.
        - LatencyVarThresholdMode (str(average | maximum)): The threshold mode for the latency variation.
        - LatencyVariationThresholdScale (str(ms | ns | us)): signifies the latency variation in the threshold scale.
        - LatencyVariationThresholdValue (number): signifies the latency variation in the threshold value.
        - LossThresholdMode (str(average | maximum)): Signifies threshold mode of the frame loss.
        - LossThresholdValue (number): Denotes the loss in threshold value.
        - PassCriteriaLoadRateMode (str(average | minimum)): The Pass Criteria per trial rate at which the DUT should be able to transmit and receive, expressed as a percentage of the maximum theoretical line speed or in terms of frames per second.
        - PassCriteriaLoadRateScale (str(fps | gbps | kbps | mbps | percent)): The load rate scale for the Pass Criteria per trial.
        - PassCriteriaLoadRateValue (number): The load rate value for the Pass Criteria per trial.
        - PassFailFrequency (str(framesizes | trials)): NOT DEFINED
        - SeqErrorsThresholdMode (str(average | maximum)): The sequence error value for the threshold mode.
        - SeqErrorsThresholdValue (number): The value for the sequence error threshold.

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
