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


class RangeTe(Base):
    """Controls the configuration of Range TE for this network range.
    The RangeTe class encapsulates a required rangeTe resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "rangeTe"
    _SDM_ATT_MAP = {
        "EnableRangeTe": "enableRangeTe",
        "TeAdmGroup": "teAdmGroup",
        "TeLinkMetric": "teLinkMetric",
        "TeMaxBandWidth": "teMaxBandWidth",
        "TeMaxReserveBandWidth": "teMaxReserveBandWidth",
        "TeRouterId": "teRouterId",
        "TeRouterIdIncrement": "teRouterIdIncrement",
        "TeUnreservedBandWidth": "teUnreservedBandWidth",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(RangeTe, self).__init__(parent, list_op)

    @property
    def EnableRangeTe(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the generation of Traffic Engineering data. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableRangeTe"])

    @EnableRangeTe.setter
    def EnableRangeTe(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableRangeTe"], value)

    @property
    def TeAdmGroup(self):
        # type: () -> str
        """
        Returns
        -------
        - str: For setting the Administrative group sub-TLV (sub-TLV 3). It is a 4-octet user-defined bit mask used to assign administrative group numbers to the interface., for use in assigning colors and resource classes. Each set bit corresponds to a single administrative group for this interface. The settings translate into Group numbers which range from 0 to 31 (integers).
        """
        return self._get_attribute(self._SDM_ATT_MAP["TeAdmGroup"])

    @TeAdmGroup.setter
    def TeAdmGroup(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TeAdmGroup"], value)

    @property
    def TeLinkMetric(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The metric associated with the interface that the TE data is advertised on.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TeLinkMetric"])

    @TeLinkMetric.setter
    def TeLinkMetric(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TeLinkMetric"], value)

    @property
    def TeMaxBandWidth(self):
        # type: () -> str
        """
        Returns
        -------
        - str: For setting the maximum link bandwidth (sub-TLV 9) allowed for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.00.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TeMaxBandWidth"])

    @TeMaxBandWidth.setter
    def TeMaxBandWidth(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TeMaxBandWidth"], value)

    @property
    def TeMaxReserveBandWidth(self):
        # type: () -> str
        """
        Returns
        -------
        - str: For setting the Maximum reservable link bandwidth sub-TLV 10). It is the maximum bandwidth that can be reserved for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.00.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TeMaxReserveBandWidth"])

    @TeMaxReserveBandWidth.setter
    def TeMaxReserveBandWidth(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TeMaxReserveBandWidth"], value)

    @property
    def TeRouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The 32-bit TE router ID assigned to the first emulated ISIS router in this network range used with the increment TE router ID value when more than one router is to be created.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TeRouterId"])

    @TeRouterId.setter
    def TeRouterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TeRouterId"], value)

    @property
    def TeRouterIdIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The 32-bit increment value that will be added to the previous TE Router ID, for automatically creating additional TE Router IDs for the emulated routers in this network range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TeRouterIdIncrement"])

    @TeRouterIdIncrement.setter
    def TeRouterIdIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TeRouterIdIncrement"], value)

    @property
    def TeUnreservedBandWidth(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The traffic engineering unreserved bandwidth for each priority to be advertised. There are eight distinct options. (default = 0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["TeUnreservedBandWidth"])

    @TeUnreservedBandWidth.setter
    def TeUnreservedBandWidth(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["TeUnreservedBandWidth"], value)

    def update(
        self,
        EnableRangeTe=None,
        TeAdmGroup=None,
        TeLinkMetric=None,
        TeMaxBandWidth=None,
        TeMaxReserveBandWidth=None,
        TeRouterId=None,
        TeRouterIdIncrement=None,
        TeUnreservedBandWidth=None,
    ):
        # type: (bool, str, int, str, str, str, str, List[str]) -> RangeTe
        """Updates rangeTe resource on the server.

        Args
        ----
        - EnableRangeTe (bool): Enables the generation of Traffic Engineering data. (default = false)
        - TeAdmGroup (str): For setting the Administrative group sub-TLV (sub-TLV 3). It is a 4-octet user-defined bit mask used to assign administrative group numbers to the interface., for use in assigning colors and resource classes. Each set bit corresponds to a single administrative group for this interface. The settings translate into Group numbers which range from 0 to 31 (integers).
        - TeLinkMetric (number): The metric associated with the interface that the TE data is advertised on.
        - TeMaxBandWidth (str): For setting the maximum link bandwidth (sub-TLV 9) allowed for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.00.
        - TeMaxReserveBandWidth (str): For setting the Maximum reservable link bandwidth sub-TLV 10). It is the maximum bandwidth that can be reserved for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.00.
        - TeRouterId (str): The 32-bit TE router ID assigned to the first emulated ISIS router in this network range used with the increment TE router ID value when more than one router is to be created.
        - TeRouterIdIncrement (str): The 32-bit increment value that will be added to the previous TE Router ID, for automatically creating additional TE Router IDs for the emulated routers in this network range.
        - TeUnreservedBandWidth (list(str)): The traffic engineering unreserved bandwidth for each priority to be advertised. There are eight distinct options. (default = 0.0)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnableRangeTe=None,
        TeAdmGroup=None,
        TeLinkMetric=None,
        TeMaxBandWidth=None,
        TeMaxReserveBandWidth=None,
        TeRouterId=None,
        TeRouterIdIncrement=None,
        TeUnreservedBandWidth=None,
    ):
        # type: (bool, str, int, str, str, str, str, List[str]) -> RangeTe
        """Finds and retrieves rangeTe resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rangeTe resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rangeTe resources from the server.

        Args
        ----
        - EnableRangeTe (bool): Enables the generation of Traffic Engineering data. (default = false)
        - TeAdmGroup (str): For setting the Administrative group sub-TLV (sub-TLV 3). It is a 4-octet user-defined bit mask used to assign administrative group numbers to the interface., for use in assigning colors and resource classes. Each set bit corresponds to a single administrative group for this interface. The settings translate into Group numbers which range from 0 to 31 (integers).
        - TeLinkMetric (number): The metric associated with the interface that the TE data is advertised on.
        - TeMaxBandWidth (str): For setting the maximum link bandwidth (sub-TLV 9) allowed for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.00.
        - TeMaxReserveBandWidth (str): For setting the Maximum reservable link bandwidth sub-TLV 10). It is the maximum bandwidth that can be reserved for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.00.
        - TeRouterId (str): The 32-bit TE router ID assigned to the first emulated ISIS router in this network range used with the increment TE router ID value when more than one router is to be created.
        - TeRouterIdIncrement (str): The 32-bit increment value that will be added to the previous TE Router ID, for automatically creating additional TE Router IDs for the emulated routers in this network range.
        - TeUnreservedBandWidth (list(str)): The traffic engineering unreserved bandwidth for each priority to be advertised. There are eight distinct options. (default = 0.0)

        Returns
        -------
        - self: This instance with matching rangeTe resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rangeTe data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rangeTe resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
