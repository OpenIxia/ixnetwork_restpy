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


class TwampTestRange(Base):
    """Represents a range of TWAMP Session-Sender.
    The TwampTestRange class encapsulates a list of twampTestRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the TwampTestRange.find() method.
    The list can be managed by using the TwampTestRange.add() and TwampTestRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "twampTestRange"
    _SDM_ATT_MAP = {
        "NegotiateReflectorPort": "NegotiateReflectorPort",
        "ControlRangeName": "controlRangeName",
        "Enabled": "enabled",
        "Explicit": "explicit",
        "Name": "name",
        "NumberOfPackets": "numberOfPackets",
        "ObjectId": "objectId",
        "PacketLength": "packetLength",
        "PacketsPerSecond": "packetsPerSecond",
        "PaddingWithZero": "paddingWithZero",
        "SessionReflectorPort": "sessionReflectorPort",
        "SessionReflectorPortIncrement": "sessionReflectorPortIncrement",
        "SessionSenderPort": "sessionSenderPort",
        "SessionSenderPortIncrement": "sessionSenderPortIncrement",
        "TestSessionsCount": "testSessionsCount",
        "Timeout": "timeout",
        "TypepDescriptor": "typepDescriptor",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TwampTestRange, self).__init__(parent, list_op)

    @property
    def NegotiateReflectorPort(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Negotitate reflector port
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegotiateReflectorPort"])

    @NegotiateReflectorPort.setter
    def NegotiateReflectorPort(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NegotiateReflectorPort"], value)

    @property
    def ControlRangeName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of the associated TWAMP Control range
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlRangeName"])

    @ControlRangeName.setter
    def ControlRangeName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlRangeName"], value)

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
    def Explicit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: True if the range needs to be created, false if the range was created automatically as first range always is
        """
        return self._get_attribute(self._SDM_ATT_MAP["Explicit"])

    @Explicit.setter
    def Explicit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Explicit"], value)

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
    def NumberOfPackets(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of packets to be sent by the Session-Sender.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfPackets"])

    @NumberOfPackets.setter
    def NumberOfPackets(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfPackets"], value)

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
    def PacketLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Packet size, including padding length as defined by the RFC4656, in section 3.5
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketLength"])

    @PacketLength.setter
    def PacketLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketLength"], value)

    @property
    def PacketsPerSecond(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Rate at which packets will be sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketsPerSecond"])

    @PacketsPerSecond.setter
    def PacketsPerSecond(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketsPerSecond"], value)

    @property
    def PaddingWithZero(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Per RFC465, data in the packets is random, unless it is configured to be zero
        """
        return self._get_attribute(self._SDM_ATT_MAP["PaddingWithZero"])

    @PaddingWithZero.setter
    def PaddingWithZero(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PaddingWithZero"], value)

    @property
    def SessionReflectorPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Port on which the reflector receives the packets from the stream initiated by Session-Sender
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionReflectorPort"])

    @SessionReflectorPort.setter
    def SessionReflectorPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessionReflectorPort"], value)

    @property
    def SessionReflectorPortIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Increment to use for above field when expanding sessions from this range
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionReflectorPortIncrement"])

    @SessionReflectorPortIncrement.setter
    def SessionReflectorPortIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessionReflectorPortIncrement"], value)

    @property
    def SessionSenderPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Source Port of the stream initiated by Session-Sender
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionSenderPort"])

    @SessionSenderPort.setter
    def SessionSenderPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessionSenderPort"], value)

    @property
    def SessionSenderPortIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Increment to use for above field when expanding sessions from this range
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionSenderPortIncrement"])

    @SessionSenderPortIncrement.setter
    def SessionSenderPortIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessionSenderPortIncrement"], value)

    @property
    def TestSessionsCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of TWAMP-Test session expanded for each range
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestSessionsCount"])

    @TestSessionsCount.setter
    def TestSessionsCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestSessionsCount"], value)

    @property
    def Timeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Timeout for receiving packets on Session-Reflector after Stop-Sessions is received, as defined by the TWAMP draft, in section 3.5
        """
        return self._get_attribute(self._SDM_ATT_MAP["Timeout"])

    @Timeout.setter
    def Timeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Timeout"], value)

    @property
    def TypepDescriptor(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Type-P descriptor sets the Differentiated Services Code Point (DSCP).
        """
        return self._get_attribute(self._SDM_ATT_MAP["TypepDescriptor"])

    @TypepDescriptor.setter
    def TypepDescriptor(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TypepDescriptor"], value)

    def update(
        self,
        NegotiateReflectorPort=None,
        ControlRangeName=None,
        Enabled=None,
        Explicit=None,
        Name=None,
        NumberOfPackets=None,
        PacketLength=None,
        PacketsPerSecond=None,
        PaddingWithZero=None,
        SessionReflectorPort=None,
        SessionReflectorPortIncrement=None,
        SessionSenderPort=None,
        SessionSenderPortIncrement=None,
        TestSessionsCount=None,
        Timeout=None,
        TypepDescriptor=None,
    ):
        # type: (bool, str, bool, bool, str, int, int, int, bool, int, int, int, int, int, int, int) -> TwampTestRange
        """Updates twampTestRange resource on the server.

        Args
        ----
        - NegotiateReflectorPort (bool): Negotitate reflector port
        - ControlRangeName (str): Name of the associated TWAMP Control range
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Explicit (bool): True if the range needs to be created, false if the range was created automatically as first range always is
        - Name (str): Name of range
        - NumberOfPackets (number): Number of packets to be sent by the Session-Sender.
        - PacketLength (number): Packet size, including padding length as defined by the RFC4656, in section 3.5
        - PacketsPerSecond (number): Rate at which packets will be sent.
        - PaddingWithZero (bool): Per RFC465, data in the packets is random, unless it is configured to be zero
        - SessionReflectorPort (number): Port on which the reflector receives the packets from the stream initiated by Session-Sender
        - SessionReflectorPortIncrement (number): Increment to use for above field when expanding sessions from this range
        - SessionSenderPort (number): Source Port of the stream initiated by Session-Sender
        - SessionSenderPortIncrement (number): Increment to use for above field when expanding sessions from this range
        - TestSessionsCount (number): Number of TWAMP-Test session expanded for each range
        - Timeout (number): Timeout for receiving packets on Session-Reflector after Stop-Sessions is received, as defined by the TWAMP draft, in section 3.5
        - TypepDescriptor (number): Type-P descriptor sets the Differentiated Services Code Point (DSCP).

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        NegotiateReflectorPort=None,
        ControlRangeName=None,
        Enabled=None,
        Explicit=None,
        Name=None,
        NumberOfPackets=None,
        PacketLength=None,
        PacketsPerSecond=None,
        PaddingWithZero=None,
        SessionReflectorPort=None,
        SessionReflectorPortIncrement=None,
        SessionSenderPort=None,
        SessionSenderPortIncrement=None,
        TestSessionsCount=None,
        Timeout=None,
        TypepDescriptor=None,
    ):
        # type: (bool, str, bool, bool, str, int, int, int, bool, int, int, int, int, int, int, int) -> TwampTestRange
        """Adds a new twampTestRange resource on the server and adds it to the container.

        Args
        ----
        - NegotiateReflectorPort (bool): Negotitate reflector port
        - ControlRangeName (str): Name of the associated TWAMP Control range
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Explicit (bool): True if the range needs to be created, false if the range was created automatically as first range always is
        - Name (str): Name of range
        - NumberOfPackets (number): Number of packets to be sent by the Session-Sender.
        - PacketLength (number): Packet size, including padding length as defined by the RFC4656, in section 3.5
        - PacketsPerSecond (number): Rate at which packets will be sent.
        - PaddingWithZero (bool): Per RFC465, data in the packets is random, unless it is configured to be zero
        - SessionReflectorPort (number): Port on which the reflector receives the packets from the stream initiated by Session-Sender
        - SessionReflectorPortIncrement (number): Increment to use for above field when expanding sessions from this range
        - SessionSenderPort (number): Source Port of the stream initiated by Session-Sender
        - SessionSenderPortIncrement (number): Increment to use for above field when expanding sessions from this range
        - TestSessionsCount (number): Number of TWAMP-Test session expanded for each range
        - Timeout (number): Timeout for receiving packets on Session-Reflector after Stop-Sessions is received, as defined by the TWAMP draft, in section 3.5
        - TypepDescriptor (number): Type-P descriptor sets the Differentiated Services Code Point (DSCP).

        Returns
        -------
        - self: This instance with all currently retrieved twampTestRange resources using find and the newly added twampTestRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained twampTestRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        NegotiateReflectorPort=None,
        ControlRangeName=None,
        Enabled=None,
        Explicit=None,
        Name=None,
        NumberOfPackets=None,
        ObjectId=None,
        PacketLength=None,
        PacketsPerSecond=None,
        PaddingWithZero=None,
        SessionReflectorPort=None,
        SessionReflectorPortIncrement=None,
        SessionSenderPort=None,
        SessionSenderPortIncrement=None,
        TestSessionsCount=None,
        Timeout=None,
        TypepDescriptor=None,
    ):
        # type: (bool, str, bool, bool, str, int, str, int, int, bool, int, int, int, int, int, int, int) -> TwampTestRange
        """Finds and retrieves twampTestRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve twampTestRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all twampTestRange resources from the server.

        Args
        ----
        - NegotiateReflectorPort (bool): Negotitate reflector port
        - ControlRangeName (str): Name of the associated TWAMP Control range
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Explicit (bool): True if the range needs to be created, false if the range was created automatically as first range always is
        - Name (str): Name of range
        - NumberOfPackets (number): Number of packets to be sent by the Session-Sender.
        - ObjectId (str): Unique identifier for this object
        - PacketLength (number): Packet size, including padding length as defined by the RFC4656, in section 3.5
        - PacketsPerSecond (number): Rate at which packets will be sent.
        - PaddingWithZero (bool): Per RFC465, data in the packets is random, unless it is configured to be zero
        - SessionReflectorPort (number): Port on which the reflector receives the packets from the stream initiated by Session-Sender
        - SessionReflectorPortIncrement (number): Increment to use for above field when expanding sessions from this range
        - SessionSenderPort (number): Source Port of the stream initiated by Session-Sender
        - SessionSenderPortIncrement (number): Increment to use for above field when expanding sessions from this range
        - TestSessionsCount (number): Number of TWAMP-Test session expanded for each range
        - Timeout (number): Timeout for receiving packets on Session-Reflector after Stop-Sessions is received, as defined by the TWAMP draft, in section 3.5
        - TypepDescriptor (number): Type-P descriptor sets the Differentiated Services Code Point (DSCP).

        Returns
        -------
        - self: This instance with matching twampTestRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of twampTestRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the twampTestRange resources from the server available through an iterator or index

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

    def TwampDeleteTestRange(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the twampDeleteTestRange operation on the server.

        Deletes a Test Range Object

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        twampDeleteTestRange(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        twampDeleteTestRange(Arg2=enum, async_operation=bool)
        -----------------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/twampTestRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampTestRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampTestRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampTestRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/twampTestRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampTestRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampTestRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampTestRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/twampTestRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/twampTestRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/twampTestRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/twampTestRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/twampTestRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/twampTestRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/twampTestRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/twampTestRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/twampTestRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/twampTestRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/twampTestRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/twampTestRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/twampTestRange,/vport/protocolStack/atm/ipEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/twampTestRange,/vport/protocolStack/ethernet/ipEndpoint/range/twampTestRange]
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
            "twampDeleteTestRange", payload=payload, response_object=None
        )
