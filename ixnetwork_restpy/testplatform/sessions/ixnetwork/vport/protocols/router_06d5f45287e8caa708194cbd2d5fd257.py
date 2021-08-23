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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files
from typing import List, Any, Union


class Router(Base):
    """The EIGRP router object represents a simulated router. In addition to some identifying options, it holds three lists for the router: (1) Interface-a router interface. (2) Route ranges-routes to be advertised by the simulated router. (3) Learned routes-routes learned by the simulated router.
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'router'
    _SDM_ATT_MAP = {
        'ActiveTime': 'activeTime',
        'AsNumber': 'asNumber',
        'DiscardLearnedRoutes': 'discardLearnedRoutes',
        'EigrpAddressFamily': 'eigrpAddressFamily',
        'EigrpMajorVersion': 'eigrpMajorVersion',
        'EigrpMinorVersion': 'eigrpMinorVersion',
        'EnablePiggyBack': 'enablePiggyBack',
        'Enabled': 'enabled',
        'IosMajorVersion': 'iosMajorVersion',
        'IosMinorVersion': 'iosMinorVersion',
        'IsRefreshComplete': 'isRefreshComplete',
        'K1': 'k1',
        'K2': 'k2',
        'K3': 'k3',
        'K4': 'k4',
        'K5': 'k5',
        'RouterId': 'routerId',
        'TrafficGroupId': 'trafficGroupId',
    }
    _SDM_ENUM_MAP = {
        'eigrpAddressFamily': ['ipv4', 'ipv6'],
    }

    def __init__(self, parent, list_op=False):
        super(Router, self).__init__(parent, list_op)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_c3c911144789a78964958c3c7bd601dc.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_c3c911144789a78964958c3c7bd601dc import Interface
        if self._properties.get('Interface', None) is not None:
            return self._properties.get('Interface')
        else:
            return Interface(self)

    @property
    def LearnedRoute(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_d56ac825d7af435a1cbaf25c843e97e3.LearnedRoute): An instance of the LearnedRoute class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_d56ac825d7af435a1cbaf25c843e97e3 import LearnedRoute
        if self._properties.get('LearnedRoute', None) is not None:
            return self._properties.get('LearnedRoute')
        else:
            return LearnedRoute(self)

    @property
    def RouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_de59685b76fa73e61393f9afda789105.RouteRange): An instance of the RouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_de59685b76fa73e61393f9afda789105 import RouteRange
        if self._properties.get('RouteRange', None) is not None:
            return self._properties.get('RouteRange')
        else:
            return RouteRange(self)

    @property
    def ActiveTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It determines the maximum time (in minutes) for which a route learned from a neighbor will be active in the topology table, if the neighbor stops sending Hellos. The valid range is 1 to 4294967295. (default = 3 minutes)
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActiveTime'])
    @ActiveTime.setter
    def ActiveTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['ActiveTime'], value)

    @property
    def AsNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The identifier of the Autonomous System (AS) where this emulated EIGRP router is located. The valid range is 1 to 4294967295. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['AsNumber'])
    @AsNumber.setter
    def AsNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['AsNumber'], value)

    @property
    def DiscardLearnedRoutes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, routes learned by emulated EIGRP Routers on this port will be discarded (not stored).
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscardLearnedRoutes'])
    @DiscardLearnedRoutes.setter
    def DiscardLearnedRoutes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['DiscardLearnedRoutes'], value)

    @property
    def EigrpAddressFamily(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ipv4 | ipv6): It denotes IP address type, one of IPv4 or IPv6 (Default is IPv4)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EigrpAddressFamily'])
    @EigrpAddressFamily.setter
    def EigrpAddressFamily(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['EigrpAddressFamily'], value)

    @property
    def EigrpMajorVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The major version level of the EIGRP software. The valid range is 0 to 255. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EigrpMajorVersion'])
    @EigrpMajorVersion.setter
    def EigrpMajorVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['EigrpMajorVersion'], value)

    @property
    def EigrpMinorVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minor version level of the EIGRP software. The valid range is 0 to 255. (default = 2).
        """
        return self._get_attribute(self._SDM_ATT_MAP['EigrpMinorVersion'])
    @EigrpMinorVersion.setter
    def EigrpMinorVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['EigrpMinorVersion'], value)

    @property
    def EnablePiggyBack(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, then EIGRP will piggyback an acknowledgement for the initial update with any unicast packet sent to the neighbor, instead of directly sending a separate acknowledgement packet to the neighbor.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePiggyBack'])
    @EnablePiggyBack.setter
    def EnablePiggyBack(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnablePiggyBack'], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the simulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IosMajorVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The major version level of the referenced software. The valid range is 0 to 255. (default = 12)
        """
        return self._get_attribute(self._SDM_ATT_MAP['IosMajorVersion'])
    @IosMajorVersion.setter
    def IosMajorVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['IosMajorVersion'], value)

    @property
    def IosMinorVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The major version level of the referenced software. The valid range is 0 to 255. (default = 3)
        """
        return self._get_attribute(self._SDM_ATT_MAP['IosMinorVersion'])
    @IosMinorVersion.setter
    def IosMinorVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['IosMinorVersion'], value)

    @property
    def IsRefreshComplete(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If true, the routes have been refreshed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRefreshComplete'])

    @property
    def K1(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Advanced parameter, only used in condition checking for establishing neighbor relationship. The valid range is 0 to 255. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['K1'])
    @K1.setter
    def K1(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['K1'], value)

    @property
    def K2(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Advanced parameter, only used in condition checking for establishing neighbor relationship. The valid range is 0 to 255. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['K2'])
    @K2.setter
    def K2(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['K2'], value)

    @property
    def K3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Advanced parameter, only used in condition checking for establishing neighbor relationship. The valid range is 0 to 255. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['K3'])
    @K3.setter
    def K3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['K3'], value)

    @property
    def K4(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Advanced parameter, only used in condition checking for establishing neighbor relationship.The valid range is 0 to 255. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['K4'])
    @K4.setter
    def K4(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['K4'], value)

    @property
    def K5(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Advanced parameter, only used in condition checking for establishing neighbor relationship.The valid range is 0 to 255. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['K5'])
    @K5.setter
    def K5(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['K5'], value)

    @property
    def RouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This is an IP-formatted string. Its default value is dependent on card/port type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterId'])
    @RouterId.setter
    def RouterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['RouterId'], value)

    @property
    def TrafficGroupId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    def update(self, ActiveTime=None, AsNumber=None, DiscardLearnedRoutes=None, EigrpAddressFamily=None, EigrpMajorVersion=None, EigrpMinorVersion=None, EnablePiggyBack=None, Enabled=None, IosMajorVersion=None, IosMinorVersion=None, K1=None, K2=None, K3=None, K4=None, K5=None, RouterId=None, TrafficGroupId=None):
        # type: (int, int, bool, str, int, int, bool, bool, int, int, int, int, int, int, int, str, str) -> Router
        """Updates router resource on the server.

        Args
        ----
        - ActiveTime (number): It determines the maximum time (in minutes) for which a route learned from a neighbor will be active in the topology table, if the neighbor stops sending Hellos. The valid range is 1 to 4294967295. (default = 3 minutes)
        - AsNumber (number): The identifier of the Autonomous System (AS) where this emulated EIGRP router is located. The valid range is 1 to 4294967295. (default = 1)
        - DiscardLearnedRoutes (bool): If enabled, routes learned by emulated EIGRP Routers on this port will be discarded (not stored).
        - EigrpAddressFamily (str(ipv4 | ipv6)): It denotes IP address type, one of IPv4 or IPv6 (Default is IPv4)
        - EigrpMajorVersion (number): The major version level of the EIGRP software. The valid range is 0 to 255. (default = 1)
        - EigrpMinorVersion (number): The minor version level of the EIGRP software. The valid range is 0 to 255. (default = 2).
        - EnablePiggyBack (bool): If enabled, then EIGRP will piggyback an acknowledgement for the initial update with any unicast packet sent to the neighbor, instead of directly sending a separate acknowledgement packet to the neighbor.
        - Enabled (bool): Enables the simulated router.
        - IosMajorVersion (number): The major version level of the referenced software. The valid range is 0 to 255. (default = 12)
        - IosMinorVersion (number): The major version level of the referenced software. The valid range is 0 to 255. (default = 3)
        - K1 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship. The valid range is 0 to 255. (default = 1)
        - K2 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship. The valid range is 0 to 255. (default = 0)
        - K3 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship. The valid range is 0 to 255. (default = 1)
        - K4 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship.The valid range is 0 to 255. (default = 0)
        - K5 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship.The valid range is 0 to 255. (default = 0)
        - RouterId (str): This is an IP-formatted string. Its default value is dependent on card/port type.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ActiveTime=None, AsNumber=None, DiscardLearnedRoutes=None, EigrpAddressFamily=None, EigrpMajorVersion=None, EigrpMinorVersion=None, EnablePiggyBack=None, Enabled=None, IosMajorVersion=None, IosMinorVersion=None, K1=None, K2=None, K3=None, K4=None, K5=None, RouterId=None, TrafficGroupId=None):
        # type: (int, int, bool, str, int, int, bool, bool, int, int, int, int, int, int, int, str, str) -> Router
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - ActiveTime (number): It determines the maximum time (in minutes) for which a route learned from a neighbor will be active in the topology table, if the neighbor stops sending Hellos. The valid range is 1 to 4294967295. (default = 3 minutes)
        - AsNumber (number): The identifier of the Autonomous System (AS) where this emulated EIGRP router is located. The valid range is 1 to 4294967295. (default = 1)
        - DiscardLearnedRoutes (bool): If enabled, routes learned by emulated EIGRP Routers on this port will be discarded (not stored).
        - EigrpAddressFamily (str(ipv4 | ipv6)): It denotes IP address type, one of IPv4 or IPv6 (Default is IPv4)
        - EigrpMajorVersion (number): The major version level of the EIGRP software. The valid range is 0 to 255. (default = 1)
        - EigrpMinorVersion (number): The minor version level of the EIGRP software. The valid range is 0 to 255. (default = 2).
        - EnablePiggyBack (bool): If enabled, then EIGRP will piggyback an acknowledgement for the initial update with any unicast packet sent to the neighbor, instead of directly sending a separate acknowledgement packet to the neighbor.
        - Enabled (bool): Enables the simulated router.
        - IosMajorVersion (number): The major version level of the referenced software. The valid range is 0 to 255. (default = 12)
        - IosMinorVersion (number): The major version level of the referenced software. The valid range is 0 to 255. (default = 3)
        - K1 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship. The valid range is 0 to 255. (default = 1)
        - K2 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship. The valid range is 0 to 255. (default = 0)
        - K3 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship. The valid range is 0 to 255. (default = 1)
        - K4 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship.The valid range is 0 to 255. (default = 0)
        - K5 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship.The valid range is 0 to 255. (default = 0)
        - RouterId (str): This is an IP-formatted string. Its default value is dependent on card/port type.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

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

    def find(self, ActiveTime=None, AsNumber=None, DiscardLearnedRoutes=None, EigrpAddressFamily=None, EigrpMajorVersion=None, EigrpMinorVersion=None, EnablePiggyBack=None, Enabled=None, IosMajorVersion=None, IosMinorVersion=None, IsRefreshComplete=None, K1=None, K2=None, K3=None, K4=None, K5=None, RouterId=None, TrafficGroupId=None):
        # type: (int, int, bool, str, int, int, bool, bool, int, int, int, int, int, int, int, int, str, str) -> Router
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - ActiveTime (number): It determines the maximum time (in minutes) for which a route learned from a neighbor will be active in the topology table, if the neighbor stops sending Hellos. The valid range is 1 to 4294967295. (default = 3 minutes)
        - AsNumber (number): The identifier of the Autonomous System (AS) where this emulated EIGRP router is located. The valid range is 1 to 4294967295. (default = 1)
        - DiscardLearnedRoutes (bool): If enabled, routes learned by emulated EIGRP Routers on this port will be discarded (not stored).
        - EigrpAddressFamily (str(ipv4 | ipv6)): It denotes IP address type, one of IPv4 or IPv6 (Default is IPv4)
        - EigrpMajorVersion (number): The major version level of the EIGRP software. The valid range is 0 to 255. (default = 1)
        - EigrpMinorVersion (number): The minor version level of the EIGRP software. The valid range is 0 to 255. (default = 2).
        - EnablePiggyBack (bool): If enabled, then EIGRP will piggyback an acknowledgement for the initial update with any unicast packet sent to the neighbor, instead of directly sending a separate acknowledgement packet to the neighbor.
        - Enabled (bool): Enables the simulated router.
        - IosMajorVersion (number): The major version level of the referenced software. The valid range is 0 to 255. (default = 12)
        - IosMinorVersion (number): The major version level of the referenced software. The valid range is 0 to 255. (default = 3)
        - IsRefreshComplete (number): If true, the routes have been refreshed.
        - K1 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship. The valid range is 0 to 255. (default = 1)
        - K2 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship. The valid range is 0 to 255. (default = 0)
        - K3 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship. The valid range is 0 to 255. (default = 1)
        - K4 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship.The valid range is 0 to 255. (default = 0)
        - K5 (number): Advanced parameter, only used in condition checking for establishing neighbor relationship.The valid range is 0 to 255. (default = 0)
        - RouterId (str): This is an IP-formatted string. Its default value is dependent on card/port type.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

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

        This exec refreshes the EIGRP learned information from the DUT.

        refreshLearnedInfo(async_operation=bool)bool
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
