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
    """The IxNetwork Test Configuration feature provides the ability to run predefined tests and allows the user to set some global test parameters for the individual test types.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'
    _SDM_ATT_MAP = {
        'AutomaticEnableIptvStats': 'automaticEnableIptvStats',
        'BackgroundTrafficEnabled': 'backgroundTrafficEnabled',
        'Duration': 'duration',
        'EnableJoinFailuresMode': 'enableJoinFailuresMode',
        'EnableLeaveFailuresMode': 'enableLeaveFailuresMode',
        'LoadType': 'loadType',
        'Numtrials': 'numtrials',
        'PassCriteriaJoinFailuresValue': 'passCriteriaJoinFailuresValue',
        'PassCriteriaJoinLatencyValue': 'passCriteriaJoinLatencyValue',
        'PassCriteriaLeaveFailuresValue': 'passCriteriaLeaveFailuresValue',
        'PassCriteriaLeaveLatencyValue': 'passCriteriaLeaveLatencyValue',
        'ProtocolItem': 'protocolItem',
        'StartIptvEndpointsBeforeTraffic': 'startIptvEndpointsBeforeTraffic',
        'TestTrafficType': 'testTrafficType',
        'TrackByEgressVlanId': 'trackByEgressVlanId',
        'TrackByFlowGroup': 'trackByFlowGroup',
        'TrackByIpDestination': 'trackByIpDestination',
    }

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def AutomaticEnableIptvStats(self):
        """
        Returns
        -------
        - str: If true, enables the automatic Iptv Statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutomaticEnableIptvStats'])
    @AutomaticEnableIptvStats.setter
    def AutomaticEnableIptvStats(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutomaticEnableIptvStats'], value)

    @property
    def BackgroundTrafficEnabled(self):
        """
        Returns
        -------
        - str: If true, the traffic in background is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BackgroundTrafficEnabled'])
    @BackgroundTrafficEnabled.setter
    def BackgroundTrafficEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BackgroundTrafficEnabled'], value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: Period of time over which the configured IPTV subscribers and multicast traffic sources execute the configured behavior.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])
    @Duration.setter
    def Duration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Duration'], value)

    @property
    def EnableJoinFailuresMode(self):
        """
        Returns
        -------
        - str: If true, Failure Mode for Joined state is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableJoinFailuresMode'])
    @EnableJoinFailuresMode.setter
    def EnableJoinFailuresMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableJoinFailuresMode'], value)

    @property
    def EnableLeaveFailuresMode(self):
        """
        Returns
        -------
        - str: If true, Failure Mode for Leave state is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLeaveFailuresMode'])
    @EnableLeaveFailuresMode.setter
    def EnableLeaveFailuresMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLeaveFailuresMode'], value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(custom): The type of load used to modify the variable parameter value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoadType'])
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoadType'], value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: The number of trials that can be run for the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Numtrials'])
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Numtrials'], value)

    @property
    def PassCriteriaJoinFailuresValue(self):
        """
        Returns
        -------
        - number: Denotes the value of Join actions marked as failed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PassCriteriaJoinFailuresValue'])
    @PassCriteriaJoinFailuresValue.setter
    def PassCriteriaJoinFailuresValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PassCriteriaJoinFailuresValue'], value)

    @property
    def PassCriteriaJoinLatencyValue(self):
        """
        Returns
        -------
        - number: The amount of time, in milliseconds, elapsed between the time the client sent an IGMP JOIN (broadcast channel) and the time it received the first byte of data.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PassCriteriaJoinLatencyValue'])
    @PassCriteriaJoinLatencyValue.setter
    def PassCriteriaJoinLatencyValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PassCriteriaJoinLatencyValue'], value)

    @property
    def PassCriteriaLeaveFailuresValue(self):
        """
        Returns
        -------
        - number: How many Leave actions were marked as Failed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PassCriteriaLeaveFailuresValue'])
    @PassCriteriaLeaveFailuresValue.setter
    def PassCriteriaLeaveFailuresValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PassCriteriaLeaveFailuresValue'], value)

    @property
    def PassCriteriaLeaveLatencyValue(self):
        """
        Returns
        -------
        - number: The amount of time, in milliseconds, elapsed between the time the client sent an IGMP LEAVE (broadcast channel) and the time it received the last byte of data.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PassCriteriaLeaveLatencyValue'])
    @PassCriteriaLeaveLatencyValue.setter
    def PassCriteriaLeaveLatencyValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PassCriteriaLeaveLatencyValue'], value)

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
    def StartIptvEndpointsBeforeTraffic(self):
        """
        Returns
        -------
        - str: The IPTV Endpoints are set before sending traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartIptvEndpointsBeforeTraffic'])
    @StartIptvEndpointsBeforeTraffic.setter
    def StartIptvEndpointsBeforeTraffic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartIptvEndpointsBeforeTraffic'], value)

    @property
    def TestTrafficType(self):
        """
        Returns
        -------
        - str: Indicates the type of traffic to be tested.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestTrafficType'])
    @TestTrafficType.setter
    def TestTrafficType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TestTrafficType'], value)

    @property
    def TrackByEgressVlanId(self):
        """
        Returns
        -------
        - str: If true, Custom Offset from Packet Locations can be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrackByEgressVlanId'])
    @TrackByEgressVlanId.setter
    def TrackByEgressVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrackByEgressVlanId'], value)

    @property
    def TrackByFlowGroup(self):
        """
        Returns
        -------
        - str: It configures flow tracking for all flow groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrackByFlowGroup'])
    @TrackByFlowGroup.setter
    def TrackByFlowGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrackByFlowGroup'], value)

    @property
    def TrackByIpDestination(self):
        """
        Returns
        -------
        - str: If true, flows are tracked by the IPv4 Destination Address as per the route ranges configured under destination endpoint.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrackByIpDestination'])
    @TrackByIpDestination.setter
    def TrackByIpDestination(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrackByIpDestination'], value)

    def update(self, AutomaticEnableIptvStats=None, BackgroundTrafficEnabled=None, Duration=None, EnableJoinFailuresMode=None, EnableLeaveFailuresMode=None, LoadType=None, Numtrials=None, PassCriteriaJoinFailuresValue=None, PassCriteriaJoinLatencyValue=None, PassCriteriaLeaveFailuresValue=None, PassCriteriaLeaveLatencyValue=None, ProtocolItem=None, StartIptvEndpointsBeforeTraffic=None, TestTrafficType=None, TrackByEgressVlanId=None, TrackByFlowGroup=None, TrackByIpDestination=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - AutomaticEnableIptvStats (str): If true, enables the automatic Iptv Statistics.
        - BackgroundTrafficEnabled (str): If true, the traffic in background is enabled.
        - Duration (number): Period of time over which the configured IPTV subscribers and multicast traffic sources execute the configured behavior.
        - EnableJoinFailuresMode (str): If true, Failure Mode for Joined state is enabled.
        - EnableLeaveFailuresMode (str): If true, Failure Mode for Leave state is enabled.
        - LoadType (str(custom)): The type of load used to modify the variable parameter value.
        - Numtrials (number): The number of trials that can be run for the test.
        - PassCriteriaJoinFailuresValue (number): Denotes the value of Join actions marked as failed.
        - PassCriteriaJoinLatencyValue (number): The amount of time, in milliseconds, elapsed between the time the client sent an IGMP JOIN (broadcast channel) and the time it received the first byte of data.
        - PassCriteriaLeaveFailuresValue (number): How many Leave actions were marked as Failed.
        - PassCriteriaLeaveLatencyValue (number): The amount of time, in milliseconds, elapsed between the time the client sent an IGMP LEAVE (broadcast channel) and the time it received the last byte of data.
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - StartIptvEndpointsBeforeTraffic (str): The IPTV Endpoints are set before sending traffic.
        - TestTrafficType (str): Indicates the type of traffic to be tested.
        - TrackByEgressVlanId (str): If true, Custom Offset from Packet Locations can be configured.
        - TrackByFlowGroup (str): It configures flow tracking for all flow groups.
        - TrackByIpDestination (str): If true, flows are tracked by the IPv4 Destination Address as per the route ranges configured under destination endpoint.

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
