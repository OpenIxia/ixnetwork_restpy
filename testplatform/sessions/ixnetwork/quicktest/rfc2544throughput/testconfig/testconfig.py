# Copyright 1997 - 2018 by IXIA Keysight
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
	"""The TestConfig class encapsulates a required testConfig node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the TestConfig property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'testConfig'

	def __init__(self, parent):
		super(TestConfig, self).__init__(parent)

	@property
	def BackoffIteration(self):
		"""This enables the test to run an extra iteration for calculating the Backoff Latency.

		Returns:
			number
		"""
		return self._get_attribute('backoffIteration')
	@BackoffIteration.setter
	def BackoffIteration(self, value):
		self._set_attribute('backoffIteration', value)

	@property
	def BinaryBackoff(self):
		"""Specifies the percentage of binary backoff.

		Returns:
			number
		"""
		return self._get_attribute('binaryBackoff')
	@BinaryBackoff.setter
	def BinaryBackoff(self, value):
		self._set_attribute('binaryBackoff', value)

	@property
	def BinaryFrameLossUnit(self):
		"""The frame loss unit for traffic in binary.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('binaryFrameLossUnit')
	@BinaryFrameLossUnit.setter
	def BinaryFrameLossUnit(self, value):
		self._set_attribute('binaryFrameLossUnit', value)

	@property
	def BinaryLoadUnit(self):
		"""The load unit value in binary. Possible values include:

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('binaryLoadUnit')
	@BinaryLoadUnit.setter
	def BinaryLoadUnit(self, value):
		self._set_attribute('binaryLoadUnit', value)

	@property
	def BinaryResolution(self):
		"""Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.

		Returns:
			number
		"""
		return self._get_attribute('binaryResolution')
	@BinaryResolution.setter
	def BinaryResolution(self, value):
		self._set_attribute('binaryResolution', value)

	@property
	def BinarySearchType(self):
		"""The binary search type value. Possible values include:

		Returns:
			str(linear|perFlow|perPort|perTrafficItem)
		"""
		return self._get_attribute('binarySearchType')
	@BinarySearchType.setter
	def BinarySearchType(self, value):
		self._set_attribute('binarySearchType', value)

	@property
	def BinaryTiLoss(self):
		"""Use loss across Rx Ports

		Returns:
			bool
		"""
		return self._get_attribute('binaryTiLoss')
	@BinaryTiLoss.setter
	def BinaryTiLoss(self, value):
		self._set_attribute('binaryTiLoss', value)

	@property
	def BinaryTolerance(self):
		"""The binary tolerance level.

		Returns:
			number
		"""
		return self._get_attribute('binaryTolerance')
	@BinaryTolerance.setter
	def BinaryTolerance(self, value):
		self._set_attribute('binaryTolerance', value)

	@property
	def Binary_delay_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('binary_delay_enableAccLoss')
	@Binary_delay_enableAccLoss.setter
	def Binary_delay_enableAccLoss(self, value):
		self._set_attribute('binary_delay_enableAccLoss', value)

	@property
	def Binary_delay_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('binary_delay_modeAccLoss')
	@Binary_delay_modeAccLoss.setter
	def Binary_delay_modeAccLoss(self, value):
		self._set_attribute('binary_delay_modeAccLoss', value)

	@property
	def Binary_delay_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('binary_delay_scaleAccLoss')
	@Binary_delay_scaleAccLoss.setter
	def Binary_delay_scaleAccLoss(self, value):
		self._set_attribute('binary_delay_scaleAccLoss', value)

	@property
	def Binary_delay_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binary_delay_thresholdAccLoss')
	@Binary_delay_thresholdAccLoss.setter
	def Binary_delay_thresholdAccLoss(self, value):
		self._set_attribute('binary_delay_thresholdAccLoss', value)

	@property
	def Binary_flooded_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('binary_flooded_enableAccLoss')
	@Binary_flooded_enableAccLoss.setter
	def Binary_flooded_enableAccLoss(self, value):
		self._set_attribute('binary_flooded_enableAccLoss', value)

	@property
	def Binary_flooded_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binary_flooded_thresholdAccLoss')
	@Binary_flooded_thresholdAccLoss.setter
	def Binary_flooded_thresholdAccLoss(self, value):
		self._set_attribute('binary_flooded_thresholdAccLoss', value)

	@property
	def Binary_integrity_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('binary_integrity_enableAccLoss')
	@Binary_integrity_enableAccLoss.setter
	def Binary_integrity_enableAccLoss(self, value):
		self._set_attribute('binary_integrity_enableAccLoss', value)

	@property
	def Binary_integrity_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binary_integrity_thresholdAccLoss')
	@Binary_integrity_thresholdAccLoss.setter
	def Binary_integrity_thresholdAccLoss(self, value):
		self._set_attribute('binary_integrity_thresholdAccLoss', value)

	@property
	def Binary_latency_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('binary_latency_enableAccLoss')
	@Binary_latency_enableAccLoss.setter
	def Binary_latency_enableAccLoss(self, value):
		self._set_attribute('binary_latency_enableAccLoss', value)

	@property
	def Binary_latency_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('binary_latency_modeAccLoss')
	@Binary_latency_modeAccLoss.setter
	def Binary_latency_modeAccLoss(self, value):
		self._set_attribute('binary_latency_modeAccLoss', value)

	@property
	def Binary_latency_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('binary_latency_scaleAccLoss')
	@Binary_latency_scaleAccLoss.setter
	def Binary_latency_scaleAccLoss(self, value):
		self._set_attribute('binary_latency_scaleAccLoss', value)

	@property
	def Binary_latency_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binary_latency_thresholdAccLoss')
	@Binary_latency_thresholdAccLoss.setter
	def Binary_latency_thresholdAccLoss(self, value):
		self._set_attribute('binary_latency_thresholdAccLoss', value)

	@property
	def Binary_seq_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('binary_seq_enableAccLoss')
	@Binary_seq_enableAccLoss.setter
	def Binary_seq_enableAccLoss(self, value):
		self._set_attribute('binary_seq_enableAccLoss', value)

	@property
	def Binary_seq_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('binary_seq_modeAccLoss')
	@Binary_seq_modeAccLoss.setter
	def Binary_seq_modeAccLoss(self, value):
		self._set_attribute('binary_seq_modeAccLoss', value)

	@property
	def Binary_seq_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('binary_seq_thresholdAccLoss')
	@Binary_seq_thresholdAccLoss.setter
	def Binary_seq_thresholdAccLoss(self, value):
		self._set_attribute('binary_seq_thresholdAccLoss', value)

	@property
	def BurstSize(self):
		"""The number of packets that are sent in a burst.

		Returns:
			number
		"""
		return self._get_attribute('burstSize')
	@BurstSize.setter
	def BurstSize(self, value):
		self._set_attribute('burstSize', value)

	@property
	def CalculateJitter(self):
		"""If true, calculates jitter.

		Returns:
			bool
		"""
		return self._get_attribute('calculateJitter')
	@CalculateJitter.setter
	def CalculateJitter(self, value):
		self._set_attribute('calculateJitter', value)

	@property
	def CalculateLatency(self):
		"""If true, calculates the latency.

		Returns:
			bool
		"""
		return self._get_attribute('calculateLatency')
	@CalculateLatency.setter
	def CalculateLatency(self, value):
		self._set_attribute('calculateLatency', value)

	@property
	def ComboBackoff(self):
		"""The backoff combination of the test configuration.

		Returns:
			number
		"""
		return self._get_attribute('comboBackoff')
	@ComboBackoff.setter
	def ComboBackoff(self, value):
		self._set_attribute('comboBackoff', value)

	@property
	def ComboFrameLossUnit(self):
		"""The frame loss unit for traffic in binary.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('comboFrameLossUnit')
	@ComboFrameLossUnit.setter
	def ComboFrameLossUnit(self, value):
		self._set_attribute('comboFrameLossUnit', value)

	@property
	def ComboLoadUnit(self):
		"""The combination of load units. Possible values include:

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('comboLoadUnit')
	@ComboLoadUnit.setter
	def ComboLoadUnit(self, value):
		self._set_attribute('comboLoadUnit', value)

	@property
	def ComboResolution(self):
		"""The combined resolution value.

		Returns:
			number
		"""
		return self._get_attribute('comboResolution')
	@ComboResolution.setter
	def ComboResolution(self, value):
		self._set_attribute('comboResolution', value)

	@property
	def ComboTiLoss(self):
		"""Use loss across Rx Ports

		Returns:
			bool
		"""
		return self._get_attribute('comboTiLoss')
	@ComboTiLoss.setter
	def ComboTiLoss(self, value):
		self._set_attribute('comboTiLoss', value)

	@property
	def ComboTolerance(self):
		"""The combined tolerance level.

		Returns:
			number
		"""
		return self._get_attribute('comboTolerance')
	@ComboTolerance.setter
	def ComboTolerance(self, value):
		self._set_attribute('comboTolerance', value)

	@property
	def Combo_delay_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('combo_delay_enableAccLoss')
	@Combo_delay_enableAccLoss.setter
	def Combo_delay_enableAccLoss(self, value):
		self._set_attribute('combo_delay_enableAccLoss', value)

	@property
	def Combo_delay_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('combo_delay_modeAccLoss')
	@Combo_delay_modeAccLoss.setter
	def Combo_delay_modeAccLoss(self, value):
		self._set_attribute('combo_delay_modeAccLoss', value)

	@property
	def Combo_delay_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('combo_delay_scaleAccLoss')
	@Combo_delay_scaleAccLoss.setter
	def Combo_delay_scaleAccLoss(self, value):
		self._set_attribute('combo_delay_scaleAccLoss', value)

	@property
	def Combo_delay_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('combo_delay_thresholdAccLoss')
	@Combo_delay_thresholdAccLoss.setter
	def Combo_delay_thresholdAccLoss(self, value):
		self._set_attribute('combo_delay_thresholdAccLoss', value)

	@property
	def Combo_flooded_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('combo_flooded_enableAccLoss')
	@Combo_flooded_enableAccLoss.setter
	def Combo_flooded_enableAccLoss(self, value):
		self._set_attribute('combo_flooded_enableAccLoss', value)

	@property
	def Combo_flooded_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('combo_flooded_thresholdAccLoss')
	@Combo_flooded_thresholdAccLoss.setter
	def Combo_flooded_thresholdAccLoss(self, value):
		self._set_attribute('combo_flooded_thresholdAccLoss', value)

	@property
	def Combo_integrity_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('combo_integrity_enableAccLoss')
	@Combo_integrity_enableAccLoss.setter
	def Combo_integrity_enableAccLoss(self, value):
		self._set_attribute('combo_integrity_enableAccLoss', value)

	@property
	def Combo_integrity_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('combo_integrity_thresholdAccLoss')
	@Combo_integrity_thresholdAccLoss.setter
	def Combo_integrity_thresholdAccLoss(self, value):
		self._set_attribute('combo_integrity_thresholdAccLoss', value)

	@property
	def Combo_latency_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('combo_latency_enableAccLoss')
	@Combo_latency_enableAccLoss.setter
	def Combo_latency_enableAccLoss(self, value):
		self._set_attribute('combo_latency_enableAccLoss', value)

	@property
	def Combo_latency_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('combo_latency_modeAccLoss')
	@Combo_latency_modeAccLoss.setter
	def Combo_latency_modeAccLoss(self, value):
		self._set_attribute('combo_latency_modeAccLoss', value)

	@property
	def Combo_latency_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('combo_latency_scaleAccLoss')
	@Combo_latency_scaleAccLoss.setter
	def Combo_latency_scaleAccLoss(self, value):
		self._set_attribute('combo_latency_scaleAccLoss', value)

	@property
	def Combo_latency_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('combo_latency_thresholdAccLoss')
	@Combo_latency_thresholdAccLoss.setter
	def Combo_latency_thresholdAccLoss(self, value):
		self._set_attribute('combo_latency_thresholdAccLoss', value)

	@property
	def Combo_seq_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('combo_seq_enableAccLoss')
	@Combo_seq_enableAccLoss.setter
	def Combo_seq_enableAccLoss(self, value):
		self._set_attribute('combo_seq_enableAccLoss', value)

	@property
	def Combo_seq_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('combo_seq_modeAccLoss')
	@Combo_seq_modeAccLoss.setter
	def Combo_seq_modeAccLoss(self, value):
		self._set_attribute('combo_seq_modeAccLoss', value)

	@property
	def Combo_seq_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('combo_seq_thresholdAccLoss')
	@Combo_seq_thresholdAccLoss.setter
	def Combo_seq_thresholdAccLoss(self, value):
		self._set_attribute('combo_seq_thresholdAccLoss', value)

	@property
	def CountRandomFrameSize(self):
		"""Randomly counts the frame size.

		Returns:
			number
		"""
		return self._get_attribute('countRandomFrameSize')
	@CountRandomFrameSize.setter
	def CountRandomFrameSize(self, value):
		self._set_attribute('countRandomFrameSize', value)

	@property
	def CountRandomIpRatio(self):
		"""Sets the count of the random ip ratio loop

		Returns:
			number
		"""
		return self._get_attribute('countRandomIpRatio')
	@CountRandomIpRatio.setter
	def CountRandomIpRatio(self, value):
		self._set_attribute('countRandomIpRatio', value)

	@property
	def CountRandomLoadRate(self):
		"""Randomly counts the load rate.

		Returns:
			number
		"""
		return self._get_attribute('countRandomLoadRate')
	@CountRandomLoadRate.setter
	def CountRandomLoadRate(self, value):
		self._set_attribute('countRandomLoadRate', value)

	@property
	def CustomLoadUnit(self):
		"""Specifies the custom load unit. Possible values include:

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('customLoadUnit')
	@CustomLoadUnit.setter
	def CustomLoadUnit(self, value):
		self._set_attribute('customLoadUnit', value)

	@property
	def CustomTiLoss(self):
		"""Use loss across Rx Ports

		Returns:
			bool
		"""
		return self._get_attribute('customTiLoss')
	@CustomTiLoss.setter
	def CustomTiLoss(self, value):
		self._set_attribute('customTiLoss', value)

	@property
	def Custom_binary_delay_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('custom_binary_delay_enableAccLoss')
	@Custom_binary_delay_enableAccLoss.setter
	def Custom_binary_delay_enableAccLoss(self, value):
		self._set_attribute('custom_binary_delay_enableAccLoss', value)

	@property
	def Custom_binary_delay_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('custom_binary_delay_modeAccLoss')
	@Custom_binary_delay_modeAccLoss.setter
	def Custom_binary_delay_modeAccLoss(self, value):
		self._set_attribute('custom_binary_delay_modeAccLoss', value)

	@property
	def Custom_binary_delay_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('custom_binary_delay_scaleAccLoss')
	@Custom_binary_delay_scaleAccLoss.setter
	def Custom_binary_delay_scaleAccLoss(self, value):
		self._set_attribute('custom_binary_delay_scaleAccLoss', value)

	@property
	def Custom_binary_delay_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_binary_delay_thresholdAccLoss')
	@Custom_binary_delay_thresholdAccLoss.setter
	def Custom_binary_delay_thresholdAccLoss(self, value):
		self._set_attribute('custom_binary_delay_thresholdAccLoss', value)

	@property
	def Custom_binary_flooded_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('custom_binary_flooded_enableAccLoss')
	@Custom_binary_flooded_enableAccLoss.setter
	def Custom_binary_flooded_enableAccLoss(self, value):
		self._set_attribute('custom_binary_flooded_enableAccLoss', value)

	@property
	def Custom_binary_flooded_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_binary_flooded_thresholdAccLoss')
	@Custom_binary_flooded_thresholdAccLoss.setter
	def Custom_binary_flooded_thresholdAccLoss(self, value):
		self._set_attribute('custom_binary_flooded_thresholdAccLoss', value)

	@property
	def Custom_binary_integrity_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('custom_binary_integrity_enableAccLoss')
	@Custom_binary_integrity_enableAccLoss.setter
	def Custom_binary_integrity_enableAccLoss(self, value):
		self._set_attribute('custom_binary_integrity_enableAccLoss', value)

	@property
	def Custom_binary_integrity_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_binary_integrity_thresholdAccLoss')
	@Custom_binary_integrity_thresholdAccLoss.setter
	def Custom_binary_integrity_thresholdAccLoss(self, value):
		self._set_attribute('custom_binary_integrity_thresholdAccLoss', value)

	@property
	def Custom_binary_latency_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('custom_binary_latency_enableAccLoss')
	@Custom_binary_latency_enableAccLoss.setter
	def Custom_binary_latency_enableAccLoss(self, value):
		self._set_attribute('custom_binary_latency_enableAccLoss', value)

	@property
	def Custom_binary_latency_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('custom_binary_latency_modeAccLoss')
	@Custom_binary_latency_modeAccLoss.setter
	def Custom_binary_latency_modeAccLoss(self, value):
		self._set_attribute('custom_binary_latency_modeAccLoss', value)

	@property
	def Custom_binary_latency_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('custom_binary_latency_scaleAccLoss')
	@Custom_binary_latency_scaleAccLoss.setter
	def Custom_binary_latency_scaleAccLoss(self, value):
		self._set_attribute('custom_binary_latency_scaleAccLoss', value)

	@property
	def Custom_binary_latency_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_binary_latency_thresholdAccLoss')
	@Custom_binary_latency_thresholdAccLoss.setter
	def Custom_binary_latency_thresholdAccLoss(self, value):
		self._set_attribute('custom_binary_latency_thresholdAccLoss', value)

	@property
	def Custom_binary_peak_Backoff(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_binary_peak_Backoff')
	@Custom_binary_peak_Backoff.setter
	def Custom_binary_peak_Backoff(self, value):
		self._set_attribute('custom_binary_peak_Backoff', value)

	@property
	def Custom_binary_peak_FrameLossUnit(self):
		"""NOT DEFINED

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('custom_binary_peak_FrameLossUnit')
	@Custom_binary_peak_FrameLossUnit.setter
	def Custom_binary_peak_FrameLossUnit(self, value):
		self._set_attribute('custom_binary_peak_FrameLossUnit', value)

	@property
	def Custom_binary_peak_Resolution(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_binary_peak_Resolution')
	@Custom_binary_peak_Resolution.setter
	def Custom_binary_peak_Resolution(self, value):
		self._set_attribute('custom_binary_peak_Resolution', value)

	@property
	def Custom_binary_peak_Tolerance(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_binary_peak_Tolerance')
	@Custom_binary_peak_Tolerance.setter
	def Custom_binary_peak_Tolerance(self, value):
		self._set_attribute('custom_binary_peak_Tolerance', value)

	@property
	def Custom_binary_peak_initialValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_binary_peak_initialValue')
	@Custom_binary_peak_initialValue.setter
	def Custom_binary_peak_initialValue(self, value):
		self._set_attribute('custom_binary_peak_initialValue', value)

	@property
	def Custom_binary_peak_maxValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_binary_peak_maxValue')
	@Custom_binary_peak_maxValue.setter
	def Custom_binary_peak_maxValue(self, value):
		self._set_attribute('custom_binary_peak_maxValue', value)

	@property
	def Custom_binary_peak_minValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_binary_peak_minValue')
	@Custom_binary_peak_minValue.setter
	def Custom_binary_peak_minValue(self, value):
		self._set_attribute('custom_binary_peak_minValue', value)

	@property
	def Custom_binary_seq_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('custom_binary_seq_enableAccLoss')
	@Custom_binary_seq_enableAccLoss.setter
	def Custom_binary_seq_enableAccLoss(self, value):
		self._set_attribute('custom_binary_seq_enableAccLoss', value)

	@property
	def Custom_binary_seq_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('custom_binary_seq_modeAccLoss')
	@Custom_binary_seq_modeAccLoss.setter
	def Custom_binary_seq_modeAccLoss(self, value):
		self._set_attribute('custom_binary_seq_modeAccLoss', value)

	@property
	def Custom_binary_seq_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_binary_seq_thresholdAccLoss')
	@Custom_binary_seq_thresholdAccLoss.setter
	def Custom_binary_seq_thresholdAccLoss(self, value):
		self._set_attribute('custom_binary_seq_thresholdAccLoss', value)

	@property
	def Custom_peak_loadType(self):
		"""NOT DEFINED

		Returns:
			str(binary|custom|step)
		"""
		return self._get_attribute('custom_peak_loadType')
	@Custom_peak_loadType.setter
	def Custom_peak_loadType(self, value):
		self._set_attribute('custom_peak_loadType', value)

	@property
	def Custom_step_delay_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('custom_step_delay_enableAccLoss')
	@Custom_step_delay_enableAccLoss.setter
	def Custom_step_delay_enableAccLoss(self, value):
		self._set_attribute('custom_step_delay_enableAccLoss', value)

	@property
	def Custom_step_delay_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('custom_step_delay_modeAccLoss')
	@Custom_step_delay_modeAccLoss.setter
	def Custom_step_delay_modeAccLoss(self, value):
		self._set_attribute('custom_step_delay_modeAccLoss', value)

	@property
	def Custom_step_delay_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('custom_step_delay_scaleAccLoss')
	@Custom_step_delay_scaleAccLoss.setter
	def Custom_step_delay_scaleAccLoss(self, value):
		self._set_attribute('custom_step_delay_scaleAccLoss', value)

	@property
	def Custom_step_delay_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_step_delay_thresholdAccLoss')
	@Custom_step_delay_thresholdAccLoss.setter
	def Custom_step_delay_thresholdAccLoss(self, value):
		self._set_attribute('custom_step_delay_thresholdAccLoss', value)

	@property
	def Custom_step_flooded_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('custom_step_flooded_enableAccLoss')
	@Custom_step_flooded_enableAccLoss.setter
	def Custom_step_flooded_enableAccLoss(self, value):
		self._set_attribute('custom_step_flooded_enableAccLoss', value)

	@property
	def Custom_step_flooded_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_step_flooded_thresholdAccLoss')
	@Custom_step_flooded_thresholdAccLoss.setter
	def Custom_step_flooded_thresholdAccLoss(self, value):
		self._set_attribute('custom_step_flooded_thresholdAccLoss', value)

	@property
	def Custom_step_integrity_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('custom_step_integrity_enableAccLoss')
	@Custom_step_integrity_enableAccLoss.setter
	def Custom_step_integrity_enableAccLoss(self, value):
		self._set_attribute('custom_step_integrity_enableAccLoss', value)

	@property
	def Custom_step_integrity_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_step_integrity_thresholdAccLoss')
	@Custom_step_integrity_thresholdAccLoss.setter
	def Custom_step_integrity_thresholdAccLoss(self, value):
		self._set_attribute('custom_step_integrity_thresholdAccLoss', value)

	@property
	def Custom_step_latency_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('custom_step_latency_enableAccLoss')
	@Custom_step_latency_enableAccLoss.setter
	def Custom_step_latency_enableAccLoss(self, value):
		self._set_attribute('custom_step_latency_enableAccLoss', value)

	@property
	def Custom_step_latency_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('custom_step_latency_modeAccLoss')
	@Custom_step_latency_modeAccLoss.setter
	def Custom_step_latency_modeAccLoss(self, value):
		self._set_attribute('custom_step_latency_modeAccLoss', value)

	@property
	def Custom_step_latency_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('custom_step_latency_scaleAccLoss')
	@Custom_step_latency_scaleAccLoss.setter
	def Custom_step_latency_scaleAccLoss(self, value):
		self._set_attribute('custom_step_latency_scaleAccLoss', value)

	@property
	def Custom_step_latency_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_step_latency_thresholdAccLoss')
	@Custom_step_latency_thresholdAccLoss.setter
	def Custom_step_latency_thresholdAccLoss(self, value):
		self._set_attribute('custom_step_latency_thresholdAccLoss', value)

	@property
	def Custom_step_peak_FrameLossUnit(self):
		"""NOT DEFINED

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('custom_step_peak_FrameLossUnit')
	@Custom_step_peak_FrameLossUnit.setter
	def Custom_step_peak_FrameLossUnit(self, value):
		self._set_attribute('custom_step_peak_FrameLossUnit', value)

	@property
	def Custom_step_peak_initialValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_step_peak_initialValue')
	@Custom_step_peak_initialValue.setter
	def Custom_step_peak_initialValue(self, value):
		self._set_attribute('custom_step_peak_initialValue', value)

	@property
	def Custom_step_peak_maxValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_step_peak_maxValue')
	@Custom_step_peak_maxValue.setter
	def Custom_step_peak_maxValue(self, value):
		self._set_attribute('custom_step_peak_maxValue', value)

	@property
	def Custom_step_peak_stepTolerance(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_step_peak_stepTolerance')
	@Custom_step_peak_stepTolerance.setter
	def Custom_step_peak_stepTolerance(self, value):
		self._set_attribute('custom_step_peak_stepTolerance', value)

	@property
	def Custom_step_peak_stepValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_step_peak_stepValue')
	@Custom_step_peak_stepValue.setter
	def Custom_step_peak_stepValue(self, value):
		self._set_attribute('custom_step_peak_stepValue', value)

	@property
	def Custom_step_seq_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('custom_step_seq_enableAccLoss')
	@Custom_step_seq_enableAccLoss.setter
	def Custom_step_seq_enableAccLoss(self, value):
		self._set_attribute('custom_step_seq_enableAccLoss', value)

	@property
	def Custom_step_seq_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('custom_step_seq_modeAccLoss')
	@Custom_step_seq_modeAccLoss.setter
	def Custom_step_seq_modeAccLoss(self, value):
		self._set_attribute('custom_step_seq_modeAccLoss', value)

	@property
	def Custom_step_seq_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('custom_step_seq_thresholdAccLoss')
	@Custom_step_seq_thresholdAccLoss.setter
	def Custom_step_seq_thresholdAccLoss(self, value):
		self._set_attribute('custom_step_seq_thresholdAccLoss', value)

	@property
	def CustompeakvalueList(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('custompeakvalueList')
	@CustompeakvalueList.setter
	def CustompeakvalueList(self, value):
		self._set_attribute('custompeakvalueList', value)

	@property
	def DelayAfterTransmit(self):
		"""Specifies the amount of delay after every transmit

		Returns:
			number
		"""
		return self._get_attribute('delayAfterTransmit')
	@DelayAfterTransmit.setter
	def DelayAfterTransmit(self, value):
		self._set_attribute('delayAfterTransmit', value)

	@property
	def DetailedResultsEnabled(self):
		"""If true, it enables the detailed results for the fully meshed case

		Returns:
			bool
		"""
		return self._get_attribute('detailedResultsEnabled')
	@DetailedResultsEnabled.setter
	def DetailedResultsEnabled(self, value):
		self._set_attribute('detailedResultsEnabled', value)

	@property
	def Duration(self):
		"""sec

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableBackoffIteration(self):
		"""If true, enables back off iteration test.

		Returns:
			bool
		"""
		return self._get_attribute('enableBackoffIteration')
	@EnableBackoffIteration.setter
	def EnableBackoffIteration(self, value):
		self._set_attribute('enableBackoffIteration', value)

	@property
	def EnableDataIntegrity(self):
		"""If true, enables data integrity test.

		Returns:
			bool
		"""
		return self._get_attribute('enableDataIntegrity')
	@EnableDataIntegrity.setter
	def EnableDataIntegrity(self, value):
		self._set_attribute('enableDataIntegrity', value)

	@property
	def EnableExtraIterations(self):
		"""If true, more iterations are performed.

		Returns:
			bool
		"""
		return self._get_attribute('enableExtraIterations')
	@EnableExtraIterations.setter
	def EnableExtraIterations(self, value):
		self._set_attribute('enableExtraIterations', value)

	@property
	def EnableFastConvergence(self):
		"""If true, the test perform iterations using the fast convergence duration configured.

		Returns:
			bool
		"""
		return self._get_attribute('enableFastConvergence')
	@EnableFastConvergence.setter
	def EnableFastConvergence(self, value):
		self._set_attribute('enableFastConvergence', value)

	@property
	def EnableLayer1Rate(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableLayer1Rate')
	@EnableLayer1Rate.setter
	def EnableLayer1Rate(self, value):
		self._set_attribute('enableLayer1Rate', value)

	@property
	def EnableMinFrameSize(self):
		"""If Enabled, The minimum size of the frame is used .

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

	@property
	def EnableOldStatsForReef(self):
		"""If true, enables old statistics for reef load module.

		Returns:
			bool
		"""
		return self._get_attribute('enableOldStatsForReef')
	@EnableOldStatsForReef.setter
	def EnableOldStatsForReef(self, value):
		self._set_attribute('enableOldStatsForReef', value)

	@property
	def EnableSaturationIteration(self):
		"""If true, SaturationIteration in enabled .

		Returns:
			bool
		"""
		return self._get_attribute('enableSaturationIteration')
	@EnableSaturationIteration.setter
	def EnableSaturationIteration(self, value):
		self._set_attribute('enableSaturationIteration', value)

	@property
	def EnableStopTestOnHighLoss(self):
		"""The test stops in case of a high loss.

		Returns:
			bool
		"""
		return self._get_attribute('enableStopTestOnHighLoss')
	@EnableStopTestOnHighLoss.setter
	def EnableStopTestOnHighLoss(self, value):
		self._set_attribute('enableStopTestOnHighLoss', value)

	@property
	def ExtraIterationOffsets(self):
		"""This enables the test to run an extra iteration.

		Returns:
			str
		"""
		return self._get_attribute('extraIterationOffsets')
	@ExtraIterationOffsets.setter
	def ExtraIterationOffsets(self, value):
		self._set_attribute('extraIterationOffsets', value)

	@property
	def FastConvergenceDuration(self):
		"""sec

		Returns:
			number
		"""
		return self._get_attribute('fastConvergenceDuration')
	@FastConvergenceDuration.setter
	def FastConvergenceDuration(self, value):
		self._set_attribute('fastConvergenceDuration', value)

	@property
	def FastConvergenceThreshold(self):
		"""This enables the test to perform iterations using the fast convergence threshold configured.

		Returns:
			number
		"""
		return self._get_attribute('fastConvergenceThreshold')
	@FastConvergenceThreshold.setter
	def FastConvergenceThreshold(self, value):
		self._set_attribute('fastConvergenceThreshold', value)

	@property
	def FixedLoadUnit(self):
		"""Possible values include:

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('fixedLoadUnit')
	@FixedLoadUnit.setter
	def FixedLoadUnit(self, value):
		self._set_attribute('fixedLoadUnit', value)

	@property
	def FloodedFramesEnabled(self):
		"""If true, it enables the flooded frames statistics

		Returns:
			bool
		"""
		return self._get_attribute('floodedFramesEnabled')
	@FloodedFramesEnabled.setter
	def FloodedFramesEnabled(self, value):
		self._set_attribute('floodedFramesEnabled', value)

	@property
	def ForceRegenerate(self):
		"""Initiates a forced regeneration.

		Returns:
			bool
		"""
		return self._get_attribute('forceRegenerate')
	@ForceRegenerate.setter
	def ForceRegenerate(self, value):
		self._set_attribute('forceRegenerate', value)

	@property
	def FrameLossUnit(self):
		"""The frame loss unit for traffic.

		Returns:
			str
		"""
		return self._get_attribute('frameLossUnit')
	@FrameLossUnit.setter
	def FrameLossUnit(self, value):
		self._set_attribute('frameLossUnit', value)

	@property
	def FrameOrderingTemp(self):
		"""NOT DEFINED

		Returns:
			str(noOrdering|peakLoading|unchanged|val2889Ordering)
		"""
		return self._get_attribute('frameOrderingTemp')
	@FrameOrderingTemp.setter
	def FrameOrderingTemp(self, value):
		self._set_attribute('frameOrderingTemp', value)

	@property
	def FrameSizeMode(self):
		"""This attribute is the frame size mode for the Quad Gaussian. Possible values includes:

		Returns:
			str(custom|increment|random|unchanged)
		"""
		return self._get_attribute('frameSizeMode')
	@FrameSizeMode.setter
	def FrameSizeMode(self, value):
		self._set_attribute('frameSizeMode', value)

	@property
	def FramesPerBurstGap(self):
		"""The number of frames to be sent after each burst.

		Returns:
			number
		"""
		return self._get_attribute('framesPerBurstGap')
	@FramesPerBurstGap.setter
	def FramesPerBurstGap(self, value):
		self._set_attribute('framesPerBurstGap', value)

	@property
	def Framesize(self):
		"""Bytes

		Returns:
			number
		"""
		return self._get_attribute('framesize')
	@Framesize.setter
	def Framesize(self, value):
		self._set_attribute('framesize', value)

	@property
	def FramesizeFixedValue(self):
		"""The fixed value of framesize.

		Returns:
			number
		"""
		return self._get_attribute('framesizeFixedValue')
	@FramesizeFixedValue.setter
	def FramesizeFixedValue(self, value):
		self._set_attribute('framesizeFixedValue', value)

	@property
	def FramesizeImixList(self):
		"""The list of the available lmix frame size.

		Returns:
			str
		"""
		return self._get_attribute('framesizeImixList')
	@FramesizeImixList.setter
	def FramesizeImixList(self, value):
		self._set_attribute('framesizeImixList', value)

	@property
	def FramesizeList(self):
		"""The list of the available frame size.

		Returns:
			list(str)
		"""
		return self._get_attribute('framesizeList')
	@FramesizeList.setter
	def FramesizeList(self, value):
		self._set_attribute('framesizeList', value)

	@property
	def Gap(self):
		"""The gap in transmission of frames.

		Returns:
			number
		"""
		return self._get_attribute('gap')
	@Gap.setter
	def Gap(self, value):
		self._set_attribute('gap', value)

	@property
	def GenerateTrackingOptionAggregationFiles(self):
		"""If true, enables the tracking option in aggregation files.

		Returns:
			bool
		"""
		return self._get_attribute('generateTrackingOptionAggregationFiles')
	@GenerateTrackingOptionAggregationFiles.setter
	def GenerateTrackingOptionAggregationFiles(self, value):
		self._set_attribute('generateTrackingOptionAggregationFiles', value)

	@property
	def ImixAdd(self):
		"""Adds an imix data.

		Returns:
			str
		"""
		return self._get_attribute('imixAdd')
	@ImixAdd.setter
	def ImixAdd(self, value):
		self._set_attribute('imixAdd', value)

	@property
	def ImixData(self):
		"""Displays the imix Data.

		Returns:
			str
		"""
		return self._get_attribute('imixData')
	@ImixData.setter
	def ImixData(self, value):
		self._set_attribute('imixData', value)

	@property
	def ImixDelete(self):
		"""Deletes the imix data.

		Returns:
			str
		"""
		return self._get_attribute('imixDelete')
	@ImixDelete.setter
	def ImixDelete(self, value):
		self._set_attribute('imixDelete', value)

	@property
	def ImixDistribution(self):
		"""Specifies the imix distribution unit.

		Returns:
			str(bwpercentage|weight)
		"""
		return self._get_attribute('imixDistribution')
	@ImixDistribution.setter
	def ImixDistribution(self, value):
		self._set_attribute('imixDistribution', value)

	@property
	def ImixEnabled(self):
		"""If True, Enables the imix value.

		Returns:
			bool
		"""
		return self._get_attribute('imixEnabled')
	@ImixEnabled.setter
	def ImixEnabled(self, value):
		self._set_attribute('imixEnabled', value)

	@property
	def ImixTemplates(self):
		"""Specefies the imix templates.

		Returns:
			str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)
		"""
		return self._get_attribute('imixTemplates')
	@ImixTemplates.setter
	def ImixTemplates(self, value):
		self._set_attribute('imixTemplates', value)

	@property
	def ImixTrafficType(self):
		"""Displays the imix traffic type.

		Returns:
			str
		"""
		return self._get_attribute('imixTrafficType')
	@ImixTrafficType.setter
	def ImixTrafficType(self, value):
		self._set_attribute('imixTrafficType', value)

	@property
	def IncrementLoadUnit(self):
		"""Possible values include:

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('incrementLoadUnit')
	@IncrementLoadUnit.setter
	def IncrementLoadUnit(self, value):
		self._set_attribute('incrementLoadUnit', value)

	@property
	def InitialBinaryLoadRate(self):
		"""The initial binary value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('initialBinaryLoadRate')
	@InitialBinaryLoadRate.setter
	def InitialBinaryLoadRate(self, value):
		self._set_attribute('initialBinaryLoadRate', value)

	@property
	def InitialComboLoadRate(self):
		"""The initial combination value of the load rate .

		Returns:
			number
		"""
		return self._get_attribute('initialComboLoadRate')
	@InitialComboLoadRate.setter
	def InitialComboLoadRate(self, value):
		self._set_attribute('initialComboLoadRate', value)

	@property
	def InitialIncrementLoadRate(self):
		"""The initial incremental value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('initialIncrementLoadRate')
	@InitialIncrementLoadRate.setter
	def InitialIncrementLoadRate(self, value):
		self._set_attribute('initialIncrementLoadRate', value)

	@property
	def InitialStepLoadRate(self):
		"""The initial step value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('initialStepLoadRate')
	@InitialStepLoadRate.setter
	def InitialStepLoadRate(self, value):
		self._set_attribute('initialStepLoadRate', value)

	@property
	def IpRatioMode(self):
		"""Sets the ip ratio mode

		Returns:
			str(custom|fixed|increment|random)
		"""
		return self._get_attribute('ipRatioMode')
	@IpRatioMode.setter
	def IpRatioMode(self, value):
		self._set_attribute('ipRatioMode', value)

	@property
	def Ipv4RatioList(self):
		"""Sets the ipv4 ratio list

		Returns:
			str
		"""
		return self._get_attribute('ipv4RatioList')
	@Ipv4RatioList.setter
	def Ipv4RatioList(self, value):
		self._set_attribute('ipv4RatioList', value)

	@property
	def Ipv4rate(self):
		"""The rate at which IPv4 traffic is sent.

		Returns:
			number
		"""
		return self._get_attribute('ipv4rate')
	@Ipv4rate.setter
	def Ipv4rate(self, value):
		self._set_attribute('ipv4rate', value)

	@property
	def Ipv6RatioList(self):
		"""Sets the ipv6 ratio list

		Returns:
			str
		"""
		return self._get_attribute('ipv6RatioList')
	@Ipv6RatioList.setter
	def Ipv6RatioList(self, value):
		self._set_attribute('ipv6RatioList', value)

	@property
	def Ipv6rate(self):
		"""The rate at which IPv6 traffic is sent.

		Returns:
			number
		"""
		return self._get_attribute('ipv6rate')
	@Ipv6rate.setter
	def Ipv6rate(self, value):
		self._set_attribute('ipv6rate', value)

	@property
	def LatencyBins(self):
		"""Sets the latency bins statistics

		Returns:
			str
		"""
		return self._get_attribute('latencyBins')
	@LatencyBins.setter
	def LatencyBins(self, value):
		self._set_attribute('latencyBins', value)

	@property
	def LatencyBinsEnabled(self):
		"""Enables the latency bins statistics

		Returns:
			bool
		"""
		return self._get_attribute('latencyBinsEnabled')
	@LatencyBinsEnabled.setter
	def LatencyBinsEnabled(self, value):
		self._set_attribute('latencyBinsEnabled', value)

	@property
	def LatencyType(self):
		"""The type of latency. Possible values include:

		Returns:
			str(cutThrough|forwardingDelay|mef|storeForward)
		"""
		return self._get_attribute('latencyType')
	@LatencyType.setter
	def LatencyType(self, value):
		self._set_attribute('latencyType', value)

	@property
	def LoadRateList(self):
		"""The list of Load Rate.

		Returns:
			str
		"""
		return self._get_attribute('loadRateList')
	@LoadRateList.setter
	def LoadRateList(self, value):
		self._set_attribute('loadRateList', value)

	@property
	def LoadRateValue(self):
		"""The value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('loadRateValue')
	@LoadRateValue.setter
	def LoadRateValue(self, value):
		self._set_attribute('loadRateValue', value)

	@property
	def LoadType(self):
		"""Possible values include:

		Returns:
			str(binary|combo|custom|quickSearch|random|step|unchanged)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def MapType(self):
		"""The mapping type.

		Returns:
			str
		"""
		return self._get_attribute('mapType')
	@MapType.setter
	def MapType(self, value):
		self._set_attribute('mapType', value)

	@property
	def MaxBinaryLoadRate(self):
		"""The upper bound of the iteration rates for each frame size during a binary search.

		Returns:
			number
		"""
		return self._get_attribute('maxBinaryLoadRate')
	@MaxBinaryLoadRate.setter
	def MaxBinaryLoadRate(self, value):
		self._set_attribute('maxBinaryLoadRate', value)

	@property
	def MaxComboLoadRate(self):
		"""The maximum value of the load rate Combo Load Type.

		Returns:
			number
		"""
		return self._get_attribute('maxComboLoadRate')
	@MaxComboLoadRate.setter
	def MaxComboLoadRate(self, value):
		self._set_attribute('maxComboLoadRate', value)

	@property
	def MaxIncrementFrameSize(self):
		"""It signifies the maximum increment frame size.

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementFrameSize')
	@MaxIncrementFrameSize.setter
	def MaxIncrementFrameSize(self, value):
		self._set_attribute('maxIncrementFrameSize', value)

	@property
	def MaxIncrementIpv4Ratio(self):
		"""Sets the maximum increment value for the ipv4 ratio

		Returns:
			str
		"""
		return self._get_attribute('maxIncrementIpv4Ratio')
	@MaxIncrementIpv4Ratio.setter
	def MaxIncrementIpv4Ratio(self, value):
		self._set_attribute('maxIncrementIpv4Ratio', value)

	@property
	def MaxIncrementIpv6Ratio(self):
		"""Sets the maximum increment value for the ipv6 ratio

		Returns:
			str
		"""
		return self._get_attribute('maxIncrementIpv6Ratio')
	@MaxIncrementIpv6Ratio.setter
	def MaxIncrementIpv6Ratio(self, value):
		self._set_attribute('maxIncrementIpv6Ratio', value)

	@property
	def MaxIncrementLoadRate(self):
		"""It signifies the maximum increment load rate value.

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementLoadRate')
	@MaxIncrementLoadRate.setter
	def MaxIncrementLoadRate(self, value):
		self._set_attribute('maxIncrementLoadRate', value)

	@property
	def MaxQuickSearchLoadRate(self):
		"""Sets the maximum QuickSearch load rate

		Returns:
			number
		"""
		return self._get_attribute('maxQuickSearchLoadRate')
	@MaxQuickSearchLoadRate.setter
	def MaxQuickSearchLoadRate(self, value):
		self._set_attribute('maxQuickSearchLoadRate', value)

	@property
	def MaxRandomFrameSize(self):
		"""It signifies the maximum random frame size value.

		Returns:
			number
		"""
		return self._get_attribute('maxRandomFrameSize')
	@MaxRandomFrameSize.setter
	def MaxRandomFrameSize(self, value):
		self._set_attribute('maxRandomFrameSize', value)

	@property
	def MaxRandomIpv4Ratio(self):
		"""Sets the maximum radom value for the ipv4 ratio

		Returns:
			str
		"""
		return self._get_attribute('maxRandomIpv4Ratio')
	@MaxRandomIpv4Ratio.setter
	def MaxRandomIpv4Ratio(self, value):
		self._set_attribute('maxRandomIpv4Ratio', value)

	@property
	def MaxRandomIpv6Ratio(self):
		"""Sets the maximum random value for the ipv6 ratio

		Returns:
			str
		"""
		return self._get_attribute('maxRandomIpv6Ratio')
	@MaxRandomIpv6Ratio.setter
	def MaxRandomIpv6Ratio(self, value):
		self._set_attribute('maxRandomIpv6Ratio', value)

	@property
	def MaxRandomLoadRate(self):
		"""It signifies the maximum random load rate value.

		Returns:
			number
		"""
		return self._get_attribute('maxRandomLoadRate')
	@MaxRandomLoadRate.setter
	def MaxRandomLoadRate(self, value):
		self._set_attribute('maxRandomLoadRate', value)

	@property
	def MaxStepLoadRate(self):
		"""It signifies the maximum step value for load rate.

		Returns:
			number
		"""
		return self._get_attribute('maxStepLoadRate')
	@MaxStepLoadRate.setter
	def MaxStepLoadRate(self, value):
		self._set_attribute('maxStepLoadRate', value)

	@property
	def MinBinaryLoadRate(self):
		"""Specifies the minimum rate of the binary algorithm.

		Returns:
			number
		"""
		return self._get_attribute('minBinaryLoadRate')
	@MinBinaryLoadRate.setter
	def MinBinaryLoadRate(self, value):
		self._set_attribute('minBinaryLoadRate', value)

	@property
	def MinComboLoadRate(self):
		"""The minimum combination load rate.

		Returns:
			number
		"""
		return self._get_attribute('minComboLoadRate')
	@MinComboLoadRate.setter
	def MinComboLoadRate(self, value):
		self._set_attribute('minComboLoadRate', value)

	@property
	def MinFpsRate(self):
		"""The rate at which minimum frames are sent per second.

		Returns:
			number
		"""
		return self._get_attribute('minFpsRate')
	@MinFpsRate.setter
	def MinFpsRate(self, value):
		self._set_attribute('minFpsRate', value)

	@property
	def MinIncrementFrameSize(self):
		"""It signifies the minimum increment frame size.

		Returns:
			number
		"""
		return self._get_attribute('minIncrementFrameSize')
	@MinIncrementFrameSize.setter
	def MinIncrementFrameSize(self, value):
		self._set_attribute('minIncrementFrameSize', value)

	@property
	def MinIncrementIpv4Ratio(self):
		"""Sets the minimum increment value for the ipv4 ratio

		Returns:
			str
		"""
		return self._get_attribute('minIncrementIpv4Ratio')
	@MinIncrementIpv4Ratio.setter
	def MinIncrementIpv4Ratio(self, value):
		self._set_attribute('minIncrementIpv4Ratio', value)

	@property
	def MinIncrementIpv6Ratio(self):
		"""Sets the minimum increment value for the ipv6 ratio

		Returns:
			str
		"""
		return self._get_attribute('minIncrementIpv6Ratio')
	@MinIncrementIpv6Ratio.setter
	def MinIncrementIpv6Ratio(self, value):
		self._set_attribute('minIncrementIpv6Ratio', value)

	@property
	def MinKbpsRate(self):
		"""The rate at which minimum frames are sent per kbps.

		Returns:
			number
		"""
		return self._get_attribute('minKbpsRate')
	@MinKbpsRate.setter
	def MinKbpsRate(self, value):
		self._set_attribute('minKbpsRate', value)

	@property
	def MinQuickSearchLoadRate(self):
		"""Sets the minum Quick Search load rate

		Returns:
			number
		"""
		return self._get_attribute('minQuickSearchLoadRate')
	@MinQuickSearchLoadRate.setter
	def MinQuickSearchLoadRate(self, value):
		self._set_attribute('minQuickSearchLoadRate', value)

	@property
	def MinRandomFrameSize(self):
		"""The minimum random frame size to be sent.

		Returns:
			number
		"""
		return self._get_attribute('minRandomFrameSize')
	@MinRandomFrameSize.setter
	def MinRandomFrameSize(self, value):
		self._set_attribute('minRandomFrameSize', value)

	@property
	def MinRandomIpv4Ratio(self):
		"""Sets the minimum random value for the ipv4 ratio

		Returns:
			str
		"""
		return self._get_attribute('minRandomIpv4Ratio')
	@MinRandomIpv4Ratio.setter
	def MinRandomIpv4Ratio(self, value):
		self._set_attribute('minRandomIpv4Ratio', value)

	@property
	def MinRandomIpv6Ratio(self):
		"""Sets the minimum random value for the ipv6 ratio

		Returns:
			str
		"""
		return self._get_attribute('minRandomIpv6Ratio')
	@MinRandomIpv6Ratio.setter
	def MinRandomIpv6Ratio(self, value):
		self._set_attribute('minRandomIpv6Ratio', value)

	@property
	def MinRandomLoadRate(self):
		"""The minimum random value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('minRandomLoadRate')
	@MinRandomLoadRate.setter
	def MinRandomLoadRate(self, value):
		self._set_attribute('minRandomLoadRate', value)

	@property
	def Numtrials(self):
		"""The integer value that states the number of trials permitted.

		Returns:
			number
		"""
		return self._get_attribute('numtrials')
	@Numtrials.setter
	def Numtrials(self, value):
		self._set_attribute('numtrials', value)

	@property
	def PeakLoadingReplicationCount(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('peakLoadingReplicationCount')
	@PeakLoadingReplicationCount.setter
	def PeakLoadingReplicationCount(self, value):
		self._set_attribute('peakLoadingReplicationCount', value)

	@property
	def Peak_customLoadUnit(self):
		"""NOT DEFINED

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('peak_customLoadUnit')
	@Peak_customLoadUnit.setter
	def Peak_customLoadUnit(self, value):
		self._set_attribute('peak_customLoadUnit', value)

	@property
	def Peak_initialStepLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('peak_initialStepLoadRate')
	@Peak_initialStepLoadRate.setter
	def Peak_initialStepLoadRate(self, value):
		self._set_attribute('peak_initialStepLoadRate', value)

	@property
	def Peak_loadRateList(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('peak_loadRateList')
	@Peak_loadRateList.setter
	def Peak_loadRateList(self, value):
		self._set_attribute('peak_loadRateList', value)

	@property
	def Peak_maxStepLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('peak_maxStepLoadRate')
	@Peak_maxStepLoadRate.setter
	def Peak_maxStepLoadRate(self, value):
		self._set_attribute('peak_maxStepLoadRate', value)

	@property
	def Peak_rate_loadType(self):
		"""NOT DEFINED

		Returns:
			str(custom|step)
		"""
		return self._get_attribute('peak_rate_loadType')
	@Peak_rate_loadType.setter
	def Peak_rate_loadType(self, value):
		self._set_attribute('peak_rate_loadType', value)

	@property
	def Peak_stepLoadUnit(self):
		"""

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('peak_stepLoadUnit')
	@Peak_stepLoadUnit.setter
	def Peak_stepLoadUnit(self, value):
		self._set_attribute('peak_stepLoadUnit', value)

	@property
	def Peak_stepStepLoadRate(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('peak_stepStepLoadRate')
	@Peak_stepStepLoadRate.setter
	def Peak_stepStepLoadRate(self, value):
		self._set_attribute('peak_stepStepLoadRate', value)

	@property
	def PerTrafficResults(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('perTrafficResults')
	@PerTrafficResults.setter
	def PerTrafficResults(self, value):
		self._set_attribute('perTrafficResults', value)

	@property
	def PercentMaxRate(self):
		"""The maximum rate percentage.

		Returns:
			number
		"""
		return self._get_attribute('percentMaxRate')
	@PercentMaxRate.setter
	def PercentMaxRate(self, value):
		self._set_attribute('percentMaxRate', value)

	@property
	def PortDelayEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('portDelayEnabled')
	@PortDelayEnabled.setter
	def PortDelayEnabled(self, value):
		self._set_attribute('portDelayEnabled', value)

	@property
	def PortDelayUnit(self):
		"""Sets the port delay unit in which it will be measured

		Returns:
			str(bytes|nanoseconds)
		"""
		return self._get_attribute('portDelayUnit')
	@PortDelayUnit.setter
	def PortDelayUnit(self, value):
		self._set_attribute('portDelayUnit', value)

	@property
	def PortDelayValue(self):
		"""Sets the port delay value

		Returns:
			number
		"""
		return self._get_attribute('portDelayValue')
	@PortDelayValue.setter
	def PortDelayValue(self, value):
		self._set_attribute('portDelayValue', value)

	@property
	def ProtocolItem(self):
		"""Protocol Items

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])
		"""
		return self._get_attribute('protocolItem')
	@ProtocolItem.setter
	def ProtocolItem(self, value):
		self._set_attribute('protocolItem', value)

	@property
	def QuickBackoffIteration(self):
		"""Sets the quicksearch backoff iteration

		Returns:
			number
		"""
		return self._get_attribute('quickBackoffIteration')
	@QuickBackoffIteration.setter
	def QuickBackoffIteration(self, value):
		self._set_attribute('quickBackoffIteration', value)

	@property
	def QuickEnableBackoffIteration(self):
		"""Enables the quick search backoff iteration

		Returns:
			bool
		"""
		return self._get_attribute('quickEnableBackoffIteration')
	@QuickEnableBackoffIteration.setter
	def QuickEnableBackoffIteration(self, value):
		self._set_attribute('quickEnableBackoffIteration', value)

	@property
	def QuickEnableSaturationIteration(self):
		"""Enables the Quick Search saturation iteration

		Returns:
			bool
		"""
		return self._get_attribute('quickEnableSaturationIteration')
	@QuickEnableSaturationIteration.setter
	def QuickEnableSaturationIteration(self, value):
		self._set_attribute('quickEnableSaturationIteration', value)

	@property
	def QuickSaturationIteration(self):
		"""Sets the quick search saturation iteration

		Returns:
			number
		"""
		return self._get_attribute('quickSaturationIteration')
	@QuickSaturationIteration.setter
	def QuickSaturationIteration(self, value):
		self._set_attribute('quickSaturationIteration', value)

	@property
	def QuickSearchFrameLossUnit(self):
		"""Sets the quick search frame loss unit

		Returns:
			str(%)
		"""
		return self._get_attribute('quickSearchFrameLossUnit')
	@QuickSearchFrameLossUnit.setter
	def QuickSearchFrameLossUnit(self, value):
		self._set_attribute('quickSearchFrameLossUnit', value)

	@property
	def QuickSearchLoadUnit(self):
		"""Sets the quick search load unit

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('quickSearchLoadUnit')
	@QuickSearchLoadUnit.setter
	def QuickSearchLoadUnit(self, value):
		self._set_attribute('quickSearchLoadUnit', value)

	@property
	def QuickSearchResolution(self):
		"""Sets the quick search resolution

		Returns:
			number
		"""
		return self._get_attribute('quickSearchResolution')
	@QuickSearchResolution.setter
	def QuickSearchResolution(self, value):
		self._set_attribute('quickSearchResolution', value)

	@property
	def QuickSearchSearchType(self):
		"""Sets the quick search type

		Returns:
			str(linear|perFlow|perPort|perTrafficItem)
		"""
		return self._get_attribute('quickSearchSearchType')
	@QuickSearchSearchType.setter
	def QuickSearchSearchType(self, value):
		self._set_attribute('quickSearchSearchType', value)

	@property
	def QuickSearchTiLoss(self):
		"""Use loss across Rx Ports

		Returns:
			bool
		"""
		return self._get_attribute('quickSearchTiLoss')
	@QuickSearchTiLoss.setter
	def QuickSearchTiLoss(self, value):
		self._set_attribute('quickSearchTiLoss', value)

	@property
	def QuickSearchTolerance(self):
		"""Sets the quick search tolerance

		Returns:
			number
		"""
		return self._get_attribute('quickSearchTolerance')
	@QuickSearchTolerance.setter
	def QuickSearchTolerance(self, value):
		self._set_attribute('quickSearchTolerance', value)

	@property
	def RandomLoadUnit(self):
		"""The random values of the load unit. Possible values include:

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('randomLoadUnit')
	@RandomLoadUnit.setter
	def RandomLoadUnit(self, value):
		self._set_attribute('randomLoadUnit', value)

	@property
	def RandomTiLoss(self):
		"""Use loss across Rx Ports

		Returns:
			bool
		"""
		return self._get_attribute('randomTiLoss')
	@RandomTiLoss.setter
	def RandomTiLoss(self, value):
		self._set_attribute('randomTiLoss', value)

	@property
	def RateSelect(self):
		"""Possible values include:

		Returns:
			str(fpsRate|kbpsRate|percentMaxRate)
		"""
		return self._get_attribute('rateSelect')
	@RateSelect.setter
	def RateSelect(self, value):
		self._set_attribute('rateSelect', value)

	@property
	def ReportSequenceError(self):
		"""Reports sequence errors in the test result.

		Returns:
			bool
		"""
		return self._get_attribute('reportSequenceError')
	@ReportSequenceError.setter
	def ReportSequenceError(self, value):
		self._set_attribute('reportSequenceError', value)

	@property
	def ReportTputRateUnit(self):
		"""The reported throughput rate unit values. Possible values include:

		Returns:
			str(gbps|gBps|kbps|kBps|mbps|mBps)
		"""
		return self._get_attribute('reportTputRateUnit')
	@ReportTputRateUnit.setter
	def ReportTputRateUnit(self, value):
		self._set_attribute('reportTputRateUnit', value)

	@property
	def Resolution(self):
		"""Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops .

		Returns:
			number
		"""
		return self._get_attribute('resolution')
	@Resolution.setter
	def Resolution(self, value):
		self._set_attribute('resolution', value)

	@property
	def Rfc2544ImixDataQoS(self):
		"""If true, it uses the same frame data qos

		Returns:
			bool
		"""
		return self._get_attribute('rfc2544ImixDataQoS')
	@Rfc2544ImixDataQoS.setter
	def Rfc2544ImixDataQoS(self, value):
		self._set_attribute('rfc2544ImixDataQoS', value)

	@property
	def Rfc2889ordering(self):
		"""If true, indicates frame ordering by Rfc2889.

		Returns:
			str(noOrdering|peakLoading|unchanged|val2889Ordering)
		"""
		return self._get_attribute('rfc2889ordering')
	@Rfc2889ordering.setter
	def Rfc2889ordering(self, value):
		self._set_attribute('rfc2889ordering', value)

	@property
	def SaturationIteration(self):
		"""This enables the test to run an extra iteration for calculating the Saturation latency.

		Returns:
			number
		"""
		return self._get_attribute('saturationIteration')
	@SaturationIteration.setter
	def SaturationIteration(self, value):
		self._set_attribute('saturationIteration', value)

	@property
	def SearchBase(self):
		"""NOT DEFINED

		Returns:
			str(rate|replicationCount)
		"""
		return self._get_attribute('searchBase')
	@SearchBase.setter
	def SearchBase(self, value):
		self._set_attribute('searchBase', value)

	@property
	def SendFullyMeshed(self):
		"""Indicates the source group mapping type used for sending data.

		Returns:
			bool
		"""
		return self._get_attribute('sendFullyMeshed')
	@SendFullyMeshed.setter
	def SendFullyMeshed(self, value):
		self._set_attribute('sendFullyMeshed', value)

	@property
	def ShowDetailedBinaryResults(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('showDetailedBinaryResults')
	@ShowDetailedBinaryResults.setter
	def ShowDetailedBinaryResults(self, value):
		self._set_attribute('showDetailedBinaryResults', value)

	@property
	def StaggeredStart(self):
		"""Starts test with a stagger.

		Returns:
			bool
		"""
		return self._get_attribute('staggeredStart')
	@StaggeredStart.setter
	def StaggeredStart(self, value):
		self._set_attribute('staggeredStart', value)

	@property
	def StepComboLoadRate(self):
		"""The step value of combination load rate.

		Returns:
			number
		"""
		return self._get_attribute('stepComboLoadRate')
	@StepComboLoadRate.setter
	def StepComboLoadRate(self, value):
		self._set_attribute('stepComboLoadRate', value)

	@property
	def StepFrameLossUnit(self):
		"""The frame loss unit.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('stepFrameLossUnit')
	@StepFrameLossUnit.setter
	def StepFrameLossUnit(self, value):
		self._set_attribute('stepFrameLossUnit', value)

	@property
	def StepIncrementFrameSize(self):
		"""The traffic step increment frame size.

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementFrameSize')
	@StepIncrementFrameSize.setter
	def StepIncrementFrameSize(self, value):
		self._set_attribute('stepIncrementFrameSize', value)

	@property
	def StepIncrementIpv4Ratio(self):
		"""The step in which the ipv4 ratio loop is incremented

		Returns:
			str
		"""
		return self._get_attribute('stepIncrementIpv4Ratio')
	@StepIncrementIpv4Ratio.setter
	def StepIncrementIpv4Ratio(self, value):
		self._set_attribute('stepIncrementIpv4Ratio', value)

	@property
	def StepIncrementIpv6Ratio(self):
		"""The step in which the ipv6 ratio loop is incremented

		Returns:
			str
		"""
		return self._get_attribute('stepIncrementIpv6Ratio')
	@StepIncrementIpv6Ratio.setter
	def StepIncrementIpv6Ratio(self, value):
		self._set_attribute('stepIncrementIpv6Ratio', value)

	@property
	def StepIncrementLoadRate(self):
		"""The incremental step value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementLoadRate')
	@StepIncrementLoadRate.setter
	def StepIncrementLoadRate(self, value):
		self._set_attribute('stepIncrementLoadRate', value)

	@property
	def StepLoadUnit(self):
		"""Specifies the step rate of the load unit. Possible values include:

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('stepLoadUnit')
	@StepLoadUnit.setter
	def StepLoadUnit(self, value):
		self._set_attribute('stepLoadUnit', value)

	@property
	def StepStepLoadRate(self):
		"""The incremental step value of load rate.

		Returns:
			number
		"""
		return self._get_attribute('stepStepLoadRate')
	@StepStepLoadRate.setter
	def StepStepLoadRate(self, value):
		self._set_attribute('stepStepLoadRate', value)

	@property
	def StepTiLoss(self):
		"""Use loss across Rx Ports

		Returns:
			bool
		"""
		return self._get_attribute('stepTiLoss')
	@StepTiLoss.setter
	def StepTiLoss(self, value):
		self._set_attribute('stepTiLoss', value)

	@property
	def StepTolerance(self):
		"""The step value of the tolerance level.

		Returns:
			number
		"""
		return self._get_attribute('stepTolerance')
	@StepTolerance.setter
	def StepTolerance(self, value):
		self._set_attribute('stepTolerance', value)

	@property
	def Step_binary_delay_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_binary_delay_enableAccLoss')
	@Step_binary_delay_enableAccLoss.setter
	def Step_binary_delay_enableAccLoss(self, value):
		self._set_attribute('step_binary_delay_enableAccLoss', value)

	@property
	def Step_binary_delay_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('step_binary_delay_modeAccLoss')
	@Step_binary_delay_modeAccLoss.setter
	def Step_binary_delay_modeAccLoss(self, value):
		self._set_attribute('step_binary_delay_modeAccLoss', value)

	@property
	def Step_binary_delay_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('step_binary_delay_scaleAccLoss')
	@Step_binary_delay_scaleAccLoss.setter
	def Step_binary_delay_scaleAccLoss(self, value):
		self._set_attribute('step_binary_delay_scaleAccLoss', value)

	@property
	def Step_binary_delay_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_binary_delay_thresholdAccLoss')
	@Step_binary_delay_thresholdAccLoss.setter
	def Step_binary_delay_thresholdAccLoss(self, value):
		self._set_attribute('step_binary_delay_thresholdAccLoss', value)

	@property
	def Step_binary_flooded_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_binary_flooded_enableAccLoss')
	@Step_binary_flooded_enableAccLoss.setter
	def Step_binary_flooded_enableAccLoss(self, value):
		self._set_attribute('step_binary_flooded_enableAccLoss', value)

	@property
	def Step_binary_flooded_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_binary_flooded_thresholdAccLoss')
	@Step_binary_flooded_thresholdAccLoss.setter
	def Step_binary_flooded_thresholdAccLoss(self, value):
		self._set_attribute('step_binary_flooded_thresholdAccLoss', value)

	@property
	def Step_binary_integrity_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_binary_integrity_enableAccLoss')
	@Step_binary_integrity_enableAccLoss.setter
	def Step_binary_integrity_enableAccLoss(self, value):
		self._set_attribute('step_binary_integrity_enableAccLoss', value)

	@property
	def Step_binary_integrity_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_binary_integrity_thresholdAccLoss')
	@Step_binary_integrity_thresholdAccLoss.setter
	def Step_binary_integrity_thresholdAccLoss(self, value):
		self._set_attribute('step_binary_integrity_thresholdAccLoss', value)

	@property
	def Step_binary_latency_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_binary_latency_enableAccLoss')
	@Step_binary_latency_enableAccLoss.setter
	def Step_binary_latency_enableAccLoss(self, value):
		self._set_attribute('step_binary_latency_enableAccLoss', value)

	@property
	def Step_binary_latency_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('step_binary_latency_modeAccLoss')
	@Step_binary_latency_modeAccLoss.setter
	def Step_binary_latency_modeAccLoss(self, value):
		self._set_attribute('step_binary_latency_modeAccLoss', value)

	@property
	def Step_binary_latency_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('step_binary_latency_scaleAccLoss')
	@Step_binary_latency_scaleAccLoss.setter
	def Step_binary_latency_scaleAccLoss(self, value):
		self._set_attribute('step_binary_latency_scaleAccLoss', value)

	@property
	def Step_binary_latency_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_binary_latency_thresholdAccLoss')
	@Step_binary_latency_thresholdAccLoss.setter
	def Step_binary_latency_thresholdAccLoss(self, value):
		self._set_attribute('step_binary_latency_thresholdAccLoss', value)

	@property
	def Step_binary_peak_Backoff(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_binary_peak_Backoff')
	@Step_binary_peak_Backoff.setter
	def Step_binary_peak_Backoff(self, value):
		self._set_attribute('step_binary_peak_Backoff', value)

	@property
	def Step_binary_peak_FrameLossUnit(self):
		"""NOT DEFINED

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('step_binary_peak_FrameLossUnit')
	@Step_binary_peak_FrameLossUnit.setter
	def Step_binary_peak_FrameLossUnit(self, value):
		self._set_attribute('step_binary_peak_FrameLossUnit', value)

	@property
	def Step_binary_peak_Resolution(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_binary_peak_Resolution')
	@Step_binary_peak_Resolution.setter
	def Step_binary_peak_Resolution(self, value):
		self._set_attribute('step_binary_peak_Resolution', value)

	@property
	def Step_binary_peak_Tolerance(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_binary_peak_Tolerance')
	@Step_binary_peak_Tolerance.setter
	def Step_binary_peak_Tolerance(self, value):
		self._set_attribute('step_binary_peak_Tolerance', value)

	@property
	def Step_binary_peak_initialValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_binary_peak_initialValue')
	@Step_binary_peak_initialValue.setter
	def Step_binary_peak_initialValue(self, value):
		self._set_attribute('step_binary_peak_initialValue', value)

	@property
	def Step_binary_peak_maxValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_binary_peak_maxValue')
	@Step_binary_peak_maxValue.setter
	def Step_binary_peak_maxValue(self, value):
		self._set_attribute('step_binary_peak_maxValue', value)

	@property
	def Step_binary_peak_minValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_binary_peak_minValue')
	@Step_binary_peak_minValue.setter
	def Step_binary_peak_minValue(self, value):
		self._set_attribute('step_binary_peak_minValue', value)

	@property
	def Step_binary_seq_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_binary_seq_enableAccLoss')
	@Step_binary_seq_enableAccLoss.setter
	def Step_binary_seq_enableAccLoss(self, value):
		self._set_attribute('step_binary_seq_enableAccLoss', value)

	@property
	def Step_binary_seq_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('step_binary_seq_modeAccLoss')
	@Step_binary_seq_modeAccLoss.setter
	def Step_binary_seq_modeAccLoss(self, value):
		self._set_attribute('step_binary_seq_modeAccLoss', value)

	@property
	def Step_binary_seq_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_binary_seq_thresholdAccLoss')
	@Step_binary_seq_thresholdAccLoss.setter
	def Step_binary_seq_thresholdAccLoss(self, value):
		self._set_attribute('step_binary_seq_thresholdAccLoss', value)

	@property
	def Step_delay_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_delay_enableAccLoss')
	@Step_delay_enableAccLoss.setter
	def Step_delay_enableAccLoss(self, value):
		self._set_attribute('step_delay_enableAccLoss', value)

	@property
	def Step_delay_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('step_delay_modeAccLoss')
	@Step_delay_modeAccLoss.setter
	def Step_delay_modeAccLoss(self, value):
		self._set_attribute('step_delay_modeAccLoss', value)

	@property
	def Step_delay_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('step_delay_scaleAccLoss')
	@Step_delay_scaleAccLoss.setter
	def Step_delay_scaleAccLoss(self, value):
		self._set_attribute('step_delay_scaleAccLoss', value)

	@property
	def Step_delay_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_delay_thresholdAccLoss')
	@Step_delay_thresholdAccLoss.setter
	def Step_delay_thresholdAccLoss(self, value):
		self._set_attribute('step_delay_thresholdAccLoss', value)

	@property
	def Step_flooded_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_flooded_enableAccLoss')
	@Step_flooded_enableAccLoss.setter
	def Step_flooded_enableAccLoss(self, value):
		self._set_attribute('step_flooded_enableAccLoss', value)

	@property
	def Step_flooded_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_flooded_thresholdAccLoss')
	@Step_flooded_thresholdAccLoss.setter
	def Step_flooded_thresholdAccLoss(self, value):
		self._set_attribute('step_flooded_thresholdAccLoss', value)

	@property
	def Step_integrity_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_integrity_enableAccLoss')
	@Step_integrity_enableAccLoss.setter
	def Step_integrity_enableAccLoss(self, value):
		self._set_attribute('step_integrity_enableAccLoss', value)

	@property
	def Step_integrity_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_integrity_thresholdAccLoss')
	@Step_integrity_thresholdAccLoss.setter
	def Step_integrity_thresholdAccLoss(self, value):
		self._set_attribute('step_integrity_thresholdAccLoss', value)

	@property
	def Step_latency_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_latency_enableAccLoss')
	@Step_latency_enableAccLoss.setter
	def Step_latency_enableAccLoss(self, value):
		self._set_attribute('step_latency_enableAccLoss', value)

	@property
	def Step_latency_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('step_latency_modeAccLoss')
	@Step_latency_modeAccLoss.setter
	def Step_latency_modeAccLoss(self, value):
		self._set_attribute('step_latency_modeAccLoss', value)

	@property
	def Step_latency_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('step_latency_scaleAccLoss')
	@Step_latency_scaleAccLoss.setter
	def Step_latency_scaleAccLoss(self, value):
		self._set_attribute('step_latency_scaleAccLoss', value)

	@property
	def Step_latency_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_latency_thresholdAccLoss')
	@Step_latency_thresholdAccLoss.setter
	def Step_latency_thresholdAccLoss(self, value):
		self._set_attribute('step_latency_thresholdAccLoss', value)

	@property
	def Step_peak_loadType(self):
		"""NOT DEFINED

		Returns:
			str(binary|custom|step)
		"""
		return self._get_attribute('step_peak_loadType')
	@Step_peak_loadType.setter
	def Step_peak_loadType(self, value):
		self._set_attribute('step_peak_loadType', value)

	@property
	def Step_seq_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_seq_enableAccLoss')
	@Step_seq_enableAccLoss.setter
	def Step_seq_enableAccLoss(self, value):
		self._set_attribute('step_seq_enableAccLoss', value)

	@property
	def Step_seq_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('step_seq_modeAccLoss')
	@Step_seq_modeAccLoss.setter
	def Step_seq_modeAccLoss(self, value):
		self._set_attribute('step_seq_modeAccLoss', value)

	@property
	def Step_seq_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_seq_thresholdAccLoss')
	@Step_seq_thresholdAccLoss.setter
	def Step_seq_thresholdAccLoss(self, value):
		self._set_attribute('step_seq_thresholdAccLoss', value)

	@property
	def Step_step_delay_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_step_delay_enableAccLoss')
	@Step_step_delay_enableAccLoss.setter
	def Step_step_delay_enableAccLoss(self, value):
		self._set_attribute('step_step_delay_enableAccLoss', value)

	@property
	def Step_step_delay_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('step_step_delay_modeAccLoss')
	@Step_step_delay_modeAccLoss.setter
	def Step_step_delay_modeAccLoss(self, value):
		self._set_attribute('step_step_delay_modeAccLoss', value)

	@property
	def Step_step_delay_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('step_step_delay_scaleAccLoss')
	@Step_step_delay_scaleAccLoss.setter
	def Step_step_delay_scaleAccLoss(self, value):
		self._set_attribute('step_step_delay_scaleAccLoss', value)

	@property
	def Step_step_delay_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_step_delay_thresholdAccLoss')
	@Step_step_delay_thresholdAccLoss.setter
	def Step_step_delay_thresholdAccLoss(self, value):
		self._set_attribute('step_step_delay_thresholdAccLoss', value)

	@property
	def Step_step_flooded_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_step_flooded_enableAccLoss')
	@Step_step_flooded_enableAccLoss.setter
	def Step_step_flooded_enableAccLoss(self, value):
		self._set_attribute('step_step_flooded_enableAccLoss', value)

	@property
	def Step_step_flooded_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_step_flooded_thresholdAccLoss')
	@Step_step_flooded_thresholdAccLoss.setter
	def Step_step_flooded_thresholdAccLoss(self, value):
		self._set_attribute('step_step_flooded_thresholdAccLoss', value)

	@property
	def Step_step_integrity_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_step_integrity_enableAccLoss')
	@Step_step_integrity_enableAccLoss.setter
	def Step_step_integrity_enableAccLoss(self, value):
		self._set_attribute('step_step_integrity_enableAccLoss', value)

	@property
	def Step_step_integrity_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_step_integrity_thresholdAccLoss')
	@Step_step_integrity_thresholdAccLoss.setter
	def Step_step_integrity_thresholdAccLoss(self, value):
		self._set_attribute('step_step_integrity_thresholdAccLoss', value)

	@property
	def Step_step_latency_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_step_latency_enableAccLoss')
	@Step_step_latency_enableAccLoss.setter
	def Step_step_latency_enableAccLoss(self, value):
		self._set_attribute('step_step_latency_enableAccLoss', value)

	@property
	def Step_step_latency_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('step_step_latency_modeAccLoss')
	@Step_step_latency_modeAccLoss.setter
	def Step_step_latency_modeAccLoss(self, value):
		self._set_attribute('step_step_latency_modeAccLoss', value)

	@property
	def Step_step_latency_scaleAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('step_step_latency_scaleAccLoss')
	@Step_step_latency_scaleAccLoss.setter
	def Step_step_latency_scaleAccLoss(self, value):
		self._set_attribute('step_step_latency_scaleAccLoss', value)

	@property
	def Step_step_latency_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_step_latency_thresholdAccLoss')
	@Step_step_latency_thresholdAccLoss.setter
	def Step_step_latency_thresholdAccLoss(self, value):
		self._set_attribute('step_step_latency_thresholdAccLoss', value)

	@property
	def Step_step_peak_FrameLossUnit(self):
		"""NOT DEFINED

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('step_step_peak_FrameLossUnit')
	@Step_step_peak_FrameLossUnit.setter
	def Step_step_peak_FrameLossUnit(self, value):
		self._set_attribute('step_step_peak_FrameLossUnit', value)

	@property
	def Step_step_peak_initialValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_step_peak_initialValue')
	@Step_step_peak_initialValue.setter
	def Step_step_peak_initialValue(self, value):
		self._set_attribute('step_step_peak_initialValue', value)

	@property
	def Step_step_peak_maxValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_step_peak_maxValue')
	@Step_step_peak_maxValue.setter
	def Step_step_peak_maxValue(self, value):
		self._set_attribute('step_step_peak_maxValue', value)

	@property
	def Step_step_peak_stepTolerance(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_step_peak_stepTolerance')
	@Step_step_peak_stepTolerance.setter
	def Step_step_peak_stepTolerance(self, value):
		self._set_attribute('step_step_peak_stepTolerance', value)

	@property
	def Step_step_peak_stepValue(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_step_peak_stepValue')
	@Step_step_peak_stepValue.setter
	def Step_step_peak_stepValue(self, value):
		self._set_attribute('step_step_peak_stepValue', value)

	@property
	def Step_step_seq_enableAccLoss(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('step_step_seq_enableAccLoss')
	@Step_step_seq_enableAccLoss.setter
	def Step_step_seq_enableAccLoss(self, value):
		self._set_attribute('step_step_seq_enableAccLoss', value)

	@property
	def Step_step_seq_modeAccLoss(self):
		"""NOT DEFINED

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('step_step_seq_modeAccLoss')
	@Step_step_seq_modeAccLoss.setter
	def Step_step_seq_modeAccLoss(self, value):
		self._set_attribute('step_step_seq_modeAccLoss', value)

	@property
	def Step_step_seq_thresholdAccLoss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('step_step_seq_thresholdAccLoss')
	@Step_step_seq_thresholdAccLoss.setter
	def Step_step_seq_thresholdAccLoss(self, value):
		self._set_attribute('step_step_seq_thresholdAccLoss', value)

	@property
	def StopTestOnHighLoss(self):
		"""It stops test on high loss.

		Returns:
			number
		"""
		return self._get_attribute('stopTestOnHighLoss')
	@StopTestOnHighLoss.setter
	def StopTestOnHighLoss(self, value):
		self._set_attribute('stopTestOnHighLoss', value)

	@property
	def SupportedTrafficTypes(self):
		"""The supported traffic types.

		Returns:
			str
		"""
		return self._get_attribute('supportedTrafficTypes')
	@SupportedTrafficTypes.setter
	def SupportedTrafficTypes(self, value):
		self._set_attribute('supportedTrafficTypes', value)

	@property
	def Tolerance(self):
		"""The tolerance value.

		Returns:
			number
		"""
		return self._get_attribute('tolerance')
	@Tolerance.setter
	def Tolerance(self, value):
		self._set_attribute('tolerance', value)

	@property
	def TrafficType(self):
		"""It signifies the traffic type for the protocol. Possible values include:

		Returns:
			str(burstyLoading|constantLoading)
		"""
		return self._get_attribute('trafficType')
	@TrafficType.setter
	def TrafficType(self, value):
		self._set_attribute('trafficType', value)

	@property
	def TxDelay(self):
		"""The minimum delay between successive packets.

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	@property
	def UnchangedInitial(self):
		"""The first value of an unchanged parameter.

		Returns:
			str(False|True)
		"""
		return self._get_attribute('unchangedInitial')
	@UnchangedInitial.setter
	def UnchangedInitial(self, value):
		self._set_attribute('unchangedInitial', value)

	@property
	def UnchangedValueList(self):
		"""A list of variable parameter values that are unchanged.

		Returns:
			str
		"""
		return self._get_attribute('unchangedValueList')
	@UnchangedValueList.setter
	def UnchangedValueList(self, value):
		self._set_attribute('unchangedValueList', value)

	@property
	def UsePercentOffsets(self):
		"""If true, sets the offset value in percentage.

		Returns:
			bool
		"""
		return self._get_attribute('usePercentOffsets')
	@UsePercentOffsets.setter
	def UsePercentOffsets(self, value):
		self._set_attribute('usePercentOffsets', value)

	@property
	def UseTiLoss(self):
		"""Use loss across Rx Ports

		Returns:
			str
		"""
		return self._get_attribute('useTiLoss')
	@UseTiLoss.setter
	def UseTiLoss(self, value):
		self._set_attribute('useTiLoss', value)

	def update(self, BackoffIteration=None, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTiLoss=None, BinaryTolerance=None, Binary_delay_enableAccLoss=None, Binary_delay_modeAccLoss=None, Binary_delay_scaleAccLoss=None, Binary_delay_thresholdAccLoss=None, Binary_flooded_enableAccLoss=None, Binary_flooded_thresholdAccLoss=None, Binary_integrity_enableAccLoss=None, Binary_integrity_thresholdAccLoss=None, Binary_latency_enableAccLoss=None, Binary_latency_modeAccLoss=None, Binary_latency_scaleAccLoss=None, Binary_latency_thresholdAccLoss=None, Binary_seq_enableAccLoss=None, Binary_seq_modeAccLoss=None, Binary_seq_thresholdAccLoss=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, ComboBackoff=None, ComboFrameLossUnit=None, ComboLoadUnit=None, ComboResolution=None, ComboTiLoss=None, ComboTolerance=None, Combo_delay_enableAccLoss=None, Combo_delay_modeAccLoss=None, Combo_delay_scaleAccLoss=None, Combo_delay_thresholdAccLoss=None, Combo_flooded_enableAccLoss=None, Combo_flooded_thresholdAccLoss=None, Combo_integrity_enableAccLoss=None, Combo_integrity_thresholdAccLoss=None, Combo_latency_enableAccLoss=None, Combo_latency_modeAccLoss=None, Combo_latency_scaleAccLoss=None, Combo_latency_thresholdAccLoss=None, Combo_seq_enableAccLoss=None, Combo_seq_modeAccLoss=None, Combo_seq_thresholdAccLoss=None, CountRandomFrameSize=None, CountRandomIpRatio=None, CountRandomLoadRate=None, CustomLoadUnit=None, CustomTiLoss=None, Custom_binary_delay_enableAccLoss=None, Custom_binary_delay_modeAccLoss=None, Custom_binary_delay_scaleAccLoss=None, Custom_binary_delay_thresholdAccLoss=None, Custom_binary_flooded_enableAccLoss=None, Custom_binary_flooded_thresholdAccLoss=None, Custom_binary_integrity_enableAccLoss=None, Custom_binary_integrity_thresholdAccLoss=None, Custom_binary_latency_enableAccLoss=None, Custom_binary_latency_modeAccLoss=None, Custom_binary_latency_scaleAccLoss=None, Custom_binary_latency_thresholdAccLoss=None, Custom_binary_peak_Backoff=None, Custom_binary_peak_FrameLossUnit=None, Custom_binary_peak_Resolution=None, Custom_binary_peak_Tolerance=None, Custom_binary_peak_initialValue=None, Custom_binary_peak_maxValue=None, Custom_binary_peak_minValue=None, Custom_binary_seq_enableAccLoss=None, Custom_binary_seq_modeAccLoss=None, Custom_binary_seq_thresholdAccLoss=None, Custom_peak_loadType=None, Custom_step_delay_enableAccLoss=None, Custom_step_delay_modeAccLoss=None, Custom_step_delay_scaleAccLoss=None, Custom_step_delay_thresholdAccLoss=None, Custom_step_flooded_enableAccLoss=None, Custom_step_flooded_thresholdAccLoss=None, Custom_step_integrity_enableAccLoss=None, Custom_step_integrity_thresholdAccLoss=None, Custom_step_latency_enableAccLoss=None, Custom_step_latency_modeAccLoss=None, Custom_step_latency_scaleAccLoss=None, Custom_step_latency_thresholdAccLoss=None, Custom_step_peak_FrameLossUnit=None, Custom_step_peak_initialValue=None, Custom_step_peak_maxValue=None, Custom_step_peak_stepTolerance=None, Custom_step_peak_stepValue=None, Custom_step_seq_enableAccLoss=None, Custom_step_seq_modeAccLoss=None, Custom_step_seq_thresholdAccLoss=None, CustompeakvalueList=None, DelayAfterTransmit=None, DetailedResultsEnabled=None, Duration=None, EnableBackoffIteration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableMinFrameSize=None, EnableOldStatsForReef=None, EnableSaturationIteration=None, EnableStopTestOnHighLoss=None, ExtraIterationOffsets=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, FixedLoadUnit=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameLossUnit=None, FrameOrderingTemp=None, FrameSizeMode=None, FramesPerBurstGap=None, Framesize=None, FramesizeFixedValue=None, FramesizeImixList=None, FramesizeList=None, Gap=None, GenerateTrackingOptionAggregationFiles=None, ImixAdd=None, ImixData=None, ImixDelete=None, ImixDistribution=None, ImixEnabled=None, ImixTemplates=None, ImixTrafficType=None, IncrementLoadUnit=None, InitialBinaryLoadRate=None, InitialComboLoadRate=None, InitialIncrementLoadRate=None, InitialStepLoadRate=None, IpRatioMode=None, Ipv4RatioList=None, Ipv4rate=None, Ipv6RatioList=None, Ipv6rate=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadRateList=None, LoadRateValue=None, LoadType=None, MapType=None, MaxBinaryLoadRate=None, MaxComboLoadRate=None, MaxIncrementFrameSize=None, MaxIncrementIpv4Ratio=None, MaxIncrementIpv6Ratio=None, MaxIncrementLoadRate=None, MaxQuickSearchLoadRate=None, MaxRandomFrameSize=None, MaxRandomIpv4Ratio=None, MaxRandomIpv6Ratio=None, MaxRandomLoadRate=None, MaxStepLoadRate=None, MinBinaryLoadRate=None, MinComboLoadRate=None, MinFpsRate=None, MinIncrementFrameSize=None, MinIncrementIpv4Ratio=None, MinIncrementIpv6Ratio=None, MinKbpsRate=None, MinQuickSearchLoadRate=None, MinRandomFrameSize=None, MinRandomIpv4Ratio=None, MinRandomIpv6Ratio=None, MinRandomLoadRate=None, Numtrials=None, PeakLoadingReplicationCount=None, Peak_customLoadUnit=None, Peak_initialStepLoadRate=None, Peak_loadRateList=None, Peak_maxStepLoadRate=None, Peak_rate_loadType=None, Peak_stepLoadUnit=None, Peak_stepStepLoadRate=None, PerTrafficResults=None, PercentMaxRate=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, QuickBackoffIteration=None, QuickEnableBackoffIteration=None, QuickEnableSaturationIteration=None, QuickSaturationIteration=None, QuickSearchFrameLossUnit=None, QuickSearchLoadUnit=None, QuickSearchResolution=None, QuickSearchSearchType=None, QuickSearchTiLoss=None, QuickSearchTolerance=None, RandomLoadUnit=None, RandomTiLoss=None, RateSelect=None, ReportSequenceError=None, ReportTputRateUnit=None, Resolution=None, Rfc2544ImixDataQoS=None, Rfc2889ordering=None, SaturationIteration=None, SearchBase=None, SendFullyMeshed=None, ShowDetailedBinaryResults=None, StaggeredStart=None, StepComboLoadRate=None, StepFrameLossUnit=None, StepIncrementFrameSize=None, StepIncrementIpv4Ratio=None, StepIncrementIpv6Ratio=None, StepIncrementLoadRate=None, StepLoadUnit=None, StepStepLoadRate=None, StepTiLoss=None, StepTolerance=None, Step_binary_delay_enableAccLoss=None, Step_binary_delay_modeAccLoss=None, Step_binary_delay_scaleAccLoss=None, Step_binary_delay_thresholdAccLoss=None, Step_binary_flooded_enableAccLoss=None, Step_binary_flooded_thresholdAccLoss=None, Step_binary_integrity_enableAccLoss=None, Step_binary_integrity_thresholdAccLoss=None, Step_binary_latency_enableAccLoss=None, Step_binary_latency_modeAccLoss=None, Step_binary_latency_scaleAccLoss=None, Step_binary_latency_thresholdAccLoss=None, Step_binary_peak_Backoff=None, Step_binary_peak_FrameLossUnit=None, Step_binary_peak_Resolution=None, Step_binary_peak_Tolerance=None, Step_binary_peak_initialValue=None, Step_binary_peak_maxValue=None, Step_binary_peak_minValue=None, Step_binary_seq_enableAccLoss=None, Step_binary_seq_modeAccLoss=None, Step_binary_seq_thresholdAccLoss=None, Step_delay_enableAccLoss=None, Step_delay_modeAccLoss=None, Step_delay_scaleAccLoss=None, Step_delay_thresholdAccLoss=None, Step_flooded_enableAccLoss=None, Step_flooded_thresholdAccLoss=None, Step_integrity_enableAccLoss=None, Step_integrity_thresholdAccLoss=None, Step_latency_enableAccLoss=None, Step_latency_modeAccLoss=None, Step_latency_scaleAccLoss=None, Step_latency_thresholdAccLoss=None, Step_peak_loadType=None, Step_seq_enableAccLoss=None, Step_seq_modeAccLoss=None, Step_seq_thresholdAccLoss=None, Step_step_delay_enableAccLoss=None, Step_step_delay_modeAccLoss=None, Step_step_delay_scaleAccLoss=None, Step_step_delay_thresholdAccLoss=None, Step_step_flooded_enableAccLoss=None, Step_step_flooded_thresholdAccLoss=None, Step_step_integrity_enableAccLoss=None, Step_step_integrity_thresholdAccLoss=None, Step_step_latency_enableAccLoss=None, Step_step_latency_modeAccLoss=None, Step_step_latency_scaleAccLoss=None, Step_step_latency_thresholdAccLoss=None, Step_step_peak_FrameLossUnit=None, Step_step_peak_initialValue=None, Step_step_peak_maxValue=None, Step_step_peak_stepTolerance=None, Step_step_peak_stepValue=None, Step_step_seq_enableAccLoss=None, Step_step_seq_modeAccLoss=None, Step_step_seq_thresholdAccLoss=None, StopTestOnHighLoss=None, SupportedTrafficTypes=None, Tolerance=None, TrafficType=None, TxDelay=None, UnchangedInitial=None, UnchangedValueList=None, UsePercentOffsets=None, UseTiLoss=None):
		"""Updates a child instance of testConfig on the server.

		Args:
			BackoffIteration (number): This enables the test to run an extra iteration for calculating the Backoff Latency.
			BinaryBackoff (number): Specifies the percentage of binary backoff.
			BinaryFrameLossUnit (str(%|frames)): The frame loss unit for traffic in binary.
			BinaryLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The load unit value in binary. Possible values include:
			BinaryResolution (number): Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.
			BinarySearchType (str(linear|perFlow|perPort|perTrafficItem)): The binary search type value. Possible values include:
			BinaryTiLoss (bool): Use loss across Rx Ports
			BinaryTolerance (number): The binary tolerance level.
			Binary_delay_enableAccLoss (bool): NOT DEFINED
			Binary_delay_modeAccLoss (str(average|maximum)): NOT DEFINED
			Binary_delay_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Binary_delay_thresholdAccLoss (number): NOT DEFINED
			Binary_flooded_enableAccLoss (bool): NOT DEFINED
			Binary_flooded_thresholdAccLoss (number): NOT DEFINED
			Binary_integrity_enableAccLoss (bool): NOT DEFINED
			Binary_integrity_thresholdAccLoss (number): NOT DEFINED
			Binary_latency_enableAccLoss (bool): NOT DEFINED
			Binary_latency_modeAccLoss (str(average|maximum)): NOT DEFINED
			Binary_latency_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Binary_latency_thresholdAccLoss (number): NOT DEFINED
			Binary_seq_enableAccLoss (bool): NOT DEFINED
			Binary_seq_modeAccLoss (str(average|maximum)): NOT DEFINED
			Binary_seq_thresholdAccLoss (number): NOT DEFINED
			BurstSize (number): The number of packets that are sent in a burst.
			CalculateJitter (bool): If true, calculates jitter.
			CalculateLatency (bool): If true, calculates the latency.
			ComboBackoff (number): The backoff combination of the test configuration.
			ComboFrameLossUnit (str(%|frames)): The frame loss unit for traffic in binary.
			ComboLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The combination of load units. Possible values include:
			ComboResolution (number): The combined resolution value.
			ComboTiLoss (bool): Use loss across Rx Ports
			ComboTolerance (number): The combined tolerance level.
			Combo_delay_enableAccLoss (bool): NOT DEFINED
			Combo_delay_modeAccLoss (str(average|maximum)): NOT DEFINED
			Combo_delay_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Combo_delay_thresholdAccLoss (number): NOT DEFINED
			Combo_flooded_enableAccLoss (bool): NOT DEFINED
			Combo_flooded_thresholdAccLoss (number): NOT DEFINED
			Combo_integrity_enableAccLoss (bool): NOT DEFINED
			Combo_integrity_thresholdAccLoss (number): NOT DEFINED
			Combo_latency_enableAccLoss (bool): NOT DEFINED
			Combo_latency_modeAccLoss (str(average|maximum)): NOT DEFINED
			Combo_latency_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Combo_latency_thresholdAccLoss (number): NOT DEFINED
			Combo_seq_enableAccLoss (bool): NOT DEFINED
			Combo_seq_modeAccLoss (str(average|maximum)): NOT DEFINED
			Combo_seq_thresholdAccLoss (number): NOT DEFINED
			CountRandomFrameSize (number): Randomly counts the frame size.
			CountRandomIpRatio (number): Sets the count of the random ip ratio loop
			CountRandomLoadRate (number): Randomly counts the load rate.
			CustomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Specifies the custom load unit. Possible values include:
			CustomTiLoss (bool): Use loss across Rx Ports
			Custom_binary_delay_enableAccLoss (bool): NOT DEFINED
			Custom_binary_delay_modeAccLoss (str(average|maximum)): NOT DEFINED
			Custom_binary_delay_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Custom_binary_delay_thresholdAccLoss (number): NOT DEFINED
			Custom_binary_flooded_enableAccLoss (bool): NOT DEFINED
			Custom_binary_flooded_thresholdAccLoss (number): NOT DEFINED
			Custom_binary_integrity_enableAccLoss (bool): NOT DEFINED
			Custom_binary_integrity_thresholdAccLoss (number): NOT DEFINED
			Custom_binary_latency_enableAccLoss (bool): NOT DEFINED
			Custom_binary_latency_modeAccLoss (str(average|maximum)): NOT DEFINED
			Custom_binary_latency_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Custom_binary_latency_thresholdAccLoss (number): NOT DEFINED
			Custom_binary_peak_Backoff (number): NOT DEFINED
			Custom_binary_peak_FrameLossUnit (str(%|frames)): NOT DEFINED
			Custom_binary_peak_Resolution (number): NOT DEFINED
			Custom_binary_peak_Tolerance (number): NOT DEFINED
			Custom_binary_peak_initialValue (number): NOT DEFINED
			Custom_binary_peak_maxValue (number): NOT DEFINED
			Custom_binary_peak_minValue (number): NOT DEFINED
			Custom_binary_seq_enableAccLoss (bool): NOT DEFINED
			Custom_binary_seq_modeAccLoss (str(average|maximum)): NOT DEFINED
			Custom_binary_seq_thresholdAccLoss (number): NOT DEFINED
			Custom_peak_loadType (str(binary|custom|step)): NOT DEFINED
			Custom_step_delay_enableAccLoss (bool): NOT DEFINED
			Custom_step_delay_modeAccLoss (str(average|maximum)): NOT DEFINED
			Custom_step_delay_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Custom_step_delay_thresholdAccLoss (number): NOT DEFINED
			Custom_step_flooded_enableAccLoss (bool): NOT DEFINED
			Custom_step_flooded_thresholdAccLoss (number): NOT DEFINED
			Custom_step_integrity_enableAccLoss (bool): NOT DEFINED
			Custom_step_integrity_thresholdAccLoss (number): NOT DEFINED
			Custom_step_latency_enableAccLoss (bool): NOT DEFINED
			Custom_step_latency_modeAccLoss (str(average|maximum)): NOT DEFINED
			Custom_step_latency_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Custom_step_latency_thresholdAccLoss (number): NOT DEFINED
			Custom_step_peak_FrameLossUnit (str(%|frames)): NOT DEFINED
			Custom_step_peak_initialValue (number): NOT DEFINED
			Custom_step_peak_maxValue (number): NOT DEFINED
			Custom_step_peak_stepTolerance (number): NOT DEFINED
			Custom_step_peak_stepValue (number): NOT DEFINED
			Custom_step_seq_enableAccLoss (bool): NOT DEFINED
			Custom_step_seq_modeAccLoss (str(average|maximum)): NOT DEFINED
			Custom_step_seq_thresholdAccLoss (number): NOT DEFINED
			CustompeakvalueList (str): NOT DEFINED
			DelayAfterTransmit (number): Specifies the amount of delay after every transmit
			DetailedResultsEnabled (bool): If true, it enables the detailed results for the fully meshed case
			Duration (number): sec
			EnableBackoffIteration (bool): If true, enables back off iteration test.
			EnableDataIntegrity (bool): If true, enables data integrity test.
			EnableExtraIterations (bool): If true, more iterations are performed.
			EnableFastConvergence (bool): If true, the test perform iterations using the fast convergence duration configured.
			EnableLayer1Rate (bool): NOT DEFINED
			EnableMinFrameSize (bool): If Enabled, The minimum size of the frame is used .
			EnableOldStatsForReef (bool): If true, enables old statistics for reef load module.
			EnableSaturationIteration (bool): If true, SaturationIteration in enabled .
			EnableStopTestOnHighLoss (bool): The test stops in case of a high loss.
			ExtraIterationOffsets (str): This enables the test to run an extra iteration.
			FastConvergenceDuration (number): sec
			FastConvergenceThreshold (number): This enables the test to perform iterations using the fast convergence threshold configured.
			FixedLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Possible values include:
			FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
			ForceRegenerate (bool): Initiates a forced regeneration.
			FrameLossUnit (str): The frame loss unit for traffic.
			FrameOrderingTemp (str(noOrdering|peakLoading|unchanged|val2889Ordering)): NOT DEFINED
			FrameSizeMode (str(custom|increment|random|unchanged)): This attribute is the frame size mode for the Quad Gaussian. Possible values includes:
			FramesPerBurstGap (number): The number of frames to be sent after each burst.
			Framesize (number): Bytes
			FramesizeFixedValue (number): The fixed value of framesize.
			FramesizeImixList (str): The list of the available lmix frame size.
			FramesizeList (list(str)): The list of the available frame size.
			Gap (number): The gap in transmission of frames.
			GenerateTrackingOptionAggregationFiles (bool): If true, enables the tracking option in aggregation files.
			ImixAdd (str): Adds an imix data.
			ImixData (str): Displays the imix Data.
			ImixDelete (str): Deletes the imix data.
			ImixDistribution (str(bwpercentage|weight)): Specifies the imix distribution unit.
			ImixEnabled (bool): If True, Enables the imix value.
			ImixTemplates (str(cisco|imix|ipsec|ipv6|none|quadmodal|standard|tcp|tolly|trimodal)): Specefies the imix templates.
			ImixTrafficType (str): Displays the imix traffic type.
			IncrementLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Possible values include:
			InitialBinaryLoadRate (number): The initial binary value of the load rate.
			InitialComboLoadRate (number): The initial combination value of the load rate .
			InitialIncrementLoadRate (number): The initial incremental value of the load rate.
			InitialStepLoadRate (number): The initial step value of the load rate.
			IpRatioMode (str(custom|fixed|increment|random)): Sets the ip ratio mode
			Ipv4RatioList (str): Sets the ipv4 ratio list
			Ipv4rate (number): The rate at which IPv4 traffic is sent.
			Ipv6RatioList (str): Sets the ipv6 ratio list
			Ipv6rate (number): The rate at which IPv6 traffic is sent.
			LatencyBins (str): Sets the latency bins statistics
			LatencyBinsEnabled (bool): Enables the latency bins statistics
			LatencyType (str(cutThrough|forwardingDelay|mef|storeForward)): The type of latency. Possible values include:
			LoadRateList (str): The list of Load Rate.
			LoadRateValue (number): The value of the load rate.
			LoadType (str(binary|combo|custom|quickSearch|random|step|unchanged)): Possible values include:
			MapType (str): The mapping type.
			MaxBinaryLoadRate (number): The upper bound of the iteration rates for each frame size during a binary search.
			MaxComboLoadRate (number): The maximum value of the load rate Combo Load Type.
			MaxIncrementFrameSize (number): It signifies the maximum increment frame size.
			MaxIncrementIpv4Ratio (str): Sets the maximum increment value for the ipv4 ratio
			MaxIncrementIpv6Ratio (str): Sets the maximum increment value for the ipv6 ratio
			MaxIncrementLoadRate (number): It signifies the maximum increment load rate value.
			MaxQuickSearchLoadRate (number): Sets the maximum QuickSearch load rate
			MaxRandomFrameSize (number): It signifies the maximum random frame size value.
			MaxRandomIpv4Ratio (str): Sets the maximum radom value for the ipv4 ratio
			MaxRandomIpv6Ratio (str): Sets the maximum random value for the ipv6 ratio
			MaxRandomLoadRate (number): It signifies the maximum random load rate value.
			MaxStepLoadRate (number): It signifies the maximum step value for load rate.
			MinBinaryLoadRate (number): Specifies the minimum rate of the binary algorithm.
			MinComboLoadRate (number): The minimum combination load rate.
			MinFpsRate (number): The rate at which minimum frames are sent per second.
			MinIncrementFrameSize (number): It signifies the minimum increment frame size.
			MinIncrementIpv4Ratio (str): Sets the minimum increment value for the ipv4 ratio
			MinIncrementIpv6Ratio (str): Sets the minimum increment value for the ipv6 ratio
			MinKbpsRate (number): The rate at which minimum frames are sent per kbps.
			MinQuickSearchLoadRate (number): Sets the minum Quick Search load rate
			MinRandomFrameSize (number): The minimum random frame size to be sent.
			MinRandomIpv4Ratio (str): Sets the minimum random value for the ipv4 ratio
			MinRandomIpv6Ratio (str): Sets the minimum random value for the ipv6 ratio
			MinRandomLoadRate (number): The minimum random value of the load rate.
			Numtrials (number): The integer value that states the number of trials permitted.
			PeakLoadingReplicationCount (number): NOT DEFINED
			Peak_customLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): NOT DEFINED
			Peak_initialStepLoadRate (number): NOT DEFINED
			Peak_loadRateList (str): NOT DEFINED
			Peak_maxStepLoadRate (number): NOT DEFINED
			Peak_rate_loadType (str(custom|step)): NOT DEFINED
			Peak_stepLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): 
			Peak_stepStepLoadRate (number): NOT DEFINED
			PerTrafficResults (bool): 
			PercentMaxRate (number): The maximum rate percentage.
			PortDelayEnabled (bool): NOT DEFINED
			PortDelayUnit (str(bytes|nanoseconds)): Sets the port delay unit in which it will be measured
			PortDelayValue (number): Sets the port delay value
			ProtocolItem (list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])): Protocol Items
			QuickBackoffIteration (number): Sets the quicksearch backoff iteration
			QuickEnableBackoffIteration (bool): Enables the quick search backoff iteration
			QuickEnableSaturationIteration (bool): Enables the Quick Search saturation iteration
			QuickSaturationIteration (number): Sets the quick search saturation iteration
			QuickSearchFrameLossUnit (str(%)): Sets the quick search frame loss unit
			QuickSearchLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Sets the quick search load unit
			QuickSearchResolution (number): Sets the quick search resolution
			QuickSearchSearchType (str(linear|perFlow|perPort|perTrafficItem)): Sets the quick search type
			QuickSearchTiLoss (bool): Use loss across Rx Ports
			QuickSearchTolerance (number): Sets the quick search tolerance
			RandomLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): The random values of the load unit. Possible values include:
			RandomTiLoss (bool): Use loss across Rx Ports
			RateSelect (str(fpsRate|kbpsRate|percentMaxRate)): Possible values include:
			ReportSequenceError (bool): Reports sequence errors in the test result.
			ReportTputRateUnit (str(gbps|gBps|kbps|kBps|mbps|mBps)): The reported throughput rate unit values. Possible values include:
			Resolution (number): Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops .
			Rfc2544ImixDataQoS (bool): If true, it uses the same frame data qos
			Rfc2889ordering (str(noOrdering|peakLoading|unchanged|val2889Ordering)): If true, indicates frame ordering by Rfc2889.
			SaturationIteration (number): This enables the test to run an extra iteration for calculating the Saturation latency.
			SearchBase (str(rate|replicationCount)): NOT DEFINED
			SendFullyMeshed (bool): Indicates the source group mapping type used for sending data.
			ShowDetailedBinaryResults (bool): NOT DEFINED
			StaggeredStart (bool): Starts test with a stagger.
			StepComboLoadRate (number): The step value of combination load rate.
			StepFrameLossUnit (str(%|frames)): The frame loss unit.
			StepIncrementFrameSize (number): The traffic step increment frame size.
			StepIncrementIpv4Ratio (str): The step in which the ipv4 ratio loop is incremented
			StepIncrementIpv6Ratio (str): The step in which the ipv6 ratio loop is incremented
			StepIncrementLoadRate (number): The incremental step value of the load rate.
			StepLoadUnit (str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)): Specifies the step rate of the load unit. Possible values include:
			StepStepLoadRate (number): The incremental step value of load rate.
			StepTiLoss (bool): Use loss across Rx Ports
			StepTolerance (number): The step value of the tolerance level.
			Step_binary_delay_enableAccLoss (bool): NOT DEFINED
			Step_binary_delay_modeAccLoss (str(average|maximum)): NOT DEFINED
			Step_binary_delay_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Step_binary_delay_thresholdAccLoss (number): NOT DEFINED
			Step_binary_flooded_enableAccLoss (bool): NOT DEFINED
			Step_binary_flooded_thresholdAccLoss (number): NOT DEFINED
			Step_binary_integrity_enableAccLoss (bool): NOT DEFINED
			Step_binary_integrity_thresholdAccLoss (number): NOT DEFINED
			Step_binary_latency_enableAccLoss (bool): NOT DEFINED
			Step_binary_latency_modeAccLoss (str(average|maximum)): NOT DEFINED
			Step_binary_latency_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Step_binary_latency_thresholdAccLoss (number): NOT DEFINED
			Step_binary_peak_Backoff (number): NOT DEFINED
			Step_binary_peak_FrameLossUnit (str(%|frames)): NOT DEFINED
			Step_binary_peak_Resolution (number): NOT DEFINED
			Step_binary_peak_Tolerance (number): NOT DEFINED
			Step_binary_peak_initialValue (number): NOT DEFINED
			Step_binary_peak_maxValue (number): NOT DEFINED
			Step_binary_peak_minValue (number): NOT DEFINED
			Step_binary_seq_enableAccLoss (bool): NOT DEFINED
			Step_binary_seq_modeAccLoss (str(average|maximum)): NOT DEFINED
			Step_binary_seq_thresholdAccLoss (number): NOT DEFINED
			Step_delay_enableAccLoss (bool): NOT DEFINED
			Step_delay_modeAccLoss (str(average|maximum)): NOT DEFINED
			Step_delay_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Step_delay_thresholdAccLoss (number): NOT DEFINED
			Step_flooded_enableAccLoss (bool): NOT DEFINED
			Step_flooded_thresholdAccLoss (number): NOT DEFINED
			Step_integrity_enableAccLoss (bool): NOT DEFINED
			Step_integrity_thresholdAccLoss (number): NOT DEFINED
			Step_latency_enableAccLoss (bool): NOT DEFINED
			Step_latency_modeAccLoss (str(average|maximum)): NOT DEFINED
			Step_latency_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Step_latency_thresholdAccLoss (number): NOT DEFINED
			Step_peak_loadType (str(binary|custom|step)): NOT DEFINED
			Step_seq_enableAccLoss (bool): NOT DEFINED
			Step_seq_modeAccLoss (str(average|maximum)): NOT DEFINED
			Step_seq_thresholdAccLoss (number): NOT DEFINED
			Step_step_delay_enableAccLoss (bool): NOT DEFINED
			Step_step_delay_modeAccLoss (str(average|maximum)): NOT DEFINED
			Step_step_delay_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Step_step_delay_thresholdAccLoss (number): NOT DEFINED
			Step_step_flooded_enableAccLoss (bool): NOT DEFINED
			Step_step_flooded_thresholdAccLoss (number): NOT DEFINED
			Step_step_integrity_enableAccLoss (bool): NOT DEFINED
			Step_step_integrity_thresholdAccLoss (number): NOT DEFINED
			Step_step_latency_enableAccLoss (bool): NOT DEFINED
			Step_step_latency_modeAccLoss (str(average|maximum)): NOT DEFINED
			Step_step_latency_scaleAccLoss (str(ms|ns|us)): NOT DEFINED
			Step_step_latency_thresholdAccLoss (number): NOT DEFINED
			Step_step_peak_FrameLossUnit (str(%|frames)): NOT DEFINED
			Step_step_peak_initialValue (number): NOT DEFINED
			Step_step_peak_maxValue (number): NOT DEFINED
			Step_step_peak_stepTolerance (number): NOT DEFINED
			Step_step_peak_stepValue (number): NOT DEFINED
			Step_step_seq_enableAccLoss (bool): NOT DEFINED
			Step_step_seq_modeAccLoss (str(average|maximum)): NOT DEFINED
			Step_step_seq_thresholdAccLoss (number): NOT DEFINED
			StopTestOnHighLoss (number): It stops test on high loss.
			SupportedTrafficTypes (str): The supported traffic types.
			Tolerance (number): The tolerance value.
			TrafficType (str(burstyLoading|constantLoading)): It signifies the traffic type for the protocol. Possible values include:
			TxDelay (number): The minimum delay between successive packets.
			UnchangedInitial (str(False|True)): The first value of an unchanged parameter.
			UnchangedValueList (str): A list of variable parameter values that are unchanged.
			UsePercentOffsets (bool): If true, sets the offset value in percentage.
			UseTiLoss (str): Use loss across Rx Ports

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def Apply(self):
		"""Executes the apply operation on the server.

		Applies the specified Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('apply', payload=payload, response_object=None)

	def ApplyAsync(self):
		"""Executes the applyAsync operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyAsync', payload=payload, response_object=None)

	def ApplyAsyncResult(self):
		"""Executes the applyAsyncResult operation on the server.

			Returns:
				bool: 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyAsyncResult', payload=payload, response_object=None)

	def ApplyITWizardConfiguration(self):
		"""Executes the applyITWizardConfiguration operation on the server.

		Applies the specified Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

	def GenerateReport(self):
		"""Executes the generateReport operation on the server.

		Generate a PDF report for the last succesfull test run.

			Returns:
				str: This method is asynchronous and has no return value.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('generateReport', payload=payload, response_object=None)

	def Run(self, *args, **kwargs):
		"""Executes the run operation on the server.

		Starts the specified Quick Test and waits for its execution to finish.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		run()list

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		run(InputParameters:string)list
			Args:
				args[0] is InputParameters (str): The input arguments of the test.

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('run', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Starts the specified Quick Test.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(InputParameters:string)
			Args:
				args[0] is InputParameters (str): The input arguments of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stops the currently running Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)

	def WaitForTest(self):
		"""Executes the waitForTest operation on the server.

		Waits for the execution of the specified Quick Test to be completed.

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('waitForTest', payload=payload, response_object=None)
