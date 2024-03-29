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


class EntryTe(Base):
    """This object describes the TE parameters associated with the entry point node in an ISIS grid.
    The EntryTe class encapsulates a required entryTe resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "entryTe"
    _SDM_ATT_MAP = {
        "EnableEntryTe": "enableEntryTe",
        "EteAdmGroup": "eteAdmGroup",
        "EteLinkMetric": "eteLinkMetric",
        "EteMaxBandWidth": "eteMaxBandWidth",
        "EteMaxReserveBandWidth": "eteMaxReserveBandWidth",
        "EteRouterId": "eteRouterId",
        "EteRouterIdIncrement": "eteRouterIdIncrement",
        "EteUnreservedBandWidth": "eteUnreservedBandWidth",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(EntryTe, self).__init__(parent, list_op)

    @property
    def EnableEntryTe(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the Entry TE configuration values specified in the ISIS Advanced Router Settings TE dialog may be overridden, and replaced by the values specified in this dialog.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableEntryTe"])

    @EnableEntryTe.setter
    def EnableEntryTe(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableEntryTe"], value)

    @property
    def EteAdmGroup(self):
        # type: () -> str
        """
        Returns
        -------
        - str: For setting the administrative group sub-TLV (sub-TLV 3). It is a 4-octet user-defined bit mask used to assign administrative group numbers to the interface., for use in assigning colors and resource classes. Each set bit corresponds to a single administrative group for this interface. The settings translate into group numbers which range from 0 to 31 (integers).The default value is 00 00 00 00 (hex)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EteAdmGroup"])

    @EteAdmGroup.setter
    def EteAdmGroup(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EteAdmGroup"], value)

    @property
    def EteLinkMetric(self):
        # type: () -> int
        """
        Returns
        -------
        - number: A user-defined metric for the link.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EteLinkMetric"])

    @EteLinkMetric.setter
    def EteLinkMetric(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EteLinkMetric"], value)

    @property
    def EteMaxBandWidth(self):
        # type: () -> str
        """
        Returns
        -------
        - str: For setting the Maximum link bandwidth (sub-TLV 9) allowed for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.00.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EteMaxBandWidth"])

    @EteMaxBandWidth.setter
    def EteMaxBandWidth(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EteMaxBandWidth"], value)

    @property
    def EteMaxReserveBandWidth(self):
        # type: () -> str
        """
        Returns
        -------
        - str: For setting the Maximum reservable link bandwidth sub-TLV 10). It is the maximum bandwidth that can be reserved for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.00.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EteMaxReserveBandWidth"])

    @EteMaxReserveBandWidth.setter
    def EteMaxReserveBandWidth(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EteMaxReserveBandWidth"], value)

    @property
    def EteRouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This attribute is the TE router ID of the first router in the grid (at row = 0, column = 0), in IPv4 format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EteRouterId"])

    @EteRouterId.setter
    def EteRouterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EteRouterId"], value)

    @property
    def EteRouterIdIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The increment step to be used for creating the router IDs for the emulated ISIS routers in this network range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EteRouterIdIncrement"])

    @EteRouterIdIncrement.setter
    def EteRouterIdIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EteRouterIdIncrement"], value)

    @property
    def EteUnreservedBandWidth(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): There are eight levels, one for each possible priority level (for colors or resource classes). The values specify the amount of bandwidth that can be reserved for each of 8 priority levels (0 through 7). The bandwidth values are 32-bit IEEE floating point values, in bytes/sec.The default is 0.00. The total bandwidth for all 8 priority levels may exceed the bandwidth of the link, in cases where the user wants to oversubscribe the link.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EteUnreservedBandWidth"])

    @EteUnreservedBandWidth.setter
    def EteUnreservedBandWidth(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["EteUnreservedBandWidth"], value)

    def update(
        self,
        EnableEntryTe=None,
        EteAdmGroup=None,
        EteLinkMetric=None,
        EteMaxBandWidth=None,
        EteMaxReserveBandWidth=None,
        EteRouterId=None,
        EteRouterIdIncrement=None,
        EteUnreservedBandWidth=None,
    ):
        # type: (bool, str, int, str, str, str, str, List[str]) -> EntryTe
        """Updates entryTe resource on the server.

        Args
        ----
        - EnableEntryTe (bool): If enabled, the Entry TE configuration values specified in the ISIS Advanced Router Settings TE dialog may be overridden, and replaced by the values specified in this dialog.
        - EteAdmGroup (str): For setting the administrative group sub-TLV (sub-TLV 3). It is a 4-octet user-defined bit mask used to assign administrative group numbers to the interface., for use in assigning colors and resource classes. Each set bit corresponds to a single administrative group for this interface. The settings translate into group numbers which range from 0 to 31 (integers).The default value is 00 00 00 00 (hex)
        - EteLinkMetric (number): A user-defined metric for the link.
        - EteMaxBandWidth (str): For setting the Maximum link bandwidth (sub-TLV 9) allowed for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.00.
        - EteMaxReserveBandWidth (str): For setting the Maximum reservable link bandwidth sub-TLV 10). It is the maximum bandwidth that can be reserved for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.00.
        - EteRouterId (str): This attribute is the TE router ID of the first router in the grid (at row = 0, column = 0), in IPv4 format.
        - EteRouterIdIncrement (str): The increment step to be used for creating the router IDs for the emulated ISIS routers in this network range.
        - EteUnreservedBandWidth (list(str)): There are eight levels, one for each possible priority level (for colors or resource classes). The values specify the amount of bandwidth that can be reserved for each of 8 priority levels (0 through 7). The bandwidth values are 32-bit IEEE floating point values, in bytes/sec.The default is 0.00. The total bandwidth for all 8 priority levels may exceed the bandwidth of the link, in cases where the user wants to oversubscribe the link.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnableEntryTe=None,
        EteAdmGroup=None,
        EteLinkMetric=None,
        EteMaxBandWidth=None,
        EteMaxReserveBandWidth=None,
        EteRouterId=None,
        EteRouterIdIncrement=None,
        EteUnreservedBandWidth=None,
    ):
        # type: (bool, str, int, str, str, str, str, List[str]) -> EntryTe
        """Finds and retrieves entryTe resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve entryTe resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all entryTe resources from the server.

        Args
        ----
        - EnableEntryTe (bool): If enabled, the Entry TE configuration values specified in the ISIS Advanced Router Settings TE dialog may be overridden, and replaced by the values specified in this dialog.
        - EteAdmGroup (str): For setting the administrative group sub-TLV (sub-TLV 3). It is a 4-octet user-defined bit mask used to assign administrative group numbers to the interface., for use in assigning colors and resource classes. Each set bit corresponds to a single administrative group for this interface. The settings translate into group numbers which range from 0 to 31 (integers).The default value is 00 00 00 00 (hex)
        - EteLinkMetric (number): A user-defined metric for the link.
        - EteMaxBandWidth (str): For setting the Maximum link bandwidth (sub-TLV 9) allowed for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.00.
        - EteMaxReserveBandWidth (str): For setting the Maximum reservable link bandwidth sub-TLV 10). It is the maximum bandwidth that can be reserved for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.00.
        - EteRouterId (str): This attribute is the TE router ID of the first router in the grid (at row = 0, column = 0), in IPv4 format.
        - EteRouterIdIncrement (str): The increment step to be used for creating the router IDs for the emulated ISIS routers in this network range.
        - EteUnreservedBandWidth (list(str)): There are eight levels, one for each possible priority level (for colors or resource classes). The values specify the amount of bandwidth that can be reserved for each of 8 priority levels (0 through 7). The bandwidth values are 32-bit IEEE floating point values, in bytes/sec.The default is 0.00. The total bandwidth for all 8 priority levels may exceed the bandwidth of the link, in cases where the user wants to oversubscribe the link.

        Returns
        -------
        - self: This instance with matching entryTe resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of entryTe data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the entryTe resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
