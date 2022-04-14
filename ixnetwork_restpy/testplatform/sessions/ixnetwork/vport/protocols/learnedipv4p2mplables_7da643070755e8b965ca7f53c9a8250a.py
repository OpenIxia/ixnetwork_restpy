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


class LearnedIpv4P2mpLables(Base):
    """This objects dispalys the learned IPv4 P2MP Labels.
    The LearnedIpv4P2mpLables class encapsulates a list of learnedIpv4P2mpLables resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedIpv4P2mpLables.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "learnedIpv4P2mpLables"
    _SDM_ATT_MAP = {
        "Label": "label",
        "LabelSpaceId": "labelSpaceId",
        "PeerIpAddress": "peerIpAddress",
        "RootAddress": "rootAddress",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LearnedIpv4P2mpLables, self).__init__(parent, list_op)

    @property
    def OpaqueValueElement(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_bcb70021648725c2761a10020b6ef5cc.OpaqueValueElement): An instance of the OpaqueValueElement class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_bcb70021648725c2761a10020b6ef5cc import (
            OpaqueValueElement,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OpaqueValueElement", None) is not None:
                return self._properties.get("OpaqueValueElement")
        return OpaqueValueElement(self)

    @property
    def Label(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the label value added to the packet(s) by the upstream LDP peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Label"])

    @property
    def LabelSpaceId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Part of the LSR Id. It forms the last 2 octets of the 6-octet LDP Identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LabelSpaceId"])

    @property
    def PeerIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The RID of the upstream LDP peer. Part of the LSR Id. It must be globally unique. It forms the first 4 octets of the 6-octet LDP Identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerIpAddress"])

    @property
    def RootAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Root Address of IPv4 P2MP labels learned.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RootAddress"])

    def add(self):
        """Adds a new learnedIpv4P2mpLables resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved learnedIpv4P2mpLables resources using find and the newly added learnedIpv4P2mpLables resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Label=None, LabelSpaceId=None, PeerIpAddress=None, RootAddress=None):
        # type: (int, int, str, str) -> LearnedIpv4P2mpLables
        """Finds and retrieves learnedIpv4P2mpLables resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedIpv4P2mpLables resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedIpv4P2mpLables resources from the server.

        Args
        ----
        - Label (number): Indicates the label value added to the packet(s) by the upstream LDP peer.
        - LabelSpaceId (number): Part of the LSR Id. It forms the last 2 octets of the 6-octet LDP Identifier.
        - PeerIpAddress (str): The RID of the upstream LDP peer. Part of the LSR Id. It must be globally unique. It forms the first 4 octets of the 6-octet LDP Identifier.
        - RootAddress (str): Root Address of IPv4 P2MP labels learned.

        Returns
        -------
        - self: This instance with matching learnedIpv4P2mpLables resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedIpv4P2mpLables data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedIpv4P2mpLables resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
