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


class Dcc(Base):
    """The Layer 1 Configuration is being configured for a POS port and DCC is selected as the Payload Type.
    The Dcc class encapsulates a required dcc resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dcc'
    _SDM_ATT_MAP = {
        'Crc': 'crc',
        'OverheadByte': 'overheadByte',
        'TimeFill': 'timeFill',
    }

    def __init__(self, parent):
        super(Dcc, self).__init__(parent)

    @property
    def Crc(self):
        """
        Returns
        -------
        - str(crc16 | crc32): Choose the type of Cyclic Redundancy Check to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Crc'])
    @Crc.setter
    def Crc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Crc'], value)

    @property
    def OverheadByte(self):
        """
        Returns
        -------
        - str(loh | soh): Choose the type of Overhead bytes to be used for transmitting the DCC packet streams.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverheadByte'])
    @OverheadByte.setter
    def OverheadByte(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverheadByte'], value)

    @property
    def TimeFill(self):
        """
        Returns
        -------
        - str(flag7E | markIdle): Choose the type of bytes used to fill the gaps between DCC frames.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeFill'])
    @TimeFill.setter
    def TimeFill(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimeFill'], value)

    def update(self, Crc=None, OverheadByte=None, TimeFill=None):
        """Updates dcc resource on the server.

        Args
        ----
        - Crc (str(crc16 | crc32)): Choose the type of Cyclic Redundancy Check to be used.
        - OverheadByte (str(loh | soh)): Choose the type of Overhead bytes to be used for transmitting the DCC packet streams.
        - TimeFill (str(flag7E | markIdle)): Choose the type of bytes used to fill the gaps between DCC frames.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
