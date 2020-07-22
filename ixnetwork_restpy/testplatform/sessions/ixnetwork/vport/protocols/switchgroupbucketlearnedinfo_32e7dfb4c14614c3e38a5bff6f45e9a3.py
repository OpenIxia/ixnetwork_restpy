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


class SwitchGroupBucketLearnedInfo(Base):
    """NOT DEFINED
    The SwitchGroupBucketLearnedInfo class encapsulates a list of switchGroupBucketLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchGroupBucketLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchGroupBucketLearnedInfo'
    _SDM_ATT_MAP = {
        'ByteCount': 'byteCount',
        'PacketCount': 'packetCount',
        'WatchGroup': 'watchGroup',
        'WatchPort': 'watchPort',
        'Weight': 'weight',
    }

    def __init__(self, parent):
        super(SwitchGroupBucketLearnedInfo, self).__init__(parent)

    @property
    def SwitchGroupActionLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgroupactionlearnedinfo_a4e29e2ee24ace112adb66bbe5661cd3.SwitchGroupActionLearnedInfo): An instance of the SwitchGroupActionLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgroupactionlearnedinfo_a4e29e2ee24ace112adb66bbe5661cd3 import SwitchGroupActionLearnedInfo
        return SwitchGroupActionLearnedInfo(self)

    @property
    def ByteCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ByteCount'])

    @property
    def PacketCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketCount'])

    @property
    def WatchGroup(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['WatchGroup'])

    @property
    def WatchPort(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['WatchPort'])

    @property
    def Weight(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Weight'])

    def find(self, ByteCount=None, PacketCount=None, WatchGroup=None, WatchPort=None, Weight=None):
        """Finds and retrieves switchGroupBucketLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchGroupBucketLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchGroupBucketLearnedInfo resources from the server.

        Args
        ----
        - ByteCount (number): NOT DEFINED
        - PacketCount (number): NOT DEFINED
        - WatchGroup (number): NOT DEFINED
        - WatchPort (number): NOT DEFINED
        - Weight (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching switchGroupBucketLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchGroupBucketLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchGroupBucketLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
