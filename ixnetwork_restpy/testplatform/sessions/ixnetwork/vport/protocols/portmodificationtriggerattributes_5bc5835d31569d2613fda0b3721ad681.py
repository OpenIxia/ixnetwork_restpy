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


class PortModificationTriggerAttributes(Base):
    """NOT DEFINED
    The PortModificationTriggerAttributes class encapsulates a required portModificationTriggerAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "portModificationTriggerAttributes"
    _SDM_ATT_MAP = {
        "AdvertisedFeatures": "advertisedFeatures",
        "DoNotSendPacketIn": "doNotSendPacketIn",
        "DropAllPackets": "dropAllPackets",
        "DropForwardedPackets": "dropForwardedPackets",
        "EnableAdvertiseFeature": "enableAdvertiseFeature",
        "EnableEthernetAddress": "enableEthernetAddress",
        "EnablePortConfig": "enablePortConfig",
        "EnablePortModPortFeatures": "enablePortModPortFeatures",
        "EnablePortNumber": "enablePortNumber",
        "EthernetAddress": "ethernetAddress",
        "PortAdministrativelyDown": "portAdministrativelyDown",
        "PortConfig": "portConfig",
        "PortConfigMask": "portConfigMask",
        "PortNumber": "portNumber",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PortModificationTriggerAttributes, self).__init__(parent, list_op)

    @property
    def LinkFeature(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkfeature_2218f0edff079bfefabc46ff517244ed.LinkFeature): An instance of the LinkFeature class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkfeature_2218f0edff079bfefabc46ff517244ed import (
            LinkFeature,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LinkFeature", None) is not None:
                return self._properties.get("LinkFeature")
        return LinkFeature(self)._select()

    @property
    def LinkMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkmode_74aa7aa60a1fac72da4cb79ff35dbccc.LinkMode): An instance of the LinkMode class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkmode_74aa7aa60a1fac72da4cb79ff35dbccc import (
            LinkMode,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LinkMode", None) is not None:
                return self._properties.get("LinkMode")
        return LinkMode(self)._select()

    @property
    def LinkType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linktype_f1c0f4e35dd4b90849930768604d1618.LinkType): An instance of the LinkType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linktype_f1c0f4e35dd4b90849930768604d1618 import (
            LinkType,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LinkType", None) is not None:
                return self._properties.get("LinkType")
        return LinkType(self)._select()

    @property
    def AdvertisedFeatures(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdvertisedFeatures"])

    @AdvertisedFeatures.setter
    def AdvertisedFeatures(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AdvertisedFeatures"], value)

    @property
    def DoNotSendPacketIn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DoNotSendPacketIn"])

    @DoNotSendPacketIn.setter
    def DoNotSendPacketIn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DoNotSendPacketIn"], value)

    @property
    def DropAllPackets(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DropAllPackets"])

    @DropAllPackets.setter
    def DropAllPackets(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DropAllPackets"], value)

    @property
    def DropForwardedPackets(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DropForwardedPackets"])

    @DropForwardedPackets.setter
    def DropForwardedPackets(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DropForwardedPackets"], value)

    @property
    def EnableAdvertiseFeature(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAdvertiseFeature"])

    @EnableAdvertiseFeature.setter
    def EnableAdvertiseFeature(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAdvertiseFeature"], value)

    @property
    def EnableEthernetAddress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableEthernetAddress"])

    @EnableEthernetAddress.setter
    def EnableEthernetAddress(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableEthernetAddress"], value)

    @property
    def EnablePortConfig(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePortConfig"])

    @EnablePortConfig.setter
    def EnablePortConfig(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePortConfig"], value)

    @property
    def EnablePortModPortFeatures(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePortModPortFeatures"])

    @EnablePortModPortFeatures.setter
    def EnablePortModPortFeatures(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePortModPortFeatures"], value)

    @property
    def EnablePortNumber(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePortNumber"])

    @EnablePortNumber.setter
    def EnablePortNumber(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePortNumber"], value)

    @property
    def EthernetAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetAddress"])

    @EthernetAddress.setter
    def EthernetAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetAddress"], value)

    @property
    def PortAdministrativelyDown(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortAdministrativelyDown"])

    @PortAdministrativelyDown.setter
    def PortAdministrativelyDown(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortAdministrativelyDown"], value)

    @property
    def PortConfig(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortConfig"])

    @PortConfig.setter
    def PortConfig(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortConfig"], value)

    @property
    def PortConfigMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortConfigMask"])

    @PortConfigMask.setter
    def PortConfigMask(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortConfigMask"], value)

    @property
    def PortNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortNumber"])

    @PortNumber.setter
    def PortNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortNumber"], value)

    def update(
        self,
        AdvertisedFeatures=None,
        DoNotSendPacketIn=None,
        DropAllPackets=None,
        DropForwardedPackets=None,
        EnableAdvertiseFeature=None,
        EnableEthernetAddress=None,
        EnablePortConfig=None,
        EnablePortModPortFeatures=None,
        EnablePortNumber=None,
        EthernetAddress=None,
        PortAdministrativelyDown=None,
        PortConfig=None,
        PortConfigMask=None,
        PortNumber=None,
    ):
        # type: (str, bool, bool, bool, bool, bool, bool, bool, bool, str, bool, str, str, int) -> PortModificationTriggerAttributes
        """Updates portModificationTriggerAttributes resource on the server.

        Args
        ----
        - AdvertisedFeatures (str): NOT DEFINED
        - DoNotSendPacketIn (bool): NOT DEFINED
        - DropAllPackets (bool): NOT DEFINED
        - DropForwardedPackets (bool): NOT DEFINED
        - EnableAdvertiseFeature (bool): NOT DEFINED
        - EnableEthernetAddress (bool): NOT DEFINED
        - EnablePortConfig (bool): NOT DEFINED
        - EnablePortModPortFeatures (bool): NOT DEFINED
        - EnablePortNumber (bool): NOT DEFINED
        - EthernetAddress (str): NOT DEFINED
        - PortAdministrativelyDown (bool): NOT DEFINED
        - PortConfig (str): NOT DEFINED
        - PortConfigMask (str): NOT DEFINED
        - PortNumber (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AdvertisedFeatures=None,
        DoNotSendPacketIn=None,
        DropAllPackets=None,
        DropForwardedPackets=None,
        EnableAdvertiseFeature=None,
        EnableEthernetAddress=None,
        EnablePortConfig=None,
        EnablePortModPortFeatures=None,
        EnablePortNumber=None,
        EthernetAddress=None,
        PortAdministrativelyDown=None,
        PortConfig=None,
        PortConfigMask=None,
        PortNumber=None,
    ):
        # type: (str, bool, bool, bool, bool, bool, bool, bool, bool, str, bool, str, str, int) -> PortModificationTriggerAttributes
        """Finds and retrieves portModificationTriggerAttributes resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve portModificationTriggerAttributes resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all portModificationTriggerAttributes resources from the server.

        Args
        ----
        - AdvertisedFeatures (str): NOT DEFINED
        - DoNotSendPacketIn (bool): NOT DEFINED
        - DropAllPackets (bool): NOT DEFINED
        - DropForwardedPackets (bool): NOT DEFINED
        - EnableAdvertiseFeature (bool): NOT DEFINED
        - EnableEthernetAddress (bool): NOT DEFINED
        - EnablePortConfig (bool): NOT DEFINED
        - EnablePortModPortFeatures (bool): NOT DEFINED
        - EnablePortNumber (bool): NOT DEFINED
        - EthernetAddress (str): NOT DEFINED
        - PortAdministrativelyDown (bool): NOT DEFINED
        - PortConfig (str): NOT DEFINED
        - PortConfigMask (str): NOT DEFINED
        - PortNumber (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching portModificationTriggerAttributes resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of portModificationTriggerAttributes data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the portModificationTriggerAttributes resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
