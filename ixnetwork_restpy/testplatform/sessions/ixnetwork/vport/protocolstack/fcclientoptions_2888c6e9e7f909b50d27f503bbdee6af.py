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


class FcClientOptions(Base):
    """
    The FcClientOptions class encapsulates a list of fcClientOptions resources that are managed by the user.
    A list of resources can be retrieved from the server using the FcClientOptions.find() method.
    The list can be managed by using the FcClientOptions.add() and FcClientOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'fcClientOptions'
    _SDM_ATT_MAP = {
        'Associates': 'associates',
        'B2bCredit': 'b2bCredit',
        'B2bRxSize': 'b2bRxSize',
        'EdTov': 'edTov',
        'EdTovMode': 'edTovMode',
        'MaxPacketsPerSecond': 'maxPacketsPerSecond',
        'ObjectId': 'objectId',
        'OverrideGlobalRate': 'overrideGlobalRate',
        'RtTov': 'rtTov',
        'RtTovMode': 'rtTovMode',
        'SetupRate': 'setupRate',
        'TeardownRate': 'teardownRate',
    }

    def __init__(self, parent):
        super(FcClientOptions, self).__init__(parent)

    @property
    def Associates(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../protocolStack]): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Associates'])
    @Associates.setter
    def Associates(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Associates'], value)

    @property
    def B2bCredit(self):
        """
        Returns
        -------
        - number: The buffer-to-buffer credit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['B2bCredit'])
    @B2bCredit.setter
    def B2bCredit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['B2bCredit'], value)

    @property
    def B2bRxSize(self):
        """
        Returns
        -------
        - number: The buffer-to-buffer receive data field size in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['B2bRxSize'])
    @B2bRxSize.setter
    def B2bRxSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['B2bRxSize'], value)

    @property
    def EdTov(self):
        """
        Returns
        -------
        - number: The user-provided Error Detect TimeOut Value. Can be edited in Override E_D_TOV mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EdTov'])
    @EdTov.setter
    def EdTov(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EdTov'], value)

    @property
    def EdTovMode(self):
        """
        Returns
        -------
        - str: Allows the user to provide the Error Detect TimeOut Value or have the Ixia port obtain it from Login.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EdTovMode'])
    @EdTovMode.setter
    def EdTovMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EdTovMode'], value)

    @property
    def MaxPacketsPerSecond(self):
        """
        Returns
        -------
        - number: The maximum number of requests transmitted in each second, for this port group.
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
        - bool: Global rate settings are automatically distributed to all port groups.If one port group has this field enabled, the distributed rate settings will be overridden with the following values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OverrideGlobalRate'])
    @OverrideGlobalRate.setter
    def OverrideGlobalRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OverrideGlobalRate'], value)

    @property
    def RtTov(self):
        """
        Returns
        -------
        - number: The user-provided Receiver-Transmitter TimeOut Value. Can be edited in Override R_T_TOV mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RtTov'])
    @RtTov.setter
    def RtTov(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RtTov'], value)

    @property
    def RtTovMode(self):
        """
        Returns
        -------
        - str: Allows the user to provide the Receiver-Transmitter TimeOut Value or have the Ixia port obtain it from Login.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RtTovMode'])
    @RtTovMode.setter
    def RtTovMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RtTovMode'], value)

    @property
    def SetupRate(self):
        """
        Returns
        -------
        - number: The number of interfaces scheduled to be configured in each second, for this port group.
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
        - number: The number of interfaces scheduled to be deconfigured in each second, for this port group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRate'])
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRate'], value)

    def update(self, Associates=None, B2bCredit=None, B2bRxSize=None, EdTov=None, EdTovMode=None, MaxPacketsPerSecond=None, OverrideGlobalRate=None, RtTov=None, RtTovMode=None, SetupRate=None, TeardownRate=None):
        """Updates fcClientOptions resource on the server.

        Args
        ----
        - Associates (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
        - B2bCredit (number): The buffer-to-buffer credit.
        - B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
        - EdTov (number): The user-provided Error Detect TimeOut Value. Can be edited in Override E_D_TOV mode.
        - EdTovMode (str): Allows the user to provide the Error Detect TimeOut Value or have the Ixia port obtain it from Login.
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second, for this port group.
        - OverrideGlobalRate (bool): Global rate settings are automatically distributed to all port groups.If one port group has this field enabled, the distributed rate settings will be overridden with the following values.
        - RtTov (number): The user-provided Receiver-Transmitter TimeOut Value. Can be edited in Override R_T_TOV mode.
        - RtTovMode (str): Allows the user to provide the Receiver-Transmitter TimeOut Value or have the Ixia port obtain it from Login.
        - SetupRate (number): The number of interfaces scheduled to be configured in each second, for this port group.
        - TeardownRate (number): The number of interfaces scheduled to be deconfigured in each second, for this port group.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Associates=None, B2bCredit=None, B2bRxSize=None, EdTov=None, EdTovMode=None, MaxPacketsPerSecond=None, OverrideGlobalRate=None, RtTov=None, RtTovMode=None, SetupRate=None, TeardownRate=None):
        """Adds a new fcClientOptions resource on the server and adds it to the container.

        Args
        ----
        - Associates (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
        - B2bCredit (number): The buffer-to-buffer credit.
        - B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
        - EdTov (number): The user-provided Error Detect TimeOut Value. Can be edited in Override E_D_TOV mode.
        - EdTovMode (str): Allows the user to provide the Error Detect TimeOut Value or have the Ixia port obtain it from Login.
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second, for this port group.
        - OverrideGlobalRate (bool): Global rate settings are automatically distributed to all port groups.If one port group has this field enabled, the distributed rate settings will be overridden with the following values.
        - RtTov (number): The user-provided Receiver-Transmitter TimeOut Value. Can be edited in Override R_T_TOV mode.
        - RtTovMode (str): Allows the user to provide the Receiver-Transmitter TimeOut Value or have the Ixia port obtain it from Login.
        - SetupRate (number): The number of interfaces scheduled to be configured in each second, for this port group.
        - TeardownRate (number): The number of interfaces scheduled to be deconfigured in each second, for this port group.

        Returns
        -------
        - self: This instance with all currently retrieved fcClientOptions resources using find and the newly added fcClientOptions resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained fcClientOptions resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Associates=None, B2bCredit=None, B2bRxSize=None, EdTov=None, EdTovMode=None, MaxPacketsPerSecond=None, ObjectId=None, OverrideGlobalRate=None, RtTov=None, RtTovMode=None, SetupRate=None, TeardownRate=None):
        """Finds and retrieves fcClientOptions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcClientOptions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcClientOptions resources from the server.

        Args
        ----
        - Associates (list(str[None | /api/v1/sessions/1/ixnetwork/vport/.../protocolStack])): The 'Associates' property applies only to 'client mode'endpoints (e.g. DHCP/L2TP/PPP). It describes a listof server endpoints that will: + always be started before the client endpoint is started + always be stopped after the client endpoint is stopped.This allows orderly, synchronized start and stop sequences to occur between associated client and server endpoints.This feature should be used when you have two or more IXIADHCP/PPP/L2TP endpoints (client and server) in a networkconfiguration. It prevents extraneous session negotiationtimeouts that may occur due to: + a server being started after a client was started + a server being stopped before a client was stopped.
        - B2bCredit (number): The buffer-to-buffer credit.
        - B2bRxSize (number): The buffer-to-buffer receive data field size in bytes.
        - EdTov (number): The user-provided Error Detect TimeOut Value. Can be edited in Override E_D_TOV mode.
        - EdTovMode (str): Allows the user to provide the Error Detect TimeOut Value or have the Ixia port obtain it from Login.
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second, for this port group.
        - ObjectId (str): Unique identifier for this object
        - OverrideGlobalRate (bool): Global rate settings are automatically distributed to all port groups.If one port group has this field enabled, the distributed rate settings will be overridden with the following values.
        - RtTov (number): The user-provided Receiver-Transmitter TimeOut Value. Can be edited in Override R_T_TOV mode.
        - RtTovMode (str): Allows the user to provide the Receiver-Transmitter TimeOut Value or have the Ixia port obtain it from Login.
        - SetupRate (number): The number of interfaces scheduled to be configured in each second, for this port group.
        - TeardownRate (number): The number of interfaces scheduled to be deconfigured in each second, for this port group.

        Returns
        -------
        - self: This instance with matching fcClientOptions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcClientOptions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcClientOptions resources from the server available through an iterator or index

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
