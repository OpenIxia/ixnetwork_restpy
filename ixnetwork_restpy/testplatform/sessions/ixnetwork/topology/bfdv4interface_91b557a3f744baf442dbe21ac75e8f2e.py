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


class Bfdv4Interface(Base):
    """BFDv4 Interface (Device) level Configuration
    The Bfdv4Interface class encapsulates a list of bfdv4Interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Bfdv4Interface.find() method.
    The list can be managed by using the Bfdv4Interface.add() and Bfdv4Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bfdv4Interface'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AggregateBfdSession': 'aggregateBfdSession',
        'ConfigureEchoSourceIp': 'configureEchoSourceIp',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EchoRxInterval': 'echoRxInterval',
        'EchoTimeOut': 'echoTimeOut',
        'EchoTxInterval': 'echoTxInterval',
        'EnableControlPlaneIndependent': 'enableControlPlaneIndependent',
        'EnableDemandMode': 'enableDemandMode',
        'Errors': 'errors',
        'FlapTxIntervals': 'flapTxIntervals',
        'IpDiffServ': 'ipDiffServ',
        'LocalRouterId': 'localRouterId',
        'MinRxInterval': 'minRxInterval',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NoOfSessions': 'noOfSessions',
        'PollInterval': 'pollInterval',
        'SessionStatus': 'sessionStatus',
        'SourceIp4': 'sourceIp4',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TimeoutMultiplier': 'timeoutMultiplier',
        'TxInterval': 'txInterval',
        'Vni': 'vni',
    }

    def __init__(self, parent):
        super(Bfdv4Interface, self).__init__(parent)

    @property
    def Bfdv4Session(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4session_dfe5a64bfc5795e7fe612df749b6836a.Bfdv4Session): An instance of the Bfdv4Session class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4session_dfe5a64bfc5795e7fe612df749b6836a import Bfdv4Session
        return Bfdv4Session(self)._select()

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
    def AggregateBfdSession(self):
        """
        Returns
        -------
        - bool: If enabled, all interfaces except on VNI 0 will be disabled and grayed-out.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AggregateBfdSession'])
    @AggregateBfdSession.setter
    def AggregateBfdSession(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AggregateBfdSession'], value)

    @property
    def ConfigureEchoSourceIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Selecting this check box enables the ability to configure the source address IP of echo message
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureEchoSourceIp']))

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
    def EchoRxInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The minimum interval, in milliseconds, between received BFD Echo packets that this interface is capable of supporting. If this value is zero, the transmitting system does not support the receipt of BFD Echo packets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EchoRxInterval']))

    @property
    def EchoTimeOut(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The interval, in milliseconds, that the interface waits for a response to the last Echo packet sent out
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EchoTimeOut']))

    @property
    def EchoTxInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Echo packets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EchoTxInterval']))

    @property
    def EnableControlPlaneIndependent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This check box enables Control Plane Independent Mode. If set, the interface's BFD is implemented in the forwarding plane and can continue to function through disruptions in the control plane
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableControlPlaneIndependent']))

    @property
    def EnableDemandMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This check box enables Demand Mode. In this mode, it is assumed the interface has an independent way of verifying it has connectivity to the other system. Once a BFD session is established, the systems stop sending BFD Control packets, except when either system feels the need to verify connectivity explicitly. In this case, a short sequence of BFD Control packets is sent
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableDemandMode']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def FlapTxIntervals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of Tx packets sent from device after which session flaps for BFD. A value of zero means no flapping
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlapTxIntervals']))

    @property
    def IpDiffServ(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP DiffServ/TOSByte (Dec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpDiffServ']))

    @property
    def LocalRouterId(self):
        """
        Returns
        -------
        - list(str): The BFD Router ID value, in IPv4 format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRouterId'])

    @property
    def MinRxInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The minimum interval, in milliseconds, between received BFD Control packets that this interface is capable of supporting
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MinRxInterval']))

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
    def NoOfSessions(self):
        """
        Returns
        -------
        - number: The number of configured BFD sessions
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfSessions'])
    @NoOfSessions.setter
    def NoOfSessions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfSessions'], value)

    @property
    def PollInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The interval, in milliseconds, between exchanges of Control Messages in Demand Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PollInterval']))

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def SourceIp4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If Configure Echo Source-IP is selected, the IPv4 source address of the Echo Message
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceIp4']))

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
    def TimeoutMultiplier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The negotiated transmit interval, multiplied by this value, provides the detection time for the interface
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeoutMultiplier']))

    @property
    def TxInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Control packets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TxInterval']))

    @property
    def Vni(self):
        """
        Returns
        -------
        - list(number): Corresponding VXLAN Protocol VNI.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vni'])

    def update(self, AggregateBfdSession=None, ConnectedVia=None, Multiplier=None, Name=None, NoOfSessions=None, StackedLayers=None):
        """Updates bfdv4Interface resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - AggregateBfdSession (bool): If enabled, all interfaces except on VNI 0 will be disabled and grayed-out.
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfSessions (number): The number of configured BFD sessions
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AggregateBfdSession=None, ConnectedVia=None, Multiplier=None, Name=None, NoOfSessions=None, StackedLayers=None):
        """Adds a new bfdv4Interface resource on the server and adds it to the container.

        Args
        ----
        - AggregateBfdSession (bool): If enabled, all interfaces except on VNI 0 will be disabled and grayed-out.
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfSessions (number): The number of configured BFD sessions
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved bfdv4Interface resources using find and the newly added bfdv4Interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bfdv4Interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AggregateBfdSession=None, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, LocalRouterId=None, Multiplier=None, Name=None, NoOfSessions=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None, Vni=None):
        """Finds and retrieves bfdv4Interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bfdv4Interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bfdv4Interface resources from the server.

        Args
        ----
        - AggregateBfdSession (bool): If enabled, all interfaces except on VNI 0 will be disabled and grayed-out.
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - LocalRouterId (list(str)): The BFD Router ID value, in IPv4 format.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfSessions (number): The number of configured BFD sessions
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - Vni (list(number)): Corresponding VXLAN Protocol VNI.

        Returns
        -------
        - self: This instance with matching bfdv4Interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bfdv4Interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bfdv4Interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, ConfigureEchoSourceIp=None, EchoRxInterval=None, EchoTimeOut=None, EchoTxInterval=None, EnableControlPlaneIndependent=None, EnableDemandMode=None, FlapTxIntervals=None, IpDiffServ=None, MinRxInterval=None, PollInterval=None, SourceIp4=None, TimeoutMultiplier=None, TxInterval=None):
        """Base class infrastructure that gets a list of bfdv4Interface device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ConfigureEchoSourceIp (str): optional regex of configureEchoSourceIp
        - EchoRxInterval (str): optional regex of echoRxInterval
        - EchoTimeOut (str): optional regex of echoTimeOut
        - EchoTxInterval (str): optional regex of echoTxInterval
        - EnableControlPlaneIndependent (str): optional regex of enableControlPlaneIndependent
        - EnableDemandMode (str): optional regex of enableDemandMode
        - FlapTxIntervals (str): optional regex of flapTxIntervals
        - IpDiffServ (str): optional regex of ipDiffServ
        - MinRxInterval (str): optional regex of minRxInterval
        - PollInterval (str): optional regex of pollInterval
        - SourceIp4 (str): optional regex of sourceIp4
        - TimeoutMultiplier (str): optional regex of timeoutMultiplier
        - TxInterval (str): optional regex of txInterval

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

    def ClearLearnedInfo(self, *args, **kwargs):
        """Executes the clearLearnedInfo operation on the server.

        Clear Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearLearnedInfo(SessionIndices=list)
        -------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        clearLearnedInfo(SessionIndices=string)
        ---------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        clearLearnedInfo(Arg2=list)list
        -------------------------------
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
        return self._execute('clearLearnedInfo', payload=payload, response_object=None)

    def DisableDemandMode(self, *args, **kwargs):
        """Executes the disableDemandMode operation on the server.

        Disable Demand Mode

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        disableDemandMode(Arg2=list, Arg3=enum)list
        -------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        disableDemandMode(Arg2=enum)list
        --------------------------------
        - Arg2 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableDemandMode', payload=payload, response_object=None)

    def EnableDemandMode(self, *args, **kwargs):
        """Executes the enableDemandMode operation on the server.

        Enable Demand Mode

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        enableDemandMode(Arg2=list, Arg3=enum)list
        ------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        enableDemandMode(Arg2=enum)list
        -------------------------------
        - Arg2 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableDemandMode', payload=payload, response_object=None)

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

    def InitiatePoll(self, *args, **kwargs):
        """Executes the initiatePoll operation on the server.

        Initiate Poll

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        initiatePoll(Arg2=list, Arg3=enum)list
        --------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        initiatePoll(Arg2=enum)list
        ---------------------------
        - Arg2 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('initiatePoll', payload=payload, response_object=None)

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

    def ResumePDU(self, *args, **kwargs):
        """Executes the resumePDU operation on the server.

        Resume PDU

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumePDU(Arg2=list, Arg3=enum)list
        -----------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        resumePDU(Arg2=enum)list
        ------------------------
        - Arg2 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('resumePDU', payload=payload, response_object=None)

    def SetAdminDown(self, *args, **kwargs):
        """Executes the setAdminDown operation on the server.

        Set Admin Down

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        setAdminDown(Arg2=list, Arg3=enum)list
        --------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        setAdminDown(Arg2=enum)list
        ---------------------------
        - Arg2 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('setAdminDown', payload=payload, response_object=None)

    def SetAdminUp(self, *args, **kwargs):
        """Executes the setAdminUp operation on the server.

        Set Admin Up

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        setAdminUp(Arg2=list, Arg3=enum)list
        ------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        setAdminUp(Arg2=enum)list
        -------------------------
        - Arg2 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('setAdminUp', payload=payload, response_object=None)

    def SetDiagnosticState(self, *args, **kwargs):
        """Executes the setDiagnosticState operation on the server.

        Set Diagnostic State

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        setDiagnosticState(Arg2=list, Arg3=enum, Arg4=enum)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Arg4 (str(controlDetectionTimeExpired | echoFunctionFailed | neighbourSignaledSessionDown | forwardingPlaneReset | pathDown | concatenatedPathDown | administrativelyDown | reverseConcatenatedPathDown | reserved)): Diagnostic Code
        - Returns list(str): ID to associate each async action invocation

        setDiagnosticState(Arg2=enum, Arg3=enum)list
        --------------------------------------------
        - Arg2 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Arg3 (str(controlDetectionTimeExpired | echoFunctionFailed | neighbourSignaledSessionDown | forwardingPlaneReset | pathDown | concatenatedPathDown | administrativelyDown | reverseConcatenatedPathDown | reserved)): Diagnostic Code
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('setDiagnosticState', payload=payload, response_object=None)

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

    def StopPDU(self, *args, **kwargs):
        """Executes the stopPDU operation on the server.

        Stop PDU

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopPDU(Arg2=list, Arg3=enum)list
        ---------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        stopPDU(Arg2=enum)list
        ----------------------
        - Arg2 (str(ospf | ospfv3 | bgp | ldp | rsvp | isis | pim | bfd)): Session used by Protocol
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopPDU', payload=payload, response_object=None)
