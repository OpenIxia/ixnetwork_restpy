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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class QuickTest(Base):
    """The IxNetwork QuickTests feature provides the ability to run predefined tests.
    The QuickTest class encapsulates a required quickTest resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "quickTest"
    _SDM_ATT_MAP = {
        "RunningTest": "runningTest",
        "RunningTestObj": "runningTestObj",
        "TestIds": "testIds",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(QuickTest, self).__init__(parent, list_op)

    @property
    def AsymmetricFrameLoss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss_9e26b411ea07830a6774d24261df4537.AsymmetricFrameLoss): An instance of the AsymmetricFrameLoss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss_9e26b411ea07830a6774d24261df4537 import (
            AsymmetricFrameLoss,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AsymmetricFrameLoss", None) is not None:
                return self._properties.get("AsymmetricFrameLoss")
        return AsymmetricFrameLoss(self)

    @property
    def AsymmetricThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput_0177e577de3fcef100ee4736ed5038fc.AsymmetricThroughput): An instance of the AsymmetricThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput_0177e577de3fcef100ee4736ed5038fc import (
            AsymmetricThroughput,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AsymmetricThroughput", None) is not None:
                return self._properties.get("AsymmetricThroughput")
        return AsymmetricThroughput(self)

    @property
    def CloudPerf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf_fdd110ba22283c5cbf388c5117f9a96a.CloudPerf): An instance of the CloudPerf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf_fdd110ba22283c5cbf388c5117f9a96a import (
            CloudPerf,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CloudPerf", None) is not None:
                return self._properties.get("CloudPerf")
        return CloudPerf(self)

    @property
    def CustomContDuration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration_589f53152bfa0216c8e0994d79e08373.CustomContDuration): An instance of the CustomContDuration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration_589f53152bfa0216c8e0994d79e08373 import (
            CustomContDuration,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CustomContDuration", None) is not None:
                return self._properties.get("CustomContDuration")
        return CustomContDuration(self)

    @property
    def CustomFixedDuration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration_61d433fa46ead4fbcc08caaf30608356.CustomFixedDuration): An instance of the CustomFixedDuration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration_61d433fa46ead4fbcc08caaf30608356 import (
            CustomFixedDuration,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CustomFixedDuration", None) is not None:
                return self._properties.get("CustomFixedDuration")
        return CustomFixedDuration(self)

    @property
    def CustomStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customstep_98f1ecce7c2d88439541c6c12fb66c1d.CustomStep): An instance of the CustomStep class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customstep_98f1ecce7c2d88439541c6c12fb66c1d import (
            CustomStep,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CustomStep", None) is not None:
                return self._properties.get("CustomStep")
        return CustomStep(self)

    @property
    def CustomThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput_43392709d9d2c48c1b386a084571fdf5.CustomThroughput): An instance of the CustomThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput_43392709d9d2c48c1b386a084571fdf5 import (
            CustomThroughput,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CustomThroughput", None) is not None:
                return self._properties.get("CustomThroughput")
        return CustomThroughput(self)

    @property
    def DhcpRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate_6f52413edee9d4b4cab233342c11f62b.DhcpRate): An instance of the DhcpRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate_6f52413edee9d4b4cab233342c11f62b import (
            DhcpRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DhcpRate", None) is not None:
                return self._properties.get("DhcpRate")
        return DhcpRate(self)

    @property
    def DhcpRateCpf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpratecpf_6209b644d3106a06341c5565d4c9938d.DhcpRateCpf): An instance of the DhcpRateCpf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpratecpf_6209b644d3106a06341c5565d4c9938d import (
            DhcpRateCpf,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DhcpRateCpf", None) is not None:
                return self._properties.get("DhcpRateCpf")
        return DhcpRateCpf(self)

    @property
    def Dhcpv6Rate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate_b7650b06ef0db627654946a311cbc9bb.Dhcpv6Rate): An instance of the Dhcpv6Rate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate_b7650b06ef0db627654946a311cbc9bb import (
            Dhcpv6Rate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv6Rate", None) is not None:
                return self._properties.get("Dhcpv6Rate")
        return Dhcpv6Rate(self)

    @property
    def Dhcpv6RateCpf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6ratecpf_6d7fd500899ffb6a0fed017f65397c33.Dhcpv6RateCpf): An instance of the Dhcpv6RateCpf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6ratecpf_6d7fd500899ffb6a0fed017f65397c33 import (
            Dhcpv6RateCpf,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv6RateCpf", None) is not None:
                return self._properties.get("Dhcpv6RateCpf")
        return Dhcpv6RateCpf(self)

    @property
    def Dot1xCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity_060163d41bdfaa3d63e917d0fa7e7995.Dot1xCapacity): An instance of the Dot1xCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity_060163d41bdfaa3d63e917d0fa7e7995 import (
            Dot1xCapacity,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dot1xCapacity", None) is not None:
                return self._properties.get("Dot1xCapacity")
        return Dot1xCapacity(self)

    @property
    def Dot1xRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate_d841037f3c95312f5d95e0c3e8e68e72.Dot1xRate): An instance of the Dot1xRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate_d841037f3c95312f5d95e0c3e8e68e72 import (
            Dot1xRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dot1xRate", None) is not None:
                return self._properties.get("Dot1xRate")
        return Dot1xRate(self)

    @property
    def EventScheduler(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler_dbcc776816146a01a3385b4bdec9a524.EventScheduler): An instance of the EventScheduler class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler_dbcc776816146a01a3385b4bdec9a524 import (
            EventScheduler,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EventScheduler", None) is not None:
                return self._properties.get("EventScheduler")
        return EventScheduler(self)

    @property
    def FcoeMaxNoDropThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput_caa036e4ea16b6d8490baab54a7a3377.FcoeMaxNoDropThroughput): An instance of the FcoeMaxNoDropThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput_caa036e4ea16b6d8490baab54a7a3377 import (
            FcoeMaxNoDropThroughput,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeMaxNoDropThroughput", None) is not None:
                return self._properties.get("FcoeMaxNoDropThroughput")
        return FcoeMaxNoDropThroughput(self)

    @property
    def FcoeMaxNoPauseThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput_5ad968ab4d3c9fe2bdf36264fc9140ae.FcoeMaxNoPauseThroughput): An instance of the FcoeMaxNoPauseThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput_5ad968ab4d3c9fe2bdf36264fc9140ae import (
            FcoeMaxNoPauseThroughput,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FcoeMaxNoPauseThroughput", None) is not None:
                return self._properties.get("FcoeMaxNoPauseThroughput")
        return FcoeMaxNoPauseThroughput(self)

    @property
    def Globals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.globals_69a5d2805874fa9bd7dc448d50ded673.Globals): An instance of the Globals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.globals_69a5d2805874fa9bd7dc448d50ded673 import (
            Globals,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Globals", None) is not None:
                return self._properties.get("Globals")
        return Globals(self)._select()

    @property
    def IptvChannelZapping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping_31de08f962d6589ac7f01ee268afa1f8.IptvChannelZapping): An instance of the IptvChannelZapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping_31de08f962d6589ac7f01ee268afa1f8 import (
            IptvChannelZapping,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IptvChannelZapping", None) is not None:
                return self._properties.get("IptvChannelZapping")
        return IptvChannelZapping(self)

    @property
    def L2tpCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpcapacity_3ea965e8ab5d5bb33868030e8987180b.L2tpCapacity): An instance of the L2tpCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpcapacity_3ea965e8ab5d5bb33868030e8987180b import (
            L2tpCapacity,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("L2tpCapacity", None) is not None:
                return self._properties.get("L2tpCapacity")
        return L2tpCapacity(self)

    @property
    def L2tpRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate_70b6ec9c1ab739f3e122bb9aa824287b.L2tpRate): An instance of the L2tpRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate_70b6ec9c1ab739f3e122bb9aa824287b import (
            L2tpRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("L2tpRate", None) is not None:
                return self._properties.get("L2tpRate")
        return L2tpRate(self)

    @property
    def L2tpRateCpf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpratecpf_783a49754bc5382d09d62eef08fb6f6f.L2tpRateCpf): An instance of the L2tpRateCpf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.l2tpratecpf_783a49754bc5382d09d62eef08fb6f6f import (
            L2tpRateCpf,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("L2tpRateCpf", None) is not None:
                return self._properties.get("L2tpRateCpf")
        return L2tpRateCpf(self)

    @property
    def LnsCpfCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.lnscpfcapacity_2e1877e2c6cfbff71589fec7847fe90d.LnsCpfCapacity): An instance of the LnsCpfCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.lnscpfcapacity_2e1877e2c6cfbff71589fec7847fe90d import (
            LnsCpfCapacity,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LnsCpfCapacity", None) is not None:
                return self._properties.get("LnsCpfCapacity")
        return LnsCpfCapacity(self)

    @property
    def OpenFlowFailoverPerformance(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance_50924ff459aa0f2719393c238b1c71a9.OpenFlowFailoverPerformance): An instance of the OpenFlowFailoverPerformance class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance_50924ff459aa0f2719393c238b1c71a9 import (
            OpenFlowFailoverPerformance,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OpenFlowFailoverPerformance", None) is not None:
                return self._properties.get("OpenFlowFailoverPerformance")
        return OpenFlowFailoverPerformance(self)

    @property
    def OpenFlowLayer2LearningRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate_e5da985364765a56bf90bf997dc09d88.OpenFlowLayer2LearningRate): An instance of the OpenFlowLayer2LearningRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate_e5da985364765a56bf90bf997dc09d88 import (
            OpenFlowLayer2LearningRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OpenFlowLayer2LearningRate", None) is not None:
                return self._properties.get("OpenFlowLayer2LearningRate")
        return OpenFlowLayer2LearningRate(self)

    @property
    def OpenFlowLayer3LearningRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate_24a64d34da695088e642bf2d3643974d.OpenFlowLayer3LearningRate): An instance of the OpenFlowLayer3LearningRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate_24a64d34da695088e642bf2d3643974d import (
            OpenFlowLayer3LearningRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OpenFlowLayer3LearningRate", None) is not None:
                return self._properties.get("OpenFlowLayer3LearningRate")
        return OpenFlowLayer3LearningRate(self)

    @property
    def OpenFlowTableCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity_9d1b2428e9419c5f88c445937490500d.OpenFlowTableCapacity): An instance of the OpenFlowTableCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity_9d1b2428e9419c5f88c445937490500d import (
            OpenFlowTableCapacity,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OpenFlowTableCapacity", None) is not None:
                return self._properties.get("OpenFlowTableCapacity")
        return OpenFlowTableCapacity(self)

    @property
    def PppServerCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity_979eb526d86ff91bb93b7632215d608e.PppServerCapacity): An instance of the PppServerCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity_979eb526d86ff91bb93b7632215d608e import (
            PppServerCapacity,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppServerCapacity", None) is not None:
                return self._properties.get("PppServerCapacity")
        return PppServerCapacity(self)

    @property
    def PppSessionRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate_7133d4b47f948b84b4bce0cc33228436.PppSessionRate): An instance of the PppSessionRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate_7133d4b47f948b84b4bce0cc33228436 import (
            PppSessionRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppSessionRate", None) is not None:
                return self._properties.get("PppSessionRate")
        return PppSessionRate(self)

    @property
    def PppoxRateCpf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpf_edf3eb55fe0471c286d4bfc9ef6bf15f.PppoxRateCpf): An instance of the PppoxRateCpf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpf_edf3eb55fe0471c286d4bfc9ef6bf15f import (
            PppoxRateCpf,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppoxRateCpf", None) is not None:
                return self._properties.get("PppoxRateCpf")
        return PppoxRateCpf(self)

    @property
    def PppoxRateCpfServerCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpfservercapacity_4fa9f2f6b60fa2de488c91d089f14bbb.PppoxRateCpfServerCapacity): An instance of the PppoxRateCpfServerCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.pppoxratecpfservercapacity_4fa9f2f6b60fa2de488c91d089f14bbb import (
            PppoxRateCpfServerCapacity,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppoxRateCpfServerCapacity", None) is not None:
                return self._properties.get("PppoxRateCpfServerCapacity")
        return PppoxRateCpfServerCapacity(self)

    @property
    def PtpBestMasterSelection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection_6f10a38d2f306fac193108a7cedda79c.PtpBestMasterSelection): An instance of the PtpBestMasterSelection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection_6f10a38d2f306fac193108a7cedda79c import (
            PtpBestMasterSelection,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PtpBestMasterSelection", None) is not None:
                return self._properties.get("PtpBestMasterSelection")
        return PtpBestMasterSelection(self)

    @property
    def PtpCorrectionFactorError(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror_a796fd71e51214e85d4e3efc9d23ff7c.PtpCorrectionFactorError): An instance of the PtpCorrectionFactorError class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror_a796fd71e51214e85d4e3efc9d23ff7c import (
            PtpCorrectionFactorError,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PtpCorrectionFactorError", None) is not None:
                return self._properties.get("PtpCorrectionFactorError")
        return PtpCorrectionFactorError(self)

    @property
    def PtpSlaveScalability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability_46be9cd153cad47ed0d8acb04a35bd60.PtpSlaveScalability): An instance of the PtpSlaveScalability class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability_46be9cd153cad47ed0d8acb04a35bd60 import (
            PtpSlaveScalability,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PtpSlaveScalability", None) is not None:
                return self._properties.get("PtpSlaveScalability")
        return PtpSlaveScalability(self)

    @property
    def Rfc2544back2back(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_cfd3f40fbe677cc70482381fc445e21e.Rfc2544back2back): An instance of the Rfc2544back2back class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_cfd3f40fbe677cc70482381fc445e21e import (
            Rfc2544back2back,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc2544back2back", None) is not None:
                return self._properties.get("Rfc2544back2back")
        return Rfc2544back2back(self)

    @property
    def Rfc2544frameLoss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_868b9746dda2d0cfeed81516cf37d39d.Rfc2544frameLoss): An instance of the Rfc2544frameLoss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_868b9746dda2d0cfeed81516cf37d39d import (
            Rfc2544frameLoss,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc2544frameLoss", None) is not None:
                return self._properties.get("Rfc2544frameLoss")
        return Rfc2544frameLoss(self)

    @property
    def Rfc2544throughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_86fc74b3228f97518d2513e6b33a3960.Rfc2544throughput): An instance of the Rfc2544throughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_86fc74b3228f97518d2513e6b33a3960 import (
            Rfc2544throughput,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc2544throughput", None) is not None:
                return self._properties.get("Rfc2544throughput")
        return Rfc2544throughput(self)

    @property
    def Rfc2889addressCache(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addresscache_a18b9d3bb943f165530ead1bd2810a19.Rfc2889addressCache): An instance of the Rfc2889addressCache class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addresscache_a18b9d3bb943f165530ead1bd2810a19 import (
            Rfc2889addressCache,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc2889addressCache", None) is not None:
                return self._properties.get("Rfc2889addressCache")
        return Rfc2889addressCache(self)

    @property
    def Rfc2889addressRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addressrate_6b4eb5ae2d6036ecd651aea962977193.Rfc2889addressRate): An instance of the Rfc2889addressRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889addressrate_6b4eb5ae2d6036ecd651aea962977193 import (
            Rfc2889addressRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc2889addressRate", None) is not None:
                return self._properties.get("Rfc2889addressRate")
        return Rfc2889addressRate(self)

    @property
    def Rfc2889broadcastRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate_1f8e1c7f7f9e4d711149db4a572058fb.Rfc2889broadcastRate): An instance of the Rfc2889broadcastRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate_1f8e1c7f7f9e4d711149db4a572058fb import (
            Rfc2889broadcastRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc2889broadcastRate", None) is not None:
                return self._properties.get("Rfc2889broadcastRate")
        return Rfc2889broadcastRate(self)

    @property
    def Rfc2889congestionControl(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol_efe62c029fd5ff197d5d57687ac167a6.Rfc2889congestionControl): An instance of the Rfc2889congestionControl class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol_efe62c029fd5ff197d5d57687ac167a6 import (
            Rfc2889congestionControl,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc2889congestionControl", None) is not None:
                return self._properties.get("Rfc2889congestionControl")
        return Rfc2889congestionControl(self)

    @property
    def Rfc2889frameErrorFiltering(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering_56eb932020f20bf8144b92be8a4285f9.Rfc2889frameErrorFiltering): An instance of the Rfc2889frameErrorFiltering class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering_56eb932020f20bf8144b92be8a4285f9 import (
            Rfc2889frameErrorFiltering,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc2889frameErrorFiltering", None) is not None:
                return self._properties.get("Rfc2889frameErrorFiltering")
        return Rfc2889frameErrorFiltering(self)

    @property
    def Rfc2889fullyMeshed(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889fullymeshed_e7a2c563a7e22586b41e6c0ca493e098.Rfc2889fullyMeshed): An instance of the Rfc2889fullyMeshed class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889fullymeshed_e7a2c563a7e22586b41e6c0ca493e098 import (
            Rfc2889fullyMeshed,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc2889fullyMeshed", None) is not None:
                return self._properties.get("Rfc2889fullyMeshed")
        return Rfc2889fullyMeshed(self)

    @property
    def Rfc2889manyToOne(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889manytoone_2b7b125a9428908981ac29770d6d23c1.Rfc2889manyToOne): An instance of the Rfc2889manyToOne class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889manytoone_2b7b125a9428908981ac29770d6d23c1 import (
            Rfc2889manyToOne,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc2889manyToOne", None) is not None:
                return self._properties.get("Rfc2889manyToOne")
        return Rfc2889manyToOne(self)

    @property
    def Rfc2889oneToMany(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889onetomany_6adf166cb7ca002410d60da9c08f8675.Rfc2889oneToMany): An instance of the Rfc2889oneToMany class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889onetomany_6adf166cb7ca002410d60da9c08f8675 import (
            Rfc2889oneToMany,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc2889oneToMany", None) is not None:
                return self._properties.get("Rfc2889oneToMany")
        return Rfc2889oneToMany(self)

    @property
    def Rfc2889partiallyMeshed(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889partiallymeshed_a4adcc6d9251331658fb739e2d7454c1.Rfc2889partiallyMeshed): An instance of the Rfc2889partiallyMeshed class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889partiallymeshed_a4adcc6d9251331658fb739e2d7454c1 import (
            Rfc2889partiallyMeshed,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc2889partiallyMeshed", None) is not None:
                return self._properties.get("Rfc2889partiallyMeshed")
        return Rfc2889partiallyMeshed(self)

    @property
    def Rfc3918aggregated(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918aggregated_1577cf9dc401fdcbed618d982960f3b4.Rfc3918aggregated): An instance of the Rfc3918aggregated class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918aggregated_1577cf9dc401fdcbed618d982960f3b4 import (
            Rfc3918aggregated,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc3918aggregated", None) is not None:
                return self._properties.get("Rfc3918aggregated")
        return Rfc3918aggregated(self)

    @property
    def Rfc3918burdenedJoinDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedjoindelay_5fb7519f5338b2bbccc6f97d3ffd91a9.Rfc3918burdenedJoinDelay): An instance of the Rfc3918burdenedJoinDelay class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedjoindelay_5fb7519f5338b2bbccc6f97d3ffd91a9 import (
            Rfc3918burdenedJoinDelay,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc3918burdenedJoinDelay", None) is not None:
                return self._properties.get("Rfc3918burdenedJoinDelay")
        return Rfc3918burdenedJoinDelay(self)

    @property
    def Rfc3918burdenedLatency(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedlatency_5c655670918a97cde2f838582cac2cb7.Rfc3918burdenedLatency): An instance of the Rfc3918burdenedLatency class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918burdenedlatency_5c655670918a97cde2f838582cac2cb7 import (
            Rfc3918burdenedLatency,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc3918burdenedLatency", None) is not None:
                return self._properties.get("Rfc3918burdenedLatency")
        return Rfc3918burdenedLatency(self)

    @property
    def Rfc3918groupCapacity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918groupcapacity_283c76beeb0bd3309d21f95efa64cf3e.Rfc3918groupCapacity): An instance of the Rfc3918groupCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918groupcapacity_283c76beeb0bd3309d21f95efa64cf3e import (
            Rfc3918groupCapacity,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc3918groupCapacity", None) is not None:
                return self._properties.get("Rfc3918groupCapacity")
        return Rfc3918groupCapacity(self)

    @property
    def Rfc3918groupPatternVerification(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918grouppatternverification_2a07ba09c7094b428c0d3922f7629306.Rfc3918groupPatternVerification): An instance of the Rfc3918groupPatternVerification class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918grouppatternverification_2a07ba09c7094b428c0d3922f7629306 import (
            Rfc3918groupPatternVerification,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("Rfc3918groupPatternVerification", None)
                is not None
            ):
                return self._properties.get("Rfc3918groupPatternVerification")
        return Rfc3918groupPatternVerification(self)

    @property
    def Rfc3918ipmcMinMaxLat(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918ipmcminmaxlat_26e8ac413e1c57bed7d65373af19d55d.Rfc3918ipmcMinMaxLat): An instance of the Rfc3918ipmcMinMaxLat class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918ipmcminmaxlat_26e8ac413e1c57bed7d65373af19d55d import (
            Rfc3918ipmcMinMaxLat,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc3918ipmcMinMaxLat", None) is not None:
                return self._properties.get("Rfc3918ipmcMinMaxLat")
        return Rfc3918ipmcMinMaxLat(self)

    @property
    def Rfc3918joinLeaveDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinleavedelay_b6d71057192e2bd335f57efa8ce87cfc.Rfc3918joinLeaveDelay): An instance of the Rfc3918joinLeaveDelay class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinleavedelay_b6d71057192e2bd335f57efa8ce87cfc import (
            Rfc3918joinLeaveDelay,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc3918joinLeaveDelay", None) is not None:
                return self._properties.get("Rfc3918joinLeaveDelay")
        return Rfc3918joinLeaveDelay(self)

    @property
    def Rfc3918joinRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinrate_6fb6ff9eb8c4ca339d14b141cf94f6d5.Rfc3918joinRate): An instance of the Rfc3918joinRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918joinrate_6fb6ff9eb8c4ca339d14b141cf94f6d5 import (
            Rfc3918joinRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc3918joinRate", None) is not None:
                return self._properties.get("Rfc3918joinRate")
        return Rfc3918joinRate(self)

    @property
    def Rfc3918mixedClassThroughput(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918mixedclassthroughput_0bc84bbc09b86982f6afb967256416cc.Rfc3918mixedClassThroughput): An instance of the Rfc3918mixedClassThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918mixedclassthroughput_0bc84bbc09b86982f6afb967256416cc import (
            Rfc3918mixedClassThroughput,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc3918mixedClassThroughput", None) is not None:
                return self._properties.get("Rfc3918mixedClassThroughput")
        return Rfc3918mixedClassThroughput(self)

    @property
    def Rfc3918scaleGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918scalegroup_1e60c67b625179ef57d82ab7ab1734f8.Rfc3918scaleGroup): An instance of the Rfc3918scaleGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc3918scalegroup_1e60c67b625179ef57d82ab7ab1734f8 import (
            Rfc3918scaleGroup,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc3918scaleGroup", None) is not None:
                return self._properties.get("Rfc3918scaleGroup")
        return Rfc3918scaleGroup(self)

    @property
    def Rfc7747failover(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747failover_7bc538e343d6f2063518f28f8b660c4d.Rfc7747failover): An instance of the Rfc7747failover class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747failover_7bc538e343d6f2063518f28f8b660c4d import (
            Rfc7747failover,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc7747failover", None) is not None:
                return self._properties.get("Rfc7747failover")
        return Rfc7747failover(self)

    @property
    def Rfc7747ribIn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747ribin_8a0b8d0a4f79939041fe1d67eb2b120d.Rfc7747ribIn): An instance of the Rfc7747ribIn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.rfc7747ribin_8a0b8d0a4f79939041fe1d67eb2b120d import (
            Rfc7747ribIn,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rfc7747ribIn", None) is not None:
                return self._properties.get("Rfc7747ribIn")
        return Rfc7747ribIn(self)

    @property
    def TrafficTest(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_f399e685b29fd795590f27fffbfa469c.TrafficTest): An instance of the TrafficTest class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_f399e685b29fd795590f27fffbfa469c import (
            TrafficTest,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficTest", None) is not None:
                return self._properties.get("TrafficTest")
        return TrafficTest(self)

    @property
    def Y1564(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.y1564_9b70a4fc765ea18ca465ea775da0fa0b.Y1564): An instance of the Y1564 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.y1564_9b70a4fc765ea18ca465ea775da0fa0b import (
            Y1564,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Y1564", None) is not None:
                return self._properties.get("Y1564")
        return Y1564(self)

    @property
    def RunningTest(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/quickTest]): Returns list containing the currently running QuickTest
        """
        return self._get_attribute(self._SDM_ATT_MAP["RunningTest"])

    @property
    def RunningTestObj(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/quickTest]): Returns list containing the currently running QuickTest
        """
        return self._get_attribute(self._SDM_ATT_MAP["RunningTestObj"])

    @property
    def TestIds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/quickTest]): Returns list containing the QuickTest test in the configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestIds"])

    def find(self, RunningTest=None, RunningTestObj=None, TestIds=None):
        # type: (List[str], List[str], List[str]) -> QuickTest
        """Finds and retrieves quickTest resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve quickTest resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all quickTest resources from the server.

        Args
        ----
        - RunningTest (list(str[None | /api/v1/sessions/1/ixnetwork/quickTest])): Returns list containing the currently running QuickTest
        - RunningTestObj (list(str[None | /api/v1/sessions/1/ixnetwork/quickTest])): Returns list containing the currently running QuickTest
        - TestIds (list(str[None | /api/v1/sessions/1/ixnetwork/quickTest])): Returns list containing the QuickTest test in the configuration

        Returns
        -------
        - self: This instance with matching quickTest resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of quickTest data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the quickTest resources from the server available through an iterator or index

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("apply", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsync", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("generateReport", payload=payload, response_object=None)

    def LoadBatchFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the loadBatchFile operation on the server.

        Loads the given batch file with all the results of the old quick test.

        loadBatchFile(Arg2=string, async_operation=bool)
        ------------------------------------------------
        - Arg2 (str): Exact path to the batch xml.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("loadBatchFile", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("run", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("waitForTest", payload=payload, response_object=None)
