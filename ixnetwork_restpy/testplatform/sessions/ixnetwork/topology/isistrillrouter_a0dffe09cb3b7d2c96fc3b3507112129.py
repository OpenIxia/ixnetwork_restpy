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


class IsisTrillRouter(Base):
    """TRILL Configuration
    The IsisTrillRouter class encapsulates a list of isisTrillRouter resources that are managed by the system.
    A list of resources can be retrieved from the server using the IsisTrillRouter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'isisTrillRouter'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AreaAddresses': 'areaAddresses',
        'AreaAuthenticationType': 'areaAuthenticationType',
        'AreaTransmitPasswordOrMD5Key': 'areaTransmitPasswordOrMD5Key',
        'Attached': 'attached',
        'CSNPInterval': 'cSNPInterval',
        'CapabilityRouterId': 'capabilityRouterId',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DiscardLSPs': 'discardLSPs',
        'EnableHelloPadding': 'enableHelloPadding',
        'EnableHostName': 'enableHostName',
        'EnableMtuProbe': 'enableMtuProbe',
        'EnableWideMetric': 'enableWideMetric',
        'Errors': 'errors',
        'HostName': 'hostName',
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
        'NoOfMtuProbes': 'noOfMtuProbes',
        'OrigLspBufSize': 'origLspBufSize',
        'Overloaded': 'overloaded',
        'PSNPInterval': 'pSNPInterval',
        'PartitionRepair': 'partitionRepair',
        'SessionInfo': 'sessionInfo',
        'SessionStatus': 'sessionStatus',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TrillMCastIpv4GroupCount': 'trillMCastIpv4GroupCount',
        'TrillMCastIpv6GroupCount': 'trillMCastIpv6GroupCount',
        'TrillMCastMacGroupCount': 'trillMCastMacGroupCount',
    }

    def __init__(self, parent):
        super(IsisTrillRouter, self).__init__(parent)

    @property
    def TrillMCastIpv4GroupList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.trillmcastipv4grouplist_067fcb786745f03382b0f3242126f4a0.TrillMCastIpv4GroupList): An instance of the TrillMCastIpv4GroupList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.trillmcastipv4grouplist_067fcb786745f03382b0f3242126f4a0 import TrillMCastIpv4GroupList
        return TrillMCastIpv4GroupList(self)._select()

    @property
    def TrillMCastIpv6GroupList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.trillmcastipv6grouplist_18b118137ec4704f682253ecb0f4797b.TrillMCastIpv6GroupList): An instance of the TrillMCastIpv6GroupList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.trillmcastipv6grouplist_18b118137ec4704f682253ecb0f4797b import TrillMCastIpv6GroupList
        return TrillMCastIpv6GroupList(self)._select()

    @property
    def TrillMCastMacGroupList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.trillmcastmacgrouplist_fef95367003707238873712058525e55.TrillMCastMacGroupList): An instance of the TrillMCastMacGroupList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.trillmcastmacgrouplist_fef95367003707238873712058525e55 import TrillMCastMacGroupList
        return TrillMCastMacGroupList(self)._select()

    @property
    def TrillTopologyList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.trilltopologylist_d5329b70c837a29596a33cda2c9bc96d.TrillTopologyList): An instance of the TrillTopologyList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.trilltopologylist_d5329b70c837a29596a33cda2c9bc96d import TrillTopologyList
        return TrillTopologyList(self)._select()

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
    def CapabilityRouterId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Capability Router Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CapabilityRouterId']))

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
    def EnableHostName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Host Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableHostName']))

    @property
    def EnableMtuProbe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MTU Probe
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableMtuProbe']))

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
    def HostName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Host Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HostName']))

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
    def NoOfMtuProbes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No. of MTU Probes
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NoOfMtuProbes']))

    @property
    def OrigLspBufSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Originating LSP Buf Size(Sz)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OrigLspBufSize']))

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
    def TrillMCastIpv4GroupCount(self):
        """
        Returns
        -------
        - number: # Multicast IPv4 Groups(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrillMCastIpv4GroupCount'])
    @TrillMCastIpv4GroupCount.setter
    def TrillMCastIpv4GroupCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrillMCastIpv4GroupCount'], value)

    @property
    def TrillMCastIpv6GroupCount(self):
        """
        Returns
        -------
        - number: # Multicast IPv6 Groups(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrillMCastIpv6GroupCount'])
    @TrillMCastIpv6GroupCount.setter
    def TrillMCastIpv6GroupCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrillMCastIpv6GroupCount'], value)

    @property
    def TrillMCastMacGroupCount(self):
        """
        Returns
        -------
        - number: MAC Group Count(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrillMCastMacGroupCount'])
    @TrillMCastMacGroupCount.setter
    def TrillMCastMacGroupCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrillMCastMacGroupCount'], value)

    def update(self, Name=None, TrillMCastIpv4GroupCount=None, TrillMCastIpv6GroupCount=None, TrillMCastMacGroupCount=None):
        """Updates isisTrillRouter resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - TrillMCastIpv4GroupCount (number): # Multicast IPv4 Groups(multiplier)
        - TrillMCastIpv6GroupCount (number): # Multicast IPv6 Groups(multiplier)
        - TrillMCastMacGroupCount (number): MAC Group Count(multiplier)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Errors=None, LocalSystemID=None, Name=None, SessionInfo=None, SessionStatus=None, StateCounts=None, Status=None, TrillMCastIpv4GroupCount=None, TrillMCastIpv6GroupCount=None, TrillMCastMacGroupCount=None):
        """Finds and retrieves isisTrillRouter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisTrillRouter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisTrillRouter resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - LocalSystemID (list(str)): System ID
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionInfo (list(str[noIfaceUp | up])): Logs additional information about the session Information
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - TrillMCastIpv4GroupCount (number): # Multicast IPv4 Groups(multiplier)
        - TrillMCastIpv6GroupCount (number): # Multicast IPv6 Groups(multiplier)
        - TrillMCastMacGroupCount (number): MAC Group Count(multiplier)

        Returns
        -------
        - self: This instance with matching isisTrillRouter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisTrillRouter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisTrillRouter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AreaAddresses=None, AreaAuthenticationType=None, AreaTransmitPasswordOrMD5Key=None, Attached=None, CSNPInterval=None, CapabilityRouterId=None, DiscardLSPs=None, EnableHelloPadding=None, EnableHostName=None, EnableMtuProbe=None, EnableWideMetric=None, HostName=None, IgnoreReceiveMD5=None, InterLSPsOrMGroupPDUBurstGap=None, LSPLifetime=None, LSPRefreshRate=None, LSPorMGroupPDUMinTransmissionInterval=None, MaxAreaAddresses=None, MaxLSPSize=None, MaxLSPsOrMGroupPDUsPerBurst=None, NoOfMtuProbes=None, OrigLspBufSize=None, Overloaded=None, PSNPInterval=None, PartitionRepair=None):
        """Base class infrastructure that gets a list of isisTrillRouter device ids encapsulated by this object.

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
        - CapabilityRouterId (str): optional regex of capabilityRouterId
        - DiscardLSPs (str): optional regex of discardLSPs
        - EnableHelloPadding (str): optional regex of enableHelloPadding
        - EnableHostName (str): optional regex of enableHostName
        - EnableMtuProbe (str): optional regex of enableMtuProbe
        - EnableWideMetric (str): optional regex of enableWideMetric
        - HostName (str): optional regex of hostName
        - IgnoreReceiveMD5 (str): optional regex of ignoreReceiveMD5
        - InterLSPsOrMGroupPDUBurstGap (str): optional regex of interLSPsOrMGroupPDUBurstGap
        - LSPLifetime (str): optional regex of lSPLifetime
        - LSPRefreshRate (str): optional regex of lSPRefreshRate
        - LSPorMGroupPDUMinTransmissionInterval (str): optional regex of lSPorMGroupPDUMinTransmissionInterval
        - MaxAreaAddresses (str): optional regex of maxAreaAddresses
        - MaxLSPSize (str): optional regex of maxLSPSize
        - MaxLSPsOrMGroupPDUsPerBurst (str): optional regex of maxLSPsOrMGroupPDUsPerBurst
        - NoOfMtuProbes (str): optional regex of noOfMtuProbes
        - OrigLspBufSize (str): optional regex of origLspBufSize
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
