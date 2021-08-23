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
        'Funcflags': 'funcflags',
        'Function': 'function',
        'IncludeBIERInfo': 'includeBIERInfo',
        'IncludeBSLObject': 'includeBSLObject',
        'Ipv6SID': 'ipv6SID',
        'Ipv6Srh': 'ipv6Srh',
        'LFlag': 'lFlag',
        'LabelRangeSize': 'labelRangeSize',
        'LabelStart': 'labelStart',
        'LocalSystemID': 'localSystemID',
        'Metric': 'metric',
        'NFlag': 'nFlag',
        'Name': 'name',
        'NoOfSidperPrefix': 'noOfSidperPrefix',
        'PFlag': 'pFlag',
        'RFlag': 'rFlag',
        'Redistribution': 'redistribution',
        'ReservedInsideFlagsOfSRv6SidTLV': 'reservedInsideFlagsOfSRv6SidTLV',
        'RouteOrigin': 'routeOrigin',
        'SIDIndexLabel': 'sIDIndexLabel',
        'SubDomainId': 'subDomainId',
        'VFlag': 'vFlag',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(IsisL3RouteProperty, self).__init__(parent, list_op)

    @property
    def CMacProperties(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180.CMacProperties): An instance of the CMacProperties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180 import CMacProperties
        if self._properties.get('CMacProperties', None) is not None:
            return self._properties.get('CMacProperties')
        else:
            return CMacProperties(self)

    @property
    def EvpnIPv4PrefixRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f.EvpnIPv4PrefixRange): An instance of the EvpnIPv4PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f import EvpnIPv4PrefixRange
        if self._properties.get('EvpnIPv4PrefixRange', None) is not None:
            return self._properties.get('EvpnIPv4PrefixRange')
        else:
            return EvpnIPv4PrefixRange(self)

    @property
    def EvpnIPv6PrefixRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86.EvpnIPv6PrefixRange): An instance of the EvpnIPv6PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86 import EvpnIPv6PrefixRange
        if self._properties.get('EvpnIPv6PrefixRange', None) is not None:
            return self._properties.get('EvpnIPv6PrefixRange')
        else:
            return EvpnIPv6PrefixRange(self)

    @property
    def IsisL3PrefixesSrSid(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isisl3prefixessrsid_d90ea659336c02c3669004f4825a6c15.IsisL3PrefixesSrSid): An instance of the IsisL3PrefixesSrSid class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isisl3prefixessrsid_d90ea659336c02c3669004f4825a6c15 import IsisL3PrefixesSrSid
        if self._properties.get('IsisL3PrefixesSrSid', None) is not None:
            return self._properties.get('IsisL3PrefixesSrSid')
        else:
            return IsisL3PrefixesSrSid(self)._select()

    @property
    def BAR(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): BIER Algorithm
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BAR']))

    @property
    def BFRId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): BFR Id
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFRId']))

    @property
    def BFRIdStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): BFR Id Step
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFRIdStep']))

    @property
    def BIERBitStringLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bit String Length
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BIERBitStringLength']))

    @property
    def IPA(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IGP Algorithm
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IPA']))

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
    def AdvIPv6Prefix(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise IPv6 Prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvIPv6Prefix']))

    @property
    def Algorithm(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Algorithm
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Algorithm']))

    @property
    def ConfigureSIDIndexLabel(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Configure SID/Index/Label
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureSIDIndexLabel']))

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
    def DBitInsideSRv6SidTLV(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): When the SID is leaked from level-2 to level-1, the D bit MUST be set. Otherwise, this bit MUST be clear.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DBitInsideSRv6SidTLV']))

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
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Explicit NULL flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EFlag']))

    @property
    def Funcflags(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is the function flags
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Funcflags']))

    @property
    def Function(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies endpoint function codes
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Function']))

    @property
    def IncludeBIERInfo(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Include BIER Info
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeBIERInfo'])
    @IncludeBIERInfo.setter
    def IncludeBIERInfo(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['IncludeBIERInfo'], value)

    @property
    def IncludeBSLObject(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If set, MPLS encapsulation sub-sub-Tlv will be advertised under Bier Info Sub-Tlv
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeBSLObject']))

    @property
    def Ipv6SID(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This refers to the IPv6 SID that is being used to reach the advertised IPv6 Prefix
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6SID']))

    @property
    def Ipv6Srh(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Advertise IPv6 SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6Srh']))

    @property
    def LFlag(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Local Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LFlag']))

    @property
    def LabelRangeSize(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Maximum Set Identifier
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelRangeSize']))

    @property
    def LabelStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Label Start
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelStart']))

    @property
    def LocalSystemID(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): System ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalSystemID'])

    @property
    def Metric(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Metric
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Metric']))

    @property
    def NFlag(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Nodal prefix flag
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
    def NoOfSidperPrefix(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of SID's per prefix
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfSidperPrefix'])
    @NoOfSidperPrefix.setter
    def NoOfSidperPrefix(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfSidperPrefix'], value)

    @property
    def PFlag(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): No-PHP flag. If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlag']))

    @property
    def RFlag(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Redistribution flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RFlag']))

    @property
    def Redistribution(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Redistribution
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Redistribution']))

    @property
    def ReservedInsideFlagsOfSRv6SidTLV(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is the reserved field (part of Flags field of SRv6 SID TLV)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedInsideFlagsOfSRv6SidTLV']))

    @property
    def RouteOrigin(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Origin
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouteOrigin']))

    @property
    def SIDIndexLabel(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SID/Index/Label
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SIDIndexLabel']))

    @property
    def SubDomainId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Sub Domain Id
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubDomainId']))

    @property
    def VFlag(self):
        # type: () -> 'Multivalue'
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Value Flag
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VFlag']))

    def update(self, IncludeBIERInfo=None, Name=None, NoOfSidperPrefix=None):
        # type: (bool, str, int) -> IsisL3RouteProperty
        """Updates isisL3RouteProperty resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - IncludeBIERInfo (bool): Include BIER Info
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfSidperPrefix (number): Number of SID's per prefix

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeBIERInfo=None, Name=None, NoOfSidperPrefix=None):
        # type: (bool, str, int) -> IsisL3RouteProperty
        """Adds a new isisL3RouteProperty resource on the json, only valid with config assistant

        Args
        ----
        - IncludeBIERInfo (bool): Include BIER Info
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfSidperPrefix (number): Number of SID's per prefix

        Returns
        -------
        - self: This instance with all currently retrieved isisL3RouteProperty resources using find and the newly added isisL3RouteProperty resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, IncludeBIERInfo=None, LocalSystemID=None, Name=None, NoOfSidperPrefix=None):
        # type: (int, str, bool, List[str], str, int) -> IsisL3RouteProperty
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
        - NoOfSidperPrefix (number): Number of SID's per prefix

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

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def AgeOutRoutes(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the ageOutRoutes operation on the server.

        Age out percentage of ISIS Routes in a L3 Route Range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ageOutRoutes(Percentage=number, async_operation=bool)
        -----------------------------------------------------
        - Percentage (number): This parameter requires a percentage of type kInteger
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        ageOutRoutes(Percentage=number, SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------------------
        - Percentage (number): This parameter requires a percentage of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        ageOutRoutes(SessionIndices=string, Percentage=number, async_operation=bool)
        ----------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a percentage of type kInteger
        - Percentage (number): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the ageoutroutes operation on the server.

        Completely/Partially age out routes contained in this route range.

        ageoutroutes(Arg2=list, Arg3=number, async_operation=bool)list
        --------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - Arg3 (number): What percentage of routes to age out. 100% means all routes.
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
        return self._execute('ageoutroutes', payload=payload, response_object=None)

    def ReadvertiseRoutes(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the readvertiseRoutes operation on the server.

        Re-advertise Aged out ISIS Routes in a L3 Route Range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        readvertiseRoutes(async_operation=bool)
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        readvertiseRoutes(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        readvertiseRoutes(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the readvertiseroutes operation on the server.

        Readvertise only the aged-out routes contained in this route range.

        readvertiseroutes(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
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
        return self._execute('readvertiseroutes', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=list, async_operation=bool)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=string, async_operation=bool)
        -------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, BAR=None, BFRId=None, BFRIdStep=None, BIERBitStringLength=None, IPA=None, Active=None, AdvIPv6Prefix=None, Algorithm=None, ConfigureSIDIndexLabel=None, DBitInsideSRv6SidTLV=None, EFlag=None, Funcflags=None, Function=None, IncludeBSLObject=None, Ipv6SID=None, Ipv6Srh=None, LFlag=None, LabelRangeSize=None, LabelStart=None, Metric=None, NFlag=None, PFlag=None, RFlag=None, Redistribution=None, ReservedInsideFlagsOfSRv6SidTLV=None, RouteOrigin=None, SIDIndexLabel=None, SubDomainId=None, VFlag=None):
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
        - Funcflags (str): optional regex of funcflags
        - Function (str): optional regex of function
        - IncludeBSLObject (str): optional regex of includeBSLObject
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
