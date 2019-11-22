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


class VlanIdInfo(Base):
    """Contains extra VLANs
    The VlanIdInfo class encapsulates a list of vlanIdInfo resources that is be managed by the user.
    A list of resources can be retrieved from the server using the VlanIdInfo.find() method.
    The list can be managed by the user by using the VlanIdInfo.add() and VlanIdInfo.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vlanIdInfo'

    def __init__(self, parent):
        super(VlanIdInfo, self).__init__(parent)

    @property
    def Enabled(self):
        """Enable/Disable checkbox for this VLAN ID

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def FirstId(self):
        """The first ID to be used for the VLAN tag.

        Returns:
            number
        """
        return self._get_attribute('firstId')
    @FirstId.setter
    def FirstId(self, value):
        self._set_attribute('firstId', value)

    @property
    def Increment(self):
        """Amount of increment per increment step for VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs

        Returns:
            number
        """
        return self._get_attribute('increment')
    @Increment.setter
    def Increment(self, value):
        self._set_attribute('increment', value)

    @property
    def IncrementStep(self):
        """Frequency of VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.

        Returns:
            number
        """
        return self._get_attribute('incrementStep')
    @IncrementStep.setter
    def IncrementStep(self, value):
        self._set_attribute('incrementStep', value)

    @property
    def Name(self):
        """Name of the VLAN Info

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
        """The 802.1Q priority to be used for the VLAN tag.

        Returns:
            number
        """
        return self._get_attribute('priority')
    @Priority.setter
    def Priority(self, value):
        self._set_attribute('priority', value)

    @property
    def Tpid(self):
        """The TPID value in the VLAN Tag.

        Returns:
            str
        """
        return self._get_attribute('tpid')
    @Tpid.setter
    def Tpid(self, value):
        self._set_attribute('tpid', value)

    @property
    def UniqueCount(self):
        """Number of unique VLAN IDs to use.

        Returns:
            number
        """
        return self._get_attribute('uniqueCount')
    @UniqueCount.setter
    def UniqueCount(self, value):
        self._set_attribute('uniqueCount', value)

    def update(self, Enabled=None, FirstId=None, Increment=None, IncrementStep=None, Name=None, Priority=None, Tpid=None, UniqueCount=None):
        """Updates a child instance of vlanIdInfo on the server.

        Args:
            Enabled (bool): Enable/Disable checkbox for this VLAN ID
            FirstId (number): The first ID to be used for the VLAN tag.
            Increment (number): Amount of increment per increment step for VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
            IncrementStep (number): Frequency of VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
            Name (str): Name of the VLAN Info
            Priority (number): The 802.1Q priority to be used for the VLAN tag.
            Tpid (str): The TPID value in the VLAN Tag.
            UniqueCount (number): Number of unique VLAN IDs to use.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Enabled=None, FirstId=None, Increment=None, IncrementStep=None, Name=None, Priority=None, Tpid=None, UniqueCount=None):
        """Adds a new vlanIdInfo node on the server and retrieves it in this instance.

        Args:
            Enabled (bool): Enable/Disable checkbox for this VLAN ID
            FirstId (number): The first ID to be used for the VLAN tag.
            Increment (number): Amount of increment per increment step for VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
            IncrementStep (number): Frequency of VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
            Name (str): Name of the VLAN Info
            Priority (number): The 802.1Q priority to be used for the VLAN tag.
            Tpid (str): The TPID value in the VLAN Tag.
            UniqueCount (number): Number of unique VLAN IDs to use.

        Returns:
            self: This instance with all currently retrieved vlanIdInfo data using find and the newly added vlanIdInfo data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the vlanIdInfo data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, FirstId=None, Increment=None, IncrementStep=None, Name=None, ObjectId=None, Priority=None, Tpid=None, UniqueCount=None):
        """Finds and retrieves vlanIdInfo data from the server.

        All named parameters support regex and can be used to selectively retrieve vlanIdInfo data from the server.
        By default the find method takes no parameters and will retrieve all vlanIdInfo data from the server.

        Args:
            Enabled (bool): Enable/Disable checkbox for this VLAN ID
            FirstId (number): The first ID to be used for the VLAN tag.
            Increment (number): Amount of increment per increment step for VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
            IncrementStep (number): Frequency of VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
            Name (str): Name of the VLAN Info
            ObjectId (str): Unique identifier for this object
            Priority (number): The 802.1Q priority to be used for the VLAN tag.
            Tpid (str): The TPID value in the VLAN Tag.
            UniqueCount (number): Number of unique VLAN IDs to use.

        Returns:
            self: This instance with matching vlanIdInfo data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of vlanIdInfo data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the vlanIdInfo data from the server available through an iterator or index

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
