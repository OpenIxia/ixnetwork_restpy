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


class PingLearnedInfo(Base):
    """This object holds lists of the ping learned information.
    The PingLearnedInfo class encapsulates a list of pingLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the PingLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "pingLearnedInfo"
    _SDM_ATT_MAP = {
        "ErrorTlvType": "errorTlvType",
        "IncomingLabelOuterInner": "incomingLabelOuterInner",
        "InterfaceLabelStackTlvInterface": "interfaceLabelStackTlvInterface",
        "InterfaceLabelStackTlvIpAddress": "interfaceLabelStackTlvIpAddress",
        "InterfaceLabelStackTlvLabels": "interfaceLabelStackTlvLabels",
        "OutgoingLabelOuterInner": "outgoingLabelOuterInner",
        "Reachability": "reachability",
        "ReturnCode": "returnCode",
        "ReturnSubcode": "returnSubcode",
        "ReversePathVerificationCode": "reversePathVerificationCode",
        "Rtt": "rtt",
        "SenderHandle": "senderHandle",
        "SequenceNumber": "sequenceNumber",
        "Type": "type",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PingLearnedInfo, self).__init__(parent, list_op)

    @property
    def ErrorTlvType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies Error TLV if it is received in lsp ping echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorTlvType"])

    @property
    def IncomingLabelOuterInner(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the incoming label information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncomingLabelOuterInner"])

    @property
    def InterfaceLabelStackTlvInterface(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This Signifies the inclusion of the Interface Id within Interface and Label Stack TLV in received lsp ping echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceLabelStackTlvInterface"])

    @property
    def InterfaceLabelStackTlvIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This Signifies the inclusion of the IP Address within Interface and Label Stack TLV in received lsp ping echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceLabelStackTlvIpAddress"])

    @property
    def InterfaceLabelStackTlvLabels(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the label stack in Interface and Label Stack TLV received in lsp ping echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceLabelStackTlvLabels"])

    @property
    def OutgoingLabelOuterInner(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the Outgoing Label information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutgoingLabelOuterInner"])

    @property
    def Reachability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This specifies whether the queried MEP could be reached or not, Yes or No.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Reachability"])

    @property
    def ReturnCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the value of the return code in the Echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReturnCode"])

    @property
    def ReturnSubcode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the value of the return sub-code in the Echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReturnSubcode"])

    @property
    def ReversePathVerificationCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This Signifies the reverse path verification code received in the lsp ping echo reply message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReversePathVerificationCode"])

    @property
    def Rtt(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the Round Trip Time.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Rtt"])

    @property
    def SenderHandle(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the sender handle information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SenderHandle"])

    @property
    def SequenceNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the sequence number for the ping learned information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SequenceNumber"])

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the type of the learned info.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    def add(self):
        """Adds a new pingLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved pingLearnedInfo resources using find and the newly added pingLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ErrorTlvType=None,
        IncomingLabelOuterInner=None,
        InterfaceLabelStackTlvInterface=None,
        InterfaceLabelStackTlvIpAddress=None,
        InterfaceLabelStackTlvLabels=None,
        OutgoingLabelOuterInner=None,
        Reachability=None,
        ReturnCode=None,
        ReturnSubcode=None,
        ReversePathVerificationCode=None,
        Rtt=None,
        SenderHandle=None,
        SequenceNumber=None,
        Type=None,
    ):
        # type: (int, str, int, str, str, str, bool, str, int, str, str, int, int, str) -> PingLearnedInfo
        """Finds and retrieves pingLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pingLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pingLearnedInfo resources from the server.

        Args
        ----
        - ErrorTlvType (number): This signifies Error TLV if it is received in lsp ping echo reply message.
        - IncomingLabelOuterInner (str): This signifies the incoming label information.
        - InterfaceLabelStackTlvInterface (number): This Signifies the inclusion of the Interface Id within Interface and Label Stack TLV in received lsp ping echo reply message.
        - InterfaceLabelStackTlvIpAddress (str): This Signifies the inclusion of the IP Address within Interface and Label Stack TLV in received lsp ping echo reply message.
        - InterfaceLabelStackTlvLabels (str): This signifies the label stack in Interface and Label Stack TLV received in lsp ping echo reply message.
        - OutgoingLabelOuterInner (str): This signifies the Outgoing Label information.
        - Reachability (bool): This specifies whether the queried MEP could be reached or not, Yes or No.
        - ReturnCode (str): This signifies the value of the return code in the Echo reply message.
        - ReturnSubcode (number): This signifies the value of the return sub-code in the Echo reply message.
        - ReversePathVerificationCode (str): This Signifies the reverse path verification code received in the lsp ping echo reply message.
        - Rtt (str): This signifies the Round Trip Time.
        - SenderHandle (number): This signifies the sender handle information.
        - SequenceNumber (number): This signifies the sequence number for the ping learned information.
        - Type (str): This signifies the type of the learned info.

        Returns
        -------
        - self: This instance with matching pingLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pingLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pingLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
