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


class IgmpMldRange(Base):
    """
    The IgmpMldRange class encapsulates a list of igmpMldRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the IgmpMldRange.find() method.
    The list can be managed by the user by using the IgmpMldRange.add() and IgmpMldRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'igmpMldRange'

    def __init__(self, parent):
        super(IgmpMldRange, self).__init__(parent)

    @property
    def JoinLeaveMulticastGroupRange(self):
        """An instance of the JoinLeaveMulticastGroupRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.joinleavemulticastgrouprange_78f2e56db214d9c5dc2e322c31b3eb36.JoinLeaveMulticastGroupRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.joinleavemulticastgrouprange_78f2e56db214d9c5dc2e322c31b3eb36 import JoinLeaveMulticastGroupRange
        return JoinLeaveMulticastGroupRange(self)

    @property
    def MulticastGroupRange(self):
        """An instance of the MulticastGroupRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.multicastgrouprange_d2776c629e203f6b9698391d7ab4289d.MulticastGroupRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.multicastgrouprange_d2776c629e203f6b9698391d7ab4289d import MulticastGroupRange
        return MulticastGroupRange(self)

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
        """If selected, responds to General Query messages.

        Returns:
            bool
        """
        return self._get_attribute('generalQueryResponseMode')
    @GeneralQueryResponseMode.setter
    def GeneralQueryResponseMode(self, value):
        self._set_attribute('generalQueryResponseMode', value)

    @property
    def ImmediateResponse(self):
        """If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.

        Returns:
            bool
        """
        return self._get_attribute('immediateResponse')
    @ImmediateResponse.setter
    def ImmediateResponse(self, value):
        self._set_attribute('immediateResponse', value)

    @property
    def JoinLeaveMultiplier(self):
        """The number of times a host sends every Join or Leave message.

        Returns:
            number
        """
        return self._get_attribute('joinLeaveMultiplier')
    @JoinLeaveMultiplier.setter
    def JoinLeaveMultiplier(self, value):
        self._set_attribute('joinLeaveMultiplier', value)

    @property
    def MeshingMode(self):
        """Defines how the hosts in a range join the selected multicast group ranges.

        Returns:
            str
        """
        return self._get_attribute('meshingMode')
    @MeshingMode.setter
    def MeshingMode(self, value):
        self._set_attribute('meshingMode', value)

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
        """When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.

        Returns:
            number
        """
        return self._get_attribute('reportFrequency')
    @ReportFrequency.setter
    def ReportFrequency(self, value):
        self._set_attribute('reportFrequency', value)

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
    def SpecificQueryResponseMode(self):
        """If selected, responds to Group-Specific Query messages.

        Returns:
            bool
        """
        return self._get_attribute('specificQueryResponseMode')
    @SpecificQueryResponseMode.setter
    def SpecificQueryResponseMode(self, value):
        self._set_attribute('specificQueryResponseMode', value)

    @property
    def UnsolicitedResponseMode(self):
        """If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.

        Returns:
            bool
        """
        return self._get_attribute('unsolicitedResponseMode')
    @UnsolicitedResponseMode.setter
    def UnsolicitedResponseMode(self, value):
        self._set_attribute('unsolicitedResponseMode', value)

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

    def update(self, Enabled=None, GeneralQueryResponseMode=None, ImmediateResponse=None, JoinLeaveMultiplier=None, MeshingMode=None, Name=None, ReportFrequency=None, RouterAlert=None, SpecificQueryResponseMode=None, UnsolicitedResponseMode=None, Version=None):
        """Updates a child instance of igmpMldRange on the server.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            GeneralQueryResponseMode (bool): If selected, responds to General Query messages.
            ImmediateResponse (bool): If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
            JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
            MeshingMode (str): Defines how the hosts in a range join the selected multicast group ranges.
            Name (str): Name of range
            ReportFrequency (number): When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
            RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
            SpecificQueryResponseMode (bool): If selected, responds to Group-Specific Query messages.
            UnsolicitedResponseMode (bool): If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
            Version (str): IGMP/MLD protocol version.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Enabled=None, GeneralQueryResponseMode=None, ImmediateResponse=None, JoinLeaveMultiplier=None, MeshingMode=None, Name=None, ReportFrequency=None, RouterAlert=None, SpecificQueryResponseMode=None, UnsolicitedResponseMode=None, Version=None):
        """Adds a new igmpMldRange node on the server and retrieves it in this instance.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            GeneralQueryResponseMode (bool): If selected, responds to General Query messages.
            ImmediateResponse (bool): If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
            JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
            MeshingMode (str): Defines how the hosts in a range join the selected multicast group ranges.
            Name (str): Name of range
            ReportFrequency (number): When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
            RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
            SpecificQueryResponseMode (bool): If selected, responds to Group-Specific Query messages.
            UnsolicitedResponseMode (bool): If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
            Version (str): IGMP/MLD protocol version.

        Returns:
            self: This instance with all currently retrieved igmpMldRange data using find and the newly added igmpMldRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the igmpMldRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, GeneralQueryResponseMode=None, ImmediateResponse=None, JoinLeaveMultiplier=None, MeshingMode=None, Name=None, ObjectId=None, ReportFrequency=None, RouterAlert=None, SpecificQueryResponseMode=None, UnsolicitedResponseMode=None, Version=None):
        """Finds and retrieves igmpMldRange data from the server.

        All named parameters support regex and can be used to selectively retrieve igmpMldRange data from the server.
        By default the find method takes no parameters and will retrieve all igmpMldRange data from the server.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            GeneralQueryResponseMode (bool): If selected, responds to General Query messages.
            ImmediateResponse (bool): If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
            JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
            MeshingMode (str): Defines how the hosts in a range join the selected multicast group ranges.
            Name (str): Name of range
            ObjectId (str): Unique identifier for this object
            ReportFrequency (number): When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
            RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
            SpecificQueryResponseMode (bool): If selected, responds to Group-Specific Query messages.
            UnsolicitedResponseMode (bool): If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
            Version (str): IGMP/MLD protocol version.

        Returns:
            self: This instance with matching igmpMldRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of igmpMldRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the igmpMldRange data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self):
        """Executes the apply operation on the server.

        Apply changes for on the fly configuration support.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('apply', payload=payload, response_object=None)

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

    def IgmpMldJoin(self, *args, **kwargs):
        """Executes the igmpMldJoin operation on the server.

        Join IGMP/MLD multicast group ranges on the fly

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        igmpMldJoin()

        igmpMldJoin(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/igmpMld,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/igmpMld,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ipEndpoint/igmpMld,/vport/protocolStack/atm/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/igmpMld,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/range/igmpMldRange]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpMldJoin', payload=payload, response_object=None)

    def IgmpMldLeave(self, *args, **kwargs):
        """Executes the igmpMldLeave operation on the server.

        Leave IGMP/MLD multicast group ranges on the fly

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        igmpMldLeave()

        igmpMldLeave(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/igmpMld,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/igmpMld,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ipEndpoint/igmpMld,/vport/protocolStack/atm/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/igmpMld,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/range/igmpMldRange]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpMldLeave', payload=payload, response_object=None)

    def IgmpMldStart(self, *args, **kwargs):
        """Executes the igmpMldStart operation on the server.

        Start IGMP/MLD on selected plugins and ranges

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        igmpMldStart()

        igmpMldStart(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/igmpMld,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/igmpMld,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ipEndpoint/igmpMld,/vport/protocolStack/atm/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/igmpMld,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/range/igmpMldRange]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpMldStart', payload=payload, response_object=None)

    def IgmpMldStop(self, *args, **kwargs):
        """Executes the igmpMldStop operation on the server.

        Stop IGMP/MLD on selected plugins and ranges

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        igmpMldStop()

        igmpMldStop(Arg2:enum)
            Args:
                args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/igmpMld,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/igmpMld,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ipEndpoint/igmpMld,/vport/protocolStack/atm/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/igmpMld,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/range/igmpMldRange]

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpMldStop', payload=payload, response_object=None)
