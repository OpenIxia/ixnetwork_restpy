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


class IgmpQuerier(Base):
    """
    The IgmpQuerier class encapsulates a list of igmpQuerier resources that are managed by the user.
    A list of resources can be retrieved from the server using the IgmpQuerier.find() method.
    The list can be managed by using the IgmpQuerier.add() and IgmpQuerier.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'igmpQuerier'
    _SDM_ATT_MAP = {
        'Name': 'name',
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(IgmpQuerier, self).__init__(parent)

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

    def update(self, Name=None):
        """Updates igmpQuerier resource on the server.

        Args
        ----
        - Name (str): Name of range

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None):
        """Adds a new igmpQuerier resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Name of range

        Returns
        -------
        - self: This instance with all currently retrieved igmpQuerier resources using find and the newly added igmpQuerier resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained igmpQuerier resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Name=None, ObjectId=None):
        """Finds and retrieves igmpQuerier resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve igmpQuerier resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all igmpQuerier resources from the server.

        Args
        ----
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching igmpQuerier resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of igmpQuerier data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the igmpQuerier resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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

    def IgmpMldQuerierStart(self, *args, **kwargs):
        """Executes the igmpMldQuerierStart operation on the server.

        Start IGMP/MLD Querier on selected plugins

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpMldQuerierStart(Arg2=enum)
        ------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpServerEndpoint/igmpQuerier,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/igmpQuerier,/vport/protocolStack/atm/emulatedRouter/ip/igmpQuerier,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpQuerier,/vport/protocolStack/atm/ip/igmpQuerier,/vport/protocolStack/atm/ipEndpoint/igmpQuerier,/vport/protocolStack/atm/pppox/igmpQuerier,/vport/protocolStack/atm/pppoxEndpoint/igmpQuerier,/vport/protocolStack/ethernet/dhcpServerEndpoint/igmpQuerier,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/igmpQuerier,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpQuerier,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpQuerier,/vport/protocolStack/ethernet/ip/igmpQuerier,/vport/protocolStack/ethernet/ipEndpoint/igmpQuerier,/vport/protocolStack/ethernet/pppox/igmpQuerier,/vport/protocolStack/ethernet/pppoxEndpoint/igmpQuerier]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpMldQuerierStart', payload=payload, response_object=None)

    def IgmpMldQuerierStop(self, *args, **kwargs):
        """Executes the igmpMldQuerierStop operation on the server.

        Stop IGMP/MLD Querier on selected plugins

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpMldQuerierStop(Arg2=enum)
        -----------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpServerEndpoint/igmpQuerier,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/igmpQuerier,/vport/protocolStack/atm/emulatedRouter/ip/igmpQuerier,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpQuerier,/vport/protocolStack/atm/ip/igmpQuerier,/vport/protocolStack/atm/ipEndpoint/igmpQuerier,/vport/protocolStack/atm/pppox/igmpQuerier,/vport/protocolStack/atm/pppoxEndpoint/igmpQuerier,/vport/protocolStack/ethernet/dhcpServerEndpoint/igmpQuerier,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/igmpQuerier,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpQuerier,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpQuerier,/vport/protocolStack/ethernet/ip/igmpQuerier,/vport/protocolStack/ethernet/ipEndpoint/igmpQuerier,/vport/protocolStack/ethernet/pppox/igmpQuerier,/vport/protocolStack/ethernet/pppoxEndpoint/igmpQuerier]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('igmpMldQuerierStop', payload=payload, response_object=None)
