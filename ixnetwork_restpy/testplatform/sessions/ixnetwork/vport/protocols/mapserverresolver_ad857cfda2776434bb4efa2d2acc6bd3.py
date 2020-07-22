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


class MapServerResolver(Base):
    """It gives details about the map server resolver
    The MapServerResolver class encapsulates a list of mapServerResolver resources that are managed by the user.
    A list of resources can be retrieved from the server using the MapServerResolver.find() method.
    The list can be managed by using the MapServerResolver.add() and MapServerResolver.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'mapServerResolver'
    _SDM_ATT_MAP = {
        'AuthenticationAlgorithm': 'authenticationAlgorithm',
        'Enabled': 'enabled',
        'ExternalMsmrAddress': 'externalMsmrAddress',
        'Family': 'family',
        'InternalIxiaMsmrRouter': 'internalIxiaMsmrRouter',
        'Key': 'key',
        'MsmrLocation': 'msmrLocation',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(MapServerResolver, self).__init__(parent)

    @property
    def AuthenticationAlgorithm(self):
        """
        Returns
        -------
        - str(sha-1-96 | sha-128-256): It gives details about the authentication algorithm
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthenticationAlgorithm'])
    @AuthenticationAlgorithm.setter
    def AuthenticationAlgorithm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AuthenticationAlgorithm'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, it enables the protocol
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def ExternalMsmrAddress(self):
        """
        Returns
        -------
        - str: It gives details about the external Msmr address
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExternalMsmrAddress'])
    @ExternalMsmrAddress.setter
    def ExternalMsmrAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExternalMsmrAddress'], value)

    @property
    def Family(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): It gives details about the ip family it represents
        """
        return self._get_attribute(self._SDM_ATT_MAP['Family'])
    @Family.setter
    def Family(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Family'], value)

    @property
    def InternalIxiaMsmrRouter(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../router): It gives details about the internal ixia msmr router
        """
        return self._get_attribute(self._SDM_ATT_MAP['InternalIxiaMsmrRouter'])
    @InternalIxiaMsmrRouter.setter
    def InternalIxiaMsmrRouter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InternalIxiaMsmrRouter'], value)

    @property
    def Key(self):
        """
        Returns
        -------
        - str: it gives details about the key
        """
        return self._get_attribute(self._SDM_ATT_MAP['Key'])
    @Key.setter
    def Key(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Key'], value)

    @property
    def MsmrLocation(self):
        """
        Returns
        -------
        - str(internal | external): It details about the msmr location
        """
        return self._get_attribute(self._SDM_ATT_MAP['MsmrLocation'])
    @MsmrLocation.setter
    def MsmrLocation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MsmrLocation'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(ms | mr | msmr): It gives details about the type
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    def update(self, AuthenticationAlgorithm=None, Enabled=None, ExternalMsmrAddress=None, Family=None, InternalIxiaMsmrRouter=None, Key=None, MsmrLocation=None, Type=None):
        """Updates mapServerResolver resource on the server.

        Args
        ----
        - AuthenticationAlgorithm (str(sha-1-96 | sha-128-256)): It gives details about the authentication algorithm
        - Enabled (bool): If true, it enables the protocol
        - ExternalMsmrAddress (str): It gives details about the external Msmr address
        - Family (str(ipv4 | ipv6)): It gives details about the ip family it represents
        - InternalIxiaMsmrRouter (str(None | /api/v1/sessions/1/ixnetwork/vport/.../router)): It gives details about the internal ixia msmr router
        - Key (str): it gives details about the key
        - MsmrLocation (str(internal | external)): It details about the msmr location
        - Type (str(ms | mr | msmr)): It gives details about the type

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AuthenticationAlgorithm=None, Enabled=None, ExternalMsmrAddress=None, Family=None, InternalIxiaMsmrRouter=None, Key=None, MsmrLocation=None, Type=None):
        """Adds a new mapServerResolver resource on the server and adds it to the container.

        Args
        ----
        - AuthenticationAlgorithm (str(sha-1-96 | sha-128-256)): It gives details about the authentication algorithm
        - Enabled (bool): If true, it enables the protocol
        - ExternalMsmrAddress (str): It gives details about the external Msmr address
        - Family (str(ipv4 | ipv6)): It gives details about the ip family it represents
        - InternalIxiaMsmrRouter (str(None | /api/v1/sessions/1/ixnetwork/vport/.../router)): It gives details about the internal ixia msmr router
        - Key (str): it gives details about the key
        - MsmrLocation (str(internal | external)): It details about the msmr location
        - Type (str(ms | mr | msmr)): It gives details about the type

        Returns
        -------
        - self: This instance with all currently retrieved mapServerResolver resources using find and the newly added mapServerResolver resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained mapServerResolver resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AuthenticationAlgorithm=None, Enabled=None, ExternalMsmrAddress=None, Family=None, InternalIxiaMsmrRouter=None, Key=None, MsmrLocation=None, Type=None):
        """Finds and retrieves mapServerResolver resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mapServerResolver resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mapServerResolver resources from the server.

        Args
        ----
        - AuthenticationAlgorithm (str(sha-1-96 | sha-128-256)): It gives details about the authentication algorithm
        - Enabled (bool): If true, it enables the protocol
        - ExternalMsmrAddress (str): It gives details about the external Msmr address
        - Family (str(ipv4 | ipv6)): It gives details about the ip family it represents
        - InternalIxiaMsmrRouter (str(None | /api/v1/sessions/1/ixnetwork/vport/.../router)): It gives details about the internal ixia msmr router
        - Key (str): it gives details about the key
        - MsmrLocation (str(internal | external)): It details about the msmr location
        - Type (str(ms | mr | msmr)): It gives details about the type

        Returns
        -------
        - self: This instance with matching mapServerResolver resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mapServerResolver data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mapServerResolver resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
