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


class TrafficProfileProxiesSgw(Base):
    """GTP Traffic Profile from IxNetwork
    The TrafficProfileProxiesSgw class encapsulates a list of trafficProfileProxiesSgw resources that are managed by the user.
    A list of resources can be retrieved from the server using the TrafficProfileProxiesSgw.find() method.
    The list can be managed by using the TrafficProfileProxiesSgw.add() and TrafficProfileProxiesSgw.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'trafficProfileProxiesSgw'
    _SDM_ATT_MAP = {
        'ActualPluginSettingsRange': 'actualPluginSettingsRange',
        'Enabled': 'enabled',
        'Name': 'name',
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(TrafficProfileProxiesSgw, self).__init__(parent)

    @property
    def ActualPluginSettingsRange(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalTrafficProfiles): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActualPluginSettingsRange'])
    @ActualPluginSettingsRange.setter
    def ActualPluginSettingsRange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActualPluginSettingsRange'], value)

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
        - str: 
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

    def update(self, ActualPluginSettingsRange=None, Enabled=None, Name=None):
        """Updates trafficProfileProxiesSgw resource on the server.

        Args
        ----
        - ActualPluginSettingsRange (str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalTrafficProfiles)): 
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ActualPluginSettingsRange=None, Enabled=None, Name=None):
        """Adds a new trafficProfileProxiesSgw resource on the server and adds it to the container.

        Args
        ----
        - ActualPluginSettingsRange (str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalTrafficProfiles)): 
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): 

        Returns
        -------
        - self: This instance with all currently retrieved trafficProfileProxiesSgw resources using find and the newly added trafficProfileProxiesSgw resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained trafficProfileProxiesSgw resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ActualPluginSettingsRange=None, Enabled=None, Name=None, ObjectId=None):
        """Finds and retrieves trafficProfileProxiesSgw resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trafficProfileProxiesSgw resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trafficProfileProxiesSgw resources from the server.

        Args
        ----
        - ActualPluginSettingsRange (str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalTrafficProfiles)): 
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): 
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching trafficProfileProxiesSgw resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of trafficProfileProxiesSgw data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trafficProfileProxiesSgw resources from the server available through an iterator or index

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
