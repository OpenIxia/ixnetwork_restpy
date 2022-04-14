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
    """Shows information about the router
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "router"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "InstanceIdForEidToRlocMapCacheRefresh": "instanceIdForEidToRlocMapCacheRefresh",
        "InstanceIdForMapServerCacheRefresh": "instanceIdForMapServerCacheRefresh",
        "IsEidToRlocMapCacheInfoRefreshed": "isEidToRlocMapCacheInfoRefreshed",
        "IsEidToRlocMapCacheRefreshAllInstances": "isEidToRlocMapCacheRefreshAllInstances",
        "IsMapServerCacheInfoRefreshed": "isMapServerCacheInfoRefreshed",
        "IsMapServerCacheRefreshAllInstances": "isMapServerCacheRefreshAllInstances",
        "MappingServiceMode": "mappingServiceMode",
        "RouterId": "routerId",
        "TunnelRouterMode": "tunnelRouterMode",
    }
    _SDM_ENUM_MAP = {
        "mappingServiceMode": ["standAlone", "alt", "na"],
        "tunnelRouterMode": ["itr", "etr", "xtr", "msmr"],
    }

    def __init__(self, parent, list_op=False):
        super(Router, self).__init__(parent, list_op)

    @property
    def EidToRlocMapCacheInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eidtorlocmapcacheinfo_d2216efccc3628c42dd062f5723dbcd0.EidToRlocMapCacheInfo): An instance of the EidToRlocMapCacheInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eidtorlocmapcacheinfo_d2216efccc3628c42dd062f5723dbcd0 import (
            EidToRlocMapCacheInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EidToRlocMapCacheInfo", None) is not None:
                return self._properties.get("EidToRlocMapCacheInfo")
        return EidToRlocMapCacheInfo(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_8401addef6ad210808a84a79291dafa1.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_8401addef6ad210808a84a79291dafa1 import (
            Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Interface", None) is not None:
                return self._properties.get("Interface")
        return Interface(self)

    @property
    def LispInstance(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lispinstance_2ff435828a95cdea01ba6bffac98e703.LispInstance): An instance of the LispInstance class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lispinstance_2ff435828a95cdea01ba6bffac98e703 import (
            LispInstance,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LispInstance", None) is not None:
                return self._properties.get("LispInstance")
        return LispInstance(self)

    @property
    def MapServerCacheInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mapservercacheinfo_e631a8f0d76b2164fb127901735b2cf0.MapServerCacheInfo): An instance of the MapServerCacheInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mapservercacheinfo_e631a8f0d76b2164fb127901735b2cf0 import (
            MapServerCacheInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MapServerCacheInfo", None) is not None:
                return self._properties.get("MapServerCacheInfo")
        return MapServerCacheInfo(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it enables the router
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def InstanceIdForEidToRlocMapCacheRefresh(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It shows the instance ID for Eid to RLOc the refreshed Map Cache
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["InstanceIdForEidToRlocMapCacheRefresh"]
        )

    @InstanceIdForEidToRlocMapCacheRefresh.setter
    def InstanceIdForEidToRlocMapCacheRefresh(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["InstanceIdForEidToRlocMapCacheRefresh"], value
        )

    @property
    def InstanceIdForMapServerCacheRefresh(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It shows the instance ID for refreshed Map Server Cache
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["InstanceIdForMapServerCacheRefresh"]
        )

    @InstanceIdForMapServerCacheRefresh.setter
    def InstanceIdForMapServerCacheRefresh(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["InstanceIdForMapServerCacheRefresh"], value
        )

    @property
    def IsEidToRlocMapCacheInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it shows the Eid to Rloc Map Cache information refreshed
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsEidToRlocMapCacheInfoRefreshed"]
        )

    @property
    def IsEidToRlocMapCacheRefreshAllInstances(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it shows the Eid to Rloc Map Cache refreshed in all instances
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsEidToRlocMapCacheRefreshAllInstances"]
        )

    @IsEidToRlocMapCacheRefreshAllInstances.setter
    def IsEidToRlocMapCacheRefreshAllInstances(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["IsEidToRlocMapCacheRefreshAllInstances"], value
        )

    @property
    def IsMapServerCacheInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it shows the Map Server Cache Information refreshed (Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsMapServerCacheInfoRefreshed"])

    @property
    def IsMapServerCacheRefreshAllInstances(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, it shows the Map Server Cache All Instances refreshed (Read-only)
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["IsMapServerCacheRefreshAllInstances"]
        )

    @IsMapServerCacheRefreshAllInstances.setter
    def IsMapServerCacheRefreshAllInstances(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["IsMapServerCacheRefreshAllInstances"], value
        )

    @property
    def MappingServiceMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(standAlone | alt | na): It shows the mapping of service mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["MappingServiceMode"])

    @MappingServiceMode.setter
    def MappingServiceMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MappingServiceMode"], value)

    @property
    def RouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It shows the Router id
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterId"])

    @RouterId.setter
    def RouterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterId"], value)

    @property
    def TunnelRouterMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(itr | etr | xtr | msmr): It shows the tunnel Router mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["TunnelRouterMode"])

    @TunnelRouterMode.setter
    def TunnelRouterMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TunnelRouterMode"], value)

    def update(
        self,
        Enabled=None,
        InstanceIdForEidToRlocMapCacheRefresh=None,
        InstanceIdForMapServerCacheRefresh=None,
        IsEidToRlocMapCacheRefreshAllInstances=None,
        IsMapServerCacheRefreshAllInstances=None,
        MappingServiceMode=None,
        RouterId=None,
        TunnelRouterMode=None,
    ):
        # type: (bool, int, int, bool, bool, str, str, str) -> Router
        """Updates router resource on the server.

        Args
        ----
        - Enabled (bool): If true, it enables the router
        - InstanceIdForEidToRlocMapCacheRefresh (number): It shows the instance ID for Eid to RLOc the refreshed Map Cache
        - InstanceIdForMapServerCacheRefresh (number): It shows the instance ID for refreshed Map Server Cache
        - IsEidToRlocMapCacheRefreshAllInstances (bool): If true, it shows the Eid to Rloc Map Cache refreshed in all instances
        - IsMapServerCacheRefreshAllInstances (bool): If true, it shows the Map Server Cache All Instances refreshed (Read-only)
        - MappingServiceMode (str(standAlone | alt | na)): It shows the mapping of service mode
        - RouterId (str): It shows the Router id
        - TunnelRouterMode (str(itr | etr | xtr | msmr)): It shows the tunnel Router mode

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Enabled=None,
        InstanceIdForEidToRlocMapCacheRefresh=None,
        InstanceIdForMapServerCacheRefresh=None,
        IsEidToRlocMapCacheRefreshAllInstances=None,
        IsMapServerCacheRefreshAllInstances=None,
        MappingServiceMode=None,
        RouterId=None,
        TunnelRouterMode=None,
    ):
        # type: (bool, int, int, bool, bool, str, str, str) -> Router
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true, it enables the router
        - InstanceIdForEidToRlocMapCacheRefresh (number): It shows the instance ID for Eid to RLOc the refreshed Map Cache
        - InstanceIdForMapServerCacheRefresh (number): It shows the instance ID for refreshed Map Server Cache
        - IsEidToRlocMapCacheRefreshAllInstances (bool): If true, it shows the Eid to Rloc Map Cache refreshed in all instances
        - IsMapServerCacheRefreshAllInstances (bool): If true, it shows the Map Server Cache All Instances refreshed (Read-only)
        - MappingServiceMode (str(standAlone | alt | na)): It shows the mapping of service mode
        - RouterId (str): It shows the Router id
        - TunnelRouterMode (str(itr | etr | xtr | msmr)): It shows the tunnel Router mode

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
        Enabled=None,
        InstanceIdForEidToRlocMapCacheRefresh=None,
        InstanceIdForMapServerCacheRefresh=None,
        IsEidToRlocMapCacheInfoRefreshed=None,
        IsEidToRlocMapCacheRefreshAllInstances=None,
        IsMapServerCacheInfoRefreshed=None,
        IsMapServerCacheRefreshAllInstances=None,
        MappingServiceMode=None,
        RouterId=None,
        TunnelRouterMode=None,
    ):
        # type: (bool, int, int, bool, bool, bool, bool, str, str, str) -> Router
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - Enabled (bool): If true, it enables the router
        - InstanceIdForEidToRlocMapCacheRefresh (number): It shows the instance ID for Eid to RLOc the refreshed Map Cache
        - InstanceIdForMapServerCacheRefresh (number): It shows the instance ID for refreshed Map Server Cache
        - IsEidToRlocMapCacheInfoRefreshed (bool): If true, it shows the Eid to Rloc Map Cache information refreshed
        - IsEidToRlocMapCacheRefreshAllInstances (bool): If true, it shows the Eid to Rloc Map Cache refreshed in all instances
        - IsMapServerCacheInfoRefreshed (bool): If true, it shows the Map Server Cache Information refreshed (Read-only)
        - IsMapServerCacheRefreshAllInstances (bool): If true, it shows the Map Server Cache All Instances refreshed (Read-only)
        - MappingServiceMode (str(standAlone | alt | na)): It shows the mapping of service mode
        - RouterId (str): It shows the Router id
        - TunnelRouterMode (str(itr | etr | xtr | msmr)): It shows the tunnel Router mode

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

    def RefreshLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshLearnedInfo operation on the server.

        NOT DEFINED

        refreshLearnedInfo(async_operation=bool)bool
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
        return self._execute(
            "refreshLearnedInfo", payload=payload, response_object=None
        )
