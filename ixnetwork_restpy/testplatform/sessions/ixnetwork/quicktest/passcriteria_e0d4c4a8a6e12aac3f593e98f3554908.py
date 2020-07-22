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
    """This applies the Pass Criteria to each trial in the test and determines whether the trial passed or failed.
    The PassCriteria class encapsulates a required passCriteria resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'passCriteria'
    _SDM_ATT_MAP = {
        'EnableLatencyPassFail': 'enableLatencyPassFail',
        'EnablePassFail': 'enablePassFail',
        'EnableRatePassFail': 'enableRatePassFail',
        'EnableStandardDeviationPassFail': 'enableStandardDeviationPassFail',
        'LatencyThresholdMode': 'latencyThresholdMode',
        'LatencyThresholdScale': 'latencyThresholdScale',
        'LatencyVarThresholdMode': 'latencyVarThresholdMode',
        'LatencyVariationThresholdScale': 'latencyVariationThresholdScale',
        'PassCriteriaLoadRateMode': 'passCriteriaLoadRateMode',
        'PassCriteriaLoadRateScale': 'passCriteriaLoadRateScale',
        'PassFailLatencyUnit': 'passFailLatencyUnit',
    }

    def __init__(self, parent):
        super(PassCriteria, self).__init__(parent)

    @property
    def EnableLatencyPassFail(self):
        """
        Returns
        -------
        - bool: If true, the latency pass fail criteria is set.
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
        - bool: If true, the rate of pass and fail criteria is set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRatePassFail'])
    @EnableRatePassFail.setter
    def EnableRatePassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRatePassFail'], value)

    @property
    def EnableStandardDeviationPassFail(self):
        """
        Returns
        -------
        - bool: If true, Standard Deviation for the Pass/Fail criteria is set.
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
        - str(average | maximum): The threshold mode for the latency.
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
        - str(ms | ns | us): The scale by which the latency variation threshold is measured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyVariationThresholdScale'])
    @LatencyVariationThresholdScale.setter
    def LatencyVariationThresholdScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatencyVariationThresholdScale'], value)

    @property
    def PassCriteriaLoadRateMode(self):
        """
        Returns
        -------
        - str(average | minimum): The pass critria set for the load rate mode.
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
        - str(fps | gbps | kbps | mbps | percent): The pass criteria scale in which the load rateis to be measured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PassCriteriaLoadRateScale'])
    @PassCriteriaLoadRateScale.setter
    def PassCriteriaLoadRateScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PassCriteriaLoadRateScale'], value)

    @property
    def PassFailLatencyUnit(self):
        """
        Returns
        -------
        - str(ms | ns | us): If true, the pass fail latency unit is set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PassFailLatencyUnit'])
    @PassFailLatencyUnit.setter
    def PassFailLatencyUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PassFailLatencyUnit'], value)

    def update(self, EnableLatencyPassFail=None, EnablePassFail=None, EnableRatePassFail=None, EnableStandardDeviationPassFail=None, LatencyThresholdMode=None, LatencyThresholdScale=None, LatencyVarThresholdMode=None, LatencyVariationThresholdScale=None, PassCriteriaLoadRateMode=None, PassCriteriaLoadRateScale=None, PassFailLatencyUnit=None):
        """Updates passCriteria resource on the server.

        Args
        ----
        - EnableLatencyPassFail (bool): If true, the latency pass fail criteria is set.
        - EnablePassFail (bool): If true, IxNetwork applies the Pass Criteria to each trial in the test and determineswhether the trial passed or failed.
        - EnableRatePassFail (bool): If true, the rate of pass and fail criteria is set.
        - EnableStandardDeviationPassFail (bool): If true, Standard Deviation for the Pass/Fail criteria is set.
        - LatencyThresholdMode (str(average | maximum)): The threshold mode for the latency.
        - LatencyThresholdScale (str(ms | ns | us)): The scale by which the latency threshold is measured.
        - LatencyVarThresholdMode (str(average | maximum)): The latency variation threshold mode.
        - LatencyVariationThresholdScale (str(ms | ns | us)): The scale by which the latency variation threshold is measured.
        - PassCriteriaLoadRateMode (str(average | minimum)): The pass critria set for the load rate mode.
        - PassCriteriaLoadRateScale (str(fps | gbps | kbps | mbps | percent)): The pass criteria scale in which the load rateis to be measured.
        - PassFailLatencyUnit (str(ms | ns | us)): If true, the pass fail latency unit is set.

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
