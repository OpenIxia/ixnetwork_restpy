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


class Pcsfilters(Base):
    """
    The Pcsfilters class encapsulates a required pcsfilters resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "pcsfilters"
    _SDM_ATT_MAP = {
        "PcsError": "pcsError",
        "StdPreamble": "stdPreamble",
        "UeCfUpdate": "ueCfUpdate",
        "UeCtlosSpacingError": "ueCtlosSpacingError",
        "UeLlrAck": "ueLlrAck",
        "UeLlrInit": "ueLlrInit",
        "UeLlrInitEcho": "ueLlrInitEcho",
        "UeLlrNack": "ueLlrNack",
        "UeLlrPreamble": "ueLlrPreamble",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Pcsfilters, self).__init__(parent, list_op)

    @property
    def PcsError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Error
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsError"])

    @PcsError.setter
    def PcsError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsError"], value)

    @property
    def StdPreamble(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Standard Preamble
        """
        return self._get_attribute(self._SDM_ATT_MAP["StdPreamble"])

    @StdPreamble.setter
    def StdPreamble(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StdPreamble"], value)

    @property
    def UeCfUpdate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CF_Update
        """
        return self._get_attribute(self._SDM_ATT_MAP["UeCfUpdate"])

    @UeCfUpdate.setter
    def UeCfUpdate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UeCfUpdate"], value)

    @property
    def UeCtlosSpacingError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: UE CtlOS Spacing Error
        """
        return self._get_attribute(self._SDM_ATT_MAP["UeCtlosSpacingError"])

    @UeCtlosSpacingError.setter
    def UeCtlosSpacingError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UeCtlosSpacingError"], value)

    @property
    def UeLlrAck(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LLR_ACK
        """
        return self._get_attribute(self._SDM_ATT_MAP["UeLlrAck"])

    @UeLlrAck.setter
    def UeLlrAck(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UeLlrAck"], value)

    @property
    def UeLlrInit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LLR_INIT
        """
        return self._get_attribute(self._SDM_ATT_MAP["UeLlrInit"])

    @UeLlrInit.setter
    def UeLlrInit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UeLlrInit"], value)

    @property
    def UeLlrInitEcho(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LLR_INIT_ECHO
        """
        return self._get_attribute(self._SDM_ATT_MAP["UeLlrInitEcho"])

    @UeLlrInitEcho.setter
    def UeLlrInitEcho(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UeLlrInitEcho"], value)

    @property
    def UeLlrNack(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LLR_NACK
        """
        return self._get_attribute(self._SDM_ATT_MAP["UeLlrNack"])

    @UeLlrNack.setter
    def UeLlrNack(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UeLlrNack"], value)

    @property
    def UeLlrPreamble(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LLR Preamble
        """
        return self._get_attribute(self._SDM_ATT_MAP["UeLlrPreamble"])

    @UeLlrPreamble.setter
    def UeLlrPreamble(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UeLlrPreamble"], value)

    def update(
        self,
        PcsError=None,
        StdPreamble=None,
        UeCfUpdate=None,
        UeCtlosSpacingError=None,
        UeLlrAck=None,
        UeLlrInit=None,
        UeLlrInitEcho=None,
        UeLlrNack=None,
        UeLlrPreamble=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool) -> Pcsfilters
        """Updates pcsfilters resource on the server.

        Args
        ----
        - PcsError (bool): PCS Error
        - StdPreamble (bool): Standard Preamble
        - UeCfUpdate (bool): CF_Update
        - UeCtlosSpacingError (bool): UE CtlOS Spacing Error
        - UeLlrAck (bool): LLR_ACK
        - UeLlrInit (bool): LLR_INIT
        - UeLlrInitEcho (bool): LLR_INIT_ECHO
        - UeLlrNack (bool): LLR_NACK
        - UeLlrPreamble (bool): LLR Preamble

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        PcsError=None,
        StdPreamble=None,
        UeCfUpdate=None,
        UeCtlosSpacingError=None,
        UeLlrAck=None,
        UeLlrInit=None,
        UeLlrInitEcho=None,
        UeLlrNack=None,
        UeLlrPreamble=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool) -> Pcsfilters
        """Finds and retrieves pcsfilters resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pcsfilters resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pcsfilters resources from the server.

        Args
        ----
        - PcsError (bool): PCS Error
        - StdPreamble (bool): Standard Preamble
        - UeCfUpdate (bool): CF_Update
        - UeCtlosSpacingError (bool): UE CtlOS Spacing Error
        - UeLlrAck (bool): LLR_ACK
        - UeLlrInit (bool): LLR_INIT
        - UeLlrInitEcho (bool): LLR_INIT_ECHO
        - UeLlrNack (bool): LLR_NACK
        - UeLlrPreamble (bool): LLR Preamble

        Returns
        -------
        - self: This instance with matching pcsfilters resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pcsfilters data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pcsfilters resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
