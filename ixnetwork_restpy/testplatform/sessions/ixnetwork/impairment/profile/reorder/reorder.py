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


class Reorder(Base):
    """Reorder packets.
    The Reorder class encapsulates a required reorder resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'reorder'
    _SDM_ATT_MAP = {
        'ClusterSize': 'clusterSize',
        'Enabled': 'enabled',
        'PercentRate': 'percentRate',
        'SkipCount': 'skipCount',
    }

    def __init__(self, parent):
        super(Reorder, self).__init__(parent)

    @property
    def ClusterSize(self):
        """
        Returns
        -------
        - number: Number of packets to reorder on each occurrence.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClusterSize'])
    @ClusterSize.setter
    def ClusterSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClusterSize'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, periodically reorder received packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def PercentRate(self):
        """
        Returns
        -------
        - number: How often to reorder packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PercentRate'])
    @PercentRate.setter
    def PercentRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PercentRate'], value)

    @property
    def SkipCount(self):
        """
        Returns
        -------
        - number: How many packets to skip before sending the reordered packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SkipCount'])
    @SkipCount.setter
    def SkipCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SkipCount'], value)

    def update(self, ClusterSize=None, Enabled=None, PercentRate=None, SkipCount=None):
        """Updates reorder resource on the server.

        Args
        ----
        - ClusterSize (number): Number of packets to reorder on each occurrence.
        - Enabled (bool): If true, periodically reorder received packets.
        - PercentRate (number): How often to reorder packets.
        - SkipCount (number): How many packets to skip before sending the reordered packets.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
