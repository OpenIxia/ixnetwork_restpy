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


class AdVpls(Base):
    """Helps to configure the attributes for the AD VPLS ranges.
    The AdVpls class encapsulates a list of adVpls resources that are managed by the system.
    A list of resources can be retrieved from the server using the AdVpls.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'adVpls'
    _SDM_ATT_MAP = {
        'NeighborAddress': 'neighborAddress',
        'NextHopAddress': 'nextHopAddress',
        'RemotePeAddress': 'remotePeAddress',
        'RemoteVplsId': 'remoteVplsId',
        'RemoteVsiId': 'remoteVsiId',
        'RouteDistinguisher': 'routeDistinguisher',
        'RouteTarget': 'routeTarget',
        'SupportedLocally': 'supportedLocally',
    }

    def __init__(self, parent):
        super(AdVpls, self).__init__(parent)

    @property
    def NeighborAddress(self):
        """
        Returns
        -------
        - str: (Read Only) The descriptive identifier for the BGP neighbor.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NeighborAddress'])

    @property
    def NextHopAddress(self):
        """
        Returns
        -------
        - str: (Read Only) A 4-octet IP address which indicates the next hop.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextHopAddress'])

    @property
    def RemotePeAddress(self):
        """
        Returns
        -------
        - str: (Read Only) The descriptive identifier for the remote PE.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemotePeAddress'])

    @property
    def RemoteVplsId(self):
        """
        Returns
        -------
        - str: (Read Only) The remote VPLS ID indicated by an IP or AS.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteVplsId'])

    @property
    def RemoteVsiId(self):
        """
        Returns
        -------
        - number: (Read Only) The remote VSI Id indicated by 4 bytes unsigned number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteVsiId'])

    @property
    def RouteDistinguisher(self):
        """
        Returns
        -------
        - str: (Read Only) The route distinguisher indicated by the IP or AS number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteDistinguisher'])

    @property
    def RouteTarget(self):
        """
        Returns
        -------
        - str: (Read Only) The route target indicated by the IP or AS number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouteTarget'])

    @property
    def SupportedLocally(self):
        """
        Returns
        -------
        - bool: (Read Only) The boolean value indicating whether it is supported locally.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportedLocally'])

    def find(self, NeighborAddress=None, NextHopAddress=None, RemotePeAddress=None, RemoteVplsId=None, RemoteVsiId=None, RouteDistinguisher=None, RouteTarget=None, SupportedLocally=None):
        """Finds and retrieves adVpls resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve adVpls resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all adVpls resources from the server.

        Args
        ----
        - NeighborAddress (str): (Read Only) The descriptive identifier for the BGP neighbor.
        - NextHopAddress (str): (Read Only) A 4-octet IP address which indicates the next hop.
        - RemotePeAddress (str): (Read Only) The descriptive identifier for the remote PE.
        - RemoteVplsId (str): (Read Only) The remote VPLS ID indicated by an IP or AS.
        - RemoteVsiId (number): (Read Only) The remote VSI Id indicated by 4 bytes unsigned number.
        - RouteDistinguisher (str): (Read Only) The route distinguisher indicated by the IP or AS number.
        - RouteTarget (str): (Read Only) The route target indicated by the IP or AS number.
        - SupportedLocally (bool): (Read Only) The boolean value indicating whether it is supported locally.

        Returns
        -------
        - self: This instance with matching adVpls resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of adVpls data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the adVpls resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
