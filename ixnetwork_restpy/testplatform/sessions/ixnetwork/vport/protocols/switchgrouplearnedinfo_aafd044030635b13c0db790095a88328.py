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


class SwitchGroupLearnedInfo(Base):
    """NOT DEFINED
    The SwitchGroupLearnedInfo class encapsulates a list of switchGroupLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchGroupLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchGroupLearnedInfo'
    _SDM_ATT_MAP = {
        'ByteCount': 'byteCount',
        'DatapathId': 'datapathId',
        'DatapathIdInHex': 'datapathIdInHex',
        'Duration': 'duration',
        'DurationInNs': 'durationInNs',
        'GroupId': 'groupId',
        'GroupType': 'groupType',
        'LocalIp': 'localIp',
        'NegotiatedVersion': 'negotiatedVersion',
        'NumOfBuckets': 'numOfBuckets',
        'PacketCount': 'packetCount',
        'ReferenceCount': 'referenceCount',
    }

    def __init__(self, parent):
        super(SwitchGroupLearnedInfo, self).__init__(parent)

    @property
    def SwitchGroupBucketLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgroupbucketlearnedinfo_32e7dfb4c14614c3e38a5bff6f45e9a3.SwitchGroupBucketLearnedInfo): An instance of the SwitchGroupBucketLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgroupbucketlearnedinfo_32e7dfb4c14614c3e38a5bff6f45e9a3 import SwitchGroupBucketLearnedInfo
        return SwitchGroupBucketLearnedInfo(self)

    @property
    def ByteCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ByteCount'])

    @property
    def DatapathId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DatapathId'])

    @property
    def DatapathIdInHex(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DatapathIdInHex'])

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])

    @property
    def DurationInNs(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['DurationInNs'])

    @property
    def GroupId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupId'])

    @property
    def GroupType(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupType'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

    @property
    def NumOfBuckets(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumOfBuckets'])

    @property
    def PacketCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketCount'])

    @property
    def ReferenceCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReferenceCount'])

    def find(self, ByteCount=None, DatapathId=None, DatapathIdInHex=None, Duration=None, DurationInNs=None, GroupId=None, GroupType=None, LocalIp=None, NegotiatedVersion=None, NumOfBuckets=None, PacketCount=None, ReferenceCount=None):
        """Finds and retrieves switchGroupLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchGroupLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchGroupLearnedInfo resources from the server.

        Args
        ----
        - ByteCount (number): NOT DEFINED
        - DatapathId (str): NOT DEFINED
        - DatapathIdInHex (str): NOT DEFINED
        - Duration (number): NOT DEFINED
        - DurationInNs (number): NOT DEFINED
        - GroupId (number): NOT DEFINED
        - GroupType (str): NOT DEFINED
        - LocalIp (str): NOT DEFINED
        - NegotiatedVersion (str): NOT DEFINED
        - NumOfBuckets (number): NOT DEFINED
        - PacketCount (number): NOT DEFINED
        - ReferenceCount (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching switchGroupLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchGroupLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchGroupLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
