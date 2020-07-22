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


class TargetPeer(Base):
    """This object holds information about a targeted peer to be associated with an LDP interface. The optional LDP test package must be installed in order for this command to operate.
    The TargetPeer class encapsulates a list of targetPeer resources that are managed by the user.
    A list of resources can be retrieved from the server using the TargetPeer.find() method.
    The list can be managed by using the TargetPeer.add() and TargetPeer.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'targetPeer'
    _SDM_ATT_MAP = {
        'Authentication': 'authentication',
        'Enabled': 'enabled',
        'InitiateTargetedHello': 'initiateTargetedHello',
        'IpAddress': 'ipAddress',
        'Md5Key': 'md5Key',
    }

    def __init__(self, parent):
        super(TargetPeer, self).__init__(parent)

    @property
    def Authentication(self):
        """
        Returns
        -------
        - str(null | md5): The cryptographic authentication type used by the targeted peer; one of: NULL (no authentication) or MD5. When MD5 is used, an md5Key must be configured by the user.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Authentication'])
    @Authentication.setter
    def Authentication(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Authentication'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of this targeted peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def InitiateTargetedHello(self):
        """
        Returns
        -------
        - bool: If true, the target peer is set a hello message exclusively.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InitiateTargetedHello'])
    @InitiateTargetedHello.setter
    def InitiateTargetedHello(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InitiateTargetedHello'], value)

    @property
    def IpAddress(self):
        """
        Returns
        -------
        - str: The IP address of the targeted peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpAddress'])
    @IpAddress.setter
    def IpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpAddress'], value)

    @property
    def Md5Key(self):
        """
        Returns
        -------
        - str: Used with MD5 authentication. A user-defined string; maximum = 255 characters.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Md5Key'])
    @Md5Key.setter
    def Md5Key(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Md5Key'], value)

    def update(self, Authentication=None, Enabled=None, InitiateTargetedHello=None, IpAddress=None, Md5Key=None):
        """Updates targetPeer resource on the server.

        Args
        ----
        - Authentication (str(null | md5)): The cryptographic authentication type used by the targeted peer; one of: NULL (no authentication) or MD5. When MD5 is used, an md5Key must be configured by the user.
        - Enabled (bool): Enables the use of this targeted peer.
        - InitiateTargetedHello (bool): If true, the target peer is set a hello message exclusively.
        - IpAddress (str): The IP address of the targeted peer.
        - Md5Key (str): Used with MD5 authentication. A user-defined string; maximum = 255 characters.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Authentication=None, Enabled=None, InitiateTargetedHello=None, IpAddress=None, Md5Key=None):
        """Adds a new targetPeer resource on the server and adds it to the container.

        Args
        ----
        - Authentication (str(null | md5)): The cryptographic authentication type used by the targeted peer; one of: NULL (no authentication) or MD5. When MD5 is used, an md5Key must be configured by the user.
        - Enabled (bool): Enables the use of this targeted peer.
        - InitiateTargetedHello (bool): If true, the target peer is set a hello message exclusively.
        - IpAddress (str): The IP address of the targeted peer.
        - Md5Key (str): Used with MD5 authentication. A user-defined string; maximum = 255 characters.

        Returns
        -------
        - self: This instance with all currently retrieved targetPeer resources using find and the newly added targetPeer resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained targetPeer resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Authentication=None, Enabled=None, InitiateTargetedHello=None, IpAddress=None, Md5Key=None):
        """Finds and retrieves targetPeer resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve targetPeer resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all targetPeer resources from the server.

        Args
        ----
        - Authentication (str(null | md5)): The cryptographic authentication type used by the targeted peer; one of: NULL (no authentication) or MD5. When MD5 is used, an md5Key must be configured by the user.
        - Enabled (bool): Enables the use of this targeted peer.
        - InitiateTargetedHello (bool): If true, the target peer is set a hello message exclusively.
        - IpAddress (str): The IP address of the targeted peer.
        - Md5Key (str): Used with MD5 authentication. A user-defined string; maximum = 255 characters.

        Returns
        -------
        - self: This instance with matching targetPeer resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of targetPeer data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the targetPeer resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
