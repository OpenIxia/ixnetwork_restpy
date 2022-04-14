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
        "OptBitDemandCircuit": "optBitDemandCircuit",
        "OptBitExternalAttributes": "optBitExternalAttributes",
        "OptBitExternalRouting": "optBitExternalRouting",
        "OptBitLsaNoForward": "optBitLsaNoForward",
        "OptBitMulticast": "optBitMulticast",
        "OptBitNssaCapability": "optBitNssaCapability",
        "OptBitTypeOfService": "optBitTypeOfService",
        "Option": "option",
    }
    _SDM_ENUM_MAP = {
        "lsaType": [
            "router",
            "network",
            "areaSummary",
            "externalSummary",
            "external",
            "nssa",
            "opaqueLocalScope",
            "opaqueAreaScope",
            "opaqueAsScope",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(UserLsa, self).__init__(parent, list_op)

    @property
    def External(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.external_5f713e4ff5ec2297a9ee77f4fc87e67f.External): An instance of the External class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.external_5f713e4ff5ec2297a9ee77f4fc87e67f import (
            External,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("External", None) is not None:
                return self._properties.get("External")
        return External(self)

    @property
    def Network(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.network_ab7cacc5147193bf15144d9976e31e5e.Network): An instance of the Network class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.network_ab7cacc5147193bf15144d9976e31e5e import (
            Network,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Network", None) is not None:
                return self._properties.get("Network")
        return Network(self)

    @property
    def Nssa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nssa_926f7a4ce5a139e05060d94a97af7411.Nssa): An instance of the Nssa class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nssa_926f7a4ce5a139e05060d94a97af7411 import (
            Nssa,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Nssa", None) is not None:
                return self._properties.get("Nssa")
        return Nssa(self)

    @property
    def Opaque(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaque_f86f4a4822065deb46f8e3927f1f473f.Opaque): An instance of the Opaque class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaque_f86f4a4822065deb46f8e3927f1f473f import (
            Opaque,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Opaque", None) is not None:
                return self._properties.get("Opaque")
        return Opaque(self)

    @property
    def Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_0adffb2d881dee33ea86b034b59de2e6.Router): An instance of the Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_0adffb2d881dee33ea86b034b59de2e6 import (
            Router,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Router", None) is not None:
                return self._properties.get("Router")
        return Router(self)

    @property
    def SummaryIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.summaryip_d35397f1c35713560a222df362b20a8a.SummaryIp): An instance of the SummaryIp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.summaryip_d35397f1c35713560a222df362b20a8a import (
            SummaryIp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SummaryIp", None) is not None:
                return self._properties.get("SummaryIp")
        return SummaryIp(self)

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
        - str(router | network | areaSummary | externalSummary | external | nssa | opaqueLocalScope | opaqueAreaScope | opaqueAsScope):
        """
        return self._get_attribute(self._SDM_ATT_MAP["LsaType"])

    @LsaType.setter
    def LsaType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LsaType"], value)

    @property
    def OptBitDemandCircuit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitDemandCircuit"])

    @OptBitDemandCircuit.setter
    def OptBitDemandCircuit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitDemandCircuit"], value)

    @property
    def OptBitExternalAttributes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitExternalAttributes"])

    @OptBitExternalAttributes.setter
    def OptBitExternalAttributes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitExternalAttributes"], value)

    @property
    def OptBitExternalRouting(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitExternalRouting"])

    @OptBitExternalRouting.setter
    def OptBitExternalRouting(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitExternalRouting"], value)

    @property
    def OptBitLsaNoForward(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitLsaNoForward"])

    @OptBitLsaNoForward.setter
    def OptBitLsaNoForward(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitLsaNoForward"], value)

    @property
    def OptBitMulticast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitMulticast"])

    @OptBitMulticast.setter
    def OptBitMulticast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitMulticast"], value)

    @property
    def OptBitNssaCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitNssaCapability"])

    @OptBitNssaCapability.setter
    def OptBitNssaCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitNssaCapability"], value)

    @property
    def OptBitTypeOfService(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["OptBitTypeOfService"])

    @OptBitTypeOfService.setter
    def OptBitTypeOfService(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OptBitTypeOfService"], value)

    @property
    def Option(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Option"])

    @Option.setter
    def Option(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Option"], value)

    def update(
        self,
        AdvertisingRouterId=None,
        Enabled=None,
        ExpandIntoLinksOrAttachedRouters=None,
        LinkStateId=None,
        LsaType=None,
        OptBitDemandCircuit=None,
        OptBitExternalAttributes=None,
        OptBitExternalRouting=None,
        OptBitLsaNoForward=None,
        OptBitMulticast=None,
        OptBitNssaCapability=None,
        OptBitTypeOfService=None,
        Option=None,
    ):
        # type: (str, bool, bool, str, str, bool, bool, bool, bool, bool, bool, bool, int) -> UserLsa
        """Updates userLsa resource on the server.

        Args
        ----
        - AdvertisingRouterId (str):
        - Enabled (bool):
        - ExpandIntoLinksOrAttachedRouters (bool):
        - LinkStateId (str):
        - LsaType (str(router | network | areaSummary | externalSummary | external | nssa | opaqueLocalScope | opaqueAreaScope | opaqueAsScope)):
        - OptBitDemandCircuit (bool):
        - OptBitExternalAttributes (bool):
        - OptBitExternalRouting (bool):
        - OptBitLsaNoForward (bool):
        - OptBitMulticast (bool):
        - OptBitNssaCapability (bool):
        - OptBitTypeOfService (bool):
        - Option (number):

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
        OptBitDemandCircuit=None,
        OptBitExternalAttributes=None,
        OptBitExternalRouting=None,
        OptBitLsaNoForward=None,
        OptBitMulticast=None,
        OptBitNssaCapability=None,
        OptBitTypeOfService=None,
        Option=None,
    ):
        # type: (str, bool, bool, str, str, bool, bool, bool, bool, bool, bool, bool, int) -> UserLsa
        """Adds a new userLsa resource on the server and adds it to the container.

        Args
        ----
        - AdvertisingRouterId (str):
        - Enabled (bool):
        - ExpandIntoLinksOrAttachedRouters (bool):
        - LinkStateId (str):
        - LsaType (str(router | network | areaSummary | externalSummary | external | nssa | opaqueLocalScope | opaqueAreaScope | opaqueAsScope)):
        - OptBitDemandCircuit (bool):
        - OptBitExternalAttributes (bool):
        - OptBitExternalRouting (bool):
        - OptBitLsaNoForward (bool):
        - OptBitMulticast (bool):
        - OptBitNssaCapability (bool):
        - OptBitTypeOfService (bool):
        - Option (number):

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
        OptBitDemandCircuit=None,
        OptBitExternalAttributes=None,
        OptBitExternalRouting=None,
        OptBitLsaNoForward=None,
        OptBitMulticast=None,
        OptBitNssaCapability=None,
        OptBitTypeOfService=None,
        Option=None,
    ):
        # type: (str, bool, bool, str, str, bool, bool, bool, bool, bool, bool, bool, int) -> UserLsa
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
        - LsaType (str(router | network | areaSummary | externalSummary | external | nssa | opaqueLocalScope | opaqueAreaScope | opaqueAsScope)):
        - OptBitDemandCircuit (bool):
        - OptBitExternalAttributes (bool):
        - OptBitExternalRouting (bool):
        - OptBitLsaNoForward (bool):
        - OptBitMulticast (bool):
        - OptBitNssaCapability (bool):
        - OptBitTypeOfService (bool):
        - Option (number):

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
