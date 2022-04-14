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


class CistLearnedInfo(Base):
    """Learned information associated with a CIST on an (MSTP) stpBridge.
    The CistLearnedInfo class encapsulates a required cistLearnedInfo resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "cistLearnedInfo"
    _SDM_ATT_MAP = {
        "RegRootCost": "regRootCost",
        "RegRootMac": "regRootMac",
        "RegRootPriority": "regRootPriority",
        "RootCost": "rootCost",
        "RootMac": "rootMac",
        "RootPriority": "rootPriority",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(CistLearnedInfo, self).__init__(parent, list_op)

    @property
    def RegRootCost(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (Read-only) The cost for the shortest path from the advertising bridge to the regional root bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RegRootCost"])

    @property
    def RegRootMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read-only) The regional root MAC address being advertised by the bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RegRootMac"])

    @property
    def RegRootPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (Read-only) The regional root priority being advertised by the bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RegRootPriority"])

    @property
    def RootCost(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (Read-only) The cost for the shortest path from the advertising bridge to the root bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RootCost"])

    @property
    def RootMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read-only) The root bridge MAC address being advertised.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RootMac"])

    @property
    def RootPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (Read-only) The priority being advertised for the root bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RootPriority"])

    def find(
        self,
        RegRootCost=None,
        RegRootMac=None,
        RegRootPriority=None,
        RootCost=None,
        RootMac=None,
        RootPriority=None,
    ):
        # type: (int, str, int, int, str, int) -> CistLearnedInfo
        """Finds and retrieves cistLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cistLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cistLearnedInfo resources from the server.

        Args
        ----
        - RegRootCost (number): (Read-only) The cost for the shortest path from the advertising bridge to the regional root bridge.
        - RegRootMac (str): (Read-only) The regional root MAC address being advertised by the bridge.
        - RegRootPriority (number): (Read-only) The regional root priority being advertised by the bridge.
        - RootCost (number): (Read-only) The cost for the shortest path from the advertising bridge to the root bridge.
        - RootMac (str): (Read-only) The root bridge MAC address being advertised.
        - RootPriority (number): (Read-only) The priority being advertised for the root bridge.

        Returns
        -------
        - self: This instance with matching cistLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cistLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cistLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
