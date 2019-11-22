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


class QueueProperty(Base):
    """An object that allows you to define the OpenFlow Queue property configurations.
    The QueueProperty class encapsulates a required queueProperty resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'queueProperty'

    def __init__(self, parent):
        super(QueueProperty, self).__init__(parent)

    @property
    def MaximumDataRate(self):
        """If true, indicates that a maximum data rate is guaranteed.

        Returns:
            bool
        """
        return self._get_attribute('maximumDataRate')
    @MaximumDataRate.setter
    def MaximumDataRate(self, value):
        self._set_attribute('maximumDataRate', value)

    @property
    def MinimumDataRateGuaranteed(self):
        """If true, indicates that a minimum data rate is guaranteed.

        Returns:
            bool
        """
        return self._get_attribute('minimumDataRateGuaranteed')
    @MinimumDataRateGuaranteed.setter
    def MinimumDataRateGuaranteed(self, value):
        self._set_attribute('minimumDataRateGuaranteed', value)

    @property
    def IsNone(self):
        """If true, indicates that no property is defined for the queue.

        Returns:
            bool
        """
        return self._get_attribute('none')
    @IsNone.setter
    def IsNone(self, value):
        self._set_attribute('none', value)

    def update(self, MaximumDataRate=None, MinimumDataRateGuaranteed=None):
        """Updates a child instance of queueProperty on the server.

        Args:
            MaximumDataRate (bool): If true, indicates that a maximum data rate is guaranteed.
            MinimumDataRateGuaranteed (bool): If true, indicates that a minimum data rate is guaranteed.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
