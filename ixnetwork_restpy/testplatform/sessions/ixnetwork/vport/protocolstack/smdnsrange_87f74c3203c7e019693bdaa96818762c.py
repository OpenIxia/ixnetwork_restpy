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


class SmDnsRange(Base):
    """DNS Range
    The SmDnsRange class encapsulates a required smDnsRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'smDnsRange'
    _SDM_ATT_MAP = {
        'CacheReplies': 'cacheReplies',
        'EdnsReceiveBufferSize': 'ednsReceiveBufferSize',
        'Enabled': 'enabled',
        'Name': 'name',
        'ObjectId': 'objectId',
        'ResolveDns': 'resolveDns',
        'ServerIp': 'serverIp',
        'UseAdditionalRecords': 'useAdditionalRecords',
        'UseEdns': 'useEdns',
        'UseTcp': 'useTcp',
    }

    def __init__(self, parent):
        super(SmDnsRange, self).__init__(parent)

    @property
    def CacheReplies(self):
        """
        Returns
        -------
        - bool: Cache DNS Replies
        """
        return self._get_attribute(self._SDM_ATT_MAP['CacheReplies'])
    @CacheReplies.setter
    def CacheReplies(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CacheReplies'], value)

    @property
    def EdnsReceiveBufferSize(self):
        """
        Returns
        -------
        - number: UDP Payload Size
        """
        return self._get_attribute(self._SDM_ATT_MAP['EdnsReceiveBufferSize'])
    @EdnsReceiveBufferSize.setter
    def EdnsReceiveBufferSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EdnsReceiveBufferSize'], value)

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
    def ResolveDns(self):
        """
        Returns
        -------
        - bool: Resolve DNS
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResolveDns'])
    @ResolveDns.setter
    def ResolveDns(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ResolveDns'], value)

    @property
    def ServerIp(self):
        """
        Returns
        -------
        - str: DNS server IP address
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerIp'])
    @ServerIp.setter
    def ServerIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerIp'], value)

    @property
    def UseAdditionalRecords(self):
        """
        Returns
        -------
        - bool: Use Additional Records if included by the server to avoid doing redundant A/AAAA queries
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseAdditionalRecords'])
    @UseAdditionalRecords.setter
    def UseAdditionalRecords(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseAdditionalRecords'], value)

    @property
    def UseEdns(self):
        """
        Returns
        -------
        - bool: Use EDNS
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseEdns'])
    @UseEdns.setter
    def UseEdns(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseEdns'], value)

    @property
    def UseTcp(self):
        """
        Returns
        -------
        - bool: Use TCP connections for DNS queries instead of UDP packets
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseTcp'])
    @UseTcp.setter
    def UseTcp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseTcp'], value)

    def update(self, CacheReplies=None, EdnsReceiveBufferSize=None, Enabled=None, Name=None, ResolveDns=None, ServerIp=None, UseAdditionalRecords=None, UseEdns=None, UseTcp=None):
        """Updates smDnsRange resource on the server.

        Args
        ----
        - CacheReplies (bool): Cache DNS Replies
        - EdnsReceiveBufferSize (number): UDP Payload Size
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): Name of range
        - ResolveDns (bool): Resolve DNS
        - ServerIp (str): DNS server IP address
        - UseAdditionalRecords (bool): Use Additional Records if included by the server to avoid doing redundant A/AAAA queries
        - UseEdns (bool): Use EDNS
        - UseTcp (bool): Use TCP connections for DNS queries instead of UDP packets

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

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