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


class DceTopologyRange(Base):
    """Sets the DCE Topology of a particular DCE ISIS Topology Range.
    The DceTopologyRange class encapsulates a list of dceTopologyRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the DceTopologyRange.find() method.
    The list can be managed by using the DceTopologyRange.add() and DceTopologyRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "dceTopologyRange"
    _SDM_ATT_MAP = {
        "EnableFtag": "enableFtag",
        "Enabled": "enabled",
        "NicknameList": "nicknameList",
        "NoOfTreesToCompute": "noOfTreesToCompute",
        "StartFtagValue": "startFtagValue",
        "TopologyCount": "topologyCount",
        "TopologyId": "topologyId",
        "TopologyIdStep": "topologyIdStep",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DceTopologyRange, self).__init__(parent, list_op)

    @property
    def DceInterestedVlanRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dceinterestedvlanrange_dbbecc283e17e29acaafa47502d26300.DceInterestedVlanRange): An instance of the DceInterestedVlanRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.dceinterestedvlanrange_dbbecc283e17e29acaafa47502d26300 import (
            DceInterestedVlanRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DceInterestedVlanRange", None) is not None:
                return self._properties.get("DceInterestedVlanRange")
        return DceInterestedVlanRange(self)

    @property
    def EnableFtag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the F tag is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableFtag"])

    @EnableFtag.setter
    def EnableFtag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableFtag"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Signifies if DCE Topology is enabled or disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def NicknameList(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:number)): The list of nicknames.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NicknameList"])

    @NicknameList.setter
    def NicknameList(self, value):
        self._set_attribute(self._SDM_ATT_MAP["NicknameList"], value)

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
    def StartFtagValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, the Ftag value is started.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartFtagValue"])

    @StartFtagValue.setter
    def StartFtagValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartFtagValue"], value)

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

    @property
    def TopologyIdStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It shows the Increment Step of the ID of DCE Topology Range. Default is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TopologyIdStep"])

    @TopologyIdStep.setter
    def TopologyIdStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TopologyIdStep"], value)

    def update(
        self,
        EnableFtag=None,
        Enabled=None,
        NicknameList=None,
        NoOfTreesToCompute=None,
        StartFtagValue=None,
        TopologyCount=None,
        TopologyId=None,
        TopologyIdStep=None,
    ):
        """Updates dceTopologyRange resource on the server.

        Args
        ----
        - EnableFtag (bool): If true, the F tag is enabled.
        - Enabled (bool): Signifies if DCE Topology is enabled or disabled.
        - NicknameList (list(dict(arg1:number,arg2:number,arg3:number))): The list of nicknames.
        - NoOfTreesToCompute (number): The number of trees to compute.
        - StartFtagValue (number): If true, the Ftag value is started.
        - TopologyCount (number): The count of the topology.
        - TopologyId (number): The unique identification number of the topology range.
        - TopologyIdStep (number): It shows the Increment Step of the ID of DCE Topology Range. Default is 1.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        EnableFtag=None,
        Enabled=None,
        NicknameList=None,
        NoOfTreesToCompute=None,
        StartFtagValue=None,
        TopologyCount=None,
        TopologyId=None,
        TopologyIdStep=None,
    ):
        """Adds a new dceTopologyRange resource on the server and adds it to the container.

        Args
        ----
        - EnableFtag (bool): If true, the F tag is enabled.
        - Enabled (bool): Signifies if DCE Topology is enabled or disabled.
        - NicknameList (list(dict(arg1:number,arg2:number,arg3:number))): The list of nicknames.
        - NoOfTreesToCompute (number): The number of trees to compute.
        - StartFtagValue (number): If true, the Ftag value is started.
        - TopologyCount (number): The count of the topology.
        - TopologyId (number): The unique identification number of the topology range.
        - TopologyIdStep (number): It shows the Increment Step of the ID of DCE Topology Range. Default is 1.

        Returns
        -------
        - self: This instance with all currently retrieved dceTopologyRange resources using find and the newly added dceTopologyRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dceTopologyRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        EnableFtag=None,
        Enabled=None,
        NicknameList=None,
        NoOfTreesToCompute=None,
        StartFtagValue=None,
        TopologyCount=None,
        TopologyId=None,
        TopologyIdStep=None,
    ):
        """Finds and retrieves dceTopologyRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dceTopologyRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dceTopologyRange resources from the server.

        Args
        ----
        - EnableFtag (bool): If true, the F tag is enabled.
        - Enabled (bool): Signifies if DCE Topology is enabled or disabled.
        - NicknameList (list(dict(arg1:number,arg2:number,arg3:number))): The list of nicknames.
        - NoOfTreesToCompute (number): The number of trees to compute.
        - StartFtagValue (number): If true, the Ftag value is started.
        - TopologyCount (number): The count of the topology.
        - TopologyId (number): The unique identification number of the topology range.
        - TopologyIdStep (number): It shows the Increment Step of the ID of DCE Topology Range. Default is 1.

        Returns
        -------
        - self: This instance with matching dceTopologyRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dceTopologyRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dceTopologyRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
