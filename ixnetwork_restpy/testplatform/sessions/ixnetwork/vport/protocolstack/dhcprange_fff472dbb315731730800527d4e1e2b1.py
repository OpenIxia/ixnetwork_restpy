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


class DhcpRange(Base):
    """Manages a range of IP addresses that are configured using DHCP protocol.
    The DhcpRange class encapsulates a required dhcpRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "dhcpRange"
    _SDM_ATT_MAP = {
        "ClientOptionSet": "clientOptionSet",
        "Count": "count",
        "Dhcp4Broadcast": "dhcp4Broadcast",
        "Dhcp4ParamRequestList": "dhcp4ParamRequestList",
        "Dhcp4ServerAddress": "dhcp4ServerAddress",
        "Dhcp4UseFirstServer": "dhcp4UseFirstServer",
        "Dhcp6DuidEnterpriseId": "dhcp6DuidEnterpriseId",
        "Dhcp6DuidType": "dhcp6DuidType",
        "Dhcp6DuidVendorId": "dhcp6DuidVendorId",
        "Dhcp6DuidVendorIdIncrement": "dhcp6DuidVendorIdIncrement",
        "Dhcp6IaId": "dhcp6IaId",
        "Dhcp6IaIdIncrement": "dhcp6IaIdIncrement",
        "Dhcp6IaT1": "dhcp6IaT1",
        "Dhcp6IaT2": "dhcp6IaT2",
        "Dhcp6IaType": "dhcp6IaType",
        "Dhcp6MasterRange": "dhcp6MasterRange",
        "Dhcp6ParamRequestList": "dhcp6ParamRequestList",
        "Enabled": "enabled",
        "IpType": "ipType",
        "Name": "name",
        "ObjectId": "objectId",
        "Relay6HostsPerOptInterfaceId": "relay6HostsPerOptInterfaceId",
        "Relay6OptInterfaceId": "relay6OptInterfaceId",
        "Relay6UseOptInterfaceId": "relay6UseOptInterfaceId",
        "RelayAddressIncrement": "relayAddressIncrement",
        "RelayCircuitId": "relayCircuitId",
        "RelayCount": "relayCount",
        "RelayDestination": "relayDestination",
        "RelayFirstAddress": "relayFirstAddress",
        "RelayFirstVlanId": "relayFirstVlanId",
        "RelayGateway": "relayGateway",
        "RelayHostsPerCircuitId": "relayHostsPerCircuitId",
        "RelayHostsPerRemoteId": "relayHostsPerRemoteId",
        "RelayOptionSet": "relayOptionSet",
        "RelayOverrideVlanSettings": "relayOverrideVlanSettings",
        "RelayRemoteId": "relayRemoteId",
        "RelaySubnet": "relaySubnet",
        "RelayUseCircuitId": "relayUseCircuitId",
        "RelayUseRemoteId": "relayUseRemoteId",
        "RelayUseSuboption6": "relayUseSuboption6",
        "RelayVlanCount": "relayVlanCount",
        "RelayVlanIncrMode": "relayVlanIncrMode",
        "RelayVlanIncrement": "relayVlanIncrement",
        "RenewTimer": "renewTimer",
        "Suboption6AddressSubnet": "suboption6AddressSubnet",
        "Suboption6FirstAddress": "suboption6FirstAddress",
        "UseRapidCommit": "useRapidCommit",
        "UseRelayAgent": "useRelayAgent",
        "UseTrustedNetworkElement": "useTrustedNetworkElement",
        "UseVendorClassId": "useVendorClassId",
        "VendorClassId": "vendorClassId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DhcpRange, self).__init__(parent, list_op)

    @property
    def VlanIdInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanidinfo_5b58ad8a545b69da5b9179316b6965ef.VlanIdInfo): An instance of the VlanIdInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanidinfo_5b58ad8a545b69da5b9179316b6965ef import (
            VlanIdInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VlanIdInfo", None) is not None:
                return self._properties.get("VlanIdInfo")
        return VlanIdInfo(self)

    @property
    def ClientOptionSet(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/dhcpGlobals/dhcpOptionSet): The DHCP client options associated with this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientOptionSet"])

    @ClientOptionSet.setter
    def ClientOptionSet(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientOptionSet"], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of DHCP clients to be created by this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @Count.setter
    def Count(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Count"], value)

    @property
    def Dhcp4Broadcast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, ask the server or relay agent to use the broadcast IP address in the replies.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp4Broadcast"])

    @Dhcp4Broadcast.setter
    def Dhcp4Broadcast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp4Broadcast"], value)

    @property
    def Dhcp4ParamRequestList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp4ParamRequestList"])

    @Dhcp4ParamRequestList.setter
    def Dhcp4ParamRequestList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp4ParamRequestList"], value)

    @property
    def Dhcp4ServerAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The address of the DHCP server from which the subnet will accept IP addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp4ServerAddress"])

    @Dhcp4ServerAddress.setter
    def Dhcp4ServerAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp4ServerAddress"], value)

    @property
    def Dhcp4UseFirstServer(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the subnet accepts the IP addresses offered by the firstserver to respond with an offer of IP addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp4UseFirstServer"])

    @Dhcp4UseFirstServer.setter
    def Dhcp4UseFirstServer(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp4UseFirstServer"], value)

    @property
    def Dhcp6DuidEnterpriseId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6DuidEnterpriseId"])

    @Dhcp6DuidEnterpriseId.setter
    def Dhcp6DuidEnterpriseId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6DuidEnterpriseId"], value)

    @property
    def Dhcp6DuidType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: DHCP Unique Identifier Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6DuidType"])

    @Dhcp6DuidType.setter
    def Dhcp6DuidType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6DuidType"], value)

    @property
    def Dhcp6DuidVendorId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6DuidVendorId"])

    @Dhcp6DuidVendorId.setter
    def Dhcp6DuidVendorId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6DuidVendorId"], value)

    @property
    def Dhcp6DuidVendorIdIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value by which the VENDOR-ID is incremented for each DHCP client.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6DuidVendorIdIncrement"])

    @Dhcp6DuidVendorIdIncrement.setter
    def Dhcp6DuidVendorIdIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6DuidVendorIdIncrement"], value)

    @property
    def Dhcp6IaId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The identity association unique ID for this range.This ID is incremented automaticaly for each DHCP client.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6IaId"])

    @Dhcp6IaId.setter
    def Dhcp6IaId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6IaId"], value)

    @property
    def Dhcp6IaIdIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value by which the IA-ID is incremented for each DHCP client.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6IaIdIncrement"])

    @Dhcp6IaIdIncrement.setter
    def Dhcp6IaIdIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6IaIdIncrement"], value)

    @property
    def Dhcp6IaT1(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The suggested time at which the client contacts the server from whichthe addresses were obtained to extend the lifetimes of the addresses assigned.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6IaT1"])

    @Dhcp6IaT1.setter
    def Dhcp6IaT1(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6IaT1"], value)

    @property
    def Dhcp6IaT2(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The suggested time at which the client contacts any available serverto extend the lifetimes of the addresses assigned.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6IaT2"])

    @Dhcp6IaT2.setter
    def Dhcp6IaT2(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6IaT2"], value)

    @property
    def Dhcp6IaType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Identity Association Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6IaType"])

    @Dhcp6IaType.setter
    def Dhcp6IaType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6IaType"], value)

    @property
    def Dhcp6MasterRange(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range/dhcpRange): The DHCP-PD range whose negotiated prefix will be used by this range to configure its addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6MasterRange"])

    @Dhcp6MasterRange.setter
    def Dhcp6MasterRange(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6MasterRange"], value)

    @property
    def Dhcp6ParamRequestList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcp6ParamRequestList"])

    @Dhcp6ParamRequestList.setter
    def Dhcp6ParamRequestList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcp6ParamRequestList"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Defines the version of IP address style to be used for describing the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpType"])

    @IpType.setter
    def IpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpType"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

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
    def Relay6HostsPerOptInterfaceId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of consecutive hosts with the same interfaceId option.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Relay6HostsPerOptInterfaceId"])

    @Relay6HostsPerOptInterfaceId.setter
    def Relay6HostsPerOptInterfaceId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Relay6HostsPerOptInterfaceId"], value)

    @property
    def Relay6OptInterfaceId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This option is added by relay agents that terminate switched or permanent circuitsand have mechanisms to identify the remote host end of the circuit (see RFC3315, section 22.18).The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].
        """
        return self._get_attribute(self._SDM_ATT_MAP["Relay6OptInterfaceId"])

    @Relay6OptInterfaceId.setter
    def Relay6OptInterfaceId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Relay6OptInterfaceId"], value)

    @property
    def Relay6UseOptInterfaceId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select to add INTERFACE-ID option to outgoing messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Relay6UseOptInterfaceId"])

    @Relay6UseOptInterfaceId.setter
    def Relay6UseOptInterfaceId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Relay6UseOptInterfaceId"], value)

    @property
    def RelayAddressIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value by which to increment the IP address for each relay agent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayAddressIncrement"])

    @RelayAddressIncrement.setter
    def RelayAddressIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayAddressIncrement"], value)

    @property
    def RelayCircuitId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This option is added by relay agents that terminate switched or permanent circuits.The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayCircuitId"])

    @RelayCircuitId.setter
    def RelayCircuitId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayCircuitId"], value)

    @property
    def RelayCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of relay agents to use in this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayCount"])

    @RelayCount.setter
    def RelayCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayCount"], value)

    @property
    def RelayDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The address to which the requests from DHCP clients are be forwarded.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayDestination"])

    @RelayDestination.setter
    def RelayDestination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayDestination"], value)

    @property
    def RelayFirstAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address used by first DHCP Relay Agent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayFirstAddress"])

    @RelayFirstAddress.setter
    def RelayFirstAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayFirstAddress"], value)

    @property
    def RelayFirstVlanId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The first (outer) vlan id to allocate to relay agent interfaces.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayFirstVlanId"])

    @RelayFirstVlanId.setter
    def RelayFirstVlanId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayFirstVlanId"], value)

    @property
    def RelayGateway(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The gateway address used for all relay agents.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayGateway"])

    @RelayGateway.setter
    def RelayGateway(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayGateway"], value)

    @property
    def RelayHostsPerCircuitId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of consecutive hosts with the same Circuit ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayHostsPerCircuitId"])

    @RelayHostsPerCircuitId.setter
    def RelayHostsPerCircuitId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayHostsPerCircuitId"], value)

    @property
    def RelayHostsPerRemoteId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of consecutive hosts with the same Remote ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayHostsPerRemoteId"])

    @RelayHostsPerRemoteId.setter
    def RelayHostsPerRemoteId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayHostsPerRemoteId"], value)

    @property
    def RelayOptionSet(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/dhcpGlobals/dhcpOptionSet): The DHCP relay options associated with this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayOptionSet"])

    @RelayOptionSet.setter
    def RelayOptionSet(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayOptionSet"], value)

    @property
    def RelayOverrideVlanSettings(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then we enable overriding of VLAN settings through relayFirstVlanId, relayVlanCount and relayVlanIncrement.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayOverrideVlanSettings"])

    @RelayOverrideVlanSettings.setter
    def RelayOverrideVlanSettings(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayOverrideVlanSettings"], value)

    @property
    def RelayRemoteId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This option is added by relay agents that terminate switched or permanent circuitsand have mechanisms to identify the remote host end of the circuit.The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayRemoteId"])

    @RelayRemoteId.setter
    def RelayRemoteId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayRemoteId"], value)

    @property
    def RelaySubnet(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The network mask used for all relay agents.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelaySubnet"])

    @RelaySubnet.setter
    def RelaySubnet(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelaySubnet"], value)

    @property
    def RelayUseCircuitId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select to add CIRCUIT-ID option to outgoing messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayUseCircuitId"])

    @RelayUseCircuitId.setter
    def RelayUseCircuitId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayUseCircuitId"], value)

    @property
    def RelayUseRemoteId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Select to add REMOTE-ID option to outgoing messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayUseRemoteId"])

    @RelayUseRemoteId.setter
    def RelayUseRemoteId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayUseRemoteId"], value)

    @property
    def RelayUseSuboption6(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then relays will add relay suboption6 (RFC3993) to the DHCP packages they send to DHCP servers.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayUseSuboption6"])

    @RelayUseSuboption6.setter
    def RelayUseSuboption6(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayUseSuboption6"], value)

    @property
    def RelayVlanCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of different vlan ids to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayVlanCount"])

    @RelayVlanCount.setter
    def RelayVlanCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayVlanCount"], value)

    @property
    def RelayVlanIncrMode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The method used to increment VLAN IDs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayVlanIncrMode"])

    @RelayVlanIncrMode.setter
    def RelayVlanIncrMode(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayVlanIncrMode"], value)

    @property
    def RelayVlanIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The vlan increment to use for relay interfaces.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayVlanIncrement"])

    @RelayVlanIncrement.setter
    def RelayVlanIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayVlanIncrement"], value)

    @property
    def RenewTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The used-defined lease renewal timer.The value is estimated in seconds and will override the lease renewaltimer if it is not zero and is smaller than server-defined value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RenewTimer"])

    @RenewTimer.setter
    def RenewTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RenewTimer"], value)

    @property
    def Suboption6AddressSubnet(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The network mask used for all suboption6 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Suboption6AddressSubnet"])

    @Suboption6AddressSubnet.setter
    def Suboption6AddressSubnet(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Suboption6AddressSubnet"], value)

    @property
    def Suboption6FirstAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: We only allow suboption6 to store the IP address of a host to which replies from the DHCP server should be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Suboption6FirstAddress"])

    @Suboption6FirstAddress.setter
    def Suboption6FirstAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Suboption6FirstAddress"], value)

    @property
    def UseRapidCommit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables DHCP clients to negotiate leases with rapid commit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseRapidCommit"])

    @UseRapidCommit.setter
    def UseRapidCommit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseRapidCommit"], value)

    @property
    def UseRelayAgent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Activates DHCP Relay Agent Emulation.Use this if the DHCP server is located in a different network.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseRelayAgent"])

    @UseRelayAgent.setter
    def UseRelayAgent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseRelayAgent"], value)

    @property
    def UseTrustedNetworkElement(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Simulate trusted network elements on the port instead of relays - that is, the packets look like normal DHCP packets, but have the relay options added (in case the circuit and Remote ID are set). This makes the remote/circuit id fields available for edit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseTrustedNetworkElement"])

    @UseTrustedNetworkElement.setter
    def UseTrustedNetworkElement(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseTrustedNetworkElement"], value)

    @property
    def UseVendorClassId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables use of the Vendor Class Identifier configured in the field below.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseVendorClassId"])

    @UseVendorClassId.setter
    def UseVendorClassId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseVendorClassId"], value)

    @property
    def VendorClassId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorClassId"])

    @VendorClassId.setter
    def VendorClassId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorClassId"], value)

    def update(
        self,
        ClientOptionSet=None,
        Count=None,
        Dhcp4Broadcast=None,
        Dhcp4ParamRequestList=None,
        Dhcp4ServerAddress=None,
        Dhcp4UseFirstServer=None,
        Dhcp6DuidEnterpriseId=None,
        Dhcp6DuidType=None,
        Dhcp6DuidVendorId=None,
        Dhcp6DuidVendorIdIncrement=None,
        Dhcp6IaId=None,
        Dhcp6IaIdIncrement=None,
        Dhcp6IaT1=None,
        Dhcp6IaT2=None,
        Dhcp6IaType=None,
        Dhcp6MasterRange=None,
        Dhcp6ParamRequestList=None,
        Enabled=None,
        IpType=None,
        Name=None,
        Relay6HostsPerOptInterfaceId=None,
        Relay6OptInterfaceId=None,
        Relay6UseOptInterfaceId=None,
        RelayAddressIncrement=None,
        RelayCircuitId=None,
        RelayCount=None,
        RelayDestination=None,
        RelayFirstAddress=None,
        RelayFirstVlanId=None,
        RelayGateway=None,
        RelayHostsPerCircuitId=None,
        RelayHostsPerRemoteId=None,
        RelayOptionSet=None,
        RelayOverrideVlanSettings=None,
        RelayRemoteId=None,
        RelaySubnet=None,
        RelayUseCircuitId=None,
        RelayUseRemoteId=None,
        RelayUseSuboption6=None,
        RelayVlanCount=None,
        RelayVlanIncrMode=None,
        RelayVlanIncrement=None,
        RenewTimer=None,
        Suboption6AddressSubnet=None,
        Suboption6FirstAddress=None,
        UseRapidCommit=None,
        UseRelayAgent=None,
        UseTrustedNetworkElement=None,
        UseVendorClassId=None,
        VendorClassId=None,
    ):
        # type: (str, int, bool, str, str, bool, int, str, int, int, int, int, int, int, str, str, str, bool, str, str, int, str, bool, str, str, int, str, str, int, str, int, int, str, bool, str, int, bool, bool, bool, int, int, int, int, int, str, bool, bool, bool, bool, str) -> DhcpRange
        """Updates dhcpRange resource on the server.

        Args
        ----
        - ClientOptionSet (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/dhcpGlobals/dhcpOptionSet)): The DHCP client options associated with this range.
        - Count (number): The number of DHCP clients to be created by this range.
        - Dhcp4Broadcast (bool): If enabled, ask the server or relay agent to use the broadcast IP address in the replies.
        - Dhcp4ParamRequestList (str): The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
        - Dhcp4ServerAddress (str): The address of the DHCP server from which the subnet will accept IP addresses.
        - Dhcp4UseFirstServer (bool): If enabled, the subnet accepts the IP addresses offered by the firstserver to respond with an offer of IP addresses.
        - Dhcp6DuidEnterpriseId (number): The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.
        - Dhcp6DuidType (str): DHCP Unique Identifier Type.
        - Dhcp6DuidVendorId (number): The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.
        - Dhcp6DuidVendorIdIncrement (number): The value by which the VENDOR-ID is incremented for each DHCP client.
        - Dhcp6IaId (number): The identity association unique ID for this range.This ID is incremented automaticaly for each DHCP client.
        - Dhcp6IaIdIncrement (number): The value by which the IA-ID is incremented for each DHCP client.
        - Dhcp6IaT1 (number): The suggested time at which the client contacts the server from whichthe addresses were obtained to extend the lifetimes of the addresses assigned.
        - Dhcp6IaT2 (number): The suggested time at which the client contacts any available serverto extend the lifetimes of the addresses assigned.
        - Dhcp6IaType (str): Identity Association Type.
        - Dhcp6MasterRange (str(None | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range/dhcpRange)): The DHCP-PD range whose negotiated prefix will be used by this range to configure its addresses.
        - Dhcp6ParamRequestList (str): The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): Defines the version of IP address style to be used for describing the range.
        - Name (str): Name of range
        - Relay6HostsPerOptInterfaceId (number): Number of consecutive hosts with the same interfaceId option.
        - Relay6OptInterfaceId (str): This option is added by relay agents that terminate switched or permanent circuitsand have mechanisms to identify the remote host end of the circuit (see RFC3315, section 22.18).The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].
        - Relay6UseOptInterfaceId (bool): Select to add INTERFACE-ID option to outgoing messages.
        - RelayAddressIncrement (str): The value by which to increment the IP address for each relay agent.
        - RelayCircuitId (str): This option is added by relay agents that terminate switched or permanent circuits.The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].
        - RelayCount (number): The number of relay agents to use in this range.
        - RelayDestination (str): The address to which the requests from DHCP clients are be forwarded.
        - RelayFirstAddress (str): The IP address used by first DHCP Relay Agent.
        - RelayFirstVlanId (number): The first (outer) vlan id to allocate to relay agent interfaces.
        - RelayGateway (str): The gateway address used for all relay agents.
        - RelayHostsPerCircuitId (number): Number of consecutive hosts with the same Circuit ID.
        - RelayHostsPerRemoteId (number): Number of consecutive hosts with the same Remote ID.
        - RelayOptionSet (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/dhcpGlobals/dhcpOptionSet)): The DHCP relay options associated with this range.
        - RelayOverrideVlanSettings (bool): If true then we enable overriding of VLAN settings through relayFirstVlanId, relayVlanCount and relayVlanIncrement.
        - RelayRemoteId (str): This option is added by relay agents that terminate switched or permanent circuitsand have mechanisms to identify the remote host end of the circuit.The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].
        - RelaySubnet (number): The network mask used for all relay agents.
        - RelayUseCircuitId (bool): Select to add CIRCUIT-ID option to outgoing messages.
        - RelayUseRemoteId (bool): Select to add REMOTE-ID option to outgoing messages.
        - RelayUseSuboption6 (bool): If true then relays will add relay suboption6 (RFC3993) to the DHCP packages they send to DHCP servers.
        - RelayVlanCount (number): The number of different vlan ids to use.
        - RelayVlanIncrMode (number): The method used to increment VLAN IDs.
        - RelayVlanIncrement (number): The vlan increment to use for relay interfaces.
        - RenewTimer (number): The used-defined lease renewal timer.The value is estimated in seconds and will override the lease renewaltimer if it is not zero and is smaller than server-defined value.
        - Suboption6AddressSubnet (number): The network mask used for all suboption6 addresses.
        - Suboption6FirstAddress (str): We only allow suboption6 to store the IP address of a host to which replies from the DHCP server should be sent.
        - UseRapidCommit (bool): Enables DHCP clients to negotiate leases with rapid commit.
        - UseRelayAgent (bool): Activates DHCP Relay Agent Emulation.Use this if the DHCP server is located in a different network.
        - UseTrustedNetworkElement (bool): Simulate trusted network elements on the port instead of relays - that is, the packets look like normal DHCP packets, but have the relay options added (in case the circuit and Remote ID are set). This makes the remote/circuit id fields available for edit.
        - UseVendorClassId (bool): Enables use of the Vendor Class Identifier configured in the field below.
        - VendorClassId (str): This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ClientOptionSet=None,
        Count=None,
        Dhcp4Broadcast=None,
        Dhcp4ParamRequestList=None,
        Dhcp4ServerAddress=None,
        Dhcp4UseFirstServer=None,
        Dhcp6DuidEnterpriseId=None,
        Dhcp6DuidType=None,
        Dhcp6DuidVendorId=None,
        Dhcp6DuidVendorIdIncrement=None,
        Dhcp6IaId=None,
        Dhcp6IaIdIncrement=None,
        Dhcp6IaT1=None,
        Dhcp6IaT2=None,
        Dhcp6IaType=None,
        Dhcp6MasterRange=None,
        Dhcp6ParamRequestList=None,
        Enabled=None,
        IpType=None,
        Name=None,
        ObjectId=None,
        Relay6HostsPerOptInterfaceId=None,
        Relay6OptInterfaceId=None,
        Relay6UseOptInterfaceId=None,
        RelayAddressIncrement=None,
        RelayCircuitId=None,
        RelayCount=None,
        RelayDestination=None,
        RelayFirstAddress=None,
        RelayFirstVlanId=None,
        RelayGateway=None,
        RelayHostsPerCircuitId=None,
        RelayHostsPerRemoteId=None,
        RelayOptionSet=None,
        RelayOverrideVlanSettings=None,
        RelayRemoteId=None,
        RelaySubnet=None,
        RelayUseCircuitId=None,
        RelayUseRemoteId=None,
        RelayUseSuboption6=None,
        RelayVlanCount=None,
        RelayVlanIncrMode=None,
        RelayVlanIncrement=None,
        RenewTimer=None,
        Suboption6AddressSubnet=None,
        Suboption6FirstAddress=None,
        UseRapidCommit=None,
        UseRelayAgent=None,
        UseTrustedNetworkElement=None,
        UseVendorClassId=None,
        VendorClassId=None,
    ):
        # type: (str, int, bool, str, str, bool, int, str, int, int, int, int, int, int, str, str, str, bool, str, str, str, int, str, bool, str, str, int, str, str, int, str, int, int, str, bool, str, int, bool, bool, bool, int, int, int, int, int, str, bool, bool, bool, bool, str) -> DhcpRange
        """Finds and retrieves dhcpRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpRange resources from the server.

        Args
        ----
        - ClientOptionSet (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/dhcpGlobals/dhcpOptionSet)): The DHCP client options associated with this range.
        - Count (number): The number of DHCP clients to be created by this range.
        - Dhcp4Broadcast (bool): If enabled, ask the server or relay agent to use the broadcast IP address in the replies.
        - Dhcp4ParamRequestList (str): The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
        - Dhcp4ServerAddress (str): The address of the DHCP server from which the subnet will accept IP addresses.
        - Dhcp4UseFirstServer (bool): If enabled, the subnet accepts the IP addresses offered by the firstserver to respond with an offer of IP addresses.
        - Dhcp6DuidEnterpriseId (number): The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.
        - Dhcp6DuidType (str): DHCP Unique Identifier Type.
        - Dhcp6DuidVendorId (number): The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.
        - Dhcp6DuidVendorIdIncrement (number): The value by which the VENDOR-ID is incremented for each DHCP client.
        - Dhcp6IaId (number): The identity association unique ID for this range.This ID is incremented automaticaly for each DHCP client.
        - Dhcp6IaIdIncrement (number): The value by which the IA-ID is incremented for each DHCP client.
        - Dhcp6IaT1 (number): The suggested time at which the client contacts the server from whichthe addresses were obtained to extend the lifetimes of the addresses assigned.
        - Dhcp6IaT2 (number): The suggested time at which the client contacts any available serverto extend the lifetimes of the addresses assigned.
        - Dhcp6IaType (str): Identity Association Type.
        - Dhcp6MasterRange (str(None | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range/dhcpRange)): The DHCP-PD range whose negotiated prefix will be used by this range to configure its addresses.
        - Dhcp6ParamRequestList (str): The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): Defines the version of IP address style to be used for describing the range.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - Relay6HostsPerOptInterfaceId (number): Number of consecutive hosts with the same interfaceId option.
        - Relay6OptInterfaceId (str): This option is added by relay agents that terminate switched or permanent circuitsand have mechanisms to identify the remote host end of the circuit (see RFC3315, section 22.18).The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].
        - Relay6UseOptInterfaceId (bool): Select to add INTERFACE-ID option to outgoing messages.
        - RelayAddressIncrement (str): The value by which to increment the IP address for each relay agent.
        - RelayCircuitId (str): This option is added by relay agents that terminate switched or permanent circuits.The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].
        - RelayCount (number): The number of relay agents to use in this range.
        - RelayDestination (str): The address to which the requests from DHCP clients are be forwarded.
        - RelayFirstAddress (str): The IP address used by first DHCP Relay Agent.
        - RelayFirstVlanId (number): The first (outer) vlan id to allocate to relay agent interfaces.
        - RelayGateway (str): The gateway address used for all relay agents.
        - RelayHostsPerCircuitId (number): Number of consecutive hosts with the same Circuit ID.
        - RelayHostsPerRemoteId (number): Number of consecutive hosts with the same Remote ID.
        - RelayOptionSet (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/dhcpGlobals/dhcpOptionSet)): The DHCP relay options associated with this range.
        - RelayOverrideVlanSettings (bool): If true then we enable overriding of VLAN settings through relayFirstVlanId, relayVlanCount and relayVlanIncrement.
        - RelayRemoteId (str): This option is added by relay agents that terminate switched or permanent circuitsand have mechanisms to identify the remote host end of the circuit.The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].
        - RelaySubnet (number): The network mask used for all relay agents.
        - RelayUseCircuitId (bool): Select to add CIRCUIT-ID option to outgoing messages.
        - RelayUseRemoteId (bool): Select to add REMOTE-ID option to outgoing messages.
        - RelayUseSuboption6 (bool): If true then relays will add relay suboption6 (RFC3993) to the DHCP packages they send to DHCP servers.
        - RelayVlanCount (number): The number of different vlan ids to use.
        - RelayVlanIncrMode (number): The method used to increment VLAN IDs.
        - RelayVlanIncrement (number): The vlan increment to use for relay interfaces.
        - RenewTimer (number): The used-defined lease renewal timer.The value is estimated in seconds and will override the lease renewaltimer if it is not zero and is smaller than server-defined value.
        - Suboption6AddressSubnet (number): The network mask used for all suboption6 addresses.
        - Suboption6FirstAddress (str): We only allow suboption6 to store the IP address of a host to which replies from the DHCP server should be sent.
        - UseRapidCommit (bool): Enables DHCP clients to negotiate leases with rapid commit.
        - UseRelayAgent (bool): Activates DHCP Relay Agent Emulation.Use this if the DHCP server is located in a different network.
        - UseTrustedNetworkElement (bool): Simulate trusted network elements on the port instead of relays - that is, the packets look like normal DHCP packets, but have the relay options added (in case the circuit and Remote ID are set). This makes the remote/circuit id fields available for edit.
        - UseVendorClassId (bool): Enables use of the Vendor Class Identifier configured in the field below.
        - VendorClassId (str): This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.

        Returns
        -------
        - self: This instance with matching dhcpRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpRange resources from the server available through an iterator or index

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
