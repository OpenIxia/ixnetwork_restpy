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


class LmiStatusLearnedInfo(Base):
    """It signifies the status learned info of Local Management Interface.
    The LmiStatusLearnedInfo class encapsulates a list of lmiStatusLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LmiStatusLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'lmiStatusLearnedInfo'
    _SDM_ATT_MAP = {
        'DataInstance': 'dataInstance',
        'DuplicatedIe': 'duplicatedIe',
        'InvalidEvcReferenceId': 'invalidEvcReferenceId',
        'InvalidMandatoryIe': 'invalidMandatoryIe',
        'InvalidMsgType': 'invalidMsgType',
        'InvalidNonMandatoryIe': 'invalidNonMandatoryIe',
        'InvalidProtocolVersion': 'invalidProtocolVersion',
        'LmiStatus': 'lmiStatus',
        'MandatoryIeMissing': 'mandatoryIeMissing',
        'OutOfSequenceIe': 'outOfSequenceIe',
        'ProtocolVersion': 'protocolVersion',
        'ReceiveSequenceNumber': 'receiveSequenceNumber',
        'SendSequenceNumber': 'sendSequenceNumber',
        'ShortMsgCounter': 'shortMsgCounter',
        'UnexpectedIe': 'unexpectedIe',
        'UnrecognizedIe': 'unrecognizedIe',
    }

    def __init__(self, parent):
        super(LmiStatusLearnedInfo, self).__init__(parent)

    @property
    def DataInstance(self):
        """
        Returns
        -------
        - number: This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0x0 for UNI-C and 0x1 for UNI-N. Max 4 octet max value, Min 0/1. Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataInstance'])

    @property
    def DuplicatedIe(self):
        """
        Returns
        -------
        - str: Type of out of sequence IE received : count of out of sequence IE received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DuplicatedIe'])

    @property
    def InvalidEvcReferenceId(self):
        """
        Returns
        -------
        - str: Invalid EVC reference Id.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InvalidEvcReferenceId'])

    @property
    def InvalidMandatoryIe(self):
        """
        Returns
        -------
        - str: Type of invalid mandatory IE : count of invalid mandatory IE.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InvalidMandatoryIe'])

    @property
    def InvalidMsgType(self):
        """
        Returns
        -------
        - str: It signfies the invalid message type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InvalidMsgType'])

    @property
    def InvalidNonMandatoryIe(self):
        """
        Returns
        -------
        - str: Type of invalid non mandatory IE : count of invalid non mandatory IE
        """
        return self._get_attribute(self._SDM_ATT_MAP['InvalidNonMandatoryIe'])

    @property
    def InvalidProtocolVersion(self):
        """
        Returns
        -------
        - str: Invalid protocol version in received ELMI message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InvalidProtocolVersion'])

    @property
    def LmiStatus(self):
        """
        Returns
        -------
        - str: It signifies the LMI status value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LmiStatus'])

    @property
    def MandatoryIeMissing(self):
        """
        Returns
        -------
        - str: Type of mandatory IE missing : count of mandatory IE missing.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MandatoryIeMissing'])

    @property
    def OutOfSequenceIe(self):
        """
        Returns
        -------
        - str: Type of out of sequence IE received : count of out of sequence IE recieved
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutOfSequenceIe'])

    @property
    def ProtocolVersion(self):
        """
        Returns
        -------
        - number: This one-octet field indicates the version supported by the sending
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolVersion'])

    @property
    def ReceiveSequenceNumber(self):
        """
        Returns
        -------
        - number: The value of Receive Sequence Number in received ELMI message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceiveSequenceNumber'])

    @property
    def SendSequenceNumber(self):
        """
        Returns
        -------
        - number: The value of Send Sequence Number in received ELMI message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendSequenceNumber'])

    @property
    def ShortMsgCounter(self):
        """
        Returns
        -------
        - number: It signifies the short message counter value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShortMsgCounter'])

    @property
    def UnexpectedIe(self):
        """
        Returns
        -------
        - str: Type of unexpected IE : count of unexpected IE.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnexpectedIe'])

    @property
    def UnrecognizedIe(self):
        """
        Returns
        -------
        - str: Type of unrecognized IE : count of unrecognized IE.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnrecognizedIe'])

    def find(self, DataInstance=None, DuplicatedIe=None, InvalidEvcReferenceId=None, InvalidMandatoryIe=None, InvalidMsgType=None, InvalidNonMandatoryIe=None, InvalidProtocolVersion=None, LmiStatus=None, MandatoryIeMissing=None, OutOfSequenceIe=None, ProtocolVersion=None, ReceiveSequenceNumber=None, SendSequenceNumber=None, ShortMsgCounter=None, UnexpectedIe=None, UnrecognizedIe=None):
        """Finds and retrieves lmiStatusLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lmiStatusLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lmiStatusLearnedInfo resources from the server.

        Args
        ----
        - DataInstance (number): This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0x0 for UNI-C and 0x1 for UNI-N. Max 4 octet max value, Min 0/1. Change of value in this field takes effect when protocol is running.
        - DuplicatedIe (str): Type of out of sequence IE received : count of out of sequence IE received.
        - InvalidEvcReferenceId (str): Invalid EVC reference Id.
        - InvalidMandatoryIe (str): Type of invalid mandatory IE : count of invalid mandatory IE.
        - InvalidMsgType (str): It signfies the invalid message type.
        - InvalidNonMandatoryIe (str): Type of invalid non mandatory IE : count of invalid non mandatory IE
        - InvalidProtocolVersion (str): Invalid protocol version in received ELMI message.
        - LmiStatus (str): It signifies the LMI status value.
        - MandatoryIeMissing (str): Type of mandatory IE missing : count of mandatory IE missing.
        - OutOfSequenceIe (str): Type of out of sequence IE received : count of out of sequence IE recieved
        - ProtocolVersion (number): This one-octet field indicates the version supported by the sending
        - ReceiveSequenceNumber (number): The value of Receive Sequence Number in received ELMI message.
        - SendSequenceNumber (number): The value of Send Sequence Number in received ELMI message.
        - ShortMsgCounter (number): It signifies the short message counter value.
        - UnexpectedIe (str): Type of unexpected IE : count of unexpected IE.
        - UnrecognizedIe (str): Type of unrecognized IE : count of unrecognized IE.

        Returns
        -------
        - self: This instance with matching lmiStatusLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lmiStatusLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lmiStatusLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
