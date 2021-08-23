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


class IsisMappingServerIPV6List(Base):
    """ISIS Mapping Server IPV6
    The IsisMappingServerIPV6List class encapsulates a required isisMappingServerIPV6List resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isisMappingServerIPV6List'
    _SDM_ATT_MAP = {
        'AFlag': 'aFlag',
        'Active': 'active',
        'Algorithm': 'algorithm',
        'Count': 'count',
        'DFlag': 'dFlag',
        'DescriptiveName': 'descriptiveName',
        'EFlag': 'eFlag',
        'FECPrefix': 'fECPrefix',
        'LFlag': 'lFlag',
        'LastFECAddress': 'lastFECAddress',
        'MFlag': 'mFlag',
        'NFlag': 'nFlag',
        'Name': 'name',
        'PFlag': 'pFlag',
        'PrefixLength': 'prefixLength',
        'RFlag': 'rFlag',
        'Range': 'range',
        'SFlag': 'sFlag',
        'StartSIDLabel': 'startSIDLabel',
        'VFlag': 'vFlag',
        'Weight': 'weight',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(IsisMappingServerIPV6List, self).__init__(parent, list_op)

    @property
    def AFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Attached flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AFlag']))

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def Algorithm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Algorithm
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Algorithm']))

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
    def DFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): When the SID/Label Binding TLV is leaked from level-2 to level-1, this flag MUST be set, else it should be clear
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DFlag']))

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
    def EFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Explicit NULL flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EFlag']))

    @property
    def FECPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 FEC Prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FECPrefix']))

    @property
    def LFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Local Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LFlag']))

    @property
    def LastFECAddress(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Last IPv6 FEC Address
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastFECAddress'])

    @property
    def MFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Mirror Context flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MFlag']))

    @property
    def NFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): N Flag: Indicates the nodal prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NFlag']))

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
    def PFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): P Flag: Indicates that to reach to a prefix, this router would be penultimate hop.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlag']))

    @property
    def PrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Length of the IPv4 FEC prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrefixLength']))

    @property
    def RFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Redistribution flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RFlag']))

    @property
    def Range(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This the count of continuous FEC IPv6 prefixes and their respective continuous SID/labels
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Range']))

    @property
    def SFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enabling this flag lets the SID/Label Binding TLV to get flooded across the entire routing domain, else this TLV should not be leaked between levels
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SFlag']))

    @property
    def StartSIDLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Starting value of SID/ Label
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartSIDLabel']))

    @property
    def VFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Value Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VFlag']))

    @property
    def Weight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Weight
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    def update(self, Name=None):
        # type: (str) -> IsisMappingServerIPV6List
        """Updates isisMappingServerIPV6List resource on the server.

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

    def Advertise(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the advertise operation on the server.

        Advertise the V6 Mapping Server Range TLVs

        advertise(Arg2=list, async_operation=bool)list
        ----------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('advertise', payload=payload, response_object=None)

    def Withdraw(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the withdraw operation on the server.

        Withdraw the V6 Mapping Server Range TLVs

        withdraw(Arg2=list, async_operation=bool)list
        ---------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('withdraw', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, AFlag=None, Active=None, Algorithm=None, DFlag=None, EFlag=None, FECPrefix=None, LFlag=None, MFlag=None, NFlag=None, PFlag=None, PrefixLength=None, RFlag=None, Range=None, SFlag=None, StartSIDLabel=None, VFlag=None, Weight=None):
        """Base class infrastructure that gets a list of isisMappingServerIPV6List device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AFlag (str): optional regex of aFlag
        - Active (str): optional regex of active
        - Algorithm (str): optional regex of algorithm
        - DFlag (str): optional regex of dFlag
        - EFlag (str): optional regex of eFlag
        - FECPrefix (str): optional regex of fECPrefix
        - LFlag (str): optional regex of lFlag
        - MFlag (str): optional regex of mFlag
        - NFlag (str): optional regex of nFlag
        - PFlag (str): optional regex of pFlag
        - PrefixLength (str): optional regex of prefixLength
        - RFlag (str): optional regex of rFlag
        - Range (str): optional regex of range
        - SFlag (str): optional regex of sFlag
        - StartSIDLabel (str): optional regex of startSIDLabel
        - VFlag (str): optional regex of vFlag
        - Weight (str): optional regex of weight

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
