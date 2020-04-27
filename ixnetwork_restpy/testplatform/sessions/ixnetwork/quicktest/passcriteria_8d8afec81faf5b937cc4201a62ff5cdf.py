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
    """This applies the Pass Criteria to each trial in the test and determines whether the trial passed or failed.
    The PassCriteria class encapsulates a required passCriteria resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'passCriteria'

    def __init__(self, parent):
        super(PassCriteria, self).__init__(parent)

    @property
    def DownstreamDataErrorThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): The downstream Data Error Threshold mode.
        """
        return self._get_attribute('downstreamDataErrorThresholdMode')
    @DownstreamDataErrorThresholdMode.setter
    def DownstreamDataErrorThresholdMode(self, value):
        self._set_attribute('downstreamDataErrorThresholdMode', value)

    @property
    def DownstreamDataErrorThresholdValue(self):
        """
        Returns
        -------
        - number: The downstream data error threshold value.
        """
        return self._get_attribute('downstreamDataErrorThresholdValue')
    @DownstreamDataErrorThresholdValue.setter
    def DownstreamDataErrorThresholdValue(self, value):
        self._set_attribute('downstreamDataErrorThresholdValue', value)

    @property
    def DownstreamEnableDataIntegrityPassFail(self):
        """
        Returns
        -------
        - bool: Enables downstream data integrity pass or fail criteria.
        """
        return self._get_attribute('downstreamEnableDataIntegrityPassFail')
    @DownstreamEnableDataIntegrityPassFail.setter
    def DownstreamEnableDataIntegrityPassFail(self, value):
        self._set_attribute('downstreamEnableDataIntegrityPassFail', value)

    @property
    def DownstreamEnableLatencyPassFail(self):
        """
        Returns
        -------
        - bool: Enable downstream traffic latency pass or fail criteria.
        """
        return self._get_attribute('downstreamEnableLatencyPassFail')
    @DownstreamEnableLatencyPassFail.setter
    def DownstreamEnableLatencyPassFail(self, value):
        self._set_attribute('downstreamEnableLatencyPassFail', value)

    @property
    def DownstreamEnableRatePassFail(self):
        """
        Returns
        -------
        - bool: Enables to check downstream pass or fail rate.
        """
        return self._get_attribute('downstreamEnableRatePassFail')
    @DownstreamEnableRatePassFail.setter
    def DownstreamEnableRatePassFail(self, value):
        self._set_attribute('downstreamEnableRatePassFail', value)

    @property
    def DownstreamEnableSequenceErrorsPassFail(self):
        """
        Returns
        -------
        - bool: Enables downstream sequence errors pass or fail criteria.
        """
        return self._get_attribute('downstreamEnableSequenceErrorsPassFail')
    @DownstreamEnableSequenceErrorsPassFail.setter
    def DownstreamEnableSequenceErrorsPassFail(self, value):
        self._set_attribute('downstreamEnableSequenceErrorsPassFail', value)

    @property
    def DownstreamEnableStandardDeviationPassFail(self):
        """
        Returns
        -------
        - bool: Enables downstream standard deviation pass or fail criteria.
        """
        return self._get_attribute('downstreamEnableStandardDeviationPassFail')
    @DownstreamEnableStandardDeviationPassFail.setter
    def DownstreamEnableStandardDeviationPassFail(self, value):
        self._set_attribute('downstreamEnableStandardDeviationPassFail', value)

    @property
    def DownstreamLatencyThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): The latency threshold mode for downstream traffic.
        """
        return self._get_attribute('downstreamLatencyThresholdMode')
    @DownstreamLatencyThresholdMode.setter
    def DownstreamLatencyThresholdMode(self, value):
        self._set_attribute('downstreamLatencyThresholdMode', value)

    @property
    def DownstreamLatencyThresholdScale(self):
        """
        Returns
        -------
        - str(ms | ns | us): The latency threshold scale for downstream trafic.
        """
        return self._get_attribute('downstreamLatencyThresholdScale')
    @DownstreamLatencyThresholdScale.setter
    def DownstreamLatencyThresholdScale(self, value):
        self._set_attribute('downstreamLatencyThresholdScale', value)

    @property
    def DownstreamLatencyThresholdValue(self):
        """
        Returns
        -------
        - number: The latency threshold value for downstream traffic.
        """
        return self._get_attribute('downstreamLatencyThresholdValue')
    @DownstreamLatencyThresholdValue.setter
    def DownstreamLatencyThresholdValue(self, value):
        self._set_attribute('downstreamLatencyThresholdValue', value)

    @property
    def DownstreamLatencyVarThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): The latency variation threshold mode for downstream traffic.
        """
        return self._get_attribute('downstreamLatencyVarThresholdMode')
    @DownstreamLatencyVarThresholdMode.setter
    def DownstreamLatencyVarThresholdMode(self, value):
        self._set_attribute('downstreamLatencyVarThresholdMode', value)

    @property
    def DownstreamLatencyVariationThresholdScale(self):
        """
        Returns
        -------
        - str(ms | ns | us): The latency variation threshold scale for downstream traffic.
        """
        return self._get_attribute('downstreamLatencyVariationThresholdScale')
    @DownstreamLatencyVariationThresholdScale.setter
    def DownstreamLatencyVariationThresholdScale(self, value):
        self._set_attribute('downstreamLatencyVariationThresholdScale', value)

    @property
    def DownstreamLatencyVariationThresholdValue(self):
        """
        Returns
        -------
        - number: The latency variation threshold value for downstream traffic.
        """
        return self._get_attribute('downstreamLatencyVariationThresholdValue')
    @DownstreamLatencyVariationThresholdValue.setter
    def DownstreamLatencyVariationThresholdValue(self, value):
        self._set_attribute('downstreamLatencyVariationThresholdValue', value)

    @property
    def DownstreamPassCriteriaLoadRateMode(self):
        """
        Returns
        -------
        - str(average | minimum): The downstream traffic pass criteria for load rate mode.
        """
        return self._get_attribute('downstreamPassCriteriaLoadRateMode')
    @DownstreamPassCriteriaLoadRateMode.setter
    def DownstreamPassCriteriaLoadRateMode(self, value):
        self._set_attribute('downstreamPassCriteriaLoadRateMode', value)

    @property
    def DownstreamPassCriteriaLoadRateScale(self):
        """
        Returns
        -------
        - str(fps | gbps | kbps | mbps | percent): The downstream traffic pass criteria for load rate scale.
        """
        return self._get_attribute('downstreamPassCriteriaLoadRateScale')
    @DownstreamPassCriteriaLoadRateScale.setter
    def DownstreamPassCriteriaLoadRateScale(self, value):
        self._set_attribute('downstreamPassCriteriaLoadRateScale', value)

    @property
    def DownstreamPassCriteriaLoadRateValue(self):
        """
        Returns
        -------
        - number: The downstream traffic pass criteria load rate value.
        """
        return self._get_attribute('downstreamPassCriteriaLoadRateValue')
    @DownstreamPassCriteriaLoadRateValue.setter
    def DownstreamPassCriteriaLoadRateValue(self, value):
        self._set_attribute('downstreamPassCriteriaLoadRateValue', value)

    @property
    def DownstreamSeqErrorsThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): The downstream traffic sequence error threshold mode.
        """
        return self._get_attribute('downstreamSeqErrorsThresholdMode')
    @DownstreamSeqErrorsThresholdMode.setter
    def DownstreamSeqErrorsThresholdMode(self, value):
        self._set_attribute('downstreamSeqErrorsThresholdMode', value)

    @property
    def DownstreamSeqErrorsThresholdValue(self):
        """
        Returns
        -------
        - number: The downstream traffic sequence error threshold value.
        """
        return self._get_attribute('downstreamSeqErrorsThresholdValue')
    @DownstreamSeqErrorsThresholdValue.setter
    def DownstreamSeqErrorsThresholdValue(self, value):
        self._set_attribute('downstreamSeqErrorsThresholdValue', value)

    @property
    def Downstream_passFailFrequency(self):
        """
        Returns
        -------
        - str(framesizes | trials): NOT DEFINED
        """
        return self._get_attribute('downstream_passFailFrequency')
    @Downstream_passFailFrequency.setter
    def Downstream_passFailFrequency(self, value):
        self._set_attribute('downstream_passFailFrequency', value)

    @property
    def UpstreamDataErrorThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): The upstream Data Error Threshold mode.
        """
        return self._get_attribute('upstreamDataErrorThresholdMode')
    @UpstreamDataErrorThresholdMode.setter
    def UpstreamDataErrorThresholdMode(self, value):
        self._set_attribute('upstreamDataErrorThresholdMode', value)

    @property
    def UpstreamDataErrorThresholdValue(self):
        """
        Returns
        -------
        - number: The upstream Data Error Threshold value.
        """
        return self._get_attribute('upstreamDataErrorThresholdValue')
    @UpstreamDataErrorThresholdValue.setter
    def UpstreamDataErrorThresholdValue(self, value):
        self._set_attribute('upstreamDataErrorThresholdValue', value)

    @property
    def UpstreamEnableDataIntegrityPassFail(self):
        """
        Returns
        -------
        - bool: Enables data integrity pass or fail criteria for upstream traffic.
        """
        return self._get_attribute('upstreamEnableDataIntegrityPassFail')
    @UpstreamEnableDataIntegrityPassFail.setter
    def UpstreamEnableDataIntegrityPassFail(self, value):
        self._set_attribute('upstreamEnableDataIntegrityPassFail', value)

    @property
    def UpstreamEnableLatencyPassFail(self):
        """
        Returns
        -------
        - bool: Enables latency pass fail criteria for upstream traffic.
        """
        return self._get_attribute('upstreamEnableLatencyPassFail')
    @UpstreamEnableLatencyPassFail.setter
    def UpstreamEnableLatencyPassFail(self, value):
        self._set_attribute('upstreamEnableLatencyPassFail', value)

    @property
    def UpstreamEnableRatePassFail(self):
        """
        Returns
        -------
        - bool: Enables pass or fail rate for upstream traffic.
        """
        return self._get_attribute('upstreamEnableRatePassFail')
    @UpstreamEnableRatePassFail.setter
    def UpstreamEnableRatePassFail(self, value):
        self._set_attribute('upstreamEnableRatePassFail', value)

    @property
    def UpstreamEnableSequenceErrorsPassFail(self):
        """
        Returns
        -------
        - bool: Enables sequence error pass or fail criteria for upstream traffic.
        """
        return self._get_attribute('upstreamEnableSequenceErrorsPassFail')
    @UpstreamEnableSequenceErrorsPassFail.setter
    def UpstreamEnableSequenceErrorsPassFail(self, value):
        self._set_attribute('upstreamEnableSequenceErrorsPassFail', value)

    @property
    def UpstreamEnableStandardDeviationPassFail(self):
        """
        Returns
        -------
        - bool: Enables upstream traffic standard deviation pass or fail.
        """
        return self._get_attribute('upstreamEnableStandardDeviationPassFail')
    @UpstreamEnableStandardDeviationPassFail.setter
    def UpstreamEnableStandardDeviationPassFail(self, value):
        self._set_attribute('upstreamEnableStandardDeviationPassFail', value)

    @property
    def UpstreamLatencyThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): The upstream latency threshold mode.
        """
        return self._get_attribute('upstreamLatencyThresholdMode')
    @UpstreamLatencyThresholdMode.setter
    def UpstreamLatencyThresholdMode(self, value):
        self._set_attribute('upstreamLatencyThresholdMode', value)

    @property
    def UpstreamLatencyThresholdScale(self):
        """
        Returns
        -------
        - str(ms | ns | us): The upstream latency threshold scale.
        """
        return self._get_attribute('upstreamLatencyThresholdScale')
    @UpstreamLatencyThresholdScale.setter
    def UpstreamLatencyThresholdScale(self, value):
        self._set_attribute('upstreamLatencyThresholdScale', value)

    @property
    def UpstreamLatencyThresholdValue(self):
        """
        Returns
        -------
        - number: The upstream latency threshold value.
        """
        return self._get_attribute('upstreamLatencyThresholdValue')
    @UpstreamLatencyThresholdValue.setter
    def UpstreamLatencyThresholdValue(self, value):
        self._set_attribute('upstreamLatencyThresholdValue', value)

    @property
    def UpstreamLatencyVarThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): The upstream latency variation threshold mode.
        """
        return self._get_attribute('upstreamLatencyVarThresholdMode')
    @UpstreamLatencyVarThresholdMode.setter
    def UpstreamLatencyVarThresholdMode(self, value):
        self._set_attribute('upstreamLatencyVarThresholdMode', value)

    @property
    def UpstreamLatencyVariationThresholdScale(self):
        """
        Returns
        -------
        - str(ms | ns | us): The upstream latency variation threshold scale.
        """
        return self._get_attribute('upstreamLatencyVariationThresholdScale')
    @UpstreamLatencyVariationThresholdScale.setter
    def UpstreamLatencyVariationThresholdScale(self, value):
        self._set_attribute('upstreamLatencyVariationThresholdScale', value)

    @property
    def UpstreamLatencyVariationThresholdValue(self):
        """
        Returns
        -------
        - number: The upstream latency variation threshold value.
        """
        return self._get_attribute('upstreamLatencyVariationThresholdValue')
    @UpstreamLatencyVariationThresholdValue.setter
    def UpstreamLatencyVariationThresholdValue(self, value):
        self._set_attribute('upstreamLatencyVariationThresholdValue', value)

    @property
    def UpstreamPassCriteriaLoadRateMode(self):
        """
        Returns
        -------
        - str(average | minimum): The upstream pass criteria load rate mode.
        """
        return self._get_attribute('upstreamPassCriteriaLoadRateMode')
    @UpstreamPassCriteriaLoadRateMode.setter
    def UpstreamPassCriteriaLoadRateMode(self, value):
        self._set_attribute('upstreamPassCriteriaLoadRateMode', value)

    @property
    def UpstreamPassCriteriaLoadRateScale(self):
        """
        Returns
        -------
        - str(fps | gbps | kbps | mbps | percent): The upstream pass criteria load rate scale.
        """
        return self._get_attribute('upstreamPassCriteriaLoadRateScale')
    @UpstreamPassCriteriaLoadRateScale.setter
    def UpstreamPassCriteriaLoadRateScale(self, value):
        self._set_attribute('upstreamPassCriteriaLoadRateScale', value)

    @property
    def UpstreamPassCriteriaLoadRateValue(self):
        """
        Returns
        -------
        - number: The upstream pass criteria load rate value.
        """
        return self._get_attribute('upstreamPassCriteriaLoadRateValue')
    @UpstreamPassCriteriaLoadRateValue.setter
    def UpstreamPassCriteriaLoadRateValue(self, value):
        self._set_attribute('upstreamPassCriteriaLoadRateValue', value)

    @property
    def UpstreamSeqErrorsThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): The upstream sequence error threshold mode.
        """
        return self._get_attribute('upstreamSeqErrorsThresholdMode')
    @UpstreamSeqErrorsThresholdMode.setter
    def UpstreamSeqErrorsThresholdMode(self, value):
        self._set_attribute('upstreamSeqErrorsThresholdMode', value)

    @property
    def UpstreamSeqErrorsThresholdValue(self):
        """
        Returns
        -------
        - number: The upstream sequence error threshold value.
        """
        return self._get_attribute('upstreamSeqErrorsThresholdValue')
    @UpstreamSeqErrorsThresholdValue.setter
    def UpstreamSeqErrorsThresholdValue(self, value):
        self._set_attribute('upstreamSeqErrorsThresholdValue', value)

    @property
    def Upstream_passFailFrequency(self):
        """
        Returns
        -------
        - str(framesizes | trials): NOT DEFINED
        """
        return self._get_attribute('upstream_passFailFrequency')
    @Upstream_passFailFrequency.setter
    def Upstream_passFailFrequency(self, value):
        self._set_attribute('upstream_passFailFrequency', value)

    def update(self, DownstreamDataErrorThresholdMode=None, DownstreamDataErrorThresholdValue=None, DownstreamEnableDataIntegrityPassFail=None, DownstreamEnableLatencyPassFail=None, DownstreamEnableRatePassFail=None, DownstreamEnableSequenceErrorsPassFail=None, DownstreamEnableStandardDeviationPassFail=None, DownstreamLatencyThresholdMode=None, DownstreamLatencyThresholdScale=None, DownstreamLatencyThresholdValue=None, DownstreamLatencyVarThresholdMode=None, DownstreamLatencyVariationThresholdScale=None, DownstreamLatencyVariationThresholdValue=None, DownstreamPassCriteriaLoadRateMode=None, DownstreamPassCriteriaLoadRateScale=None, DownstreamPassCriteriaLoadRateValue=None, DownstreamSeqErrorsThresholdMode=None, DownstreamSeqErrorsThresholdValue=None, Downstream_passFailFrequency=None, UpstreamDataErrorThresholdMode=None, UpstreamDataErrorThresholdValue=None, UpstreamEnableDataIntegrityPassFail=None, UpstreamEnableLatencyPassFail=None, UpstreamEnableRatePassFail=None, UpstreamEnableSequenceErrorsPassFail=None, UpstreamEnableStandardDeviationPassFail=None, UpstreamLatencyThresholdMode=None, UpstreamLatencyThresholdScale=None, UpstreamLatencyThresholdValue=None, UpstreamLatencyVarThresholdMode=None, UpstreamLatencyVariationThresholdScale=None, UpstreamLatencyVariationThresholdValue=None, UpstreamPassCriteriaLoadRateMode=None, UpstreamPassCriteriaLoadRateScale=None, UpstreamPassCriteriaLoadRateValue=None, UpstreamSeqErrorsThresholdMode=None, UpstreamSeqErrorsThresholdValue=None, Upstream_passFailFrequency=None):
        """Updates passCriteria resource on the server.

        Args
        ----
        - DownstreamDataErrorThresholdMode (str(average | maximum)): The downstream Data Error Threshold mode.
        - DownstreamDataErrorThresholdValue (number): The downstream data error threshold value.
        - DownstreamEnableDataIntegrityPassFail (bool): Enables downstream data integrity pass or fail criteria.
        - DownstreamEnableLatencyPassFail (bool): Enable downstream traffic latency pass or fail criteria.
        - DownstreamEnableRatePassFail (bool): Enables to check downstream pass or fail rate.
        - DownstreamEnableSequenceErrorsPassFail (bool): Enables downstream sequence errors pass or fail criteria.
        - DownstreamEnableStandardDeviationPassFail (bool): Enables downstream standard deviation pass or fail criteria.
        - DownstreamLatencyThresholdMode (str(average | maximum)): The latency threshold mode for downstream traffic.
        - DownstreamLatencyThresholdScale (str(ms | ns | us)): The latency threshold scale for downstream trafic.
        - DownstreamLatencyThresholdValue (number): The latency threshold value for downstream traffic.
        - DownstreamLatencyVarThresholdMode (str(average | maximum)): The latency variation threshold mode for downstream traffic.
        - DownstreamLatencyVariationThresholdScale (str(ms | ns | us)): The latency variation threshold scale for downstream traffic.
        - DownstreamLatencyVariationThresholdValue (number): The latency variation threshold value for downstream traffic.
        - DownstreamPassCriteriaLoadRateMode (str(average | minimum)): The downstream traffic pass criteria for load rate mode.
        - DownstreamPassCriteriaLoadRateScale (str(fps | gbps | kbps | mbps | percent)): The downstream traffic pass criteria for load rate scale.
        - DownstreamPassCriteriaLoadRateValue (number): The downstream traffic pass criteria load rate value.
        - DownstreamSeqErrorsThresholdMode (str(average | maximum)): The downstream traffic sequence error threshold mode.
        - DownstreamSeqErrorsThresholdValue (number): The downstream traffic sequence error threshold value.
        - Downstream_passFailFrequency (str(framesizes | trials)): NOT DEFINED
        - UpstreamDataErrorThresholdMode (str(average | maximum)): The upstream Data Error Threshold mode.
        - UpstreamDataErrorThresholdValue (number): The upstream Data Error Threshold value.
        - UpstreamEnableDataIntegrityPassFail (bool): Enables data integrity pass or fail criteria for upstream traffic.
        - UpstreamEnableLatencyPassFail (bool): Enables latency pass fail criteria for upstream traffic.
        - UpstreamEnableRatePassFail (bool): Enables pass or fail rate for upstream traffic.
        - UpstreamEnableSequenceErrorsPassFail (bool): Enables sequence error pass or fail criteria for upstream traffic.
        - UpstreamEnableStandardDeviationPassFail (bool): Enables upstream traffic standard deviation pass or fail.
        - UpstreamLatencyThresholdMode (str(average | maximum)): The upstream latency threshold mode.
        - UpstreamLatencyThresholdScale (str(ms | ns | us)): The upstream latency threshold scale.
        - UpstreamLatencyThresholdValue (number): The upstream latency threshold value.
        - UpstreamLatencyVarThresholdMode (str(average | maximum)): The upstream latency variation threshold mode.
        - UpstreamLatencyVariationThresholdScale (str(ms | ns | us)): The upstream latency variation threshold scale.
        - UpstreamLatencyVariationThresholdValue (number): The upstream latency variation threshold value.
        - UpstreamPassCriteriaLoadRateMode (str(average | minimum)): The upstream pass criteria load rate mode.
        - UpstreamPassCriteriaLoadRateScale (str(fps | gbps | kbps | mbps | percent)): The upstream pass criteria load rate scale.
        - UpstreamPassCriteriaLoadRateValue (number): The upstream pass criteria load rate value.
        - UpstreamSeqErrorsThresholdMode (str(average | maximum)): The upstream sequence error threshold mode.
        - UpstreamSeqErrorsThresholdValue (number): The upstream sequence error threshold value.
        - Upstream_passFailFrequency (str(framesizes | trials)): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

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
