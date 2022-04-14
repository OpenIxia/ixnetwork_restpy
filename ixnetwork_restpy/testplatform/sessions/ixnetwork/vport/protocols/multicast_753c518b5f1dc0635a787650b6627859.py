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


class Multicast(Base):
    """This object configures the multicast attributes for the L3 Site route ranges.
    The Multicast class encapsulates a required multicast resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "multicast"
    _SDM_ATT_MAP = {
        "EnableMulticast": "enableMulticast",
        "EnableMulticastCluster": "enableMulticastCluster",
        "GroupAddress": "groupAddress",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Multicast, self).__init__(parent, list_op)

    @property
    def Cluster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_8dcd05006226c29e0542a45bb95b4f8f.Cluster): An instance of the Cluster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_8dcd05006226c29e0542a45bb95b4f8f import (
            Cluster,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Cluster", None) is not None:
                return self._properties.get("Cluster")
        return Cluster(self)._select()

    @property
    def RouteDistinguisher(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routedistinguisher_2c6f642c4d203efc1987442fcc10ae18.RouteDistinguisher): An instance of the RouteDistinguisher class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routedistinguisher_2c6f642c4d203efc1987442fcc10ae18 import (
            RouteDistinguisher,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RouteDistinguisher", None) is not None:
                return self._properties.get("RouteDistinguisher")
        return RouteDistinguisher(self)._select()

    @property
    def EnableMulticast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of Multicast VRFs (MVRFs). (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMulticast"])

    @EnableMulticast.setter
    def EnableMulticast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMulticast"], value)

    @property
    def EnableMulticastCluster(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the use of BGP route reflection clusters for multicast VPN route distribution. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMulticastCluster"])

    @EnableMulticastCluster.setter
    def EnableMulticastCluster(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMulticastCluster"], value)

    @property
    def GroupAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address for the Multicast Group. The default value is the default MDT group address, used as the Multicast Group address used as the destination for the MVPN tunnel. (default = 239.1.1.1
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupAddress"])

    @GroupAddress.setter
    def GroupAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupAddress"], value)

    def update(
        self, EnableMulticast=None, EnableMulticastCluster=None, GroupAddress=None
    ):
        # type: (bool, bool, str) -> Multicast
        """Updates multicast resource on the server.

        Args
        ----
        - EnableMulticast (bool): Enables the use of Multicast VRFs (MVRFs). (default = false)
        - EnableMulticastCluster (bool): If true, enables the use of BGP route reflection clusters for multicast VPN route distribution. (default = false)
        - GroupAddress (str): The IP address for the Multicast Group. The default value is the default MDT group address, used as the Multicast Group address used as the destination for the MVPN tunnel. (default = 239.1.1.1

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self, EnableMulticast=None, EnableMulticastCluster=None, GroupAddress=None
    ):
        # type: (bool, bool, str) -> Multicast
        """Finds and retrieves multicast resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve multicast resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all multicast resources from the server.

        Args
        ----
        - EnableMulticast (bool): Enables the use of Multicast VRFs (MVRFs). (default = false)
        - EnableMulticastCluster (bool): If true, enables the use of BGP route reflection clusters for multicast VPN route distribution. (default = false)
        - GroupAddress (str): The IP address for the Multicast Group. The default value is the default MDT group address, used as the Multicast Group address used as the destination for the MVPN tunnel. (default = 239.1.1.1

        Returns
        -------
        - self: This instance with matching multicast resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of multicast data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the multicast resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
