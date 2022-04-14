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


class OfTopologyLearnedInformation(Base):
    """This object allows to configure the OF Toplogy Learned Information parameters.
    The OfTopologyLearnedInformation class encapsulates a required ofTopologyLearnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ofTopologyLearnedInformation"
    _SDM_ATT_MAP = {
        "EnableInstallLldpFlow": "enableInstallLldpFlow",
        "EnableRefreshLldpLearnedInformation": "enableRefreshLldpLearnedInformation",
        "IsOfTopologyLearnedInformationRefreshed": "isOfTopologyLearnedInformationRefreshed",
        "LldpDestinationMac": "lldpDestinationMac",
        "LldpResponseTimeOut": "lldpResponseTimeOut",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(OfTopologyLearnedInformation, self).__init__(parent, list_op)

    @property
    def TopologyLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.topologylearnedinfo_32a09f78d836778332eb6d186e001e53.TopologyLearnedInfo): An instance of the TopologyLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.topologylearnedinfo_32a09f78d836778332eb6d186e001e53 import (
            TopologyLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TopologyLearnedInfo", None) is not None:
                return self._properties.get("TopologyLearnedInfo")
        return TopologyLearnedInfo(self)

    @property
    def EnableInstallLldpFlow(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, Install Flow in Switch for LLDP Packets to explicitly send to Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableInstallLldpFlow"])

    @EnableInstallLldpFlow.setter
    def EnableInstallLldpFlow(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableInstallLldpFlow"], value)

    @property
    def EnableRefreshLldpLearnedInformation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the LLDP trigger configuration parameters are available.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableRefreshLldpLearnedInformation"]
        )

    @EnableRefreshLldpLearnedInformation.setter
    def EnableRefreshLldpLearnedInformation(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableRefreshLldpLearnedInformation"], value
        )

    @property
    def IsOfTopologyLearnedInformationRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it denotes that the Topology Learned Info is received.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsOfTopologyLearnedInformationRefreshed"]
        )

    @property
    def LldpDestinationMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the Destination MAC Address for LLDP PacketOut.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LldpDestinationMac"])

    @LldpDestinationMac.setter
    def LldpDestinationMac(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LldpDestinationMac"], value)

    @property
    def LldpResponseTimeOut(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no Topology learned info response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LldpResponseTimeOut"])

    @LldpResponseTimeOut.setter
    def LldpResponseTimeOut(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LldpResponseTimeOut"], value)

    def update(
        self,
        EnableInstallLldpFlow=None,
        EnableRefreshLldpLearnedInformation=None,
        LldpDestinationMac=None,
        LldpResponseTimeOut=None,
    ):
        # type: (bool, bool, str, int) -> OfTopologyLearnedInformation
        """Updates ofTopologyLearnedInformation resource on the server.

        Args
        ----
        - EnableInstallLldpFlow (bool): If true, Install Flow in Switch for LLDP Packets to explicitly send to Controller.
        - EnableRefreshLldpLearnedInformation (bool): If true, the LLDP trigger configuration parameters are available.
        - LldpDestinationMac (str): Indicates the Destination MAC Address for LLDP PacketOut.
        - LldpResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no Topology learned info response is received.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnableInstallLldpFlow=None,
        EnableRefreshLldpLearnedInformation=None,
        IsOfTopologyLearnedInformationRefreshed=None,
        LldpDestinationMac=None,
        LldpResponseTimeOut=None,
    ):
        # type: (bool, bool, bool, str, int) -> OfTopologyLearnedInformation
        """Finds and retrieves ofTopologyLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ofTopologyLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ofTopologyLearnedInformation resources from the server.

        Args
        ----
        - EnableInstallLldpFlow (bool): If true, Install Flow in Switch for LLDP Packets to explicitly send to Controller.
        - EnableRefreshLldpLearnedInformation (bool): If true, the LLDP trigger configuration parameters are available.
        - IsOfTopologyLearnedInformationRefreshed (bool): If true, it denotes that the Topology Learned Info is received.
        - LldpDestinationMac (str): Indicates the Destination MAC Address for LLDP PacketOut.
        - LldpResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no Topology learned info response is received.

        Returns
        -------
        - self: This instance with matching ofTopologyLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ofTopologyLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ofTopologyLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshOfTopology(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the refreshOfTopology operation on the server.

        Exec to refresh ofChannel topology.

        refreshOfTopology(async_operation=bool)number
        ---------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("refreshOfTopology", payload=payload, response_object=None)
