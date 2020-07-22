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


class BitError(Base):
    """Introduce bit errors.
    The BitError class encapsulates a required bitError resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bitError'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'LogRate': 'logRate',
        'SkipEndOctets': 'skipEndOctets',
        'SkipStartOctets': 'skipStartOctets',
    }

    def __init__(self, parent):
        super(BitError, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, periodically introduce bit errors.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def LogRate(self):
        """
        Returns
        -------
        - number: If logRate is n, error one out of 10^n bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LogRate'])
    @LogRate.setter
    def LogRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LogRate'], value)

    @property
    def SkipEndOctets(self):
        """
        Returns
        -------
        - number: Number of octets to skip at the end of each packet when erroring bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SkipEndOctets'])
    @SkipEndOctets.setter
    def SkipEndOctets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SkipEndOctets'], value)

    @property
    def SkipStartOctets(self):
        """
        Returns
        -------
        - number: Number of octets to skip at the start of each packet when erroring bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SkipStartOctets'])
    @SkipStartOctets.setter
    def SkipStartOctets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SkipStartOctets'], value)

    def update(self, Enabled=None, LogRate=None, SkipEndOctets=None, SkipStartOctets=None):
        """Updates bitError resource on the server.

        Args
        ----
        - Enabled (bool): If true, periodically introduce bit errors.
        - LogRate (number): If logRate is n, error one out of 10^n bits.
        - SkipEndOctets (number): Number of octets to skip at the end of each packet when erroring bits.
        - SkipStartOctets (number): Number of octets to skip at the start of each packet when erroring bits.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
