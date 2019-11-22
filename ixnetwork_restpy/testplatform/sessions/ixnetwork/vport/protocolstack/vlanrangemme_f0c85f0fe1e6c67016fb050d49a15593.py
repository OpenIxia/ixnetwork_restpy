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


class VlanRangeMme(Base):
    """
    The VlanRangeMme class encapsulates a required vlanRangeMme resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'vlanRangeMme'

    def __init__(self, parent):
        super(VlanRangeMme, self).__init__(parent)

    @property
    def VlanIdInfo(self):
        """An instance of the VlanIdInfo class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanidinfo_4189441cf1ddfb7d0ff9ccfe190b6209.VlanIdInfo)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanidinfo_4189441cf1ddfb7d0ff9ccfe190b6209 import VlanIdInfo
        return VlanIdInfo(self)

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
    def FirstId(self):
        """DEPRECATED The first ID to be used for the first VLAN tag.

        Returns:
            number
        """
        return self._get_attribute('firstId')
    @FirstId.setter
    def FirstId(self, value):
        self._set_attribute('firstId', value)

    @property
    def IdIncrMode(self):
        """Method used to increment VLAN IDs. May take the following values: 0 (First VLAN first), 1 (Last VLAN first), 2 (All).

        Returns:
            number
        """
        return self._get_attribute('idIncrMode')
    @IdIncrMode.setter
    def IdIncrMode(self, value):
        self._set_attribute('idIncrMode', value)

    @property
    def Increment(self):
        """DEPRECATED Amount of increment per increment step for first VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs

        Returns:
            number
        """
        return self._get_attribute('increment')
    @Increment.setter
    def Increment(self, value):
        self._set_attribute('increment', value)

    @property
    def IncrementStep(self):
        """DEPRECATED Frequency of first VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.

        Returns:
            number
        """
        return self._get_attribute('incrementStep')
    @IncrementStep.setter
    def IncrementStep(self, value):
        self._set_attribute('incrementStep', value)

    @property
    def InnerEnable(self):
        """DEPRECATED Enable the inner VLAN.

        Returns:
            bool
        """
        return self._get_attribute('innerEnable')
    @InnerEnable.setter
    def InnerEnable(self, value):
        self._set_attribute('innerEnable', value)

    @property
    def InnerFirstId(self):
        """DEPRECATED The first ID to be used for the inner VLAN tag.

        Returns:
            number
        """
        return self._get_attribute('innerFirstId')
    @InnerFirstId.setter
    def InnerFirstId(self, value):
        self._set_attribute('innerFirstId', value)

    @property
    def InnerIncrement(self):
        """DEPRECATED Amount of increment per increment step for Inner VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs

        Returns:
            number
        """
        return self._get_attribute('innerIncrement')
    @InnerIncrement.setter
    def InnerIncrement(self, value):
        self._set_attribute('innerIncrement', value)

    @property
    def InnerIncrementStep(self):
        """DEPRECATED Frequency of inner VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.

        Returns:
            number
        """
        return self._get_attribute('innerIncrementStep')
    @InnerIncrementStep.setter
    def InnerIncrementStep(self, value):
        self._set_attribute('innerIncrementStep', value)

    @property
    def InnerPriority(self):
        """DEPRECATED The 802.1Q priority to be used for the inner VLAN tag.

        Returns:
            number
        """
        return self._get_attribute('innerPriority')
    @InnerPriority.setter
    def InnerPriority(self, value):
        self._set_attribute('innerPriority', value)

    @property
    def InnerTpid(self):
        """DEPRECATED The TPID value in the inner VLAN Tag.

        Returns:
            str
        """
        return self._get_attribute('innerTpid')
    @InnerTpid.setter
    def InnerTpid(self, value):
        self._set_attribute('innerTpid', value)

    @property
    def InnerUniqueCount(self):
        """DEPRECATED Number of unique inner VLAN IDs to use.

        Returns:
            number
        """
        return self._get_attribute('innerUniqueCount')
    @InnerUniqueCount.setter
    def InnerUniqueCount(self, value):
        self._set_attribute('innerUniqueCount', value)

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
    def Priority(self):
        """DEPRECATED The 802.1Q priority to be used for the outer VLAN tag.

        Returns:
            number
        """
        return self._get_attribute('priority')
    @Priority.setter
    def Priority(self, value):
        self._set_attribute('priority', value)

    @property
    def Tpid(self):
        """DEPRECATED The TPID value in the outer VLAN Tag.

        Returns:
            str
        """
        return self._get_attribute('tpid')
    @Tpid.setter
    def Tpid(self, value):
        self._set_attribute('tpid', value)

    @property
    def UniqueCount(self):
        """DEPRECATED Number of unique first VLAN IDs to use.

        Returns:
            number
        """
        return self._get_attribute('uniqueCount')
    @UniqueCount.setter
    def UniqueCount(self, value):
        self._set_attribute('uniqueCount', value)

    def update(self, Enabled=None, FirstId=None, IdIncrMode=None, Increment=None, IncrementStep=None, InnerEnable=None, InnerFirstId=None, InnerIncrement=None, InnerIncrementStep=None, InnerPriority=None, InnerTpid=None, InnerUniqueCount=None, Name=None, Priority=None, Tpid=None, UniqueCount=None):
        """Updates a child instance of vlanRangeMme on the server.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FirstId (number): The first ID to be used for the first VLAN tag.
            IdIncrMode (number): Method used to increment VLAN IDs. May take the following values: 0 (First VLAN first), 1 (Last VLAN first), 2 (All).
            Increment (number): Amount of increment per increment step for first VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
            IncrementStep (number): Frequency of first VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
            InnerEnable (bool): Enable the inner VLAN.
            InnerFirstId (number): The first ID to be used for the inner VLAN tag.
            InnerIncrement (number): Amount of increment per increment step for Inner VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
            InnerIncrementStep (number): Frequency of inner VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
            InnerPriority (number): The 802.1Q priority to be used for the inner VLAN tag.
            InnerTpid (str): The TPID value in the inner VLAN Tag.
            InnerUniqueCount (number): Number of unique inner VLAN IDs to use.
            Name (str): Name of range
            Priority (number): The 802.1Q priority to be used for the outer VLAN tag.
            Tpid (str): The TPID value in the outer VLAN Tag.
            UniqueCount (number): Number of unique first VLAN IDs to use.

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
