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


class GlobalEgtpApnS5S8(Base):
    """
    The GlobalEgtpApnS5S8 class encapsulates a list of globalEgtpApnS5S8 resources that is be managed by the user.
    A list of resources can be retrieved from the server using the GlobalEgtpApnS5S8.find() method.
    The list can be managed by the user by using the GlobalEgtpApnS5S8.add() and GlobalEgtpApnS5S8.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'globalEgtpApnS5S8'

    def __init__(self, parent):
        super(GlobalEgtpApnS5S8, self).__init__(parent)

    @property
    def AddressPoolStartIPv4(self):
        """Defines the base IPv4 address to be used for enumerating all the addresses in the range.

        Returns:
            str
        """
        return self._get_attribute('addressPoolStartIPv4')
    @AddressPoolStartIPv4.setter
    def AddressPoolStartIPv4(self, value):
        self._set_attribute('addressPoolStartIPv4', value)

    @property
    def AddressPoolStartIPv6(self):
        """Defines the base IPv6 address to be used for enumerating all the addresses in the range.

        Returns:
            str
        """
        return self._get_attribute('addressPoolStartIPv6')
    @AddressPoolStartIPv6.setter
    def AddressPoolStartIPv6(self, value):
        self._set_attribute('addressPoolStartIPv6', value)

    @property
    def AmbrDL(self):
        """Aggregated Maximum Bit Rate for down-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.

        Returns:
            number
        """
        return self._get_attribute('ambrDL')
    @AmbrDL.setter
    def AmbrDL(self, value):
        self._set_attribute('ambrDL', value)

    @property
    def AmbrUL(self):
        """Aggregated Maximum Bit Rate for up-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.

        Returns:
            number
        """
        return self._get_attribute('ambrUL')
    @AmbrUL.setter
    def AmbrUL(self, value):
        self._set_attribute('ambrUL', value)

    @property
    def ArpPreemptionCapability(self):
        """If true preemption capability is enabled

        Returns:
            bool
        """
        return self._get_attribute('arpPreemptionCapability')
    @ArpPreemptionCapability.setter
    def ArpPreemptionCapability(self, value):
        self._set_attribute('arpPreemptionCapability', value)

    @property
    def ArpPreemptionVulnerability(self):
        """If true preemption vulnerability is enabled

        Returns:
            bool
        """
        return self._get_attribute('arpPreemptionVulnerability')
    @ArpPreemptionVulnerability.setter
    def ArpPreemptionVulnerability(self, value):
        self._set_attribute('arpPreemptionVulnerability', value)

    @property
    def ArpPriorityLevel(self):
        """Priority Level 1=highest 15=lowest

        Returns:
            number
        """
        return self._get_attribute('arpPriorityLevel')
    @ArpPriorityLevel.setter
    def ArpPriorityLevel(self, value):
        self._set_attribute('arpPriorityLevel', value)

    @property
    def EnableLifetime(self):
        """Enable UE PDN connection lifetime control. The UE will disconnect from specified APN after the specified time.

        Returns:
            bool
        """
        return self._get_attribute('enableLifetime')
    @EnableLifetime.setter
    def EnableLifetime(self, value):
        self._set_attribute('enableLifetime', value)

    @property
    def EnablePgwDistribution(self):
        """Enable PGW Distribution of IPs on SGW

        Returns:
            bool
        """
        return self._get_attribute('enablePgwDistribution')
    @EnablePgwDistribution.setter
    def EnablePgwDistribution(self, value):
        self._set_attribute('enablePgwDistribution', value)

    @property
    def EnableStaticIpAllocation(self):
        """This enables the static ip allocation for the User Plane. The Create Session Request at initial attach in E-Utran shall have the PAA set to the values set here.

        Returns:
            bool
        """
        return self._get_attribute('enableStaticIpAllocation')
    @EnableStaticIpAllocation.setter
    def EnableStaticIpAllocation(self, value):
        self._set_attribute('enableStaticIpAllocation', value)

    @property
    def Enabled(self):
        """Disabled ranges won't be configured nor validated.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def IpType(self):
        """Defines the IP type to be used by the UE. IP type IPv4v6 is used for dual stack functionality.

        Returns:
            str
        """
        return self._get_attribute('ipType')
    @IpType.setter
    def IpType(self, value):
        self._set_attribute('ipType', value)

    @property
    def Lifetime(self):
        """Amount of time (in seconds) to wait after PDN attach procedure completes before scheduling forced detach.

        Returns:
            number
        """
        return self._get_attribute('lifetime')
    @Lifetime.setter
    def Lifetime(self, value):
        self._set_attribute('lifetime', value)

    @property
    def Mbrd(self):
        """Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.

        Returns:
            number
        """
        return self._get_attribute('mbrd')
    @Mbrd.setter
    def Mbrd(self, value):
        self._set_attribute('mbrd', value)

    @property
    def Mbru(self):
        """Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.

        Returns:
            number
        """
        return self._get_attribute('mbru')
    @Mbru.setter
    def Mbru(self, value):
        self._set_attribute('mbru', value)

    @property
    def Name(self):
        """APN name

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def PgwCount(self):
        """Defines the number of PGW addresses in the range.

        Returns:
            number
        """
        return self._get_attribute('pgwCount')
    @PgwCount.setter
    def PgwCount(self, value):
        self._set_attribute('pgwCount', value)

    @property
    def PgwIp(self):
        """PGW IP

        Returns:
            str
        """
        return self._get_attribute('pgwIp')
    @PgwIp.setter
    def PgwIp(self, value):
        self._set_attribute('pgwIp', value)

    @property
    def PgwIpCount(self):
        """

        Returns:
            number
        """
        return self._get_attribute('pgwIpCount')
    @PgwIpCount.setter
    def PgwIpCount(self, value):
        self._set_attribute('pgwIpCount', value)

    @property
    def Qci(self):
        """QoS Class Identifier

        Returns:
            number
        """
        return self._get_attribute('qci')
    @Qci.setter
    def Qci(self, value):
        self._set_attribute('qci', value)

    @property
    def Restriction(self):
        """Authorization to access another APN

        Returns:
            number
        """
        return self._get_attribute('restriction')
    @Restriction.setter
    def Restriction(self, value):
        self._set_attribute('restriction', value)

    @property
    def SelectionMode(self):
        """Indicates the origin of the APN in the message

        Returns:
            number
        """
        return self._get_attribute('selectionMode')
    @SelectionMode.setter
    def SelectionMode(self, value):
        self._set_attribute('selectionMode', value)

    @property
    def UpdateAmbrEnable(self):
        """Update APN-AMBR for this UE

        Returns:
            bool
        """
        return self._get_attribute('updateAmbrEnable')
    @UpdateAmbrEnable.setter
    def UpdateAmbrEnable(self, value):
        self._set_attribute('updateAmbrEnable', value)

    @property
    def UpdateAmbrIncrement(self):
        """Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.

        Returns:
            number
        """
        return self._get_attribute('updateAmbrIncrement')
    @UpdateAmbrIncrement.setter
    def UpdateAmbrIncrement(self, value):
        self._set_attribute('updateAmbrIncrement', value)

    @property
    def UpdateAmbrIterations(self):
        """How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates

        Returns:
            number
        """
        return self._get_attribute('updateAmbrIterations')
    @UpdateAmbrIterations.setter
    def UpdateAmbrIterations(self, value):
        self._set_attribute('updateAmbrIterations', value)

    @property
    def UpdateAmbrTimeout(self):
        """Time to wait (in seconds) since the session was created until sending the update

        Returns:
            number
        """
        return self._get_attribute('updateAmbrTimeout')
    @UpdateAmbrTimeout.setter
    def UpdateAmbrTimeout(self, value):
        self._set_attribute('updateAmbrTimeout', value)

    @property
    def UseFullApn(self):
        """Send the full APN in CreateSessionRequest by appending APN-OI to the APN name

        Returns:
            bool
        """
        return self._get_attribute('useFullApn')
    @UseFullApn.setter
    def UseFullApn(self, value):
        self._set_attribute('useFullApn', value)

    def update(self, AddressPoolStartIPv4=None, AddressPoolStartIPv6=None, AmbrDL=None, AmbrUL=None, ArpPreemptionCapability=None, ArpPreemptionVulnerability=None, ArpPriorityLevel=None, EnableLifetime=None, EnablePgwDistribution=None, EnableStaticIpAllocation=None, Enabled=None, IpType=None, Lifetime=None, Mbrd=None, Mbru=None, Name=None, PgwCount=None, PgwIp=None, PgwIpCount=None, Qci=None, Restriction=None, SelectionMode=None, UpdateAmbrEnable=None, UpdateAmbrIncrement=None, UpdateAmbrIterations=None, UpdateAmbrTimeout=None, UseFullApn=None):
        """Updates a child instance of globalEgtpApnS5S8 on the server.

        Args:
            AddressPoolStartIPv4 (str): Defines the base IPv4 address to be used for enumerating all the addresses in the range.
            AddressPoolStartIPv6 (str): Defines the base IPv6 address to be used for enumerating all the addresses in the range.
            AmbrDL (number): Aggregated Maximum Bit Rate for down-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
            AmbrUL (number): Aggregated Maximum Bit Rate for up-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
            ArpPreemptionCapability (bool): If true preemption capability is enabled
            ArpPreemptionVulnerability (bool): If true preemption vulnerability is enabled
            ArpPriorityLevel (number): Priority Level 1=highest 15=lowest
            EnableLifetime (bool): Enable UE PDN connection lifetime control. The UE will disconnect from specified APN after the specified time.
            EnablePgwDistribution (bool): Enable PGW Distribution of IPs on SGW
            EnableStaticIpAllocation (bool): This enables the static ip allocation for the User Plane. The Create Session Request at initial attach in E-Utran shall have the PAA set to the values set here.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IpType (str): Defines the IP type to be used by the UE. IP type IPv4v6 is used for dual stack functionality.
            Lifetime (number): Amount of time (in seconds) to wait after PDN attach procedure completes before scheduling forced detach.
            Mbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Mbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Name (str): APN name
            PgwCount (number): Defines the number of PGW addresses in the range.
            PgwIp (str): PGW IP
            PgwIpCount (number): 
            Qci (number): QoS Class Identifier
            Restriction (number): Authorization to access another APN
            SelectionMode (number): Indicates the origin of the APN in the message
            UpdateAmbrEnable (bool): Update APN-AMBR for this UE
            UpdateAmbrIncrement (number): Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
            UpdateAmbrIterations (number): How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
            UpdateAmbrTimeout (number): Time to wait (in seconds) since the session was created until sending the update
            UseFullApn (bool): Send the full APN in CreateSessionRequest by appending APN-OI to the APN name

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AddressPoolStartIPv4=None, AddressPoolStartIPv6=None, AmbrDL=None, AmbrUL=None, ArpPreemptionCapability=None, ArpPreemptionVulnerability=None, ArpPriorityLevel=None, EnableLifetime=None, EnablePgwDistribution=None, EnableStaticIpAllocation=None, Enabled=None, IpType=None, Lifetime=None, Mbrd=None, Mbru=None, Name=None, PgwCount=None, PgwIp=None, PgwIpCount=None, Qci=None, Restriction=None, SelectionMode=None, UpdateAmbrEnable=None, UpdateAmbrIncrement=None, UpdateAmbrIterations=None, UpdateAmbrTimeout=None, UseFullApn=None):
        """Adds a new globalEgtpApnS5S8 node on the server and retrieves it in this instance.

        Args:
            AddressPoolStartIPv4 (str): Defines the base IPv4 address to be used for enumerating all the addresses in the range.
            AddressPoolStartIPv6 (str): Defines the base IPv6 address to be used for enumerating all the addresses in the range.
            AmbrDL (number): Aggregated Maximum Bit Rate for down-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
            AmbrUL (number): Aggregated Maximum Bit Rate for up-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
            ArpPreemptionCapability (bool): If true preemption capability is enabled
            ArpPreemptionVulnerability (bool): If true preemption vulnerability is enabled
            ArpPriorityLevel (number): Priority Level 1=highest 15=lowest
            EnableLifetime (bool): Enable UE PDN connection lifetime control. The UE will disconnect from specified APN after the specified time.
            EnablePgwDistribution (bool): Enable PGW Distribution of IPs on SGW
            EnableStaticIpAllocation (bool): This enables the static ip allocation for the User Plane. The Create Session Request at initial attach in E-Utran shall have the PAA set to the values set here.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IpType (str): Defines the IP type to be used by the UE. IP type IPv4v6 is used for dual stack functionality.
            Lifetime (number): Amount of time (in seconds) to wait after PDN attach procedure completes before scheduling forced detach.
            Mbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Mbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Name (str): APN name
            PgwCount (number): Defines the number of PGW addresses in the range.
            PgwIp (str): PGW IP
            PgwIpCount (number): 
            Qci (number): QoS Class Identifier
            Restriction (number): Authorization to access another APN
            SelectionMode (number): Indicates the origin of the APN in the message
            UpdateAmbrEnable (bool): Update APN-AMBR for this UE
            UpdateAmbrIncrement (number): Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
            UpdateAmbrIterations (number): How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
            UpdateAmbrTimeout (number): Time to wait (in seconds) since the session was created until sending the update
            UseFullApn (bool): Send the full APN in CreateSessionRequest by appending APN-OI to the APN name

        Returns:
            self: This instance with all currently retrieved globalEgtpApnS5S8 data using find and the newly added globalEgtpApnS5S8 data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the globalEgtpApnS5S8 data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AddressPoolStartIPv4=None, AddressPoolStartIPv6=None, AmbrDL=None, AmbrUL=None, ArpPreemptionCapability=None, ArpPreemptionVulnerability=None, ArpPriorityLevel=None, EnableLifetime=None, EnablePgwDistribution=None, EnableStaticIpAllocation=None, Enabled=None, IpType=None, Lifetime=None, Mbrd=None, Mbru=None, Name=None, ObjectId=None, PgwCount=None, PgwIp=None, PgwIpCount=None, Qci=None, Restriction=None, SelectionMode=None, UpdateAmbrEnable=None, UpdateAmbrIncrement=None, UpdateAmbrIterations=None, UpdateAmbrTimeout=None, UseFullApn=None):
        """Finds and retrieves globalEgtpApnS5S8 data from the server.

        All named parameters support regex and can be used to selectively retrieve globalEgtpApnS5S8 data from the server.
        By default the find method takes no parameters and will retrieve all globalEgtpApnS5S8 data from the server.

        Args:
            AddressPoolStartIPv4 (str): Defines the base IPv4 address to be used for enumerating all the addresses in the range.
            AddressPoolStartIPv6 (str): Defines the base IPv6 address to be used for enumerating all the addresses in the range.
            AmbrDL (number): Aggregated Maximum Bit Rate for down-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
            AmbrUL (number): Aggregated Maximum Bit Rate for up-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
            ArpPreemptionCapability (bool): If true preemption capability is enabled
            ArpPreemptionVulnerability (bool): If true preemption vulnerability is enabled
            ArpPriorityLevel (number): Priority Level 1=highest 15=lowest
            EnableLifetime (bool): Enable UE PDN connection lifetime control. The UE will disconnect from specified APN after the specified time.
            EnablePgwDistribution (bool): Enable PGW Distribution of IPs on SGW
            EnableStaticIpAllocation (bool): This enables the static ip allocation for the User Plane. The Create Session Request at initial attach in E-Utran shall have the PAA set to the values set here.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IpType (str): Defines the IP type to be used by the UE. IP type IPv4v6 is used for dual stack functionality.
            Lifetime (number): Amount of time (in seconds) to wait after PDN attach procedure completes before scheduling forced detach.
            Mbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Mbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
            Name (str): APN name
            ObjectId (str): Unique identifier for this object
            PgwCount (number): Defines the number of PGW addresses in the range.
            PgwIp (str): PGW IP
            PgwIpCount (number): 
            Qci (number): QoS Class Identifier
            Restriction (number): Authorization to access another APN
            SelectionMode (number): Indicates the origin of the APN in the message
            UpdateAmbrEnable (bool): Update APN-AMBR for this UE
            UpdateAmbrIncrement (number): Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
            UpdateAmbrIterations (number): How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
            UpdateAmbrTimeout (number): Time to wait (in seconds) since the session was created until sending the update
            UseFullApn (bool): Send the full APN in CreateSessionRequest by appending APN-OI to the APN name

        Returns:
            self: This instance with matching globalEgtpApnS5S8 data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of globalEgtpApnS5S8 data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the globalEgtpApnS5S8 data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
