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


class AppLibProfile(Base):
    """This object specifies the properties of the particular application traffic profile.
    The AppLibProfile class encapsulates a list of appLibProfile resources that are managed by the user.
    A list of resources can be retrieved from the server using the AppLibProfile.find() method.
    The list can be managed by using the AppLibProfile.add() and AppLibProfile.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'appLibProfile'
    _SDM_ATT_MAP = {
        'AvailableFlows': 'availableFlows',
        'ConfiguredFlows': 'configuredFlows',
        'EnablePerIPStats': 'enablePerIPStats',
        'ObjectiveDistribution': 'objectiveDistribution',
        'ObjectiveType': 'objectiveType',
        'ObjectiveValue': 'objectiveValue',
        'TrafficState': 'trafficState',
    }

    def __init__(self, parent):
        super(AppLibProfile, self).__init__(parent)

    @property
    def AppLibFlow(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.applibflow.AppLibFlow): An instance of the AppLibFlow class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.applibflow import AppLibFlow
        return AppLibFlow(self)

    @property
    def AvailableFlows(self):
        """
        Returns
        -------
        - list(str[]): (Read only) All available application library flows.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableFlows'])

    @property
    def ConfiguredFlows(self):
        """
        Returns
        -------
        - list(str[]): Configured application library flows within profile.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfiguredFlows'])
    @ConfiguredFlows.setter
    def ConfiguredFlows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConfiguredFlows'], value)

    @property
    def EnablePerIPStats(self):
        """
        Returns
        -------
        - bool: Enable Per IP Stats. When true then Per IP statistic drilldown is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePerIPStats'])
    @EnablePerIPStats.setter
    def EnablePerIPStats(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePerIPStats'], value)

    @property
    def ObjectiveDistribution(self):
        """
        Returns
        -------
        - str(applyFullObjectiveToEachPort | splitObjectiveEvenlyAmongPorts): Objective distribution value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectiveDistribution'])
    @ObjectiveDistribution.setter
    def ObjectiveDistribution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ObjectiveDistribution'], value)

    @property
    def ObjectiveType(self):
        """
        Returns
        -------
        - str(simulatedUsers | throughputGbps | throughputKbps | throughputMbps): The objective type of the test.A Test Objective is the way the user sets the actual rate of the Application Library Traffic transmission.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectiveType'])
    @ObjectiveType.setter
    def ObjectiveType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ObjectiveType'], value)

    @property
    def ObjectiveValue(self):
        """
        Returns
        -------
        - number: The absolute value of either simulated users or throughput in its measure unit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectiveValue'])
    @ObjectiveValue.setter
    def ObjectiveValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ObjectiveValue'], value)

    @property
    def TrafficState(self):
        """
        Returns
        -------
        - str(Configured | Interim | Running | Unconfigured): (Read only) A read-only field which indicates the current state of the traffic item.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficState'])

    def update(self, ConfiguredFlows=None, EnablePerIPStats=None, ObjectiveDistribution=None, ObjectiveType=None, ObjectiveValue=None):
        """Updates appLibProfile resource on the server.

        Args
        ----
        - ConfiguredFlows (list(str[])): Configured application library flows within profile.
        - EnablePerIPStats (bool): Enable Per IP Stats. When true then Per IP statistic drilldown is available.
        - ObjectiveDistribution (str(applyFullObjectiveToEachPort | splitObjectiveEvenlyAmongPorts)): Objective distribution value.
        - ObjectiveType (str(simulatedUsers | throughputGbps | throughputKbps | throughputMbps)): The objective type of the test.A Test Objective is the way the user sets the actual rate of the Application Library Traffic transmission.
        - ObjectiveValue (number): The absolute value of either simulated users or throughput in its measure unit.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConfiguredFlows=None, EnablePerIPStats=None, ObjectiveDistribution=None, ObjectiveType=None, ObjectiveValue=None):
        """Adds a new appLibProfile resource on the server and adds it to the container.

        Args
        ----
        - ConfiguredFlows (list(str[])): Configured application library flows within profile.
        - EnablePerIPStats (bool): Enable Per IP Stats. When true then Per IP statistic drilldown is available.
        - ObjectiveDistribution (str(applyFullObjectiveToEachPort | splitObjectiveEvenlyAmongPorts)): Objective distribution value.
        - ObjectiveType (str(simulatedUsers | throughputGbps | throughputKbps | throughputMbps)): The objective type of the test.A Test Objective is the way the user sets the actual rate of the Application Library Traffic transmission.
        - ObjectiveValue (number): The absolute value of either simulated users or throughput in its measure unit.

        Returns
        -------
        - self: This instance with all currently retrieved appLibProfile resources using find and the newly added appLibProfile resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained appLibProfile resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AvailableFlows=None, ConfiguredFlows=None, EnablePerIPStats=None, ObjectiveDistribution=None, ObjectiveType=None, ObjectiveValue=None, TrafficState=None):
        """Finds and retrieves appLibProfile resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve appLibProfile resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all appLibProfile resources from the server.

        Args
        ----
        - AvailableFlows (list(str[])): (Read only) All available application library flows.
        - ConfiguredFlows (list(str[])): Configured application library flows within profile.
        - EnablePerIPStats (bool): Enable Per IP Stats. When true then Per IP statistic drilldown is available.
        - ObjectiveDistribution (str(applyFullObjectiveToEachPort | splitObjectiveEvenlyAmongPorts)): Objective distribution value.
        - ObjectiveType (str(simulatedUsers | throughputGbps | throughputKbps | throughputMbps)): The objective type of the test.A Test Objective is the way the user sets the actual rate of the Application Library Traffic transmission.
        - ObjectiveValue (number): The absolute value of either simulated users or throughput in its measure unit.
        - TrafficState (str(Configured | Interim | Running | Unconfigured)): (Read only) A read-only field which indicates the current state of the traffic item.

        Returns
        -------
        - self: This instance with matching appLibProfile resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of appLibProfile data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the appLibProfile resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddAppLibraryFlow(self, *args, **kwargs):
        """Executes the addAppLibraryFlow operation on the server.

        This exec adds a flow to an application traffic profile.

        addAppLibraryFlow(Arg2=list)
        ----------------------------
        - Arg2 (list(str[])): This object specifies the flow(s) to be added.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('addAppLibraryFlow', payload=payload, response_object=None)

    def AddAppLibraryFlowEx(self, *args, **kwargs):
        """Executes the addAppLibraryFlowEx operation on the server.

        This exec adds a flow to an application traffic profile.

        addAppLibraryFlowEx(Arg2=list)
        ------------------------------
        - Arg2 (list(str)): This object specifies an array of the flow names to be added.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('addAppLibraryFlowEx', payload=payload, response_object=None)

    def DistributeFlowsEvenly(self):
        """Executes the distributeFlowsEvenly operation on the server.

        This exec distributes the percentage for each flow evenly.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('distributeFlowsEvenly', payload=payload, response_object=None)

    def RemoveAppLibraryFlow(self, *args, **kwargs):
        """Executes the removeAppLibraryFlow operation on the server.

        This exec removes a flow from an application traffic profile.

        removeAppLibraryFlow(Arg2=list)
        -------------------------------
        - Arg2 (list(str[])): This object specifies the flow(s) to be removed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('removeAppLibraryFlow', payload=payload, response_object=None)

    def Start(self):
        """Executes the start operation on the server.

        This exec starts running the configured application traffic.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        This exec stops the configured application traffic from running.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
