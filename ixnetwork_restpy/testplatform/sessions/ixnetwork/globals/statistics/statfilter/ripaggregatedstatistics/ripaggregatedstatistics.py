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


class RipAggregatedStatistics(Base):
    """Represents stats of RIP Aggregated Statistics
    The RipAggregatedStatistics class encapsulates a required ripAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ripAggregatedStatistics"
    _SDM_ATT_MAP = {
        "PortName": "portName",
        "RegularUpdatePacketTx": "regularUpdatePacketTx",
        "RequestPacketTx": "requestPacketTx",
        "RoutersConfigured": "routersConfigured",
        "RoutesAdvertisedTx": "routesAdvertisedTx",
        "RoutesWithdrawsTx": "routesWithdrawsTx",
        "TriggeredUpdatePacketTx": "triggeredUpdatePacketTx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(RipAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def PortName(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Name
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortName"])

    @PortName.setter
    def PortName(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortName"], value)

    @property
    def RegularUpdatePacketTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Regular Update Packet Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RegularUpdatePacketTx"])

    @RegularUpdatePacketTx.setter
    def RegularUpdatePacketTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RegularUpdatePacketTx"], value)

    @property
    def RequestPacketTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Request Packet Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RequestPacketTx"])

    @RequestPacketTx.setter
    def RequestPacketTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RequestPacketTx"], value)

    @property
    def RoutersConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routers Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutersConfigured"])

    @RoutersConfigured.setter
    def RoutersConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutersConfigured"], value)

    @property
    def RoutesAdvertisedTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routes Advertised Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutesAdvertisedTx"])

    @RoutesAdvertisedTx.setter
    def RoutesAdvertisedTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutesAdvertisedTx"], value)

    @property
    def RoutesWithdrawsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routes Withdraws Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutesWithdrawsTx"])

    @RoutesWithdrawsTx.setter
    def RoutesWithdrawsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutesWithdrawsTx"], value)

    @property
    def TriggeredUpdatePacketTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Triggered Update Packet Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TriggeredUpdatePacketTx"])

    @TriggeredUpdatePacketTx.setter
    def TriggeredUpdatePacketTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TriggeredUpdatePacketTx"], value)

    def update(
        self,
        PortName=None,
        RegularUpdatePacketTx=None,
        RequestPacketTx=None,
        RoutersConfigured=None,
        RoutesAdvertisedTx=None,
        RoutesWithdrawsTx=None,
        TriggeredUpdatePacketTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool) -> RipAggregatedStatistics
        """Updates ripAggregatedStatistics resource on the server.

        Args
        ----
        - PortName (bool): Port Name
        - RegularUpdatePacketTx (bool): Regular Update Packet Tx
        - RequestPacketTx (bool): Request Packet Tx
        - RoutersConfigured (bool): Routers Configured
        - RoutesAdvertisedTx (bool): Routes Advertised Tx
        - RoutesWithdrawsTx (bool): Routes Withdraws Tx
        - TriggeredUpdatePacketTx (bool): Triggered Update Packet Tx

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        PortName=None,
        RegularUpdatePacketTx=None,
        RequestPacketTx=None,
        RoutersConfigured=None,
        RoutesAdvertisedTx=None,
        RoutesWithdrawsTx=None,
        TriggeredUpdatePacketTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool) -> RipAggregatedStatistics
        """Finds and retrieves ripAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ripAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ripAggregatedStatistics resources from the server.

        Args
        ----
        - PortName (bool): Port Name
        - RegularUpdatePacketTx (bool): Regular Update Packet Tx
        - RequestPacketTx (bool): Request Packet Tx
        - RoutersConfigured (bool): Routers Configured
        - RoutesAdvertisedTx (bool): Routes Advertised Tx
        - RoutesWithdrawsTx (bool): Routes Withdraws Tx
        - TriggeredUpdatePacketTx (bool): Triggered Update Packet Tx

        Returns
        -------
        - self: This instance with matching ripAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ripAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ripAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
