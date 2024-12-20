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


class Plca(Base):
    """
    The Plca class encapsulates a required plca resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "plca"
    _SDM_ATT_MAP = {
        "BurstCount": "burstCount",
        "BurstTimer": "burstTimer",
        "Enable": "enable",
        "NodeCount": "nodeCount",
        "NodeId": "nodeId",
        "NodeType": "nodeType",
        "TransmitOpportunityTimer": "transmitOpportunityTimer",
    }
    _SDM_ENUM_MAP = {
        "nodeType": ["coordinator", "follower"],
    }

    def __init__(self, parent, list_op=False):
        super(Plca, self).__init__(parent, list_op)

    @property
    def BurstCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of additional packets allowed to be transmitted in a single transmit opportunity window.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BurstCount"])

    @BurstCount.setter
    def BurstCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BurstCount"], value)

    @property
    def BurstTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum number of bit-times the PLCA network waits for a new packet before yielding the transmit opportunity window. Each increment in this field represents 100ns i.e. the value 2 represents 200 ns, and so on.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BurstTimer"])

    @BurstTimer.setter
    def BurstTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BurstTimer"], value)

    @property
    def Enable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable Physical Layer Collision Avoidance(PLCA).
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enable"])

    @Enable.setter
    def Enable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enable"], value)

    @property
    def NodeCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of nodes on the PLCA network.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NodeCount"])

    @NodeCount.setter
    def NodeCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NodeCount"], value)

    @property
    def NodeId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: ID of the local node on the PLCA network.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NodeId"])

    @NodeId.setter
    def NodeId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NodeId"], value)

    @property
    def NodeType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(coordinator | follower): Node can be a coordinator(nodeId= 0) or follower(nodeId= 1 to 254).
        """
        return self._get_attribute(self._SDM_ATT_MAP["NodeType"])

    @property
    def TransmitOpportunityTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Transmit opportunity timer is used to establish Transmit Opportunities(TOs) for each node in the PLCA network.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitOpportunityTimer"])

    @TransmitOpportunityTimer.setter
    def TransmitOpportunityTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitOpportunityTimer"], value)

    def update(
        self,
        BurstCount=None,
        BurstTimer=None,
        Enable=None,
        NodeCount=None,
        NodeId=None,
        TransmitOpportunityTimer=None,
    ):
        # type: (int, int, bool, int, int, int) -> Plca
        """Updates plca resource on the server.

        Args
        ----
        - BurstCount (number): Maximum number of additional packets allowed to be transmitted in a single transmit opportunity window.
        - BurstTimer (number): Maximum number of bit-times the PLCA network waits for a new packet before yielding the transmit opportunity window. Each increment in this field represents 100ns i.e. the value 2 represents 200 ns, and so on.
        - Enable (bool): Enable Physical Layer Collision Avoidance(PLCA).
        - NodeCount (number): Number of nodes on the PLCA network.
        - NodeId (number): ID of the local node on the PLCA network.
        - TransmitOpportunityTimer (number): Transmit opportunity timer is used to establish Transmit Opportunities(TOs) for each node in the PLCA network.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BurstCount=None,
        BurstTimer=None,
        Enable=None,
        NodeCount=None,
        NodeId=None,
        NodeType=None,
        TransmitOpportunityTimer=None,
    ):
        # type: (int, int, bool, int, int, str, int) -> Plca
        """Finds and retrieves plca resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve plca resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all plca resources from the server.

        Args
        ----
        - BurstCount (number): Maximum number of additional packets allowed to be transmitted in a single transmit opportunity window.
        - BurstTimer (number): Maximum number of bit-times the PLCA network waits for a new packet before yielding the transmit opportunity window. Each increment in this field represents 100ns i.e. the value 2 represents 200 ns, and so on.
        - Enable (bool): Enable Physical Layer Collision Avoidance(PLCA).
        - NodeCount (number): Number of nodes on the PLCA network.
        - NodeId (number): ID of the local node on the PLCA network.
        - NodeType (str(coordinator | follower)): Node can be a coordinator(nodeId= 0) or follower(nodeId= 1 to 254).
        - TransmitOpportunityTimer (number): Transmit opportunity timer is used to establish Transmit Opportunities(TOs) for each node in the PLCA network.

        Returns
        -------
        - self: This instance with matching plca resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of plca data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the plca resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
