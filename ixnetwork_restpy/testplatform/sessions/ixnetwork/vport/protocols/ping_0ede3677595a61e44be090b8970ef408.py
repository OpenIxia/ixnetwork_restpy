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


class Ping(Base):
    """"Packet Internet Groper/PING" uses Internet Message Control Protocol (ICMP) echo messages and responses.
    The Ping class encapsulates a list of ping resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ping.find() method.
    The list can be managed by using the Ping.add() and Ping.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ping'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
    }

    def __init__(self, parent):
        super(Ping, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables IPv4 PING transmission and reception for this port. PING messages are IPv4 ICMP messages of type Echo Request. Responses are IPv4 ICMP message of type Echo Response.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    def update(self, Enabled=None):
        """Updates ping resource on the server.

        Args
        ----
        - Enabled (bool): Enables IPv4 PING transmission and reception for this port. PING messages are IPv4 ICMP messages of type Echo Request. Responses are IPv4 ICMP message of type Echo Response.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None):
        """Adds a new ping resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Enables IPv4 PING transmission and reception for this port. PING messages are IPv4 ICMP messages of type Echo Request. Responses are IPv4 ICMP message of type Echo Response.

        Returns
        -------
        - self: This instance with all currently retrieved ping resources using find and the newly added ping resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ping resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None):
        """Finds and retrieves ping resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ping resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ping resources from the server.

        Args
        ----
        - Enabled (bool): Enables IPv4 PING transmission and reception for this port. PING messages are IPv4 ICMP messages of type Echo Request. Responses are IPv4 ICMP message of type Echo Response.

        Returns
        -------
        - self: This instance with matching ping resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ping data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ping resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
