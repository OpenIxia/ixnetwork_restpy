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


class QueueStatLearnedInformation(Base):
    """This object allows to configure the queue statistics learned information parameters.
    The QueueStatLearnedInformation class encapsulates a list of queueStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the QueueStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'queueStatLearnedInformation'
    _SDM_ATT_MAP = {
        'BytesTx': 'bytesTx',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'Duration': 'duration',
        'DurationInNsec': 'durationInNsec',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'NegotiatedVersion': 'negotiatedVersion',
        'PacketsTx': 'packetsTx',
        'PortNumber': 'portNumber',
        'QueueId': 'queueId',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
        'TxErrors': 'txErrors',
    }

    def __init__(self, parent):
        super(QueueStatLearnedInformation, self).__init__(parent)

    @property
    def BytesTx(self):
        """
        Returns
        -------
        - str: Indicates the number of transmitted bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BytesTx'])

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: Indicates the Datapath ID of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: Indicates the Datapath ID, in hexadecimal format, of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: The time in seconds, for which the queue has been alive.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])

    @property
    def DurationInNsec(self):
        """
        Returns
        -------
        - number: The time in nanoseconds, for which the queue has been alive beyond Duration (sec).
        """
        return self._get_attribute(self._SDM_ATT_MAP['DurationInNsec'])

    @property
    def ErrorCode(self):
        """
        Returns
        -------
        - str: Signifies the error code of the error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorCode'])

    @property
    def ErrorType(self):
        """
        Returns
        -------
        - str: Signifies the type of the error received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorType'])

    @property
    def Latency(self):
        """
        Returns
        -------
        - number: Indicates the duration elapsed (in microsecond) between the learned info request and response.
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
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

    @property
    def PacketsTx(self):
        """
        Returns
        -------
        - str: Indicates the number of transmitted packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketsTx'])

    @property
    def PortNumber(self):
        """
        Returns
        -------
        - number: Indicates the port to which the queue belongs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortNumber'])

    @property
    def QueueId(self):
        """
        Returns
        -------
        - number: Indicates the Identifier of the queue.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueueId'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: Indicates the IP of the remote end of the OF Channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: Indicates the reply state of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyState'])

    @property
    def TxErrors(self):
        """
        Returns
        -------
        - str: Indicates the number of packets dropped due to overrun.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxErrors'])

    def find(self, BytesTx=None, DataPathId=None, DataPathIdAsHex=None, Duration=None, DurationInNsec=None, ErrorCode=None, ErrorType=None, Latency=None, LocalIp=None, NegotiatedVersion=None, PacketsTx=None, PortNumber=None, QueueId=None, RemoteIp=None, ReplyState=None, TxErrors=None):
        """Finds and retrieves queueStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve queueStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all queueStatLearnedInformation resources from the server.

        Args
        ----
        - BytesTx (str): Indicates the number of transmitted bytes.
        - DataPathId (str): Indicates the Datapath ID of the switch.
        - DataPathIdAsHex (str): Indicates the Datapath ID, in hexadecimal format, of the switch.
        - Duration (number): The time in seconds, for which the queue has been alive.
        - DurationInNsec (number): The time in nanoseconds, for which the queue has been alive beyond Duration (sec).
        - ErrorCode (str): Signifies the error code of the error received.
        - ErrorType (str): Signifies the type of the error received.
        - Latency (number): Indicates the duration elapsed (in microsecond) between the learned info request and response.
        - LocalIp (str): Indicates the local IP of the Controller.
        - NegotiatedVersion (str): Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        - PacketsTx (str): Indicates the number of transmitted packets.
        - PortNumber (number): Indicates the port to which the queue belongs.
        - QueueId (number): Indicates the Identifier of the queue.
        - RemoteIp (str): Indicates the IP of the remote end of the OF Channel.
        - ReplyState (str): Indicates the reply state of the switch.
        - TxErrors (str): Indicates the number of packets dropped due to overrun.

        Returns
        -------
        - self: This instance with matching queueStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of queueStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the queueStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
