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


class IgmpQuerierRange(Base):
    """
    The IgmpQuerierRange class encapsulates a list of igmpQuerierRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the IgmpQuerierRange.find() method.
    The list can be managed by the user by using the IgmpQuerierRange.add() and IgmpQuerierRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'igmpQuerierRange'

    def __init__(self, parent):
        super(IgmpQuerierRange, self).__init__(parent)

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
    def GeneralQueryInterval(self):
        """The amount of time in seconds between IGMP/MLD General Query messages sent by the querier.

        Returns:
            number
        """
        return self._get_attribute('generalQueryInterval')
    @GeneralQueryInterval.setter
    def GeneralQueryInterval(self, value):
        self._set_attribute('generalQueryInterval', value)

    @property
    def GeneralQueryResponseInterval(self):
        """Indicates the maximum amount of time in milliseconds that the IGMP/MLD querier waits to receive a response to a General Query message. The query response must be lesser than the query interval.

        Returns:
            number
        """
        return self._get_attribute('generalQueryResponseInterval')
    @GeneralQueryResponseInterval.setter
    def GeneralQueryResponseInterval(self, value):
        self._set_attribute('generalQueryResponseInterval', value)

    @property
    def Name(self):
        """Name of range

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
    def RobustnessVariable(self):
        """Defines the subnet vulnerability to lost packets. IGMP/MLD can recover from robustness variable minus 1 lost IGMP/MLD packets.

        Returns:
            number
        """
        return self._get_attribute('robustnessVariable')
    @RobustnessVariable.setter
    def RobustnessVariable(self, value):
        self._set_attribute('robustnessVariable', value)

    @property
    def RouterAlert(self):
        """If selected, sets the Send Router Alert bit in the IP header.

        Returns:
            bool
        """
        return self._get_attribute('routerAlert')
    @RouterAlert.setter
    def RouterAlert(self, value):
        self._set_attribute('routerAlert', value)

    @property
    def SpecificQueryResponseCount(self):
        """Indicates the total number of Specific Query messages sent every Specific Query Response Interval seconds before assuming that there is no interested listener for the particular group/source.

        Returns:
            number
        """
        return self._get_attribute('specificQueryResponseCount')
    @SpecificQueryResponseCount.setter
    def SpecificQueryResponseCount(self, value):
        self._set_attribute('specificQueryResponseCount', value)

    @property
    def SpecificQueryResponseInterval(self):
        """Indicates the maximum amount of time in milliseconds that the IGMP/MLD Querier waits to receive a response to a Specific Query message. The query response must be lesser than the query interval.

        Returns:
            number
        """
        return self._get_attribute('specificQueryResponseInterval')
    @SpecificQueryResponseInterval.setter
    def SpecificQueryResponseInterval(self, value):
        self._set_attribute('specificQueryResponseInterval', value)

    @property
    def StartupQueryCount(self):
        """The number of general query messages sent at startup.

        Returns:
            number
        """
        return self._get_attribute('startupQueryCount')
    @StartupQueryCount.setter
    def StartupQueryCount(self, value):
        self._set_attribute('startupQueryCount', value)

    @property
    def Version(self):
        """IGMP/MLD protocol version.

        Returns:
            str
        """
        return self._get_attribute('version')
    @Version.setter
    def Version(self, value):
        self._set_attribute('version', value)

    def update(self, Enabled=None, GeneralQueryInterval=None, GeneralQueryResponseInterval=None, Name=None, RobustnessVariable=None, RouterAlert=None, SpecificQueryResponseCount=None, SpecificQueryResponseInterval=None, StartupQueryCount=None, Version=None):
        """Updates a child instance of igmpQuerierRange on the server.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            GeneralQueryInterval (number): The amount of time in seconds between IGMP/MLD General Query messages sent by the querier.
            GeneralQueryResponseInterval (number): Indicates the maximum amount of time in milliseconds that the IGMP/MLD querier waits to receive a response to a General Query message. The query response must be lesser than the query interval.
            Name (str): Name of range
            RobustnessVariable (number): Defines the subnet vulnerability to lost packets. IGMP/MLD can recover from robustness variable minus 1 lost IGMP/MLD packets.
            RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
            SpecificQueryResponseCount (number): Indicates the total number of Specific Query messages sent every Specific Query Response Interval seconds before assuming that there is no interested listener for the particular group/source.
            SpecificQueryResponseInterval (number): Indicates the maximum amount of time in milliseconds that the IGMP/MLD Querier waits to receive a response to a Specific Query message. The query response must be lesser than the query interval.
            StartupQueryCount (number): The number of general query messages sent at startup.
            Version (str): IGMP/MLD protocol version.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Enabled=None, GeneralQueryInterval=None, GeneralQueryResponseInterval=None, Name=None, RobustnessVariable=None, RouterAlert=None, SpecificQueryResponseCount=None, SpecificQueryResponseInterval=None, StartupQueryCount=None, Version=None):
        """Adds a new igmpQuerierRange node on the server and retrieves it in this instance.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            GeneralQueryInterval (number): The amount of time in seconds between IGMP/MLD General Query messages sent by the querier.
            GeneralQueryResponseInterval (number): Indicates the maximum amount of time in milliseconds that the IGMP/MLD querier waits to receive a response to a General Query message. The query response must be lesser than the query interval.
            Name (str): Name of range
            RobustnessVariable (number): Defines the subnet vulnerability to lost packets. IGMP/MLD can recover from robustness variable minus 1 lost IGMP/MLD packets.
            RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
            SpecificQueryResponseCount (number): Indicates the total number of Specific Query messages sent every Specific Query Response Interval seconds before assuming that there is no interested listener for the particular group/source.
            SpecificQueryResponseInterval (number): Indicates the maximum amount of time in milliseconds that the IGMP/MLD Querier waits to receive a response to a Specific Query message. The query response must be lesser than the query interval.
            StartupQueryCount (number): The number of general query messages sent at startup.
            Version (str): IGMP/MLD protocol version.

        Returns:
            self: This instance with all currently retrieved igmpQuerierRange data using find and the newly added igmpQuerierRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the igmpQuerierRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, GeneralQueryInterval=None, GeneralQueryResponseInterval=None, Name=None, ObjectId=None, RobustnessVariable=None, RouterAlert=None, SpecificQueryResponseCount=None, SpecificQueryResponseInterval=None, StartupQueryCount=None, Version=None):
        """Finds and retrieves igmpQuerierRange data from the server.

        All named parameters support regex and can be used to selectively retrieve igmpQuerierRange data from the server.
        By default the find method takes no parameters and will retrieve all igmpQuerierRange data from the server.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            GeneralQueryInterval (number): The amount of time in seconds between IGMP/MLD General Query messages sent by the querier.
            GeneralQueryResponseInterval (number): Indicates the maximum amount of time in milliseconds that the IGMP/MLD querier waits to receive a response to a General Query message. The query response must be lesser than the query interval.
            Name (str): Name of range
            ObjectId (str): Unique identifier for this object
            RobustnessVariable (number): Defines the subnet vulnerability to lost packets. IGMP/MLD can recover from robustness variable minus 1 lost IGMP/MLD packets.
            RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
            SpecificQueryResponseCount (number): Indicates the total number of Specific Query messages sent every Specific Query Response Interval seconds before assuming that there is no interested listener for the particular group/source.
            SpecificQueryResponseInterval (number): Indicates the maximum amount of time in milliseconds that the IGMP/MLD Querier waits to receive a response to a Specific Query message. The query response must be lesser than the query interval.
            StartupQueryCount (number): The number of general query messages sent at startup.
            Version (str): IGMP/MLD protocol version.

        Returns:
            self: This instance with matching igmpQuerierRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of igmpQuerierRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the igmpQuerierRange data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
