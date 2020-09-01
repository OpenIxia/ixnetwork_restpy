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


class MldMcastIPv6GroupList(Base):
    """MLD Multicast IPv6 Groups
    The MldMcastIPv6GroupList class encapsulates a required mldMcastIPv6GroupList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'mldMcastIPv6GroupList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'McastAddrCnt': 'mcastAddrCnt',
        'McastAddrIncr': 'mcastAddrIncr',
        'Name': 'name',
        'NoOfSrcRanges': 'noOfSrcRanges',
        'SourceMode': 'sourceMode',
        'StartMcastAddr': 'startMcastAddr',
        'State': 'state',
    }

    def __init__(self, parent):
        super(MldMcastIPv6GroupList, self).__init__(parent)

    @property
    def MldUcastIPv6SourceList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mlducastipv6sourcelist_d83ad2fbae6376e2b6cb9b364249dbb9.MldUcastIPv6SourceList): An instance of the MldUcastIPv6SourceList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mlducastipv6sourcelist_d83ad2fbae6376e2b6cb9b364249dbb9 import MldUcastIPv6SourceList
        return MldUcastIPv6SourceList(self)._select()

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
    def McastAddrCnt(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Address Count
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['McastAddrCnt']))

    @property
    def McastAddrIncr(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Address Increment
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['McastAddrIncr']))

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
    def NoOfSrcRanges(self):
        """
        Returns
        -------
        - number: Sources per Multicast Group (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfSrcRanges'])
    @NoOfSrcRanges.setter
    def NoOfSrcRanges(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfSrcRanges'], value)

    @property
    def SourceMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the IGMP/MLD Source Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceMode']))

    @property
    def StartMcastAddr(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start Multicast Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartMcastAddr']))

    @property
    def State(self):
        """
        Returns
        -------
        - list(str[iptv | joined | notJoined | notStarted]): Indicates the state of the groups in the range
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    def update(self, Name=None, NoOfSrcRanges=None):
        """Updates mldMcastIPv6GroupList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfSrcRanges (number): Sources per Multicast Group (multiplier)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, McastAddrCnt=None, McastAddrIncr=None, SourceMode=None, StartMcastAddr=None):
        """Base class infrastructure that gets a list of mldMcastIPv6GroupList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - McastAddrCnt (str): optional regex of mcastAddrCnt
        - McastAddrIncr (str): optional regex of mcastAddrIncr
        - SourceMode (str): optional regex of sourceMode
        - StartMcastAddr (str): optional regex of startMcastAddr

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Join(self, *args, **kwargs):
        """Executes the join operation on the server.

        Sends a Join on selected Group Ranges

        join(Arg2=list)list
        -------------------
        - Arg2 (list(number)): List of indices into the group range grid
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('join', payload=payload, response_object=None)

    def Leave(self, *args, **kwargs):
        """Executes the leave operation on the server.

        Sends a Leave on selected Group Ranges

        leave(Arg2=list)list
        --------------------
        - Arg2 (list(number)): List of indices into the group range grid
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('leave', payload=payload, response_object=None)

    def MldJoinGroup(self, *args, **kwargs):
        """Executes the mldJoinGroup operation on the server.

        Join Group

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        mldJoinGroup(SessionIndices=list)
        ---------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        mldJoinGroup(SessionIndices=string)
        -----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('mldJoinGroup', payload=payload, response_object=None)

    def MldLeaveGroup(self, *args, **kwargs):
        """Executes the mldLeaveGroup operation on the server.

        Leave Group

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        mldLeaveGroup(SessionIndices=list)
        ----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        mldLeaveGroup(SessionIndices=string)
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
        return self._execute('mldLeaveGroup', payload=payload, response_object=None)
