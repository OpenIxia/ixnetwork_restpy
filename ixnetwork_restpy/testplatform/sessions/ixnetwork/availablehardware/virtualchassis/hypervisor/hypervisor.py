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


class Hypervisor(Base):
    """List of hypervisor credentials
    The Hypervisor class encapsulates a list of hypervisor resources that are managed by the user.
    A list of resources can be retrieved from the server using the Hypervisor.find() method.
    The list can be managed by using the Hypervisor.add() and Hypervisor.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'hypervisor'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'Password': 'password',
        'ServerIp': 'serverIp',
        'Type': 'type',
        'User': 'user',
    }

    def __init__(self, parent):
        super(Hypervisor, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true the hypervisor is enabled
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Password(self):
        """
        Returns
        -------
        - str: Represents the hypervisor password
        """
        return self._get_attribute(self._SDM_ATT_MAP['Password'])
    @Password.setter
    def Password(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Password'], value)

    @property
    def ServerIp(self):
        """
        Returns
        -------
        - str: Represents the hypervisor Ip
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerIp'])
    @ServerIp.setter
    def ServerIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerIp'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(qemu | vCenter | vmware): Represents the hypervisor host type
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    @property
    def User(self):
        """
        Returns
        -------
        - str: Represents the hypervisor username
        """
        return self._get_attribute(self._SDM_ATT_MAP['User'])
    @User.setter
    def User(self, value):
        self._set_attribute(self._SDM_ATT_MAP['User'], value)

    def update(self, Enabled=None, Password=None, ServerIp=None, Type=None, User=None):
        """Updates hypervisor resource on the server.

        Args
        ----
        - Enabled (bool): If true the hypervisor is enabled
        - Password (str): Represents the hypervisor password
        - ServerIp (str): Represents the hypervisor Ip
        - Type (str(qemu | vCenter | vmware)): Represents the hypervisor host type
        - User (str): Represents the hypervisor username

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, Password=None, ServerIp=None, Type=None, User=None):
        """Adds a new hypervisor resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true the hypervisor is enabled
        - Password (str): Represents the hypervisor password
        - ServerIp (str): Represents the hypervisor Ip
        - Type (str(qemu | vCenter | vmware)): Represents the hypervisor host type
        - User (str): Represents the hypervisor username

        Returns
        -------
        - self: This instance with all currently retrieved hypervisor resources using find and the newly added hypervisor resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained hypervisor resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, Password=None, ServerIp=None, Type=None, User=None):
        """Finds and retrieves hypervisor resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve hypervisor resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all hypervisor resources from the server.

        Args
        ----
        - Enabled (bool): If true the hypervisor is enabled
        - Password (str): Represents the hypervisor password
        - ServerIp (str): Represents the hypervisor Ip
        - Type (str(qemu | vCenter | vmware)): Represents the hypervisor host type
        - User (str): Represents the hypervisor username

        Returns
        -------
        - self: This instance with matching hypervisor resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of hypervisor data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the hypervisor resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
