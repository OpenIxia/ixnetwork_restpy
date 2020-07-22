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


class PceUpdateSrMetricSubObjectList(Base):
    """
    The PceUpdateSrMetricSubObjectList class encapsulates a list of pceUpdateSrMetricSubObjectList resources that are managed by the system.
    A list of resources can be retrieved from the server using the PceUpdateSrMetricSubObjectList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'pceUpdateSrMetricSubObjectList'
    _SDM_ATT_MAP = {
        'ActiveThisMetric': 'activeThisMetric',
        'BFlag': 'bFlag',
        'MetricType': 'metricType',
        'MetricValue': 'metricValue',
    }

    def __init__(self, parent):
        super(PceUpdateSrMetricSubObjectList, self).__init__(parent)

    @property
    def ActiveThisMetric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies whether the corresponding metric object is active or not.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveThisMetric']))

    @property
    def BFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B (bound) flag MUST be set in the METRIC object, which specifies that the SID depth for the computed path MUST NOT exceed the metric-value.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFlag']))

    @property
    def MetricType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a drop down which has 4 choices: IGP/ TE/ Hop count/ MSD.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetricType']))

    @property
    def MetricValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User can specify the metric value corresponding to the metric type selected.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetricValue']))

    def find(self):
        """Finds and retrieves pceUpdateSrMetricSubObjectList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pceUpdateSrMetricSubObjectList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pceUpdateSrMetricSubObjectList resources from the server.

        Returns
        -------
        - self: This instance with matching pceUpdateSrMetricSubObjectList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pceUpdateSrMetricSubObjectList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pceUpdateSrMetricSubObjectList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ActiveThisMetric=None, BFlag=None, MetricType=None, MetricValue=None):
        """Base class infrastructure that gets a list of pceUpdateSrMetricSubObjectList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActiveThisMetric (str): optional regex of activeThisMetric
        - BFlag (str): optional regex of bFlag
        - MetricType (str): optional regex of metricType
        - MetricValue (str): optional regex of metricValue

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
