# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Router(Base):
    """Shows information about the router
    The Router class encapsulates a list of router resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by the user by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'router'

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def EidToRlocMapCacheInfo(self):
        """An instance of the EidToRlocMapCacheInfo class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eidtorlocmapcacheinfo_2a98c1aa60a9047fb48dbc968f95e9c0.EidToRlocMapCacheInfo)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eidtorlocmapcacheinfo_2a98c1aa60a9047fb48dbc968f95e9c0 import EidToRlocMapCacheInfo
        return EidToRlocMapCacheInfo(self)

    @property
    def Interface(self):
        """An instance of the Interface class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ea733dddb68a8cff7a5bc6dece32e698.Interface)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ea733dddb68a8cff7a5bc6dece32e698 import Interface
        return Interface(self)

    @property
    def LispInstance(self):
        """An instance of the LispInstance class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lispinstance_57bc98a2800f45a2475dd78bb8cd3769.LispInstance)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lispinstance_57bc98a2800f45a2475dd78bb8cd3769 import LispInstance
        return LispInstance(self)

    @property
    def MapServerCacheInfo(self):
        """An instance of the MapServerCacheInfo class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mapservercacheinfo_7e4c2b9e625e093dcea328657ed6ecc8.MapServerCacheInfo)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mapservercacheinfo_7e4c2b9e625e093dcea328657ed6ecc8 import MapServerCacheInfo
        return MapServerCacheInfo(self)

    @property
    def Enabled(self):
        """If true, it enables the router

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def InstanceIdForEidToRlocMapCacheRefresh(self):
        """It shows the instance ID for Eid to RLOc the refreshed Map Cache

        Returns:
            number
        """
        return self._get_attribute('instanceIdForEidToRlocMapCacheRefresh')
    @InstanceIdForEidToRlocMapCacheRefresh.setter
    def InstanceIdForEidToRlocMapCacheRefresh(self, value):
        self._set_attribute('instanceIdForEidToRlocMapCacheRefresh', value)

    @property
    def InstanceIdForMapServerCacheRefresh(self):
        """It shows the instance ID for refreshed Map Server Cache

        Returns:
            number
        """
        return self._get_attribute('instanceIdForMapServerCacheRefresh')
    @InstanceIdForMapServerCacheRefresh.setter
    def InstanceIdForMapServerCacheRefresh(self, value):
        self._set_attribute('instanceIdForMapServerCacheRefresh', value)

    @property
    def IsEidToRlocMapCacheInfoRefreshed(self):
        """If true, it shows the Eid to Rloc Map Cache information refreshed

        Returns:
            bool
        """
        return self._get_attribute('isEidToRlocMapCacheInfoRefreshed')

    @property
    def IsEidToRlocMapCacheRefreshAllInstances(self):
        """If true, it shows the Eid to Rloc Map Cache refreshed in all instances

        Returns:
            bool
        """
        return self._get_attribute('isEidToRlocMapCacheRefreshAllInstances')
    @IsEidToRlocMapCacheRefreshAllInstances.setter
    def IsEidToRlocMapCacheRefreshAllInstances(self, value):
        self._set_attribute('isEidToRlocMapCacheRefreshAllInstances', value)

    @property
    def IsMapServerCacheInfoRefreshed(self):
        """If true, it shows the Map Server Cache Information refreshed (Read-only)

        Returns:
            bool
        """
        return self._get_attribute('isMapServerCacheInfoRefreshed')

    @property
    def IsMapServerCacheRefreshAllInstances(self):
        """If true, it shows the Map Server Cache All Instances refreshed (Read-only)

        Returns:
            bool
        """
        return self._get_attribute('isMapServerCacheRefreshAllInstances')
    @IsMapServerCacheRefreshAllInstances.setter
    def IsMapServerCacheRefreshAllInstances(self, value):
        self._set_attribute('isMapServerCacheRefreshAllInstances', value)

    @property
    def MappingServiceMode(self):
        """It shows the mapping of service mode

        Returns:
            str(standAlone|alt|na)
        """
        return self._get_attribute('mappingServiceMode')
    @MappingServiceMode.setter
    def MappingServiceMode(self, value):
        self._set_attribute('mappingServiceMode', value)

    @property
    def RouterId(self):
        """It shows the Router id

        Returns:
            str
        """
        return self._get_attribute('routerId')
    @RouterId.setter
    def RouterId(self, value):
        self._set_attribute('routerId', value)

    @property
    def TunnelRouterMode(self):
        """It shows the tunnel Router mode

        Returns:
            str(itr|etr|xtr|msmr)
        """
        return self._get_attribute('tunnelRouterMode')
    @TunnelRouterMode.setter
    def TunnelRouterMode(self, value):
        self._set_attribute('tunnelRouterMode', value)

    def update(self, Enabled=None, InstanceIdForEidToRlocMapCacheRefresh=None, InstanceIdForMapServerCacheRefresh=None, IsEidToRlocMapCacheRefreshAllInstances=None, IsMapServerCacheRefreshAllInstances=None, MappingServiceMode=None, RouterId=None, TunnelRouterMode=None):
        """Updates a child instance of router on the server.

        Args:
            Enabled (bool): If true, it enables the router
            InstanceIdForEidToRlocMapCacheRefresh (number): It shows the instance ID for Eid to RLOc the refreshed Map Cache
            InstanceIdForMapServerCacheRefresh (number): It shows the instance ID for refreshed Map Server Cache
            IsEidToRlocMapCacheRefreshAllInstances (bool): If true, it shows the Eid to Rloc Map Cache refreshed in all instances
            IsMapServerCacheRefreshAllInstances (bool): If true, it shows the Map Server Cache All Instances refreshed (Read-only)
            MappingServiceMode (str(standAlone|alt|na)): It shows the mapping of service mode
            RouterId (str): It shows the Router id
            TunnelRouterMode (str(itr|etr|xtr|msmr)): It shows the tunnel Router mode

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Enabled=None, InstanceIdForEidToRlocMapCacheRefresh=None, InstanceIdForMapServerCacheRefresh=None, IsEidToRlocMapCacheRefreshAllInstances=None, IsMapServerCacheRefreshAllInstances=None, MappingServiceMode=None, RouterId=None, TunnelRouterMode=None):
        """Adds a new router node on the server and retrieves it in this instance.

        Args:
            Enabled (bool): If true, it enables the router
            InstanceIdForEidToRlocMapCacheRefresh (number): It shows the instance ID for Eid to RLOc the refreshed Map Cache
            InstanceIdForMapServerCacheRefresh (number): It shows the instance ID for refreshed Map Server Cache
            IsEidToRlocMapCacheRefreshAllInstances (bool): If true, it shows the Eid to Rloc Map Cache refreshed in all instances
            IsMapServerCacheRefreshAllInstances (bool): If true, it shows the Map Server Cache All Instances refreshed (Read-only)
            MappingServiceMode (str(standAlone|alt|na)): It shows the mapping of service mode
            RouterId (str): It shows the Router id
            TunnelRouterMode (str(itr|etr|xtr|msmr)): It shows the tunnel Router mode

        Returns:
            self: This instance with all currently retrieved router data using find and the newly added router data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the router data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, InstanceIdForEidToRlocMapCacheRefresh=None, InstanceIdForMapServerCacheRefresh=None, IsEidToRlocMapCacheInfoRefreshed=None, IsEidToRlocMapCacheRefreshAllInstances=None, IsMapServerCacheInfoRefreshed=None, IsMapServerCacheRefreshAllInstances=None, MappingServiceMode=None, RouterId=None, TunnelRouterMode=None):
        """Finds and retrieves router data from the server.

        All named parameters support regex and can be used to selectively retrieve router data from the server.
        By default the find method takes no parameters and will retrieve all router data from the server.

        Args:
            Enabled (bool): If true, it enables the router
            InstanceIdForEidToRlocMapCacheRefresh (number): It shows the instance ID for Eid to RLOc the refreshed Map Cache
            InstanceIdForMapServerCacheRefresh (number): It shows the instance ID for refreshed Map Server Cache
            IsEidToRlocMapCacheInfoRefreshed (bool): If true, it shows the Eid to Rloc Map Cache information refreshed
            IsEidToRlocMapCacheRefreshAllInstances (bool): If true, it shows the Eid to Rloc Map Cache refreshed in all instances
            IsMapServerCacheInfoRefreshed (bool): If true, it shows the Map Server Cache Information refreshed (Read-only)
            IsMapServerCacheRefreshAllInstances (bool): If true, it shows the Map Server Cache All Instances refreshed (Read-only)
            MappingServiceMode (str(standAlone|alt|na)): It shows the mapping of service mode
            RouterId (str): It shows the Router id
            TunnelRouterMode (str(itr|etr|xtr|msmr)): It shows the tunnel Router mode

        Returns:
            self: This instance with matching router data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the router data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshLearnedInfo(self):
        """Executes the refreshLearnedInfo operation on the server.

        NOT DEFINED

            Returns:
                bool: NOT DEFINED

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
