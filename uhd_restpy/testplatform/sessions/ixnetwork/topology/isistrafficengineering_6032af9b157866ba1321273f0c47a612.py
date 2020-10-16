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


class IsisTrafficEngineering(Base):
    """DEPRECATED Isis Traffic Engineering Configuration
    The IsisTrafficEngineering class encapsulates a required isisTrafficEngineering resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isisTrafficEngineering'
    _SDM_ATT_MAP = {
        'AdministratorGroup': 'administratorGroup',
        'BandwidthPriority0': 'bandwidthPriority0',
        'BandwidthPriority1': 'bandwidthPriority1',
        'BandwidthPriority2': 'bandwidthPriority2',
        'BandwidthPriority3': 'bandwidthPriority3',
        'BandwidthPriority4': 'bandwidthPriority4',
        'BandwidthPriority5': 'bandwidthPriority5',
        'BandwidthPriority6': 'bandwidthPriority6',
        'BandwidthPriority7': 'bandwidthPriority7',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'MaxBandwidth': 'maxBandwidth',
        'MaxReservableBandwidth': 'maxReservableBandwidth',
        'MetricLevel': 'metricLevel',
        'Name': 'name',
    }

    def __init__(self, parent):
        super(IsisTrafficEngineering, self).__init__(parent)

    @property
    def AdministratorGroup(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Administrator Group
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdministratorGroup']))

    @property
    def BandwidthPriority0(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 0 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority0']))

    @property
    def BandwidthPriority1(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 1 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority1']))

    @property
    def BandwidthPriority2(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 2 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority2']))

    @property
    def BandwidthPriority3(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 3 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority3']))

    @property
    def BandwidthPriority4(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 4 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority4']))

    @property
    def BandwidthPriority5(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 5 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority5']))

    @property
    def BandwidthPriority6(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 6 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority6']))

    @property
    def BandwidthPriority7(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bandwidth for Priority 7 (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority7']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def MaxBandwidth(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Maximum Bandwidth (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxBandwidth']))

    @property
    def MaxReservableBandwidth(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Maximum Reservable Bandwidth (B/sec)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxReservableBandwidth']))

    @property
    def MetricLevel(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TE Metric Level
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetricLevel']))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    def update(self, Name=None):
        """Updates isisTrafficEngineering resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, AdministratorGroup=None, BandwidthPriority0=None, BandwidthPriority1=None, BandwidthPriority2=None, BandwidthPriority3=None, BandwidthPriority4=None, BandwidthPriority5=None, BandwidthPriority6=None, BandwidthPriority7=None, MaxBandwidth=None, MaxReservableBandwidth=None, MetricLevel=None):
        """Base class infrastructure that gets a list of isisTrafficEngineering device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AdministratorGroup (str): optional regex of administratorGroup
        - BandwidthPriority0 (str): optional regex of bandwidthPriority0
        - BandwidthPriority1 (str): optional regex of bandwidthPriority1
        - BandwidthPriority2 (str): optional regex of bandwidthPriority2
        - BandwidthPriority3 (str): optional regex of bandwidthPriority3
        - BandwidthPriority4 (str): optional regex of bandwidthPriority4
        - BandwidthPriority5 (str): optional regex of bandwidthPriority5
        - BandwidthPriority6 (str): optional regex of bandwidthPriority6
        - BandwidthPriority7 (str): optional regex of bandwidthPriority7
        - MaxBandwidth (str): optional regex of maxBandwidth
        - MaxReservableBandwidth (str): optional regex of maxReservableBandwidth
        - MetricLevel (str): optional regex of metricLevel

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
