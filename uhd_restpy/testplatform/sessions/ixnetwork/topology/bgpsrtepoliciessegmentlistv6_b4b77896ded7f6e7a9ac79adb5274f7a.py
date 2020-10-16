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


class BgpSRTEPoliciesSegmentListV6(Base):
    """
    The BgpSRTEPoliciesSegmentListV6 class encapsulates a required bgpSRTEPoliciesSegmentListV6 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpSRTEPoliciesSegmentListV6'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnWeight': 'enWeight',
        'Name': 'name',
        'NumberOfActiveSegments': 'numberOfActiveSegments',
        'NumberOfSegmentsV6': 'numberOfSegmentsV6',
        'SegmentListNumber': 'segmentListNumber',
        'SrtepolicyName': 'srtepolicyName',
        'Weight': 'weight',
    }

    def __init__(self, parent):
        super(BgpSRTEPoliciesSegmentListV6, self).__init__(parent)

    @property
    def BgpSRTEPoliciesSegmentsCollectionV6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepoliciessegmentscollectionv6_7dace127dbb526f56b4a0b3fbf40ea33.BgpSRTEPoliciesSegmentsCollectionV6): An instance of the BgpSRTEPoliciesSegmentsCollectionV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepoliciessegmentscollectionv6_7dace127dbb526f56b4a0b3fbf40ea33 import BgpSRTEPoliciesSegmentsCollectionV6
        return BgpSRTEPoliciesSegmentsCollectionV6(self)._select()

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

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
    def EnWeight(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Weight Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnWeight']))

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

    @property
    def NumberOfActiveSegments(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Count of Segment
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumberOfActiveSegments']))

    @property
    def NumberOfSegmentsV6(self):
        """
        Returns
        -------
        - number: Count of Segments Per Segment List
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfSegmentsV6'])
    @NumberOfSegmentsV6.setter
    def NumberOfSegmentsV6(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfSegmentsV6'], value)

    @property
    def SegmentListNumber(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Segment List Number For Reference
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SegmentListNumber']))

    @property
    def SrtepolicyName(self):
        """
        Returns
        -------
        - list(str): Policy Name For Reference
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrtepolicyName'])

    @property
    def Weight(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Weight Value
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    def update(self, Name=None, NumberOfSegmentsV6=None):
        """Updates bgpSRTEPoliciesSegmentListV6 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfSegmentsV6 (number): Count of Segments Per Segment List

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, EnWeight=None, NumberOfActiveSegments=None, SegmentListNumber=None, Weight=None):
        """Base class infrastructure that gets a list of bgpSRTEPoliciesSegmentListV6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - EnWeight (str): optional regex of enWeight
        - NumberOfActiveSegments (str): optional regex of numberOfActiveSegments
        - SegmentListNumber (str): optional regex of segmentListNumber
        - Weight (str): optional regex of weight

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
