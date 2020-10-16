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


class IsisSRv6AdjSIDList(Base):
    """ISIS SRv6 Adj SID
    The IsisSRv6AdjSIDList class encapsulates a required isisSRv6AdjSIDList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isisSRv6AdjSIDList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdvertiseCustomSubTLV': 'advertiseCustomSubTLV',
        'Algorithm': 'algorithm',
        'ArgumentLength': 'argumentLength',
        'BFlag': 'bFlag',
        'Count': 'count',
        'CustomSubTlv': 'customSubTlv',
        'DescriptiveName': 'descriptiveName',
        'EndPointFunction': 'endPointFunction',
        'FunctionLength': 'functionLength',
        'IncludeSRv6SIDStructureSubSubTlv': 'includeSRv6SIDStructureSubSubTlv',
        'Ipv6AdjSid': 'ipv6AdjSid',
        'LocatorBlockLength': 'locatorBlockLength',
        'LocatorNodeLength': 'locatorNodeLength',
        'Name': 'name',
        'PFlag': 'pFlag',
        'Reserved': 'reserved',
        'SFlag': 'sFlag',
        'Weight': 'weight',
    }

    def __init__(self, parent):
        super(IsisSRv6AdjSIDList, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AdvertiseCustomSubTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise Custom Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseCustomSubTLV']))

    @property
    def Algorithm(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Algorithm
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Algorithm']))

    @property
    def ArgumentLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Argument Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ArgumentLength']))

    @property
    def BFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): B-Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFlag']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def CustomSubTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Custom Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CustomSubTlv']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EndPointFunction(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): End-Point Function
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EndPointFunction']))

    @property
    def FunctionLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Function Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FunctionLength']))

    @property
    def IncludeSRv6SIDStructureSubSubTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Include SRv6 SID Structure Sub-Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSRv6SIDStructureSubSubTlv']))

    @property
    def Ipv6AdjSid(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Adj SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6AdjSid']))

    @property
    def LocatorBlockLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Locator Block Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorBlockLength']))

    @property
    def LocatorNodeLength(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Locator Node Length in Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorNodeLength']))

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
    def PFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): P-Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlag']))

    @property
    def Reserved(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reserved
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def SFlag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): S-Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SFlag']))

    @property
    def Weight(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Weight
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    def update(self, Name=None):
        """Updates isisSRv6AdjSIDList resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, AdvertiseCustomSubTLV=None, Algorithm=None, ArgumentLength=None, BFlag=None, CustomSubTlv=None, EndPointFunction=None, FunctionLength=None, IncludeSRv6SIDStructureSubSubTlv=None, Ipv6AdjSid=None, LocatorBlockLength=None, LocatorNodeLength=None, PFlag=None, Reserved=None, SFlag=None, Weight=None):
        """Base class infrastructure that gets a list of isisSRv6AdjSIDList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdvertiseCustomSubTLV (str): optional regex of advertiseCustomSubTLV
        - Algorithm (str): optional regex of algorithm
        - ArgumentLength (str): optional regex of argumentLength
        - BFlag (str): optional regex of bFlag
        - CustomSubTlv (str): optional regex of customSubTlv
        - EndPointFunction (str): optional regex of endPointFunction
        - FunctionLength (str): optional regex of functionLength
        - IncludeSRv6SIDStructureSubSubTlv (str): optional regex of includeSRv6SIDStructureSubSubTlv
        - Ipv6AdjSid (str): optional regex of ipv6AdjSid
        - LocatorBlockLength (str): optional regex of locatorBlockLength
        - LocatorNodeLength (str): optional regex of locatorNodeLength
        - PFlag (str): optional regex of pFlag
        - Reserved (str): optional regex of reserved
        - SFlag (str): optional regex of sFlag
        - Weight (str): optional regex of weight

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
