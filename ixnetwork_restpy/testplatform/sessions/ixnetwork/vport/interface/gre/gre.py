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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Gre(Base):
    """Allows the user to set up GRE tunnels from the Ixia port to the DUT port. The GRE protocol can be used to encapsulate packets of many different protocol types and tunnel them across a network of a different protocol type. This basic encapsulation method indicates the Ethertype of the payload packet, and depends on a delivery header with both Layer 2 and Layer 3 information to forward the packet across the network.
    The Gre class encapsulates a required gre resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "gre"
    _SDM_ATT_MAP = {
        "Dest": "dest",
        "InKey": "inKey",
        "OutKey": "outKey",
        "Source": "source",
        "UseChecksum": "useChecksum",
        "UseKey": "useKey",
        "UseSequence": "useSequence",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Gre, self).__init__(parent, list_op)

    @property
    def Dest(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Part of the GRE Delivery Header: The IP address of the Destination router at the remote end of the GRE tunnel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dest"])

    @Dest.setter
    def Dest(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dest"], value)

    @property
    def InKey(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This is the user-assigned GRE header authentication key value that the receiving router will check for to validate GRE packets being sent via the tunnel. All packets sent via a specific tunnel should contain the same key value (one key per GRE tunnel).
        """
        return self._get_attribute(self._SDM_ATT_MAP["InKey"])

    @InKey.setter
    def InKey(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InKey"], value)

    @property
    def OutKey(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This is the user-assigned GRE header authentication key value that will be included in the GRE packets being sent via the tunnel. All packets sent via a specific tunnel should contain the same key value (one key per GRE tunnel). In most cases, the In Key and Out Key will be the same.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutKey"])

    @OutKey.setter
    def OutKey(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutKey"], value)

    @property
    def Source(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface/ipv4 | /api/v1/sessions/1/ixnetwork/vport/interface/ipv6): Part of the GRE Delivery Header: The IP address of the connected interface associated with the source of this GRE tunnel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Source"])

    @Source.setter
    def Source(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Source"], value)

    @property
    def UseChecksum(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of the optional GRE checksum.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseChecksum"])

    @UseChecksum.setter
    def UseChecksum(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseChecksum"], value)

    @property
    def UseKey(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of the optional GRE header key field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseKey"])

    @UseKey.setter
    def UseKey(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseKey"], value)

    @property
    def UseSequence(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If more than one GRE tunnel will be used, this is the amount that will be added to create each additional authentication key value to be sent in the GRE packets (one key per GRE tunnel).
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseSequence"])

    @UseSequence.setter
    def UseSequence(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseSequence"], value)

    def update(
        self,
        Dest=None,
        InKey=None,
        OutKey=None,
        Source=None,
        UseChecksum=None,
        UseKey=None,
        UseSequence=None,
    ):
        # type: (str, int, int, str, bool, bool, bool) -> Gre
        """Updates gre resource on the server.

        Args
        ----
        - Dest (str): Part of the GRE Delivery Header: The IP address of the Destination router at the remote end of the GRE tunnel.
        - InKey (number): This is the user-assigned GRE header authentication key value that the receiving router will check for to validate GRE packets being sent via the tunnel. All packets sent via a specific tunnel should contain the same key value (one key per GRE tunnel).
        - OutKey (number): This is the user-assigned GRE header authentication key value that will be included in the GRE packets being sent via the tunnel. All packets sent via a specific tunnel should contain the same key value (one key per GRE tunnel). In most cases, the In Key and Out Key will be the same.
        - Source (str(None | /api/v1/sessions/1/ixnetwork/vport/interface/ipv4 | /api/v1/sessions/1/ixnetwork/vport/interface/ipv6)): Part of the GRE Delivery Header: The IP address of the connected interface associated with the source of this GRE tunnel.
        - UseChecksum (bool): Enables the use of the optional GRE checksum.
        - UseKey (bool): Enables the use of the optional GRE header key field.
        - UseSequence (bool): If more than one GRE tunnel will be used, this is the amount that will be added to create each additional authentication key value to be sent in the GRE packets (one key per GRE tunnel).

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Dest=None,
        InKey=None,
        OutKey=None,
        Source=None,
        UseChecksum=None,
        UseKey=None,
        UseSequence=None,
    ):
        # type: (str, int, int, str, bool, bool, bool) -> Gre
        """Finds and retrieves gre resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve gre resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all gre resources from the server.

        Args
        ----
        - Dest (str): Part of the GRE Delivery Header: The IP address of the Destination router at the remote end of the GRE tunnel.
        - InKey (number): This is the user-assigned GRE header authentication key value that the receiving router will check for to validate GRE packets being sent via the tunnel. All packets sent via a specific tunnel should contain the same key value (one key per GRE tunnel).
        - OutKey (number): This is the user-assigned GRE header authentication key value that will be included in the GRE packets being sent via the tunnel. All packets sent via a specific tunnel should contain the same key value (one key per GRE tunnel). In most cases, the In Key and Out Key will be the same.
        - Source (str(None | /api/v1/sessions/1/ixnetwork/vport/interface/ipv4 | /api/v1/sessions/1/ixnetwork/vport/interface/ipv6)): Part of the GRE Delivery Header: The IP address of the connected interface associated with the source of this GRE tunnel.
        - UseChecksum (bool): Enables the use of the optional GRE checksum.
        - UseKey (bool): Enables the use of the optional GRE header key field.
        - UseSequence (bool): If more than one GRE tunnel will be used, this is the amount that will be added to create each additional authentication key value to be sent in the GRE packets (one key per GRE tunnel).

        Returns
        -------
        - self: This instance with matching gre resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of gre data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the gre resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
