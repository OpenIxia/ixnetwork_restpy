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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class DhcpUsersList(Base):
    """DHCP Subscribers.
    The DhcpUsersList class encapsulates a required dhcpUsersList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "dhcpUsersList"
    _SDM_ATT_MAP = {
        "AccessType": "accessType",
        "AccountType": "accountType",
        "Active": "active",
        "AdvertiseFlag": "advertiseFlag",
        "AutoPopulateIanaAddress": "autoPopulateIanaAddress",
        "AutoPopulateIanaNhAddress": "autoPopulateIanaNhAddress",
        "AutoPopulateIanaNhWithLlPrefix": "autoPopulateIanaNhWithLlPrefix",
        "AutoPopulateIanaPrefix": "autoPopulateIanaPrefix",
        "AutoPopulateNdAddress": "autoPopulateNdAddress",
        "AutoPopulateNdNhAddress": "autoPopulateNdNhAddress",
        "AutoPopulateNdNhWithLlPrefix": "autoPopulateNdNhWithLlPrefix",
        "AutoPopulateNdPrefix": "autoPopulateNdPrefix",
        "AutoPopulatePdAddress": "autoPopulatePdAddress",
        "AutoPopulatePdNhAddress": "autoPopulatePdNhAddress",
        "AutoPopulatePdNhWithLlPrefix": "autoPopulatePdNhWithLlPrefix",
        "AutoPopulatePdPrefix": "autoPopulatePdPrefix",
        "Cbs": "cbs",
        "CbsEgress": "cbsEgress",
        "CbsUnit": "cbsUnit",
        "CbsUnitEgress": "cbsUnitEgress",
        "ChassisNumber": "chassisNumber",
        "Cir": "cir",
        "CirEgress": "cirEgress",
        "CirUnit": "cirUnit",
        "CirUnitEgress": "cirUnitEgress",
        "Cost": "cost",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "DetectInterval": "detectInterval",
        "DetectTimes": "detectTimes",
        "EchoEnable": "echoEnable",
        "EgressHqosLevel2InstanceName": "egressHqosLevel2InstanceName",
        "EgressHqosLevel3ProfileName": "egressHqosLevel3ProfileName",
        "EgressHqosLevel4ProfileName": "egressHqosLevel4ProfileName",
        "EgressPriority": "egressPriority",
        "EgressUPGroupName": "egressUPGroupName",
        "EnableIfDescTLV": "enableIfDescTLV",
        "EnableMSS": "enableMSS",
        "GatewayAddress": "gatewayAddress",
        "GatewayPrefixLength": "gatewayPrefixLength",
        "HqosBwModifyMethod": "hqosBwModifyMethod",
        "IanaAddress": "ianaAddress",
        "IanaAddressPrefixLength": "ianaAddressPrefixLength",
        "IanaDestAddress": "ianaDestAddress",
        "IanaDestAddressPrefixLength": "ianaDestAddressPrefixLength",
        "IanaNhAddress": "ianaNhAddress",
        "IanaNhAddressPrefixLength": "ianaNhAddressPrefixLength",
        "IncludeUserAuthInfo": "includeUserAuthInfo",
        "IngressHqosLevel2InstanceName": "ingressHqosLevel2InstanceName",
        "IngressHqosLevel3ProfileName": "ingressHqosLevel3ProfileName",
        "IngressHqosLevel4ProfileName": "ingressHqosLevel4ProfileName",
        "IngressPriority": "ingressPriority",
        "IngressUPGroupName": "ingressUPGroupName",
        "Ipv4DestAddress": "ipv4DestAddress",
        "Ipv4DestAddressPrefixLength": "ipv4DestAddressPrefixLength",
        "Ipv4Prefix": "ipv4Prefix",
        "Ipv4PrefixLength": "ipv4PrefixLength",
        "Ipv4Urf": "ipv4Urf",
        "LogicID": "logicID",
        "MapSubscribersToUpPort": "mapSubscribersToUpPort",
        "McastProfilev4Name": "mcastProfilev4Name",
        "McastProfilev6Name": "mcastProfilev6Name",
        "Mss": "mss",
        "Mtu": "mtu",
        "MvipStack": "mvipStack",
        "Name": "name",
        "NatInstance": "natInstance",
        "NdAddress": "ndAddress",
        "NdAddressPrefixLength": "ndAddressPrefixLength",
        "NdDestAddress": "ndDestAddress",
        "NdDestAddressPrefixLength": "ndDestAddressPrefixLength",
        "NdNhAddress": "ndNhAddress",
        "NdNhAddressPrefixLength": "ndNhAddressPrefixLength",
        "NextHopAddress": "nextHopAddress",
        "NextHopPrefixLength": "nextHopPrefixLength",
        "Pbs": "pbs",
        "PbsEgress": "pbsEgress",
        "PbsUnit": "pbsUnit",
        "PbsUnitEgress": "pbsUnitEgress",
        "PdAddress": "pdAddress",
        "PdAddressPrefixLength": "pdAddressPrefixLength",
        "PdDestAddress": "pdDestAddress",
        "PdDestAddressPrefixLength": "pdDestAddressPrefixLength",
        "PdNhAddress": "pdNhAddress",
        "PdNhAddressPrefixLength": "pdNhAddressPrefixLength",
        "Pir": "pir",
        "PirEgress": "pirEgress",
        "PirUnit": "pirUnit",
        "PirUnitEgress": "pirUnitEgress",
        "PortNumber": "portNumber",
        "PortType": "portType",
        "PortalForce": "portalForce",
        "RouteType": "routeType",
        "SlotNumber": "slotNumber",
        "SubAccessType": "subAccessType",
        "SubPortNumber": "subPortNumber",
        "SubTlvs": "subTlvs",
        "SubscriberGrouping": "subscriberGrouping",
        "SubslotNumber": "subslotNumber",
        "Tag": "tag",
        "UserIPAuthorType": "userIPAuthorType",
        "UserIPRunType": "userIPRunType",
        "WebForce": "webForce",
        "WebPortalProfileName": "webPortalProfileName",
    }
    _SDM_ENUM_MAP = {
        "subscriberGrouping": ["countBased", "subnetBased"],
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

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AccessType"]))

    @property
    def AccountType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Account Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AccountType"]))

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AdvertiseFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseFlag"]))

    @property
    def AutoPopulateIanaAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Populate IANA Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoPopulateIanaAddress"])
        )

    @property
    def AutoPopulateIanaNhAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Populate IANA Next Hop Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoPopulateIanaNhAddress"])
        )

    @property
    def AutoPopulateIanaNhWithLlPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Populate IANA Next Hop with LL Prefix.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AutoPopulateIanaNhWithLlPrefix"]),
        )

    @property
    def AutoPopulateIanaPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Populate IANA Prefix.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoPopulateIanaPrefix"])
        )

    @property
    def AutoPopulateNdAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Populate ND Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoPopulateNdAddress"])
        )

    @property
    def AutoPopulateNdNhAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Populate ND Next Hop Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoPopulateNdNhAddress"])
        )

    @property
    def AutoPopulateNdNhWithLlPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Populate ND Next Hop with LL Prefix.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoPopulateNdNhWithLlPrefix"])
        )

    @property
    def AutoPopulateNdPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Populate ND Prefix.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoPopulateNdPrefix"])
        )

    @property
    def AutoPopulatePdAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Populate PD Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoPopulatePdAddress"])
        )

    @property
    def AutoPopulatePdNhAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Populate PD Next Hop Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoPopulatePdNhAddress"])
        )

    @property
    def AutoPopulatePdNhWithLlPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Populate PD Next Hop with LL Prefix.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoPopulatePdNhWithLlPrefix"])
        )

    @property
    def AutoPopulatePdPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Populate PD Prefix.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoPopulatePdPrefix"])
        )

    @property
    def Cbs(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The token bucket in bytes.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Cbs"]))

    @property
    def CbsEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The token bucket in bytes.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CbsEgress"]))

    @property
    def CbsUnit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Guaranteed Token Bucket Unit.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CbsUnit"]))

    @property
    def CbsUnitEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Guaranteed Token Bucket Unit.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CbsUnitEgress"]))

    @property
    def ChassisNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Chassis number.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ChassisNumber"]))

    @property
    def Cir(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Committed Information Rate.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Cir"]))

    @property
    def CirEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Committed Information Rate.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CirEgress"]))

    @property
    def CirUnit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Guaranteed rate units.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CirUnit"]))

    @property
    def CirUnitEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Guaranteed rate units.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CirUnitEgress"]))

    @property
    def Cost(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Cost
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Cost"]))

    @property
    def Count(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Subscriber Count in a Group.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Count"]))

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def DetectInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The time interval UP waits for a subscriber to respond to a detection probe.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DetectInterval"])
        )

    @property
    def DetectTimes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of detection timeouts after which the subscriber session is deleted. 0 means no detection is performed.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DetectTimes"]))

    @property
    def EchoEnable(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Both PPP/ARP are compatible, and the microcode will quickly return to ARP Req or PPP Echo. 0: off, 1: on.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EchoEnable"]))

    @property
    def EgressHqosLevel2InstanceName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Egress HQoS Level 2 Instance Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressHqosLevel2InstanceName"])
        )

    @property
    def EgressHqosLevel3ProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Egress HQoS Level 3 Profile Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressHqosLevel3ProfileName"])
        )

    @property
    def EgressHqosLevel4ProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Egress HQoS Level 4 Profile Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressHqosLevel4ProfileName"])
        )

    @property
    def EgressPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Downward direction priority.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressPriority"])
        )

    @property
    def EgressUPGroupName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Egress-User-Policy-Group Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressUPGroupName"])
        )

    @property
    def EnableIfDescTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable IF DESC TLV. It will advertise back the IF DESC advertised by UP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableIfDescTLV"])
        )

    @property
    def EnableMSS(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MSS
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableMSS"]))

    @property
    def GatewayAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Gateway Address of the subscriber.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GatewayAddress"])
        )

    @property
    def GatewayPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Gateway Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GatewayPrefixLength"])
        )

    @property
    def HqosBwModifyMethod(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): HQoS Bandwidth Modiy Method.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HqosBwModifyMethod"])
        )

    @property
    def IanaAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IANA Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IanaAddress"]))

    @property
    def IanaAddressPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IANA Address Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IanaAddressPrefixLength"])
        )

    @property
    def IanaDestAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IANA Destination Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IanaDestAddress"])
        )

    @property
    def IanaDestAddressPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IANA Destination Address Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IanaDestAddressPrefixLength"])
        )

    @property
    def IanaNhAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IANA Next Hop Address to be used to reach the destination.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IanaNhAddress"]))

    @property
    def IanaNhAddressPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IANA Next Hop Address Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IanaNhAddressPrefixLength"])
        )

    @property
    def IncludeUserAuthInfo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include User Auth Info.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeUserAuthInfo"])
        )

    @property
    def IngressHqosLevel2InstanceName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ingress HQoS Level 2 Instance Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IngressHqosLevel2InstanceName"]),
        )

    @property
    def IngressHqosLevel3ProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ingress HQoS Level 3 Profile Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IngressHqosLevel3ProfileName"])
        )

    @property
    def IngressHqosLevel4ProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ingress HQoS Level 4 Profile Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IngressHqosLevel4ProfileName"])
        )

    @property
    def IngressPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Upward direction priority.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IngressPriority"])
        )

    @property
    def IngressUPGroupName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ingress-User-Policy-Group Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IngressUPGroupName"])
        )

    @property
    def Ipv4DestAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Destination Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4DestAddress"])
        )

    @property
    def Ipv4DestAddressPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Destination Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4DestAddressPrefixLength"])
        )

    @property
    def Ipv4Prefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 prefix of the user.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv4Prefix"]))

    @property
    def Ipv4PrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4PrefixLength"])
        )

    @property
    def Ipv4Urf(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Unicast Reverse Path Forwarding (URPF) flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv4Urf"]))

    @property
    def LogicID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Virtual port number.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LogicID"]))

    @property
    def MapSubscribersToUpPort(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Map Subscribers to UP port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapSubscribersToUpPort"])

    @MapSubscribersToUpPort.setter
    def MapSubscribersToUpPort(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapSubscribersToUpPort"], value)

    @property
    def McastProfilev4Name(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Profilev4 Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["McastProfilev4Name"])
        )

    @property
    def McastProfilev6Name(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Profilev6 Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["McastProfilev6Name"])
        )

    @property
    def Mss(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MSS Value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mss"]))

    @property
    def Mtu(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MTU
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mtu"]))

    @property
    def MvipStack(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This drop box is provided to select ipv4 or ipv6 or dual stack subscribers.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MvipStack"]))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NatInstance(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Nat Instance Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NatInstance"]))

    @property
    def NdAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ND Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NdAddress"]))

    @property
    def NdAddressPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ND Address Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NdAddressPrefixLength"])
        )

    @property
    def NdDestAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ND Destination Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NdDestAddress"]))

    @property
    def NdDestAddressPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ND Destination Address Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NdDestAddressPrefixLength"])
        )

    @property
    def NdNhAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ND Next Hop Address to be used to reach the destination.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NdNhAddress"]))

    @property
    def NdNhAddressPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ND Next Hop Address Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NdNhAddressPrefixLength"])
        )

    @property
    def NextHopAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Next hop address to be used by the UP to reach the Destination address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextHopAddress"])
        )

    @property
    def NextHopPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Next Hop Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextHopPrefixLength"])
        )

    @property
    def Pbs(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst token buckets in bytes.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Pbs"]))

    @property
    def PbsEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst token buckets in bytes.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PbsEgress"]))

    @property
    def PbsUnit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst Token Bucket Unit.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PbsUnit"]))

    @property
    def PbsUnitEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst Token Bucket Unit.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PbsUnitEgress"]))

    @property
    def PdAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PD Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PdAddress"]))

    @property
    def PdAddressPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PD Address Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PdAddressPrefixLength"])
        )

    @property
    def PdDestAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PD Destination Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PdDestAddress"]))

    @property
    def PdDestAddressPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PD Destination Address Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PdDestAddressPrefixLength"])
        )

    @property
    def PdNhAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PD Next Hop Address to be used to reach the destination.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PdNhAddress"]))

    @property
    def PdNhAddressPrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PD Next Hop Address Prefix Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PdNhAddressPrefixLength"])
        )

    @property
    def Pir(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peak Information Rate.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Pir"]))

    @property
    def PirEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peak Information Rate.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PirEgress"]))

    @property
    def PirUnit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst rate units.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PirUnit"]))

    @property
    def PirUnitEgress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Burst rate units.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PirUnitEgress"]))

    @property
    def PortNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Physical port number.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PortNumber"]))

    @property
    def PortType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The type of the Port.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PortType"]))

    @property
    def PortalForce(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Push advertising switch, 0: off, 1: on.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PortalForce"]))

    @property
    def RouteType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RouteType"]))

    @property
    def SlotNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Interface index.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SlotNumber"]))

    @property
    def SubAccessType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub Access Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SubAccessType"]))

    @property
    def SubPortNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub port number.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SubPortNumber"]))

    @property
    def SubTlvs(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub TLVs.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SubTlvs"]))

    @property
    def SubscriberGrouping(self):
        # type: () -> str
        """
        Returns
        -------
        - str(countBased | subnetBased): Basis of subscriber grouping.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SubscriberGrouping"])

    @SubscriberGrouping.setter
    def SubscriberGrouping(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SubscriberGrouping"], value)

    @property
    def SubslotNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Interface index.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SubslotNumber"]))

    @property
    def Tag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tag"]))

    @property
    def UserIPAuthorType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User IP Author Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserIPAuthorType"])
        )

    @property
    def UserIPRunType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User IP Run Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UserIPRunType"]))

    @property
    def WebForce(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 WebForce push flag, 0: off, 1: on.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["WebForce"]))

    @property
    def WebPortalProfileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Web Portal Profile Name.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["WebPortalProfileName"])
        )

    def update(self, MapSubscribersToUpPort=None, Name=None, SubscriberGrouping=None):
        # type: (bool, str, str) -> DhcpUsersList
        """Updates dhcpUsersList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - MapSubscribersToUpPort (bool): Map Subscribers to UP port.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SubscriberGrouping (str(countBased | subnetBased)): Basis of subscriber grouping.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        DescriptiveName=None,
        MapSubscribersToUpPort=None,
        Name=None,
        SubscriberGrouping=None,
    ):
        # type: (str, bool, str, str) -> DhcpUsersList
        """Finds and retrieves dhcpUsersList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpUsersList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpUsersList resources from the server.

        Args
        ----
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - MapSubscribersToUpPort (bool): Map Subscribers to UP port.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SubscriberGrouping (str(countBased | subnetBased)): Basis of subscriber grouping.

        Returns
        -------
        - self: This instance with matching dhcpUsersList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpUsersList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpUsersList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        AccessType=None,
        AccountType=None,
        Active=None,
        AdvertiseFlag=None,
        AutoPopulateIanaAddress=None,
        AutoPopulateIanaNhAddress=None,
        AutoPopulateIanaNhWithLlPrefix=None,
        AutoPopulateIanaPrefix=None,
        AutoPopulateNdAddress=None,
        AutoPopulateNdNhAddress=None,
        AutoPopulateNdNhWithLlPrefix=None,
        AutoPopulateNdPrefix=None,
        AutoPopulatePdAddress=None,
        AutoPopulatePdNhAddress=None,
        AutoPopulatePdNhWithLlPrefix=None,
        AutoPopulatePdPrefix=None,
        Cbs=None,
        CbsEgress=None,
        CbsUnit=None,
        CbsUnitEgress=None,
        ChassisNumber=None,
        Cir=None,
        CirEgress=None,
        CirUnit=None,
        CirUnitEgress=None,
        Cost=None,
        Count=None,
        DetectInterval=None,
        DetectTimes=None,
        EchoEnable=None,
        EgressHqosLevel2InstanceName=None,
        EgressHqosLevel3ProfileName=None,
        EgressHqosLevel4ProfileName=None,
        EgressPriority=None,
        EgressUPGroupName=None,
        EnableIfDescTLV=None,
        EnableMSS=None,
        GatewayAddress=None,
        GatewayPrefixLength=None,
        HqosBwModifyMethod=None,
        IanaAddress=None,
        IanaAddressPrefixLength=None,
        IanaDestAddress=None,
        IanaDestAddressPrefixLength=None,
        IanaNhAddress=None,
        IanaNhAddressPrefixLength=None,
        IncludeUserAuthInfo=None,
        IngressHqosLevel2InstanceName=None,
        IngressHqosLevel3ProfileName=None,
        IngressHqosLevel4ProfileName=None,
        IngressPriority=None,
        IngressUPGroupName=None,
        Ipv4DestAddress=None,
        Ipv4DestAddressPrefixLength=None,
        Ipv4Prefix=None,
        Ipv4PrefixLength=None,
        Ipv4Urf=None,
        LogicID=None,
        McastProfilev4Name=None,
        McastProfilev6Name=None,
        Mss=None,
        Mtu=None,
        MvipStack=None,
        NatInstance=None,
        NdAddress=None,
        NdAddressPrefixLength=None,
        NdDestAddress=None,
        NdDestAddressPrefixLength=None,
        NdNhAddress=None,
        NdNhAddressPrefixLength=None,
        NextHopAddress=None,
        NextHopPrefixLength=None,
        Pbs=None,
        PbsEgress=None,
        PbsUnit=None,
        PbsUnitEgress=None,
        PdAddress=None,
        PdAddressPrefixLength=None,
        PdDestAddress=None,
        PdDestAddressPrefixLength=None,
        PdNhAddress=None,
        PdNhAddressPrefixLength=None,
        Pir=None,
        PirEgress=None,
        PirUnit=None,
        PirUnitEgress=None,
        PortNumber=None,
        PortType=None,
        PortalForce=None,
        RouteType=None,
        SlotNumber=None,
        SubAccessType=None,
        SubPortNumber=None,
        SubTlvs=None,
        SubslotNumber=None,
        Tag=None,
        UserIPAuthorType=None,
        UserIPRunType=None,
        WebForce=None,
        WebPortalProfileName=None,
    ):
        """Base class infrastructure that gets a list of dhcpUsersList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AccessType (str): optional regex of accessType
        - AccountType (str): optional regex of accountType
        - Active (str): optional regex of active
        - AdvertiseFlag (str): optional regex of advertiseFlag
        - AutoPopulateIanaAddress (str): optional regex of autoPopulateIanaAddress
        - AutoPopulateIanaNhAddress (str): optional regex of autoPopulateIanaNhAddress
        - AutoPopulateIanaNhWithLlPrefix (str): optional regex of autoPopulateIanaNhWithLlPrefix
        - AutoPopulateIanaPrefix (str): optional regex of autoPopulateIanaPrefix
        - AutoPopulateNdAddress (str): optional regex of autoPopulateNdAddress
        - AutoPopulateNdNhAddress (str): optional regex of autoPopulateNdNhAddress
        - AutoPopulateNdNhWithLlPrefix (str): optional regex of autoPopulateNdNhWithLlPrefix
        - AutoPopulateNdPrefix (str): optional regex of autoPopulateNdPrefix
        - AutoPopulatePdAddress (str): optional regex of autoPopulatePdAddress
        - AutoPopulatePdNhAddress (str): optional regex of autoPopulatePdNhAddress
        - AutoPopulatePdNhWithLlPrefix (str): optional regex of autoPopulatePdNhWithLlPrefix
        - AutoPopulatePdPrefix (str): optional regex of autoPopulatePdPrefix
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
        - IanaAddress (str): optional regex of ianaAddress
        - IanaAddressPrefixLength (str): optional regex of ianaAddressPrefixLength
        - IanaDestAddress (str): optional regex of ianaDestAddress
        - IanaDestAddressPrefixLength (str): optional regex of ianaDestAddressPrefixLength
        - IanaNhAddress (str): optional regex of ianaNhAddress
        - IanaNhAddressPrefixLength (str): optional regex of ianaNhAddressPrefixLength
        - IncludeUserAuthInfo (str): optional regex of includeUserAuthInfo
        - IngressHqosLevel2InstanceName (str): optional regex of ingressHqosLevel2InstanceName
        - IngressHqosLevel3ProfileName (str): optional regex of ingressHqosLevel3ProfileName
        - IngressHqosLevel4ProfileName (str): optional regex of ingressHqosLevel4ProfileName
        - IngressPriority (str): optional regex of ingressPriority
        - IngressUPGroupName (str): optional regex of ingressUPGroupName
        - Ipv4DestAddress (str): optional regex of ipv4DestAddress
        - Ipv4DestAddressPrefixLength (str): optional regex of ipv4DestAddressPrefixLength
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
        - NdAddress (str): optional regex of ndAddress
        - NdAddressPrefixLength (str): optional regex of ndAddressPrefixLength
        - NdDestAddress (str): optional regex of ndDestAddress
        - NdDestAddressPrefixLength (str): optional regex of ndDestAddressPrefixLength
        - NdNhAddress (str): optional regex of ndNhAddress
        - NdNhAddressPrefixLength (str): optional regex of ndNhAddressPrefixLength
        - NextHopAddress (str): optional regex of nextHopAddress
        - NextHopPrefixLength (str): optional regex of nextHopPrefixLength
        - Pbs (str): optional regex of pbs
        - PbsEgress (str): optional regex of pbsEgress
        - PbsUnit (str): optional regex of pbsUnit
        - PbsUnitEgress (str): optional regex of pbsUnitEgress
        - PdAddress (str): optional regex of pdAddress
        - PdAddressPrefixLength (str): optional regex of pdAddressPrefixLength
        - PdDestAddress (str): optional regex of pdDestAddress
        - PdDestAddressPrefixLength (str): optional regex of pdDestAddressPrefixLength
        - PdNhAddress (str): optional regex of pdNhAddress
        - PdNhAddressPrefixLength (str): optional regex of pdNhAddressPrefixLength
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
