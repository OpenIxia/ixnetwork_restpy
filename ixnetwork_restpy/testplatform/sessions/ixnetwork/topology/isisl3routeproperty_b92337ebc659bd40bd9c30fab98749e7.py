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


class IsisL3RouteProperty(Base):
    """ISIS L3 Route Range Table
    The IsisL3RouteProperty class encapsulates a list of isisL3RouteProperty resources that are managed by the system.
    A list of resources can be retrieved from the server using the IsisL3RouteProperty.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'isisL3RouteProperty'
    _SDM_ATT_MAP = {
        'BAR': 'BAR',
        'BFRId': 'BFRId',
        'BFRIdStep': 'BFRIdStep',
        'BIERBitStringLength': 'BIERBitStringLength',
        'IPA': 'IPA',
        'Active': 'active',
        'AdvIPv6Prefix': 'advIPv6Prefix',
        'Algorithm': 'algorithm',
        'ConfigureSIDIndexLabel': 'configureSIDIndexLabel',
        'Count': 'count',
        'DBitInsideSRv6SidTLV': 'dBitInsideSRv6SidTLV',
        'DescriptiveName': 'descriptiveName',
        'EFlag': 'eFlag',
        'Enable': 'enable',
        'EnableBit4': 'enableBit4',
        'EnableBit5': 'enableBit5',
        'EnableBit6': 'enableBit6',
        'EnableBit7': 'enableBit7',
        'EnableBit8': 'enableBit8',
        'EnableNFlag': 'enableNFlag',
        'EnableRFlag': 'enableRFlag',
        'EnableXFlag': 'enableXFlag',
        'Funcflags': 'funcflags',
        'Function': 'function',
        'IPv6SourceRouterID': 'iPv6SourceRouterID',
        'IncludeBIERInfo': 'includeBIERInfo',
        'IncludeBSLObject': 'includeBSLObject',
        'IncludeSourceRouterID': 'includeSourceRouterID',
        'Ipv4SourceRouterID': 'ipv4SourceRouterID',
        'Ipv6SID': 'ipv6SID',
        'Ipv6Srh': 'ipv6Srh',
        'LFlag': 'lFlag',
        'LabelRangeSize': 'labelRangeSize',
        'LabelStart': 'labelStart',
        'LocalSystemID': 'localSystemID',
        'Metric': 'metric',
        'NFlag': 'nFlag',
        'Name': 'name',
        'NoOfMtIds': 'noOfMtIds',
        'NoOfSidperPrefix': 'noOfSidperPrefix',
        'OverWriteRoutersMt': 'overWriteRoutersMt',
        'PFlag': 'pFlag',
        'RFlag': 'rFlag',
        'Redistribution': 'redistribution',
        'ReservedInsideFlagsOfSRv6SidTLV': 'reservedInsideFlagsOfSRv6SidTLV',
        'RouteOrigin': 'routeOrigin',
        'SIDIndexLabel': 'sIDIndexLabel',
        'SubDomainId': 'subDomainId',
        'VFlag': 'vFlag',
    }

    def __init__(self, parent):
        super(IsisL3RouteProperty, self).__init__(parent)

    @property
    def CMacProperties(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180.CMacProperties): An instance of the CMacProperties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180 import CMacProperties
        return CMacProperties(self)

    @property
    def EvpnIPv4PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f.EvpnIPv4PrefixRange): An instance of the EvpnIPv4PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f import EvpnIPv4PrefixRange
        return EvpnIPv4PrefixRange(self)

    @property
    def EvpnIPv6PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86.EvpnIPv6PrefixRange): An instance of the EvpnIPv6PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86 import EvpnIPv6PrefixRange
        return EvpnIPv6PrefixRange(self)

    @property
    def IsisL3PrefixesMtId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3prefixesmtid_c3122c5d3adb2a25f8100a28e93af4ac.IsisL3PrefixesMtId): An instance of the IsisL3PrefixesMtId class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3prefixesmtid_c3122c5d3adb2a25f8100a28e93af4ac import IsisL3PrefixesMtId
        return IsisL3PrefixesMtId(self)._select()

    @property
    def IsisL3PrefixesSrSid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3prefixessrsid_d90ea659336c02c3669004f4825a6c15.IsisL3PrefixesSrSid): An instance of the IsisL3PrefixesSrSid class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3prefixessrsid_d90ea659336c02c3669004f4825a6c15 import IsisL3PrefixesSrSid
        return IsisL3PrefixesSrSid(self)._select()

    @property
    def BAR(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BIER Algorithm
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BAR']))

    @property
    def BFRId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFR Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFRId']))

    @property
    def BFRIdStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFR Id Step
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFRIdStep']))

    @property
    def BIERBitStringLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bit String Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BIERBitStringLength']))

    @property
    def IPA(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IGP Algorithm
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IPA']))

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
    def AdvIPv6Prefix(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise IPv6 Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvIPv6Prefix']))

    @property
    def Algorithm(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Algorithm
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Algorithm']))

    @property
    def ConfigureSIDIndexLabel(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure SID/Index/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureSIDIndexLabel']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DBitInsideSRv6SidTLV(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When the SID is leaked from level-2 to level-1, the D bit MUST be set. Otherwise, this bit MUST be clear.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DBitInsideSRv6SidTLV']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EFlag(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Explicit NULL flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EFlag']))

    @property
    def Enable(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This,if enabled, sends the prefix attributes flags.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Enable']))

    @property
    def EnableBit4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 4th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBit4']))

    @property
    def EnableBit5(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 5th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBit5']))

    @property
    def EnableBit6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 6th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBit6']))

    @property
    def EnableBit7(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 7th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBit7']))

    @property
    def EnableBit8(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 8th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBit8']))

    @property
    def EnableNFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables node flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableNFlag']))

    @property
    def EnableRFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables redistribution flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableRFlag']))

    @property
    def EnableXFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables external flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableXFlag']))

    @property
    def Funcflags(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the function flags
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Funcflags']))

    @property
    def Function(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies endpoint function codes
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Function']))

    @property
    def IPv6SourceRouterID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This takes the value of the ipv6 source router id.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IPv6SourceRouterID']))

    @property
    def IncludeBIERInfo(self):
        """
        Returns
        -------
        - bool: Include BIER Info
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeBIERInfo'])
    @IncludeBIERInfo.setter
    def IncludeBIERInfo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeBIERInfo'], value)

    @property
    def IncludeBSLObject(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, MPLS encapsulation sub-sub-Tlv will be advertised under Bier Info Sub-Tlv
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeBSLObject']))

    @property
    def IncludeSourceRouterID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This drop box is provided to select ipv4 or ipv6 source id or none of them.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSourceRouterID']))

    @property
    def Ipv4SourceRouterID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This takes the value of the ipv4 source router id.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4SourceRouterID']))

    @property
    def Ipv6SID(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This refers to the IPv6 SID that is being used to reach the advertised IPv6 Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6SID']))

    @property
    def Ipv6Srh(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise IPv6 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6Srh']))

    @property
    def LFlag(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LFlag']))

    @property
    def LabelRangeSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Set Identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelRangeSize']))

    @property
    def LabelStart(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Start
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelStart']))

    @property
    def LocalSystemID(self):
        """
        Returns
        -------
        - list(str): System ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalSystemID'])

    @property
    def Metric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Metric']))

    @property
    def NFlag(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Nodal prefix flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NFlag']))

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
    def NoOfMtIds(self):
        """
        Returns
        -------
        - number: Number of MTIDs
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfMtIds'])
    @NoOfMtIds.setter
    def NoOfMtIds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfMtIds'], value)

    @property
    def NoOfSidperPrefix(self):
        """
        Returns
        -------
        - number: Number of SID's per prefix
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfSidperPrefix'])
    @NoOfSidperPrefix.setter
    def NoOfSidperPrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfSidperPrefix'], value)

    @property
    def OverWriteRoutersMt(self):
        """
        Returns
        -------
        - bool: If false, routers MT IDs which is union of all interfaces MTIDs would be used. If true, configured MT IDs in route range would be used
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverWriteRoutersMt'])
    @OverWriteRoutersMt.setter
    def OverWriteRoutersMt(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverWriteRoutersMt'], value)

    @property
    def PFlag(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No-PHP flag. If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlag']))

    @property
    def RFlag(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Redistribution flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RFlag']))

    @property
    def Redistribution(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Redistribution
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Redistribution']))

    @property
    def ReservedInsideFlagsOfSRv6SidTLV(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the reserved field (part of Flags field of SRv6 SID TLV)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedInsideFlagsOfSRv6SidTLV']))

    @property
    def RouteOrigin(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Origin
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouteOrigin']))

    @property
    def SIDIndexLabel(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SID/Index/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SIDIndexLabel']))

    @property
    def SubDomainId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub Domain Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubDomainId']))

    @property
    def VFlag(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VFlag']))

    def update(self, IncludeBIERInfo=None, Name=None, NoOfMtIds=None, NoOfSidperPrefix=None, OverWriteRoutersMt=None):
        """Updates isisL3RouteProperty resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - IncludeBIERInfo (bool): Include BIER Info
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfMtIds (number): Number of MTIDs
        - NoOfSidperPrefix (number): Number of SID's per prefix
        - OverWriteRoutersMt (bool): If false, routers MT IDs which is union of all interfaces MTIDs would be used. If true, configured MT IDs in route range would be used

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, IncludeBIERInfo=None, LocalSystemID=None, Name=None, NoOfMtIds=None, NoOfSidperPrefix=None, OverWriteRoutersMt=None):
        """Finds and retrieves isisL3RouteProperty resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisL3RouteProperty resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisL3RouteProperty resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - IncludeBIERInfo (bool): Include BIER Info
        - LocalSystemID (list(str)): System ID
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfMtIds (number): Number of MTIDs
        - NoOfSidperPrefix (number): Number of SID's per prefix
        - OverWriteRoutersMt (bool): If false, routers MT IDs which is union of all interfaces MTIDs would be used. If true, configured MT IDs in route range would be used

        Returns
        -------
        - self: This instance with matching isisL3RouteProperty resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisL3RouteProperty data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisL3RouteProperty resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, BAR=None, BFRId=None, BFRIdStep=None, BIERBitStringLength=None, IPA=None, Active=None, AdvIPv6Prefix=None, Algorithm=None, ConfigureSIDIndexLabel=None, DBitInsideSRv6SidTLV=None, EFlag=None, Enable=None, EnableBit4=None, EnableBit5=None, EnableBit6=None, EnableBit7=None, EnableBit8=None, EnableNFlag=None, EnableRFlag=None, EnableXFlag=None, Funcflags=None, Function=None, IPv6SourceRouterID=None, IncludeBSLObject=None, IncludeSourceRouterID=None, Ipv4SourceRouterID=None, Ipv6SID=None, Ipv6Srh=None, LFlag=None, LabelRangeSize=None, LabelStart=None, Metric=None, NFlag=None, PFlag=None, RFlag=None, Redistribution=None, ReservedInsideFlagsOfSRv6SidTLV=None, RouteOrigin=None, SIDIndexLabel=None, SubDomainId=None, VFlag=None):
        """Base class infrastructure that gets a list of isisL3RouteProperty device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BAR (str): optional regex of BAR
        - BFRId (str): optional regex of BFRId
        - BFRIdStep (str): optional regex of BFRIdStep
        - BIERBitStringLength (str): optional regex of BIERBitStringLength
        - IPA (str): optional regex of IPA
        - Active (str): optional regex of active
        - AdvIPv6Prefix (str): optional regex of advIPv6Prefix
        - Algorithm (str): optional regex of algorithm
        - ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
        - DBitInsideSRv6SidTLV (str): optional regex of dBitInsideSRv6SidTLV
        - EFlag (str): optional regex of eFlag
        - Enable (str): optional regex of enable
        - EnableBit4 (str): optional regex of enableBit4
        - EnableBit5 (str): optional regex of enableBit5
        - EnableBit6 (str): optional regex of enableBit6
        - EnableBit7 (str): optional regex of enableBit7
        - EnableBit8 (str): optional regex of enableBit8
        - EnableNFlag (str): optional regex of enableNFlag
        - EnableRFlag (str): optional regex of enableRFlag
        - EnableXFlag (str): optional regex of enableXFlag
        - Funcflags (str): optional regex of funcflags
        - Function (str): optional regex of function
        - IPv6SourceRouterID (str): optional regex of iPv6SourceRouterID
        - IncludeBSLObject (str): optional regex of includeBSLObject
        - IncludeSourceRouterID (str): optional regex of includeSourceRouterID
        - Ipv4SourceRouterID (str): optional regex of ipv4SourceRouterID
        - Ipv6SID (str): optional regex of ipv6SID
        - Ipv6Srh (str): optional regex of ipv6Srh
        - LFlag (str): optional regex of lFlag
        - LabelRangeSize (str): optional regex of labelRangeSize
        - LabelStart (str): optional regex of labelStart
        - Metric (str): optional regex of metric
        - NFlag (str): optional regex of nFlag
        - PFlag (str): optional regex of pFlag
        - RFlag (str): optional regex of rFlag
        - Redistribution (str): optional regex of redistribution
        - ReservedInsideFlagsOfSRv6SidTLV (str): optional regex of reservedInsideFlagsOfSRv6SidTLV
        - RouteOrigin (str): optional regex of routeOrigin
        - SIDIndexLabel (str): optional regex of sIDIndexLabel
        - SubDomainId (str): optional regex of subDomainId
        - VFlag (str): optional regex of vFlag

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('abort', payload=payload, response_object=None)

    def AgeOutRoutes(self, *args, **kwargs):
        """Executes the ageOutRoutes operation on the server.

        Age out percentage of ISIS Routes in a L3 Route Range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ageOutRoutes(Percentage=number)
        -------------------------------
        - Percentage (number): This parameter requires a percentage of type kInteger

        ageOutRoutes(Percentage=number, SessionIndices=list)
        ----------------------------------------------------
        - Percentage (number): This parameter requires a percentage of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        ageOutRoutes(SessionIndices=string, Percentage=number)
        ------------------------------------------------------
        - SessionIndices (str): This parameter requires a percentage of type kInteger
        - Percentage (number): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ageOutRoutes', payload=payload, response_object=None)

    def Ageoutroutes(self, *args, **kwargs):
        """Executes the ageoutroutes operation on the server.

        Completely/Partially age out routes contained in this route range.

        ageoutroutes(Arg2=list, Arg3=number)list
        ----------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - Arg3 (number): What percentage of routes to age out. 100% means all routes.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ageoutroutes', payload=payload, response_object=None)

    def ReadvertiseRoutes(self, *args, **kwargs):
        """Executes the readvertiseRoutes operation on the server.

        Re-advertise Aged out ISIS Routes in a L3 Route Range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        readvertiseRoutes(SessionIndices=list)
        --------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        readvertiseRoutes(SessionIndices=string)
        ----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('readvertiseRoutes', payload=payload, response_object=None)

    def Readvertiseroutes(self, *args, **kwargs):
        """Executes the readvertiseroutes operation on the server.

        Readvertise only the aged-out routes contained in this route range.

        readvertiseroutes(Arg2=list)list
        --------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('readvertiseroutes', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
