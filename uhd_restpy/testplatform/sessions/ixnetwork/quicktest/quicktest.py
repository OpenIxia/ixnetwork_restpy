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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


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
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss_23e9ec9c789cfca78365ee935c3c3488.AsymmetricFrameLoss): An instance of the AsymmetricFrameLoss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricframeloss_23e9ec9c789cfca78365ee935c3c3488 import AsymmetricFrameLoss
        return AsymmetricFrameLoss(self)

    @property
    def AsymmetricThroughput(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput_b9e3c6717e2faf761c693cccff9c71b8.AsymmetricThroughput): An instance of the AsymmetricThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.asymmetricthroughput_b9e3c6717e2faf761c693cccff9c71b8 import AsymmetricThroughput
        return AsymmetricThroughput(self)

    @property
    def CloudPerf(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf_354bfb3429a11911999c2a796c4a9c1c.CloudPerf): An instance of the CloudPerf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.cloudperf_354bfb3429a11911999c2a796c4a9c1c import CloudPerf
        return CloudPerf(self)

    @property
    def CustomContDuration(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration_afd0ec7957951071cbe4070215782b68.CustomContDuration): An instance of the CustomContDuration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customcontduration_afd0ec7957951071cbe4070215782b68 import CustomContDuration
        return CustomContDuration(self)

    @property
    def CustomFixedDuration(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration_9a6f20f065966a060e70d9d3098af43b.CustomFixedDuration): An instance of the CustomFixedDuration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customfixedduration_9a6f20f065966a060e70d9d3098af43b import CustomFixedDuration
        return CustomFixedDuration(self)

    @property
    def CustomStep(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customstep_2a6f0cec52fe41c2c67188afbd8bdcdc.CustomStep): An instance of the CustomStep class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customstep_2a6f0cec52fe41c2c67188afbd8bdcdc import CustomStep
        return CustomStep(self)

    @property
    def CustomThroughput(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput_97500fff3f335c6329b02f39f0ad94f4.CustomThroughput): An instance of the CustomThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.customthroughput_97500fff3f335c6329b02f39f0ad94f4 import CustomThroughput
        return CustomThroughput(self)

    @property
    def DhcpRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate_a1d50c13e49087adee284d9705f20ea9.DhcpRate): An instance of the DhcpRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dhcprate_a1d50c13e49087adee284d9705f20ea9 import DhcpRate
        return DhcpRate(self)

    @property
    def Dhcpv6Rate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate_17ca1fc0e1ab7156c518d207263c2755.Dhcpv6Rate): An instance of the Dhcpv6Rate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dhcpv6rate_17ca1fc0e1ab7156c518d207263c2755 import Dhcpv6Rate
        return Dhcpv6Rate(self)

    @property
    def Dot1xCapacity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity_ddddaeb52f72ebee3e8c89bb27e5a9bd.Dot1xCapacity): An instance of the Dot1xCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xcapacity_ddddaeb52f72ebee3e8c89bb27e5a9bd import Dot1xCapacity
        return Dot1xCapacity(self)

    @property
    def Dot1xRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate_920cbb0c4f9de176a44b8d1eec6d1654.Dot1xRate): An instance of the Dot1xRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.dot1xrate_920cbb0c4f9de176a44b8d1eec6d1654 import Dot1xRate
        return Dot1xRate(self)

    @property
    def EventScheduler(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler_1adeddd0d2588a7b6a2bb0dfa0dbbbd5.EventScheduler): An instance of the EventScheduler class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.eventscheduler_1adeddd0d2588a7b6a2bb0dfa0dbbbd5 import EventScheduler
        return EventScheduler(self)

    @property
    def FcoeMaxNoDropThroughput(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput_5a8b5a2dd7200e911f9e2cc4e02d9cdf.FcoeMaxNoDropThroughput): An instance of the FcoeMaxNoDropThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnodropthroughput_5a8b5a2dd7200e911f9e2cc4e02d9cdf import FcoeMaxNoDropThroughput
        return FcoeMaxNoDropThroughput(self)

    @property
    def FcoeMaxNoPauseThroughput(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput_5c5bcb306f8c2ea47dbeb4bd93f05b4a.FcoeMaxNoPauseThroughput): An instance of the FcoeMaxNoPauseThroughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.fcoemaxnopausethroughput_5c5bcb306f8c2ea47dbeb4bd93f05b4a import FcoeMaxNoPauseThroughput
        return FcoeMaxNoPauseThroughput(self)

    @property
    def Globals(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.globals_189e36988976210137e69f36458134c2.Globals): An instance of the Globals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.globals_189e36988976210137e69f36458134c2 import Globals
        return Globals(self)._select()

    @property
    def IptvChannelZapping(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping_f76f09e6cca53cc063af4a62acaad345.IptvChannelZapping): An instance of the IptvChannelZapping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannelzapping_f76f09e6cca53cc063af4a62acaad345 import IptvChannelZapping
        return IptvChannelZapping(self)

    @property
    def L2tpRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate_3f836413e8c133cd9b3153b0ece79355.L2tpRate): An instance of the L2tpRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.l2tprate_3f836413e8c133cd9b3153b0ece79355 import L2tpRate
        return L2tpRate(self)

    @property
    def OpenFlowFailoverPerformance(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance_497acfbd872605986ec31fac8a22909e.OpenFlowFailoverPerformance): An instance of the OpenFlowFailoverPerformance class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowfailoverperformance_497acfbd872605986ec31fac8a22909e import OpenFlowFailoverPerformance
        return OpenFlowFailoverPerformance(self)

    @property
    def OpenFlowLayer2LearningRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate_3db88746f7f375303f2eda376386a9a8.OpenFlowLayer2LearningRate): An instance of the OpenFlowLayer2LearningRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer2learningrate_3db88746f7f375303f2eda376386a9a8 import OpenFlowLayer2LearningRate
        return OpenFlowLayer2LearningRate(self)

    @property
    def OpenFlowLayer3LearningRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate_3d5fc2ac25caa8bc279f7dd74cb1ebb4.OpenFlowLayer3LearningRate): An instance of the OpenFlowLayer3LearningRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowlayer3learningrate_3d5fc2ac25caa8bc279f7dd74cb1ebb4 import OpenFlowLayer3LearningRate
        return OpenFlowLayer3LearningRate(self)

    @property
    def OpenFlowTableCapacity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity_ede63934d6923146dc0eff0fec6a3023.OpenFlowTableCapacity): An instance of the OpenFlowTableCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.openflowtablecapacity_ede63934d6923146dc0eff0fec6a3023 import OpenFlowTableCapacity
        return OpenFlowTableCapacity(self)

    @property
    def PppServerCapacity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity_af2ef3e74eab82cea91b425ee7119872.PppServerCapacity): An instance of the PppServerCapacity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.pppservercapacity_af2ef3e74eab82cea91b425ee7119872 import PppServerCapacity
        return PppServerCapacity(self)

    @property
    def PppSessionRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate_3c902892c18a09c0398be23c0a97ef85.PppSessionRate): An instance of the PppSessionRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.pppsessionrate_3c902892c18a09c0398be23c0a97ef85 import PppSessionRate
        return PppSessionRate(self)

    @property
    def PtpBestMasterSelection(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection_bd6cd77082c14a379f852945024f02c5.PtpBestMasterSelection): An instance of the PtpBestMasterSelection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.ptpbestmasterselection_bd6cd77082c14a379f852945024f02c5 import PtpBestMasterSelection
        return PtpBestMasterSelection(self)

    @property
    def PtpCorrectionFactorError(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror_6ee1b2ad82283aaeee35905a0a1ed5dc.PtpCorrectionFactorError): An instance of the PtpCorrectionFactorError class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.ptpcorrectionfactorerror_6ee1b2ad82283aaeee35905a0a1ed5dc import PtpCorrectionFactorError
        return PtpCorrectionFactorError(self)

    @property
    def PtpSlaveScalability(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability_6510fa33eea238d2b2963267efeca729.PtpSlaveScalability): An instance of the PtpSlaveScalability class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.ptpslavescalability_6510fa33eea238d2b2963267efeca729 import PtpSlaveScalability
        return PtpSlaveScalability(self)

    @property
    def Rfc2544back2back(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_98477f12f665b89fbc05f63bb31ee827.Rfc2544back2back): An instance of the Rfc2544back2back class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544back2back_98477f12f665b89fbc05f63bb31ee827 import Rfc2544back2back
        return Rfc2544back2back(self)

    @property
    def Rfc2544frameLoss(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_f6a794f7d6a00f8572021fc418d8807f.Rfc2544frameLoss): An instance of the Rfc2544frameLoss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544frameloss_f6a794f7d6a00f8572021fc418d8807f import Rfc2544frameLoss
        return Rfc2544frameLoss(self)

    @property
    def Rfc2544throughput(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_5a77c9a28f5fa2bb9ce9f4280eb5122f.Rfc2544throughput): An instance of the Rfc2544throughput class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2544throughput_5a77c9a28f5fa2bb9ce9f4280eb5122f import Rfc2544throughput
        return Rfc2544throughput(self)

    @property
    def Rfc2889broadcastRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate_1309c81b5bb27d5345ac1823c48958d6.Rfc2889broadcastRate): An instance of the Rfc2889broadcastRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889broadcastrate_1309c81b5bb27d5345ac1823c48958d6 import Rfc2889broadcastRate
        return Rfc2889broadcastRate(self)

    @property
    def Rfc2889congestionControl(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol_2e3ba8b814e3177aeefdef4c3ba3957f.Rfc2889congestionControl): An instance of the Rfc2889congestionControl class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889congestioncontrol_2e3ba8b814e3177aeefdef4c3ba3957f import Rfc2889congestionControl
        return Rfc2889congestionControl(self)

    @property
    def Rfc2889frameErrorFiltering(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering_bbdf8e68236e7582480e73591a3c427f.Rfc2889frameErrorFiltering): An instance of the Rfc2889frameErrorFiltering class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.rfc2889frameerrorfiltering_bbdf8e68236e7582480e73591a3c427f import Rfc2889frameErrorFiltering
        return Rfc2889frameErrorFiltering(self)

    @property
    def TrafficTest(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_9709f3566877e5d5fb6ae115268058c6.TrafficTest): An instance of the TrafficTest class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.traffictest_9709f3566877e5d5fb6ae115268058c6 import TrafficTest
        return TrafficTest(self)

    @property
    def Y1564(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.quicktest.y1564_6674f9c7023c1667145343e451a0128c.Y1564): An instance of the Y1564 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.quicktest.y1564_6674f9c7023c1667145343e451a0128c import Y1564
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
