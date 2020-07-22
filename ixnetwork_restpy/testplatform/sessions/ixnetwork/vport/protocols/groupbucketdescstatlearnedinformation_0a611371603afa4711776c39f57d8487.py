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


class GroupBucketDescStatLearnedInformation(Base):
    """NOT DEFINED
    The GroupBucketDescStatLearnedInformation class encapsulates a list of groupBucketDescStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the GroupBucketDescStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'groupBucketDescStatLearnedInformation'
    _SDM_ATT_MAP = {
        'ActionCount': 'actionCount',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'GroupId': 'groupId',
        'LocalIp': 'localIp',
        'RemoteIp': 'remoteIp',
        'WatchGroup': 'watchGroup',
        'WatchPort': 'watchPort',
        'Weight': 'weight',
    }

    def __init__(self, parent):
        super(GroupBucketDescStatLearnedInformation, self).__init__(parent)

    @property
    def ActionCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActionCount'])

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: The Data Path ID of the OpenFlow switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: The Data Path ID of the OpenFlow switch in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def GroupId(self):
        """
        Returns
        -------
        - number: A 32-bit integer uniquely identifying the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupId'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: The Data Path ID of the OpenFlow switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: The Remote IP address of the selected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def WatchGroup(self):
        """
        Returns
        -------
        - number: A group whose state determines whether this bucket is live or not. Default value OFPG_ANY(4,294,967,295) indicates that Watch Group is not specified in ofp_group_mod packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WatchGroup'])

    @property
    def WatchPort(self):
        """
        Returns
        -------
        - number: A Port whose state determines whether this bucket is live or not. Default value OFPP_ANY(4,294,967,295) indicates that Watch Port is not specified in ofp_group_mod packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WatchPort'])

    @property
    def Weight(self):
        """
        Returns
        -------
        - number: Specify the weight of buckets. The range allowed is 0-65535.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Weight'])

    def find(self, ActionCount=None, DataPathId=None, DataPathIdAsHex=None, GroupId=None, LocalIp=None, RemoteIp=None, WatchGroup=None, WatchPort=None, Weight=None):
        """Finds and retrieves groupBucketDescStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve groupBucketDescStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all groupBucketDescStatLearnedInformation resources from the server.

        Args
        ----
        - ActionCount (number): NOT DEFINED
        - DataPathId (str): The Data Path ID of the OpenFlow switch.
        - DataPathIdAsHex (str): The Data Path ID of the OpenFlow switch in hexadecimal format.
        - GroupId (number): A 32-bit integer uniquely identifying the group.
        - LocalIp (str): The Data Path ID of the OpenFlow switch.
        - RemoteIp (str): The Remote IP address of the selected interface.
        - WatchGroup (number): A group whose state determines whether this bucket is live or not. Default value OFPG_ANY(4,294,967,295) indicates that Watch Group is not specified in ofp_group_mod packets.
        - WatchPort (number): A Port whose state determines whether this bucket is live or not. Default value OFPP_ANY(4,294,967,295) indicates that Watch Port is not specified in ofp_group_mod packets.
        - Weight (number): Specify the weight of buckets. The range allowed is 0-65535.

        Returns
        -------
        - self: This instance with matching groupBucketDescStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of groupBucketDescStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the groupBucketDescStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
