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


class FrameRateDistribution(Base):
    """This object provides the options for Frame Rate distribution.
    The FrameRateDistribution class encapsulates a required frameRateDistribution resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'frameRateDistribution'

    def __init__(self, parent):
        super(FrameRateDistribution, self).__init__(parent)

    @property
    def PortDistribution(self):
        """At the port level, apply the target configuration transmission rate for each encapsulation.

        Returns:
            str(applyRateToAll|splitRateEvenly)
        """
        return self._get_attribute('portDistribution')
    @PortDistribution.setter
    def PortDistribution(self, value):
        self._set_attribute('portDistribution', value)

    @property
    def StreamDistribution(self):
        """At the flow group level, apply the target rate of each port.

        Returns:
            str(applyRateToAll|splitRateEvenly)
        """
        return self._get_attribute('streamDistribution')
    @StreamDistribution.setter
    def StreamDistribution(self, value):
        self._set_attribute('streamDistribution', value)

    def update(self, PortDistribution=None, StreamDistribution=None):
        """Updates a child instance of frameRateDistribution on the server.

        Args:
            PortDistribution (str(applyRateToAll|splitRateEvenly)): At the port level, apply the target configuration transmission rate for each encapsulation.
            StreamDistribution (str(applyRateToAll|splitRateEvenly)): At the flow group level, apply the target rate of each port.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
