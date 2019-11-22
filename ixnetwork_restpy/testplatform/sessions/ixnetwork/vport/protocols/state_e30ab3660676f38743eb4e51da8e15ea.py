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


class State(Base):
    """Describes the current state of the physical port.
    The State class encapsulates a required state resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'state'

    def __init__(self, parent):
        super(State, self).__init__(parent)

    @property
    def LinkDown(self):
        """Indicates that, no physical link is present.

        Returns:
            bool
        """
        return self._get_attribute('linkDown')
    @LinkDown.setter
    def LinkDown(self, value):
        self._set_attribute('linkDown', value)

    @property
    def StpBlock(self):
        """Indicates that the port is not part of spanning tree.

        Returns:
            bool
        """
        return self._get_attribute('stpBlock')
    @StpBlock.setter
    def StpBlock(self, value):
        self._set_attribute('stpBlock', value)

    @property
    def StpForward(self):
        """Indicates that the port is learning and relaying frames.

        Returns:
            bool
        """
        return self._get_attribute('stpForward')
    @StpForward.setter
    def StpForward(self, value):
        self._set_attribute('stpForward', value)

    @property
    def StpLearn(self):
        """Indicates that the port is learning but not relaying frames.

        Returns:
            bool
        """
        return self._get_attribute('stpLearn')
    @StpLearn.setter
    def StpLearn(self, value):
        self._set_attribute('stpLearn', value)

    @property
    def StpListen(self):
        """Indicates that the port is not learning or relaying frames.

        Returns:
            bool
        """
        return self._get_attribute('stpListen')
    @StpListen.setter
    def StpListen(self, value):
        self._set_attribute('stpListen', value)

    def update(self, LinkDown=None, StpBlock=None, StpForward=None, StpLearn=None, StpListen=None):
        """Updates a child instance of state on the server.

        Args:
            LinkDown (bool): Indicates that, no physical link is present.
            StpBlock (bool): Indicates that the port is not part of spanning tree.
            StpForward (bool): Indicates that the port is learning and relaying frames.
            StpLearn (bool): Indicates that the port is learning but not relaying frames.
            StpListen (bool): Indicates that the port is not learning or relaying frames.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
