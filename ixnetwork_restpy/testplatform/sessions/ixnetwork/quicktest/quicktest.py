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
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss_2f10c18995084860a7994c6935aef033.AsymmetricFrameLoss): An instance of the AsymmetricFrameLoss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss_2f10c18995084860a7994c6935aef033 import AsymmetricFrameLoss
        return AsymmetricFrameLoss(self)

    @property
    def AsymmetricThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput_5f60c944befbee0ea93fb2b4a142281d.AsymmetricThroughput): An instance of the AsymmetricThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput_5f60c944befbee0ea93fb2b4a142281d import AsymmetricThroughput
        return AsymmetricThroughput(self)

    @property
    def CloudPerf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf_f2434025209793f1c981502d88c07b03.CloudPerf): An instance of the CloudPerf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf_f2434025209793f1c981502d88c07b03 import CloudPerf
        return CloudPerf(self)

    @property
    def CustomContDuration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration_dd6b2aad1f18237c8cf967e3bbf4317e.CustomContDuration): An instance of the CustomContDuration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration_dd6b2aad1f18237c8cf967e3bbf4317e import CustomContDuration
        return CustomContDuration(self)

    @property
    def CustomFixedDuration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration_ecf6815289fc18c909b8be469aaaf69e.CustomFixedDuration): An instance of the CustomFixedDuration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration_ecf6815289fc18c909b8be469aaaf69e import CustomFixedDuration
        return CustomFixedDuration(self)

    @property
    def CustomStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customstep_0bbe57722cdfb4a3e668e10f8d102dca.CustomStep): An instance of the CustomStep class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customstep_0bbe57722cdfb4a3e668e10f8d102dca import CustomStep
        return CustomStep(self)

    @property
    def CustomThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput_7af59ea4d4e41b516489842a17d15ec5.CustomThroughput): An instance of the CustomThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput_7af59ea4d4e41b516489842a17d15ec5 import CustomThroughput
        return CustomThroughput(self)

    @property
    def DhcpRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate_f1626ae851cac0d25ce7162e05dbe765.DhcpRate): An instance of the DhcpRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate_f1626ae851cac0d25ce7162e05dbe765 import DhcpRate
        return DhcpRate(self)

    @property
    def DhcpRateCpf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpratecpf_fe98596686a1b876c85bd194b5ba98c7.DhcpRateCpf): An instance of the DhcpRateCpf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpratecpf_fe98596686a1b876c85bd194b5ba98c7 import DhcpRateCpf
        return DhcpRateCpf(self)

    @property
    def Dhcpv6Rate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate_3df3cc8acb6f1bcfe8689a869ffbc2b5.Dhcpv6Rate): An instance of the Dhcpv6Rate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate_3df3cc8acb6f1bcfe8689a869ffbc2b5 import Dhcpv6Rate
        return Dhcpv6Rate(self)

    @property
    def Dhcpv6RateCpf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6ratecpf_2661dd0eb3355ca8a43152df2ca37c20.Dhcpv6RateCpf): An instance of the Dhcpv6RateCpf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6ratecpf_2661dd0eb3355ca8a43152df2ca37c20 import Dhcpv6RateCpf
        return Dhcpv6RateCpf(self)

    @property
    def Dot1xCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity_8f1c82679815437b5e5727b98da27544.Dot1xCapacity): An instance of the Dot1xCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity_8f1c82679815437b5e5727b98da27544 import Dot1xCapacity
        return Dot1xCapacity(self)

    @property
    def Dot1xRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate_fc6bcf7af2a1651e8801c10e2ed4cff0.Dot1xRate): An instance of the Dot1xRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate_fc6bcf7af2a1651e8801c10e2ed4cff0 import Dot1xRate
        return Dot1xRate(self)

    @property
    def EventScheduler(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler_219594c0625599eb47a5906e96ce202b.EventScheduler): An instance of the EventScheduler class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler_219594c0625599eb47a5906e96ce202b import EventScheduler
        return EventScheduler(self)

    @property
    def FcoeMaxNoDropThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput_a17d66f0c0c148318a40f959b5e5a87f.FcoeMaxNoDropThroughput): An instance of the FcoeMaxNoDropThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput_a17d66f0c0c148318a40f959b5e5a87f import FcoeMaxNoDropThroughput
        return FcoeMaxNoDropThroughput(self)

    @property
    def FcoeMaxNoPauseThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput_fb669ebd7344f1c07e0b312ed0d73f12.FcoeMaxNoPauseThroughput): An instance of the FcoeMaxNoPauseThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput_fb669ebd7344f1c07e0b312ed0d73f12 import FcoeMaxNoPauseThroughput
        return FcoeMaxNoPauseThroughput(self)

    @property
    def Globals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.globals_033830cb5397cb0e5ef66253f90ad9e7.Globals): An instance of the Globals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.globals_033830cb5397cb0e5ef66253f90ad9e7 import Globals
        return Globals(self)._select()

    @property
    def IptvChannelZapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping_c35fa2603b52975fd86cf60a764f1bc4.IptvChannelZapping): An instance of the IptvChannelZapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping_c35fa2603b52975fd86cf60a764f1bc4 import IptvChannelZapping
        return IptvChannelZapping(self)

    @property
    def L2tpCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpcapacity_26420a4c073ef2e5567c09114f87fe93.L2tpCapacity): An instance of the L2tpCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpcapacity_26420a4c073ef2e5567c09114f87fe93 import L2tpCapacity
        return L2tpCapacity(self)

    @property
    def L2tpRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate_27f47bfa9d82a466bf7039955ae00577.L2tpRate): An instance of the L2tpRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate_27f47bfa9d82a466bf7039955ae00577 import L2tpRate
        return L2tpRate(self)

    @property
    def L2tpRateCpf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpratecpf_783f5a0ed938906c9d7aa8783627a802.L2tpRateCpf): An instance of the L2tpRateCpf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpratecpf_783f5a0ed938906c9d7aa8783627a802 import L2tpRateCpf
        return L2tpRateCpf(self)

    @property
    def LnsCpfCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.lnscpfcapacity_afa6277f02d2c7f917dbd0be43db8179.LnsCpfCapacity): An instance of the LnsCpfCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.lnscpfcapacity_afa6277f02d2c7f917dbd0be43db8179 import LnsCpfCapacity
        return LnsCpfCapacity(self)

    @property
    def OpenFlowFailoverPerformance(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance_55e83c38e79ac2265ca1f0105dfb3b3c.OpenFlowFailoverPerformance): An instance of the OpenFlowFailoverPerformance class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance_55e83c38e79ac2265ca1f0105dfb3b3c import OpenFlowFailoverPerformance
        return OpenFlowFailoverPerformance(self)

    @property
    def OpenFlowLayer2LearningRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate_a5ca2769d3fcd94a0525e69ac907a187.OpenFlowLayer2LearningRate): An instance of the OpenFlowLayer2LearningRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate_a5ca2769d3fcd94a0525e69ac907a187 import OpenFlowLayer2LearningRate
        return OpenFlowLayer2LearningRate(self)

    @property
    def OpenFlowLayer3LearningRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate_c370fb0e73f7599f0a27b9ef7a000b06.OpenFlowLayer3LearningRate): An instance of the OpenFlowLayer3LearningRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate_c370fb0e73f7599f0a27b9ef7a000b06 import OpenFlowLayer3LearningRate
        return OpenFlowLayer3LearningRate(self)

    @property
    def OpenFlowTableCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity_611c21f1ccd5750a8fd8285af9eeef8a.OpenFlowTableCapacity): An instance of the OpenFlowTableCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity_611c21f1ccd5750a8fd8285af9eeef8a import OpenFlowTableCapacity
        return OpenFlowTableCapacity(self)

    @property
    def PppServerCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity_809dcb2ee4813529875c98463aca2e93.PppServerCapacity): An instance of the PppServerCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity_809dcb2ee4813529875c98463aca2e93 import PppServerCapacity
        return PppServerCapacity(self)

    @property
    def PppSessionRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate_380a968447e35ed60b30156645ecb9bc.PppSessionRate): An instance of the PppSessionRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate_380a968447e35ed60b30156645ecb9bc import PppSessionRate
        return PppSessionRate(self)

    @property
    def PppoxRateCpf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpf_c007f5e23f6133639a8416ca23a81ceb.PppoxRateCpf): An instance of the PppoxRateCpf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpf_c007f5e23f6133639a8416ca23a81ceb import PppoxRateCpf
        return PppoxRateCpf(self)

    @property
    def PppoxRateCpfServerCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpfservercapacity_caae3ae33a1dfe5143d1a68921af7707.PppoxRateCpfServerCapacity): An instance of the PppoxRateCpfServerCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpfservercapacity_caae3ae33a1dfe5143d1a68921af7707 import PppoxRateCpfServerCapacity
        return PppoxRateCpfServerCapacity(self)

    @property
    def PtpBestMasterSelection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection_996e5e528a2d5698be2c2e7adcff2e4d.PtpBestMasterSelection): An instance of the PtpBestMasterSelection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection_996e5e528a2d5698be2c2e7adcff2e4d import PtpBestMasterSelection
        return PtpBestMasterSelection(self)

    @property
    def PtpCorrectionFactorError(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror_509550cef5a0a7369cebd2bff0e350a9.PtpCorrectionFactorError): An instance of the PtpCorrectionFactorError class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror_509550cef5a0a7369cebd2bff0e350a9 import PtpCorrectionFactorError
        return PtpCorrectionFactorError(self)

    @property
    def PtpSlaveScalability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability_df907f07dd3aa56da5905010c99f7569.PtpSlaveScalability): An instance of the PtpSlaveScalability class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability_df907f07dd3aa56da5905010c99f7569 import PtpSlaveScalability
        return PtpSlaveScalability(self)

    @property
    def Rfc2544back2back(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_12578170a02b49f64e35c906b56d2366.Rfc2544back2back): An instance of the Rfc2544back2back class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_12578170a02b49f64e35c906b56d2366 import Rfc2544back2back
        return Rfc2544back2back(self)

    @property
    def Rfc2544frameLoss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_39298ecf3feb5a37055336394191132f.Rfc2544frameLoss): An instance of the Rfc2544frameLoss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_39298ecf3feb5a37055336394191132f import Rfc2544frameLoss
        return Rfc2544frameLoss(self)

    @property
    def Rfc2544throughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_2993ee9d3aa1842ea5cbff3edf8a2923.Rfc2544throughput): An instance of the Rfc2544throughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_2993ee9d3aa1842ea5cbff3edf8a2923 import Rfc2544throughput
        return Rfc2544throughput(self)

    @property
    def Rfc2889addressCache(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addresscache_e7041b395ffba168c52e36bf3ea992d0.Rfc2889addressCache): An instance of the Rfc2889addressCache class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addresscache_e7041b395ffba168c52e36bf3ea992d0 import Rfc2889addressCache
        return Rfc2889addressCache(self)

    @property
    def Rfc2889addressRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addressrate_0eb3340422d7cbfb50d5e57f70eac2d5.Rfc2889addressRate): An instance of the Rfc2889addressRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addressrate_0eb3340422d7cbfb50d5e57f70eac2d5 import Rfc2889addressRate
        return Rfc2889addressRate(self)

    @property
    def Rfc2889broadcastRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate_83d4e40fbaa25df4a6ff032d53810095.Rfc2889broadcastRate): An instance of the Rfc2889broadcastRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate_83d4e40fbaa25df4a6ff032d53810095 import Rfc2889broadcastRate
        return Rfc2889broadcastRate(self)

    @property
    def Rfc2889congestionControl(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol_67cfbfb215f79073fcca050c97fad1db.Rfc2889congestionControl): An instance of the Rfc2889congestionControl class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol_67cfbfb215f79073fcca050c97fad1db import Rfc2889congestionControl
        return Rfc2889congestionControl(self)

    @property
    def Rfc2889frameErrorFiltering(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering_f5e44fa5e9afed5f140a683bfe3acc6e.Rfc2889frameErrorFiltering): An instance of the Rfc2889frameErrorFiltering class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering_f5e44fa5e9afed5f140a683bfe3acc6e import Rfc2889frameErrorFiltering
        return Rfc2889frameErrorFiltering(self)

    @property
    def Rfc2889fullyMeshed(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889fullymeshed_437f8a90c6738122b454022e19733647.Rfc2889fullyMeshed): An instance of the Rfc2889fullyMeshed class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889fullymeshed_437f8a90c6738122b454022e19733647 import Rfc2889fullyMeshed
        return Rfc2889fullyMeshed(self)

    @property
    def Rfc2889manyToOne(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889manytoone_e0d69da5c63539d76b7e272c4afaf842.Rfc2889manyToOne): An instance of the Rfc2889manyToOne class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889manytoone_e0d69da5c63539d76b7e272c4afaf842 import Rfc2889manyToOne
        return Rfc2889manyToOne(self)

    @property
    def Rfc2889oneToMany(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889onetomany_f7a2a5a500b7346fe02962d7cc152595.Rfc2889oneToMany): An instance of the Rfc2889oneToMany class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889onetomany_f7a2a5a500b7346fe02962d7cc152595 import Rfc2889oneToMany
        return Rfc2889oneToMany(self)

    @property
    def Rfc2889partiallyMeshed(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889partiallymeshed_333db96771598d71c507872d5b1d462f.Rfc2889partiallyMeshed): An instance of the Rfc2889partiallyMeshed class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889partiallymeshed_333db96771598d71c507872d5b1d462f import Rfc2889partiallyMeshed
        return Rfc2889partiallyMeshed(self)

    @property
    def Rfc3918aggregated(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918aggregated_468c5ad8a207f561036eafe632b80296.Rfc3918aggregated): An instance of the Rfc3918aggregated class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918aggregated_468c5ad8a207f561036eafe632b80296 import Rfc3918aggregated
        return Rfc3918aggregated(self)

    @property
    def Rfc3918burdenedJoinDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedjoindelay_778fcaab0dc095f7632f49846264f03c.Rfc3918burdenedJoinDelay): An instance of the Rfc3918burdenedJoinDelay class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedjoindelay_778fcaab0dc095f7632f49846264f03c import Rfc3918burdenedJoinDelay
        return Rfc3918burdenedJoinDelay(self)

    @property
    def Rfc3918burdenedLatency(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedlatency_051415586a773e942feecf0dcf688960.Rfc3918burdenedLatency): An instance of the Rfc3918burdenedLatency class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedlatency_051415586a773e942feecf0dcf688960 import Rfc3918burdenedLatency
        return Rfc3918burdenedLatency(self)

    @property
    def Rfc3918groupCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918groupcapacity_f70d8d60e13ef4b973f6cb9a39a7cafe.Rfc3918groupCapacity): An instance of the Rfc3918groupCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918groupcapacity_f70d8d60e13ef4b973f6cb9a39a7cafe import Rfc3918groupCapacity
        return Rfc3918groupCapacity(self)

    @property
    def Rfc3918groupPatternVerification(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918grouppatternverification_ad3991f1b75d80d42a2d51082c6df60b.Rfc3918groupPatternVerification): An instance of the Rfc3918groupPatternVerification class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918grouppatternverification_ad3991f1b75d80d42a2d51082c6df60b import Rfc3918groupPatternVerification
        return Rfc3918groupPatternVerification(self)

    @property
    def Rfc3918ipmcMinMaxLat(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918ipmcminmaxlat_82718cbf506d637a0cfb1991514ca0d2.Rfc3918ipmcMinMaxLat): An instance of the Rfc3918ipmcMinMaxLat class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918ipmcminmaxlat_82718cbf506d637a0cfb1991514ca0d2 import Rfc3918ipmcMinMaxLat
        return Rfc3918ipmcMinMaxLat(self)

    @property
    def Rfc3918joinLeaveDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinleavedelay_e5020feb33af636e00beb0298db8c585.Rfc3918joinLeaveDelay): An instance of the Rfc3918joinLeaveDelay class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinleavedelay_e5020feb33af636e00beb0298db8c585 import Rfc3918joinLeaveDelay
        return Rfc3918joinLeaveDelay(self)

    @property
    def Rfc3918joinRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinrate_df91aab42be266e95ba24cebf7db50ff.Rfc3918joinRate): An instance of the Rfc3918joinRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinrate_df91aab42be266e95ba24cebf7db50ff import Rfc3918joinRate
        return Rfc3918joinRate(self)

    @property
    def Rfc3918mixedClassThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918mixedclassthroughput_7d9fa4d08c344e14ee38ce04b4d35042.Rfc3918mixedClassThroughput): An instance of the Rfc3918mixedClassThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918mixedclassthroughput_7d9fa4d08c344e14ee38ce04b4d35042 import Rfc3918mixedClassThroughput
        return Rfc3918mixedClassThroughput(self)

    @property
    def Rfc3918scaleGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918scalegroup_ee466f99d8ac98dbcd9d0be5c0856d14.Rfc3918scaleGroup): An instance of the Rfc3918scaleGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918scalegroup_ee466f99d8ac98dbcd9d0be5c0856d14 import Rfc3918scaleGroup
        return Rfc3918scaleGroup(self)

    @property
    def Rfc7747failover(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747failover_8333e060227da2d8ed45c7456c99872c.Rfc7747failover): An instance of the Rfc7747failover class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747failover_8333e060227da2d8ed45c7456c99872c import Rfc7747failover
        return Rfc7747failover(self)

    @property
    def Rfc7747ribIn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747ribin_5b839ddf0a3f19dfee6fd0576b401464.Rfc7747ribIn): An instance of the Rfc7747ribIn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747ribin_5b839ddf0a3f19dfee6fd0576b401464 import Rfc7747ribIn
        return Rfc7747ribIn(self)

    @property
    def TrafficTest(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_9d35200ffccac8a312e6b44f015bd7dc.TrafficTest): An instance of the TrafficTest class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_9d35200ffccac8a312e6b44f015bd7dc import TrafficTest
        return TrafficTest(self)

    @property
    def Y1564(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.y1564_24c9fbc236066a2c74c63118f4cbdeae.Y1564): An instance of the Y1564 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.y1564_24c9fbc236066a2c74c63118f4cbdeae import Y1564
        return Y1564(self)

    @property
    def RunningTest(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../*]): Returns list containing the currently running QuickTest
        """
        return self._get_attribute('runningTest')

    @property
    def RunningTestObj(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../*]): Returns list containing the currently running QuickTest
        """
        return self._get_attribute('runningTestObj')

    @property
    def TestIds(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../*]): Returns list containing the QuickTest test in the configuration
        """
        return self._get_attribute('testIds')

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
