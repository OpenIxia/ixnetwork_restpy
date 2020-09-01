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


class DceTopologyList(Base):
    """Fabric-Path Topology
    The DceTopologyList class encapsulates a required dceTopologyList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dceTopologyList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableFTAG': 'enableFTAG',
        'InterestedVlanRangeCount': 'interestedVlanRangeCount',
        'Name': 'name',
        'NicknameCount': 'nicknameCount',
        'NoOfTreesToCompute': 'noOfTreesToCompute',
        'StartFTAGValue': 'startFTAGValue',
        'TopologyId': 'topologyId',
    }

    def __init__(self, parent):
        super(DceTopologyList, self).__init__(parent)

    @property
    def InterestedVlanList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interestedvlanlist_728a61dfe3033f50a4c4b24dd65f6d27.InterestedVlanList): An instance of the InterestedVlanList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interestedvlanlist_728a61dfe3033f50a4c4b24dd65f6d27 import InterestedVlanList
        return InterestedVlanList(self)._select()

    @property
    def NicknameRecordList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nicknamerecordlist_035390df83e22e146cb32cc19244f93b.NicknameRecordList): An instance of the NicknameRecordList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nicknamerecordlist_035390df83e22e146cb32cc19244f93b import NicknameRecordList
        return NicknameRecordList(self)._select()

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
    def EnableFTAG(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable FTAG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFTAG']))

    @property
    def InterestedVlanRangeCount(self):
        """
        Returns
        -------
        - number: Interested VLAN Range Count(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterestedVlanRangeCount'])
    @InterestedVlanRangeCount.setter
    def InterestedVlanRangeCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterestedVlanRangeCount'], value)

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
    def NicknameCount(self):
        """
        Returns
        -------
        - number: Nickname Count(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NicknameCount'])
    @NicknameCount.setter
    def NicknameCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NicknameCount'], value)

    @property
    def NoOfTreesToCompute(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No. of Trees to Compute
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NoOfTreesToCompute']))

    @property
    def StartFTAGValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start FTAG Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartFTAGValue']))

    @property
    def TopologyId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Topology Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TopologyId']))

    def update(self, InterestedVlanRangeCount=None, Name=None, NicknameCount=None):
        """Updates dceTopologyList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - InterestedVlanRangeCount (number): Interested VLAN Range Count(multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NicknameCount (number): Nickname Count(multiplier)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, EnableFTAG=None, NoOfTreesToCompute=None, StartFTAGValue=None, TopologyId=None):
        """Base class infrastructure that gets a list of dceTopologyList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - EnableFTAG (str): optional regex of enableFTAG
        - NoOfTreesToCompute (str): optional regex of noOfTreesToCompute
        - StartFTAGValue (str): optional regex of startFTAGValue
        - TopologyId (str): optional regex of topologyId

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
