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


class BgpSRTEPoliciesSegmentsCollectionV4(Base):
    """
    The BgpSRTEPoliciesSegmentsCollectionV4 class encapsulates a required bgpSRTEPoliciesSegmentsCollectionV4 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpSRTEPoliciesSegmentsCollectionV4'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'BottomOfStack': 'bottomOfStack',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'InterfaceIndex': 'interfaceIndex',
        'Ipv4LocalAddress': 'ipv4LocalAddress',
        'Ipv4NodeAddress': 'ipv4NodeAddress',
        'Ipv4RemoteAddress': 'ipv4RemoteAddress',
        'Ipv6LocalAddress': 'ipv6LocalAddress',
        'Ipv6NodeAddress': 'ipv6NodeAddress',
        'Ipv6RemoteAddress': 'ipv6RemoteAddress',
        'Ipv6SID': 'ipv6SID',
        'Label': 'label',
        'Name': 'name',
        'OptionalBottomOfStack': 'optionalBottomOfStack',
        'OptionalIpv6SID': 'optionalIpv6SID',
        'OptionalLabel': 'optionalLabel',
        'OptionalTLVType': 'optionalTLVType',
        'OptionalTimeToLive': 'optionalTimeToLive',
        'OptionalTrafficClass': 'optionalTrafficClass',
        'SegmentListNumber': 'segmentListNumber',
        'SegmentType': 'segmentType',
        'SrtepolicyName': 'srtepolicyName',
        'TimeToLive': 'timeToLive',
        'TrafficClass': 'trafficClass',
    }

    def __init__(self, parent):
        super(BgpSRTEPoliciesSegmentsCollectionV4, self).__init__(parent)

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
    def BottomOfStack(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bottom Of Stack
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BottomOfStack']))

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
    def InterfaceIndex(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interface Index
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InterfaceIndex']))

    @property
    def Ipv4LocalAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Local Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4LocalAddress']))

    @property
    def Ipv4NodeAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Node Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4NodeAddress']))

    @property
    def Ipv4RemoteAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 Remote Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4RemoteAddress']))

    @property
    def Ipv6LocalAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Local Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6LocalAddress']))

    @property
    def Ipv6NodeAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Node Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6NodeAddress']))

    @property
    def Ipv6RemoteAddress(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 Remote Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6RemoteAddress']))

    @property
    def Ipv6SID(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6SID']))

    @property
    def Label(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Label
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Label']))

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
    def OptionalBottomOfStack(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Bottom Of Stack
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OptionalBottomOfStack']))

    @property
    def OptionalIpv6SID(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv6 SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OptionalIpv6SID']))

    @property
    def OptionalLabel(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Label
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OptionalLabel']))

    @property
    def OptionalTLVType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Optional TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OptionalTLVType']))

    @property
    def OptionalTimeToLive(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TTL
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OptionalTimeToLive']))

    @property
    def OptionalTrafficClass(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Traffic Class
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OptionalTrafficClass']))

    @property
    def SegmentListNumber(self):
        """
        Returns
        -------
        - list(str): Segment List Number For Reference
        """
        return self._get_attribute(self._SDM_ATT_MAP['SegmentListNumber'])

    @property
    def SegmentType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Segment Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SegmentType']))

    @property
    def SrtepolicyName(self):
        """
        Returns
        -------
        - list(str): Policy Name For Reference
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrtepolicyName'])

    @property
    def TimeToLive(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): TTL
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeToLive']))

    @property
    def TrafficClass(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Traffic Class
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TrafficClass']))

    def update(self, Name=None):
        """Updates bgpSRTEPoliciesSegmentsCollectionV4 resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, BottomOfStack=None, InterfaceIndex=None, Ipv4LocalAddress=None, Ipv4NodeAddress=None, Ipv4RemoteAddress=None, Ipv6LocalAddress=None, Ipv6NodeAddress=None, Ipv6RemoteAddress=None, Ipv6SID=None, Label=None, OptionalBottomOfStack=None, OptionalIpv6SID=None, OptionalLabel=None, OptionalTLVType=None, OptionalTimeToLive=None, OptionalTrafficClass=None, SegmentType=None, TimeToLive=None, TrafficClass=None):
        """Base class infrastructure that gets a list of bgpSRTEPoliciesSegmentsCollectionV4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - BottomOfStack (str): optional regex of bottomOfStack
        - InterfaceIndex (str): optional regex of interfaceIndex
        - Ipv4LocalAddress (str): optional regex of ipv4LocalAddress
        - Ipv4NodeAddress (str): optional regex of ipv4NodeAddress
        - Ipv4RemoteAddress (str): optional regex of ipv4RemoteAddress
        - Ipv6LocalAddress (str): optional regex of ipv6LocalAddress
        - Ipv6NodeAddress (str): optional regex of ipv6NodeAddress
        - Ipv6RemoteAddress (str): optional regex of ipv6RemoteAddress
        - Ipv6SID (str): optional regex of ipv6SID
        - Label (str): optional regex of label
        - OptionalBottomOfStack (str): optional regex of optionalBottomOfStack
        - OptionalIpv6SID (str): optional regex of optionalIpv6SID
        - OptionalLabel (str): optional regex of optionalLabel
        - OptionalTLVType (str): optional regex of optionalTLVType
        - OptionalTimeToLive (str): optional regex of optionalTimeToLive
        - OptionalTrafficClass (str): optional regex of optionalTrafficClass
        - SegmentType (str): optional regex of segmentType
        - TimeToLive (str): optional regex of timeToLive
        - TrafficClass (str): optional regex of trafficClass

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
