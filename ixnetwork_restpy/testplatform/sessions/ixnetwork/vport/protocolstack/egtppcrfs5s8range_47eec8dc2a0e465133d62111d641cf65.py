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


class EgtpPcrfS5S8Range(Base):
    """PCRF Range
    The EgtpPcrfS5S8Range class encapsulates a required egtpPcrfS5S8Range resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "egtpPcrfS5S8Range"
    _SDM_ATT_MAP = {
        "Apn": "apn",
        "Apn_AMBRD": "apn_AMBRD",
        "Apn_AMBRU": "apn_AMBRU",
        "Db_gbrd": "db_gbrd",
        "Db_gbru": "db_gbru",
        "Db_mbrd": "db_mbrd",
        "Db_mbru": "db_mbru",
        "Db_pci": "db_pci",
        "Db_pl": "db_pl",
        "Db_pvi": "db_pvi",
        "Db_qci": "db_qci",
        "DefaultBearerLifetimeTimer": "defaultBearerLifetimeTimer",
        "EnableDefaultBearerLifetime": "enableDefaultBearerLifetime",
        "EnableNIDBCreationDelay": "enableNIDBCreationDelay",
        "Enabled": "enabled",
        "IMSI": "iMSI",
        "Ims_apn": "ims_apn",
        "IpType": "ipType",
        "Name": "name",
        "NidbCreationDelay": "nidbCreationDelay",
        "ObjectId": "objectId",
        "ParentPgw": "parentPgw",
        "PoolSize": "poolSize",
        "PoolStartIPv4": "poolStartIPv4",
        "PoolStartIPv6": "poolStartIPv6",
        "PoolStartIp": "poolStartIp",
        "RoundRobinDistribution": "roundRobinDistribution",
        "TotalCount": "totalCount",
        "UserPlaneIPv4Address": "userPlaneIPv4Address",
        "UserPlaneIPv6Address": "userPlaneIPv6Address",
        "UserPlaneIpAddress": "userPlaneIpAddress",
        "UserPlaneIpCount": "userPlaneIpCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(EgtpPcrfS5S8Range, self).__init__(parent, list_op)

    @property
    def DedicatedBearersS5S8Pgw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dedicatedbearerss5s8pgw_5b6e9922b532dbc7fb4073e8b42f3ff7.DedicatedBearersS5S8Pgw): An instance of the DedicatedBearersS5S8Pgw class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dedicatedbearerss5s8pgw_5b6e9922b532dbc7fb4073e8b42f3ff7 import (
            DedicatedBearersS5S8Pgw,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DedicatedBearersS5S8Pgw", None) is not None:
                return self._properties.get("DedicatedBearersS5S8Pgw")
        return DedicatedBearersS5S8Pgw(self)

    @property
    def TrafficProfileProxiesS5S8Pgw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxiess5s8pgw_47d0afd20663ef6a4faa05f791965f38.TrafficProfileProxiesS5S8Pgw): An instance of the TrafficProfileProxiesS5S8Pgw class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxiess5s8pgw_47d0afd20663ef6a4faa05f791965f38 import (
            TrafficProfileProxiesS5S8Pgw,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrafficProfileProxiesS5S8Pgw", None) is not None:
                return self._properties.get("TrafficProfileProxiesS5S8Pgw")
        return TrafficProfileProxiesS5S8Pgw(self)

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
    def Apn_AMBRD(self):
        # type: () -> int
        """
        Returns
        -------
        - number: APN aggregated maximum bit rate for downlink. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Apn_AMBRD"])

    @Apn_AMBRD.setter
    def Apn_AMBRD(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Apn_AMBRD"], value)

    @property
    def Apn_AMBRU(self):
        # type: () -> int
        """
        Returns
        -------
        - number: APN aggregated maximum bit rate for uplink.For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Apn_AMBRU"])

    @Apn_AMBRU.setter
    def Apn_AMBRU(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Apn_AMBRU"], value)

    @property
    def Db_gbrd(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Deprecated. Field is ignored. Kept for TCL BW compatibility
        """
        return self._get_attribute(self._SDM_ATT_MAP["Db_gbrd"])

    @Db_gbrd.setter
    def Db_gbrd(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Db_gbrd"], value)

    @property
    def Db_gbru(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Deprecated. Field is ignored. Kept for TCL BW compatibility
        """
        return self._get_attribute(self._SDM_ATT_MAP["Db_gbru"])

    @Db_gbru.setter
    def Db_gbru(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Db_gbru"], value)

    @property
    def Db_mbrd(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Db_mbrd"])

    @Db_mbrd.setter
    def Db_mbrd(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Db_mbrd"], value)

    @property
    def Db_mbru(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Db_mbru"])

    @Db_mbru.setter
    def Db_mbru(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Db_mbru"], value)

    @property
    def Db_pci(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ARP Preemption Capability
        """
        return self._get_attribute(self._SDM_ATT_MAP["Db_pci"])

    @Db_pci.setter
    def Db_pci(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Db_pci"], value)

    @property
    def Db_pl(self):
        # type: () -> int
        """
        Returns
        -------
        - number: ARP Priority Level
        """
        return self._get_attribute(self._SDM_ATT_MAP["Db_pl"])

    @Db_pl.setter
    def Db_pl(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Db_pl"], value)

    @property
    def Db_pvi(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ARP Preemption Vulnerability
        """
        return self._get_attribute(self._SDM_ATT_MAP["Db_pvi"])

    @Db_pvi.setter
    def Db_pvi(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Db_pvi"], value)

    @property
    def Db_qci(self):
        # type: () -> int
        """
        Returns
        -------
        - number: QoS Class Identifier
        """
        return self._get_attribute(self._SDM_ATT_MAP["Db_qci"])

    @Db_qci.setter
    def Db_qci(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Db_qci"], value)

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
    def EnableNIDBCreationDelay(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Delay Network Initiated Dedicated Bearer(NIDB) Creation
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableNIDBCreationDelay"])

    @EnableNIDBCreationDelay.setter
    def EnableNIDBCreationDelay(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableNIDBCreationDelay"], value)

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
    def IMSI(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first International Mobile Subscriber Identifier that will be accepted.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IMSI"])

    @IMSI.setter
    def IMSI(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IMSI"], value)

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
    def ParentPgw(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range): Id of parent PGW range
        """
        return self._get_attribute(self._SDM_ATT_MAP["ParentPgw"])

    @ParentPgw.setter
    def ParentPgw(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ParentPgw"], value)

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
    def PoolStartIPv4(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first IPv4 address to be assigned to an UE.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PoolStartIPv4"])

    @PoolStartIPv4.setter
    def PoolStartIPv4(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PoolStartIPv4"], value)

    @property
    def PoolStartIPv6(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first IPv6 address to be assigned to an UE.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PoolStartIPv6"])

    @PoolStartIPv6.setter
    def PoolStartIPv6(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PoolStartIPv6"], value)

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
    def RoundRobinDistribution(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Distribute the IMSIs on the assigned ports in a round-robin manner (E.g.: When having 3 IMSIs to distribute and 2 ports assigned the first IMSI will be distributed on the first port, the second one on the second port and the 3rd one on the first port)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RoundRobinDistribution"])

    @RoundRobinDistribution.setter
    def RoundRobinDistribution(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RoundRobinDistribution"], value)

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
    def UserPlaneIPv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first IPv4 address to be used by the L4-7 server activies.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserPlaneIPv4Address"])

    @UserPlaneIPv4Address.setter
    def UserPlaneIPv4Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserPlaneIPv4Address"], value)

    @property
    def UserPlaneIPv6Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The first IPv6 address to be used by the L4-7 server activies.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserPlaneIPv6Address"])

    @UserPlaneIPv6Address.setter
    def UserPlaneIPv6Address(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserPlaneIPv6Address"], value)

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

    def update(
        self,
        Apn=None,
        Apn_AMBRD=None,
        Apn_AMBRU=None,
        Db_gbrd=None,
        Db_gbru=None,
        Db_mbrd=None,
        Db_mbru=None,
        Db_pci=None,
        Db_pl=None,
        Db_pvi=None,
        Db_qci=None,
        DefaultBearerLifetimeTimer=None,
        EnableDefaultBearerLifetime=None,
        EnableNIDBCreationDelay=None,
        Enabled=None,
        IMSI=None,
        Ims_apn=None,
        IpType=None,
        Name=None,
        NidbCreationDelay=None,
        ParentPgw=None,
        PoolSize=None,
        PoolStartIPv4=None,
        PoolStartIPv6=None,
        PoolStartIp=None,
        RoundRobinDistribution=None,
        TotalCount=None,
        UserPlaneIPv4Address=None,
        UserPlaneIPv6Address=None,
        UserPlaneIpAddress=None,
        UserPlaneIpCount=None,
    ):
        # type: (str, int, int, int, int, int, int, bool, int, bool, int, int, bool, bool, bool, str, bool, str, str, int, str, int, str, str, str, bool, int, str, str, str, int) -> EgtpPcrfS5S8Range
        """Updates egtpPcrfS5S8Range resource on the server.

        Args
        ----
        - Apn (str): Access Point Name
        - Apn_AMBRD (number): APN aggregated maximum bit rate for downlink. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - Apn_AMBRU (number): APN aggregated maximum bit rate for uplink.For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - Db_gbrd (number): Deprecated. Field is ignored. Kept for TCL BW compatibility
        - Db_gbru (number): Deprecated. Field is ignored. Kept for TCL BW compatibility
        - Db_mbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Db_mbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Db_pci (bool): ARP Preemption Capability
        - Db_pl (number): ARP Priority Level
        - Db_pvi (bool): ARP Preemption Vulnerability
        - Db_qci (number): QoS Class Identifier
        - DefaultBearerLifetimeTimer (number): The time, in seconds, after which the default bearer is deleted
        - EnableDefaultBearerLifetime (bool): If enabled the default bearer will be deleted using the PGW initiated bearer deactivation procedure
        - EnableNIDBCreationDelay (bool): Delay Network Initiated Dedicated Bearer(NIDB) Creation
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IMSI (str): The first International Mobile Subscriber Identifier that will be accepted.
        - Ims_apn (bool): IMS APN
        - IpType (str): The IP type of the address(es) that will be assigned to the UEs. When choosing IPv4v6 both an IPv4 address and an IPv6 address will be assigned to the UE.
        - Name (str): Name of range
        - NidbCreationDelay (number): Time to wait (in seconds), from the moment the UE is attached, before sending Create Bearer Request for Network Initiated Dedicated Bearers(NIDB). This does not apply to MS Initiated Dedicated Bearers
        - ParentPgw (str(None | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range)): Id of parent PGW range
        - PoolSize (number): The number of UEs that will be accepted.
        - PoolStartIPv4 (str): The first IPv4 address to be assigned to an UE.
        - PoolStartIPv6 (str): The first IPv6 address to be assigned to an UE.
        - PoolStartIp (str): Obsolete - use poolStartIPv4 or poolStartIPv6
        - RoundRobinDistribution (bool): Distribute the IMSIs on the assigned ports in a round-robin manner (E.g.: When having 3 IMSIs to distribute and 2 ports assigned the first IMSI will be distributed on the first port, the second one on the second port and the 3rd one on the first port)
        - TotalCount (number): Layer 7 Server Count On All Ports
        - UserPlaneIPv4Address (str): The first IPv4 address to be used by the L4-7 server activies.
        - UserPlaneIPv6Address (str): The first IPv6 address to be used by the L4-7 server activies.
        - UserPlaneIpAddress (str): Obsolete - use userPlaneIPv4Address or userPlaneIPv6Address
        - UserPlaneIpCount (number): Layer 7 Server Count Per Port

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Apn=None,
        Apn_AMBRD=None,
        Apn_AMBRU=None,
        Db_gbrd=None,
        Db_gbru=None,
        Db_mbrd=None,
        Db_mbru=None,
        Db_pci=None,
        Db_pl=None,
        Db_pvi=None,
        Db_qci=None,
        DefaultBearerLifetimeTimer=None,
        EnableDefaultBearerLifetime=None,
        EnableNIDBCreationDelay=None,
        Enabled=None,
        IMSI=None,
        Ims_apn=None,
        IpType=None,
        Name=None,
        NidbCreationDelay=None,
        ObjectId=None,
        ParentPgw=None,
        PoolSize=None,
        PoolStartIPv4=None,
        PoolStartIPv6=None,
        PoolStartIp=None,
        RoundRobinDistribution=None,
        TotalCount=None,
        UserPlaneIPv4Address=None,
        UserPlaneIPv6Address=None,
        UserPlaneIpAddress=None,
        UserPlaneIpCount=None,
    ):
        # type: (str, int, int, int, int, int, int, bool, int, bool, int, int, bool, bool, bool, str, bool, str, str, int, str, str, int, str, str, str, bool, int, str, str, str, int) -> EgtpPcrfS5S8Range
        """Finds and retrieves egtpPcrfS5S8Range resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve egtpPcrfS5S8Range resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all egtpPcrfS5S8Range resources from the server.

        Args
        ----
        - Apn (str): Access Point Name
        - Apn_AMBRD (number): APN aggregated maximum bit rate for downlink. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - Apn_AMBRU (number): APN aggregated maximum bit rate for uplink.For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - Db_gbrd (number): Deprecated. Field is ignored. Kept for TCL BW compatibility
        - Db_gbru (number): Deprecated. Field is ignored. Kept for TCL BW compatibility
        - Db_mbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Db_mbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Db_pci (bool): ARP Preemption Capability
        - Db_pl (number): ARP Priority Level
        - Db_pvi (bool): ARP Preemption Vulnerability
        - Db_qci (number): QoS Class Identifier
        - DefaultBearerLifetimeTimer (number): The time, in seconds, after which the default bearer is deleted
        - EnableDefaultBearerLifetime (bool): If enabled the default bearer will be deleted using the PGW initiated bearer deactivation procedure
        - EnableNIDBCreationDelay (bool): Delay Network Initiated Dedicated Bearer(NIDB) Creation
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IMSI (str): The first International Mobile Subscriber Identifier that will be accepted.
        - Ims_apn (bool): IMS APN
        - IpType (str): The IP type of the address(es) that will be assigned to the UEs. When choosing IPv4v6 both an IPv4 address and an IPv6 address will be assigned to the UE.
        - Name (str): Name of range
        - NidbCreationDelay (number): Time to wait (in seconds), from the moment the UE is attached, before sending Create Bearer Request for Network Initiated Dedicated Bearers(NIDB). This does not apply to MS Initiated Dedicated Bearers
        - ObjectId (str): Unique identifier for this object
        - ParentPgw (str(None | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range)): Id of parent PGW range
        - PoolSize (number): The number of UEs that will be accepted.
        - PoolStartIPv4 (str): The first IPv4 address to be assigned to an UE.
        - PoolStartIPv6 (str): The first IPv6 address to be assigned to an UE.
        - PoolStartIp (str): Obsolete - use poolStartIPv4 or poolStartIPv6
        - RoundRobinDistribution (bool): Distribute the IMSIs on the assigned ports in a round-robin manner (E.g.: When having 3 IMSIs to distribute and 2 ports assigned the first IMSI will be distributed on the first port, the second one on the second port and the 3rd one on the first port)
        - TotalCount (number): Layer 7 Server Count On All Ports
        - UserPlaneIPv4Address (str): The first IPv4 address to be used by the L4-7 server activies.
        - UserPlaneIPv6Address (str): The first IPv6 address to be used by the L4-7 server activies.
        - UserPlaneIpAddress (str): Obsolete - use userPlaneIPv4Address or userPlaneIPv6Address
        - UserPlaneIpCount (number): Layer 7 Server Count Per Port

        Returns
        -------
        - self: This instance with matching egtpPcrfS5S8Range resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of egtpPcrfS5S8Range data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the egtpPcrfS5S8Range resources from the server available through an iterator or index

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
