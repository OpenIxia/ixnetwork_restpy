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


class Ldpvplsbgpad(Base):
    """LDP FEC129 Configuration
    The Ldpvplsbgpad class encapsulates a list of ldpvplsbgpad resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ldpvplsbgpad.find() method.
    The list can be managed by using the Ldpvplsbgpad.add() and Ldpvplsbgpad.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ldpvplsbgpad'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AsNumberVplsId': 'asNumberVplsId',
        'AssignedNumberVplsId': 'assignedNumberVplsId',
        'AutoPeerID': 'autoPeerID',
        'AutoPeerId': 'autoPeerId',
        'BfdPwCV': 'bfdPwCV',
        'BfdUdpCV': 'bfdUdpCV',
        'CBitEnabled': 'cBitEnabled',
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
        'GroupId': 'groupId',
        'InterfaceType': 'interfaceType',
        'IpAddressVplsId': 'ipAddressVplsId',
        'Ipv6PeerId': 'ipv6PeerId',
        'LSPPingCV': 'lSPPingCV',
        'Label': 'label',
        'LocalRouterID': 'localRouterID',
        'Mtu': 'mtu',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'PWACHCC': 'pWACHCC',
        'PWStatusCode': 'pWStatusCode',
        'PeerId': 'peerId',
        'ProvisioningModelType': 'provisioningModelType',
        'PwStatusSendNotification': 'pwStatusSendNotification',
        'RepeatCount': 'repeatCount',
        'RouterAlertCC': 'routerAlertCC',
        'SessionStatus': 'sessionStatus',
        'SourceAIIType': 'sourceAIIType',
        'SourceAIIasIP': 'sourceAIIasIP',
        'SourceAIIasNumber': 'sourceAIIasNumber',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TargetAIIType': 'targetAIIType',
        'TargetAIIasIP': 'targetAIIasIP',
        'TargetAIIasNumber': 'targetAIIasNumber',
        'TypeVplsId': 'typeVplsId',
        'UpInterval': 'upInterval',
    }

    def __init__(self, parent):
        super(Ldpvplsbgpad, self).__init__(parent)

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
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AsNumberVplsId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The AS number of the VPLS Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsNumberVplsId']))

    @property
    def AssignedNumberVplsId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The assigned number for the VPLS Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AssignedNumberVplsId']))

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
    def CBitEnabled(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, sets the C-Bit (flag). It is the highest order bit in the VC Type field. If the bit is set, it indicates the presence of a control word on this VC.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CBitEnabled']))

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
    def GroupId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A user-defined 32-bit value used to identify a group of VCs
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupId']))

    @property
    def InterfaceType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The 15-bit VC Type used in the VC FEC element.It depends on the Layer 2 protocol used on the interface
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InterfaceType']))

    @property
    def IpAddressVplsId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The IP address of the VPLS id.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpAddressVplsId']))

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
    def PeerId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The 32-bit IPv4 address of the LDP Peer.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeerId']))

    @property
    def ProvisioningModelType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Provisioning Model Type. Manual or BGP Autodiscovery
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ProvisioningModelType']))

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
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def SourceAIIType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source AII Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceAIIType']))

    @property
    def SourceAIIasIP(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source AII as IP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceAIIasIP']))

    @property
    def SourceAIIasNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source AII as Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceAIIasNumber']))

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
    def TargetAIIType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Target AII Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TargetAIIType']))

    @property
    def TargetAIIasIP(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Target AII as IP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TargetAIIasIP']))

    @property
    def TargetAIIasNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Target AII as Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TargetAIIasNumber']))

    @property
    def TypeVplsId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The VPLS Id format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TypeVplsId']))

    @property
    def UpInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time Interval for which the PW status will remain in Up state before transitioning again to Down state.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UpInterval']))

    def update(self, AutoPeerId=None, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Updates ldpvplsbgpad resource on the server.

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
        """Adds a new ldpvplsbgpad resource on the server and adds it to the container.

        Args
        ----
        - AutoPeerId (bool): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved ldpvplsbgpad resources using find and the newly added ldpvplsbgpad resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ldpvplsbgpad resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AutoPeerId=None, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, LocalRouterID=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves ldpvplsbgpad resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ldpvplsbgpad resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ldpvplsbgpad resources from the server.

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
        - self: This instance with matching ldpvplsbgpad resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ldpvplsbgpad data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ldpvplsbgpad resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AsNumberVplsId=None, AssignedNumberVplsId=None, AutoPeerID=None, BfdPwCV=None, BfdUdpCV=None, CBitEnabled=None, DescEnabled=None, Description=None, DownInterval=None, DownStart=None, EnableCCCVNegotiation=None, EnablePWStatus=None, GroupId=None, InterfaceType=None, IpAddressVplsId=None, Ipv6PeerId=None, LSPPingCV=None, Label=None, Mtu=None, PWACHCC=None, PWStatusCode=None, PeerId=None, ProvisioningModelType=None, PwStatusSendNotification=None, RepeatCount=None, RouterAlertCC=None, SourceAIIType=None, SourceAIIasIP=None, SourceAIIasNumber=None, TargetAIIType=None, TargetAIIasIP=None, TargetAIIasNumber=None, TypeVplsId=None, UpInterval=None):
        """Base class infrastructure that gets a list of ldpvplsbgpad device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AsNumberVplsId (str): optional regex of asNumberVplsId
        - AssignedNumberVplsId (str): optional regex of assignedNumberVplsId
        - AutoPeerID (str): optional regex of autoPeerID
        - BfdPwCV (str): optional regex of bfdPwCV
        - BfdUdpCV (str): optional regex of bfdUdpCV
        - CBitEnabled (str): optional regex of cBitEnabled
        - DescEnabled (str): optional regex of descEnabled
        - Description (str): optional regex of description
        - DownInterval (str): optional regex of downInterval
        - DownStart (str): optional regex of downStart
        - EnableCCCVNegotiation (str): optional regex of enableCCCVNegotiation
        - EnablePWStatus (str): optional regex of enablePWStatus
        - GroupId (str): optional regex of groupId
        - InterfaceType (str): optional regex of interfaceType
        - IpAddressVplsId (str): optional regex of ipAddressVplsId
        - Ipv6PeerId (str): optional regex of ipv6PeerId
        - LSPPingCV (str): optional regex of lSPPingCV
        - Label (str): optional regex of label
        - Mtu (str): optional regex of mtu
        - PWACHCC (str): optional regex of pWACHCC
        - PWStatusCode (str): optional regex of pWStatusCode
        - PeerId (str): optional regex of peerId
        - ProvisioningModelType (str): optional regex of provisioningModelType
        - PwStatusSendNotification (str): optional regex of pwStatusSendNotification
        - RepeatCount (str): optional regex of repeatCount
        - RouterAlertCC (str): optional regex of routerAlertCC
        - SourceAIIType (str): optional regex of sourceAIIType
        - SourceAIIasIP (str): optional regex of sourceAIIasIP
        - SourceAIIasNumber (str): optional regex of sourceAIIasNumber
        - TargetAIIType (str): optional regex of targetAIIType
        - TargetAIIasIP (str): optional regex of targetAIIasIP
        - TargetAIIasNumber (str): optional regex of targetAIIasNumber
        - TypeVplsId (str): optional regex of typeVplsId
        - UpInterval (str): optional regex of upInterval

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
