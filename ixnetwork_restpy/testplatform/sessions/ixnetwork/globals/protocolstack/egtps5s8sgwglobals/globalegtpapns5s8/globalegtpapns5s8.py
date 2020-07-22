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


class GlobalEgtpApnS5S8(Base):
    """
    The GlobalEgtpApnS5S8 class encapsulates a list of globalEgtpApnS5S8 resources that are managed by the user.
    A list of resources can be retrieved from the server using the GlobalEgtpApnS5S8.find() method.
    The list can be managed by using the GlobalEgtpApnS5S8.add() and GlobalEgtpApnS5S8.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'globalEgtpApnS5S8'
    _SDM_ATT_MAP = {
        'AddressPoolStartIPv4': 'addressPoolStartIPv4',
        'AddressPoolStartIPv6': 'addressPoolStartIPv6',
        'AmbrDL': 'ambrDL',
        'AmbrUL': 'ambrUL',
        'ArpPreemptionCapability': 'arpPreemptionCapability',
        'ArpPreemptionVulnerability': 'arpPreemptionVulnerability',
        'ArpPriorityLevel': 'arpPriorityLevel',
        'EnableLifetime': 'enableLifetime',
        'EnablePgwDistribution': 'enablePgwDistribution',
        'EnableStaticIpAllocation': 'enableStaticIpAllocation',
        'Enabled': 'enabled',
        'IpType': 'ipType',
        'Lifetime': 'lifetime',
        'Mbrd': 'mbrd',
        'Mbru': 'mbru',
        'Name': 'name',
        'ObjectId': 'objectId',
        'PgwCount': 'pgwCount',
        'PgwIp': 'pgwIp',
        'PgwIpCount': 'pgwIpCount',
        'Qci': 'qci',
        'Restriction': 'restriction',
        'SelectionMode': 'selectionMode',
        'UpdateAmbrEnable': 'updateAmbrEnable',
        'UpdateAmbrIncrement': 'updateAmbrIncrement',
        'UpdateAmbrIterations': 'updateAmbrIterations',
        'UpdateAmbrTimeout': 'updateAmbrTimeout',
        'UseFullApn': 'useFullApn',
    }

    def __init__(self, parent):
        super(GlobalEgtpApnS5S8, self).__init__(parent)

    @property
    def AddressPoolStartIPv4(self):
        """
        Returns
        -------
        - str: Defines the base IPv4 address to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressPoolStartIPv4'])
    @AddressPoolStartIPv4.setter
    def AddressPoolStartIPv4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddressPoolStartIPv4'], value)

    @property
    def AddressPoolStartIPv6(self):
        """
        Returns
        -------
        - str: Defines the base IPv6 address to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressPoolStartIPv6'])
    @AddressPoolStartIPv6.setter
    def AddressPoolStartIPv6(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddressPoolStartIPv6'], value)

    @property
    def AmbrDL(self):
        """
        Returns
        -------
        - number: Aggregated Maximum Bit Rate for down-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AmbrDL'])
    @AmbrDL.setter
    def AmbrDL(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AmbrDL'], value)

    @property
    def AmbrUL(self):
        """
        Returns
        -------
        - number: Aggregated Maximum Bit Rate for up-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AmbrUL'])
    @AmbrUL.setter
    def AmbrUL(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AmbrUL'], value)

    @property
    def ArpPreemptionCapability(self):
        """
        Returns
        -------
        - bool: If true preemption capability is enabled
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpPreemptionCapability'])
    @ArpPreemptionCapability.setter
    def ArpPreemptionCapability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpPreemptionCapability'], value)

    @property
    def ArpPreemptionVulnerability(self):
        """
        Returns
        -------
        - bool: If true preemption vulnerability is enabled
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpPreemptionVulnerability'])
    @ArpPreemptionVulnerability.setter
    def ArpPreemptionVulnerability(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpPreemptionVulnerability'], value)

    @property
    def ArpPriorityLevel(self):
        """
        Returns
        -------
        - number: Priority Level 1=highest 15=lowest
        """
        return self._get_attribute(self._SDM_ATT_MAP['ArpPriorityLevel'])
    @ArpPriorityLevel.setter
    def ArpPriorityLevel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ArpPriorityLevel'], value)

    @property
    def EnableLifetime(self):
        """
        Returns
        -------
        - bool: Enable UE PDN connection lifetime control. The UE will disconnect from specified APN after the specified time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLifetime'])
    @EnableLifetime.setter
    def EnableLifetime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLifetime'], value)

    @property
    def EnablePgwDistribution(self):
        """
        Returns
        -------
        - bool: Enable PGW Distribution of IPs on SGW
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePgwDistribution'])
    @EnablePgwDistribution.setter
    def EnablePgwDistribution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePgwDistribution'], value)

    @property
    def EnableStaticIpAllocation(self):
        """
        Returns
        -------
        - bool: This enables the static ip allocation for the User Plane. The Create Session Request at initial attach in E-Utran shall have the PAA set to the values set here.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableStaticIpAllocation'])
    @EnableStaticIpAllocation.setter
    def EnableStaticIpAllocation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableStaticIpAllocation'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - str: Defines the IP type to be used by the UE. IP type IPv4v6 is used for dual stack functionality.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpType'])
    @IpType.setter
    def IpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpType'], value)

    @property
    def Lifetime(self):
        """
        Returns
        -------
        - number: Amount of time (in seconds) to wait after PDN attach procedure completes before scheduling forced detach.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Lifetime'])
    @Lifetime.setter
    def Lifetime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Lifetime'], value)

    @property
    def Mbrd(self):
        """
        Returns
        -------
        - number: Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mbrd'])
    @Mbrd.setter
    def Mbrd(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mbrd'], value)

    @property
    def Mbru(self):
        """
        Returns
        -------
        - number: Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mbru'])
    @Mbru.setter
    def Mbru(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mbru'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: APN name
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def PgwCount(self):
        """
        Returns
        -------
        - number: Defines the number of PGW addresses in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PgwCount'])
    @PgwCount.setter
    def PgwCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PgwCount'], value)

    @property
    def PgwIp(self):
        """
        Returns
        -------
        - str: PGW IP
        """
        return self._get_attribute(self._SDM_ATT_MAP['PgwIp'])
    @PgwIp.setter
    def PgwIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PgwIp'], value)

    @property
    def PgwIpCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PgwIpCount'])
    @PgwIpCount.setter
    def PgwIpCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PgwIpCount'], value)

    @property
    def Qci(self):
        """
        Returns
        -------
        - number: QoS Class Identifier
        """
        return self._get_attribute(self._SDM_ATT_MAP['Qci'])
    @Qci.setter
    def Qci(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Qci'], value)

    @property
    def Restriction(self):
        """
        Returns
        -------
        - number: Authorization to access another APN
        """
        return self._get_attribute(self._SDM_ATT_MAP['Restriction'])
    @Restriction.setter
    def Restriction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Restriction'], value)

    @property
    def SelectionMode(self):
        """
        Returns
        -------
        - number: Indicates the origin of the APN in the message
        """
        return self._get_attribute(self._SDM_ATT_MAP['SelectionMode'])
    @SelectionMode.setter
    def SelectionMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SelectionMode'], value)

    @property
    def UpdateAmbrEnable(self):
        """
        Returns
        -------
        - bool: Update APN-AMBR for this UE
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateAmbrEnable'])
    @UpdateAmbrEnable.setter
    def UpdateAmbrEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateAmbrEnable'], value)

    @property
    def UpdateAmbrIncrement(self):
        """
        Returns
        -------
        - number: Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateAmbrIncrement'])
    @UpdateAmbrIncrement.setter
    def UpdateAmbrIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateAmbrIncrement'], value)

    @property
    def UpdateAmbrIterations(self):
        """
        Returns
        -------
        - number: How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateAmbrIterations'])
    @UpdateAmbrIterations.setter
    def UpdateAmbrIterations(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateAmbrIterations'], value)

    @property
    def UpdateAmbrTimeout(self):
        """
        Returns
        -------
        - number: Time to wait (in seconds) since the session was created until sending the update
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateAmbrTimeout'])
    @UpdateAmbrTimeout.setter
    def UpdateAmbrTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateAmbrTimeout'], value)

    @property
    def UseFullApn(self):
        """
        Returns
        -------
        - bool: Send the full APN in CreateSessionRequest by appending APN-OI to the APN name
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseFullApn'])
    @UseFullApn.setter
    def UseFullApn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseFullApn'], value)

    def update(self, AddressPoolStartIPv4=None, AddressPoolStartIPv6=None, AmbrDL=None, AmbrUL=None, ArpPreemptionCapability=None, ArpPreemptionVulnerability=None, ArpPriorityLevel=None, EnableLifetime=None, EnablePgwDistribution=None, EnableStaticIpAllocation=None, Enabled=None, IpType=None, Lifetime=None, Mbrd=None, Mbru=None, Name=None, PgwCount=None, PgwIp=None, PgwIpCount=None, Qci=None, Restriction=None, SelectionMode=None, UpdateAmbrEnable=None, UpdateAmbrIncrement=None, UpdateAmbrIterations=None, UpdateAmbrTimeout=None, UseFullApn=None):
        """Updates globalEgtpApnS5S8 resource on the server.

        Args
        ----
        - AddressPoolStartIPv4 (str): Defines the base IPv4 address to be used for enumerating all the addresses in the range.
        - AddressPoolStartIPv6 (str): Defines the base IPv6 address to be used for enumerating all the addresses in the range.
        - AmbrDL (number): Aggregated Maximum Bit Rate for down-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - AmbrUL (number): Aggregated Maximum Bit Rate for up-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - ArpPreemptionCapability (bool): If true preemption capability is enabled
        - ArpPreemptionVulnerability (bool): If true preemption vulnerability is enabled
        - ArpPriorityLevel (number): Priority Level 1=highest 15=lowest
        - EnableLifetime (bool): Enable UE PDN connection lifetime control. The UE will disconnect from specified APN after the specified time.
        - EnablePgwDistribution (bool): Enable PGW Distribution of IPs on SGW
        - EnableStaticIpAllocation (bool): This enables the static ip allocation for the User Plane. The Create Session Request at initial attach in E-Utran shall have the PAA set to the values set here.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): Defines the IP type to be used by the UE. IP type IPv4v6 is used for dual stack functionality.
        - Lifetime (number): Amount of time (in seconds) to wait after PDN attach procedure completes before scheduling forced detach.
        - Mbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Mbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Name (str): APN name
        - PgwCount (number): Defines the number of PGW addresses in the range.
        - PgwIp (str): PGW IP
        - PgwIpCount (number): 
        - Qci (number): QoS Class Identifier
        - Restriction (number): Authorization to access another APN
        - SelectionMode (number): Indicates the origin of the APN in the message
        - UpdateAmbrEnable (bool): Update APN-AMBR for this UE
        - UpdateAmbrIncrement (number): Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
        - UpdateAmbrIterations (number): How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
        - UpdateAmbrTimeout (number): Time to wait (in seconds) since the session was created until sending the update
        - UseFullApn (bool): Send the full APN in CreateSessionRequest by appending APN-OI to the APN name

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AddressPoolStartIPv4=None, AddressPoolStartIPv6=None, AmbrDL=None, AmbrUL=None, ArpPreemptionCapability=None, ArpPreemptionVulnerability=None, ArpPriorityLevel=None, EnableLifetime=None, EnablePgwDistribution=None, EnableStaticIpAllocation=None, Enabled=None, IpType=None, Lifetime=None, Mbrd=None, Mbru=None, Name=None, PgwCount=None, PgwIp=None, PgwIpCount=None, Qci=None, Restriction=None, SelectionMode=None, UpdateAmbrEnable=None, UpdateAmbrIncrement=None, UpdateAmbrIterations=None, UpdateAmbrTimeout=None, UseFullApn=None):
        """Adds a new globalEgtpApnS5S8 resource on the server and adds it to the container.

        Args
        ----
        - AddressPoolStartIPv4 (str): Defines the base IPv4 address to be used for enumerating all the addresses in the range.
        - AddressPoolStartIPv6 (str): Defines the base IPv6 address to be used for enumerating all the addresses in the range.
        - AmbrDL (number): Aggregated Maximum Bit Rate for down-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - AmbrUL (number): Aggregated Maximum Bit Rate for up-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - ArpPreemptionCapability (bool): If true preemption capability is enabled
        - ArpPreemptionVulnerability (bool): If true preemption vulnerability is enabled
        - ArpPriorityLevel (number): Priority Level 1=highest 15=lowest
        - EnableLifetime (bool): Enable UE PDN connection lifetime control. The UE will disconnect from specified APN after the specified time.
        - EnablePgwDistribution (bool): Enable PGW Distribution of IPs on SGW
        - EnableStaticIpAllocation (bool): This enables the static ip allocation for the User Plane. The Create Session Request at initial attach in E-Utran shall have the PAA set to the values set here.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): Defines the IP type to be used by the UE. IP type IPv4v6 is used for dual stack functionality.
        - Lifetime (number): Amount of time (in seconds) to wait after PDN attach procedure completes before scheduling forced detach.
        - Mbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Mbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Name (str): APN name
        - PgwCount (number): Defines the number of PGW addresses in the range.
        - PgwIp (str): PGW IP
        - PgwIpCount (number): 
        - Qci (number): QoS Class Identifier
        - Restriction (number): Authorization to access another APN
        - SelectionMode (number): Indicates the origin of the APN in the message
        - UpdateAmbrEnable (bool): Update APN-AMBR for this UE
        - UpdateAmbrIncrement (number): Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
        - UpdateAmbrIterations (number): How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
        - UpdateAmbrTimeout (number): Time to wait (in seconds) since the session was created until sending the update
        - UseFullApn (bool): Send the full APN in CreateSessionRequest by appending APN-OI to the APN name

        Returns
        -------
        - self: This instance with all currently retrieved globalEgtpApnS5S8 resources using find and the newly added globalEgtpApnS5S8 resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained globalEgtpApnS5S8 resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AddressPoolStartIPv4=None, AddressPoolStartIPv6=None, AmbrDL=None, AmbrUL=None, ArpPreemptionCapability=None, ArpPreemptionVulnerability=None, ArpPriorityLevel=None, EnableLifetime=None, EnablePgwDistribution=None, EnableStaticIpAllocation=None, Enabled=None, IpType=None, Lifetime=None, Mbrd=None, Mbru=None, Name=None, ObjectId=None, PgwCount=None, PgwIp=None, PgwIpCount=None, Qci=None, Restriction=None, SelectionMode=None, UpdateAmbrEnable=None, UpdateAmbrIncrement=None, UpdateAmbrIterations=None, UpdateAmbrTimeout=None, UseFullApn=None):
        """Finds and retrieves globalEgtpApnS5S8 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve globalEgtpApnS5S8 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all globalEgtpApnS5S8 resources from the server.

        Args
        ----
        - AddressPoolStartIPv4 (str): Defines the base IPv4 address to be used for enumerating all the addresses in the range.
        - AddressPoolStartIPv6 (str): Defines the base IPv6 address to be used for enumerating all the addresses in the range.
        - AmbrDL (number): Aggregated Maximum Bit Rate for down-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - AmbrUL (number): Aggregated Maximum Bit Rate for up-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - ArpPreemptionCapability (bool): If true preemption capability is enabled
        - ArpPreemptionVulnerability (bool): If true preemption vulnerability is enabled
        - ArpPriorityLevel (number): Priority Level 1=highest 15=lowest
        - EnableLifetime (bool): Enable UE PDN connection lifetime control. The UE will disconnect from specified APN after the specified time.
        - EnablePgwDistribution (bool): Enable PGW Distribution of IPs on SGW
        - EnableStaticIpAllocation (bool): This enables the static ip allocation for the User Plane. The Create Session Request at initial attach in E-Utran shall have the PAA set to the values set here.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): Defines the IP type to be used by the UE. IP type IPv4v6 is used for dual stack functionality.
        - Lifetime (number): Amount of time (in seconds) to wait after PDN attach procedure completes before scheduling forced detach.
        - Mbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Mbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Name (str): APN name
        - ObjectId (str): Unique identifier for this object
        - PgwCount (number): Defines the number of PGW addresses in the range.
        - PgwIp (str): PGW IP
        - PgwIpCount (number): 
        - Qci (number): QoS Class Identifier
        - Restriction (number): Authorization to access another APN
        - SelectionMode (number): Indicates the origin of the APN in the message
        - UpdateAmbrEnable (bool): Update APN-AMBR for this UE
        - UpdateAmbrIncrement (number): Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
        - UpdateAmbrIterations (number): How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
        - UpdateAmbrTimeout (number): Time to wait (in seconds) since the session was created until sending the update
        - UseFullApn (bool): Send the full APN in CreateSessionRequest by appending APN-OI to the APN name

        Returns
        -------
        - self: This instance with matching globalEgtpApnS5S8 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of globalEgtpApnS5S8 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the globalEgtpApnS5S8 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
