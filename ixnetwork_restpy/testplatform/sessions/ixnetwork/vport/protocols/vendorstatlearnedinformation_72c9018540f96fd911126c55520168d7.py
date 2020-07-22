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


class VendorStatLearnedInformation(Base):
    """Signifies the information learnt from the vendor statistics.
    The VendorStatLearnedInformation class encapsulates a list of vendorStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the VendorStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'vendorStatLearnedInformation'
    _SDM_ATT_MAP = {
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'ErrorCode': 'errorCode',
        'ErrorType': 'errorType',
        'ExperimenterType': 'experimenterType',
        'Latency': 'latency',
        'LocalIp': 'localIp',
        'MessageLength': 'messageLength',
        'NegotiatedVersion': 'negotiatedVersion',
        'RemoteIp': 'remoteIp',
        'ReplyState': 'replyState',
        'VendorId': 'vendorId',
        'VendorMessage': 'vendorMessage',
    }

    def __init__(self, parent):
        super(VendorStatLearnedInformation, self).__init__(parent)

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
    def ErrorCode(self):
        """
        Returns
        -------
        - str: Signifies the error code of the error received
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
    def ExperimenterType(self):
        """
        Returns
        -------
        - number: Type of experimenter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterType'])

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
    def MessageLength(self):
        """
        Returns
        -------
        - number: Signifies the length of the message transmitted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MessageLength'])

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiatedVersion'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: The IP address of the DUT at the other end of the Open Flow channel.
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
    def VendorId(self):
        """
        Returns
        -------
        - number: Signifies the vendor identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorId'])

    @property
    def VendorMessage(self):
        """
        Returns
        -------
        - str: Signifies the vendor message value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VendorMessage'])

    def find(self, DataPathId=None, DataPathIdAsHex=None, ErrorCode=None, ErrorType=None, ExperimenterType=None, Latency=None, LocalIp=None, MessageLength=None, NegotiatedVersion=None, RemoteIp=None, ReplyState=None, VendorId=None, VendorMessage=None):
        """Finds and retrieves vendorStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vendorStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vendorStatLearnedInformation resources from the server.

        Args
        ----
        - DataPathId (str): Signifies the datapath ID of the OpenFlow switch.
        - DataPathIdAsHex (str): Signifies the datapath ID of the OpenFlow switch in hexadecimal format.
        - ErrorCode (str): Signifies the error code of the error received
        - ErrorType (str): Signifies the type of the error received.
        - ExperimenterType (number): Type of experimenter.
        - Latency (number): Signifies the latency measurement for the OpenFlow channel in microseconds.
        - LocalIp (str): Signifies the local IP address of the selected interface.
        - MessageLength (number): Signifies the length of the message transmitted.
        - NegotiatedVersion (str): Version of the protocol that has been negotiated between OpenFLow Controller and Switch.
        - RemoteIp (str): The IP address of the DUT at the other end of the Open Flow channel.
        - ReplyState (str): Signifies the reply state of the OF Channel.
        - VendorId (number): Signifies the vendor identifier.
        - VendorMessage (str): Signifies the vendor message value.

        Returns
        -------
        - self: This instance with matching vendorStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vendorStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vendorStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
