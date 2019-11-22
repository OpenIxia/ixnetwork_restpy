# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class EgtpSgwRange(Base):
    """PCRF Range
    The EgtpSgwRange class encapsulates a required egtpSgwRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'egtpSgwRange'

    def __init__(self, parent):
        super(EgtpSgwRange, self).__init__(parent)

    @property
    def DedicatedBearer(self):
        """An instance of the DedicatedBearer class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dedicatedbearer_3766b0a77129c7051ae891dbaedd94ca.DedicatedBearer)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dedicatedbearer_3766b0a77129c7051ae891dbaedd94ca import DedicatedBearer
        return DedicatedBearer(self)

    @property
    def TrafficProfileProxiesSgw(self):
        """An instance of the TrafficProfileProxiesSgw class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxiessgw_d7841c0cda4ce19fc6772c2ce2fadb06.TrafficProfileProxiesSgw)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.trafficprofileproxiessgw_d7841c0cda4ce19fc6772c2ce2fadb06 import TrafficProfileProxiesSgw
        return TrafficProfileProxiesSgw(self)

    @property
    def Apn(self):
        """Access Point Name

        Returns:
            str
        """
        return self._get_attribute('apn')
    @Apn.setter
    def Apn(self, value):
        self._set_attribute('apn', value)

    @property
    def ApnAmbrd(self):
        """APN aggregated maximum bit rate for downlink. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.

        Returns:
            number
        """
        return self._get_attribute('apnAmbrd')
    @ApnAmbrd.setter
    def ApnAmbrd(self, value):
        self._set_attribute('apnAmbrd', value)

    @property
    def ApnAmbru(self):
        """APN aggregated maximum bit rate for uplink.For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.

        Returns:
            number
        """
        return self._get_attribute('apnAmbru')
    @ApnAmbru.setter
    def ApnAmbru(self, value):
        self._set_attribute('apnAmbru', value)

    @property
    def DbMbrd(self):
        """Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.

        Returns:
            number
        """
        return self._get_attribute('dbMbrd')
    @DbMbrd.setter
    def DbMbrd(self, value):
        self._set_attribute('dbMbrd', value)

    @property
    def DbMbru(self):
        """Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.

        Returns:
            number
        """
        return self._get_attribute('dbMbru')
    @DbMbru.setter
    def DbMbru(self, value):
        self._set_attribute('dbMbru', value)

    @property
    def DbPci(self):
        """ARP Preemption Capability

        Returns:
            bool
        """
        return self._get_attribute('dbPci')
    @DbPci.setter
    def DbPci(self, value):
        self._set_attribute('dbPci', value)

    @property
    def DbPl(self):
        """ARP Priority Level

        Returns:
            number
        """
        return self._get_attribute('dbPl')
    @DbPl.setter
    def DbPl(self, value):
        self._set_attribute('dbPl', value)

    @property
    def DbPvi(self):
        """ARP Preemption Vulnerability

        Returns:
            bool
        """
        return self._get_attribute('dbPvi')
    @DbPvi.setter
    def DbPvi(self, value):
        self._set_attribute('dbPvi', value)

    @property
    def DbQci(self):
        """QoS Class Identifier

        Returns:
            number
        """
        return self._get_attribute('dbQci')
    @DbQci.setter
    def DbQci(self, value):
        self._set_attribute('dbQci', value)

    @property
    def DefaultBearerLifetimeTimer(self):
        """The time, in seconds, after which the default bearer is deleted

        Returns:
            number
        """
        return self._get_attribute('defaultBearerLifetimeTimer')
    @DefaultBearerLifetimeTimer.setter
    def DefaultBearerLifetimeTimer(self, value):
        self._set_attribute('defaultBearerLifetimeTimer', value)

    @property
    def EnableDefaultBearerLifetime(self):
        """If enabled the default bearer will be deleted using the PGW initiated bearer deactivation procedure

        Returns:
            bool
        """
        return self._get_attribute('enableDefaultBearerLifetime')
    @EnableDefaultBearerLifetime.setter
    def EnableDefaultBearerLifetime(self, value):
        self._set_attribute('enableDefaultBearerLifetime', value)

    @property
    def EnableNidbCreationDelay(self):
        """Delay Network Initiated Dedicated Bearer(NIDB) Creation

        Returns:
            bool
        """
        return self._get_attribute('enableNidbCreationDelay')
    @EnableNidbCreationDelay.setter
    def EnableNidbCreationDelay(self, value):
        self._set_attribute('enableNidbCreationDelay', value)

    @property
    def Enabled(self):
        """Disabled ranges won't be configured nor validated.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def Ims_apn(self):
        """IMS APN

        Returns:
            bool
        """
        return self._get_attribute('ims_apn')
    @Ims_apn.setter
    def Ims_apn(self, value):
        self._set_attribute('ims_apn', value)

    @property
    def Imsi(self):
        """The first International Mobile Subscriber Identifier that will be accepted.

        Returns:
            str
        """
        return self._get_attribute('imsi')
    @Imsi.setter
    def Imsi(self, value):
        self._set_attribute('imsi', value)

    @property
    def IpType(self):
        """The IP type of the address(es) that will be assigned to the UEs. When choosing IPv4v6 both an IPv4 address and an IPv6 address will be assigned to the UE.

        Returns:
            str
        """
        return self._get_attribute('ipType')
    @IpType.setter
    def IpType(self, value):
        self._set_attribute('ipType', value)

    @property
    def Name(self):
        """Name of range

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NidbCreationDelay(self):
        """Time to wait (in seconds), from the moment the UE is attached, before sending Create Bearer Request for Network Initiated Dedicated Bearers(NIDB). This does not apply to MS Initiated Dedicated Bearers

        Returns:
            number
        """
        return self._get_attribute('nidbCreationDelay')
    @NidbCreationDelay.setter
    def NidbCreationDelay(self, value):
        self._set_attribute('nidbCreationDelay', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def PoolSize(self):
        """The number of UEs that will be accepted.

        Returns:
            number
        """
        return self._get_attribute('poolSize')
    @PoolSize.setter
    def PoolSize(self, value):
        self._set_attribute('poolSize', value)

    @property
    def PoolStartIp(self):
        """Obsolete - use poolStartIPv4 or poolStartIPv6

        Returns:
            str
        """
        return self._get_attribute('poolStartIp')
    @PoolStartIp.setter
    def PoolStartIp(self, value):
        self._set_attribute('poolStartIp', value)

    @property
    def PoolStartIpv4(self):
        """The first IPv4 address to be assigned to an UE.

        Returns:
            str
        """
        return self._get_attribute('poolStartIpv4')
    @PoolStartIpv4.setter
    def PoolStartIpv4(self, value):
        self._set_attribute('poolStartIpv4', value)

    @property
    def PoolStartIpv6(self):
        """The first IPv6 address to be assigned to an UE.

        Returns:
            str
        """
        return self._get_attribute('poolStartIpv6')
    @PoolStartIpv6.setter
    def PoolStartIpv6(self, value):
        self._set_attribute('poolStartIpv6', value)

    @property
    def TotalCount(self):
        """Layer 7 Server Count On All Ports

        Returns:
            number
        """
        return self._get_attribute('totalCount')
    @TotalCount.setter
    def TotalCount(self, value):
        self._set_attribute('totalCount', value)

    @property
    def UserPlaneIpAddress(self):
        """Obsolete - use userPlaneIPv4Address or userPlaneIPv6Address

        Returns:
            str
        """
        return self._get_attribute('userPlaneIpAddress')
    @UserPlaneIpAddress.setter
    def UserPlaneIpAddress(self, value):
        self._set_attribute('userPlaneIpAddress', value)

    @property
    def UserPlaneIpCount(self):
        """Layer 7 Server Count Per Port

        Returns:
            number
        """
        return self._get_attribute('userPlaneIpCount')
    @UserPlaneIpCount.setter
    def UserPlaneIpCount(self, value):
        self._set_attribute('userPlaneIpCount', value)

    @property
    def UserPlaneIpv4Address(self):
        """The first IPv4 address to be used by the L4-7 server activies.

        Returns:
            str
        """
        return self._get_attribute('userPlaneIpv4Address')
    @UserPlaneIpv4Address.setter
    def UserPlaneIpv4Address(self, value):
        self._set_attribute('userPlaneIpv4Address', value)

    @property
    def UserPlaneIpv6Address(self):
        """The first IPv6 address to be used by the L4-7 server activies.

        Returns:
            str
        """
        return self._get_attribute('userPlaneIpv6Address')
    @UserPlaneIpv6Address.setter
    def UserPlaneIpv6Address(self, value):
        self._set_attribute('userPlaneIpv6Address', value)

    def update(self, Apn=None, ApnAmbrd=None, ApnAmbru=None, DbMbrd=None, DbMbru=None, DbPci=None, DbPl=None, DbPvi=None, DbQci=None, DefaultBearerLifetimeTimer=None, EnableDefaultBearerLifetime=None, EnableNidbCreationDelay=None, Enabled=None, Ims_apn=None, Imsi=None, IpType=None, Name=None, NidbCreationDelay=None, PoolSize=None, PoolStartIp=None, PoolStartIpv4=None, PoolStartIpv6=None, TotalCount=None, UserPlaneIpAddress=None, UserPlaneIpCount=None, UserPlaneIpv4Address=None, UserPlaneIpv6Address=None):
        """Updates a child instance of egtpSgwRange on the server.

        Args:
            Apn (str): Access Point Name
            ApnAmbrd (number): APN aggregated maximum bit rate for downlink. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
            ApnAmbru (number): APN aggregated maximum bit rate for uplink.For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
            DbMbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            DbMbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            DbPci (bool): ARP Preemption Capability
            DbPl (number): ARP Priority Level
            DbPvi (bool): ARP Preemption Vulnerability
            DbQci (number): QoS Class Identifier
            DefaultBearerLifetimeTimer (number): The time, in seconds, after which the default bearer is deleted
            EnableDefaultBearerLifetime (bool): If enabled the default bearer will be deleted using the PGW initiated bearer deactivation procedure
            EnableNidbCreationDelay (bool): Delay Network Initiated Dedicated Bearer(NIDB) Creation
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Ims_apn (bool): IMS APN
            Imsi (str): The first International Mobile Subscriber Identifier that will be accepted.
            IpType (str): The IP type of the address(es) that will be assigned to the UEs. When choosing IPv4v6 both an IPv4 address and an IPv6 address will be assigned to the UE.
            Name (str): Name of range
            NidbCreationDelay (number): Time to wait (in seconds), from the moment the UE is attached, before sending Create Bearer Request for Network Initiated Dedicated Bearers(NIDB). This does not apply to MS Initiated Dedicated Bearers
            PoolSize (number): The number of UEs that will be accepted.
            PoolStartIp (str): Obsolete - use poolStartIPv4 or poolStartIPv6
            PoolStartIpv4 (str): The first IPv4 address to be assigned to an UE.
            PoolStartIpv6 (str): The first IPv6 address to be assigned to an UE.
            TotalCount (number): Layer 7 Server Count On All Ports
            UserPlaneIpAddress (str): Obsolete - use userPlaneIPv4Address or userPlaneIPv6Address
            UserPlaneIpCount (number): Layer 7 Server Count Per Port
            UserPlaneIpv4Address (str): The first IPv4 address to be used by the L4-7 server activies.
            UserPlaneIpv6Address (str): The first IPv6 address to be used by the L4-7 server activies.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
