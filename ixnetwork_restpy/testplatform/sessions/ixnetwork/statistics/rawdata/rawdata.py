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


class RawData(Base):
    """Raw data parameters.
    The RawData class encapsulates a required rawData resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "rawData"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "LastRawDataFolder": "lastRawDataFolder",
        "Path": "path",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(RawData, self).__init__(parent, list_op)

    @property
    def Statistic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.statistic.statistic.Statistic): An instance of the Statistic class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.statistic.statistic import (
            Statistic,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Statistic", None) is not None:
                return self._properties.get("Statistic")
        return Statistic(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable/disable Raw Data Collection.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def LastRawDataFolder(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Last save location.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastRawDataFolder"])

    @property
    def Path(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Path to Save Raw Data.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Path"])

    @Path.setter
    def Path(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Path"], value)

    def update(self, Enabled=None, Path=None):
        # type: (bool, str) -> RawData
        """Updates rawData resource on the server.

        Args
        ----
        - Enabled (bool): Enable/disable Raw Data Collection.
        - Path (str): Path to Save Raw Data.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Enabled=None, LastRawDataFolder=None, Path=None):
        # type: (bool, str, str) -> RawData
        """Finds and retrieves rawData resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rawData resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rawData resources from the server.

        Args
        ----
        - Enabled (bool): Enable/disable Raw Data Collection.
        - LastRawDataFolder (str): Last save location.
        - Path (str): Path to Save Raw Data.

        Returns
        -------
        - self: This instance with matching rawData resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rawData data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rawData resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def StopCollection(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopCollection operation on the server.

        NOT DEFINED

        stopCollection(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stopCollection", payload=payload, response_object=None)
