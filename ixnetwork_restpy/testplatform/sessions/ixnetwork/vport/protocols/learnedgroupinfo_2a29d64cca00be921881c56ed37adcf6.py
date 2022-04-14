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


class LearnedGroupInfo(Base):
    """This object contains the learned information for IGMP queriers.
    The LearnedGroupInfo class encapsulates a list of learnedGroupInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedGroupInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "learnedGroupInfo"
    _SDM_ATT_MAP = {
        "CompatibilityMode": "compatibilityMode",
        "CompatibilityTimer": "compatibilityTimer",
        "FilterMode": "filterMode",
        "GroupAddress": "groupAddress",
        "GroupTimer": "groupTimer",
        "SourceAddress": "sourceAddress",
        "SourceTimer": "sourceTimer",
    }
    _SDM_ENUM_MAP = {
        "compatibilityMode": ["igmpv1", "igmpv2", "igmpv3"],
        "filterMode": ["include", "exclude"],
    }

    def __init__(self, parent, list_op=False):
        super(LearnedGroupInfo, self).__init__(parent, list_op)

    @property
    def CompatibilityMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(igmpv1 | igmpv2 | igmpv3): (read only) The IGMP version compatibility mode of the IGMP querier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CompatibilityMode"])

    @property
    def CompatibilityTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The number of seconds remaining in the compatibility timer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CompatibilityTimer"])

    @property
    def FilterMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(include | exclude): (read only) Displays the filter mode of the querier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FilterMode"])

    @property
    def GroupAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The IPv4 address for the multicast group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupAddress"])

    @property
    def GroupTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The number of seconds remaining in the group address timer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupTimer"])

    @property
    def SourceAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The source IP addresses from which the host receives messages for this multicast group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceAddress"])

    @property
    def SourceTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The number of seconds remaining in the source address timer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceTimer"])

    def add(self):
        """Adds a new learnedGroupInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved learnedGroupInfo resources using find and the newly added learnedGroupInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CompatibilityMode=None,
        CompatibilityTimer=None,
        FilterMode=None,
        GroupAddress=None,
        GroupTimer=None,
        SourceAddress=None,
        SourceTimer=None,
    ):
        # type: (str, int, str, str, int, str, int) -> LearnedGroupInfo
        """Finds and retrieves learnedGroupInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedGroupInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedGroupInfo resources from the server.

        Args
        ----
        - CompatibilityMode (str(igmpv1 | igmpv2 | igmpv3)): (read only) The IGMP version compatibility mode of the IGMP querier.
        - CompatibilityTimer (number): (read only) The number of seconds remaining in the compatibility timer.
        - FilterMode (str(include | exclude)): (read only) Displays the filter mode of the querier.
        - GroupAddress (str): (read only) The IPv4 address for the multicast group.
        - GroupTimer (number): (read only) The number of seconds remaining in the group address timer.
        - SourceAddress (str): (read only) The source IP addresses from which the host receives messages for this multicast group.
        - SourceTimer (number): (read only) The number of seconds remaining in the source address timer.

        Returns
        -------
        - self: This instance with matching learnedGroupInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedGroupInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedGroupInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
