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


class SendgPtpSignalingParams(Base):
    """Send Signaling messages for the selected PTP IEEE 802.1AS sessions.
    The SendgPtpSignalingParams class encapsulates a required sendgPtpSignalingParams resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'sendgPtpSignalingParams'
    _SDM_ATT_MAP = {
        'AnnounceInterval': 'announceInterval',
        'ComputeNeighborPropDelay': 'computeNeighborPropDelay',
        'ComputeNeighborRateRatio': 'computeNeighborRateRatio',
        'LinkDelayInterval': 'linkDelayInterval',
        'TimeSyncInterval': 'timeSyncInterval',
    }

    def __init__(self, parent):
        super(SendgPtpSignalingParams, self).__init__(parent)

    @property
    def AnnounceInterval(self):
        """
        Returns
        -------
        - str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_): Desired announceInterval
        """
        return self._get_attribute(self._SDM_ATT_MAP['AnnounceInterval'])
    @AnnounceInterval.setter
    def AnnounceInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AnnounceInterval'], value)

    @property
    def ComputeNeighborPropDelay(self):
        """
        Returns
        -------
        - bool: computeNeighborPropDelay flag
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComputeNeighborPropDelay'])
    @ComputeNeighborPropDelay.setter
    def ComputeNeighborPropDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComputeNeighborPropDelay'], value)

    @property
    def ComputeNeighborRateRatio(self):
        """
        Returns
        -------
        - bool: computeNeighborRateRatio flag
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComputeNeighborRateRatio'])
    @ComputeNeighborRateRatio.setter
    def ComputeNeighborRateRatio(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ComputeNeighborRateRatio'], value)

    @property
    def LinkDelayInterval(self):
        """
        Returns
        -------
        - str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_): Desired linkDelayInterval
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkDelayInterval'])
    @LinkDelayInterval.setter
    def LinkDelayInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkDelayInterval'], value)

    @property
    def TimeSyncInterval(self):
        """
        Returns
        -------
        - str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_): Desired timeSyncInterval
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeSyncInterval'])
    @TimeSyncInterval.setter
    def TimeSyncInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimeSyncInterval'], value)

    def update(self, AnnounceInterval=None, ComputeNeighborPropDelay=None, ComputeNeighborRateRatio=None, LinkDelayInterval=None, TimeSyncInterval=None):
        """Updates sendgPtpSignalingParams resource on the server.

        Args
        ----
        - AnnounceInterval (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired announceInterval
        - ComputeNeighborPropDelay (bool): computeNeighborPropDelay flag
        - ComputeNeighborRateRatio (bool): computeNeighborRateRatio flag
        - LinkDelayInterval (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired linkDelayInterval
        - TimeSyncInterval (str(v0_1_per_second_ | v1_1_per_2_seconds_ | v2_1_per_4_seconds_ | v3_1_per_8_seconds_ | v4_1_per_16_seconds_ | v5_1_per_32_seconds_ | v6_1_per_64_seconds_ | v7_1_per_128_seconds_ | v8_1_per_256_seconds_ | v9_1_per_512_seconds_ | initial | stop | doNotChange | vneg9_512_per_second_ | vneg8_256_per_second_ | vneg7_128_per_second_ | vneg6_64_per_second_ | vneg5_32_per_second_ | vneg4_16_per_second_ | vneg3_8_per_second_ | vneg2_4_per_second_ | vneg1_2_per_second_)): Desired timeSyncInterval

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def SendgPtpSignaling(self):
        """Executes the sendgPtpSignaling operation on the server.

        Send Signaling messages for the selected PTP IEEE 802.1AS sessions.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendgPtpSignaling', payload=payload, response_object=None)
