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


class LinkMode(Base):
    """NOT DEFINED
    The LinkMode class encapsulates a required linkMode resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'linkMode'
    _SDM_ATT_MAP = {
        'Ofppf100GbFd': 'ofppf100GbFd',
        'Ofppf100MbFd': 'ofppf100MbFd',
        'Ofppf100MbHd': 'ofppf100MbHd',
        'Ofppf10GbFd': 'ofppf10GbFd',
        'Ofppf10MbFd': 'ofppf10MbFd',
        'Ofppf10MbHd': 'ofppf10MbHd',
        'Ofppf1GbFd': 'ofppf1GbFd',
        'Ofppf1GbHd': 'ofppf1GbHd',
        'Ofppf1TbFd': 'ofppf1TbFd',
        'Ofppf40GbFd': 'ofppf40GbFd',
        'OfppfOther': 'ofppfOther',
    }

    def __init__(self, parent):
        super(LinkMode, self).__init__(parent)

    @property
    def Ofppf100GbFd(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ofppf100GbFd'])
    @Ofppf100GbFd.setter
    def Ofppf100GbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ofppf100GbFd'], value)

    @property
    def Ofppf100MbFd(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ofppf100MbFd'])
    @Ofppf100MbFd.setter
    def Ofppf100MbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ofppf100MbFd'], value)

    @property
    def Ofppf100MbHd(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ofppf100MbHd'])
    @Ofppf100MbHd.setter
    def Ofppf100MbHd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ofppf100MbHd'], value)

    @property
    def Ofppf10GbFd(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ofppf10GbFd'])
    @Ofppf10GbFd.setter
    def Ofppf10GbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ofppf10GbFd'], value)

    @property
    def Ofppf10MbFd(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ofppf10MbFd'])
    @Ofppf10MbFd.setter
    def Ofppf10MbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ofppf10MbFd'], value)

    @property
    def Ofppf10MbHd(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ofppf10MbHd'])
    @Ofppf10MbHd.setter
    def Ofppf10MbHd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ofppf10MbHd'], value)

    @property
    def Ofppf1GbFd(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ofppf1GbFd'])
    @Ofppf1GbFd.setter
    def Ofppf1GbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ofppf1GbFd'], value)

    @property
    def Ofppf1GbHd(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ofppf1GbHd'])
    @Ofppf1GbHd.setter
    def Ofppf1GbHd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ofppf1GbHd'], value)

    @property
    def Ofppf1TbFd(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ofppf1TbFd'])
    @Ofppf1TbFd.setter
    def Ofppf1TbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ofppf1TbFd'], value)

    @property
    def Ofppf40GbFd(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ofppf40GbFd'])
    @Ofppf40GbFd.setter
    def Ofppf40GbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ofppf40GbFd'], value)

    @property
    def OfppfOther(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['OfppfOther'])
    @OfppfOther.setter
    def OfppfOther(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OfppfOther'], value)

    def update(self, Ofppf100GbFd=None, Ofppf100MbFd=None, Ofppf100MbHd=None, Ofppf10GbFd=None, Ofppf10MbFd=None, Ofppf10MbHd=None, Ofppf1GbFd=None, Ofppf1GbHd=None, Ofppf1TbFd=None, Ofppf40GbFd=None, OfppfOther=None):
        """Updates linkMode resource on the server.

        Args
        ----
        - Ofppf100GbFd (bool): NOT DEFINED
        - Ofppf100MbFd (bool): NOT DEFINED
        - Ofppf100MbHd (bool): NOT DEFINED
        - Ofppf10GbFd (bool): NOT DEFINED
        - Ofppf10MbFd (bool): NOT DEFINED
        - Ofppf10MbHd (bool): NOT DEFINED
        - Ofppf1GbFd (bool): NOT DEFINED
        - Ofppf1GbHd (bool): NOT DEFINED
        - Ofppf1TbFd (bool): NOT DEFINED
        - Ofppf40GbFd (bool): NOT DEFINED
        - OfppfOther (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
