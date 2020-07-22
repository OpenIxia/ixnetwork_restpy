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


class MacAddressRange(Base):
    """This object represents the MAC addresses for this L2 site.
    The MacAddressRange class encapsulates a list of macAddressRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the MacAddressRange.find() method.
    The list can be managed by using the MacAddressRange.add() and MacAddressRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'macAddressRange'
    _SDM_ATT_MAP = {
        'EnableVlan': 'enableVlan',
        'Enabled': 'enabled',
        'IncrementVlan': 'incrementVlan',
        'IncrementVlanMode': 'incrementVlanMode',
        'IncremetVlanMode': 'incremetVlanMode',
        'MacCount': 'macCount',
        'MacCountPerL2Site': 'macCountPerL2Site',
        'MacIncrement': 'macIncrement',
        'SkipVlanIdZero': 'skipVlanIdZero',
        'StartMacAddress': 'startMacAddress',
        'TotalMacCount': 'totalMacCount',
        'Tpid': 'tpid',
        'VlanCount': 'vlanCount',
        'VlanId': 'vlanId',
        'VlanPriority': 'vlanPriority',
    }

    def __init__(self, parent):
        super(MacAddressRange, self).__init__(parent)

    @property
    def EnableVlan(self):
        """
        Returns
        -------
        - bool: If enabled, VLANs will be created and associated with the MAC addresses. The default is disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVlan'])
    @EnableVlan.setter
    def EnableVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVlan'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the MAC address range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IncrementVlan(self):
        """
        Returns
        -------
        - bool: If enabled, each additional VLAN in the range will be incremented to create unique VLAN IDs. The increment value is 1. The default is disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementVlan'])
    @IncrementVlan.setter
    def IncrementVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementVlan'], value)

    @property
    def IncrementVlanMode(self):
        """
        Returns
        -------
        - str(noIncrement | parallelIncrement | innerFirst | outerFirst): If enabled, each additional VLAN in the range is incremented to create unique VLAN IDs. The increment value is 1. The default is disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementVlanMode'])
    @IncrementVlanMode.setter
    def IncrementVlanMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementVlanMode'], value)

    @property
    def IncremetVlanMode(self):
        """DEPRECATED 
        Returns
        -------
        - str(noIncrement | parallelIncrement | innerFirst | outerFirst): If enabled, each additional VLAN in the range is incremented to create unique VLAN IDs. The increment value is 1. The default is disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncremetVlanMode'])
    @IncremetVlanMode.setter
    def IncremetVlanMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncremetVlanMode'], value)

    @property
    def MacCount(self):
        """DEPRECATED 
        Returns
        -------
        - number: The number of MAC addresses to be created for this range. A 4-byte unsigned integer. The default is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacCount'])
    @MacCount.setter
    def MacCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacCount'], value)

    @property
    def MacCountPerL2Site(self):
        """
        Returns
        -------
        - number: Signifies the count of MAC values per L2 site
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacCountPerL2Site'])
    @MacCountPerL2Site.setter
    def MacCountPerL2Site(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacCountPerL2Site'], value)

    @property
    def MacIncrement(self):
        """
        Returns
        -------
        - bool: If enabled, each additional MAC Address in this range of addresses will be incremented by 00 00 00 00 00 01.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacIncrement'])
    @MacIncrement.setter
    def MacIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacIncrement'], value)

    @property
    def SkipVlanIdZero(self):
        """
        Returns
        -------
        - bool: If enabled, the VLAN ID with zero value will be ignored.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SkipVlanIdZero'])
    @SkipVlanIdZero.setter
    def SkipVlanIdZero(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SkipVlanIdZero'], value)

    @property
    def StartMacAddress(self):
        """
        Returns
        -------
        - str: The first 6-byte MAC address in the range of MAC addresses. The default is 00 00 00 00 00 00.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartMacAddress'])
    @StartMacAddress.setter
    def StartMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartMacAddress'], value)

    @property
    def TotalMacCount(self):
        """
        Returns
        -------
        - number: Signifies the total MAC count
        """
        return self._get_attribute(self._SDM_ATT_MAP['TotalMacCount'])

    @property
    def Tpid(self):
        """
        Returns
        -------
        - str: Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag).The dropdown list contains the available TPIDs. Choose one of: 0x8100 (the default), 0x88a8, 0x9100, 0x9200.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tpid'])
    @Tpid.setter
    def Tpid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Tpid'], value)

    @property
    def VlanCount(self):
        """
        Returns
        -------
        - number: The number of VLANs created.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanCount'])
    @VlanCount.setter
    def VlanCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanCount'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - str: The ID for the first VLAN in a range of VLANs. An 2-byte unsigned integer. The valid range is 0 to 4095. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - str: The User Priority for this VLAN. A value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    def update(self, EnableVlan=None, Enabled=None, IncrementVlan=None, IncrementVlanMode=None, IncremetVlanMode=None, MacCount=None, MacCountPerL2Site=None, MacIncrement=None, SkipVlanIdZero=None, StartMacAddress=None, Tpid=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Updates macAddressRange resource on the server.

        Args
        ----
        - EnableVlan (bool): If enabled, VLANs will be created and associated with the MAC addresses. The default is disabled.
        - Enabled (bool): Enables the MAC address range.
        - IncrementVlan (bool): If enabled, each additional VLAN in the range will be incremented to create unique VLAN IDs. The increment value is 1. The default is disabled.
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If enabled, each additional VLAN in the range is incremented to create unique VLAN IDs. The increment value is 1. The default is disabled.
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If enabled, each additional VLAN in the range is incremented to create unique VLAN IDs. The increment value is 1. The default is disabled.
        - MacCount (number): The number of MAC addresses to be created for this range. A 4-byte unsigned integer. The default is 1.
        - MacCountPerL2Site (number): Signifies the count of MAC values per L2 site
        - MacIncrement (bool): If enabled, each additional MAC Address in this range of addresses will be incremented by 00 00 00 00 00 01.
        - SkipVlanIdZero (bool): If enabled, the VLAN ID with zero value will be ignored.
        - StartMacAddress (str): The first 6-byte MAC address in the range of MAC addresses. The default is 00 00 00 00 00 00.
        - Tpid (str): Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag).The dropdown list contains the available TPIDs. Choose one of: 0x8100 (the default), 0x88a8, 0x9100, 0x9200.
        - VlanCount (number): The number of VLANs created.
        - VlanId (str): The ID for the first VLAN in a range of VLANs. An 2-byte unsigned integer. The valid range is 0 to 4095. The default is 0.
        - VlanPriority (str): The User Priority for this VLAN. A value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableVlan=None, Enabled=None, IncrementVlan=None, IncrementVlanMode=None, IncremetVlanMode=None, MacCount=None, MacCountPerL2Site=None, MacIncrement=None, SkipVlanIdZero=None, StartMacAddress=None, Tpid=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Adds a new macAddressRange resource on the server and adds it to the container.

        Args
        ----
        - EnableVlan (bool): If enabled, VLANs will be created and associated with the MAC addresses. The default is disabled.
        - Enabled (bool): Enables the MAC address range.
        - IncrementVlan (bool): If enabled, each additional VLAN in the range will be incremented to create unique VLAN IDs. The increment value is 1. The default is disabled.
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If enabled, each additional VLAN in the range is incremented to create unique VLAN IDs. The increment value is 1. The default is disabled.
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If enabled, each additional VLAN in the range is incremented to create unique VLAN IDs. The increment value is 1. The default is disabled.
        - MacCount (number): The number of MAC addresses to be created for this range. A 4-byte unsigned integer. The default is 1.
        - MacCountPerL2Site (number): Signifies the count of MAC values per L2 site
        - MacIncrement (bool): If enabled, each additional MAC Address in this range of addresses will be incremented by 00 00 00 00 00 01.
        - SkipVlanIdZero (bool): If enabled, the VLAN ID with zero value will be ignored.
        - StartMacAddress (str): The first 6-byte MAC address in the range of MAC addresses. The default is 00 00 00 00 00 00.
        - Tpid (str): Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag).The dropdown list contains the available TPIDs. Choose one of: 0x8100 (the default), 0x88a8, 0x9100, 0x9200.
        - VlanCount (number): The number of VLANs created.
        - VlanId (str): The ID for the first VLAN in a range of VLANs. An 2-byte unsigned integer. The valid range is 0 to 4095. The default is 0.
        - VlanPriority (str): The User Priority for this VLAN. A value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.

        Returns
        -------
        - self: This instance with all currently retrieved macAddressRange resources using find and the newly added macAddressRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained macAddressRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableVlan=None, Enabled=None, IncrementVlan=None, IncrementVlanMode=None, IncremetVlanMode=None, MacCount=None, MacCountPerL2Site=None, MacIncrement=None, SkipVlanIdZero=None, StartMacAddress=None, TotalMacCount=None, Tpid=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves macAddressRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve macAddressRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all macAddressRange resources from the server.

        Args
        ----
        - EnableVlan (bool): If enabled, VLANs will be created and associated with the MAC addresses. The default is disabled.
        - Enabled (bool): Enables the MAC address range.
        - IncrementVlan (bool): If enabled, each additional VLAN in the range will be incremented to create unique VLAN IDs. The increment value is 1. The default is disabled.
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If enabled, each additional VLAN in the range is incremented to create unique VLAN IDs. The increment value is 1. The default is disabled.
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If enabled, each additional VLAN in the range is incremented to create unique VLAN IDs. The increment value is 1. The default is disabled.
        - MacCount (number): The number of MAC addresses to be created for this range. A 4-byte unsigned integer. The default is 1.
        - MacCountPerL2Site (number): Signifies the count of MAC values per L2 site
        - MacIncrement (bool): If enabled, each additional MAC Address in this range of addresses will be incremented by 00 00 00 00 00 01.
        - SkipVlanIdZero (bool): If enabled, the VLAN ID with zero value will be ignored.
        - StartMacAddress (str): The first 6-byte MAC address in the range of MAC addresses. The default is 00 00 00 00 00 00.
        - TotalMacCount (number): Signifies the total MAC count
        - Tpid (str): Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag).The dropdown list contains the available TPIDs. Choose one of: 0x8100 (the default), 0x88a8, 0x9100, 0x9200.
        - VlanCount (number): The number of VLANs created.
        - VlanId (str): The ID for the first VLAN in a range of VLANs. An 2-byte unsigned integer. The valid range is 0 to 4095. The default is 0.
        - VlanPriority (str): The User Priority for this VLAN. A value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.

        Returns
        -------
        - self: This instance with matching macAddressRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of macAddressRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the macAddressRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
