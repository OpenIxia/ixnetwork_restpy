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


class PortStatusMaskSlave(Base):
    """As ports are added, modified, and removed from the datapath, the controller needs to be informed. But it may get no response from the Controller based on what the asynchronous message contains.
    The PortStatusMaskSlave class encapsulates a required portStatusMaskSlave resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "portStatusMaskSlave"
    _SDM_ATT_MAP = {
        "PortAdd": "portAdd",
        "PortDelete": "portDelete",
        "PortModify": "portModify",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PortStatusMaskSlave, self).__init__(parent, list_op)

    @property
    def PortAdd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This indicates that a port is added.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortAdd"])

    @PortAdd.setter
    def PortAdd(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortAdd"], value)

    @property
    def PortDelete(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This indicates that a port is removed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortDelete"])

    @PortDelete.setter
    def PortDelete(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortDelete"], value)

    @property
    def PortModify(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This indicates that some attributes of the port is changed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortModify"])

    @PortModify.setter
    def PortModify(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortModify"], value)

    def update(self, PortAdd=None, PortDelete=None, PortModify=None):
        # type: (bool, bool, bool) -> PortStatusMaskSlave
        """Updates portStatusMaskSlave resource on the server.

        Args
        ----
        - PortAdd (bool): This indicates that a port is added.
        - PortDelete (bool): This indicates that a port is removed.
        - PortModify (bool): This indicates that some attributes of the port is changed.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, PortAdd=None, PortDelete=None, PortModify=None):
        # type: (bool, bool, bool) -> PortStatusMaskSlave
        """Finds and retrieves portStatusMaskSlave resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve portStatusMaskSlave resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all portStatusMaskSlave resources from the server.

        Args
        ----
        - PortAdd (bool): This indicates that a port is added.
        - PortDelete (bool): This indicates that a port is removed.
        - PortModify (bool): This indicates that some attributes of the port is changed.

        Returns
        -------
        - self: This instance with matching portStatusMaskSlave resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of portStatusMaskSlave data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the portStatusMaskSlave resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
