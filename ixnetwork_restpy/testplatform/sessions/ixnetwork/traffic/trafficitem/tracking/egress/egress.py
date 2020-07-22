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


class Egress(Base):
    """DEPRECATED This object provides different options for Egress Tracking.
    The Egress class encapsulates a required egress resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'egress'
    _SDM_ATT_MAP = {
        'AvailableEncapsulations': 'availableEncapsulations',
        'AvailableOffsets': 'availableOffsets',
        'CustomOffsetBits': 'customOffsetBits',
        'CustomWidthBits': 'customWidthBits',
        'Enabled': 'enabled',
        'Encapsulation': 'encapsulation',
        'Offset': 'offset',
    }

    def __init__(self, parent):
        super(Egress, self).__init__(parent)

    @property
    def FieldOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.tracking.egress.fieldoffset.fieldoffset.FieldOffset): An instance of the FieldOffset class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.tracking.egress.fieldoffset.fieldoffset import FieldOffset
        return FieldOffset(self)._select()

    @property
    def AvailableEncapsulations(self):
        """
        Returns
        -------
        - list(str): Specifies the available Encapsulations for Egress Tracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableEncapsulations'])

    @property
    def AvailableOffsets(self):
        """
        Returns
        -------
        - list(str): Specifies the available Offsets for Egress Tracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableOffsets'])

    @property
    def CustomOffsetBits(self):
        """
        Returns
        -------
        - number: Specifies the Custom Offset in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomOffsetBits'])
    @CustomOffsetBits.setter
    def CustomOffsetBits(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomOffsetBits'], value)

    @property
    def CustomWidthBits(self):
        """
        Returns
        -------
        - number: Specifies the Custom Width in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomWidthBits'])
    @CustomWidthBits.setter
    def CustomWidthBits(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomWidthBits'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, egress tracking is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Encapsulation(self):
        """
        Returns
        -------
        - str: Specifies the Encapsulation for Egress Tracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Encapsulation'])
    @Encapsulation.setter
    def Encapsulation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Encapsulation'], value)

    @property
    def Offset(self):
        """
        Returns
        -------
        - str: Specifies the Offset for Egress Tracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Offset'])
    @Offset.setter
    def Offset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Offset'], value)

    def update(self, CustomOffsetBits=None, CustomWidthBits=None, Enabled=None, Encapsulation=None, Offset=None):
        """Updates egress resource on the server.

        Args
        ----
        - CustomOffsetBits (number): Specifies the Custom Offset in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings.
        - CustomWidthBits (number): Specifies the Custom Width in bits for Egress Tracking when Encapsulation is Any: Use Custom Settings.
        - Enabled (bool): If true, egress tracking is enabled.
        - Encapsulation (str): Specifies the Encapsulation for Egress Tracking.
        - Offset (str): Specifies the Offset for Egress Tracking.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
