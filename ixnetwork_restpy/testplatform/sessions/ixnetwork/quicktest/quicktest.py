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
    def RunningTest(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/30/ixnetwork/quickTest/.../*]): Returns list containing the currently running QuickTest
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningTest'])

    @property
    def RunningTestObj(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/30/ixnetwork/quickTest/.../*]): Returns list containing the currently running QuickTest
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningTestObj'])

    @property
    def TestIds(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/30/ixnetwork/quickTest/.../*]): Returns list containing the QuickTest test in the configuration
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
