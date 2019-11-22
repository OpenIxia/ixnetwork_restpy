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


class IptvRange(Base):
    """
    The IptvRange class encapsulates a list of iptvRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the IptvRange.find() method.
    The list can be managed by the user by using the IptvRange.add() and IptvRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'iptvRange'

    def __init__(self, parent):
        super(IptvRange, self).__init__(parent)

    @property
    def IptvChannels(self):
        """An instance of the IptvChannels class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iptvchannels_3eba6a9199e4b1f319d0be07a0193d23.IptvChannels)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iptvchannels_3eba6a9199e4b1f319d0be07a0193d23 import IptvChannels
        return IptvChannels(self)

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
    def GeneralQueryResponseMode(self):
        """DEPRECATED If selected, responds to General Query messages.

        Returns:
            bool
        """
        return self._get_attribute('generalQueryResponseMode')
    @GeneralQueryResponseMode.setter
    def GeneralQueryResponseMode(self, value):
        self._set_attribute('generalQueryResponseMode', value)

    @property
    def ImmediateResponse(self):
        """DEPRECATED If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.

        Returns:
            bool
        """
        return self._get_attribute('immediateResponse')
    @ImmediateResponse.setter
    def ImmediateResponse(self, value):
        self._set_attribute('immediateResponse', value)

    @property
    def InterStbStartDelay(self):
        """Time in milliseconds between Join messages from clients within the same range.

        Returns:
            number
        """
        return self._get_attribute('interStbStartDelay')
    @InterStbStartDelay.setter
    def InterStbStartDelay(self, value):
        self._set_attribute('interStbStartDelay', value)

    @property
    def JoinLatencyThreshold(self):
        """The maximum time that is allowed for a multicast stream to arrive for channel for which a Join has been sent.

        Returns:
            number
        """
        return self._get_attribute('joinLatencyThreshold')
    @JoinLatencyThreshold.setter
    def JoinLatencyThreshold(self, value):
        self._set_attribute('joinLatencyThreshold', value)

    @property
    def JoinLeaveMultiplier(self):
        """DEPRECATED The number of times a host sends every Join or Leave message.

        Returns:
            number
        """
        return self._get_attribute('joinLeaveMultiplier')
    @JoinLeaveMultiplier.setter
    def JoinLeaveMultiplier(self, value):
        self._set_attribute('joinLeaveMultiplier', value)

    @property
    def LeaveLatencyThreshold(self):
        """The maximum time allowed for a multicast stream to stop for a channel for which a Leave has been sent.

        Returns:
            number
        """
        return self._get_attribute('leaveLatencyThreshold')
    @LeaveLatencyThreshold.setter
    def LeaveLatencyThreshold(self, value):
        self._set_attribute('leaveLatencyThreshold', value)

    @property
    def LogFailureTimestamps(self):
        """If enabled, the timestamps for Join and Leave failures are saved to a log file.

        Returns:
            bool
        """
        return self._get_attribute('logFailureTimestamps')
    @LogFailureTimestamps.setter
    def LogFailureTimestamps(self, value):
        self._set_attribute('logFailureTimestamps', value)

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
    def ReportFrequency(self):
        """DEPRECATED When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.

        Returns:
            number
        """
        return self._get_attribute('reportFrequency')
    @ReportFrequency.setter
    def ReportFrequency(self, value):
        self._set_attribute('reportFrequency', value)

    @property
    def RouterAlert(self):
        """DEPRECATED If selected, sets the Send Router Alert bit in the IP header.

        Returns:
            bool
        """
        return self._get_attribute('routerAlert')
    @RouterAlert.setter
    def RouterAlert(self, value):
        self._set_attribute('routerAlert', value)

    @property
    def SpecificQueryResponseMode(self):
        """DEPRECATED If selected, responds to Group-Specific Query messages.

        Returns:
            bool
        """
        return self._get_attribute('specificQueryResponseMode')
    @SpecificQueryResponseMode.setter
    def SpecificQueryResponseMode(self, value):
        self._set_attribute('specificQueryResponseMode', value)

    @property
    def StbLeaveJoinDelay(self):
        """Time in milliseconds between sending a Leave for the current channel and Join for the next channel.

        Returns:
            number
        """
        return self._get_attribute('stbLeaveJoinDelay')
    @StbLeaveJoinDelay.setter
    def StbLeaveJoinDelay(self, value):
        self._set_attribute('stbLeaveJoinDelay', value)

    @property
    def UnsolicitedResponseMode(self):
        """DEPRECATED If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.

        Returns:
            bool
        """
        return self._get_attribute('unsolicitedResponseMode')
    @UnsolicitedResponseMode.setter
    def UnsolicitedResponseMode(self, value):
        self._set_attribute('unsolicitedResponseMode', value)

    @property
    def Version(self):
        """DEPRECATED IGMP/MLD protocol version.

        Returns:
            str
        """
        return self._get_attribute('version')
    @Version.setter
    def Version(self, value):
        self._set_attribute('version', value)

    @property
    def ViewingProfile(self):
        """Template describing the behavior of how clients view the lists of channels.

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=iptvProfile)
        """
        return self._get_attribute('viewingProfile')
    @ViewingProfile.setter
    def ViewingProfile(self, value):
        self._set_attribute('viewingProfile', value)

    def update(self, Enabled=None, GeneralQueryResponseMode=None, ImmediateResponse=None, InterStbStartDelay=None, JoinLatencyThreshold=None, JoinLeaveMultiplier=None, LeaveLatencyThreshold=None, LogFailureTimestamps=None, Name=None, ReportFrequency=None, RouterAlert=None, SpecificQueryResponseMode=None, StbLeaveJoinDelay=None, UnsolicitedResponseMode=None, Version=None, ViewingProfile=None):
        """Updates a child instance of iptvRange on the server.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            GeneralQueryResponseMode (bool): If selected, responds to General Query messages.
            ImmediateResponse (bool): If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
            InterStbStartDelay (number): Time in milliseconds between Join messages from clients within the same range.
            JoinLatencyThreshold (number): The maximum time that is allowed for a multicast stream to arrive for channel for which a Join has been sent.
            JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
            LeaveLatencyThreshold (number): The maximum time allowed for a multicast stream to stop for a channel for which a Leave has been sent.
            LogFailureTimestamps (bool): If enabled, the timestamps for Join and Leave failures are saved to a log file.
            Name (str): Name of range
            ReportFrequency (number): When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
            RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
            SpecificQueryResponseMode (bool): If selected, responds to Group-Specific Query messages.
            StbLeaveJoinDelay (number): Time in milliseconds between sending a Leave for the current channel and Join for the next channel.
            UnsolicitedResponseMode (bool): If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
            Version (str): IGMP/MLD protocol version.
            ViewingProfile (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=iptvProfile)): Template describing the behavior of how clients view the lists of channels.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Enabled=None, GeneralQueryResponseMode=None, ImmediateResponse=None, InterStbStartDelay=None, JoinLatencyThreshold=None, JoinLeaveMultiplier=None, LeaveLatencyThreshold=None, LogFailureTimestamps=None, Name=None, ReportFrequency=None, RouterAlert=None, SpecificQueryResponseMode=None, StbLeaveJoinDelay=None, UnsolicitedResponseMode=None, Version=None, ViewingProfile=None):
        """Adds a new iptvRange node on the server and retrieves it in this instance.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            GeneralQueryResponseMode (bool): If selected, responds to General Query messages.
            ImmediateResponse (bool): If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
            InterStbStartDelay (number): Time in milliseconds between Join messages from clients within the same range.
            JoinLatencyThreshold (number): The maximum time that is allowed for a multicast stream to arrive for channel for which a Join has been sent.
            JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
            LeaveLatencyThreshold (number): The maximum time allowed for a multicast stream to stop for a channel for which a Leave has been sent.
            LogFailureTimestamps (bool): If enabled, the timestamps for Join and Leave failures are saved to a log file.
            Name (str): Name of range
            ReportFrequency (number): When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
            RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
            SpecificQueryResponseMode (bool): If selected, responds to Group-Specific Query messages.
            StbLeaveJoinDelay (number): Time in milliseconds between sending a Leave for the current channel and Join for the next channel.
            UnsolicitedResponseMode (bool): If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
            Version (str): IGMP/MLD protocol version.
            ViewingProfile (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=iptvProfile)): Template describing the behavior of how clients view the lists of channels.

        Returns:
            self: This instance with all currently retrieved iptvRange data using find and the newly added iptvRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the iptvRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, GeneralQueryResponseMode=None, ImmediateResponse=None, InterStbStartDelay=None, JoinLatencyThreshold=None, JoinLeaveMultiplier=None, LeaveLatencyThreshold=None, LogFailureTimestamps=None, Name=None, ObjectId=None, ReportFrequency=None, RouterAlert=None, SpecificQueryResponseMode=None, StbLeaveJoinDelay=None, UnsolicitedResponseMode=None, Version=None, ViewingProfile=None):
        """Finds and retrieves iptvRange data from the server.

        All named parameters support regex and can be used to selectively retrieve iptvRange data from the server.
        By default the find method takes no parameters and will retrieve all iptvRange data from the server.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            GeneralQueryResponseMode (bool): If selected, responds to General Query messages.
            ImmediateResponse (bool): If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
            InterStbStartDelay (number): Time in milliseconds between Join messages from clients within the same range.
            JoinLatencyThreshold (number): The maximum time that is allowed for a multicast stream to arrive for channel for which a Join has been sent.
            JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
            LeaveLatencyThreshold (number): The maximum time allowed for a multicast stream to stop for a channel for which a Leave has been sent.
            LogFailureTimestamps (bool): If enabled, the timestamps for Join and Leave failures are saved to a log file.
            Name (str): Name of range
            ObjectId (str): Unique identifier for this object
            ReportFrequency (number): When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
            RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
            SpecificQueryResponseMode (bool): If selected, responds to Group-Specific Query messages.
            StbLeaveJoinDelay (number): Time in milliseconds between sending a Leave for the current channel and Join for the next channel.
            UnsolicitedResponseMode (bool): If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
            Version (str): IGMP/MLD protocol version.
            ViewingProfile (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=iptvProfile)): Template describing the behavior of how clients view the lists of channels.

        Returns:
            self: This instance with matching iptvRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of iptvRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the iptvRange data from the server available through an iterator or index

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

    def IptvStart(self, *args, **kwargs):
        """Executes the iptvStart operation on the server.

        Start IPTV on selected plugins and ranges

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        iptvStart()

        iptvStart(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/iptv,/vport/protocolStack/atm/dhcpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/iptv,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/iptv,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/iptv,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/iptv,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/atm/ipEndpoint/iptv,/vport/protocolStack/atm/ipEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/iptv,/vport/protocolStack/atm/pppoxEndpoint/iptv,/vport/protocolStack/atm/pppoxEndpoint/range/iptvRange,/vport/protocolStack/ethernet/dhcpEndpoint/iptv,/vport/protocolStack/ethernet/dhcpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/iptv,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/iptv,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/iptv,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/iptv,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ipEndpoint/iptv,/vport/protocolStack/ethernet/ipEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/iptv,/vport/protocolStack/ethernet/pppoxEndpoint/iptv,/vport/protocolStack/ethernet/pppoxEndpoint/range/iptvRange]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('iptvStart', payload=payload, response_object=None)

    def IptvStop(self, *args, **kwargs):
        """Executes the iptvStop operation on the server.

        Stop IPTV on selected plugins and ranges

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        iptvStop()

        iptvStop(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/iptv,/vport/protocolStack/atm/dhcpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/iptv,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/iptv,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/iptv,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/iptv,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/atm/ipEndpoint/iptv,/vport/protocolStack/atm/ipEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/iptv,/vport/protocolStack/atm/pppoxEndpoint/iptv,/vport/protocolStack/atm/pppoxEndpoint/range/iptvRange,/vport/protocolStack/ethernet/dhcpEndpoint/iptv,/vport/protocolStack/ethernet/dhcpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/iptv,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/iptv,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/iptv,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/iptv,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ipEndpoint/iptv,/vport/protocolStack/ethernet/ipEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/iptv,/vport/protocolStack/ethernet/pppoxEndpoint/iptv,/vport/protocolStack/ethernet/pppoxEndpoint/range/iptvRange]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('iptvStop', payload=payload, response_object=None)
