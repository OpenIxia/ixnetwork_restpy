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


class TwampTestRange(Base):
    """Represents a range of TWAMP Session-Sender.
    The TwampTestRange class encapsulates a list of twampTestRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the TwampTestRange.find() method.
    The list can be managed by the user by using the TwampTestRange.add() and TwampTestRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'twampTestRange'

    def __init__(self, parent):
        super(TwampTestRange, self).__init__(parent)

    @property
    def ControlRangeName(self):
        """Name of the associated TWAMP Control range

        Returns:
            str
        """
        return self._get_attribute('controlRangeName')
    @ControlRangeName.setter
    def ControlRangeName(self, value):
        self._set_attribute('controlRangeName', value)

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
    def Explicit(self):
        """True if the range needs to be created, false if the range was created automatically as first range always is

        Returns:
            bool
        """
        return self._get_attribute('explicit')
    @Explicit.setter
    def Explicit(self, value):
        self._set_attribute('explicit', value)

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
    def NumberOfPackets(self):
        """Number of packets to be sent by the Session-Sender.

        Returns:
            number
        """
        return self._get_attribute('numberOfPackets')
    @NumberOfPackets.setter
    def NumberOfPackets(self, value):
        self._set_attribute('numberOfPackets', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def PacketLength(self):
        """Packet size, including padding length as defined by the RFC4656, in section 3.5

        Returns:
            number
        """
        return self._get_attribute('packetLength')
    @PacketLength.setter
    def PacketLength(self, value):
        self._set_attribute('packetLength', value)

    @property
    def PacketsPerSecond(self):
        """Rate at which packets will be sent.

        Returns:
            number
        """
        return self._get_attribute('packetsPerSecond')
    @PacketsPerSecond.setter
    def PacketsPerSecond(self, value):
        self._set_attribute('packetsPerSecond', value)

    @property
    def PaddingWithZero(self):
        """Per RFC465, data in the packets is random, unless it is configured to be zero

        Returns:
            bool
        """
        return self._get_attribute('paddingWithZero')
    @PaddingWithZero.setter
    def PaddingWithZero(self, value):
        self._set_attribute('paddingWithZero', value)

    @property
    def SessionReflectorPort(self):
        """Port on which the reflector receives the packets from the stream initiated by Session-Sender

        Returns:
            number
        """
        return self._get_attribute('sessionReflectorPort')
    @SessionReflectorPort.setter
    def SessionReflectorPort(self, value):
        self._set_attribute('sessionReflectorPort', value)

    @property
    def SessionReflectorPortIncrement(self):
        """Increment to use for above field when expanding sessions from this range

        Returns:
            number
        """
        return self._get_attribute('sessionReflectorPortIncrement')
    @SessionReflectorPortIncrement.setter
    def SessionReflectorPortIncrement(self, value):
        self._set_attribute('sessionReflectorPortIncrement', value)

    @property
    def SessionSenderPort(self):
        """Source Port of the stream initiated by Session-Sender

        Returns:
            number
        """
        return self._get_attribute('sessionSenderPort')
    @SessionSenderPort.setter
    def SessionSenderPort(self, value):
        self._set_attribute('sessionSenderPort', value)

    @property
    def SessionSenderPortIncrement(self):
        """Increment to use for above field when expanding sessions from this range

        Returns:
            number
        """
        return self._get_attribute('sessionSenderPortIncrement')
    @SessionSenderPortIncrement.setter
    def SessionSenderPortIncrement(self, value):
        self._set_attribute('sessionSenderPortIncrement', value)

    @property
    def TestSessionsCount(self):
        """Number of TWAMP-Test session expanded for each range

        Returns:
            number
        """
        return self._get_attribute('testSessionsCount')
    @TestSessionsCount.setter
    def TestSessionsCount(self, value):
        self._set_attribute('testSessionsCount', value)

    @property
    def Timeout(self):
        """Timeout for receiving packets on Session-Reflector after Stop-Sessions is received, as defined by the TWAMP draft, in section 3.5

        Returns:
            number
        """
        return self._get_attribute('timeout')
    @Timeout.setter
    def Timeout(self, value):
        self._set_attribute('timeout', value)

    @property
    def TypepDescriptor(self):
        """Type-P descriptor sets the Differentiated Services Code Point (DSCP).

        Returns:
            number
        """
        return self._get_attribute('typepDescriptor')
    @TypepDescriptor.setter
    def TypepDescriptor(self, value):
        self._set_attribute('typepDescriptor', value)

    def update(self, ControlRangeName=None, Enabled=None, Explicit=None, Name=None, NumberOfPackets=None, PacketLength=None, PacketsPerSecond=None, PaddingWithZero=None, SessionReflectorPort=None, SessionReflectorPortIncrement=None, SessionSenderPort=None, SessionSenderPortIncrement=None, TestSessionsCount=None, Timeout=None, TypepDescriptor=None):
        """Updates a child instance of twampTestRange on the server.

        Args:
            ControlRangeName (str): Name of the associated TWAMP Control range
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Explicit (bool): True if the range needs to be created, false if the range was created automatically as first range always is
            Name (str): Name of range
            NumberOfPackets (number): Number of packets to be sent by the Session-Sender.
            PacketLength (number): Packet size, including padding length as defined by the RFC4656, in section 3.5
            PacketsPerSecond (number): Rate at which packets will be sent.
            PaddingWithZero (bool): Per RFC465, data in the packets is random, unless it is configured to be zero
            SessionReflectorPort (number): Port on which the reflector receives the packets from the stream initiated by Session-Sender
            SessionReflectorPortIncrement (number): Increment to use for above field when expanding sessions from this range
            SessionSenderPort (number): Source Port of the stream initiated by Session-Sender
            SessionSenderPortIncrement (number): Increment to use for above field when expanding sessions from this range
            TestSessionsCount (number): Number of TWAMP-Test session expanded for each range
            Timeout (number): Timeout for receiving packets on Session-Reflector after Stop-Sessions is received, as defined by the TWAMP draft, in section 3.5
            TypepDescriptor (number): Type-P descriptor sets the Differentiated Services Code Point (DSCP).

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ControlRangeName=None, Enabled=None, Explicit=None, Name=None, NumberOfPackets=None, PacketLength=None, PacketsPerSecond=None, PaddingWithZero=None, SessionReflectorPort=None, SessionReflectorPortIncrement=None, SessionSenderPort=None, SessionSenderPortIncrement=None, TestSessionsCount=None, Timeout=None, TypepDescriptor=None):
        """Adds a new twampTestRange node on the server and retrieves it in this instance.

        Args:
            ControlRangeName (str): Name of the associated TWAMP Control range
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Explicit (bool): True if the range needs to be created, false if the range was created automatically as first range always is
            Name (str): Name of range
            NumberOfPackets (number): Number of packets to be sent by the Session-Sender.
            PacketLength (number): Packet size, including padding length as defined by the RFC4656, in section 3.5
            PacketsPerSecond (number): Rate at which packets will be sent.
            PaddingWithZero (bool): Per RFC465, data in the packets is random, unless it is configured to be zero
            SessionReflectorPort (number): Port on which the reflector receives the packets from the stream initiated by Session-Sender
            SessionReflectorPortIncrement (number): Increment to use for above field when expanding sessions from this range
            SessionSenderPort (number): Source Port of the stream initiated by Session-Sender
            SessionSenderPortIncrement (number): Increment to use for above field when expanding sessions from this range
            TestSessionsCount (number): Number of TWAMP-Test session expanded for each range
            Timeout (number): Timeout for receiving packets on Session-Reflector after Stop-Sessions is received, as defined by the TWAMP draft, in section 3.5
            TypepDescriptor (number): Type-P descriptor sets the Differentiated Services Code Point (DSCP).

        Returns:
            self: This instance with all currently retrieved twampTestRange data using find and the newly added twampTestRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the twampTestRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ControlRangeName=None, Enabled=None, Explicit=None, Name=None, NumberOfPackets=None, ObjectId=None, PacketLength=None, PacketsPerSecond=None, PaddingWithZero=None, SessionReflectorPort=None, SessionReflectorPortIncrement=None, SessionSenderPort=None, SessionSenderPortIncrement=None, TestSessionsCount=None, Timeout=None, TypepDescriptor=None):
        """Finds and retrieves twampTestRange data from the server.

        All named parameters support regex and can be used to selectively retrieve twampTestRange data from the server.
        By default the find method takes no parameters and will retrieve all twampTestRange data from the server.

        Args:
            ControlRangeName (str): Name of the associated TWAMP Control range
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Explicit (bool): True if the range needs to be created, false if the range was created automatically as first range always is
            Name (str): Name of range
            NumberOfPackets (number): Number of packets to be sent by the Session-Sender.
            ObjectId (str): Unique identifier for this object
            PacketLength (number): Packet size, including padding length as defined by the RFC4656, in section 3.5
            PacketsPerSecond (number): Rate at which packets will be sent.
            PaddingWithZero (bool): Per RFC465, data in the packets is random, unless it is configured to be zero
            SessionReflectorPort (number): Port on which the reflector receives the packets from the stream initiated by Session-Sender
            SessionReflectorPortIncrement (number): Increment to use for above field when expanding sessions from this range
            SessionSenderPort (number): Source Port of the stream initiated by Session-Sender
            SessionSenderPortIncrement (number): Increment to use for above field when expanding sessions from this range
            TestSessionsCount (number): Number of TWAMP-Test session expanded for each range
            Timeout (number): Timeout for receiving packets on Session-Reflector after Stop-Sessions is received, as defined by the TWAMP draft, in section 3.5
            TypepDescriptor (number): Type-P descriptor sets the Differentiated Services Code Point (DSCP).

        Returns:
            self: This instance with matching twampTestRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of twampTestRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the twampTestRange data from the server available through an iterator or index

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
