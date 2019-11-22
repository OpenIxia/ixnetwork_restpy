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


class AdvertisedFeatures(Base):
    """This object allows to define the advertised features of physical ports available in a datapath.
    The AdvertisedFeatures class encapsulates a required advertisedFeatures resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'advertisedFeatures'

    def __init__(self, parent):
        super(AdvertisedFeatures, self).__init__(parent)

    @property
    def HundredMbFd(self):
        """Indicates that the advertized features include 100 Mb full-duplex rate support.

        Returns:
            bool
        """
        return self._get_attribute('100MbFd')
    @HundredMbFd.setter
    def HundredMbFd(self, value):
        self._set_attribute('100MbFd', value)

    @property
    def HundredMbHd(self):
        """Indicates that the advertized features include 100 Mb half-duplex rate support.

        Returns:
            bool
        """
        return self._get_attribute('100MbHd')
    @HundredMbHd.setter
    def HundredMbHd(self, value):
        self._set_attribute('100MbHd', value)

    @property
    def TenGbFd(self):
        """Indicates that the advertized features include 10 Gb full-duplex rate support.

        Returns:
            bool
        """
        return self._get_attribute('10GbFd')
    @TenGbFd.setter
    def TenGbFd(self, value):
        self._set_attribute('10GbFd', value)

    @property
    def TenMbFd(self):
        """Indicates that the advertized features include 10 Mb full-duplex rate support.

        Returns:
            bool
        """
        return self._get_attribute('10MbFd')
    @TenMbFd.setter
    def TenMbFd(self, value):
        self._set_attribute('10MbFd', value)

    @property
    def TenMbHd(self):
        """Indicates that the advertized features include 10 Mb half-duplex rate support.

        Returns:
            bool
        """
        return self._get_attribute('10MbHd')
    @TenMbHd.setter
    def TenMbHd(self, value):
        self._set_attribute('10MbHd', value)

    @property
    def OneGbFd(self):
        """Indicates that the advertized features include 1 Gb full-duplex rate support.

        Returns:
            bool
        """
        return self._get_attribute('1GbFd')
    @OneGbFd.setter
    def OneGbFd(self, value):
        self._set_attribute('1GbFd', value)

    @property
    def OneGbHd(self):
        """Indicates that the advertized features include 1 Gb half-duplex rate support.

        Returns:
            bool
        """
        return self._get_attribute('1GbHd')
    @OneGbHd.setter
    def OneGbHd(self, value):
        self._set_attribute('1GbHd', value)

    @property
    def AsymmetricPause(self):
        """Indicates that the advertized features include Asymmetric pause.

        Returns:
            bool
        """
        return self._get_attribute('asymmetricPause')
    @AsymmetricPause.setter
    def AsymmetricPause(self, value):
        self._set_attribute('asymmetricPause', value)

    @property
    def AutoNegotiation(self):
        """Indicates that the advertized features include Auto-negotiation.

        Returns:
            bool
        """
        return self._get_attribute('autoNegotiation')
    @AutoNegotiation.setter
    def AutoNegotiation(self, value):
        self._set_attribute('autoNegotiation', value)

    @property
    def CopperMedium(self):
        """Indicates that the advertized features include Copper medium.

        Returns:
            bool
        """
        return self._get_attribute('copperMedium')
    @CopperMedium.setter
    def CopperMedium(self, value):
        self._set_attribute('copperMedium', value)

    @property
    def FiberMedium(self):
        """Indicates that the advertized features include Fiber medium.

        Returns:
            bool
        """
        return self._get_attribute('fiberMedium')
    @FiberMedium.setter
    def FiberMedium(self, value):
        self._set_attribute('fiberMedium', value)

    @property
    def Pause(self):
        """Indicates that the advertized features include Pause.

        Returns:
            bool
        """
        return self._get_attribute('pause')
    @Pause.setter
    def Pause(self, value):
        self._set_attribute('pause', value)

    def update(self, HundredMbFd=None, HundredMbHd=None, TenGbFd=None, TenMbFd=None, TenMbHd=None, OneGbFd=None, OneGbHd=None, AsymmetricPause=None, AutoNegotiation=None, CopperMedium=None, FiberMedium=None, Pause=None):
        """Updates a child instance of advertisedFeatures on the server.

        Args:
            HundredMbFd (bool): Indicates that the advertized features include 100 Mb full-duplex rate support.
            HundredMbHd (bool): Indicates that the advertized features include 100 Mb half-duplex rate support.
            TenGbFd (bool): Indicates that the advertized features include 10 Gb full-duplex rate support.
            TenMbFd (bool): Indicates that the advertized features include 10 Mb full-duplex rate support.
            TenMbHd (bool): Indicates that the advertized features include 10 Mb half-duplex rate support.
            OneGbFd (bool): Indicates that the advertized features include 1 Gb full-duplex rate support.
            OneGbHd (bool): Indicates that the advertized features include 1 Gb half-duplex rate support.
            AsymmetricPause (bool): Indicates that the advertized features include Asymmetric pause.
            AutoNegotiation (bool): Indicates that the advertized features include Auto-negotiation.
            CopperMedium (bool): Indicates that the advertized features include Copper medium.
            FiberMedium (bool): Indicates that the advertized features include Fiber medium.
            Pause (bool): Indicates that the advertized features include Pause.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
