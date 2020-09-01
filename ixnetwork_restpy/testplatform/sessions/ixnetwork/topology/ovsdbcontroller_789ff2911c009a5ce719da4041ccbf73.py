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


class Ovsdbcontroller(Base):
    """
    The Ovsdbcontroller class encapsulates a list of ovsdbcontroller resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ovsdbcontroller.find() method.
    The list can be managed by using the Ovsdbcontroller.add() and Ovsdbcontroller.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ovsdbcontroller'
    _SDM_ATT_MAP = {
        'ClearDumpDbFiles': 'clearDumpDbFiles',
        'ConnectedVia': 'connectedVia',
        'ConnectionType': 'connectionType',
        'ControllerTcpPort': 'controllerTcpPort',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DirectoryName': 'directoryName',
        'DumpdbDirectoryName': 'dumpdbDirectoryName',
        'EnableLogging': 'enableLogging',
        'EnableOvsdbServerIp': 'enableOvsdbServerIp',
        'ErrorCode': 'errorCode',
        'ErrorDesc': 'errorDesc',
        'ErrorLogDirectoryName': 'errorLogDirectoryName',
        'ErrorLogicalSwitchName': 'errorLogicalSwitchName',
        'ErrorPhysicalSwitchName': 'errorPhysicalSwitchName',
        'ErrorTimeStamp': 'errorTimeStamp',
        'Errors': 'errors',
        'FileCaCertificate': 'fileCaCertificate',
        'FileCertificate': 'fileCertificate',
        'FileHWGatewayCertificate': 'fileHWGatewayCertificate',
        'FilePrivKey': 'filePrivKey',
        'HSCConfiguration': 'hSCConfiguration',
        'LatestDumpDbFileNames': 'latestDumpDbFileNames',
        'LatestErrorFileNames': 'latestErrorFileNames',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'OvsdbSchema': 'ovsdbSchema',
        'OvsdbServerIp': 'ovsdbServerIp',
        'PseudoConnectedTo': 'pseudoConnectedTo',
        'PseudoConnectedToBfd': 'pseudoConnectedToBfd',
        'PseudoConnectedToVxlanReplicator': 'pseudoConnectedToVxlanReplicator',
        'PseudoMultiplier': 'pseudoMultiplier',
        'PseudoMultiplierBfd': 'pseudoMultiplierBfd',
        'PseudoMultiplierVxlanReplicator': 'pseudoMultiplierVxlanReplicator',
        'Role': 'role',
        'ServerAddDeleteConnectionError': 'serverAddDeleteConnectionError',
        'ServerAddDeleteStatus': 'serverAddDeleteStatus',
        'ServerConnectionIp': 'serverConnectionIp',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TableNames': 'tableNames',
        'TimeOut': 'timeOut',
        'VerifyHWGatewayCertificate': 'verifyHWGatewayCertificate',
        'VerifyPeerCertificate': 'verifyPeerCertificate',
        'Vxlan': 'vxlan',
        'VxlanReplicator': 'vxlanReplicator',
    }

    def __init__(self, parent):
        super(Ovsdbcontroller, self).__init__(parent)

    @property
    def ClusterData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.clusterdata_14465bf77bf9eb0d40ce3ac056e3b337.ClusterData): An instance of the ClusterData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.clusterdata_14465bf77bf9eb0d40ce3ac056e3b337 import ClusterData
        return ClusterData(self)._select()

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
    def ClearDumpDbFiles(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClearDumpDbFiles']))

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
    def ConnectionType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Connection should use TCP or TLS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConnectionType']))

    @property
    def ControllerTcpPort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the TCP port for the Controller
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ControllerTcpPort']))

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
    def DirectoryName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Location of Directory in Client where the Certificate and Key Files are available
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DirectoryName']))

    @property
    def DumpdbDirectoryName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Location of Directory in Client where the DumpDb Files are available
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DumpdbDirectoryName']))

    @property
    def EnableLogging(self):
        """
        Returns
        -------
        - bool: If true, Port debug logs will be recorded, Maximum recording will be upto 500 MB .
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLogging'])
    @EnableLogging.setter
    def EnableLogging(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLogging'], value)

    @property
    def EnableOvsdbServerIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOvsdbServerIp']))

    @property
    def ErrorCode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Error Code
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ErrorCode']))

    @property
    def ErrorDesc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Description of Error occured
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ErrorDesc']))

    @property
    def ErrorLogDirectoryName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Location of Directory in Client where the ErrorLog Files are available
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ErrorLogDirectoryName']))

    @property
    def ErrorLogicalSwitchName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Error occured for this Logical Switch Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ErrorLogicalSwitchName']))

    @property
    def ErrorPhysicalSwitchName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Error occured for this Physical Switch Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ErrorPhysicalSwitchName']))

    @property
    def ErrorTimeStamp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time Stamp at which Last Error occurred
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ErrorTimeStamp']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def FileCaCertificate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CA Certificate File
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FileCaCertificate']))

    @property
    def FileCertificate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Certificate File
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FileCertificate']))

    @property
    def FileHWGatewayCertificate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): HW Gateway Certificate File
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FileHWGatewayCertificate']))

    @property
    def FilePrivKey(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Private Key File
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FilePrivKey']))

    @property
    def HSCConfiguration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Each VTEP has its own Hardware Switch Controller.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HSCConfiguration']))

    @property
    def LatestDumpDbFileNames(self):
        """
        Returns
        -------
        - str: Api to fetch latest DumpDb Files
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatestDumpDbFileNames'])
    @LatestDumpDbFileNames.setter
    def LatestDumpDbFileNames(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatestDumpDbFileNames'], value)

    @property
    def LatestErrorFileNames(self):
        """
        Returns
        -------
        - str: Api to fetch latest Error Files
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatestErrorFileNames'])
    @LatestErrorFileNames.setter
    def LatestErrorFileNames(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatestErrorFileNames'], value)

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
    def OvsdbSchema(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Database schema
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OvsdbSchema']))

    @property
    def OvsdbServerIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The IP address of the DUT or Ovs Server.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OvsdbServerIp']))

    @property
    def PseudoConnectedTo(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/topology/.../*): GUI-only connection
        """
        return self._get_attribute(self._SDM_ATT_MAP['PseudoConnectedTo'])
    @PseudoConnectedTo.setter
    def PseudoConnectedTo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PseudoConnectedTo'], value)

    @property
    def PseudoConnectedToBfd(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/topology/.../*): GUI-only connection
        """
        return self._get_attribute(self._SDM_ATT_MAP['PseudoConnectedToBfd'])
    @PseudoConnectedToBfd.setter
    def PseudoConnectedToBfd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PseudoConnectedToBfd'], value)

    @property
    def PseudoConnectedToVxlanReplicator(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/topology/.../*): GUI-only connection
        """
        return self._get_attribute(self._SDM_ATT_MAP['PseudoConnectedToVxlanReplicator'])
    @PseudoConnectedToVxlanReplicator.setter
    def PseudoConnectedToVxlanReplicator(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PseudoConnectedToVxlanReplicator'], value)

    @property
    def PseudoMultiplier(self):
        """
        Returns
        -------
        - number: Multiplier for GUI-only connection
        """
        return self._get_attribute(self._SDM_ATT_MAP['PseudoMultiplier'])

    @property
    def PseudoMultiplierBfd(self):
        """
        Returns
        -------
        - number: Multiplier for GUI-only connection
        """
        return self._get_attribute(self._SDM_ATT_MAP['PseudoMultiplierBfd'])

    @property
    def PseudoMultiplierVxlanReplicator(self):
        """
        Returns
        -------
        - number: Multiplier for GUI-only connection
        """
        return self._get_attribute(self._SDM_ATT_MAP['PseudoMultiplierVxlanReplicator'])

    @property
    def Role(self):
        """
        Returns
        -------
        - list(str[master | none | slave]): The role of the OVSDB Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Role'])

    @property
    def ServerAddDeleteConnectionError(self):
        """
        Returns
        -------
        - str: API to retrieve error occured while Adding/ Deleting Server
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerAddDeleteConnectionError'])
    @ServerAddDeleteConnectionError.setter
    def ServerAddDeleteConnectionError(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerAddDeleteConnectionError'], value)

    @property
    def ServerAddDeleteStatus(self):
        """
        Returns
        -------
        - str: Status of all servers Added/Deleted to Controller. Use Get Server Add/Delete Status, right click action to get current status
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerAddDeleteStatus'])

    @property
    def ServerConnectionIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The IP address of the DUT or Ovs Server which needs to be Added/Deleted.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ServerConnectionIp']))

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
    def TableNames(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TableNames']))

    @property
    def TimeOut(self):
        """
        Returns
        -------
        - number: Transact request Time Out in seconds. For scale scenarios increase this Timeout value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeOut'])
    @TimeOut.setter
    def TimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimeOut'], value)

    @property
    def VerifyHWGatewayCertificate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Verify HW Gateway Certificate
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VerifyHWGatewayCertificate']))

    @property
    def VerifyPeerCertificate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Verify Peer Certificate
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VerifyPeerCertificate']))

    @property
    def Vxlan(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/topology/.../*): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vxlan'])
    @Vxlan.setter
    def Vxlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Vxlan'], value)

    @property
    def VxlanReplicator(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/topology/.../*): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['VxlanReplicator'])
    @VxlanReplicator.setter
    def VxlanReplicator(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VxlanReplicator'], value)

    def update(self, ConnectedVia=None, EnableLogging=None, LatestDumpDbFileNames=None, LatestErrorFileNames=None, Multiplier=None, Name=None, PseudoConnectedTo=None, PseudoConnectedToBfd=None, PseudoConnectedToVxlanReplicator=None, ServerAddDeleteConnectionError=None, StackedLayers=None, TimeOut=None, Vxlan=None, VxlanReplicator=None):
        """Updates ovsdbcontroller resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - EnableLogging (bool): If true, Port debug logs will be recorded, Maximum recording will be upto 500 MB .
        - LatestDumpDbFileNames (str): Api to fetch latest DumpDb Files
        - LatestErrorFileNames (str): Api to fetch latest Error Files
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PseudoConnectedTo (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): GUI-only connection
        - PseudoConnectedToBfd (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): GUI-only connection
        - PseudoConnectedToVxlanReplicator (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): GUI-only connection
        - ServerAddDeleteConnectionError (str): API to retrieve error occured while Adding/ Deleting Server
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - TimeOut (number): Transact request Time Out in seconds. For scale scenarios increase this Timeout value.
        - Vxlan (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): 
        - VxlanReplicator (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, EnableLogging=None, LatestDumpDbFileNames=None, LatestErrorFileNames=None, Multiplier=None, Name=None, PseudoConnectedTo=None, PseudoConnectedToBfd=None, PseudoConnectedToVxlanReplicator=None, ServerAddDeleteConnectionError=None, StackedLayers=None, TimeOut=None, Vxlan=None, VxlanReplicator=None):
        """Adds a new ovsdbcontroller resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - EnableLogging (bool): If true, Port debug logs will be recorded, Maximum recording will be upto 500 MB .
        - LatestDumpDbFileNames (str): Api to fetch latest DumpDb Files
        - LatestErrorFileNames (str): Api to fetch latest Error Files
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PseudoConnectedTo (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): GUI-only connection
        - PseudoConnectedToBfd (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): GUI-only connection
        - PseudoConnectedToVxlanReplicator (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): GUI-only connection
        - ServerAddDeleteConnectionError (str): API to retrieve error occured while Adding/ Deleting Server
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - TimeOut (number): Transact request Time Out in seconds. For scale scenarios increase this Timeout value.
        - Vxlan (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): 
        - VxlanReplicator (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): 

        Returns
        -------
        - self: This instance with all currently retrieved ovsdbcontroller resources using find and the newly added ovsdbcontroller resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ovsdbcontroller resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, EnableLogging=None, Errors=None, LatestDumpDbFileNames=None, LatestErrorFileNames=None, Multiplier=None, Name=None, PseudoConnectedTo=None, PseudoConnectedToBfd=None, PseudoConnectedToVxlanReplicator=None, PseudoMultiplier=None, PseudoMultiplierBfd=None, PseudoMultiplierVxlanReplicator=None, Role=None, ServerAddDeleteConnectionError=None, ServerAddDeleteStatus=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None, TimeOut=None, Vxlan=None, VxlanReplicator=None):
        """Finds and retrieves ovsdbcontroller resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ovsdbcontroller resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ovsdbcontroller resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableLogging (bool): If true, Port debug logs will be recorded, Maximum recording will be upto 500 MB .
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - LatestDumpDbFileNames (str): Api to fetch latest DumpDb Files
        - LatestErrorFileNames (str): Api to fetch latest Error Files
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PseudoConnectedTo (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): GUI-only connection
        - PseudoConnectedToBfd (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): GUI-only connection
        - PseudoConnectedToVxlanReplicator (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): GUI-only connection
        - PseudoMultiplier (number): Multiplier for GUI-only connection
        - PseudoMultiplierBfd (number): Multiplier for GUI-only connection
        - PseudoMultiplierVxlanReplicator (number): Multiplier for GUI-only connection
        - Role (list(str[master | none | slave])): The role of the OVSDB Controller.
        - ServerAddDeleteConnectionError (str): API to retrieve error occured while Adding/ Deleting Server
        - ServerAddDeleteStatus (str): Status of all servers Added/Deleted to Controller. Use Get Server Add/Delete Status, right click action to get current status
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - TimeOut (number): Transact request Time Out in seconds. For scale scenarios increase this Timeout value.
        - Vxlan (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): 
        - VxlanReplicator (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): 

        Returns
        -------
        - self: This instance with matching ovsdbcontroller resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ovsdbcontroller data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ovsdbcontroller resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ClearDumpDbFiles=None, ConnectionType=None, ControllerTcpPort=None, DirectoryName=None, DumpdbDirectoryName=None, EnableOvsdbServerIp=None, ErrorCode=None, ErrorDesc=None, ErrorLogDirectoryName=None, ErrorLogicalSwitchName=None, ErrorPhysicalSwitchName=None, ErrorTimeStamp=None, FileCaCertificate=None, FileCertificate=None, FileHWGatewayCertificate=None, FilePrivKey=None, HSCConfiguration=None, OvsdbSchema=None, OvsdbServerIp=None, ServerConnectionIp=None, TableNames=None, VerifyHWGatewayCertificate=None, VerifyPeerCertificate=None):
        """Base class infrastructure that gets a list of ovsdbcontroller device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ClearDumpDbFiles (str): optional regex of clearDumpDbFiles
        - ConnectionType (str): optional regex of connectionType
        - ControllerTcpPort (str): optional regex of controllerTcpPort
        - DirectoryName (str): optional regex of directoryName
        - DumpdbDirectoryName (str): optional regex of dumpdbDirectoryName
        - EnableOvsdbServerIp (str): optional regex of enableOvsdbServerIp
        - ErrorCode (str): optional regex of errorCode
        - ErrorDesc (str): optional regex of errorDesc
        - ErrorLogDirectoryName (str): optional regex of errorLogDirectoryName
        - ErrorLogicalSwitchName (str): optional regex of errorLogicalSwitchName
        - ErrorPhysicalSwitchName (str): optional regex of errorPhysicalSwitchName
        - ErrorTimeStamp (str): optional regex of errorTimeStamp
        - FileCaCertificate (str): optional regex of fileCaCertificate
        - FileCertificate (str): optional regex of fileCertificate
        - FileHWGatewayCertificate (str): optional regex of fileHWGatewayCertificate
        - FilePrivKey (str): optional regex of filePrivKey
        - HSCConfiguration (str): optional regex of hSCConfiguration
        - OvsdbSchema (str): optional regex of ovsdbSchema
        - OvsdbServerIp (str): optional regex of ovsdbServerIp
        - ServerConnectionIp (str): optional regex of serverConnectionIp
        - TableNames (str): optional regex of tableNames
        - VerifyHWGatewayCertificate (str): optional regex of verifyHWGatewayCertificate
        - VerifyPeerCertificate (str): optional regex of verifyPeerCertificate

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

    def AddServer(self, *args, **kwargs):
        """Executes the addServer operation on the server.

        Add Server.

        addServer(Arg2=list)list
        ------------------------
        - Arg2 (list(number)): List of indices for which to Add Server.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('addServer', payload=payload, response_object=None)

    def ClearLastErrors(self, *args, **kwargs):
        """Executes the clearLastErrors operation on the server.

        Clear Error Messages reported due to Last Action.

        clearLastErrors(Arg2=list)list
        ------------------------------
        - Arg2 (list(number)): List of indices for which to clear last reported error messages.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearLastErrors', payload=payload, response_object=None)

    def ClearPortLogs(self, *args, **kwargs):
        """Executes the clearPortLogs operation on the server.

        Add Server.

        clearPortLogs(Arg2=list)list
        ----------------------------
        - Arg2 (list(number)): List of indices for which to Add Server.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearPortLogs', payload=payload, response_object=None)

    def ControllerDumpDB(self, *args, **kwargs):
        """Executes the controllerDumpDB operation on the server.

        Command to fetch Tor Information stored internally.

        controllerDumpDB(Arg2=list)list
        -------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('controllerDumpDB', payload=payload, response_object=None)

    def DeleteServer(self, *args, **kwargs):
        """Executes the deleteServer operation on the server.

        Delete Server.

        deleteServer(Arg2=list)list
        ---------------------------
        - Arg2 (list(number)): List of indices for which to Delete Server.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('deleteServer', payload=payload, response_object=None)

    def DumpDB(self, *args, **kwargs):
        """Executes the dumpDB operation on the server.

        Attach.

        dumpDB(Arg2=list)list
        ---------------------
        - Arg2 (list(number)): List of indices into the device group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dumpDB', payload=payload, response_object=None)

    def GetServerAddDeleteStatus(self, *args, **kwargs):
        """Executes the getServerAddDeleteStatus operation on the server.

        Get Server Status.

        getServerAddDeleteStatus(Arg2=list)list
        ---------------------------------------
        - Arg2 (list(number)): List of indices for which to get Server Status.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getServerAddDeleteStatus', payload=payload, response_object=None)

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
