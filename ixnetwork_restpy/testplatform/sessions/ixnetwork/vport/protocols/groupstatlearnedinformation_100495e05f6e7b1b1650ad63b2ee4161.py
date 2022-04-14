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


class GroupStatLearnedInformation(Base):
    """NOT DEFINED
    The GroupStatLearnedInformation class encapsulates a list of groupStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the GroupStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "groupStatLearnedInformation"
    _SDM_ATT_MAP = {
        "ByteCount": "byteCount",
        "DataPathId": "dataPathId",
        "DataPathIdAsHex": "dataPathIdAsHex",
        "DurationInNSec": "durationInNSec",
        "DurationInSec": "durationInSec",
        "ErrorCode": "errorCode",
        "ErrorType": "errorType",
        "GroupId": "groupId",
        "Latency": "latency",
        "LocalIp": "localIp",
        "NegotiatedVersion": "negotiatedVersion",
        "NumberOfBucketStats": "numberOfBucketStats",
        "PacketCount": "packetCount",
        "ReferenceCount": "referenceCount",
        "RemoteIp": "remoteIp",
        "ReplyState": "replyState",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(GroupStatLearnedInformation, self).__init__(parent, list_op)

    @property
    def GroupStatBucketLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupstatbucketlearnedinformation_4457768602bbf2c9ed3e3e2bb1a30d7c.GroupStatBucketLearnedInformation): An instance of the GroupStatBucketLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupstatbucketlearnedinformation_4457768602bbf2c9ed3e3e2bb1a30d7c import (
            GroupStatBucketLearnedInformation,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("GroupStatBucketLearnedInformation", None)
                is not None
            ):
                return self._properties.get("GroupStatBucketLearnedInformation")
        return GroupStatBucketLearnedInformation(self)

    @property
    def ByteCount(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ByteCount"])

    @property
    def DataPathId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathId"])

    @property
    def DataPathIdAsHex(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataPathIdAsHex"])

    @property
    def DurationInNSec(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DurationInNSec"])

    @property
    def DurationInSec(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DurationInSec"])

    @property
    def ErrorCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorCode"])

    @property
    def ErrorType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorType"])

    @property
    def GroupId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupId"])

    @property
    def Latency(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Latency"])

    @property
    def LocalIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalIp"])

    @property
    def NegotiatedVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegotiatedVersion"])

    @property
    def NumberOfBucketStats(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfBucketStats"])

    @property
    def PacketCount(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketCount"])

    @property
    def ReferenceCount(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReferenceCount"])

    @property
    def RemoteIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteIp"])

    @property
    def ReplyState(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReplyState"])

    def add(self):
        """Adds a new groupStatLearnedInformation resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved groupStatLearnedInformation resources using find and the newly added groupStatLearnedInformation resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ByteCount=None,
        DataPathId=None,
        DataPathIdAsHex=None,
        DurationInNSec=None,
        DurationInSec=None,
        ErrorCode=None,
        ErrorType=None,
        GroupId=None,
        Latency=None,
        LocalIp=None,
        NegotiatedVersion=None,
        NumberOfBucketStats=None,
        PacketCount=None,
        ReferenceCount=None,
        RemoteIp=None,
        ReplyState=None,
    ):
        # type: (str, str, str, str, str, str, str, str, int, str, str, str, str, str, str, str) -> GroupStatLearnedInformation
        """Finds and retrieves groupStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve groupStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all groupStatLearnedInformation resources from the server.

        Args
        ----
        - ByteCount (str): NOT DEFINED
        - DataPathId (str): NOT DEFINED
        - DataPathIdAsHex (str): NOT DEFINED
        - DurationInNSec (str): NOT DEFINED
        - DurationInSec (str): NOT DEFINED
        - ErrorCode (str): NOT DEFINED
        - ErrorType (str): NOT DEFINED
        - GroupId (str): NOT DEFINED
        - Latency (number): NOT DEFINED
        - LocalIp (str): NOT DEFINED
        - NegotiatedVersion (str): NOT DEFINED
        - NumberOfBucketStats (str): NOT DEFINED
        - PacketCount (str): NOT DEFINED
        - ReferenceCount (str): NOT DEFINED
        - RemoteIp (str): NOT DEFINED
        - ReplyState (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching groupStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of groupStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the groupStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
