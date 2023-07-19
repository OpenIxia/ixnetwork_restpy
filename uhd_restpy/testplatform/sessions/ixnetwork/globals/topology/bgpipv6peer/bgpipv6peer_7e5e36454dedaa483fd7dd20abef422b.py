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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class BgpIpv6Peer(Base):
    """BGP Port level Configuration
    The BgpIpv6Peer class encapsulates a required bgpIpv6Peer resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpIpv6Peer'
    _SDM_ATT_MAP = {
        'BIERTunnelType': 'BIERTunnelType',
        'LLGRCapabilityCode': 'LLGRCapabilityCode',
        'BgpConfMemType': 'bgpConfMemType',
        'BgpRouterId': 'bgpRouterId',
        'BindingType': 'bindingType',
        'ColorType': 'colorType',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DisableReceivedUpdateValidation': 'disableReceivedUpdateValidation',
        'ENLPType': 'eNLPType',
        'EVPNSIDType': 'eVPNSIDType',
        'EnLenthForPolicyNLRI': 'enLenthForPolicyNLRI',
        'EnableAdVplsPrefixLength': 'enableAdVplsPrefixLength',
        'IBgpTester4BytesAsNumber': 'iBgpTester4BytesAsNumber',
        'IBgpTesterAsNumber': 'iBgpTesterAsNumber',
        'InitiateEbgpActiveConnection': 'initiateEbgpActiveConnection',
        'InitiateIbgpActiveConnection': 'initiateIbgpActiveConnection',
        'Ipv4AddrIndexType': 'ipv4AddrIndexType',
        'Ipv4LocRemoteAddrType': 'ipv4LocRemoteAddrType',
        'Ipv4NodeAddrType': 'ipv4NodeAddrType',
        'Ipv6AddrIndexType': 'ipv6AddrIndexType',
        'Ipv6LocRemoteAddrType': 'ipv6LocRemoteAddrType',
        'Ipv6NodeAddrType': 'ipv6NodeAddrType',
        'Ipv6SIDType': 'ipv6SIDType',
        'LenthForPolicyNLRI': 'lenthForPolicyNLRI',
        'MldpP2mpFecType': 'mldpP2mpFecType',
        'MplsSIDType': 'mplsSIDType',
        'Name': 'name',
        'PeerAdjSidType': 'peerAdjSidType',
        'PeerNodeSidType': 'peerNodeSidType',
        'PeerSetSidType': 'peerSetSidType',
        'PolicyNameType': 'policyNameType',
        'PolicyPriorityType': 'policyPriorityType',
        'PreferenceType': 'preferenceType',
        'PrefixSIDAttrType': 'prefixSIDAttrType',
        'ProtoclIdType': 'protoclIdType',
        'RemoteEndpointType': 'remoteEndpointType',
        'RequestVpnLabelExchangeOverLsp': 'requestVpnLabelExchangeOverLsp',
        'RowNames': 'rowNames',
        'SRv6VPNSIDTLVType': 'sRv6VPNSIDTLVType',
        'SegmentListType': 'segmentListType',
        'SrtePolicyAttrType': 'srtePolicyAttrType',
        'SrtePolicySAFI': 'srtePolicySAFI',
        'SrtePolicyType': 'srtePolicyType',
        'Srv6DraftNum': 'srv6DraftNum',
        'TriggerVplsPwInitiation': 'triggerVplsPwInitiation',
        'UdpDestinationPort': 'udpDestinationPort',
        'UseUnicastDestMacForBierTraffic': 'useUnicastDestMacForBierTraffic',
        'VPNSIDType': 'vPNSIDType',
        'VrfRouteImportExtendedCommunitySubType': 'vrfRouteImportExtendedCommunitySubType',
        'WeightType': 'weightType',
    }
    _SDM_ENUM_MAP = {
        'srv6DraftNum': ['version04', 'version_ietf_01'],
    }

    def __init__(self, parent, list_op=False):
        super(BgpIpv6Peer, self).__init__(parent, list_op)

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0 import StartRate
        if len(self._object_properties) > 0:
            if self._properties.get('StartRate', None) is not None:
                return self._properties.get('StartRate')
        return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04 import StopRate
        if len(self._object_properties) > 0:
            if self._properties.get('StopRate', None) is not None:
                return self._properties.get('StopRate')
        return StopRate(self)._select()

    @property
    def TlvEditor(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.tlveditor_9737bec75dbac826009c3374be76c5f7.TlvEditor): An instance of the TlvEditor class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.tlveditor_9737bec75dbac826009c3374be76c5f7 import TlvEditor
        if len(self._object_properties) > 0:
            if self._properties.get('TlvEditor', None) is not None:
                return self._properties.get('TlvEditor')
        return TlvEditor(self)

    @property
    def BIERTunnelType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): BIER Tunnel Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BIERTunnelType']))

    @property
    def LLGRCapabilityCode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Long Live Graceful Restart Capability Code
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LLGRCapabilityCode']))

    @property
    def BgpConfMemType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): BGP Confederation Member Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BgpConfMemType']))

    @property
    def BgpRouterId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): BGP Router-ID Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BgpRouterId']))

    @property
    def BindingType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Binding Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BindingType']))

    @property
    def ColorType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Color Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ColorType']))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DisableReceivedUpdateValidation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Disable Received Update Validation (Enabled for High Performance)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DisableReceivedUpdateValidation']))

    @property
    def ENLPType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Explicit NULL Label Policy Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ENLPType']))

    @property
    def EVPNSIDType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): EVPN SID Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EVPNSIDType']))

    @property
    def EnLenthForPolicyNLRI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include Length Field in SR TE Policy NLRI
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnLenthForPolicyNLRI']))

    @property
    def EnableAdVplsPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable AD VPLS Prefix Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAdVplsPrefixLength']))

    @property
    def IBgpTester4BytesAsNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Tester 4 Byte AS# for iBGP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IBgpTester4BytesAsNumber']))

    @property
    def IBgpTesterAsNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Tester AS# for iBGP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IBgpTesterAsNumber']))

    @property
    def InitiateEbgpActiveConnection(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Initiate eBGP Active Connection
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InitiateEbgpActiveConnection']))

    @property
    def InitiateIbgpActiveConnection(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Initiate iBGP Active Connection
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InitiateIbgpActiveConnection']))

    @property
    def Ipv4AddrIndexType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Address + Index Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4AddrIndexType']))

    @property
    def Ipv4LocRemoteAddrType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Local and Remote Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4LocRemoteAddrType']))

    @property
    def Ipv4NodeAddrType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Node Address Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4NodeAddrType']))

    @property
    def Ipv6AddrIndexType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Address + Index Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6AddrIndexType']))

    @property
    def Ipv6LocRemoteAddrType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Local and Remote Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6LocRemoteAddrType']))

    @property
    def Ipv6NodeAddrType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Node Address Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6NodeAddrType']))

    @property
    def Ipv6SIDType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 SID Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6SIDType']))

    @property
    def LenthForPolicyNLRI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Length Unit
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LenthForPolicyNLRI']))

    @property
    def MldpP2mpFecType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MLDP P2MP FEC Type (Hex)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MldpP2mpFecType']))

    @property
    def MplsSIDType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): MPLS SID Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MplsSIDType']))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def PeerAdjSidType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Peer-Adj-SID Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeerAdjSidType']))

    @property
    def PeerNodeSidType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Peer-Node-SID Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeerNodeSidType']))

    @property
    def PeerSetSidType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Peer-Set-SID Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeerSetSidType']))

    @property
    def PolicyNameType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Policy Name Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PolicyNameType']))

    @property
    def PolicyPriorityType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Policy Priority Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PolicyPriorityType']))

    @property
    def PreferenceType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Preference Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PreferenceType']))

    @property
    def PrefixSIDAttrType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Prefix SID Attr Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrefixSIDAttrType']))

    @property
    def ProtoclIdType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Protocol-ID Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ProtoclIdType']))

    @property
    def RemoteEndpointType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Remote Endpoint Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteEndpointType']))

    @property
    def RequestVpnLabelExchangeOverLsp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Request VPN Label Exchange over LSP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RequestVpnLabelExchangeOverLsp']))

    @property
    def RowNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowNames'])

    @property
    def SRv6VPNSIDTLVType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6-VPN SID TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SRv6VPNSIDTLVType']))

    @property
    def SegmentListType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Segment List Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SegmentListType']))

    @property
    def SrtePolicyAttrType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Tunnel Encaps Attribute Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrtePolicyAttrType']))

    @property
    def SrtePolicySAFI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SR TE Policy SAFI
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrtePolicySAFI']))

    @property
    def SrtePolicyType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Tunnel Type for SR Policy
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrtePolicyType']))

    @property
    def Srv6DraftNum(self):
        # type: () -> str
        """
        Returns
        -------
        - str(version04 | version_ietf_01): SRv6 VPN Draft Version Number to be used both for L3VPN and EVPN
        """
        return self._get_attribute(self._SDM_ATT_MAP['Srv6DraftNum'])
    @Srv6DraftNum.setter
    def Srv6DraftNum(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Srv6DraftNum'], value)

    @property
    def TriggerVplsPwInitiation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Trigger VPLS PW Initiation
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TriggerVplsPwInitiation']))

    @property
    def UdpDestinationPort(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): UDP Destination Port for VXLAN
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UdpDestinationPort']))

    @property
    def UseUnicastDestMacForBierTraffic(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Use Unicast Dst MAC for Traffic
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseUnicastDestMacForBierTraffic']))

    @property
    def VPNSIDType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): L3VPN SID Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VPNSIDType']))

    @property
    def VrfRouteImportExtendedCommunitySubType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VRF Route Import Extended Community Sub Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VrfRouteImportExtendedCommunitySubType']))

    @property
    def WeightType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Weight Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WeightType']))

    def update(self, Name=None, Srv6DraftNum=None):
        # type: (str, str) -> BgpIpv6Peer
        """Updates bgpIpv6Peer resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - Srv6DraftNum (str(version04 | version_ietf_01)): SRv6 VPN Draft Version Number to be used both for L3VPN and EVPN

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, RowNames=None, Srv6DraftNum=None):
        # type: (int, str, str, List[str], str) -> BgpIpv6Peer
        """Finds and retrieves bgpIpv6Peer resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpIpv6Peer resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpIpv6Peer resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - RowNames (list(str)): Name of rows
        - Srv6DraftNum (str(version04 | version_ietf_01)): SRv6 VPN Draft Version Number to be used both for L3VPN and EVPN

        Returns
        -------
        - self: This instance with matching bgpIpv6Peer resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpIpv6Peer data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpIpv6Peer resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, BIERTunnelType=None, LLGRCapabilityCode=None, BgpConfMemType=None, BgpRouterId=None, BindingType=None, ColorType=None, DisableReceivedUpdateValidation=None, ENLPType=None, EVPNSIDType=None, EnLenthForPolicyNLRI=None, EnableAdVplsPrefixLength=None, IBgpTester4BytesAsNumber=None, IBgpTesterAsNumber=None, InitiateEbgpActiveConnection=None, InitiateIbgpActiveConnection=None, Ipv4AddrIndexType=None, Ipv4LocRemoteAddrType=None, Ipv4NodeAddrType=None, Ipv6AddrIndexType=None, Ipv6LocRemoteAddrType=None, Ipv6NodeAddrType=None, Ipv6SIDType=None, LenthForPolicyNLRI=None, MldpP2mpFecType=None, MplsSIDType=None, PeerAdjSidType=None, PeerNodeSidType=None, PeerSetSidType=None, PolicyNameType=None, PolicyPriorityType=None, PreferenceType=None, PrefixSIDAttrType=None, ProtoclIdType=None, RemoteEndpointType=None, RequestVpnLabelExchangeOverLsp=None, SRv6VPNSIDTLVType=None, SegmentListType=None, SrtePolicyAttrType=None, SrtePolicySAFI=None, SrtePolicyType=None, TriggerVplsPwInitiation=None, UdpDestinationPort=None, UseUnicastDestMacForBierTraffic=None, VPNSIDType=None, VrfRouteImportExtendedCommunitySubType=None, WeightType=None):
        """Base class infrastructure that gets a list of bgpIpv6Peer device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BIERTunnelType (str): optional regex of BIERTunnelType
        - LLGRCapabilityCode (str): optional regex of LLGRCapabilityCode
        - BgpConfMemType (str): optional regex of bgpConfMemType
        - BgpRouterId (str): optional regex of bgpRouterId
        - BindingType (str): optional regex of bindingType
        - ColorType (str): optional regex of colorType
        - DisableReceivedUpdateValidation (str): optional regex of disableReceivedUpdateValidation
        - ENLPType (str): optional regex of eNLPType
        - EVPNSIDType (str): optional regex of eVPNSIDType
        - EnLenthForPolicyNLRI (str): optional regex of enLenthForPolicyNLRI
        - EnableAdVplsPrefixLength (str): optional regex of enableAdVplsPrefixLength
        - IBgpTester4BytesAsNumber (str): optional regex of iBgpTester4BytesAsNumber
        - IBgpTesterAsNumber (str): optional regex of iBgpTesterAsNumber
        - InitiateEbgpActiveConnection (str): optional regex of initiateEbgpActiveConnection
        - InitiateIbgpActiveConnection (str): optional regex of initiateIbgpActiveConnection
        - Ipv4AddrIndexType (str): optional regex of ipv4AddrIndexType
        - Ipv4LocRemoteAddrType (str): optional regex of ipv4LocRemoteAddrType
        - Ipv4NodeAddrType (str): optional regex of ipv4NodeAddrType
        - Ipv6AddrIndexType (str): optional regex of ipv6AddrIndexType
        - Ipv6LocRemoteAddrType (str): optional regex of ipv6LocRemoteAddrType
        - Ipv6NodeAddrType (str): optional regex of ipv6NodeAddrType
        - Ipv6SIDType (str): optional regex of ipv6SIDType
        - LenthForPolicyNLRI (str): optional regex of lenthForPolicyNLRI
        - MldpP2mpFecType (str): optional regex of mldpP2mpFecType
        - MplsSIDType (str): optional regex of mplsSIDType
        - PeerAdjSidType (str): optional regex of peerAdjSidType
        - PeerNodeSidType (str): optional regex of peerNodeSidType
        - PeerSetSidType (str): optional regex of peerSetSidType
        - PolicyNameType (str): optional regex of policyNameType
        - PolicyPriorityType (str): optional regex of policyPriorityType
        - PreferenceType (str): optional regex of preferenceType
        - PrefixSIDAttrType (str): optional regex of prefixSIDAttrType
        - ProtoclIdType (str): optional regex of protoclIdType
        - RemoteEndpointType (str): optional regex of remoteEndpointType
        - RequestVpnLabelExchangeOverLsp (str): optional regex of requestVpnLabelExchangeOverLsp
        - SRv6VPNSIDTLVType (str): optional regex of sRv6VPNSIDTLVType
        - SegmentListType (str): optional regex of segmentListType
        - SrtePolicyAttrType (str): optional regex of srtePolicyAttrType
        - SrtePolicySAFI (str): optional regex of srtePolicySAFI
        - SrtePolicyType (str): optional regex of srtePolicyType
        - TriggerVplsPwInitiation (str): optional regex of triggerVplsPwInitiation
        - UdpDestinationPort (str): optional regex of udpDestinationPort
        - UseUnicastDestMacForBierTraffic (str): optional regex of useUnicastDestMacForBierTraffic
        - VPNSIDType (str): optional regex of vPNSIDType
        - VrfRouteImportExtendedCommunitySubType (str): optional regex of vrfRouteImportExtendedCommunitySubType
        - WeightType (str): optional regex of weightType

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
