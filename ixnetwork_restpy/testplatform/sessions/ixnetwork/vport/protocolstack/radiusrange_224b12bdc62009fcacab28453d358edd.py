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


class RadiusRange(Base):
    """Represents a RADIUS range.
    The RadiusRange class encapsulates a list of radiusRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the RadiusRange.find() method.
    The list can be managed by the user by using the RadiusRange.add() and RadiusRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'radiusRange'

    def __init__(self, parent):
        super(RadiusRange, self).__init__(parent)

    @property
    def AccountingPort(self):
        """Accounting UDP port

        Returns:
            number
        """
        return self._get_attribute('accountingPort')
    @AccountingPort.setter
    def AccountingPort(self, value):
        self._set_attribute('accountingPort', value)

    @property
    def AccountingServer(self):
        """RADIUS Accounting Server, specified as IP address

        Returns:
            str
        """
        return self._get_attribute('accountingServer')
    @AccountingServer.setter
    def AccountingServer(self, value):
        self._set_attribute('accountingServer', value)

    @property
    def AuthenticationPort(self):
        """Authentication UDP port

        Returns:
            number
        """
        return self._get_attribute('authenticationPort')
    @AuthenticationPort.setter
    def AuthenticationPort(self, value):
        self._set_attribute('authenticationPort', value)

    @property
    def AuthenticationServer(self):
        """RADIUS Authentication Server, specified as IP address

        Returns:
            str
        """
        return self._get_attribute('authenticationServer')
    @AuthenticationServer.setter
    def AuthenticationServer(self, value):
        self._set_attribute('authenticationServer', value)

    @property
    def EnableAccounting(self):
        """Enables support for RADIUS accounting

        Returns:
            bool
        """
        return self._get_attribute('enableAccounting')
    @EnableAccounting.setter
    def EnableAccounting(self, value):
        self._set_attribute('enableAccounting', value)

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
    def Retries(self):
        """RADIUS retry value

        Returns:
            number
        """
        return self._get_attribute('retries')
    @Retries.setter
    def Retries(self, value):
        self._set_attribute('retries', value)

    @property
    def Secret(self):
        """Shared secret used by Ixia RADIUS client and RADIUS server

        Returns:
            str
        """
        return self._get_attribute('secret')
    @Secret.setter
    def Secret(self, value):
        self._set_attribute('secret', value)

    @property
    def Timeout(self):
        """RADIUS timeout value

        Returns:
            number
        """
        return self._get_attribute('timeout')
    @Timeout.setter
    def Timeout(self, value):
        self._set_attribute('timeout', value)

    @property
    def TunnelAttributeSet(self):
        """Defines the RADIUS tunnel attributes

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=dhcpOptionSet)
        """
        return self._get_attribute('tunnelAttributeSet')
    @TunnelAttributeSet.setter
    def TunnelAttributeSet(self, value):
        self._set_attribute('tunnelAttributeSet', value)

    def update(self, AccountingPort=None, AccountingServer=None, AuthenticationPort=None, AuthenticationServer=None, EnableAccounting=None, Enabled=None, Name=None, Retries=None, Secret=None, Timeout=None, TunnelAttributeSet=None):
        """Updates a child instance of radiusRange on the server.

        Args:
            AccountingPort (number): Accounting UDP port
            AccountingServer (str): RADIUS Accounting Server, specified as IP address
            AuthenticationPort (number): Authentication UDP port
            AuthenticationServer (str): RADIUS Authentication Server, specified as IP address
            EnableAccounting (bool): Enables support for RADIUS accounting
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Name (str): Name of range
            Retries (number): RADIUS retry value
            Secret (str): Shared secret used by Ixia RADIUS client and RADIUS server
            Timeout (number): RADIUS timeout value
            TunnelAttributeSet (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=dhcpOptionSet)): Defines the RADIUS tunnel attributes

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AccountingPort=None, AccountingServer=None, AuthenticationPort=None, AuthenticationServer=None, EnableAccounting=None, Enabled=None, Name=None, Retries=None, Secret=None, Timeout=None, TunnelAttributeSet=None):
        """Adds a new radiusRange node on the server and retrieves it in this instance.

        Args:
            AccountingPort (number): Accounting UDP port
            AccountingServer (str): RADIUS Accounting Server, specified as IP address
            AuthenticationPort (number): Authentication UDP port
            AuthenticationServer (str): RADIUS Authentication Server, specified as IP address
            EnableAccounting (bool): Enables support for RADIUS accounting
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Name (str): Name of range
            Retries (number): RADIUS retry value
            Secret (str): Shared secret used by Ixia RADIUS client and RADIUS server
            Timeout (number): RADIUS timeout value
            TunnelAttributeSet (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=dhcpOptionSet)): Defines the RADIUS tunnel attributes

        Returns:
            self: This instance with all currently retrieved radiusRange data using find and the newly added radiusRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the radiusRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AccountingPort=None, AccountingServer=None, AuthenticationPort=None, AuthenticationServer=None, EnableAccounting=None, Enabled=None, Name=None, ObjectId=None, Retries=None, Secret=None, Timeout=None, TunnelAttributeSet=None):
        """Finds and retrieves radiusRange data from the server.

        All named parameters support regex and can be used to selectively retrieve radiusRange data from the server.
        By default the find method takes no parameters and will retrieve all radiusRange data from the server.

        Args:
            AccountingPort (number): Accounting UDP port
            AccountingServer (str): RADIUS Accounting Server, specified as IP address
            AuthenticationPort (number): Authentication UDP port
            AuthenticationServer (str): RADIUS Authentication Server, specified as IP address
            EnableAccounting (bool): Enables support for RADIUS accounting
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Name (str): Name of range
            ObjectId (str): Unique identifier for this object
            Retries (number): RADIUS retry value
            Secret (str): Shared secret used by Ixia RADIUS client and RADIUS server
            Timeout (number): RADIUS timeout value
            TunnelAttributeSet (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=dhcpOptionSet)): Defines the RADIUS tunnel attributes

        Returns:
            self: This instance with matching radiusRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of radiusRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the radiusRange data from the server available through an iterator or index

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
