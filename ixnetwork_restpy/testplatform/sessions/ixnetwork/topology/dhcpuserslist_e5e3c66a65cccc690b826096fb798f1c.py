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


class DhcpUsersList(Base):
    """DHCP Subscribers.
    The DhcpUsersList class encapsulates a required dhcpUsersList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpUsersList'
    _SDM_ATT_MAP = {
        'AccessType': 'accessType',
        'AccountType': 'accountType',
        'Active': 'active',
        'AdvertiseFlag': 'advertiseFlag',
        'Cbs': 'cbs',
        'CbsEgress': 'cbsEgress',
        'CbsUnit': 'cbsUnit',
        'CbsUnitEgress': 'cbsUnitEgress',
        'ChassisNumber': 'chassisNumber',
        'Cir': 'cir',
        'CirEgress': 'cirEgress',
        'CirUnit': 'cirUnit',
        'CirUnitEgress': 'cirUnitEgress',
        'Cost': 'cost',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DetectInterval': 'detectInterval',
        'DetectTimes': 'detectTimes',
        'EchoEnable': 'echoEnable',
        'EgressHqosLevel2InstanceName': 'egressHqosLevel2InstanceName',
        'EgressHqosLevel3ProfileName': 'egressHqosLevel3ProfileName',
        'EgressHqosLevel4ProfileName': 'egressHqosLevel4ProfileName',
        'EgressPriority': 'egressPriority',
        'EgressUPGroupName': 'egressUPGroupName',
        'EnableIfDescTLV': 'enableIfDescTLV',
        'EnableMSS': 'enableMSS',
        'GatewayAddress': 'gatewayAddress',
        'GatewayPrefixLength': 'gatewayPrefixLength',
        'HqosBwModifyMethod': 'hqosBwModifyMethod',
        'IncludeUserAuthInfo': 'includeUserAuthInfo',
        'IngressHqosLevel2InstanceName': 'ingressHqosLevel2InstanceName',
        'IngressHqosLevel3ProfileName': 'ingressHqosLevel3ProfileName',
        'IngressHqosLevel4ProfileName': 'ingressHqosLevel4ProfileName',
        'IngressPriority': 'ingressPriority',
        'IngressUPGroupName': 'ingressUPGroupName',
        'Ipv4Prefix': 'ipv4Prefix',
        'Ipv4PrefixLength': 'ipv4PrefixLength',
        'Ipv4Urf': 'ipv4Urf',
        'LogicID': 'logicID',
        'McastProfilev4Name': 'mcastProfilev4Name',
        'McastProfilev6Name': 'mcastProfilev6Name',
        'Mss': 'mss',
        'Mtu': 'mtu',
        'MvipStack': 'mvipStack',
        'Name': 'name',
        'NatInstance': 'natInstance',
        'NextHopAddress': 'nextHopAddress',
        'NextHopPrefixLength': 'nextHopPrefixLength',
        'Pbs': 'pbs',
        'PbsEgress': 'pbsEgress',
        'PbsUnit': 'pbsUnit',
        'PbsUnitEgress': 'pbsUnitEgress',
        'Pir': 'pir',
        'PirEgress': 'pirEgress',
        'PirUnit': 'pirUnit',
        'PirUnitEgress': 'pirUnitEgress',
        'PortNumber': 'portNumber',
        'PortType': 'portType',
        'PortalForce': 'portalForce',
        'RouteType': 'routeType',
        'SlotNumber': 'slotNumber',
        'SubAccessType': 'subAccessType',
        'SubPortNumber': 'subPortNumber',
        'SubTlvs': 'subTlvs',
        'SubslotNumber': 'subslotNumber',
        'Tag': 'tag',
        'UserIPAuthorType': 'userIPAuthorType',
        'UserIPRunType': 'userIPRunType',
        'WebForce': 'webForce',
        'WebPortalProfileName': 'webPortalProfileName',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(DhcpUsersList, self).__init__(parent, list_op)

    @property
    def AccessType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Access Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AccessType']))

    @property
    def AccountType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Account Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AccountType']))

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AdvertiseFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseFlag']))

    @property
    def Cbs(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The token bucket in bytes.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Cbs']))

    @property
    def CbsEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The token bucket in bytes.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CbsEgress']))

    @property
    def CbsUnit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Guaranteed Token Bucket Unit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CbsUnit']))

    @property
    def CbsUnitEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Guaranteed Token Bucket Unit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CbsUnitEgress']))

    @property
    def ChassisNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Chassis number.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ChassisNumber']))

    @property
    def Cir(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Committed Information Rate.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Cir']))

    @property
    def CirEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Committed Information Rate.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CirEgress']))

    @property
    def CirUnit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Guaranteed rate units.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CirUnit']))

    @property
    def CirUnitEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Guaranteed rate units.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CirUnitEgress']))

    @property
    def Cost(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Cost
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Cost']))

    @property
    def Count(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Subscriber Count in a Group.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Count']))

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
    def DetectInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Detect Interval (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DetectInterval']))

    @property
    def DetectTimes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Detect Times,0 no probe
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DetectTimes']))

    @property
    def EchoEnable(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Echo-Enable.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EchoEnable']))

    @property
    def EgressHqosLevel2InstanceName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Egress HQoS Level 2 Instance Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EgressHqosLevel2InstanceName']))

    @property
    def EgressHqosLevel3ProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Egress HQoS Level 3 Profile Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EgressHqosLevel3ProfileName']))

    @property
    def EgressHqosLevel4ProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Egress HQoS Level 4 Profile Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EgressHqosLevel4ProfileName']))

    @property
    def EgressPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Egress-Priority.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EgressPriority']))

    @property
    def EgressUPGroupName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Egress-User-Policy-Group Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EgressUPGroupName']))

    @property
    def EnableIfDescTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable IF DESC TLV. It will advertise back the IF DESC advertised by UP.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableIfDescTLV']))

    @property
    def EnableMSS(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MSS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableMSS']))

    @property
    def GatewayAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Gateway Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GatewayAddress']))

    @property
    def GatewayPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Gateway Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GatewayPrefixLength']))

    @property
    def HqosBwModifyMethod(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): HQoS Bandwidth Modiy Method.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HqosBwModifyMethod']))

    @property
    def IncludeUserAuthInfo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include User Auth Info.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeUserAuthInfo']))

    @property
    def IngressHqosLevel2InstanceName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ingress HQoS Level 2 Instance Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IngressHqosLevel2InstanceName']))

    @property
    def IngressHqosLevel3ProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ingress HQoS Level 3 Profile Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IngressHqosLevel3ProfileName']))

    @property
    def IngressHqosLevel4ProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ingress HQoS Level 4 Profile Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IngressHqosLevel4ProfileName']))

    @property
    def IngressPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ingress-Priority.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IngressPriority']))

    @property
    def IngressUPGroupName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ingress-User-Policy-Group Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IngressUPGroupName']))

    @property
    def Ipv4Prefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 prefix of the user.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4Prefix']))

    @property
    def Ipv4PrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4PrefixLength']))

    @property
    def Ipv4Urf(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4-URPF.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4Urf']))

    @property
    def LogicID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Virtual port number.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LogicID']))

    @property
    def McastProfilev4Name(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Profilev4 Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['McastProfilev4Name']))

    @property
    def McastProfilev6Name(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Profilev6 Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['McastProfilev6Name']))

    @property
    def Mss(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MSS Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Mss']))

    @property
    def Mtu(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MTU
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Mtu']))

    @property
    def MvipStack(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This drop box is provided to select ipv4 or ipv6 or dual stack subscribers.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MvipStack']))

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
    def NatInstance(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Nat Instance Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NatInstance']))

    @property
    def NextHopAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Next Hop address of the UP.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextHopAddress']))

    @property
    def NextHopPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Next Hop Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NextHopPrefixLength']))

    @property
    def Pbs(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst token buckets in bytes.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Pbs']))

    @property
    def PbsEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst token buckets in bytes.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PbsEgress']))

    @property
    def PbsUnit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst Token Bucket Unit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PbsUnit']))

    @property
    def PbsUnitEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst Token Bucket Unit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PbsUnitEgress']))

    @property
    def Pir(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peak Information Rate.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Pir']))

    @property
    def PirEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peak Information Rate.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PirEgress']))

    @property
    def PirUnit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst rate units.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PirUnit']))

    @property
    def PirUnitEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst rate units.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PirUnitEgress']))

    @property
    def PortNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Physical port number.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PortNumber']))

    @property
    def PortType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The type of the Port.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PortType']))

    @property
    def PortalForce(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Portal-Force.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PortalForce']))

    @property
    def RouteType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouteType']))

    @property
    def SlotNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Interface index.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlotNumber']))

    @property
    def SubAccessType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub Access Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubAccessType']))

    @property
    def SubPortNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub port number.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubPortNumber']))

    @property
    def SubTlvs(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub TLVs.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubTlvs']))

    @property
    def SubslotNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Interface index.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubslotNumber']))

    @property
    def Tag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Tag']))

    @property
    def UserIPAuthorType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User IP Author Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UserIPAuthorType']))

    @property
    def UserIPRunType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User IP Run Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UserIPRunType']))

    @property
    def WebForce(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Web-Force.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WebForce']))

    @property
    def WebPortalProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Web Portal Profile Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['WebPortalProfileName']))

    def update(self, Name=None):
        # type: (str) -> DhcpUsersList
        """Updates dhcpUsersList resource on the server.

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

    def get_device_ids(self, PortNames=None, AccessType=None, AccountType=None, Active=None, AdvertiseFlag=None, Cbs=None, CbsEgress=None, CbsUnit=None, CbsUnitEgress=None, ChassisNumber=None, Cir=None, CirEgress=None, CirUnit=None, CirUnitEgress=None, Cost=None, Count=None, DetectInterval=None, DetectTimes=None, EchoEnable=None, EgressHqosLevel2InstanceName=None, EgressHqosLevel3ProfileName=None, EgressHqosLevel4ProfileName=None, EgressPriority=None, EgressUPGroupName=None, EnableIfDescTLV=None, EnableMSS=None, GatewayAddress=None, GatewayPrefixLength=None, HqosBwModifyMethod=None, IncludeUserAuthInfo=None, IngressHqosLevel2InstanceName=None, IngressHqosLevel3ProfileName=None, IngressHqosLevel4ProfileName=None, IngressPriority=None, IngressUPGroupName=None, Ipv4Prefix=None, Ipv4PrefixLength=None, Ipv4Urf=None, LogicID=None, McastProfilev4Name=None, McastProfilev6Name=None, Mss=None, Mtu=None, MvipStack=None, NatInstance=None, NextHopAddress=None, NextHopPrefixLength=None, Pbs=None, PbsEgress=None, PbsUnit=None, PbsUnitEgress=None, Pir=None, PirEgress=None, PirUnit=None, PirUnitEgress=None, PortNumber=None, PortType=None, PortalForce=None, RouteType=None, SlotNumber=None, SubAccessType=None, SubPortNumber=None, SubTlvs=None, SubslotNumber=None, Tag=None, UserIPAuthorType=None, UserIPRunType=None, WebForce=None, WebPortalProfileName=None):
        """Base class infrastructure that gets a list of dhcpUsersList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AccessType (str): optional regex of accessType
        - AccountType (str): optional regex of accountType
        - Active (str): optional regex of active
        - AdvertiseFlag (str): optional regex of advertiseFlag
        - Cbs (str): optional regex of cbs
        - CbsEgress (str): optional regex of cbsEgress
        - CbsUnit (str): optional regex of cbsUnit
        - CbsUnitEgress (str): optional regex of cbsUnitEgress
        - ChassisNumber (str): optional regex of chassisNumber
        - Cir (str): optional regex of cir
        - CirEgress (str): optional regex of cirEgress
        - CirUnit (str): optional regex of cirUnit
        - CirUnitEgress (str): optional regex of cirUnitEgress
        - Cost (str): optional regex of cost
        - Count (str): optional regex of count
        - DetectInterval (str): optional regex of detectInterval
        - DetectTimes (str): optional regex of detectTimes
        - EchoEnable (str): optional regex of echoEnable
        - EgressHqosLevel2InstanceName (str): optional regex of egressHqosLevel2InstanceName
        - EgressHqosLevel3ProfileName (str): optional regex of egressHqosLevel3ProfileName
        - EgressHqosLevel4ProfileName (str): optional regex of egressHqosLevel4ProfileName
        - EgressPriority (str): optional regex of egressPriority
        - EgressUPGroupName (str): optional regex of egressUPGroupName
        - EnableIfDescTLV (str): optional regex of enableIfDescTLV
        - EnableMSS (str): optional regex of enableMSS
        - GatewayAddress (str): optional regex of gatewayAddress
        - GatewayPrefixLength (str): optional regex of gatewayPrefixLength
        - HqosBwModifyMethod (str): optional regex of hqosBwModifyMethod
        - IncludeUserAuthInfo (str): optional regex of includeUserAuthInfo
        - IngressHqosLevel2InstanceName (str): optional regex of ingressHqosLevel2InstanceName
        - IngressHqosLevel3ProfileName (str): optional regex of ingressHqosLevel3ProfileName
        - IngressHqosLevel4ProfileName (str): optional regex of ingressHqosLevel4ProfileName
        - IngressPriority (str): optional regex of ingressPriority
        - IngressUPGroupName (str): optional regex of ingressUPGroupName
        - Ipv4Prefix (str): optional regex of ipv4Prefix
        - Ipv4PrefixLength (str): optional regex of ipv4PrefixLength
        - Ipv4Urf (str): optional regex of ipv4Urf
        - LogicID (str): optional regex of logicID
        - McastProfilev4Name (str): optional regex of mcastProfilev4Name
        - McastProfilev6Name (str): optional regex of mcastProfilev6Name
        - Mss (str): optional regex of mss
        - Mtu (str): optional regex of mtu
        - MvipStack (str): optional regex of mvipStack
        - NatInstance (str): optional regex of natInstance
        - NextHopAddress (str): optional regex of nextHopAddress
        - NextHopPrefixLength (str): optional regex of nextHopPrefixLength
        - Pbs (str): optional regex of pbs
        - PbsEgress (str): optional regex of pbsEgress
        - PbsUnit (str): optional regex of pbsUnit
        - PbsUnitEgress (str): optional regex of pbsUnitEgress
        - Pir (str): optional regex of pir
        - PirEgress (str): optional regex of pirEgress
        - PirUnit (str): optional regex of pirUnit
        - PirUnitEgress (str): optional regex of pirUnitEgress
        - PortNumber (str): optional regex of portNumber
        - PortType (str): optional regex of portType
        - PortalForce (str): optional regex of portalForce
        - RouteType (str): optional regex of routeType
        - SlotNumber (str): optional regex of slotNumber
        - SubAccessType (str): optional regex of subAccessType
        - SubPortNumber (str): optional regex of subPortNumber
        - SubTlvs (str): optional regex of subTlvs
        - SubslotNumber (str): optional regex of subslotNumber
        - Tag (str): optional regex of tag
        - UserIPAuthorType (str): optional regex of userIPAuthorType
        - UserIPRunType (str): optional regex of userIPRunType
        - WebForce (str): optional regex of webForce
        - WebPortalProfileName (str): optional regex of webPortalProfileName

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
