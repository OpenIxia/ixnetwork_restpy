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


class Ldpotherpws(Base):
    """LDP FEC128 Pseudo Wire Configuration[Other than Ethernet VLAN type]
    The Ldpotherpws class encapsulates a list of ldpotherpws resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ldpotherpws.find() method.
    The list can be managed by using the Ldpotherpws.add() and Ldpotherpws.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ldpotherpws'
    _SDM_ATT_MAP = {
        'ATMPresent': 'aTMPresent',
        'Active': 'active',
        'AutoPeerID': 'autoPeerID',
        'AutoPeerId': 'autoPeerId',
        'BfdPwCV': 'bfdPwCV',
        'BfdUdpCV': 'bfdUdpCV',
        'CAS': 'cAS',
        'CBitEnabled': 'cBitEnabled',
        'CEMOption': 'cEMOption',
        'CEMOptionPresent': 'cEMOptionPresent',
        'CEMPayLoadEnable': 'cEMPayLoadEnable',
        'CEMPayload': 'cEMPayload',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DescEnabled': 'descEnabled',
        'Description': 'description',
        'DescriptiveName': 'descriptiveName',
        'DownInterval': 'downInterval',
        'DownStart': 'downStart',
        'EnableCCCVNegotiation': 'enableCCCVNegotiation',
        'EnablePWStatus': 'enablePWStatus',
        'Errors': 'errors',
        'Frequency': 'frequency',
        'GroupId': 'groupId',
        'IfaceType': 'ifaceType',
        'IncludeRTPHeader': 'includeRTPHeader',
        'IncludeSSRC': 'includeSSRC',
        'IncludeTDMBitrate': 'includeTDMBitrate',
        'IncludeTDMOption': 'includeTDMOption',
        'IncludeTDMPayload': 'includeTDMPayload',
        'Ipv6PeerId': 'ipv6PeerId',
        'LSPPingCV': 'lSPPingCV',
        'Label': 'label',
        'LocalRouterID': 'localRouterID',
        'MaxATMCells': 'maxATMCells',
        'Mtu': 'mtu',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'PWACHCC': 'pWACHCC',
        'PWStatusCode': 'pWStatusCode',
        'PayloadType': 'payloadType',
        'PeerId': 'peerId',
        'PwStatusSendNotification': 'pwStatusSendNotification',
        'RepeatCount': 'repeatCount',
        'RouterAlertCC': 'routerAlertCC',
        'SP': 'sP',
        'SSRC': 'sSRC',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TDMBitrate': 'tDMBitrate',
        'TDMDataSize': 'tDMDataSize',
        'TimestampMode': 'timestampMode',
        'UpInterval': 'upInterval',
        'VCIDStart': 'vCIDStart',
    }

    def __init__(self, parent):
        super(Ldpotherpws, self).__init__(parent)

    @property
    def Connector(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b.Connector): An instance of the Connector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b import Connector
        return Connector(self)

    @property
    def Ethernet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet_18677f1f170027c217563a3250b1f635.Ethernet): An instance of the Ethernet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet_18677f1f170027c217563a3250b1f635 import Ethernet
        return Ethernet(self)

    @property
    def Ipv4Loopback(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback_f84286c6e2c90f5267670278dde3f258.Ipv4Loopback): An instance of the Ipv4Loopback class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback_f84286c6e2c90f5267670278dde3f258 import Ipv4Loopback
        return Ipv4Loopback(self)

    @property
    def Ipv6Loopback(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback_c5557054afff2b9cc84b7676de50b805.Ipv6Loopback): An instance of the Ipv6Loopback class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback_c5557054afff2b9cc84b7676de50b805 import Ipv6Loopback
        return Ipv6Loopback(self)

    @property
    def LdpBasicRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter_53e2de40003674322c811a1ba519dbb6.LdpBasicRouter): An instance of the LdpBasicRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter_53e2de40003674322c811a1ba519dbb6 import LdpBasicRouter
        return LdpBasicRouter(self)

    @property
    def LdpBasicRouterV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6_b554f464616f39033d7acad4846e556c.LdpBasicRouterV6): An instance of the LdpBasicRouterV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6_b554f464616f39033d7acad4846e556c import LdpBasicRouterV6
        return LdpBasicRouterV6(self)

    @property
    def LdpTargetedRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter_85c7a9993d80996c22a9dbd739df9692.LdpTargetedRouter): An instance of the LdpTargetedRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter_85c7a9993d80996c22a9dbd739df9692 import LdpTargetedRouter
        return LdpTargetedRouter(self)

    @property
    def LdpTargetedRouterV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6_e86e77f17dfccefac9e15769756089cf.LdpTargetedRouterV6): An instance of the LdpTargetedRouterV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6_e86e77f17dfccefac9e15769756089cf import LdpTargetedRouterV6
        return LdpTargetedRouterV6(self)

    @property
    def ATMPresent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, indicates that ATM Transparent Cell Transport mode is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ATMPresent']))

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AutoPeerID(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoPeerID']))

    @property
    def AutoPeerId(self):
        """
        Returns
        -------
        - bool: If selected, LDP Peer IP would be taken from LDP router's peer configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoPeerId'])
    @AutoPeerId.setter
    def AutoPeerId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoPeerId'], value)

    @property
    def BfdPwCV(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFD PW-ACH CV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BfdPwCV']))

    @property
    def BfdUdpCV(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFD IP/UDP CV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BfdUdpCV']))

    @property
    def CAS(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CAS Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CAS']))

    @property
    def CBitEnabled(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, sets the C-Bit (flag). It is the highest order bit in the VC Type field. If the bit is set, it indicates the presence of a control word on this VC.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CBitEnabled']))

    @property
    def CEMOption(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value of the CEM option
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CEMOption']))

    @property
    def CEMOptionPresent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, indicates that a CEM option is present
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CEMOptionPresent']))

    @property
    def CEMPayLoadEnable(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, indicates that there is a Circuit Emulation Service over MPLS (CEM) payload
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CEMPayLoadEnable']))

    @property
    def CEMPayload(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The length of the CEM payload (in bytes)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CEMPayload']))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer is used to connect with to the wire.
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
    def DescEnabled(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, indicates that an optional Interface Description is present
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DescEnabled']))

    @property
    def Description(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): An optional user-defined Interface Description. It may be used with ALL VC types. Valid length is 0 to 80 octets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Description']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DownInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time interval for which the PW status will remain down
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DownInterval']))

    @property
    def DownStart(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The duration in time after session becomes up and a notification message being sent to make the session down
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DownStart']))

    @property
    def EnableCCCVNegotiation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, indicates that CCCV Negotiation is enabled
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableCCCVNegotiation']))

    @property
    def EnablePWStatus(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, this enables the use of PW Status TLV in notification messages to notify the PW status
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnablePWStatus']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def Frequency(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configures the frequency of the payload type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Frequency']))

    @property
    def GroupId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A user-defined 32-bit value used to identify a group of VCs
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupId']))

    @property
    def IfaceType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The 15-bit VC Type used in the VC FEC element.It depends on the Layer 2 protocol used on the interface
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IfaceType']))

    @property
    def IncludeRTPHeader(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, indicates that RTP Header is present
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeRTPHeader']))

    @property
    def IncludeSSRC(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Click to enable SSRC
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSSRC']))

    @property
    def IncludeTDMBitrate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, indicates that TDM Bitrate is present
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTDMBitrate']))

    @property
    def IncludeTDMOption(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include TDM Option
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTDMOption']))

    @property
    def IncludeTDMPayload(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, indicates that TDM Payload is present
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeTDMPayload']))

    @property
    def Ipv6PeerId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The 128-bit IPv6 address of the LDP Peer.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6PeerId']))

    @property
    def LSPPingCV(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP Ping CV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LSPPingCV']))

    @property
    def Label(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Label']))

    @property
    def LocalRouterID(self):
        """
        Returns
        -------
        - list(str): Router ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRouterID'])

    @property
    def MaxATMCells(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Maximum number of ATM Cells which may be concatenated and sent in a single MPLS frame
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxATMCells']))

    @property
    def Mtu(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The 2-octet value for the maximum Transmission Unit (MTU).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Mtu']))

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
    def PWACHCC(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PW-ACH CC
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PWACHCC']))

    @property
    def PWStatusCode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PW Status Code to be sent when to transition to down state if PW Status Send Notification is enabled
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PWStatusCode']))

    @property
    def PayloadType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configures the pay load type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PayloadType']))

    @property
    def PeerId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The 32-bit IPv4 address of the LDP Peer.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeerId']))

    @property
    def PwStatusSendNotification(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, it signifies whether to send a notification message with a PW status for the corresponding PW
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PwStatusSendNotification']))

    @property
    def RepeatCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of times to repeat the Up/Down status of the PW. '0' means keep toggling the Up/Down state indefinitely.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RepeatCount']))

    @property
    def RouterAlertCC(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router Alert CC
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouterAlertCC']))

    @property
    def SP(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SP Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SP']))

    @property
    def SSRC(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SSRC Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SSRC']))

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
    def TDMBitrate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value of the TDM bitrate
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TDMBitrate']))

    @property
    def TDMDataSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The total size of the TDM data
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TDMDataSize']))

    @property
    def TimestampMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timestamp Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimestampMode']))

    @property
    def UpInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time Interval for which the PW status will remain in Up state before transitioning again to Down state.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UpInterval']))

    @property
    def VCIDStart(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value of the VC ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VCIDStart']))

    def update(self, AutoPeerId=None, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Updates ldpotherpws resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - AutoPeerId (bool): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AutoPeerId=None, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Adds a new ldpotherpws resource on the server and adds it to the container.

        Args
        ----
        - AutoPeerId (bool): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved ldpotherpws resources using find and the newly added ldpotherpws resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ldpotherpws resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AutoPeerId=None, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, LocalRouterID=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves ldpotherpws resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ldpotherpws resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ldpotherpws resources from the server.

        Args
        ----
        - AutoPeerId (bool): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - LocalRouterID (list(str)): Router ID
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching ldpotherpws resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ldpotherpws data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ldpotherpws resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ATMPresent=None, Active=None, AutoPeerID=None, BfdPwCV=None, BfdUdpCV=None, CAS=None, CBitEnabled=None, CEMOption=None, CEMOptionPresent=None, CEMPayLoadEnable=None, CEMPayload=None, DescEnabled=None, Description=None, DownInterval=None, DownStart=None, EnableCCCVNegotiation=None, EnablePWStatus=None, Frequency=None, GroupId=None, IfaceType=None, IncludeRTPHeader=None, IncludeSSRC=None, IncludeTDMBitrate=None, IncludeTDMOption=None, IncludeTDMPayload=None, Ipv6PeerId=None, LSPPingCV=None, Label=None, MaxATMCells=None, Mtu=None, PWACHCC=None, PWStatusCode=None, PayloadType=None, PeerId=None, PwStatusSendNotification=None, RepeatCount=None, RouterAlertCC=None, SP=None, SSRC=None, TDMBitrate=None, TDMDataSize=None, TimestampMode=None, UpInterval=None, VCIDStart=None):
        """Base class infrastructure that gets a list of ldpotherpws device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ATMPresent (str): optional regex of aTMPresent
        - Active (str): optional regex of active
        - AutoPeerID (str): optional regex of autoPeerID
        - BfdPwCV (str): optional regex of bfdPwCV
        - BfdUdpCV (str): optional regex of bfdUdpCV
        - CAS (str): optional regex of cAS
        - CBitEnabled (str): optional regex of cBitEnabled
        - CEMOption (str): optional regex of cEMOption
        - CEMOptionPresent (str): optional regex of cEMOptionPresent
        - CEMPayLoadEnable (str): optional regex of cEMPayLoadEnable
        - CEMPayload (str): optional regex of cEMPayload
        - DescEnabled (str): optional regex of descEnabled
        - Description (str): optional regex of description
        - DownInterval (str): optional regex of downInterval
        - DownStart (str): optional regex of downStart
        - EnableCCCVNegotiation (str): optional regex of enableCCCVNegotiation
        - EnablePWStatus (str): optional regex of enablePWStatus
        - Frequency (str): optional regex of frequency
        - GroupId (str): optional regex of groupId
        - IfaceType (str): optional regex of ifaceType
        - IncludeRTPHeader (str): optional regex of includeRTPHeader
        - IncludeSSRC (str): optional regex of includeSSRC
        - IncludeTDMBitrate (str): optional regex of includeTDMBitrate
        - IncludeTDMOption (str): optional regex of includeTDMOption
        - IncludeTDMPayload (str): optional regex of includeTDMPayload
        - Ipv6PeerId (str): optional regex of ipv6PeerId
        - LSPPingCV (str): optional regex of lSPPingCV
        - Label (str): optional regex of label
        - MaxATMCells (str): optional regex of maxATMCells
        - Mtu (str): optional regex of mtu
        - PWACHCC (str): optional regex of pWACHCC
        - PWStatusCode (str): optional regex of pWStatusCode
        - PayloadType (str): optional regex of payloadType
        - PeerId (str): optional regex of peerId
        - PwStatusSendNotification (str): optional regex of pwStatusSendNotification
        - RepeatCount (str): optional regex of repeatCount
        - RouterAlertCC (str): optional regex of routerAlertCC
        - SP (str): optional regex of sP
        - SSRC (str): optional regex of sSRC
        - TDMBitrate (str): optional regex of tDMBitrate
        - TDMDataSize (str): optional regex of tDMDataSize
        - TimestampMode (str): optional regex of timestampMode
        - UpInterval (str): optional regex of upInterval
        - VCIDStart (str): optional regex of vCIDStart

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

    def PurgeVCRanges(self, *args, **kwargs):
        """Executes the purgeVCRanges operation on the server.

        Purge VC Ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        purgeVCRanges(SessionIndices=list)
        ----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        purgeVCRanges(SessionIndices=string)
        ------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('purgeVCRanges', payload=payload, response_object=None)

    def Purgevcranges(self, *args, **kwargs):
        """Executes the purgevcranges operation on the server.

        Purge Ethernet VC. Sends Address Withdraw message to purge all MACs learnt for this VC. Applicable for Ethernet Type VC only ( not VLAN).

        purgevcranges(Arg2=list)list
        ----------------------------
        - Arg2 (list(number)): Purge VC Ranges.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('purgevcranges', payload=payload, response_object=None)

    def PurgeVPLSMac(self, *args, **kwargs):
        """Executes the purgeVPLSMac operation on the server.

        Purge VPLS MAC

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        purgeVPLSMac(Mac_count=number, Mac=string)
        ------------------------------------------
        - Mac_count (number): This parameter requires a mac_count of type kInteger
        - Mac (str): This parameter requires a mac of type kString

        purgeVPLSMac(Mac_count=number, Mac=string, SessionIndices=list)
        ---------------------------------------------------------------
        - Mac_count (number): This parameter requires a mac_count of type kInteger
        - Mac (str): This parameter requires a mac of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        purgeVPLSMac(SessionIndices=string, Mac_count=number, Mac=string)
        -----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a mac_count of type kInteger
        - Mac_count (number): This parameter requires a mac of type kString
        - Mac (str): This parameter requires a string of session numbers 1-4;6;7-12

        purgeVPLSMac(Arg2=list, Arg3=number, Arg4=string)list
        -----------------------------------------------------
        - Arg2 (list(number)): Purge Ethernet MAC.
        - Arg3 (number): Number of Mac addresses to purge
        - Arg4 (str): Mac addresses start
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('purgeVPLSMac', payload=payload, response_object=None)

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
