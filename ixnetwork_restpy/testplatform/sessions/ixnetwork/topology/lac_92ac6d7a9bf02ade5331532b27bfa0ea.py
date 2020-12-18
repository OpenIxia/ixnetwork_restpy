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


class Lac(Base):
    """L2TP Access Concentrator protocol.
    The Lac class encapsulates a list of lac resources that are managed by the user.
    A list of resources can be retrieved from the server using the Lac.find() method.
    The list can be managed by using the Lac.add() and Lac.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'lac'
    _SDM_ATT_MAP = {
        'BaseLnsIp': 'baseLnsIp',
        'BearerCapability': 'bearerCapability',
        'BearerType': 'bearerType',
        'Callingnum': 'callingnum',
        'ConnectedVia': 'connectedVia',
        'ControlMsgsRetryCounter': 'controlMsgsRetryCounter',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableControlChecksum': 'enableControlChecksum',
        'EnableDataChecksum': 'enableDataChecksum',
        'EnableExcludeHdlc': 'enableExcludeHdlc',
        'EnableHelloRequest': 'enableHelloRequest',
        'EnableRedial': 'enableRedial',
        'Errors': 'errors',
        'FramingCapability': 'framingCapability',
        'HelloRequestInterval': 'helloRequestInterval',
        'InitRetransmitInterval': 'initRetransmitInterval',
        'LacHostName': 'lacHostName',
        'LacSecret': 'lacSecret',
        'MaxRedialAttempts': 'maxRedialAttempts',
        'MaxRetransmitInterval': 'maxRetransmitInterval',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'OffsetByte': 'offsetByte',
        'OffsetLength': 'offsetLength',
        'ReceiveWindowSize': 'receiveWindowSize',
        'RedialInterval': 'redialInterval',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TunnelAuthentication': 'tunnelAuthentication',
        'TunnelsPerInterfaceMultiplier': 'tunnelsPerInterfaceMultiplier',
        'UdpDestinationPort': 'udpDestinationPort',
        'UdpSourcePort': 'udpSourcePort',
        'UseHiddenAVPs': 'useHiddenAVPs',
        'UseLengthBitInPayload': 'useLengthBitInPayload',
        'UseOffsetBitInPayload': 'useOffsetBitInPayload',
        'UseSequenceNoInPayload': 'useSequenceNoInPayload',
    }

    def __init__(self, parent):
        super(Lac, self).__init__(parent)

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
    def BaseLnsIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the base address to be used by the L2TP tunnel
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BaseLnsIp']))

    @property
    def BearerCapability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates to the DUT the bearer device types from which incoming calls will be accepted.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BearerCapability']))

    @property
    def BearerType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The bearer type.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BearerType']))

    @property
    def Callingnum(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Calling Number AVP in ICRQ
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Callingnum']))

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
    def ControlMsgsRetryCounter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of L2TP retries
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ControlMsgsRetryCounter']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnableControlChecksum(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, UDP checksum is enabled on control plane packets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableControlChecksum']))

    @property
    def EnableDataChecksum(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, UDP checksum is enabled on data plane packets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableDataChecksum']))

    @property
    def EnableExcludeHdlc(self):
        """
        Returns
        -------
        - bool: If checked, HDLC header is not encoded in the L2TP packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableExcludeHdlc'])
    @EnableExcludeHdlc.setter
    def EnableExcludeHdlc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableExcludeHdlc'], value)

    @property
    def EnableHelloRequest(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, L2TP hello request is enabled
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableHelloRequest']))

    @property
    def EnableRedial(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, L2TP redial is enabled
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRedial']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def FramingCapability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Designates sync or async framing
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FramingCapability']))

    @property
    def HelloRequestInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for L2TP hello request, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HelloRequestInterval']))

    @property
    def InitRetransmitInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The initial amount of time that can elapse before an unacknowledged control message is retransmitted.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InitRetransmitInterval']))

    @property
    def LacHostName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LAC Hostname used for tunnel authentication.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LacHostName']))

    @property
    def LacSecret(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Secret value used for tunnel authentication.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LacSecret']))

    @property
    def MaxRedialAttempts(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum number of L2TP redial attempts
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxRedialAttempts']))

    @property
    def MaxRetransmitInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The maximum amount of time that can elapse for receiving a reply for a control message.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxRetransmitInterval']))

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
    def OffsetByte(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L2TP offset byte. Applicable only if offset bit is set.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OffsetByte']))

    @property
    def OffsetLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L2TP offset length in bytes. Applicable only if offset bit set.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OffsetLength']))

    @property
    def ReceiveWindowSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L2TP Receive Window Size
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReceiveWindowSize']))

    @property
    def RedialInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L2TP redial timeout, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RedialInterval']))

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
    def TunnelAuthentication(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables or disables L2TP tunnel authentication
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TunnelAuthentication']))

    @property
    def TunnelsPerInterfaceMultiplier(self):
        """
        Returns
        -------
        - number: Number of tunnels per interface (multiplier).
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelsPerInterfaceMultiplier'])
    @TunnelsPerInterfaceMultiplier.setter
    def TunnelsPerInterfaceMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelsPerInterfaceMultiplier'], value)

    @property
    def UdpDestinationPort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): UDP port to employ for tunneling destinations
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UdpDestinationPort']))

    @property
    def UdpSourcePort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): UDP port to employ for tunneling sources
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UdpSourcePort']))

    @property
    def UseHiddenAVPs(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, Attribute Value Pair hiding is enabled
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseHiddenAVPs']))

    @property
    def UseLengthBitInPayload(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, length bit is set in L2TP data packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseLengthBitInPayload']))

    @property
    def UseOffsetBitInPayload(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, offset bit is enabled in L2TP data packets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseOffsetBitInPayload']))

    @property
    def UseSequenceNoInPayload(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, sequence bit is set in L2TP data packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseSequenceNoInPayload']))

    def update(self, ConnectedVia=None, EnableExcludeHdlc=None, Multiplier=None, Name=None, StackedLayers=None, TunnelsPerInterfaceMultiplier=None):
        """Updates lac resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - EnableExcludeHdlc (bool): If checked, HDLC header is not encoded in the L2TP packets.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - TunnelsPerInterfaceMultiplier (number): Number of tunnels per interface (multiplier).

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, EnableExcludeHdlc=None, Multiplier=None, Name=None, StackedLayers=None, TunnelsPerInterfaceMultiplier=None):
        """Adds a new lac resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - EnableExcludeHdlc (bool): If checked, HDLC header is not encoded in the L2TP packets.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - TunnelsPerInterfaceMultiplier (number): Number of tunnels per interface (multiplier).

        Returns
        -------
        - self: This instance with all currently retrieved lac resources using find and the newly added lac resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained lac resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, EnableExcludeHdlc=None, Errors=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None, TunnelsPerInterfaceMultiplier=None):
        """Finds and retrieves lac resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lac resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lac resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableExcludeHdlc (bool): If checked, HDLC header is not encoded in the L2TP packets.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - TunnelsPerInterfaceMultiplier (number): Number of tunnels per interface (multiplier).

        Returns
        -------
        - self: This instance with matching lac resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lac data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lac resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, BaseLnsIp=None, BearerCapability=None, BearerType=None, Callingnum=None, ControlMsgsRetryCounter=None, EnableControlChecksum=None, EnableDataChecksum=None, EnableHelloRequest=None, EnableRedial=None, FramingCapability=None, HelloRequestInterval=None, InitRetransmitInterval=None, LacHostName=None, LacSecret=None, MaxRedialAttempts=None, MaxRetransmitInterval=None, OffsetByte=None, OffsetLength=None, ReceiveWindowSize=None, RedialInterval=None, TunnelAuthentication=None, UdpDestinationPort=None, UdpSourcePort=None, UseHiddenAVPs=None, UseLengthBitInPayload=None, UseOffsetBitInPayload=None, UseSequenceNoInPayload=None):
        """Base class infrastructure that gets a list of lac device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BaseLnsIp (str): optional regex of baseLnsIp
        - BearerCapability (str): optional regex of bearerCapability
        - BearerType (str): optional regex of bearerType
        - Callingnum (str): optional regex of callingnum
        - ControlMsgsRetryCounter (str): optional regex of controlMsgsRetryCounter
        - EnableControlChecksum (str): optional regex of enableControlChecksum
        - EnableDataChecksum (str): optional regex of enableDataChecksum
        - EnableHelloRequest (str): optional regex of enableHelloRequest
        - EnableRedial (str): optional regex of enableRedial
        - FramingCapability (str): optional regex of framingCapability
        - HelloRequestInterval (str): optional regex of helloRequestInterval
        - InitRetransmitInterval (str): optional regex of initRetransmitInterval
        - LacHostName (str): optional regex of lacHostName
        - LacSecret (str): optional regex of lacSecret
        - MaxRedialAttempts (str): optional regex of maxRedialAttempts
        - MaxRetransmitInterval (str): optional regex of maxRetransmitInterval
        - OffsetByte (str): optional regex of offsetByte
        - OffsetLength (str): optional regex of offsetLength
        - ReceiveWindowSize (str): optional regex of receiveWindowSize
        - RedialInterval (str): optional regex of redialInterval
        - TunnelAuthentication (str): optional regex of tunnelAuthentication
        - UdpDestinationPort (str): optional regex of udpDestinationPort
        - UdpSourcePort (str): optional regex of udpSourcePort
        - UseHiddenAVPs (str): optional regex of useHiddenAVPs
        - UseLengthBitInPayload (str): optional regex of useLengthBitInPayload
        - UseOffsetBitInPayload (str): optional regex of useOffsetBitInPayload
        - UseSequenceNoInPayload (str): optional regex of useSequenceNoInPayload

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
