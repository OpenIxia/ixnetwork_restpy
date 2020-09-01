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


class SpbNodeTopologyList(Base):
    """SPB Node Topology
    The SpbNodeTopologyList class encapsulates a required spbNodeTopologyList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'spbNodeTopologyList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'BaseVIDCount': 'baseVIDCount',
        'CistExternalRootCost': 'cistExternalRootCost',
        'CistRootId': 'cistRootId',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Name': 'name',
        'NumberOfPorts': 'numberOfPorts',
        'PortIdentifier': 'portIdentifier',
        'TopologyId': 'topologyId',
        'Vbit': 'vbit',
    }

    def __init__(self, parent):
        super(SpbNodeTopologyList, self).__init__(parent)

    @property
    def BaseVidList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.basevidlist_0854f00d7287dd167f5cc03126e3011d.BaseVidList): An instance of the BaseVidList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.basevidlist_0854f00d7287dd167f5cc03126e3011d import BaseVidList
        return BaseVidList(self)._select()

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
    def BaseVIDCount(self):
        """
        Returns
        -------
        - number: Base VID Count(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['BaseVIDCount'])
    @BaseVIDCount.setter
    def BaseVIDCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BaseVIDCount'], value)

    @property
    def CistExternalRootCost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CIST External Root Cost
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CistExternalRootCost']))

    @property
    def CistRootId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CIST Root Identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CistRootId']))

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
    def NumberOfPorts(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of Ports
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumberOfPorts']))

    @property
    def PortIdentifier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Port Identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PortIdentifier']))

    @property
    def TopologyId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Topology Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TopologyId']))

    @property
    def Vbit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable V Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Vbit']))

    def update(self, BaseVIDCount=None, Name=None):
        """Updates spbNodeTopologyList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - BaseVIDCount (number): Base VID Count(multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, CistExternalRootCost=None, CistRootId=None, NumberOfPorts=None, PortIdentifier=None, TopologyId=None, Vbit=None):
        """Base class infrastructure that gets a list of spbNodeTopologyList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - CistExternalRootCost (str): optional regex of cistExternalRootCost
        - CistRootId (str): optional regex of cistRootId
        - NumberOfPorts (str): optional regex of numberOfPorts
        - PortIdentifier (str): optional regex of portIdentifier
        - TopologyId (str): optional regex of topologyId
        - Vbit (str): optional regex of vbit

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
