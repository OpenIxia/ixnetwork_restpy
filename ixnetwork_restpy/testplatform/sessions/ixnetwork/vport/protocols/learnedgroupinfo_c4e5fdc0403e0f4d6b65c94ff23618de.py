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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LearnedGroupInfo(Base):
    """This object contains the learned information for IGMP queriers.
    The LearnedGroupInfo class encapsulates a list of learnedGroupInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedGroupInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedGroupInfo'
    _SDM_ATT_MAP = {
        'CompatibilityMode': 'compatibilityMode',
        'CompatibilityTimer': 'compatibilityTimer',
        'FilterMode': 'filterMode',
        'GroupAddress': 'groupAddress',
        'GroupTimer': 'groupTimer',
        'SourceAddress': 'sourceAddress',
        'SourceTimer': 'sourceTimer',
    }

    def __init__(self, parent):
        super(LearnedGroupInfo, self).__init__(parent)

    @property
    def CompatibilityMode(self):
        """
        Returns
        -------
        - str(igmpv1 | igmpv2 | igmpv3): (read only) The IGMP version compatibility mode of the IGMP querier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CompatibilityMode'])

    @property
    def CompatibilityTimer(self):
        """
        Returns
        -------
        - number: (read only) The number of seconds remaining in the compatibility timer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CompatibilityTimer'])

    @property
    def FilterMode(self):
        """
        Returns
        -------
        - str(include | exclude): (read only) Displays the filter mode of the querier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FilterMode'])

    @property
    def GroupAddress(self):
        """
        Returns
        -------
        - str: (read only) The IPv4 address for the multicast group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupAddress'])

    @property
    def GroupTimer(self):
        """
        Returns
        -------
        - number: (read only) The number of seconds remaining in the group address timer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupTimer'])

    @property
    def SourceAddress(self):
        """
        Returns
        -------
        - str: (read only) The source IP addresses from which the host receives messages for this multicast group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAddress'])

    @property
    def SourceTimer(self):
        """
        Returns
        -------
        - number: (read only) The number of seconds remaining in the source address timer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceTimer'])

    def find(self, CompatibilityMode=None, CompatibilityTimer=None, FilterMode=None, GroupAddress=None, GroupTimer=None, SourceAddress=None, SourceTimer=None):
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
