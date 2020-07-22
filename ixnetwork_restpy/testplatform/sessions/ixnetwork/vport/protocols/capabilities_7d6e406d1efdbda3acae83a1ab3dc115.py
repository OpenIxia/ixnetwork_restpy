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


class Capabilities(Base):
    """This object allows to define the Bitmap of supported capabilities.
    The Capabilities class encapsulates a required capabilities resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'capabilities'
    _SDM_ATT_MAP = {
        'FlowStatistics': 'flowStatistics',
        'MatchIpAddressInArpPackets': 'matchIpAddressInArpPackets',
        'PortStatistics': 'portStatistics',
        'QueueStatistics': 'queueStatistics',
        'ReassambleIpFragments': 'reassambleIpFragments',
        'Reserved': 'reserved',
        'SpanningTree': 'spanningTree',
        'TableStatistics': 'tableStatistics',
    }

    def __init__(self, parent):
        super(Capabilities, self).__init__(parent)

    @property
    def FlowStatistics(self):
        """
        Returns
        -------
        - bool: Indicates that the ofChannel capabilities of the switch includes flow statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowStatistics'])
    @FlowStatistics.setter
    def FlowStatistics(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowStatistics'], value)

    @property
    def MatchIpAddressInArpPackets(self):
        """
        Returns
        -------
        - bool: Indicates that the ofChannel capabilities of the switch includes Match IP addresses in ARP pkts.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchIpAddressInArpPackets'])
    @MatchIpAddressInArpPackets.setter
    def MatchIpAddressInArpPackets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MatchIpAddressInArpPackets'], value)

    @property
    def PortStatistics(self):
        """
        Returns
        -------
        - bool: Indicates that the ofChannel capabilities of the switch includes port statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortStatistics'])
    @PortStatistics.setter
    def PortStatistics(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortStatistics'], value)

    @property
    def QueueStatistics(self):
        """
        Returns
        -------
        - bool: Indicates that the ofChannel capabilities of the switch include Queue statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueStatistics'])
    @QueueStatistics.setter
    def QueueStatistics(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueStatistics'], value)

    @property
    def ReassambleIpFragments(self):
        """
        Returns
        -------
        - bool: Indicates that the ofChannel capabilities of the switch include reassemble IP fragments at the receiver.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReassambleIpFragments'])
    @ReassambleIpFragments.setter
    def ReassambleIpFragments(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReassambleIpFragments'], value)

    @property
    def Reserved(self):
        """
        Returns
        -------
        - bool: Indicates that the ofChannel capabilities of the switch includes reserved, must be zero.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Reserved'])
    @Reserved.setter
    def Reserved(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Reserved'], value)

    @property
    def SpanningTree(self):
        """
        Returns
        -------
        - bool: Indicates that the ofChannel capabilities of the switch includes 802.1d spanning tree.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SpanningTree'])
    @SpanningTree.setter
    def SpanningTree(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SpanningTree'], value)

    @property
    def TableStatistics(self):
        """
        Returns
        -------
        - bool: Indicates that the ofChannel capabilities of the switch includes table statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableStatistics'])
    @TableStatistics.setter
    def TableStatistics(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableStatistics'], value)

    def update(self, FlowStatistics=None, MatchIpAddressInArpPackets=None, PortStatistics=None, QueueStatistics=None, ReassambleIpFragments=None, Reserved=None, SpanningTree=None, TableStatistics=None):
        """Updates capabilities resource on the server.

        Args
        ----
        - FlowStatistics (bool): Indicates that the ofChannel capabilities of the switch includes flow statistics.
        - MatchIpAddressInArpPackets (bool): Indicates that the ofChannel capabilities of the switch includes Match IP addresses in ARP pkts.
        - PortStatistics (bool): Indicates that the ofChannel capabilities of the switch includes port statistics.
        - QueueStatistics (bool): Indicates that the ofChannel capabilities of the switch include Queue statistics.
        - ReassambleIpFragments (bool): Indicates that the ofChannel capabilities of the switch include reassemble IP fragments at the receiver.
        - Reserved (bool): Indicates that the ofChannel capabilities of the switch includes reserved, must be zero.
        - SpanningTree (bool): Indicates that the ofChannel capabilities of the switch includes 802.1d spanning tree.
        - TableStatistics (bool): Indicates that the ofChannel capabilities of the switch includes table statistics.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
