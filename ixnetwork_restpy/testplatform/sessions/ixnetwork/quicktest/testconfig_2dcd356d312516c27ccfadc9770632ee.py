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


class TestConfig(Base):
    """
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'CustomLoadUnit': 'customLoadUnit',
        'DataPlaneJitterWindow': 'dataPlaneJitterWindow',
        'EnableBFD': 'enableBFD',
        'EnableTolerance': 'enableTolerance',
        'FailoverMode': 'failoverMode',
        'FailoverPortIndex': 'failoverPortIndex',
        'FailoverScheduling': 'failoverScheduling',
        'FixedFrameSize': 'fixedFrameSize',
        'ForceContinuosTraffic': 'forceContinuosTraffic',
        'FrameSizeMode': 'frameSizeMode',
        'Framesize': 'framesize',
        'HoldDownTimer': 'holdDownTimer',
        'IpRatioMode': 'ipRatioMode',
        'Ipv4rate': 'ipv4rate',
        'Ipv6rate': 'ipv6rate',
        'LoadRateValue': 'loadRateValue',
        'LoadType': 'loadType',
        'NetworkGroupRoutesType': 'networkGroupRoutesType',
        'NetworkGroupSizeListIpv4': 'networkGroupSizeListIpv4',
        'NetworkGroupSizeListIpv6': 'networkGroupSizeListIpv6',
        'NetworkGroupSizeModeIpv4': 'networkGroupSizeModeIpv4',
        'NetworkGroupSizeModeIpv6': 'networkGroupSizeModeIpv6',
        'Numtrials': 'numtrials',
        'ProtocolItem': 'protocolItem',
        'ReportConvergenceUnit': 'reportConvergenceUnit',
        'ReportPacketLossDurationUnit': 'reportPacketLossDurationUnit',
        'RoutesDistribution': 'routesDistribution',
        'TestMethodology': 'testMethodology',
        'TestTrafficType': 'testTrafficType',
        'Threshold': 'threshold',
        'TimeoutAfterFailover': 'timeoutAfterFailover',
        'TimeoutBeforeFailover': 'timeoutBeforeFailover',
        'Tolerance': 'tolerance',
        'TrafficType': 'trafficType',
    }

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def CustomLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomLoadUnit'])
    @CustomLoadUnit.setter
    def CustomLoadUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomLoadUnit'], value)

    @property
    def DataPlaneJitterWindow(self):
        """
        Returns
        -------
        - str(k_10485760 | k_1310720 | k_167772160 | k_20971520 | k_2621440 | k_335544320 | k_41943040 | k_5242880 | k_671088640 | k_83886080): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPlaneJitterWindow'])
    @DataPlaneJitterWindow.setter
    def DataPlaneJitterWindow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DataPlaneJitterWindow'], value)

    @property
    def EnableBFD(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBFD'])
    @EnableBFD.setter
    def EnableBFD(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBFD'], value)

    @property
    def EnableTolerance(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableTolerance'])
    @EnableTolerance.setter
    def EnableTolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableTolerance'], value)

    @property
    def FailoverMode(self):
        """
        Returns
        -------
        - str(portDown | withdrawRoutes): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FailoverMode'])
    @FailoverMode.setter
    def FailoverMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FailoverMode'], value)

    @property
    def FailoverPortIndex(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FailoverPortIndex'])
    @FailoverPortIndex.setter
    def FailoverPortIndex(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FailoverPortIndex'], value)

    @property
    def FailoverScheduling(self):
        """
        Returns
        -------
        - str(singleLinkMultiplePortsSequential | singleLinkSinglePort | singleLinkSinglePortSequential): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FailoverScheduling'])
    @FailoverScheduling.setter
    def FailoverScheduling(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FailoverScheduling'], value)

    @property
    def FixedFrameSize(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FixedFrameSize'])
    @FixedFrameSize.setter
    def FixedFrameSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FixedFrameSize'], value)

    @property
    def ForceContinuosTraffic(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceContinuosTraffic'])
    @ForceContinuosTraffic.setter
    def ForceContinuosTraffic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForceContinuosTraffic'], value)

    @property
    def FrameSizeMode(self):
        """
        Returns
        -------
        - str(fixed): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeMode'])
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeMode'], value)

    @property
    def Framesize(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Framesize'])
    @Framesize.setter
    def Framesize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Framesize'], value)

    @property
    def HoldDownTimer(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['HoldDownTimer'])
    @HoldDownTimer.setter
    def HoldDownTimer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HoldDownTimer'], value)

    @property
    def IpRatioMode(self):
        """
        Returns
        -------
        - str(custom | fixed | increment | random): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpRatioMode'])
    @IpRatioMode.setter
    def IpRatioMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpRatioMode'], value)

    @property
    def Ipv4rate(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4rate'])
    @Ipv4rate.setter
    def Ipv4rate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4rate'], value)

    @property
    def Ipv6rate(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6rate'])
    @Ipv6rate.setter
    def Ipv6rate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6rate'], value)

    @property
    def LoadRateValue(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadRateValue'])
    @LoadRateValue.setter
    def LoadRateValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadRateValue'], value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadType'])
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadType'], value)

    @property
    def NetworkGroupRoutesType(self):
        """
        Returns
        -------
        - str(ipv4 | ipv4/ipv6 | ipv6): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkGroupRoutesType'])
    @NetworkGroupRoutesType.setter
    def NetworkGroupRoutesType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkGroupRoutesType'], value)

    @property
    def NetworkGroupSizeListIpv4(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkGroupSizeListIpv4'])
    @NetworkGroupSizeListIpv4.setter
    def NetworkGroupSizeListIpv4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkGroupSizeListIpv4'], value)

    @property
    def NetworkGroupSizeListIpv6(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkGroupSizeListIpv6'])
    @NetworkGroupSizeListIpv6.setter
    def NetworkGroupSizeListIpv6(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkGroupSizeListIpv6'], value)

    @property
    def NetworkGroupSizeModeIpv4(self):
        """
        Returns
        -------
        - str(custom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkGroupSizeModeIpv4'])
    @NetworkGroupSizeModeIpv4.setter
    def NetworkGroupSizeModeIpv4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkGroupSizeModeIpv4'], value)

    @property
    def NetworkGroupSizeModeIpv6(self):
        """
        Returns
        -------
        - str(custom): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkGroupSizeModeIpv6'])
    @NetworkGroupSizeModeIpv6.setter
    def NetworkGroupSizeModeIpv6(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkGroupSizeModeIpv6'], value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def ProtocolItem(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan]): Protocol Items
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolItem'])
    @ProtocolItem.setter
    def ProtocolItem(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolItem'], value)

    @property
    def ReportConvergenceUnit(self):
        """
        Returns
        -------
        - str(ms | s | us): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportConvergenceUnit'])
    @ReportConvergenceUnit.setter
    def ReportConvergenceUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReportConvergenceUnit'], value)

    @property
    def ReportPacketLossDurationUnit(self):
        """
        Returns
        -------
        - str(ms): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportPacketLossDurationUnit'])
    @ReportPacketLossDurationUnit.setter
    def ReportPacketLossDurationUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReportPacketLossDurationUnit'], value)

    @property
    def RoutesDistribution(self):
        """
        Returns
        -------
        - str(equalCostOnEachPort): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RoutesDistribution'])
    @RoutesDistribution.setter
    def RoutesDistribution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RoutesDistribution'], value)

    @property
    def TestMethodology(self):
        """
        Returns
        -------
        - str(packetLossDuration | trueViewConvergence): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestMethodology'])
    @TestMethodology.setter
    def TestMethodology(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestMethodology'], value)

    @property
    def TestTrafficType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestTrafficType'])
    @TestTrafficType.setter
    def TestTrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestTrafficType'], value)

    @property
    def Threshold(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Threshold'])
    @Threshold.setter
    def Threshold(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Threshold'], value)

    @property
    def TimeoutAfterFailover(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeoutAfterFailover'])
    @TimeoutAfterFailover.setter
    def TimeoutAfterFailover(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimeoutAfterFailover'], value)

    @property
    def TimeoutBeforeFailover(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeoutBeforeFailover'])
    @TimeoutBeforeFailover.setter
    def TimeoutBeforeFailover(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimeoutBeforeFailover'], value)

    @property
    def Tolerance(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tolerance'])
    @Tolerance.setter
    def Tolerance(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Tolerance'], value)

    @property
    def TrafficType(self):
        """
        Returns
        -------
        - str(burstyLoading | constantLoading): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficType'])
    @TrafficType.setter
    def TrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficType'], value)

    def update(self, CustomLoadUnit=None, DataPlaneJitterWindow=None, EnableBFD=None, EnableTolerance=None, FailoverMode=None, FailoverPortIndex=None, FailoverScheduling=None, FixedFrameSize=None, ForceContinuosTraffic=None, FrameSizeMode=None, Framesize=None, HoldDownTimer=None, IpRatioMode=None, Ipv4rate=None, Ipv6rate=None, LoadRateValue=None, LoadType=None, NetworkGroupRoutesType=None, NetworkGroupSizeListIpv4=None, NetworkGroupSizeListIpv6=None, NetworkGroupSizeModeIpv4=None, NetworkGroupSizeModeIpv6=None, Numtrials=None, ProtocolItem=None, ReportConvergenceUnit=None, ReportPacketLossDurationUnit=None, RoutesDistribution=None, TestMethodology=None, TestTrafficType=None, Threshold=None, TimeoutAfterFailover=None, TimeoutBeforeFailover=None, Tolerance=None, TrafficType=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - CustomLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): 
        - DataPlaneJitterWindow (str(k_10485760 | k_1310720 | k_167772160 | k_20971520 | k_2621440 | k_335544320 | k_41943040 | k_5242880 | k_671088640 | k_83886080)): 
        - EnableBFD (bool): 
        - EnableTolerance (bool): 
        - FailoverMode (str(portDown | withdrawRoutes)): 
        - FailoverPortIndex (str): 
        - FailoverScheduling (str(singleLinkMultiplePortsSequential | singleLinkSinglePort | singleLinkSinglePortSequential)): 
        - FixedFrameSize (number): 
        - ForceContinuosTraffic (bool): 
        - FrameSizeMode (str(fixed)): 
        - Framesize (str): 
        - HoldDownTimer (number): 
        - IpRatioMode (str(custom | fixed | increment | random)): 
        - Ipv4rate (number): 
        - Ipv6rate (number): 
        - LoadRateValue (number): 
        - LoadType (str(binary | combo | custom | fixed | increment | quickSearch | random | step | unchanged)): 
        - NetworkGroupRoutesType (str(ipv4 | ipv4/ipv6 | ipv6)): 
        - NetworkGroupSizeListIpv4 (list(str)): 
        - NetworkGroupSizeListIpv6 (list(str)): 
        - NetworkGroupSizeModeIpv4 (str(custom)): 
        - NetworkGroupSizeModeIpv6 (str(custom)): 
        - Numtrials (number): 
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - ReportConvergenceUnit (str(ms | s | us)): 
        - ReportPacketLossDurationUnit (str(ms)): 
        - RoutesDistribution (str(equalCostOnEachPort)): 
        - TestMethodology (str(packetLossDuration | trueViewConvergence)): 
        - TestTrafficType (str): 
        - Threshold (number): 
        - TimeoutAfterFailover (number): 
        - TimeoutBeforeFailover (number): 
        - Tolerance (number): 
        - TrafficType (str(burstyLoading | constantLoading)): 

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
