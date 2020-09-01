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


class Bfdv4Session(Base):
    """BFDv4 Session (Device) level Configuration
    The Bfdv4Session class encapsulates a required bfdv4Session resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bfdv4Session'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableAutoChooseSourceIp': 'enableAutoChooseSourceIp',
        'EnableOVSDBCommunication': 'enableOVSDBCommunication',
        'EnableRemoteDiscriminatorLearned': 'enableRemoteDiscriminatorLearned',
        'IpTTL': 'ipTTL',
        'LearnedRemoteIP': 'learnedRemoteIP',
        'LearnedRemoteMac': 'learnedRemoteMac',
        'LocalRouterId': 'localRouterId',
        'MyDiscriminator': 'myDiscriminator',
        'Name': 'name',
        'RemoteDiscriminator': 'remoteDiscriminator',
        'RemoteIp4': 'remoteIp4',
        'RemoteMac': 'remoteMac',
        'SessionInfo': 'sessionInfo',
        'SessionType': 'sessionType',
        'SourceIp4': 'sourceIp4',
        'Vni': 'vni',
    }

    def __init__(self, parent):
        super(Bfdv4Session, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

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
    def EnableAutoChooseSourceIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Selecting this check box enables the ability to configure the source IP address IP of BFD Session
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAutoChooseSourceIp']))

    @property
    def EnableOVSDBCommunication(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Selecting this check box enables the ability to communicate the remote IP and MAC address of BFD Session
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableOVSDBCommunication']))

    @property
    def EnableRemoteDiscriminatorLearned(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Selecting this check box enables the ability to configure the remote discriminator for BFD Session
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRemoteDiscriminatorLearned']))

    @property
    def IpTTL(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TTL value of inner ip of BFDoVXLAN packet
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpTTL']))

    @property
    def LearnedRemoteIP(self):
        """
        Returns
        -------
        - list(str): The learned remote IP address from controller
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnedRemoteIP'])

    @property
    def LearnedRemoteMac(self):
        """
        Returns
        -------
        - list(str): The learned remote MAC address from controller
        """
        return self._get_attribute(self._SDM_ATT_MAP['LearnedRemoteMac'])

    @property
    def LocalRouterId(self):
        """
        Returns
        -------
        - list(str): The BFD Router ID value, in IPv4 format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRouterId'])

    @property
    def MyDiscriminator(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The discriminator used locally for the BFD session
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MyDiscriminator']))

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
    def RemoteDiscriminator(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The remote discriminator used by the peer BFD for session
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteDiscriminator']))

    @property
    def RemoteIp4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The remote IP address used in BFD session
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteIp4']))

    @property
    def RemoteMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remote MAC Address of Peer
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteMac']))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[adminDown | awaitingIp | down | init | maxState | sessDeleted | unknownState | up]): Logs additional information about the Session state
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def SessionType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Session Type used in BFD session. One of: Single Hop, Multi Hops
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SessionType']))

    @property
    def SourceIp4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The source IP address used in BFD session
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceIp4']))

    @property
    def Vni(self):
        """
        Returns
        -------
        - list(number): Corresponding VXLAN Protocol VNI.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vni'])

    def update(self, Name=None):
        """Updates bfdv4Session resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, EnableAutoChooseSourceIp=None, EnableOVSDBCommunication=None, EnableRemoteDiscriminatorLearned=None, IpTTL=None, MyDiscriminator=None, RemoteDiscriminator=None, RemoteIp4=None, RemoteMac=None, SessionType=None, SourceIp4=None):
        """Base class infrastructure that gets a list of bfdv4Session device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - EnableAutoChooseSourceIp (str): optional regex of enableAutoChooseSourceIp
        - EnableOVSDBCommunication (str): optional regex of enableOVSDBCommunication
        - EnableRemoteDiscriminatorLearned (str): optional regex of enableRemoteDiscriminatorLearned
        - IpTTL (str): optional regex of ipTTL
        - MyDiscriminator (str): optional regex of myDiscriminator
        - RemoteDiscriminator (str): optional regex of remoteDiscriminator
        - RemoteIp4 (str): optional regex of remoteIp4
        - RemoteMac (str): optional regex of remoteMac
        - SessionType (str): optional regex of sessionType
        - SourceIp4 (str): optional regex of sourceIp4

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Activate Session

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        start(Arg2=list)list
        --------------------
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
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Deactivate Session

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        stop(Arg2=list)list
        -------------------
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
        return self._execute('stop', payload=payload, response_object=None)
