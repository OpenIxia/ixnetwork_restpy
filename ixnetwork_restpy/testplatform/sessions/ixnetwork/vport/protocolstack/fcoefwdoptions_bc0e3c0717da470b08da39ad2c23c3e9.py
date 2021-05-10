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


class FcoeFwdOptions(Base):
    """StackManager FCoE PortGroup Settings
    The FcoeFwdOptions class encapsulates a list of fcoeFwdOptions resources that are managed by the user.
    A list of resources can be retrieved from the server using the FcoeFwdOptions.find() method.
    The list can be managed by using the FcoeFwdOptions.add() and FcoeFwdOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'fcoeFwdOptions'
    _SDM_ATT_MAP = {
        'MaxPacketsPerSecond': 'maxPacketsPerSecond',
        'ObjectId': 'objectId',
        'OverrideGlobalRate': 'overrideGlobalRate',
        'UnsolDiscoveryTpid': 'unsolDiscoveryTpid',
    }

    def __init__(self, parent):
        super(FcoeFwdOptions, self).__init__(parent)

    @property
    def MaxPacketsPerSecond(self):
        """
        Returns
        -------
        - number: The maximum number of PLOGI requests transmitted in each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxPacketsPerSecond'])
    @MaxPacketsPerSecond.setter
    def MaxPacketsPerSecond(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxPacketsPerSecond'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def OverrideGlobalRate(self):
        """
        Returns
        -------
        - bool: Global rate settings are automatically distributed to all port groups. If one port group has this field enabled, the distributed rate settings will be overridden with the following values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideGlobalRate'])
    @OverrideGlobalRate.setter
    def OverrideGlobalRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideGlobalRate'], value)

    @property
    def UnsolDiscoveryTpid(self):
        """
        Returns
        -------
        - str: Server VLAN TPIDs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnsolDiscoveryTpid'])
    @UnsolDiscoveryTpid.setter
    def UnsolDiscoveryTpid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UnsolDiscoveryTpid'], value)

    def update(self, MaxPacketsPerSecond=None, OverrideGlobalRate=None, UnsolDiscoveryTpid=None):
        """Updates fcoeFwdOptions resource on the server.

        Args
        ----
        - MaxPacketsPerSecond (number): The maximum number of PLOGI requests transmitted in each second.
        - OverrideGlobalRate (bool): Global rate settings are automatically distributed to all port groups. If one port group has this field enabled, the distributed rate settings will be overridden with the following values.
        - UnsolDiscoveryTpid (str): Server VLAN TPIDs.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, MaxPacketsPerSecond=None, OverrideGlobalRate=None, UnsolDiscoveryTpid=None):
        """Adds a new fcoeFwdOptions resource on the server and adds it to the container.

        Args
        ----
        - MaxPacketsPerSecond (number): The maximum number of PLOGI requests transmitted in each second.
        - OverrideGlobalRate (bool): Global rate settings are automatically distributed to all port groups. If one port group has this field enabled, the distributed rate settings will be overridden with the following values.
        - UnsolDiscoveryTpid (str): Server VLAN TPIDs.

        Returns
        -------
        - self: This instance with all currently retrieved fcoeFwdOptions resources using find and the newly added fcoeFwdOptions resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained fcoeFwdOptions resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, MaxPacketsPerSecond=None, ObjectId=None, OverrideGlobalRate=None, UnsolDiscoveryTpid=None):
        """Finds and retrieves fcoeFwdOptions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcoeFwdOptions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcoeFwdOptions resources from the server.

        Args
        ----
        - MaxPacketsPerSecond (number): The maximum number of PLOGI requests transmitted in each second.
        - ObjectId (str): Unique identifier for this object
        - OverrideGlobalRate (bool): Global rate settings are automatically distributed to all port groups. If one port group has this field enabled, the distributed rate settings will be overridden with the following values.
        - UnsolDiscoveryTpid (str): Server VLAN TPIDs.

        Returns
        -------
        - self: This instance with matching fcoeFwdOptions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcoeFwdOptions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcoeFwdOptions resources from the server available through an iterator or index

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
