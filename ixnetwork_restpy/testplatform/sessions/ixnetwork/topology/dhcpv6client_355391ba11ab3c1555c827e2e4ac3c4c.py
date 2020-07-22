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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Dhcpv6client(Base):
    """DHCPv6 Client protocol.
    The Dhcpv6client class encapsulates a list of dhcpv6client resources that are managed by the user.
    A list of resources can be retrieved from the server using the Dhcpv6client.find() method.
    The list can be managed by using the Dhcpv6client.add() and Dhcpv6client.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpv6client'
    _SDM_ATT_MAP = {
        'ComputedIapdAddresses': 'computedIapdAddresses',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'CustomLinkLocalAddress': 'customLinkLocalAddress',
        'DescriptiveName': 'descriptiveName',
        'Dhcp6DuidEnterpriseId': 'dhcp6DuidEnterpriseId',
        'Dhcp6DuidType': 'dhcp6DuidType',
        'Dhcp6DuidVendorId': 'dhcp6DuidVendorId',
        'Dhcp6GatewayAddress': 'dhcp6GatewayAddress',
        'Dhcp6GatewayMac': 'dhcp6GatewayMac',
        'Dhcp6IANACount': 'dhcp6IANACount',
        'Dhcp6IAPDCount': 'dhcp6IAPDCount',
        'Dhcp6IaId': 'dhcp6IaId',
        'Dhcp6IaIdInc': 'dhcp6IaIdInc',
        'Dhcp6IaT1': 'dhcp6IaT1',
        'Dhcp6IaT2': 'dhcp6IaT2',
        'Dhcp6IaType': 'dhcp6IaType',
        'Dhcp6UsePDGlobalAddress': 'dhcp6UsePDGlobalAddress',
        'DiscoveredAddresses': 'discoveredAddresses',
        'DiscoveredGateways': 'discoveredGateways',
        'DiscoveredPrefix': 'discoveredPrefix',
        'DiscoveredPrefixLength': 'discoveredPrefixLength',
        'EnableStateless': 'enableStateless',
        'Errors': 'errors',
        'MaxNoPerClient': 'maxNoPerClient',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NoOfAddresses': 'noOfAddresses',
        'NoOfPrefixes': 'noOfPrefixes',
        'RenewTimer': 'renewTimer',
        'SessionInfo': 'sessionInfo',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'UseCustomLinkLocalAddress': 'useCustomLinkLocalAddress',
        'UseRapidCommit': 'useRapidCommit',
    }

    def __init__(self, parent):
        super(Dhcpv6client, self).__init__(parent)

    @property
    def Bfdv6Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface_b9a91920db1b70c8c6410d2de0b438d3.Bfdv6Interface): An instance of the Bfdv6Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface_b9a91920db1b70c8c6410d2de0b438d3 import Bfdv6Interface
        return Bfdv6Interface(self)

    @property
    def BgpIpv6Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer_d4ac277d9da759fd5a152b8e6eb0ab20.BgpIpv6Peer): An instance of the BgpIpv6Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer_d4ac277d9da759fd5a152b8e6eb0ab20 import BgpIpv6Peer
        return BgpIpv6Peer(self)

    @property
    def Dhcp6Iana(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana_1fdc932fd14b686d54038abe7dbb6f0c.Dhcp6Iana): An instance of the Dhcp6Iana class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana_1fdc932fd14b686d54038abe7dbb6f0c import Dhcp6Iana
        return Dhcp6Iana(self)._select()

    @property
    def Dhcp6Iana1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana1_afae4078d5465a41b7a0b1fa28f04ed6.Dhcp6Iana1): An instance of the Dhcp6Iana1 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana1_afae4078d5465a41b7a0b1fa28f04ed6 import Dhcp6Iana1
        return Dhcp6Iana1(self)._select()

    @property
    def Dhcp6Iana2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana2_8780d42215180f08e6e8445b53170c10.Dhcp6Iana2): An instance of the Dhcp6Iana2 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana2_8780d42215180f08e6e8445b53170c10 import Dhcp6Iana2
        return Dhcp6Iana2(self)._select()

    @property
    def Dhcp6Iana3(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana3_d9182a6f15c9c4511011e7796b6e6482.Dhcp6Iana3): An instance of the Dhcp6Iana3 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana3_d9182a6f15c9c4511011e7796b6e6482 import Dhcp6Iana3
        return Dhcp6Iana3(self)._select()

    @property
    def Dhcp6Iana4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana4_59de65e7b5806938834b0b31ab911645.Dhcp6Iana4): An instance of the Dhcp6Iana4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana4_59de65e7b5806938834b0b31ab911645 import Dhcp6Iana4
        return Dhcp6Iana4(self)._select()

    @property
    def Dhcp6Iana5(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana5_9f29804966bbe93dd53900eafa383c22.Dhcp6Iana5): An instance of the Dhcp6Iana5 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana5_9f29804966bbe93dd53900eafa383c22 import Dhcp6Iana5
        return Dhcp6Iana5(self)._select()

    @property
    def Dhcp6Iana6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana6_7939c0233bac17c3e3764bc9bc1a9571.Dhcp6Iana6): An instance of the Dhcp6Iana6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana6_7939c0233bac17c3e3764bc9bc1a9571 import Dhcp6Iana6
        return Dhcp6Iana6(self)._select()

    @property
    def Dhcp6Iana7(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana7_e0f696023e5c20916196c8d33f395cae.Dhcp6Iana7): An instance of the Dhcp6Iana7 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana7_e0f696023e5c20916196c8d33f395cae import Dhcp6Iana7
        return Dhcp6Iana7(self)._select()

    @property
    def Dhcp6Iapd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd_b6cbdab151b403cbbdb4bf99e1caf7b1.Dhcp6Iapd): An instance of the Dhcp6Iapd class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd_b6cbdab151b403cbbdb4bf99e1caf7b1 import Dhcp6Iapd
        return Dhcp6Iapd(self)._select()

    @property
    def Dhcp6Iapd1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd1_7faba276e9bd1fe8044fca79065254a7.Dhcp6Iapd1): An instance of the Dhcp6Iapd1 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd1_7faba276e9bd1fe8044fca79065254a7 import Dhcp6Iapd1
        return Dhcp6Iapd1(self)._select()

    @property
    def Dhcp6Iapd2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd2_a86dfc2bcc765583bc7cf336b264c68b.Dhcp6Iapd2): An instance of the Dhcp6Iapd2 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd2_a86dfc2bcc765583bc7cf336b264c68b import Dhcp6Iapd2
        return Dhcp6Iapd2(self)._select()

    @property
    def Dhcp6Iapd3(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd3_ba20e56748a428c3b9345cf88c1539fd.Dhcp6Iapd3): An instance of the Dhcp6Iapd3 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd3_ba20e56748a428c3b9345cf88c1539fd import Dhcp6Iapd3
        return Dhcp6Iapd3(self)._select()

    @property
    def Dhcp6Iapd4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd4_491b33d4a7b6a77105854603fd6a9004.Dhcp6Iapd4): An instance of the Dhcp6Iapd4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd4_491b33d4a7b6a77105854603fd6a9004 import Dhcp6Iapd4
        return Dhcp6Iapd4(self)._select()

    @property
    def Dhcp6Iapd5(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd5_36145a5bec4444c5107e1c59676ab3a1.Dhcp6Iapd5): An instance of the Dhcp6Iapd5 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd5_36145a5bec4444c5107e1c59676ab3a1 import Dhcp6Iapd5
        return Dhcp6Iapd5(self)._select()

    @property
    def Dhcp6Iapd6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd6_1010a4aa43f5dd9a03d6aab4c6a66a68.Dhcp6Iapd6): An instance of the Dhcp6Iapd6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd6_1010a4aa43f5dd9a03d6aab4c6a66a68 import Dhcp6Iapd6
        return Dhcp6Iapd6(self)._select()

    @property
    def Dhcp6Iapd7(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd7_156f14311910b918f77a699ecec78e79.Dhcp6Iapd7): An instance of the Dhcp6Iapd7 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd7_156f14311910b918f77a699ecec78e79 import Dhcp6Iapd7
        return Dhcp6Iapd7(self)._select()

    @property
    def Dhcp6LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6learnedinfo_096f62fbfd89979e813da06c573399d9.Dhcp6LearnedInfo): An instance of the Dhcp6LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6learnedinfo_096f62fbfd89979e813da06c573399d9 import Dhcp6LearnedInfo
        return Dhcp6LearnedInfo(self)._select()

    @property
    def MldHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost_824a1bed927138d4bb32f7d2631197a5.MldHost): An instance of the MldHost class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost_824a1bed927138d4bb32f7d2631197a5 import MldHost
        return MldHost(self)

    @property
    def MldQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier_e20671d730d138d65036e88d7cad63ac.MldQuerier): An instance of the MldQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier_e20671d730d138d65036e88d7cad63ac import MldQuerier
        return MldQuerier(self)

    @property
    def Ospfv3(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3_c029fd7cd4a9e9897b7b4e4547458751.Ospfv3): An instance of the Ospfv3 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3_c029fd7cd4a9e9897b7b4e4547458751 import Ospfv3
        return Ospfv3(self)

    @property
    def PimV6Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface_74a3aa08a315ca50732e853e3e8cdc43.PimV6Interface): An instance of the PimV6Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface_74a3aa08a315ca50732e853e3e8cdc43 import PimV6Interface
        return PimV6Interface(self)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        return Tag(self)

    @property
    def TlvProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_69db000d3ef3b060f5edc387b878736c.TlvProfile): An instance of the TlvProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_69db000d3ef3b060f5edc387b878736c import TlvProfile
        return TlvProfile(self)

    @property
    def Vxlanv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanv6_c18187deccae3db44b9e9de30ad538ec.Vxlanv6): An instance of the Vxlanv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanv6_c18187deccae3db44b9e9de30ad538ec import Vxlanv6
        return Vxlanv6(self)

    @property
    def ComputedIapdAddresses(self):
        """
        Returns
        -------
        - list(str): The computed IPv6 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ComputedIapdAddresses'])

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer used to connect to the wire
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def CustomLinkLocalAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configures the Manual Link-Local IPv6 Address for the DHCPv6 Client.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CustomLinkLocalAddress']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Dhcp6DuidEnterpriseId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The enterprise-number is the vendor's registered Private Enterprise Number as maintained by IANA.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6DuidEnterpriseId']))

    @property
    def Dhcp6DuidType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DHCP Unique Identifier Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6DuidType']))

    @property
    def Dhcp6DuidVendorId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The vendor-assigned unique ID for this range. This ID is incremented automaticaly for each DHCP client.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6DuidVendorId']))

    @property
    def Dhcp6GatewayAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configures the Manual Gateway IPv6 Address for the DHCPv6 Client.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6GatewayAddress']))

    @property
    def Dhcp6GatewayMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configures the Manual Gateway MAC corresponding to the configured Manual Gateway IP of the DHCPv6 Client session.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6GatewayMac']))

    @property
    def Dhcp6IANACount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of IANA options to be included in a negotiation. This value must be smaller than Maximum Leases per Client.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6IANACount']))

    @property
    def Dhcp6IAPDCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of IAPD options to be included in a negotiation. This value must be smaller than Maximum Leases per Client.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6IAPDCount']))

    @property
    def Dhcp6IaId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The identity association unique ID for this range.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6IaId']))

    @property
    def Dhcp6IaIdInc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Increment step for each IAID in a multiple IANA/IAPD case.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6IaIdInc']))

    @property
    def Dhcp6IaT1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The suggested time at which the client contacts the server from which the addresses were obtained to extend the lifetimes of the addresses assigned.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6IaT1']))

    @property
    def Dhcp6IaT2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The suggested time at which the client contacts any available server to extend the lifetimes of the addresses assigned.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6IaT2']))

    @property
    def Dhcp6IaType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Identity Association Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6IaType']))

    @property
    def Dhcp6UsePDGlobalAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use DHCPc6-PD global addressing.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dhcp6UsePDGlobalAddress']))

    @property
    def DiscoveredAddresses(self):
        """
        Returns
        -------
        - list(str): The discovered IPv6 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveredAddresses'])

    @property
    def DiscoveredGateways(self):
        """
        Returns
        -------
        - list(str): The discovered gateway IPv6 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveredGateways'])

    @property
    def DiscoveredPrefix(self):
        """
        Returns
        -------
        - list(str): The discovered IPv6 prefix.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveredPrefix'])

    @property
    def DiscoveredPrefixLength(self):
        """
        Returns
        -------
        - list(number): The length of the discovered IPv6 prefix.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscoveredPrefixLength'])

    @property
    def EnableStateless(self):
        """
        Returns
        -------
        - bool: Enables DHCP stateless.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableStateless'])
    @EnableStateless.setter
    def EnableStateless(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableStateless'], value)

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def MaxNoPerClient(self):
        """
        Returns
        -------
        - number: Maximum number of Addresses/Prefixes accepted by a Client in a negotiation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxNoPerClient'])
    @MaxNoPerClient.setter
    def MaxNoPerClient(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxNoPerClient'], value)

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NoOfAddresses(self):
        """
        Returns
        -------
        - list(number): Number of Negotiated Addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfAddresses'])

    @property
    def NoOfPrefixes(self):
        """
        Returns
        -------
        - list(number): Number of Negotiated Addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfPrefixes'])

    @property
    def RenewTimer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The used-defined lease renewal timer. The value is estimated in seconds and will override the lease renewal timer if it is not zero and is smaller than server-defined value.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RenewTimer']))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[duidNak | excessiveTlvs | noAddrsAvail | noAddrsBelow | none | noPrefixAvail | nsFailed | partiallyNegotiated | rebindTimeout | relayDown | renewTimeout | requestTimeout | solicitTimeout]): Logs additional information about the session state
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def StackedLayers(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StackedLayers'], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateCounts'])

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def UseCustomLinkLocalAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables users to manually set non-EUI link local addresses
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseCustomLinkLocalAddress']))

    @property
    def UseRapidCommit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables DHCP clients to negotiate leases with rapid commit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseRapidCommit']))

    def update(self, ConnectedVia=None, EnableStateless=None, MaxNoPerClient=None, Multiplier=None, Name=None, StackedLayers=None):
        """Updates dhcpv6client resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - EnableStateless (bool): Enables DHCP stateless.
        - MaxNoPerClient (number): Maximum number of Addresses/Prefixes accepted by a Client in a negotiation.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, EnableStateless=None, MaxNoPerClient=None, Multiplier=None, Name=None, StackedLayers=None):
        """Adds a new dhcpv6client resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - EnableStateless (bool): Enables DHCP stateless.
        - MaxNoPerClient (number): Maximum number of Addresses/Prefixes accepted by a Client in a negotiation.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved dhcpv6client resources using find and the newly added dhcpv6client resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dhcpv6client resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ComputedIapdAddresses=None, ConnectedVia=None, Count=None, DescriptiveName=None, DiscoveredAddresses=None, DiscoveredGateways=None, DiscoveredPrefix=None, DiscoveredPrefixLength=None, EnableStateless=None, Errors=None, MaxNoPerClient=None, Multiplier=None, Name=None, NoOfAddresses=None, NoOfPrefixes=None, SessionInfo=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves dhcpv6client resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpv6client resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpv6client resources from the server.

        Args
        ----
        - ComputedIapdAddresses (list(str)): The computed IPv6 addresses.
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - DiscoveredAddresses (list(str)): The discovered IPv6 addresses.
        - DiscoveredGateways (list(str)): The discovered gateway IPv6 addresses.
        - DiscoveredPrefix (list(str)): The discovered IPv6 prefix.
        - DiscoveredPrefixLength (list(number)): The length of the discovered IPv6 prefix.
        - EnableStateless (bool): Enables DHCP stateless.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - MaxNoPerClient (number): Maximum number of Addresses/Prefixes accepted by a Client in a negotiation.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfAddresses (list(number)): Number of Negotiated Addresses.
        - NoOfPrefixes (list(number)): Number of Negotiated Addresses.
        - SessionInfo (list(str[duidNak | excessiveTlvs | noAddrsAvail | noAddrsBelow | none | noPrefixAvail | nsFailed | partiallyNegotiated | rebindTimeout | relayDown | renewTimeout | requestTimeout | solicitTimeout])): Logs additional information about the session state
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching dhcpv6client resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpv6client data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpv6client resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, CustomLinkLocalAddress=None, Dhcp6DuidEnterpriseId=None, Dhcp6DuidType=None, Dhcp6DuidVendorId=None, Dhcp6GatewayAddress=None, Dhcp6GatewayMac=None, Dhcp6IANACount=None, Dhcp6IAPDCount=None, Dhcp6IaId=None, Dhcp6IaIdInc=None, Dhcp6IaT1=None, Dhcp6IaT2=None, Dhcp6IaType=None, Dhcp6UsePDGlobalAddress=None, RenewTimer=None, UseCustomLinkLocalAddress=None, UseRapidCommit=None):
        """Base class infrastructure that gets a list of dhcpv6client device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - CustomLinkLocalAddress (str): optional regex of customLinkLocalAddress
        - Dhcp6DuidEnterpriseId (str): optional regex of dhcp6DuidEnterpriseId
        - Dhcp6DuidType (str): optional regex of dhcp6DuidType
        - Dhcp6DuidVendorId (str): optional regex of dhcp6DuidVendorId
        - Dhcp6GatewayAddress (str): optional regex of dhcp6GatewayAddress
        - Dhcp6GatewayMac (str): optional regex of dhcp6GatewayMac
        - Dhcp6IANACount (str): optional regex of dhcp6IANACount
        - Dhcp6IAPDCount (str): optional regex of dhcp6IAPDCount
        - Dhcp6IaId (str): optional regex of dhcp6IaId
        - Dhcp6IaIdInc (str): optional regex of dhcp6IaIdInc
        - Dhcp6IaT1 (str): optional regex of dhcp6IaT1
        - Dhcp6IaT2 (str): optional regex of dhcp6IaT2
        - Dhcp6IaType (str): optional regex of dhcp6IaType
        - Dhcp6UsePDGlobalAddress (str): optional regex of dhcp6UsePDGlobalAddress
        - RenewTimer (str): optional regex of renewTimer
        - UseCustomLinkLocalAddress (str): optional regex of useCustomLinkLocalAddress
        - UseRapidCommit (str): optional regex of useRapidCommit

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self, *args, **kwargs):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        abort(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def Rebind(self, *args, **kwargs):
        """Executes the rebind operation on the server.

        Rebind selected DHCPv6 items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        rebind(SessionIndices=list)
        ---------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        rebind(SessionIndices=string)
        -----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('rebind', payload=payload, response_object=None)

    def Renew(self, *args, **kwargs):
        """Executes the renew operation on the server.

        Renew selected DHCPv6 items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        renew(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        renew(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('renew', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        restartDown(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def SendPing(self, *args, **kwargs):
        """Executes the sendPing operation on the server.

        Send ping for selected DHCPv6 items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPing(DestIP=string)list
        ---------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing(DestIP=string, SessionIndices=list)list
        ------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing(SessionIndices=string, DestIP=string)list
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a destIP of type kString
        - DestIP (str): This parameter requires a string of session numbers 1-4;6;7-12
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendPing', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
