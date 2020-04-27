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


class Lan(Base):
    """This object holds the list  of statically-configured LANs for the port.
    The Lan class encapsulates a list of lan resources that are managed by the user.
    A list of resources can be retrieved from the server using the Lan.find() method.
    The list can be managed by using the Lan.add() and Lan.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'lan'

    def __init__(self, parent):
        super(Lan, self).__init__(parent)

    @property
    def AtmEncapsulation(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../atm): Select the ATM VPI/VCI Name from the list configured in the atm object.
        """
        return self._get_attribute('atmEncapsulation')
    @AtmEncapsulation.setter
    def AtmEncapsulation(self, value):
        self._set_attribute('atmEncapsulation', value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: If the VLAN is enabled, then this is the number of MAC address/VLAN combinations that will be created.
        """
        return self._get_attribute('count')
    @Count.setter
    def Count(self, value):
        self._set_attribute('count', value)

    @property
    def CountPerVc(self):
        """
        Returns
        -------
        - number: The total count per VC in this bundled mode.
        """
        return self._get_attribute('countPerVc')
    @CountPerVc.setter
    def CountPerVc(self, value):
        self._set_attribute('countPerVc', value)

    @property
    def EnableIncrementMac(self):
        """
        Returns
        -------
        - bool: Enables the use of multiple MAC addresses, which are incremented for each additional address. The default increment is 00 00 00 00 00 01.
        """
        return self._get_attribute('enableIncrementMac')
    @EnableIncrementMac.setter
    def EnableIncrementMac(self, value):
        self._set_attribute('enableIncrementMac', value)

    @property
    def EnableIncrementVlan(self):
        """
        Returns
        -------
        - bool: Enables the use of multiple VLANs, which are incremented for each additional VLAN. The default increment is 1.
        """
        return self._get_attribute('enableIncrementVlan')
    @EnableIncrementVlan.setter
    def EnableIncrementVlan(self, value):
        self._set_attribute('enableIncrementVlan', value)

    @property
    def EnableSiteId(self):
        """
        Returns
        -------
        - bool: Enables this site identifier (ID).
        """
        return self._get_attribute('enableSiteId')
    @EnableSiteId.setter
    def EnableSiteId(self, value):
        self._set_attribute('enableSiteId', value)

    @property
    def EnableVlan(self):
        """
        Returns
        -------
        - bool: Enables the use of VLANs.
        """
        return self._get_attribute('enableVlan')
    @EnableVlan.setter
    def EnableVlan(self, value):
        self._set_attribute('enableVlan', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables this LAN entry.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def FrEncapsulation(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../fr): Selects the Frame Relay encapsulation for the LAN based on the configuration of the fr object.
        """
        return self._get_attribute('frEncapsulation')
    @FrEncapsulation.setter
    def FrEncapsulation(self, value):
        self._set_attribute('frEncapsulation', value)

    @property
    def IncrementPerVcVlanMode(self):
        """
        Returns
        -------
        - str(noIncrement | parallelIncrement | innerFirst | outerFirst): If true, enables the use of multiple VLANs, which are incremented for each additional VLAN per VC. The default increment is 1.
        """
        return self._get_attribute('incrementPerVcVlanMode')
    @IncrementPerVcVlanMode.setter
    def IncrementPerVcVlanMode(self, value):
        self._set_attribute('incrementPerVcVlanMode', value)

    @property
    def IncrementVlanMode(self):
        """
        Returns
        -------
        - str(noIncrement | parallelIncrement | innerFirst | outerFirst): If true, enables the use of multiple VLANs, which are incremented for each additional VLAN per VC. The default increment is 1.
        """
        return self._get_attribute('incrementVlanMode')
    @IncrementVlanMode.setter
    def IncrementVlanMode(self, value):
        self._set_attribute('incrementVlanMode', value)

    @property
    def IncremetVlanMode(self):
        """DEPRECATED 
        Returns
        -------
        - str(noIncrement | parallelIncrement | innerFirst | outerFirst): If true, enables the use of multiple VLANs, which are incremented for each additional VLAN per VC. The default increment is 1.
        """
        return self._get_attribute('incremetVlanMode')
    @IncremetVlanMode.setter
    def IncremetVlanMode(self, value):
        self._set_attribute('incremetVlanMode', value)

    @property
    def Mac(self):
        """
        Returns
        -------
        - str: The first MAC address in the range.
        """
        return self._get_attribute('mac')
    @Mac.setter
    def Mac(self, value):
        self._set_attribute('mac', value)

    @property
    def MacRangeMode(self):
        """
        Returns
        -------
        - str(normal | bundled): Indicates the available MAC range mode.
        """
        return self._get_attribute('macRangeMode')
    @MacRangeMode.setter
    def MacRangeMode(self, value):
        self._set_attribute('macRangeMode', value)

    @property
    def NumberOfVcs(self):
        """
        Returns
        -------
        - number: The total number of VCs in this mode.
        """
        return self._get_attribute('numberOfVcs')
    @NumberOfVcs.setter
    def NumberOfVcs(self, value):
        self._set_attribute('numberOfVcs', value)

    @property
    def SiteId(self):
        """
        Returns
        -------
        - number: The value of the site identifier (ID). The valid range is 0 to 4,294,967,295. The default is 0.
        """
        return self._get_attribute('siteId')
    @SiteId.setter
    def SiteId(self, value):
        self._set_attribute('siteId', value)

    @property
    def SkipVlanIdZero(self):
        """
        Returns
        -------
        - bool: Skip the value of vlad id, if the vlan id value is equal to zero.
        """
        return self._get_attribute('skipVlanIdZero')
    @SkipVlanIdZero.setter
    def SkipVlanIdZero(self, value):
        self._set_attribute('skipVlanIdZero', value)

    @property
    def Tpid(self):
        """
        Returns
        -------
        - str: Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag).The dropdown list contains the available TPIDs. Choose one of: 0x8100 (the default), 0x88a8, 0x9100, 0x9200.
        """
        return self._get_attribute('tpid')
    @Tpid.setter
    def Tpid(self, value):
        self._set_attribute('tpid', value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute('trafficGroupId')
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute('trafficGroupId', value)

    @property
    def VlanCount(self):
        """
        Returns
        -------
        - number: The number of VLANs created.
        """
        return self._get_attribute('vlanCount')
    @VlanCount.setter
    def VlanCount(self, value):
        self._set_attribute('vlanCount', value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - str: The identifier for the first VLAN in the range.
        """
        return self._get_attribute('vlanId')
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute('vlanId', value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - str: The User Priority for this VLAN. A value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.
        """
        return self._get_attribute('vlanPriority')
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute('vlanPriority', value)

    def update(self, AtmEncapsulation=None, Count=None, CountPerVc=None, EnableIncrementMac=None, EnableIncrementVlan=None, EnableSiteId=None, EnableVlan=None, Enabled=None, FrEncapsulation=None, IncrementPerVcVlanMode=None, IncrementVlanMode=None, IncremetVlanMode=None, Mac=None, MacRangeMode=None, NumberOfVcs=None, SiteId=None, SkipVlanIdZero=None, Tpid=None, TrafficGroupId=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Updates lan resource on the server.

        Args
        ----
        - AtmEncapsulation (str(None | /api/v1/sessions/1/ixnetwork/vport/.../atm)): Select the ATM VPI/VCI Name from the list configured in the atm object.
        - Count (number): If the VLAN is enabled, then this is the number of MAC address/VLAN combinations that will be created.
        - CountPerVc (number): The total count per VC in this bundled mode.
        - EnableIncrementMac (bool): Enables the use of multiple MAC addresses, which are incremented for each additional address. The default increment is 00 00 00 00 00 01.
        - EnableIncrementVlan (bool): Enables the use of multiple VLANs, which are incremented for each additional VLAN. The default increment is 1.
        - EnableSiteId (bool): Enables this site identifier (ID).
        - EnableVlan (bool): Enables the use of VLANs.
        - Enabled (bool): Enables this LAN entry.
        - FrEncapsulation (str(None | /api/v1/sessions/1/ixnetwork/vport/.../fr)): Selects the Frame Relay encapsulation for the LAN based on the configuration of the fr object.
        - IncrementPerVcVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, enables the use of multiple VLANs, which are incremented for each additional VLAN per VC. The default increment is 1.
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, enables the use of multiple VLANs, which are incremented for each additional VLAN per VC. The default increment is 1.
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, enables the use of multiple VLANs, which are incremented for each additional VLAN per VC. The default increment is 1.
        - Mac (str): The first MAC address in the range.
        - MacRangeMode (str(normal | bundled)): Indicates the available MAC range mode.
        - NumberOfVcs (number): The total number of VCs in this mode.
        - SiteId (number): The value of the site identifier (ID). The valid range is 0 to 4,294,967,295. The default is 0.
        - SkipVlanIdZero (bool): Skip the value of vlad id, if the vlan id value is equal to zero.
        - Tpid (str): Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag).The dropdown list contains the available TPIDs. Choose one of: 0x8100 (the default), 0x88a8, 0x9100, 0x9200.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - VlanCount (number): The number of VLANs created.
        - VlanId (str): The identifier for the first VLAN in the range.
        - VlanPriority (str): The User Priority for this VLAN. A value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, AtmEncapsulation=None, Count=None, CountPerVc=None, EnableIncrementMac=None, EnableIncrementVlan=None, EnableSiteId=None, EnableVlan=None, Enabled=None, FrEncapsulation=None, IncrementPerVcVlanMode=None, IncrementVlanMode=None, IncremetVlanMode=None, Mac=None, MacRangeMode=None, NumberOfVcs=None, SiteId=None, SkipVlanIdZero=None, Tpid=None, TrafficGroupId=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Adds a new lan resource on the server and adds it to the container.

        Args
        ----
        - AtmEncapsulation (str(None | /api/v1/sessions/1/ixnetwork/vport/.../atm)): Select the ATM VPI/VCI Name from the list configured in the atm object.
        - Count (number): If the VLAN is enabled, then this is the number of MAC address/VLAN combinations that will be created.
        - CountPerVc (number): The total count per VC in this bundled mode.
        - EnableIncrementMac (bool): Enables the use of multiple MAC addresses, which are incremented for each additional address. The default increment is 00 00 00 00 00 01.
        - EnableIncrementVlan (bool): Enables the use of multiple VLANs, which are incremented for each additional VLAN. The default increment is 1.
        - EnableSiteId (bool): Enables this site identifier (ID).
        - EnableVlan (bool): Enables the use of VLANs.
        - Enabled (bool): Enables this LAN entry.
        - FrEncapsulation (str(None | /api/v1/sessions/1/ixnetwork/vport/.../fr)): Selects the Frame Relay encapsulation for the LAN based on the configuration of the fr object.
        - IncrementPerVcVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, enables the use of multiple VLANs, which are incremented for each additional VLAN per VC. The default increment is 1.
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, enables the use of multiple VLANs, which are incremented for each additional VLAN per VC. The default increment is 1.
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, enables the use of multiple VLANs, which are incremented for each additional VLAN per VC. The default increment is 1.
        - Mac (str): The first MAC address in the range.
        - MacRangeMode (str(normal | bundled)): Indicates the available MAC range mode.
        - NumberOfVcs (number): The total number of VCs in this mode.
        - SiteId (number): The value of the site identifier (ID). The valid range is 0 to 4,294,967,295. The default is 0.
        - SkipVlanIdZero (bool): Skip the value of vlad id, if the vlan id value is equal to zero.
        - Tpid (str): Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag).The dropdown list contains the available TPIDs. Choose one of: 0x8100 (the default), 0x88a8, 0x9100, 0x9200.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - VlanCount (number): The number of VLANs created.
        - VlanId (str): The identifier for the first VLAN in the range.
        - VlanPriority (str): The User Priority for this VLAN. A value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.

        Returns
        -------
        - self: This instance with all currently retrieved lan resources using find and the newly added lan resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained lan resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AtmEncapsulation=None, Count=None, CountPerVc=None, EnableIncrementMac=None, EnableIncrementVlan=None, EnableSiteId=None, EnableVlan=None, Enabled=None, FrEncapsulation=None, IncrementPerVcVlanMode=None, IncrementVlanMode=None, IncremetVlanMode=None, Mac=None, MacRangeMode=None, NumberOfVcs=None, SiteId=None, SkipVlanIdZero=None, Tpid=None, TrafficGroupId=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves lan resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lan resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lan resources from the server.

        Args
        ----
        - AtmEncapsulation (str(None | /api/v1/sessions/1/ixnetwork/vport/.../atm)): Select the ATM VPI/VCI Name from the list configured in the atm object.
        - Count (number): If the VLAN is enabled, then this is the number of MAC address/VLAN combinations that will be created.
        - CountPerVc (number): The total count per VC in this bundled mode.
        - EnableIncrementMac (bool): Enables the use of multiple MAC addresses, which are incremented for each additional address. The default increment is 00 00 00 00 00 01.
        - EnableIncrementVlan (bool): Enables the use of multiple VLANs, which are incremented for each additional VLAN. The default increment is 1.
        - EnableSiteId (bool): Enables this site identifier (ID).
        - EnableVlan (bool): Enables the use of VLANs.
        - Enabled (bool): Enables this LAN entry.
        - FrEncapsulation (str(None | /api/v1/sessions/1/ixnetwork/vport/.../fr)): Selects the Frame Relay encapsulation for the LAN based on the configuration of the fr object.
        - IncrementPerVcVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, enables the use of multiple VLANs, which are incremented for each additional VLAN per VC. The default increment is 1.
        - IncrementVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, enables the use of multiple VLANs, which are incremented for each additional VLAN per VC. The default increment is 1.
        - IncremetVlanMode (str(noIncrement | parallelIncrement | innerFirst | outerFirst)): If true, enables the use of multiple VLANs, which are incremented for each additional VLAN per VC. The default increment is 1.
        - Mac (str): The first MAC address in the range.
        - MacRangeMode (str(normal | bundled)): Indicates the available MAC range mode.
        - NumberOfVcs (number): The total number of VCs in this mode.
        - SiteId (number): The value of the site identifier (ID). The valid range is 0 to 4,294,967,295. The default is 0.
        - SkipVlanIdZero (bool): Skip the value of vlad id, if the vlan id value is equal to zero.
        - Tpid (str): Tag Protocol Identifier / TPID (hex). The EtherType that identifies the protocol header that follows the VLAN header (tag).The dropdown list contains the available TPIDs. Choose one of: 0x8100 (the default), 0x88a8, 0x9100, 0x9200.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - VlanCount (number): The number of VLANs created.
        - VlanId (str): The identifier for the first VLAN in the range.
        - VlanPriority (str): The User Priority for this VLAN. A value from 0 through 7. The use and interpretation of this field is defined in ISO/IEC 15802-3.

        Returns
        -------
        - self: This instance with matching lan resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of lan data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lan resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
