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
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(QuickTest, self).__init__(parent, list_op)

    @property
    def AsymmetricFrameLoss(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss_9e26b411ea07830a6774d24261df4537.AsymmetricFrameLoss): An instance of the AsymmetricFrameLoss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss_9e26b411ea07830a6774d24261df4537 import AsymmetricFrameLoss
        if len(self._object_properties) > 0:
            if self._properties.get('AsymmetricFrameLoss', None) is not None:
                return self._properties.get('AsymmetricFrameLoss')
        return AsymmetricFrameLoss(self)

    @property
    def AsymmetricThroughput(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput_0177e577de3fcef100ee4736ed5038fc.AsymmetricThroughput): An instance of the AsymmetricThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput_0177e577de3fcef100ee4736ed5038fc import AsymmetricThroughput
        if len(self._object_properties) > 0:
            if self._properties.get('AsymmetricThroughput', None) is not None:
                return self._properties.get('AsymmetricThroughput')
        return AsymmetricThroughput(self)

    @property
    def CloudPerf(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf_fdd110ba22283c5cbf388c5117f9a96a.CloudPerf): An instance of the CloudPerf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf_fdd110ba22283c5cbf388c5117f9a96a import CloudPerf
        if len(self._object_properties) > 0:
            if self._properties.get('CloudPerf', None) is not None:
                return self._properties.get('CloudPerf')
        return CloudPerf(self)

    @property
    def CustomContDuration(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration_589f53152bfa0216c8e0994d79e08373.CustomContDuration): An instance of the CustomContDuration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration_589f53152bfa0216c8e0994d79e08373 import CustomContDuration
        if len(self._object_properties) > 0:
            if self._properties.get('CustomContDuration', None) is not None:
                return self._properties.get('CustomContDuration')
        return CustomContDuration(self)

    @property
    def CustomFixedDuration(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration_61d433fa46ead4fbcc08caaf30608356.CustomFixedDuration): An instance of the CustomFixedDuration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration_61d433fa46ead4fbcc08caaf30608356 import CustomFixedDuration
        if len(self._object_properties) > 0:
            if self._properties.get('CustomFixedDuration', None) is not None:
                return self._properties.get('CustomFixedDuration')
        return CustomFixedDuration(self)

    @property
    def CustomStep(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customstep_98f1ecce7c2d88439541c6c12fb66c1d.CustomStep): An instance of the CustomStep class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customstep_98f1ecce7c2d88439541c6c12fb66c1d import CustomStep
        if len(self._object_properties) > 0:
            if self._properties.get('CustomStep', None) is not None:
                return self._properties.get('CustomStep')
        return CustomStep(self)

    @property
    def CustomThroughput(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput_43392709d9d2c48c1b386a084571fdf5.CustomThroughput): An instance of the CustomThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput_43392709d9d2c48c1b386a084571fdf5 import CustomThroughput
        if len(self._object_properties) > 0:
            if self._properties.get('CustomThroughput', None) is not None:
                return self._properties.get('CustomThroughput')
        return CustomThroughput(self)

    @property
    def DhcpRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate_6f52413edee9d4b4cab233342c11f62b.DhcpRate): An instance of the DhcpRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate_6f52413edee9d4b4cab233342c11f62b import DhcpRate
        if len(self._object_properties) > 0:
            if self._properties.get('DhcpRate', None) is not None:
                return self._properties.get('DhcpRate')
        return DhcpRate(self)

    @property
    def Dhcpv6Rate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate_b7650b06ef0db627654946a311cbc9bb.Dhcpv6Rate): An instance of the Dhcpv6Rate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate_b7650b06ef0db627654946a311cbc9bb import Dhcpv6Rate
        if len(self._object_properties) > 0:
            if self._properties.get('Dhcpv6Rate', None) is not None:
                return self._properties.get('Dhcpv6Rate')
        return Dhcpv6Rate(self)

    @property
    def Dot1xCapacity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity_060163d41bdfaa3d63e917d0fa7e7995.Dot1xCapacity): An instance of the Dot1xCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity_060163d41bdfaa3d63e917d0fa7e7995 import Dot1xCapacity
        if len(self._object_properties) > 0:
            if self._properties.get('Dot1xCapacity', None) is not None:
                return self._properties.get('Dot1xCapacity')
        return Dot1xCapacity(self)

    @property
    def Dot1xRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate_d841037f3c95312f5d95e0c3e8e68e72.Dot1xRate): An instance of the Dot1xRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate_d841037f3c95312f5d95e0c3e8e68e72 import Dot1xRate
        if len(self._object_properties) > 0:
            if self._properties.get('Dot1xRate', None) is not None:
                return self._properties.get('Dot1xRate')
        return Dot1xRate(self)

    @property
    def EventScheduler(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler_dbcc776816146a01a3385b4bdec9a524.EventScheduler): An instance of the EventScheduler class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler_dbcc776816146a01a3385b4bdec9a524 import EventScheduler
        if len(self._object_properties) > 0:
            if self._properties.get('EventScheduler', None) is not None:
                return self._properties.get('EventScheduler')
        return EventScheduler(self)

    @property
    def FcoeMaxNoDropThroughput(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput_caa036e4ea16b6d8490baab54a7a3377.FcoeMaxNoDropThroughput): An instance of the FcoeMaxNoDropThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput_caa036e4ea16b6d8490baab54a7a3377 import FcoeMaxNoDropThroughput
        if len(self._object_properties) > 0:
            if self._properties.get('FcoeMaxNoDropThroughput', None) is not None:
                return self._properties.get('FcoeMaxNoDropThroughput')
        return FcoeMaxNoDropThroughput(self)

    @property
    def FcoeMaxNoPauseThroughput(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput_5ad968ab4d3c9fe2bdf36264fc9140ae.FcoeMaxNoPauseThroughput): An instance of the FcoeMaxNoPauseThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput_5ad968ab4d3c9fe2bdf36264fc9140ae import FcoeMaxNoPauseThroughput
        if len(self._object_properties) > 0:
            if self._properties.get('FcoeMaxNoPauseThroughput', None) is not None:
                return self._properties.get('FcoeMaxNoPauseThroughput')
        return FcoeMaxNoPauseThroughput(self)

    @property
    def Globals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.globals_605c8d39970b93a1aba6b6a97467871c.Globals): An instance of the Globals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.globals_605c8d39970b93a1aba6b6a97467871c import Globals
        if len(self._object_properties) > 0:
            if self._properties.get('Globals', None) is not None:
                return self._properties.get('Globals')
        return Globals(self)._select()

    @property
    def IptvChannelZapping(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping_31de08f962d6589ac7f01ee268afa1f8.IptvChannelZapping): An instance of the IptvChannelZapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping_31de08f962d6589ac7f01ee268afa1f8 import IptvChannelZapping
        if len(self._object_properties) > 0:
            if self._properties.get('IptvChannelZapping', None) is not None:
                return self._properties.get('IptvChannelZapping')
        return IptvChannelZapping(self)

    @property
    def L2tpRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate_70b6ec9c1ab739f3e122bb9aa824287b.L2tpRate): An instance of the L2tpRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate_70b6ec9c1ab739f3e122bb9aa824287b import L2tpRate
        if len(self._object_properties) > 0:
            if self._properties.get('L2tpRate', None) is not None:
                return self._properties.get('L2tpRate')
        return L2tpRate(self)

    @property
    def OpenFlowFailoverPerformance(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance_50924ff459aa0f2719393c238b1c71a9.OpenFlowFailoverPerformance): An instance of the OpenFlowFailoverPerformance class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance_50924ff459aa0f2719393c238b1c71a9 import OpenFlowFailoverPerformance
        if len(self._object_properties) > 0:
            if self._properties.get('OpenFlowFailoverPerformance', None) is not None:
                return self._properties.get('OpenFlowFailoverPerformance')
        return OpenFlowFailoverPerformance(self)

    @property
    def OpenFlowLayer2LearningRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate_e5da985364765a56bf90bf997dc09d88.OpenFlowLayer2LearningRate): An instance of the OpenFlowLayer2LearningRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate_e5da985364765a56bf90bf997dc09d88 import OpenFlowLayer2LearningRate
        if len(self._object_properties) > 0:
            if self._properties.get('OpenFlowLayer2LearningRate', None) is not None:
                return self._properties.get('OpenFlowLayer2LearningRate')
        return OpenFlowLayer2LearningRate(self)

    @property
    def OpenFlowLayer3LearningRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate_24a64d34da695088e642bf2d3643974d.OpenFlowLayer3LearningRate): An instance of the OpenFlowLayer3LearningRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate_24a64d34da695088e642bf2d3643974d import OpenFlowLayer3LearningRate
        if len(self._object_properties) > 0:
            if self._properties.get('OpenFlowLayer3LearningRate', None) is not None:
                return self._properties.get('OpenFlowLayer3LearningRate')
        return OpenFlowLayer3LearningRate(self)

    @property
    def OpenFlowTableCapacity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity_9d1b2428e9419c5f88c445937490500d.OpenFlowTableCapacity): An instance of the OpenFlowTableCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity_9d1b2428e9419c5f88c445937490500d import OpenFlowTableCapacity
        if len(self._object_properties) > 0:
            if self._properties.get('OpenFlowTableCapacity', None) is not None:
                return self._properties.get('OpenFlowTableCapacity')
        return OpenFlowTableCapacity(self)

    @property
    def PppServerCapacity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity_979eb526d86ff91bb93b7632215d608e.PppServerCapacity): An instance of the PppServerCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity_979eb526d86ff91bb93b7632215d608e import PppServerCapacity
        if len(self._object_properties) > 0:
            if self._properties.get('PppServerCapacity', None) is not None:
                return self._properties.get('PppServerCapacity')
        return PppServerCapacity(self)

    @property
    def PppSessionRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate_7133d4b47f948b84b4bce0cc33228436.PppSessionRate): An instance of the PppSessionRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate_7133d4b47f948b84b4bce0cc33228436 import PppSessionRate
        if len(self._object_properties) > 0:
            if self._properties.get('PppSessionRate', None) is not None:
                return self._properties.get('PppSessionRate')
        return PppSessionRate(self)

    @property
    def PtpBestMasterSelection(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection_6f10a38d2f306fac193108a7cedda79c.PtpBestMasterSelection): An instance of the PtpBestMasterSelection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection_6f10a38d2f306fac193108a7cedda79c import PtpBestMasterSelection
        if len(self._object_properties) > 0:
            if self._properties.get('PtpBestMasterSelection', None) is not None:
                return self._properties.get('PtpBestMasterSelection')
        return PtpBestMasterSelection(self)

    @property
    def PtpCorrectionFactorError(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror_a796fd71e51214e85d4e3efc9d23ff7c.PtpCorrectionFactorError): An instance of the PtpCorrectionFactorError class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror_a796fd71e51214e85d4e3efc9d23ff7c import PtpCorrectionFactorError
        if len(self._object_properties) > 0:
            if self._properties.get('PtpCorrectionFactorError', None) is not None:
                return self._properties.get('PtpCorrectionFactorError')
        return PtpCorrectionFactorError(self)

    @property
    def PtpSlaveScalability(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability_46be9cd153cad47ed0d8acb04a35bd60.PtpSlaveScalability): An instance of the PtpSlaveScalability class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability_46be9cd153cad47ed0d8acb04a35bd60 import PtpSlaveScalability
        if len(self._object_properties) > 0:
            if self._properties.get('PtpSlaveScalability', None) is not None:
                return self._properties.get('PtpSlaveScalability')
        return PtpSlaveScalability(self)

    @property
    def Rfc2544back2back(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_cfd3f40fbe677cc70482381fc445e21e.Rfc2544back2back): An instance of the Rfc2544back2back class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_cfd3f40fbe677cc70482381fc445e21e import Rfc2544back2back
        if len(self._object_properties) > 0:
            if self._properties.get('Rfc2544back2back', None) is not None:
                return self._properties.get('Rfc2544back2back')
        return Rfc2544back2back(self)

    @property
    def Rfc2544frameLoss(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_868b9746dda2d0cfeed81516cf37d39d.Rfc2544frameLoss): An instance of the Rfc2544frameLoss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_868b9746dda2d0cfeed81516cf37d39d import Rfc2544frameLoss
        if len(self._object_properties) > 0:
            if self._properties.get('Rfc2544frameLoss', None) is not None:
                return self._properties.get('Rfc2544frameLoss')
        return Rfc2544frameLoss(self)

    @property
    def Rfc2544throughput(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_86fc74b3228f97518d2513e6b33a3960.Rfc2544throughput): An instance of the Rfc2544throughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_86fc74b3228f97518d2513e6b33a3960 import Rfc2544throughput
        if len(self._object_properties) > 0:
            if self._properties.get('Rfc2544throughput', None) is not None:
                return self._properties.get('Rfc2544throughput')
        return Rfc2544throughput(self)

    @property
    def Rfc2889broadcastRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate_1f8e1c7f7f9e4d711149db4a572058fb.Rfc2889broadcastRate): An instance of the Rfc2889broadcastRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate_1f8e1c7f7f9e4d711149db4a572058fb import Rfc2889broadcastRate
        if len(self._object_properties) > 0:
            if self._properties.get('Rfc2889broadcastRate', None) is not None:
                return self._properties.get('Rfc2889broadcastRate')
        return Rfc2889broadcastRate(self)

    @property
    def Rfc2889congestionControl(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol_efe62c029fd5ff197d5d57687ac167a6.Rfc2889congestionControl): An instance of the Rfc2889congestionControl class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol_efe62c029fd5ff197d5d57687ac167a6 import Rfc2889congestionControl
        if len(self._object_properties) > 0:
            if self._properties.get('Rfc2889congestionControl', None) is not None:
                return self._properties.get('Rfc2889congestionControl')
        return Rfc2889congestionControl(self)

    @property
    def Rfc2889frameErrorFiltering(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering_56eb932020f20bf8144b92be8a4285f9.Rfc2889frameErrorFiltering): An instance of the Rfc2889frameErrorFiltering class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering_56eb932020f20bf8144b92be8a4285f9 import Rfc2889frameErrorFiltering
        if len(self._object_properties) > 0:
            if self._properties.get('Rfc2889frameErrorFiltering', None) is not None:
                return self._properties.get('Rfc2889frameErrorFiltering')
        return Rfc2889frameErrorFiltering(self)

    @property
    def TrafficTest(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_f399e685b29fd795590f27fffbfa469c.TrafficTest): An instance of the TrafficTest class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_f399e685b29fd795590f27fffbfa469c import TrafficTest
        if len(self._object_properties) > 0:
            if self._properties.get('TrafficTest', None) is not None:
                return self._properties.get('TrafficTest')
        return TrafficTest(self)

    @property
    def Y1564(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.y1564_9b70a4fc765ea18ca465ea775da0fa0b.Y1564): An instance of the Y1564 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.y1564_9b70a4fc765ea18ca465ea775da0fa0b import Y1564
        if len(self._object_properties) > 0:
            if self._properties.get('Y1564', None) is not None:
                return self._properties.get('Y1564')
        return Y1564(self)

    @property
    def RunningTest(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../*]): Returns list containing the currently running QuickTest
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningTest'])

    @property
    def RunningTestObj(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../*]): Returns list containing the currently running QuickTest
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningTestObj'])

    @property
    def TestIds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../*]): Returns list containing the QuickTest test in the configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestIds'])

    def find(self, RunningTest=None, RunningTestObj=None, TestIds=None):
        # type: (List[str], List[str], List[str]) -> QuickTest
        """Finds and retrieves quickTest resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve quickTest resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all quickTest resources from the server.

        Args
        ----
        - RunningTest (list(str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../*])): Returns list containing the currently running QuickTest
        - RunningTestObj (list(str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../*])): Returns list containing the currently running QuickTest
        - TestIds (list(str[None | /api/v1/sessions/1/ixnetwork/quickTest/.../*])): Returns list containing the QuickTest test in the configuration

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
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('loadBatchFile', payload=payload, response_object=None)

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
