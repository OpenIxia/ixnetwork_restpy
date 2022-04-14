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


class GroupTypes(Base):
    """Specify the group types supported by Switch.
    The GroupTypes class encapsulates a required groupTypes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "groupTypes"
    _SDM_ATT_MAP = {
        "All": "all",
        "FastFailover": "fastFailover",
        "Indirect": "indirect",
        "Select": "select",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(GroupTypes, self).__init__(parent, list_op)

    @property
    def All(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, all buckets in the group are forwarded. This group is used for multicast or broadcast forwarding. The packet is effectively cloned for each bucket. One packet is processed for each bucket of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["All"])

    @All.setter
    def All(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["All"], value)

    @property
    def FastFailover(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, the first active bucket is forwarded. Each action bucket is associated with a specific port and/or group that controls its liveness. The buckets are evaluated in the order defined by the group, and the first bucket which is associated with a live port/group is selected. This group type allows the switch to change forwarding without requiring a round trip to the controller. If no buckets are live, packets are dropped.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastFailover"])

    @FastFailover.setter
    def FastFailover(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastFailover"], value)

    @property
    def Indirect(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, the one defined bucket in this group is forwarded. This group supports only a single bucket. It allows multiple flow entries or groups to point to a common group identifier, supporting faster, more efficient convergence. For instance, next hops for IP forwarding.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Indirect"])

    @Indirect.setter
    def Indirect(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Indirect"], value)

    @property
    def Select(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, a single bucket in the group is forwarded.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Select"])

    @Select.setter
    def Select(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Select"], value)

    def update(self, All=None, FastFailover=None, Indirect=None, Select=None):
        # type: (bool, bool, bool, bool) -> GroupTypes
        """Updates groupTypes resource on the server.

        Args
        ----
        - All (bool): If selected, all buckets in the group are forwarded. This group is used for multicast or broadcast forwarding. The packet is effectively cloned for each bucket. One packet is processed for each bucket of the group.
        - FastFailover (bool): If selected, the first active bucket is forwarded. Each action bucket is associated with a specific port and/or group that controls its liveness. The buckets are evaluated in the order defined by the group, and the first bucket which is associated with a live port/group is selected. This group type allows the switch to change forwarding without requiring a round trip to the controller. If no buckets are live, packets are dropped.
        - Indirect (bool): If selected, the one defined bucket in this group is forwarded. This group supports only a single bucket. It allows multiple flow entries or groups to point to a common group identifier, supporting faster, more efficient convergence. For instance, next hops for IP forwarding.
        - Select (bool): If selected, a single bucket in the group is forwarded.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, All=None, FastFailover=None, Indirect=None, Select=None):
        # type: (bool, bool, bool, bool) -> GroupTypes
        """Finds and retrieves groupTypes resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve groupTypes resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all groupTypes resources from the server.

        Args
        ----
        - All (bool): If selected, all buckets in the group are forwarded. This group is used for multicast or broadcast forwarding. The packet is effectively cloned for each bucket. One packet is processed for each bucket of the group.
        - FastFailover (bool): If selected, the first active bucket is forwarded. Each action bucket is associated with a specific port and/or group that controls its liveness. The buckets are evaluated in the order defined by the group, and the first bucket which is associated with a live port/group is selected. This group type allows the switch to change forwarding without requiring a round trip to the controller. If no buckets are live, packets are dropped.
        - Indirect (bool): If selected, the one defined bucket in this group is forwarded. This group supports only a single bucket. It allows multiple flow entries or groups to point to a common group identifier, supporting faster, more efficient convergence. For instance, next hops for IP forwarding.
        - Select (bool): If selected, a single bucket in the group is forwarded.

        Returns
        -------
        - self: This instance with matching groupTypes resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of groupTypes data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the groupTypes resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
