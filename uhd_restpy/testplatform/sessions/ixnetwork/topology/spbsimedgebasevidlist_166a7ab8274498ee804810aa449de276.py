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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
from typing import List, Any, Union


class SpbSimEdgeBaseVidList(Base):
    """ISIS SPB Simulated Edge BaseVID Configuration
    The SpbSimEdgeBaseVidList class encapsulates a required spbSimEdgeBaseVidList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'spbSimEdgeBaseVidList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'BaseVid': 'baseVid',
        'BaseVlanPriority': 'baseVlanPriority',
        'BvlanTpid': 'bvlanTpid',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EctAlgorithm': 'ectAlgorithm',
        'IsidCount': 'isidCount',
        'Name': 'name',
        'UseFlagBit': 'useFlagBit',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(SpbSimEdgeBaseVidList, self).__init__(parent, list_op)

    @property
    def SpbSimEdgeIsidList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.spbsimedgeisidlist_cfeb124762b8e4653da4ea2e084e78c8.SpbSimEdgeIsidList): An instance of the SpbSimEdgeIsidList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.spbsimedgeisidlist_cfeb124762b8e4653da4ea2e084e78c8 import SpbSimEdgeIsidList
        if self._properties.get('SpbSimEdgeIsidList', None) is not None:
            return self._properties.get('SpbSimEdgeIsidList')
        else:
            return SpbSimEdgeIsidList(self)._select()

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def BaseVid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Base VID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BaseVid']))

    @property
    def BaseVlanPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): B-VLAN Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BaseVlanPriority']))

    @property
    def BvlanTpid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): B-VLAN TPID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BvlanTpid']))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EctAlgorithm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): ECT AlgorithmType
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EctAlgorithm']))

    @property
    def IsidCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: ISID Count(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsidCount'])
    @IsidCount.setter
    def IsidCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['IsidCount'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def UseFlagBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Use Flag Bit
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseFlagBit']))

    def update(self, IsidCount=None, Name=None):
        # type: (int, str) -> SpbSimEdgeBaseVidList
        """Updates spbSimEdgeBaseVidList resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, BaseVid=None, BaseVlanPriority=None, BvlanTpid=None, EctAlgorithm=None, UseFlagBit=None):
        """Base class infrastructure that gets a list of spbSimEdgeBaseVidList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - BaseVid (str): optional regex of baseVid
        - BaseVlanPriority (str): optional regex of baseVlanPriority
        - BvlanTpid (str): optional regex of bvlanTpid
        - EctAlgorithm (str): optional regex of ectAlgorithm
        - UseFlagBit (str): optional regex of useFlagBit

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
