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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
from typing import List, Any, Union


class Dhcpv6PdOptionSet(Base):
    """DHCP client options
    The Dhcpv6PdOptionSet class encapsulates a list of dhcpv6PdOptionSet resources that are managed by the user.
    A list of resources can be retrieved from the server using the Dhcpv6PdOptionSet.find() method.
    The list can be managed by using the Dhcpv6PdOptionSet.add() and Dhcpv6PdOptionSet.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpv6PdOptionSet'
    _SDM_ATT_MAP = {
        'Defaultp': 'defaultp',
        'IpType': 'ipType',
        'Name': 'name',
        'ObjectId': 'objectId',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Dhcpv6PdOptionSet, self).__init__(parent, list_op)

    @property
    def Dhcpv6PdOptionTlv(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6pdclientglobals.dhcpv6pdoptionset.dhcpv6pdoptiontlv.dhcpv6pdoptiontlv.Dhcpv6PdOptionTlv): An instance of the Dhcpv6PdOptionTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6pdclientglobals.dhcpv6pdoptionset.dhcpv6pdoptiontlv.dhcpv6pdoptiontlv import Dhcpv6PdOptionTlv
        if self._properties.get('Dhcpv6PdOptionTlv', None) is not None:
            return self._properties.get('Dhcpv6PdOptionTlv')
        else:
            return Dhcpv6PdOptionTlv(self)

    @property
    def Defaultp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: True to assign this option set to new ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Defaultp'])
    @Defaultp.setter
    def Defaultp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Defaultp'], value)

    @property
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP version used with this option set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpType'])
    @IpType.setter
    def IpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['IpType'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Option set name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    def update(self, Defaultp=None, IpType=None, Name=None):
        # type: (bool, str, str) -> Dhcpv6PdOptionSet
        """Updates dhcpv6PdOptionSet resource on the server.

        Args
        ----
        - Defaultp (bool): True to assign this option set to new ranges.
        - IpType (str): The IP version used with this option set.
        - Name (str): Option set name.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Defaultp=None, IpType=None, Name=None):
        # type: (bool, str, str) -> Dhcpv6PdOptionSet
        """Adds a new dhcpv6PdOptionSet resource on the server and adds it to the container.

        Args
        ----
        - Defaultp (bool): True to assign this option set to new ranges.
        - IpType (str): The IP version used with this option set.
        - Name (str): Option set name.

        Returns
        -------
        - self: This instance with all currently retrieved dhcpv6PdOptionSet resources using find and the newly added dhcpv6PdOptionSet resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dhcpv6PdOptionSet resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Defaultp=None, IpType=None, Name=None, ObjectId=None):
        # type: (bool, str, str, str) -> Dhcpv6PdOptionSet
        """Finds and retrieves dhcpv6PdOptionSet resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpv6PdOptionSet resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpv6PdOptionSet resources from the server.

        Args
        ----
        - Defaultp (bool): True to assign this option set to new ranges.
        - IpType (str): The IP version used with this option set.
        - Name (str): Option set name.
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching dhcpv6PdOptionSet resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpv6PdOptionSet data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpv6PdOptionSet resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
