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


class Phy(Base):
    """
    The Phy class encapsulates a required phy resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "phy"
    _SDM_ATT_MAP = {
        "LlrCtlOSTargetSpacing": "llrCtlOSTargetSpacing",
        "OCode": "oCode",
        "RxValCtlosMinSpacing": "rxValCtlosMinSpacing",
        "RxValEnableCtlosMinSpacing": "rxValEnableCtlosMinSpacing",
        "RxValEnableLlrAckNack": "rxValEnableLlrAckNack",
        "RxValEnableLlrMinInit": "rxValEnableLlrMinInit",
        "RxValLlrAckNackSpacing": "rxValLlrAckNackSpacing",
        "RxValLlrMinInitInterval": "rxValLlrMinInitInterval",
        "TxCtlOSMinSpacing": "txCtlOSMinSpacing",
        "TxCtlOSMinSpacingStartPkt": "txCtlOSMinSpacingStartPkt",
        "TxCtlOSMinSpacingWithinPkt": "txCtlOSMinSpacingWithinPkt",
    }
    _SDM_ENUM_MAP = {
        "oCode": [
            "0x0",
            "0x1",
            "0x2",
            "0x3",
            "0x4",
            "0x5",
            "0x6",
            "0x7",
            "0x8",
            "0x9",
            "0xA",
            "0xB",
            "0xC",
            "0xD",
            "0xE",
            "0xF",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Phy, self).__init__(parent, list_op)

    @property
    def LlrCtlOSTargetSpacing(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Target spacing (in bytes) between successive LLR_ACK / LLR_NACK CtlOS frames on transmit. Range: [320, 32760].
        """
        return self._get_attribute(self._SDM_ATT_MAP["LlrCtlOSTargetSpacing"])

    @LlrCtlOSTargetSpacing.setter
    def LlrCtlOSTargetSpacing(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LlrCtlOSTargetSpacing"], value)

    @property
    def OCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(0x0 | 0x1 | 0x2 | 0x3 | 0x4 | 0x5 | 0x6 | 0x7 | 0x8 | 0x9 | 0xA | 0xB | 0xC | 0xD | 0xE | 0xF): 4-bit O-Code value (0x00xF) inserted into transmitted ordered sets to identify the CtlOS variant.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OCode"])

    @OCode.setter
    def OCode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["OCode"], value)

    @property
    def RxValCtlosMinSpacing(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Minimum allowed spacing (in bytes) between received CtlOS frames. Range: [0, 131064].
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxValCtlosMinSpacing"])

    @RxValCtlosMinSpacing.setter
    def RxValCtlosMinSpacing(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxValCtlosMinSpacing"], value)

    @property
    def RxValEnableCtlosMinSpacing(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When ON, the receiver validates that incoming CtlOS frames meet the configured minimum spacing.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxValEnableCtlosMinSpacing"])

    @RxValEnableCtlosMinSpacing.setter
    def RxValEnableCtlosMinSpacing(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxValEnableCtlosMinSpacing"], value)

    @property
    def RxValEnableLlrAckNack(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When ON, the receiver validates that incoming LLR_ACK / LLR_NACK CtlOS frames meet the configured minimum spacing.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxValEnableLlrAckNack"])

    @RxValEnableLlrAckNack.setter
    def RxValEnableLlrAckNack(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxValEnableLlrAckNack"], value)

    @property
    def RxValEnableLlrMinInit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When ON, the receiver validates that incoming LLR_INIT CtlOS frames meet the configured minimum interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxValEnableLlrMinInit"])

    @RxValEnableLlrMinInit.setter
    def RxValEnableLlrMinInit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxValEnableLlrMinInit"], value)

    @property
    def RxValLlrAckNackSpacing(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Minimum allowed spacing (in bytes) between received LLR_ACK / LLR_NACK CtlOS frames. Range: [0, 131064].
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxValLlrAckNackSpacing"])

    @RxValLlrAckNackSpacing.setter
    def RxValLlrAckNackSpacing(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxValLlrAckNackSpacing"], value)

    @property
    def RxValLlrMinInitInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: When ON, the receiver validates that incoming LLR_INIT CtlOS frames meet the configured minimum interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxValLlrMinInitInterval"])

    @RxValLlrMinInitInterval.setter
    def RxValLlrMinInitInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxValLlrMinInitInterval"], value)

    @property
    def TxCtlOSMinSpacing(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Minimum spacing (in bytes) the transmitter enforces between consecutive CtlOS frames on the wire. Range: [320, 32760].
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxCtlOSMinSpacing"])

    @TxCtlOSMinSpacing.setter
    def TxCtlOSMinSpacing(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxCtlOSMinSpacing"], value)

    @property
    def TxCtlOSMinSpacingStartPkt(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Minimum spacing (in bytes) between a CtlOS frame and the start of a data packet on transmit. Range: [64, 1008].
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxCtlOSMinSpacingStartPkt"])

    @TxCtlOSMinSpacingStartPkt.setter
    def TxCtlOSMinSpacingStartPkt(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxCtlOSMinSpacingStartPkt"], value)

    @property
    def TxCtlOSMinSpacingWithinPkt(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Minimum spacing (in bytes) between CtlOS frames inserted within an ongoing data packet on transmit. Range: [1024, 8184].
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxCtlOSMinSpacingWithinPkt"])

    @TxCtlOSMinSpacingWithinPkt.setter
    def TxCtlOSMinSpacingWithinPkt(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxCtlOSMinSpacingWithinPkt"], value)

    def update(
        self,
        LlrCtlOSTargetSpacing=None,
        OCode=None,
        RxValCtlosMinSpacing=None,
        RxValEnableCtlosMinSpacing=None,
        RxValEnableLlrAckNack=None,
        RxValEnableLlrMinInit=None,
        RxValLlrAckNackSpacing=None,
        RxValLlrMinInitInterval=None,
        TxCtlOSMinSpacing=None,
        TxCtlOSMinSpacingStartPkt=None,
        TxCtlOSMinSpacingWithinPkt=None,
    ):
        # type: (int, str, int, bool, bool, bool, int, int, int, int, int) -> Phy
        """Updates phy resource on the server.

        Args
        ----
        - LlrCtlOSTargetSpacing (number): Target spacing (in bytes) between successive LLR_ACK / LLR_NACK CtlOS frames on transmit. Range: [320, 32760].
        - OCode (str(0x0 | 0x1 | 0x2 | 0x3 | 0x4 | 0x5 | 0x6 | 0x7 | 0x8 | 0x9 | 0xA | 0xB | 0xC | 0xD | 0xE | 0xF)): 4-bit O-Code value (0x00xF) inserted into transmitted ordered sets to identify the CtlOS variant.
        - RxValCtlosMinSpacing (number): Minimum allowed spacing (in bytes) between received CtlOS frames. Range: [0, 131064].
        - RxValEnableCtlosMinSpacing (bool): When ON, the receiver validates that incoming CtlOS frames meet the configured minimum spacing.
        - RxValEnableLlrAckNack (bool): When ON, the receiver validates that incoming LLR_ACK / LLR_NACK CtlOS frames meet the configured minimum spacing.
        - RxValEnableLlrMinInit (bool): When ON, the receiver validates that incoming LLR_INIT CtlOS frames meet the configured minimum interval.
        - RxValLlrAckNackSpacing (number): Minimum allowed spacing (in bytes) between received LLR_ACK / LLR_NACK CtlOS frames. Range: [0, 131064].
        - RxValLlrMinInitInterval (number): When ON, the receiver validates that incoming LLR_INIT CtlOS frames meet the configured minimum interval.
        - TxCtlOSMinSpacing (number): Minimum spacing (in bytes) the transmitter enforces between consecutive CtlOS frames on the wire. Range: [320, 32760].
        - TxCtlOSMinSpacingStartPkt (number): Minimum spacing (in bytes) between a CtlOS frame and the start of a data packet on transmit. Range: [64, 1008].
        - TxCtlOSMinSpacingWithinPkt (number): Minimum spacing (in bytes) between CtlOS frames inserted within an ongoing data packet on transmit. Range: [1024, 8184].

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        LlrCtlOSTargetSpacing=None,
        OCode=None,
        RxValCtlosMinSpacing=None,
        RxValEnableCtlosMinSpacing=None,
        RxValEnableLlrAckNack=None,
        RxValEnableLlrMinInit=None,
        RxValLlrAckNackSpacing=None,
        RxValLlrMinInitInterval=None,
        TxCtlOSMinSpacing=None,
        TxCtlOSMinSpacingStartPkt=None,
        TxCtlOSMinSpacingWithinPkt=None,
    ):
        # type: (int, str, int, bool, bool, bool, int, int, int, int, int) -> Phy
        """Finds and retrieves phy resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve phy resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all phy resources from the server.

        Args
        ----
        - LlrCtlOSTargetSpacing (number): Target spacing (in bytes) between successive LLR_ACK / LLR_NACK CtlOS frames on transmit. Range: [320, 32760].
        - OCode (str(0x0 | 0x1 | 0x2 | 0x3 | 0x4 | 0x5 | 0x6 | 0x7 | 0x8 | 0x9 | 0xA | 0xB | 0xC | 0xD | 0xE | 0xF)): 4-bit O-Code value (0x00xF) inserted into transmitted ordered sets to identify the CtlOS variant.
        - RxValCtlosMinSpacing (number): Minimum allowed spacing (in bytes) between received CtlOS frames. Range: [0, 131064].
        - RxValEnableCtlosMinSpacing (bool): When ON, the receiver validates that incoming CtlOS frames meet the configured minimum spacing.
        - RxValEnableLlrAckNack (bool): When ON, the receiver validates that incoming LLR_ACK / LLR_NACK CtlOS frames meet the configured minimum spacing.
        - RxValEnableLlrMinInit (bool): When ON, the receiver validates that incoming LLR_INIT CtlOS frames meet the configured minimum interval.
        - RxValLlrAckNackSpacing (number): Minimum allowed spacing (in bytes) between received LLR_ACK / LLR_NACK CtlOS frames. Range: [0, 131064].
        - RxValLlrMinInitInterval (number): When ON, the receiver validates that incoming LLR_INIT CtlOS frames meet the configured minimum interval.
        - TxCtlOSMinSpacing (number): Minimum spacing (in bytes) the transmitter enforces between consecutive CtlOS frames on the wire. Range: [320, 32760].
        - TxCtlOSMinSpacingStartPkt (number): Minimum spacing (in bytes) between a CtlOS frame and the start of a data packet on transmit. Range: [64, 1008].
        - TxCtlOSMinSpacingWithinPkt (number): Minimum spacing (in bytes) between CtlOS frames inserted within an ongoing data packet on transmit. Range: [1024, 8184].

        Returns
        -------
        - self: This instance with matching phy resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of phy data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the phy resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
