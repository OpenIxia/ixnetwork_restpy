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


class NextHopInfo(Base):
    """(Read Only) List of next hops learned.
    The NextHopInfo class encapsulates a list of nextHopInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the NextHopInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "nextHopInfo"
    _SDM_ATT_MAP = {
        "NextHop": "nextHop",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(NextHopInfo, self).__init__(parent, list_op)

    @property
    def RdInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rdinfo_4880f052fc533ebf0339e97b80d3331e.RdInfo): An instance of the RdInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rdinfo_4880f052fc533ebf0339e97b80d3331e import (
            RdInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RdInfo", None) is not None:
                return self._properties.get("RdInfo")
        return RdInfo(self)

    @property
    def NextHop(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read Only) Next Hop IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NextHop"])

    def add(self):
        """Adds a new nextHopInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved nextHopInfo resources using find and the newly added nextHopInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, NextHop=None):
        # type: (str) -> NextHopInfo
        """Finds and retrieves nextHopInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve nextHopInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all nextHopInfo resources from the server.

        Args
        ----
        - NextHop (str): (Read Only) Next Hop IP.

        Returns
        -------
        - self: This instance with matching nextHopInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of nextHopInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the nextHopInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
