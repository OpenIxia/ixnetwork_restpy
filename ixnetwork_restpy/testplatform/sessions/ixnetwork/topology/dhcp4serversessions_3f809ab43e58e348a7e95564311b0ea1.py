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


class Dhcp4ServerSessions(Base):
    """DHCPv4 Leases.
    The Dhcp4ServerSessions class encapsulates a required dhcp4ServerSessions resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcp4ServerSessions'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DefaultLeaseTime': 'defaultLeaseTime',
        'DescriptiveName': 'descriptiveName',
        'EchoRelayInfo': 'echoRelayInfo',
        'EnableVssAddrAssgnmt': 'enableVssAddrAssgnmt',
        'IpAddress': 'ipAddress',
        'IpAddressIncrement': 'ipAddressIncrement',
        'IpDns1': 'ipDns1',
        'IpDns2': 'ipDns2',
        'IpGateway': 'ipGateway',
        'IpPrefix': 'ipPrefix',
        'Name': 'name',
        'PoolSize': 'poolSize',
        'SessionInfo': 'sessionInfo',
        'VpnId': 'vpnId',
        'VpnName': 'vpnName',
    }

    def __init__(self, parent):
        super(Dhcp4ServerSessions, self).__init__(parent)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DefaultLeaseTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Life Time length in seconds that will be assigned to a lease if the requesting DHCP Client does not specify a specific expiration time.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DefaultLeaseTime']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EchoRelayInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable echoing of DHCP option 82.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EchoRelayInfo']))

    @property
    def EnableVssAddrAssgnmt(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, DHCP server will assign leases based on VPN.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableVssAddrAssgnmt']))

    @property
    def IpAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The IP address of the first lease pool.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpAddress']))

    @property
    def IpAddressIncrement(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The increment value for the lease address within the lease pool.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpAddressIncrement']))

    @property
    def IpDns1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The first DNS address advertised in DHCP Offer and Reply messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpDns1']))

    @property
    def IpDns2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The second DNS address advertised in DHCP Offer and Reply messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpDns2']))

    @property
    def IpGateway(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Router address advertised in DHCP Offer and Reply messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpGateway']))

    @property
    def IpPrefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Subnet Address length used to compute the subnetwork the advertised lease is part of.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpPrefix']))

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
    def PoolSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of leases to be allocated per each server address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PoolSize']))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[excessiveTlvs | none | poolTooLarge]): Logs additional information about the session state
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def VpnId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Based on this VPN ID, DHCP server will assign leases.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VpnId']))

    @property
    def VpnName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Based on this VPN Name, DHCP server will assign leases.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VpnName']))

    def update(self, Name=None):
        """Updates dhcp4ServerSessions resource on the server.

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

    def get_device_ids(self, PortNames=None, DefaultLeaseTime=None, EchoRelayInfo=None, EnableVssAddrAssgnmt=None, IpAddress=None, IpAddressIncrement=None, IpDns1=None, IpDns2=None, IpGateway=None, IpPrefix=None, PoolSize=None, VpnId=None, VpnName=None):
        """Base class infrastructure that gets a list of dhcp4ServerSessions device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - DefaultLeaseTime (str): optional regex of defaultLeaseTime
        - EchoRelayInfo (str): optional regex of echoRelayInfo
        - EnableVssAddrAssgnmt (str): optional regex of enableVssAddrAssgnmt
        - IpAddress (str): optional regex of ipAddress
        - IpAddressIncrement (str): optional regex of ipAddressIncrement
        - IpDns1 (str): optional regex of ipDns1
        - IpDns2 (str): optional regex of ipDns2
        - IpGateway (str): optional regex of ipGateway
        - IpPrefix (str): optional regex of ipPrefix
        - PoolSize (str): optional regex of poolSize
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
