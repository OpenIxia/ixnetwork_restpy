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
from typing import List, Any, Union


class BgpSRTEPoliciesSegmentListV4(Base):
    """
    The BgpSRTEPoliciesSegmentListV4 class encapsulates a required bgpSRTEPoliciesSegmentListV4 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpSRTEPoliciesSegmentListV4'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnWeight': 'enWeight',
        'Name': 'name',
        'NumberOfActiveSegments': 'numberOfActiveSegments',
        'NumberOfSegmentsV4': 'numberOfSegmentsV4',
        'SegmentListNumber': 'segmentListNumber',
        'SrtepolicyName': 'srtepolicyName',
        'Weight': 'weight',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(BgpSRTEPoliciesSegmentListV4, self).__init__(parent, list_op)

    @property
    def BgpSRTEPoliciesSegmentsCollectionV4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepoliciessegmentscollectionv4_d6a62629f62aedd8a178ab387f891990.BgpSRTEPoliciesSegmentsCollectionV4): An instance of the BgpSRTEPoliciesSegmentsCollectionV4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepoliciessegmentscollectionv4_d6a62629f62aedd8a178ab387f891990 import BgpSRTEPoliciesSegmentsCollectionV4
        if self._properties.get('BgpSRTEPoliciesSegmentsCollectionV4', None) is not None:
            return self._properties.get('BgpSRTEPoliciesSegmentsCollectionV4')
        else:
            return BgpSRTEPoliciesSegmentsCollectionV4(self)._select()

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnWeight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Weight Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnWeight']))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NumberOfActiveSegments(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Count of Segment
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumberOfActiveSegments']))

    @property
    def NumberOfSegmentsV4(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Count of Segments Per Segment List.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfSegmentsV4'])
    @NumberOfSegmentsV4.setter
    def NumberOfSegmentsV4(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfSegmentsV4'], value)

    @property
    def SegmentListNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Segment List Number For Reference
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SegmentListNumber']))

    @property
    def SrtepolicyName(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Policy Name For Reference
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrtepolicyName'])

    @property
    def Weight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Weight Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    def update(self, Name=None, NumberOfSegmentsV4=None):
        # type: (str, int) -> BgpSRTEPoliciesSegmentListV4
        """Updates bgpSRTEPoliciesSegmentListV4 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfSegmentsV4 (number): Count of Segments Per Segment List.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, EnWeight=None, NumberOfActiveSegments=None, SegmentListNumber=None, Weight=None):
        """Base class infrastructure that gets a list of bgpSRTEPoliciesSegmentListV4 device ids encapsulated by this object.

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
