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


class MeshPatternRing(Base):
    """Implements Ring meshing
    The MeshPatternRing class encapsulates a list of MeshPatternRing resources that are managed by the user.
    A list of resources can be retrieved from the server using the MeshPatternRing.find() method.
    The list can be managed by using the MeshPatternRing.add() and MeshPatternRing.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "MeshPatternRing"
    _SDM_ATT_MAP = {
        "Bidirectional": "bidirectional",
        "Name": "name",
        "RemoteEndpointCount": "remoteEndpointCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(MeshPatternRing, self).__init__(parent, list_op)

    @property
    def Endpoints(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.meshing.patterns.meshpatternring.endpoints.endpoints.Endpoints): An instance of the Endpoints class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.meshing.patterns.meshpatternring.endpoints.endpoints import (
            Endpoints,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Endpoints", None) is not None:
                return self._properties.get("Endpoints")
        return Endpoints(self)

    @property
    def Bidirectional(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Generate flows in both directions.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Bidirectional"])

    @Bidirectional.setter
    def Bidirectional(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Bidirectional"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique name of the global pattern.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def RemoteEndpointCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of remote endpoints.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteEndpointCount"])

    def update(self, Bidirectional=None, Name=None):
        # type: (bool, str) -> MeshPatternRing
        """Updates MeshPatternRing resource on the server.

        Args
        ----
        - Bidirectional (bool): Generate flows in both directions.
        - Name (str): Unique name of the global pattern.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Bidirectional=None, Name=None):
        # type: (bool, str) -> MeshPatternRing
        """Adds a new MeshPatternRing resource on the server and adds it to the container.

        Args
        ----
        - Bidirectional (bool): Generate flows in both directions.
        - Name (str): Unique name of the global pattern.

        Returns
        -------
        - self: This instance with all currently retrieved MeshPatternRing resources using find and the newly added MeshPatternRing resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained MeshPatternRing resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Bidirectional=None, Name=None, RemoteEndpointCount=None):
        # type: (bool, str, int) -> MeshPatternRing
        """Finds and retrieves MeshPatternRing resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve MeshPatternRing resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all MeshPatternRing resources from the server.

        Args
        ----
        - Bidirectional (bool): Generate flows in both directions.
        - Name (str): Unique name of the global pattern.
        - RemoteEndpointCount (number): Number of remote endpoints.

        Returns
        -------
        - self: This instance with matching MeshPatternRing resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of MeshPatternRing data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the MeshPatternRing resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ClearOverlays(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearOverlays operation on the server.

        Revert all values changed by the user.

        clearOverlays(async_operation=bool)
        -----------------------------------
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
        return self._execute("clearOverlays", payload=payload, response_object=None)
