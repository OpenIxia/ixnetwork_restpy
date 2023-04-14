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


class FecErrorInsertion(Base):
    """
    The FecErrorInsertion class encapsulates a required fecErrorInsertion resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "fecErrorInsertion"
    _SDM_ATT_MAP = {
        "BerCoefficient": "berCoefficient",
        "BerExponent": "berExponent",
        "Continuous": "continuous",
        "Distribution": "distribution",
        "ErrorBits": "errorBits",
        "ErrorType": "errorType",
        "LaneNumber": "laneNumber",
        "Loopcount": "loopcount",
        "PerCodeword": "perCodeword",
        "SequentialCorrect": "sequentialCorrect",
        "SequentialErrors": "sequentialErrors",
    }
    _SDM_ENUM_MAP = {
        "errorType": [
            "random",
            "laneMarkers",
            "codeWords",
            "maxConsecutiveUncorrectableWithoutLossOfLink",
            "minConsecutiveUncorrectableWithLossOfLink",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(FecErrorInsertion, self).__init__(parent, list_op)

    @property
    def BerCoefficient(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Bit error rate coefficient value for random error insertion. Valid range : [0.00, 9.99]
        """
        return self._get_attribute(self._SDM_ATT_MAP["BerCoefficient"])

    @BerCoefficient.setter
    def BerCoefficient(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BerCoefficient"], value)

    @property
    def BerExponent(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Bit error rate exponent(e-) value for random error insertion. Valid range : [5, 15]
        """
        return self._get_attribute(self._SDM_ATT_MAP["BerExponent"])

    @BerExponent.setter
    def BerExponent(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BerExponent"], value)

    @property
    def Continuous(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable/Disable continuous error insertion.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Continuous"])

    @Continuous.setter
    def Continuous(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Continuous"], value)

    @property
    def Distribution(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Error distribution for random error insertion.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Distribution"])

    @Distribution.setter
    def Distribution(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Distribution"], value)

    @property
    def ErrorBits(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Error Bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorBits"])

    @ErrorBits.setter
    def ErrorBits(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErrorBits"], value)

    @property
    def ErrorType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(random | laneMarkers | codeWords | maxConsecutiveUncorrectableWithoutLossOfLink | minConsecutiveUncorrectableWithLossOfLink): Type of Fec error insertion.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorType"])

    @ErrorType.setter
    def ErrorType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErrorType"], value)

    @property
    def LaneNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Lane Number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LaneNumber"])

    @LaneNumber.setter
    def LaneNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LaneNumber"], value)

    @property
    def Loopcount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Loop count value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Loopcount"])

    @Loopcount.setter
    def Loopcount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Loopcount"], value)

    @property
    def PerCodeword(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Per Codeword.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PerCodeword"])

    @PerCodeword.setter
    def PerCodeword(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PerCodeword"], value)

    @property
    def SequentialCorrect(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sequential Correct.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SequentialCorrect"])

    @SequentialCorrect.setter
    def SequentialCorrect(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SequentialCorrect"], value)

    @property
    def SequentialErrors(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sequential Errors.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SequentialErrors"])

    @SequentialErrors.setter
    def SequentialErrors(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SequentialErrors"], value)

    def update(
        self,
        BerCoefficient=None,
        BerExponent=None,
        Continuous=None,
        Distribution=None,
        ErrorBits=None,
        ErrorType=None,
        LaneNumber=None,
        Loopcount=None,
        PerCodeword=None,
        SequentialCorrect=None,
        SequentialErrors=None,
    ):
        # type: (int, int, bool, int, int, str, int, int, int, int, int) -> FecErrorInsertion
        """Updates fecErrorInsertion resource on the server.

        Args
        ----
        - BerCoefficient (number): Bit error rate coefficient value for random error insertion. Valid range : [0.00, 9.99]
        - BerExponent (number): Bit error rate exponent(e-) value for random error insertion. Valid range : [5, 15]
        - Continuous (bool): Enable/Disable continuous error insertion.
        - Distribution (number): Error distribution for random error insertion.
        - ErrorBits (number): Error Bits.
        - ErrorType (str(random | laneMarkers | codeWords | maxConsecutiveUncorrectableWithoutLossOfLink | minConsecutiveUncorrectableWithLossOfLink)): Type of Fec error insertion.
        - LaneNumber (number): Lane Number.
        - Loopcount (number): Loop count value.
        - PerCodeword (number): Per Codeword.
        - SequentialCorrect (number): Sequential Correct.
        - SequentialErrors (number): Sequential Errors.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BerCoefficient=None,
        BerExponent=None,
        Continuous=None,
        Distribution=None,
        ErrorBits=None,
        ErrorType=None,
        LaneNumber=None,
        Loopcount=None,
        PerCodeword=None,
        SequentialCorrect=None,
        SequentialErrors=None,
    ):
        # type: (int, int, bool, int, int, str, int, int, int, int, int) -> FecErrorInsertion
        """Finds and retrieves fecErrorInsertion resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fecErrorInsertion resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fecErrorInsertion resources from the server.

        Args
        ----
        - BerCoefficient (number): Bit error rate coefficient value for random error insertion. Valid range : [0.00, 9.99]
        - BerExponent (number): Bit error rate exponent(e-) value for random error insertion. Valid range : [5, 15]
        - Continuous (bool): Enable/Disable continuous error insertion.
        - Distribution (number): Error distribution for random error insertion.
        - ErrorBits (number): Error Bits.
        - ErrorType (str(random | laneMarkers | codeWords | maxConsecutiveUncorrectableWithoutLossOfLink | minConsecutiveUncorrectableWithLossOfLink)): Type of Fec error insertion.
        - LaneNumber (number): Lane Number.
        - Loopcount (number): Loop count value.
        - PerCodeword (number): Per Codeword.
        - SequentialCorrect (number): Sequential Correct.
        - SequentialErrors (number): Sequential Errors.

        Returns
        -------
        - self: This instance with matching fecErrorInsertion resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fecErrorInsertion data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fecErrorInsertion resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
