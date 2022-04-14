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


class LearnedFilter(Base):
    """This object contains criteria for filtering the learned routes.
    The LearnedFilter class encapsulates a required learnedFilter resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "learnedFilter"
    _SDM_ATT_MAP = {
        "Afi": "afi",
        "EnableAfiSafi": "enableAfiSafi",
        "EnablePrefix": "enablePrefix",
        "Safi": "safi",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LearnedFilter, self).__init__(parent, list_op)

    @property
    def Capabilities(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.capabilities_0f99151175aca98019658ce36676a82c.Capabilities): An instance of the Capabilities class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.capabilities_0f99151175aca98019658ce36676a82c import (
            Capabilities,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Capabilities", None) is not None:
                return self._properties.get("Capabilities")
        return Capabilities(self)._select()

    @property
    def Prefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.prefix_0eba571084c9891c5e7d1691a9106eeb.Prefix): An instance of the Prefix class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.prefix_0eba571084c9891c5e7d1691a9106eeb import (
            Prefix,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Prefix", None) is not None:
                return self._properties.get("Prefix")
        return Prefix(self)._select()

    @property
    def Afi(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Address Family Identifier value. Identifies the network layer protocol to be used with these routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Afi"])

    @Afi.setter
    def Afi(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Afi"], value)

    @property
    def EnableAfiSafi(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, allows the user to set values to be used for BGP-MP - the user-specified AFI and SAFI values for the BGP MP_REACH_NLRI.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAfiSafi"])

    @EnableAfiSafi.setter
    def EnableAfiSafi(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAfiSafi"], value)

    @property
    def EnablePrefix(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, BGP Prefix Filters configured in this dialog will be used to filter for routes that match those filter entries. Only those routes will be stored in the routing table. If disabled, all learned BGP routes will be stored.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePrefix"])

    @EnablePrefix.setter
    def EnablePrefix(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePrefix"], value)

    @property
    def Safi(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Subsequent Address Family Identifier value. Used with, and provides additional information about, the AFI in the NLRI, per RFC 2858.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Safi"])

    @Safi.setter
    def Safi(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Safi"], value)

    def update(self, Afi=None, EnableAfiSafi=None, EnablePrefix=None, Safi=None):
        # type: (int, bool, bool, int) -> LearnedFilter
        """Updates learnedFilter resource on the server.

        Args
        ----
        - Afi (number): Address Family Identifier value. Identifies the network layer protocol to be used with these routes.
        - EnableAfiSafi (bool): If enabled, allows the user to set values to be used for BGP-MP - the user-specified AFI and SAFI values for the BGP MP_REACH_NLRI.
        - EnablePrefix (bool): If enabled, BGP Prefix Filters configured in this dialog will be used to filter for routes that match those filter entries. Only those routes will be stored in the routing table. If disabled, all learned BGP routes will be stored.
        - Safi (number): Subsequent Address Family Identifier value. Used with, and provides additional information about, the AFI in the NLRI, per RFC 2858.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Afi=None, EnableAfiSafi=None, EnablePrefix=None, Safi=None):
        # type: (int, bool, bool, int) -> LearnedFilter
        """Finds and retrieves learnedFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedFilter resources from the server.

        Args
        ----
        - Afi (number): Address Family Identifier value. Identifies the network layer protocol to be used with these routes.
        - EnableAfiSafi (bool): If enabled, allows the user to set values to be used for BGP-MP - the user-specified AFI and SAFI values for the BGP MP_REACH_NLRI.
        - EnablePrefix (bool): If enabled, BGP Prefix Filters configured in this dialog will be used to filter for routes that match those filter entries. Only those routes will be stored in the routing table. If disabled, all learned BGP routes will be stored.
        - Safi (number): Subsequent Address Family Identifier value. Used with, and provides additional information about, the AFI in the NLRI, per RFC 2858.

        Returns
        -------
        - self: This instance with matching learnedFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
