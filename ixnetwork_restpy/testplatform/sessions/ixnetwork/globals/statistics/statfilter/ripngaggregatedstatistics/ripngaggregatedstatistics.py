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


class RipngAggregatedStatistics(Base):
    """Represents stats of RIPng Aggregated Statistics
    The RipngAggregatedStatistics class encapsulates a required ripngAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ripngAggregatedStatistics"
    _SDM_ATT_MAP = {
        "PortName": "portName",
        "RegularUpdatePacketTx": "regularUpdatePacketTx",
        "RequestPacketRx": "requestPacketRx",
        "ResponsePacketRx": "responsePacketRx",
        "ResponsePacketTx": "responsePacketTx",
        "RoutersConfigured": "routersConfigured",
        "RoutersRunning": "routersRunning",
        "RoutesAdvertisedRx": "routesAdvertisedRx",
        "RoutesAdvertisedTx": "routesAdvertisedTx",
        "RoutesPoisonedTx": "routesPoisonedTx",
        "RoutesWithdrawsRx": "routesWithdrawsRx",
        "RoutesWithdrawsTx": "routesWithdrawsTx",
        "TriggeredUpdatePacketTx": "triggeredUpdatePacketTx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(RipngAggregatedStatistics, self).__init__(parent, list_op)

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
    def RequestPacketRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Request Packet Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RequestPacketRx"])

    @RequestPacketRx.setter
    def RequestPacketRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RequestPacketRx"], value)

    @property
    def ResponsePacketRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Response Packet Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResponsePacketRx"])

    @ResponsePacketRx.setter
    def ResponsePacketRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResponsePacketRx"], value)

    @property
    def ResponsePacketTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Response Packet Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResponsePacketTx"])

    @ResponsePacketTx.setter
    def ResponsePacketTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResponsePacketTx"], value)

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
    def RoutersRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routers Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutersRunning"])

    @RoutersRunning.setter
    def RoutersRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutersRunning"], value)

    @property
    def RoutesAdvertisedRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routes Advertised Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutesAdvertisedRx"])

    @RoutesAdvertisedRx.setter
    def RoutesAdvertisedRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutesAdvertisedRx"], value)

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
    def RoutesPoisonedTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routes Poisoned Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutesPoisonedTx"])

    @RoutesPoisonedTx.setter
    def RoutesPoisonedTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutesPoisonedTx"], value)

    @property
    def RoutesWithdrawsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routes Withdraws Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutesWithdrawsRx"])

    @RoutesWithdrawsRx.setter
    def RoutesWithdrawsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutesWithdrawsRx"], value)

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
        RequestPacketRx=None,
        ResponsePacketRx=None,
        ResponsePacketTx=None,
        RoutersConfigured=None,
        RoutersRunning=None,
        RoutesAdvertisedRx=None,
        RoutesAdvertisedTx=None,
        RoutesPoisonedTx=None,
        RoutesWithdrawsRx=None,
        RoutesWithdrawsTx=None,
        TriggeredUpdatePacketTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> RipngAggregatedStatistics
        """Updates ripngAggregatedStatistics resource on the server.

        Args
        ----
        - PortName (bool): Port Name
        - RegularUpdatePacketTx (bool): Regular Update Packet Tx
        - RequestPacketRx (bool): Request Packet Rx
        - ResponsePacketRx (bool): Response Packet Rx
        - ResponsePacketTx (bool): Response Packet Tx
        - RoutersConfigured (bool): Routers Configured
        - RoutersRunning (bool): Routers Running
        - RoutesAdvertisedRx (bool): Routes Advertised Rx
        - RoutesAdvertisedTx (bool): Routes Advertised Tx
        - RoutesPoisonedTx (bool): Routes Poisoned Tx
        - RoutesWithdrawsRx (bool): Routes Withdraws Rx
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
        RequestPacketRx=None,
        ResponsePacketRx=None,
        ResponsePacketTx=None,
        RoutersConfigured=None,
        RoutersRunning=None,
        RoutesAdvertisedRx=None,
        RoutesAdvertisedTx=None,
        RoutesPoisonedTx=None,
        RoutesWithdrawsRx=None,
        RoutesWithdrawsTx=None,
        TriggeredUpdatePacketTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> RipngAggregatedStatistics
        """Finds and retrieves ripngAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ripngAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ripngAggregatedStatistics resources from the server.

        Args
        ----
        - PortName (bool): Port Name
        - RegularUpdatePacketTx (bool): Regular Update Packet Tx
        - RequestPacketRx (bool): Request Packet Rx
        - ResponsePacketRx (bool): Response Packet Rx
        - ResponsePacketTx (bool): Response Packet Tx
        - RoutersConfigured (bool): Routers Configured
        - RoutersRunning (bool): Routers Running
        - RoutesAdvertisedRx (bool): Routes Advertised Rx
        - RoutesAdvertisedTx (bool): Routes Advertised Tx
        - RoutesPoisonedTx (bool): Routes Poisoned Tx
        - RoutesWithdrawsRx (bool): Routes Withdraws Rx
        - RoutesWithdrawsTx (bool): Routes Withdraws Tx
        - TriggeredUpdatePacketTx (bool): Triggered Update Packet Tx

        Returns
        -------
        - self: This instance with matching ripngAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ripngAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ripngAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
