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


class EgtpSgwRange(Base):
    """PCRF Range
    The EgtpSgwRange class encapsulates a required egtpSgwRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "egtpSgwRange"
    _SDM_ATT_MAP = {
        "Apn": "apn",
        "ApnAmbrd": "apnAmbrd",
        "ApnAmbru": "apnAmbru",
        "DbMbrd": "dbMbrd",
        "DbMbru": "dbMbru",
        "DbPci": "dbPci",
        "DbPl": "dbPl",
        "DbPvi": "dbPvi",
        "DbQci": "dbQci",
        "DefaultBearerLifetimeTimer": "defaultBearerLifetimeTimer",
        "EnableDefaultBearerLifetime": "enableDefaultBearerLifetime",
        "EnableNidbCreationDelay": "enableNidbCreationDelay",
        "Enabled": "enabled",
        "Ims_apn": "ims_apn",
        "Imsi": "imsi",
        "IpType": "ipType",
        "Name": "name",
        "NidbCreationDelay": "nidbCreationDelay",
        "ObjectId": "objectId",
        "PoolSize": "poolSize",
        "PoolStartIp": "poolStartIp",
        "PoolStartIpv4": "poolStartIpv4",
        "PoolStartIpv6": "poolStartIpv6",
        "TotalCount": "totalCount",
        "UserPlaneIpAddress": "userPlaneIpAddress",
        "UserPlaneIpCount": "userPlaneIpCount",
        "UserPlaneIpv4Address": "userPlaneIpv4Address",
        "UserPlaneIpv6Address": "userPlaneIpv6Address",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(EgtpSgwRange, self).__init__(parent, list_op)

    @property
    def DedicatedBearer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dedicatedbearer_f9a0d0ce2b62efc55ec60bc7a6a96c56.DedicatedBearer): An instance of the DedicatedBearer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dedicatedbearer_f9a0d0ce2b62efc55ec60bc7a6a96c56 import (
            DedicatedBearer,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DedicatedBearer", None) is not None:
                return self._properties.get("DedicatedBearer")
        return DedicatedBearer(self)

    @property
    def TrafficProfileProxiesSgw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxiessgw_b0da1e27ea5ae3e015eae8ae4d510cb3.TrafficProfileProxiesSgw): An instance of the TrafficProfileProxiesSgw class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxiessgw_b0da1e27ea5ae3e015eae8ae4d510cb3 import (
            TrafficProfileProxiesSgw,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficProfileProxiesSgw", None) is not None:
                return self._properties.get("TrafficProfileProxiesSgw")
        return TrafficProfileProxiesSgw(self)

    @property
    def Apn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Access Point Name
        """
        return self._get_attribute(self._SDM_ATT_MAP["Apn"])

    @Apn.setter
    def Apn(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Apn"], value)

    @property
    def ApnAmbrd(self):
        # type: () -> int
        """
        Returns
        -------
        - number: APN aggregated maximum bit rate for downlink. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApnAmbrd"])

    @ApnAmbrd.setter
    def ApnAmbrd(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApnAmbrd"], value)

    @property
    def ApnAmbru(self):
        # type: () -> int
        """
        Returns
        -------
        - number: APN aggregated maximum bit rate for uplink.For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApnAmbru"])

    @ApnAmbru.setter
    def ApnAmbru(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApnAmbru"], value)

    @property
    def DbMbrd(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DbMbrd"])

    @DbMbrd.setter
    def DbMbrd(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DbMbrd"], value)

    @property
    def DbMbru(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DbMbru"])

    @DbMbru.setter
    def DbMbru(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DbMbru"], value)

    @property
    def DbPci(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ARP Preemption Capability
        """
        return self._get_attribute(self._SDM_ATT_MAP["DbPci"])

    @DbPci.setter
    def DbPci(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DbPci"], value)

    @property
    def DbPl(self):
        # type: () -> int
        """
        Returns
        -------
        - number: ARP Priority Level
        """
        return self._get_attribute(self._SDM_ATT_MAP["DbPl"])

    @DbPl.setter
    def DbPl(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DbPl"], value)

    @property
    def DbPvi(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ARP Preemption Vulnerability
        """
        return self._get_attribute(self._SDM_ATT_MAP["DbPvi"])

    @DbPvi.setter
    def DbPvi(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DbPvi"], value)

    @property
    def DbQci(self):
        # type: () -> int
        """
        Returns
        -------
        - number: QoS Class Identifier
        """
        return self._get_attribute(self._SDM_ATT_MAP["DbQci"])

    @DbQci.setter
    def DbQci(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DbQci"], value)

    @property
    def DefaultBearerLifetimeTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time, in seconds, after which the default bearer is deleted
        """
        return self._get_attribute(self._SDM_ATT_MAP["DefaultBearerLifetimeTimer"])

    @DefaultBearerLifetimeTimer.setter
    def DefaultBearerLifetimeTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DefaultBearerLifetimeTimer"], value)

    @property
    def EnableDefaultBearerLifetime(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled the default bearer will be deleted using the PGW initiated bearer deactivation procedure
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDefaultBearerLifetime"])

    @EnableDefaultBearerLifetime.setter
    def EnableDefaultBearerLifetime(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDefaultBearerLifetime"], value)

    @property
    def EnableNidbCreationDelay(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Delay Network Initiated Dedicated Bearer(NIDB) Creation
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableNidbCreationDelay"])

    @EnableNidbCreationDelay.setter
    def EnableNidbCreationDelay(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableNidbCreationDelay"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def Ims_apn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IMS APN
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ims_apn"])

    @Ims_apn.setter
    def Ims_apn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ims_apn"], value)

    @property
    def Imsi(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first International Mobile Subscriber Identifier that will be accepted.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Imsi"])

    @Imsi.setter
    def Imsi(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Imsi"], value)

    @property
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP type of the address(es) that will be assigned to the UEs. When choosing IPv4v6 both an IPv4 address and an IPv6 address will be assigned to the UE.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpType"])

    @IpType.setter
    def IpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpType"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NidbCreationDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Time to wait (in seconds), from the moment the UE is attached, before sending Create Bearer Request for Network Initiated Dedicated Bearers(NIDB). This does not apply to MS Initiated Dedicated Bearers
        """
        return self._get_attribute(self._SDM_ATT_MAP["NidbCreationDelay"])

    @NidbCreationDelay.setter
    def NidbCreationDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NidbCreationDelay"], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    @property
    def PoolSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of UEs that will be accepted.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PoolSize"])

    @PoolSize.setter
    def PoolSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PoolSize"], value)

    @property
    def PoolStartIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Obsolete - use poolStartIPv4 or poolStartIPv6
        """
        return self._get_attribute(self._SDM_ATT_MAP["PoolStartIp"])

    @PoolStartIp.setter
    def PoolStartIp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PoolStartIp"], value)

    @property
    def PoolStartIpv4(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first IPv4 address to be assigned to an UE.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PoolStartIpv4"])

    @PoolStartIpv4.setter
    def PoolStartIpv4(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PoolStartIpv4"], value)

    @property
    def PoolStartIpv6(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first IPv6 address to be assigned to an UE.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PoolStartIpv6"])

    @PoolStartIpv6.setter
    def PoolStartIpv6(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PoolStartIpv6"], value)

    @property
    def TotalCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Layer 7 Server Count On All Ports
        """
        return self._get_attribute(self._SDM_ATT_MAP["TotalCount"])

    @TotalCount.setter
    def TotalCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TotalCount"], value)

    @property
    def UserPlaneIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Obsolete - use userPlaneIPv4Address or userPlaneIPv6Address
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserPlaneIpAddress"])

    @UserPlaneIpAddress.setter
    def UserPlaneIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserPlaneIpAddress"], value)

    @property
    def UserPlaneIpCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Layer 7 Server Count Per Port
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserPlaneIpCount"])

    @UserPlaneIpCount.setter
    def UserPlaneIpCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserPlaneIpCount"], value)

    @property
    def UserPlaneIpv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first IPv4 address to be used by the L4-7 server activies.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserPlaneIpv4Address"])

    @UserPlaneIpv4Address.setter
    def UserPlaneIpv4Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserPlaneIpv4Address"], value)

    @property
    def UserPlaneIpv6Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first IPv6 address to be used by the L4-7 server activies.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserPlaneIpv6Address"])

    @UserPlaneIpv6Address.setter
    def UserPlaneIpv6Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserPlaneIpv6Address"], value)

    def update(
        self,
        Apn=None,
        ApnAmbrd=None,
        ApnAmbru=None,
        DbMbrd=None,
        DbMbru=None,
        DbPci=None,
        DbPl=None,
        DbPvi=None,
        DbQci=None,
        DefaultBearerLifetimeTimer=None,
        EnableDefaultBearerLifetime=None,
        EnableNidbCreationDelay=None,
        Enabled=None,
        Ims_apn=None,
        Imsi=None,
        IpType=None,
        Name=None,
        NidbCreationDelay=None,
        PoolSize=None,
        PoolStartIp=None,
        PoolStartIpv4=None,
        PoolStartIpv6=None,
        TotalCount=None,
        UserPlaneIpAddress=None,
        UserPlaneIpCount=None,
        UserPlaneIpv4Address=None,
        UserPlaneIpv6Address=None,
    ):
        # type: (str, int, int, int, int, bool, int, bool, int, int, bool, bool, bool, bool, str, str, str, int, int, str, str, str, int, str, int, str, str) -> EgtpSgwRange
        """Updates egtpSgwRange resource on the server.

        Args
        ----
        - Apn (str): Access Point Name
        - ApnAmbrd (number): APN aggregated maximum bit rate for downlink. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - ApnAmbru (number): APN aggregated maximum bit rate for uplink.For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - DbMbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - DbMbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - DbPci (bool): ARP Preemption Capability
        - DbPl (number): ARP Priority Level
        - DbPvi (bool): ARP Preemption Vulnerability
        - DbQci (number): QoS Class Identifier
        - DefaultBearerLifetimeTimer (number): The time, in seconds, after which the default bearer is deleted
        - EnableDefaultBearerLifetime (bool): If enabled the default bearer will be deleted using the PGW initiated bearer deactivation procedure
        - EnableNidbCreationDelay (bool): Delay Network Initiated Dedicated Bearer(NIDB) Creation
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Ims_apn (bool): IMS APN
        - Imsi (str): The first International Mobile Subscriber Identifier that will be accepted.
        - IpType (str): The IP type of the address(es) that will be assigned to the UEs. When choosing IPv4v6 both an IPv4 address and an IPv6 address will be assigned to the UE.
        - Name (str): Name of range
        - NidbCreationDelay (number): Time to wait (in seconds), from the moment the UE is attached, before sending Create Bearer Request for Network Initiated Dedicated Bearers(NIDB). This does not apply to MS Initiated Dedicated Bearers
        - PoolSize (number): The number of UEs that will be accepted.
        - PoolStartIp (str): Obsolete - use poolStartIPv4 or poolStartIPv6
        - PoolStartIpv4 (str): The first IPv4 address to be assigned to an UE.
        - PoolStartIpv6 (str): The first IPv6 address to be assigned to an UE.
        - TotalCount (number): Layer 7 Server Count On All Ports
        - UserPlaneIpAddress (str): Obsolete - use userPlaneIPv4Address or userPlaneIPv6Address
        - UserPlaneIpCount (number): Layer 7 Server Count Per Port
        - UserPlaneIpv4Address (str): The first IPv4 address to be used by the L4-7 server activies.
        - UserPlaneIpv6Address (str): The first IPv6 address to be used by the L4-7 server activies.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Apn=None,
        ApnAmbrd=None,
        ApnAmbru=None,
        DbMbrd=None,
        DbMbru=None,
        DbPci=None,
        DbPl=None,
        DbPvi=None,
        DbQci=None,
        DefaultBearerLifetimeTimer=None,
        EnableDefaultBearerLifetime=None,
        EnableNidbCreationDelay=None,
        Enabled=None,
        Ims_apn=None,
        Imsi=None,
        IpType=None,
        Name=None,
        NidbCreationDelay=None,
        ObjectId=None,
        PoolSize=None,
        PoolStartIp=None,
        PoolStartIpv4=None,
        PoolStartIpv6=None,
        TotalCount=None,
        UserPlaneIpAddress=None,
        UserPlaneIpCount=None,
        UserPlaneIpv4Address=None,
        UserPlaneIpv6Address=None,
    ):
        # type: (str, int, int, int, int, bool, int, bool, int, int, bool, bool, bool, bool, str, str, str, int, str, int, str, str, str, int, str, int, str, str) -> EgtpSgwRange
        """Finds and retrieves egtpSgwRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve egtpSgwRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all egtpSgwRange resources from the server.

        Args
        ----
        - Apn (str): Access Point Name
        - ApnAmbrd (number): APN aggregated maximum bit rate for downlink. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - ApnAmbru (number): APN aggregated maximum bit rate for uplink.For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - DbMbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - DbMbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - DbPci (bool): ARP Preemption Capability
        - DbPl (number): ARP Priority Level
        - DbPvi (bool): ARP Preemption Vulnerability
        - DbQci (number): QoS Class Identifier
        - DefaultBearerLifetimeTimer (number): The time, in seconds, after which the default bearer is deleted
        - EnableDefaultBearerLifetime (bool): If enabled the default bearer will be deleted using the PGW initiated bearer deactivation procedure
        - EnableNidbCreationDelay (bool): Delay Network Initiated Dedicated Bearer(NIDB) Creation
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Ims_apn (bool): IMS APN
        - Imsi (str): The first International Mobile Subscriber Identifier that will be accepted.
        - IpType (str): The IP type of the address(es) that will be assigned to the UEs. When choosing IPv4v6 both an IPv4 address and an IPv6 address will be assigned to the UE.
        - Name (str): Name of range
        - NidbCreationDelay (number): Time to wait (in seconds), from the moment the UE is attached, before sending Create Bearer Request for Network Initiated Dedicated Bearers(NIDB). This does not apply to MS Initiated Dedicated Bearers
        - ObjectId (str): Unique identifier for this object
        - PoolSize (number): The number of UEs that will be accepted.
        - PoolStartIp (str): Obsolete - use poolStartIPv4 or poolStartIPv6
        - PoolStartIpv4 (str): The first IPv4 address to be assigned to an UE.
        - PoolStartIpv6 (str): The first IPv6 address to be assigned to an UE.
        - TotalCount (number): Layer 7 Server Count On All Ports
        - UserPlaneIpAddress (str): Obsolete - use userPlaneIPv4Address or userPlaneIPv6Address
        - UserPlaneIpCount (number): Layer 7 Server Count Per Port
        - UserPlaneIpv4Address (str): The first IPv4 address to be used by the L4-7 server activies.
        - UserPlaneIpv6Address (str): The first IPv6 address to be used by the L4-7 server activies.

        Returns
        -------
        - self: This instance with matching egtpSgwRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of egtpSgwRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the egtpSgwRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "customProtocolStack", payload=payload, response_object=None
        )

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

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
        return self._execute(
            "disableProtocolStack", payload=payload, response_object=None
        )

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

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
        return self._execute(
            "enableProtocolStack", payload=payload, response_object=None
        )
