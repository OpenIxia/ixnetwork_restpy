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


class IxVmPort(Base):
    """Retrieves the list of ports from an IxVM card
    The IxVmPort class encapsulates a list of ixVmPort resources that are managed by the user.
    A list of resources can be retrieved from the server using the IxVmPort.find() method.
    The list can be managed by using the IxVmPort.add() and IxVmPort.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ixVmPort'
    _SDM_ATT_MAP = {
        'Interface': 'interface',
        'IpAddress': 'ipAddress',
        'MacAddress': 'macAddress',
        'Mtu': 'mtu',
        'Owner': 'owner',
        'PortId': 'portId',
        'PortName': 'portName',
        'PortState': 'portState',
        'PromiscMode': 'promiscMode',
    }

    def __init__(self, parent):
        super(IxVmPort, self).__init__(parent)

    @property
    def Interface(self):
        """
        Returns
        -------
        - str: Represents the interface name
        """
        return self._get_attribute(self._SDM_ATT_MAP['Interface'])
    @Interface.setter
    def Interface(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Interface'], value)

    @property
    def IpAddress(self):
        """
        Returns
        -------
        - str: Represents the IP address
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpAddress'])
    @IpAddress.setter
    def IpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpAddress'], value)

    @property
    def MacAddress(self):
        """
        Returns
        -------
        - str: Represents the MAC address
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacAddress'])
    @MacAddress.setter
    def MacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacAddress'], value)

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: Represents MTU
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mtu'], value)

    @property
    def Owner(self):
        """
        Returns
        -------
        - str: Represents the user owning the port
        """
        return self._get_attribute(self._SDM_ATT_MAP['Owner'])

    @property
    def PortId(self):
        """
        Returns
        -------
        - str: Represents a slot on the card
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortId'])
    @PortId.setter
    def PortId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortId'], value)

    @property
    def PortName(self):
        """
        Returns
        -------
        - str: Represents a port name
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortName'])
    @PortName.setter
    def PortName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortName'], value)

    @property
    def PortState(self):
        """
        Returns
        -------
        - str(invalidNIC | ixVmPortUnitialized | portLicenseNotFound | portNotAdded | portOK | portRemoved | portUnconnectedCard | portUnknownError): Represents the port State
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortState'])

    @property
    def PromiscMode(self):
        """
        Returns
        -------
        - bool: Represents the promiscuos Mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['PromiscMode'])
    @PromiscMode.setter
    def PromiscMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PromiscMode'], value)

    def update(self, Interface=None, IpAddress=None, MacAddress=None, Mtu=None, PortId=None, PortName=None, PromiscMode=None):
        """Updates ixVmPort resource on the server.

        Args
        ----
        - Interface (str): Represents the interface name
        - IpAddress (str): Represents the IP address
        - MacAddress (str): Represents the MAC address
        - Mtu (number): Represents MTU
        - PortId (str): Represents a slot on the card
        - PortName (str): Represents a port name
        - PromiscMode (bool): Represents the promiscuos Mode

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Interface=None, IpAddress=None, MacAddress=None, Mtu=None, PortId=None, PortName=None, PromiscMode=None):
        """Adds a new ixVmPort resource on the server and adds it to the container.

        Args
        ----
        - Interface (str): Represents the interface name
        - IpAddress (str): Represents the IP address
        - MacAddress (str): Represents the MAC address
        - Mtu (number): Represents MTU
        - PortId (str): Represents a slot on the card
        - PortName (str): Represents a port name
        - PromiscMode (bool): Represents the promiscuos Mode

        Returns
        -------
        - self: This instance with all currently retrieved ixVmPort resources using find and the newly added ixVmPort resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ixVmPort resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Interface=None, IpAddress=None, MacAddress=None, Mtu=None, Owner=None, PortId=None, PortName=None, PortState=None, PromiscMode=None):
        """Finds and retrieves ixVmPort resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ixVmPort resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ixVmPort resources from the server.

        Args
        ----
        - Interface (str): Represents the interface name
        - IpAddress (str): Represents the IP address
        - MacAddress (str): Represents the MAC address
        - Mtu (number): Represents MTU
        - Owner (str): Represents the user owning the port
        - PortId (str): Represents a slot on the card
        - PortName (str): Represents a port name
        - PortState (str(invalidNIC | ixVmPortUnitialized | portLicenseNotFound | portNotAdded | portOK | portRemoved | portUnconnectedCard | portUnknownError)): Represents the port State
        - PromiscMode (bool): Represents the promiscuos Mode

        Returns
        -------
        - self: This instance with matching ixVmPort resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ixVmPort data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ixVmPort resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
