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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class DynamicRate(Base):
    """This object provides different options for the rate that can be changed on the fly.
    The DynamicRate class encapsulates a list of dynamicRate resources that are managed by the system.
    A list of resources can be retrieved from the server using the DynamicRate.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'dynamicRate'
    _SDM_ATT_MAP = {
        'BitRateUnitsType': 'bitRateUnitsType',
        'EnforceMinimumInterPacketGap': 'enforceMinimumInterPacketGap',
        'HighLevelStreamName': 'highLevelStreamName',
        'InterPacketGapUnitsType': 'interPacketGapUnitsType',
        'OverSubscribed': 'overSubscribed',
        'Rate': 'rate',
        'RateType': 'rateType',
        'TrafficItemName': 'trafficItemName',
        'TxPort': 'txPort',
    }
    _SDM_ENUM_MAP = {
        'bitRateUnitsType': ['bitsPerSec', 'bytesPerSec', 'kbitsPerSec', 'kbytesPerSec', 'mbitsPerSec', 'mbytesPerSec'],
        'interPacketGapUnitsType': ['bytes', 'nanoseconds'],
        'rateType': ['bitsPerSecond', 'framesPerSecond', 'interPacketGap', 'percentLineRate'],
    }

    def __init__(self, parent, list_op=False):
        super(DynamicRate, self).__init__(parent, list_op)

    @property
    def BitRateUnitsType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bitsPerSec | bytesPerSec | kbitsPerSec | kbytesPerSec | mbitsPerSec | mbytesPerSec): The rate units for transmitting packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BitRateUnitsType'])
    @BitRateUnitsType.setter
    def BitRateUnitsType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['BitRateUnitsType'], value)

    @property
    def EnforceMinimumInterPacketGap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the minimum inter-packet gap allowed for Ethernet ports only.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnforceMinimumInterPacketGap'])
    @EnforceMinimumInterPacketGap.setter
    def EnforceMinimumInterPacketGap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnforceMinimumInterPacketGap'], value)

    @property
    def HighLevelStreamName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the high level stream
        """
        return self._get_attribute(self._SDM_ATT_MAP['HighLevelStreamName'])

    @property
    def InterPacketGapUnitsType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bytes | nanoseconds): The inter-packet gap expressed in units.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterPacketGapUnitsType'])
    @InterPacketGapUnitsType.setter
    def InterPacketGapUnitsType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['InterPacketGapUnitsType'], value)

    @property
    def OverSubscribed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the packet transmission rate is oversubscribed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverSubscribed'])

    @property
    def Rate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The rate at which packet is transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rate'])
    @Rate.setter
    def Rate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Rate'], value)

    @property
    def RateType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bitsPerSecond | framesPerSecond | interPacketGap | percentLineRate): The types of packet rate transmission.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RateType'])
    @RateType.setter
    def RateType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['RateType'], value)

    @property
    def TrafficItemName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the parent traffic item.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficItemName'])

    @property
    def TxPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The transmitting port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxPort'])

    def update(self, BitRateUnitsType=None, EnforceMinimumInterPacketGap=None, InterPacketGapUnitsType=None, Rate=None, RateType=None):
        # type: (str, int, str, int, str) -> DynamicRate
        """Updates dynamicRate resource on the server.

        Args
        ----
        - BitRateUnitsType (str(bitsPerSec | bytesPerSec | kbitsPerSec | kbytesPerSec | mbitsPerSec | mbytesPerSec)): The rate units for transmitting packet.
        - EnforceMinimumInterPacketGap (number): Sets the minimum inter-packet gap allowed for Ethernet ports only.
        - InterPacketGapUnitsType (str(bytes | nanoseconds)): The inter-packet gap expressed in units.
        - Rate (number): The rate at which packet is transmitted.
        - RateType (str(bitsPerSecond | framesPerSecond | interPacketGap | percentLineRate)): The types of packet rate transmission.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, BitRateUnitsType=None, EnforceMinimumInterPacketGap=None, InterPacketGapUnitsType=None, Rate=None, RateType=None):
        # type: (str, int, str, int, str) -> DynamicRate
        """Adds a new dynamicRate resource on the json, only valid with batch add utility

        Args
        ----
        - BitRateUnitsType (str(bitsPerSec | bytesPerSec | kbitsPerSec | kbytesPerSec | mbitsPerSec | mbytesPerSec)): The rate units for transmitting packet.
        - EnforceMinimumInterPacketGap (number): Sets the minimum inter-packet gap allowed for Ethernet ports only.
        - InterPacketGapUnitsType (str(bytes | nanoseconds)): The inter-packet gap expressed in units.
        - Rate (number): The rate at which packet is transmitted.
        - RateType (str(bitsPerSecond | framesPerSecond | interPacketGap | percentLineRate)): The types of packet rate transmission.

        Returns
        -------
        - self: This instance with all currently retrieved dynamicRate resources using find and the newly added dynamicRate resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, BitRateUnitsType=None, EnforceMinimumInterPacketGap=None, HighLevelStreamName=None, InterPacketGapUnitsType=None, OverSubscribed=None, Rate=None, RateType=None, TrafficItemName=None, TxPort=None):
        # type: (str, int, str, str, bool, int, str, str, int) -> DynamicRate
        """Finds and retrieves dynamicRate resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dynamicRate resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dynamicRate resources from the server.

        Args
        ----
        - BitRateUnitsType (str(bitsPerSec | bytesPerSec | kbitsPerSec | kbytesPerSec | mbitsPerSec | mbytesPerSec)): The rate units for transmitting packet.
        - EnforceMinimumInterPacketGap (number): Sets the minimum inter-packet gap allowed for Ethernet ports only.
        - HighLevelStreamName (str): The name of the high level stream
        - InterPacketGapUnitsType (str(bytes | nanoseconds)): The inter-packet gap expressed in units.
        - OverSubscribed (bool): If true, the packet transmission rate is oversubscribed.
        - Rate (number): The rate at which packet is transmitted.
        - RateType (str(bitsPerSecond | framesPerSecond | interPacketGap | percentLineRate)): The types of packet rate transmission.
        - TrafficItemName (str): The name of the parent traffic item.
        - TxPort (number): The transmitting port.

        Returns
        -------
        - self: This instance with matching dynamicRate resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dynamicRate data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dynamicRate resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
