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


class Interface(Base):
    """A network interface, which will be included in the BFD router.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "interface"
    _SDM_ATT_MAP = {
        "EchoConfigureSrcIp": "echoConfigureSrcIp",
        "EchoInterval": "echoInterval",
        "EchoSrcIpv4Address": "echoSrcIpv4Address",
        "EchoSrcIpv6Address": "echoSrcIpv6Address",
        "EchoTimeout": "echoTimeout",
        "EchoTxInterval": "echoTxInterval",
        "EnableCtrlPlaneIndependent": "enableCtrlPlaneIndependent",
        "EnableDemandMode": "enableDemandMode",
        "Enabled": "enabled",
        "FlapTxInterval": "flapTxInterval",
        "InterfaceId": "interfaceId",
        "InterfaceIndex": "interfaceIndex",
        "InterfaceType": "interfaceType",
        "Interfaces": "interfaces",
        "IpDifferentiatedServiceField": "ipDifferentiatedServiceField",
        "MinRxInterval": "minRxInterval",
        "Multiplier": "multiplier",
        "PollInterval": "pollInterval",
        "TxInterval": "txInterval",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Interface, self).__init__(parent, list_op)

    @property
    def Session(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.session_528e31d9c93d0ad2afb513a10d9d8be3.Session): An instance of the Session class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.session_528e31d9c93d0ad2afb513a10d9d8be3 import (
            Session,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Session", None) is not None:
                return self._properties.get("Session")
        return Session(self)

    @property
    def EchoConfigureSrcIp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, allows the user to configure the source IP address of the Echo Message, using echoSrcIpv4Address or echoSrcIpv6Address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoConfigureSrcIp"])

    @EchoConfigureSrcIp.setter
    def EchoConfigureSrcIp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoConfigureSrcIp"], value)

    @property
    def EchoInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This option indicates the desired interval between BFD echo packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoInterval"])

    @EchoInterval.setter
    def EchoInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoInterval"], value)

    @property
    def EchoSrcIpv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the IPv4 echo source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoSrcIpv4Address"])

    @EchoSrcIpv4Address.setter
    def EchoSrcIpv4Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoSrcIpv4Address"], value)

    @property
    def EchoSrcIpv6Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets the IPv6 echo source address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoSrcIpv6Address"])

    @EchoSrcIpv6Address.setter
    def EchoSrcIpv6Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoSrcIpv6Address"], value)

    @property
    def EchoTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The interval, in microseconds, that the interface waits for a response to the last Echo packet sent out.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoTimeout"])

    @EchoTimeout.setter
    def EchoTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoTimeout"], value)

    @property
    def EchoTxInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum interval, in microseconds, that the interface would like to use when transmitting BFD Echo packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EchoTxInterval"])

    @EchoTxInterval.setter
    def EchoTxInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EchoTxInterval"], value)

    @property
    def EnableCtrlPlaneIndependent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set to 1 if the local system's BFD implementation is independent of the control plane.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCtrlPlaneIndependent"])

    @EnableCtrlPlaneIndependent.setter
    def EnableCtrlPlaneIndependent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCtrlPlaneIndependent"], value)

    @property
    def EnableDemandMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables demand mode. 1 indicates demand mode enabled, and 0 indicates demand mode disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDemandMode"])

    @EnableDemandMode.setter
    def EnableDemandMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDemandMode"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of the simulated interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def FlapTxInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: BFD sessions will flap every flapTxIntvs. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlapTxInterval"])

    @FlapTxInterval.setter
    def FlapTxInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlapTxInterval"], value)

    @property
    def InterfaceId(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface): This is a local ID and is unique per router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceId"])

    @InterfaceId.setter
    def InterfaceId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterfaceId"], value)

    @property
    def InterfaceIndex(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The assigned protocol interface ID for this BFD interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceIndex"])

    @InterfaceIndex.setter
    def InterfaceIndex(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterfaceIndex"], value)

    @property
    def InterfaceType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The type of interface to be selected for this BFD interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceType"])

    @InterfaceType.setter
    def InterfaceType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterfaceType"], value)

    @property
    def Interfaces(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernetEndpoint/range): The interfaces that are associated with the selected interface type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Interfaces"])

    @Interfaces.setter
    def Interfaces(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Interfaces"], value)

    @property
    def IpDifferentiatedServiceField(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the TOS byte for IP Differentiated Service Field
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpDifferentiatedServiceField"])

    @IpDifferentiatedServiceField.setter
    def IpDifferentiatedServiceField(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpDifferentiatedServiceField"], value)

    @property
    def MinRxInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This option indicates the desired minimum interval between received BFD control packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRxInterval"])

    @MinRxInterval.setter
    def MinRxInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRxInterval"], value)

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Multiplier * intv defines the timeout period. (default = 3)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Multiplier"])

    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Multiplier"], value)

    @property
    def PollInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If in the Demand Mode, polling will take place every pollIntv interval. (default = 1,000)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PollInterval"])

    @PollInterval.setter
    def PollInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PollInterval"], value)

    @property
    def TxInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This option indicates the desired interval between transmitted BFD control packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxInterval"])

    @TxInterval.setter
    def TxInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxInterval"], value)

    def update(
        self,
        EchoConfigureSrcIp=None,
        EchoInterval=None,
        EchoSrcIpv4Address=None,
        EchoSrcIpv6Address=None,
        EchoTimeout=None,
        EchoTxInterval=None,
        EnableCtrlPlaneIndependent=None,
        EnableDemandMode=None,
        Enabled=None,
        FlapTxInterval=None,
        InterfaceId=None,
        InterfaceIndex=None,
        InterfaceType=None,
        Interfaces=None,
        IpDifferentiatedServiceField=None,
        MinRxInterval=None,
        Multiplier=None,
        PollInterval=None,
        TxInterval=None,
    ):
        # type: (bool, int, str, str, int, int, bool, bool, bool, int, str, int, str, str, int, int, int, int, int) -> Interface
        """Updates interface resource on the server.

        Args
        ----
        - EchoConfigureSrcIp (bool): If true, allows the user to configure the source IP address of the Echo Message, using echoSrcIpv4Address or echoSrcIpv6Address.
        - EchoInterval (number): This option indicates the desired interval between BFD echo packets.
        - EchoSrcIpv4Address (str): Sets the IPv4 echo source address.
        - EchoSrcIpv6Address (str): Sets the IPv6 echo source address.
        - EchoTimeout (number): The interval, in microseconds, that the interface waits for a response to the last Echo packet sent out.
        - EchoTxInterval (number): The minimum interval, in microseconds, that the interface would like to use when transmitting BFD Echo packets.
        - EnableCtrlPlaneIndependent (bool): Set to 1 if the local system's BFD implementation is independent of the control plane.
        - EnableDemandMode (bool): Enables demand mode. 1 indicates demand mode enabled, and 0 indicates demand mode disabled.
        - Enabled (bool): Enables the use of the simulated interface.
        - FlapTxInterval (number): BFD sessions will flap every flapTxIntvs. (default = 0)
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): This is a local ID and is unique per router.
        - InterfaceIndex (number): The assigned protocol interface ID for this BFD interface.
        - InterfaceType (str): The type of interface to be selected for this BFD interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/interface | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernetEndpoint/range)): The interfaces that are associated with the selected interface type.
        - IpDifferentiatedServiceField (number): Sets the TOS byte for IP Differentiated Service Field
        - MinRxInterval (number): This option indicates the desired minimum interval between received BFD control packets.
        - Multiplier (number): Multiplier * intv defines the timeout period. (default = 3)
        - PollInterval (number): If in the Demand Mode, polling will take place every pollIntv interval. (default = 1,000)
        - TxInterval (number): This option indicates the desired interval between transmitted BFD control packets.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        EchoConfigureSrcIp=None,
        EchoInterval=None,
        EchoSrcIpv4Address=None,
        EchoSrcIpv6Address=None,
        EchoTimeout=None,
        EchoTxInterval=None,
        EnableCtrlPlaneIndependent=None,
        EnableDemandMode=None,
        Enabled=None,
        FlapTxInterval=None,
        InterfaceId=None,
        InterfaceIndex=None,
        InterfaceType=None,
        Interfaces=None,
        IpDifferentiatedServiceField=None,
        MinRxInterval=None,
        Multiplier=None,
        PollInterval=None,
        TxInterval=None,
    ):
        # type: (bool, int, str, str, int, int, bool, bool, bool, int, str, int, str, str, int, int, int, int, int) -> Interface
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - EchoConfigureSrcIp (bool): If true, allows the user to configure the source IP address of the Echo Message, using echoSrcIpv4Address or echoSrcIpv6Address.
        - EchoInterval (number): This option indicates the desired interval between BFD echo packets.
        - EchoSrcIpv4Address (str): Sets the IPv4 echo source address.
        - EchoSrcIpv6Address (str): Sets the IPv6 echo source address.
        - EchoTimeout (number): The interval, in microseconds, that the interface waits for a response to the last Echo packet sent out.
        - EchoTxInterval (number): The minimum interval, in microseconds, that the interface would like to use when transmitting BFD Echo packets.
        - EnableCtrlPlaneIndependent (bool): Set to 1 if the local system's BFD implementation is independent of the control plane.
        - EnableDemandMode (bool): Enables demand mode. 1 indicates demand mode enabled, and 0 indicates demand mode disabled.
        - Enabled (bool): Enables the use of the simulated interface.
        - FlapTxInterval (number): BFD sessions will flap every flapTxIntvs. (default = 0)
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): This is a local ID and is unique per router.
        - InterfaceIndex (number): The assigned protocol interface ID for this BFD interface.
        - InterfaceType (str): The type of interface to be selected for this BFD interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/interface | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernetEndpoint/range)): The interfaces that are associated with the selected interface type.
        - IpDifferentiatedServiceField (number): Sets the TOS byte for IP Differentiated Service Field
        - MinRxInterval (number): This option indicates the desired minimum interval between received BFD control packets.
        - Multiplier (number): Multiplier * intv defines the timeout period. (default = 3)
        - PollInterval (number): If in the Demand Mode, polling will take place every pollIntv interval. (default = 1,000)
        - TxInterval (number): This option indicates the desired interval between transmitted BFD control packets.

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        EchoConfigureSrcIp=None,
        EchoInterval=None,
        EchoSrcIpv4Address=None,
        EchoSrcIpv6Address=None,
        EchoTimeout=None,
        EchoTxInterval=None,
        EnableCtrlPlaneIndependent=None,
        EnableDemandMode=None,
        Enabled=None,
        FlapTxInterval=None,
        InterfaceId=None,
        InterfaceIndex=None,
        InterfaceType=None,
        Interfaces=None,
        IpDifferentiatedServiceField=None,
        MinRxInterval=None,
        Multiplier=None,
        PollInterval=None,
        TxInterval=None,
    ):
        # type: (bool, int, str, str, int, int, bool, bool, bool, int, str, int, str, str, int, int, int, int, int) -> Interface
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - EchoConfigureSrcIp (bool): If true, allows the user to configure the source IP address of the Echo Message, using echoSrcIpv4Address or echoSrcIpv6Address.
        - EchoInterval (number): This option indicates the desired interval between BFD echo packets.
        - EchoSrcIpv4Address (str): Sets the IPv4 echo source address.
        - EchoSrcIpv6Address (str): Sets the IPv6 echo source address.
        - EchoTimeout (number): The interval, in microseconds, that the interface waits for a response to the last Echo packet sent out.
        - EchoTxInterval (number): The minimum interval, in microseconds, that the interface would like to use when transmitting BFD Echo packets.
        - EnableCtrlPlaneIndependent (bool): Set to 1 if the local system's BFD implementation is independent of the control plane.
        - EnableDemandMode (bool): Enables demand mode. 1 indicates demand mode enabled, and 0 indicates demand mode disabled.
        - Enabled (bool): Enables the use of the simulated interface.
        - FlapTxInterval (number): BFD sessions will flap every flapTxIntvs. (default = 0)
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): This is a local ID and is unique per router.
        - InterfaceIndex (number): The assigned protocol interface ID for this BFD interface.
        - InterfaceType (str): The type of interface to be selected for this BFD interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/interface | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernetEndpoint/range)): The interfaces that are associated with the selected interface type.
        - IpDifferentiatedServiceField (number): Sets the TOS byte for IP Differentiated Service Field
        - MinRxInterval (number): This option indicates the desired minimum interval between received BFD control packets.
        - Multiplier (number): Multiplier * intv defines the timeout period. (default = 3)
        - PollInterval (number): If in the Demand Mode, polling will take place every pollIntv interval. (default = 1,000)
        - TxInterval (number): This option indicates the desired interval between transmitted BFD control packets.

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetInterfaceAccessorIfaceList(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getInterfaceAccessorIfaceList operation on the server.

        NOT DEFINED

        getInterfaceAccessorIfaceList(async_operation=bool)string
        ---------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: NOT DEFINED

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
            "getInterfaceAccessorIfaceList", payload=payload, response_object=None
        )
