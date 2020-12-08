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


class VpnParameter(Base):
    """VPN
    The VpnParameter class encapsulates a list of vpnParameter resources that are managed by the user.
    A list of resources can be retrieved from the server using the VpnParameter.find() method.
    The list can be managed by using the VpnParameter.add() and VpnParameter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vpnParameter'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'SiteId': 'siteId',
        'UseVpnParameters': 'useVpnParameters',
    }

    def __init__(self, parent):
        super(VpnParameter, self).__init__(parent)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def SiteId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VPN Site Identifier
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SiteId']))

    @property
    def UseVpnParameters(self):
        """
        Returns
        -------
        - bool: Flag to determine whether optional VPN parameters are provided.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseVpnParameters'])
    @UseVpnParameters.setter
    def UseVpnParameters(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseVpnParameters'], value)

    def update(self, UseVpnParameters=None):
        """Updates vpnParameter resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - UseVpnParameters (bool): Flag to determine whether optional VPN parameters are provided.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, UseVpnParameters=None):
        """Adds a new vpnParameter resource on the server and adds it to the container.

        Args
        ----
        - UseVpnParameters (bool): Flag to determine whether optional VPN parameters are provided.

        Returns
        -------
        - self: This instance with all currently retrieved vpnParameter resources using find and the newly added vpnParameter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained vpnParameter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, UseVpnParameters=None):
        """Finds and retrieves vpnParameter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vpnParameter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vpnParameter resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - UseVpnParameters (bool): Flag to determine whether optional VPN parameters are provided.

        Returns
        -------
        - self: This instance with matching vpnParameter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vpnParameter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vpnParameter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, SiteId=None):
        """Base class infrastructure that gets a list of vpnParameter device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - SiteId (str): optional regex of siteId

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
