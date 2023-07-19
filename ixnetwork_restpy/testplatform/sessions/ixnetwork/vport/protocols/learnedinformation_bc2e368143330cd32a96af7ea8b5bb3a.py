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


class LearnedInformation(Base):
    """The ISISL2/L3 Learned Information option fetches and shows the information learned by ISIS.
    The LearnedInformation class encapsulates a required learnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "learnedInformation"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LearnedInformation, self).__init__(parent, list_op)

    @property
    def Ipv4Multicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_ffbbf9bad5b0dd3adbd1429202fe8f05.Ipv4Multicast): An instance of the Ipv4Multicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4multicast_ffbbf9bad5b0dd3adbd1429202fe8f05 import (
            Ipv4Multicast,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4Multicast", None) is not None:
                return self._properties.get("Ipv4Multicast")
        return Ipv4Multicast(self)

    @property
    def Ipv4Prefixes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4prefixes_f96a80cda825b1a5d753e2fdd03c2f4c.Ipv4Prefixes): An instance of the Ipv4Prefixes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4prefixes_f96a80cda825b1a5d753e2fdd03c2f4c import (
            Ipv4Prefixes,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4Prefixes", None) is not None:
                return self._properties.get("Ipv4Prefixes")
        return Ipv4Prefixes(self)

    @property
    def Ipv6Multicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_0096a70d93b3d898efd66f5409ac1aa2.Ipv6Multicast): An instance of the Ipv6Multicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6multicast_0096a70d93b3d898efd66f5409ac1aa2 import (
            Ipv6Multicast,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6Multicast", None) is not None:
                return self._properties.get("Ipv6Multicast")
        return Ipv6Multicast(self)

    @property
    def Ipv6Prefixes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6prefixes_47c8f11b30c65a2910f738a1bde52713.Ipv6Prefixes): An instance of the Ipv6Prefixes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv6prefixes_47c8f11b30c65a2910f738a1bde52713 import (
            Ipv6Prefixes,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6Prefixes", None) is not None:
                return self._properties.get("Ipv6Prefixes")
        return Ipv6Prefixes(self)

    @property
    def MacMulticast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macmulticast_517ac4b2affad69abc45b64c6639080a.MacMulticast): An instance of the MacMulticast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macmulticast_517ac4b2affad69abc45b64c6639080a import (
            MacMulticast,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MacMulticast", None) is not None:
                return self._properties.get("MacMulticast")
        return MacMulticast(self)

    @property
    def RBridges(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rbridges_f1e7cd2ada46dc4fa57a6e5ffb697b8e.RBridges): An instance of the RBridges class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rbridges_f1e7cd2ada46dc4fa57a6e5ffb697b8e import (
            RBridges,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RBridges", None) is not None:
                return self._properties.get("RBridges")
        return RBridges(self)

    @property
    def SpbRbridges(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbrbridges_f27436a3d5a4a17a5d95d4ffeb815ee2.SpbRbridges): An instance of the SpbRbridges class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbrbridges_f27436a3d5a4a17a5d95d4ffeb815ee2 import (
            SpbRbridges,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SpbRbridges", None) is not None:
                return self._properties.get("SpbRbridges")
        return SpbRbridges(self)

    @property
    def TrillMacUnicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillmacunicast_c7ebb4e606f42c0146fa33c6ccd8e6b9.TrillMacUnicast): An instance of the TrillMacUnicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trillmacunicast_c7ebb4e606f42c0146fa33c6ccd8e6b9 import (
            TrillMacUnicast,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrillMacUnicast", None) is not None:
                return self._properties.get("TrillMacUnicast")
        return TrillMacUnicast(self)

    @property
    def TrillOamPing(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trilloamping_91c4c53e08d73819ab1f0099985adc94.TrillOamPing): An instance of the TrillOamPing class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.trilloamping_91c4c53e08d73819ab1f0099985adc94 import (
            TrillOamPing,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TrillOamPing", None) is not None:
                return self._properties.get("TrillOamPing")
        return TrillOamPing(self)

    def find(self):
        """Finds and retrieves learnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInformation resources from the server.

        Returns
        -------
        - self: This instance with matching learnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
