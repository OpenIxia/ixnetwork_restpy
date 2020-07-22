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


class DhcpV4Properties(Base):
    """Controls the general DHCPv4 interface properties.
    The DhcpV4Properties class encapsulates a required dhcpV4Properties resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpV4Properties'
    _SDM_ATT_MAP = {
        'ClientId': 'clientId',
        'Enabled': 'enabled',
        'RenewTimer': 'renewTimer',
        'RequestRate': 'requestRate',
        'ServerId': 'serverId',
        'Tlvs': 'tlvs',
        'VendorId': 'vendorId',
    }

    def __init__(self, parent):
        super(DhcpV4Properties, self).__init__(parent)

    @property
    def ClientId(self):
        """
        Returns
        -------
        - str: The user may optionally assign an identifier for the Client. This value must be unique on the subnet where the DHCP Client is located.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientId'])
    @ClientId.setter
    def ClientId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientId'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If enabled, DHCP negotiation will be started and an IPv4 address learned from the DHCP server will be assigned automatically to the protocol interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def RenewTimer(self):
        """
        Returns
        -------
        - number: The renew timer value specified by the DHCPv4 server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RenewTimer'])
    @RenewTimer.setter
    def RenewTimer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RenewTimer'], value)

    @property
    def RequestRate(self):
        """
        Returns
        -------
        - number: (For rate control) The user-specified maximum number of Request messages that can be sent per second from the client to the DHCP server, requesting an IPv4 address. A value of zero (0) indicates that there will be no rate control, i.e., Requests will be sent as quickly as possible.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RequestRate'])
    @RequestRate.setter
    def RequestRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RequestRate'], value)

    @property
    def ServerId(self):
        """
        Returns
        -------
        - str: This IPv4 address value is used to identify the DHCP Server and as a destination address from the client.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerId'])
    @ServerId.setter
    def ServerId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerId'], value)

    @property
    def Tlvs(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:str)): The type length value for DHCP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tlvs'])
    @Tlvs.setter
    def Tlvs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Tlvs'], value)

    @property
    def VendorId(self):
        """
        Returns
        -------
        - str: The optional, user-assigned Vendor ID (vendor class identifier).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorId'])
    @VendorId.setter
    def VendorId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VendorId'], value)

    def update(self, ClientId=None, Enabled=None, RenewTimer=None, RequestRate=None, ServerId=None, Tlvs=None, VendorId=None):
        """Updates dhcpV4Properties resource on the server.

        Args
        ----
        - ClientId (str): The user may optionally assign an identifier for the Client. This value must be unique on the subnet where the DHCP Client is located.
        - Enabled (bool): If enabled, DHCP negotiation will be started and an IPv4 address learned from the DHCP server will be assigned automatically to the protocol interface.
        - RenewTimer (number): The renew timer value specified by the DHCPv4 server.
        - RequestRate (number): (For rate control) The user-specified maximum number of Request messages that can be sent per second from the client to the DHCP server, requesting an IPv4 address. A value of zero (0) indicates that there will be no rate control, i.e., Requests will be sent as quickly as possible.
        - ServerId (str): This IPv4 address value is used to identify the DHCP Server and as a destination address from the client.
        - Tlvs (list(dict(arg1:number,arg2:str))): The type length value for DHCP.
        - VendorId (str): The optional, user-assigned Vendor ID (vendor class identifier).

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
