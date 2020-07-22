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


class MacRanges(Base):
    """The macRanges object controls the configuration of trunk MAC ranges.
    The MacRanges class encapsulates a list of macRanges resources that are managed by the user.
    A list of resources can be retrieved from the server using the MacRanges.find() method.
    The list can be managed by using the MacRanges.add() and MacRanges.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'macRanges'
    _SDM_ATT_MAP = {
        'CVlanId': 'cVlanId',
        'CVlanPriority': 'cVlanPriority',
        'CVlanTpId': 'cVlanTpId',
        'Count': 'count',
        'EnableVlan': 'enableVlan',
        'Enabled': 'enabled',
        'ITagethernetType': 'iTagethernetType',
        'ITagiSid': 'iTagiSid',
        'SVlanId': 'sVlanId',
        'SVlanPriority': 'sVlanPriority',
        'SVlanTpId': 'sVlanTpId',
        'StartMacAddress': 'startMacAddress',
        'Step': 'step',
        'TrafficGroupId': 'trafficGroupId',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(MacRanges, self).__init__(parent)

    @property
    def CVlanId(self):
        """
        Returns
        -------
        - number: The identifier for the C-VLAN for the MAC range. A unique,12-bit VLAN Identifier which specifies the C-VLAN with which this frame is associated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlanId'])
    @CVlanId.setter
    def CVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CVlanId'], value)

    @property
    def CVlanPriority(self):
        """
        Returns
        -------
        - number: The user priority of the tag: a value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlanPriority'])
    @CVlanPriority.setter
    def CVlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CVlanPriority'], value)

    @property
    def CVlanTpId(self):
        """
        Returns
        -------
        - str: The Tag Protocol ID. EtherTypes identify the protocol that follows the VLAN header. Select from a list of hex options: 0x8100, 0x9100, 0x9200, 0x88A8.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlanTpId'])
    @CVlanTpId.setter
    def CVlanTpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CVlanTpId'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The number of times to increment in this MAC range, starting with the address set in macAddress.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def EnableVlan(self):
        """
        Returns
        -------
        - bool: If true, the VLAN assigned to the MAC range is enabled.
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
        - bool: If true, the MAC range is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def ITagethernetType(self):
        """
        Returns
        -------
        - str: (Read-only) The I-Tag Ethernet type for the MAC range. An I-Tag is amultiplexing tag for service instance scaling in Provider Bridged Networks. This value is set to 0x88E7.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ITagethernetType'])

    @property
    def ITagiSid(self):
        """
        Returns
        -------
        - number: The I-Tag service instance identifier, and is a 3 octet field. The default is 0. Min:0 Max: 16777215
        """
        return self._get_attribute(self._SDM_ATT_MAP['ITagiSid'])
    @ITagiSid.setter
    def ITagiSid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ITagiSid'], value)

    @property
    def SVlanId(self):
        """
        Returns
        -------
        - number: A unique, 12-bit VLAN Identifier which specifies the VLAN with which this frame is associated. Default = 1 Min: 1 Max: 4095
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlanId'])
    @SVlanId.setter
    def SVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SVlanId'], value)

    @property
    def SVlanPriority(self):
        """
        Returns
        -------
        - number: The user priority of the tag: a value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlanPriority'])
    @SVlanPriority.setter
    def SVlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SVlanPriority'], value)

    @property
    def SVlanTpId(self):
        """
        Returns
        -------
        - str: The Tag Protocol ID. EtherTypes identify the protocol that follows the VLAN header. Select from a list of hex options: 0x8100, 0x9100, 0x9200, 0x88A8.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlanTpId'])
    @SVlanTpId.setter
    def SVlanTpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SVlanTpId'], value)

    @property
    def StartMacAddress(self):
        """
        Returns
        -------
        - str: The MAC address of the first entry in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartMacAddress'])
    @StartMacAddress.setter
    def StartMacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartMacAddress'], value)

    @property
    def Step(self):
        """
        Returns
        -------
        - str: The amount to increment each MAC address in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Step'])
    @Step.setter
    def Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Step'], value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): Assigns a traffic group to the MAC range. The traffic group must be previously configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(singleVlan | stackedVlan): Selects the VLAN type, either single or stacked. Stacked VLANS have an inner and outer value. Default = single.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    def update(self, CVlanId=None, CVlanPriority=None, CVlanTpId=None, Count=None, EnableVlan=None, Enabled=None, ITagiSid=None, SVlanId=None, SVlanPriority=None, SVlanTpId=None, StartMacAddress=None, Step=None, TrafficGroupId=None, Type=None):
        """Updates macRanges resource on the server.

        Args
        ----
        - CVlanId (number): The identifier for the C-VLAN for the MAC range. A unique,12-bit VLAN Identifier which specifies the C-VLAN with which this frame is associated.
        - CVlanPriority (number): The user priority of the tag: a value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.
        - CVlanTpId (str): The Tag Protocol ID. EtherTypes identify the protocol that follows the VLAN header. Select from a list of hex options: 0x8100, 0x9100, 0x9200, 0x88A8.
        - Count (number): The number of times to increment in this MAC range, starting with the address set in macAddress.
        - EnableVlan (bool): If true, the VLAN assigned to the MAC range is enabled.
        - Enabled (bool): If true, the MAC range is enabled.
        - ITagiSid (number): The I-Tag service instance identifier, and is a 3 octet field. The default is 0. Min:0 Max: 16777215
        - SVlanId (number): A unique, 12-bit VLAN Identifier which specifies the VLAN with which this frame is associated. Default = 1 Min: 1 Max: 4095
        - SVlanPriority (number): The user priority of the tag: a value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.
        - SVlanTpId (str): The Tag Protocol ID. EtherTypes identify the protocol that follows the VLAN header. Select from a list of hex options: 0x8100, 0x9100, 0x9200, 0x88A8.
        - StartMacAddress (str): The MAC address of the first entry in the range.
        - Step (str): The amount to increment each MAC address in the range.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Assigns a traffic group to the MAC range. The traffic group must be previously configured.
        - Type (str(singleVlan | stackedVlan)): Selects the VLAN type, either single or stacked. Stacked VLANS have an inner and outer value. Default = single.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CVlanId=None, CVlanPriority=None, CVlanTpId=None, Count=None, EnableVlan=None, Enabled=None, ITagiSid=None, SVlanId=None, SVlanPriority=None, SVlanTpId=None, StartMacAddress=None, Step=None, TrafficGroupId=None, Type=None):
        """Adds a new macRanges resource on the server and adds it to the container.

        Args
        ----
        - CVlanId (number): The identifier for the C-VLAN for the MAC range. A unique,12-bit VLAN Identifier which specifies the C-VLAN with which this frame is associated.
        - CVlanPriority (number): The user priority of the tag: a value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.
        - CVlanTpId (str): The Tag Protocol ID. EtherTypes identify the protocol that follows the VLAN header. Select from a list of hex options: 0x8100, 0x9100, 0x9200, 0x88A8.
        - Count (number): The number of times to increment in this MAC range, starting with the address set in macAddress.
        - EnableVlan (bool): If true, the VLAN assigned to the MAC range is enabled.
        - Enabled (bool): If true, the MAC range is enabled.
        - ITagiSid (number): The I-Tag service instance identifier, and is a 3 octet field. The default is 0. Min:0 Max: 16777215
        - SVlanId (number): A unique, 12-bit VLAN Identifier which specifies the VLAN with which this frame is associated. Default = 1 Min: 1 Max: 4095
        - SVlanPriority (number): The user priority of the tag: a value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.
        - SVlanTpId (str): The Tag Protocol ID. EtherTypes identify the protocol that follows the VLAN header. Select from a list of hex options: 0x8100, 0x9100, 0x9200, 0x88A8.
        - StartMacAddress (str): The MAC address of the first entry in the range.
        - Step (str): The amount to increment each MAC address in the range.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Assigns a traffic group to the MAC range. The traffic group must be previously configured.
        - Type (str(singleVlan | stackedVlan)): Selects the VLAN type, either single or stacked. Stacked VLANS have an inner and outer value. Default = single.

        Returns
        -------
        - self: This instance with all currently retrieved macRanges resources using find and the newly added macRanges resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained macRanges resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CVlanId=None, CVlanPriority=None, CVlanTpId=None, Count=None, EnableVlan=None, Enabled=None, ITagethernetType=None, ITagiSid=None, SVlanId=None, SVlanPriority=None, SVlanTpId=None, StartMacAddress=None, Step=None, TrafficGroupId=None, Type=None):
        """Finds and retrieves macRanges resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve macRanges resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all macRanges resources from the server.

        Args
        ----
        - CVlanId (number): The identifier for the C-VLAN for the MAC range. A unique,12-bit VLAN Identifier which specifies the C-VLAN with which this frame is associated.
        - CVlanPriority (number): The user priority of the tag: a value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.
        - CVlanTpId (str): The Tag Protocol ID. EtherTypes identify the protocol that follows the VLAN header. Select from a list of hex options: 0x8100, 0x9100, 0x9200, 0x88A8.
        - Count (number): The number of times to increment in this MAC range, starting with the address set in macAddress.
        - EnableVlan (bool): If true, the VLAN assigned to the MAC range is enabled.
        - Enabled (bool): If true, the MAC range is enabled.
        - ITagethernetType (str): (Read-only) The I-Tag Ethernet type for the MAC range. An I-Tag is amultiplexing tag for service instance scaling in Provider Bridged Networks. This value is set to 0x88E7.
        - ITagiSid (number): The I-Tag service instance identifier, and is a 3 octet field. The default is 0. Min:0 Max: 16777215
        - SVlanId (number): A unique, 12-bit VLAN Identifier which specifies the VLAN with which this frame is associated. Default = 1 Min: 1 Max: 4095
        - SVlanPriority (number): The user priority of the tag: a value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.
        - SVlanTpId (str): The Tag Protocol ID. EtherTypes identify the protocol that follows the VLAN header. Select from a list of hex options: 0x8100, 0x9100, 0x9200, 0x88A8.
        - StartMacAddress (str): The MAC address of the first entry in the range.
        - Step (str): The amount to increment each MAC address in the range.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Assigns a traffic group to the MAC range. The traffic group must be previously configured.
        - Type (str(singleVlan | stackedVlan)): Selects the VLAN type, either single or stacked. Stacked VLANS have an inner and outer value. Default = single.

        Returns
        -------
        - self: This instance with matching macRanges resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of macRanges data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the macRanges resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
