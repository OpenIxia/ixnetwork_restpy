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
        "CsvLoggingResultsFolder": "csvLoggingResultsFolder",
        "CsvLoggingRootFolder": "csvLoggingRootFolder",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Statistics, self).__init__(parent, list_op)

    @property
    def Advanced(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.advanced.Advanced): An instance of the Advanced class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.advanced import (
            Advanced,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Advanced", None) is not None:
                return self._properties.get("Advanced")
        return Advanced(self)._select()

    @property
    def Datacenter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.datacenter.datacenter.Datacenter): An instance of the Datacenter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.datacenter.datacenter import (
            Datacenter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Datacenter", None) is not None:
                return self._properties.get("Datacenter")
        return Datacenter(self)._select()

    @property
    def ReportGenerator(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.reportgenerator.reportgenerator.ReportGenerator): An instance of the ReportGenerator class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.reportgenerator.reportgenerator import (
            ReportGenerator,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ReportGenerator", None) is not None:
                return self._properties.get("ReportGenerator")
        return ReportGenerator(self)._select()

    @property
    def StatFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.statfilter.StatFilter): An instance of the StatFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.statfilter import (
            StatFilter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StatFilter", None) is not None:
                return self._properties.get("StatFilter")
        return StatFilter(self)._select()

    @property
    def TestInspector(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.testinspector.TestInspector): An instance of the TestInspector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.testinspector import (
            TestInspector,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TestInspector", None) is not None:
                return self._properties.get("TestInspector")
        return TestInspector(self)._select()

    @property
    def CsvLoggingResultsFolder(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Fetch the current result folder
        """
        return self._get_attribute(self._SDM_ATT_MAP["CsvLoggingResultsFolder"])

    @property
    def CsvLoggingRootFolder(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Set the CSV Logging Path (the root folder for test results {csv logging, snapshot}) which is stored in config
        """
        return self._get_attribute(self._SDM_ATT_MAP["CsvLoggingRootFolder"])

    @CsvLoggingRootFolder.setter
    def CsvLoggingRootFolder(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CsvLoggingRootFolder"], value)

    def update(self, CsvLoggingRootFolder=None):
        # type: (str) -> Statistics
        """Updates statistics resource on the server.

        Args
        ----
        - CsvLoggingRootFolder (str): Set the CSV Logging Path (the root folder for test results {csv logging, snapshot}) which is stored in config

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, CsvLoggingResultsFolder=None, CsvLoggingRootFolder=None):
        # type: (str, str) -> Statistics
        """Finds and retrieves statistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve statistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all statistics resources from the server.

        Args
        ----
        - CsvLoggingResultsFolder (str): Fetch the current result folder
        - CsvLoggingRootFolder (str): Set the CSV Logging Path (the root folder for test results {csv logging, snapshot}) which is stored in config

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
