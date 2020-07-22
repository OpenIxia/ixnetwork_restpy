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


class DhcpV6Properties(Base):
    """Controls the general DHCPv6 interface properties.
    The DhcpV6Properties class encapsulates a required dhcpV6Properties resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpV6Properties'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'IaId': 'iaId',
        'IaType': 'iaType',
        'RenewTimer': 'renewTimer',
        'RequestRate': 'requestRate',
        'Tlvs': 'tlvs',
    }

    def __init__(self, parent):
        super(DhcpV6Properties, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the DHCPv6 client feature. DHCPv6 negotiation will be started and an IPv6 address learned from the DHCPv6 server will be assigned automatically to the protocol interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IaId(self):
        """
        Returns
        -------
        - number: The unique identifier value for the Identity Association (IA).
        """
        return self._get_attribute(self._SDM_ATT_MAP['IaId'])
    @IaId.setter
    def IaId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IaId'], value)

    @property
    def IaType(self):
        """
        Returns
        -------
        - str(permanent | temporary | prefixDelegation): The Identity Association (IA) Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IaType'])
    @IaType.setter
    def IaType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IaType'], value)

    @property
    def RenewTimer(self):
        """
        Returns
        -------
        - number: The user-specified value and the lease timer (from the DHCP Server) are compared. The lowest value is used as the release/renew timer. After this time period has elapsed, the address will be renewed.
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
        - number: The user-specified maximum number of Request messages that can be sent per second from the client to the DHCPv6 server, requesting an IPv6 address. A value of zero (0) indicates that there will be no rate control, that is, requests will be sent as quickly as possible.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RequestRate'])
    @RequestRate.setter
    def RequestRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RequestRate'], value)

    @property
    def Tlvs(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:str)): DHCP TLVs (type length value) for custom DHCP options.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tlvs'])
    @Tlvs.setter
    def Tlvs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Tlvs'], value)

    def update(self, Enabled=None, IaId=None, IaType=None, RenewTimer=None, RequestRate=None, Tlvs=None):
        """Updates dhcpV6Properties resource on the server.

        Args
        ----
        - Enabled (bool): Enables the DHCPv6 client feature. DHCPv6 negotiation will be started and an IPv6 address learned from the DHCPv6 server will be assigned automatically to the protocol interface.
        - IaId (number): The unique identifier value for the Identity Association (IA).
        - IaType (str(permanent | temporary | prefixDelegation)): The Identity Association (IA) Type.
        - RenewTimer (number): The user-specified value and the lease timer (from the DHCP Server) are compared. The lowest value is used as the release/renew timer. After this time period has elapsed, the address will be renewed.
        - RequestRate (number): The user-specified maximum number of Request messages that can be sent per second from the client to the DHCPv6 server, requesting an IPv6 address. A value of zero (0) indicates that there will be no rate control, that is, requests will be sent as quickly as possible.
        - Tlvs (list(dict(arg1:number,arg2:str))): DHCP TLVs (type length value) for custom DHCP options.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
