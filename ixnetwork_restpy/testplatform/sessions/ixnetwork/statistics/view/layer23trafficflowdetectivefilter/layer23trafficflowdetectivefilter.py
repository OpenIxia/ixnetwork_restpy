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


class Layer23TrafficFlowDetectiveFilter(Base):
    """Filters associated with layer23TrafficFlowDetective view.
    The Layer23TrafficFlowDetectiveFilter class encapsulates a list of layer23TrafficFlowDetectiveFilter resources that are managed by the user.
    A list of resources can be retrieved from the server using the Layer23TrafficFlowDetectiveFilter.find() method.
    The list can be managed by using the Layer23TrafficFlowDetectiveFilter.add() and Layer23TrafficFlowDetectiveFilter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'layer23TrafficFlowDetectiveFilter'
    _SDM_ATT_MAP = {
        'DeadFlowsCount': 'deadFlowsCount',
        'DeadFlowsThreshold': 'deadFlowsThreshold',
        'FlowFilterType': 'flowFilterType',
        'PortFilterIds': 'portFilterIds',
        'ShowEgressFlows': 'showEgressFlows',
        'TrafficItemFilterId': 'trafficItemFilterId',
        'TrafficItemFilterIds': 'trafficItemFilterIds',
    }

    def __init__(self, parent):
        super(Layer23TrafficFlowDetectiveFilter, self).__init__(parent)

    @property
    def AllFlowsFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.allflowsfilter.allflowsfilter.AllFlowsFilter): An instance of the AllFlowsFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.allflowsfilter.allflowsfilter import AllFlowsFilter
        return AllFlowsFilter(self)

    @property
    def DeadFlowsFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.deadflowsfilter.deadflowsfilter.DeadFlowsFilter): An instance of the DeadFlowsFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.deadflowsfilter.deadflowsfilter import DeadFlowsFilter
        return DeadFlowsFilter(self)

    @property
    def LiveFlowsFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.liveflowsfilter.liveflowsfilter.LiveFlowsFilter): An instance of the LiveFlowsFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.liveflowsfilter.liveflowsfilter import LiveFlowsFilter
        return LiveFlowsFilter(self)

    @property
    def StatisticFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.statisticfilter.statisticfilter.StatisticFilter): An instance of the StatisticFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.statisticfilter.statisticfilter import StatisticFilter
        return StatisticFilter(self)

    @property
    def TrackingFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.trackingfilter.trackingfilter.TrackingFilter): An instance of the TrackingFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.trackingfilter.trackingfilter import TrackingFilter
        return TrackingFilter(self)

    @property
    def DeadFlowsCount(self):
        """
        Returns
        -------
        - number: The number of flows declared dead. A flow is declared dead if no traffic is received for a specified number of seconds. To change this threshold use the deadFlowsThreshold attribute.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeadFlowsCount'])

    @property
    def DeadFlowsThreshold(self):
        """
        Returns
        -------
        - number: Threshold in seconds after which the flows are declared dead if there are no packets received for a specified number of seconds. This is a global attibute and hence the latest value entered takes precedence over previous values in all the custom views.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeadFlowsThreshold'])
    @DeadFlowsThreshold.setter
    def DeadFlowsThreshold(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DeadFlowsThreshold'], value)

    @property
    def FlowFilterType(self):
        """
        Returns
        -------
        - str(allFlows | deadFlows | liveFlows): Indicates the flow detective filter settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowFilterType'])
    @FlowFilterType.setter
    def FlowFilterType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowFilterType'], value)

    @property
    def PortFilterIds(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter]): Selected port filters from the availablePortFilter list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortFilterIds'])
    @PortFilterIds.setter
    def PortFilterIds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortFilterIds'], value)

    @property
    def ShowEgressFlows(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowEgressFlows'])
    @ShowEgressFlows.setter
    def ShowEgressFlows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowEgressFlows'], value)

    @property
    def TrafficItemFilterId(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter): Selected traffic flow detective filter from the availableTrafficItemFilter list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficItemFilterId'])
    @TrafficItemFilterId.setter
    def TrafficItemFilterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficItemFilterId'], value)

    @property
    def TrafficItemFilterIds(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter]): Selected traffic item filters from the availableTrafficItemFilter list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficItemFilterIds'])
    @TrafficItemFilterIds.setter
    def TrafficItemFilterIds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficItemFilterIds'], value)

    def update(self, DeadFlowsThreshold=None, FlowFilterType=None, PortFilterIds=None, ShowEgressFlows=None, TrafficItemFilterId=None, TrafficItemFilterIds=None):
        """Updates layer23TrafficFlowDetectiveFilter resource on the server.

        Args
        ----
        - DeadFlowsThreshold (number): Threshold in seconds after which the flows are declared dead if there are no packets received for a specified number of seconds. This is a global attibute and hence the latest value entered takes precedence over previous values in all the custom views.
        - FlowFilterType (str(allFlows | deadFlows | liveFlows)): Indicates the flow detective filter settings.
        - PortFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter])): Selected port filters from the availablePortFilter list.
        - ShowEgressFlows (bool): NOT DEFINED
        - TrafficItemFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter)): Selected traffic flow detective filter from the availableTrafficItemFilter list.
        - TrafficItemFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter])): Selected traffic item filters from the availableTrafficItemFilter list.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DeadFlowsThreshold=None, FlowFilterType=None, PortFilterIds=None, ShowEgressFlows=None, TrafficItemFilterId=None, TrafficItemFilterIds=None):
        """Adds a new layer23TrafficFlowDetectiveFilter resource on the server and adds it to the container.

        Args
        ----
        - DeadFlowsThreshold (number): Threshold in seconds after which the flows are declared dead if there are no packets received for a specified number of seconds. This is a global attibute and hence the latest value entered takes precedence over previous values in all the custom views.
        - FlowFilterType (str(allFlows | deadFlows | liveFlows)): Indicates the flow detective filter settings.
        - PortFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter])): Selected port filters from the availablePortFilter list.
        - ShowEgressFlows (bool): NOT DEFINED
        - TrafficItemFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter)): Selected traffic flow detective filter from the availableTrafficItemFilter list.
        - TrafficItemFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter])): Selected traffic item filters from the availableTrafficItemFilter list.

        Returns
        -------
        - self: This instance with all currently retrieved layer23TrafficFlowDetectiveFilter resources using find and the newly added layer23TrafficFlowDetectiveFilter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained layer23TrafficFlowDetectiveFilter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DeadFlowsCount=None, DeadFlowsThreshold=None, FlowFilterType=None, PortFilterIds=None, ShowEgressFlows=None, TrafficItemFilterId=None, TrafficItemFilterIds=None):
        """Finds and retrieves layer23TrafficFlowDetectiveFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve layer23TrafficFlowDetectiveFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all layer23TrafficFlowDetectiveFilter resources from the server.

        Args
        ----
        - DeadFlowsCount (number): The number of flows declared dead. A flow is declared dead if no traffic is received for a specified number of seconds. To change this threshold use the deadFlowsThreshold attribute.
        - DeadFlowsThreshold (number): Threshold in seconds after which the flows are declared dead if there are no packets received for a specified number of seconds. This is a global attibute and hence the latest value entered takes precedence over previous values in all the custom views.
        - FlowFilterType (str(allFlows | deadFlows | liveFlows)): Indicates the flow detective filter settings.
        - PortFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter])): Selected port filters from the availablePortFilter list.
        - ShowEgressFlows (bool): NOT DEFINED
        - TrafficItemFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter)): Selected traffic flow detective filter from the availableTrafficItemFilter list.
        - TrafficItemFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter])): Selected traffic item filters from the availableTrafficItemFilter list.

        Returns
        -------
        - self: This instance with matching layer23TrafficFlowDetectiveFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of layer23TrafficFlowDetectiveFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the layer23TrafficFlowDetectiveFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
