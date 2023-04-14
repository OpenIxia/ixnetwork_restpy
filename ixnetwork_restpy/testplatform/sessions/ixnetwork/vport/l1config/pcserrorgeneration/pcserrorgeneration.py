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


class PcsErrorGeneration(Base):
    """
    The PcsErrorGeneration class encapsulates a required pcsErrorGeneration resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "pcsErrorGeneration"
    _SDM_ATT_MAP = {
        "Continuous": "continuous",
        "Count": "count",
        "ErrorBitsHexLaneMarkers": "errorBitsHexLaneMarkers",
        "PcsLane": "pcsLane",
        "Period": "period",
        "PeriodType": "periodType",
        "Repeat": "repeat",
        "SyncHex": "syncHex",
    }
    _SDM_ENUM_MAP = {
        "periodType": ["laneMarkers", "laneMarkersAndPayload"],
    }

    def __init__(self, parent, list_op=False):
        super(PcsErrorGeneration, self).__init__(parent, list_op)

    @property
    def Continuous(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable/Disable continuous error generation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Continuous"])

    @Continuous.setter
    def Continuous(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Continuous"], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Count value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @Count.setter
    def Count(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Count"], value)

    @property
    def ErrorBitsHexLaneMarkers(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Error bits Lane Markers value in hexadecimal. E.g. - 00 00 00 00 11 FF 00 0A
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorBitsHexLaneMarkers"])

    @ErrorBitsHexLaneMarkers.setter
    def ErrorBitsHexLaneMarkers(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErrorBitsHexLaneMarkers"], value)

    @property
    def PcsLane(self):
        # type: () -> int
        """
        Returns
        -------
        - number: PCS lane number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsLane"])

    @PcsLane.setter
    def PcsLane(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsLane"], value)

    @property
    def Period(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Period value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Period"])

    @Period.setter
    def Period(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Period"], value)

    @property
    def PeriodType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(laneMarkers | laneMarkersAndPayload): Period Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeriodType"])

    @PeriodType.setter
    def PeriodType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PeriodType"], value)

    @property
    def Repeat(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Repeat value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Repeat"])

    @Repeat.setter
    def Repeat(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Repeat"], value)

    @property
    def SyncHex(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sync error bit value in hexadecimal.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SyncHex"])

    @SyncHex.setter
    def SyncHex(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SyncHex"], value)

    def update(
        self,
        Continuous=None,
        Count=None,
        ErrorBitsHexLaneMarkers=None,
        PcsLane=None,
        Period=None,
        PeriodType=None,
        Repeat=None,
        SyncHex=None,
    ):
        # type: (bool, int, str, int, int, str, int, str) -> PcsErrorGeneration
        """Updates pcsErrorGeneration resource on the server.

        Args
        ----
        - Continuous (bool): Enable/Disable continuous error generation.
        - Count (number): Count value.
        - ErrorBitsHexLaneMarkers (str): Error bits Lane Markers value in hexadecimal. E.g. - 00 00 00 00 11 FF 00 0A
        - PcsLane (number): PCS lane number.
        - Period (number): Period value.
        - PeriodType (str(laneMarkers | laneMarkersAndPayload)): Period Type.
        - Repeat (number): Repeat value.
        - SyncHex (str): Sync error bit value in hexadecimal.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Continuous=None,
        Count=None,
        ErrorBitsHexLaneMarkers=None,
        PcsLane=None,
        Period=None,
        PeriodType=None,
        Repeat=None,
        SyncHex=None,
    ):
        # type: (bool, int, str, int, int, str, int, str) -> PcsErrorGeneration
        """Finds and retrieves pcsErrorGeneration resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pcsErrorGeneration resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pcsErrorGeneration resources from the server.

        Args
        ----
        - Continuous (bool): Enable/Disable continuous error generation.
        - Count (number): Count value.
        - ErrorBitsHexLaneMarkers (str): Error bits Lane Markers value in hexadecimal. E.g. - 00 00 00 00 11 FF 00 0A
        - PcsLane (number): PCS lane number.
        - Period (number): Period value.
        - PeriodType (str(laneMarkers | laneMarkersAndPayload)): Period Type.
        - Repeat (number): Repeat value.
        - SyncHex (str): Sync error bit value in hexadecimal.

        Returns
        -------
        - self: This instance with matching pcsErrorGeneration resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pcsErrorGeneration data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pcsErrorGeneration resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
