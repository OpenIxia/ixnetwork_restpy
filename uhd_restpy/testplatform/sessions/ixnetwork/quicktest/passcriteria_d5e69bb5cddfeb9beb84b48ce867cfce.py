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
import sys
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


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
    _SDM_ENUM_MAP = {
        'downstreamDataErrorThresholdMode': ['average', 'maximum'],
        'downstreamLatencyThresholdMode': ['average', 'maximum'],
        'downstreamLatencyThresholdScale': ['ms', 'ns', 'us'],
        'downstreamLatencyVarThresholdMode': ['average', 'maximum'],
        'downstreamLatencyVariationThresholdScale': ['ms', 'ns', 'us'],
        'downstreamPassCriteriaLoadRateMode': ['average', 'minimum'],
        'downstreamPassCriteriaLoadRateScale': ['fps', 'gbps', 'kbps', 'mbps', 'percent'],
        'downstreamSeqErrorsThresholdMode': ['average', 'maximum'],
        'downstream_passFailFrequency': ['framesizes', 'trials'],
        'upstreamDataErrorThresholdMode': ['average', 'maximum'],
        'upstreamLatencyThresholdMode': ['average', 'maximum'],
        'upstreamLatencyThresholdScale': ['ms', 'ns', 'us'],
        'upstreamLatencyVarThresholdMode': ['average', 'maximum'],
        'upstreamLatencyVariationThresholdScale': ['ms', 'ns', 'us'],
        'upstreamPassCriteriaLoadRateMode': ['average', 'minimum'],
        'upstreamPassCriteriaLoadRateScale': ['fps', 'gbps', 'kbps', 'mbps', 'percent'],
        'upstreamSeqErrorsThresholdMode': ['average', 'maximum'],
        'upstream_passFailFrequency': ['framesizes', 'trials'],
    }

    def __init__(self, parent, list_op=False):
        super(PassCriteria, self).__init__(parent, list_op)

    @property
    def DownstreamDataErrorThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): Signifies threshold mode for downstream data error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamDataErrorThresholdMode'])
    @DownstreamDataErrorThresholdMode.setter
    def DownstreamDataErrorThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamDataErrorThresholdMode'], value)

    @property
    def DownstreamDataErrorThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the downstream data error threshold value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamDataErrorThresholdValue'])
    @DownstreamDataErrorThresholdValue.setter
    def DownstreamDataErrorThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamDataErrorThresholdValue'], value)

    @property
    def DownstreamEnableDataIntegrityPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: if true, enables pass or faill of data integrity for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamEnableDataIntegrityPassFail'])
    @DownstreamEnableDataIntegrityPassFail.setter
    def DownstreamEnableDataIntegrityPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamEnableDataIntegrityPassFail'], value)

    @property
    def DownstreamEnableLatencyPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables latency pass fail for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamEnableLatencyPassFail'])
    @DownstreamEnableLatencyPassFail.setter
    def DownstreamEnableLatencyPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamEnableLatencyPassFail'], value)

    @property
    def DownstreamEnableRatePassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables pass fail rate for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamEnableRatePassFail'])
    @DownstreamEnableRatePassFail.setter
    def DownstreamEnableRatePassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamEnableRatePassFail'], value)

    @property
    def DownstreamEnableSequenceErrorsPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the pass fail for sequence errors for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamEnableSequenceErrorsPassFail'])
    @DownstreamEnableSequenceErrorsPassFail.setter
    def DownstreamEnableSequenceErrorsPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamEnableSequenceErrorsPassFail'], value)

    @property
    def DownstreamEnableStandardDeviationPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables pass fail of standard deviation for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamEnableStandardDeviationPassFail'])
    @DownstreamEnableStandardDeviationPassFail.setter
    def DownstreamEnableStandardDeviationPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamEnableStandardDeviationPassFail'], value)

    @property
    def DownstreamLatencyThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): Signifies the latency threshold mode for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLatencyThresholdMode'])
    @DownstreamLatencyThresholdMode.setter
    def DownstreamLatencyThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLatencyThresholdMode'], value)

    @property
    def DownstreamLatencyThresholdScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | ns | us): Signifies the threshold scale for downstream latency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLatencyThresholdScale'])
    @DownstreamLatencyThresholdScale.setter
    def DownstreamLatencyThresholdScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLatencyThresholdScale'], value)

    @property
    def DownstreamLatencyThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the latency threshold value for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLatencyThresholdValue'])
    @DownstreamLatencyThresholdValue.setter
    def DownstreamLatencyThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLatencyThresholdValue'], value)

    @property
    def DownstreamLatencyVarThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): Signifies latency variation threshold mode for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLatencyVarThresholdMode'])
    @DownstreamLatencyVarThresholdMode.setter
    def DownstreamLatencyVarThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLatencyVarThresholdMode'], value)

    @property
    def DownstreamLatencyVariationThresholdScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | ns | us): Signifies latency variation threshold scale for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLatencyVariationThresholdScale'])
    @DownstreamLatencyVariationThresholdScale.setter
    def DownstreamLatencyVariationThresholdScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLatencyVariationThresholdScale'], value)

    @property
    def DownstreamLatencyVariationThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the latency variation threshold value for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamLatencyVariationThresholdValue'])
    @DownstreamLatencyVariationThresholdValue.setter
    def DownstreamLatencyVariationThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamLatencyVariationThresholdValue'], value)

    @property
    def DownstreamPassCriteriaLoadRateMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | minimum): Signifies the pass criteria load rate mode for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamPassCriteriaLoadRateMode'])
    @DownstreamPassCriteriaLoadRateMode.setter
    def DownstreamPassCriteriaLoadRateMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamPassCriteriaLoadRateMode'], value)

    @property
    def DownstreamPassCriteriaLoadRateScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fps | gbps | kbps | mbps | percent): Signifies the pass criteria load rate scale for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamPassCriteriaLoadRateScale'])
    @DownstreamPassCriteriaLoadRateScale.setter
    def DownstreamPassCriteriaLoadRateScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamPassCriteriaLoadRateScale'], value)

    @property
    def DownstreamPassCriteriaLoadRateValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies pass criteria load rate value for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamPassCriteriaLoadRateValue'])
    @DownstreamPassCriteriaLoadRateValue.setter
    def DownstreamPassCriteriaLoadRateValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamPassCriteriaLoadRateValue'], value)

    @property
    def DownstreamSeqErrorsThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): Signifies the threshold mode for sequence errors for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamSeqErrorsThresholdMode'])
    @DownstreamSeqErrorsThresholdMode.setter
    def DownstreamSeqErrorsThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamSeqErrorsThresholdMode'], value)

    @property
    def DownstreamSeqErrorsThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the threshold value for sequence errors for downstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DownstreamSeqErrorsThresholdValue'])
    @DownstreamSeqErrorsThresholdValue.setter
    def DownstreamSeqErrorsThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['DownstreamSeqErrorsThresholdValue'], value)

    @property
    def Downstream_passFailFrequency(self):
        # type: () -> str
        """
        Returns
        -------
        - str(framesizes | trials): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Downstream_passFailFrequency'])
    @Downstream_passFailFrequency.setter
    def Downstream_passFailFrequency(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Downstream_passFailFrequency'], value)

    @property
    def UpstreamDataErrorThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): Signifies the data error threshold mode for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamDataErrorThresholdMode'])
    @UpstreamDataErrorThresholdMode.setter
    def UpstreamDataErrorThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamDataErrorThresholdMode'], value)

    @property
    def UpstreamDataErrorThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies data error threshold value for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamDataErrorThresholdValue'])
    @UpstreamDataErrorThresholdValue.setter
    def UpstreamDataErrorThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamDataErrorThresholdValue'], value)

    @property
    def UpstreamEnableDataIntegrityPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables pass fail of data integrity for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamEnableDataIntegrityPassFail'])
    @UpstreamEnableDataIntegrityPassFail.setter
    def UpstreamEnableDataIntegrityPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamEnableDataIntegrityPassFail'], value)

    @property
    def UpstreamEnableLatencyPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables latency pass fail for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamEnableLatencyPassFail'])
    @UpstreamEnableLatencyPassFail.setter
    def UpstreamEnableLatencyPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamEnableLatencyPassFail'], value)

    @property
    def UpstreamEnableRatePassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the rate of pass fail for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamEnableRatePassFail'])
    @UpstreamEnableRatePassFail.setter
    def UpstreamEnableRatePassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamEnableRatePassFail'], value)

    @property
    def UpstreamEnableSequenceErrorsPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables sequence errors pass fail for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamEnableSequenceErrorsPassFail'])
    @UpstreamEnableSequenceErrorsPassFail.setter
    def UpstreamEnableSequenceErrorsPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamEnableSequenceErrorsPassFail'], value)

    @property
    def UpstreamEnableStandardDeviationPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables standard deviation of pass and fail for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamEnableStandardDeviationPassFail'])
    @UpstreamEnableStandardDeviationPassFail.setter
    def UpstreamEnableStandardDeviationPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamEnableStandardDeviationPassFail'], value)

    @property
    def UpstreamLatencyThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): Signifies the latency threshold mode for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLatencyThresholdMode'])
    @UpstreamLatencyThresholdMode.setter
    def UpstreamLatencyThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLatencyThresholdMode'], value)

    @property
    def UpstreamLatencyThresholdScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | ns | us): Signifies the latency threshold scale for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLatencyThresholdScale'])
    @UpstreamLatencyThresholdScale.setter
    def UpstreamLatencyThresholdScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLatencyThresholdScale'], value)

    @property
    def UpstreamLatencyThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It is the latency threshold value for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLatencyThresholdValue'])
    @UpstreamLatencyThresholdValue.setter
    def UpstreamLatencyThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLatencyThresholdValue'], value)

    @property
    def UpstreamLatencyVarThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): Signifies the latency variation threshold mode for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLatencyVarThresholdMode'])
    @UpstreamLatencyVarThresholdMode.setter
    def UpstreamLatencyVarThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLatencyVarThresholdMode'], value)

    @property
    def UpstreamLatencyVariationThresholdScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | ns | us): It is the latency variation threshold scale for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLatencyVariationThresholdScale'])
    @UpstreamLatencyVariationThresholdScale.setter
    def UpstreamLatencyVariationThresholdScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLatencyVariationThresholdScale'], value)

    @property
    def UpstreamLatencyVariationThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the latency variation threshold value for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamLatencyVariationThresholdValue'])
    @UpstreamLatencyVariationThresholdValue.setter
    def UpstreamLatencyVariationThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamLatencyVariationThresholdValue'], value)

    @property
    def UpstreamPassCriteriaLoadRateMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | minimum): Signifies the pass criteria load rate mode for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamPassCriteriaLoadRateMode'])
    @UpstreamPassCriteriaLoadRateMode.setter
    def UpstreamPassCriteriaLoadRateMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamPassCriteriaLoadRateMode'], value)

    @property
    def UpstreamPassCriteriaLoadRateScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fps | gbps | kbps | mbps | percent): Signifies pass criteria for load rate scale for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamPassCriteriaLoadRateScale'])
    @UpstreamPassCriteriaLoadRateScale.setter
    def UpstreamPassCriteriaLoadRateScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamPassCriteriaLoadRateScale'], value)

    @property
    def UpstreamPassCriteriaLoadRateValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the pass criteria load rate value for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamPassCriteriaLoadRateValue'])
    @UpstreamPassCriteriaLoadRateValue.setter
    def UpstreamPassCriteriaLoadRateValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamPassCriteriaLoadRateValue'], value)

    @property
    def UpstreamSeqErrorsThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): Signifies the sequence errors threshold mode for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamSeqErrorsThresholdMode'])
    @UpstreamSeqErrorsThresholdMode.setter
    def UpstreamSeqErrorsThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamSeqErrorsThresholdMode'], value)

    @property
    def UpstreamSeqErrorsThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies sequence errors threshold value for upstream.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpstreamSeqErrorsThresholdValue'])
    @UpstreamSeqErrorsThresholdValue.setter
    def UpstreamSeqErrorsThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['UpstreamSeqErrorsThresholdValue'], value)

    @property
    def Upstream_passFailFrequency(self):
        # type: () -> str
        """
        Returns
        -------
        - str(framesizes | trials): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Upstream_passFailFrequency'])
    @Upstream_passFailFrequency.setter
    def Upstream_passFailFrequency(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Upstream_passFailFrequency'], value)

    def update(self, DownstreamDataErrorThresholdMode=None, DownstreamDataErrorThresholdValue=None, DownstreamEnableDataIntegrityPassFail=None, DownstreamEnableLatencyPassFail=None, DownstreamEnableRatePassFail=None, DownstreamEnableSequenceErrorsPassFail=None, DownstreamEnableStandardDeviationPassFail=None, DownstreamLatencyThresholdMode=None, DownstreamLatencyThresholdScale=None, DownstreamLatencyThresholdValue=None, DownstreamLatencyVarThresholdMode=None, DownstreamLatencyVariationThresholdScale=None, DownstreamLatencyVariationThresholdValue=None, DownstreamPassCriteriaLoadRateMode=None, DownstreamPassCriteriaLoadRateScale=None, DownstreamPassCriteriaLoadRateValue=None, DownstreamSeqErrorsThresholdMode=None, DownstreamSeqErrorsThresholdValue=None, Downstream_passFailFrequency=None, UpstreamDataErrorThresholdMode=None, UpstreamDataErrorThresholdValue=None, UpstreamEnableDataIntegrityPassFail=None, UpstreamEnableLatencyPassFail=None, UpstreamEnableRatePassFail=None, UpstreamEnableSequenceErrorsPassFail=None, UpstreamEnableStandardDeviationPassFail=None, UpstreamLatencyThresholdMode=None, UpstreamLatencyThresholdScale=None, UpstreamLatencyThresholdValue=None, UpstreamLatencyVarThresholdMode=None, UpstreamLatencyVariationThresholdScale=None, UpstreamLatencyVariationThresholdValue=None, UpstreamPassCriteriaLoadRateMode=None, UpstreamPassCriteriaLoadRateScale=None, UpstreamPassCriteriaLoadRateValue=None, UpstreamSeqErrorsThresholdMode=None, UpstreamSeqErrorsThresholdValue=None, Upstream_passFailFrequency=None):
        # type: (str, int, bool, bool, bool, bool, bool, str, str, int, str, str, int, str, str, int, str, int, str, str, int, bool, bool, bool, bool, bool, str, str, int, str, str, int, str, str, int, str, int, str) -> PassCriteria
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

    def find(self, DownstreamDataErrorThresholdMode=None, DownstreamDataErrorThresholdValue=None, DownstreamEnableDataIntegrityPassFail=None, DownstreamEnableLatencyPassFail=None, DownstreamEnableRatePassFail=None, DownstreamEnableSequenceErrorsPassFail=None, DownstreamEnableStandardDeviationPassFail=None, DownstreamLatencyThresholdMode=None, DownstreamLatencyThresholdScale=None, DownstreamLatencyThresholdValue=None, DownstreamLatencyVarThresholdMode=None, DownstreamLatencyVariationThresholdScale=None, DownstreamLatencyVariationThresholdValue=None, DownstreamPassCriteriaLoadRateMode=None, DownstreamPassCriteriaLoadRateScale=None, DownstreamPassCriteriaLoadRateValue=None, DownstreamSeqErrorsThresholdMode=None, DownstreamSeqErrorsThresholdValue=None, Downstream_passFailFrequency=None, UpstreamDataErrorThresholdMode=None, UpstreamDataErrorThresholdValue=None, UpstreamEnableDataIntegrityPassFail=None, UpstreamEnableLatencyPassFail=None, UpstreamEnableRatePassFail=None, UpstreamEnableSequenceErrorsPassFail=None, UpstreamEnableStandardDeviationPassFail=None, UpstreamLatencyThresholdMode=None, UpstreamLatencyThresholdScale=None, UpstreamLatencyThresholdValue=None, UpstreamLatencyVarThresholdMode=None, UpstreamLatencyVariationThresholdScale=None, UpstreamLatencyVariationThresholdValue=None, UpstreamPassCriteriaLoadRateMode=None, UpstreamPassCriteriaLoadRateScale=None, UpstreamPassCriteriaLoadRateValue=None, UpstreamSeqErrorsThresholdMode=None, UpstreamSeqErrorsThresholdValue=None, Upstream_passFailFrequency=None):
        # type: (str, int, bool, bool, bool, bool, bool, str, str, int, str, str, int, str, str, int, str, int, str, str, int, bool, bool, bool, bool, bool, str, str, int, str, str, int, str, str, int, str, int, str) -> PassCriteria
        """Finds and retrieves passCriteria resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve passCriteria resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all passCriteria resources from the server.

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

        Returns
        -------
        - self: This instance with matching passCriteria resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of passCriteria data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the passCriteria resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('apply', payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyAsync', payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyAsyncResult', payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('generateReport', payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
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
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('waitForTest', payload=payload, response_object=None)
