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


class FrameRate(Base):
    """This object provides different options for the Frame Rate.
    The FrameRate class encapsulates a required frameRate resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'frameRate'
    _SDM_ATT_MAP = {
        'BitRateUnitsType': 'bitRateUnitsType',
        'EnforceMinimumInterPacketGap': 'enforceMinimumInterPacketGap',
        'InterPacketGapUnitsType': 'interPacketGapUnitsType',
        'Rate': 'rate',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(FrameRate, self).__init__(parent)

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
        - number: Sets the minimum inter-packet gap allowed for Ethernet ports only. The default is 12 bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnforceMinimumInterPacketGap'])
    @EnforceMinimumInterPacketGap.setter
    def EnforceMinimumInterPacketGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnforceMinimumInterPacketGap'], value)

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
    def Type(self):
        """
        Returns
        -------
        - str(bitsPerSecond | framesPerSecond | interPacketGap | percentLineRate): Sets the frame rate types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    def update(self, BitRateUnitsType=None, EnforceMinimumInterPacketGap=None, InterPacketGapUnitsType=None, Rate=None, Type=None):
        """Updates frameRate resource on the server.

        Args
        ----
        - BitRateUnitsType (str(bitsPerSec | bytesPerSec | kbitsPerSec | kbytesPerSec | mbitsPerSec | mbytesPerSec)): The rate units for transmitting packet.
        - EnforceMinimumInterPacketGap (number): Sets the minimum inter-packet gap allowed for Ethernet ports only. The default is 12 bytes.
        - InterPacketGapUnitsType (str(bytes | nanoseconds)): The inter-packet gap expressed in units.
        - Rate (number): The rate at which packet is transmitted.
        - Type (str(bitsPerSecond | framesPerSecond | interPacketGap | percentLineRate)): Sets the frame rate types.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
