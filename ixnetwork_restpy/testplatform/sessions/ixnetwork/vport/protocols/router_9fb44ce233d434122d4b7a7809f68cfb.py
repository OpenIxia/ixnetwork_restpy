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


class Router(Base):
    """Represents a simulated RIPng router which holds a list of route ranges and interfaces associated with the simulated router.
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "router"
    _SDM_ATT_MAP = {
        "EnableInterfaceMetric": "enableInterfaceMetric",
        "Enabled": "enabled",
        "ReceiveType": "receiveType",
        "RouterId": "routerId",
        "TrafficGroupId": "trafficGroupId",
        "UpdateInterval": "updateInterval",
        "UpdateIntervalOffset": "updateIntervalOffset",
    }
    _SDM_ENUM_MAP = {
        "receiveType": ["ignore", "store"],
    }

    def __init__(self, parent, list_op=False):
        super(Router, self).__init__(parent, list_op)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ae15d2fc221167d74bd1e54f2452375b.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ae15d2fc221167d74bd1e54f2452375b import (
            Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Interface", None) is not None:
                return self._properties.get("Interface")
        return Interface(self)

    @property
    def RouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_9547e9183edfabd34063407e5c2e1c0b.RouteRange): An instance of the RouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_9547e9183edfabd34063407e5c2e1c0b import (
            RouteRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RouteRange", None) is not None:
                return self._properties.get("RouteRange")
        return RouteRange(self)

    @property
    def EnableInterfaceMetric(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of the RIPng interface metric. This user-assigned metric is added to the normal routing metric.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableInterfaceMetric"])

    @EnableInterfaceMetric.setter
    def EnableInterfaceMetric(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableInterfaceMetric"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the RIPing interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def ReceiveType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ignore | store): Determines how the emulated RIPng router will handle received RIPng update messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceiveType"])

    @ReceiveType.setter
    def ReceiveType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReceiveType"], value)

    @property
    def RouterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The assigned router ID. The default is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterId"])

    @RouterId.setter
    def RouterId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterId"], value)

    @property
    def TrafficGroupId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficGroupId"])

    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficGroupId"], value)

    @property
    def UpdateInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: In seconds) Triggered events, such as sending of unsolicited response messages, are spaced at timed intervals.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpdateInterval"])

    @UpdateInterval.setter
    def UpdateInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpdateInterval"], value)

    @property
    def UpdateIntervalOffset(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (In seconds) To avoid synchronization of the update messages sent by all routers, the update interval is incremented/decremented by a small random time.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpdateIntervalOffset"])

    @UpdateIntervalOffset.setter
    def UpdateIntervalOffset(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpdateIntervalOffset"], value)

    def update(
        self,
        EnableInterfaceMetric=None,
        Enabled=None,
        ReceiveType=None,
        RouterId=None,
        TrafficGroupId=None,
        UpdateInterval=None,
        UpdateIntervalOffset=None,
    ):
        # type: (bool, bool, str, int, str, int, int) -> Router
        """Updates router resource on the server.

        Args
        ----
        - EnableInterfaceMetric (bool): Enables the use of the RIPng interface metric. This user-assigned metric is added to the normal routing metric.
        - Enabled (bool): Enables the RIPing interface.
        - ReceiveType (str(ignore | store)): Determines how the emulated RIPng router will handle received RIPng update messages.
        - RouterId (number): The assigned router ID. The default is 1.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - UpdateInterval (number): In seconds) Triggered events, such as sending of unsolicited response messages, are spaced at timed intervals.
        - UpdateIntervalOffset (number): (In seconds) To avoid synchronization of the update messages sent by all routers, the update interval is incremented/decremented by a small random time.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        EnableInterfaceMetric=None,
        Enabled=None,
        ReceiveType=None,
        RouterId=None,
        TrafficGroupId=None,
        UpdateInterval=None,
        UpdateIntervalOffset=None,
    ):
        # type: (bool, bool, str, int, str, int, int) -> Router
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - EnableInterfaceMetric (bool): Enables the use of the RIPng interface metric. This user-assigned metric is added to the normal routing metric.
        - Enabled (bool): Enables the RIPing interface.
        - ReceiveType (str(ignore | store)): Determines how the emulated RIPng router will handle received RIPng update messages.
        - RouterId (number): The assigned router ID. The default is 1.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - UpdateInterval (number): In seconds) Triggered events, such as sending of unsolicited response messages, are spaced at timed intervals.
        - UpdateIntervalOffset (number): (In seconds) To avoid synchronization of the update messages sent by all routers, the update interval is incremented/decremented by a small random time.

        Returns
        -------
        - self: This instance with all currently retrieved router resources using find and the newly added router resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained router resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        EnableInterfaceMetric=None,
        Enabled=None,
        ReceiveType=None,
        RouterId=None,
        TrafficGroupId=None,
        UpdateInterval=None,
        UpdateIntervalOffset=None,
    ):
        # type: (bool, bool, str, int, str, int, int) -> Router
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - EnableInterfaceMetric (bool): Enables the use of the RIPng interface metric. This user-assigned metric is added to the normal routing metric.
        - Enabled (bool): Enables the RIPing interface.
        - ReceiveType (str(ignore | store)): Determines how the emulated RIPng router will handle received RIPng update messages.
        - RouterId (number): The assigned router ID. The default is 1.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - UpdateInterval (number): In seconds) Triggered events, such as sending of unsolicited response messages, are spaced at timed intervals.
        - UpdateIntervalOffset (number): (In seconds) To avoid synchronization of the update messages sent by all routers, the update interval is incremented/decremented by a small random time.

        Returns
        -------
        - self: This instance with matching router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
