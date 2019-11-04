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


class QuickTest(Base):
	"""The IxNetwork QuickTests feature provides the ability to run predefined tests.
	The QuickTest class encapsulates a required quickTest resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'quickTest'

	def __init__(self, parent):
		super(QuickTest, self).__init__(parent)

	@property
	def AsymmetricFrameLoss(self):
		"""An instance of the AsymmetricFrameLoss class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss_vzdc9hc3ltbwv0cmljrnjhbwvmb3nz.AsymmetricFrameLoss)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss_vzdc9hc3ltbwv0cmljrnjhbwvmb3nz import AsymmetricFrameLoss
		return AsymmetricFrameLoss(self)

	@property
	def AsymmetricThroughput(self):
		"""An instance of the AsymmetricThroughput class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput_dc9hc3ltbwv0cmljvghyb3vnahb1da.AsymmetricThroughput)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput_dc9hc3ltbwv0cmljvghyb3vnahb1da import AsymmetricThroughput
		return AsymmetricThroughput(self)

	@property
	def CloudPerf(self):
		"""An instance of the CloudPerf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf_l3f1awnrvgvzdc9jbg91zfblcmy.CloudPerf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf_l3f1awnrvgvzdc9jbg91zfblcmy import CloudPerf
		return CloudPerf(self)

	@property
	def CustomContDuration(self):
		"""An instance of the CustomContDuration class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration_gvzdc9jdxn0b21db250rhvyyxrpb24.CustomContDuration)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration_gvzdc9jdxn0b21db250rhvyyxrpb24 import CustomContDuration
		return CustomContDuration(self)

	@property
	def CustomFixedDuration(self):
		"""An instance of the CustomFixedDuration class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration_vzdc9jdxn0b21gaxhlzer1cmf0aw9u.CustomFixedDuration)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration_vzdc9jdxn0b21gaxhlzer1cmf0aw9u import CustomFixedDuration
		return CustomFixedDuration(self)

	@property
	def CustomStep(self):
		"""An instance of the CustomStep class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customstep_l3f1awnrvgvzdc9jdxn0b21tdgvw.CustomStep)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customstep_l3f1awnrvgvzdc9jdxn0b21tdgvw import CustomStep
		return CustomStep(self)

	@property
	def CustomThroughput(self):
		"""An instance of the CustomThroughput class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput_nrvgvzdc9jdxn0b21uahjvdwdochv0.CustomThroughput)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput_nrvgvzdc9jdxn0b21uahjvdwdochv0 import CustomThroughput
		return CustomThroughput(self)

	@property
	def DhcpRate(self):
		"""An instance of the DhcpRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate_l3f1awnrvgvzdc9kagnwumf0zq.DhcpRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate_l3f1awnrvgvzdc9kagnwumf0zq import DhcpRate
		return DhcpRate(self)

	@property
	def DhcpRateCpf(self):
		"""An instance of the DhcpRateCpf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpratecpf_l3f1awnrvgvzdc9kagnwumf0zunwzg.DhcpRateCpf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpratecpf_l3f1awnrvgvzdc9kagnwumf0zunwzg import DhcpRateCpf
		return DhcpRateCpf(self)

	@property
	def Dhcpv6Rate(self):
		"""An instance of the Dhcpv6Rate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate_l3f1awnrvgvzdc9kagnwdjzsyxrl.Dhcpv6Rate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate_l3f1awnrvgvzdc9kagnwdjzsyxrl import Dhcpv6Rate
		return Dhcpv6Rate(self)

	@property
	def Dhcpv6RateCpf(self):
		"""An instance of the Dhcpv6RateCpf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6ratecpf_f1awnrvgvzdc9kagnwdjzsyxrlq3bm.Dhcpv6RateCpf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6ratecpf_f1awnrvgvzdc9kagnwdjzsyxrlq3bm import Dhcpv6RateCpf
		return Dhcpv6RateCpf(self)

	@property
	def Dot1xCapacity(self):
		"""An instance of the Dot1xCapacity class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity_f1awnrvgvzdc9kb3qxeenhcgfjaxr5.Dot1xCapacity)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity_f1awnrvgvzdc9kb3qxeenhcgfjaxr5 import Dot1xCapacity
		return Dot1xCapacity(self)

	@property
	def Dot1xRate(self):
		"""An instance of the Dot1xRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate_l3f1awnrvgvzdc9kb3qxefjhdgu.Dot1xRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate_l3f1awnrvgvzdc9kb3qxefjhdgu import Dot1xRate
		return Dot1xRate(self)

	@property
	def EventScheduler(self):
		"""An instance of the EventScheduler class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler_awnrvgvzdc9ldmvudfnjagvkdwxlcg.EventScheduler)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler_awnrvgvzdc9ldmvudfnjagvkdwxlcg import EventScheduler
		return EventScheduler(self)

	@property
	def FcoeMaxNoDropThroughput(self):
		"""An instance of the FcoeMaxNoDropThroughput class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput_y29ltwf4tm9ecm9wvghyb3vnahb1da.FcoeMaxNoDropThroughput)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput_y29ltwf4tm9ecm9wvghyb3vnahb1da import FcoeMaxNoDropThroughput
		return FcoeMaxNoDropThroughput(self)

	@property
	def FcoeMaxNoPauseThroughput(self):
		"""An instance of the FcoeMaxNoPauseThroughput class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput_29ltwf4tm9qyxvzzvrocm91z2hwdxq.FcoeMaxNoPauseThroughput)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput_29ltwf4tm9qyxvzzvrocm91z2hwdxq import FcoeMaxNoPauseThroughput
		return FcoeMaxNoPauseThroughput(self)

	@property
	def Globals(self):
		"""An instance of the Globals class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.globals_l3f1awnrvgvzdc9nbg9iywxz.Globals)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.globals_l3f1awnrvgvzdc9nbg9iywxz import Globals
		return Globals(self)._select()

	@property
	def IptvChannelZapping(self):
		"""An instance of the IptvChannelZapping class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping_gvzdc9pchr2q2hhbm5lbfphchbpbmc.IptvChannelZapping)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping_gvzdc9pchr2q2hhbm5lbfphchbpbmc import IptvChannelZapping
		return IptvChannelZapping(self)

	@property
	def L2tpCapacity(self):
		"""An instance of the L2tpCapacity class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpcapacity_3f1awnrvgvzdc9smnrwq2fwywnpdhk.L2tpCapacity)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpcapacity_3f1awnrvgvzdc9smnrwq2fwywnpdhk import L2tpCapacity
		return L2tpCapacity(self)

	@property
	def L2tpRate(self):
		"""An instance of the L2tpRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate_l3f1awnrvgvzdc9smnrwumf0zq.L2tpRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate_l3f1awnrvgvzdc9smnrwumf0zq import L2tpRate
		return L2tpRate(self)

	@property
	def L2tpRateCpf(self):
		"""An instance of the L2tpRateCpf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpratecpf_l3f1awnrvgvzdc9smnrwumf0zunwzg.L2tpRateCpf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpratecpf_l3f1awnrvgvzdc9smnrwumf0zunwzg import L2tpRateCpf
		return L2tpRateCpf(self)

	@property
	def LnsCpfCapacity(self):
		"""An instance of the LnsCpfCapacity class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.lnscpfcapacity_awnrvgvzdc9sbnndcgzdyxbhy2l0eq.LnsCpfCapacity)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.lnscpfcapacity_awnrvgvzdc9sbnndcgzdyxbhy2l0eq import LnsCpfCapacity
		return LnsCpfCapacity(self)

	@property
	def OpenFlowFailoverPerformance(self):
		"""An instance of the OpenFlowFailoverPerformance class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance_mxvd0zhawxvdmvyugvyzm9ybwfuy2u.OpenFlowFailoverPerformance)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance_mxvd0zhawxvdmvyugvyzm9ybwfuy2u import OpenFlowFailoverPerformance
		return OpenFlowFailoverPerformance(self)

	@property
	def OpenFlowLayer2LearningRate(self):
		"""An instance of the OpenFlowLayer2LearningRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate_rmxvd0xhewvymkxlyxjuaw5numf0zq.OpenFlowLayer2LearningRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate_rmxvd0xhewvymkxlyxjuaw5numf0zq import OpenFlowLayer2LearningRate
		return OpenFlowLayer2LearningRate(self)

	@property
	def OpenFlowLayer3LearningRate(self):
		"""An instance of the OpenFlowLayer3LearningRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate_rmxvd0xhewvym0xlyxjuaw5numf0zq.OpenFlowLayer3LearningRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate_rmxvd0xhewvym0xlyxjuaw5numf0zq import OpenFlowLayer3LearningRate
		return OpenFlowLayer3LearningRate(self)

	@property
	def OpenFlowTableCapacity(self):
		"""An instance of the OpenFlowTableCapacity class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity_c9vcgvurmxvd1rhymxlq2fwywnpdhk.OpenFlowTableCapacity)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity_c9vcgvurmxvd1rhymxlq2fwywnpdhk import OpenFlowTableCapacity
		return OpenFlowTableCapacity(self)

	@property
	def PppServerCapacity(self):
		"""An instance of the PppServerCapacity class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity_vgvzdc9wchbtzxj2zxjdyxbhy2l0eq.PppServerCapacity)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity_vgvzdc9wchbtzxj2zxjdyxbhy2l0eq import PppServerCapacity
		return PppServerCapacity(self)

	@property
	def PppSessionRate(self):
		"""An instance of the PppSessionRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate_awnrvgvzdc9wchbtzxnzaw9uumf0zq.PppSessionRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate_awnrvgvzdc9wchbtzxnzaw9uumf0zq import PppSessionRate
		return PppSessionRate(self)

	@property
	def PppoxRateCpf(self):
		"""An instance of the PppoxRateCpf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpf_3f1awnrvgvzdc9wchbvefjhdgvdcgy.PppoxRateCpf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpf_3f1awnrvgvzdc9wchbvefjhdgvdcgy import PppoxRateCpf
		return PppoxRateCpf(self)

	@property
	def PppoxRateCpfServerCapacity(self):
		"""An instance of the PppoxRateCpfServerCapacity class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpfservercapacity_efjhdgvdcgztzxj2zxjdyxbhy2l0eq.PppoxRateCpfServerCapacity)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpfservercapacity_efjhdgvdcgztzxj2zxjdyxbhy2l0eq import PppoxRateCpfServerCapacity
		return PppoxRateCpfServerCapacity(self)

	@property
	def PtpBestMasterSelection(self):
		"""An instance of the PtpBestMasterSelection class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection_9wdhbczxn0twfzdgvyu2vszwn0aw9u.PtpBestMasterSelection)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection_9wdhbczxn0twfzdgvyu2vszwn0aw9u import PtpBestMasterSelection
		return PtpBestMasterSelection(self)

	@property
	def PtpCorrectionFactorError(self):
		"""An instance of the PtpCorrectionFactorError class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror_hbdb3jyzwn0aw9urmfjdg9yrxjyb3i.PtpCorrectionFactorError)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror_hbdb3jyzwn0aw9urmfjdg9yrxjyb3i import PtpCorrectionFactorError
		return PtpCorrectionFactorError(self)

	@property
	def PtpSlaveScalability(self):
		"""An instance of the PtpSlaveScalability class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability_vzdc9wdhbtbgf2zvnjywxhymlsaxr5.PtpSlaveScalability)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability_vzdc9wdhbtbgf2zvnjywxhymlsaxr5 import PtpSlaveScalability
		return PtpSlaveScalability(self)

	@property
	def Rfc2544back2back(self):
		"""An instance of the Rfc2544back2back class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_nrvgvzdc9yzmmyntq0ymfjazjiywnr.Rfc2544back2back)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_nrvgvzdc9yzmmyntq0ymfjazjiywnr import Rfc2544back2back
		return Rfc2544back2back(self)

	@property
	def Rfc2544frameLoss(self):
		"""An instance of the Rfc2544frameLoss class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_nrvgvzdc9yzmmyntq0znjhbwvmb3nz.Rfc2544frameLoss)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_nrvgvzdc9yzmmyntq0znjhbwvmb3nz import Rfc2544frameLoss
		return Rfc2544frameLoss(self)

	@property
	def Rfc2544throughput(self):
		"""An instance of the Rfc2544throughput class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_vgvzdc9yzmmyntq0dghyb3vnahb1da.Rfc2544throughput)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_vgvzdc9yzmmyntq0dghyb3vnahb1da import Rfc2544throughput
		return Rfc2544throughput(self)

	@property
	def Rfc2889addressCache(self):
		"""An instance of the Rfc2889addressCache class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addresscache_vzdc9yzmmyodg5ywrkcmvzc0nhy2hl.Rfc2889addressCache)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addresscache_vzdc9yzmmyodg5ywrkcmvzc0nhy2hl import Rfc2889addressCache
		return Rfc2889addressCache(self)

	@property
	def Rfc2889addressRate(self):
		"""An instance of the Rfc2889addressRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addressrate_gvzdc9yzmmyodg5ywrkcmvzc1jhdgu.Rfc2889addressRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addressrate_gvzdc9yzmmyodg5ywrkcmvzc1jhdgu import Rfc2889addressRate
		return Rfc2889addressRate(self)

	@property
	def Rfc2889broadcastRate(self):
		"""An instance of the Rfc2889broadcastRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate_dc9yzmmyodg5ynjvywrjyxn0umf0zq.Rfc2889broadcastRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate_dc9yzmmyodg5ynjvywrjyxn0umf0zq import Rfc2889broadcastRate
		return Rfc2889broadcastRate(self)

	@property
	def Rfc2889congestionControl(self):
		"""An instance of the Rfc2889congestionControl class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol_mmyodg5y29uz2vzdglvbknvbnryb2w.Rfc2889congestionControl)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol_mmyodg5y29uz2vzdglvbknvbnryb2w import Rfc2889congestionControl
		return Rfc2889congestionControl(self)

	@property
	def Rfc2889frameErrorFiltering(self):
		"""An instance of the Rfc2889frameErrorFiltering class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering_odg5znjhbwvfcnjvckzpbhrlcmluzw.Rfc2889frameErrorFiltering)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering_odg5znjhbwvfcnjvckzpbhrlcmluzw import Rfc2889frameErrorFiltering
		return Rfc2889frameErrorFiltering(self)

	@property
	def Rfc2889fullyMeshed(self):
		"""An instance of the Rfc2889fullyMeshed class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889fullymeshed_gvzdc9yzmmyodg5znvsbhlnzxnozwq.Rfc2889fullyMeshed)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889fullymeshed_gvzdc9yzmmyodg5znvsbhlnzxnozwq import Rfc2889fullyMeshed
		return Rfc2889fullyMeshed(self)

	@property
	def Rfc2889manyToOne(self):
		"""An instance of the Rfc2889manyToOne class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889manytoone_nrvgvzdc9yzmmyodg5bwfuevrvt25l.Rfc2889manyToOne)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889manytoone_nrvgvzdc9yzmmyodg5bwfuevrvt25l import Rfc2889manyToOne
		return Rfc2889manyToOne(self)

	@property
	def Rfc2889oneToMany(self):
		"""An instance of the Rfc2889oneToMany class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889onetomany_nrvgvzdc9yzmmyodg5b25lvg9nyw55.Rfc2889oneToMany)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889onetomany_nrvgvzdc9yzmmyodg5b25lvg9nyw55 import Rfc2889oneToMany
		return Rfc2889oneToMany(self)

	@property
	def Rfc2889partiallyMeshed(self):
		"""An instance of the Rfc2889partiallyMeshed class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889partiallymeshed_9yzmmyodg5cgfydglhbgx5twvzagvk.Rfc2889partiallyMeshed)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889partiallymeshed_9yzmmyodg5cgfydglhbgx5twvzagvk import Rfc2889partiallyMeshed
		return Rfc2889partiallyMeshed(self)

	@property
	def Rfc3918aggregated(self):
		"""An instance of the Rfc3918aggregated class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918aggregated_vgvzdc9yzmmzote4ywdncmvnyxrlza.Rfc3918aggregated)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918aggregated_vgvzdc9yzmmzote4ywdncmvnyxrlza import Rfc3918aggregated
		return Rfc3918aggregated(self)

	@property
	def Rfc3918burdenedJoinDelay(self):
		"""An instance of the Rfc3918burdenedJoinDelay class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedjoindelay_mmzote4ynvyzgvuzwrkb2lurgvsyxk.Rfc3918burdenedJoinDelay)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedjoindelay_mmzote4ynvyzgvuzwrkb2lurgvsyxk import Rfc3918burdenedJoinDelay
		return Rfc3918burdenedJoinDelay(self)

	@property
	def Rfc3918burdenedLatency(self):
		"""An instance of the Rfc3918burdenedLatency class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedlatency_9yzmmzote4ynvyzgvuzwrmyxrlbmn5.Rfc3918burdenedLatency)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedlatency_9yzmmzote4ynvyzgvuzwrmyxrlbmn5 import Rfc3918burdenedLatency
		return Rfc3918burdenedLatency(self)

	@property
	def Rfc3918groupCapacity(self):
		"""An instance of the Rfc3918groupCapacity class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918groupcapacity_dc9yzmmzote4z3jvdxbdyxbhy2l0eq.Rfc3918groupCapacity)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918groupcapacity_dc9yzmmzote4z3jvdxbdyxbhy2l0eq import Rfc3918groupCapacity
		return Rfc3918groupCapacity(self)

	@property
	def Rfc3918groupPatternVerification(self):
		"""An instance of the Rfc3918groupPatternVerification class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918grouppatternverification_jvdxbqyxr0zxjuvmvyawzpy2f0aw9u.Rfc3918groupPatternVerification)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918grouppatternverification_jvdxbqyxr0zxjuvmvyawzpy2f0aw9u import Rfc3918groupPatternVerification
		return Rfc3918groupPatternVerification(self)

	@property
	def Rfc3918ipmcMinMaxLat(self):
		"""An instance of the Rfc3918ipmcMinMaxLat class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918ipmcminmaxlat_dc9yzmmzote4axbty01pbk1heexhda.Rfc3918ipmcMinMaxLat)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918ipmcminmaxlat_dc9yzmmzote4axbty01pbk1heexhda import Rfc3918ipmcMinMaxLat
		return Rfc3918ipmcMinMaxLat(self)

	@property
	def Rfc3918joinLeaveDelay(self):
		"""An instance of the Rfc3918joinLeaveDelay class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinleavedelay_c9yzmmzote4am9pbkxlyxzlrgvsyxk.Rfc3918joinLeaveDelay)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinleavedelay_c9yzmmzote4am9pbkxlyxzlrgvsyxk import Rfc3918joinLeaveDelay
		return Rfc3918joinLeaveDelay(self)

	@property
	def Rfc3918joinRate(self):
		"""An instance of the Rfc3918joinRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinrate_wnrvgvzdc9yzmmzote4am9pbljhdgu.Rfc3918joinRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinrate_wnrvgvzdc9yzmmzote4am9pbljhdgu import Rfc3918joinRate
		return Rfc3918joinRate(self)

	@property
	def Rfc3918mixedClassThroughput(self):
		"""An instance of the Rfc3918mixedClassThroughput class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918mixedclassthroughput_te4bwl4zwrdbgfzc1rocm91z2hwdxq.Rfc3918mixedClassThroughput)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918mixedclassthroughput_te4bwl4zwrdbgfzc1rocm91z2hwdxq import Rfc3918mixedClassThroughput
		return Rfc3918mixedClassThroughput(self)

	@property
	def Rfc3918scaleGroup(self):
		"""An instance of the Rfc3918scaleGroup class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918scalegroup_vgvzdc9yzmmzote4c2nhbgvhcm91ca.Rfc3918scaleGroup)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918scalegroup_vgvzdc9yzmmzote4c2nhbgvhcm91ca import Rfc3918scaleGroup
		return Rfc3918scaleGroup(self)

	@property
	def Rfc7747failover(self):
		"""An instance of the Rfc7747failover class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747failover_wnrvgvzdc9yzmm3nzq3zmfpbg92zxi.Rfc7747failover)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747failover_wnrvgvzdc9yzmm3nzq3zmfpbg92zxi import Rfc7747failover
		return Rfc7747failover(self)

	@property
	def Rfc7747ribIn(self):
		"""An instance of the Rfc7747ribIn class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747ribin_3f1awnrvgvzdc9yzmm3nzq3cmlisw4.Rfc7747ribIn)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747ribin_3f1awnrvgvzdc9yzmm3nzq3cmlisw4 import Rfc7747ribIn
		return Rfc7747ribIn(self)

	@property
	def TrafficTest(self):
		"""An instance of the TrafficTest class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_l3f1awnrvgvzdc90cmfmzmljvgvzda.TrafficTest)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_l3f1awnrvgvzdc90cmfmzmljvgvzda import TrafficTest
		return TrafficTest(self)

	@property
	def Y1564(self):
		"""An instance of the Y1564 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.y1564_l3f1awnrvgvzdc95mtu2na.Y1564)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.y1564_l3f1awnrvgvzdc95mtu2na import Y1564
		return Y1564(self)

	@property
	def RunningTest(self):
		"""Returns list containing the currently running QuickTest

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/quickTest?deepchild=*])
		"""
		return self._get_attribute('runningTest')

	@property
	def RunningTestObj(self):
		"""Returns list containing the currently running QuickTest

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/quickTest?deepchild=*])
		"""
		return self._get_attribute('runningTestObj')

	@property
	def TestIds(self):
		"""Returns list containing the QuickTest test in the configuration

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/quickTest?deepchild=*])
		"""
		return self._get_attribute('testIds')

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

	def LoadBatchFile(self, *args, **kwargs):
		"""Executes the loadBatchFile operation on the server.

		Loads the given batch file with all the results of the old quick test.

		loadBatchFile(Arg2:string)
			Args:
				args[0] is Arg2 (str): Exact path to the batch xml.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('loadBatchFile', payload=payload, response_object=None)

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
