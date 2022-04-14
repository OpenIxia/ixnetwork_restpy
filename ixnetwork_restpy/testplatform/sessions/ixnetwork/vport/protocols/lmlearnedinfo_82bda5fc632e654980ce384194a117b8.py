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


class LmLearnedInfo(Base):
    """This object holds lists of the lm learned information.
    The LmLearnedInfo class encapsulates a list of lmLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LmLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "lmLearnedInfo"
    _SDM_ATT_MAP = {
        "IncomingLabelOuterInner": "incomingLabelOuterInner",
        "LastLmResponseDutRx": "lastLmResponseDutRx",
        "LastLmResponseDutTx": "lastLmResponseDutTx",
        "LastLmResponseMyTx": "lastLmResponseMyTx",
        "LmQueriesSent": "lmQueriesSent",
        "LmRemoteUsing64Bit": "lmRemoteUsing64Bit",
        "LmResponsesReceived": "lmResponsesReceived",
        "OutgoingLabelOuterInner": "outgoingLabelOuterInner",
        "Type": "type",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LmLearnedInfo, self).__init__(parent, list_op)

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
    def LastLmResponseDutRx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the value of the DUT Rx counter in the last LM Response received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastLmResponseDutRx"])

    @property
    def LastLmResponseDutTx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the value of the DUT Tx counter in the last LM Response received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastLmResponseDutTx"])

    @property
    def LastLmResponseMyTx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the value of the My Tx counter in the last LM Response received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastLmResponseMyTx"])

    @property
    def LmQueriesSent(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the number of LM queries sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmQueriesSent"])

    @property
    def LmRemoteUsing64Bit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This specifies whether the remote end is using 64bit counter or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmRemoteUsing64Bit"])

    @property
    def LmResponsesReceived(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This signifies the number of LM responses received.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmResponsesReceived"])

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
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This signifies the Selection of this option to filter according to the following types LSP and PW.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    def add(self):
        """Adds a new lmLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved lmLearnedInfo resources using find and the newly added lmLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        IncomingLabelOuterInner=None,
        LastLmResponseDutRx=None,
        LastLmResponseDutTx=None,
        LastLmResponseMyTx=None,
        LmQueriesSent=None,
        LmRemoteUsing64Bit=None,
        LmResponsesReceived=None,
        OutgoingLabelOuterInner=None,
        Type=None,
    ):
        # type: (str, int, int, int, int, bool, int, str, str) -> LmLearnedInfo
        """Finds and retrieves lmLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lmLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lmLearnedInfo resources from the server.

        Args
        ----
        - IncomingLabelOuterInner (str): This signifies the incoming label information.
        - LastLmResponseDutRx (number): This signifies the value of the DUT Rx counter in the last LM Response received.
        - LastLmResponseDutTx (number): This signifies the value of the DUT Tx counter in the last LM Response received.
        - LastLmResponseMyTx (number): This signifies the value of the My Tx counter in the last LM Response received.
        - LmQueriesSent (number): This signifies the number of LM queries sent.
        - LmRemoteUsing64Bit (bool): This specifies whether the remote end is using 64bit counter or not.
        - LmResponsesReceived (number): This signifies the number of LM responses received.
        - OutgoingLabelOuterInner (str): This signifies the Outgoing Label information.
        - Type (str): This signifies the Selection of this option to filter according to the following types LSP and PW.

        Returns
        -------
        - self: This instance with matching lmLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lmLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lmLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
