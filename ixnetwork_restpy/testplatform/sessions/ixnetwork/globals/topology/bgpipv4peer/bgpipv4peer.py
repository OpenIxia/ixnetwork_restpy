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


class BgpIpv4Peer(Base):
    """BGP Port level Configuration
    The BgpIpv4Peer class encapsulates a required bgpIpv4Peer resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpIpv4Peer'

    def __init__(self, parent):
        super(BgpIpv4Peer, self).__init__(parent)

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.startrate.startrate.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.startrate.startrate import StartRate
        return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.stoprate.stoprate.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.stoprate.stoprate import StopRate
        return StopRate(self)._select()

    @property
    def TlvEditor(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.tlveditor.TlvEditor): An instance of the TlvEditor class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.tlveditor import TlvEditor
        return TlvEditor(self)

    @property
    def BIERTunnelType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BIER Tunnel Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('BIERTunnelType'))

    @property
    def LLGRCapabilityCode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Long Live Graceful Restart Capability Code
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('LLGRCapabilityCode'))

    @property
    def BgpConfMemType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BGP Confederation Member Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bgpConfMemType'))

    @property
    def BgpRouterId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BGP Router-ID Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bgpRouterId'))

    @property
    def BindingType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Binding Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bindingType'))

    @property
    def ColorType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Color Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('colorType'))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute('descriptiveName')

    @property
    def DisableReceivedUpdateValidation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Disable Received Update Validation (Enabled for High Performance)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('disableReceivedUpdateValidation'))

    @property
    def ENLPType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Explicit NULL Label Policy Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('eNLPType'))

    @property
    def EVPNSIDType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): EVPN SID Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('eVPNSIDType'))

    @property
    def EnLenthForPolicyNLRI(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Length Field in SR TE Policy NLRI
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enLenthForPolicyNLRI'))

    @property
    def EnableAdVplsPrefixLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable AD VPLS Prefix Length in Bits
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableAdVplsPrefixLength'))

    @property
    def IBgpTester4BytesAsNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tester 4 Byte AS# for iBGP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('iBgpTester4BytesAsNumber'))

    @property
    def IBgpTesterAsNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tester AS# for iBGP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('iBgpTesterAsNumber'))

    @property
    def InitiateEbgpActiveConnection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Initiate eBGP Active Connection
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('initiateEbgpActiveConnection'))

    @property
    def InitiateIbgpActiveConnection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Initiate iBGP Active Connection
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('initiateIbgpActiveConnection'))

    @property
    def Ipv4AddrIndexType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Address + Index Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ipv4AddrIndexType'))

    @property
    def Ipv4LocRemoteAddrType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Local and Remote Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ipv4LocRemoteAddrType'))

    @property
    def Ipv4NodeAddrType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Node Address Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ipv4NodeAddrType'))

    @property
    def Ipv6AddrIndexType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Address + Index Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ipv6AddrIndexType'))

    @property
    def Ipv6LocRemoteAddrType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Local and Remote Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ipv6LocRemoteAddrType'))

    @property
    def Ipv6NodeAddrType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Node Address Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ipv6NodeAddrType'))

    @property
    def Ipv6SIDType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 SID Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ipv6SIDType'))

    @property
    def LenthForPolicyNLRI(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Length Unit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('lenthForPolicyNLRI'))

    @property
    def MldpP2mpFecType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MLDP P2MP FEC Type (Hex)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mldpP2mpFecType'))

    @property
    def MplsSIDType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MPLS SID Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mplsSIDType'))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def PeerAdjSidType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peer-Adj-SID Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('peerAdjSidType'))

    @property
    def PeerNodeSidType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peer-Node-SID Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('peerNodeSidType'))

    @property
    def PeerSetSidType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peer-Set-SID Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('peerSetSidType'))

    @property
    def PolicyNameType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Policy Name Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('policyNameType'))

    @property
    def PolicyPriorityType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Policy Priority Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('policyPriorityType'))

    @property
    def PreferenceType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Preference Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('preferenceType'))

    @property
    def PrefixSIDAttrType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Prefix SID Attr Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('prefixSIDAttrType'))

    @property
    def ProtoclIdType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Protocol-ID Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('protoclIdType'))

    @property
    def RemoteEndpointType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remote Endpoint Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('remoteEndpointType'))

    @property
    def RequestVpnLabelExchangeOverLsp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Request VPN Label Exchange over LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('requestVpnLabelExchangeOverLsp'))

    @property
    def RowNames(self):
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute('rowNames')

    @property
    def SRv6VPNSIDTLVType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6-VPN SID TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('sRv6VPNSIDTLVType'))

    @property
    def SegmentListType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Segment List Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('segmentListType'))

    @property
    def SrtePolicyAttrType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tunnel Encaps Attribute Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srtePolicyAttrType'))

    @property
    def SrtePolicySAFI(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SR TE Policy SAFI
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srtePolicySAFI'))

    @property
    def SrtePolicyType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tunnel Type for SR Policy
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srtePolicyType'))

    @property
    def Srv6DraftNum(self):
        """
        Returns
        -------
        - str(version04 | version_ietf_01): L3VPN SRv6 Draft Version Number
        """
        return self._get_attribute('srv6DraftNum')
    @Srv6DraftNum.setter
    def Srv6DraftNum(self, value):
        self._set_attribute('srv6DraftNum', value)

    @property
    def TriggerVplsPwInitiation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Trigger VPLS PW Initiation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('triggerVplsPwInitiation'))

    @property
    def UdpDestinationPort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): UDP Destination Port for VXLAN
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('udpDestinationPort'))

    @property
    def UseUnicastDestMacForBierTraffic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Unicast Dst MAC for Traffic
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('useUnicastDestMacForBierTraffic'))

    @property
    def VPNSIDType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L3VPN SID Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('vPNSIDType'))

    @property
    def VrfRouteImportExtendedCommunitySubType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VRF Route Import Extended Community Sub Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('vrfRouteImportExtendedCommunitySubType'))

    @property
    def WeightType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Weight Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('weightType'))

    def update(self, Name=None, Srv6DraftNum=None):
        """Updates bgpIpv4Peer resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - Srv6DraftNum (str(version04 | version_ietf_01)): L3VPN SRv6 Draft Version Number

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def get_device_ids(self, PortNames=None, BIERTunnelType=None, LLGRCapabilityCode=None, BgpConfMemType=None, BgpRouterId=None, BindingType=None, ColorType=None, DisableReceivedUpdateValidation=None, ENLPType=None, EVPNSIDType=None, EnLenthForPolicyNLRI=None, EnableAdVplsPrefixLength=None, IBgpTester4BytesAsNumber=None, IBgpTesterAsNumber=None, InitiateEbgpActiveConnection=None, InitiateIbgpActiveConnection=None, Ipv4AddrIndexType=None, Ipv4LocRemoteAddrType=None, Ipv4NodeAddrType=None, Ipv6AddrIndexType=None, Ipv6LocRemoteAddrType=None, Ipv6NodeAddrType=None, Ipv6SIDType=None, LenthForPolicyNLRI=None, MldpP2mpFecType=None, MplsSIDType=None, PeerAdjSidType=None, PeerNodeSidType=None, PeerSetSidType=None, PolicyNameType=None, PolicyPriorityType=None, PreferenceType=None, PrefixSIDAttrType=None, ProtoclIdType=None, RemoteEndpointType=None, RequestVpnLabelExchangeOverLsp=None, SRv6VPNSIDTLVType=None, SegmentListType=None, SrtePolicyAttrType=None, SrtePolicySAFI=None, SrtePolicyType=None, TriggerVplsPwInitiation=None, UdpDestinationPort=None, UseUnicastDestMacForBierTraffic=None, VPNSIDType=None, VrfRouteImportExtendedCommunitySubType=None, WeightType=None):
        """Base class infrastructure that gets a list of bgpIpv4Peer device ids encapsulated by this object.

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
