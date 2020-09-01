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


class RsvpteIf(Base):
    """Rsvp Neighbor (Device) level Configuration
    The RsvpteIf class encapsulates a list of rsvpteIf resources that are managed by the user.
    A list of resources can be retrieved from the server using the RsvpteIf.find() method.
    The list can be managed by using the RsvpteIf.add() and RsvpteIf.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'rsvpteIf'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'ActualRestartTime': 'actualRestartTime',
        'AdvertisedRestartTime': 'advertisedRestartTime',
        'AuthenticationAlgorithm': 'authenticationAlgorithm',
        'AuthenticationKeyForReceivedPackets': 'authenticationKeyForReceivedPackets',
        'AuthenticationKeyForSentPackets': 'authenticationKeyForSentPackets',
        'AuthenticationKeyIdentifier': 'authenticationKeyIdentifier',
        'AutoGenerateAuthenticationKeyIdentifier': 'autoGenerateAuthenticationKeyIdentifier',
        'BundleMessageThresholdTime': 'bundleMessageThresholdTime',
        'CheckIntegrityForReceivedPackets': 'checkIntegrityForReceivedPackets',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DutIp': 'dutIp',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'EnableBundleMessageSending': 'enableBundleMessageSending',
        'EnableBundleMessageThresholdTimer': 'enableBundleMessageThresholdTimer',
        'EnableGracefulRestartHelperMode': 'enableGracefulRestartHelperMode',
        'EnableGracefulRestartRestartingMode': 'enableGracefulRestartRestartingMode',
        'EnableHelloExtension': 'enableHelloExtension',
        'EnableRefreshReduction': 'enableRefreshReduction',
        'Errors': 'errors',
        'GenerateSequenceNumberBasedOnRealTime': 'generateSequenceNumberBasedOnRealTime',
        'HandshakeRequired': 'handshakeRequired',
        'HelloInterval': 'helloInterval',
        'HelloTimeoutMultiplier': 'helloTimeoutMultiplier',
        'InitialSequenceNumber': 'initialSequenceNumber',
        'LabelReqRefCount': 'labelReqRefCount',
        'LabelSpaceEnd': 'labelSpaceEnd',
        'LabelSpaceStart': 'labelSpaceStart',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NumberOfRestarts': 'numberOfRestarts',
        'OurIp': 'ourIp',
        'RecoveryTime': 'recoveryTime',
        'RestartStartTime': 'restartStartTime',
        'RestartUpTime': 'restartUpTime',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'SummaryRefreshInterval': 'summaryRefreshInterval',
        'UseSameAuthenticationKeyForPeer': 'useSameAuthenticationKeyForPeer',
        'UsingGatewayIp': 'usingGatewayIp',
    }

    def __init__(self, parent):
        super(RsvpteIf, self).__init__(parent)

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import LearnedInfo
        return LearnedInfo(self)

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
    def ActualRestartTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Actual Restart Time (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActualRestartTime']))

    @property
    def AdvertisedRestartTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertised Restart Time (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertisedRestartTime']))

    @property
    def AuthenticationAlgorithm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Authentication Algorithm
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuthenticationAlgorithm']))

    @property
    def AuthenticationKeyForReceivedPackets(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Authentication Key for Received Packets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuthenticationKeyForReceivedPackets']))

    @property
    def AuthenticationKeyForSentPackets(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Authentication Key for Sent Packets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuthenticationKeyForSentPackets']))

    @property
    def AuthenticationKeyIdentifier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Authentication Key Identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuthenticationKeyIdentifier']))

    @property
    def AutoGenerateAuthenticationKeyIdentifier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Generate Authentication Key Identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoGenerateAuthenticationKeyIdentifier']))

    @property
    def BundleMessageThresholdTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bundle Message Threshold Time (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BundleMessageThresholdTime']))

    @property
    def CheckIntegrityForReceivedPackets(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Check Integrity for Received Packets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CheckIntegrityForReceivedPackets']))

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
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DutIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DUT IP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DutIp']))

    @property
    def EnableBfdRegistration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable BFD Registration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBfdRegistration']))

    @property
    def EnableBundleMessageSending(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Bundle Message Sending
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBundleMessageSending']))

    @property
    def EnableBundleMessageThresholdTimer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Bundle Message Threshold Timer
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBundleMessageThresholdTimer']))

    @property
    def EnableGracefulRestartHelperMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Helper-Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableGracefulRestartHelperMode']))

    @property
    def EnableGracefulRestartRestartingMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Restarting-Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableGracefulRestartRestartingMode']))

    @property
    def EnableHelloExtension(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Hello Extension
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableHelloExtension']))

    @property
    def EnableRefreshReduction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Refresh Reduction
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRefreshReduction']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def GenerateSequenceNumberBasedOnRealTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Generate Sequence Number Based on Real Time
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GenerateSequenceNumberBasedOnRealTime']))

    @property
    def HandshakeRequired(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Handshake Required
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HandshakeRequired']))

    @property
    def HelloInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hello Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HelloInterval']))

    @property
    def HelloTimeoutMultiplier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hello Timeout Multiplier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HelloTimeoutMultiplier']))

    @property
    def InitialSequenceNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Initial Sequence Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InitialSequenceNumber']))

    @property
    def LabelReqRefCount(self):
        """
        Returns
        -------
        - number: Number of Label Req in RSVP-TE DG
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelReqRefCount'])
    @LabelReqRefCount.setter
    def LabelReqRefCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelReqRefCount'], value)

    @property
    def LabelSpaceEnd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Space End
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelSpaceEnd']))

    @property
    def LabelSpaceStart(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Space Start
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelSpaceStart']))

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
    def NumberOfRestarts(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of Restarts
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumberOfRestarts']))

    @property
    def OurIp(self):
        """
        Returns
        -------
        - list(str): Local IP
        """
        return self._get_attribute(self._SDM_ATT_MAP['OurIp'])

    @property
    def RecoveryTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Recovery Time (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RecoveryTime']))

    @property
    def RestartStartTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Restart Start Time (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RestartStartTime']))

    @property
    def RestartUpTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Restart Up Time (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RestartUpTime']))

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
    def SummaryRefreshInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Summary Refresh Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SummaryRefreshInterval']))

    @property
    def UseSameAuthenticationKeyForPeer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Same Authentication Key for Peer
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseSameAuthenticationKeyForPeer']))

    @property
    def UsingGatewayIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Using Gateway IP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UsingGatewayIp']))

    def update(self, ConnectedVia=None, LabelReqRefCount=None, Multiplier=None, Name=None, StackedLayers=None):
        """Updates rsvpteIf resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - LabelReqRefCount (number): Number of Label Req in RSVP-TE DG
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, LabelReqRefCount=None, Multiplier=None, Name=None, StackedLayers=None):
        """Adds a new rsvpteIf resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - LabelReqRefCount (number): Number of Label Req in RSVP-TE DG
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved rsvpteIf resources using find and the newly added rsvpteIf resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained rsvpteIf resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, LabelReqRefCount=None, Multiplier=None, Name=None, OurIp=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves rsvpteIf resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rsvpteIf resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rsvpteIf resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - LabelReqRefCount (number): Number of Label Req in RSVP-TE DG
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - OurIp (list(str)): Local IP
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching rsvpteIf resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rsvpteIf data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rsvpteIf resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, ActualRestartTime=None, AdvertisedRestartTime=None, AuthenticationAlgorithm=None, AuthenticationKeyForReceivedPackets=None, AuthenticationKeyForSentPackets=None, AuthenticationKeyIdentifier=None, AutoGenerateAuthenticationKeyIdentifier=None, BundleMessageThresholdTime=None, CheckIntegrityForReceivedPackets=None, DutIp=None, EnableBfdRegistration=None, EnableBundleMessageSending=None, EnableBundleMessageThresholdTimer=None, EnableGracefulRestartHelperMode=None, EnableGracefulRestartRestartingMode=None, EnableHelloExtension=None, EnableRefreshReduction=None, GenerateSequenceNumberBasedOnRealTime=None, HandshakeRequired=None, HelloInterval=None, HelloTimeoutMultiplier=None, InitialSequenceNumber=None, LabelSpaceEnd=None, LabelSpaceStart=None, NumberOfRestarts=None, RecoveryTime=None, RestartStartTime=None, RestartUpTime=None, SummaryRefreshInterval=None, UseSameAuthenticationKeyForPeer=None, UsingGatewayIp=None):
        """Base class infrastructure that gets a list of rsvpteIf device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ActualRestartTime (str): optional regex of actualRestartTime
        - AdvertisedRestartTime (str): optional regex of advertisedRestartTime
        - AuthenticationAlgorithm (str): optional regex of authenticationAlgorithm
        - AuthenticationKeyForReceivedPackets (str): optional regex of authenticationKeyForReceivedPackets
        - AuthenticationKeyForSentPackets (str): optional regex of authenticationKeyForSentPackets
        - AuthenticationKeyIdentifier (str): optional regex of authenticationKeyIdentifier
        - AutoGenerateAuthenticationKeyIdentifier (str): optional regex of autoGenerateAuthenticationKeyIdentifier
        - BundleMessageThresholdTime (str): optional regex of bundleMessageThresholdTime
        - CheckIntegrityForReceivedPackets (str): optional regex of checkIntegrityForReceivedPackets
        - DutIp (str): optional regex of dutIp
        - EnableBfdRegistration (str): optional regex of enableBfdRegistration
        - EnableBundleMessageSending (str): optional regex of enableBundleMessageSending
        - EnableBundleMessageThresholdTimer (str): optional regex of enableBundleMessageThresholdTimer
        - EnableGracefulRestartHelperMode (str): optional regex of enableGracefulRestartHelperMode
        - EnableGracefulRestartRestartingMode (str): optional regex of enableGracefulRestartRestartingMode
        - EnableHelloExtension (str): optional regex of enableHelloExtension
        - EnableRefreshReduction (str): optional regex of enableRefreshReduction
        - GenerateSequenceNumberBasedOnRealTime (str): optional regex of generateSequenceNumberBasedOnRealTime
        - HandshakeRequired (str): optional regex of handshakeRequired
        - HelloInterval (str): optional regex of helloInterval
        - HelloTimeoutMultiplier (str): optional regex of helloTimeoutMultiplier
        - InitialSequenceNumber (str): optional regex of initialSequenceNumber
        - LabelSpaceEnd (str): optional regex of labelSpaceEnd
        - LabelSpaceStart (str): optional regex of labelSpaceStart
        - NumberOfRestarts (str): optional regex of numberOfRestarts
        - RecoveryTime (str): optional regex of recoveryTime
        - RestartStartTime (str): optional regex of restartStartTime
        - RestartUpTime (str): optional regex of restartUpTime
        - SummaryRefreshInterval (str): optional regex of summaryRefreshInterval
        - UseSameAuthenticationKeyForPeer (str): optional regex of useSameAuthenticationKeyForPeer
        - UsingGatewayIp (str): optional regex of usingGatewayIp

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

    def GetLearnedInfo(self, *args, **kwargs):
        """Executes the getLearnedInfo operation on the server.

        Get Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getLearnedInfo(SessionIndices=list)
        -----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getLearnedInfo(SessionIndices=string)
        -------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getLearnedInfo(Arg2=list)list
        -----------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getLearnedInfo', payload=payload, response_object=None)

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

    def RestartNeighbor(self, *args, **kwargs):
        """Executes the restartNeighbor operation on the server.

        Restart Neighbor

        restartNeighbor(Arg2=list)list
        ------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartNeighbor', payload=payload, response_object=None)

    def RsvpRestartNeighbor(self, *args, **kwargs):
        """Executes the rsvpRestartNeighbor operation on the server.

        Gracefully restart selected Neighbors

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        rsvpRestartNeighbor(SessionIndices=list)
        ----------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        rsvpRestartNeighbor(SessionIndices=string)
        ------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('rsvpRestartNeighbor', payload=payload, response_object=None)

    def RsvpResumeHello(self, *args, **kwargs):
        """Executes the rsvpResumeHello operation on the server.

        Resume sending Hello messages from selected Neighbors

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        rsvpResumeHello(SessionIndices=list)
        ------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        rsvpResumeHello(SessionIndices=string)
        --------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('rsvpResumeHello', payload=payload, response_object=None)

    def RsvpStartSRefresh(self, *args, **kwargs):
        """Executes the rsvpStartSRefresh operation on the server.

        Start sending SRefresh messages from selected Neighbors

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        rsvpStartSRefresh(SessionIndices=list)
        --------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        rsvpStartSRefresh(SessionIndices=string)
        ----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('rsvpStartSRefresh', payload=payload, response_object=None)

    def RsvpStopHello(self, *args, **kwargs):
        """Executes the rsvpStopHello operation on the server.

        Stop sending Hello messages from selected Neighbors

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        rsvpStopHello(SessionIndices=list)
        ----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        rsvpStopHello(SessionIndices=string)
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
        return self._execute('rsvpStopHello', payload=payload, response_object=None)

    def RsvpStopSRefresh(self, *args, **kwargs):
        """Executes the rsvpStopSRefresh operation on the server.

        Stop sending SRefresh messages from selected Neighbors

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        rsvpStopSRefresh(SessionIndices=list)
        -------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        rsvpStopSRefresh(SessionIndices=string)
        ---------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('rsvpStopSRefresh', payload=payload, response_object=None)

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

    def StartHello(self, *args, **kwargs):
        """Executes the startHello operation on the server.

        Start Hello

        startHello(Arg2=list)list
        -------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startHello', payload=payload, response_object=None)

    def StartSRefresh(self, *args, **kwargs):
        """Executes the startSRefresh operation on the server.

        Start SRefresh

        startSRefresh(Arg2=list)list
        ----------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startSRefresh', payload=payload, response_object=None)

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

    def StopHello(self, *args, **kwargs):
        """Executes the stopHello operation on the server.

        Stop Hello

        stopHello(Arg2=list)list
        ------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopHello', payload=payload, response_object=None)

    def StopSRefresh(self, *args, **kwargs):
        """Executes the stopSRefresh operation on the server.

        Stop SRefresh

        stopSRefresh(Arg2=list)list
        ---------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopSRefresh', payload=payload, response_object=None)
