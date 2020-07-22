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


class CurrentFeatures(Base):
    """An object that allows to select the current features (link modes, link types, and link features) from the list that the port will support.
    The CurrentFeatures class encapsulates a required currentFeatures resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'currentFeatures'
    _SDM_ATT_MAP = {
        'HundredGbFd': '100GbFd',
        'HundredMbFd': '100MbFd',
        'HundredMbHd': '100MbHd',
        'TenGbFd': '10GbFd',
        'TenMbFd': '10MbFd',
        'TenMbHd': '10MbHd',
        'OneGbFd': '1GbFd',
        'OneGbHd': '1GbHd',
        'OneTbFd': '1TbFd',
        'FortyGbFd': '40GbFd',
        'AsymmetricPause': 'asymmetricPause',
        'AutoNegotiation': 'autoNegotiation',
        'CopperMedium': 'copperMedium',
        'FiberMedium': 'fiberMedium',
        'OtherRate': 'otherRate',
        'Pause': 'pause',
    }

    def __init__(self, parent):
        super(CurrentFeatures, self).__init__(parent)

    @property
    def HundredGbFd(self):
        """
        Returns
        -------
        - bool: If true, 100 GB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HundredGbFd'])
    @HundredGbFd.setter
    def HundredGbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HundredGbFd'], value)

    @property
    def HundredMbFd(self):
        """
        Returns
        -------
        - bool: If true, 100 MB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HundredMbFd'])
    @HundredMbFd.setter
    def HundredMbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HundredMbFd'], value)

    @property
    def HundredMbHd(self):
        """
        Returns
        -------
        - bool: If true, 100 MB half-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HundredMbHd'])
    @HundredMbHd.setter
    def HundredMbHd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HundredMbHd'], value)

    @property
    def TenGbFd(self):
        """
        Returns
        -------
        - bool: If true, 10 GB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TenGbFd'])
    @TenGbFd.setter
    def TenGbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TenGbFd'], value)

    @property
    def TenMbFd(self):
        """
        Returns
        -------
        - bool: If true, 10 MB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TenMbFd'])
    @TenMbFd.setter
    def TenMbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TenMbFd'], value)

    @property
    def TenMbHd(self):
        """
        Returns
        -------
        - bool: If true, 10 MB half-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TenMbHd'])
    @TenMbHd.setter
    def TenMbHd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TenMbHd'], value)

    @property
    def OneGbFd(self):
        """
        Returns
        -------
        - bool: If true, 1 GB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OneGbFd'])
    @OneGbFd.setter
    def OneGbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OneGbFd'], value)

    @property
    def OneGbHd(self):
        """
        Returns
        -------
        - bool: If true, 1 GB half-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OneGbHd'])
    @OneGbHd.setter
    def OneGbHd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OneGbHd'], value)

    @property
    def OneTbFd(self):
        """
        Returns
        -------
        - bool: If true, 1 TB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OneTbFd'])
    @OneTbFd.setter
    def OneTbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OneTbFd'], value)

    @property
    def FortyGbFd(self):
        """
        Returns
        -------
        - bool: If true, 40 GB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FortyGbFd'])
    @FortyGbFd.setter
    def FortyGbFd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FortyGbFd'], value)

    @property
    def AsymmetricPause(self):
        """
        Returns
        -------
        - bool: If true, asymmetric pause of ports feature is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsymmetricPause'])
    @AsymmetricPause.setter
    def AsymmetricPause(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AsymmetricPause'], value)

    @property
    def AutoNegotiation(self):
        """
        Returns
        -------
        - bool: If true, auto negotiation of ports is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoNegotiation'])
    @AutoNegotiation.setter
    def AutoNegotiation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoNegotiation'], value)

    @property
    def CopperMedium(self):
        """
        Returns
        -------
        - bool: If true, copper medium link type is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CopperMedium'])
    @CopperMedium.setter
    def CopperMedium(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CopperMedium'], value)

    @property
    def FiberMedium(self):
        """
        Returns
        -------
        - bool: If true, fiber medium link type is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FiberMedium'])
    @FiberMedium.setter
    def FiberMedium(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FiberMedium'], value)

    @property
    def OtherRate(self):
        """
        Returns
        -------
        - bool: If true, supports other rate, not in the list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OtherRate'])
    @OtherRate.setter
    def OtherRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OtherRate'], value)

    @property
    def Pause(self):
        """
        Returns
        -------
        - bool: If true, pause ports feature is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Pause'])
    @Pause.setter
    def Pause(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Pause'], value)

    def update(self, HundredGbFd=None, HundredMbFd=None, HundredMbHd=None, TenGbFd=None, TenMbFd=None, TenMbHd=None, OneGbFd=None, OneGbHd=None, OneTbFd=None, FortyGbFd=None, AsymmetricPause=None, AutoNegotiation=None, CopperMedium=None, FiberMedium=None, OtherRate=None, Pause=None):
        """Updates currentFeatures resource on the server.

        Args
        ----
        - HundredGbFd (bool): If true, 100 GB full-duplex rate support is available.
        - HundredMbFd (bool): If true, 100 MB full-duplex rate support is available.
        - HundredMbHd (bool): If true, 100 MB half-duplex rate support is available.
        - TenGbFd (bool): If true, 10 GB full-duplex rate support is available.
        - TenMbFd (bool): If true, 10 MB full-duplex rate support is available.
        - TenMbHd (bool): If true, 10 MB half-duplex rate support is available.
        - OneGbFd (bool): If true, 1 GB full-duplex rate support is available.
        - OneGbHd (bool): If true, 1 GB half-duplex rate support is available.
        - OneTbFd (bool): If true, 1 TB full-duplex rate support is available.
        - FortyGbFd (bool): If true, 40 GB full-duplex rate support is available.
        - AsymmetricPause (bool): If true, asymmetric pause of ports feature is available.
        - AutoNegotiation (bool): If true, auto negotiation of ports is available.
        - CopperMedium (bool): If true, copper medium link type is available.
        - FiberMedium (bool): If true, fiber medium link type is available.
        - OtherRate (bool): If true, supports other rate, not in the list.
        - Pause (bool): If true, pause ports feature is available.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
