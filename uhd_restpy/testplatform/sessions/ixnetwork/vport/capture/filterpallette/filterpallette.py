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


class FilterPallette(Base):
    """This object specifies the filter pallette properties.
    The FilterPallette class encapsulates a required filterPallette resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'filterPallette'
    _SDM_ATT_MAP = {
        'DA1': 'DA1',
        'DA2': 'DA2',
        'DAMask1': 'DAMask1',
        'DAMask2': 'DAMask2',
        'SA1': 'SA1',
        'SA2': 'SA2',
        'SAMask1': 'SAMask1',
        'SAMask2': 'SAMask2',
        'Pattern1': 'pattern1',
        'Pattern2': 'pattern2',
        'PatternMask1': 'patternMask1',
        'PatternMask2': 'patternMask2',
        'PatternOffset1': 'patternOffset1',
        'PatternOffset2': 'patternOffset2',
        'PatternOffsetType1': 'patternOffsetType1',
        'PatternOffsetType2': 'patternOffsetType2',
    }

    def __init__(self, parent):
        super(FilterPallette, self).__init__(parent)

    @property
    def DA1(self):
        """
        Returns
        -------
        - str: Only frames that contain this destination MAC address are filtered, captured or counted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DA1'])
    @DA1.setter
    def DA1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DA1'], value)

    @property
    def DA2(self):
        """
        Returns
        -------
        - str: Only frames that contain this destination MAC address are filtered, captured or counted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DA2'])
    @DA2.setter
    def DA2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DA2'], value)

    @property
    def DAMask1(self):
        """
        Returns
        -------
        - str: Only frames that contain this destination MAC address are filtered, captured or counted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DAMask1'])
    @DAMask1.setter
    def DAMask1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DAMask1'], value)

    @property
    def DAMask2(self):
        """
        Returns
        -------
        - str: A bit mask that allows the user to specify which bits of the DA2 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter
        """
        return self._get_attribute(self._SDM_ATT_MAP['DAMask2'])
    @DAMask2.setter
    def DAMask2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DAMask2'], value)

    @property
    def SA1(self):
        """
        Returns
        -------
        - str: Only frames that contain this source MAC address are filtered, captured or counted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SA1'])
    @SA1.setter
    def SA1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SA1'], value)

    @property
    def SA2(self):
        """
        Returns
        -------
        - str: Only frames that contain this source MAC address are filtered, captured or counted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SA2'])
    @SA2.setter
    def SA2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SA2'], value)

    @property
    def SAMask1(self):
        """
        Returns
        -------
        - str: A bit mask that allows the user to specify which bits of the SA1 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SAMask1'])
    @SAMask1.setter
    def SAMask1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SAMask1'], value)

    @property
    def SAMask2(self):
        """
        Returns
        -------
        - str: A bit mask that allows the user to specify which bits of the SA2 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter
        """
        return self._get_attribute(self._SDM_ATT_MAP['SAMask2'])
    @SAMask2.setter
    def SAMask2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SAMask2'], value)

    @property
    def Pattern1(self):
        """
        Returns
        -------
        - str: Only frames that contain this pattern at offset patternOffset1 are filtered, captured or counted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Pattern1'])
    @Pattern1.setter
    def Pattern1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Pattern1'], value)

    @property
    def Pattern2(self):
        """
        Returns
        -------
        - str: Only frames that contain this pattern at offset patternOffset2 are filtered, captured or counted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Pattern2'])
    @Pattern2.setter
    def Pattern2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Pattern2'], value)

    @property
    def PatternMask1(self):
        """
        Returns
        -------
        - str: A bit mask that allows the user to specify which bits of pattern1 should be used when filtering. If the mask bit is set low, the pattern bit will be used in the filter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PatternMask1'])
    @PatternMask1.setter
    def PatternMask1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PatternMask1'], value)

    @property
    def PatternMask2(self):
        """
        Returns
        -------
        - str: A bit mask that allows the user to specify which bits of pattern2 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PatternMask2'])
    @PatternMask2.setter
    def PatternMask2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PatternMask2'], value)

    @property
    def PatternOffset1(self):
        """
        Returns
        -------
        - number: Offset of pattern1 in the frame to be filtered, captured or counted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PatternOffset1'])
    @PatternOffset1.setter
    def PatternOffset1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PatternOffset1'], value)

    @property
    def PatternOffset2(self):
        """
        Returns
        -------
        - number: Offset of pattern2 in the frame to be filtered, captured or counted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PatternOffset2'])
    @PatternOffset2.setter
    def PatternOffset2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PatternOffset2'], value)

    @property
    def PatternOffsetType1(self):
        """
        Returns
        -------
        - str(filterPalletteOffsetStartOfFrame | filterPalletteOffsetStartOfIp | filterPalletteOffsetStartOfProtocol): For ports that support the portFeaturePatternOffsetFlexible feature, this option specifies the place that patternOffset1 is relative to.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PatternOffsetType1'])
    @PatternOffsetType1.setter
    def PatternOffsetType1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PatternOffsetType1'], value)

    @property
    def PatternOffsetType2(self):
        """
        Returns
        -------
        - str(filterPalletteOffsetStartOfFrame | filterPalletteOffsetStartOfIp | filterPalletteOffsetStartOfProtocol): For ports that support the portFeaturePatternOffsetFlexible feature, this option specifies the place that patternOffset1 is relative to.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PatternOffsetType2'])
    @PatternOffsetType2.setter
    def PatternOffsetType2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PatternOffsetType2'], value)

    def update(self, DA1=None, DA2=None, DAMask1=None, DAMask2=None, SA1=None, SA2=None, SAMask1=None, SAMask2=None, Pattern1=None, Pattern2=None, PatternMask1=None, PatternMask2=None, PatternOffset1=None, PatternOffset2=None, PatternOffsetType1=None, PatternOffsetType2=None):
        """Updates filterPallette resource on the server.

        Args
        ----
        - DA1 (str): Only frames that contain this destination MAC address are filtered, captured or counted.
        - DA2 (str): Only frames that contain this destination MAC address are filtered, captured or counted.
        - DAMask1 (str): Only frames that contain this destination MAC address are filtered, captured or counted.
        - DAMask2 (str): A bit mask that allows the user to specify which bits of the DA2 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter
        - SA1 (str): Only frames that contain this source MAC address are filtered, captured or counted.
        - SA2 (str): Only frames that contain this source MAC address are filtered, captured or counted.
        - SAMask1 (str): A bit mask that allows the user to specify which bits of the SA1 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter.
        - SAMask2 (str): A bit mask that allows the user to specify which bits of the SA2 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter
        - Pattern1 (str): Only frames that contain this pattern at offset patternOffset1 are filtered, captured or counted.
        - Pattern2 (str): Only frames that contain this pattern at offset patternOffset2 are filtered, captured or counted.
        - PatternMask1 (str): A bit mask that allows the user to specify which bits of pattern1 should be used when filtering. If the mask bit is set low, the pattern bit will be used in the filter.
        - PatternMask2 (str): A bit mask that allows the user to specify which bits of pattern2 should be used when filtering. If the mask bit is set high, the pattern bit will be used in the filter.
        - PatternOffset1 (number): Offset of pattern1 in the frame to be filtered, captured or counted.
        - PatternOffset2 (number): Offset of pattern2 in the frame to be filtered, captured or counted.
        - PatternOffsetType1 (str(filterPalletteOffsetStartOfFrame | filterPalletteOffsetStartOfIp | filterPalletteOffsetStartOfProtocol)): For ports that support the portFeaturePatternOffsetFlexible feature, this option specifies the place that patternOffset1 is relative to.
        - PatternOffsetType2 (str(filterPalletteOffsetStartOfFrame | filterPalletteOffsetStartOfIp | filterPalletteOffsetStartOfProtocol)): For ports that support the portFeaturePatternOffsetFlexible feature, this option specifies the place that patternOffset1 is relative to.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
