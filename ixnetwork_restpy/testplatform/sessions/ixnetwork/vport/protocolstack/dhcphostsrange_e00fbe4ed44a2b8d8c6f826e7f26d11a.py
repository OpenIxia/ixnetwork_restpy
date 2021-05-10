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


class DhcpHostsRange(Base):
    """Manages a range of IP addresses that are configured using DHCP protocol.
    The DhcpHostsRange class encapsulates a required dhcpHostsRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpHostsRange'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'Enabled': 'enabled',
        'EuiIncrement': 'euiIncrement',
        'FirstEui': 'firstEui',
        'IpPrefix': 'ipPrefix',
        'IpType': 'ipType',
        'Name': 'name',
        'ObjectId': 'objectId',
        'SubnetCount': 'subnetCount',
    }

    def __init__(self, parent):
        super(DhcpHostsRange, self).__init__(parent)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The number of hosts
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

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
    def EuiIncrement(self):
        """
        Returns
        -------
        - str: Defines the EUI increment.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EuiIncrement'])
    @EuiIncrement.setter
    def EuiIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EuiIncrement'], value)

    @property
    def FirstEui(self):
        """
        Returns
        -------
        - str: Defines the first EUI to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstEui'])
    @FirstEui.setter
    def FirstEui(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstEui'], value)

    @property
    def IpPrefix(self):
        """
        Returns
        -------
        - number: The network prefix length associated with this address pool.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpPrefix'])
    @IpPrefix.setter
    def IpPrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpPrefix'], value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - str: The IP version to be used for describing the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpType'])
    @IpType.setter
    def IpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpType'], value)

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
    def SubnetCount(self):
        """
        Returns
        -------
        - number: The number of subnets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SubnetCount'])
    @SubnetCount.setter
    def SubnetCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SubnetCount'], value)

    def update(self, Count=None, Enabled=None, EuiIncrement=None, FirstEui=None, IpPrefix=None, IpType=None, Name=None, SubnetCount=None):
        """Updates dhcpHostsRange resource on the server.

        Args
        ----
        - Count (number): The number of hosts
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - EuiIncrement (str): Defines the EUI increment.
        - FirstEui (str): Defines the first EUI to be used.
        - IpPrefix (number): The network prefix length associated with this address pool.
        - IpType (str): The IP version to be used for describing the range.
        - Name (str): Name of range
        - SubnetCount (number): The number of subnets.

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