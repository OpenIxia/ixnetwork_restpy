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


class MacRangeMme(Base):
    """Range of multiple MAC addresses for fine grained configuration
    The MacRangeMme class encapsulates a required macRangeMme resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'macRangeMme'

    def __init__(self, parent):
        super(MacRangeMme, self).__init__(parent)

    @property
    def Count(self):
        """The total number of interfaces to be created for the range.

        Returns:
            number
        """
        return self._get_attribute('count')
    @Count.setter
    def Count(self, value):
        self._set_attribute('count', value)

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
    def IncrementBy(self):
        """Incrementor used when the plugin creates a range of MACs.

        Returns:
            str
        """
        return self._get_attribute('incrementBy')
    @IncrementBy.setter
    def IncrementBy(self, value):
        self._set_attribute('incrementBy', value)

    @property
    def Mac(self):
        """Base value used when the plugin creates a MAC address.

        Returns:
            str
        """
        return self._get_attribute('mac')
    @Mac.setter
    def Mac(self, value):
        self._set_attribute('mac', value)

    @property
    def Mtu(self):
        """Maximum Transmission Unit. The largest packet that a given network medium can carry. Ethernet, for example, has a fixed MTU of 1500 bytes without and 9500 bytes with Jumbo frame support. ATM has a fixed MTU of 48 bytes and PPP has a negotiated MTU that is usually between 500 and 2000 bytes.

        Returns:
            number
        """
        return self._get_attribute('mtu')
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute('mtu', value)

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

    def update(self, Count=None, Enabled=None, IncrementBy=None, Mac=None, Mtu=None, Name=None):
        """Updates a child instance of macRangeMme on the server.

        Args:
            Count (number): The total number of interfaces to be created for the range.
            Enabled (bool): Disabled ranges won't be configured nor validated.
            IncrementBy (str): Incrementor used when the plugin creates a range of MACs.
            Mac (str): Base value used when the plugin creates a MAC address.
            Mtu (number): Maximum Transmission Unit. The largest packet that a given network medium can carry. Ethernet, for example, has a fixed MTU of 1500 bytes without and 9500 bytes with Jumbo frame support. ATM has a fixed MTU of 48 bytes and PPP has a negotiated MTU that is usually between 500 and 2000 bytes.
            Name (str): Name of range

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

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
