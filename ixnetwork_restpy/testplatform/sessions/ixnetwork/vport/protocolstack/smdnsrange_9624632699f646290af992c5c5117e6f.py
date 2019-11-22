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


class SmDnsRange(Base):
    """DNS Range
    The SmDnsRange class encapsulates a required smDnsRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'smDnsRange'

    def __init__(self, parent):
        super(SmDnsRange, self).__init__(parent)

    @property
    def CacheReplies(self):
        """Cache DNS Replies

        Returns:
            bool
        """
        return self._get_attribute('cacheReplies')
    @CacheReplies.setter
    def CacheReplies(self, value):
        self._set_attribute('cacheReplies', value)

    @property
    def EdnsReceiveBufferSize(self):
        """UDP Payload Size

        Returns:
            number
        """
        return self._get_attribute('ednsReceiveBufferSize')
    @EdnsReceiveBufferSize.setter
    def EdnsReceiveBufferSize(self, value):
        self._set_attribute('ednsReceiveBufferSize', value)

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
    def ResolveDns(self):
        """Resolve DNS

        Returns:
            bool
        """
        return self._get_attribute('resolveDns')
    @ResolveDns.setter
    def ResolveDns(self, value):
        self._set_attribute('resolveDns', value)

    @property
    def ServerIp(self):
        """DNS server IP address

        Returns:
            str
        """
        return self._get_attribute('serverIp')
    @ServerIp.setter
    def ServerIp(self, value):
        self._set_attribute('serverIp', value)

    @property
    def UseAdditionalRecords(self):
        """Use Additional Records if included by the server to avoid doing redundant A/AAAA queries

        Returns:
            bool
        """
        return self._get_attribute('useAdditionalRecords')
    @UseAdditionalRecords.setter
    def UseAdditionalRecords(self, value):
        self._set_attribute('useAdditionalRecords', value)

    @property
    def UseEdns(self):
        """Use EDNS

        Returns:
            bool
        """
        return self._get_attribute('useEdns')
    @UseEdns.setter
    def UseEdns(self, value):
        self._set_attribute('useEdns', value)

    @property
    def UseTcp(self):
        """Use TCP connections for DNS queries instead of UDP packets

        Returns:
            bool
        """
        return self._get_attribute('useTcp')
    @UseTcp.setter
    def UseTcp(self, value):
        self._set_attribute('useTcp', value)

    def update(self, CacheReplies=None, EdnsReceiveBufferSize=None, Enabled=None, Name=None, ResolveDns=None, ServerIp=None, UseAdditionalRecords=None, UseEdns=None, UseTcp=None):
        """Updates a child instance of smDnsRange on the server.

        Args:
            CacheReplies (bool): Cache DNS Replies
            EdnsReceiveBufferSize (number): UDP Payload Size
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Name (str): Name of range
            ResolveDns (bool): Resolve DNS
            ServerIp (str): DNS server IP address
            UseAdditionalRecords (bool): Use Additional Records if included by the server to avoid doing redundant A/AAAA queries
            UseEdns (bool): Use EDNS
            UseTcp (bool): Use TCP connections for DNS queries instead of UDP packets

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
