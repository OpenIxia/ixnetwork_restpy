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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Capabilities(Base):
    """A high level object that allows to define the OpenFlow Switch capabilities configuration.
    The Capabilities class encapsulates a required capabilities resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "capabilities"
    _SDM_ATT_MAP = {
        "FlowStatistics": "flowStatistics",
        "GroupStatistics": "groupStatistics",
        "MatchIpAddressInArpPackets": "matchIpAddressInArpPackets",
        "PortStatistics": "portStatistics",
        "QueueStatistics": "queueStatistics",
        "ReassambleIpFragments": "reassambleIpFragments",
        "Reserved": "reserved",
        "SpanningTree": "spanningTree",
        "SwitchWillBlockLoopingPorts": "switchWillBlockLoopingPorts",
        "TableStatistics": "tableStatistics",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Capabilities, self).__init__(parent, list_op)

    @property
    def FlowStatistics(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the ofChannel capabilities of the switch includes flow statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowStatistics"])

    @FlowStatistics.setter
    def FlowStatistics(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowStatistics"], value)

    @property
    def GroupStatistics(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, indicates that the capabilities of the switch include Group Statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupStatistics"])

    @GroupStatistics.setter
    def GroupStatistics(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupStatistics"], value)

    @property
    def MatchIpAddressInArpPackets(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, indicates that the capabilities of the switch includes Match IP addresses in ARP pkts.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MatchIpAddressInArpPackets"])

    @MatchIpAddressInArpPackets.setter
    def MatchIpAddressInArpPackets(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MatchIpAddressInArpPackets"], value)

    @property
    def PortStatistics(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the ofChannel capabilities of the switch includes port statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortStatistics"])

    @PortStatistics.setter
    def PortStatistics(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortStatistics"], value)

    @property
    def QueueStatistics(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the capabilities of the switch include Queue statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueueStatistics"])

    @QueueStatistics.setter
    def QueueStatistics(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueueStatistics"], value)

    @property
    def ReassambleIpFragments(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the capabilities of the switch include reassemble IP fragments at the receiver.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReassambleIpFragments"])

    @ReassambleIpFragments.setter
    def ReassambleIpFragments(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReassambleIpFragments"], value)

    @property
    def Reserved(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the capabilities of the switch includes reserved, must be zero.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Reserved"])

    @Reserved.setter
    def Reserved(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Reserved"], value)

    @property
    def SpanningTree(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the capabilities of the switch includes 802.1d spanning tree.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SpanningTree"])

    @SpanningTree.setter
    def SpanningTree(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SpanningTree"], value)

    @property
    def SwitchWillBlockLoopingPorts(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, indicates that switch will block looping ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SwitchWillBlockLoopingPorts"])

    @SwitchWillBlockLoopingPorts.setter
    def SwitchWillBlockLoopingPorts(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SwitchWillBlockLoopingPorts"], value)

    @property
    def TableStatistics(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that the capabilities of the switch includes table statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TableStatistics"])

    @TableStatistics.setter
    def TableStatistics(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TableStatistics"], value)

    def update(
        self,
        FlowStatistics=None,
        GroupStatistics=None,
        MatchIpAddressInArpPackets=None,
        PortStatistics=None,
        QueueStatistics=None,
        ReassambleIpFragments=None,
        Reserved=None,
        SpanningTree=None,
        SwitchWillBlockLoopingPorts=None,
        TableStatistics=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> Capabilities
        """Updates capabilities resource on the server.

        Args
        ----
        - FlowStatistics (bool): Indicates that the ofChannel capabilities of the switch includes flow statistics.
        - GroupStatistics (bool): If true, indicates that the capabilities of the switch include Group Statistics.
        - MatchIpAddressInArpPackets (bool): If true, indicates that the capabilities of the switch includes Match IP addresses in ARP pkts.
        - PortStatistics (bool): Indicates that the ofChannel capabilities of the switch includes port statistics.
        - QueueStatistics (bool): Indicates that the capabilities of the switch include Queue statistics.
        - ReassambleIpFragments (bool): Indicates that the capabilities of the switch include reassemble IP fragments at the receiver.
        - Reserved (bool): Indicates that the capabilities of the switch includes reserved, must be zero.
        - SpanningTree (bool): Indicates that the capabilities of the switch includes 802.1d spanning tree.
        - SwitchWillBlockLoopingPorts (bool): If true, indicates that switch will block looping ports.
        - TableStatistics (bool): Indicates that the capabilities of the switch includes table statistics.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        FlowStatistics=None,
        GroupStatistics=None,
        MatchIpAddressInArpPackets=None,
        PortStatistics=None,
        QueueStatistics=None,
        ReassambleIpFragments=None,
        Reserved=None,
        SpanningTree=None,
        SwitchWillBlockLoopingPorts=None,
        TableStatistics=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> Capabilities
        """Finds and retrieves capabilities resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve capabilities resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all capabilities resources from the server.

        Args
        ----
        - FlowStatistics (bool): Indicates that the ofChannel capabilities of the switch includes flow statistics.
        - GroupStatistics (bool): If true, indicates that the capabilities of the switch include Group Statistics.
        - MatchIpAddressInArpPackets (bool): If true, indicates that the capabilities of the switch includes Match IP addresses in ARP pkts.
        - PortStatistics (bool): Indicates that the ofChannel capabilities of the switch includes port statistics.
        - QueueStatistics (bool): Indicates that the capabilities of the switch include Queue statistics.
        - ReassambleIpFragments (bool): Indicates that the capabilities of the switch include reassemble IP fragments at the receiver.
        - Reserved (bool): Indicates that the capabilities of the switch includes reserved, must be zero.
        - SpanningTree (bool): Indicates that the capabilities of the switch includes 802.1d spanning tree.
        - SwitchWillBlockLoopingPorts (bool): If true, indicates that switch will block looping ports.
        - TableStatistics (bool): Indicates that the capabilities of the switch includes table statistics.

        Returns
        -------
        - self: This instance with matching capabilities resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of capabilities data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the capabilities resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
