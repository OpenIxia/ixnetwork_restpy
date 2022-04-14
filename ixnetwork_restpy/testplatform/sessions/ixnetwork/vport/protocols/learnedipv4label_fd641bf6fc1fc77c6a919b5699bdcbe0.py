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


class LearnedIpv4Label(Base):
    """A single IPv4 ATM label from the list maintained by interface.
    The LearnedIpv4Label class encapsulates a list of learnedIpv4Label resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedIpv4Label.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "learnedIpv4Label"
    _SDM_ATT_MAP = {
        "Fec": "fec",
        "FecPrefixLen": "fecPrefixLen",
        "Label": "label",
        "LabelSpaceId": "labelSpaceId",
        "PeerIpAddress": "peerIpAddress",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LearnedIpv4Label, self).__init__(parent, list_op)

    @property
    def Fec(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Forwarding equivalence class (FEC) type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Fec"])

    @property
    def FecPrefixLen(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The length of the prefix associated with the FEC.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecPrefixLen"])

    @property
    def Label(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The label value added to the packet(s) by the upstream LDP peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Label"])

    @property
    def LabelSpaceId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Part of the LSR ID. It forms the last 2 octets of the 6-octet LDP identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LabelSpaceId"])

    @property
    def PeerIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The RID of the upstream LDP peer. Part of the LSR ID. It must be globally unique. It forms the first 4 octets of the 6-octet LDP identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerIpAddress"])

    def add(self):
        """Adds a new learnedIpv4Label resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved learnedIpv4Label resources using find and the newly added learnedIpv4Label resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Fec=None,
        FecPrefixLen=None,
        Label=None,
        LabelSpaceId=None,
        PeerIpAddress=None,
    ):
        # type: (str, int, int, int, str) -> LearnedIpv4Label
        """Finds and retrieves learnedIpv4Label resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedIpv4Label resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedIpv4Label resources from the server.

        Args
        ----
        - Fec (str): Forwarding equivalence class (FEC) type.
        - FecPrefixLen (number): The length of the prefix associated with the FEC.
        - Label (number): The label value added to the packet(s) by the upstream LDP peer.
        - LabelSpaceId (number): Part of the LSR ID. It forms the last 2 octets of the 6-octet LDP identifier.
        - PeerIpAddress (str): The RID of the upstream LDP peer. Part of the LSR ID. It must be globally unique. It forms the first 4 octets of the 6-octet LDP identifier.

        Returns
        -------
        - self: This instance with matching learnedIpv4Label resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedIpv4Label data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedIpv4Label resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
