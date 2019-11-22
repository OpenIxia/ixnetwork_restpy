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


class Arp(Base):
    """Address Resolution Protocol (Ethernet-based only).
    The Arp class encapsulates a list of arp resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Arp.find() method.
    The list can be managed by the user by using the Arp.add() and Arp.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'arp'

    def __init__(self, parent):
        super(Arp, self).__init__(parent)

    @property
    def Enabled(self):
        """(Non-POS cards only) Enables ARP requests and responses for this port. ARP requests are received at the MAC level.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    def update(self, Enabled=None):
        """Updates a child instance of arp on the server.

        Args:
            Enabled (bool): (Non-POS cards only) Enables ARP requests and responses for this port. ARP requests are received at the MAC level.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Enabled=None):
        """Adds a new arp node on the server and retrieves it in this instance.

        Args:
            Enabled (bool): (Non-POS cards only) Enables ARP requests and responses for this port. ARP requests are received at the MAC level.

        Returns:
            self: This instance with all currently retrieved arp data using find and the newly added arp data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the arp data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None):
        """Finds and retrieves arp data from the server.

        All named parameters support regex and can be used to selectively retrieve arp data from the server.
        By default the find method takes no parameters and will retrieve all arp data from the server.

        Args:
            Enabled (bool): (Non-POS cards only) Enables ARP requests and responses for this port. ARP requests are received at the MAC level.

        Returns:
            self: This instance with matching arp data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of arp data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the arp data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
