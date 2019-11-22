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


class CistLearnedInfo(Base):
    """Learned information associated with a CIST on an (MSTP) stpBridge.
    The CistLearnedInfo class encapsulates a required cistLearnedInfo resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'cistLearnedInfo'

    def __init__(self, parent):
        super(CistLearnedInfo, self).__init__(parent)

    @property
    def RegRootCost(self):
        """(Read-only) The cost for the shortest path from the advertising bridge to the regional root bridge.

        Returns:
            number
        """
        return self._get_attribute('regRootCost')

    @property
    def RegRootMac(self):
        """(Read-only) The regional root MAC address being advertised by the bridge.

        Returns:
            str
        """
        return self._get_attribute('regRootMac')

    @property
    def RegRootPriority(self):
        """(Read-only) The regional root priority being advertised by the bridge.

        Returns:
            number
        """
        return self._get_attribute('regRootPriority')

    @property
    def RootCost(self):
        """(Read-only) The cost for the shortest path from the advertising bridge to the root bridge.

        Returns:
            number
        """
        return self._get_attribute('rootCost')

    @property
    def RootMac(self):
        """(Read-only) The root bridge MAC address being advertised.

        Returns:
            str
        """
        return self._get_attribute('rootMac')

    @property
    def RootPriority(self):
        """(Read-only) The priority being advertised for the root bridge.

        Returns:
            number
        """
        return self._get_attribute('rootPriority')
