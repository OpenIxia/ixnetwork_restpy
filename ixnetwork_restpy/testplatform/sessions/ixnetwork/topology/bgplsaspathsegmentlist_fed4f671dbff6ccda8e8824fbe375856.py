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


class BgpLsAsPathSegmentList(Base):
    """Bgp LS Path segments
    The BgpLsAsPathSegmentList class encapsulates a list of bgpLsAsPathSegmentList resources that are managed by the system.
    A list of resources can be retrieved from the server using the BgpLsAsPathSegmentList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpLsAsPathSegmentList'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableASPathSegment': 'enableASPathSegment',
        'Name': 'name',
        'NumberOfAsNumberInSegment': 'numberOfAsNumberInSegment',
        'SegmentType': 'segmentType',
    }

    def __init__(self, parent):
        super(BgpLsAsPathSegmentList, self).__init__(parent)

    @property
    def BgpAsNumberList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpasnumberlist_1529f0c2f511c5c16621b75c6205cf08.BgpAsNumberList): An instance of the BgpAsNumberList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpasnumberlist_1529f0c2f511c5c16621b75c6205cf08 import BgpAsNumberList
        return BgpAsNumberList(self)

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
    def EnableASPathSegment(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable AS Path Segment
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableASPathSegment']))

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
    def NumberOfAsNumberInSegment(self):
        """
        Returns
        -------
        - number: Number of AS Number In Segment
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfAsNumberInSegment'])
    @NumberOfAsNumberInSegment.setter
    def NumberOfAsNumberInSegment(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfAsNumberInSegment'], value)

    @property
    def SegmentType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SegmentType
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SegmentType']))

    def update(self, Name=None, NumberOfAsNumberInSegment=None):
        """Updates bgpLsAsPathSegmentList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAsNumberInSegment (number): Number of AS Number In Segment

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, NumberOfAsNumberInSegment=None):
        """Finds and retrieves bgpLsAsPathSegmentList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpLsAsPathSegmentList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpLsAsPathSegmentList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAsNumberInSegment (number): Number of AS Number In Segment

        Returns
        -------
        - self: This instance with matching bgpLsAsPathSegmentList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpLsAsPathSegmentList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpLsAsPathSegmentList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, EnableASPathSegment=None, SegmentType=None):
        """Base class infrastructure that gets a list of bgpLsAsPathSegmentList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - EnableASPathSegment (str): optional regex of enableASPathSegment
        - SegmentType (str): optional regex of segmentType

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
