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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Filter(Base):
    """This object specifies the field properties.
    The Filter class encapsulates a required filter resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'filter'
    _SDM_ATT_MAP = {
        'CaptureFilterDA': 'captureFilterDA',
        'CaptureFilterEnable': 'captureFilterEnable',
        'CaptureFilterError': 'captureFilterError',
        'CaptureFilterExpressionString': 'captureFilterExpressionString',
        'CaptureFilterFrameSizeEnable': 'captureFilterFrameSizeEnable',
        'CaptureFilterFrameSizeFrom': 'captureFilterFrameSizeFrom',
        'CaptureFilterFrameSizeTo': 'captureFilterFrameSizeTo',
        'CaptureFilterPattern': 'captureFilterPattern',
        'CaptureFilterSA': 'captureFilterSA',
    }
    _SDM_ENUM_MAP = {
        'captureFilterDA': ['addr1', 'addr2', 'anyAddr', 'notAddr1', 'notAddr2'],
        'captureFilterError': ['errAnyFrame', 'errAnyIpTcpUdpChecksumError', 'errAnySequencekError', 'errBadCRC', 'errBadFrame', 'errBigSequenceError', 'errDataIntegrityError', 'errGoodFrame', 'errInvalidFcoeFrame', 'errReverseSequenceError', 'errSmallSequenceError'],
        'captureFilterPattern': ['anyPattern', 'notPattern1', 'notPattern2', 'pattern1', 'pattern1AndPattern2', 'pattern2'],
        'captureFilterSA': ['addr1', 'addr2', 'anyAddr', 'notAddr1', 'notAddr2'],
    }

    def __init__(self, parent, list_op=False):
        super(Filter, self).__init__(parent, list_op)

    @property
    def CaptureFilterDA(self):
        # type: () -> str
        """
        Returns
        -------
        - str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2): One of two available destination MAC addresses to filter on. Applicable only when capturefilternable is set to true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterDA'])
    @CaptureFilterDA.setter
    def CaptureFilterDA(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterDA'], value)

    @property
    def CaptureFilterEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables the capture filter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterEnable'])
    @CaptureFilterEnable.setter
    def CaptureFilterEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterEnable'], value)

    @property
    def CaptureFilterError(self):
        # type: () -> str
        """
        Returns
        -------
        - str(errAnyFrame | errAnyIpTcpUdpChecksumError | errAnySequencekError | errBadCRC | errBadFrame | errBigSequenceError | errDataIntegrityError | errGoodFrame | errInvalidFcoeFrame | errReverseSequenceError | errSmallSequenceError): Applicable only when captureFilterEnable is set to true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterError'])
    @CaptureFilterError.setter
    def CaptureFilterError(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterError'], value)

    @property
    def CaptureFilterExpressionString(self):
        # type: () -> str
        """
        Returns
        -------
        - str: String composed of SA1, DA1, P1, P2, optionally negated with '!', and connected with operators 'and', 'or', 'xor', 'nand' or 'nor'. (Eg: {DA1 and SA1 or !P1 and P2} ). NOTE: The 'or', 'xor', 'nand' and 'nor' operators are available only on the following load modules: XMVDC, NGY, XMSP12, LAVA(MK), Xcellon AP, Xcellon NP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterExpressionString'])
    @CaptureFilterExpressionString.setter
    def CaptureFilterExpressionString(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterExpressionString'], value)

    @property
    def CaptureFilterFrameSizeEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables the frame size constraint which specifies a range of frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterFrameSizeEnable'])
    @CaptureFilterFrameSizeEnable.setter
    def CaptureFilterFrameSizeEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterFrameSizeEnable'], value)

    @property
    def CaptureFilterFrameSizeFrom(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Applicable only when captureFilterFrameSizeEnable is enabled. The minimum range of the size of frame to be filtered.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterFrameSizeFrom'])
    @CaptureFilterFrameSizeFrom.setter
    def CaptureFilterFrameSizeFrom(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterFrameSizeFrom'], value)

    @property
    def CaptureFilterFrameSizeTo(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Applicable only when captureFilterFrameSizeEnable is enabled. The maximum range of the size of frame to be filtered.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterFrameSizeTo'])
    @CaptureFilterFrameSizeTo.setter
    def CaptureFilterFrameSizeTo(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterFrameSizeTo'], value)

    @property
    def CaptureFilterPattern(self):
        # type: () -> str
        """
        Returns
        -------
        - str(anyPattern | notPattern1 | notPattern2 | pattern1 | pattern1AndPattern2 | pattern2): Applicable only when captureFilterEnable is set to true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterPattern'])
    @CaptureFilterPattern.setter
    def CaptureFilterPattern(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterPattern'], value)

    @property
    def CaptureFilterSA(self):
        # type: () -> str
        """
        Returns
        -------
        - str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2): One of two available destination MAC addresses to filter on. Applicable only when capturefilternable is set to true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterSA'])
    @CaptureFilterSA.setter
    def CaptureFilterSA(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterSA'], value)

    def update(self, CaptureFilterDA=None, CaptureFilterEnable=None, CaptureFilterError=None, CaptureFilterExpressionString=None, CaptureFilterFrameSizeEnable=None, CaptureFilterFrameSizeFrom=None, CaptureFilterFrameSizeTo=None, CaptureFilterPattern=None, CaptureFilterSA=None):
        # type: (str, bool, str, str, bool, int, int, str, str) -> Filter
        """Updates filter resource on the server.

        Args
        ----
        - CaptureFilterDA (str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2)): One of two available destination MAC addresses to filter on. Applicable only when capturefilternable is set to true.
        - CaptureFilterEnable (bool): Enables or disables the capture filter.
        - CaptureFilterError (str(errAnyFrame | errAnyIpTcpUdpChecksumError | errAnySequencekError | errBadCRC | errBadFrame | errBigSequenceError | errDataIntegrityError | errGoodFrame | errInvalidFcoeFrame | errReverseSequenceError | errSmallSequenceError)): Applicable only when captureFilterEnable is set to true.
        - CaptureFilterExpressionString (str): String composed of SA1, DA1, P1, P2, optionally negated with '!', and connected with operators 'and', 'or', 'xor', 'nand' or 'nor'. (Eg: {DA1 and SA1 or !P1 and P2} ). NOTE: The 'or', 'xor', 'nand' and 'nor' operators are available only on the following load modules: XMVDC, NGY, XMSP12, LAVA(MK), Xcellon AP, Xcellon NP.
        - CaptureFilterFrameSizeEnable (bool): Enables or disables the frame size constraint which specifies a range of frame.
        - CaptureFilterFrameSizeFrom (number): Applicable only when captureFilterFrameSizeEnable is enabled. The minimum range of the size of frame to be filtered.
        - CaptureFilterFrameSizeTo (number): Applicable only when captureFilterFrameSizeEnable is enabled. The maximum range of the size of frame to be filtered.
        - CaptureFilterPattern (str(anyPattern | notPattern1 | notPattern2 | pattern1 | pattern1AndPattern2 | pattern2)): Applicable only when captureFilterEnable is set to true.
        - CaptureFilterSA (str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2)): One of two available destination MAC addresses to filter on. Applicable only when capturefilternable is set to true.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, CaptureFilterDA=None, CaptureFilterEnable=None, CaptureFilterError=None, CaptureFilterExpressionString=None, CaptureFilterFrameSizeEnable=None, CaptureFilterFrameSizeFrom=None, CaptureFilterFrameSizeTo=None, CaptureFilterPattern=None, CaptureFilterSA=None):
        # type: (str, bool, str, str, bool, int, int, str, str) -> Filter
        """Finds and retrieves filter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve filter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all filter resources from the server.

        Args
        ----
        - CaptureFilterDA (str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2)): One of two available destination MAC addresses to filter on. Applicable only when capturefilternable is set to true.
        - CaptureFilterEnable (bool): Enables or disables the capture filter.
        - CaptureFilterError (str(errAnyFrame | errAnyIpTcpUdpChecksumError | errAnySequencekError | errBadCRC | errBadFrame | errBigSequenceError | errDataIntegrityError | errGoodFrame | errInvalidFcoeFrame | errReverseSequenceError | errSmallSequenceError)): Applicable only when captureFilterEnable is set to true.
        - CaptureFilterExpressionString (str): String composed of SA1, DA1, P1, P2, optionally negated with '!', and connected with operators 'and', 'or', 'xor', 'nand' or 'nor'. (Eg: {DA1 and SA1 or !P1 and P2} ). NOTE: The 'or', 'xor', 'nand' and 'nor' operators are available only on the following load modules: XMVDC, NGY, XMSP12, LAVA(MK), Xcellon AP, Xcellon NP.
        - CaptureFilterFrameSizeEnable (bool): Enables or disables the frame size constraint which specifies a range of frame.
        - CaptureFilterFrameSizeFrom (number): Applicable only when captureFilterFrameSizeEnable is enabled. The minimum range of the size of frame to be filtered.
        - CaptureFilterFrameSizeTo (number): Applicable only when captureFilterFrameSizeEnable is enabled. The maximum range of the size of frame to be filtered.
        - CaptureFilterPattern (str(anyPattern | notPattern1 | notPattern2 | pattern1 | pattern1AndPattern2 | pattern2)): Applicable only when captureFilterEnable is set to true.
        - CaptureFilterSA (str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2)): One of two available destination MAC addresses to filter on. Applicable only when capturefilternable is set to true.

        Returns
        -------
        - self: This instance with matching filter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of filter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the filter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
