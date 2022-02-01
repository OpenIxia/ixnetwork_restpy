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


class DelayVariation(Base):
    """This object fetches delay variation statistics.
    The DelayVariation class encapsulates a required delayVariation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'delayVariation'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'LargeSequenceNumberErrorThreshold': 'largeSequenceNumberErrorThreshold',
        'LatencyMode': 'latencyMode',
        'StatisticsMode': 'statisticsMode',
    }
    _SDM_ENUM_MAP = {
        'latencyMode': ['cutThrough', 'forwardingDelay', 'mef', 'storeForward'],
        'statisticsMode': ['rxDelayVariationAverage', 'rxDelayVariationErrorsAndRate', 'rxDelayVariationMinMaxAndRate'],
    }

    def __init__(self, parent, list_op=False):
        super(DelayVariation, self).__init__(parent, list_op)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, fetches latency delay variation statistics with average, minimum, and maximum measurements.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def LargeSequenceNumberErrorThreshold(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value for the large sequence number error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LargeSequenceNumberErrorThreshold'])
    @LargeSequenceNumberErrorThreshold.setter
    def LargeSequenceNumberErrorThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['LargeSequenceNumberErrorThreshold'], value)

    @property
    def LatencyMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cutThrough | forwardingDelay | mef | storeForward): If enabled, allows to use Cut Through, Forwarding Delay, MEF, and Store and Forward Delay variation statictics measurements.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatencyMode'])
    @LatencyMode.setter
    def LatencyMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LatencyMode'], value)

    @property
    def StatisticsMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(rxDelayVariationAverage | rxDelayVariationErrorsAndRate | rxDelayVariationMinMaxAndRate): If enabled, allows to receive delay variation statistics with sequence error measurements.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StatisticsMode'])
    @StatisticsMode.setter
    def StatisticsMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['StatisticsMode'], value)

    def update(self, Enabled=None, LargeSequenceNumberErrorThreshold=None, LatencyMode=None, StatisticsMode=None):
        # type: (bool, int, str, str) -> DelayVariation
        """Updates delayVariation resource on the server.

        Args
        ----
        - Enabled (bool): If enabled, fetches latency delay variation statistics with average, minimum, and maximum measurements.
        - LargeSequenceNumberErrorThreshold (number): The value for the large sequence number error.
        - LatencyMode (str(cutThrough | forwardingDelay | mef | storeForward)): If enabled, allows to use Cut Through, Forwarding Delay, MEF, and Store and Forward Delay variation statictics measurements.
        - StatisticsMode (str(rxDelayVariationAverage | rxDelayVariationErrorsAndRate | rxDelayVariationMinMaxAndRate)): If enabled, allows to receive delay variation statistics with sequence error measurements.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Enabled=None, LargeSequenceNumberErrorThreshold=None, LatencyMode=None, StatisticsMode=None):
        # type: (bool, int, str, str) -> DelayVariation
        """Finds and retrieves delayVariation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve delayVariation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all delayVariation resources from the server.

        Args
        ----
        - Enabled (bool): If enabled, fetches latency delay variation statistics with average, minimum, and maximum measurements.
        - LargeSequenceNumberErrorThreshold (number): The value for the large sequence number error.
        - LatencyMode (str(cutThrough | forwardingDelay | mef | storeForward)): If enabled, allows to use Cut Through, Forwarding Delay, MEF, and Store and Forward Delay variation statictics measurements.
        - StatisticsMode (str(rxDelayVariationAverage | rxDelayVariationErrorsAndRate | rxDelayVariationMinMaxAndRate)): If enabled, allows to receive delay variation statistics with sequence error measurements.

        Returns
        -------
        - self: This instance with matching delayVariation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of delayVariation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the delayVariation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
