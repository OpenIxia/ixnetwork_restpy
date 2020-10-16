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

    def __init__(self, parent):
        super(DynamicRate, self).__init__(parent)

    @property
    def BitRateUnitsType(self):
        """
        Returns
        -------
        - str(bitsPerSec | bytesPerSec | kbitsPerSec | kbytesPerSec | mbitsPerSec | mbytesPerSec): The rate units for transmitting packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BitRateUnitsType'])
    @BitRateUnitsType.setter
    def BitRateUnitsType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BitRateUnitsType'], value)

    @property
    def EnforceMinimumInterPacketGap(self):
        """
        Returns
        -------
        - number: Sets the minimum inter-packet gap allowed for Ethernet ports only.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnforceMinimumInterPacketGap'])
    @EnforceMinimumInterPacketGap.setter
    def EnforceMinimumInterPacketGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnforceMinimumInterPacketGap'], value)

    @property
    def HighLevelStreamName(self):
        """
        Returns
        -------
        - str: The name of the high level stream
        """
        return self._get_attribute(self._SDM_ATT_MAP['HighLevelStreamName'])

    @property
    def InterPacketGapUnitsType(self):
        """
        Returns
        -------
        - str(bytes | nanoseconds): The inter-packet gap expressed in units.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterPacketGapUnitsType'])
    @InterPacketGapUnitsType.setter
    def InterPacketGapUnitsType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterPacketGapUnitsType'], value)

    @property
    def OverSubscribed(self):
        """
        Returns
        -------
        - bool: If true, the packet transmission rate is oversubscribed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverSubscribed'])

    @property
    def Rate(self):
        """
        Returns
        -------
        - number: The rate at which packet is transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rate'])
    @Rate.setter
    def Rate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rate'], value)

    @property
    def RateType(self):
        """
        Returns
        -------
        - str(bitsPerSecond | framesPerSecond | interPacketGap | percentLineRate): The types of packet rate transmission.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RateType'])
    @RateType.setter
    def RateType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RateType'], value)

    @property
    def TrafficItemName(self):
        """
        Returns
        -------
        - str: The name of the parent traffic item.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficItemName'])

    @property
    def TxPort(self):
        """
        Returns
        -------
        - number: The transmitting port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxPort'])

    def update(self, BitRateUnitsType=None, EnforceMinimumInterPacketGap=None, InterPacketGapUnitsType=None, Rate=None, RateType=None):
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

    def find(self, BitRateUnitsType=None, EnforceMinimumInterPacketGap=None, HighLevelStreamName=None, InterPacketGapUnitsType=None, OverSubscribed=None, Rate=None, RateType=None, TrafficItemName=None, TxPort=None):
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
