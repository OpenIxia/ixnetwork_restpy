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
from typing import List, Any, Union


class OspfFlexAlgorithmList(Base):
    """OSPF Flex Algorithm
    The OspfFlexAlgorithmList class encapsulates a required ospfFlexAlgorithmList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfFlexAlgorithmList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'CalcType': 'calcType',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableExcludeAg': 'enableExcludeAg',
        'EnableFadfTlv': 'enableFadfTlv',
        'EnableIncludeAllAg': 'enableIncludeAllAg',
        'EnableIncludeAnyAg': 'enableIncludeAnyAg',
        'ExcludeAgExtAg': 'excludeAgExtAg',
        'ExcludeAgExtAgLen': 'excludeAgExtAgLen',
        'FadFlag': 'fadFlag',
        'FadfLen': 'fadfLen',
        'FlexAlgo': 'flexAlgo',
        'IncludeAllAgExtAg': 'includeAllAgExtAg',
        'IncludeAllAgExtAgLen': 'includeAllAgExtAgLen',
        'IncludeAnyAgExtAg': 'includeAnyAgExtAg',
        'IncludeAnyAgExtAgLen': 'includeAnyAgExtAgLen',
        'MetricType': 'metricType',
        'Name': 'name',
        'Priority': 'priority',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(OspfFlexAlgorithmList, self).__init__(parent, list_op)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def CalcType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Calc Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CalcType']))

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
    def EnableExcludeAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, Flexible Algorithm Exclude Admin Group Sub TLV is advertised with FAD TLV. By default, it is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableExcludeAg']))

    @property
    def EnableFadfTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, OSPF Flexible Algorithm Definition Flags Sub-TLV (FADF sub-TLV) is advertised with FAD TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFadfTlv']))

    @property
    def EnableIncludeAllAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, Flexible Algorithm Extended Include All Admin Group Sub TLV is advertised with FAD TLV. By default, it is not enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableIncludeAllAg']))

    @property
    def EnableIncludeAnyAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, Flexible Algorithm Include Any Admin Group Sub TLV is advertised with FAD TLV. By default, it is not enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableIncludeAnyAg']))

    @property
    def ExcludeAgExtAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext AG denotes the Extended Admin Group. The default value is 0x00000001.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExcludeAgExtAg']))

    @property
    def ExcludeAgExtAgLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext AG Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExcludeAgExtAgLen']))

    @property
    def FadFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To set the M-Flag, the MSB should be set to 1. For Example : in Hex 0x80000000.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FadFlag']))

    @property
    def FadfLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FADF AG Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FadfLen']))

    @property
    def FlexAlgo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flex Algo
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlexAlgo']))

    @property
    def IncludeAllAgExtAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Include-All AG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAllAgExtAg']))

    @property
    def IncludeAllAgExtAgLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext AG Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAllAgExtAgLen']))

    @property
    def IncludeAnyAgExtAg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Include-Any AG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAnyAgExtAg']))

    @property
    def IncludeAnyAgExtAgLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext AG Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeAnyAgExtAgLen']))

    @property
    def MetricType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Metric Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetricType']))

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
    def Priority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Priority']))

    def update(self, Name=None):
        # type: (str) -> OspfFlexAlgorithmList
        """Updates ospfFlexAlgorithmList resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, CalcType=None, EnableExcludeAg=None, EnableFadfTlv=None, EnableIncludeAllAg=None, EnableIncludeAnyAg=None, ExcludeAgExtAg=None, ExcludeAgExtAgLen=None, FadFlag=None, FadfLen=None, FlexAlgo=None, IncludeAllAgExtAg=None, IncludeAllAgExtAgLen=None, IncludeAnyAgExtAg=None, IncludeAnyAgExtAgLen=None, MetricType=None, Priority=None):
        """Base class infrastructure that gets a list of ospfFlexAlgorithmList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - CalcType (str): optional regex of calcType
        - EnableExcludeAg (str): optional regex of enableExcludeAg
        - EnableFadfTlv (str): optional regex of enableFadfTlv
        - EnableIncludeAllAg (str): optional regex of enableIncludeAllAg
        - EnableIncludeAnyAg (str): optional regex of enableIncludeAnyAg
        - ExcludeAgExtAg (str): optional regex of excludeAgExtAg
        - ExcludeAgExtAgLen (str): optional regex of excludeAgExtAgLen
        - FadFlag (str): optional regex of fadFlag
        - FadfLen (str): optional regex of fadfLen
        - FlexAlgo (str): optional regex of flexAlgo
        - IncludeAllAgExtAg (str): optional regex of includeAllAgExtAg
        - IncludeAllAgExtAgLen (str): optional regex of includeAllAgExtAgLen
        - IncludeAnyAgExtAg (str): optional regex of includeAnyAgExtAg
        - IncludeAnyAgExtAgLen (str): optional regex of includeAnyAgExtAgLen
        - MetricType (str): optional regex of metricType
        - Priority (str): optional regex of priority

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
