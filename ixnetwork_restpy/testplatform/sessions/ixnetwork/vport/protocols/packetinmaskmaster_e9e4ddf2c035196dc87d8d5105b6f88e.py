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


class PacketInMaskMaster(Base):
    """When packets are received by the datapath and sent to the Controller, it may get no response from the Controller based on what the asynchronous message contains
    The PacketInMaskMaster class encapsulates a required packetInMaskMaster resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "packetInMaskMaster"
    _SDM_ATT_MAP = {
        "Action": "action",
        "InvalidTtl": "invalidTtl",
        "NoMatch": "noMatch",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PacketInMaskMaster, self).__init__(parent, list_op)

    @property
    def Action(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Action explicitly output to controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Action"])

    @Action.setter
    def Action(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Action"], value)

    @property
    def InvalidTtl(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This indicates that a packet with an invalid IP TTL or MPLS TTL was rejected by the OpenFlow pipeline and passed to the controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidTtl"])

    @InvalidTtl.setter
    def InvalidTtl(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidTtl"], value)

    @property
    def NoMatch(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This indicates that a packet with no matching flow (table-miss flow entry) is passed to the controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoMatch"])

    @NoMatch.setter
    def NoMatch(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoMatch"], value)

    def update(self, Action=None, InvalidTtl=None, NoMatch=None):
        # type: (bool, bool, bool) -> PacketInMaskMaster
        """Updates packetInMaskMaster resource on the server.

        Args
        ----
        - Action (bool): Action explicitly output to controller.
        - InvalidTtl (bool): This indicates that a packet with an invalid IP TTL or MPLS TTL was rejected by the OpenFlow pipeline and passed to the controller.
        - NoMatch (bool): This indicates that a packet with no matching flow (table-miss flow entry) is passed to the controller.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Action=None, InvalidTtl=None, NoMatch=None):
        # type: (bool, bool, bool) -> PacketInMaskMaster
        """Finds and retrieves packetInMaskMaster resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve packetInMaskMaster resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all packetInMaskMaster resources from the server.

        Args
        ----
        - Action (bool): Action explicitly output to controller.
        - InvalidTtl (bool): This indicates that a packet with an invalid IP TTL or MPLS TTL was rejected by the OpenFlow pipeline and passed to the controller.
        - NoMatch (bool): This indicates that a packet with no matching flow (table-miss flow entry) is passed to the controller.

        Returns
        -------
        - self: This instance with matching packetInMaskMaster resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of packetInMaskMaster data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the packetInMaskMaster resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
