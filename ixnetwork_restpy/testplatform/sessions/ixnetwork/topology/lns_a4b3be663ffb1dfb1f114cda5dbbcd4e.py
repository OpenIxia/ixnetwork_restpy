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


class Lns(Base):
    """L2TP Network Server protocol.
    The Lns class encapsulates a list of lns resources that are managed by the user.
    A list of resources can be retrieved from the server using the Lns.find() method.
    The list can be managed by using the Lns.add() and Lns.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'lns'
    _SDM_ATT_MAP = {
        'BearerCapability': 'bearerCapability',
        'BearerType': 'bearerType',
        'ConnectedVia': 'connectedVia',
        'ControlMsgsRetryCounter': 'controlMsgsRetryCounter',
        'Count': 'count',
        'CredentialsCount': 'credentialsCount',
        'DescriptiveName': 'descriptiveName',
        'EnableControlChecksum': 'enableControlChecksum',
        'EnableDataChecksum': 'enableDataChecksum',
        'EnableExcludeHdlc': 'enableExcludeHdlc',
        'EnableHelloRequest': 'enableHelloRequest',
        'EnablePeriodicCSURQ': 'enablePeriodicCSURQ',
        'Errors': 'errors',
        'FramingCapability': 'framingCapability',
        'HelloRequestInterval': 'helloRequestInterval',
        'InitRetransmitInterval': 'initRetransmitInterval',
        'LacHostName': 'lacHostName',
        'LacSecret': 'lacSecret',
        'LnsHostName': 'lnsHostName',
        'MaxRetransmitInterval': 'maxRetransmitInterval',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NoCallTimeout': 'noCallTimeout',
        'OffsetByte': 'offsetByte',
        'OffsetLength': 'offsetLength',
        'PeriodicCSURQInterval': 'periodicCSURQInterval',
        'ReceiveWindowSize': 'receiveWindowSize',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TunnelAuthentication': 'tunnelAuthentication',
        'UdpDestinationPort': 'udpDestinationPort',
        'UdpSourcePort': 'udpSourcePort',
        'UseHiddenAVPs': 'useHiddenAVPs',
        'UseLengthBitInPayload': 'useLengthBitInPayload',
        'UseOffsetBitInPayload': 'useOffsetBitInPayload',
        'UseSequenceNoInPayload': 'useSequenceNoInPayload',
    }

    def __init__(self, parent):
        super(Lns, self).__init__(parent)

    @property
    def LnsAuthCredentials(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lnsauthcredentials_caa048d94ca4e6927df8160f32c829bf.LnsAuthCredentials): An instance of the LnsAuthCredentials class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lnsauthcredentials_caa048d94ca4e6927df8160f32c829bf import LnsAuthCredentials
        return LnsAuthCredentials(self)._select()

    @property
    def Pppoxserver(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserver_01e736fa724c12e1c2636295184e449c.Pppoxserver): An instance of the Pppoxserver class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserver_01e736fa724c12e1c2636295184e449c import Pppoxserver
        return Pppoxserver(self)

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
    def CredentialsCount(self):
        """
        Returns
        -------
        - number: Number of L2TP authentication credentials the LNS accepts for multiple tunnels establishment.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CredentialsCount'])
    @CredentialsCount.setter
    def CredentialsCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CredentialsCount'], value)

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
    def EnablePeriodicCSURQ(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, CSURQ will be sent at CSURQ interval periodically
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnablePeriodicCSURQ']))

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
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the hostname used in authentication.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LacHostName']))

    @property
    def LacSecret(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L2TP secret to be used in authentication
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LacSecret']))

    @property
    def LnsHostName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L2TP hostname sent by Ixia port when acting as LNS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LnsHostName']))

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
    def NoCallTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for no call establishment, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NoCallTimeout']))

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
    def PeriodicCSURQInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CSURQ interval, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeriodicCSURQInterval']))

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

    def update(self, ConnectedVia=None, CredentialsCount=None, EnableExcludeHdlc=None, Multiplier=None, Name=None, StackedLayers=None):
        """Updates lns resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - CredentialsCount (number): Number of L2TP authentication credentials the LNS accepts for multiple tunnels establishment.
        - EnableExcludeHdlc (bool): If checked, HDLC header is not encoded in the L2TP packets.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, CredentialsCount=None, EnableExcludeHdlc=None, Multiplier=None, Name=None, StackedLayers=None):
        """Adds a new lns resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - CredentialsCount (number): Number of L2TP authentication credentials the LNS accepts for multiple tunnels establishment.
        - EnableExcludeHdlc (bool): If checked, HDLC header is not encoded in the L2TP packets.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved lns resources using find and the newly added lns resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained lns resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, CredentialsCount=None, DescriptiveName=None, EnableExcludeHdlc=None, Errors=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves lns resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lns resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lns resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - CredentialsCount (number): Number of L2TP authentication credentials the LNS accepts for multiple tunnels establishment.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableExcludeHdlc (bool): If checked, HDLC header is not encoded in the L2TP packets.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching lns resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lns data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lns resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, BearerCapability=None, BearerType=None, ControlMsgsRetryCounter=None, EnableControlChecksum=None, EnableDataChecksum=None, EnableHelloRequest=None, EnablePeriodicCSURQ=None, FramingCapability=None, HelloRequestInterval=None, InitRetransmitInterval=None, LacHostName=None, LacSecret=None, LnsHostName=None, MaxRetransmitInterval=None, NoCallTimeout=None, OffsetByte=None, OffsetLength=None, PeriodicCSURQInterval=None, ReceiveWindowSize=None, TunnelAuthentication=None, UdpDestinationPort=None, UdpSourcePort=None, UseHiddenAVPs=None, UseLengthBitInPayload=None, UseOffsetBitInPayload=None, UseSequenceNoInPayload=None):
        """Base class infrastructure that gets a list of lns device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BearerCapability (str): optional regex of bearerCapability
        - BearerType (str): optional regex of bearerType
        - ControlMsgsRetryCounter (str): optional regex of controlMsgsRetryCounter
        - EnableControlChecksum (str): optional regex of enableControlChecksum
        - EnableDataChecksum (str): optional regex of enableDataChecksum
        - EnableHelloRequest (str): optional regex of enableHelloRequest
        - EnablePeriodicCSURQ (str): optional regex of enablePeriodicCSURQ
        - FramingCapability (str): optional regex of framingCapability
        - HelloRequestInterval (str): optional regex of helloRequestInterval
        - InitRetransmitInterval (str): optional regex of initRetransmitInterval
        - LacHostName (str): optional regex of lacHostName
        - LacSecret (str): optional regex of lacSecret
        - LnsHostName (str): optional regex of lnsHostName
        - MaxRetransmitInterval (str): optional regex of maxRetransmitInterval
        - NoCallTimeout (str): optional regex of noCallTimeout
        - OffsetByte (str): optional regex of offsetByte
        - OffsetLength (str): optional regex of offsetLength
        - PeriodicCSURQInterval (str): optional regex of periodicCSURQInterval
        - ReceiveWindowSize (str): optional regex of receiveWindowSize
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

    def SendCSURQ(self, *args, **kwargs):
        """Executes the sendCSURQ operation on the server.

        Sends CSURQ from LNS

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendCSURQ(RemoteSessionId=string, TunnelId=number)
        --------------------------------------------------
        - RemoteSessionId (str): This parameter requires a remoteSessionId of type kString
        - TunnelId (number): This parameter requires a tunnelId of type kInteger

        sendCSURQ(RemoteSessionId=string, TunnelId=number, SessionIndices=list)
        -----------------------------------------------------------------------
        - RemoteSessionId (str): This parameter requires a remoteSessionId of type kString
        - TunnelId (number): This parameter requires a tunnelId of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendCSURQ(SessionIndices=string, RemoteSessionId=string, TunnelId=number)
        -------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a remoteSessionId of type kString
        - RemoteSessionId (str): This parameter requires a tunnelId of type kInteger
        - TunnelId (number): This parameter requires a string of session numbers 1-4;6;7-12

        sendCSURQ(Arg2=list, Arg3=string, Arg4=number)list
        --------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group for the corresponding device instances whose IPv4 addresses are used as the source of the request messages.
        - Arg3 (str): Session id for which CSURQ will be sent
        - Arg4 (number): Tunnel id for which CSURQ will be sent
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendCSURQ', payload=payload, response_object=None)

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
