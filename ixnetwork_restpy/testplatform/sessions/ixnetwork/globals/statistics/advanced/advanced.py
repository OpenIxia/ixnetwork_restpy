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


class Advanced(Base):
    """This node contains Advanced Settings for StatViewer Options.
    The Advanced class encapsulates a required advanced resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "advanced"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Advanced, self).__init__(parent, list_op)

    @property
    def CsvLoggingSettings(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.csvloggingsettings.csvloggingsettings.CsvLoggingSettings): An instance of the CsvLoggingSettings class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.csvloggingsettings.csvloggingsettings import (
            CsvLoggingSettings,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CsvLoggingSettings", None) is not None:
                return self._properties.get("CsvLoggingSettings")
        return CsvLoggingSettings(self)._select()

    @property
    def CustomGraph(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.customgraph.customgraph.CustomGraph): An instance of the CustomGraph class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.customgraph.customgraph import (
            CustomGraph,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CustomGraph", None) is not None:
                return self._properties.get("CustomGraph")
        return CustomGraph(self)._select()

    @property
    def DataStoreSettings(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.datastoresettings.datastoresettings.DataStoreSettings): An instance of the DataStoreSettings class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.datastoresettings.datastoresettings import (
            DataStoreSettings,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DataStoreSettings", None) is not None:
                return self._properties.get("DataStoreSettings")
        return DataStoreSettings(self)._select()

    @property
    def EgressView(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.egressview.egressview.EgressView): An instance of the EgressView class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.egressview.egressview import (
            EgressView,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EgressView", None) is not None:
                return self._properties.get("EgressView")
        return EgressView(self)._select()

    @property
    def GuardRail(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.guardrail.guardrail.GuardRail): An instance of the GuardRail class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.guardrail.guardrail import (
            GuardRail,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("GuardRail", None) is not None:
                return self._properties.get("GuardRail")
        return GuardRail(self)._select()

    @property
    def PollingSettings(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.pollingsettings.pollingsettings.PollingSettings): An instance of the PollingSettings class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.pollingsettings.pollingsettings import (
            PollingSettings,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PollingSettings", None) is not None:
                return self._properties.get("PollingSettings")
        return PollingSettings(self)._select()

    @property
    def TimeSynchronization(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.timesynchronization.timesynchronization.TimeSynchronization): An instance of the TimeSynchronization class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.timesynchronization.timesynchronization import (
            TimeSynchronization,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TimeSynchronization", None) is not None:
                return self._properties.get("TimeSynchronization")
        return TimeSynchronization(self)._select()

    @property
    def Timestamp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.timestamp.timestamp.Timestamp): An instance of the Timestamp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.advanced.timestamp.timestamp import (
            Timestamp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Timestamp", None) is not None:
                return self._properties.get("Timestamp")
        return Timestamp(self)._select()

    def find(self):
        """Finds and retrieves advanced resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve advanced resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all advanced resources from the server.

        Returns
        -------
        - self: This instance with matching advanced resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of advanced data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the advanced resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
