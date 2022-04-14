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


class UserLsa(Base):
    """
    The UserLsa class encapsulates a list of userLsa resources that are managed by the user.
    A list of resources can be retrieved from the server using the UserLsa.find() method.
    The list can be managed by using the UserLsa.add() and UserLsa.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "userLsa"
    _SDM_ATT_MAP = {
        "AdvertisingRouterId": "advertisingRouterId",
        "Enabled": "enabled",
        "ExpandIntoLinksOrAttachedRouters": "expandIntoLinksOrAttachedRouters",
        "LinkStateId": "linkStateId",
        "LsaType": "lsaType",
    }
    _SDM_ENUM_MAP = {
        "lsaType": [
            "router",
            "network",
            "interAreaPrefix",
            "interAreaRouter",
            "asExternal",
            "link",
            "intraAreaPrefix",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(UserLsa, self).__init__(parent, list_op)

    @property
    def AsExternal(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.asexternal_12dfafe33ad036e6bec4644070502044.AsExternal): An instance of the AsExternal class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.asexternal_12dfafe33ad036e6bec4644070502044 import (
            AsExternal,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AsExternal", None) is not None:
                return self._properties.get("AsExternal")
        return AsExternal(self)

    @property
    def InterAreaPrefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interareaprefix_51bc1fa5c3615d5498ea43e228445c3c.InterAreaPrefix): An instance of the InterAreaPrefix class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interareaprefix_51bc1fa5c3615d5498ea43e228445c3c import (
            InterAreaPrefix,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("InterAreaPrefix", None) is not None:
                return self._properties.get("InterAreaPrefix")
        return InterAreaPrefix(self)

    @property
    def InterAreaRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interarearouter_edc636547087f303c13b929510c197e4.InterAreaRouter): An instance of the InterAreaRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interarearouter_edc636547087f303c13b929510c197e4 import (
            InterAreaRouter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("InterAreaRouter", None) is not None:
                return self._properties.get("InterAreaRouter")
        return InterAreaRouter(self)

    @property
    def IntraAreaPrefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.intraareaprefix_4ec65d4b4fd020944df3498606a28a76.IntraAreaPrefix): An instance of the IntraAreaPrefix class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.intraareaprefix_4ec65d4b4fd020944df3498606a28a76 import (
            IntraAreaPrefix,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IntraAreaPrefix", None) is not None:
                return self._properties.get("IntraAreaPrefix")
        return IntraAreaPrefix(self)

    @property
    def Link(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_7f592ebf252bce0f6d8d1042bf348acd.Link): An instance of the Link class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.link_7f592ebf252bce0f6d8d1042bf348acd import (
            Link,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Link", None) is not None:
                return self._properties.get("Link")
        return Link(self)

    @property
    def Network(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.network_6984533d658be615d6eb86f965975b8b.Network): An instance of the Network class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.network_6984533d658be615d6eb86f965975b8b import (
            Network,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Network", None) is not None:
                return self._properties.get("Network")
        return Network(self)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_b249d35e2a940b6bd8f505a80cb0d44a.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_b249d35e2a940b6bd8f505a80cb0d44a import (
            Router,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Router", None) is not None:
                return self._properties.get("Router")
        return Router(self)

    @property
    def AdvertisingRouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdvertisingRouterId"])

    @AdvertisingRouterId.setter
    def AdvertisingRouterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AdvertisingRouterId"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def ExpandIntoLinksOrAttachedRouters(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ExpandIntoLinksOrAttachedRouters"]
        )

    @ExpandIntoLinksOrAttachedRouters.setter
    def ExpandIntoLinksOrAttachedRouters(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ExpandIntoLinksOrAttachedRouters"], value
        )

    @property
    def LinkStateId(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkStateId"])

    @LinkStateId.setter
    def LinkStateId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkStateId"], value)

    @property
    def LsaType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(router | network | interAreaPrefix | interAreaRouter | asExternal | link | intraAreaPrefix):
        """
        return self._get_attribute(self._SDM_ATT_MAP["LsaType"])

    @LsaType.setter
    def LsaType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LsaType"], value)

    def update(
        self,
        AdvertisingRouterId=None,
        Enabled=None,
        ExpandIntoLinksOrAttachedRouters=None,
        LinkStateId=None,
        LsaType=None,
    ):
        # type: (str, bool, bool, str, str) -> UserLsa
        """Updates userLsa resource on the server.

        Args
        ----
        - AdvertisingRouterId (str):
        - Enabled (bool):
        - ExpandIntoLinksOrAttachedRouters (bool):
        - LinkStateId (str):
        - LsaType (str(router | network | interAreaPrefix | interAreaRouter | asExternal | link | intraAreaPrefix)):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AdvertisingRouterId=None,
        Enabled=None,
        ExpandIntoLinksOrAttachedRouters=None,
        LinkStateId=None,
        LsaType=None,
    ):
        # type: (str, bool, bool, str, str) -> UserLsa
        """Adds a new userLsa resource on the server and adds it to the container.

        Args
        ----
        - AdvertisingRouterId (str):
        - Enabled (bool):
        - ExpandIntoLinksOrAttachedRouters (bool):
        - LinkStateId (str):
        - LsaType (str(router | network | interAreaPrefix | interAreaRouter | asExternal | link | intraAreaPrefix)):

        Returns
        -------
        - self: This instance with all currently retrieved userLsa resources using find and the newly added userLsa resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained userLsa resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AdvertisingRouterId=None,
        Enabled=None,
        ExpandIntoLinksOrAttachedRouters=None,
        LinkStateId=None,
        LsaType=None,
    ):
        # type: (str, bool, bool, str, str) -> UserLsa
        """Finds and retrieves userLsa resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve userLsa resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all userLsa resources from the server.

        Args
        ----
        - AdvertisingRouterId (str):
        - Enabled (bool):
        - ExpandIntoLinksOrAttachedRouters (bool):
        - LinkStateId (str):
        - LsaType (str(router | network | interAreaPrefix | interAreaRouter | asExternal | link | intraAreaPrefix)):

        Returns
        -------
        - self: This instance with matching userLsa resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of userLsa data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the userLsa resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
