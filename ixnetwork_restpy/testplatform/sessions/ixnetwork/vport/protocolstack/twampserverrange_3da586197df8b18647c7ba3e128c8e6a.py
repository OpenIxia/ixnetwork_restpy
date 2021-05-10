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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TwampServerRange(Base):
    """A network stack element representing an RFC 4656 TWAMP Control-Server and Session-Reflector.
    The TwampServerRange class encapsulates a list of twampServerRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the TwampServerRange.find() method.
    The list can be managed by using the TwampServerRange.add() and TwampServerRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'twampServerRange'
    _SDM_ATT_MAP = {
        'NegotiateReflectorPort': 'NegotiateReflectorPort',
        'ControlPort': 'controlPort',
        'Count': 'count',
        'EnableAccessControl': 'enableAccessControl',
        'Enabled': 'enabled',
        'IterationCount': 'iterationCount',
        'KeyId': 'keyId',
        'MaxTestSessions': 'maxTestSessions',
        'Mode': 'mode',
        'Name': 'name',
        'ObjectId': 'objectId',
        'PermittedIp': 'permittedIp',
        'PermittedIpIncrement': 'permittedIpIncrement',
        'PermittedSenderPort': 'permittedSenderPort',
        'ReflectorPort': 'reflectorPort',
        'Secret': 'secret',
    }

    def __init__(self, parent):
        super(TwampServerRange, self).__init__(parent)

    @property
    def NegotiateReflectorPort(self):
        """
        Returns
        -------
        - bool: Negotitate reflector port
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiateReflectorPort'])
    @NegotiateReflectorPort.setter
    def NegotiateReflectorPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NegotiateReflectorPort'], value)

    @property
    def ControlPort(self):
        """
        Returns
        -------
        - number: TWAMP Control-Server TCP port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ControlPort'])
    @ControlPort.setter
    def ControlPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ControlPort'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Maximum number of sessions the TWAMP Server will accept
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def EnableAccessControl(self):
        """
        Returns
        -------
        - bool: Restrict access to the TWAMP server
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAccessControl'])
    @EnableAccessControl.setter
    def EnableAccessControl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAccessControl'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IterationCount(self):
        """
        Returns
        -------
        - number: Iteration count required for password-based key derivation function PBKDF2 (PKCS #5) [RFC2898] Count MUST be a power of 2. Count MUST be at least 1024. Count SHOULD be increased as more computing power becomes common.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IterationCount'])
    @IterationCount.setter
    def IterationCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IterationCount'], value)

    @property
    def KeyId(self):
        """
        Returns
        -------
        - str: Indicates which shared secret the client wishes to use to authenticate or encrypt. [RFC 4656]
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeyId'])
    @KeyId.setter
    def KeyId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['KeyId'], value)

    @property
    def MaxTestSessions(self):
        """
        Returns
        -------
        - number: Maximum number of test sessions the TWAMP Server will accept per control connection
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxTestSessions'])
    @MaxTestSessions.setter
    def MaxTestSessions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxTestSessions'], value)

    @property
    def Mode(self):
        """
        Returns
        -------
        - str: TWAMP mode of operation for the Control and Test Sessions
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mode'])
    @Mode.setter
    def Mode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mode'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def PermittedIp(self):
        """
        Returns
        -------
        - str: IP address from which clients are permitted to access the TWAMP server
        """
        return self._get_attribute(self._SDM_ATT_MAP['PermittedIp'])
    @PermittedIp.setter
    def PermittedIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PermittedIp'], value)

    @property
    def PermittedIpIncrement(self):
        """
        Returns
        -------
        - str: Increment, allowing specification of several permitted client IPs
        """
        return self._get_attribute(self._SDM_ATT_MAP['PermittedIpIncrement'])
    @PermittedIpIncrement.setter
    def PermittedIpIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PermittedIpIncrement'], value)

    @property
    def PermittedSenderPort(self):
        """
        Returns
        -------
        - number: Permitted TWAMP Session-Sender UDP port number, all other will be rejected
        """
        return self._get_attribute(self._SDM_ATT_MAP['PermittedSenderPort'])
    @PermittedSenderPort.setter
    def PermittedSenderPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PermittedSenderPort'], value)

    @property
    def ReflectorPort(self):
        """
        Returns
        -------
        - number: TWAMP Session-Reflector TCP port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReflectorPort'])
    @ReflectorPort.setter
    def ReflectorPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReflectorPort'], value)

    @property
    def Secret(self):
        """
        Returns
        -------
        - str: Shared secret used for key derivation
        """
        return self._get_attribute(self._SDM_ATT_MAP['Secret'])
    @Secret.setter
    def Secret(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Secret'], value)

    def update(self, NegotiateReflectorPort=None, ControlPort=None, Count=None, EnableAccessControl=None, Enabled=None, IterationCount=None, KeyId=None, MaxTestSessions=None, Mode=None, Name=None, PermittedIp=None, PermittedIpIncrement=None, PermittedSenderPort=None, ReflectorPort=None, Secret=None):
        """Updates twampServerRange resource on the server.

        Args
        ----
        - NegotiateReflectorPort (bool): Negotitate reflector port
        - ControlPort (number): TWAMP Control-Server TCP port.
        - Count (number): Maximum number of sessions the TWAMP Server will accept
        - EnableAccessControl (bool): Restrict access to the TWAMP server
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IterationCount (number): Iteration count required for password-based key derivation function PBKDF2 (PKCS #5) [RFC2898] Count MUST be a power of 2. Count MUST be at least 1024. Count SHOULD be increased as more computing power becomes common.
        - KeyId (str): Indicates which shared secret the client wishes to use to authenticate or encrypt. [RFC 4656]
        - MaxTestSessions (number): Maximum number of test sessions the TWAMP Server will accept per control connection
        - Mode (str): TWAMP mode of operation for the Control and Test Sessions
        - Name (str): Name of range
        - PermittedIp (str): IP address from which clients are permitted to access the TWAMP server
        - PermittedIpIncrement (str): Increment, allowing specification of several permitted client IPs
        - PermittedSenderPort (number): Permitted TWAMP Session-Sender UDP port number, all other will be rejected
        - ReflectorPort (number): TWAMP Session-Reflector TCP port.
        - Secret (str): Shared secret used for key derivation

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, NegotiateReflectorPort=None, ControlPort=None, Count=None, EnableAccessControl=None, Enabled=None, IterationCount=None, KeyId=None, MaxTestSessions=None, Mode=None, Name=None, PermittedIp=None, PermittedIpIncrement=None, PermittedSenderPort=None, ReflectorPort=None, Secret=None):
        """Adds a new twampServerRange resource on the server and adds it to the container.

        Args
        ----
        - NegotiateReflectorPort (bool): Negotitate reflector port
        - ControlPort (number): TWAMP Control-Server TCP port.
        - Count (number): Maximum number of sessions the TWAMP Server will accept
        - EnableAccessControl (bool): Restrict access to the TWAMP server
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IterationCount (number): Iteration count required for password-based key derivation function PBKDF2 (PKCS #5) [RFC2898] Count MUST be a power of 2. Count MUST be at least 1024. Count SHOULD be increased as more computing power becomes common.
        - KeyId (str): Indicates which shared secret the client wishes to use to authenticate or encrypt. [RFC 4656]
        - MaxTestSessions (number): Maximum number of test sessions the TWAMP Server will accept per control connection
        - Mode (str): TWAMP mode of operation for the Control and Test Sessions
        - Name (str): Name of range
        - PermittedIp (str): IP address from which clients are permitted to access the TWAMP server
        - PermittedIpIncrement (str): Increment, allowing specification of several permitted client IPs
        - PermittedSenderPort (number): Permitted TWAMP Session-Sender UDP port number, all other will be rejected
        - ReflectorPort (number): TWAMP Session-Reflector TCP port.
        - Secret (str): Shared secret used for key derivation

        Returns
        -------
        - self: This instance with all currently retrieved twampServerRange resources using find and the newly added twampServerRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained twampServerRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, NegotiateReflectorPort=None, ControlPort=None, Count=None, EnableAccessControl=None, Enabled=None, IterationCount=None, KeyId=None, MaxTestSessions=None, Mode=None, Name=None, ObjectId=None, PermittedIp=None, PermittedIpIncrement=None, PermittedSenderPort=None, ReflectorPort=None, Secret=None):
        """Finds and retrieves twampServerRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve twampServerRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all twampServerRange resources from the server.

        Args
        ----
        - NegotiateReflectorPort (bool): Negotitate reflector port
        - ControlPort (number): TWAMP Control-Server TCP port.
        - Count (number): Maximum number of sessions the TWAMP Server will accept
        - EnableAccessControl (bool): Restrict access to the TWAMP server
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IterationCount (number): Iteration count required for password-based key derivation function PBKDF2 (PKCS #5) [RFC2898] Count MUST be a power of 2. Count MUST be at least 1024. Count SHOULD be increased as more computing power becomes common.
        - KeyId (str): Indicates which shared secret the client wishes to use to authenticate or encrypt. [RFC 4656]
        - MaxTestSessions (number): Maximum number of test sessions the TWAMP Server will accept per control connection
        - Mode (str): TWAMP mode of operation for the Control and Test Sessions
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - PermittedIp (str): IP address from which clients are permitted to access the TWAMP server
        - PermittedIpIncrement (str): Increment, allowing specification of several permitted client IPs
        - PermittedSenderPort (number): Permitted TWAMP Session-Sender UDP port number, all other will be rejected
        - ReflectorPort (number): TWAMP Session-Reflector TCP port.
        - Secret (str): Shared secret used for key derivation

        Returns
        -------
        - self: This instance with matching twampServerRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of twampServerRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the twampServerRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
