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
import sys
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class MeasurementMode(Base):
    """Signifies the measurement mode.
    The MeasurementMode class encapsulates a required measurementMode resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'measurementMode'
    _SDM_ATT_MAP = {
        'MeasurementMode': 'measurementMode',
    }
    _SDM_ENUM_MAP = {
        'measurementMode': ['cumulativeMode', 'instantaneousMode', 'mixedMode'],
    }

    def __init__(self, parent, list_op=False):
        super(MeasurementMode, self).__init__(parent, list_op)

    @property
    def MeasurementMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cumulativeMode | instantaneousMode | mixedMode): Mode of the measurement
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeasurementMode'])
    @MeasurementMode.setter
    def MeasurementMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MeasurementMode'], value)

    def update(self, MeasurementMode=None):
        # type: (str) -> MeasurementMode
        """Updates measurementMode resource on the server.

        Args
        ----
        - MeasurementMode (str(cumulativeMode | instantaneousMode | mixedMode)): Mode of the measurement

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, MeasurementMode=None):
        # type: (str) -> MeasurementMode
        """Finds and retrieves measurementMode resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve measurementMode resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all measurementMode resources from the server.

        Args
        ----
        - MeasurementMode (str(cumulativeMode | instantaneousMode | mixedMode)): Mode of the measurement

        Returns
        -------
        - self: This instance with matching measurementMode resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of measurementMode data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the measurementMode resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
