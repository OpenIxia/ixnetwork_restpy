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


class RangeList(Base):
    """It lists the range name.
    The RangeList class encapsulates a list of rangeList resources that are managed by the user.
    A list of resources can be retrieved from the server using the RangeList.find() method.
    The list can be managed by using the RangeList.add() and RangeList.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "rangeList"
    _SDM_ATT_MAP = {
        "ChannelListAsString": "channelListAsString",
        "ChannelsList": "channelsList",
        "Enable": "enable",
        "Enabled": "enabled",
        "GeneralQueryResponseMode": "generalQueryResponseMode",
        "ImmediateResponse": "immediateResponse",
        "InterStbStartDelay": "interStbStartDelay",
        "JoinLatencyThreshold": "joinLatencyThreshold",
        "JoinLeaveMultiplier": "joinLeaveMultiplier",
        "LeaveLatencyThreshold": "leaveLatencyThreshold",
        "LogFailureTimestamps": "logFailureTimestamps",
        "Name": "name",
        "PortGroupName": "portGroupName",
        "Protocol": "protocol",
        "RangeName": "rangeName",
        "ReportFrequency": "reportFrequency",
        "RouterAlert": "routerAlert",
        "SaveTimestamps": "saveTimestamps",
        "SpecificQueryResponseMode": "specificQueryResponseMode",
        "StbLeaveJoinDelay": "stbLeaveJoinDelay",
        "UnsolicitedResponseMode": "unsolicitedResponseMode",
        "Version": "version",
        "ViewingProfileAsString": "viewingProfileAsString",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(RangeList, self).__init__(parent, list_op)

    @property
    def IptvChannels(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannels_470de127e37844db81b3b69187dcc060.IptvChannels): An instance of the IptvChannels class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.iptvchannels_470de127e37844db81b3b69187dcc060 import (
            IptvChannels,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IptvChannels", None) is not None:
                return self._properties.get("IptvChannels")
        return IptvChannels(self)

    @property
    def TargetRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.targetrange_b341229c5f88ca72d944dd8e29bb118a.TargetRange): An instance of the TargetRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.targetrange_b341229c5f88ca72d944dd8e29bb118a import (
            TargetRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TargetRange", None) is not None:
                return self._properties.get("TargetRange")
        return TargetRange(self)._select()

    @property
    def ViewingProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.viewingprofile_c2ba4914dfcb3070ec69b2f9a2bc04a5.ViewingProfile): An instance of the ViewingProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.viewingprofile_c2ba4914dfcb3070ec69b2f9a2bc04a5 import (
            ViewingProfile,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ViewingProfile", None) is not None:
                return self._properties.get("ViewingProfile")
        return ViewingProfile(self)._select()

    @property
    def ChannelListAsString(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It channels lists as string.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChannelListAsString"])

    @ChannelListAsString.setter
    def ChannelListAsString(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChannelListAsString"], value)

    @property
    def ChannelsList(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It lists the channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChannelsList"])

    @ChannelsList.setter
    def ChannelsList(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChannelsList"], value)

    @property
    def Enable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it enables the range list.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enable"])

    @Enable.setter
    def Enable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enable"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The range list is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def GeneralQueryResponseMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, responds to General Query messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GeneralQueryResponseMode"])

    @GeneralQueryResponseMode.setter
    def GeneralQueryResponseMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GeneralQueryResponseMode"], value)

    @property
    def ImmediateResponse(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the state machine will ignore the value specified in the Maximum Response Delay in the Membership Query message.
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
        - number: It delays the inter STB start value.
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
        - number: It signifies the joint latency threshold.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinLatencyThreshold"])

    @JoinLatencyThreshold.setter
    def JoinLatencyThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinLatencyThreshold"], value)

    @property
    def JoinLeaveMultiplier(self):
        # type: () -> int
        """
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
        - number: The maximum time, in milliseconds, allowed for a multicast stream to stop for a channel for which a Leave has been sent.
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
        - str: A unique name that IxNetwork assigns to the IPTV range. It is usereditable.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def PortGroupName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies th port group name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortGroupName"])

    @PortGroupName.setter
    def PortGroupName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortGroupName"], value)

    @property
    def Protocol(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies a set of rules and regulation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Protocol"])

    @Protocol.setter
    def Protocol(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Protocol"], value)

    @property
    def RangeName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signfies the range name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeName"])

    @RangeName.setter
    def RangeName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeName"], value)

    @property
    def ReportFrequency(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Can be configured only when the Unsolicited Response Mode option is true.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportFrequency"])

    @ReportFrequency.setter
    def ReportFrequency(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportFrequency"], value)

    @property
    def RouterAlert(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, Send Router Alert is set in the bit in the IP header.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterAlert"])

    @RouterAlert.setter
    def RouterAlert(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterAlert"], value)

    @property
    def SaveTimestamps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the timestamps for Join and Leave messages are saved to a log file.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SaveTimestamps"])

    @SaveTimestamps.setter
    def SaveTimestamps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SaveTimestamps"], value)

    @property
    def SpecificQueryResponseMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Receives a specific query response mode.
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
        - number: It signifies the STB leave and joining delay values.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StbLeaveJoinDelay"])

    @StbLeaveJoinDelay.setter
    def StbLeaveJoinDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StbLeaveJoinDelay"], value)

    @property
    def UnsolicitedResponseMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, causes the emulated host to automatically send full membership messages at regular intervals, without waiting for a query message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnsolicitedResponseMode"])

    @UnsolicitedResponseMode.setter
    def UnsolicitedResponseMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnsolicitedResponseMode"], value)

    @property
    def Version(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The protocol version to use for the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Version"])

    @Version.setter
    def Version(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Version"], value)

    @property
    def ViewingProfileAsString(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the viewing profile as string.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ViewingProfileAsString"])

    @ViewingProfileAsString.setter
    def ViewingProfileAsString(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ViewingProfileAsString"], value)

    def update(
        self,
        ChannelListAsString=None,
        ChannelsList=None,
        Enable=None,
        Enabled=None,
        GeneralQueryResponseMode=None,
        ImmediateResponse=None,
        InterStbStartDelay=None,
        JoinLatencyThreshold=None,
        JoinLeaveMultiplier=None,
        LeaveLatencyThreshold=None,
        LogFailureTimestamps=None,
        Name=None,
        PortGroupName=None,
        Protocol=None,
        RangeName=None,
        ReportFrequency=None,
        RouterAlert=None,
        SaveTimestamps=None,
        SpecificQueryResponseMode=None,
        StbLeaveJoinDelay=None,
        UnsolicitedResponseMode=None,
        Version=None,
        ViewingProfileAsString=None,
    ):
        # type: (str, str, bool, bool, bool, bool, int, int, int, int, bool, str, str, str, str, int, bool, bool, bool, int, bool, str, str) -> RangeList
        """Updates rangeList resource on the server.

        Args
        ----
        - ChannelListAsString (str): It channels lists as string.
        - ChannelsList (str): It lists the channel.
        - Enable (bool): If true, it enables the range list.
        - Enabled (bool): The range list is enabled.
        - GeneralQueryResponseMode (bool): If true, responds to General Query messages.
        - ImmediateResponse (bool): If true, the state machine will ignore the value specified in the Maximum Response Delay in the Membership Query message.
        - InterStbStartDelay (number): It delays the inter STB start value.
        - JoinLatencyThreshold (number): It signifies the joint latency threshold.
        - JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
        - LeaveLatencyThreshold (number): The maximum time, in milliseconds, allowed for a multicast stream to stop for a channel for which a Leave has been sent.
        - LogFailureTimestamps (bool): If enabled, the timestamps for Join and Leave failures are saved to a log file.
        - Name (str): A unique name that IxNetwork assigns to the IPTV range. It is usereditable.
        - PortGroupName (str): It signifies th port group name.
        - Protocol (str): It signifies a set of rules and regulation.
        - RangeName (str): It signfies the range name.
        - ReportFrequency (number): Can be configured only when the Unsolicited Response Mode option is true.
        - RouterAlert (bool): If true, Send Router Alert is set in the bit in the IP header.
        - SaveTimestamps (bool): If enabled, the timestamps for Join and Leave messages are saved to a log file.
        - SpecificQueryResponseMode (bool): Receives a specific query response mode.
        - StbLeaveJoinDelay (number): It signifies the STB leave and joining delay values.
        - UnsolicitedResponseMode (bool): If true, causes the emulated host to automatically send full membership messages at regular intervals, without waiting for a query message.
        - Version (str): The protocol version to use for the range.
        - ViewingProfileAsString (str): It signifies the viewing profile as string.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ChannelListAsString=None,
        ChannelsList=None,
        Enable=None,
        Enabled=None,
        GeneralQueryResponseMode=None,
        ImmediateResponse=None,
        InterStbStartDelay=None,
        JoinLatencyThreshold=None,
        JoinLeaveMultiplier=None,
        LeaveLatencyThreshold=None,
        LogFailureTimestamps=None,
        Name=None,
        PortGroupName=None,
        Protocol=None,
        RangeName=None,
        ReportFrequency=None,
        RouterAlert=None,
        SaveTimestamps=None,
        SpecificQueryResponseMode=None,
        StbLeaveJoinDelay=None,
        UnsolicitedResponseMode=None,
        Version=None,
        ViewingProfileAsString=None,
    ):
        # type: (str, str, bool, bool, bool, bool, int, int, int, int, bool, str, str, str, str, int, bool, bool, bool, int, bool, str, str) -> RangeList
        """Adds a new rangeList resource on the server and adds it to the container.

        Args
        ----
        - ChannelListAsString (str): It channels lists as string.
        - ChannelsList (str): It lists the channel.
        - Enable (bool): If true, it enables the range list.
        - Enabled (bool): The range list is enabled.
        - GeneralQueryResponseMode (bool): If true, responds to General Query messages.
        - ImmediateResponse (bool): If true, the state machine will ignore the value specified in the Maximum Response Delay in the Membership Query message.
        - InterStbStartDelay (number): It delays the inter STB start value.
        - JoinLatencyThreshold (number): It signifies the joint latency threshold.
        - JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
        - LeaveLatencyThreshold (number): The maximum time, in milliseconds, allowed for a multicast stream to stop for a channel for which a Leave has been sent.
        - LogFailureTimestamps (bool): If enabled, the timestamps for Join and Leave failures are saved to a log file.
        - Name (str): A unique name that IxNetwork assigns to the IPTV range. It is usereditable.
        - PortGroupName (str): It signifies th port group name.
        - Protocol (str): It signifies a set of rules and regulation.
        - RangeName (str): It signfies the range name.
        - ReportFrequency (number): Can be configured only when the Unsolicited Response Mode option is true.
        - RouterAlert (bool): If true, Send Router Alert is set in the bit in the IP header.
        - SaveTimestamps (bool): If enabled, the timestamps for Join and Leave messages are saved to a log file.
        - SpecificQueryResponseMode (bool): Receives a specific query response mode.
        - StbLeaveJoinDelay (number): It signifies the STB leave and joining delay values.
        - UnsolicitedResponseMode (bool): If true, causes the emulated host to automatically send full membership messages at regular intervals, without waiting for a query message.
        - Version (str): The protocol version to use for the range.
        - ViewingProfileAsString (str): It signifies the viewing profile as string.

        Returns
        -------
        - self: This instance with all currently retrieved rangeList resources using find and the newly added rangeList resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained rangeList resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ChannelListAsString=None,
        ChannelsList=None,
        Enable=None,
        Enabled=None,
        GeneralQueryResponseMode=None,
        ImmediateResponse=None,
        InterStbStartDelay=None,
        JoinLatencyThreshold=None,
        JoinLeaveMultiplier=None,
        LeaveLatencyThreshold=None,
        LogFailureTimestamps=None,
        Name=None,
        PortGroupName=None,
        Protocol=None,
        RangeName=None,
        ReportFrequency=None,
        RouterAlert=None,
        SaveTimestamps=None,
        SpecificQueryResponseMode=None,
        StbLeaveJoinDelay=None,
        UnsolicitedResponseMode=None,
        Version=None,
        ViewingProfileAsString=None,
    ):
        # type: (str, str, bool, bool, bool, bool, int, int, int, int, bool, str, str, str, str, int, bool, bool, bool, int, bool, str, str) -> RangeList
        """Finds and retrieves rangeList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rangeList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rangeList resources from the server.

        Args
        ----
        - ChannelListAsString (str): It channels lists as string.
        - ChannelsList (str): It lists the channel.
        - Enable (bool): If true, it enables the range list.
        - Enabled (bool): The range list is enabled.
        - GeneralQueryResponseMode (bool): If true, responds to General Query messages.
        - ImmediateResponse (bool): If true, the state machine will ignore the value specified in the Maximum Response Delay in the Membership Query message.
        - InterStbStartDelay (number): It delays the inter STB start value.
        - JoinLatencyThreshold (number): It signifies the joint latency threshold.
        - JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
        - LeaveLatencyThreshold (number): The maximum time, in milliseconds, allowed for a multicast stream to stop for a channel for which a Leave has been sent.
        - LogFailureTimestamps (bool): If enabled, the timestamps for Join and Leave failures are saved to a log file.
        - Name (str): A unique name that IxNetwork assigns to the IPTV range. It is usereditable.
        - PortGroupName (str): It signifies th port group name.
        - Protocol (str): It signifies a set of rules and regulation.
        - RangeName (str): It signfies the range name.
        - ReportFrequency (number): Can be configured only when the Unsolicited Response Mode option is true.
        - RouterAlert (bool): If true, Send Router Alert is set in the bit in the IP header.
        - SaveTimestamps (bool): If enabled, the timestamps for Join and Leave messages are saved to a log file.
        - SpecificQueryResponseMode (bool): Receives a specific query response mode.
        - StbLeaveJoinDelay (number): It signifies the STB leave and joining delay values.
        - UnsolicitedResponseMode (bool): If true, causes the emulated host to automatically send full membership messages at regular intervals, without waiting for a query message.
        - Version (str): The protocol version to use for the range.
        - ViewingProfileAsString (str): It signifies the viewing profile as string.

        Returns
        -------
        - self: This instance with matching rangeList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rangeList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rangeList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("apply", payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("applyAsync", payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool:

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
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

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
        return self._execute("generateReport", payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

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
        return self._execute("run", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("stop", payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

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
        return self._execute("waitForTest", payload=payload, response_object=None)
