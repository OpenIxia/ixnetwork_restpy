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


class MeterCapabilities(Base):
    """Specify the meter capabilities supported by Switch.
    The MeterCapabilities class encapsulates a required meterCapabilities resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'meterCapabilities'
    _SDM_ATT_MAP = {
        'CollectStatistics': 'collectStatistics',
        'DoBurstSize': 'doBurstSize',
        'KiloBitPerSecond': 'kiloBitPerSecond',
        'PacketPerSecond': 'packetPerSecond',
    }

    def __init__(self, parent):
        super(MeterCapabilities, self).__init__(parent)

    @property
    def CollectStatistics(self):
        """
        Returns
        -------
        - bool: The capability to collect statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CollectStatistics'])
    @CollectStatistics.setter
    def CollectStatistics(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CollectStatistics'], value)

    @property
    def DoBurstSize(self):
        """
        Returns
        -------
        - bool: The size of burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DoBurstSize'])
    @DoBurstSize.setter
    def DoBurstSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DoBurstSize'], value)

    @property
    def KiloBitPerSecond(self):
        """
        Returns
        -------
        - bool: Rate value in kilo-bit per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['KiloBitPerSecond'])
    @KiloBitPerSecond.setter
    def KiloBitPerSecond(self, value):
        self._set_attribute(self._SDM_ATT_MAP['KiloBitPerSecond'], value)

    @property
    def PacketPerSecond(self):
        """
        Returns
        -------
        - bool: Rate value in packet per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketPerSecond'])
    @PacketPerSecond.setter
    def PacketPerSecond(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketPerSecond'], value)

    def update(self, CollectStatistics=None, DoBurstSize=None, KiloBitPerSecond=None, PacketPerSecond=None):
        """Updates meterCapabilities resource on the server.

        Args
        ----
        - CollectStatistics (bool): The capability to collect statistics.
        - DoBurstSize (bool): The size of burst.
        - KiloBitPerSecond (bool): Rate value in kilo-bit per second.
        - PacketPerSecond (bool): Rate value in packet per second.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
