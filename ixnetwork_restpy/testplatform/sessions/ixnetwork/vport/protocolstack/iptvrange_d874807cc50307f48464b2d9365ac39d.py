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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class IptvRange(Base):
    """
    The IptvRange class encapsulates a list of iptvRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the IptvRange.find() method.
    The list can be managed by using the IptvRange.add() and IptvRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "iptvRange"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "GeneralQueryResponseMode": "generalQueryResponseMode",
        "ImmediateResponse": "immediateResponse",
        "InterStbStartDelay": "interStbStartDelay",
        "JoinLatencyThreshold": "joinLatencyThreshold",
        "JoinLeaveMultiplier": "joinLeaveMultiplier",
        "LeaveLatencyThreshold": "leaveLatencyThreshold",
        "LogFailureTimestamps": "logFailureTimestamps",
        "Name": "name",
        "ObjectId": "objectId",
        "ReportFrequency": "reportFrequency",
        "RouterAlert": "routerAlert",
        "SpecificQueryResponseMode": "specificQueryResponseMode",
        "StbLeaveJoinDelay": "stbLeaveJoinDelay",
        "UnsolicitedResponseMode": "unsolicitedResponseMode",
        "Version": "version",
        "ViewingProfile": "viewingProfile",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IptvRange, self).__init__(parent, list_op)

    @property
    def IptvChannels(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iptvchannels_4c812667c5698b74cefd911419454bf7.IptvChannels): An instance of the IptvChannels class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iptvchannels_4c812667c5698b74cefd911419454bf7 import (
            IptvChannels,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IptvChannels", None) is not None:
                return self._properties.get("IptvChannels")
        return IptvChannels(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def GeneralQueryResponseMode(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If selected, responds to General Query messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GeneralQueryResponseMode"])

    @GeneralQueryResponseMode.setter
    def GeneralQueryResponseMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GeneralQueryResponseMode"], value)

    @property
    def ImmediateResponse(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImmediateResponse"])

    @ImmediateResponse.setter
    def ImmediateResponse(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ImmediateResponse"], value)

    @property
    def InterStbStartDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Time in milliseconds between Join messages from clients within the same range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterStbStartDelay"])

    @InterStbStartDelay.setter
    def InterStbStartDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterStbStartDelay"], value)

    @property
    def JoinLatencyThreshold(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum time that is allowed for a multicast stream to arrive for channel for which a Join has been sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinLatencyThreshold"])

    @JoinLatencyThreshold.setter
    def JoinLatencyThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinLatencyThreshold"], value)

    @property
    def JoinLeaveMultiplier(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: The number of times a host sends every Join or Leave message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinLeaveMultiplier"])

    @JoinLeaveMultiplier.setter
    def JoinLeaveMultiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinLeaveMultiplier"], value)

    @property
    def LeaveLatencyThreshold(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum time allowed for a multicast stream to stop for a channel for which a Leave has been sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LeaveLatencyThreshold"])

    @LeaveLatencyThreshold.setter
    def LeaveLatencyThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LeaveLatencyThreshold"], value)

    @property
    def LogFailureTimestamps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the timestamps for Join and Leave failures are saved to a log file.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LogFailureTimestamps"])

    @LogFailureTimestamps.setter
    def LogFailureTimestamps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LogFailureTimestamps"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    @property
    def ReportFrequency(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportFrequency"])

    @ReportFrequency.setter
    def ReportFrequency(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportFrequency"], value)

    @property
    def RouterAlert(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If selected, sets the Send Router Alert bit in the IP header.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterAlert"])

    @RouterAlert.setter
    def RouterAlert(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterAlert"], value)

    @property
    def SpecificQueryResponseMode(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If selected, responds to Group-Specific Query messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SpecificQueryResponseMode"])

    @SpecificQueryResponseMode.setter
    def SpecificQueryResponseMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SpecificQueryResponseMode"], value)

    @property
    def StbLeaveJoinDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Time in milliseconds between sending a Leave for the current channel and Join for the next channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StbLeaveJoinDelay"])

    @StbLeaveJoinDelay.setter
    def StbLeaveJoinDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StbLeaveJoinDelay"], value)

    @property
    def UnsolicitedResponseMode(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnsolicitedResponseMode"])

    @UnsolicitedResponseMode.setter
    def UnsolicitedResponseMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnsolicitedResponseMode"], value)

    @property
    def Version(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str: IGMP/MLD protocol version.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Version"])

    @Version.setter
    def Version(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Version"], value)

    @property
    def ViewingProfile(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/iptvGlobals/iptvProfile): Template describing the behavior of how clients view the lists of channels.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ViewingProfile"])

    @ViewingProfile.setter
    def ViewingProfile(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ViewingProfile"], value)

    def update(
        self,
        Enabled=None,
        GeneralQueryResponseMode=None,
        ImmediateResponse=None,
        InterStbStartDelay=None,
        JoinLatencyThreshold=None,
        JoinLeaveMultiplier=None,
        LeaveLatencyThreshold=None,
        LogFailureTimestamps=None,
        Name=None,
        ReportFrequency=None,
        RouterAlert=None,
        SpecificQueryResponseMode=None,
        StbLeaveJoinDelay=None,
        UnsolicitedResponseMode=None,
        Version=None,
        ViewingProfile=None,
    ):
        # type: (bool, bool, bool, int, int, int, int, bool, str, int, bool, bool, int, bool, str, str) -> IptvRange
        """Updates iptvRange resource on the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - GeneralQueryResponseMode (bool): If selected, responds to General Query messages.
        - ImmediateResponse (bool): If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
        - InterStbStartDelay (number): Time in milliseconds between Join messages from clients within the same range.
        - JoinLatencyThreshold (number): The maximum time that is allowed for a multicast stream to arrive for channel for which a Join has been sent.
        - JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
        - LeaveLatencyThreshold (number): The maximum time allowed for a multicast stream to stop for a channel for which a Leave has been sent.
        - LogFailureTimestamps (bool): If enabled, the timestamps for Join and Leave failures are saved to a log file.
        - Name (str): Name of range
        - ReportFrequency (number): When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
        - RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
        - SpecificQueryResponseMode (bool): If selected, responds to Group-Specific Query messages.
        - StbLeaveJoinDelay (number): Time in milliseconds between sending a Leave for the current channel and Join for the next channel.
        - UnsolicitedResponseMode (bool): If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
        - Version (str): IGMP/MLD protocol version.
        - ViewingProfile (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/iptvGlobals/iptvProfile)): Template describing the behavior of how clients view the lists of channels.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Enabled=None,
        GeneralQueryResponseMode=None,
        ImmediateResponse=None,
        InterStbStartDelay=None,
        JoinLatencyThreshold=None,
        JoinLeaveMultiplier=None,
        LeaveLatencyThreshold=None,
        LogFailureTimestamps=None,
        Name=None,
        ReportFrequency=None,
        RouterAlert=None,
        SpecificQueryResponseMode=None,
        StbLeaveJoinDelay=None,
        UnsolicitedResponseMode=None,
        Version=None,
        ViewingProfile=None,
    ):
        # type: (bool, bool, bool, int, int, int, int, bool, str, int, bool, bool, int, bool, str, str) -> IptvRange
        """Adds a new iptvRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - GeneralQueryResponseMode (bool): If selected, responds to General Query messages.
        - ImmediateResponse (bool): If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
        - InterStbStartDelay (number): Time in milliseconds between Join messages from clients within the same range.
        - JoinLatencyThreshold (number): The maximum time that is allowed for a multicast stream to arrive for channel for which a Join has been sent.
        - JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
        - LeaveLatencyThreshold (number): The maximum time allowed for a multicast stream to stop for a channel for which a Leave has been sent.
        - LogFailureTimestamps (bool): If enabled, the timestamps for Join and Leave failures are saved to a log file.
        - Name (str): Name of range
        - ReportFrequency (number): When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
        - RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
        - SpecificQueryResponseMode (bool): If selected, responds to Group-Specific Query messages.
        - StbLeaveJoinDelay (number): Time in milliseconds between sending a Leave for the current channel and Join for the next channel.
        - UnsolicitedResponseMode (bool): If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
        - Version (str): IGMP/MLD protocol version.
        - ViewingProfile (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/iptvGlobals/iptvProfile)): Template describing the behavior of how clients view the lists of channels.

        Returns
        -------
        - self: This instance with all currently retrieved iptvRange resources using find and the newly added iptvRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained iptvRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Enabled=None,
        GeneralQueryResponseMode=None,
        ImmediateResponse=None,
        InterStbStartDelay=None,
        JoinLatencyThreshold=None,
        JoinLeaveMultiplier=None,
        LeaveLatencyThreshold=None,
        LogFailureTimestamps=None,
        Name=None,
        ObjectId=None,
        ReportFrequency=None,
        RouterAlert=None,
        SpecificQueryResponseMode=None,
        StbLeaveJoinDelay=None,
        UnsolicitedResponseMode=None,
        Version=None,
        ViewingProfile=None,
    ):
        # type: (bool, bool, bool, int, int, int, int, bool, str, str, int, bool, bool, int, bool, str, str) -> IptvRange
        """Finds and retrieves iptvRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve iptvRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all iptvRange resources from the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - GeneralQueryResponseMode (bool): If selected, responds to General Query messages.
        - ImmediateResponse (bool): If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
        - InterStbStartDelay (number): Time in milliseconds between Join messages from clients within the same range.
        - JoinLatencyThreshold (number): The maximum time that is allowed for a multicast stream to arrive for channel for which a Join has been sent.
        - JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
        - LeaveLatencyThreshold (number): The maximum time allowed for a multicast stream to stop for a channel for which a Leave has been sent.
        - LogFailureTimestamps (bool): If enabled, the timestamps for Join and Leave failures are saved to a log file.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - ReportFrequency (number): When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
        - RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
        - SpecificQueryResponseMode (bool): If selected, responds to Group-Specific Query messages.
        - StbLeaveJoinDelay (number): Time in milliseconds between sending a Leave for the current channel and Join for the next channel.
        - UnsolicitedResponseMode (bool): If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
        - Version (str): IGMP/MLD protocol version.
        - ViewingProfile (str(None | /api/v1/sessions/1/ixnetwork/globals/protocolStack/iptvGlobals/iptvProfile)): Template describing the behavior of how clients view the lists of channels.

        Returns
        -------
        - self: This instance with matching iptvRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of iptvRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the iptvRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "customProtocolStack", payload=payload, response_object=None
        )

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "disableProtocolStack", payload=payload, response_object=None
        )

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "enableProtocolStack", payload=payload, response_object=None
        )

    def IptvStart(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the iptvStart operation on the server.

        Start IPTV on selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        iptvStart(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        iptvStart(Arg2=enum, async_operation=bool)
        ------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/iptv,/vport/protocolStack/atm/dhcpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/iptv,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/iptv,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/iptv,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/iptv,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/atm/ipEndpoint/iptv,/vport/protocolStack/atm/ipEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/iptv,/vport/protocolStack/atm/pppoxEndpoint/iptv,/vport/protocolStack/atm/pppoxEndpoint/range/iptvRange,/vport/protocolStack/ethernet/dhcpEndpoint/iptv,/vport/protocolStack/ethernet/dhcpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/iptv,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/iptv,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/iptv,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/iptv,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ipEndpoint/iptv,/vport/protocolStack/ethernet/ipEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/iptv,/vport/protocolStack/ethernet/pppoxEndpoint/iptv,/vport/protocolStack/ethernet/pppoxEndpoint/range/iptvRange]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("iptvStart", payload=payload, response_object=None)

    def IptvStop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the iptvStop operation on the server.

        Stop IPTV on selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        iptvStop(async_operation=bool)
        ------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        iptvStop(Arg2=enum, async_operation=bool)
        -----------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/iptv,/vport/protocolStack/atm/dhcpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/iptv,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/iptv,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/iptv,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/iptv,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/atm/ipEndpoint/iptv,/vport/protocolStack/atm/ipEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/iptvRange,/vport/protocolStack/atm/pppox/iptv,/vport/protocolStack/atm/pppoxEndpoint/iptv,/vport/protocolStack/atm/pppoxEndpoint/range/iptvRange,/vport/protocolStack/ethernet/dhcpEndpoint/iptv,/vport/protocolStack/ethernet/dhcpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/iptv,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/iptv,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/iptv,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/iptv,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/iptvRange,/vport/protocolStack/ethernet/ipEndpoint/iptv,/vport/protocolStack/ethernet/ipEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/iptvRange,/vport/protocolStack/ethernet/pppox/iptv,/vport/protocolStack/ethernet/pppoxEndpoint/iptv,/vport/protocolStack/ethernet/pppoxEndpoint/range/iptvRange]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("iptvStop", payload=payload, response_object=None)
