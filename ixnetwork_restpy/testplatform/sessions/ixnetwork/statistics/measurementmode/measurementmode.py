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


class MeasurementMode(Base):
    """Signifies the measurement mode.
    The MeasurementMode class encapsulates a required measurementMode resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'measurementMode'

    def __init__(self, parent):
        super(MeasurementMode, self).__init__(parent)

    @property
    def MeasurementMode(self):
        """Mode of the measurement

        Returns:
            str(cumulativeMode|instantaneousMode|mixedMode)
        """
        return self._get_attribute('measurementMode')
    @MeasurementMode.setter
    def MeasurementMode(self, value):
        self._set_attribute('measurementMode', value)

    def update(self, MeasurementMode=None):
        """Updates a child instance of measurementMode on the server.

        Args:
            MeasurementMode (str(cumulativeMode|instantaneousMode|mixedMode)): Mode of the measurement

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
