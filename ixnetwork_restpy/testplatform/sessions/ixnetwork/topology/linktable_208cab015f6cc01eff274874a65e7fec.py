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


class LinkTable(Base):
    """Topology Link Table. sizes of fromNodeIndex and toNodeIndex are the same.
    The LinkTable class encapsulates a required linkTable resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "linkTable"
    _SDM_ATT_MAP = {
        "FromNodeIndex": "fromNodeIndex",
        "ToNodeIndex": "toNodeIndex",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LinkTable, self).__init__(parent, list_op)

    @property
    def FromNodeIndex(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): from node index.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FromNodeIndex"])

    @FromNodeIndex.setter
    def FromNodeIndex(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["FromNodeIndex"], value)

    @property
    def ToNodeIndex(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): to node index.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ToNodeIndex"])

    @ToNodeIndex.setter
    def ToNodeIndex(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["ToNodeIndex"], value)

    def update(self, FromNodeIndex=None, ToNodeIndex=None):
        # type: (List[str], List[str]) -> LinkTable
        """Updates linkTable resource on the server.

        Args
        ----
        - FromNodeIndex (list(str)): from node index.
        - ToNodeIndex (list(str)): to node index.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, FromNodeIndex=None, ToNodeIndex=None):
        # type: (List[str], List[str]) -> LinkTable
        """Finds and retrieves linkTable resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve linkTable resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all linkTable resources from the server.

        Args
        ----
        - FromNodeIndex (list(str)): from node index.
        - ToNodeIndex (list(str)): to node index.

        Returns
        -------
        - self: This instance with matching linkTable resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of linkTable data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the linkTable resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
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
