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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class SequenceChecking(Base):
    """This object fetches sequence checking statistics.
    The SequenceChecking class encapsulates a required sequenceChecking resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "sequenceChecking"
    _SDM_ATT_MAP = {
        "AdvancedSequenceThreshold": "advancedSequenceThreshold",
        "Enabled": "enabled",
        "SequenceMode": "sequenceMode",
    }
    _SDM_ENUM_MAP = {
        "sequenceMode": [
            "advanced",
            "rxPacketArrival",
            "rxSwitchedPath",
            "rxThreshold",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(SequenceChecking, self).__init__(parent, list_op)

    @property
    def AdvancedSequenceThreshold(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Checks the sequence.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdvancedSequenceThreshold"])

    @AdvancedSequenceThreshold.setter
    def AdvancedSequenceThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AdvancedSequenceThreshold"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, fetches sequence checking statistics to measure duplicate packets, sequence gap, and the last sequence number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def SequenceMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(advanced | rxPacketArrival | rxSwitchedPath | rxThreshold): The mode to conduct sequence checking.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SequenceMode"])

    @SequenceMode.setter
    def SequenceMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SequenceMode"], value)

    def update(self, AdvancedSequenceThreshold=None, Enabled=None, SequenceMode=None):
        # type: (int, bool, str) -> SequenceChecking
        """Updates sequenceChecking resource on the server.

        Args
        ----
        - AdvancedSequenceThreshold (number): Checks the sequence.
        - Enabled (bool): If enabled, fetches sequence checking statistics to measure duplicate packets, sequence gap, and the last sequence number.
        - SequenceMode (str(advanced | rxPacketArrival | rxSwitchedPath | rxThreshold)): The mode to conduct sequence checking.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AdvancedSequenceThreshold=None, Enabled=None, SequenceMode=None):
        # type: (int, bool, str) -> SequenceChecking
        """Finds and retrieves sequenceChecking resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve sequenceChecking resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all sequenceChecking resources from the server.

        Args
        ----
        - AdvancedSequenceThreshold (number): Checks the sequence.
        - Enabled (bool): If enabled, fetches sequence checking statistics to measure duplicate packets, sequence gap, and the last sequence number.
        - SequenceMode (str(advanced | rxPacketArrival | rxSwitchedPath | rxThreshold)): The mode to conduct sequence checking.

        Returns
        -------
        - self: This instance with matching sequenceChecking resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of sequenceChecking data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the sequenceChecking resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
