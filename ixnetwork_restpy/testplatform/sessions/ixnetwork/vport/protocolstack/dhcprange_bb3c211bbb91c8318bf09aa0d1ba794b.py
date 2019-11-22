# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DhcpRange(Base):
    """Manages a range of IP addresses that are configured using DHCP protocol.
    The DhcpRange class encapsulates a required dhcpRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpRange'

    def __init__(self, parent):
        super(DhcpRange, self).__init__(parent)

    @property
    def VlanIdInfo(self):
        """An instance of the VlanIdInfo class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanidinfo_ea25450d9cdaa58681e8494173179d80.VlanIdInfo)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanidinfo_ea25450d9cdaa58681e8494173179d80 import VlanIdInfo
        return VlanIdInfo(self)

    @property
    def ClientOptionSet(self):
        """The DHCP client options associated with this range.

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=dhcpOptionSet)
        """
        return self._get_attribute('clientOptionSet')
    @ClientOptionSet.setter
    def ClientOptionSet(self, value):
        self._set_attribute('clientOptionSet', value)

    @property
    def Count(self):
        """The number of DHCP clients to be created by this range.

        Returns:
            number
        """
        return self._get_attribute('count')
    @Count.setter
    def Count(self, value):
        self._set_attribute('count', value)

    @property
    def Dhcp4Broadcast(self):
        """If enabled, ask the server or relay agent to use the broadcast IP address in the replies.

        Returns:
            bool
        """
        return self._get_attribute('dhcp4Broadcast')
    @Dhcp4Broadcast.setter
    def Dhcp4Broadcast(self, value):
        self._set_attribute('dhcp4Broadcast', value)

    @property
    def Dhcp4ParamRequestList(self):
        """The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.

        Returns:
            str
        """
        return self._get_attribute('dhcp4ParamRequestList')
    @Dhcp4ParamRequestList.setter
    def Dhcp4ParamRequestList(self, value):
        self._set_attribute('dhcp4ParamRequestList', value)

    @property
    def Dhcp4ServerAddress(self):
        """The address of the DHCP server from which the subnet will accept IP addresses.

        Returns:
            str
        """
        return self._get_attribute('dhcp4ServerAddress')
    @Dhcp4ServerAddress.setter
    def Dhcp4ServerAddress(self, value):
        self._set_attribute('dhcp4ServerAddress', value)

    @property
    def Dhcp4UseFirstServer(self):
        """If enabled, the subnet accepts the IP addresses offered by the firstserver to respond with an offer of IP addresses.

        Returns:
            bool
        """
        return self._get_attribute('dhcp4UseFirstServer')
    @Dhcp4UseFirstServer.setter
    def Dhcp4UseFirstServer(self, value):
        self._set_attribute('dhcp4UseFirstServer', value)

    @property
    def Dhcp6DuidEnterpriseId(self):
        """The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.

        Returns:
            number
        """
        return self._get_attribute('dhcp6DuidEnterpriseId')
    @Dhcp6DuidEnterpriseId.setter
    def Dhcp6DuidEnterpriseId(self, value):
        self._set_attribute('dhcp6DuidEnterpriseId', value)

    @property
    def Dhcp6DuidType(self):
        """DHCP Unique Identifier Type.

        Returns:
            str
        """
        return self._get_attribute('dhcp6DuidType')
    @Dhcp6DuidType.setter
    def Dhcp6DuidType(self, value):
        self._set_attribute('dhcp6DuidType', value)

    @property
    def Dhcp6DuidVendorId(self):
        """The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.

        Returns:
            number
        """
        return self._get_attribute('dhcp6DuidVendorId')
    @Dhcp6DuidVendorId.setter
    def Dhcp6DuidVendorId(self, value):
        self._set_attribute('dhcp6DuidVendorId', value)

    @property
    def Dhcp6DuidVendorIdIncrement(self):
        """The value by which the VENDOR-ID is incremented for each DHCP client.

        Returns:
            number
        """
        return self._get_attribute('dhcp6DuidVendorIdIncrement')
    @Dhcp6DuidVendorIdIncrement.setter
    def Dhcp6DuidVendorIdIncrement(self, value):
        self._set_attribute('dhcp6DuidVendorIdIncrement', value)

    @property
    def Dhcp6IaId(self):
        """The identity association unique ID for this range.This ID is incremented automaticaly for each DHCP client.

        Returns:
            number
        """
        return self._get_attribute('dhcp6IaId')
    @Dhcp6IaId.setter
    def Dhcp6IaId(self, value):
        self._set_attribute('dhcp6IaId', value)

    @property
    def Dhcp6IaIdIncrement(self):
        """The value by which the IA-ID is incremented for each DHCP client.

        Returns:
            number
        """
        return self._get_attribute('dhcp6IaIdIncrement')
    @Dhcp6IaIdIncrement.setter
    def Dhcp6IaIdIncrement(self, value):
        self._set_attribute('dhcp6IaIdIncrement', value)

    @property
    def Dhcp6IaT1(self):
        """The suggested time at which the client contacts the server from whichthe addresses were obtained to extend the lifetimes of the addresses assigned.

        Returns:
            number
        """
        return self._get_attribute('dhcp6IaT1')
    @Dhcp6IaT1.setter
    def Dhcp6IaT1(self, value):
        self._set_attribute('dhcp6IaT1', value)

    @property
    def Dhcp6IaT2(self):
        """The suggested time at which the client contacts any available serverto extend the lifetimes of the addresses assigned.

        Returns:
            number
        """
        return self._get_attribute('dhcp6IaT2')
    @Dhcp6IaT2.setter
    def Dhcp6IaT2(self, value):
        self._set_attribute('dhcp6IaT2', value)

    @property
    def Dhcp6IaType(self):
        """Identity Association Type.

        Returns:
            str
        """
        return self._get_attribute('dhcp6IaType')
    @Dhcp6IaType.setter
    def Dhcp6IaType(self, value):
        self._set_attribute('dhcp6IaType', value)

    @property
    def Dhcp6MasterRange(self):
        """The DHCP-PD range whose negotiated prefix will be used by this range to configure its addresses.

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=dhcpRange)
        """
        return self._get_attribute('dhcp6MasterRange')
    @Dhcp6MasterRange.setter
    def Dhcp6MasterRange(self, value):
        self._set_attribute('dhcp6MasterRange', value)

    @property
    def Dhcp6ParamRequestList(self):
        """The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.

        Returns:
            str
        """
        return self._get_attribute('dhcp6ParamRequestList')
    @Dhcp6ParamRequestList.setter
    def Dhcp6ParamRequestList(self, value):
        self._set_attribute('dhcp6ParamRequestList', value)

    @property
    def Enabled(self):
        """Disabled ranges won't be configured nor validated.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def IpType(self):
        """Defines the version of IP address style to be used for describing the range.

        Returns:
            str
        """
        return self._get_attribute('ipType')
    @IpType.setter
    def IpType(self, value):
        self._set_attribute('ipType', value)

    @property
    def Name(self):
        """Name of range

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def Relay6HostsPerOptInterfaceId(self):
        """Number of consecutive hosts with the same interfaceId option.

        Returns:
            number
        """
        return self._get_attribute('relay6HostsPerOptInterfaceId')
    @Relay6HostsPerOptInterfaceId.setter
    def Relay6HostsPerOptInterfaceId(self, value):
        self._set_attribute('relay6HostsPerOptInterfaceId', value)

    @property
    def Relay6OptInterfaceId(self):
        """This option is added by relay agents that terminate switched or permanent circuitsand have mechanisms to identify the remote host end of the circuit (see RFC3315, section 22.18).The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].

        Returns:
            str
        """
        return self._get_attribute('relay6OptInterfaceId')
    @Relay6OptInterfaceId.setter
    def Relay6OptInterfaceId(self, value):
        self._set_attribute('relay6OptInterfaceId', value)

    @property
    def Relay6UseOptInterfaceId(self):
        """Select to add INTERFACE-ID option to outgoing messages.

        Returns:
            bool
        """
        return self._get_attribute('relay6UseOptInterfaceId')
    @Relay6UseOptInterfaceId.setter
    def Relay6UseOptInterfaceId(self, value):
        self._set_attribute('relay6UseOptInterfaceId', value)

    @property
    def RelayAddressIncrement(self):
        """The value by which to increment the IP address for each relay agent.

        Returns:
            str
        """
        return self._get_attribute('relayAddressIncrement')
    @RelayAddressIncrement.setter
    def RelayAddressIncrement(self, value):
        self._set_attribute('relayAddressIncrement', value)

    @property
    def RelayCircuitId(self):
        """This option is added by relay agents that terminate switched or permanent circuits.The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].

        Returns:
            str
        """
        return self._get_attribute('relayCircuitId')
    @RelayCircuitId.setter
    def RelayCircuitId(self, value):
        self._set_attribute('relayCircuitId', value)

    @property
    def RelayCount(self):
        """The number of relay agents to use in this range.

        Returns:
            number
        """
        return self._get_attribute('relayCount')
    @RelayCount.setter
    def RelayCount(self, value):
        self._set_attribute('relayCount', value)

    @property
    def RelayDestination(self):
        """The address to which the requests from DHCP clients are be forwarded.

        Returns:
            str
        """
        return self._get_attribute('relayDestination')
    @RelayDestination.setter
    def RelayDestination(self, value):
        self._set_attribute('relayDestination', value)

    @property
    def RelayFirstAddress(self):
        """The IP address used by first DHCP Relay Agent.

        Returns:
            str
        """
        return self._get_attribute('relayFirstAddress')
    @RelayFirstAddress.setter
    def RelayFirstAddress(self, value):
        self._set_attribute('relayFirstAddress', value)

    @property
    def RelayFirstVlanId(self):
        """The first (outer) vlan id to allocate to relay agent interfaces.

        Returns:
            number
        """
        return self._get_attribute('relayFirstVlanId')
    @RelayFirstVlanId.setter
    def RelayFirstVlanId(self, value):
        self._set_attribute('relayFirstVlanId', value)

    @property
    def RelayGateway(self):
        """The gateway address used for all relay agents.

        Returns:
            str
        """
        return self._get_attribute('relayGateway')
    @RelayGateway.setter
    def RelayGateway(self, value):
        self._set_attribute('relayGateway', value)

    @property
    def RelayHostsPerCircuitId(self):
        """Number of consecutive hosts with the same Circuit ID.

        Returns:
            number
        """
        return self._get_attribute('relayHostsPerCircuitId')
    @RelayHostsPerCircuitId.setter
    def RelayHostsPerCircuitId(self, value):
        self._set_attribute('relayHostsPerCircuitId', value)

    @property
    def RelayHostsPerRemoteId(self):
        """Number of consecutive hosts with the same Remote ID.

        Returns:
            number
        """
        return self._get_attribute('relayHostsPerRemoteId')
    @RelayHostsPerRemoteId.setter
    def RelayHostsPerRemoteId(self, value):
        self._set_attribute('relayHostsPerRemoteId', value)

    @property
    def RelayOptionSet(self):
        """The DHCP relay options associated with this range.

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=dhcpOptionSet)
        """
        return self._get_attribute('relayOptionSet')
    @RelayOptionSet.setter
    def RelayOptionSet(self, value):
        self._set_attribute('relayOptionSet', value)

    @property
    def RelayOverrideVlanSettings(self):
        """If true then we enable overriding of VLAN settings through relayFirstVlanId, relayVlanCount and relayVlanIncrement.

        Returns:
            bool
        """
        return self._get_attribute('relayOverrideVlanSettings')
    @RelayOverrideVlanSettings.setter
    def RelayOverrideVlanSettings(self, value):
        self._set_attribute('relayOverrideVlanSettings', value)

    @property
    def RelayRemoteId(self):
        """This option is added by relay agents that terminate switched or permanent circuitsand have mechanisms to identify the remote host end of the circuit.The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].

        Returns:
            str
        """
        return self._get_attribute('relayRemoteId')
    @RelayRemoteId.setter
    def RelayRemoteId(self, value):
        self._set_attribute('relayRemoteId', value)

    @property
    def RelaySubnet(self):
        """The network mask used for all relay agents.

        Returns:
            number
        """
        return self._get_attribute('relaySubnet')
    @RelaySubnet.setter
    def RelaySubnet(self, value):
        self._set_attribute('relaySubnet', value)

    @property
    def RelayUseCircuitId(self):
        """Select to add CIRCUIT-ID option to outgoing messages.

        Returns:
            bool
        """
        return self._get_attribute('relayUseCircuitId')
    @RelayUseCircuitId.setter
    def RelayUseCircuitId(self, value):
        self._set_attribute('relayUseCircuitId', value)

    @property
    def RelayUseRemoteId(self):
        """Select to add REMOTE-ID option to outgoing messages.

        Returns:
            bool
        """
        return self._get_attribute('relayUseRemoteId')
    @RelayUseRemoteId.setter
    def RelayUseRemoteId(self, value):
        self._set_attribute('relayUseRemoteId', value)

    @property
    def RelayUseSuboption6(self):
        """If true then relays will add relay suboption6 (RFC3993) to the DHCP packages they send to DHCP servers.

        Returns:
            bool
        """
        return self._get_attribute('relayUseSuboption6')
    @RelayUseSuboption6.setter
    def RelayUseSuboption6(self, value):
        self._set_attribute('relayUseSuboption6', value)

    @property
    def RelayVlanCount(self):
        """The number of different vlan ids to use.

        Returns:
            number
        """
        return self._get_attribute('relayVlanCount')
    @RelayVlanCount.setter
    def RelayVlanCount(self, value):
        self._set_attribute('relayVlanCount', value)

    @property
    def RelayVlanIncrMode(self):
        """The method used to increment VLAN IDs.

        Returns:
            number
        """
        return self._get_attribute('relayVlanIncrMode')
    @RelayVlanIncrMode.setter
    def RelayVlanIncrMode(self, value):
        self._set_attribute('relayVlanIncrMode', value)

    @property
    def RelayVlanIncrement(self):
        """The vlan increment to use for relay interfaces.

        Returns:
            number
        """
        return self._get_attribute('relayVlanIncrement')
    @RelayVlanIncrement.setter
    def RelayVlanIncrement(self, value):
        self._set_attribute('relayVlanIncrement', value)

    @property
    def RenewTimer(self):
        """The used-defined lease renewal timer.The value is estimated in seconds and will override the lease renewaltimer if it is not zero and is smaller than server-defined value.

        Returns:
            number
        """
        return self._get_attribute('renewTimer')
    @RenewTimer.setter
    def RenewTimer(self, value):
        self._set_attribute('renewTimer', value)

    @property
    def Suboption6AddressSubnet(self):
        """The network mask used for all suboption6 addresses.

        Returns:
            number
        """
        return self._get_attribute('suboption6AddressSubnet')
    @Suboption6AddressSubnet.setter
    def Suboption6AddressSubnet(self, value):
        self._set_attribute('suboption6AddressSubnet', value)

    @property
    def Suboption6FirstAddress(self):
        """We only allow suboption6 to store the IP address of a host to which replies from the DHCP server should be sent.

        Returns:
            str
        """
        return self._get_attribute('suboption6FirstAddress')
    @Suboption6FirstAddress.setter
    def Suboption6FirstAddress(self, value):
        self._set_attribute('suboption6FirstAddress', value)

    @property
    def UseRapidCommit(self):
        """Enables DHCP clients to negotiate leases with rapid commit.

        Returns:
            bool
        """
        return self._get_attribute('useRapidCommit')
    @UseRapidCommit.setter
    def UseRapidCommit(self, value):
        self._set_attribute('useRapidCommit', value)

    @property
    def UseRelayAgent(self):
        """Activates DHCP Relay Agent Emulation.Use this if the DHCP server is located in a different network.

        Returns:
            bool
        """
        return self._get_attribute('useRelayAgent')
    @UseRelayAgent.setter
    def UseRelayAgent(self, value):
        self._set_attribute('useRelayAgent', value)

    @property
    def UseTrustedNetworkElement(self):
        """Simulate trusted network elements on the port instead of relays - that is, the packets look like normal DHCP packets, but have the relay options added (in case the circuit and Remote ID are set). This makes the remote/circuit id fields available for edit.

        Returns:
            bool
        """
        return self._get_attribute('useTrustedNetworkElement')
    @UseTrustedNetworkElement.setter
    def UseTrustedNetworkElement(self, value):
        self._set_attribute('useTrustedNetworkElement', value)

    @property
    def UseVendorClassId(self):
        """Enables use of the Vendor Class Identifier configured in the field below.

        Returns:
            bool
        """
        return self._get_attribute('useVendorClassId')
    @UseVendorClassId.setter
    def UseVendorClassId(self, value):
        self._set_attribute('useVendorClassId', value)

    @property
    def VendorClassId(self):
        """This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.

        Returns:
            str
        """
        return self._get_attribute('vendorClassId')
    @VendorClassId.setter
    def VendorClassId(self, value):
        self._set_attribute('vendorClassId', value)

    def update(self, ClientOptionSet=None, Count=None, Dhcp4Broadcast=None, Dhcp4ParamRequestList=None, Dhcp4ServerAddress=None, Dhcp4UseFirstServer=None, Dhcp6DuidEnterpriseId=None, Dhcp6DuidType=None, Dhcp6DuidVendorId=None, Dhcp6DuidVendorIdIncrement=None, Dhcp6IaId=None, Dhcp6IaIdIncrement=None, Dhcp6IaT1=None, Dhcp6IaT2=None, Dhcp6IaType=None, Dhcp6MasterRange=None, Dhcp6ParamRequestList=None, Enabled=None, IpType=None, Name=None, Relay6HostsPerOptInterfaceId=None, Relay6OptInterfaceId=None, Relay6UseOptInterfaceId=None, RelayAddressIncrement=None, RelayCircuitId=None, RelayCount=None, RelayDestination=None, RelayFirstAddress=None, RelayFirstVlanId=None, RelayGateway=None, RelayHostsPerCircuitId=None, RelayHostsPerRemoteId=None, RelayOptionSet=None, RelayOverrideVlanSettings=None, RelayRemoteId=None, RelaySubnet=None, RelayUseCircuitId=None, RelayUseRemoteId=None, RelayUseSuboption6=None, RelayVlanCount=None, RelayVlanIncrMode=None, RelayVlanIncrement=None, RenewTimer=None, Suboption6AddressSubnet=None, Suboption6FirstAddress=None, UseRapidCommit=None, UseRelayAgent=None, UseTrustedNetworkElement=None, UseVendorClassId=None, VendorClassId=None):
        """Updates a child instance of dhcpRange on the server.

        Args:
            ClientOptionSet (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=dhcpOptionSet)): The DHCP client options associated with this range.
            Count (number): The number of DHCP clients to be created by this range.
            Dhcp4Broadcast (bool): If enabled, ask the server or relay agent to use the broadcast IP address in the replies.
            Dhcp4ParamRequestList (str): The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
            Dhcp4ServerAddress (str): The address of the DHCP server from which the subnet will accept IP addresses.
            Dhcp4UseFirstServer (bool): If enabled, the subnet accepts the IP addresses offered by the firstserver to respond with an offer of IP addresses.
            Dhcp6DuidEnterpriseId (number): The enterprise-number is the vendor's registeredPrivate Enterprise Number as maintained by IANA.
            Dhcp6DuidType (str): DHCP Unique Identifier Type.
            Dhcp6DuidVendorId (number): The vendor-assigned unique ID for this range.This ID is incremented automaticaly for each DHCP client.
            Dhcp6DuidVendorIdIncrement (number): The value by which the VENDOR-ID is incremented for each DHCP client.
            Dhcp6IaId (number): The identity association unique ID for this range.This ID is incremented automaticaly for each DHCP client.
            Dhcp6IaIdIncrement (number): The value by which the IA-ID is incremented for each DHCP client.
            Dhcp6IaT1 (number): The suggested time at which the client contacts the server from whichthe addresses were obtained to extend the lifetimes of the addresses assigned.
            Dhcp6IaT2 (number): The suggested time at which the client contacts any available serverto extend the lifetimes of the addresses assigned.
            Dhcp6IaType (str): Identity Association Type.
            Dhcp6MasterRange (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=dhcpRange)): The DHCP-PD range whose negotiated prefix will be used by this range to configure its addresses.
            Dhcp6ParamRequestList (str): The Option Request option is used to identify a list of optionsin a message between a client and a server.Multiple options can be specified in a semicolon separated list.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IpType (str): Defines the version of IP address style to be used for describing the range.
            Name (str): Name of range
            Relay6HostsPerOptInterfaceId (number): Number of consecutive hosts with the same interfaceId option.
            Relay6OptInterfaceId (str): This option is added by relay agents that terminate switched or permanent circuitsand have mechanisms to identify the remote host end of the circuit (see RFC3315, section 22.18).The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].
            Relay6UseOptInterfaceId (bool): Select to add INTERFACE-ID option to outgoing messages.
            RelayAddressIncrement (str): The value by which to increment the IP address for each relay agent.
            RelayCircuitId (str): This option is added by relay agents that terminate switched or permanent circuits.The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].
            RelayCount (number): The number of relay agents to use in this range.
            RelayDestination (str): The address to which the requests from DHCP clients are be forwarded.
            RelayFirstAddress (str): The IP address used by first DHCP Relay Agent.
            RelayFirstVlanId (number): The first (outer) vlan id to allocate to relay agent interfaces.
            RelayGateway (str): The gateway address used for all relay agents.
            RelayHostsPerCircuitId (number): Number of consecutive hosts with the same Circuit ID.
            RelayHostsPerRemoteId (number): Number of consecutive hosts with the same Remote ID.
            RelayOptionSet (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=dhcpOptionSet)): The DHCP relay options associated with this range.
            RelayOverrideVlanSettings (bool): If true then we enable overriding of VLAN settings through relayFirstVlanId, relayVlanCount and relayVlanIncrement.
            RelayRemoteId (str): This option is added by relay agents that terminate switched or permanent circuitsand have mechanisms to identify the remote host end of the circuit.The string can contain a sequence of values represented in form of [StartValue-EndValue].Examples: Decimals [11-22], Hexadecimals [0x00-0xFF], Characters [AA-ZZ].
            RelaySubnet (number): The network mask used for all relay agents.
            RelayUseCircuitId (bool): Select to add CIRCUIT-ID option to outgoing messages.
            RelayUseRemoteId (bool): Select to add REMOTE-ID option to outgoing messages.
            RelayUseSuboption6 (bool): If true then relays will add relay suboption6 (RFC3993) to the DHCP packages they send to DHCP servers.
            RelayVlanCount (number): The number of different vlan ids to use.
            RelayVlanIncrMode (number): The method used to increment VLAN IDs.
            RelayVlanIncrement (number): The vlan increment to use for relay interfaces.
            RenewTimer (number): The used-defined lease renewal timer.The value is estimated in seconds and will override the lease renewaltimer if it is not zero and is smaller than server-defined value.
            Suboption6AddressSubnet (number): The network mask used for all suboption6 addresses.
            Suboption6FirstAddress (str): We only allow suboption6 to store the IP address of a host to which replies from the DHCP server should be sent.
            UseRapidCommit (bool): Enables DHCP clients to negotiate leases with rapid commit.
            UseRelayAgent (bool): Activates DHCP Relay Agent Emulation.Use this if the DHCP server is located in a different network.
            UseTrustedNetworkElement (bool): Simulate trusted network elements on the port instead of relays - that is, the packets look like normal DHCP packets, but have the relay options added (in case the circuit and Remote ID are set). This makes the remote/circuit id fields available for edit.
            UseVendorClassId (bool): Enables use of the Vendor Class Identifier configured in the field below.
            VendorClassId (str): This option is used by a client to identify the vendor thatmanufactured the hardware on which the client is running.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
