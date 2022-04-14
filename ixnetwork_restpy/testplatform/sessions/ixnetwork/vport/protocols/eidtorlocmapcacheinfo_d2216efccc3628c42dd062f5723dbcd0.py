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


class EidToRlocMapCacheInfo(Base):
    """It gives details about the eid to rloc map cache information
    The EidToRlocMapCacheInfo class encapsulates a list of eidToRlocMapCacheInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the EidToRlocMapCacheInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "eidToRlocMapCacheInfo"
    _SDM_ATT_MAP = {
        "Action": "action",
        "ExpiresAfter": "expiresAfter",
        "InstanceId": "instanceId",
        "MapReplyRx": "mapReplyRx",
        "MapRequestTx": "mapRequestTx",
        "MapVersionNumber": "mapVersionNumber",
        "NegativeMapReplyRx": "negativeMapReplyRx",
        "RemoteEidMappingStatus": "remoteEidMappingStatus",
        "RemoteEidPrefix": "remoteEidPrefix",
        "RemoteEidPrefixAfi": "remoteEidPrefixAfi",
        "RemoteEidPrefixLength": "remoteEidPrefixLength",
        "ResponderIp": "responderIp",
        "RlocProbeReplyRx": "rlocProbeReplyRx",
        "RlocProbeRequestTx": "rlocProbeRequestTx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(EidToRlocMapCacheInfo, self).__init__(parent, list_op)

    @property
    def RemoteLocators(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.remotelocators_69a782e2029768935eb54ff9c03fbc3d.RemoteLocators): An instance of the RemoteLocators class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.remotelocators_69a782e2029768935eb54ff9c03fbc3d import (
            RemoteLocators,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RemoteLocators", None) is not None:
                return self._properties.get("RemoteLocators")
        return RemoteLocators(self)

    @property
    def Action(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It gives details about the action (Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Action"])

    @property
    def ExpiresAfter(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It gives details about the expiration (Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExpiresAfter"])

    @property
    def InstanceId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the instance id (Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["InstanceId"])

    @property
    def MapReplyRx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the Map reply at the receivers end (Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapReplyRx"])

    @property
    def MapRequestTx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the Map request at the transmitters end (Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapRequestTx"])

    @property
    def MapVersionNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about map version number(Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapVersionNumber"])

    @property
    def NegativeMapReplyRx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the Map reply at the receivers end in negation (Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegativeMapReplyRx"])

    @property
    def RemoteEidMappingStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It gives details about the remote Eid mapping status (Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteEidMappingStatus"])

    @property
    def RemoteEidPrefix(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It gives details about the remote Eid Prefix (Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteEidPrefix"])

    @property
    def RemoteEidPrefixAfi(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It gives details about the remote Eid Prefix Afi(Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteEidPrefixAfi"])

    @property
    def RemoteEidPrefixLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the remote Eid Prefix Length(Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteEidPrefixLength"])

    @property
    def ResponderIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It gives details about the responder Ip (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResponderIp"])

    @property
    def RlocProbeReplyRx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the rloc Probe Reply at receivers end(Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RlocProbeReplyRx"])

    @property
    def RlocProbeRequestTx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It gives details about the rloc Probe Reply at transmitters end(Read-only)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RlocProbeRequestTx"])

    def add(self):
        """Adds a new eidToRlocMapCacheInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved eidToRlocMapCacheInfo resources using find and the newly added eidToRlocMapCacheInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Action=None,
        ExpiresAfter=None,
        InstanceId=None,
        MapReplyRx=None,
        MapRequestTx=None,
        MapVersionNumber=None,
        NegativeMapReplyRx=None,
        RemoteEidMappingStatus=None,
        RemoteEidPrefix=None,
        RemoteEidPrefixAfi=None,
        RemoteEidPrefixLength=None,
        ResponderIp=None,
        RlocProbeReplyRx=None,
        RlocProbeRequestTx=None,
    ):
        # type: (str, str, int, int, int, int, int, str, str, str, int, str, int, int) -> EidToRlocMapCacheInfo
        """Finds and retrieves eidToRlocMapCacheInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve eidToRlocMapCacheInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all eidToRlocMapCacheInfo resources from the server.

        Args
        ----
        - Action (str): It gives details about the action (Read-only)
        - ExpiresAfter (str): It gives details about the expiration (Read-only)
        - InstanceId (number): It gives details about the instance id (Read-only)
        - MapReplyRx (number): It gives details about the Map reply at the receivers end (Read-only)
        - MapRequestTx (number): It gives details about the Map request at the transmitters end (Read-only)
        - MapVersionNumber (number): It gives details about map version number(Read-Only)
        - NegativeMapReplyRx (number): It gives details about the Map reply at the receivers end in negation (Read-only)
        - RemoteEidMappingStatus (str): It gives details about the remote Eid mapping status (Read-only)
        - RemoteEidPrefix (str): It gives details about the remote Eid Prefix (Read-only)
        - RemoteEidPrefixAfi (str): It gives details about the remote Eid Prefix Afi(Read-only)
        - RemoteEidPrefixLength (number): It gives details about the remote Eid Prefix Length(Read-only)
        - ResponderIp (str): It gives details about the responder Ip (Read-Only)
        - RlocProbeReplyRx (number): It gives details about the rloc Probe Reply at receivers end(Read-only)
        - RlocProbeRequestTx (number): It gives details about the rloc Probe Reply at transmitters end(Read-only)

        Returns
        -------
        - self: This instance with matching eidToRlocMapCacheInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of eidToRlocMapCacheInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the eidToRlocMapCacheInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
