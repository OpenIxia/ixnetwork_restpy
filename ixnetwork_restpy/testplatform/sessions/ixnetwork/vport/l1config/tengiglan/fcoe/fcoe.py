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


class Fcoe(Base):
    """This object contains the Layer 1 (physical) parameters for a fcoe port.
    The Fcoe class encapsulates a required fcoe resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "fcoe"
    _SDM_ATT_MAP = {
        "EnablePFCPauseDelay": "enablePFCPauseDelay",
        "FlowControlType": "flowControlType",
        "PfcPauseDelay": "pfcPauseDelay",
        "PfcPriorityGroups": "pfcPriorityGroups",
        "PfcQueueGroupSize": "pfcQueueGroupSize",
        "PfcQueueGroups": "pfcQueueGroups",
        "PriorityGroupSize": "priorityGroupSize",
        "SupportDataCenterMode": "supportDataCenterMode",
    }
    _SDM_ENUM_MAP = {
        "flowControlType": ["ieee802.1Qbb", "ieee802.3x"],
        "pfcQueueGroupSize": [
            "pfcQueueGroupSize-1",
            "pfcQueueGroupSize-4",
            "pfcQueueGroupSize-8",
        ],
        "priorityGroupSize": [
            "priorityGroupSize-1",
            "priorityGroupSize-4",
            "priorityGroupSize-8",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Fcoe, self).__init__(parent, list_op)

    @property
    def EnablePFCPauseDelay(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, PFC pause delay is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePFCPauseDelay"])

    @EnablePFCPauseDelay.setter
    def EnablePFCPauseDelay(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePFCPauseDelay"], value)

    @property
    def FlowControlType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ieee802.1Qbb | ieee802.3x): The type of flow control to be selected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowControlType"])

    @FlowControlType.setter
    def FlowControlType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowControlType"], value)

    @property
    def PfcPauseDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If selected, enables to increase the number of frames that is sent when a pause frame is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPauseDelay"])

    @PfcPauseDelay.setter
    def PfcPauseDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPauseDelay"], value)

    @property
    def PfcPriorityGroups(self):
        # type: () -> List[str]
        """DEPRECATED
        Returns
        -------
        - list(str): When you select 802.1Qbb as the flowControlType, you can use the PFC/Priority settings to map each of the eight PFC priorities to one of the two/four/eight Priority Groups (or to None). The PFCs are numbered 0-7.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriorityGroups"])

    @PfcPriorityGroups.setter
    def PfcPriorityGroups(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriorityGroups"], value)

    @property
    def PfcQueueGroupSize(self):
        # type: () -> str
        """
        Returns
        -------
        - str(pfcQueueGroupSize-1 | pfcQueueGroupSize-4 | pfcQueueGroupSize-8): Max PFC queue group size
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcQueueGroupSize"])

    @PfcQueueGroupSize.setter
    def PfcQueueGroupSize(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcQueueGroupSize"], value)

    @property
    def PfcQueueGroups(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): When you select 802.1Qbb as the flowControlType, you can use the Priority/PFC Queue settings to map each of the eight PFC priorities to one of the two/four/eight PFC Queue Groups (or to None).
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcQueueGroups"])

    @PfcQueueGroups.setter
    def PfcQueueGroups(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcQueueGroups"], value)

    @property
    def PriorityGroupSize(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(priorityGroupSize-1 | priorityGroupSize-4 | priorityGroupSize-8): The maximum size of a Priority Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PriorityGroupSize"])

    @PriorityGroupSize.setter
    def PriorityGroupSize(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PriorityGroupSize"], value)

    @property
    def SupportDataCenterMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, this mode automatically sets Transmit Mode to Interleaved Streams.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupportDataCenterMode"])

    @SupportDataCenterMode.setter
    def SupportDataCenterMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupportDataCenterMode"], value)

    def update(
        self,
        EnablePFCPauseDelay=None,
        FlowControlType=None,
        PfcPauseDelay=None,
        PfcPriorityGroups=None,
        PfcQueueGroupSize=None,
        PfcQueueGroups=None,
        PriorityGroupSize=None,
        SupportDataCenterMode=None,
    ):
        # type: (bool, str, int, List[str], str, List[str], str, bool) -> Fcoe
        """Updates fcoe resource on the server.

        Args
        ----
        - EnablePFCPauseDelay (bool): If true, PFC pause delay is enabled.
        - FlowControlType (str(ieee802.1Qbb | ieee802.3x)): The type of flow control to be selected.
        - PfcPauseDelay (number): If selected, enables to increase the number of frames that is sent when a pause frame is received.
        - PfcPriorityGroups (list(str)): When you select 802.1Qbb as the flowControlType, you can use the PFC/Priority settings to map each of the eight PFC priorities to one of the two/four/eight Priority Groups (or to None). The PFCs are numbered 0-7.
        - PfcQueueGroupSize (str(pfcQueueGroupSize-1 | pfcQueueGroupSize-4 | pfcQueueGroupSize-8)): Max PFC queue group size
        - PfcQueueGroups (list(str)): When you select 802.1Qbb as the flowControlType, you can use the Priority/PFC Queue settings to map each of the eight PFC priorities to one of the two/four/eight PFC Queue Groups (or to None).
        - PriorityGroupSize (str(priorityGroupSize-1 | priorityGroupSize-4 | priorityGroupSize-8)): The maximum size of a Priority Group.
        - SupportDataCenterMode (bool): If true, this mode automatically sets Transmit Mode to Interleaved Streams.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnablePFCPauseDelay=None,
        FlowControlType=None,
        PfcPauseDelay=None,
        PfcPriorityGroups=None,
        PfcQueueGroupSize=None,
        PfcQueueGroups=None,
        PriorityGroupSize=None,
        SupportDataCenterMode=None,
    ):
        # type: (bool, str, int, List[str], str, List[str], str, bool) -> Fcoe
        """Finds and retrieves fcoe resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcoe resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcoe resources from the server.

        Args
        ----
        - EnablePFCPauseDelay (bool): If true, PFC pause delay is enabled.
        - FlowControlType (str(ieee802.1Qbb | ieee802.3x)): The type of flow control to be selected.
        - PfcPauseDelay (number): If selected, enables to increase the number of frames that is sent when a pause frame is received.
        - PfcPriorityGroups (list(str)): When you select 802.1Qbb as the flowControlType, you can use the PFC/Priority settings to map each of the eight PFC priorities to one of the two/four/eight Priority Groups (or to None). The PFCs are numbered 0-7.
        - PfcQueueGroupSize (str(pfcQueueGroupSize-1 | pfcQueueGroupSize-4 | pfcQueueGroupSize-8)): Max PFC queue group size
        - PfcQueueGroups (list(str)): When you select 802.1Qbb as the flowControlType, you can use the Priority/PFC Queue settings to map each of the eight PFC priorities to one of the two/four/eight PFC Queue Groups (or to None).
        - PriorityGroupSize (str(priorityGroupSize-1 | priorityGroupSize-4 | priorityGroupSize-8)): The maximum size of a Priority Group.
        - SupportDataCenterMode (bool): If true, this mode automatically sets Transmit Mode to Interleaved Streams.

        Returns
        -------
        - self: This instance with matching fcoe resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcoe data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcoe resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
