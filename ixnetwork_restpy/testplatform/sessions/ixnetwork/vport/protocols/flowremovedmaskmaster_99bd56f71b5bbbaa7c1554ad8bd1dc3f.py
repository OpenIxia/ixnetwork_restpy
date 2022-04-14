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


class FlowRemovedMaskMaster(Base):
    """When flow entries time out or are deleted from tables, the controller is notified. But it may get no response from the Controller based on what the asynchronous message contains
    The FlowRemovedMaskMaster class encapsulates a required flowRemovedMaskMaster resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "flowRemovedMaskMaster"
    _SDM_ATT_MAP = {
        "Delete": "delete",
        "GroupDelete": "groupDelete",
        "HardTimeout": "hardTimeout",
        "IdleTimeout": "idleTimeout",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(FlowRemovedMaskMaster, self).__init__(parent, list_op)

    @property
    def Delete(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This indicates that flow entry is evicted by a delete Flow Mod message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Delete"])

    @Delete.setter
    def Delete(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Delete"], value)

    @property
    def GroupDelete(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This indicates that the group is removed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupDelete"])

    @GroupDelete.setter
    def GroupDelete(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupDelete"], value)

    @property
    def HardTimeout(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This indicates that Flow idle time exceeded hard timeout.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HardTimeout"])

    @HardTimeout.setter
    def HardTimeout(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HardTimeout"], value)

    @property
    def IdleTimeout(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This indicates that Flow idle time exceeded idle timeout.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IdleTimeout"])

    @IdleTimeout.setter
    def IdleTimeout(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IdleTimeout"], value)

    def update(self, Delete=None, GroupDelete=None, HardTimeout=None, IdleTimeout=None):
        # type: (bool, bool, bool, bool) -> FlowRemovedMaskMaster
        """Updates flowRemovedMaskMaster resource on the server.

        Args
        ----
        - Delete (bool): This indicates that flow entry is evicted by a delete Flow Mod message.
        - GroupDelete (bool): This indicates that the group is removed.
        - HardTimeout (bool): This indicates that Flow idle time exceeded hard timeout.
        - IdleTimeout (bool): This indicates that Flow idle time exceeded idle timeout.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Delete=None, GroupDelete=None, HardTimeout=None, IdleTimeout=None):
        # type: (bool, bool, bool, bool) -> FlowRemovedMaskMaster
        """Finds and retrieves flowRemovedMaskMaster resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve flowRemovedMaskMaster resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all flowRemovedMaskMaster resources from the server.

        Args
        ----
        - Delete (bool): This indicates that flow entry is evicted by a delete Flow Mod message.
        - GroupDelete (bool): This indicates that the group is removed.
        - HardTimeout (bool): This indicates that Flow idle time exceeded hard timeout.
        - IdleTimeout (bool): This indicates that Flow idle time exceeded idle timeout.

        Returns
        -------
        - self: This instance with matching flowRemovedMaskMaster resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of flowRemovedMaskMaster data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the flowRemovedMaskMaster resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
