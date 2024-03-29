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


class Options(Base):
    """Global NDP settings, per port
    The Options class encapsulates a required options resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "options"
    _SDM_ATT_MAP = {
        "ActOnGratArp": "actOnGratArp",
        "ArpRefreshInterval": "arpRefreshInterval",
        "DadEnabled": "dadEnabled",
        "DadTransmits": "dadTransmits",
        "IgnoreMldQueries": "ignoreMldQueries",
        "Ipv4McastSolicit": "ipv4McastSolicit",
        "Ipv4RetransTime": "ipv4RetransTime",
        "Mcast_solicit": "mcast_solicit",
        "NsRefreshInterval": "nsRefreshInterval",
        "ObjectId": "objectId",
        "RetransTime": "retransTime",
        "RouterSolicitationDelay": "routerSolicitationDelay",
        "RouterSolicitationInterval": "routerSolicitationInterval",
        "RouterSolicitations": "routerSolicitations",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Options, self).__init__(parent, list_op)

    @property
    def ActOnGratArp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When enabled, the ARP refresh timer in kernel will be set to initial value configured by the user when GratArp message is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActOnGratArp"])

    @ActOnGratArp.setter
    def ActOnGratArp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ActOnGratArp"], value)

    @property
    def ArpRefreshInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time interval in seconds taken by IxNetwork to refresh IPv4 address cache. By default, it is set to 60 seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpRefreshInterval"])

    @ArpRefreshInterval.setter
    def ArpRefreshInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpRefreshInterval"], value)

    @property
    def DadEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When enabled, IPv6 server will reply to NDP DAD NS messages with Neighbor Advertisement packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DadEnabled"])

    @DadEnabled.setter
    def DadEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DadEnabled"], value)

    @property
    def DadTransmits(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Neighbor Solicitations to send until assuming no routers are present.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DadTransmits"])

    @DadTransmits.setter
    def DadTransmits(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DadTransmits"], value)

    @property
    def IgnoreMldQueries(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When enabled IPv6 emulation will not respond to MLD queries with Solicited node membership reports.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IgnoreMldQueries"])

    @IgnoreMldQueries.setter
    def IgnoreMldQueries(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IgnoreMldQueries"], value)

    @property
    def Ipv4McastSolicit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of ARP requests to send to resolve one MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4McastSolicit"])

    @Ipv4McastSolicit.setter
    def Ipv4McastSolicit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4McastSolicit"], value)

    @property
    def Ipv4RetransTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of milliseconds to wait between ARP requests.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4RetransTime"])

    @Ipv4RetransTime.setter
    def Ipv4RetransTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4RetransTime"], value)

    @property
    def Mcast_solicit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Neighbor Solicitations to send until giving up on link layer address resolution.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mcast_solicit"])

    @Mcast_solicit.setter
    def Mcast_solicit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mcast_solicit"], value)

    @property
    def NsRefreshInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time interval in seconds taken by IxNetwork to refresh IPv6 address cache. By default, it is set to 60 seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["NsRefreshInterval"])

    @NsRefreshInterval.setter
    def NsRefreshInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NsRefreshInterval"], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    @property
    def RetransTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of milliseconds to wait between Neighbor Solicitations.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RetransTime"])

    @RetransTime.setter
    def RetransTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RetransTime"], value)

    @property
    def RouterSolicitationDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of seconds to wait after interface is brought up before sending Router Solicitations. When an IPv6 link-local address is added to an interface, first NS can be sent after no more than the value of this setting seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterSolicitationDelay"])

    @RouterSolicitationDelay.setter
    def RouterSolicitationDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterSolicitationDelay"], value)

    @property
    def RouterSolicitationInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of seconds to wait between Router Solicitations.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterSolicitationInterval"])

    @RouterSolicitationInterval.setter
    def RouterSolicitationInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterSolicitationInterval"], value)

    @property
    def RouterSolicitations(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Router Solicitations to send until assuming no routers are present.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterSolicitations"])

    @RouterSolicitations.setter
    def RouterSolicitations(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterSolicitations"], value)

    def update(
        self,
        ActOnGratArp=None,
        ArpRefreshInterval=None,
        DadEnabled=None,
        DadTransmits=None,
        IgnoreMldQueries=None,
        Ipv4McastSolicit=None,
        Ipv4RetransTime=None,
        Mcast_solicit=None,
        NsRefreshInterval=None,
        RetransTime=None,
        RouterSolicitationDelay=None,
        RouterSolicitationInterval=None,
        RouterSolicitations=None,
    ):
        # type: (bool, int, bool, int, bool, int, int, int, int, int, int, int, int) -> Options
        """Updates options resource on the server.

        Args
        ----
        - ActOnGratArp (bool): When enabled, the ARP refresh timer in kernel will be set to initial value configured by the user when GratArp message is received.
        - ArpRefreshInterval (number): The time interval in seconds taken by IxNetwork to refresh IPv4 address cache. By default, it is set to 60 seconds
        - DadEnabled (bool): When enabled, IPv6 server will reply to NDP DAD NS messages with Neighbor Advertisement packets.
        - DadTransmits (number): Number of Neighbor Solicitations to send until assuming no routers are present.
        - IgnoreMldQueries (bool): When enabled IPv6 emulation will not respond to MLD queries with Solicited node membership reports.
        - Ipv4McastSolicit (number): Maximum number of ARP requests to send to resolve one MAC address.
        - Ipv4RetransTime (number): Number of milliseconds to wait between ARP requests.
        - Mcast_solicit (number): Number of Neighbor Solicitations to send until giving up on link layer address resolution.
        - NsRefreshInterval (number): The time interval in seconds taken by IxNetwork to refresh IPv6 address cache. By default, it is set to 60 seconds
        - RetransTime (number): Number of milliseconds to wait between Neighbor Solicitations.
        - RouterSolicitationDelay (number): Number of seconds to wait after interface is brought up before sending Router Solicitations. When an IPv6 link-local address is added to an interface, first NS can be sent after no more than the value of this setting seconds.
        - RouterSolicitationInterval (number): Number of seconds to wait between Router Solicitations.
        - RouterSolicitations (number): Number of Router Solicitations to send until assuming no routers are present.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ActOnGratArp=None,
        ArpRefreshInterval=None,
        DadEnabled=None,
        DadTransmits=None,
        IgnoreMldQueries=None,
        Ipv4McastSolicit=None,
        Ipv4RetransTime=None,
        Mcast_solicit=None,
        NsRefreshInterval=None,
        ObjectId=None,
        RetransTime=None,
        RouterSolicitationDelay=None,
        RouterSolicitationInterval=None,
        RouterSolicitations=None,
    ):
        # type: (bool, int, bool, int, bool, int, int, int, int, str, int, int, int, int) -> Options
        """Finds and retrieves options resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve options resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all options resources from the server.

        Args
        ----
        - ActOnGratArp (bool): When enabled, the ARP refresh timer in kernel will be set to initial value configured by the user when GratArp message is received.
        - ArpRefreshInterval (number): The time interval in seconds taken by IxNetwork to refresh IPv4 address cache. By default, it is set to 60 seconds
        - DadEnabled (bool): When enabled, IPv6 server will reply to NDP DAD NS messages with Neighbor Advertisement packets.
        - DadTransmits (number): Number of Neighbor Solicitations to send until assuming no routers are present.
        - IgnoreMldQueries (bool): When enabled IPv6 emulation will not respond to MLD queries with Solicited node membership reports.
        - Ipv4McastSolicit (number): Maximum number of ARP requests to send to resolve one MAC address.
        - Ipv4RetransTime (number): Number of milliseconds to wait between ARP requests.
        - Mcast_solicit (number): Number of Neighbor Solicitations to send until giving up on link layer address resolution.
        - NsRefreshInterval (number): The time interval in seconds taken by IxNetwork to refresh IPv6 address cache. By default, it is set to 60 seconds
        - ObjectId (str): Unique identifier for this object
        - RetransTime (number): Number of milliseconds to wait between Neighbor Solicitations.
        - RouterSolicitationDelay (number): Number of seconds to wait after interface is brought up before sending Router Solicitations. When an IPv6 link-local address is added to an interface, first NS can be sent after no more than the value of this setting seconds.
        - RouterSolicitationInterval (number): Number of seconds to wait between Router Solicitations.
        - RouterSolicitations (number): Number of Router Solicitations to send until assuming no routers are present.

        Returns
        -------
        - self: This instance with matching options resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of options data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the options resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "customProtocolStack", payload=payload, response_object=None
        )

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "disableProtocolStack", payload=payload, response_object=None
        )

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "enableProtocolStack", payload=payload, response_object=None
        )
