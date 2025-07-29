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


class LearnedInfoUpdate(Base):
    """The learned information trigger node that contains trigger tables of learned information.
    The LearnedInfoUpdate class encapsulates a list of learnedInfoUpdate resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedInfoUpdate.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "learnedInfoUpdate"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LearnedInfoUpdate, self).__init__(parent, list_op)

    @property
    def PceBasicRsvpSyncLspUpdateParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicrsvpsynclspupdateparams_6eef9dc1a488da175ab4c3b99257d713.PceBasicRsvpSyncLspUpdateParams): An instance of the PceBasicRsvpSyncLspUpdateParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicrsvpsynclspupdateparams_6eef9dc1a488da175ab4c3b99257d713 import (
            PceBasicRsvpSyncLspUpdateParams,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("PceBasicRsvpSyncLspUpdateParams", None)
                is not None
            ):
                return self._properties.get("PceBasicRsvpSyncLspUpdateParams")
        return PceBasicRsvpSyncLspUpdateParams(self)

    @property
    def PceBasicSrSyncLspUpdateParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrsynclspupdateparams_839812d760e58fe174a298d562594b9c.PceBasicSrSyncLspUpdateParams): An instance of the PceBasicSrSyncLspUpdateParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrsynclspupdateparams_839812d760e58fe174a298d562594b9c import (
            PceBasicSrSyncLspUpdateParams,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PceBasicSrSyncLspUpdateParams", None) is not None:
                return self._properties.get("PceBasicSrSyncLspUpdateParams")
        return PceBasicSrSyncLspUpdateParams(self)

    @property
    def PceBasicSrv6SyncLspUpdateParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrv6synclspupdateparams_b175f83a2c05b15420a2cf0686935a06.PceBasicSrv6SyncLspUpdateParams): An instance of the PceBasicSrv6SyncLspUpdateParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrv6synclspupdateparams_b175f83a2c05b15420a2cf0686935a06 import (
            PceBasicSrv6SyncLspUpdateParams,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("PceBasicSrv6SyncLspUpdateParams", None)
                is not None
            ):
                return self._properties.get("PceBasicSrv6SyncLspUpdateParams")
        return PceBasicSrv6SyncLspUpdateParams(self)

    @property
    def PceDetailedRsvpSyncLspUpdateParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedrsvpsynclspupdateparams_5359566e935ff47ef6207bf169bfaeaa.PceDetailedRsvpSyncLspUpdateParams): An instance of the PceDetailedRsvpSyncLspUpdateParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedrsvpsynclspupdateparams_5359566e935ff47ef6207bf169bfaeaa import (
            PceDetailedRsvpSyncLspUpdateParams,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("PceDetailedRsvpSyncLspUpdateParams", None)
                is not None
            ):
                return self._properties.get("PceDetailedRsvpSyncLspUpdateParams")
        return PceDetailedRsvpSyncLspUpdateParams(self)

    @property
    def PceDetailedSrSyncLspUpdateParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrsynclspupdateparams_41ca7e6032359598f9db7d1ff0f1d198.PceDetailedSrSyncLspUpdateParams): An instance of the PceDetailedSrSyncLspUpdateParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrsynclspupdateparams_41ca7e6032359598f9db7d1ff0f1d198 import (
            PceDetailedSrSyncLspUpdateParams,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("PceDetailedSrSyncLspUpdateParams", None)
                is not None
            ):
                return self._properties.get("PceDetailedSrSyncLspUpdateParams")
        return PceDetailedSrSyncLspUpdateParams(self)

    @property
    def PceDetailedSrv6SyncLspUpdateParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrv6synclspupdateparams_d75fffd280181810b452064aa4da1d72.PceDetailedSrv6SyncLspUpdateParams): An instance of the PceDetailedSrv6SyncLspUpdateParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrv6synclspupdateparams_d75fffd280181810b452064aa4da1d72 import (
            PceDetailedSrv6SyncLspUpdateParams,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("PceDetailedSrv6SyncLspUpdateParams", None)
                is not None
            ):
                return self._properties.get("PceDetailedSrv6SyncLspUpdateParams")
        return PceDetailedSrv6SyncLspUpdateParams(self)

    def add(self):
        """Adds a new learnedInfoUpdate resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved learnedInfoUpdate resources using find and the newly added learnedInfoUpdate resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self):
        """Finds and retrieves learnedInfoUpdate resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedInfoUpdate resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedInfoUpdate resources from the server.

        Returns
        -------
        - self: This instance with matching learnedInfoUpdate resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedInfoUpdate data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedInfoUpdate resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (bool):
        - Arg3 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def PerformActionOnAllObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the performActionOnAllObjects operation on the server.

        Action on All Objects

        performActionOnAllObjects(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------------
        - Arg2 (str): Action Name
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

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
            "performActionOnAllObjects", payload=payload, response_object=None
        )
