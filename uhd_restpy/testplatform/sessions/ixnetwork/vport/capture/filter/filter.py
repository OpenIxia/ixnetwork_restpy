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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


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

    def __init__(self, parent):
        super(Filter, self).__init__(parent)

    @property
    def CaptureFilterDA(self):
        """
        Returns
        -------
        - str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2): One of two available destination MAC addresses to filter on. Applicable only when capturefilternable is set to true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterDA'])
    @CaptureFilterDA.setter
    def CaptureFilterDA(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterDA'], value)

    @property
    def CaptureFilterEnable(self):
        """
        Returns
        -------
        - bool: Enables or disables the capture filter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterEnable'])
    @CaptureFilterEnable.setter
    def CaptureFilterEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterEnable'], value)

    @property
    def CaptureFilterError(self):
        """
        Returns
        -------
        - str(errAnyFrame | errAnyIpTcpUdpChecksumError | errAnySequencekError | errBadCRC | errBadFrame | errBigSequenceError | errDataIntegrityError | errGoodFrame | errInvalidFcoeFrame | errReverseSequenceError | errSmallSequenceError): Applicable only when captureFilterEnable is set to true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterError'])
    @CaptureFilterError.setter
    def CaptureFilterError(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterError'], value)

    @property
    def CaptureFilterExpressionString(self):
        """
        Returns
        -------
        - str: String composed of SA1, DA1, P1, P2, optionally negated with '!', and connected with operators 'and', 'or', 'xor', 'nand' or 'nor'. (Eg: {DA1 and SA1 or !P1 and P2} ). NOTE: The 'or', 'xor', 'nand' and 'nor' operators are available only on the following load modules: XMVDC, NGY, XMSP12, LAVA(MK), Xcellon AP, Xcellon NP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterExpressionString'])
    @CaptureFilterExpressionString.setter
    def CaptureFilterExpressionString(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterExpressionString'], value)

    @property
    def CaptureFilterFrameSizeEnable(self):
        """
        Returns
        -------
        - bool: Enables or disables the frame size constraint which specifies a range of frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterFrameSizeEnable'])
    @CaptureFilterFrameSizeEnable.setter
    def CaptureFilterFrameSizeEnable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterFrameSizeEnable'], value)

    @property
    def CaptureFilterFrameSizeFrom(self):
        """
        Returns
        -------
        - number: Applicable only when captureFilterFrameSizeEnable is enabled. The minimum range of the size of frame to be filtered.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterFrameSizeFrom'])
    @CaptureFilterFrameSizeFrom.setter
    def CaptureFilterFrameSizeFrom(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterFrameSizeFrom'], value)

    @property
    def CaptureFilterFrameSizeTo(self):
        """
        Returns
        -------
        - number: Applicable only when captureFilterFrameSizeEnable is enabled. The maximum range of the size of frame to be filtered.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterFrameSizeTo'])
    @CaptureFilterFrameSizeTo.setter
    def CaptureFilterFrameSizeTo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterFrameSizeTo'], value)

    @property
    def CaptureFilterPattern(self):
        """
        Returns
        -------
        - str(anyPattern | notPattern1 | notPattern2 | pattern1 | pattern1AndPattern2 | pattern2): Applicable only when captureFilterEnable is set to true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterPattern'])
    @CaptureFilterPattern.setter
    def CaptureFilterPattern(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterPattern'], value)

    @property
    def CaptureFilterSA(self):
        """
        Returns
        -------
        - str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2): One of two available destination MAC addresses to filter on. Applicable only when capturefilternable is set to true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaptureFilterSA'])
    @CaptureFilterSA.setter
    def CaptureFilterSA(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CaptureFilterSA'], value)

    def update(self, CaptureFilterDA=None, CaptureFilterEnable=None, CaptureFilterError=None, CaptureFilterExpressionString=None, CaptureFilterFrameSizeEnable=None, CaptureFilterFrameSizeFrom=None, CaptureFilterFrameSizeTo=None, CaptureFilterPattern=None, CaptureFilterSA=None):
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
