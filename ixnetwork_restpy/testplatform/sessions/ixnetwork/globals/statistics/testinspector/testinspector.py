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


class TestInspector(Base):
    """This node contains Test Inspector Settings.
    The TestInspector class encapsulates a required testInspector resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "testInspector"
    _SDM_ATT_MAP = {
        "EnableRealTimeMonitoring": "enableRealTimeMonitoring",
        "PollingInterval": "pollingInterval",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TestInspector, self).__init__(parent, list_op)

    @property
    def AverageLatency(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.averagelatency.averagelatency.AverageLatency): An instance of the AverageLatency class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.averagelatency.averagelatency import (
            AverageLatency,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AverageLatency", None) is not None:
                return self._properties.get("AverageLatency")
        return AverageLatency(self)._select()

    @property
    def Collisions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.collisions.collisions.Collisions): An instance of the Collisions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.collisions.collisions import (
            Collisions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Collisions", None) is not None:
                return self._properties.get("Collisions")
        return Collisions(self)._select()

    @property
    def CrcErrors(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.crcerrors.crcerrors.CrcErrors): An instance of the CrcErrors class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.crcerrors.crcerrors import (
            CrcErrors,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CrcErrors", None) is not None:
                return self._properties.get("CrcErrors")
        return CrcErrors(self)._select()

    @property
    def LossPercent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.losspercent.losspercent.LossPercent): An instance of the LossPercent class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.losspercent.losspercent import (
            LossPercent,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LossPercent", None) is not None:
                return self._properties.get("LossPercent")
        return LossPercent(self)._select()

    @property
    def LostFrames(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.lostframes.lostframes.LostFrames): An instance of the LostFrames class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.lostframes.lostframes import (
            LostFrames,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LostFrames", None) is not None:
                return self._properties.get("LostFrames")
        return LostFrames(self)._select()

    @property
    def MisdirectedPacketCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.misdirectedpacketcount.misdirectedpacketcount.MisdirectedPacketCount): An instance of the MisdirectedPacketCount class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.misdirectedpacketcount.misdirectedpacketcount import (
            MisdirectedPacketCount,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MisdirectedPacketCount", None) is not None:
                return self._properties.get("MisdirectedPacketCount")
        return MisdirectedPacketCount(self)._select()

    @property
    def PcsSyncErrors(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.pcssyncerrors.pcssyncerrors.PcsSyncErrors): An instance of the PcsSyncErrors class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.pcssyncerrors.pcssyncerrors import (
            PcsSyncErrors,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PcsSyncErrors", None) is not None:
                return self._properties.get("PcsSyncErrors")
        return PcsSyncErrors(self)._select()

    @property
    def SequenceErrors(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.sequenceerrors.sequenceerrors.SequenceErrors): An instance of the SequenceErrors class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.testinspector.sequenceerrors.sequenceerrors import (
            SequenceErrors,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SequenceErrors", None) is not None:
                return self._properties.get("SequenceErrors")
        return SequenceErrors(self)._select()

    @property
    def EnableRealTimeMonitoring(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable/Disable Test Inspector
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableRealTimeMonitoring"])

    @EnableRealTimeMonitoring.setter
    def EnableRealTimeMonitoring(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableRealTimeMonitoring"], value)

    @property
    def PollingInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Test Inspector's polling interval. For best performance set this to a multiple of the Stat Viewer polling interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PollingInterval"])

    @PollingInterval.setter
    def PollingInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PollingInterval"], value)

    def update(self, EnableRealTimeMonitoring=None, PollingInterval=None):
        # type: (bool, int) -> TestInspector
        """Updates testInspector resource on the server.

        Args
        ----
        - EnableRealTimeMonitoring (bool): Enable/Disable Test Inspector
        - PollingInterval (number): Test Inspector's polling interval. For best performance set this to a multiple of the Stat Viewer polling interval.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, EnableRealTimeMonitoring=None, PollingInterval=None):
        # type: (bool, int) -> TestInspector
        """Finds and retrieves testInspector resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testInspector resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testInspector resources from the server.

        Args
        ----
        - EnableRealTimeMonitoring (bool): Enable/Disable Test Inspector
        - PollingInterval (number): Test Inspector's polling interval. For best performance set this to a multiple of the Stat Viewer polling interval.

        Returns
        -------
        - self: This instance with matching testInspector resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of testInspector data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the testInspector resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
