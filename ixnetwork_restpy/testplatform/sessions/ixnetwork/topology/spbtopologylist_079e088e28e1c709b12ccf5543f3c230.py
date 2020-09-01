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


class SpbTopologyList(Base):
    """ISIS SPB Topology Range Configuration
    The SpbTopologyList class encapsulates a required spbTopologyList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'spbTopologyList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AuxMcidConfName': 'auxMcidConfName',
        'AuxMcidSignature': 'auxMcidSignature',
        'BaseVidCount': 'baseVidCount',
        'BridgePriority': 'bridgePriority',
        'CistExternalRootCost': 'cistExternalRootCost',
        'CistRootId': 'cistRootId',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'LinkMetric': 'linkMetric',
        'McidConfName': 'mcidConfName',
        'McidSignature': 'mcidSignature',
        'Name': 'name',
        'NumberOfPorts': 'numberOfPorts',
        'PortIdentifier': 'portIdentifier',
        'SpSourceId': 'spSourceId',
        'TopologyId': 'topologyId',
        'Vbit': 'vbit',
    }

    def __init__(self, parent):
        super(SpbTopologyList, self).__init__(parent)

    @property
    def BaseVidList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.basevidlist_145d5b3b39acf879821ed1634b49f17f.BaseVidList): An instance of the BaseVidList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.basevidlist_145d5b3b39acf879821ed1634b49f17f import BaseVidList
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
    def AuxMcidConfName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aux MCID Config Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuxMcidConfName']))

    @property
    def AuxMcidSignature(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aux MCID Signature
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuxMcidSignature']))

    @property
    def BaseVidCount(self):
        """
        Returns
        -------
        - number: Base VID Count(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['BaseVidCount'])
    @BaseVidCount.setter
    def BaseVidCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BaseVidCount'], value)

    @property
    def BridgePriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bridge Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BridgePriority']))

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
    def LinkMetric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Link Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LinkMetric']))

    @property
    def McidConfName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MCID Config Name
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['McidConfName']))

    @property
    def McidSignature(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MCID Signature
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['McidSignature']))

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
    def SpSourceId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SP Source ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SpSourceId']))

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

    def update(self, BaseVidCount=None, Name=None):
        """Updates spbTopologyList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - BaseVidCount (number): Base VID Count(multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, AuxMcidConfName=None, AuxMcidSignature=None, BridgePriority=None, CistExternalRootCost=None, CistRootId=None, LinkMetric=None, McidConfName=None, McidSignature=None, NumberOfPorts=None, PortIdentifier=None, SpSourceId=None, TopologyId=None, Vbit=None):
        """Base class infrastructure that gets a list of spbTopologyList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AuxMcidConfName (str): optional regex of auxMcidConfName
        - AuxMcidSignature (str): optional regex of auxMcidSignature
        - BridgePriority (str): optional regex of bridgePriority
        - CistExternalRootCost (str): optional regex of cistExternalRootCost
        - CistRootId (str): optional regex of cistRootId
        - LinkMetric (str): optional regex of linkMetric
        - McidConfName (str): optional regex of mcidConfName
        - McidSignature (str): optional regex of mcidSignature
        - NumberOfPorts (str): optional regex of numberOfPorts
        - PortIdentifier (str): optional regex of portIdentifier
        - SpSourceId (str): optional regex of spSourceId
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
