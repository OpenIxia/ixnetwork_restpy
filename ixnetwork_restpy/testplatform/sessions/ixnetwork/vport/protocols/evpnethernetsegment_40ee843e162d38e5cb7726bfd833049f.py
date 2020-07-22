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


class EvpnEthernetSegment(Base):
    """(Read Only) EVPN Ethernet Segment route type.
    The EvpnEthernetSegment class encapsulates a list of evpnEthernetSegment resources that are managed by the system.
    A list of resources can be retrieved from the server using the EvpnEthernetSegment.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'evpnEthernetSegment'
    _SDM_ATT_MAP = {
        'Esi': 'esi',
        'Neighbor': 'neighbor',
    }

    def __init__(self, parent):
        super(EvpnEthernetSegment, self).__init__(parent)

    @property
    def OriginIpInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.originipinfo_23d90847d9ffce969bc4e52d8acb6233.OriginIpInfo): An instance of the OriginIpInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.originipinfo_23d90847d9ffce969bc4e52d8acb6233 import OriginIpInfo
        return OriginIpInfo(self)

    @property
    def Esi(self):
        """
        Returns
        -------
        - str: (Read Only) Learned Ethernet Segment Id.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Esi'])

    @property
    def Neighbor(self):
        """
        Returns
        -------
        - str: (Read Only) Neighbor IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Neighbor'])

    def find(self, Esi=None, Neighbor=None):
        """Finds and retrieves evpnEthernetSegment resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve evpnEthernetSegment resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all evpnEthernetSegment resources from the server.

        Args
        ----
        - Esi (str): (Read Only) Learned Ethernet Segment Id.
        - Neighbor (str): (Read Only) Neighbor IP.

        Returns
        -------
        - self: This instance with matching evpnEthernetSegment resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of evpnEthernetSegment data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the evpnEthernetSegment resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
