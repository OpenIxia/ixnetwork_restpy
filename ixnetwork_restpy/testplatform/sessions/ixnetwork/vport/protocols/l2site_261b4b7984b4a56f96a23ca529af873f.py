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


class L2Site(Base):
    """Represents a VPN layer 2 site.
    The L2Site class encapsulates a list of l2Site resources that are managed by the user.
    A list of resources can be retrieved from the server using the L2Site.find() method.
    The list can be managed by using the L2Site.add() and L2Site.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "l2Site"
    _SDM_ATT_MAP = {
        "DistinguishAssignedIncrement": "distinguishAssignedIncrement",
        "DistinguishIpIncrement": "distinguishIpIncrement",
        "DistinguishNumberIncrementAs": "distinguishNumberIncrementAs",
        "EnableBfdVccv": "enableBfdVccv",
        "EnableCluster": "enableCluster",
        "EnableControlWord": "enableControlWord",
        "EnableL2SiteAsTrafficEndpoint": "enableL2SiteAsTrafficEndpoint",
        "EnableSequenceDelivery": "enableSequenceDelivery",
        "EnableVccvPing": "enableVccvPing",
        "Enabled": "enabled",
        "IsLearnedInfoRefreshed": "isLearnedInfoRefreshed",
        "Mtu": "mtu",
        "NoOfL2Site": "noOfL2Site",
        "RouteDistinguisherAs": "routeDistinguisherAs",
        "RouteDistinguisherAssignedNum": "routeDistinguisherAssignedNum",
        "RouteDistinguisherIp": "routeDistinguisherIp",
        "RouteDistinguisherType": "routeDistinguisherType",
        "RouteTargetAs": "routeTargetAs",
        "RouteTargetAssignedNum": "routeTargetAssignedNum",
        "RouteTargetIp": "routeTargetIp",
        "RouteTargetType": "routeTargetType",
        "SiteId": "siteId",
        "SiteIdIncrement": "siteIdIncrement",
        "TargetAssignedNumberIncrement": "targetAssignedNumberIncrement",
        "TargetIncrementAs": "targetIncrementAs",
        "TargetIpIncrement": "targetIpIncrement",
        "TrafficGroupId": "trafficGroupId",
    }
    _SDM_ENUM_MAP = {
        "routeDistinguisherType": ["twoOctetAs", "ip", "fourOctetAs"],
        "routeTargetType": ["as", "ip"],
    }

    def __init__(self, parent, list_op=False):
        super(L2Site, self).__init__(parent, list_op)

    @property
    def Cluster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_044b5666a07dd04f7fe6493072b12207.Cluster): An instance of the Cluster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_044b5666a07dd04f7fe6493072b12207 import (
            Cluster,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Cluster", None) is not None:
                return self._properties.get("Cluster")
        return Cluster(self)._select()

    @property
    def LabelBlock(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelblock_9dc039523bf8ddf644ba0b304bd91db9.LabelBlock): An instance of the LabelBlock class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelblock_9dc039523bf8ddf644ba0b304bd91db9 import (
            LabelBlock,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LabelBlock", None) is not None:
                return self._properties.get("LabelBlock")
        return LabelBlock(self)

    @property
    def LearnedRoute(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_fcc7cef4c15bb872fcc8499e708cc164.LearnedRoute): An instance of the LearnedRoute class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_fcc7cef4c15bb872fcc8499e708cc164 import (
            LearnedRoute,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedRoute", None) is not None:
                return self._properties.get("LearnedRoute")
        return LearnedRoute(self)

    @property
    def MacAddressRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macaddressrange_cb64b65b0ce814edd651d27ccd0840b2.MacAddressRange): An instance of the MacAddressRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macaddressrange_cb64b65b0ce814edd651d27ccd0840b2 import (
            MacAddressRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MacAddressRange", None) is not None:
                return self._properties.get("MacAddressRange")
        return MacAddressRange(self)

    @property
    def DistinguishAssignedIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Distinguishes increment of the assigned value
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguishAssignedIncrement"])

    @DistinguishAssignedIncrement.setter
    def DistinguishAssignedIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguishAssignedIncrement"], value)

    @property
    def DistinguishIpIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Distinguishes the increment of the IP address
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguishIpIncrement"])

    @DistinguishIpIncrement.setter
    def DistinguishIpIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguishIpIncrement"], value)

    @property
    def DistinguishNumberIncrementAs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the distinguished increment as number
        """
        return self._get_attribute(self._SDM_ATT_MAP["DistinguishNumberIncrementAs"])

    @DistinguishNumberIncrementAs.setter
    def DistinguishNumberIncrementAs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DistinguishNumberIncrementAs"], value)

    @property
    def EnableBfdVccv(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables BFD VCCV
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableBfdVccv"])

    @EnableBfdVccv.setter
    def EnableBfdVccv(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableBfdVccv"], value)

    @property
    def EnableCluster(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables and controls the use of L2 VPN VPLS.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableCluster"])

    @EnableCluster.setter
    def EnableCluster(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableCluster"], value)

    @property
    def EnableControlWord(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of a control word, as part of the extended community information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableControlWord"])

    @EnableControlWord.setter
    def EnableControlWord(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableControlWord"], value)

    @property
    def EnableL2SiteAsTrafficEndpoint(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables L2 site as traffic endpoint
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableL2SiteAsTrafficEndpoint"])

    @EnableL2SiteAsTrafficEndpoint.setter
    def EnableL2SiteAsTrafficEndpoint(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableL2SiteAsTrafficEndpoint"], value)

    @property
    def EnableSequenceDelivery(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of sequenced delivery of frames, as part of the extended community information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSequenceDelivery"])

    @EnableSequenceDelivery.setter
    def EnableSequenceDelivery(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSequenceDelivery"], value)

    @property
    def EnableVccvPing(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the VCCV ping
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableVccvPing"])

    @EnableVccvPing.setter
    def EnableVccvPing(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableVccvPing"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables use of the L2 VPN site.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def IsLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, learned information is refreshed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLearnedInfoRefreshed"])

    @property
    def Mtu(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Maximum Transmission Unit (MTU) allowed on this link, in bytes. The valid range is 0 to 16777215. (default = 1,500 bytes)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mtu"])

    @Mtu.setter
    def Mtu(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mtu"], value)

    @property
    def NoOfL2Site(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the number of L2 sites
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfL2Site"])

    @NoOfL2Site.setter
    def NoOfL2Site(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfL2Site"], value)

    @property
    def RouteDistinguisherAs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Available for use only if the route distinguish type is set to AS. The route distinguisher autonomous system (AS) number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteDistinguisherAs"])

    @RouteDistinguisherAs.setter
    def RouteDistinguisherAs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteDistinguisherAs"], value)

    @property
    def RouteDistinguisherAssignedNum(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The assigned number for use with the distinguisher IP address or AS number, to create the route distinguisher.The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteDistinguisherAssignedNum"])

    @RouteDistinguisherAssignedNum.setter
    def RouteDistinguisherAssignedNum(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteDistinguisherAssignedNum"], value)

    @property
    def RouteDistinguisherIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Available for use only if the route Distinguish Type is set to IP. The route distinguisher IP address. A 4-byte IPv4 address.The default is 0.0.0.0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteDistinguisherIp"])

    @RouteDistinguisherIp.setter
    def RouteDistinguisherIp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteDistinguisherIp"], value)

    @property
    def RouteDistinguisherType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(twoOctetAs | ip | fourOctetAs): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteDistinguisherType"])

    @RouteDistinguisherType.setter
    def RouteDistinguisherType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteDistinguisherType"], value)

    @property
    def RouteTargetAs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Autonomous system (AS) number. A 2-byte AS number, used to create the route target extended community attribute associated with this L2 site.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteTargetAs"])

    @RouteTargetAs.setter
    def RouteTargetAs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteTargetAs"], value)

    @property
    def RouteTargetAssignedNum(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Autonomous system (AS) and assigned number. A 2-byte AS number and a 4-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteTargetAssignedNum"])

    @RouteTargetAssignedNum.setter
    def RouteTargetAssignedNum(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteTargetAssignedNum"], value)

    @property
    def RouteTargetIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: IP address and assigned number. A 4-byte IPv4 address and a 2-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteTargetIp"])

    @RouteTargetIp.setter
    def RouteTargetIp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteTargetIp"], value)

    @property
    def RouteTargetType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(as | ip): The Admin part type is to the type of route target attribute
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouteTargetType"])

    @RouteTargetType.setter
    def RouteTargetType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouteTargetType"], value)

    @property
    def SiteId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The identifier for the L2 (CE) site. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SiteId"])

    @SiteId.setter
    def SiteId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SiteId"], value)

    @property
    def SiteIdIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Increments the site identifier
        """
        return self._get_attribute(self._SDM_ATT_MAP["SiteIdIncrement"])

    @SiteIdIncrement.setter
    def SiteIdIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SiteIdIncrement"], value)

    @property
    def TargetAssignedNumberIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies increment of the target assigned number
        """
        return self._get_attribute(self._SDM_ATT_MAP["TargetAssignedNumberIncrement"])

    @TargetAssignedNumberIncrement.setter
    def TargetAssignedNumberIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TargetAssignedNumberIncrement"], value)

    @property
    def TargetIncrementAs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies increment as target
        """
        return self._get_attribute(self._SDM_ATT_MAP["TargetIncrementAs"])

    @TargetIncrementAs.setter
    def TargetIncrementAs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TargetIncrementAs"], value)

    @property
    def TargetIpIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the increment of IP as target
        """
        return self._get_attribute(self._SDM_ATT_MAP["TargetIpIncrement"])

    @TargetIpIncrement.setter
    def TargetIpIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TargetIpIncrement"], value)

    @property
    def TrafficGroupId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficGroupId"])

    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficGroupId"], value)

    def update(
        self,
        DistinguishAssignedIncrement=None,
        DistinguishIpIncrement=None,
        DistinguishNumberIncrementAs=None,
        EnableBfdVccv=None,
        EnableCluster=None,
        EnableControlWord=None,
        EnableL2SiteAsTrafficEndpoint=None,
        EnableSequenceDelivery=None,
        EnableVccvPing=None,
        Enabled=None,
        Mtu=None,
        NoOfL2Site=None,
        RouteDistinguisherAs=None,
        RouteDistinguisherAssignedNum=None,
        RouteDistinguisherIp=None,
        RouteDistinguisherType=None,
        RouteTargetAs=None,
        RouteTargetAssignedNum=None,
        RouteTargetIp=None,
        RouteTargetType=None,
        SiteId=None,
        SiteIdIncrement=None,
        TargetAssignedNumberIncrement=None,
        TargetIncrementAs=None,
        TargetIpIncrement=None,
        TrafficGroupId=None,
    ):
        # type: (int, str, int, bool, bool, bool, bool, bool, bool, bool, int, int, int, int, str, str, int, int, str, str, int, int, int, int, str, str) -> L2Site
        """Updates l2Site resource on the server.

        Args
        ----
        - DistinguishAssignedIncrement (number): Distinguishes increment of the assigned value
        - DistinguishIpIncrement (str): Distinguishes the increment of the IP address
        - DistinguishNumberIncrementAs (number): Signifies the distinguished increment as number
        - EnableBfdVccv (bool): If true, enables BFD VCCV
        - EnableCluster (bool): Enables and controls the use of L2 VPN VPLS.
        - EnableControlWord (bool): Enables the use of a control word, as part of the extended community information.
        - EnableL2SiteAsTrafficEndpoint (bool): If true, enables L2 site as traffic endpoint
        - EnableSequenceDelivery (bool): Enables the use of sequenced delivery of frames, as part of the extended community information.
        - EnableVccvPing (bool): If true, enables the VCCV ping
        - Enabled (bool): Enables or disables use of the L2 VPN site.
        - Mtu (number): The Maximum Transmission Unit (MTU) allowed on this link, in bytes. The valid range is 0 to 16777215. (default = 1,500 bytes)
        - NoOfL2Site (number): Signifies the number of L2 sites
        - RouteDistinguisherAs (number): Available for use only if the route distinguish type is set to AS. The route distinguisher autonomous system (AS) number.
        - RouteDistinguisherAssignedNum (number): The assigned number for use with the distinguisher IP address or AS number, to create the route distinguisher.The default is 0.
        - RouteDistinguisherIp (str): Available for use only if the route Distinguish Type is set to IP. The route distinguisher IP address. A 4-byte IPv4 address.The default is 0.0.0.0.
        - RouteDistinguisherType (str(twoOctetAs | ip | fourOctetAs)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        - RouteTargetAs (number): Autonomous system (AS) number. A 2-byte AS number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetAssignedNum (number): Autonomous system (AS) and assigned number. A 2-byte AS number and a 4-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetIp (str): IP address and assigned number. A 4-byte IPv4 address and a 2-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetType (str(as | ip)): The Admin part type is to the type of route target attribute
        - SiteId (number): The identifier for the L2 (CE) site. The default is 0.
        - SiteIdIncrement (number): Increments the site identifier
        - TargetAssignedNumberIncrement (number): Signifies increment of the target assigned number
        - TargetIncrementAs (number): Signifies increment as target
        - TargetIpIncrement (str): Signifies the increment of IP as target
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        DistinguishAssignedIncrement=None,
        DistinguishIpIncrement=None,
        DistinguishNumberIncrementAs=None,
        EnableBfdVccv=None,
        EnableCluster=None,
        EnableControlWord=None,
        EnableL2SiteAsTrafficEndpoint=None,
        EnableSequenceDelivery=None,
        EnableVccvPing=None,
        Enabled=None,
        Mtu=None,
        NoOfL2Site=None,
        RouteDistinguisherAs=None,
        RouteDistinguisherAssignedNum=None,
        RouteDistinguisherIp=None,
        RouteDistinguisherType=None,
        RouteTargetAs=None,
        RouteTargetAssignedNum=None,
        RouteTargetIp=None,
        RouteTargetType=None,
        SiteId=None,
        SiteIdIncrement=None,
        TargetAssignedNumberIncrement=None,
        TargetIncrementAs=None,
        TargetIpIncrement=None,
        TrafficGroupId=None,
    ):
        # type: (int, str, int, bool, bool, bool, bool, bool, bool, bool, int, int, int, int, str, str, int, int, str, str, int, int, int, int, str, str) -> L2Site
        """Adds a new l2Site resource on the server and adds it to the container.

        Args
        ----
        - DistinguishAssignedIncrement (number): Distinguishes increment of the assigned value
        - DistinguishIpIncrement (str): Distinguishes the increment of the IP address
        - DistinguishNumberIncrementAs (number): Signifies the distinguished increment as number
        - EnableBfdVccv (bool): If true, enables BFD VCCV
        - EnableCluster (bool): Enables and controls the use of L2 VPN VPLS.
        - EnableControlWord (bool): Enables the use of a control word, as part of the extended community information.
        - EnableL2SiteAsTrafficEndpoint (bool): If true, enables L2 site as traffic endpoint
        - EnableSequenceDelivery (bool): Enables the use of sequenced delivery of frames, as part of the extended community information.
        - EnableVccvPing (bool): If true, enables the VCCV ping
        - Enabled (bool): Enables or disables use of the L2 VPN site.
        - Mtu (number): The Maximum Transmission Unit (MTU) allowed on this link, in bytes. The valid range is 0 to 16777215. (default = 1,500 bytes)
        - NoOfL2Site (number): Signifies the number of L2 sites
        - RouteDistinguisherAs (number): Available for use only if the route distinguish type is set to AS. The route distinguisher autonomous system (AS) number.
        - RouteDistinguisherAssignedNum (number): The assigned number for use with the distinguisher IP address or AS number, to create the route distinguisher.The default is 0.
        - RouteDistinguisherIp (str): Available for use only if the route Distinguish Type is set to IP. The route distinguisher IP address. A 4-byte IPv4 address.The default is 0.0.0.0.
        - RouteDistinguisherType (str(twoOctetAs | ip | fourOctetAs)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        - RouteTargetAs (number): Autonomous system (AS) number. A 2-byte AS number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetAssignedNum (number): Autonomous system (AS) and assigned number. A 2-byte AS number and a 4-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetIp (str): IP address and assigned number. A 4-byte IPv4 address and a 2-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetType (str(as | ip)): The Admin part type is to the type of route target attribute
        - SiteId (number): The identifier for the L2 (CE) site. The default is 0.
        - SiteIdIncrement (number): Increments the site identifier
        - TargetAssignedNumberIncrement (number): Signifies increment of the target assigned number
        - TargetIncrementAs (number): Signifies increment as target
        - TargetIpIncrement (str): Signifies the increment of IP as target
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.

        Returns
        -------
        - self: This instance with all currently retrieved l2Site resources using find and the newly added l2Site resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained l2Site resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        DistinguishAssignedIncrement=None,
        DistinguishIpIncrement=None,
        DistinguishNumberIncrementAs=None,
        EnableBfdVccv=None,
        EnableCluster=None,
        EnableControlWord=None,
        EnableL2SiteAsTrafficEndpoint=None,
        EnableSequenceDelivery=None,
        EnableVccvPing=None,
        Enabled=None,
        IsLearnedInfoRefreshed=None,
        Mtu=None,
        NoOfL2Site=None,
        RouteDistinguisherAs=None,
        RouteDistinguisherAssignedNum=None,
        RouteDistinguisherIp=None,
        RouteDistinguisherType=None,
        RouteTargetAs=None,
        RouteTargetAssignedNum=None,
        RouteTargetIp=None,
        RouteTargetType=None,
        SiteId=None,
        SiteIdIncrement=None,
        TargetAssignedNumberIncrement=None,
        TargetIncrementAs=None,
        TargetIpIncrement=None,
        TrafficGroupId=None,
    ):
        # type: (int, str, int, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, int, str, str, int, int, str, str, int, int, int, int, str, str) -> L2Site
        """Finds and retrieves l2Site resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l2Site resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l2Site resources from the server.

        Args
        ----
        - DistinguishAssignedIncrement (number): Distinguishes increment of the assigned value
        - DistinguishIpIncrement (str): Distinguishes the increment of the IP address
        - DistinguishNumberIncrementAs (number): Signifies the distinguished increment as number
        - EnableBfdVccv (bool): If true, enables BFD VCCV
        - EnableCluster (bool): Enables and controls the use of L2 VPN VPLS.
        - EnableControlWord (bool): Enables the use of a control word, as part of the extended community information.
        - EnableL2SiteAsTrafficEndpoint (bool): If true, enables L2 site as traffic endpoint
        - EnableSequenceDelivery (bool): Enables the use of sequenced delivery of frames, as part of the extended community information.
        - EnableVccvPing (bool): If true, enables the VCCV ping
        - Enabled (bool): Enables or disables use of the L2 VPN site.
        - IsLearnedInfoRefreshed (bool): If true, learned information is refreshed.
        - Mtu (number): The Maximum Transmission Unit (MTU) allowed on this link, in bytes. The valid range is 0 to 16777215. (default = 1,500 bytes)
        - NoOfL2Site (number): Signifies the number of L2 sites
        - RouteDistinguisherAs (number): Available for use only if the route distinguish type is set to AS. The route distinguisher autonomous system (AS) number.
        - RouteDistinguisherAssignedNum (number): The assigned number for use with the distinguisher IP address or AS number, to create the route distinguisher.The default is 0.
        - RouteDistinguisherIp (str): Available for use only if the route Distinguish Type is set to IP. The route distinguisher IP address. A 4-byte IPv4 address.The default is 0.0.0.0.
        - RouteDistinguisherType (str(twoOctetAs | ip | fourOctetAs)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        - RouteTargetAs (number): Autonomous system (AS) number. A 2-byte AS number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetAssignedNum (number): Autonomous system (AS) and assigned number. A 2-byte AS number and a 4-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetIp (str): IP address and assigned number. A 4-byte IPv4 address and a 2-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetType (str(as | ip)): The Admin part type is to the type of route target attribute
        - SiteId (number): The identifier for the L2 (CE) site. The default is 0.
        - SiteIdIncrement (number): Increments the site identifier
        - TargetAssignedNumberIncrement (number): Signifies increment of the target assigned number
        - TargetIncrementAs (number): Signifies increment as target
        - TargetIpIncrement (str): Signifies the increment of IP as target
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.

        Returns
        -------
        - self: This instance with matching l2Site resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of l2Site data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l2Site resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshLearnedInfo operation on the server.

        This function argument allows to refreshe the BGP learned information from the DUT.

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
