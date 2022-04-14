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


class DestinationRange(Base):
    """Describes a set of routers that are the destination of MPLS tunnels. Destination ranges correspond to Ingress or Egress routers.
    The DestinationRange class encapsulates a list of destinationRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the DestinationRange.find() method.
    The list can be managed by using the DestinationRange.add() and DestinationRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "destinationRange"
    _SDM_ATT_MAP = {
        "Behavior": "behavior",
        "EmulationType": "emulationType",
        "EnableReplyingLspPing": "enableReplyingLspPing",
        "Enabled": "enabled",
        "IpAddressFrom": "ipAddressFrom",
        "IpCount": "ipCount",
        "IsConnectedIpAppended": "isConnectedIpAppended",
        "IsHeadIpPrepended": "isHeadIpPrepended",
        "IsLeafIpPrepended": "isLeafIpPrepended",
        "IsSendingAsRro": "isSendingAsRro",
        "IsSendingAsSrro": "isSendingAsSrro",
        "P2mpId": "p2mpId",
    }
    _SDM_ENUM_MAP = {
        "behavior": ["ingress", "egress"],
        "emulationType": ["reserved", "rsvpTe", "rsvpTeP2mP"],
    }

    def __init__(self, parent, list_op=False):
        super(DestinationRange, self).__init__(parent, list_op)

    @property
    def Egress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.egress_eafa79ad778e0a6c6cd87e7f67bde5ec.Egress): An instance of the Egress class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.egress_eafa79ad778e0a6c6cd87e7f67bde5ec import (
            Egress,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Egress", None) is not None:
                return self._properties.get("Egress")
        return Egress(self)._select()

    @property
    def Ingress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ingress_da8eb3f5bded227d4615e7b9e030b32d.Ingress): An instance of the Ingress class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ingress_da8eb3f5bded227d4615e7b9e030b32d import (
            Ingress,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ingress", None) is not None:
                return self._properties.get("Ingress")
        return Ingress(self)._select()

    @property
    def TunnelLeafRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tunnelleafrange_66cac69e2e026fc7d2fdc68b1e28e7ca.TunnelLeafRange): An instance of the TunnelLeafRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tunnelleafrange_66cac69e2e026fc7d2fdc68b1e28e7ca import (
            TunnelLeafRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TunnelLeafRange", None) is not None:
                return self._properties.get("TunnelLeafRange")
        return TunnelLeafRange(self)

    @property
    def TunnelTailTrafficEndPoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tunneltailtrafficendpoint_284f93fd059aad011661455f3f6293cb.TunnelTailTrafficEndPoint): An instance of the TunnelTailTrafficEndPoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tunneltailtrafficendpoint_284f93fd059aad011661455f3f6293cb import (
            TunnelTailTrafficEndPoint,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TunnelTailTrafficEndPoint", None) is not None:
                return self._properties.get("TunnelTailTrafficEndPoint")
        return TunnelTailTrafficEndPoint(self)

    @property
    def Behavior(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ingress | egress): Indicates whether the destination range corresponds to an Ingress or Egress router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Behavior"])

    @Behavior.setter
    def Behavior(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Behavior"], value)

    @property
    def EmulationType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(reserved | rsvpTe | rsvpTeP2mP): The emulation type selected, the values being RSVP-TE, RSVP-TE P2MP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EmulationType"])

    @EmulationType.setter
    def EmulationType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EmulationType"], value)

    @property
    def EnableReplyingLspPing(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableReplyingLspPing"])

    @EnableReplyingLspPing.setter
    def EnableReplyingLspPing(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableReplyingLspPing"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables the use of the destination range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def IpAddressFrom(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address of the first destination router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpAddressFrom"])

    @IpAddressFrom.setter
    def IpAddressFrom(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpAddressFrom"], value)

    @property
    def IpCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of destination routers. Each router's address is one greater than the previous one's.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpCount"])

    @IpCount.setter
    def IpCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpCount"], value)

    @property
    def IsConnectedIpAppended(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Append the connected IP as RRO/SRRO subobject at the end of the RRo/SRRO list in the packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsConnectedIpAppended"])

    @IsConnectedIpAppended.setter
    def IsConnectedIpAppended(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsConnectedIpAppended"], value)

    @property
    def IsHeadIpPrepended(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, prepend the tunnel head IP as a RRO/SERO subobject at the beginning of the RRO/SRRO list in the packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsHeadIpPrepended"])

    @IsHeadIpPrepended.setter
    def IsHeadIpPrepended(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsHeadIpPrepended"], value)

    @property
    def IsLeafIpPrepended(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, prepend the tunnel leaf IP as a RRO/SRRO subobject at the beginning of the RRO/SRRO list in the packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLeafIpPrepended"])

    @IsLeafIpPrepended.setter
    def IsLeafIpPrepended(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsLeafIpPrepended"], value)

    @property
    def IsSendingAsRro(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, send this as a RRO. True only if emulation type is RSVP-TE P2MP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsSendingAsRro"])

    @IsSendingAsRro.setter
    def IsSendingAsRro(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsSendingAsRro"], value)

    @property
    def IsSendingAsSrro(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, send this as a SRRO. Note that both Send as RRO and Send as SRRO can be selected at the same time if so required by the user. True only if emulation type is RSVP-TE P2MP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsSendingAsSrro"])

    @IsSendingAsSrro.setter
    def IsSendingAsSrro(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsSendingAsSrro"], value)

    @property
    def P2mpId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The P2MP id represented in IP address format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["P2mpId"])

    @P2mpId.setter
    def P2mpId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["P2mpId"], value)

    def update(
        self,
        Behavior=None,
        EmulationType=None,
        EnableReplyingLspPing=None,
        Enabled=None,
        IpAddressFrom=None,
        IpCount=None,
        IsConnectedIpAppended=None,
        IsHeadIpPrepended=None,
        IsLeafIpPrepended=None,
        IsSendingAsRro=None,
        IsSendingAsSrro=None,
        P2mpId=None,
    ):
        # type: (str, str, bool, bool, str, int, bool, bool, bool, bool, bool, str) -> DestinationRange
        """Updates destinationRange resource on the server.

        Args
        ----
        - Behavior (str(ingress | egress)): Indicates whether the destination range corresponds to an Ingress or Egress router.
        - EmulationType (str(reserved | rsvpTe | rsvpTeP2mP)): The emulation type selected, the values being RSVP-TE, RSVP-TE P2MP.
        - EnableReplyingLspPing (bool): NOT DEFINED
        - Enabled (bool): Enables or disables the use of the destination range.
        - IpAddressFrom (str): The IP address of the first destination router.
        - IpCount (number): The number of destination routers. Each router's address is one greater than the previous one's.
        - IsConnectedIpAppended (bool): Append the connected IP as RRO/SRRO subobject at the end of the RRo/SRRO list in the packet.
        - IsHeadIpPrepended (bool): If true, prepend the tunnel head IP as a RRO/SERO subobject at the beginning of the RRO/SRRO list in the packet.
        - IsLeafIpPrepended (bool): If true, prepend the tunnel leaf IP as a RRO/SRRO subobject at the beginning of the RRO/SRRO list in the packet.
        - IsSendingAsRro (bool): If true, send this as a RRO. True only if emulation type is RSVP-TE P2MP.
        - IsSendingAsSrro (bool): If true, send this as a SRRO. Note that both Send as RRO and Send as SRRO can be selected at the same time if so required by the user. True only if emulation type is RSVP-TE P2MP.
        - P2mpId (str): The P2MP id represented in IP address format.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Behavior=None,
        EmulationType=None,
        EnableReplyingLspPing=None,
        Enabled=None,
        IpAddressFrom=None,
        IpCount=None,
        IsConnectedIpAppended=None,
        IsHeadIpPrepended=None,
        IsLeafIpPrepended=None,
        IsSendingAsRro=None,
        IsSendingAsSrro=None,
        P2mpId=None,
    ):
        # type: (str, str, bool, bool, str, int, bool, bool, bool, bool, bool, str) -> DestinationRange
        """Adds a new destinationRange resource on the server and adds it to the container.

        Args
        ----
        - Behavior (str(ingress | egress)): Indicates whether the destination range corresponds to an Ingress or Egress router.
        - EmulationType (str(reserved | rsvpTe | rsvpTeP2mP)): The emulation type selected, the values being RSVP-TE, RSVP-TE P2MP.
        - EnableReplyingLspPing (bool): NOT DEFINED
        - Enabled (bool): Enables or disables the use of the destination range.
        - IpAddressFrom (str): The IP address of the first destination router.
        - IpCount (number): The number of destination routers. Each router's address is one greater than the previous one's.
        - IsConnectedIpAppended (bool): Append the connected IP as RRO/SRRO subobject at the end of the RRo/SRRO list in the packet.
        - IsHeadIpPrepended (bool): If true, prepend the tunnel head IP as a RRO/SERO subobject at the beginning of the RRO/SRRO list in the packet.
        - IsLeafIpPrepended (bool): If true, prepend the tunnel leaf IP as a RRO/SRRO subobject at the beginning of the RRO/SRRO list in the packet.
        - IsSendingAsRro (bool): If true, send this as a RRO. True only if emulation type is RSVP-TE P2MP.
        - IsSendingAsSrro (bool): If true, send this as a SRRO. Note that both Send as RRO and Send as SRRO can be selected at the same time if so required by the user. True only if emulation type is RSVP-TE P2MP.
        - P2mpId (str): The P2MP id represented in IP address format.

        Returns
        -------
        - self: This instance with all currently retrieved destinationRange resources using find and the newly added destinationRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained destinationRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Behavior=None,
        EmulationType=None,
        EnableReplyingLspPing=None,
        Enabled=None,
        IpAddressFrom=None,
        IpCount=None,
        IsConnectedIpAppended=None,
        IsHeadIpPrepended=None,
        IsLeafIpPrepended=None,
        IsSendingAsRro=None,
        IsSendingAsSrro=None,
        P2mpId=None,
    ):
        # type: (str, str, bool, bool, str, int, bool, bool, bool, bool, bool, str) -> DestinationRange
        """Finds and retrieves destinationRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve destinationRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all destinationRange resources from the server.

        Args
        ----
        - Behavior (str(ingress | egress)): Indicates whether the destination range corresponds to an Ingress or Egress router.
        - EmulationType (str(reserved | rsvpTe | rsvpTeP2mP)): The emulation type selected, the values being RSVP-TE, RSVP-TE P2MP.
        - EnableReplyingLspPing (bool): NOT DEFINED
        - Enabled (bool): Enables or disables the use of the destination range.
        - IpAddressFrom (str): The IP address of the first destination router.
        - IpCount (number): The number of destination routers. Each router's address is one greater than the previous one's.
        - IsConnectedIpAppended (bool): Append the connected IP as RRO/SRRO subobject at the end of the RRo/SRRO list in the packet.
        - IsHeadIpPrepended (bool): If true, prepend the tunnel head IP as a RRO/SERO subobject at the beginning of the RRO/SRRO list in the packet.
        - IsLeafIpPrepended (bool): If true, prepend the tunnel leaf IP as a RRO/SRRO subobject at the beginning of the RRO/SRRO list in the packet.
        - IsSendingAsRro (bool): If true, send this as a RRO. True only if emulation type is RSVP-TE P2MP.
        - IsSendingAsSrro (bool): If true, send this as a SRRO. Note that both Send as RRO and Send as SRRO can be selected at the same time if so required by the user. True only if emulation type is RSVP-TE P2MP.
        - P2mpId (str): The P2MP id represented in IP address format.

        Returns
        -------
        - self: This instance with matching destinationRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of destinationRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the destinationRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
