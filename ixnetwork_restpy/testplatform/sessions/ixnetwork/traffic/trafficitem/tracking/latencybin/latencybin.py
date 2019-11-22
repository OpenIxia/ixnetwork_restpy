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


class LatencyBin(Base):
    """This object provides different options for Latency Bin Tracking.
    The LatencyBin class encapsulates a required latencyBin resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'latencyBin'

    def __init__(self, parent):
        super(LatencyBin, self).__init__(parent)

    @property
    def BinLimits(self):
        """Specifies the upper limit of each Time Bins for Latency Bin Tracking.

        Returns:
            list(number)
        """
        return self._get_attribute('binLimits')
    @BinLimits.setter
    def BinLimits(self, value):
        self._set_attribute('binLimits', value)

    @property
    def Enabled(self):
        """If true, Latency Bin Tracking is enabled.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def NumberOfBins(self):
        """Specifies the number of Time Bins for Latency Bin Tracking.

        Returns:
            number
        """
        return self._get_attribute('numberOfBins')
    @NumberOfBins.setter
    def NumberOfBins(self, value):
        self._set_attribute('numberOfBins', value)

    def update(self, BinLimits=None, Enabled=None, NumberOfBins=None):
        """Updates a child instance of latencyBin on the server.

        Args:
            BinLimits (list(number)): Specifies the upper limit of each Time Bins for Latency Bin Tracking.
            Enabled (bool): If true, Latency Bin Tracking is enabled.
            NumberOfBins (number): Specifies the number of Time Bins for Latency Bin Tracking.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
