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


class AcMac(Base):
    """PPPoX Mac schema for multi range support
    The AcMac class encapsulates a list of acMac resources that are managed by the user.
    A list of resources can be retrieved from the server using the AcMac.find() method.
    The list can be managed by using the AcMac.add() and AcMac.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'acMac'
    _SDM_ATT_MAP = {
        'AcMac': 'acMac',
        'ObjectId': 'objectId',
        'Percentage': 'percentage',
        'Select': 'select',
    }

    def __init__(self, parent):
        super(AcMac, self).__init__(parent)

    @property
    def AcMac(self):
        """
        Returns
        -------
        - str: Access Concentrator MAC address
        """
        return self._get_attribute(self._SDM_ATT_MAP['AcMac'])
    @AcMac.setter
    def AcMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AcMac'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def Percentage(self):
        """
        Returns
        -------
        - number: Percentage of PPPoE sessions for this AC MAC
        """
        return self._get_attribute(self._SDM_ATT_MAP['Percentage'])
    @Percentage.setter
    def Percentage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Percentage'], value)

    @property
    def Select(self):
        """
        Returns
        -------
        - bool: Enable/disable AC MAC entry
        """
        return self._get_attribute(self._SDM_ATT_MAP['Select'])
    @Select.setter
    def Select(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Select'], value)

    def update(self, AcMac=None, Percentage=None, Select=None):
        """Updates acMac resource on the server.

        Args
        ----
        - AcMac (str): Access Concentrator MAC address
        - Percentage (number): Percentage of PPPoE sessions for this AC MAC
        - Select (bool): Enable/disable AC MAC entry

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AcMac=None, Percentage=None, Select=None):
        """Adds a new acMac resource on the server and adds it to the container.

        Args
        ----
        - AcMac (str): Access Concentrator MAC address
        - Percentage (number): Percentage of PPPoE sessions for this AC MAC
        - Select (bool): Enable/disable AC MAC entry

        Returns
        -------
        - self: This instance with all currently retrieved acMac resources using find and the newly added acMac resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained acMac resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AcMac=None, ObjectId=None, Percentage=None, Select=None):
        """Finds and retrieves acMac resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve acMac resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all acMac resources from the server.

        Args
        ----
        - AcMac (str): Access Concentrator MAC address
        - ObjectId (str): Unique identifier for this object
        - Percentage (number): Percentage of PPPoE sessions for this AC MAC
        - Select (bool): Enable/disable AC MAC entry

        Returns
        -------
        - self: This instance with matching acMac resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of acMac data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the acMac resources from the server available through an iterator or index

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
