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


class BgpAggregatedStatistics(Base):
    """Represents stats of BGP Aggregated Statistics
    The BgpAggregatedStatistics class encapsulates a required bgpAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "bgpAggregatedStatistics"
    _SDM_ATT_MAP = {
        "ActiveStateCount": "activeStateCount",
        "ConnectStateCount": "connectStateCount",
        "EstablishedStateCount": "establishedStateCount",
        "GracefulRestartsAttempted": "gracefulRestartsAttempted",
        "GracefulRestartsFailed": "gracefulRestartsFailed",
        "IdleStateCount": "idleStateCount",
        "KeepalivesRx": "keepalivesRx",
        "KeepalivesTx": "keepalivesTx",
        "MessagesRx": "messagesRx",
        "MessagesTx": "messagesTx",
        "NotificationsRx": "notificationsRx",
        "NotificationsTx": "notificationsTx",
        "OpenconfirmStateCount": "openconfirmStateCount",
        "OpensRx": "opensRx",
        "OpensTx": "opensTx",
        "OpensentStateCount": "opensentStateCount",
        "PortName": "portName",
        "RouteWithdrawsRx": "routeWithdrawsRx",
        "RoutesAdvertised": "routesAdvertised",
        "RoutesRx": "routesRx",
        "RoutesRxGracefulRestart": "routesRxGracefulRestart",
        "RoutesWithdrawn": "routesWithdrawn",
        "SessConfigured": "sessConfigured",
        "SessUp": "sessUp",
        "SessionFlapCount": "sessionFlapCount",
        "StartsOccurred": "startsOccurred",
        "UpdatesRx": "updatesRx",
        "UpdatesTx": "updatesTx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BgpAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def ActiveStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Active State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActiveStateCount"])

    @ActiveStateCount.setter
    def ActiveStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ActiveStateCount"], value)

    @property
    def ConnectStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Connect State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectStateCount"])

    @ConnectStateCount.setter
    def ConnectStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectStateCount"], value)

    @property
    def EstablishedStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Established State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["EstablishedStateCount"])

    @EstablishedStateCount.setter
    def EstablishedStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EstablishedStateCount"], value)

    @property
    def GracefulRestartsAttempted(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Graceful Restarts Attempted
        """
        return self._get_attribute(self._SDM_ATT_MAP["GracefulRestartsAttempted"])

    @GracefulRestartsAttempted.setter
    def GracefulRestartsAttempted(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GracefulRestartsAttempted"], value)

    @property
    def GracefulRestartsFailed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Graceful Restarts Failed
        """
        return self._get_attribute(self._SDM_ATT_MAP["GracefulRestartsFailed"])

    @GracefulRestartsFailed.setter
    def GracefulRestartsFailed(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GracefulRestartsFailed"], value)

    @property
    def IdleStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Idle State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["IdleStateCount"])

    @IdleStateCount.setter
    def IdleStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IdleStateCount"], value)

    @property
    def KeepalivesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: KeepAlives Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["KeepalivesRx"])

    @KeepalivesRx.setter
    def KeepalivesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["KeepalivesRx"], value)

    @property
    def KeepalivesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: KeepAlives Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["KeepalivesTx"])

    @KeepalivesTx.setter
    def KeepalivesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["KeepalivesTx"], value)

    @property
    def MessagesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Messages Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MessagesRx"])

    @MessagesRx.setter
    def MessagesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MessagesRx"], value)

    @property
    def MessagesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Messages Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MessagesTx"])

    @MessagesTx.setter
    def MessagesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MessagesTx"], value)

    @property
    def NotificationsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Notifications Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["NotificationsRx"])

    @NotificationsRx.setter
    def NotificationsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NotificationsRx"], value)

    @property
    def NotificationsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Notifications Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["NotificationsTx"])

    @NotificationsTx.setter
    def NotificationsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NotificationsTx"], value)

    @property
    def OpenconfirmStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OpenConfirm State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["OpenconfirmStateCount"])

    @OpenconfirmStateCount.setter
    def OpenconfirmStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OpenconfirmStateCount"], value)

    @property
    def OpensRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Opens Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["OpensRx"])

    @OpensRx.setter
    def OpensRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OpensRx"], value)

    @property
    def OpensTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Opens Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["OpensTx"])

    @OpensTx.setter
    def OpensTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OpensTx"], value)

    @property
    def OpensentStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OpenSent State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["OpensentStateCount"])

    @OpensentStateCount.setter
    def OpensentStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OpensentStateCount"], value)

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
    def RouteWithdrawsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Route Withdraws Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteWithdrawsRx"])

    @RouteWithdrawsRx.setter
    def RouteWithdrawsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteWithdrawsRx"], value)

    @property
    def RoutesAdvertised(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routes Advertised
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutesAdvertised"])

    @RoutesAdvertised.setter
    def RoutesAdvertised(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutesAdvertised"], value)

    @property
    def RoutesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routes Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutesRx"])

    @RoutesRx.setter
    def RoutesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutesRx"], value)

    @property
    def RoutesRxGracefulRestart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routes Rx Graceful Restart
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutesRxGracefulRestart"])

    @RoutesRxGracefulRestart.setter
    def RoutesRxGracefulRestart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutesRxGracefulRestart"], value)

    @property
    def RoutesWithdrawn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Routes Withdrawn
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoutesWithdrawn"])

    @RoutesWithdrawn.setter
    def RoutesWithdrawn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoutesWithdrawn"], value)

    @property
    def SessConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sess. Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessConfigured"])

    @SessConfigured.setter
    def SessConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessConfigured"], value)

    @property
    def SessUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sess. Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessUp"])

    @SessUp.setter
    def SessUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessUp"], value)

    @property
    def SessionFlapCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Session Flap Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionFlapCount"])

    @SessionFlapCount.setter
    def SessionFlapCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessionFlapCount"], value)

    @property
    def StartsOccurred(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Starts Occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartsOccurred"])

    @StartsOccurred.setter
    def StartsOccurred(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartsOccurred"], value)

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
        ActiveStateCount=None,
        ConnectStateCount=None,
        EstablishedStateCount=None,
        GracefulRestartsAttempted=None,
        GracefulRestartsFailed=None,
        IdleStateCount=None,
        KeepalivesRx=None,
        KeepalivesTx=None,
        MessagesRx=None,
        MessagesTx=None,
        NotificationsRx=None,
        NotificationsTx=None,
        OpenconfirmStateCount=None,
        OpensRx=None,
        OpensTx=None,
        OpensentStateCount=None,
        PortName=None,
        RouteWithdrawsRx=None,
        RoutesAdvertised=None,
        RoutesRx=None,
        RoutesRxGracefulRestart=None,
        RoutesWithdrawn=None,
        SessConfigured=None,
        SessUp=None,
        SessionFlapCount=None,
        StartsOccurred=None,
        UpdatesRx=None,
        UpdatesTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> BgpAggregatedStatistics
        """Updates bgpAggregatedStatistics resource on the server.

        Args
        ----
        - ActiveStateCount (bool): Active State Count
        - ConnectStateCount (bool): Connect State Count
        - EstablishedStateCount (bool): Established State Count
        - GracefulRestartsAttempted (bool): Graceful Restarts Attempted
        - GracefulRestartsFailed (bool): Graceful Restarts Failed
        - IdleStateCount (bool): Idle State Count
        - KeepalivesRx (bool): KeepAlives Rx
        - KeepalivesTx (bool): KeepAlives Tx
        - MessagesRx (bool): Messages Rx
        - MessagesTx (bool): Messages Tx
        - NotificationsRx (bool): Notifications Rx
        - NotificationsTx (bool): Notifications Tx
        - OpenconfirmStateCount (bool): OpenConfirm State Count
        - OpensRx (bool): Opens Rx
        - OpensTx (bool): Opens Tx
        - OpensentStateCount (bool): OpenSent State Count
        - PortName (bool): Port Name
        - RouteWithdrawsRx (bool): Route Withdraws Rx
        - RoutesAdvertised (bool): Routes Advertised
        - RoutesRx (bool): Routes Rx
        - RoutesRxGracefulRestart (bool): Routes Rx Graceful Restart
        - RoutesWithdrawn (bool): Routes Withdrawn
        - SessConfigured (bool): Sess. Configured
        - SessUp (bool): Sess. Up
        - SessionFlapCount (bool): Session Flap Count
        - StartsOccurred (bool): Starts Occurred
        - UpdatesRx (bool): Updates Rx
        - UpdatesTx (bool): Updates Tx

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ActiveStateCount=None,
        ConnectStateCount=None,
        EstablishedStateCount=None,
        GracefulRestartsAttempted=None,
        GracefulRestartsFailed=None,
        IdleStateCount=None,
        KeepalivesRx=None,
        KeepalivesTx=None,
        MessagesRx=None,
        MessagesTx=None,
        NotificationsRx=None,
        NotificationsTx=None,
        OpenconfirmStateCount=None,
        OpensRx=None,
        OpensTx=None,
        OpensentStateCount=None,
        PortName=None,
        RouteWithdrawsRx=None,
        RoutesAdvertised=None,
        RoutesRx=None,
        RoutesRxGracefulRestart=None,
        RoutesWithdrawn=None,
        SessConfigured=None,
        SessUp=None,
        SessionFlapCount=None,
        StartsOccurred=None,
        UpdatesRx=None,
        UpdatesTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> BgpAggregatedStatistics
        """Finds and retrieves bgpAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpAggregatedStatistics resources from the server.

        Args
        ----
        - ActiveStateCount (bool): Active State Count
        - ConnectStateCount (bool): Connect State Count
        - EstablishedStateCount (bool): Established State Count
        - GracefulRestartsAttempted (bool): Graceful Restarts Attempted
        - GracefulRestartsFailed (bool): Graceful Restarts Failed
        - IdleStateCount (bool): Idle State Count
        - KeepalivesRx (bool): KeepAlives Rx
        - KeepalivesTx (bool): KeepAlives Tx
        - MessagesRx (bool): Messages Rx
        - MessagesTx (bool): Messages Tx
        - NotificationsRx (bool): Notifications Rx
        - NotificationsTx (bool): Notifications Tx
        - OpenconfirmStateCount (bool): OpenConfirm State Count
        - OpensRx (bool): Opens Rx
        - OpensTx (bool): Opens Tx
        - OpensentStateCount (bool): OpenSent State Count
        - PortName (bool): Port Name
        - RouteWithdrawsRx (bool): Route Withdraws Rx
        - RoutesAdvertised (bool): Routes Advertised
        - RoutesRx (bool): Routes Rx
        - RoutesRxGracefulRestart (bool): Routes Rx Graceful Restart
        - RoutesWithdrawn (bool): Routes Withdrawn
        - SessConfigured (bool): Sess. Configured
        - SessUp (bool): Sess. Up
        - SessionFlapCount (bool): Session Flap Count
        - StartsOccurred (bool): Starts Occurred
        - UpdatesRx (bool): Updates Rx
        - UpdatesTx (bool): Updates Tx

        Returns
        -------
        - self: This instance with matching bgpAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
