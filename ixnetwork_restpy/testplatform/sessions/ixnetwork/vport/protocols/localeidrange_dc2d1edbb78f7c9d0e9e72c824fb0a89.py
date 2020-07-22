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


class LocalEidRange(Base):
    """It gives details about the local Eid range
    The LocalEidRange class encapsulates a list of localEidRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the LocalEidRange.find() method.
    The list can be managed by using the LocalEidRange.add() and LocalEidRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'localEidRange'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'EnableProxyMapReplyBit': 'enableProxyMapReplyBit',
        'EnableWantMapNotifyBit': 'enableWantMapNotifyBit',
        'Enabled': 'enabled',
        'Family': 'family',
        'MaxRecordPerMapRegisterPacket': 'maxRecordPerMapRegisterPacket',
        'PeriodicRefreshInterval': 'periodicRefreshInterval',
        'PrefixLength': 'prefixLength',
        'QuickRegistrationPeriod': 'quickRegistrationPeriod',
        'RefreshIntervalInQuickRegistrationPeriod': 'refreshIntervalInQuickRegistrationPeriod',
        'StartAddress': 'startAddress',
        'SupportSmrGeneration': 'supportSmrGeneration',
        'Ttl': 'ttl',
        'UseAllInterfaceAddressesAsLocator': 'useAllInterfaceAddressesAsLocator',
    }

    def __init__(self, parent):
        super(LocalEidRange, self).__init__(parent)

    @property
    def Locator(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.locator_f1fe3315f725c10b55c405019beb788b.Locator): An instance of the Locator class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.locator_f1fe3315f725c10b55c405019beb788b import Locator
        return Locator(self)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: It gives details about the count
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def EnableProxyMapReplyBit(self):
        """
        Returns
        -------
        - bool: If true, it enables the proxy map reply bit
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableProxyMapReplyBit'])
    @EnableProxyMapReplyBit.setter
    def EnableProxyMapReplyBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableProxyMapReplyBit'], value)

    @property
    def EnableWantMapNotifyBit(self):
        """
        Returns
        -------
        - str(always | duringQuickRegistration | never): If true, it enables the Want map Notify bit
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableWantMapNotifyBit'])
    @EnableWantMapNotifyBit.setter
    def EnableWantMapNotifyBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableWantMapNotifyBit'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, it enables the protocol
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Family(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): It gives details about the family
        """
        return self._get_attribute(self._SDM_ATT_MAP['Family'])
    @Family.setter
    def Family(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Family'], value)

    @property
    def MaxRecordPerMapRegisterPacket(self):
        """
        Returns
        -------
        - number: It gives details about the maximum record per map register packet
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRecordPerMapRegisterPacket'])
    @MaxRecordPerMapRegisterPacket.setter
    def MaxRecordPerMapRegisterPacket(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRecordPerMapRegisterPacket'], value)

    @property
    def PeriodicRefreshInterval(self):
        """
        Returns
        -------
        - number: It gives details about the periodic refresh interval
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeriodicRefreshInterval'])
    @PeriodicRefreshInterval.setter
    def PeriodicRefreshInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeriodicRefreshInterval'], value)

    @property
    def PrefixLength(self):
        """
        Returns
        -------
        - number: it gives details about the prefix length
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrefixLength'])
    @PrefixLength.setter
    def PrefixLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PrefixLength'], value)

    @property
    def QuickRegistrationPeriod(self):
        """
        Returns
        -------
        - number: it gives details about the quick registration period
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuickRegistrationPeriod'])
    @QuickRegistrationPeriod.setter
    def QuickRegistrationPeriod(self, value):
        self._set_attribute(self._SDM_ATT_MAP['QuickRegistrationPeriod'], value)

    @property
    def RefreshIntervalInQuickRegistrationPeriod(self):
        """
        Returns
        -------
        - number: It refreshs the interval in quick registration periods
        """
        return self._get_attribute(self._SDM_ATT_MAP['RefreshIntervalInQuickRegistrationPeriod'])
    @RefreshIntervalInQuickRegistrationPeriod.setter
    def RefreshIntervalInQuickRegistrationPeriod(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RefreshIntervalInQuickRegistrationPeriod'], value)

    @property
    def StartAddress(self):
        """
        Returns
        -------
        - str: It gives details about the start address
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartAddress'])
    @StartAddress.setter
    def StartAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartAddress'], value)

    @property
    def SupportSmrGeneration(self):
        """
        Returns
        -------
        - bool: It supports smr generation
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportSmrGeneration'])
    @SupportSmrGeneration.setter
    def SupportSmrGeneration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportSmrGeneration'], value)

    @property
    def Ttl(self):
        """
        Returns
        -------
        - number: It gives details about the ttl
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ttl'])
    @Ttl.setter
    def Ttl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ttl'], value)

    @property
    def UseAllInterfaceAddressesAsLocator(self):
        """
        Returns
        -------
        - bool: If True, it uses all interface address as locator
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseAllInterfaceAddressesAsLocator'])
    @UseAllInterfaceAddressesAsLocator.setter
    def UseAllInterfaceAddressesAsLocator(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseAllInterfaceAddressesAsLocator'], value)

    def update(self, Count=None, EnableProxyMapReplyBit=None, EnableWantMapNotifyBit=None, Enabled=None, Family=None, MaxRecordPerMapRegisterPacket=None, PeriodicRefreshInterval=None, PrefixLength=None, QuickRegistrationPeriod=None, RefreshIntervalInQuickRegistrationPeriod=None, StartAddress=None, SupportSmrGeneration=None, Ttl=None, UseAllInterfaceAddressesAsLocator=None):
        """Updates localEidRange resource on the server.

        Args
        ----
        - Count (number): It gives details about the count
        - EnableProxyMapReplyBit (bool): If true, it enables the proxy map reply bit
        - EnableWantMapNotifyBit (str(always | duringQuickRegistration | never)): If true, it enables the Want map Notify bit
        - Enabled (bool): If true, it enables the protocol
        - Family (str(ipv4 | ipv6)): It gives details about the family
        - MaxRecordPerMapRegisterPacket (number): It gives details about the maximum record per map register packet
        - PeriodicRefreshInterval (number): It gives details about the periodic refresh interval
        - PrefixLength (number): it gives details about the prefix length
        - QuickRegistrationPeriod (number): it gives details about the quick registration period
        - RefreshIntervalInQuickRegistrationPeriod (number): It refreshs the interval in quick registration periods
        - StartAddress (str): It gives details about the start address
        - SupportSmrGeneration (bool): It supports smr generation
        - Ttl (number): It gives details about the ttl
        - UseAllInterfaceAddressesAsLocator (bool): If True, it uses all interface address as locator

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Count=None, EnableProxyMapReplyBit=None, EnableWantMapNotifyBit=None, Enabled=None, Family=None, MaxRecordPerMapRegisterPacket=None, PeriodicRefreshInterval=None, PrefixLength=None, QuickRegistrationPeriod=None, RefreshIntervalInQuickRegistrationPeriod=None, StartAddress=None, SupportSmrGeneration=None, Ttl=None, UseAllInterfaceAddressesAsLocator=None):
        """Adds a new localEidRange resource on the server and adds it to the container.

        Args
        ----
        - Count (number): It gives details about the count
        - EnableProxyMapReplyBit (bool): If true, it enables the proxy map reply bit
        - EnableWantMapNotifyBit (str(always | duringQuickRegistration | never)): If true, it enables the Want map Notify bit
        - Enabled (bool): If true, it enables the protocol
        - Family (str(ipv4 | ipv6)): It gives details about the family
        - MaxRecordPerMapRegisterPacket (number): It gives details about the maximum record per map register packet
        - PeriodicRefreshInterval (number): It gives details about the periodic refresh interval
        - PrefixLength (number): it gives details about the prefix length
        - QuickRegistrationPeriod (number): it gives details about the quick registration period
        - RefreshIntervalInQuickRegistrationPeriod (number): It refreshs the interval in quick registration periods
        - StartAddress (str): It gives details about the start address
        - SupportSmrGeneration (bool): It supports smr generation
        - Ttl (number): It gives details about the ttl
        - UseAllInterfaceAddressesAsLocator (bool): If True, it uses all interface address as locator

        Returns
        -------
        - self: This instance with all currently retrieved localEidRange resources using find and the newly added localEidRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained localEidRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, EnableProxyMapReplyBit=None, EnableWantMapNotifyBit=None, Enabled=None, Family=None, MaxRecordPerMapRegisterPacket=None, PeriodicRefreshInterval=None, PrefixLength=None, QuickRegistrationPeriod=None, RefreshIntervalInQuickRegistrationPeriod=None, StartAddress=None, SupportSmrGeneration=None, Ttl=None, UseAllInterfaceAddressesAsLocator=None):
        """Finds and retrieves localEidRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve localEidRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all localEidRange resources from the server.

        Args
        ----
        - Count (number): It gives details about the count
        - EnableProxyMapReplyBit (bool): If true, it enables the proxy map reply bit
        - EnableWantMapNotifyBit (str(always | duringQuickRegistration | never)): If true, it enables the Want map Notify bit
        - Enabled (bool): If true, it enables the protocol
        - Family (str(ipv4 | ipv6)): It gives details about the family
        - MaxRecordPerMapRegisterPacket (number): It gives details about the maximum record per map register packet
        - PeriodicRefreshInterval (number): It gives details about the periodic refresh interval
        - PrefixLength (number): it gives details about the prefix length
        - QuickRegistrationPeriod (number): it gives details about the quick registration period
        - RefreshIntervalInQuickRegistrationPeriod (number): It refreshs the interval in quick registration periods
        - StartAddress (str): It gives details about the start address
        - SupportSmrGeneration (bool): It supports smr generation
        - Ttl (number): It gives details about the ttl
        - UseAllInterfaceAddressesAsLocator (bool): If True, it uses all interface address as locator

        Returns
        -------
        - self: This instance with matching localEidRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of localEidRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the localEidRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
