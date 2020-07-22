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


class AmtOptions(Base):
    """Portgroup settings placeholder for AMTPlugin.
    The AmtOptions class encapsulates a list of amtOptions resources that are managed by the user.
    A list of resources can be retrieved from the server using the AmtOptions.find() method.
    The list can be managed by using the AmtOptions.add() and AmtOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'amtOptions'
    _SDM_ATT_MAP = {
        'MaxOutstandingSessions': 'maxOutstandingSessions',
        'ObjectId': 'objectId',
        'OverrideGlobalSetupRate': 'overrideGlobalSetupRate',
        'OverrideGlobalTeardownRate': 'overrideGlobalTeardownRate',
        'SetupRate': 'setupRate',
        'TeardownRate': 'teardownRate',
        'TunnelOriginate': 'tunnelOriginate',
    }

    def __init__(self, parent):
        super(AmtOptions, self).__init__(parent)

    @property
    def MaxOutstandingSessions(self):
        """
        Returns
        -------
        - number: This is the point at which AMT Sessions will be restricted. AMT Discovery/Requests are sent at the configured speed until these are the number of AMT Sessions in progress, without receiving AMT messages; at which point new Discovery/Requests messages are sent only when other are completed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOutstandingSessions'])
    @MaxOutstandingSessions.setter
    def MaxOutstandingSessions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxOutstandingSessions'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def OverrideGlobalSetupRate(self):
        """
        Returns
        -------
        - bool: If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideGlobalSetupRate'])
    @OverrideGlobalSetupRate.setter
    def OverrideGlobalSetupRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideGlobalSetupRate'], value)

    @property
    def OverrideGlobalTeardownRate(self):
        """
        Returns
        -------
        - bool: If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideGlobalTeardownRate'])
    @OverrideGlobalTeardownRate.setter
    def OverrideGlobalTeardownRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideGlobalTeardownRate'], value)

    @property
    def SetupRate(self):
        """
        Returns
        -------
        - number: Discovery Rate is the number of AMT Discovery/Request packets to send in each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRate'])
    @SetupRate.setter
    def SetupRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRate'], value)

    @property
    def TeardownRate(self):
        """
        Returns
        -------
        - number: Teardown rate is the number of clients to stop in each second. This value represents the initial value for teardown rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRate'])
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRate'], value)

    @property
    def TunnelOriginate(self):
        """
        Returns
        -------
        - str: Tunnels can be originated from same IP per range (first IP from range) or from each IP per range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelOriginate'])
    @TunnelOriginate.setter
    def TunnelOriginate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelOriginate'], value)

    def update(self, MaxOutstandingSessions=None, OverrideGlobalSetupRate=None, OverrideGlobalTeardownRate=None, SetupRate=None, TeardownRate=None, TunnelOriginate=None):
        """Updates amtOptions resource on the server.

        Args
        ----
        - MaxOutstandingSessions (number): This is the point at which AMT Sessions will be restricted. AMT Discovery/Requests are sent at the configured speed until these are the number of AMT Sessions in progress, without receiving AMT messages; at which point new Discovery/Requests messages are sent only when other are completed.
        - OverrideGlobalSetupRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        - OverrideGlobalTeardownRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        - SetupRate (number): Discovery Rate is the number of AMT Discovery/Request packets to send in each second.
        - TeardownRate (number): Teardown rate is the number of clients to stop in each second. This value represents the initial value for teardown rate.
        - TunnelOriginate (str): Tunnels can be originated from same IP per range (first IP from range) or from each IP per range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, MaxOutstandingSessions=None, OverrideGlobalSetupRate=None, OverrideGlobalTeardownRate=None, SetupRate=None, TeardownRate=None, TunnelOriginate=None):
        """Adds a new amtOptions resource on the server and adds it to the container.

        Args
        ----
        - MaxOutstandingSessions (number): This is the point at which AMT Sessions will be restricted. AMT Discovery/Requests are sent at the configured speed until these are the number of AMT Sessions in progress, without receiving AMT messages; at which point new Discovery/Requests messages are sent only when other are completed.
        - OverrideGlobalSetupRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        - OverrideGlobalTeardownRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        - SetupRate (number): Discovery Rate is the number of AMT Discovery/Request packets to send in each second.
        - TeardownRate (number): Teardown rate is the number of clients to stop in each second. This value represents the initial value for teardown rate.
        - TunnelOriginate (str): Tunnels can be originated from same IP per range (first IP from range) or from each IP per range.

        Returns
        -------
        - self: This instance with all currently retrieved amtOptions resources using find and the newly added amtOptions resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained amtOptions resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, MaxOutstandingSessions=None, ObjectId=None, OverrideGlobalSetupRate=None, OverrideGlobalTeardownRate=None, SetupRate=None, TeardownRate=None, TunnelOriginate=None):
        """Finds and retrieves amtOptions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve amtOptions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all amtOptions resources from the server.

        Args
        ----
        - MaxOutstandingSessions (number): This is the point at which AMT Sessions will be restricted. AMT Discovery/Requests are sent at the configured speed until these are the number of AMT Sessions in progress, without receiving AMT messages; at which point new Discovery/Requests messages are sent only when other are completed.
        - ObjectId (str): Unique identifier for this object
        - OverrideGlobalSetupRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        - OverrideGlobalTeardownRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
        - SetupRate (number): Discovery Rate is the number of AMT Discovery/Request packets to send in each second.
        - TeardownRate (number): Teardown rate is the number of clients to stop in each second. This value represents the initial value for teardown rate.
        - TunnelOriginate (str): Tunnels can be originated from same IP per range (first IP from range) or from each IP per range.

        Returns
        -------
        - self: This instance with matching amtOptions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of amtOptions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the amtOptions resources from the server available through an iterator or index

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
