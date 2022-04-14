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


class EigrpAggregatedStatistics(Base):
    """Represents stats of EIGRP Aggregated Statistics
    The EigrpAggregatedStatistics class encapsulates a required eigrpAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "eigrpAggregatedStatistics"
    _SDM_ATT_MAP = {
        "AcksRx": "acksRx",
        "AcksTx": "acksTx",
        "HellosRx": "hellosRx",
        "HellosTx": "hellosTx",
        "Ipv4NeighborsDeleted": "ipv4NeighborsDeleted",
        "Ipv4NeighborsLearned": "ipv4NeighborsLearned",
        "Ipv4RouteWithdrawsRx": "ipv4RouteWithdrawsRx",
        "Ipv4RoutersConfigured": "ipv4RoutersConfigured",
        "Ipv4RoutersRunning": "ipv4RoutersRunning",
        "Ipv4RoutesLearned": "ipv4RoutesLearned",
        "Ipv4RoutesRx": "ipv4RoutesRx",
        "Ipv4RoutesTx": "ipv4RoutesTx",
        "Ipv4RoutesWithdrawn": "ipv4RoutesWithdrawn",
        "Ipv6NeighborsDeleted": "ipv6NeighborsDeleted",
        "Ipv6NeighborsLearned": "ipv6NeighborsLearned",
        "Ipv6RouteWithdrawsRx": "ipv6RouteWithdrawsRx",
        "Ipv6RoutersConfigured": "ipv6RoutersConfigured",
        "Ipv6RoutersRunning": "ipv6RoutersRunning",
        "Ipv6RoutesLearned": "ipv6RoutesLearned",
        "Ipv6RoutesRx": "ipv6RoutesRx",
        "Ipv6RoutesTx": "ipv6RoutesTx",
        "Ipv6RoutesWithdrawn": "ipv6RoutesWithdrawn",
        "PacketsRx": "packetsRx",
        "PacketsTx": "packetsTx",
        "PortName": "portName",
        "QueriesRx": "queriesRx",
        "QueriesTx": "queriesTx",
        "RepliesRx": "repliesRx",
        "RepliesTx": "repliesTx",
        "RetransmissionCount": "retransmissionCount",
        "UpdatesRx": "updatesRx",
        "UpdatesTx": "updatesTx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(EigrpAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def AcksRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ACKs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["AcksRx"])

    @AcksRx.setter
    def AcksRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AcksRx"], value)

    @property
    def AcksTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ACKs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["AcksTx"])

    @AcksTx.setter
    def AcksTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AcksTx"], value)

    @property
    def HellosRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Hellos Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HellosRx"])

    @HellosRx.setter
    def HellosRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HellosRx"], value)

    @property
    def HellosTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Hellos Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HellosTx"])

    @HellosTx.setter
    def HellosTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HellosTx"], value)

    @property
    def Ipv4NeighborsDeleted(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Neighbors Deleted
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4NeighborsDeleted"])

    @Ipv4NeighborsDeleted.setter
    def Ipv4NeighborsDeleted(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4NeighborsDeleted"], value)

    @property
    def Ipv4NeighborsLearned(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Neighbors Learned
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4NeighborsLearned"])

    @Ipv4NeighborsLearned.setter
    def Ipv4NeighborsLearned(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4NeighborsLearned"], value)

    @property
    def Ipv4RouteWithdrawsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Route Withdraws Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4RouteWithdrawsRx"])

    @Ipv4RouteWithdrawsRx.setter
    def Ipv4RouteWithdrawsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4RouteWithdrawsRx"], value)

    @property
    def Ipv4RoutersConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Routers Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4RoutersConfigured"])

    @Ipv4RoutersConfigured.setter
    def Ipv4RoutersConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4RoutersConfigured"], value)

    @property
    def Ipv4RoutersRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Routers Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4RoutersRunning"])

    @Ipv4RoutersRunning.setter
    def Ipv4RoutersRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4RoutersRunning"], value)

    @property
    def Ipv4RoutesLearned(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Routes Learned
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4RoutesLearned"])

    @Ipv4RoutesLearned.setter
    def Ipv4RoutesLearned(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4RoutesLearned"], value)

    @property
    def Ipv4RoutesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Routes Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4RoutesRx"])

    @Ipv4RoutesRx.setter
    def Ipv4RoutesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4RoutesRx"], value)

    @property
    def Ipv4RoutesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Routes Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4RoutesTx"])

    @Ipv4RoutesTx.setter
    def Ipv4RoutesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4RoutesTx"], value)

    @property
    def Ipv4RoutesWithdrawn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Routes Withdrawn
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4RoutesWithdrawn"])

    @Ipv4RoutesWithdrawn.setter
    def Ipv4RoutesWithdrawn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4RoutesWithdrawn"], value)

    @property
    def Ipv6NeighborsDeleted(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 Neighbors Deleted
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NeighborsDeleted"])

    @Ipv6NeighborsDeleted.setter
    def Ipv6NeighborsDeleted(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6NeighborsDeleted"], value)

    @property
    def Ipv6NeighborsLearned(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 Neighbors Learned
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6NeighborsLearned"])

    @Ipv6NeighborsLearned.setter
    def Ipv6NeighborsLearned(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6NeighborsLearned"], value)

    @property
    def Ipv6RouteWithdrawsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 Route Withdraws Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6RouteWithdrawsRx"])

    @Ipv6RouteWithdrawsRx.setter
    def Ipv6RouteWithdrawsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6RouteWithdrawsRx"], value)

    @property
    def Ipv6RoutersConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 Routers Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6RoutersConfigured"])

    @Ipv6RoutersConfigured.setter
    def Ipv6RoutersConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6RoutersConfigured"], value)

    @property
    def Ipv6RoutersRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 Routers Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6RoutersRunning"])

    @Ipv6RoutersRunning.setter
    def Ipv6RoutersRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6RoutersRunning"], value)

    @property
    def Ipv6RoutesLearned(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 Routes Learned
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6RoutesLearned"])

    @Ipv6RoutesLearned.setter
    def Ipv6RoutesLearned(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6RoutesLearned"], value)

    @property
    def Ipv6RoutesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 Routes Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6RoutesRx"])

    @Ipv6RoutesRx.setter
    def Ipv6RoutesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6RoutesRx"], value)

    @property
    def Ipv6RoutesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 Routes Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6RoutesTx"])

    @Ipv6RoutesTx.setter
    def Ipv6RoutesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6RoutesTx"], value)

    @property
    def Ipv6RoutesWithdrawn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 Routes Withdrawn
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6RoutesWithdrawn"])

    @Ipv6RoutesWithdrawn.setter
    def Ipv6RoutesWithdrawn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6RoutesWithdrawn"], value)

    @property
    def PacketsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Packets Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketsRx"])

    @PacketsRx.setter
    def PacketsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketsRx"], value)

    @property
    def PacketsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Packets Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketsTx"])

    @PacketsTx.setter
    def PacketsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketsTx"], value)

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
    def QueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueriesRx"])

    @QueriesRx.setter
    def QueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueriesRx"], value)

    @property
    def QueriesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Queries Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueriesTx"])

    @QueriesTx.setter
    def QueriesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueriesTx"], value)

    @property
    def RepliesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Replies Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RepliesRx"])

    @RepliesRx.setter
    def RepliesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RepliesRx"], value)

    @property
    def RepliesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Replies Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RepliesTx"])

    @RepliesTx.setter
    def RepliesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RepliesTx"], value)

    @property
    def RetransmissionCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Retransmission Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RetransmissionCount"])

    @RetransmissionCount.setter
    def RetransmissionCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RetransmissionCount"], value)

    @property
    def UpdatesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Updates Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpdatesRx"])

    @UpdatesRx.setter
    def UpdatesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpdatesRx"], value)

    @property
    def UpdatesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Updates Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpdatesTx"])

    @UpdatesTx.setter
    def UpdatesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpdatesTx"], value)

    def update(
        self,
        AcksRx=None,
        AcksTx=None,
        HellosRx=None,
        HellosTx=None,
        Ipv4NeighborsDeleted=None,
        Ipv4NeighborsLearned=None,
        Ipv4RouteWithdrawsRx=None,
        Ipv4RoutersConfigured=None,
        Ipv4RoutersRunning=None,
        Ipv4RoutesLearned=None,
        Ipv4RoutesRx=None,
        Ipv4RoutesTx=None,
        Ipv4RoutesWithdrawn=None,
        Ipv6NeighborsDeleted=None,
        Ipv6NeighborsLearned=None,
        Ipv6RouteWithdrawsRx=None,
        Ipv6RoutersConfigured=None,
        Ipv6RoutersRunning=None,
        Ipv6RoutesLearned=None,
        Ipv6RoutesRx=None,
        Ipv6RoutesTx=None,
        Ipv6RoutesWithdrawn=None,
        PacketsRx=None,
        PacketsTx=None,
        PortName=None,
        QueriesRx=None,
        QueriesTx=None,
        RepliesRx=None,
        RepliesTx=None,
        RetransmissionCount=None,
        UpdatesRx=None,
        UpdatesTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> EigrpAggregatedStatistics
        """Updates eigrpAggregatedStatistics resource on the server.

        Args
        ----
        - AcksRx (bool): ACKs Rx
        - AcksTx (bool): ACKs Tx
        - HellosRx (bool): Hellos Rx
        - HellosTx (bool): Hellos Tx
        - Ipv4NeighborsDeleted (bool): IPv4 Neighbors Deleted
        - Ipv4NeighborsLearned (bool): IPv4 Neighbors Learned
        - Ipv4RouteWithdrawsRx (bool): IPv4 Route Withdraws Rx
        - Ipv4RoutersConfigured (bool): IPv4 Routers Configured
        - Ipv4RoutersRunning (bool): IPv4 Routers Running
        - Ipv4RoutesLearned (bool): IPv4 Routes Learned
        - Ipv4RoutesRx (bool): IPv4 Routes Rx
        - Ipv4RoutesTx (bool): IPv4 Routes Tx
        - Ipv4RoutesWithdrawn (bool): IPv4 Routes Withdrawn
        - Ipv6NeighborsDeleted (bool): IPv6 Neighbors Deleted
        - Ipv6NeighborsLearned (bool): IPv6 Neighbors Learned
        - Ipv6RouteWithdrawsRx (bool): IPv6 Route Withdraws Rx
        - Ipv6RoutersConfigured (bool): IPv6 Routers Configured
        - Ipv6RoutersRunning (bool): IPv6 Routers Running
        - Ipv6RoutesLearned (bool): IPv6 Routes Learned
        - Ipv6RoutesRx (bool): IPv6 Routes Rx
        - Ipv6RoutesTx (bool): IPv6 Routes Tx
        - Ipv6RoutesWithdrawn (bool): IPv6 Routes Withdrawn
        - PacketsRx (bool): Packets Rx
        - PacketsTx (bool): Packets Tx
        - PortName (bool): Port Name
        - QueriesRx (bool): Queries Rx
        - QueriesTx (bool): Queries Tx
        - RepliesRx (bool): Replies Rx
        - RepliesTx (bool): Replies Tx
        - RetransmissionCount (bool): Retransmission Count
        - UpdatesRx (bool): Updates Rx
        - UpdatesTx (bool): Updates Tx

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AcksRx=None,
        AcksTx=None,
        HellosRx=None,
        HellosTx=None,
        Ipv4NeighborsDeleted=None,
        Ipv4NeighborsLearned=None,
        Ipv4RouteWithdrawsRx=None,
        Ipv4RoutersConfigured=None,
        Ipv4RoutersRunning=None,
        Ipv4RoutesLearned=None,
        Ipv4RoutesRx=None,
        Ipv4RoutesTx=None,
        Ipv4RoutesWithdrawn=None,
        Ipv6NeighborsDeleted=None,
        Ipv6NeighborsLearned=None,
        Ipv6RouteWithdrawsRx=None,
        Ipv6RoutersConfigured=None,
        Ipv6RoutersRunning=None,
        Ipv6RoutesLearned=None,
        Ipv6RoutesRx=None,
        Ipv6RoutesTx=None,
        Ipv6RoutesWithdrawn=None,
        PacketsRx=None,
        PacketsTx=None,
        PortName=None,
        QueriesRx=None,
        QueriesTx=None,
        RepliesRx=None,
        RepliesTx=None,
        RetransmissionCount=None,
        UpdatesRx=None,
        UpdatesTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> EigrpAggregatedStatistics
        """Finds and retrieves eigrpAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve eigrpAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all eigrpAggregatedStatistics resources from the server.

        Args
        ----
        - AcksRx (bool): ACKs Rx
        - AcksTx (bool): ACKs Tx
        - HellosRx (bool): Hellos Rx
        - HellosTx (bool): Hellos Tx
        - Ipv4NeighborsDeleted (bool): IPv4 Neighbors Deleted
        - Ipv4NeighborsLearned (bool): IPv4 Neighbors Learned
        - Ipv4RouteWithdrawsRx (bool): IPv4 Route Withdraws Rx
        - Ipv4RoutersConfigured (bool): IPv4 Routers Configured
        - Ipv4RoutersRunning (bool): IPv4 Routers Running
        - Ipv4RoutesLearned (bool): IPv4 Routes Learned
        - Ipv4RoutesRx (bool): IPv4 Routes Rx
        - Ipv4RoutesTx (bool): IPv4 Routes Tx
        - Ipv4RoutesWithdrawn (bool): IPv4 Routes Withdrawn
        - Ipv6NeighborsDeleted (bool): IPv6 Neighbors Deleted
        - Ipv6NeighborsLearned (bool): IPv6 Neighbors Learned
        - Ipv6RouteWithdrawsRx (bool): IPv6 Route Withdraws Rx
        - Ipv6RoutersConfigured (bool): IPv6 Routers Configured
        - Ipv6RoutersRunning (bool): IPv6 Routers Running
        - Ipv6RoutesLearned (bool): IPv6 Routes Learned
        - Ipv6RoutesRx (bool): IPv6 Routes Rx
        - Ipv6RoutesTx (bool): IPv6 Routes Tx
        - Ipv6RoutesWithdrawn (bool): IPv6 Routes Withdrawn
        - PacketsRx (bool): Packets Rx
        - PacketsTx (bool): Packets Tx
        - PortName (bool): Port Name
        - QueriesRx (bool): Queries Rx
        - QueriesTx (bool): Queries Tx
        - RepliesRx (bool): Replies Rx
        - RepliesTx (bool): Replies Tx
        - RetransmissionCount (bool): Retransmission Count
        - UpdatesRx (bool): Updates Rx
        - UpdatesTx (bool): Updates Tx

        Returns
        -------
        - self: This instance with matching eigrpAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of eigrpAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the eigrpAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
