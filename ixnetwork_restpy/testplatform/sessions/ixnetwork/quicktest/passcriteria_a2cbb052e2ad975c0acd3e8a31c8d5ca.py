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
    """Signifies pass criteria
    The PassCriteria class encapsulates a required passCriteria resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'passCriteria'
    _SDM_ATT_MAP = {
        'DownstreamDataErrorThresholdMode': 'downstreamDataErrorThresholdMode',
        'DownstreamDataErrorThresholdValue': 'downstreamDataErrorThresholdValue',
        'DownstreamEnableDataIntegrityPassFail': 'downstreamEnableDataIntegrityPassFail',
        'DownstreamEnableLatencyPassFail': 'downstreamEnableLatencyPassFail',
        'DownstreamEnableRatePassFail': 'downstreamEnableRatePassFail',
        'DownstreamEnableSequenceErrorsPassFail': 'downstreamEnableSequenceErrorsPassFail',
        'DownstreamEnableStandardDeviationPassFail': 'downstreamEnableStandardDeviationPassFail',
        'DownstreamLatencyThresholdMode': 'downstreamLatencyThresholdMode',
        'DownstreamLatencyThresholdScale': 'downstreamLatencyThresholdScale',
        'DownstreamLatencyThresholdValue': 'downstreamLatencyThresholdValue',
        'DownstreamLatencyVarThresholdMode': 'downstreamLatencyVarThresholdMode',
        'DownstreamLatencyVariationThresholdScale': 'downstreamLatencyVariationThresholdScale',
        'DownstreamLatencyVariationThresholdValue': 'downstreamLatencyVariationThresholdValue',
        'DownstreamPassCriteriaLoadRateMode': 'downstreamPassCriteriaLoadRateMode',
        'DownstreamPassCriteriaLoadRateScale': 'downstreamPassCriteriaLoadRateScale',
        'DownstreamPassCriteriaLoadRateValue': 'downstreamPassCriteriaLoadRateValue',
        'DownstreamSeqErrorsThresholdMode': 'downstreamSeqErrorsThresholdMode',
        'DownstreamSeqErrorsThresholdValue': 'downstreamSeqErrorsThresholdValue',
        'Downstream_passFailFrequency': 'downstream_passFailFrequency',
        'UpstreamDataErrorThresholdMode': 'upstreamDataErrorThresholdMode',
        'UpstreamDataErrorThresholdValue': 'upstreamDataErrorThresholdValue',
        'UpstreamEnableDataIntegrityPassFail': 'upstreamEnableDataIntegrityPassFail',
        'UpstreamEnableLatencyPassFail': 'upstreamEnableLatencyPassFail',
        'UpstreamEnableRatePassFail': 'upstreamEnableRatePassFail',
        'UpstreamEnableSequenceErrorsPassFail': 'upstreamEnableSequenceErrorsPassFail',
        'UpstreamEnableStandardDeviationPassFail': 'upstreamEnableStandardDeviationPassFail',
        'UpstreamLatencyThresholdMode': 'upstreamLatencyThresholdMode',
        'UpstreamLatencyThresholdScale': 'upstreamLatencyThresholdScale',
        'UpstreamLatencyThresholdValue': 'upstreamLatencyThresholdValue',
        'UpstreamLatencyVarThresholdMode': 'upstreamLatencyVarThresholdMode',
        'UpstreamLatencyVariationThresholdScale': 'upstreamLatencyVariationThresholdScale',
        'UpstreamLatencyVariationThresholdValue': 'upstreamLatencyVariationThresholdValue',
        'UpstreamPassCriteriaLoadRateMode': 'upstreamPassCriteriaLoadRateMode',
        'UpstreamPassCriteriaLoadRateScale': 'upstreamPassCriteriaLoadRateScale',
        'UpstreamPassCriteriaLoadRateValue': 'upstreamPassCriteriaLoadRateValue',
        'UpstreamSeqErrorsThresholdMode': 'upstreamSeqErrorsThresholdMode',
        'UpstreamSeqErrorsThresholdValue': 'upstreamSeqErrorsThresholdValue',
        'Upstream_passFailFrequency': 'upstream_passFailFrequency',
    }

    def __init__(self, parent):
        super(PassCriteria, self).__init__(parent)

    @property
    def DownstreamDataErrorThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): Signifies threshold mode for downstream data error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamDataErrorThresholdMode'])
    @DownstreamDataErrorThresholdMode.setter
    def DownstreamDataErrorThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamDataErrorThresholdMode'], value)

    @property
    def DownstreamDataErrorThresholdValue(self):
        """
        Returns
        -------
        - number: Signifies the downstream data error threshold value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamDataErrorThresholdValue'])
    @DownstreamDataErrorThresholdValue.setter
    def DownstreamDataErrorThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamDataErrorThresholdValue'], value)

    @property
    def DownstreamEnableDataIntegrityPassFail(self):
        """
        Returns
        -------
        - bool: if true, enables pass or faill of data integrity for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamEnableDataIntegrityPassFail'])
    @DownstreamEnableDataIntegrityPassFail.setter
    def DownstreamEnableDataIntegrityPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamEnableDataIntegrityPassFail'], value)

    @property
    def DownstreamEnableLatencyPassFail(self):
        """
        Returns
        -------
        - bool: If true, enables latency pass fail for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamEnableLatencyPassFail'])
    @DownstreamEnableLatencyPassFail.setter
    def DownstreamEnableLatencyPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamEnableLatencyPassFail'], value)

    @property
    def DownstreamEnableRatePassFail(self):
        """
        Returns
        -------
        - bool: If true, enables pass fail rate for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamEnableRatePassFail'])
    @DownstreamEnableRatePassFail.setter
    def DownstreamEnableRatePassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamEnableRatePassFail'], value)

    @property
    def DownstreamEnableSequenceErrorsPassFail(self):
        """
        Returns
        -------
        - bool: If true, enables the pass fail for sequence errors for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamEnableSequenceErrorsPassFail'])
    @DownstreamEnableSequenceErrorsPassFail.setter
    def DownstreamEnableSequenceErrorsPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamEnableSequenceErrorsPassFail'], value)

    @property
    def DownstreamEnableStandardDeviationPassFail(self):
        """
        Returns
        -------
        - bool: If true, enables pass fail of standard deviation for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamEnableStandardDeviationPassFail'])
    @DownstreamEnableStandardDeviationPassFail.setter
    def DownstreamEnableStandardDeviationPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamEnableStandardDeviationPassFail'], value)

    @property
    def DownstreamLatencyThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): Signifies the latency threshold mode for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLatencyThresholdMode'])
    @DownstreamLatencyThresholdMode.setter
    def DownstreamLatencyThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLatencyThresholdMode'], value)

    @property
    def DownstreamLatencyThresholdScale(self):
        """
        Returns
        -------
        - str(ms | ns | us): Signifies the threshold scale for downstream latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLatencyThresholdScale'])
    @DownstreamLatencyThresholdScale.setter
    def DownstreamLatencyThresholdScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLatencyThresholdScale'], value)

    @property
    def DownstreamLatencyThresholdValue(self):
        """
        Returns
        -------
        - number: Signifies the latency threshold value for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLatencyThresholdValue'])
    @DownstreamLatencyThresholdValue.setter
    def DownstreamLatencyThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLatencyThresholdValue'], value)

    @property
    def DownstreamLatencyVarThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): Signifies latency variation threshold mode for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLatencyVarThresholdMode'])
    @DownstreamLatencyVarThresholdMode.setter
    def DownstreamLatencyVarThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLatencyVarThresholdMode'], value)

    @property
    def DownstreamLatencyVariationThresholdScale(self):
        """
        Returns
        -------
        - str(ms | ns | us): Signifies latency variation threshold scale for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLatencyVariationThresholdScale'])
    @DownstreamLatencyVariationThresholdScale.setter
    def DownstreamLatencyVariationThresholdScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLatencyVariationThresholdScale'], value)

    @property
    def DownstreamLatencyVariationThresholdValue(self):
        """
        Returns
        -------
        - number: Signifies the latency variation threshold value for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLatencyVariationThresholdValue'])
    @DownstreamLatencyVariationThresholdValue.setter
    def DownstreamLatencyVariationThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLatencyVariationThresholdValue'], value)

    @property
    def DownstreamPassCriteriaLoadRateMode(self):
        """
        Returns
        -------
        - str(average | minimum): Signifies the pass criteria load rate mode for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamPassCriteriaLoadRateMode'])
    @DownstreamPassCriteriaLoadRateMode.setter
    def DownstreamPassCriteriaLoadRateMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamPassCriteriaLoadRateMode'], value)

    @property
    def DownstreamPassCriteriaLoadRateScale(self):
        """
        Returns
        -------
        - str(fps | gbps | kbps | mbps | percent): Signifies the pass criteria load rate scale for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamPassCriteriaLoadRateScale'])
    @DownstreamPassCriteriaLoadRateScale.setter
    def DownstreamPassCriteriaLoadRateScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamPassCriteriaLoadRateScale'], value)

    @property
    def DownstreamPassCriteriaLoadRateValue(self):
        """
        Returns
        -------
        - number: Signifies pass criteria load rate value for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamPassCriteriaLoadRateValue'])
    @DownstreamPassCriteriaLoadRateValue.setter
    def DownstreamPassCriteriaLoadRateValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamPassCriteriaLoadRateValue'], value)

    @property
    def DownstreamSeqErrorsThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): Signifies the threshold mode for sequence errors for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamSeqErrorsThresholdMode'])
    @DownstreamSeqErrorsThresholdMode.setter
    def DownstreamSeqErrorsThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamSeqErrorsThresholdMode'], value)

    @property
    def DownstreamSeqErrorsThresholdValue(self):
        """
        Returns
        -------
        - number: Signifies the threshold value for sequence errors for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamSeqErrorsThresholdValue'])
    @DownstreamSeqErrorsThresholdValue.setter
    def DownstreamSeqErrorsThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DownstreamSeqErrorsThresholdValue'], value)

    @property
    def Downstream_passFailFrequency(self):
        """
        Returns
        -------
        - str(framesizes | trials): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Downstream_passFailFrequency'])
    @Downstream_passFailFrequency.setter
    def Downstream_passFailFrequency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Downstream_passFailFrequency'], value)

    @property
    def UpstreamDataErrorThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): Signifies the data error threshold mode for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamDataErrorThresholdMode'])
    @UpstreamDataErrorThresholdMode.setter
    def UpstreamDataErrorThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamDataErrorThresholdMode'], value)

    @property
    def UpstreamDataErrorThresholdValue(self):
        """
        Returns
        -------
        - number: Signifies data error threshold value for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamDataErrorThresholdValue'])
    @UpstreamDataErrorThresholdValue.setter
    def UpstreamDataErrorThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamDataErrorThresholdValue'], value)

    @property
    def UpstreamEnableDataIntegrityPassFail(self):
        """
        Returns
        -------
        - bool: If true, enables pass fail of data integrity for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamEnableDataIntegrityPassFail'])
    @UpstreamEnableDataIntegrityPassFail.setter
    def UpstreamEnableDataIntegrityPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamEnableDataIntegrityPassFail'], value)

    @property
    def UpstreamEnableLatencyPassFail(self):
        """
        Returns
        -------
        - bool: If true, enables latency pass fail for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamEnableLatencyPassFail'])
    @UpstreamEnableLatencyPassFail.setter
    def UpstreamEnableLatencyPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamEnableLatencyPassFail'], value)

    @property
    def UpstreamEnableRatePassFail(self):
        """
        Returns
        -------
        - bool: If true, enables the rate of pass fail for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamEnableRatePassFail'])
    @UpstreamEnableRatePassFail.setter
    def UpstreamEnableRatePassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamEnableRatePassFail'], value)

    @property
    def UpstreamEnableSequenceErrorsPassFail(self):
        """
        Returns
        -------
        - bool: If true, enables sequence errors pass fail for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamEnableSequenceErrorsPassFail'])
    @UpstreamEnableSequenceErrorsPassFail.setter
    def UpstreamEnableSequenceErrorsPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamEnableSequenceErrorsPassFail'], value)

    @property
    def UpstreamEnableStandardDeviationPassFail(self):
        """
        Returns
        -------
        - bool: If true, enables standard deviation of pass and fail for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamEnableStandardDeviationPassFail'])
    @UpstreamEnableStandardDeviationPassFail.setter
    def UpstreamEnableStandardDeviationPassFail(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamEnableStandardDeviationPassFail'], value)

    @property
    def UpstreamLatencyThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): Signifies the latency threshold mode for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLatencyThresholdMode'])
    @UpstreamLatencyThresholdMode.setter
    def UpstreamLatencyThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLatencyThresholdMode'], value)

    @property
    def UpstreamLatencyThresholdScale(self):
        """
        Returns
        -------
        - str(ms | ns | us): Signifies the latency threshold scale for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLatencyThresholdScale'])
    @UpstreamLatencyThresholdScale.setter
    def UpstreamLatencyThresholdScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLatencyThresholdScale'], value)

    @property
    def UpstreamLatencyThresholdValue(self):
        """
        Returns
        -------
        - number: It is the latency threshold value for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLatencyThresholdValue'])
    @UpstreamLatencyThresholdValue.setter
    def UpstreamLatencyThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLatencyThresholdValue'], value)

    @property
    def UpstreamLatencyVarThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): Signifies the latency variation threshold mode for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLatencyVarThresholdMode'])
    @UpstreamLatencyVarThresholdMode.setter
    def UpstreamLatencyVarThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLatencyVarThresholdMode'], value)

    @property
    def UpstreamLatencyVariationThresholdScale(self):
        """
        Returns
        -------
        - str(ms | ns | us): It is the latency variation threshold scale for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLatencyVariationThresholdScale'])
    @UpstreamLatencyVariationThresholdScale.setter
    def UpstreamLatencyVariationThresholdScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLatencyVariationThresholdScale'], value)

    @property
    def UpstreamLatencyVariationThresholdValue(self):
        """
        Returns
        -------
        - number: Signifies the latency variation threshold value for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLatencyVariationThresholdValue'])
    @UpstreamLatencyVariationThresholdValue.setter
    def UpstreamLatencyVariationThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLatencyVariationThresholdValue'], value)

    @property
    def UpstreamPassCriteriaLoadRateMode(self):
        """
        Returns
        -------
        - str(average | minimum): Signifies the pass criteria load rate mode for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamPassCriteriaLoadRateMode'])
    @UpstreamPassCriteriaLoadRateMode.setter
    def UpstreamPassCriteriaLoadRateMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamPassCriteriaLoadRateMode'], value)

    @property
    def UpstreamPassCriteriaLoadRateScale(self):
        """
        Returns
        -------
        - str(fps | gbps | kbps | mbps | percent): Signifies pass criteria for load rate scale for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamPassCriteriaLoadRateScale'])
    @UpstreamPassCriteriaLoadRateScale.setter
    def UpstreamPassCriteriaLoadRateScale(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamPassCriteriaLoadRateScale'], value)

    @property
    def UpstreamPassCriteriaLoadRateValue(self):
        """
        Returns
        -------
        - number: Signifies the pass criteria load rate value for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamPassCriteriaLoadRateValue'])
    @UpstreamPassCriteriaLoadRateValue.setter
    def UpstreamPassCriteriaLoadRateValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamPassCriteriaLoadRateValue'], value)

    @property
    def UpstreamSeqErrorsThresholdMode(self):
        """
        Returns
        -------
        - str(average | maximum): Signifies the sequence errors threshold mode for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamSeqErrorsThresholdMode'])
    @UpstreamSeqErrorsThresholdMode.setter
    def UpstreamSeqErrorsThresholdMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamSeqErrorsThresholdMode'], value)

    @property
    def UpstreamSeqErrorsThresholdValue(self):
        """
        Returns
        -------
        - number: Signifies sequence errors threshold value for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamSeqErrorsThresholdValue'])
    @UpstreamSeqErrorsThresholdValue.setter
    def UpstreamSeqErrorsThresholdValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpstreamSeqErrorsThresholdValue'], value)

    @property
    def Upstream_passFailFrequency(self):
        """
        Returns
        -------
        - str(framesizes | trials): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Upstream_passFailFrequency'])
    @Upstream_passFailFrequency.setter
    def Upstream_passFailFrequency(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Upstream_passFailFrequency'], value)

    def update(self, DownstreamDataErrorThresholdMode=None, DownstreamDataErrorThresholdValue=None, DownstreamEnableDataIntegrityPassFail=None, DownstreamEnableLatencyPassFail=None, DownstreamEnableRatePassFail=None, DownstreamEnableSequenceErrorsPassFail=None, DownstreamEnableStandardDeviationPassFail=None, DownstreamLatencyThresholdMode=None, DownstreamLatencyThresholdScale=None, DownstreamLatencyThresholdValue=None, DownstreamLatencyVarThresholdMode=None, DownstreamLatencyVariationThresholdScale=None, DownstreamLatencyVariationThresholdValue=None, DownstreamPassCriteriaLoadRateMode=None, DownstreamPassCriteriaLoadRateScale=None, DownstreamPassCriteriaLoadRateValue=None, DownstreamSeqErrorsThresholdMode=None, DownstreamSeqErrorsThresholdValue=None, Downstream_passFailFrequency=None, UpstreamDataErrorThresholdMode=None, UpstreamDataErrorThresholdValue=None, UpstreamEnableDataIntegrityPassFail=None, UpstreamEnableLatencyPassFail=None, UpstreamEnableRatePassFail=None, UpstreamEnableSequenceErrorsPassFail=None, UpstreamEnableStandardDeviationPassFail=None, UpstreamLatencyThresholdMode=None, UpstreamLatencyThresholdScale=None, UpstreamLatencyThresholdValue=None, UpstreamLatencyVarThresholdMode=None, UpstreamLatencyVariationThresholdScale=None, UpstreamLatencyVariationThresholdValue=None, UpstreamPassCriteriaLoadRateMode=None, UpstreamPassCriteriaLoadRateScale=None, UpstreamPassCriteriaLoadRateValue=None, UpstreamSeqErrorsThresholdMode=None, UpstreamSeqErrorsThresholdValue=None, Upstream_passFailFrequency=None):
        """Updates passCriteria resource on the server.

        Args
        ----
        - DownstreamDataErrorThresholdMode (str(average | maximum)): Signifies threshold mode for downstream data error.
        - DownstreamDataErrorThresholdValue (number): Signifies the downstream data error threshold value.
        - DownstreamEnableDataIntegrityPassFail (bool): if true, enables pass or faill of data integrity for downstream.
        - DownstreamEnableLatencyPassFail (bool): If true, enables latency pass fail for downstream.
        - DownstreamEnableRatePassFail (bool): If true, enables pass fail rate for downstream.
        - DownstreamEnableSequenceErrorsPassFail (bool): If true, enables the pass fail for sequence errors for downstream.
        - DownstreamEnableStandardDeviationPassFail (bool): If true, enables pass fail of standard deviation for downstream.
        - DownstreamLatencyThresholdMode (str(average | maximum)): Signifies the latency threshold mode for downstream.
        - DownstreamLatencyThresholdScale (str(ms | ns | us)): Signifies the threshold scale for downstream latency.
        - DownstreamLatencyThresholdValue (number): Signifies the latency threshold value for downstream.
        - DownstreamLatencyVarThresholdMode (str(average | maximum)): Signifies latency variation threshold mode for downstream.
        - DownstreamLatencyVariationThresholdScale (str(ms | ns | us)): Signifies latency variation threshold scale for downstream.
        - DownstreamLatencyVariationThresholdValue (number): Signifies the latency variation threshold value for downstream.
        - DownstreamPassCriteriaLoadRateMode (str(average | minimum)): Signifies the pass criteria load rate mode for downstream.
        - DownstreamPassCriteriaLoadRateScale (str(fps | gbps | kbps | mbps | percent)): Signifies the pass criteria load rate scale for downstream.
        - DownstreamPassCriteriaLoadRateValue (number): Signifies pass criteria load rate value for downstream.
        - DownstreamSeqErrorsThresholdMode (str(average | maximum)): Signifies the threshold mode for sequence errors for downstream.
        - DownstreamSeqErrorsThresholdValue (number): Signifies the threshold value for sequence errors for downstream.
        - Downstream_passFailFrequency (str(framesizes | trials)): NOT DEFINED
        - UpstreamDataErrorThresholdMode (str(average | maximum)): Signifies the data error threshold mode for upstream.
        - UpstreamDataErrorThresholdValue (number): Signifies data error threshold value for upstream.
        - UpstreamEnableDataIntegrityPassFail (bool): If true, enables pass fail of data integrity for upstream.
        - UpstreamEnableLatencyPassFail (bool): If true, enables latency pass fail for upstream.
        - UpstreamEnableRatePassFail (bool): If true, enables the rate of pass fail for upstream.
        - UpstreamEnableSequenceErrorsPassFail (bool): If true, enables sequence errors pass fail for upstream.
        - UpstreamEnableStandardDeviationPassFail (bool): If true, enables standard deviation of pass and fail for upstream.
        - UpstreamLatencyThresholdMode (str(average | maximum)): Signifies the latency threshold mode for upstream.
        - UpstreamLatencyThresholdScale (str(ms | ns | us)): Signifies the latency threshold scale for upstream.
        - UpstreamLatencyThresholdValue (number): It is the latency threshold value for upstream.
        - UpstreamLatencyVarThresholdMode (str(average | maximum)): Signifies the latency variation threshold mode for upstream.
        - UpstreamLatencyVariationThresholdScale (str(ms | ns | us)): It is the latency variation threshold scale for upstream.
        - UpstreamLatencyVariationThresholdValue (number): Signifies the latency variation threshold value for upstream.
        - UpstreamPassCriteriaLoadRateMode (str(average | minimum)): Signifies the pass criteria load rate mode for upstream.
        - UpstreamPassCriteriaLoadRateScale (str(fps | gbps | kbps | mbps | percent)): Signifies pass criteria for load rate scale for upstream.
        - UpstreamPassCriteriaLoadRateValue (number): Signifies the pass criteria load rate value for upstream.
        - UpstreamSeqErrorsThresholdMode (str(average | maximum)): Signifies the sequence errors threshold mode for upstream.
        - UpstreamSeqErrorsThresholdValue (number): Signifies sequence errors threshold value for upstream.
        - Upstream_passFailFrequency (str(framesizes | trials)): NOT DEFINED

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
