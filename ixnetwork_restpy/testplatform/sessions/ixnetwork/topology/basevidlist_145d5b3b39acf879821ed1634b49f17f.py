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


class BaseVidList(Base):
    """ISIS SPB BaseVID Configuration
    The BaseVidList class encapsulates a required baseVidList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'baseVidList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'BaseVid': 'baseVid',
        'BaseVlanPriority': 'baseVlanPriority',
        'Bmac': 'bmac',
        'BmacSameAsSystemId': 'bmacSameAsSystemId',
        'BvlanTpid': 'bvlanTpid',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EctAlgorithm': 'ectAlgorithm',
        'IsidCount': 'isidCount',
        'Name': 'name',
        'TopologyId': 'topologyId',
        'UseFlagBit': 'useFlagBit',
    }

    def __init__(self, parent):
        super(BaseVidList, self).__init__(parent)

    @property
    def IsidList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isidlist_e6ba204fca19b050969280a4a79443f8.IsidList): An instance of the IsidList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isidlist_e6ba204fca19b050969280a4a79443f8 import IsidList
        return IsidList(self)._select()

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
    def BaseVid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Base VID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BaseVid']))

    @property
    def BaseVlanPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BaseVlanPriority']))

    @property
    def Bmac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B-MAC Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Bmac']))

    @property
    def BmacSameAsSystemId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BMAC Same As System Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BmacSameAsSystemId']))

    @property
    def BvlanTpid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BvlanTpid']))

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
    def EctAlgorithm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ECT AlgorithmType
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EctAlgorithm']))

    @property
    def IsidCount(self):
        """
        Returns
        -------
        - number: ISID Count(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsidCount'])
    @IsidCount.setter
    def IsidCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsidCount'], value)

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
    def TopologyId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Topology Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TopologyId']))

    @property
    def UseFlagBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Flag Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseFlagBit']))

    def update(self, IsidCount=None, Name=None):
        """Updates baseVidList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - IsidCount (number): ISID Count(multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, BaseVid=None, BaseVlanPriority=None, Bmac=None, BmacSameAsSystemId=None, BvlanTpid=None, EctAlgorithm=None, TopologyId=None, UseFlagBit=None):
        """Base class infrastructure that gets a list of baseVidList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - BaseVid (str): optional regex of baseVid
        - BaseVlanPriority (str): optional regex of baseVlanPriority
        - Bmac (str): optional regex of bmac
        - BmacSameAsSystemId (str): optional regex of bmacSameAsSystemId
        - BvlanTpid (str): optional regex of bvlanTpid
        - EctAlgorithm (str): optional regex of ectAlgorithm
        - TopologyId (str): optional regex of topologyId
        - UseFlagBit (str): optional regex of useFlagBit

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
