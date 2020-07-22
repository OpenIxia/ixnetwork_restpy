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


class DhcpOptionSet(Base):
    """A group of DHCP options.
    The DhcpOptionSet class encapsulates a list of dhcpOptionSet resources that are managed by the user.
    A list of resources can be retrieved from the server using the DhcpOptionSet.find() method.
    The list can be managed by using the DhcpOptionSet.add() and DhcpOptionSet.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpOptionSet'
    _SDM_ATT_MAP = {
        'Defaultp': 'defaultp',
        'IpType': 'ipType',
        'Name': 'name',
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(DhcpOptionSet, self).__init__(parent)

    @property
    def DhcpOptionTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpglobals.dhcpoptionset.dhcpoptiontlv.dhcpoptiontlv.DhcpOptionTlv): An instance of the DhcpOptionTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpglobals.dhcpoptionset.dhcpoptiontlv.dhcpoptiontlv import DhcpOptionTlv
        return DhcpOptionTlv(self)

    @property
    def Defaultp(self):
        """
        Returns
        -------
        - bool: True to assign this option set to new ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Defaultp'])
    @Defaultp.setter
    def Defaultp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Defaultp'], value)

    @property
    def IpType(self):
        """
        Returns
        -------
        - str: The IP version used with this option set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpType'])
    @IpType.setter
    def IpType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpType'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Option set name.
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

    def update(self, Defaultp=None, IpType=None, Name=None):
        """Updates dhcpOptionSet resource on the server.

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
        """Adds a new dhcpOptionSet resource on the server and adds it to the container.

        Args
        ----
        - Defaultp (bool): True to assign this option set to new ranges.
        - IpType (str): The IP version used with this option set.
        - Name (str): Option set name.

        Returns
        -------
        - self: This instance with all currently retrieved dhcpOptionSet resources using find and the newly added dhcpOptionSet resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dhcpOptionSet resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Defaultp=None, IpType=None, Name=None, ObjectId=None):
        """Finds and retrieves dhcpOptionSet resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpOptionSet resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpOptionSet resources from the server.

        Args
        ----
        - Defaultp (bool): True to assign this option set to new ranges.
        - IpType (str): The IP version used with this option set.
        - Name (str): Option set name.
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching dhcpOptionSet resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpOptionSet data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpOptionSet resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
