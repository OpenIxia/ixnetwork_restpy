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


class QuickTest(Base):
    """The IxNetwork QuickTests feature provides the ability to run predefined tests.
    The QuickTest class encapsulates a required quickTest resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'quickTest'
    _SDM_ATT_MAP = {
        'RunningTest': 'runningTest',
        'RunningTestObj': 'runningTestObj',
        'TestIds': 'testIds',
    }

    def __init__(self, parent):
        super(QuickTest, self).__init__(parent)

    @property
    def AsymmetricFrameLoss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss_23e9ec9c789cfca78365ee935c3c3488.AsymmetricFrameLoss): An instance of the AsymmetricFrameLoss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss_23e9ec9c789cfca78365ee935c3c3488 import AsymmetricFrameLoss
        return AsymmetricFrameLoss(self)

    @property
    def AsymmetricThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput_b9e3c6717e2faf761c693cccff9c71b8.AsymmetricThroughput): An instance of the AsymmetricThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput_b9e3c6717e2faf761c693cccff9c71b8 import AsymmetricThroughput
        return AsymmetricThroughput(self)

    @property
    def CloudPerf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf_354bfb3429a11911999c2a796c4a9c1c.CloudPerf): An instance of the CloudPerf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf_354bfb3429a11911999c2a796c4a9c1c import CloudPerf
        return CloudPerf(self)

    @property
    def CustomContDuration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration_afd0ec7957951071cbe4070215782b68.CustomContDuration): An instance of the CustomContDuration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration_afd0ec7957951071cbe4070215782b68 import CustomContDuration
        return CustomContDuration(self)

    @property
    def CustomFixedDuration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration_9a6f20f065966a060e70d9d3098af43b.CustomFixedDuration): An instance of the CustomFixedDuration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration_9a6f20f065966a060e70d9d3098af43b import CustomFixedDuration
        return CustomFixedDuration(self)

    @property
    def CustomStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customstep_2a6f0cec52fe41c2c67188afbd8bdcdc.CustomStep): An instance of the CustomStep class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customstep_2a6f0cec52fe41c2c67188afbd8bdcdc import CustomStep
        return CustomStep(self)

    @property
    def CustomThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput_97500fff3f335c6329b02f39f0ad94f4.CustomThroughput): An instance of the CustomThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput_97500fff3f335c6329b02f39f0ad94f4 import CustomThroughput
        return CustomThroughput(self)

    @property
    def DhcpRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate_a1d50c13e49087adee284d9705f20ea9.DhcpRate): An instance of the DhcpRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate_a1d50c13e49087adee284d9705f20ea9 import DhcpRate
        return DhcpRate(self)

    @property
    def DhcpRateCpf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpratecpf_f2ec20ecf18a5a7ea658bd69e6b32386.DhcpRateCpf): An instance of the DhcpRateCpf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpratecpf_f2ec20ecf18a5a7ea658bd69e6b32386 import DhcpRateCpf
        return DhcpRateCpf(self)

    @property
    def Dhcpv6Rate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate_17ca1fc0e1ab7156c518d207263c2755.Dhcpv6Rate): An instance of the Dhcpv6Rate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate_17ca1fc0e1ab7156c518d207263c2755 import Dhcpv6Rate
        return Dhcpv6Rate(self)

    @property
    def Dhcpv6RateCpf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6ratecpf_a6372f0ad4d75b8c25e8d9160a42a12c.Dhcpv6RateCpf): An instance of the Dhcpv6RateCpf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6ratecpf_a6372f0ad4d75b8c25e8d9160a42a12c import Dhcpv6RateCpf
        return Dhcpv6RateCpf(self)

    @property
    def Dot1xCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity_ddddaeb52f72ebee3e8c89bb27e5a9bd.Dot1xCapacity): An instance of the Dot1xCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity_ddddaeb52f72ebee3e8c89bb27e5a9bd import Dot1xCapacity
        return Dot1xCapacity(self)

    @property
    def Dot1xRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate_920cbb0c4f9de176a44b8d1eec6d1654.Dot1xRate): An instance of the Dot1xRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate_920cbb0c4f9de176a44b8d1eec6d1654 import Dot1xRate
        return Dot1xRate(self)

    @property
    def EventScheduler(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler_1adeddd0d2588a7b6a2bb0dfa0dbbbd5.EventScheduler): An instance of the EventScheduler class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler_1adeddd0d2588a7b6a2bb0dfa0dbbbd5 import EventScheduler
        return EventScheduler(self)

    @property
    def FcoeMaxNoDropThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput_5a8b5a2dd7200e911f9e2cc4e02d9cdf.FcoeMaxNoDropThroughput): An instance of the FcoeMaxNoDropThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput_5a8b5a2dd7200e911f9e2cc4e02d9cdf import FcoeMaxNoDropThroughput
        return FcoeMaxNoDropThroughput(self)

    @property
    def FcoeMaxNoPauseThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput_5c5bcb306f8c2ea47dbeb4bd93f05b4a.FcoeMaxNoPauseThroughput): An instance of the FcoeMaxNoPauseThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput_5c5bcb306f8c2ea47dbeb4bd93f05b4a import FcoeMaxNoPauseThroughput
        return FcoeMaxNoPauseThroughput(self)

    @property
    def Globals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.globals_189e36988976210137e69f36458134c2.Globals): An instance of the Globals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.globals_189e36988976210137e69f36458134c2 import Globals
        return Globals(self)._select()

    @property
    def IptvChannelZapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping_f76f09e6cca53cc063af4a62acaad345.IptvChannelZapping): An instance of the IptvChannelZapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping_f76f09e6cca53cc063af4a62acaad345 import IptvChannelZapping
        return IptvChannelZapping(self)

    @property
    def L2tpCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpcapacity_1fb03b1eecddd532c02195eaf76667b2.L2tpCapacity): An instance of the L2tpCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpcapacity_1fb03b1eecddd532c02195eaf76667b2 import L2tpCapacity
        return L2tpCapacity(self)

    @property
    def L2tpRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate_3f836413e8c133cd9b3153b0ece79355.L2tpRate): An instance of the L2tpRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate_3f836413e8c133cd9b3153b0ece79355 import L2tpRate
        return L2tpRate(self)

    @property
    def L2tpRateCpf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpratecpf_f677e702e077f88c48d42e24b1069b88.L2tpRateCpf): An instance of the L2tpRateCpf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpratecpf_f677e702e077f88c48d42e24b1069b88 import L2tpRateCpf
        return L2tpRateCpf(self)

    @property
    def LnsCpfCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.lnscpfcapacity_8fb5a4abc39bee4e5a1614e2cd11f829.LnsCpfCapacity): An instance of the LnsCpfCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.lnscpfcapacity_8fb5a4abc39bee4e5a1614e2cd11f829 import LnsCpfCapacity
        return LnsCpfCapacity(self)

    @property
    def OpenFlowFailoverPerformance(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance_497acfbd872605986ec31fac8a22909e.OpenFlowFailoverPerformance): An instance of the OpenFlowFailoverPerformance class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance_497acfbd872605986ec31fac8a22909e import OpenFlowFailoverPerformance
        return OpenFlowFailoverPerformance(self)

    @property
    def OpenFlowLayer2LearningRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate_3db88746f7f375303f2eda376386a9a8.OpenFlowLayer2LearningRate): An instance of the OpenFlowLayer2LearningRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate_3db88746f7f375303f2eda376386a9a8 import OpenFlowLayer2LearningRate
        return OpenFlowLayer2LearningRate(self)

    @property
    def OpenFlowLayer3LearningRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate_3d5fc2ac25caa8bc279f7dd74cb1ebb4.OpenFlowLayer3LearningRate): An instance of the OpenFlowLayer3LearningRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate_3d5fc2ac25caa8bc279f7dd74cb1ebb4 import OpenFlowLayer3LearningRate
        return OpenFlowLayer3LearningRate(self)

    @property
    def OpenFlowTableCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity_ede63934d6923146dc0eff0fec6a3023.OpenFlowTableCapacity): An instance of the OpenFlowTableCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity_ede63934d6923146dc0eff0fec6a3023 import OpenFlowTableCapacity
        return OpenFlowTableCapacity(self)

    @property
    def PppServerCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity_af2ef3e74eab82cea91b425ee7119872.PppServerCapacity): An instance of the PppServerCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity_af2ef3e74eab82cea91b425ee7119872 import PppServerCapacity
        return PppServerCapacity(self)

    @property
    def PppSessionRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate_3c902892c18a09c0398be23c0a97ef85.PppSessionRate): An instance of the PppSessionRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate_3c902892c18a09c0398be23c0a97ef85 import PppSessionRate
        return PppSessionRate(self)

    @property
    def PppoxRateCpf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpf_9c440412a274245098fbcd041905e457.PppoxRateCpf): An instance of the PppoxRateCpf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpf_9c440412a274245098fbcd041905e457 import PppoxRateCpf
        return PppoxRateCpf(self)

    @property
    def PppoxRateCpfServerCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpfservercapacity_2543f7ecee1fc35f208601e89cbb5723.PppoxRateCpfServerCapacity): An instance of the PppoxRateCpfServerCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpfservercapacity_2543f7ecee1fc35f208601e89cbb5723 import PppoxRateCpfServerCapacity
        return PppoxRateCpfServerCapacity(self)

    @property
    def PtpBestMasterSelection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection_bd6cd77082c14a379f852945024f02c5.PtpBestMasterSelection): An instance of the PtpBestMasterSelection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection_bd6cd77082c14a379f852945024f02c5 import PtpBestMasterSelection
        return PtpBestMasterSelection(self)

    @property
    def PtpCorrectionFactorError(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror_6ee1b2ad82283aaeee35905a0a1ed5dc.PtpCorrectionFactorError): An instance of the PtpCorrectionFactorError class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror_6ee1b2ad82283aaeee35905a0a1ed5dc import PtpCorrectionFactorError
        return PtpCorrectionFactorError(self)

    @property
    def PtpSlaveScalability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability_6510fa33eea238d2b2963267efeca729.PtpSlaveScalability): An instance of the PtpSlaveScalability class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability_6510fa33eea238d2b2963267efeca729 import PtpSlaveScalability
        return PtpSlaveScalability(self)

    @property
    def Rfc2544back2back(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_98477f12f665b89fbc05f63bb31ee827.Rfc2544back2back): An instance of the Rfc2544back2back class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_98477f12f665b89fbc05f63bb31ee827 import Rfc2544back2back
        return Rfc2544back2back(self)

    @property
    def Rfc2544frameLoss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_f6a794f7d6a00f8572021fc418d8807f.Rfc2544frameLoss): An instance of the Rfc2544frameLoss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_f6a794f7d6a00f8572021fc418d8807f import Rfc2544frameLoss
        return Rfc2544frameLoss(self)

    @property
    def Rfc2544throughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_5a77c9a28f5fa2bb9ce9f4280eb5122f.Rfc2544throughput): An instance of the Rfc2544throughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_5a77c9a28f5fa2bb9ce9f4280eb5122f import Rfc2544throughput
        return Rfc2544throughput(self)

    @property
    def Rfc2889addressCache(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addresscache_21525f74b3881751df0d47bcbc1beb2e.Rfc2889addressCache): An instance of the Rfc2889addressCache class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addresscache_21525f74b3881751df0d47bcbc1beb2e import Rfc2889addressCache
        return Rfc2889addressCache(self)

    @property
    def Rfc2889addressRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addressrate_9f13a82b67c65f0e111d2fcb2631abe1.Rfc2889addressRate): An instance of the Rfc2889addressRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addressrate_9f13a82b67c65f0e111d2fcb2631abe1 import Rfc2889addressRate
        return Rfc2889addressRate(self)

    @property
    def Rfc2889broadcastRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate_1309c81b5bb27d5345ac1823c48958d6.Rfc2889broadcastRate): An instance of the Rfc2889broadcastRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate_1309c81b5bb27d5345ac1823c48958d6 import Rfc2889broadcastRate
        return Rfc2889broadcastRate(self)

    @property
    def Rfc2889congestionControl(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol_2e3ba8b814e3177aeefdef4c3ba3957f.Rfc2889congestionControl): An instance of the Rfc2889congestionControl class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol_2e3ba8b814e3177aeefdef4c3ba3957f import Rfc2889congestionControl
        return Rfc2889congestionControl(self)

    @property
    def Rfc2889frameErrorFiltering(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering_bbdf8e68236e7582480e73591a3c427f.Rfc2889frameErrorFiltering): An instance of the Rfc2889frameErrorFiltering class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering_bbdf8e68236e7582480e73591a3c427f import Rfc2889frameErrorFiltering
        return Rfc2889frameErrorFiltering(self)

    @property
    def Rfc2889fullyMeshed(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889fullymeshed_6b4738418bba0afb6d50903264b20d3e.Rfc2889fullyMeshed): An instance of the Rfc2889fullyMeshed class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889fullymeshed_6b4738418bba0afb6d50903264b20d3e import Rfc2889fullyMeshed
        return Rfc2889fullyMeshed(self)

    @property
    def Rfc2889manyToOne(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889manytoone_c944e4a05240f0719e24167b12d02a98.Rfc2889manyToOne): An instance of the Rfc2889manyToOne class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889manytoone_c944e4a05240f0719e24167b12d02a98 import Rfc2889manyToOne
        return Rfc2889manyToOne(self)

    @property
    def Rfc2889oneToMany(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889onetomany_0e5e7ff0c5e75af7273d70a7c2890118.Rfc2889oneToMany): An instance of the Rfc2889oneToMany class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889onetomany_0e5e7ff0c5e75af7273d70a7c2890118 import Rfc2889oneToMany
        return Rfc2889oneToMany(self)

    @property
    def Rfc2889partiallyMeshed(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889partiallymeshed_acbb762bb3ca6f755f638364672edd6c.Rfc2889partiallyMeshed): An instance of the Rfc2889partiallyMeshed class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889partiallymeshed_acbb762bb3ca6f755f638364672edd6c import Rfc2889partiallyMeshed
        return Rfc2889partiallyMeshed(self)

    @property
    def Rfc3918aggregated(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918aggregated_d2c8b1ad0eedb9c640edd885fc04ed87.Rfc3918aggregated): An instance of the Rfc3918aggregated class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918aggregated_d2c8b1ad0eedb9c640edd885fc04ed87 import Rfc3918aggregated
        return Rfc3918aggregated(self)

    @property
    def Rfc3918burdenedJoinDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedjoindelay_3d43a60cbda9472f021931c9c5a95f2f.Rfc3918burdenedJoinDelay): An instance of the Rfc3918burdenedJoinDelay class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedjoindelay_3d43a60cbda9472f021931c9c5a95f2f import Rfc3918burdenedJoinDelay
        return Rfc3918burdenedJoinDelay(self)

    @property
    def Rfc3918burdenedLatency(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedlatency_7d3d3be2db0c111bf4cf27d8f5998b7b.Rfc3918burdenedLatency): An instance of the Rfc3918burdenedLatency class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedlatency_7d3d3be2db0c111bf4cf27d8f5998b7b import Rfc3918burdenedLatency
        return Rfc3918burdenedLatency(self)

    @property
    def Rfc3918groupCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918groupcapacity_d11cfab77e3f338d5bbc1d1600495aae.Rfc3918groupCapacity): An instance of the Rfc3918groupCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918groupcapacity_d11cfab77e3f338d5bbc1d1600495aae import Rfc3918groupCapacity
        return Rfc3918groupCapacity(self)

    @property
    def Rfc3918groupPatternVerification(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918grouppatternverification_12de5f4348bcd491f41072583d58e4ee.Rfc3918groupPatternVerification): An instance of the Rfc3918groupPatternVerification class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918grouppatternverification_12de5f4348bcd491f41072583d58e4ee import Rfc3918groupPatternVerification
        return Rfc3918groupPatternVerification(self)

    @property
    def Rfc3918ipmcMinMaxLat(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918ipmcminmaxlat_2b4a5abe7dfed10705b6843a3c52969c.Rfc3918ipmcMinMaxLat): An instance of the Rfc3918ipmcMinMaxLat class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918ipmcminmaxlat_2b4a5abe7dfed10705b6843a3c52969c import Rfc3918ipmcMinMaxLat
        return Rfc3918ipmcMinMaxLat(self)

    @property
    def Rfc3918joinLeaveDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinleavedelay_74928f8eedbb05504506d4fa05a16ba9.Rfc3918joinLeaveDelay): An instance of the Rfc3918joinLeaveDelay class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinleavedelay_74928f8eedbb05504506d4fa05a16ba9 import Rfc3918joinLeaveDelay
        return Rfc3918joinLeaveDelay(self)

    @property
    def Rfc3918joinRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinrate_3be605d66c1ba720bb00e9fd8b4a635a.Rfc3918joinRate): An instance of the Rfc3918joinRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinrate_3be605d66c1ba720bb00e9fd8b4a635a import Rfc3918joinRate
        return Rfc3918joinRate(self)

    @property
    def Rfc3918mixedClassThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918mixedclassthroughput_51b11be7da6751ca02f81e065657f970.Rfc3918mixedClassThroughput): An instance of the Rfc3918mixedClassThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918mixedclassthroughput_51b11be7da6751ca02f81e065657f970 import Rfc3918mixedClassThroughput
        return Rfc3918mixedClassThroughput(self)

    @property
    def Rfc3918scaleGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918scalegroup_456c7d718fcfe586814e14bf2501b3f0.Rfc3918scaleGroup): An instance of the Rfc3918scaleGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918scalegroup_456c7d718fcfe586814e14bf2501b3f0 import Rfc3918scaleGroup
        return Rfc3918scaleGroup(self)

    @property
    def Rfc7747failover(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747failover_c36c9eac10b2d8bc7d431cc07b17de0f.Rfc7747failover): An instance of the Rfc7747failover class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747failover_c36c9eac10b2d8bc7d431cc07b17de0f import Rfc7747failover
        return Rfc7747failover(self)

    @property
    def Rfc7747ribIn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747ribin_6acd728bf004a993f981fcb33fb3c735.Rfc7747ribIn): An instance of the Rfc7747ribIn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747ribin_6acd728bf004a993f981fcb33fb3c735 import Rfc7747ribIn
        return Rfc7747ribIn(self)

    @property
    def TrafficTest(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_9709f3566877e5d5fb6ae115268058c6.TrafficTest): An instance of the TrafficTest class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_9709f3566877e5d5fb6ae115268058c6 import TrafficTest
        return TrafficTest(self)

    @property
    def Y1564(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.y1564_6674f9c7023c1667145343e451a0128c.Y1564): An instance of the Y1564 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.y1564_6674f9c7023c1667145343e451a0128c import Y1564
        return Y1564(self)

    @property
    def RunningTest(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../*]): Returns list containing the currently running QuickTest
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningTest'])

    @property
    def RunningTestObj(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../*]): Returns list containing the currently running QuickTest
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningTestObj'])

    @property
    def TestIds(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../*]): Returns list containing the QuickTest test in the configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestIds'])

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

    def LoadBatchFile(self, *args, **kwargs):
        """Executes the loadBatchFile operation on the server.

        Loads the given batch file with all the results of the old quick test.

        loadBatchFile(Arg2=string)
        --------------------------
        - Arg2 (str): Exact path to the batch xml.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('loadBatchFile', payload=payload, response_object=None)

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
