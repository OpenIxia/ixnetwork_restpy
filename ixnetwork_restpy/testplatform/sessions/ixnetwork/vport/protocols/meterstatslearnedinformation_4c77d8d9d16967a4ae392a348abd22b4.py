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


class MeterStatsLearnedInformation(Base):
    """NOT DEFINED
    The MeterStatsLearnedInformation class encapsulates a list of meterStatsLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the MeterStatsLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'meterStatsLearnedInformation'
    _SDM_ATT_MAP = {
        'ByteInCount': 'byteInCount',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'DurationNSec': 'durationNSec',
        'DurationSec': 'durationSec',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'FlowCount': 'flowCount',
        'LastErrorCode': 'lastErrorCode',
        'LastErrorType': 'lastErrorType',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'MeterId': 'meterId',
        'NegotiatedVersion': 'negotiatedVersion',
        'NumberOfBandStats': 'numberOfBandStats',
        'PacketInCount': 'packetInCount',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
    }

    def __init__(self, parent):
        super(MeterStatsLearnedInformation, self).__init__(parent)

    @property
    def MeterStatsBandLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterstatsbandlearnedinformation_90980d0cbd3143936f111bd2d0e9299c.MeterStatsBandLearnedInformation): An instance of the MeterStatsBandLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterstatsbandlearnedinformation_90980d0cbd3143936f111bd2d0e9299c import MeterStatsBandLearnedInformation
        return MeterStatsBandLearnedInformation(self)

    @property
    def ByteInCount(self):
        """
        Returns
        -------
        - number: Specifies Byte in Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['ByteInCount'])

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - number: The Data Path identifier of the OpenFlow controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: The Data Path identifier of the OpenFlow controller in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def DurationNSec(self):
        """
        Returns
        -------
        - number: Specifies Duration Nano Second
        """
        return self._get_attribute(self._SDM_ATT_MAP['DurationNSec'])

    @property
    def DurationSec(self):
        """
        Returns
        -------
        - number: Specifies Duration in Second
        """
        return self._get_attribute(self._SDM_ATT_MAP['DurationSec'])

    @property
    def ErrorCode(self):
        """
        Returns
        -------
        - str: The error code of the received error.
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
    def FlowCount(self):
        """
        Returns
        -------
        - number: Specifies the Flow Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowCount'])

    @property
    def LastErrorCode(self):
        """
        Returns
        -------
        - str: The Last error code of the received error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastErrorCode'])

    @property
    def LastErrorType(self):
        """
        Returns
        -------
        - str: The type of the Last error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastErrorType'])

    @property
    def Latency(self):
        """
        Returns
        -------
        - number: The latency measurement for the OpenFlow channel in microseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Latency'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: Indicates the local IP of the Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def MeterId(self):
        """
        Returns
        -------
        - number: Specifies Meter ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterId'])

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

    @property
    def NumberOfBandStats(self):
        """
        Returns
        -------
        - number: Specifies the number of band
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfBandStats'])

    @property
    def PacketInCount(self):
        """
        Returns
        -------
        - number: Specifies Packet In Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketInCount'])

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
        - str: The state of reply for the Open Flow channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyState'])

    def find(self, ByteInCount=None, DataPathId=None, DataPathIdAsHex=None, DurationNSec=None, DurationSec=None, ErrorCode=None, ErrorType=None, FlowCount=None, LastErrorCode=None, LastErrorType=None, Latency=None, LocalIp=None, MeterId=None, NegotiatedVersion=None, NumberOfBandStats=None, PacketInCount=None, RemoteIp=None, ReplyState=None):
        """Finds and retrieves meterStatsLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve meterStatsLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all meterStatsLearnedInformation resources from the server.

        Args
        ----
        - ByteInCount (number): Specifies Byte in Count
        - DataPathId (number): The Data Path identifier of the OpenFlow controller.
        - DataPathIdAsHex (str): The Data Path identifier of the OpenFlow controller in hexadecimal format.
        - DurationNSec (number): Specifies Duration Nano Second
        - DurationSec (number): Specifies Duration in Second
        - ErrorCode (str): The error code of the received error.
        - ErrorType (str): The type of the error received.
        - FlowCount (number): Specifies the Flow Count
        - LastErrorCode (str): The Last error code of the received error.
        - LastErrorType (str): The type of the Last error received.
        - Latency (number): The latency measurement for the OpenFlow channel in microseconds.
        - LocalIp (str): Indicates the local IP of the Controller.
        - MeterId (number): Specifies Meter ID
        - NegotiatedVersion (str): Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        - NumberOfBandStats (number): Specifies the number of band
        - PacketInCount (number): Specifies Packet In Count
        - RemoteIp (str): The Remote IP address of the selected interface.
        - ReplyState (str): The state of reply for the Open Flow channel.

        Returns
        -------
        - self: This instance with matching meterStatsLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of meterStatsLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the meterStatsLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
