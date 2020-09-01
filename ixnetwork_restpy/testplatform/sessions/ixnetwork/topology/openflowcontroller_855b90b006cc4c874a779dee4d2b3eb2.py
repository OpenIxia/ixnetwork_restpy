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


class OpenFlowController(Base):
    """OpenFlow Session (Device) level Configuration
    The OpenFlowController class encapsulates a list of openFlowController resources that are managed by the user.
    A list of resources can be retrieved from the server using the OpenFlowController.find() method.
    The list can be managed by using the OpenFlowController.add() and OpenFlowController.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'openFlowController'
    _SDM_ATT_MAP = {
        'AcceptUnconfiguredChannel': 'acceptUnconfiguredChannel',
        'Active': 'active',
        'AuxConnTimeout': 'auxConnTimeout',
        'AuxNonHelloStartupOption': 'auxNonHelloStartupOption',
        'BadVersionErrorAction': 'badVersionErrorAction',
        'ConnectedVia': 'connectedVia',
        'ControllerLocalIp': 'controllerLocalIp',
        'Count': 'count',
        'DelFlowsAtStartup': 'delFlowsAtStartup',
        'DescriptiveName': 'descriptiveName',
        'DirectoryName': 'directoryName',
        'EchoInterval': 'echoInterval',
        'EchoTimeOut': 'echoTimeOut',
        'Errors': 'errors',
        'FeatRequestTimeout': 'featRequestTimeout',
        'FeatureRquestTimeoutAction': 'featureRquestTimeoutAction',
        'FileCaCertificate': 'fileCaCertificate',
        'FileCertificate': 'fileCertificate',
        'FilePrivKey': 'filePrivKey',
        'InstallFlowForLLDP': 'installFlowForLLDP',
        'InstallLLDPFlow': 'installLLDPFlow',
        'LLDPDestinactionMac': 'lLDPDestinactionMac',
        'LldpDstMacAddress': 'lldpDstMacAddress',
        'ModeOfConnection': 'modeOfConnection',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NumberOfChannels': 'numberOfChannels',
        'PeriodicEcho': 'periodicEcho',
        'PeriodicLLDP': 'periodicLLDP',
        'PeriodicLLDPInterval': 'periodicLLDPInterval',
        'ResponseTimeout': 'responseTimeout',
        'SendPortFeatureAtStartup': 'sendPortFeatureAtStartup',
        'SessionStatus': 'sessionStatus',
        'SetAsyncConfig': 'setAsyncConfig',
        'SetSwitchConfig': 'setSwitchConfig',
        'StackedLayers': 'stackedLayers',
        'StartupEmptyTableFeatureRequest': 'startupEmptyTableFeatureRequest',
        'StartupFeatureRequest': 'startupFeatureRequest',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TcpPort': 'tcpPort',
        'TimeoutOption': 'timeoutOption',
        'TimeoutOptionValue': 'timeoutOptionValue',
        'TlsVersion': 'tlsVersion',
        'TriggerLldp': 'triggerLldp',
        'TypeOfConnection': 'typeOfConnection',
        'Version': 'version',
        'VersionSupported': 'versionSupported',
    }

    def __init__(self, parent):
        super(OpenFlowController, self).__init__(parent)

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
    def LearnedInfoUpdate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfoupdate_b6503122c0a4a58877467964920e27b5.LearnedInfoUpdate): An instance of the LearnedInfoUpdate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfoupdate_b6503122c0a4a58877467964920e27b5 import LearnedInfoUpdate
        return LearnedInfoUpdate(self)

    @property
    def OpenFlowChannel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowchannel_97012d0be69c2c7c1b2ca179dbbe39ac.OpenFlowChannel): An instance of the OpenFlowChannel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowchannel_97012d0be69c2c7c1b2ca179dbbe39ac import OpenFlowChannel
        return OpenFlowChannel(self)

    @property
    def AcceptUnconfiguredChannel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, un-configured channels are accepted for this interface.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AcceptUnconfiguredChannel']))

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
    def AuxConnTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The inactive time in milliseconds after which the auxiliary connection will timeout and close.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuxConnTimeout']))

    @property
    def AuxNonHelloStartupOption(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the action from the following options for non-hello message when connection is established. The options are: 1) Accept Connection 2) Return Error
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuxNonHelloStartupOption']))

    @property
    def BadVersionErrorAction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the action to be performed when an invalid version error occurs. The options are: 1) Re-send Hello 2) Terminate Connection
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BadVersionErrorAction']))

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
    def ControllerLocalIp(self):
        """
        Returns
        -------
        - list(str): The local IP address of the interface. This field is auto-populated and cannot be changed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ControllerLocalIp'])

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DelFlowsAtStartup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, Controller sends an OpenFlow delete message (for all wild card entries) at start-up. This deletes all existing flows in the DUT.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelFlowsAtStartup']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DirectoryName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Location of Directory in Client where the Certificate and Key Files are available
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DirectoryName']))

    @property
    def EchoInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The periodic interval in seconds at which the Interface sends Echo Request Packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EchoInterval']))

    @property
    def EchoTimeOut(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the echo request times out when they have been sent for a specified number of times, or when the time value specified has lapsed, but no response is received
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EchoTimeOut']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def FeatRequestTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The inactive time in milliseconds after which the feature request will timeout.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FeatRequestTimeout']))

    @property
    def FeatureRquestTimeoutAction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the action to be performed when a feature request times out. The options are: 1) Re-send Feature Request 2) Terminate Connection
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FeatureRquestTimeoutAction']))

    @property
    def FileCaCertificate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Browse and upload a CA Certificate file for TLS session.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FileCaCertificate']))

    @property
    def FileCertificate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Browse and upload the certificate file for TLS session.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FileCertificate']))

    @property
    def FilePrivKey(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Browse and upload the private key file for TLS session.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FilePrivKey']))

    @property
    def InstallFlowForLLDP(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the controller sends add flow to each connected switch in such a way that each switch forwards LLDP packet to all other connected switches.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InstallFlowForLLDP']))

    @property
    def InstallLLDPFlow(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, LLDP Flow is installed.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InstallLLDPFlow']))

    @property
    def LLDPDestinactionMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the LLDP Destination MAC address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LLDPDestinactionMac']))

    @property
    def LldpDstMacAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The destination MAC Address for the LLDP packet.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LldpDstMacAddress']))

    @property
    def ModeOfConnection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The mode of connection used for the Interface. Options include: 1) Active 2) Passive 3) Mixed
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ModeOfConnection']))

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
    def NumberOfChannels(self):
        """
        Returns
        -------
        - number: Total number of OpenFlow channels to be added for this protocol interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfChannels'])
    @NumberOfChannels.setter
    def NumberOfChannels(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfChannels'], value)

    @property
    def PeriodicEcho(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the Interface sends echo requests periodically to keep the OpenFlow session connected.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeriodicEcho']))

    @property
    def PeriodicLLDP(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the interface sends LLDP packets periodically to discover new links.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeriodicLLDP']))

    @property
    def PeriodicLLDPInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The periodic interval in milliseconds at which the Interface sends LLDP packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeriodicLLDPInterval']))

    @property
    def ResponseTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The time in milliseconds after which the trigger request times out, if no response is received
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ResponseTimeout']))

    @property
    def SendPortFeatureAtStartup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, port Description request is sent when the connection is established
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendPortFeatureAtStartup']))

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def SetAsyncConfig(self):
        """
        Returns
        -------
        - bool: Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetAsyncConfig'])
    @SetAsyncConfig.setter
    def SetAsyncConfig(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetAsyncConfig'], value)

    @property
    def SetSwitchConfig(self):
        """
        Returns
        -------
        - bool: Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetSwitchConfig'])
    @SetSwitchConfig.setter
    def SetSwitchConfig(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetSwitchConfig'], value)

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
    def StartupEmptyTableFeatureRequest(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the Table Feature Request is sent at start up.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartupEmptyTableFeatureRequest']))

    @property
    def StartupFeatureRequest(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, port feature request is sent when the connection is established.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartupFeatureRequest']))

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
    def TcpPort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the TCP port for this interface
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TcpPort']))

    @property
    def TimeoutOption(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The types of timeout options supported. Choose one of the following: 1) Multiplier 2) Timeout Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeoutOption']))

    @property
    def TimeoutOptionValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value specified for the selected Timeout option.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeoutOptionValue']))

    @property
    def TlsVersion(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TLS version selection
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TlsVersion']))

    @property
    def TriggerLldp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, LLDP is triggered
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TriggerLldp']))

    @property
    def TypeOfConnection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The type of connection used for the Interface. Options include: 1) TCP 2) TLS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TypeOfConnection']))

    @property
    def Version(self):
        """
        Returns
        -------
        - number: Implementation Version
        """
        return self._get_attribute(self._SDM_ATT_MAP['Version'])

    @property
    def VersionSupported(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the supported OpenFlow version number.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VersionSupported']))

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, NumberOfChannels=None, SetAsyncConfig=None, SetSwitchConfig=None, StackedLayers=None):
        """Updates openFlowController resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfChannels (number): Total number of OpenFlow channels to be added for this protocol interface.
        - SetAsyncConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
        - SetSwitchConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, NumberOfChannels=None, SetAsyncConfig=None, SetSwitchConfig=None, StackedLayers=None):
        """Adds a new openFlowController resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfChannels (number): Total number of OpenFlow channels to be added for this protocol interface.
        - SetAsyncConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
        - SetSwitchConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved openFlowController resources using find and the newly added openFlowController resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained openFlowController resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, ControllerLocalIp=None, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, NumberOfChannels=None, SessionStatus=None, SetAsyncConfig=None, SetSwitchConfig=None, StackedLayers=None, StateCounts=None, Status=None, Version=None):
        """Finds and retrieves openFlowController resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve openFlowController resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all openFlowController resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - ControllerLocalIp (list(str)): The local IP address of the interface. This field is auto-populated and cannot be changed.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfChannels (number): Total number of OpenFlow channels to be added for this protocol interface.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - SetAsyncConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
        - SetSwitchConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - Version (number): Implementation Version

        Returns
        -------
        - self: This instance with matching openFlowController resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of openFlowController data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the openFlowController resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, AcceptUnconfiguredChannel=None, Active=None, AuxConnTimeout=None, AuxNonHelloStartupOption=None, BadVersionErrorAction=None, DelFlowsAtStartup=None, DirectoryName=None, EchoInterval=None, EchoTimeOut=None, FeatRequestTimeout=None, FeatureRquestTimeoutAction=None, FileCaCertificate=None, FileCertificate=None, FilePrivKey=None, InstallFlowForLLDP=None, InstallLLDPFlow=None, LLDPDestinactionMac=None, LldpDstMacAddress=None, ModeOfConnection=None, PeriodicEcho=None, PeriodicLLDP=None, PeriodicLLDPInterval=None, ResponseTimeout=None, SendPortFeatureAtStartup=None, StartupEmptyTableFeatureRequest=None, StartupFeatureRequest=None, TcpPort=None, TimeoutOption=None, TimeoutOptionValue=None, TlsVersion=None, TriggerLldp=None, TypeOfConnection=None, VersionSupported=None):
        """Base class infrastructure that gets a list of openFlowController device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AcceptUnconfiguredChannel (str): optional regex of acceptUnconfiguredChannel
        - Active (str): optional regex of active
        - AuxConnTimeout (str): optional regex of auxConnTimeout
        - AuxNonHelloStartupOption (str): optional regex of auxNonHelloStartupOption
        - BadVersionErrorAction (str): optional regex of badVersionErrorAction
        - DelFlowsAtStartup (str): optional regex of delFlowsAtStartup
        - DirectoryName (str): optional regex of directoryName
        - EchoInterval (str): optional regex of echoInterval
        - EchoTimeOut (str): optional regex of echoTimeOut
        - FeatRequestTimeout (str): optional regex of featRequestTimeout
        - FeatureRquestTimeoutAction (str): optional regex of featureRquestTimeoutAction
        - FileCaCertificate (str): optional regex of fileCaCertificate
        - FileCertificate (str): optional regex of fileCertificate
        - FilePrivKey (str): optional regex of filePrivKey
        - InstallFlowForLLDP (str): optional regex of installFlowForLLDP
        - InstallLLDPFlow (str): optional regex of installLLDPFlow
        - LLDPDestinactionMac (str): optional regex of lLDPDestinactionMac
        - LldpDstMacAddress (str): optional regex of lldpDstMacAddress
        - ModeOfConnection (str): optional regex of modeOfConnection
        - PeriodicEcho (str): optional regex of periodicEcho
        - PeriodicLLDP (str): optional regex of periodicLLDP
        - PeriodicLLDPInterval (str): optional regex of periodicLLDPInterval
        - ResponseTimeout (str): optional regex of responseTimeout
        - SendPortFeatureAtStartup (str): optional regex of sendPortFeatureAtStartup
        - StartupEmptyTableFeatureRequest (str): optional regex of startupEmptyTableFeatureRequest
        - StartupFeatureRequest (str): optional regex of startupFeatureRequest
        - TcpPort (str): optional regex of tcpPort
        - TimeoutOption (str): optional regex of timeoutOption
        - TimeoutOptionValue (str): optional regex of timeoutOptionValue
        - TlsVersion (str): optional regex of tlsVersion
        - TriggerLldp (str): optional regex of triggerLldp
        - TypeOfConnection (str): optional regex of typeOfConnection
        - VersionSupported (str): optional regex of versionSupported

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

    def ClearAllLearnedInfo(self, *args, **kwargs):
        """Executes the clearAllLearnedInfo operation on the server.

        Clear All Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearAllLearnedInfo(SessionIndices=list)
        ----------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        clearAllLearnedInfo(SessionIndices=string)
        ------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        clearAllLearnedInfo(Arg2=list)list
        ----------------------------------
        - Arg2 (list(number)): List of OF Channel into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearAllLearnedInfo', payload=payload, response_object=None)

    def GetOFChannelLearnedInfo(self, *args, **kwargs):
        """Executes the getOFChannelLearnedInfo operation on the server.

        Get OF Channel Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getOFChannelLearnedInfo(SessionIndices=list)
        --------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getOFChannelLearnedInfo(SessionIndices=string)
        ----------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getOFChannelLearnedInfo(Arg2=list)list
        --------------------------------------
        - Arg2 (list(number)): List of OF Channel into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getOFChannelLearnedInfo', payload=payload, response_object=None)

    def GetOFTopologyLearnedInfo(self, *args, **kwargs):
        """Executes the getOFTopologyLearnedInfo operation on the server.

        Get OF Topology Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getOFTopologyLearnedInfo(SessionIndices=list)
        ---------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getOFTopologyLearnedInfo(SessionIndices=string)
        -----------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getOFTopologyLearnedInfo(Arg2=list)list
        ---------------------------------------
        - Arg2 (list(number)): List of OF session into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getOFTopologyLearnedInfo', payload=payload, response_object=None)

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

    def SendLLDPPacketOut(self, *args, **kwargs):
        """Executes the sendLLDPPacketOut operation on the server.

        Send LLDP Packet Out

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendLLDPPacketOut(LldpDestination=string, EnableLldpFlowAdd=bool, LldpTimeoutVal=number)
        ----------------------------------------------------------------------------------------
        - LldpDestination (str): This parameter requires a lldpDestination of type kString
        - EnableLldpFlowAdd (bool): This parameter requires a enableLldpFlowAdd of type kBool
        - LldpTimeoutVal (number): This parameter requires a lldpTimeoutVal of type kInteger

        sendLLDPPacketOut(LldpDestination=string, EnableLldpFlowAdd=bool, LldpTimeoutVal=number, SessionIndices=list)
        -------------------------------------------------------------------------------------------------------------
        - LldpDestination (str): This parameter requires a lldpDestination of type kString
        - EnableLldpFlowAdd (bool): This parameter requires a enableLldpFlowAdd of type kBool
        - LldpTimeoutVal (number): This parameter requires a lldpTimeoutVal of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendLLDPPacketOut(SessionIndices=string, LldpDestination=string, EnableLldpFlowAdd=bool, LldpTimeoutVal=number)
        ---------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a lldpDestination of type kString
        - LldpDestination (str): This parameter requires a enableLldpFlowAdd of type kBool
        - EnableLldpFlowAdd (bool): This parameter requires a lldpTimeoutVal of type kInteger
        - LldpTimeoutVal (number): This parameter requires a string of session numbers 1-4;6;7-12

        sendLLDPPacketOut(Arg2=list, Arg3=string, Arg4=bool, Arg5=number)list
        ---------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str): LLDP Destination MAC
        - Arg4 (bool): Enable LLDP Flow Add in Switch
        - Arg5 (number): LLDP Timeout Value
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendLLDPPacketOut', payload=payload, response_object=None)

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

    def StartController(self, *args, **kwargs):
        """Executes the startController operation on the server.

        Start OpenFlow Controller

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        startController(SessionIndices=list)
        ------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        startController(SessionIndices=string)
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
        return self._execute('startController', payload=payload, response_object=None)

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

    def StopController(self, *args, **kwargs):
        """Executes the stopController operation on the server.

        Stop OpenFlow Controller

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopController(SessionIndices=list)
        -----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stopController(SessionIndices=string)
        -------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopController', payload=payload, response_object=None)
