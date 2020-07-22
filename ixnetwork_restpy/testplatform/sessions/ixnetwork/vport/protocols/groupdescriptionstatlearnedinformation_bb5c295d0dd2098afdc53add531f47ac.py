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


class GroupDescriptionStatLearnedInformation(Base):
    """NOT DEFINED
    The GroupDescriptionStatLearnedInformation class encapsulates a list of groupDescriptionStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the GroupDescriptionStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'groupDescriptionStatLearnedInformation'
    _SDM_ATT_MAP = {
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'GroupId': 'groupId',
        'GroupType': 'groupType',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'NegotiatedVersion': 'negotiatedVersion',
        'NumberOfBucketStats': 'numberOfBucketStats',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
    }

    def __init__(self, parent):
        super(GroupDescriptionStatLearnedInformation, self).__init__(parent)

    @property
    def GroupBucketDescStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupbucketdescstatlearnedinformation_0a611371603afa4711776c39f57d8487.GroupBucketDescStatLearnedInformation): An instance of the GroupBucketDescStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupbucketdescstatlearnedinformation_0a611371603afa4711776c39f57d8487 import GroupBucketDescStatLearnedInformation
        return GroupBucketDescStatLearnedInformation(self)

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: The Data Path ID of the connected switch.
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
    def ErrorCode(self):
        """
        Returns
        -------
        - str: The error code of the error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorCode'])

    @property
    def ErrorType(self):
        """
        Returns
        -------
        - str: The type of the error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorType'])

    @property
    def GroupId(self):
        """
        Returns
        -------
        - number: A 32-bit integer uniquely identifying the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupId'])

    @property
    def GroupType(self):
        """
        Returns
        -------
        - str: Specify the group types supported by Switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupType'])

    @property
    def Latency(self):
        """
        Returns
        -------
        - number: The latency measurement for the OpenFlow channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Latency'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: The local IP address of the selected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: The OpenFlow version supported by this configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

    @property
    def NumberOfBucketStats(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfBucketStats'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: The Remote IP address of the selected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: The reply state of the OF Channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyState'])

    def find(self, DataPathId=None, DataPathIdAsHex=None, ErrorCode=None, ErrorType=None, GroupId=None, GroupType=None, Latency=None, LocalIp=None, NegotiatedVersion=None, NumberOfBucketStats=None, RemoteIp=None, ReplyState=None):
        """Finds and retrieves groupDescriptionStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve groupDescriptionStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all groupDescriptionStatLearnedInformation resources from the server.

        Args
        ----
        - DataPathId (str): The Data Path ID of the connected switch.
        - DataPathIdAsHex (str): The Data Path ID of the OpenFlow switch in hexadecimal format.
        - ErrorCode (str): The error code of the error received.
        - ErrorType (str): The type of the error received.
        - GroupId (number): A 32-bit integer uniquely identifying the group.
        - GroupType (str): Specify the group types supported by Switch.
        - Latency (number): The latency measurement for the OpenFlow channel.
        - LocalIp (str): The local IP address of the selected interface.
        - NegotiatedVersion (str): The OpenFlow version supported by this configuration.
        - NumberOfBucketStats (str): NOT DEFINED
        - RemoteIp (str): The Remote IP address of the selected interface.
        - ReplyState (str): The reply state of the OF Channel.

        Returns
        -------
        - self: This instance with matching groupDescriptionStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of groupDescriptionStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the groupDescriptionStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
