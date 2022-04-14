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


class DceNodeTopologyRange(Base):
    """Sets the DCE Node Topology of a particular DCE ISIS Topology Range.
    The DceNodeTopologyRange class encapsulates a list of dceNodeTopologyRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the DceNodeTopologyRange.find() method.
    The list can be managed by using the DceNodeTopologyRange.add() and DceNodeTopologyRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "dceNodeTopologyRange"
    _SDM_ATT_MAP = {
        "BroadcastPriority": "broadcastPriority",
        "IncludeL2Topology": "includeL2Topology",
        "InternodeNicknameIncrement": "internodeNicknameIncrement",
        "NicknameCount": "nicknameCount",
        "NoOfTreesToCompute": "noOfTreesToCompute",
        "StartNickname": "startNickname",
        "TopologyCount": "topologyCount",
        "TopologyId": "topologyId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DceNodeTopologyRange, self).__init__(parent, list_op)

    @property
    def DceNodeInterestedVlanRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenodeinterestedvlanrange_b15c6822c508a957290b5d3ed2b3ea4e.DceNodeInterestedVlanRange): An instance of the DceNodeInterestedVlanRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dcenodeinterestedvlanrange_b15c6822c508a957290b5d3ed2b3ea4e import (
            DceNodeInterestedVlanRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DceNodeInterestedVlanRange", None) is not None:
                return self._properties.get("DceNodeInterestedVlanRange")
        return DceNodeInterestedVlanRange(self)

    @property
    def BroadcastPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the priority in which the topology is broadcast.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BroadcastPriority"])

    @BroadcastPriority.setter
    def BroadcastPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BroadcastPriority"], value)

    @property
    def IncludeL2Topology(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, includes the L2 topology.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeL2Topology"])

    @IncludeL2Topology.setter
    def IncludeL2Topology(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeL2Topology"], value)

    @property
    def InternodeNicknameIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The increment step to be used for creating the internode increment.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InternodeNicknameIncrement"])

    @InternodeNicknameIncrement.setter
    def InternodeNicknameIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InternodeNicknameIncrement"], value)

    @property
    def NicknameCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The count of the nickname.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NicknameCount"])

    @NicknameCount.setter
    def NicknameCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NicknameCount"], value)

    @property
    def NoOfTreesToCompute(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of trees to compute.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfTreesToCompute"])

    @NoOfTreesToCompute.setter
    def NoOfTreesToCompute(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfTreesToCompute"], value)

    @property
    def StartNickname(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, uses the nickname.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartNickname"])

    @StartNickname.setter
    def StartNickname(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartNickname"], value)

    @property
    def TopologyCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The count of the topology.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TopologyCount"])

    @TopologyCount.setter
    def TopologyCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TopologyCount"], value)

    @property
    def TopologyId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique identification number of the topology range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TopologyId"])

    @TopologyId.setter
    def TopologyId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TopologyId"], value)

    def update(
        self,
        BroadcastPriority=None,
        IncludeL2Topology=None,
        InternodeNicknameIncrement=None,
        NicknameCount=None,
        NoOfTreesToCompute=None,
        StartNickname=None,
        TopologyCount=None,
        TopologyId=None,
    ):
        # type: (int, bool, int, int, int, int, int, int) -> DceNodeTopologyRange
        """Updates dceNodeTopologyRange resource on the server.

        Args
        ----
        - BroadcastPriority (number): Sets the priority in which the topology is broadcast.
        - IncludeL2Topology (bool): If true, includes the L2 topology.
        - InternodeNicknameIncrement (number): The increment step to be used for creating the internode increment.
        - NicknameCount (number): The count of the nickname.
        - NoOfTreesToCompute (number): The number of trees to compute.
        - StartNickname (number): If true, uses the nickname.
        - TopologyCount (number): The count of the topology.
        - TopologyId (number): The unique identification number of the topology range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        BroadcastPriority=None,
        IncludeL2Topology=None,
        InternodeNicknameIncrement=None,
        NicknameCount=None,
        NoOfTreesToCompute=None,
        StartNickname=None,
        TopologyCount=None,
        TopologyId=None,
    ):
        # type: (int, bool, int, int, int, int, int, int) -> DceNodeTopologyRange
        """Adds a new dceNodeTopologyRange resource on the server and adds it to the container.

        Args
        ----
        - BroadcastPriority (number): Sets the priority in which the topology is broadcast.
        - IncludeL2Topology (bool): If true, includes the L2 topology.
        - InternodeNicknameIncrement (number): The increment step to be used for creating the internode increment.
        - NicknameCount (number): The count of the nickname.
        - NoOfTreesToCompute (number): The number of trees to compute.
        - StartNickname (number): If true, uses the nickname.
        - TopologyCount (number): The count of the topology.
        - TopologyId (number): The unique identification number of the topology range.

        Returns
        -------
        - self: This instance with all currently retrieved dceNodeTopologyRange resources using find and the newly added dceNodeTopologyRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dceNodeTopologyRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        BroadcastPriority=None,
        IncludeL2Topology=None,
        InternodeNicknameIncrement=None,
        NicknameCount=None,
        NoOfTreesToCompute=None,
        StartNickname=None,
        TopologyCount=None,
        TopologyId=None,
    ):
        # type: (int, bool, int, int, int, int, int, int) -> DceNodeTopologyRange
        """Finds and retrieves dceNodeTopologyRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dceNodeTopologyRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dceNodeTopologyRange resources from the server.

        Args
        ----
        - BroadcastPriority (number): Sets the priority in which the topology is broadcast.
        - IncludeL2Topology (bool): If true, includes the L2 topology.
        - InternodeNicknameIncrement (number): The increment step to be used for creating the internode increment.
        - NicknameCount (number): The count of the nickname.
        - NoOfTreesToCompute (number): The number of trees to compute.
        - StartNickname (number): If true, uses the nickname.
        - TopologyCount (number): The count of the topology.
        - TopologyId (number): The unique identification number of the topology range.

        Returns
        -------
        - self: This instance with matching dceNodeTopologyRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dceNodeTopologyRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dceNodeTopologyRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
