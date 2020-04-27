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
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'router'

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def EidToRlocMapCacheInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eidtorlocmapcacheinfo_2a98c1aa60a9047fb48dbc968f95e9c0.EidToRlocMapCacheInfo): An instance of the EidToRlocMapCacheInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eidtorlocmapcacheinfo_2a98c1aa60a9047fb48dbc968f95e9c0 import EidToRlocMapCacheInfo
        return EidToRlocMapCacheInfo(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ea733dddb68a8cff7a5bc6dece32e698.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ea733dddb68a8cff7a5bc6dece32e698 import Interface
        return Interface(self)

    @property
    def LispInstance(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lispinstance_57bc98a2800f45a2475dd78bb8cd3769.LispInstance): An instance of the LispInstance class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lispinstance_57bc98a2800f45a2475dd78bb8cd3769 import LispInstance
        return LispInstance(self)

    @property
    def MapServerCacheInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mapservercacheinfo_7e4c2b9e625e093dcea328657ed6ecc8.MapServerCacheInfo): An instance of the MapServerCacheInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mapservercacheinfo_7e4c2b9e625e093dcea328657ed6ecc8 import MapServerCacheInfo
        return MapServerCacheInfo(self)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, it enables the router
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def InstanceIdForEidToRlocMapCacheRefresh(self):
        """
        Returns
        -------
        - number: It shows the instance ID for Eid to RLOc the refreshed Map Cache
        """
        return self._get_attribute('instanceIdForEidToRlocMapCacheRefresh')
    @InstanceIdForEidToRlocMapCacheRefresh.setter
    def InstanceIdForEidToRlocMapCacheRefresh(self, value):
        self._set_attribute('instanceIdForEidToRlocMapCacheRefresh', value)

    @property
    def InstanceIdForMapServerCacheRefresh(self):
        """
        Returns
        -------
        - number: It shows the instance ID for refreshed Map Server Cache
        """
        return self._get_attribute('instanceIdForMapServerCacheRefresh')
    @InstanceIdForMapServerCacheRefresh.setter
    def InstanceIdForMapServerCacheRefresh(self, value):
        self._set_attribute('instanceIdForMapServerCacheRefresh', value)

    @property
    def IsEidToRlocMapCacheInfoRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it shows the Eid to Rloc Map Cache information refreshed
        """
        return self._get_attribute('isEidToRlocMapCacheInfoRefreshed')

    @property
    def IsEidToRlocMapCacheRefreshAllInstances(self):
        """
        Returns
        -------
        - bool: If true, it shows the Eid to Rloc Map Cache refreshed in all instances
        """
        return self._get_attribute('isEidToRlocMapCacheRefreshAllInstances')
    @IsEidToRlocMapCacheRefreshAllInstances.setter
    def IsEidToRlocMapCacheRefreshAllInstances(self, value):
        self._set_attribute('isEidToRlocMapCacheRefreshAllInstances', value)

    @property
    def IsMapServerCacheInfoRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it shows the Map Server Cache Information refreshed (Read-only)
        """
        return self._get_attribute('isMapServerCacheInfoRefreshed')

    @property
    def IsMapServerCacheRefreshAllInstances(self):
        """
        Returns
        -------
        - bool: If true, it shows the Map Server Cache All Instances refreshed (Read-only)
        """
        return self._get_attribute('isMapServerCacheRefreshAllInstances')
    @IsMapServerCacheRefreshAllInstances.setter
    def IsMapServerCacheRefreshAllInstances(self, value):
        self._set_attribute('isMapServerCacheRefreshAllInstances', value)

    @property
    def MappingServiceMode(self):
        """
        Returns
        -------
        - str(standAlone | alt | na): It shows the mapping of service mode
        """
        return self._get_attribute('mappingServiceMode')
    @MappingServiceMode.setter
    def MappingServiceMode(self, value):
        self._set_attribute('mappingServiceMode', value)

    @property
    def RouterId(self):
        """
        Returns
        -------
        - str: It shows the Router id
        """
        return self._get_attribute('routerId')
    @RouterId.setter
    def RouterId(self, value):
        self._set_attribute('routerId', value)

    @property
    def TunnelRouterMode(self):
        """
        Returns
        -------
        - str(itr | etr | xtr | msmr): It shows the tunnel Router mode
        """
        return self._get_attribute('tunnelRouterMode')
    @TunnelRouterMode.setter
    def TunnelRouterMode(self, value):
        self._set_attribute('tunnelRouterMode', value)

    def update(self, Enabled=None, InstanceIdForEidToRlocMapCacheRefresh=None, InstanceIdForMapServerCacheRefresh=None, IsEidToRlocMapCacheRefreshAllInstances=None, IsMapServerCacheRefreshAllInstances=None, MappingServiceMode=None, RouterId=None, TunnelRouterMode=None):
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
        return self._update(locals())

    def add(self, Enabled=None, InstanceIdForEidToRlocMapCacheRefresh=None, InstanceIdForMapServerCacheRefresh=None, IsEidToRlocMapCacheRefreshAllInstances=None, IsMapServerCacheRefreshAllInstances=None, MappingServiceMode=None, RouterId=None, TunnelRouterMode=None):
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
        return self._create(locals())

    def remove(self):
        """Deletes all the contained router resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, InstanceIdForEidToRlocMapCacheRefresh=None, InstanceIdForMapServerCacheRefresh=None, IsEidToRlocMapCacheInfoRefreshed=None, IsEidToRlocMapCacheRefreshAllInstances=None, IsMapServerCacheInfoRefreshed=None, IsMapServerCacheRefreshAllInstances=None, MappingServiceMode=None, RouterId=None, TunnelRouterMode=None):
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
        return self._select(locals())

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

    def RefreshLearnedInfo(self):
        """Executes the refreshLearnedInfo operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
