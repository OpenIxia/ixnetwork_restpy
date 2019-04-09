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


class QuickTest(Base):
	"""The QuickTest class encapsulates a required quickTest node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the QuickTest property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'quickTest'

	def __init__(self, parent):
		super(QuickTest, self).__init__(parent)

	@property
	def AsymmetricFrameLoss(self):
		"""An instance of the AsymmetricFrameLoss class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss.asymmetricframeloss.AsymmetricFrameLoss)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss.asymmetricframeloss import AsymmetricFrameLoss
		return AsymmetricFrameLoss(self)

	@property
	def AsymmetricThroughput(self):
		"""An instance of the AsymmetricThroughput class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput.asymmetricthroughput.AsymmetricThroughput)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput.asymmetricthroughput import AsymmetricThroughput
		return AsymmetricThroughput(self)

	@property
	def CloudPerf(self):
		"""An instance of the CloudPerf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf.cloudperf.CloudPerf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf.cloudperf import CloudPerf
		return CloudPerf(self)

	@property
	def CustomContDuration(self):
		"""An instance of the CustomContDuration class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration.customcontduration.CustomContDuration)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration.customcontduration import CustomContDuration
		return CustomContDuration(self)

	@property
	def CustomFixedDuration(self):
		"""An instance of the CustomFixedDuration class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration.customfixedduration.CustomFixedDuration)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration.customfixedduration import CustomFixedDuration
		return CustomFixedDuration(self)

	@property
	def CustomStep(self):
		"""An instance of the CustomStep class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customstep.customstep.CustomStep)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customstep.customstep import CustomStep
		return CustomStep(self)

	@property
	def CustomThroughput(self):
		"""An instance of the CustomThroughput class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput.customthroughput.CustomThroughput)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput.customthroughput import CustomThroughput
		return CustomThroughput(self)

	@property
	def DhcpRate(self):
		"""An instance of the DhcpRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate.dhcprate.DhcpRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate.dhcprate import DhcpRate
		return DhcpRate(self)

	@property
	def DhcpRateCpf(self):
		"""An instance of the DhcpRateCpf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpratecpf.dhcpratecpf.DhcpRateCpf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpratecpf.dhcpratecpf import DhcpRateCpf
		return DhcpRateCpf(self)

	@property
	def Dhcpv6Rate(self):
		"""An instance of the Dhcpv6Rate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate.dhcpv6rate.Dhcpv6Rate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate.dhcpv6rate import Dhcpv6Rate
		return Dhcpv6Rate(self)

	@property
	def Dhcpv6RateCpf(self):
		"""An instance of the Dhcpv6RateCpf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6ratecpf.dhcpv6ratecpf.Dhcpv6RateCpf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6ratecpf.dhcpv6ratecpf import Dhcpv6RateCpf
		return Dhcpv6RateCpf(self)

	@property
	def Dot1xCapacity(self):
		"""An instance of the Dot1xCapacity class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity.dot1xcapacity.Dot1xCapacity)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity.dot1xcapacity import Dot1xCapacity
		return Dot1xCapacity(self)

	@property
	def Dot1xRate(self):
		"""An instance of the Dot1xRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate.dot1xrate.Dot1xRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate.dot1xrate import Dot1xRate
		return Dot1xRate(self)

	@property
	def EventScheduler(self):
		"""An instance of the EventScheduler class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler.eventscheduler.EventScheduler)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler.eventscheduler import EventScheduler
		return EventScheduler(self)

	@property
	def FcoeMaxNoDropThroughput(self):
		"""An instance of the FcoeMaxNoDropThroughput class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput.fcoemaxnodropthroughput.FcoeMaxNoDropThroughput)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput.fcoemaxnodropthroughput import FcoeMaxNoDropThroughput
		return FcoeMaxNoDropThroughput(self)

	@property
	def FcoeMaxNoPauseThroughput(self):
		"""An instance of the FcoeMaxNoPauseThroughput class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput.fcoemaxnopausethroughput.FcoeMaxNoPauseThroughput)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput.fcoemaxnopausethroughput import FcoeMaxNoPauseThroughput
		return FcoeMaxNoPauseThroughput(self)

	@property
	def Globals(self):
		"""An instance of the Globals class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.globals.globals.Globals)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.globals.globals import Globals
		return Globals(self)._select()

	@property
	def IptvChannelZapping(self):
		"""An instance of the IptvChannelZapping class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping.iptvchannelzapping.IptvChannelZapping)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping.iptvchannelzapping import IptvChannelZapping
		return IptvChannelZapping(self)

	@property
	def L2tpCapacity(self):
		"""An instance of the L2tpCapacity class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpcapacity.l2tpcapacity.L2tpCapacity)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpcapacity.l2tpcapacity import L2tpCapacity
		return L2tpCapacity(self)

	@property
	def L2tpRate(self):
		"""An instance of the L2tpRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate.l2tprate.L2tpRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate.l2tprate import L2tpRate
		return L2tpRate(self)

	@property
	def L2tpRateCpf(self):
		"""An instance of the L2tpRateCpf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpratecpf.l2tpratecpf.L2tpRateCpf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpratecpf.l2tpratecpf import L2tpRateCpf
		return L2tpRateCpf(self)

	@property
	def OpenFlowFailoverPerformance(self):
		"""An instance of the OpenFlowFailoverPerformance class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance.openflowfailoverperformance.OpenFlowFailoverPerformance)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance.openflowfailoverperformance import OpenFlowFailoverPerformance
		return OpenFlowFailoverPerformance(self)

	@property
	def OpenFlowLayer2LearningRate(self):
		"""An instance of the OpenFlowLayer2LearningRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate.openflowlayer2learningrate.OpenFlowLayer2LearningRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate.openflowlayer2learningrate import OpenFlowLayer2LearningRate
		return OpenFlowLayer2LearningRate(self)

	@property
	def OpenFlowLayer3LearningRate(self):
		"""An instance of the OpenFlowLayer3LearningRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate.openflowlayer3learningrate.OpenFlowLayer3LearningRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate.openflowlayer3learningrate import OpenFlowLayer3LearningRate
		return OpenFlowLayer3LearningRate(self)

	@property
	def OpenFlowTableCapacity(self):
		"""An instance of the OpenFlowTableCapacity class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity.openflowtablecapacity.OpenFlowTableCapacity)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity.openflowtablecapacity import OpenFlowTableCapacity
		return OpenFlowTableCapacity(self)

	@property
	def PppServerCapacity(self):
		"""An instance of the PppServerCapacity class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity.pppservercapacity.PppServerCapacity)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity.pppservercapacity import PppServerCapacity
		return PppServerCapacity(self)

	@property
	def PppSessionRate(self):
		"""An instance of the PppSessionRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate.pppsessionrate.PppSessionRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate.pppsessionrate import PppSessionRate
		return PppSessionRate(self)

	@property
	def PppoxRateCpf(self):
		"""An instance of the PppoxRateCpf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpf.pppoxratecpf.PppoxRateCpf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpf.pppoxratecpf import PppoxRateCpf
		return PppoxRateCpf(self)

	@property
	def PtpBestMasterSelection(self):
		"""An instance of the PtpBestMasterSelection class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection.ptpbestmasterselection.PtpBestMasterSelection)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection.ptpbestmasterselection import PtpBestMasterSelection
		return PtpBestMasterSelection(self)

	@property
	def PtpCorrectionFactorError(self):
		"""An instance of the PtpCorrectionFactorError class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror.ptpcorrectionfactorerror.PtpCorrectionFactorError)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror.ptpcorrectionfactorerror import PtpCorrectionFactorError
		return PtpCorrectionFactorError(self)

	@property
	def PtpSlaveScalability(self):
		"""An instance of the PtpSlaveScalability class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability.ptpslavescalability.PtpSlaveScalability)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability.ptpslavescalability import PtpSlaveScalability
		return PtpSlaveScalability(self)

	@property
	def Rfc2544back2back(self):
		"""An instance of the Rfc2544back2back class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back.rfc2544back2back.Rfc2544back2back)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back.rfc2544back2back import Rfc2544back2back
		return Rfc2544back2back(self)

	@property
	def Rfc2544frameLoss(self):
		"""An instance of the Rfc2544frameLoss class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss.rfc2544frameloss.Rfc2544frameLoss)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss.rfc2544frameloss import Rfc2544frameLoss
		return Rfc2544frameLoss(self)

	@property
	def Rfc2544throughput(self):
		"""An instance of the Rfc2544throughput class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput.rfc2544throughput.Rfc2544throughput)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput.rfc2544throughput import Rfc2544throughput
		return Rfc2544throughput(self)

	@property
	def Rfc2889addressCache(self):
		"""An instance of the Rfc2889addressCache class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addresscache.rfc2889addresscache.Rfc2889addressCache)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addresscache.rfc2889addresscache import Rfc2889addressCache
		return Rfc2889addressCache(self)

	@property
	def Rfc2889addressRate(self):
		"""An instance of the Rfc2889addressRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addressrate.rfc2889addressrate.Rfc2889addressRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addressrate.rfc2889addressrate import Rfc2889addressRate
		return Rfc2889addressRate(self)

	@property
	def Rfc2889broadcastRate(self):
		"""An instance of the Rfc2889broadcastRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate.rfc2889broadcastrate.Rfc2889broadcastRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate.rfc2889broadcastrate import Rfc2889broadcastRate
		return Rfc2889broadcastRate(self)

	@property
	def Rfc2889congestionControl(self):
		"""An instance of the Rfc2889congestionControl class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol.rfc2889congestioncontrol.Rfc2889congestionControl)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol.rfc2889congestioncontrol import Rfc2889congestionControl
		return Rfc2889congestionControl(self)

	@property
	def Rfc2889frameErrorFiltering(self):
		"""An instance of the Rfc2889frameErrorFiltering class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering.rfc2889frameerrorfiltering.Rfc2889frameErrorFiltering)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering.rfc2889frameerrorfiltering import Rfc2889frameErrorFiltering
		return Rfc2889frameErrorFiltering(self)

	@property
	def Rfc2889fullyMeshed(self):
		"""An instance of the Rfc2889fullyMeshed class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889fullymeshed.rfc2889fullymeshed.Rfc2889fullyMeshed)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889fullymeshed.rfc2889fullymeshed import Rfc2889fullyMeshed
		return Rfc2889fullyMeshed(self)

	@property
	def Rfc2889manyToOne(self):
		"""An instance of the Rfc2889manyToOne class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889manytoone.rfc2889manytoone.Rfc2889manyToOne)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889manytoone.rfc2889manytoone import Rfc2889manyToOne
		return Rfc2889manyToOne(self)

	@property
	def Rfc2889oneToMany(self):
		"""An instance of the Rfc2889oneToMany class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889onetomany.rfc2889onetomany.Rfc2889oneToMany)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889onetomany.rfc2889onetomany import Rfc2889oneToMany
		return Rfc2889oneToMany(self)

	@property
	def Rfc2889partiallyMeshed(self):
		"""An instance of the Rfc2889partiallyMeshed class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889partiallymeshed.rfc2889partiallymeshed.Rfc2889partiallyMeshed)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889partiallymeshed.rfc2889partiallymeshed import Rfc2889partiallyMeshed
		return Rfc2889partiallyMeshed(self)

	@property
	def Rfc3918aggregated(self):
		"""An instance of the Rfc3918aggregated class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918aggregated.rfc3918aggregated.Rfc3918aggregated)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918aggregated.rfc3918aggregated import Rfc3918aggregated
		return Rfc3918aggregated(self)

	@property
	def Rfc3918burdenedJoinDelay(self):
		"""An instance of the Rfc3918burdenedJoinDelay class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedjoindelay.rfc3918burdenedjoindelay.Rfc3918burdenedJoinDelay)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedjoindelay.rfc3918burdenedjoindelay import Rfc3918burdenedJoinDelay
		return Rfc3918burdenedJoinDelay(self)

	@property
	def Rfc3918burdenedLatency(self):
		"""An instance of the Rfc3918burdenedLatency class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedlatency.rfc3918burdenedlatency.Rfc3918burdenedLatency)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedlatency.rfc3918burdenedlatency import Rfc3918burdenedLatency
		return Rfc3918burdenedLatency(self)

	@property
	def Rfc3918groupCapacity(self):
		"""An instance of the Rfc3918groupCapacity class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918groupcapacity.rfc3918groupcapacity.Rfc3918groupCapacity)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918groupcapacity.rfc3918groupcapacity import Rfc3918groupCapacity
		return Rfc3918groupCapacity(self)

	@property
	def Rfc3918groupPatternVerification(self):
		"""An instance of the Rfc3918groupPatternVerification class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918grouppatternverification.rfc3918grouppatternverification.Rfc3918groupPatternVerification)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918grouppatternverification.rfc3918grouppatternverification import Rfc3918groupPatternVerification
		return Rfc3918groupPatternVerification(self)

	@property
	def Rfc3918ipmcMinMaxLat(self):
		"""An instance of the Rfc3918ipmcMinMaxLat class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918ipmcminmaxlat.rfc3918ipmcminmaxlat.Rfc3918ipmcMinMaxLat)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918ipmcminmaxlat.rfc3918ipmcminmaxlat import Rfc3918ipmcMinMaxLat
		return Rfc3918ipmcMinMaxLat(self)

	@property
	def Rfc3918joinLeaveDelay(self):
		"""An instance of the Rfc3918joinLeaveDelay class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinleavedelay.rfc3918joinleavedelay.Rfc3918joinLeaveDelay)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinleavedelay.rfc3918joinleavedelay import Rfc3918joinLeaveDelay
		return Rfc3918joinLeaveDelay(self)

	@property
	def Rfc3918joinRate(self):
		"""An instance of the Rfc3918joinRate class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinrate.rfc3918joinrate.Rfc3918joinRate)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinrate.rfc3918joinrate import Rfc3918joinRate
		return Rfc3918joinRate(self)

	@property
	def Rfc3918mixedClassThroughput(self):
		"""An instance of the Rfc3918mixedClassThroughput class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918mixedclassthroughput.rfc3918mixedclassthroughput.Rfc3918mixedClassThroughput)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918mixedclassthroughput.rfc3918mixedclassthroughput import Rfc3918mixedClassThroughput
		return Rfc3918mixedClassThroughput(self)

	@property
	def Rfc3918scaleGroup(self):
		"""An instance of the Rfc3918scaleGroup class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918scalegroup.rfc3918scalegroup.Rfc3918scaleGroup)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918scalegroup.rfc3918scalegroup import Rfc3918scaleGroup
		return Rfc3918scaleGroup(self)

	@property
	def Rfc7747failover(self):
		"""An instance of the Rfc7747failover class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747failover.rfc7747failover.Rfc7747failover)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747failover.rfc7747failover import Rfc7747failover
		return Rfc7747failover(self)

	@property
	def Rfc7747ribIn(self):
		"""An instance of the Rfc7747ribIn class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747ribin.rfc7747ribin.Rfc7747ribIn)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747ribin.rfc7747ribin import Rfc7747ribIn
		return Rfc7747ribIn(self)

	@property
	def TrafficTest(self):
		"""An instance of the TrafficTest class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest.traffictest.TrafficTest)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest.traffictest import TrafficTest
		return TrafficTest(self)

	@property
	def Y1564(self):
		"""An instance of the Y1564 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.y1564.y1564.Y1564)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.y1564.y1564 import Y1564
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
