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


class Pcc(Base):
    """Pcep Session (Device) level Configuration
    The Pcc class encapsulates a list of pcc resources that are managed by the user.
    A list of resources can be retrieved from the server using the Pcc.find() method.
    The list can be managed by using the Pcc.add() and Pcc.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'pcc'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Active_pre_established_lsps': 'active_pre_established_lsps',
        'Authentication': 'authentication',
        'BurstInterval': 'burstInterval',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DeadInterval': 'deadInterval',
        'DescriptiveName': 'descriptiveName',
        'ErrorValue': 'errorValue',
        'Errors': 'errors',
        'ExpectedInitiatedLspsForTraffic': 'expectedInitiatedLspsForTraffic',
        'KeepaliveInterval': 'keepaliveInterval',
        'LspInstantiationCapability': 'lspInstantiationCapability',
        'LspUpdateCapability': 'lspUpdateCapability',
        'MD5Key': 'mD5Key',
        'MaxLspPerPcReq': 'maxLspPerPcReq',
        'MaxLspsPerPcRpt': 'maxLspsPerPcRpt',
        'MaxReconnectInterval': 'maxReconnectInterval',
        'MaxRequestedLspPerInterval': 'maxRequestedLspPerInterval',
        'MaxSyncLspPerInterval': 'maxSyncLspPerInterval',
        'MaximumSidDepth': 'maximumSidDepth',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NumberOfBackupPCEs': 'numberOfBackupPCEs',
        'PccPpagTLVType': 'pccPpagTLVType',
        'PccTEPathBindingTLVType': 'pccTEPathBindingTLVType',
        'PceIpv4Address': 'pceIpv4Address',
        'PreEstablishedSrLspsPerPcc': 'preEstablishedSrLspsPerPcc',
        'RateControl': 'rateControl',
        'ReconnectInterval': 'reconnectInterval',
        'RequestedLspsPerPcc': 'requestedLspsPerPcc',
        'ReturnInstantiationError': 'returnInstantiationError',
        'SessionStatus': 'sessionStatus',
        'SrPceCapability': 'srPceCapability',
        'Srv6MaxSL': 'srv6MaxSL',
        'Srv6PceCapability': 'srv6PceCapability',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'StateTimeoutInterval': 'stateTimeoutInterval',
        'Status': 'status',
        'TcpPort': 'tcpPort',
    }

    def __init__(self, parent):
        super(Pcc, self).__init__(parent)

    @property
    def ExpectedInitiatedLspList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.expectedinitiatedlsplist_c1edb3ac572c229482ac3b16768b81b1.ExpectedInitiatedLspList): An instance of the ExpectedInitiatedLspList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.expectedinitiatedlsplist_c1edb3ac572c229482ac3b16768b81b1 import ExpectedInitiatedLspList
        return ExpectedInitiatedLspList(self)._select()

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
    def PccLearnedLspDb(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcclearnedlspdb_1f09e65ced78209c908d7bf80bf0e73d.PccLearnedLspDb): An instance of the PccLearnedLspDb class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcclearnedlspdb_1f09e65ced78209c908d7bf80bf0e73d import PccLearnedLspDb
        return PccLearnedLspDb(self)._select()

    @property
    def PcepBackupPCEs(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepbackuppces_f780e95e8b1b209ab7ad3ca8a9f3a4c6.PcepBackupPCEs): An instance of the PcepBackupPCEs class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepbackuppces_f780e95e8b1b209ab7ad3ca8a9f3a4c6 import PcepBackupPCEs
        return PcepBackupPCEs(self)._select()

    @property
    def PreEstablishedSrLsps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.preestablishedsrlsps_a4b5c388b0a9f1cd18fdc396c2ea1c6a.PreEstablishedSrLsps): An instance of the PreEstablishedSrLsps class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.preestablishedsrlsps_a4b5c388b0a9f1cd18fdc396c2ea1c6a import PreEstablishedSrLsps
        return PreEstablishedSrLsps(self)._select()

    @property
    def RequestedLsps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.requestedlsps_13f940a8c982ec765fee3bc34ba5d305.RequestedLsps): An instance of the RequestedLsps class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.requestedlsps_13f940a8c982ec765fee3bc34ba5d305 import RequestedLsps
        return RequestedLsps(self)._select()

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
    def Active_pre_established_lsps(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Active_pre_established_lsps'])
    @Active_pre_established_lsps.setter
    def Active_pre_established_lsps(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Active_pre_established_lsps'], value)

    @property
    def Authentication(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The type of cryptographic authentication to be used on this link interface
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Authentication']))

    @property
    def BurstInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Interval in milisecond in which desired rate of messages needs to be maintained.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BurstInterval']))

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
    def DeadInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the time interval, after the expiration of which, a PCEP peer declares the session down if no PCEP message has been received.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DeadInterval']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def ErrorValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To configure the type of error. Editable only if Return Instantiation Error is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ErrorValue']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def ExpectedInitiatedLspsForTraffic(self):
        """
        Returns
        -------
        - number: Based on the value in this control the number of Expected Initiated LSPs for Traffic can be configured. This is used for traffic only.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExpectedInitiatedLspsForTraffic'])
    @ExpectedInitiatedLspsForTraffic.setter
    def ExpectedInitiatedLspsForTraffic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExpectedInitiatedLspsForTraffic'], value)

    @property
    def KeepaliveInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Frequency/Time Interval of sending PCEP messages to keep the session active.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['KeepaliveInterval']))

    @property
    def LspInstantiationCapability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If Stateful PCE Capability is enabled then this control should be activated to set the LSP Instantiation capability in the Stateful PCE Capability TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspInstantiationCapability']))

    @property
    def LspUpdateCapability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If Stateful PCE Capability is enabled then this control should be activated to set the update capability in the Stateful PCE Capability TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspUpdateCapability']))

    @property
    def MD5Key(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A value to be used as the secret MD5 Key.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MD5Key']))

    @property
    def MaxLspPerPcReq(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max LSPs Per PCReq
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxLspPerPcReq']))

    @property
    def MaxLspsPerPcRpt(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Controls the maximum LSP information that can be present in a Path report message when the session is stateful session.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxLspsPerPcRpt']))

    @property
    def MaxReconnectInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the maximum time interval, by which recoonect timer will be increased upto.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxReconnectInterval']))

    @property
    def MaxRequestedLspPerInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum number of LSP computation request messages can be sent per interval.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxRequestedLspPerInterval']))

    @property
    def MaxSyncLspPerInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum number of LSP sync can be sent per interval.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxSyncLspPerInterval']))

    @property
    def MaximumSidDepth(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum SID Depth field (MSD) specifies the maximum number of SIDs that a PCC is capable of imposing on a packet. Editable only if SR PCE Capability is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaximumSidDepth']))

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
    def NumberOfBackupPCEs(self):
        """
        Returns
        -------
        - number: Number of Backup PCEs
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfBackupPCEs'])
    @NumberOfBackupPCEs.setter
    def NumberOfBackupPCEs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfBackupPCEs'], value)

    @property
    def PccPpagTLVType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PPAG TLV Type specifies PCC's capability of interpreting this type of PPAG TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PccPpagTLVType']))

    @property
    def PccTEPathBindingTLVType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PCC TE-PATH-BINDING TLV Type is a TLV that carries MPLS label binding or SRv6 Binding SID. This is only configurable if the Binding SID Draft Version is set to ietf-pce-binding-label-sid. The minimum value is 0. The maximum value is 65535. The default value is 31.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PccTEPathBindingTLVType']))

    @property
    def PceIpv4Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the PCE. This column is greyed out in case of PCCv6.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PceIpv4Address']))

    @property
    def PreEstablishedSrLspsPerPcc(self):
        """
        Returns
        -------
        - number: Pre-Established SR LSPs per PCC
        """
        return self._get_attribute(self._SDM_ATT_MAP['PreEstablishedSrLspsPerPcc'])
    @PreEstablishedSrLspsPerPcc.setter
    def PreEstablishedSrLspsPerPcc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PreEstablishedSrLspsPerPcc'], value)

    @property
    def RateControl(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The rate control is an optional feature associated with PCE initiated LSP.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RateControl']))

    @property
    def ReconnectInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the time interval, after the expiration of which, retry to establish the broken session by PCC happen.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReconnectInterval']))

    @property
    def RequestedLspsPerPcc(self):
        """
        Returns
        -------
        - number: Requested LSPs per PCC
        """
        return self._get_attribute(self._SDM_ATT_MAP['RequestedLspsPerPcc'])
    @RequestedLspsPerPcc.setter
    def RequestedLspsPerPcc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RequestedLspsPerPcc'], value)

    @property
    def ReturnInstantiationError(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, then PCC will reply PCErr upon receiving PCInitiate message.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReturnInstantiationError']))

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def SrPceCapability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The SR PCE Capability TLV is an optional TLV associated with the OPEN Object to exchange SR capability of PCEP speakers.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrPceCapability']))

    @property
    def Srv6MaxSL(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum value of the Segments Left (SL) in the SRH.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6MaxSL']))

    @property
    def Srv6PceCapability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The SRv6 PCE Capability TLV is a sub-TLV that comes under PATH-SETUP-TYPE-CAPABILITY TLV if PST List contains SRv6 PST type. This TLV is associated with the OPEN Object to exchange SRv6 capability of PCEP speakers.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6PceCapability']))

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
    def StateTimeoutInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the time interval, after the expiration of which, LSP is cleaned up by PCC.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StateTimeoutInterval']))

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): PCEP operates over TCP using a registered TCP port (default - 4189). This allows the requirements of reliable messaging and flow control to bemet without further protocol work. This control can be configured when user does not want to use the default one.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TcpPort']))

    def update(self, Active_pre_established_lsps=None, ConnectedVia=None, ExpectedInitiatedLspsForTraffic=None, Multiplier=None, Name=None, NumberOfBackupPCEs=None, PreEstablishedSrLspsPerPcc=None, RequestedLspsPerPcc=None, StackedLayers=None):
        """Updates pcc resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Active_pre_established_lsps (number): 
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - ExpectedInitiatedLspsForTraffic (number): Based on the value in this control the number of Expected Initiated LSPs for Traffic can be configured. This is used for traffic only.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfBackupPCEs (number): Number of Backup PCEs
        - PreEstablishedSrLspsPerPcc (number): Pre-Established SR LSPs per PCC
        - RequestedLspsPerPcc (number): Requested LSPs per PCC
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Active_pre_established_lsps=None, ConnectedVia=None, ExpectedInitiatedLspsForTraffic=None, Multiplier=None, Name=None, NumberOfBackupPCEs=None, PreEstablishedSrLspsPerPcc=None, RequestedLspsPerPcc=None, StackedLayers=None):
        """Adds a new pcc resource on the server and adds it to the container.

        Args
        ----
        - Active_pre_established_lsps (number): 
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - ExpectedInitiatedLspsForTraffic (number): Based on the value in this control the number of Expected Initiated LSPs for Traffic can be configured. This is used for traffic only.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfBackupPCEs (number): Number of Backup PCEs
        - PreEstablishedSrLspsPerPcc (number): Pre-Established SR LSPs per PCC
        - RequestedLspsPerPcc (number): Requested LSPs per PCC
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved pcc resources using find and the newly added pcc resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained pcc resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Active_pre_established_lsps=None, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, ExpectedInitiatedLspsForTraffic=None, Multiplier=None, Name=None, NumberOfBackupPCEs=None, PreEstablishedSrLspsPerPcc=None, RequestedLspsPerPcc=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves pcc resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pcc resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pcc resources from the server.

        Args
        ----
        - Active_pre_established_lsps (number): 
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - ExpectedInitiatedLspsForTraffic (number): Based on the value in this control the number of Expected Initiated LSPs for Traffic can be configured. This is used for traffic only.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfBackupPCEs (number): Number of Backup PCEs
        - PreEstablishedSrLspsPerPcc (number): Pre-Established SR LSPs per PCC
        - RequestedLspsPerPcc (number): Requested LSPs per PCC
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching pcc resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pcc data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pcc resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, Authentication=None, BurstInterval=None, DeadInterval=None, ErrorValue=None, KeepaliveInterval=None, LspInstantiationCapability=None, LspUpdateCapability=None, MD5Key=None, MaxLspPerPcReq=None, MaxLspsPerPcRpt=None, MaxReconnectInterval=None, MaxRequestedLspPerInterval=None, MaxSyncLspPerInterval=None, MaximumSidDepth=None, PccPpagTLVType=None, PccTEPathBindingTLVType=None, PceIpv4Address=None, RateControl=None, ReconnectInterval=None, ReturnInstantiationError=None, SrPceCapability=None, Srv6MaxSL=None, Srv6PceCapability=None, StateTimeoutInterval=None, TcpPort=None):
        """Base class infrastructure that gets a list of pcc device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - Authentication (str): optional regex of authentication
        - BurstInterval (str): optional regex of burstInterval
        - DeadInterval (str): optional regex of deadInterval
        - ErrorValue (str): optional regex of errorValue
        - KeepaliveInterval (str): optional regex of keepaliveInterval
        - LspInstantiationCapability (str): optional regex of lspInstantiationCapability
        - LspUpdateCapability (str): optional regex of lspUpdateCapability
        - MD5Key (str): optional regex of mD5Key
        - MaxLspPerPcReq (str): optional regex of maxLspPerPcReq
        - MaxLspsPerPcRpt (str): optional regex of maxLspsPerPcRpt
        - MaxReconnectInterval (str): optional regex of maxReconnectInterval
        - MaxRequestedLspPerInterval (str): optional regex of maxRequestedLspPerInterval
        - MaxSyncLspPerInterval (str): optional regex of maxSyncLspPerInterval
        - MaximumSidDepth (str): optional regex of maximumSidDepth
        - PccPpagTLVType (str): optional regex of pccPpagTLVType
        - PccTEPathBindingTLVType (str): optional regex of pccTEPathBindingTLVType
        - PceIpv4Address (str): optional regex of pceIpv4Address
        - RateControl (str): optional regex of rateControl
        - ReconnectInterval (str): optional regex of reconnectInterval
        - ReturnInstantiationError (str): optional regex of returnInstantiationError
        - SrPceCapability (str): optional regex of srPceCapability
        - Srv6MaxSL (str): optional regex of srv6MaxSL
        - Srv6PceCapability (str): optional regex of srv6PceCapability
        - StateTimeoutInterval (str): optional regex of stateTimeoutInterval
        - TcpPort (str): optional regex of tcpPort

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

    def ClearPccLearnedInfoInClient(self, *args, **kwargs):
        """Executes the clearPccLearnedInfoInClient operation on the server.

        Clears ALL Learned LSP Information of PCC Device.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearPccLearnedInfoInClient(SessionIndices=list)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        clearPccLearnedInfoInClient(SessionIndices=string)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        clearPccLearnedInfoInClient(Arg2=list)list
        ------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearPccLearnedInfoInClient', payload=payload, response_object=None)

    def GetPccBasicAllSrLspLearnedInfo(self, *args, **kwargs):
        """Executes the getPccBasicAllSrLspLearnedInfo operation on the server.

        Gets Basic Information about All SR LSPs learnt by this PCC.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPccBasicAllSrLspLearnedInfo(SessionIndices=list)
        ---------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getPccBasicAllSrLspLearnedInfo(SessionIndices=string)
        -----------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getPccBasicAllSrLspLearnedInfo(Arg2=list)list
        ---------------------------------------------
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
        return self._execute('getPccBasicAllSrLspLearnedInfo', payload=payload, response_object=None)

    def GetPccBasicAllSrv6LspLearnedInfo(self, *args, **kwargs):
        """Executes the getPccBasicAllSrv6LspLearnedInfo operation on the server.

        Gets Basic Information about All SRv6 LSPs learnt by this PCC.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPccBasicAllSrv6LspLearnedInfo(SessionIndices=list)
        -----------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getPccBasicAllSrv6LspLearnedInfo(SessionIndices=string)
        -------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getPccBasicAllSrv6LspLearnedInfo(Arg2=list)list
        -----------------------------------------------
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
        return self._execute('getPccBasicAllSrv6LspLearnedInfo', payload=payload, response_object=None)

    def GetPccBasicSrPccRequestedLspLearnedInfo(self, *args, **kwargs):
        """Executes the getPccBasicSrPccRequestedLspLearnedInfo operation on the server.

        Gets Basic Information about SR-TE PCC Requested LSPs learnt by this PCC.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPccBasicSrPccRequestedLspLearnedInfo(SessionIndices=list)
        ------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getPccBasicSrPccRequestedLspLearnedInfo(SessionIndices=string)
        --------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getPccBasicSrPccRequestedLspLearnedInfo(Arg2=list)list
        ------------------------------------------------------
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
        return self._execute('getPccBasicSrPccRequestedLspLearnedInfo', payload=payload, response_object=None)

    def GetPccBasicSrPccSyncOrReportLspLearnedInfo(self, *args, **kwargs):
        """Executes the getPccBasicSrPccSyncOrReportLspLearnedInfo operation on the server.

        Gets Basic Information about SR-TE PCC Sync/Report LSPs learnt by this PCC.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPccBasicSrPccSyncOrReportLspLearnedInfo(SessionIndices=list)
        ---------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getPccBasicSrPccSyncOrReportLspLearnedInfo(SessionIndices=string)
        -----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getPccBasicSrPccSyncOrReportLspLearnedInfo(Arg2=list)list
        ---------------------------------------------------------
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
        return self._execute('getPccBasicSrPccSyncOrReportLspLearnedInfo', payload=payload, response_object=None)

    def GetPccBasicSrPceInitiatedLspLearnedInfo(self, *args, **kwargs):
        """Executes the getPccBasicSrPceInitiatedLspLearnedInfo operation on the server.

        Gets Basic Information about SR-TE PCE Initiated LSPs learnt by this PCC.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPccBasicSrPceInitiatedLspLearnedInfo(SessionIndices=list)
        ------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getPccBasicSrPceInitiatedLspLearnedInfo(SessionIndices=string)
        --------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getPccBasicSrPceInitiatedLspLearnedInfo(Arg2=list)list
        ------------------------------------------------------
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
        return self._execute('getPccBasicSrPceInitiatedLspLearnedInfo', payload=payload, response_object=None)

    def GetPccBasicSrv6PccRequestedLspLearnedInfo(self, *args, **kwargs):
        """Executes the getPccBasicSrv6PccRequestedLspLearnedInfo operation on the server.

        Gets Basic Information about SRv6 PCC Requested LSPs learnt by this PCC.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPccBasicSrv6PccRequestedLspLearnedInfo(SessionIndices=list)
        --------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getPccBasicSrv6PccRequestedLspLearnedInfo(SessionIndices=string)
        ----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getPccBasicSrv6PccRequestedLspLearnedInfo(Arg2=list)list
        --------------------------------------------------------
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
        return self._execute('getPccBasicSrv6PccRequestedLspLearnedInfo', payload=payload, response_object=None)

    def GetPccBasicSrv6PccSyncOrReportLspLearnedInfo(self, *args, **kwargs):
        """Executes the getPccBasicSrv6PccSyncOrReportLspLearnedInfo operation on the server.

        Gets Basic Information about SRv6 PCC Sync/Report LSPs learnt by this PCC.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPccBasicSrv6PccSyncOrReportLspLearnedInfo(SessionIndices=list)
        -----------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getPccBasicSrv6PccSyncOrReportLspLearnedInfo(SessionIndices=string)
        -------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getPccBasicSrv6PccSyncOrReportLspLearnedInfo(Arg2=list)list
        -----------------------------------------------------------
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
        return self._execute('getPccBasicSrv6PccSyncOrReportLspLearnedInfo', payload=payload, response_object=None)

    def GetPccBasicSrv6PceInitiatedLspLearnedInfo(self, *args, **kwargs):
        """Executes the getPccBasicSrv6PceInitiatedLspLearnedInfo operation on the server.

        Gets Basic Information about SRv6 PCE Initiated LSPs learnt by this PCC.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPccBasicSrv6PceInitiatedLspLearnedInfo(SessionIndices=list)
        --------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getPccBasicSrv6PceInitiatedLspLearnedInfo(SessionIndices=string)
        ----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getPccBasicSrv6PceInitiatedLspLearnedInfo(Arg2=list)list
        --------------------------------------------------------
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
        return self._execute('getPccBasicSrv6PceInitiatedLspLearnedInfo', payload=payload, response_object=None)

    def GetPccLearnedInfo(self, *args, **kwargs):
        """Executes the getPccLearnedInfo operation on the server.

        Gets Detailed Information about All SR LSPs learnt by this PCC.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPccLearnedInfo(SessionIndices=list)
        --------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getPccLearnedInfo(SessionIndices=string)
        ----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getPccLearnedInfo(Arg2=list)list
        --------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPccLearnedInfo', payload=payload, response_object=None)

    def GetPccSrv6LearnedInfo(self, *args, **kwargs):
        """Executes the getPccSrv6LearnedInfo operation on the server.

        Gets Detailed Information about All SRv6 LSPs learnt by this PCC.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPccSrv6LearnedInfo(SessionIndices=list)
        ------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getPccSrv6LearnedInfo(SessionIndices=string)
        --------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getPccSrv6LearnedInfo(Arg2=list)list
        ------------------------------------
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
        return self._execute('getPccSrv6LearnedInfo', payload=payload, response_object=None)

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
