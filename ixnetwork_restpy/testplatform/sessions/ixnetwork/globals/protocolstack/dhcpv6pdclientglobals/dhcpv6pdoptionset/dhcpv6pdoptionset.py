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


class Dhcpv6PdOptionSet(Base):
    """DHCP client options
    The Dhcpv6PdOptionSet class encapsulates a list of dhcpv6PdOptionSet resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Dhcpv6PdOptionSet.find() method.
    The list can be managed by the user by using the Dhcpv6PdOptionSet.add() and Dhcpv6PdOptionSet.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpv6PdOptionSet'

    def __init__(self, parent):
        super(Dhcpv6PdOptionSet, self).__init__(parent)

    @property
    def Dhcpv6PdOptionTlv(self):
        """An instance of the Dhcpv6PdOptionTlv class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6pdclientglobals.dhcpv6pdoptionset.dhcpv6pdoptiontlv.dhcpv6pdoptiontlv.Dhcpv6PdOptionTlv)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6pdclientglobals.dhcpv6pdoptionset.dhcpv6pdoptiontlv.dhcpv6pdoptiontlv import Dhcpv6PdOptionTlv
        return Dhcpv6PdOptionTlv(self)

    @property
    def Defaultp(self):
        """True to assign this option set to new ranges.

        Returns:
            bool
        """
        return self._get_attribute('defaultp')
    @Defaultp.setter
    def Defaultp(self, value):
        self._set_attribute('defaultp', value)

    @property
    def IpType(self):
        """The IP version used with this option set.

        Returns:
            str
        """
        return self._get_attribute('ipType')
    @IpType.setter
    def IpType(self, value):
        self._set_attribute('ipType', value)

    @property
    def Name(self):
        """Option set name.

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    def update(self, Defaultp=None, IpType=None, Name=None):
        """Updates a child instance of dhcpv6PdOptionSet on the server.

        Args:
            Defaultp (bool): True to assign this option set to new ranges.
            IpType (str): The IP version used with this option set.
            Name (str): Option set name.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Defaultp=None, IpType=None, Name=None):
        """Adds a new dhcpv6PdOptionSet node on the server and retrieves it in this instance.

        Args:
            Defaultp (bool): True to assign this option set to new ranges.
            IpType (str): The IP version used with this option set.
            Name (str): Option set name.

        Returns:
            self: This instance with all currently retrieved dhcpv6PdOptionSet data using find and the newly added dhcpv6PdOptionSet data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the dhcpv6PdOptionSet data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Defaultp=None, IpType=None, Name=None, ObjectId=None):
        """Finds and retrieves dhcpv6PdOptionSet data from the server.

        All named parameters support regex and can be used to selectively retrieve dhcpv6PdOptionSet data from the server.
        By default the find method takes no parameters and will retrieve all dhcpv6PdOptionSet data from the server.

        Args:
            Defaultp (bool): True to assign this option set to new ranges.
            IpType (str): The IP version used with this option set.
            Name (str): Option set name.
            ObjectId (str): Unique identifier for this object

        Returns:
            self: This instance with matching dhcpv6PdOptionSet data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of dhcpv6PdOptionSet data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the dhcpv6PdOptionSet data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
