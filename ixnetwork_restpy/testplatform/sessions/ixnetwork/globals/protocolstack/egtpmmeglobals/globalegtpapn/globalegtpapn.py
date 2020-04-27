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


class GlobalEgtpApn(Base):
    """
    The GlobalEgtpApn class encapsulates a list of globalEgtpApn resources that are managed by the user.
    A list of resources can be retrieved from the server using the GlobalEgtpApn.find() method.
    The list can be managed by using the GlobalEgtpApn.add() and GlobalEgtpApn.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'globalEgtpApn'

    def __init__(self, parent):
        super(GlobalEgtpApn, self).__init__(parent)

    @property
    def AddressPoolStartIpv4(self):
        """
        Returns
        -------
        - str: Defines the base IPv4 address to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute('addressPoolStartIpv4')
    @AddressPoolStartIpv4.setter
    def AddressPoolStartIpv4(self, value):
        self._set_attribute('addressPoolStartIpv4', value)

    @property
    def AddressPoolStartIpv6(self):
        """
        Returns
        -------
        - str: Defines the base IPv6 address to be used for enumerating all the addresses in the range.
        """
        return self._get_attribute('addressPoolStartIpv6')
    @AddressPoolStartIpv6.setter
    def AddressPoolStartIpv6(self, value):
        self._set_attribute('addressPoolStartIpv6', value)

    @property
    def AmbrDl(self):
        """
        Returns
        -------
        - number: Aggregated Maximum Bit Rate for down-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        """
        return self._get_attribute('ambrDl')
    @AmbrDl.setter
    def AmbrDl(self, value):
        self._set_attribute('ambrDl', value)

    @property
    def AmbrUl(self):
        """
        Returns
        -------
        - number: Aggregated Maximum Bit Rate for up-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        """
        return self._get_attribute('ambrUl')
    @AmbrUl.setter
    def AmbrUl(self, value):
        self._set_attribute('ambrUl', value)

    @property
    def ArpPreemptionCapability(self):
        """
        Returns
        -------
        - bool: If true preemption capability is enabled
        """
        return self._get_attribute('arpPreemptionCapability')
    @ArpPreemptionCapability.setter
    def ArpPreemptionCapability(self, value):
        self._set_attribute('arpPreemptionCapability', value)

    @property
    def ArpPreemptionVulnerability(self):
        """
        Returns
        -------
        - bool: If true preemption vulnerability is enabled
        """
        return self._get_attribute('arpPreemptionVulnerability')
    @ArpPreemptionVulnerability.setter
    def ArpPreemptionVulnerability(self, value):
        self._set_attribute('arpPreemptionVulnerability', value)

    @property
    def ArpPriorityLevel(self):
        """
        Returns
        -------
        - number: Priority Level 1=highest 15=lowest
        """
        return self._get_attribute('arpPriorityLevel')
    @ArpPriorityLevel.setter
    def ArpPriorityLevel(self, value):
        self._set_attribute('arpPriorityLevel', value)

    @property
    def EnableLifetime(self):
        """
        Returns
        -------
        - bool: Enable UE PDN connection lifetime control. The UE will disconnect from specified APN after the specified time.
        """
        return self._get_attribute('enableLifetime')
    @EnableLifetime.setter
    def EnableLifetime(self, value):
        self._set_attribute('enableLifetime', value)

    @property
    def EnableStaticIpAllocation(self):
        """
        Returns
        -------
        - bool: This enables the static ip allocation for the User Plane. The Create Session Request at initial attach in E-Utran shall have the PAA set to the values set here.
        """
        return self._get_attribute('enableStaticIpAllocation')
    @EnableStaticIpAllocation.setter
    def EnableStaticIpAllocation(self, value):
        self._set_attribute('enableStaticIpAllocation', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - str: Defines the IP type to be used by the UE. IP type IPv4v6 is used for dual stack functionality.
        """
        return self._get_attribute('ipType')
    @IpType.setter
    def IpType(self, value):
        self._set_attribute('ipType', value)

    @property
    def Lifetime(self):
        """
        Returns
        -------
        - number: Amount of time (in seconds) to wait after PDN attach procedure completes before scheduling forced detach.
        """
        return self._get_attribute('lifetime')
    @Lifetime.setter
    def Lifetime(self, value):
        self._set_attribute('lifetime', value)

    @property
    def Mbrd(self):
        """
        Returns
        -------
        - number: Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        """
        return self._get_attribute('mbrd')
    @Mbrd.setter
    def Mbrd(self, value):
        self._set_attribute('mbrd', value)

    @property
    def Mbru(self):
        """
        Returns
        -------
        - number: Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        """
        return self._get_attribute('mbru')
    @Mbru.setter
    def Mbru(self, value):
        self._set_attribute('mbru', value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: APN name
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute('objectId')

    @property
    def PgwIp(self):
        """
        Returns
        -------
        - str: PGW IP
        """
        return self._get_attribute('pgwIp')
    @PgwIp.setter
    def PgwIp(self, value):
        self._set_attribute('pgwIp', value)

    @property
    def PgwIpCount(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute('pgwIpCount')
    @PgwIpCount.setter
    def PgwIpCount(self, value):
        self._set_attribute('pgwIpCount', value)

    @property
    def Qci(self):
        """
        Returns
        -------
        - number: QoS Class Identifier
        """
        return self._get_attribute('qci')
    @Qci.setter
    def Qci(self, value):
        self._set_attribute('qci', value)

    @property
    def QosLabel(self):
        """
        Returns
        -------
        - str: Quality of Service characteristics requested by the SGSN for the primary PDP contexts.
        """
        return self._get_attribute('qosLabel')
    @QosLabel.setter
    def QosLabel(self, value):
        self._set_attribute('qosLabel', value)

    @property
    def Restriction(self):
        """
        Returns
        -------
        - number: Authorization to access another APN
        """
        return self._get_attribute('restriction')
    @Restriction.setter
    def Restriction(self, value):
        self._set_attribute('restriction', value)

    @property
    def SelectionMode(self):
        """
        Returns
        -------
        - number: Indicates the origin of the APN in the message
        """
        return self._get_attribute('selectionMode')
    @SelectionMode.setter
    def SelectionMode(self, value):
        self._set_attribute('selectionMode', value)

    @property
    def SendImcnFlagPco(self):
        """
        Returns
        -------
        - bool: Set the IM CN Subsystem signalling flag in the PCO IE
        """
        return self._get_attribute('sendImcnFlagPco')
    @SendImcnFlagPco.setter
    def SendImcnFlagPco(self, value):
        self._set_attribute('sendImcnFlagPco', value)

    @property
    def SendPcscfv4RequestPco(self):
        """
        Returns
        -------
        - bool: Send a request for a P-CSCF IPv4 address in the PCO IE
        """
        return self._get_attribute('sendPcscfv4RequestPco')
    @SendPcscfv4RequestPco.setter
    def SendPcscfv4RequestPco(self, value):
        self._set_attribute('sendPcscfv4RequestPco', value)

    @property
    def SendPcscfv6RequestPco(self):
        """
        Returns
        -------
        - bool: Send a request for a P-CSCF IPv6 address in the PCO IE
        """
        return self._get_attribute('sendPcscfv6RequestPco')
    @SendPcscfv6RequestPco.setter
    def SendPcscfv6RequestPco(self, value):
        self._set_attribute('sendPcscfv6RequestPco', value)

    @property
    def UpdateAmbrEnable(self):
        """
        Returns
        -------
        - bool: Update APN-AMBR for this UE
        """
        return self._get_attribute('updateAmbrEnable')
    @UpdateAmbrEnable.setter
    def UpdateAmbrEnable(self, value):
        self._set_attribute('updateAmbrEnable', value)

    @property
    def UpdateAmbrIncrement(self):
        """
        Returns
        -------
        - number: Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
        """
        return self._get_attribute('updateAmbrIncrement')
    @UpdateAmbrIncrement.setter
    def UpdateAmbrIncrement(self, value):
        self._set_attribute('updateAmbrIncrement', value)

    @property
    def UpdateAmbrIterations(self):
        """
        Returns
        -------
        - number: How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
        """
        return self._get_attribute('updateAmbrIterations')
    @UpdateAmbrIterations.setter
    def UpdateAmbrIterations(self, value):
        self._set_attribute('updateAmbrIterations', value)

    @property
    def UpdateAmbrTimeout(self):
        """
        Returns
        -------
        - number: Time to wait (in seconds) since the session was created until sending the update
        """
        return self._get_attribute('updateAmbrTimeout')
    @UpdateAmbrTimeout.setter
    def UpdateAmbrTimeout(self, value):
        self._set_attribute('updateAmbrTimeout', value)

    @property
    def UseFullApn(self):
        """
        Returns
        -------
        - bool: Send the full APN in CreateSessionRequest by appending APN-OI to the APN name
        """
        return self._get_attribute('useFullApn')
    @UseFullApn.setter
    def UseFullApn(self, value):
        self._set_attribute('useFullApn', value)

    def update(self, AddressPoolStartIpv4=None, AddressPoolStartIpv6=None, AmbrDl=None, AmbrUl=None, ArpPreemptionCapability=None, ArpPreemptionVulnerability=None, ArpPriorityLevel=None, EnableLifetime=None, EnableStaticIpAllocation=None, Enabled=None, IpType=None, Lifetime=None, Mbrd=None, Mbru=None, Name=None, PgwIp=None, PgwIpCount=None, Qci=None, QosLabel=None, Restriction=None, SelectionMode=None, SendImcnFlagPco=None, SendPcscfv4RequestPco=None, SendPcscfv6RequestPco=None, UpdateAmbrEnable=None, UpdateAmbrIncrement=None, UpdateAmbrIterations=None, UpdateAmbrTimeout=None, UseFullApn=None):
        """Updates globalEgtpApn resource on the server.

        Args
        ----
        - AddressPoolStartIpv4 (str): Defines the base IPv4 address to be used for enumerating all the addresses in the range.
        - AddressPoolStartIpv6 (str): Defines the base IPv6 address to be used for enumerating all the addresses in the range.
        - AmbrDl (number): Aggregated Maximum Bit Rate for down-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - AmbrUl (number): Aggregated Maximum Bit Rate for up-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - ArpPreemptionCapability (bool): If true preemption capability is enabled
        - ArpPreemptionVulnerability (bool): If true preemption vulnerability is enabled
        - ArpPriorityLevel (number): Priority Level 1=highest 15=lowest
        - EnableLifetime (bool): Enable UE PDN connection lifetime control. The UE will disconnect from specified APN after the specified time.
        - EnableStaticIpAllocation (bool): This enables the static ip allocation for the User Plane. The Create Session Request at initial attach in E-Utran shall have the PAA set to the values set here.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): Defines the IP type to be used by the UE. IP type IPv4v6 is used for dual stack functionality.
        - Lifetime (number): Amount of time (in seconds) to wait after PDN attach procedure completes before scheduling forced detach.
        - Mbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Mbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Name (str): APN name
        - PgwIp (str): PGW IP
        - PgwIpCount (number): 
        - Qci (number): QoS Class Identifier
        - QosLabel (str): Quality of Service characteristics requested by the SGSN for the primary PDP contexts.
        - Restriction (number): Authorization to access another APN
        - SelectionMode (number): Indicates the origin of the APN in the message
        - SendImcnFlagPco (bool): Set the IM CN Subsystem signalling flag in the PCO IE
        - SendPcscfv4RequestPco (bool): Send a request for a P-CSCF IPv4 address in the PCO IE
        - SendPcscfv6RequestPco (bool): Send a request for a P-CSCF IPv6 address in the PCO IE
        - UpdateAmbrEnable (bool): Update APN-AMBR for this UE
        - UpdateAmbrIncrement (number): Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
        - UpdateAmbrIterations (number): How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
        - UpdateAmbrTimeout (number): Time to wait (in seconds) since the session was created until sending the update
        - UseFullApn (bool): Send the full APN in CreateSessionRequest by appending APN-OI to the APN name

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, AddressPoolStartIpv4=None, AddressPoolStartIpv6=None, AmbrDl=None, AmbrUl=None, ArpPreemptionCapability=None, ArpPreemptionVulnerability=None, ArpPriorityLevel=None, EnableLifetime=None, EnableStaticIpAllocation=None, Enabled=None, IpType=None, Lifetime=None, Mbrd=None, Mbru=None, Name=None, PgwIp=None, PgwIpCount=None, Qci=None, QosLabel=None, Restriction=None, SelectionMode=None, SendImcnFlagPco=None, SendPcscfv4RequestPco=None, SendPcscfv6RequestPco=None, UpdateAmbrEnable=None, UpdateAmbrIncrement=None, UpdateAmbrIterations=None, UpdateAmbrTimeout=None, UseFullApn=None):
        """Adds a new globalEgtpApn resource on the server and adds it to the container.

        Args
        ----
        - AddressPoolStartIpv4 (str): Defines the base IPv4 address to be used for enumerating all the addresses in the range.
        - AddressPoolStartIpv6 (str): Defines the base IPv6 address to be used for enumerating all the addresses in the range.
        - AmbrDl (number): Aggregated Maximum Bit Rate for down-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - AmbrUl (number): Aggregated Maximum Bit Rate for up-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - ArpPreemptionCapability (bool): If true preemption capability is enabled
        - ArpPreemptionVulnerability (bool): If true preemption vulnerability is enabled
        - ArpPriorityLevel (number): Priority Level 1=highest 15=lowest
        - EnableLifetime (bool): Enable UE PDN connection lifetime control. The UE will disconnect from specified APN after the specified time.
        - EnableStaticIpAllocation (bool): This enables the static ip allocation for the User Plane. The Create Session Request at initial attach in E-Utran shall have the PAA set to the values set here.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): Defines the IP type to be used by the UE. IP type IPv4v6 is used for dual stack functionality.
        - Lifetime (number): Amount of time (in seconds) to wait after PDN attach procedure completes before scheduling forced detach.
        - Mbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Mbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Name (str): APN name
        - PgwIp (str): PGW IP
        - PgwIpCount (number): 
        - Qci (number): QoS Class Identifier
        - QosLabel (str): Quality of Service characteristics requested by the SGSN for the primary PDP contexts.
        - Restriction (number): Authorization to access another APN
        - SelectionMode (number): Indicates the origin of the APN in the message
        - SendImcnFlagPco (bool): Set the IM CN Subsystem signalling flag in the PCO IE
        - SendPcscfv4RequestPco (bool): Send a request for a P-CSCF IPv4 address in the PCO IE
        - SendPcscfv6RequestPco (bool): Send a request for a P-CSCF IPv6 address in the PCO IE
        - UpdateAmbrEnable (bool): Update APN-AMBR for this UE
        - UpdateAmbrIncrement (number): Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
        - UpdateAmbrIterations (number): How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
        - UpdateAmbrTimeout (number): Time to wait (in seconds) since the session was created until sending the update
        - UseFullApn (bool): Send the full APN in CreateSessionRequest by appending APN-OI to the APN name

        Returns
        -------
        - self: This instance with all currently retrieved globalEgtpApn resources using find and the newly added globalEgtpApn resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained globalEgtpApn resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AddressPoolStartIpv4=None, AddressPoolStartIpv6=None, AmbrDl=None, AmbrUl=None, ArpPreemptionCapability=None, ArpPreemptionVulnerability=None, ArpPriorityLevel=None, EnableLifetime=None, EnableStaticIpAllocation=None, Enabled=None, IpType=None, Lifetime=None, Mbrd=None, Mbru=None, Name=None, ObjectId=None, PgwIp=None, PgwIpCount=None, Qci=None, QosLabel=None, Restriction=None, SelectionMode=None, SendImcnFlagPco=None, SendPcscfv4RequestPco=None, SendPcscfv6RequestPco=None, UpdateAmbrEnable=None, UpdateAmbrIncrement=None, UpdateAmbrIterations=None, UpdateAmbrTimeout=None, UseFullApn=None):
        """Finds and retrieves globalEgtpApn resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve globalEgtpApn resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all globalEgtpApn resources from the server.

        Args
        ----
        - AddressPoolStartIpv4 (str): Defines the base IPv4 address to be used for enumerating all the addresses in the range.
        - AddressPoolStartIpv6 (str): Defines the base IPv6 address to be used for enumerating all the addresses in the range.
        - AmbrDl (number): Aggregated Maximum Bit Rate for down-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - AmbrUl (number): Aggregated Maximum Bit Rate for up-link. For both spec versions (December '09 and December '10) this value represents kbps and the maximum value that can be encoded is 4,294,967,295 kbps.
        - ArpPreemptionCapability (bool): If true preemption capability is enabled
        - ArpPreemptionVulnerability (bool): If true preemption vulnerability is enabled
        - ArpPriorityLevel (number): Priority Level 1=highest 15=lowest
        - EnableLifetime (bool): Enable UE PDN connection lifetime control. The UE will disconnect from specified APN after the specified time.
        - EnableStaticIpAllocation (bool): This enables the static ip allocation for the User Plane. The Create Session Request at initial attach in E-Utran shall have the PAA set to the values set here.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): Defines the IP type to be used by the UE. IP type IPv4v6 is used for dual stack functionality.
        - Lifetime (number): Amount of time (in seconds) to wait after PDN attach procedure completes before scheduling forced detach.
        - Mbrd (number): Maximum bitrate for downlink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Mbru (number): Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Name (str): APN name
        - ObjectId (str): Unique identifier for this object
        - PgwIp (str): PGW IP
        - PgwIpCount (number): 
        - Qci (number): QoS Class Identifier
        - QosLabel (str): Quality of Service characteristics requested by the SGSN for the primary PDP contexts.
        - Restriction (number): Authorization to access another APN
        - SelectionMode (number): Indicates the origin of the APN in the message
        - SendImcnFlagPco (bool): Set the IM CN Subsystem signalling flag in the PCO IE
        - SendPcscfv4RequestPco (bool): Send a request for a P-CSCF IPv4 address in the PCO IE
        - SendPcscfv6RequestPco (bool): Send a request for a P-CSCF IPv6 address in the PCO IE
        - UpdateAmbrEnable (bool): Update APN-AMBR for this UE
        - UpdateAmbrIncrement (number): Percentage to increase the value of APN-AMBR at each update. Use negative values to decrease it.
        - UpdateAmbrIterations (number): How many updates to be sent during the lifetime of each session. Use 0 to send unlimited number of updates
        - UpdateAmbrTimeout (number): Time to wait (in seconds) since the session was created until sending the update
        - UseFullApn (bool): Send the full APN in CreateSessionRequest by appending APN-OI to the APN name

        Returns
        -------
        - self: This instance with matching globalEgtpApn resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of globalEgtpApn data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the globalEgtpApn resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
