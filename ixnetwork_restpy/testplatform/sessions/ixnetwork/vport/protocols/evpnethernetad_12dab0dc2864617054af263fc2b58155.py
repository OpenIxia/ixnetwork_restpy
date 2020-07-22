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


class EvpnEthernetAd(Base):
    """(Read Only) Ethernet Auto-Discovery route type.
    The EvpnEthernetAd class encapsulates a list of evpnEthernetAd resources that are managed by the system.
    A list of resources can be retrieved from the server using the EvpnEthernetAd.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'evpnEthernetAd'
    _SDM_ATT_MAP = {
        'Esi': 'esi',
        'Neighbor': 'neighbor',
    }

    def __init__(self, parent):
        super(EvpnEthernetAd, self).__init__(parent)

    @property
    def NextHopInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexthopinfo_40741fdc50dd0497f1076fabd3d74d08.NextHopInfo): An instance of the NextHopInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nexthopinfo_40741fdc50dd0497f1076fabd3d74d08 import NextHopInfo
        return NextHopInfo(self)

    @property
    def Esi(self):
        """
        Returns
        -------
        - str: (Read Only) Ethernet Segment ID.
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
        """Finds and retrieves evpnEthernetAd resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve evpnEthernetAd resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all evpnEthernetAd resources from the server.

        Args
        ----
        - Esi (str): (Read Only) Ethernet Segment ID.
        - Neighbor (str): (Read Only) Neighbor IP.

        Returns
        -------
        - self: This instance with matching evpnEthernetAd resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of evpnEthernetAd data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the evpnEthernetAd resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
