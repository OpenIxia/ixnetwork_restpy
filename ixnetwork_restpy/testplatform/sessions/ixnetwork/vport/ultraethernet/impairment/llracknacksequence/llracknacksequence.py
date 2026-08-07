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


class LlrAckNackSequence(Base):
    """
    The LlrAckNackSequence class encapsulates a required llrAckNackSequence resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "llrAckNackSequence"
    _SDM_ATT_MAP = {
        "CtlOSType": "ctlOSType",
        "DeltaSequenceNumber": "deltaSequenceNumber",
        "SkipCount": "skipCount",
        "TestState": "testState",
        "TestStatus": "testStatus",
    }
    _SDM_ENUM_MAP = {
        "ctlOSType": ["ack", "nack"],
        "testState": ["notRunning", "running", "stopping", "error"],
    }

    def __init__(self, parent, list_op=False):
        super(LlrAckNackSequence, self).__init__(parent, list_op)

    @property
    def CtlOSType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ack | nack): Selects which CtlOS to corrupt with an incorrect sequence number: ACK or NACK.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CtlOSType"])

    @CtlOSType.setter
    def CtlOSType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CtlOSType"], value)

    @property
    def DeltaSequenceNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signed offset applied to the ACK/NACK sequence number when injecting the incorrect-sequence impairment.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeltaSequenceNumber"])

    @DeltaSequenceNumber.setter
    def DeltaSequenceNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeltaSequenceNumber"], value)

    @property
    def SkipCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of ACK/NACK CtlOS frames to send normally before injecting an incorrect sequence number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SkipCount"])

    @SkipCount.setter
    def SkipCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SkipCount"], value)

    @property
    def TestState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(notRunning | running | stopping | error): Current execution state of the impairment test (Not Running / Running / Stopping / Error).
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestState"])

    @property
    def TestStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Status of the impairment test's last/current run (e.g., Started, Stopped, error details).
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestStatus"])

    def update(self, CtlOSType=None, DeltaSequenceNumber=None, SkipCount=None):
        # type: (str, int, int) -> LlrAckNackSequence
        """Updates llrAckNackSequence resource on the server.

        Args
        ----
        - CtlOSType (str(ack | nack)): Selects which CtlOS to corrupt with an incorrect sequence number: ACK or NACK.
        - DeltaSequenceNumber (number): Signed offset applied to the ACK/NACK sequence number when injecting the incorrect-sequence impairment.
        - SkipCount (number): Number of ACK/NACK CtlOS frames to send normally before injecting an incorrect sequence number.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CtlOSType=None,
        DeltaSequenceNumber=None,
        SkipCount=None,
        TestState=None,
        TestStatus=None,
    ):
        # type: (str, int, int, str, str) -> LlrAckNackSequence
        """Finds and retrieves llrAckNackSequence resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve llrAckNackSequence resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all llrAckNackSequence resources from the server.

        Args
        ----
        - CtlOSType (str(ack | nack)): Selects which CtlOS to corrupt with an incorrect sequence number: ACK or NACK.
        - DeltaSequenceNumber (number): Signed offset applied to the ACK/NACK sequence number when injecting the incorrect-sequence impairment.
        - SkipCount (number): Number of ACK/NACK CtlOS frames to send normally before injecting an incorrect sequence number.
        - TestState (str(notRunning | running | stopping | error)): Current execution state of the impairment test (Not Running / Running / Stopping / Error).
        - TestStatus (str): Status of the impairment test's last/current run (e.g., Started, Stopped, error details).

        Returns
        -------
        - self: This instance with matching llrAckNackSequence resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of llrAckNackSequence data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the llrAckNackSequence resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
