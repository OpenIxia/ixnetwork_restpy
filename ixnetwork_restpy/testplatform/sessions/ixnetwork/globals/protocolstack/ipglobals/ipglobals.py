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


class IpGlobals(Base):
    """Global settings for IP plugin.
    The IpGlobals class encapsulates a list of ipGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the IpGlobals.find() method.
    The list can be managed by the user by using the IpGlobals.add() and IpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ipGlobals'

    def __init__(self, parent):
        super(IpGlobals, self).__init__(parent)

    @property
    def EnableGatewayArp(self):
        """When enabled, every IP address will ARP the specified gateway.

        Returns:
            bool
        """
        return self._get_attribute('enableGatewayArp')
    @EnableGatewayArp.setter
    def EnableGatewayArp(self, value):
        self._set_attribute('enableGatewayArp', value)

    @property
    def GatewayArpRequestRate(self):
        """Maximum ARP request rate

        Returns:
            number
        """
        return self._get_attribute('gatewayArpRequestRate')
    @GatewayArpRequestRate.setter
    def GatewayArpRequestRate(self, value):
        self._set_attribute('gatewayArpRequestRate', value)

    @property
    def MaxOutstandingGatewayArpRequests(self):
        """Threshold at which the plugin begins throttling back the number of new ARP requests sent out.

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingGatewayArpRequests')
    @MaxOutstandingGatewayArpRequests.setter
    def MaxOutstandingGatewayArpRequests(self, value):
        self._set_attribute('maxOutstandingGatewayArpRequests', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def SendOneArpFromEachInterface(self):
        """When set, each interface will send one ARP request.

        Returns:
            bool
        """
        return self._get_attribute('sendOneArpFromEachInterface')
    @SendOneArpFromEachInterface.setter
    def SendOneArpFromEachInterface(self, value):
        self._set_attribute('sendOneArpFromEachInterface', value)

    def update(self, EnableGatewayArp=None, GatewayArpRequestRate=None, MaxOutstandingGatewayArpRequests=None, SendOneArpFromEachInterface=None):
        """Updates a child instance of ipGlobals on the server.

        Args:
            EnableGatewayArp (bool): When enabled, every IP address will ARP the specified gateway.
            GatewayArpRequestRate (number): Maximum ARP request rate
            MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new ARP requests sent out.
            SendOneArpFromEachInterface (bool): When set, each interface will send one ARP request.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, EnableGatewayArp=None, GatewayArpRequestRate=None, MaxOutstandingGatewayArpRequests=None, SendOneArpFromEachInterface=None):
        """Adds a new ipGlobals node on the server and retrieves it in this instance.

        Args:
            EnableGatewayArp (bool): When enabled, every IP address will ARP the specified gateway.
            GatewayArpRequestRate (number): Maximum ARP request rate
            MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new ARP requests sent out.
            SendOneArpFromEachInterface (bool): When set, each interface will send one ARP request.

        Returns:
            self: This instance with all currently retrieved ipGlobals data using find and the newly added ipGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the ipGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableGatewayArp=None, GatewayArpRequestRate=None, MaxOutstandingGatewayArpRequests=None, ObjectId=None, SendOneArpFromEachInterface=None):
        """Finds and retrieves ipGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve ipGlobals data from the server.
        By default the find method takes no parameters and will retrieve all ipGlobals data from the server.

        Args:
            EnableGatewayArp (bool): When enabled, every IP address will ARP the specified gateway.
            GatewayArpRequestRate (number): Maximum ARP request rate
            MaxOutstandingGatewayArpRequests (number): Threshold at which the plugin begins throttling back the number of new ARP requests sent out.
            ObjectId (str): Unique identifier for this object
            SendOneArpFromEachInterface (bool): When set, each interface will send one ARP request.

        Returns:
            self: This instance with matching ipGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of ipGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the ipGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
