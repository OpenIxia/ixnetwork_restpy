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


class IsisSpbRouter(Base):
    """SPB Configuration
    The IsisSpbRouter class encapsulates a list of isisSpbRouter resources that are managed by the user.
    A list of resources can be retrieved from the server using the IsisSpbRouter.find() method.
    The list can be managed by using the IsisSpbRouter.add() and IsisSpbRouter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'isisSpbRouter'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AreaAddresses': 'areaAddresses',
        'AreaAuthenticationType': 'areaAuthenticationType',
        'AreaTransmitPasswordOrMD5Key': 'areaTransmitPasswordOrMD5Key',
        'Attached': 'attached',
        'CSNPInterval': 'cSNPInterval',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DiscardLSPs': 'discardLSPs',
        'EnableHelloPadding': 'enableHelloPadding',
        'EnableHitlessRestart': 'enableHitlessRestart',
        'EnableHostName': 'enableHostName',
        'EnableWideMetric': 'enableWideMetric',
        'Errors': 'errors',
        'HitlessRestartMode': 'hitlessRestartMode',
        'HitlessRestartTime': 'hitlessRestartTime',
        'HitlessRestartVersion': 'hitlessRestartVersion',
        'HostName': 'hostName',
        'IgnoreMTPortCapability': 'ignoreMTPortCapability',
        'IgnoreReceiveMD5': 'ignoreReceiveMD5',
        'InterLSPsOrMGroupPDUBurstGap': 'interLSPsOrMGroupPDUBurstGap',
        'LSPLifetime': 'lSPLifetime',
        'LSPRefreshRate': 'lSPRefreshRate',
        'LSPorMGroupPDUMinTransmissionInterval': 'lSPorMGroupPDUMinTransmissionInterval',
        'LocalSystemID': 'localSystemID',
        'MaxAreaAddresses': 'maxAreaAddresses',
        'MaxLSPSize': 'maxLSPSize',
        'MaxLSPsOrMGroupPDUsPerBurst': 'maxLSPsOrMGroupPDUsPerBurst',
        'Name': 'name',
        'Overloaded': 'overloaded',
        'PSNPInterval': 'pSNPInterval',
        'PartitionRepair': 'partitionRepair',
        'SessionInfo': 'sessionInfo',
        'SessionStatus': 'sessionStatus',
        'SpbTopologyCount': 'spbTopologyCount',
        'StateCounts': 'stateCounts',
        'Status': 'status',
    }

    def __init__(self, parent):
        super(IsisSpbRouter, self).__init__(parent)

    @property
    def SpbTopologyList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.spbtopologylist_079e088e28e1c709b12ccf5543f3c230.SpbTopologyList): An instance of the SpbTopologyList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.spbtopologylist_079e088e28e1c709b12ccf5543f3c230 import SpbTopologyList
        return SpbTopologyList(self)._select()

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
    def AreaAddresses(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Addresses
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AreaAddresses']))

    @property
    def AreaAuthenticationType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Authentication Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AreaAuthenticationType']))

    @property
    def AreaTransmitPasswordOrMD5Key(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Transmit Password / MD5-Key
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AreaTransmitPasswordOrMD5Key']))

    @property
    def Attached(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Attached
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Attached']))

    @property
    def CSNPInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CSNP Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CSNPInterval']))

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
    def DiscardLSPs(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Discard LSPs
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DiscardLSPs']))

    @property
    def EnableHelloPadding(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Hello Padding
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableHelloPadding']))

    @property
    def EnableHitlessRestart(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Hitless Restart
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableHitlessRestart']))

    @property
    def EnableHostName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Host Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableHostName']))

    @property
    def EnableWideMetric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Wide Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableWideMetric']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def HitlessRestartMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Restart Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HitlessRestartMode']))

    @property
    def HitlessRestartTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Restart Time
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HitlessRestartTime']))

    @property
    def HitlessRestartVersion(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Restart Version
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HitlessRestartVersion']))

    @property
    def HostName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Host Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HostName']))

    @property
    def IgnoreMTPortCapability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ignore MT Port Capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IgnoreMTPortCapability']))

    @property
    def IgnoreReceiveMD5(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ignore Receive MD5
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IgnoreReceiveMD5']))

    @property
    def InterLSPsOrMGroupPDUBurstGap(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Inter LSPs/MGROUP-PDUs Burst Gap (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InterLSPsOrMGroupPDUBurstGap']))

    @property
    def LSPLifetime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP Rifetime (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LSPLifetime']))

    @property
    def LSPRefreshRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP Refresh Rate (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LSPRefreshRate']))

    @property
    def LSPorMGroupPDUMinTransmissionInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP/MGROUP-PDU Min Transmission Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LSPorMGroupPDUMinTransmissionInterval']))

    @property
    def LocalSystemID(self):
        """
        Returns
        -------
        - list(str): System ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalSystemID'])

    @property
    def MaxAreaAddresses(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Area Addresses
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxAreaAddresses']))

    @property
    def MaxLSPSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max LSP Size
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxLSPSize']))

    @property
    def MaxLSPsOrMGroupPDUsPerBurst(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max LSPs/MGROUP-PDUs Per Burst
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxLSPsOrMGroupPDUsPerBurst']))

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
    def Overloaded(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Overloaded
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Overloaded']))

    @property
    def PSNPInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PSNP Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PSNPInterval']))

    @property
    def PartitionRepair(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Partition Repair
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PartitionRepair']))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[noIfaceUp | up]): Logs additional information about the session Information
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def SpbTopologyCount(self):
        """
        Returns
        -------
        - number: Topology Count(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['SpbTopologyCount'])
    @SpbTopologyCount.setter
    def SpbTopologyCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SpbTopologyCount'], value)

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

    def update(self, Name=None, SpbTopologyCount=None):
        """Updates isisSpbRouter resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SpbTopologyCount (number): Topology Count(multiplier)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None, SpbTopologyCount=None):
        """Adds a new isisSpbRouter resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SpbTopologyCount (number): Topology Count(multiplier)

        Returns
        -------
        - self: This instance with all currently retrieved isisSpbRouter resources using find and the newly added isisSpbRouter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained isisSpbRouter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, DescriptiveName=None, Errors=None, LocalSystemID=None, Name=None, SessionInfo=None, SessionStatus=None, SpbTopologyCount=None, StateCounts=None, Status=None):
        """Finds and retrieves isisSpbRouter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisSpbRouter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisSpbRouter resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - LocalSystemID (list(str)): System ID
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionInfo (list(str[noIfaceUp | up])): Logs additional information about the session Information
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - SpbTopologyCount (number): Topology Count(multiplier)
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching isisSpbRouter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisSpbRouter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisSpbRouter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AreaAddresses=None, AreaAuthenticationType=None, AreaTransmitPasswordOrMD5Key=None, Attached=None, CSNPInterval=None, DiscardLSPs=None, EnableHelloPadding=None, EnableHitlessRestart=None, EnableHostName=None, EnableWideMetric=None, HitlessRestartMode=None, HitlessRestartTime=None, HitlessRestartVersion=None, HostName=None, IgnoreMTPortCapability=None, IgnoreReceiveMD5=None, InterLSPsOrMGroupPDUBurstGap=None, LSPLifetime=None, LSPRefreshRate=None, LSPorMGroupPDUMinTransmissionInterval=None, MaxAreaAddresses=None, MaxLSPSize=None, MaxLSPsOrMGroupPDUsPerBurst=None, Overloaded=None, PSNPInterval=None, PartitionRepair=None):
        """Base class infrastructure that gets a list of isisSpbRouter device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AreaAddresses (str): optional regex of areaAddresses
        - AreaAuthenticationType (str): optional regex of areaAuthenticationType
        - AreaTransmitPasswordOrMD5Key (str): optional regex of areaTransmitPasswordOrMD5Key
        - Attached (str): optional regex of attached
        - CSNPInterval (str): optional regex of cSNPInterval
        - DiscardLSPs (str): optional regex of discardLSPs
        - EnableHelloPadding (str): optional regex of enableHelloPadding
        - EnableHitlessRestart (str): optional regex of enableHitlessRestart
        - EnableHostName (str): optional regex of enableHostName
        - EnableWideMetric (str): optional regex of enableWideMetric
        - HitlessRestartMode (str): optional regex of hitlessRestartMode
        - HitlessRestartTime (str): optional regex of hitlessRestartTime
        - HitlessRestartVersion (str): optional regex of hitlessRestartVersion
        - HostName (str): optional regex of hostName
        - IgnoreMTPortCapability (str): optional regex of ignoreMTPortCapability
        - IgnoreReceiveMD5 (str): optional regex of ignoreReceiveMD5
        - InterLSPsOrMGroupPDUBurstGap (str): optional regex of interLSPsOrMGroupPDUBurstGap
        - LSPLifetime (str): optional regex of lSPLifetime
        - LSPRefreshRate (str): optional regex of lSPRefreshRate
        - LSPorMGroupPDUMinTransmissionInterval (str): optional regex of lSPorMGroupPDUMinTransmissionInterval
        - MaxAreaAddresses (str): optional regex of maxAreaAddresses
        - MaxLSPSize (str): optional regex of maxLSPSize
        - MaxLSPsOrMGroupPDUsPerBurst (str): optional regex of maxLSPsOrMGroupPDUsPerBurst
        - Overloaded (str): optional regex of overloaded
        - PSNPInterval (str): optional regex of pSNPInterval
        - PartitionRepair (str): optional regex of partitionRepair

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

    def IsisStartRouter(self, *args, **kwargs):
        """Executes the isisStartRouter operation on the server.

        Start ISIS Router

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        isisStartRouter(SessionIndices=list)
        ------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        isisStartRouter(SessionIndices=string)
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
        return self._execute('isisStartRouter', payload=payload, response_object=None)

    def IsisStopRouter(self, *args, **kwargs):
        """Executes the isisStopRouter operation on the server.

        Stop ISIS Router

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        isisStopRouter(SessionIndices=list)
        -----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        isisStopRouter(SessionIndices=string)
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
        return self._execute('isisStopRouter', payload=payload, response_object=None)

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
