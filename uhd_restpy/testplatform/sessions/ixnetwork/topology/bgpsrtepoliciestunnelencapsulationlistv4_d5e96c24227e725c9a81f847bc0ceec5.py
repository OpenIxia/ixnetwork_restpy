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


class BgpSRTEPoliciesTunnelEncapsulationListV4(Base):
    """
    The BgpSRTEPoliciesTunnelEncapsulationListV4 class encapsulates a required bgpSRTEPoliciesTunnelEncapsulationListV4 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpSRTEPoliciesTunnelEncapsulationListV4'
    _SDM_ATT_MAP = {
        'ENLPValue': 'ENLPValue',
        'IPv6SID': 'IPv6SID',
        'SID4Octet': 'SID4Octet',
        'Active': 'active',
        'AddressFamily': 'addressFamily',
        'As4Number': 'as4Number',
        'BindingSIDType': 'bindingSIDType',
        'ColorCOBits': 'colorCOBits',
        'ColorReservedBits': 'colorReservedBits',
        'ColorValue': 'colorValue',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnBindingTLV': 'enBindingTLV',
        'EnColorTLV': 'enColorTLV',
        'EnENLPTLV': 'enENLPTLV',
        'EnPolicyNameTLV': 'enPolicyNameTLV',
        'EnPolicyPrioritySubTLV': 'enPolicyPrioritySubTLV',
        'EnPrefTLV': 'enPrefTLV',
        'EnRemoteEndPointTLV': 'enRemoteEndPointTLV',
        'Name': 'name',
        'NumberOfActiveSegmentList': 'numberOfActiveSegmentList',
        'NumberOfSegmentListV4': 'numberOfSegmentListV4',
        'PolicyName': 'policyName',
        'PrefValue': 'prefValue',
        'Priority': 'priority',
        'RemoteEndpointIPv4': 'remoteEndpointIPv4',
        'RemoteEndpointIPv6': 'remoteEndpointIPv6',
        'SrtepolicyName': 'srtepolicyName',
        'TunnelType': 'tunnelType',
        'UseAsMPLSLabel': 'useAsMPLSLabel',
    }

    def __init__(self, parent):
        super(BgpSRTEPoliciesTunnelEncapsulationListV4, self).__init__(parent)

    @property
    def BgpSRTEPoliciesSegmentListV4(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepoliciessegmentlistv4_20f07dda61e493fe2f4aacf4ca7e10d5.BgpSRTEPoliciesSegmentListV4): An instance of the BgpSRTEPoliciesSegmentListV4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepoliciessegmentlistv4_20f07dda61e493fe2f4aacf4ca7e10d5 import BgpSRTEPoliciesSegmentListV4
        return BgpSRTEPoliciesSegmentListV4(self)._select()

    @property
    def ENLPValue(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Explicit NULL Label Policy Value
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ENLPValue']))

    @property
    def IPv6SID(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IPv6SID']))

    @property
    def SID4Octet(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): 4 Octet SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SID4Octet']))

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AddressFamily(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Address Family
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AddressFamily']))

    @property
    def As4Number(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): AS Number (4 Octects)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['As4Number']))

    @property
    def BindingSIDType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Binding SID Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BindingSIDType']))

    @property
    def ColorCOBits(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Color CO Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ColorCOBits']))

    @property
    def ColorReservedBits(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Color Reserved Bits
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ColorReservedBits']))

    @property
    def ColorValue(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Color Value
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ColorValue']))

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
    def EnBindingTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Binding Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnBindingTLV']))

    @property
    def EnColorTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Color Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnColorTLV']))

    @property
    def EnENLPTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Explicit NULL Label Policy Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnENLPTLV']))

    @property
    def EnPolicyNameTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Policy Name Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnPolicyNameTLV']))

    @property
    def EnPolicyPrioritySubTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Policy Priority Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnPolicyPrioritySubTLV']))

    @property
    def EnPrefTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Preference Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnPrefTLV']))

    @property
    def EnRemoteEndPointTLV(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Remote Endpoint Sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnRemoteEndPointTLV']))

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
    def NumberOfActiveSegmentList(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): 
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumberOfActiveSegmentList']))

    @property
    def NumberOfSegmentListV4(self):
        """
        Returns
        -------
        - number: Count of Segment Lists Per Tunnel
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfSegmentListV4'])
    @NumberOfSegmentListV4.setter
    def NumberOfSegmentListV4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfSegmentListV4'], value)

    @property
    def PolicyName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Policy Name
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PolicyName']))

    @property
    def PrefValue(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Preference
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrefValue']))

    @property
    def Priority(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Priority
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Priority']))

    @property
    def RemoteEndpointIPv4(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteEndpointIPv4']))

    @property
    def RemoteEndpointIPv6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteEndpointIPv6']))

    @property
    def SrtepolicyName(self):
        """
        Returns
        -------
        - list(str): Policy Name For Reference
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrtepolicyName'])

    @property
    def TunnelType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Tunnel Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TunnelType']))

    @property
    def UseAsMPLSLabel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Use BSID (SID 4 Octet) As MPLS Label
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UseAsMPLSLabel']))

    def update(self, Name=None, NumberOfSegmentListV4=None):
        """Updates bgpSRTEPoliciesTunnelEncapsulationListV4 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfSegmentListV4 (number): Count of Segment Lists Per Tunnel

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, ENLPValue=None, IPv6SID=None, SID4Octet=None, Active=None, AddressFamily=None, As4Number=None, BindingSIDType=None, ColorCOBits=None, ColorReservedBits=None, ColorValue=None, EnBindingTLV=None, EnColorTLV=None, EnENLPTLV=None, EnPolicyNameTLV=None, EnPolicyPrioritySubTLV=None, EnPrefTLV=None, EnRemoteEndPointTLV=None, NumberOfActiveSegmentList=None, PolicyName=None, PrefValue=None, Priority=None, RemoteEndpointIPv4=None, RemoteEndpointIPv6=None, TunnelType=None, UseAsMPLSLabel=None):
        """Base class infrastructure that gets a list of bgpSRTEPoliciesTunnelEncapsulationListV4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ENLPValue (str): optional regex of ENLPValue
        - IPv6SID (str): optional regex of IPv6SID
        - SID4Octet (str): optional regex of SID4Octet
        - Active (str): optional regex of active
        - AddressFamily (str): optional regex of addressFamily
        - As4Number (str): optional regex of as4Number
        - BindingSIDType (str): optional regex of bindingSIDType
        - ColorCOBits (str): optional regex of colorCOBits
        - ColorReservedBits (str): optional regex of colorReservedBits
        - ColorValue (str): optional regex of colorValue
        - EnBindingTLV (str): optional regex of enBindingTLV
        - EnColorTLV (str): optional regex of enColorTLV
        - EnENLPTLV (str): optional regex of enENLPTLV
        - EnPolicyNameTLV (str): optional regex of enPolicyNameTLV
        - EnPolicyPrioritySubTLV (str): optional regex of enPolicyPrioritySubTLV
        - EnPrefTLV (str): optional regex of enPrefTLV
        - EnRemoteEndPointTLV (str): optional regex of enRemoteEndPointTLV
        - NumberOfActiveSegmentList (str): optional regex of numberOfActiveSegmentList
        - PolicyName (str): optional regex of policyName
        - PrefValue (str): optional regex of prefValue
        - Priority (str): optional regex of priority
        - RemoteEndpointIPv4 (str): optional regex of remoteEndpointIPv4
        - RemoteEndpointIPv6 (str): optional regex of remoteEndpointIPv6
        - TunnelType (str): optional regex of tunnelType
        - UseAsMPLSLabel (str): optional regex of useAsMPLSLabel

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
