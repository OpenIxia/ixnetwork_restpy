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


class Layer23TrafficFlowFilter(Base):
    """Filters associated with layer23TrafficFlow view.
    The Layer23TrafficFlowFilter class encapsulates a list of layer23TrafficFlowFilter resources that are managed by the user.
    A list of resources can be retrieved from the server using the Layer23TrafficFlowFilter.find() method.
    The list can be managed by using the Layer23TrafficFlowFilter.add() and Layer23TrafficFlowFilter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'layer23TrafficFlowFilter'
    _SDM_ATT_MAP = {
        'AggregatedAcrossPorts': 'aggregatedAcrossPorts',
        'EgressLatencyBinDisplayOption': 'egressLatencyBinDisplayOption',
        'PortFilterIds': 'portFilterIds',
        'TrafficItemFilterId': 'trafficItemFilterId',
        'TrafficItemFilterIds': 'trafficItemFilterIds',
    }

    def __init__(self, parent):
        super(Layer23TrafficFlowFilter, self).__init__(parent)

    @property
    def EnumerationFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.enumerationfilter.enumerationfilter.EnumerationFilter): An instance of the EnumerationFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.enumerationfilter.enumerationfilter import EnumerationFilter
        return EnumerationFilter(self)

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
    def AggregatedAcrossPorts(self):
        """
        Returns
        -------
        - bool: If true, displays aggregated stat value across ports selected by portFilterIds. Default = false
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregatedAcrossPorts'])
    @AggregatedAcrossPorts.setter
    def AggregatedAcrossPorts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregatedAcrossPorts'], value)

    @property
    def EgressLatencyBinDisplayOption(self):
        """
        Returns
        -------
        - str(none | showEgressFlatView | showEgressRows | showLatencyBinStats): Emulates Latency Bin SV or Egress Tracking SV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EgressLatencyBinDisplayOption'])
    @EgressLatencyBinDisplayOption.setter
    def EgressLatencyBinDisplayOption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EgressLatencyBinDisplayOption'], value)

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
    def TrafficItemFilterId(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter): Selected traffic item filter from the availableTrafficItemFilter list.
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

    def update(self, AggregatedAcrossPorts=None, EgressLatencyBinDisplayOption=None, PortFilterIds=None, TrafficItemFilterId=None, TrafficItemFilterIds=None):
        """Updates layer23TrafficFlowFilter resource on the server.

        Args
        ----
        - AggregatedAcrossPorts (bool): If true, displays aggregated stat value across ports selected by portFilterIds. Default = false
        - EgressLatencyBinDisplayOption (str(none | showEgressFlatView | showEgressRows | showLatencyBinStats)): Emulates Latency Bin SV or Egress Tracking SV.
        - PortFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter])): Selected port filters from the availablePortFilter list.
        - TrafficItemFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter)): Selected traffic item filter from the availableTrafficItemFilter list.
        - TrafficItemFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter])): Selected traffic item filters from the availableTrafficItemFilter list.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AggregatedAcrossPorts=None, EgressLatencyBinDisplayOption=None, PortFilterIds=None, TrafficItemFilterId=None, TrafficItemFilterIds=None):
        """Adds a new layer23TrafficFlowFilter resource on the server and adds it to the container.

        Args
        ----
        - AggregatedAcrossPorts (bool): If true, displays aggregated stat value across ports selected by portFilterIds. Default = false
        - EgressLatencyBinDisplayOption (str(none | showEgressFlatView | showEgressRows | showLatencyBinStats)): Emulates Latency Bin SV or Egress Tracking SV.
        - PortFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter])): Selected port filters from the availablePortFilter list.
        - TrafficItemFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter)): Selected traffic item filter from the availableTrafficItemFilter list.
        - TrafficItemFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter])): Selected traffic item filters from the availableTrafficItemFilter list.

        Returns
        -------
        - self: This instance with all currently retrieved layer23TrafficFlowFilter resources using find and the newly added layer23TrafficFlowFilter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained layer23TrafficFlowFilter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AggregatedAcrossPorts=None, EgressLatencyBinDisplayOption=None, PortFilterIds=None, TrafficItemFilterId=None, TrafficItemFilterIds=None):
        """Finds and retrieves layer23TrafficFlowFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve layer23TrafficFlowFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all layer23TrafficFlowFilter resources from the server.

        Args
        ----
        - AggregatedAcrossPorts (bool): If true, displays aggregated stat value across ports selected by portFilterIds. Default = false
        - EgressLatencyBinDisplayOption (str(none | showEgressFlatView | showEgressRows | showLatencyBinStats)): Emulates Latency Bin SV or Egress Tracking SV.
        - PortFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter])): Selected port filters from the availablePortFilter list.
        - TrafficItemFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter)): Selected traffic item filter from the availableTrafficItemFilter list.
        - TrafficItemFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter])): Selected traffic item filters from the availableTrafficItemFilter list.

        Returns
        -------
        - self: This instance with matching layer23TrafficFlowFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of layer23TrafficFlowFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the layer23TrafficFlowFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
