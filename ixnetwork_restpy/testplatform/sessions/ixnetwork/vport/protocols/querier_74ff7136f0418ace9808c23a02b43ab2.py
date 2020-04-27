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


class Querier(Base):
    """This object contains the IGMP querier configuration.
    The Querier class encapsulates a list of querier resources that are managed by the user.
    A list of resources can be retrieved from the server using the Querier.find() method.
    The list can be managed by using the Querier.add() and Querier.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'querier'

    def __init__(self, parent):
        super(Querier, self).__init__(parent)

    @property
    def LearnedGroupInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedgroupinfo_7c507a18013ad2de8d72d84ff282da55.LearnedGroupInfo): An instance of the LearnedGroupInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedgroupinfo_7c507a18013ad2de8d72d84ff282da55 import LearnedGroupInfo
        return LearnedGroupInfo(self)

    @property
    def DiscardLearnedInfo(self):
        """
        Returns
        -------
        - bool: If true, the Querier doesn't maintain any database and only sends periodic general queries. The specific query group/source record information isn't calculated based on any earlier received Report, but solely based on the last received report. If false, the emulated Querier maintains a complete record state for received reports and send queries (based on timer expiry for received groups and sources). Default is true.
        """
        return self._get_attribute('discardLearnedInfo')
    @DiscardLearnedInfo.setter
    def DiscardLearnedInfo(self, value):
        self._set_attribute('discardLearnedInfo', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the querier is enabled.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def GeneralQueryInterval(self):
        """
        Returns
        -------
        - number: The amount of time in seconds between MLD General Query messages sent by the querier. The default query interval is 125 seconds.
        """
        return self._get_attribute('generalQueryInterval')
    @GeneralQueryInterval.setter
    def GeneralQueryInterval(self, value):
        self._set_attribute('generalQueryInterval', value)

    @property
    def GqResponseInterval(self):
        """
        Returns
        -------
        - number: The maximum amount of time in seconds that the MLD querier waits to receive a response to a General Query message. The default query response interval is 10000 milliseconds and must be less than the query interval.
        """
        return self._get_attribute('gqResponseInterval')
    @GqResponseInterval.setter
    def GqResponseInterval(self, value):
        self._set_attribute('gqResponseInterval', value)

    @property
    def InterfaceId(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): The interface associated with the MLD querier. The interface must be previously configured.
        """
        return self._get_attribute('interfaceId')
    @InterfaceId.setter
    def InterfaceId(self, value):
        self._set_attribute('interfaceId', value)

    @property
    def InterfaceIndex(self):
        """
        Returns
        -------
        - number: The assigned protocol interface ID for this SM interface.
        """
        return self._get_attribute('interfaceIndex')
    @InterfaceIndex.setter
    def InterfaceIndex(self, value):
        self._set_attribute('interfaceIndex', value)

    @property
    def InterfaceType(self):
        """
        Returns
        -------
        - str: The type of interface to be selected for this SM interface.
        """
        return self._get_attribute('interfaceType')
    @InterfaceType.setter
    def InterfaceType(self, value):
        self._set_attribute('interfaceType', value)

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range): The interfaces that are associated with the selected interface type.
        """
        return self._get_attribute('interfaces')
    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute('interfaces', value)

    @property
    def IsQuerier(self):
        """
        Returns
        -------
        - bool: If true, this MLD entity is a querier.
        """
        return self._get_attribute('isQuerier')

    @property
    def IsRefreshComplete(self):
        """
        Returns
        -------
        - bool: If true, the querier information is current.
        """
        return self._get_attribute('isRefreshComplete')

    @property
    def QuerierAddress(self):
        """
        Returns
        -------
        - str: The querier IP address.
        """
        return self._get_attribute('querierAddress')

    @property
    def QuerierWorkingVersion(self):
        """
        Returns
        -------
        - number: The querier working MLD version.
        """
        return self._get_attribute('querierWorkingVersion')

    @property
    def RobustnessVariable(self):
        """
        Returns
        -------
        - number: Defines the subnet vulnerability to lost packets. MLD can recover from robustness variable minus 1 lost MLD packets. The robustness variable should be set to a value of 2 or greater. The default robustness variable value is 2.
        """
        return self._get_attribute('robustnessVariable')
    @RobustnessVariable.setter
    def RobustnessVariable(self, value):
        self._set_attribute('robustnessVariable', value)

    @property
    def RouterAlert(self):
        """
        Returns
        -------
        - bool: If true, sets the Send Router Alert bit in the IP header.
        """
        return self._get_attribute('routerAlert')
    @RouterAlert.setter
    def RouterAlert(self, value):
        self._set_attribute('routerAlert', value)

    @property
    def SqResponseInterval(self):
        """
        Returns
        -------
        - number: The maximum amount of time in seconds that the MLD querier waits to receive a response to a Specific Query message. The default query response interval is 1000 milliseconds and must be less than the query interval.
        """
        return self._get_attribute('sqResponseInterval')
    @SqResponseInterval.setter
    def SqResponseInterval(self, value):
        self._set_attribute('sqResponseInterval', value)

    @property
    def SqTransmissionCount(self):
        """
        Returns
        -------
        - number: Indicates the total number of specific Query messages sent every Specific Query Response Interval seconds before assuming that there is no interested listener for the particular group/source.
        """
        return self._get_attribute('sqTransmissionCount')
    @SqTransmissionCount.setter
    def SqTransmissionCount(self, value):
        self._set_attribute('sqTransmissionCount', value)

    @property
    def StartupQueryCount(self):
        """
        Returns
        -------
        - number: The number of general query messages sent at startup. The default startup query count is 2.
        """
        return self._get_attribute('startupQueryCount')
    @StartupQueryCount.setter
    def StartupQueryCount(self, value):
        self._set_attribute('startupQueryCount', value)

    @property
    def SupportElection(self):
        """
        Returns
        -------
        - bool: If true, indicates whether the Querier participates in querier election or not. If disabled, then all incoming query messages are discarded.
        """
        return self._get_attribute('supportElection')
    @SupportElection.setter
    def SupportElection(self, value):
        self._set_attribute('supportElection', value)

    @property
    def SupportOlderVersionHost(self):
        """
        Returns
        -------
        - bool: If true, indicates whether the Querier will comply to RFC 3376 Section 7.3.2 and RFC 3810 Section 8.3.2. If disabled, all membership reports with version less than the current version are discarded.
        """
        return self._get_attribute('supportOlderVersionHost')
    @SupportOlderVersionHost.setter
    def SupportOlderVersionHost(self, value):
        self._set_attribute('supportOlderVersionHost', value)

    @property
    def SupportOlderVersionQuerier(self):
        """
        Returns
        -------
        - bool: If true, indicates whether the Querier downgrades to the lowest version of received query messages. If disabled, all query messages with version less than the current version are discarded.
        """
        return self._get_attribute('supportOlderVersionQuerier')
    @SupportOlderVersionQuerier.setter
    def SupportOlderVersionQuerier(self, value):
        self._set_attribute('supportOlderVersionQuerier', value)

    @property
    def Version(self):
        """
        Returns
        -------
        - str(version1 | version2): Sets the version for the MLD querier.
        """
        return self._get_attribute('version')
    @Version.setter
    def Version(self, value):
        self._set_attribute('version', value)

    def update(self, DiscardLearnedInfo=None, Enabled=None, GeneralQueryInterval=None, GqResponseInterval=None, InterfaceId=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, RobustnessVariable=None, RouterAlert=None, SqResponseInterval=None, SqTransmissionCount=None, StartupQueryCount=None, SupportElection=None, SupportOlderVersionHost=None, SupportOlderVersionQuerier=None, Version=None):
        """Updates querier resource on the server.

        Args
        ----
        - DiscardLearnedInfo (bool): If true, the Querier doesn't maintain any database and only sends periodic general queries. The specific query group/source record information isn't calculated based on any earlier received Report, but solely based on the last received report. If false, the emulated Querier maintains a complete record state for received reports and send queries (based on timer expiry for received groups and sources). Default is true.
        - Enabled (bool): If true, the querier is enabled.
        - GeneralQueryInterval (number): The amount of time in seconds between MLD General Query messages sent by the querier. The default query interval is 125 seconds.
        - GqResponseInterval (number): The maximum amount of time in seconds that the MLD querier waits to receive a response to a General Query message. The default query response interval is 10000 milliseconds and must be less than the query interval.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The interface associated with the MLD querier. The interface must be previously configured.
        - InterfaceIndex (number): The assigned protocol interface ID for this SM interface.
        - InterfaceType (str): The type of interface to be selected for this SM interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - RobustnessVariable (number): Defines the subnet vulnerability to lost packets. MLD can recover from robustness variable minus 1 lost MLD packets. The robustness variable should be set to a value of 2 or greater. The default robustness variable value is 2.
        - RouterAlert (bool): If true, sets the Send Router Alert bit in the IP header.
        - SqResponseInterval (number): The maximum amount of time in seconds that the MLD querier waits to receive a response to a Specific Query message. The default query response interval is 1000 milliseconds and must be less than the query interval.
        - SqTransmissionCount (number): Indicates the total number of specific Query messages sent every Specific Query Response Interval seconds before assuming that there is no interested listener for the particular group/source.
        - StartupQueryCount (number): The number of general query messages sent at startup. The default startup query count is 2.
        - SupportElection (bool): If true, indicates whether the Querier participates in querier election or not. If disabled, then all incoming query messages are discarded.
        - SupportOlderVersionHost (bool): If true, indicates whether the Querier will comply to RFC 3376 Section 7.3.2 and RFC 3810 Section 8.3.2. If disabled, all membership reports with version less than the current version are discarded.
        - SupportOlderVersionQuerier (bool): If true, indicates whether the Querier downgrades to the lowest version of received query messages. If disabled, all query messages with version less than the current version are discarded.
        - Version (str(version1 | version2)): Sets the version for the MLD querier.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, DiscardLearnedInfo=None, Enabled=None, GeneralQueryInterval=None, GqResponseInterval=None, InterfaceId=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, RobustnessVariable=None, RouterAlert=None, SqResponseInterval=None, SqTransmissionCount=None, StartupQueryCount=None, SupportElection=None, SupportOlderVersionHost=None, SupportOlderVersionQuerier=None, Version=None):
        """Adds a new querier resource on the server and adds it to the container.

        Args
        ----
        - DiscardLearnedInfo (bool): If true, the Querier doesn't maintain any database and only sends periodic general queries. The specific query group/source record information isn't calculated based on any earlier received Report, but solely based on the last received report. If false, the emulated Querier maintains a complete record state for received reports and send queries (based on timer expiry for received groups and sources). Default is true.
        - Enabled (bool): If true, the querier is enabled.
        - GeneralQueryInterval (number): The amount of time in seconds between MLD General Query messages sent by the querier. The default query interval is 125 seconds.
        - GqResponseInterval (number): The maximum amount of time in seconds that the MLD querier waits to receive a response to a General Query message. The default query response interval is 10000 milliseconds and must be less than the query interval.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The interface associated with the MLD querier. The interface must be previously configured.
        - InterfaceIndex (number): The assigned protocol interface ID for this SM interface.
        - InterfaceType (str): The type of interface to be selected for this SM interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - RobustnessVariable (number): Defines the subnet vulnerability to lost packets. MLD can recover from robustness variable minus 1 lost MLD packets. The robustness variable should be set to a value of 2 or greater. The default robustness variable value is 2.
        - RouterAlert (bool): If true, sets the Send Router Alert bit in the IP header.
        - SqResponseInterval (number): The maximum amount of time in seconds that the MLD querier waits to receive a response to a Specific Query message. The default query response interval is 1000 milliseconds and must be less than the query interval.
        - SqTransmissionCount (number): Indicates the total number of specific Query messages sent every Specific Query Response Interval seconds before assuming that there is no interested listener for the particular group/source.
        - StartupQueryCount (number): The number of general query messages sent at startup. The default startup query count is 2.
        - SupportElection (bool): If true, indicates whether the Querier participates in querier election or not. If disabled, then all incoming query messages are discarded.
        - SupportOlderVersionHost (bool): If true, indicates whether the Querier will comply to RFC 3376 Section 7.3.2 and RFC 3810 Section 8.3.2. If disabled, all membership reports with version less than the current version are discarded.
        - SupportOlderVersionQuerier (bool): If true, indicates whether the Querier downgrades to the lowest version of received query messages. If disabled, all query messages with version less than the current version are discarded.
        - Version (str(version1 | version2)): Sets the version for the MLD querier.

        Returns
        -------
        - self: This instance with all currently retrieved querier resources using find and the newly added querier resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained querier resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DiscardLearnedInfo=None, Enabled=None, GeneralQueryInterval=None, GqResponseInterval=None, InterfaceId=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, IsQuerier=None, IsRefreshComplete=None, QuerierAddress=None, QuerierWorkingVersion=None, RobustnessVariable=None, RouterAlert=None, SqResponseInterval=None, SqTransmissionCount=None, StartupQueryCount=None, SupportElection=None, SupportOlderVersionHost=None, SupportOlderVersionQuerier=None, Version=None):
        """Finds and retrieves querier resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve querier resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all querier resources from the server.

        Args
        ----
        - DiscardLearnedInfo (bool): If true, the Querier doesn't maintain any database and only sends periodic general queries. The specific query group/source record information isn't calculated based on any earlier received Report, but solely based on the last received report. If false, the emulated Querier maintains a complete record state for received reports and send queries (based on timer expiry for received groups and sources). Default is true.
        - Enabled (bool): If true, the querier is enabled.
        - GeneralQueryInterval (number): The amount of time in seconds between MLD General Query messages sent by the querier. The default query interval is 125 seconds.
        - GqResponseInterval (number): The maximum amount of time in seconds that the MLD querier waits to receive a response to a General Query message. The default query response interval is 10000 milliseconds and must be less than the query interval.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The interface associated with the MLD querier. The interface must be previously configured.
        - InterfaceIndex (number): The assigned protocol interface ID for this SM interface.
        - InterfaceType (str): The type of interface to be selected for this SM interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - IsQuerier (bool): If true, this MLD entity is a querier.
        - IsRefreshComplete (bool): If true, the querier information is current.
        - QuerierAddress (str): The querier IP address.
        - QuerierWorkingVersion (number): The querier working MLD version.
        - RobustnessVariable (number): Defines the subnet vulnerability to lost packets. MLD can recover from robustness variable minus 1 lost MLD packets. The robustness variable should be set to a value of 2 or greater. The default robustness variable value is 2.
        - RouterAlert (bool): If true, sets the Send Router Alert bit in the IP header.
        - SqResponseInterval (number): The maximum amount of time in seconds that the MLD querier waits to receive a response to a Specific Query message. The default query response interval is 1000 milliseconds and must be less than the query interval.
        - SqTransmissionCount (number): Indicates the total number of specific Query messages sent every Specific Query Response Interval seconds before assuming that there is no interested listener for the particular group/source.
        - StartupQueryCount (number): The number of general query messages sent at startup. The default startup query count is 2.
        - SupportElection (bool): If true, indicates whether the Querier participates in querier election or not. If disabled, then all incoming query messages are discarded.
        - SupportOlderVersionHost (bool): If true, indicates whether the Querier will comply to RFC 3376 Section 7.3.2 and RFC 3810 Section 8.3.2. If disabled, all membership reports with version less than the current version are discarded.
        - SupportOlderVersionQuerier (bool): If true, indicates whether the Querier downgrades to the lowest version of received query messages. If disabled, all query messages with version less than the current version are discarded.
        - Version (str(version1 | version2)): Sets the version for the MLD querier.

        Returns
        -------
        - self: This instance with matching querier resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of querier data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the querier resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetInterfaceAccessorIfaceList(self):
        """Executes the getInterfaceAccessorIfaceList operation on the server.

        Gets the interface accesor Iface list.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('getInterfaceAccessorIfaceList', payload=payload, response_object=None)

    def RefreshLearnedInfo(self):
        """Executes the refreshLearnedInfo operation on the server.

        If enabled, it refreshes the learned info.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
