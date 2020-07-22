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


class NetconfServer(Base):
    """Netconf Server emulates a Netconf DUT which connects to a Netconf Client supporting Netconf as per RFC6241/RFC6242
    The NetconfServer class encapsulates a list of netconfServer resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetconfServer.find() method.
    The list can be managed by using the NetconfServer.add() and NetconfServer.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'netconfServer'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'CapabilitiesBase1Dot0': 'capabilitiesBase1Dot0',
        'CapabilitiesBase1Dot1': 'capabilitiesBase1Dot1',
        'CapabilitiesCandidate': 'capabilitiesCandidate',
        'CapabilitiesConfirmedCommit': 'capabilitiesConfirmedCommit',
        'CapabilitiesInterleave': 'capabilitiesInterleave',
        'CapabilitiesNotification': 'capabilitiesNotification',
        'CapabilitiesRollbackOnError': 'capabilitiesRollbackOnError',
        'CapabilitiesStartup': 'capabilitiesStartup',
        'CapabilitiesUrl': 'capabilitiesUrl',
        'CapabilitiesValidate': 'capabilitiesValidate',
        'CapabilitiesWritableRunning': 'capabilitiesWritableRunning',
        'CapabilitiesXpath': 'capabilitiesXpath',
        'ClientIpv4Address': 'clientIpv4Address',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DecryptedCapture': 'decryptedCapture',
        'DescriptiveName': 'descriptiveName',
        'ErrorInfo': 'errorInfo',
        'ErrorPercentage': 'errorPercentage',
        'ErrorSeverity': 'errorSeverity',
        'ErrorTag': 'errorTag',
        'ErrorType': 'errorType',
        'Errors': 'errors',
        'GetConfigReplyXML': 'getConfigReplyXML',
        'IncludeErrorInfo': 'includeErrorInfo',
        'IncludeRxTimestampInReplyMsg': 'includeRxTimestampInReplyMsg',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NetconfSessionState': 'netconfSessionState',
        'OutputDirectory': 'outputDirectory',
        'Password': 'password',
        'PortNumber': 'portNumber',
        'PublicKeyDirectory': 'publicKeyDirectory',
        'PublicKeyFileName': 'publicKeyFileName',
        'ResponseXMLDirectory': 'responseXMLDirectory',
        'SendOkResponse': 'sendOkResponse',
        'SessionStatus': 'sessionStatus',
        'SshAuthenticationMechanism': 'sshAuthenticationMechanism',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'UserName': 'userName',
    }

    def __init__(self, parent):
        super(NetconfServer, self).__init__(parent)

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
    def CapabilitiesBase1Dot0(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether base1.0 support should be advertised in Capabilities.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilitiesBase1Dot0']))

    @property
    def CapabilitiesBase1Dot1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether base1.1 support should be advertised in Capabilities.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilitiesBase1Dot1']))

    @property
    def CapabilitiesCandidate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether supports capability candidate to make changes into an intermediate candidate database. Normally this is preferred over writable-running.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilitiesCandidate']))

    @property
    def CapabilitiesConfirmedCommit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether supports capability confirmed-commit to specify ability to commit a group of commands or none as a batch.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilitiesConfirmedCommit']))

    @property
    def CapabilitiesInterleave(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether supports capability interleave to interleave notifications and responses.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilitiesInterleave']))

    @property
    def CapabilitiesNotification(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether supports capability notification to aynchronously send notifications to Netconf client.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilitiesNotification']))

    @property
    def CapabilitiesRollbackOnError(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether supports capability rollback to rollback partial changes make changes on detection of error during validate or commit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilitiesRollbackOnError']))

    @property
    def CapabilitiesStartup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether supports capability startup to make changes in config persistent on device restart.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilitiesStartup']))

    @property
    def CapabilitiesUrl(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether supports capability url to specify netconf commands using url.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilitiesUrl']))

    @property
    def CapabilitiesValidate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether supports capability validate to specify ability to validate a netconf command prior to commit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilitiesValidate']))

    @property
    def CapabilitiesWritableRunning(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether supports capability writable-running to directly modify running config.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilitiesWritableRunning']))

    @property
    def CapabilitiesXpath(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether supports capability xpath to specify netconf commands and filters using xpath extensions.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilitiesXpath']))

    @property
    def ClientIpv4Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the IPv4 address of the Netconf Client which will connect with this Server.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClientIpv4Address']))

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
    def DecryptedCapture(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether SSH packets for this session will be captured and stored on client in decrypted form. Note that this is not linked to IxNetwork control or data capture which will capture the packets in encrypted format only. The Decrypted Capture can be viewed by either doing right-click on a client where this option is enabled and doing Get Decrypted Capture ( allowed on 5 servers at a time ; each of the captures will be opened in a new Wireshark pop-up) OR by stopping the server and then directly opening it from the configured Output Directory from inside the current run folder/capture. This option can be enabled even when a session is already up in which case the capture will be started from that point of time.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DecryptedCapture']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def ErrorInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Contains protocol or data-model-specific error content.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ErrorInfo']))

    @property
    def ErrorPercentage(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The percentage of requests whose response will be errors
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ErrorPercentage']))

    @property
    def ErrorSeverity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Contains a string identifying the error severity, as determined by the device.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ErrorSeverity']))

    @property
    def ErrorTag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Contains a string identifying the error condition.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ErrorTag']))

    @property
    def ErrorType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Defines the conceptual layer that the error occurred.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ErrorType']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def GetConfigReplyXML(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): File containing the response to a <get-config> request.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GetConfigReplyXML']))

    @property
    def IncludeErrorInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether 'error-info' element should be included in rpc error messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeErrorInfo']))

    @property
    def IncludeRxTimestampInReplyMsg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Whether timestamp of received request messages will be included in the replies
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeRxTimestampInReplyMsg']))

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
    def NetconfSessionState(self):
        """
        Returns
        -------
        - list(str[authenticated | channelOpened | multipleConnections | none | ready | subsystemRequested]): Shows the current state of the Netconf SSH Session. None - Not started. Authenticated - The SSH session has been authenticated by the server using user/password or Key-based authentication. Channel Opened- SSH session is established and SSH Channel has been opened on which data will be sent. Subsystem Requested- Netconf Subsystem has been requested on top of SSH channel. Ready - The SSH session is in Ready state and waiting for Netconf data to be exchanged. Note that this does not mean that NETCONF is in Up state. That is reached only after Netconf Capabilities are negotiated and there is at least one matching Netconf version (1.0 or 1.1) supported on both client and server. Multiple connections - The server has multiple connections
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetconfSessionState'])

    @property
    def OutputDirectory(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Location of Directory in Client where the decrypted capture(if enabled) will be stored.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OutputDirectory']))

    @property
    def Password(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Password for Username/Password mode.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Password']))

    @property
    def PortNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The TCP Port Number the Netconf Server is listening on to which to connect.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PortNumber']))

    @property
    def PublicKeyDirectory(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Directory containing public key file for this session
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PublicKeyDirectory']))

    @property
    def PublicKeyFileName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): File containing public key (e.g. generated using ssh_keygen). For multiple server rows and assymetric public key filenames( which cannot be expressed easily as a pattern) please explore File option in Master Row Pattern Editor by putting the file namesin a .csv and pulling those values into the column cells.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PublicKeyFileName']))

    @property
    def ResponseXMLDirectory(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Directory where Reply XMLs for <get-config> operations are present
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ResponseXMLDirectory']))

    @property
    def SendOkResponse(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether <ok> element should be sent in <rpc-reply> in response to <get-config> requests. If this is unchecked, custom reply based on <get-config> response xml will be sent out
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendOkResponse']))

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def SshAuthenticationMechanism(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The authentication mechanism for connecting to Netconf Client.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SshAuthenticationMechanism']))

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
    def UserName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Username for Username/Password mode and Username for Key-Based authentication mode if applicable.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UserName']))

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Updates netconfServer resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Adds a new netconfServer resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved netconfServer resources using find and the newly added netconfServer resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained netconfServer resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, NetconfSessionState=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves netconfServer resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve netconfServer resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all netconfServer resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NetconfSessionState (list(str[authenticated | channelOpened | multipleConnections | none | ready | subsystemRequested])): Shows the current state of the Netconf SSH Session. None - Not started. Authenticated - The SSH session has been authenticated by the server using user/password or Key-based authentication. Channel Opened- SSH session is established and SSH Channel has been opened on which data will be sent. Subsystem Requested- Netconf Subsystem has been requested on top of SSH channel. Ready - The SSH session is in Ready state and waiting for Netconf data to be exchanged. Note that this does not mean that NETCONF is in Up state. That is reached only after Netconf Capabilities are negotiated and there is at least one matching Netconf version (1.0 or 1.1) supported on both client and server. Multiple connections - The server has multiple connections
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching netconfServer resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of netconfServer data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the netconfServer resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, CapabilitiesBase1Dot0=None, CapabilitiesBase1Dot1=None, CapabilitiesCandidate=None, CapabilitiesConfirmedCommit=None, CapabilitiesInterleave=None, CapabilitiesNotification=None, CapabilitiesRollbackOnError=None, CapabilitiesStartup=None, CapabilitiesUrl=None, CapabilitiesValidate=None, CapabilitiesWritableRunning=None, CapabilitiesXpath=None, ClientIpv4Address=None, DecryptedCapture=None, ErrorInfo=None, ErrorPercentage=None, ErrorSeverity=None, ErrorTag=None, ErrorType=None, GetConfigReplyXML=None, IncludeErrorInfo=None, IncludeRxTimestampInReplyMsg=None, OutputDirectory=None, Password=None, PortNumber=None, PublicKeyDirectory=None, PublicKeyFileName=None, ResponseXMLDirectory=None, SendOkResponse=None, SshAuthenticationMechanism=None, UserName=None):
        """Base class infrastructure that gets a list of netconfServer device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - CapabilitiesBase1Dot0 (str): optional regex of capabilitiesBase1Dot0
        - CapabilitiesBase1Dot1 (str): optional regex of capabilitiesBase1Dot1
        - CapabilitiesCandidate (str): optional regex of capabilitiesCandidate
        - CapabilitiesConfirmedCommit (str): optional regex of capabilitiesConfirmedCommit
        - CapabilitiesInterleave (str): optional regex of capabilitiesInterleave
        - CapabilitiesNotification (str): optional regex of capabilitiesNotification
        - CapabilitiesRollbackOnError (str): optional regex of capabilitiesRollbackOnError
        - CapabilitiesStartup (str): optional regex of capabilitiesStartup
        - CapabilitiesUrl (str): optional regex of capabilitiesUrl
        - CapabilitiesValidate (str): optional regex of capabilitiesValidate
        - CapabilitiesWritableRunning (str): optional regex of capabilitiesWritableRunning
        - CapabilitiesXpath (str): optional regex of capabilitiesXpath
        - ClientIpv4Address (str): optional regex of clientIpv4Address
        - DecryptedCapture (str): optional regex of decryptedCapture
        - ErrorInfo (str): optional regex of errorInfo
        - ErrorPercentage (str): optional regex of errorPercentage
        - ErrorSeverity (str): optional regex of errorSeverity
        - ErrorTag (str): optional regex of errorTag
        - ErrorType (str): optional regex of errorType
        - GetConfigReplyXML (str): optional regex of getConfigReplyXML
        - IncludeErrorInfo (str): optional regex of includeErrorInfo
        - IncludeRxTimestampInReplyMsg (str): optional regex of includeRxTimestampInReplyMsg
        - OutputDirectory (str): optional regex of outputDirectory
        - Password (str): optional regex of password
        - PortNumber (str): optional regex of portNumber
        - PublicKeyDirectory (str): optional regex of publicKeyDirectory
        - PublicKeyFileName (str): optional regex of publicKeyFileName
        - ResponseXMLDirectory (str): optional regex of responseXMLDirectory
        - SendOkResponse (str): optional regex of sendOkResponse
        - SshAuthenticationMechanism (str): optional regex of sshAuthenticationMechanism
        - UserName (str): optional regex of userName

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

    def GetDecryptedCapture(self, *args, **kwargs):
        """Executes the getDecryptedCapture operation on the server.

        If Enable Capture is enabled, this will fetch and open the decrypted capture for selected sessions.

        getDecryptedCapture(Arg2=list, Arg3=number)list
        -----------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - Arg3 (number): The TCP Port number of the server connection for which the capture file is to be fetched. Enter 0 for the first server connection
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getDecryptedCapture', payload=payload, response_object=None)

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

    def ResumeRPCReply(self, *args, **kwargs):
        """Executes the resumeRPCReply operation on the server.

        Resume sending responses to RPC requests.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumeRPCReply(SessionIndices=list)
        -----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        resumeRPCReply(SessionIndices=string)
        -------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        resumeRPCReply(Arg2=list)list
        -----------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('resumeRPCReply', payload=payload, response_object=None)

    def SendRPCReplyWithWrongCharacterCount(self, *args, **kwargs):
        """Executes the sendRPCReplyWithWrongCharacterCount operation on the server.

        The response to the next RPC request will be sent with wrong message Id.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendRPCReplyWithWrongCharacterCount(SessionIndices=list)
        --------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendRPCReplyWithWrongCharacterCount(SessionIndices=string)
        ----------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendRPCReplyWithWrongCharacterCount(Arg2=list)list
        --------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendRPCReplyWithWrongCharacterCount', payload=payload, response_object=None)

    def SendRPCReplyWithWrongMessageId(self, *args, **kwargs):
        """Executes the sendRPCReplyWithWrongMessageId operation on the server.

        The response to the next RPC request will be sent with wrong message Id.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendRPCReplyWithWrongMessageId(SessionIndices=list)
        ---------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendRPCReplyWithWrongMessageId(SessionIndices=string)
        -----------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        sendRPCReplyWithWrongMessageId(Arg2=list)list
        ---------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendRPCReplyWithWrongMessageId', payload=payload, response_object=None)

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

    def StopRPCReplyDropOutstandingRequests(self, *args, **kwargs):
        """Executes the stopRPCReplyDropOutstandingRequests operation on the server.

        Stop sending replies to rpc requests. Drop the outstanding requests so that when Resume RPC Reply is triggered, responses will not be sent for these requests.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopRPCReplyDropOutstandingRequests(SessionIndices=list)
        --------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stopRPCReplyDropOutstandingRequests(SessionIndices=string)
        ----------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        stopRPCReplyDropOutstandingRequests(Arg2=list)list
        --------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopRPCReplyDropOutstandingRequests', payload=payload, response_object=None)

    def StopRPCReplyStoreOutstandingRequests(self, *args, **kwargs):
        """Executes the stopRPCReplyStoreOutstandingRequests operation on the server.

        Stop sending replies to rpc requests. Store the outstanding requests so that when Resume RPC Reply is triggered, responses will be sent for these requests.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopRPCReplyStoreOutstandingRequests(SessionIndices=list)
        ---------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stopRPCReplyStoreOutstandingRequests(SessionIndices=string)
        -----------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        stopRPCReplyStoreOutstandingRequests(Arg2=list)list
        ---------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopRPCReplyStoreOutstandingRequests', payload=payload, response_object=None)
