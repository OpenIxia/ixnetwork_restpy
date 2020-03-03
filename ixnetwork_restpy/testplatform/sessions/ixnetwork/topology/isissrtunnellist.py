# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class IsisSRTunnelList(Base):
    """ISIS MPLS SR Tunnel
    The IsisSRTunnelList class encapsulates a required isisSRTunnelList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isisSRTunnelList'

    def __init__(self, parent):
        super(IsisSRTunnelList, self).__init__(parent)

    @property
    def IsisSegmentList(self):
        """An instance of the IsisSegmentList class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissegmentlist.IsisSegmentList)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissegmentlist import IsisSegmentList
        return IsisSegmentList(self)

    @property
    def Tag(self):
        """An instance of the Tag class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
        return Tag(self)

    @property
    def Active(self):
        """Activate/Deactivate Configuration

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('active')

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def Name(self):
        """Name of NGPF element, guaranteed to be unique in Scenario

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NumberOfSegments(self):
        """Number of Segments

        Returns:
            number
        """
        return self._get_attribute('numberOfSegments')
    @NumberOfSegments.setter
    def NumberOfSegments(self, value):
        self._set_attribute('numberOfSegments', value)

    @property
    def SourceIpv4(self):
        """Source IPv4

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sourceIpv4')

    @property
    def SourceIpv6(self):
        """Source IPv6

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sourceIpv6')

    @property
    def TunnelDescription(self):
        """Tunnel Description

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tunnelDescription')

    @property
    def UsingHeadEndNodePrefix(self):
        """Using head end Node prefix

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('usingHeadEndNodePrefix')

    def update(self, Name=None, NumberOfSegments=None):
        """Updates a child instance of isisSRTunnelList on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            NumberOfSegments (number): Number of Segments

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def get_device_ids(self, PortNames=None, Active=None, SourceIpv4=None, SourceIpv6=None, TunnelDescription=None, UsingHeadEndNodePrefix=None):
        """Base class infrastructure that gets a list of isisSRTunnelList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            Active (str): optional regex of active
            SourceIpv4 (str): optional regex of sourceIpv4
            SourceIpv6 (str): optional regex of sourceIpv6
            TunnelDescription (str): optional regex of tunnelDescription
            UsingHeadEndNodePrefix (str): optional regex of usingHeadEndNodePrefix

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
