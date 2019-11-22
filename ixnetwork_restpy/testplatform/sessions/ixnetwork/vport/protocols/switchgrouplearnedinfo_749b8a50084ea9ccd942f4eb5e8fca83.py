# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class SwitchGroupLearnedInfo(Base):
    """NOT DEFINED
    The SwitchGroupLearnedInfo class encapsulates a list of switchGroupLearnedInfo resources that is managed by the system.
    A list of resources can be retrieved from the server using the SwitchGroupLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchGroupLearnedInfo'

    def __init__(self, parent):
        super(SwitchGroupLearnedInfo, self).__init__(parent)

    @property
    def SwitchGroupBucketLearnedInfo(self):
        """An instance of the SwitchGroupBucketLearnedInfo class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgroupbucketlearnedinfo_1a690be54303809914304eadeaa153bf.SwitchGroupBucketLearnedInfo)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgroupbucketlearnedinfo_1a690be54303809914304eadeaa153bf import SwitchGroupBucketLearnedInfo
        return SwitchGroupBucketLearnedInfo(self)

    @property
    def ByteCount(self):
        """NOT DEFINED

        Returns:
            number
        """
        return self._get_attribute('byteCount')

    @property
    def DatapathId(self):
        """NOT DEFINED

        Returns:
            str
        """
        return self._get_attribute('datapathId')

    @property
    def DatapathIdInHex(self):
        """NOT DEFINED

        Returns:
            str
        """
        return self._get_attribute('datapathIdInHex')

    @property
    def Duration(self):
        """NOT DEFINED

        Returns:
            number
        """
        return self._get_attribute('duration')

    @property
    def DurationInNs(self):
        """NOT DEFINED

        Returns:
            number
        """
        return self._get_attribute('durationInNs')

    @property
    def GroupId(self):
        """NOT DEFINED

        Returns:
            number
        """
        return self._get_attribute('groupId')

    @property
    def GroupType(self):
        """NOT DEFINED

        Returns:
            str
        """
        return self._get_attribute('groupType')

    @property
    def LocalIp(self):
        """NOT DEFINED

        Returns:
            str
        """
        return self._get_attribute('localIp')

    @property
    def NegotiatedVersion(self):
        """NOT DEFINED

        Returns:
            str
        """
        return self._get_attribute('negotiatedVersion')

    @property
    def NumOfBuckets(self):
        """NOT DEFINED

        Returns:
            number
        """
        return self._get_attribute('numOfBuckets')

    @property
    def PacketCount(self):
        """NOT DEFINED

        Returns:
            number
        """
        return self._get_attribute('packetCount')

    @property
    def ReferenceCount(self):
        """NOT DEFINED

        Returns:
            number
        """
        return self._get_attribute('referenceCount')

    def find(self, ByteCount=None, DatapathId=None, DatapathIdInHex=None, Duration=None, DurationInNs=None, GroupId=None, GroupType=None, LocalIp=None, NegotiatedVersion=None, NumOfBuckets=None, PacketCount=None, ReferenceCount=None):
        """Finds and retrieves switchGroupLearnedInfo data from the server.

        All named parameters support regex and can be used to selectively retrieve switchGroupLearnedInfo data from the server.
        By default the find method takes no parameters and will retrieve all switchGroupLearnedInfo data from the server.

        Args:
            ByteCount (number): NOT DEFINED
            DatapathId (str): NOT DEFINED
            DatapathIdInHex (str): NOT DEFINED
            Duration (number): NOT DEFINED
            DurationInNs (number): NOT DEFINED
            GroupId (number): NOT DEFINED
            GroupType (str): NOT DEFINED
            LocalIp (str): NOT DEFINED
            NegotiatedVersion (str): NOT DEFINED
            NumOfBuckets (number): NOT DEFINED
            PacketCount (number): NOT DEFINED
            ReferenceCount (number): NOT DEFINED

        Returns:
            self: This instance with matching switchGroupLearnedInfo data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of switchGroupLearnedInfo data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the switchGroupLearnedInfo data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
