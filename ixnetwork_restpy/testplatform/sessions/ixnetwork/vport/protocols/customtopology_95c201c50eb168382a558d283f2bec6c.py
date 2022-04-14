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


class CustomTopology(Base):
    """NOT DEFINED
    The CustomTopology class encapsulates a list of customTopology resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopology.find() method.
    The list can be managed by using the CustomTopology.add() and CustomTopology.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "customTopology"
    _SDM_ATT_MAP = {
        "CapRouterId": "capRouterId",
        "EnableHostname": "enableHostname",
        "Enabled": "enabled",
        "HostNamePrefix": "hostNamePrefix",
        "InterfaceMetric": "interfaceMetric",
        "StartSysId": "startSysId",
        "SysIdInc": "sysIdInc",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(CustomTopology, self).__init__(parent, list_op)

    @property
    def CustomTopologyMulticastIpv4GroupRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastipv4grouprange_9d19522687e570b2612a647ef6eec0f3.CustomTopologyMulticastIpv4GroupRange): An instance of the CustomTopologyMulticastIpv4GroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastipv4grouprange_9d19522687e570b2612a647ef6eec0f3 import (
            CustomTopologyMulticastIpv4GroupRange,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("CustomTopologyMulticastIpv4GroupRange", None)
                is not None
            ):
                return self._properties.get("CustomTopologyMulticastIpv4GroupRange")
        return CustomTopologyMulticastIpv4GroupRange(self)

    @property
    def CustomTopologyMulticastIpv6GroupRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastipv6grouprange_1084bcd8c4ba63b5afb4987b4a06e574.CustomTopologyMulticastIpv6GroupRange): An instance of the CustomTopologyMulticastIpv6GroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastipv6grouprange_1084bcd8c4ba63b5afb4987b4a06e574 import (
            CustomTopologyMulticastIpv6GroupRange,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("CustomTopologyMulticastIpv6GroupRange", None)
                is not None
            ):
                return self._properties.get("CustomTopologyMulticastIpv6GroupRange")
        return CustomTopologyMulticastIpv6GroupRange(self)

    @property
    def CustomTopologyMulticastMacRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastmacrange_3e16b26e0a0e86e9899bec4037756f4b.CustomTopologyMulticastMacRange): An instance of the CustomTopologyMulticastMacRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologymulticastmacrange_3e16b26e0a0e86e9899bec4037756f4b import (
            CustomTopologyMulticastMacRange,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("CustomTopologyMulticastMacRange", None)
                is not None
            ):
                return self._properties.get("CustomTopologyMulticastMacRange")
        return CustomTopologyMulticastMacRange(self)

    @property
    def CustomTopologyNode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologynode_0b9b312d608aa93cb26d0457892552b0.CustomTopologyNode): An instance of the CustomTopologyNode class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologynode_0b9b312d608aa93cb26d0457892552b0 import (
            CustomTopologyNode,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CustomTopologyNode", None) is not None:
                return self._properties.get("CustomTopologyNode")
        return CustomTopologyNode(self)

    @property
    def CustomTopologyNodeTopologyRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologynodetopologyrange_4d32635ad74f7f368c2bf92ae60c207c.CustomTopologyNodeTopologyRange): An instance of the CustomTopologyNodeTopologyRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologynodetopologyrange_4d32635ad74f7f368c2bf92ae60c207c import (
            CustomTopologyNodeTopologyRange,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("CustomTopologyNodeTopologyRange", None)
                is not None
            ):
                return self._properties.get("CustomTopologyNodeTopologyRange")
        return CustomTopologyNodeTopologyRange(self)

    @property
    def CustomTopologyRbLinks(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyrblinks_0932f6b9efaed07e8b33d7f83f8c0051.CustomTopologyRbLinks): An instance of the CustomTopologyRbLinks class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyrblinks_0932f6b9efaed07e8b33d7f83f8c0051 import (
            CustomTopologyRbLinks,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CustomTopologyRbLinks", None) is not None:
                return self._properties.get("CustomTopologyRbLinks")
        return CustomTopologyRbLinks(self)

    @property
    def CustomTopologySpbNodeTopologyRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyspbnodetopologyrange_f8b5e7f7ba20491acaffdef257a0259c.CustomTopologySpbNodeTopologyRange): An instance of the CustomTopologySpbNodeTopologyRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyspbnodetopologyrange_f8b5e7f7ba20491acaffdef257a0259c import (
            CustomTopologySpbNodeTopologyRange,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("CustomTopologySpbNodeTopologyRange", None)
                is not None
            ):
                return self._properties.get("CustomTopologySpbNodeTopologyRange")
        return CustomTopologySpbNodeTopologyRange(self)

    @property
    def CustomTopologyUnicastMacRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyunicastmacrange_45433238099b8e4640614c04f49605bb.CustomTopologyUnicastMacRange): An instance of the CustomTopologyUnicastMacRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyunicastmacrange_45433238099b8e4640614c04f49605bb import (
            CustomTopologyUnicastMacRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CustomTopologyUnicastMacRange", None) is not None:
                return self._properties.get("CustomTopologyUnicastMacRange")
        return CustomTopologyUnicastMacRange(self)

    @property
    def CapRouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["CapRouterId"])

    @CapRouterId.setter
    def CapRouterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CapRouterId"], value)

    @property
    def EnableHostname(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableHostname"])

    @EnableHostname.setter
    def EnableHostname(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableHostname"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def HostNamePrefix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostNamePrefix"])

    @HostNamePrefix.setter
    def HostNamePrefix(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["HostNamePrefix"], value)

    @property
    def InterfaceMetric(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceMetric"])

    @InterfaceMetric.setter
    def InterfaceMetric(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterfaceMetric"], value)

    @property
    def StartSysId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartSysId"])

    @StartSysId.setter
    def StartSysId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartSysId"], value)

    @property
    def SysIdInc(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SysIdInc"])

    @SysIdInc.setter
    def SysIdInc(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SysIdInc"], value)

    def update(
        self,
        CapRouterId=None,
        EnableHostname=None,
        Enabled=None,
        HostNamePrefix=None,
        InterfaceMetric=None,
        StartSysId=None,
        SysIdInc=None,
    ):
        # type: (str, bool, bool, str, int, str, str) -> CustomTopology
        """Updates customTopology resource on the server.

        Args
        ----
        - CapRouterId (str): NOT DEFINED
        - EnableHostname (bool): NOT DEFINED
        - Enabled (bool): NOT DEFINED
        - HostNamePrefix (str): NOT DEFINED
        - InterfaceMetric (number): NOT DEFINED
        - StartSysId (str): NOT DEFINED
        - SysIdInc (str): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        CapRouterId=None,
        EnableHostname=None,
        Enabled=None,
        HostNamePrefix=None,
        InterfaceMetric=None,
        StartSysId=None,
        SysIdInc=None,
    ):
        # type: (str, bool, bool, str, int, str, str) -> CustomTopology
        """Adds a new customTopology resource on the server and adds it to the container.

        Args
        ----
        - CapRouterId (str): NOT DEFINED
        - EnableHostname (bool): NOT DEFINED
        - Enabled (bool): NOT DEFINED
        - HostNamePrefix (str): NOT DEFINED
        - InterfaceMetric (number): NOT DEFINED
        - StartSysId (str): NOT DEFINED
        - SysIdInc (str): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopology resources using find and the newly added customTopology resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopology resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        CapRouterId=None,
        EnableHostname=None,
        Enabled=None,
        HostNamePrefix=None,
        InterfaceMetric=None,
        StartSysId=None,
        SysIdInc=None,
    ):
        # type: (str, bool, bool, str, int, str, str) -> CustomTopology
        """Finds and retrieves customTopology resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopology resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopology resources from the server.

        Args
        ----
        - CapRouterId (str): NOT DEFINED
        - EnableHostname (bool): NOT DEFINED
        - Enabled (bool): NOT DEFINED
        - HostNamePrefix (str): NOT DEFINED
        - InterfaceMetric (number): NOT DEFINED
        - StartSysId (str): NOT DEFINED
        - SysIdInc (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopology resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopology data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopology resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
