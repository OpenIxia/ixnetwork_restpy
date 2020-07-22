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


class CMacMappedIp(Base):
    """This objects holds all the IP (V4/V6) addresses associated with a B-MAC of an ethernet segment.
    The CMacMappedIp class encapsulates a list of cMacMappedIp resources that are managed by the user.
    A list of resources can be retrieved from the server using the CMacMappedIp.find() method.
    The list can be managed by using the CMacMappedIp.add() and CMacMappedIp.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'cMacMappedIp'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'IpAddress': 'ipAddress',
        'IpStep': 'ipStep',
        'IpType': 'ipType',
    }

    def __init__(self, parent):
        super(CMacMappedIp, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true then this IP is associated with the B-MAC of the ethernet segment. Default value is false.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IpAddress(self):
        """
        Returns
        -------
        - str: IP address value is given here depending on the IP Type. Default value is all zero.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpAddress'])
    @IpAddress.setter
    def IpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpAddress'], value)

    @property
    def IpStep(self):
        """
        Returns
        -------
        - number: If IP address is associated with a MAC range (C-MAC Range) then this step value is used to make the IP addresses for all C-MAC of that range unique. For example if C-MAC range has no of C-MAC 3 and IP address associated with this mac range is 1.1.1.1 with step 2 then IP addresses for 3 MACs of the mac range will be 1.1.1.1, 1.1.1.3 and 1.1.1.5. Default value is 1. This is used only in EVPN mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpStep'])
    @IpStep.setter
    def IpStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpStep'], value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): Drop down of {IPv4, IPv6}. If IPv4 is selected then IPv4 address is used. If IPv6 is selected then IPv6 address is used. Default value is IPv4.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpType'])
    @IpType.setter
    def IpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpType'], value)

    def update(self, Enabled=None, IpAddress=None, IpStep=None, IpType=None):
        """Updates cMacMappedIp resource on the server.

        Args
        ----
        - Enabled (bool): If true then this IP is associated with the B-MAC of the ethernet segment. Default value is false.
        - IpAddress (str): IP address value is given here depending on the IP Type. Default value is all zero.
        - IpStep (number): If IP address is associated with a MAC range (C-MAC Range) then this step value is used to make the IP addresses for all C-MAC of that range unique. For example if C-MAC range has no of C-MAC 3 and IP address associated with this mac range is 1.1.1.1 with step 2 then IP addresses for 3 MACs of the mac range will be 1.1.1.1, 1.1.1.3 and 1.1.1.5. Default value is 1. This is used only in EVPN mode.
        - IpType (str(ipv4 | ipv6)): Drop down of {IPv4, IPv6}. If IPv4 is selected then IPv4 address is used. If IPv6 is selected then IPv6 address is used. Default value is IPv4.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, IpAddress=None, IpStep=None, IpType=None):
        """Adds a new cMacMappedIp resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true then this IP is associated with the B-MAC of the ethernet segment. Default value is false.
        - IpAddress (str): IP address value is given here depending on the IP Type. Default value is all zero.
        - IpStep (number): If IP address is associated with a MAC range (C-MAC Range) then this step value is used to make the IP addresses for all C-MAC of that range unique. For example if C-MAC range has no of C-MAC 3 and IP address associated with this mac range is 1.1.1.1 with step 2 then IP addresses for 3 MACs of the mac range will be 1.1.1.1, 1.1.1.3 and 1.1.1.5. Default value is 1. This is used only in EVPN mode.
        - IpType (str(ipv4 | ipv6)): Drop down of {IPv4, IPv6}. If IPv4 is selected then IPv4 address is used. If IPv6 is selected then IPv6 address is used. Default value is IPv4.

        Returns
        -------
        - self: This instance with all currently retrieved cMacMappedIp resources using find and the newly added cMacMappedIp resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained cMacMappedIp resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, IpAddress=None, IpStep=None, IpType=None):
        """Finds and retrieves cMacMappedIp resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cMacMappedIp resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cMacMappedIp resources from the server.

        Args
        ----
        - Enabled (bool): If true then this IP is associated with the B-MAC of the ethernet segment. Default value is false.
        - IpAddress (str): IP address value is given here depending on the IP Type. Default value is all zero.
        - IpStep (number): If IP address is associated with a MAC range (C-MAC Range) then this step value is used to make the IP addresses for all C-MAC of that range unique. For example if C-MAC range has no of C-MAC 3 and IP address associated with this mac range is 1.1.1.1 with step 2 then IP addresses for 3 MACs of the mac range will be 1.1.1.1, 1.1.1.3 and 1.1.1.5. Default value is 1. This is used only in EVPN mode.
        - IpType (str(ipv4 | ipv6)): Drop down of {IPv4, IPv6}. If IPv4 is selected then IPv4 address is used. If IPv6 is selected then IPv6 address is used. Default value is IPv4.

        Returns
        -------
        - self: This instance with matching cMacMappedIp resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cMacMappedIp data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cMacMappedIp resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
