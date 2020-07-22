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


class VlanIdInfo(Base):
    """Contains extra VLANs
    The VlanIdInfo class encapsulates a list of vlanIdInfo resources that are managed by the user.
    A list of resources can be retrieved from the server using the VlanIdInfo.find() method.
    The list can be managed by using the VlanIdInfo.add() and VlanIdInfo.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vlanIdInfo'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'FirstId': 'firstId',
        'Increment': 'increment',
        'IncrementStep': 'incrementStep',
        'Name': 'name',
        'ObjectId': 'objectId',
        'Priority': 'priority',
        'Tpid': 'tpid',
        'UniqueCount': 'uniqueCount',
    }

    def __init__(self, parent):
        super(VlanIdInfo, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enable/Disable checkbox for this VLAN ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def FirstId(self):
        """
        Returns
        -------
        - number: The first ID to be used for the VLAN tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstId'])
    @FirstId.setter
    def FirstId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstId'], value)

    @property
    def Increment(self):
        """
        Returns
        -------
        - number: Amount of increment per increment step for VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
        """
        return self._get_attribute(self._SDM_ATT_MAP['Increment'])
    @Increment.setter
    def Increment(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Increment'], value)

    @property
    def IncrementStep(self):
        """
        Returns
        -------
        - number: Frequency of VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementStep'])
    @IncrementStep.setter
    def IncrementStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementStep'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of the VLAN Info
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
    def Priority(self):
        """
        Returns
        -------
        - number: The 802.1Q priority to be used for the VLAN tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])
    @Priority.setter
    def Priority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Priority'], value)

    @property
    def Tpid(self):
        """
        Returns
        -------
        - str: The TPID value in the VLAN Tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Tpid'])
    @Tpid.setter
    def Tpid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Tpid'], value)

    @property
    def UniqueCount(self):
        """
        Returns
        -------
        - number: Number of unique VLAN IDs to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UniqueCount'])
    @UniqueCount.setter
    def UniqueCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UniqueCount'], value)

    def update(self, Enabled=None, FirstId=None, Increment=None, IncrementStep=None, Name=None, Priority=None, Tpid=None, UniqueCount=None):
        """Updates vlanIdInfo resource on the server.

        Args
        ----
        - Enabled (bool): Enable/Disable checkbox for this VLAN ID
        - FirstId (number): The first ID to be used for the VLAN tag.
        - Increment (number): Amount of increment per increment step for VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
        - IncrementStep (number): Frequency of VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
        - Name (str): Name of the VLAN Info
        - Priority (number): The 802.1Q priority to be used for the VLAN tag.
        - Tpid (str): The TPID value in the VLAN Tag.
        - UniqueCount (number): Number of unique VLAN IDs to use.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, FirstId=None, Increment=None, IncrementStep=None, Name=None, Priority=None, Tpid=None, UniqueCount=None):
        """Adds a new vlanIdInfo resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Enable/Disable checkbox for this VLAN ID
        - FirstId (number): The first ID to be used for the VLAN tag.
        - Increment (number): Amount of increment per increment step for VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
        - IncrementStep (number): Frequency of VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
        - Name (str): Name of the VLAN Info
        - Priority (number): The 802.1Q priority to be used for the VLAN tag.
        - Tpid (str): The TPID value in the VLAN Tag.
        - UniqueCount (number): Number of unique VLAN IDs to use.

        Returns
        -------
        - self: This instance with all currently retrieved vlanIdInfo resources using find and the newly added vlanIdInfo resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained vlanIdInfo resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, FirstId=None, Increment=None, IncrementStep=None, Name=None, ObjectId=None, Priority=None, Tpid=None, UniqueCount=None):
        """Finds and retrieves vlanIdInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vlanIdInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vlanIdInfo resources from the server.

        Args
        ----
        - Enabled (bool): Enable/Disable checkbox for this VLAN ID
        - FirstId (number): The first ID to be used for the VLAN tag.
        - Increment (number): Amount of increment per increment step for VLAN. E.g. increment step = 10 and increment = 2 means increment VLAN ID by 2 for every 10 IPs
        - IncrementStep (number): Frequency of VLAN ID increment. E.g., value of 10 means increment VLAN ID once for every 10 IP addresses.
        - Name (str): Name of the VLAN Info
        - ObjectId (str): Unique identifier for this object
        - Priority (number): The 802.1Q priority to be used for the VLAN tag.
        - Tpid (str): The TPID value in the VLAN Tag.
        - UniqueCount (number): Number of unique VLAN IDs to use.

        Returns
        -------
        - self: This instance with matching vlanIdInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vlanIdInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vlanIdInfo resources from the server available through an iterator or index

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
