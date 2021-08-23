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


class InterfaceLearnedInfo(Base):
    """This objects contains the learned information from the
interface.
    The InterfaceLearnedInfo class encapsulates a required interfaceLearnedInfo resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'interfaceLearnedInfo'
    _SDM_ATT_MAP = {
        'GatewayIp': 'gatewayIp',
        'IpType': 'ipType',
        'OwnIp': 'ownIp',
        'PrefixLength': 'prefixLength',
    }
    _SDM_ENUM_MAP = {
        'ipType': ['kIpv4', 'kIpv6'],
    }

    def __init__(self, parent, list_op=False):
        super(InterfaceLearnedInfo, self).__init__(parent, list_op)

    @property
    def GatewayIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address of the Gateway to the network, typically an interface on the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GatewayIp'])

    @property
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(kIpv4 | kIpv6): The IP version used with this option set: IPv4 or IPv6.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpType'])

    @property
    def OwnIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The own ip type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OwnIp'])

    @property
    def PrefixLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: A learned/allocated IPv4 address prefix length (mask) for this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLength'])
