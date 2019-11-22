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


class TwampServerRange(Base):
    """A network stack element representing an RFC 4656 TWAMP Control-Server and Session-Reflector.
    The TwampServerRange class encapsulates a list of twampServerRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the TwampServerRange.find() method.
    The list can be managed by the user by using the TwampServerRange.add() and TwampServerRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'twampServerRange'

    def __init__(self, parent):
        super(TwampServerRange, self).__init__(parent)

    @property
    def ControlPort(self):
        """TWAMP Control-Server TCP port.

        Returns:
            number
        """
        return self._get_attribute('controlPort')
    @ControlPort.setter
    def ControlPort(self, value):
        self._set_attribute('controlPort', value)

    @property
    def Count(self):
        """Maximum number of sessions the TWAMP Server will accept

        Returns:
            number
        """
        return self._get_attribute('count')
    @Count.setter
    def Count(self, value):
        self._set_attribute('count', value)

    @property
    def EnableAccessControl(self):
        """Restrict access to the TWAMP server

        Returns:
            bool
        """
        return self._get_attribute('enableAccessControl')
    @EnableAccessControl.setter
    def EnableAccessControl(self, value):
        self._set_attribute('enableAccessControl', value)

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
    def IterationCount(self):
        """Iteration count required for password-based key derivation function PBKDF2 (PKCS #5) [RFC2898] Count MUST be a power of 2. Count MUST be at least 1024. Count SHOULD be increased as more computing power becomes common.

        Returns:
            number
        """
        return self._get_attribute('iterationCount')
    @IterationCount.setter
    def IterationCount(self, value):
        self._set_attribute('iterationCount', value)

    @property
    def KeyId(self):
        """Indicates which shared secret the client wishes to use to authenticate or encrypt. [RFC 4656]

        Returns:
            str
        """
        return self._get_attribute('keyId')
    @KeyId.setter
    def KeyId(self, value):
        self._set_attribute('keyId', value)

    @property
    def MaxTestSessions(self):
        """Maximum number of test sessions the TWAMP Server will accept per control connection

        Returns:
            number
        """
        return self._get_attribute('maxTestSessions')
    @MaxTestSessions.setter
    def MaxTestSessions(self, value):
        self._set_attribute('maxTestSessions', value)

    @property
    def Mode(self):
        """TWAMP mode of operation for the Control and Test Sessions

        Returns:
            str
        """
        return self._get_attribute('mode')
    @Mode.setter
    def Mode(self, value):
        self._set_attribute('mode', value)

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
    def PermittedIp(self):
        """IP address from which clients are permitted to access the TWAMP server

        Returns:
            str
        """
        return self._get_attribute('permittedIp')
    @PermittedIp.setter
    def PermittedIp(self, value):
        self._set_attribute('permittedIp', value)

    @property
    def PermittedIpIncrement(self):
        """Increment, allowing specification of several permitted client IPs

        Returns:
            str
        """
        return self._get_attribute('permittedIpIncrement')
    @PermittedIpIncrement.setter
    def PermittedIpIncrement(self, value):
        self._set_attribute('permittedIpIncrement', value)

    @property
    def PermittedSenderPort(self):
        """Permitted TWAMP Session-Sender UDP port number, all other will be rejected

        Returns:
            number
        """
        return self._get_attribute('permittedSenderPort')
    @PermittedSenderPort.setter
    def PermittedSenderPort(self, value):
        self._set_attribute('permittedSenderPort', value)

    @property
    def ReflectorPort(self):
        """TWAMP Session-Reflector TCP port.

        Returns:
            number
        """
        return self._get_attribute('reflectorPort')
    @ReflectorPort.setter
    def ReflectorPort(self, value):
        self._set_attribute('reflectorPort', value)

    @property
    def Secret(self):
        """Shared secret used for key derivation

        Returns:
            str
        """
        return self._get_attribute('secret')
    @Secret.setter
    def Secret(self, value):
        self._set_attribute('secret', value)

    def update(self, ControlPort=None, Count=None, EnableAccessControl=None, Enabled=None, IterationCount=None, KeyId=None, MaxTestSessions=None, Mode=None, Name=None, PermittedIp=None, PermittedIpIncrement=None, PermittedSenderPort=None, ReflectorPort=None, Secret=None):
        """Updates a child instance of twampServerRange on the server.

        Args:
            ControlPort (number): TWAMP Control-Server TCP port.
            Count (number): Maximum number of sessions the TWAMP Server will accept
            EnableAccessControl (bool): Restrict access to the TWAMP server
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IterationCount (number): Iteration count required for password-based key derivation function PBKDF2 (PKCS #5) [RFC2898] Count MUST be a power of 2. Count MUST be at least 1024. Count SHOULD be increased as more computing power becomes common.
            KeyId (str): Indicates which shared secret the client wishes to use to authenticate or encrypt. [RFC 4656]
            MaxTestSessions (number): Maximum number of test sessions the TWAMP Server will accept per control connection
            Mode (str): TWAMP mode of operation for the Control and Test Sessions
            Name (str): Name of range
            PermittedIp (str): IP address from which clients are permitted to access the TWAMP server
            PermittedIpIncrement (str): Increment, allowing specification of several permitted client IPs
            PermittedSenderPort (number): Permitted TWAMP Session-Sender UDP port number, all other will be rejected
            ReflectorPort (number): TWAMP Session-Reflector TCP port.
            Secret (str): Shared secret used for key derivation

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ControlPort=None, Count=None, EnableAccessControl=None, Enabled=None, IterationCount=None, KeyId=None, MaxTestSessions=None, Mode=None, Name=None, PermittedIp=None, PermittedIpIncrement=None, PermittedSenderPort=None, ReflectorPort=None, Secret=None):
        """Adds a new twampServerRange node on the server and retrieves it in this instance.

        Args:
            ControlPort (number): TWAMP Control-Server TCP port.
            Count (number): Maximum number of sessions the TWAMP Server will accept
            EnableAccessControl (bool): Restrict access to the TWAMP server
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IterationCount (number): Iteration count required for password-based key derivation function PBKDF2 (PKCS #5) [RFC2898] Count MUST be a power of 2. Count MUST be at least 1024. Count SHOULD be increased as more computing power becomes common.
            KeyId (str): Indicates which shared secret the client wishes to use to authenticate or encrypt. [RFC 4656]
            MaxTestSessions (number): Maximum number of test sessions the TWAMP Server will accept per control connection
            Mode (str): TWAMP mode of operation for the Control and Test Sessions
            Name (str): Name of range
            PermittedIp (str): IP address from which clients are permitted to access the TWAMP server
            PermittedIpIncrement (str): Increment, allowing specification of several permitted client IPs
            PermittedSenderPort (number): Permitted TWAMP Session-Sender UDP port number, all other will be rejected
            ReflectorPort (number): TWAMP Session-Reflector TCP port.
            Secret (str): Shared secret used for key derivation

        Returns:
            self: This instance with all currently retrieved twampServerRange data using find and the newly added twampServerRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the twampServerRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ControlPort=None, Count=None, EnableAccessControl=None, Enabled=None, IterationCount=None, KeyId=None, MaxTestSessions=None, Mode=None, Name=None, ObjectId=None, PermittedIp=None, PermittedIpIncrement=None, PermittedSenderPort=None, ReflectorPort=None, Secret=None):
        """Finds and retrieves twampServerRange data from the server.

        All named parameters support regex and can be used to selectively retrieve twampServerRange data from the server.
        By default the find method takes no parameters and will retrieve all twampServerRange data from the server.

        Args:
            ControlPort (number): TWAMP Control-Server TCP port.
            Count (number): Maximum number of sessions the TWAMP Server will accept
            EnableAccessControl (bool): Restrict access to the TWAMP server
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IterationCount (number): Iteration count required for password-based key derivation function PBKDF2 (PKCS #5) [RFC2898] Count MUST be a power of 2. Count MUST be at least 1024. Count SHOULD be increased as more computing power becomes common.
            KeyId (str): Indicates which shared secret the client wishes to use to authenticate or encrypt. [RFC 4656]
            MaxTestSessions (number): Maximum number of test sessions the TWAMP Server will accept per control connection
            Mode (str): TWAMP mode of operation for the Control and Test Sessions
            Name (str): Name of range
            ObjectId (str): Unique identifier for this object
            PermittedIp (str): IP address from which clients are permitted to access the TWAMP server
            PermittedIpIncrement (str): Increment, allowing specification of several permitted client IPs
            PermittedSenderPort (number): Permitted TWAMP Session-Sender UDP port number, all other will be rejected
            ReflectorPort (number): TWAMP Session-Reflector TCP port.
            Secret (str): Shared secret used for key derivation

        Returns:
            self: This instance with matching twampServerRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of twampServerRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the twampServerRange data from the server available through an iterator or index

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
