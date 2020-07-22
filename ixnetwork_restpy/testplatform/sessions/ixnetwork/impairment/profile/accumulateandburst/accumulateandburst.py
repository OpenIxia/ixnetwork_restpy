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


class AccumulateAndBurst(Base):
    """Accumulates packets in a queue and transmit groups of packets as a burst. It can only be used on a profile if delayVariation and customDelayVariation are disabled.
    The AccumulateAndBurst class encapsulates a required accumulateAndBurst resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'accumulateAndBurst'
    _SDM_ATT_MAP = {
        'BurstSize': 'burstSize',
        'BurstSizeUnit': 'burstSizeUnit',
        'BurstTimeout': 'burstTimeout',
        'BurstTimeoutUnit': 'burstTimeoutUnit',
        'Enabled': 'enabled',
        'InterBurstGap': 'interBurstGap',
        'InterBurstGapValue': 'interBurstGapValue',
        'InterBurstGapValueUnit': 'interBurstGapValueUnit',
        'PacketCount': 'packetCount',
        'QueueAutoSize': 'queueAutoSize',
        'QueueAutoSizeEnabled': 'queueAutoSizeEnabled',
        'QueueSize': 'queueSize',
    }

    def __init__(self, parent):
        super(AccumulateAndBurst, self).__init__(parent)

    @property
    def BurstSize(self):
        """
        Returns
        -------
        - number: Represents the burst octet size. The default value is 1014.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurstSize'])
    @BurstSize.setter
    def BurstSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BurstSize'], value)

    @property
    def BurstSizeUnit(self):
        """
        Returns
        -------
        - str(kilobytes | kKilobytes | kMegabytes | megabytes): The burst size unit is either megabytes or kilobytes. The default unit is kilobytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurstSizeUnit'])
    @BurstSizeUnit.setter
    def BurstSizeUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BurstSizeUnit'], value)

    @property
    def BurstTimeout(self):
        """
        Returns
        -------
        - str: The burst timeout.The default value is 5 seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurstTimeout'])
    @BurstTimeout.setter
    def BurstTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BurstTimeout'], value)

    @property
    def BurstTimeoutUnit(self):
        """
        Returns
        -------
        - str(kMilliseconds | kSeconds | kTimeFormat | milliseconds | seconds | timeFormat): Seconds(default) / milliseconds / mm:ss.fff time format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurstTimeoutUnit'])
    @BurstTimeoutUnit.setter
    def BurstTimeoutUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BurstTimeoutUnit'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, received packets are queued and transmitted in bursts.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def InterBurstGap(self):
        """
        Returns
        -------
        - str(headToHead | kHeadToHead | kTailToHead | tailToHead): Tail to head (default) / Head to head.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterBurstGap'])
    @InterBurstGap.setter
    def InterBurstGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterBurstGap'], value)

    @property
    def InterBurstGapValue(self):
        """
        Returns
        -------
        - number: The InterBurst gap value. The default value is 20 ms.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterBurstGapValue'])
    @InterBurstGapValue.setter
    def InterBurstGapValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterBurstGapValue'], value)

    @property
    def InterBurstGapValueUnit(self):
        """
        Returns
        -------
        - str(kMilliseconds | kSeconds | milliseconds | seconds): Seconds / milliseconds (default).
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterBurstGapValueUnit'])
    @InterBurstGapValueUnit.setter
    def InterBurstGapValueUnit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterBurstGapValueUnit'], value)

    @property
    def PacketCount(self):
        """
        Returns
        -------
        - number: Represents the burst packet count. The default value is 1000 packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketCount'])
    @PacketCount.setter
    def PacketCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketCount'], value)

    @property
    def QueueAutoSize(self):
        """
        Returns
        -------
        - number: Gets the automatically calculated queue size when queueAutoSizeEnable is true or zero when queueAutoSizeEnable is false.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueAutoSize'])

    @property
    def QueueAutoSizeEnabled(self):
        """
        Returns
        -------
        - bool: Automatically calculate queue size. The default value is true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueAutoSizeEnabled'])
    @QueueAutoSizeEnabled.setter
    def QueueAutoSizeEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueAutoSizeEnabled'], value)

    @property
    def QueueSize(self):
        """
        Returns
        -------
        - number: The accumulate-and-burst queue size expressed in MB. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueSize'])
    @QueueSize.setter
    def QueueSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QueueSize'], value)

    def update(self, BurstSize=None, BurstSizeUnit=None, BurstTimeout=None, BurstTimeoutUnit=None, Enabled=None, InterBurstGap=None, InterBurstGapValue=None, InterBurstGapValueUnit=None, PacketCount=None, QueueAutoSizeEnabled=None, QueueSize=None):
        """Updates accumulateAndBurst resource on the server.

        Args
        ----
        - BurstSize (number): Represents the burst octet size. The default value is 1014.
        - BurstSizeUnit (str(kilobytes | kKilobytes | kMegabytes | megabytes)): The burst size unit is either megabytes or kilobytes. The default unit is kilobytes.
        - BurstTimeout (str): The burst timeout.The default value is 5 seconds.
        - BurstTimeoutUnit (str(kMilliseconds | kSeconds | kTimeFormat | milliseconds | seconds | timeFormat)): Seconds(default) / milliseconds / mm:ss.fff time format.
        - Enabled (bool): If true, received packets are queued and transmitted in bursts.
        - InterBurstGap (str(headToHead | kHeadToHead | kTailToHead | tailToHead)): Tail to head (default) / Head to head.
        - InterBurstGapValue (number): The InterBurst gap value. The default value is 20 ms.
        - InterBurstGapValueUnit (str(kMilliseconds | kSeconds | milliseconds | seconds)): Seconds / milliseconds (default).
        - PacketCount (number): Represents the burst packet count. The default value is 1000 packets.
        - QueueAutoSizeEnabled (bool): Automatically calculate queue size. The default value is true.
        - QueueSize (number): The accumulate-and-burst queue size expressed in MB. The default value is 1.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
