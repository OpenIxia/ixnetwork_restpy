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


class ExpectedInitiatedLspList(Base):
    """This specifies the Expected Initiated LSPs from the PCE for traffic generation.
    The ExpectedInitiatedLspList class encapsulates a required expectedInitiatedLspList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'expectedInitiatedLspList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'InsertIpv6ExplicitNull': 'insertIpv6ExplicitNull',
        'MaxExpectedSegmentCount': 'maxExpectedSegmentCount',
        'Name': 'name',
        'SourceIpv4Address': 'sourceIpv4Address',
        'SourceIpv6Address': 'sourceIpv6Address',
        'SymbolicPathName': 'symbolicPathName',
    }

    def __init__(self, parent):
        super(ExpectedInitiatedLspList, self).__init__(parent)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        return Tag(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
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
    def InsertIpv6ExplicitNull(self):
        """
        Returns
        -------
        - bool: Insert IPv6 Explicit Null MPLS header if the traffic type is of type IPv6
        """
        return self._get_attribute(self._SDM_ATT_MAP['InsertIpv6ExplicitNull'])
    @InsertIpv6ExplicitNull.setter
    def InsertIpv6ExplicitNull(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InsertIpv6ExplicitNull'], value)

    @property
    def MaxExpectedSegmentCount(self):
        """
        Returns
        -------
        - number: This control is used to set the maximum Segment count/ MPLS labels that would be present in the generted traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxExpectedSegmentCount'])
    @MaxExpectedSegmentCount.setter
    def MaxExpectedSegmentCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxExpectedSegmentCount'], value)

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
    def SourceIpv4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is used to set the Source IPv4 address in the IP header of the generated traffic.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceIpv4Address']))

    @property
    def SourceIpv6Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is used to set the Source IPv6 address in the IP header of the generated traffic.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceIpv6Address']))

    @property
    def SymbolicPathName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is used for generating the traffic for those LSPs from PCE for which the Symbolic Path Name is configured and matches the value.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SymbolicPathName']))

    def update(self, InsertIpv6ExplicitNull=None, MaxExpectedSegmentCount=None, Name=None):
        """Updates expectedInitiatedLspList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - InsertIpv6ExplicitNull (bool): Insert IPv6 Explicit Null MPLS header if the traffic type is of type IPv6
        - MaxExpectedSegmentCount (number): This control is used to set the maximum Segment count/ MPLS labels that would be present in the generted traffic.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, SourceIpv4Address=None, SourceIpv6Address=None, SymbolicPathName=None):
        """Base class infrastructure that gets a list of expectedInitiatedLspList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - SourceIpv4Address (str): optional regex of sourceIpv4Address
        - SourceIpv6Address (str): optional regex of sourceIpv6Address
        - SymbolicPathName (str): optional regex of symbolicPathName

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
