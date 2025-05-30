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


class Dhcp6ServerSessions(Base):
    """DHCPv6 Leases.
    The Dhcp6ServerSessions class encapsulates a required dhcp6ServerSessions resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "dhcp6ServerSessions"
    _SDM_ATT_MAP = {
        "AddressDuidMask": "addressDuidMask",
        "AddressDuidPattern": "addressDuidPattern",
        "AddressesPerIA": "addressesPerIA",
        "Count": "count",
        "CustomRebindTime": "customRebindTime",
        "CustomRenewTime": "customRenewTime",
        "DefaultLeaseTime": "defaultLeaseTime",
        "DescriptiveName": "descriptiveName",
        "EnableAddressMatchDuid": "enableAddressMatchDuid",
        "EnablePrefixMatchDuid": "enablePrefixMatchDuid",
        "EnableVssAddrAssgnmt": "enableVssAddrAssgnmt",
        "IaType": "iaType",
        "Ignore": "ignore",
        "IgnoreMask": "ignoreMask",
        "IgnorePattern": "ignorePattern",
        "IpAddress": "ipAddress",
        "IpAddressIncrement": "ipAddressIncrement",
        "IpAddressPD": "ipAddressPD",
        "IpPrefix": "ipPrefix",
        "IpPrefixIncrement": "ipPrefixIncrement",
        "LeaseTimeIncrement": "leaseTimeIncrement",
        "Nak": "nak",
        "NakMask": "nakMask",
        "NakPattern": "nakPattern",
        "Name": "name",
        "PoolPrefixSize": "poolPrefixSize",
        "PoolSize": "poolSize",
        "PrefixDuidIncrement": "prefixDuidIncrement",
        "PrefixDuidStart": "prefixDuidStart",
        "PrefixLength": "prefixLength",
        "PrefixesPerIA": "prefixesPerIA",
        "UseCustomTimes": "useCustomTimes",
        "VpnId": "vpnId",
        "VpnName": "vpnName",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Dhcp6ServerSessions, self).__init__(parent, list_op)

    @property
    def AddressDuidMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The mask based on which the DUIDs are chosen for address assignment.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressDuidMask"])
        )

    @property
    def AddressDuidPattern(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The pattern based on which the DUIDs are chosen for address assignment.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressDuidPattern"])
        )

    @property
    def AddressesPerIA(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of addresses to be advertised in a single IANA option.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressesPerIA"])
        )

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def CustomRebindTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Time (in seconds) after the client will start rebinding the leases from the server.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CustomRebindTime"])
        )

    @property
    def CustomRenewTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Time (in seconds) after the client will start renewing the leases from the server.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CustomRenewTime"])
        )

    @property
    def DefaultLeaseTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Life Time length in seconds that will be assigned to a lease if the requesting DHCP Client does not specify a specific expiration time.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefaultLeaseTime"])
        )

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
    def EnableAddressMatchDuid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, the requests with DUIDs matching the mask and pattern will be assigned addresses from this pool.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableAddressMatchDuid"])
        )

    @property
    def EnablePrefixMatchDuid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, the requests with DUIDs matching DUID start and increment will be given a specific prefix from this pool.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnablePrefixMatchDuid"])
        )

    @property
    def EnableVssAddrAssgnmt(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, DHCP server will assign leases based on VPN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableVssAddrAssgnmt"])
        )

    @property
    def IaType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Identity Association type supported by IPv6 address pools .
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IaType"]))

    @property
    def Ignore(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, the requests with DUIDs matching the mask and pattern will be ignored by the Server.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ignore"]))

    @property
    def IgnoreMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The mask based on which the DUIDs of ignored addresses are chosen.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IgnoreMask"]))

    @property
    def IgnorePattern(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The pattern based on which the DUIDs of ignored addresses are chosen.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IgnorePattern"]))

    @property
    def IpAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The IP address of the first lease pool.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IpAddress"]))

    @property
    def IpAddressIncrement(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The increment value for the lease address within the lease pool.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpAddressIncrement"])
        )

    @property
    def IpAddressPD(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The prefix of the first lease pool.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IpAddressPD"]))

    @property
    def IpPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Subnet Address length used to compute the subnetwork the advertised lease is part of.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IpPrefix"]))

    @property
    def IpPrefixIncrement(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The increment value for the lease prefix within the lease pool.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpPrefixIncrement"])
        )

    @property
    def LeaseTimeIncrement(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Increment step for Lease Time.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LeaseTimeIncrement"])
        )

    @property
    def Nak(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, the requests with DUIDs matching the mask and pattern will be NAKed by the Server.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Nak"]))

    @property
    def NakMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The mask based on which the DUIDs of NAKed addresses are chosen.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NakMask"]))

    @property
    def NakPattern(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The pattern based on which the DUIDs of NAKed addresses are chosen.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NakPattern"]))

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
    def PoolPrefixSize(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of leases to be allocated per each server prefix.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PoolPrefixSize"])
        )

    @property
    def PoolSize(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of leases to be allocated per each server address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PoolSize"]))

    @property
    def PrefixDuidIncrement(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The increment used to generate the DUIDs which will be chosen for prefix assignment.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrefixDuidIncrement"])
        )

    @property
    def PrefixDuidStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The first DUID which will be chosen for prefix assignment.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrefixDuidStart"])
        )

    @property
    def PrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The subnet address length advertised in DHCP Offer and Reply messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrefixLength"]))

    @property
    def PrefixesPerIA(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of prefixes to be advertised in a single IANA option.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrefixesPerIA"]))

    @property
    def UseCustomTimes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): >Use Custom Renew/Rebind Times instead of the ones computed from the valability times of the leases.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseCustomTimes"])
        )

    @property
    def VpnId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Based on this VPN ID, DHCP server will assign leases.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VpnId"]))

    @property
    def VpnName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Based on this VPN Name, DHCP server will assign leases.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VpnName"]))

    def update(self, Name=None):
        # type: (str) -> Dhcp6ServerSessions
        """Updates dhcp6ServerSessions resource on the server.

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

    def find(self, Count=None, DescriptiveName=None, Name=None):
        # type: (int, str, str) -> Dhcp6ServerSessions
        """Finds and retrieves dhcp6ServerSessions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcp6ServerSessions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcp6ServerSessions resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching dhcp6ServerSessions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcp6ServerSessions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcp6ServerSessions resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (bool):
        - Arg3 (bool):
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

    def PerformActionOnAllObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the performActionOnAllObjects operation on the server.

        Action on All Objects

        performActionOnAllObjects(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------------
        - Arg2 (str): Action Name
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

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
            "performActionOnAllObjects", payload=payload, response_object=None
        )

    def get_device_ids(
        self,
        PortNames=None,
        AddressDuidMask=None,
        AddressDuidPattern=None,
        AddressesPerIA=None,
        CustomRebindTime=None,
        CustomRenewTime=None,
        DefaultLeaseTime=None,
        EnableAddressMatchDuid=None,
        EnablePrefixMatchDuid=None,
        EnableVssAddrAssgnmt=None,
        IaType=None,
        Ignore=None,
        IgnoreMask=None,
        IgnorePattern=None,
        IpAddress=None,
        IpAddressIncrement=None,
        IpAddressPD=None,
        IpPrefix=None,
        IpPrefixIncrement=None,
        LeaseTimeIncrement=None,
        Nak=None,
        NakMask=None,
        NakPattern=None,
        PoolPrefixSize=None,
        PoolSize=None,
        PrefixDuidIncrement=None,
        PrefixDuidStart=None,
        PrefixLength=None,
        PrefixesPerIA=None,
        UseCustomTimes=None,
        VpnId=None,
        VpnName=None,
    ):
        """Base class infrastructure that gets a list of dhcp6ServerSessions device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AddressDuidMask (str): optional regex of addressDuidMask
        - AddressDuidPattern (str): optional regex of addressDuidPattern
        - AddressesPerIA (str): optional regex of addressesPerIA
        - CustomRebindTime (str): optional regex of customRebindTime
        - CustomRenewTime (str): optional regex of customRenewTime
        - DefaultLeaseTime (str): optional regex of defaultLeaseTime
        - EnableAddressMatchDuid (str): optional regex of enableAddressMatchDuid
        - EnablePrefixMatchDuid (str): optional regex of enablePrefixMatchDuid
        - EnableVssAddrAssgnmt (str): optional regex of enableVssAddrAssgnmt
        - IaType (str): optional regex of iaType
        - Ignore (str): optional regex of ignore
        - IgnoreMask (str): optional regex of ignoreMask
        - IgnorePattern (str): optional regex of ignorePattern
        - IpAddress (str): optional regex of ipAddress
        - IpAddressIncrement (str): optional regex of ipAddressIncrement
        - IpAddressPD (str): optional regex of ipAddressPD
        - IpPrefix (str): optional regex of ipPrefix
        - IpPrefixIncrement (str): optional regex of ipPrefixIncrement
        - LeaseTimeIncrement (str): optional regex of leaseTimeIncrement
        - Nak (str): optional regex of nak
        - NakMask (str): optional regex of nakMask
        - NakPattern (str): optional regex of nakPattern
        - PoolPrefixSize (str): optional regex of poolPrefixSize
        - PoolSize (str): optional regex of poolSize
        - PrefixDuidIncrement (str): optional regex of prefixDuidIncrement
        - PrefixDuidStart (str): optional regex of prefixDuidStart
        - PrefixLength (str): optional regex of prefixLength
        - PrefixesPerIA (str): optional regex of prefixesPerIA
        - UseCustomTimes (str): optional regex of useCustomTimes
        - VpnId (str): optional regex of vpnId
        - VpnName (str): optional regex of vpnName

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
