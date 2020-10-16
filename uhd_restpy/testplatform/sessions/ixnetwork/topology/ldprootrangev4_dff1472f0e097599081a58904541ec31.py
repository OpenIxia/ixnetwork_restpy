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


class LdpRootRangeV4(Base):
    """LDP Basic RootRange V4 Configuration
    The LdpRootRangeV4 class encapsulates a required ldpRootRangeV4 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ldpRootRangeV4'
    _SDM_ATT_MAP = {
        'ContinuousIncrementOVAcrossRoot': 'continuousIncrementOVAcrossRoot',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'FilterOnGroupAddress': 'filterOnGroupAddress',
        'GroupCountPerLSP': 'groupCountPerLSP',
        'LspCountPerRoot': 'lspCountPerRoot',
        'Name': 'name',
        'NumberOfTLVs': 'numberOfTLVs',
        'RootAddress': 'rootAddress',
        'RootAddressCount': 'rootAddressCount',
        'RootAddressStep': 'rootAddressStep',
        'SourceAddressV4': 'sourceAddressV4',
        'SourceAddressV6': 'sourceAddressV6',
        'SourceCountPerLSP': 'sourceCountPerLSP',
        'StartGroupAddressV4': 'startGroupAddressV4',
        'StartGroupAddressV6': 'startGroupAddressV6',
    }

    def __init__(self, parent):
        super(LdpRootRangeV4, self).__init__(parent)

    @property
    def LdpTLVList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.ldptlvlist_30bf84fe9b838fe1c5800e633f13cff2.LdpTLVList): An instance of the LdpTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.ldptlvlist_30bf84fe9b838fe1c5800e633f13cff2 import LdpTLVList
        return LdpTLVList(self)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        return Tag(self)

    @property
    def ContinuousIncrementOVAcrossRoot(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Continuous Increment Opaque Value Across Root
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ContinuousIncrementOVAcrossRoot']))

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
    def FilterOnGroupAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If selected, all the LSPs will belong to the same set of groups
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FilterOnGroupAddress']))

    @property
    def GroupCountPerLSP(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Count Per LSP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupCountPerLSP']))

    @property
    def LspCountPerRoot(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): LSP Count Per Root
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspCountPerRoot']))

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
    def NumberOfTLVs(self):
        """
        Returns
        -------
        - number: Number Of TLVs
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfTLVs'])
    @NumberOfTLVs.setter
    def NumberOfTLVs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfTLVs'], value)

    @property
    def RootAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Root Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RootAddress']))

    @property
    def RootAddressCount(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Root Address Count
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RootAddressCount']))

    @property
    def RootAddressStep(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Root Address Step
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RootAddressStep']))

    @property
    def SourceAddressV4(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Source Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceAddressV4']))

    @property
    def SourceAddressV6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Source Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceAddressV6']))

    @property
    def SourceCountPerLSP(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source Count Per LSP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceCountPerLSP']))

    @property
    def StartGroupAddressV4(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Start Group Address(V4)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartGroupAddressV4']))

    @property
    def StartGroupAddressV6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Start Group Address(V6)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartGroupAddressV6']))

    def update(self, Name=None, NumberOfTLVs=None):
        """Updates ldpRootRangeV4 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfTLVs (number): Number Of TLVs

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, ContinuousIncrementOVAcrossRoot=None, FilterOnGroupAddress=None, GroupCountPerLSP=None, LspCountPerRoot=None, RootAddress=None, RootAddressCount=None, RootAddressStep=None, SourceAddressV4=None, SourceAddressV6=None, SourceCountPerLSP=None, StartGroupAddressV4=None, StartGroupAddressV6=None):
        """Base class infrastructure that gets a list of ldpRootRangeV4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ContinuousIncrementOVAcrossRoot (str): optional regex of continuousIncrementOVAcrossRoot
        - FilterOnGroupAddress (str): optional regex of filterOnGroupAddress
        - GroupCountPerLSP (str): optional regex of groupCountPerLSP
        - LspCountPerRoot (str): optional regex of lspCountPerRoot
        - RootAddress (str): optional regex of rootAddress
        - RootAddressCount (str): optional regex of rootAddressCount
        - RootAddressStep (str): optional regex of rootAddressStep
        - SourceAddressV4 (str): optional regex of sourceAddressV4
        - SourceAddressV6 (str): optional regex of sourceAddressV6
        - SourceCountPerLSP (str): optional regex of sourceCountPerLSP
        - StartGroupAddressV4 (str): optional regex of startGroupAddressV4
        - StartGroupAddressV6 (str): optional regex of startGroupAddressV6

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
