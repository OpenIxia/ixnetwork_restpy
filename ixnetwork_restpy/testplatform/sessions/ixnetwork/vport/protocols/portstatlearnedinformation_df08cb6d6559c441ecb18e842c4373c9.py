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


class PortStatLearnedInformation(Base):
    """Signifies the information learned from the port.
    The PortStatLearnedInformation class encapsulates a list of portStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the PortStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'portStatLearnedInformation'
    _SDM_ATT_MAP = {
        'Collisions': 'collisions',
        'CrcErrors': 'crcErrors',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'Duration': 'duration',
        'DurationInNsec': 'durationInNsec',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'FrameAlignmentErrors': 'frameAlignmentErrors',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'NegotiatedVersion': 'negotiatedVersion',
        'PacketsDroppedByRx': 'packetsDroppedByRx',
        'PacketsDroppedByTx': 'packetsDroppedByTx',
        'PacketsWithRxOverrun': 'packetsWithRxOverrun',
        'PortNo': 'portNo',
        'ReceivedBytes': 'receivedBytes',
        'ReceivedErrors': 'receivedErrors',
        'ReceivedPackets': 'receivedPackets',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
        'TransmitErrors': 'transmitErrors',
        'TransmittedBytes': 'transmittedBytes',
        'TransmittedPackets': 'transmittedPackets',
    }

    def __init__(self, parent):
        super(PortStatLearnedInformation, self).__init__(parent)

    @property
    def Collisions(self):
        """
        Returns
        -------
        - str: Indicates the number of collisions.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Collisions'])

    @property
    def CrcErrors(self):
        """
        Returns
        -------
        - str: Signifies the number of CRC errors.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CrcErrors'])

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: Signifies the datapath ID of the OpenFlow switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: Signifies the datapath ID of the OpenFlow switch in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: The time in seconds, for which the port has been alive.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Duration'])

    @property
    def DurationInNsec(self):
        """
        Returns
        -------
        - number: The time in nanoseconds, for which the port has been alive beyond Duration (sec).
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
    def FrameAlignmentErrors(self):
        """
        Returns
        -------
        - str: Signifies the number of Frame Alignment errors.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameAlignmentErrors'])

    @property
    def Latency(self):
        """
        Returns
        -------
        - number: Signifies the latency measurement for the OpenFlow channel in microseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Latency'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: Signifies the local IP address of the selected interface.
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
    def PacketsDroppedByRx(self):
        """
        Returns
        -------
        - str: Signifies the number of packets dropped by the receiving port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketsDroppedByRx'])

    @property
    def PacketsDroppedByTx(self):
        """
        Returns
        -------
        - str: Signifies the number of packets dropped by the transmitting port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketsDroppedByTx'])

    @property
    def PacketsWithRxOverrun(self):
        """
        Returns
        -------
        - str: Signifies the number of packets with received overruns.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketsWithRxOverrun'])

    @property
    def PortNo(self):
        """
        Returns
        -------
        - number: Signifies the port number used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortNo'])

    @property
    def ReceivedBytes(self):
        """
        Returns
        -------
        - str: Signifies the number of bytes received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedBytes'])

    @property
    def ReceivedErrors(self):
        """
        Returns
        -------
        - str: Signifies the number of received errors.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedErrors'])

    @property
    def ReceivedPackets(self):
        """
        Returns
        -------
        - str: Signifies the number of packets received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedPackets'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: Signifies the Remote IP address of the selected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: Signifies the reply state of the OF Channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyState'])

    @property
    def TransmitErrors(self):
        """
        Returns
        -------
        - str: Signifies the number of Transmit errors.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmitErrors'])

    @property
    def TransmittedBytes(self):
        """
        Returns
        -------
        - str: Signifies the number of bytes transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmittedBytes'])

    @property
    def TransmittedPackets(self):
        """
        Returns
        -------
        - str: Signifies the number of packets transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmittedPackets'])

    def find(self, Collisions=None, CrcErrors=None, DataPathId=None, DataPathIdAsHex=None, Duration=None, DurationInNsec=None, ErrorCode=None, ErrorType=None, FrameAlignmentErrors=None, Latency=None, LocalIp=None, NegotiatedVersion=None, PacketsDroppedByRx=None, PacketsDroppedByTx=None, PacketsWithRxOverrun=None, PortNo=None, ReceivedBytes=None, ReceivedErrors=None, ReceivedPackets=None, RemoteIp=None, ReplyState=None, TransmitErrors=None, TransmittedBytes=None, TransmittedPackets=None):
        """Finds and retrieves portStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve portStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all portStatLearnedInformation resources from the server.

        Args
        ----
        - Collisions (str): Indicates the number of collisions.
        - CrcErrors (str): Signifies the number of CRC errors.
        - DataPathId (str): Signifies the datapath ID of the OpenFlow switch.
        - DataPathIdAsHex (str): Signifies the datapath ID of the OpenFlow switch in hexadecimal format.
        - Duration (number): The time in seconds, for which the port has been alive.
        - DurationInNsec (number): The time in nanoseconds, for which the port has been alive beyond Duration (sec).
        - ErrorCode (str): Signifies the error code of the error received.
        - ErrorType (str): Signifies the type of the error received.
        - FrameAlignmentErrors (str): Signifies the number of Frame Alignment errors.
        - Latency (number): Signifies the latency measurement for the OpenFlow channel in microseconds.
        - LocalIp (str): Signifies the local IP address of the selected interface.
        - NegotiatedVersion (str): Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        - PacketsDroppedByRx (str): Signifies the number of packets dropped by the receiving port.
        - PacketsDroppedByTx (str): Signifies the number of packets dropped by the transmitting port.
        - PacketsWithRxOverrun (str): Signifies the number of packets with received overruns.
        - PortNo (number): Signifies the port number used.
        - ReceivedBytes (str): Signifies the number of bytes received.
        - ReceivedErrors (str): Signifies the number of received errors.
        - ReceivedPackets (str): Signifies the number of packets received.
        - RemoteIp (str): Signifies the Remote IP address of the selected interface.
        - ReplyState (str): Signifies the reply state of the OF Channel.
        - TransmitErrors (str): Signifies the number of Transmit errors.
        - TransmittedBytes (str): Signifies the number of bytes transmitted.
        - TransmittedPackets (str): Signifies the number of packets transmitted.

        Returns
        -------
        - self: This instance with matching portStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of portStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the portStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
