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


class Statistics(Base):
    """
    The Statistics class encapsulates a required statistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "statistics"
    _SDM_ATT_MAP = {
        "ForceLegacyPortNameInStats": "forceLegacyPortNameInStats",
        "GraphHistoryClockTime": "graphHistoryClockTime",
        "PersistenceMode": "persistenceMode",
        "SnapshotCSVMode": "snapshotCSVMode",
        "SnapshotCSVPath": "snapshotCSVPath",
    }
    _SDM_ENUM_MAP = {
        "persistenceMode": [
            "mixed",
            "none",
            "persistInBothLocations",
            "persistInConfiguration",
            "persistInUserSettings",
            "preferencesNotSet",
        ],
        "snapshotCSVMode": ["appendCSVFile", "newCSVFile", "overwriteCSVFile"],
    }

    def __init__(self, parent, list_op=False):
        super(Statistics, self).__init__(parent, list_op)

    @property
    def ForceLegacyPortNameInStats(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When false, IxNetwork statistics show port name in <Chassis/Front Panel Port Number> format. When true, it is in <Chassis/Card/Port> format
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForceLegacyPortNameInStats"])

    @ForceLegacyPortNameInStats.setter
    def ForceLegacyPortNameInStats(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForceLegacyPortNameInStats"], value)

    @property
    def GraphHistoryClockTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Tells us amount of time for which data is to be shown (in mint). Min:1, Max:30
        """
        return self._get_attribute(self._SDM_ATT_MAP["GraphHistoryClockTime"])

    @GraphHistoryClockTime.setter
    def GraphHistoryClockTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GraphHistoryClockTime"], value)

    @property
    def PersistenceMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(mixed | none | persistInBothLocations | persistInConfiguration | persistInUserSettings | preferencesNotSet): Set the Persistence Mode: whether to store the data in user location or configuration or both/none
        """
        return self._get_attribute(self._SDM_ATT_MAP["PersistenceMode"])

    @PersistenceMode.setter
    def PersistenceMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PersistenceMode"], value)

    @property
    def SnapshotCSVMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(appendCSVFile | newCSVFile | overwriteCSVFile): Set the CSV Generation Mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["SnapshotCSVMode"])

    @SnapshotCSVMode.setter
    def SnapshotCSVMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SnapshotCSVMode"], value)

    @property
    def SnapshotCSVPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Set the Snapshot CSV Path
        """
        return self._get_attribute(self._SDM_ATT_MAP["SnapshotCSVPath"])

    @SnapshotCSVPath.setter
    def SnapshotCSVPath(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SnapshotCSVPath"], value)

    def update(
        self,
        ForceLegacyPortNameInStats=None,
        GraphHistoryClockTime=None,
        PersistenceMode=None,
        SnapshotCSVMode=None,
        SnapshotCSVPath=None,
    ):
        # type: (bool, int, str, str, str) -> Statistics
        """Updates statistics resource on the server.

        Args
        ----
        - ForceLegacyPortNameInStats (bool): When false, IxNetwork statistics show port name in <Chassis/Front Panel Port Number> format. When true, it is in <Chassis/Card/Port> format
        - GraphHistoryClockTime (number): Tells us amount of time for which data is to be shown (in mint). Min:1, Max:30
        - PersistenceMode (str(mixed | none | persistInBothLocations | persistInConfiguration | persistInUserSettings | preferencesNotSet)): Set the Persistence Mode: whether to store the data in user location or configuration or both/none
        - SnapshotCSVMode (str(appendCSVFile | newCSVFile | overwriteCSVFile)): Set the CSV Generation Mode
        - SnapshotCSVPath (str): Set the Snapshot CSV Path

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ForceLegacyPortNameInStats=None,
        GraphHistoryClockTime=None,
        PersistenceMode=None,
        SnapshotCSVMode=None,
        SnapshotCSVPath=None,
    ):
        # type: (bool, int, str, str, str) -> Statistics
        """Finds and retrieves statistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve statistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all statistics resources from the server.

        Args
        ----
        - ForceLegacyPortNameInStats (bool): When false, IxNetwork statistics show port name in <Chassis/Front Panel Port Number> format. When true, it is in <Chassis/Card/Port> format
        - GraphHistoryClockTime (number): Tells us amount of time for which data is to be shown (in mint). Min:1, Max:30
        - PersistenceMode (str(mixed | none | persistInBothLocations | persistInConfiguration | persistInUserSettings | preferencesNotSet)): Set the Persistence Mode: whether to store the data in user location or configuration or both/none
        - SnapshotCSVMode (str(appendCSVFile | newCSVFile | overwriteCSVFile)): Set the CSV Generation Mode
        - SnapshotCSVPath (str): Set the Snapshot CSV Path

        Returns
        -------
        - self: This instance with matching statistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of statistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the statistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
