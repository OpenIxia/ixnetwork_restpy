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


class Impairment(Base):
    """
    The Impairment class encapsulates a required impairment resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "impairment"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Impairment, self).__init__(parent, list_op)

    @property
    def LlrAckNackSequence(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llracknacksequence.llracknacksequence.LlrAckNackSequence): An instance of the LlrAckNackSequence class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llracknacksequence.llracknacksequence import (
            LlrAckNackSequence,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LlrAckNackSequence", None) is not None:
                return self._properties.get("LlrAckNackSequence")
        return LlrAckNackSequence(self)._select()

    @property
    def LlrAckSequenceFreeze(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llracksequencefreeze.llracksequencefreeze.LlrAckSequenceFreeze): An instance of the LlrAckSequenceFreeze class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llracksequencefreeze.llracksequencefreeze import (
            LlrAckSequenceFreeze,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LlrAckSequenceFreeze", None) is not None:
                return self._properties.get("LlrAckSequenceFreeze")
        return LlrAckSequenceFreeze(self)._select()

    @property
    def LlrFrameCrcError(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llrframecrcerror.llrframecrcerror.LlrFrameCrcError): An instance of the LlrFrameCrcError class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llrframecrcerror.llrframecrcerror import (
            LlrFrameCrcError,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LlrFrameCrcError", None) is not None:
                return self._properties.get("LlrFrameCrcError")
        return LlrFrameCrcError(self)._select()

    @property
    def LlrFramePoisonedCrc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llrframepoisonedcrc.llrframepoisonedcrc.LlrFramePoisonedCrc): An instance of the LlrFramePoisonedCrc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llrframepoisonedcrc.llrframepoisonedcrc import (
            LlrFramePoisonedCrc,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LlrFramePoisonedCrc", None) is not None:
                return self._properties.get("LlrFramePoisonedCrc")
        return LlrFramePoisonedCrc(self)._select()

    @property
    def LlrFrameSeqJump(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llrframeseqjump.llrframeseqjump.LlrFrameSeqJump): An instance of the LlrFrameSeqJump class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llrframeseqjump.llrframeseqjump import (
            LlrFrameSeqJump,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LlrFrameSeqJump", None) is not None:
                return self._properties.get("LlrFrameSeqJump")
        return LlrFrameSeqJump(self)._select()

    @property
    def LlrInitEchoError(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llrinitechoerror.llrinitechoerror.LlrInitEchoError): An instance of the LlrInitEchoError class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llrinitechoerror.llrinitechoerror import (
            LlrInitEchoError,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LlrInitEchoError", None) is not None:
                return self._properties.get("LlrInitEchoError")
        return LlrInitEchoError(self)._select()

    @property
    def LlrRxFrameDrop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llrrxframedrop.llrrxframedrop.LlrRxFrameDrop): An instance of the LlrRxFrameDrop class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llrrxframedrop.llrrxframedrop import (
            LlrRxFrameDrop,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LlrRxFrameDrop", None) is not None:
                return self._properties.get("LlrRxFrameDrop")
        return LlrRxFrameDrop(self)._select()

    @property
    def LlrTxForceReplay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llrtxforcereplay.llrtxforcereplay.LlrTxForceReplay): An instance of the LlrTxForceReplay class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.llrtxforcereplay.llrtxforcereplay import (
            LlrTxForceReplay,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LlrTxForceReplay", None) is not None:
                return self._properties.get("LlrTxForceReplay")
        return LlrTxForceReplay(self)._select()

    @property
    def RxCtlOSDrop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.rxctlosdrop.rxctlosdrop.RxCtlOSDrop): An instance of the RxCtlOSDrop class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.rxctlosdrop.rxctlosdrop import (
            RxCtlOSDrop,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RxCtlOSDrop", None) is not None:
                return self._properties.get("RxCtlOSDrop")
        return RxCtlOSDrop(self)._select()

    @property
    def TxCtlOSDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.txctlosdelay.txctlosdelay.TxCtlOSDelay): An instance of the TxCtlOSDelay class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.txctlosdelay.txctlosdelay import (
            TxCtlOSDelay,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TxCtlOSDelay", None) is not None:
                return self._properties.get("TxCtlOSDelay")
        return TxCtlOSDelay(self)._select()

    @property
    def TxCtlOSDrop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.txctlosdrop.txctlosdrop.TxCtlOSDrop): An instance of the TxCtlOSDrop class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.ultraethernet.impairment.txctlosdrop.txctlosdrop import (
            TxCtlOSDrop,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TxCtlOSDrop", None) is not None:
                return self._properties.get("TxCtlOSDrop")
        return TxCtlOSDrop(self)._select()

    def find(self):
        """Finds and retrieves impairment resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve impairment resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all impairment resources from the server.

        Returns
        -------
        - self: This instance with matching impairment resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of impairment data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the impairment resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
