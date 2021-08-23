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
from typing import List, Any, Union


class Dhcp6LearnedInfo(Base):
    """DHCPv6 Client Learned Info.
    The Dhcp6LearnedInfo class encapsulates a required dhcp6LearnedInfo resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcp6LearnedInfo'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Name': 'name',
        'TabbedDiscoveredAddresses': 'tabbedDiscoveredAddresses',
        'TabbedDiscoveredGateways': 'tabbedDiscoveredGateways',
        'TabbedDiscoveredPrefix': 'tabbedDiscoveredPrefix',
        'TabbedDiscoveredPrefixLength': 'tabbedDiscoveredPrefixLength',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Dhcp6LearnedInfo, self).__init__(parent, list_op)

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
    def TabbedDiscoveredAddresses(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The discovered IPv6 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TabbedDiscoveredAddresses'])

    @property
    def TabbedDiscoveredGateways(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The discovered gateway IPv6 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TabbedDiscoveredGateways'])

    @property
    def TabbedDiscoveredPrefix(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The discovered IPv6 prefix.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TabbedDiscoveredPrefix'])

    @property
    def TabbedDiscoveredPrefixLength(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): The length of the discovered IPv6 prefix.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TabbedDiscoveredPrefixLength'])

    def update(self, Name=None):
        # type: (str) -> Dhcp6LearnedInfo
        """Updates dhcp6LearnedInfo resource on the server.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
