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


class IsisAggregatedStatistics(Base):
    """Represents stats of ISIS Aggregated Statistics
    The IsisAggregatedStatistics class encapsulates a required isisAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "isisAggregatedStatistics"
    _SDM_ATT_MAP = {
        "Ipv4GroupRecordsLearned": "ipv4GroupRecordsLearned",
        "Ipv6GroupRecordsLearned": "ipv6GroupRecordsLearned",
        "L1CSNPRx": "l1CSNPRx",
        "L1CSNPTx": "l1CSNPTx",
        "L1DBSize": "l1DBSize",
        "L1FullStateCount": "l1FullStateCount",
        "L1HellosRx": "l1HellosRx",
        "L1HellosTx": "l1HellosTx",
        "L1InitStateCount": "l1InitStateCount",
        "L1LSPRx": "l1LSPRx",
        "L1LSPTx": "l1LSPTx",
        "L1Neighbors": "l1Neighbors",
        "L1PSNPRx": "l1PSNPRx",
        "L1PSNPTx": "l1PSNPTx",
        "L1PTPHellosRx": "l1PTPHellosRx",
        "L1PTPHellosTx": "l1PTPHellosTx",
        "L1SessConfigured": "l1SessConfigured",
        "L1SessUp": "l1SessUp",
        "L1SessionFlapCount": "l1SessionFlapCount",
        "L2CSNPRx": "l2CSNPRx",
        "L2CSNPTx": "l2CSNPTx",
        "L2DBSize": "l2DBSize",
        "L2FullStateCount": "l2FullStateCount",
        "L2HellosRx": "l2HellosRx",
        "L2HellosTx": "l2HellosTx",
        "L2InitStateCount": "l2InitStateCount",
        "L2LSPRx": "l2LSPRx",
        "L2LSPTx": "l2LSPTx",
        "L2Neighbors": "l2Neighbors",
        "L2PSNPRx": "l2PSNPRx",
        "L2PSNPTx": "l2PSNPTx",
        "L2PTPHellosRx": "l2PTPHellosRx",
        "L2PTPHellosTx": "l2PTPHellosTx",
        "L2SessConfigured": "l2SessConfigured",
        "L2SessUp": "l2SessUp",
        "L2SessionFlapCount": "l2SessionFlapCount",
        "MGROUPCSNPsRx": "mGROUPCSNPsRx",
        "MGROUPCSNPsTx": "mGROUPCSNPsTx",
        "MGROUPLSPRx": "mGROUPLSPRx",
        "MGROUPLSPTx": "mGROUPLSPTx",
        "MGROUPPSNPsRx": "mGROUPPSNPsRx",
        "MGROUPPSNPsTx": "mGROUPPSNPsTx",
        "MacGroupRecordsLearned": "macGroupRecordsLearned",
        "MulticastIPv4GroupRecordRx": "multicastIPv4GroupRecordRx",
        "MulticastIPv4GroupRecordTx": "multicastIPv4GroupRecordTx",
        "MulticastIPv6GroupRecordRx": "multicastIPv6GroupRecordRx",
        "MulticastIPv6GroupRecordTx": "multicastIPv6GroupRecordTx",
        "MulticastMACGroupRecordRx": "multicastMACGroupRecordRx",
        "MulticastMACGroupRecordTx": "multicastMACGroupRecordTx",
        "PortName": "portName",
        "RateControlBlockedSendingLSPMGROUP": "rateControlBlockedSendingLSPMGROUP",
        "RbchannelEchoReplyRx": "rbchannelEchoReplyRx",
        "RbchannelEchoReplyTx": "rbchannelEchoReplyTx",
        "RbchannelEchoRequestRx": "rbchannelEchoRequestRx",
        "RbchannelEchoRequestTx": "rbchannelEchoRequestTx",
        "RbchannelErrNotifRx": "rbchannelErrNotifRx",
        "RbchannelErrNotifTx": "rbchannelErrNotifTx",
        "RbchannelErrorRx": "rbchannelErrorRx",
        "RbchannelErrorTx": "rbchannelErrorTx",
        "RbchannelFramesRx": "rbchannelFramesRx",
        "RbchannelFramesTx": "rbchannelFramesTx",
        "RbridgesLearned": "rbridgesLearned",
        "UnicastMACGroupRecordRx": "unicastMACGroupRecordRx",
        "UnicastMACGroupRecordTx": "unicastMACGroupRecordTx",
        "UnicastMACRangesLearned": "unicastMACRangesLearned",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IsisAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def Ipv4GroupRecordsLearned(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Group Records Learned
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4GroupRecordsLearned"])

    @Ipv4GroupRecordsLearned.setter
    def Ipv4GroupRecordsLearned(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4GroupRecordsLearned"], value)

    @property
    def Ipv6GroupRecordsLearned(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv6 Group Records Learned
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv6GroupRecordsLearned"])

    @Ipv6GroupRecordsLearned.setter
    def Ipv6GroupRecordsLearned(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv6GroupRecordsLearned"], value)

    @property
    def L1CSNPRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 CSNP Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1CSNPRx"])

    @L1CSNPRx.setter
    def L1CSNPRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1CSNPRx"], value)

    @property
    def L1CSNPTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 CSNP Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1CSNPTx"])

    @L1CSNPTx.setter
    def L1CSNPTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1CSNPTx"], value)

    @property
    def L1DBSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 DB Size
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1DBSize"])

    @L1DBSize.setter
    def L1DBSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1DBSize"], value)

    @property
    def L1FullStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Full State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1FullStateCount"])

    @L1FullStateCount.setter
    def L1FullStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1FullStateCount"], value)

    @property
    def L1HellosRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Hellos Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1HellosRx"])

    @L1HellosRx.setter
    def L1HellosRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1HellosRx"], value)

    @property
    def L1HellosTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Hellos Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1HellosTx"])

    @L1HellosTx.setter
    def L1HellosTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1HellosTx"], value)

    @property
    def L1InitStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Init State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1InitStateCount"])

    @L1InitStateCount.setter
    def L1InitStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1InitStateCount"], value)

    @property
    def L1LSPRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 LSP Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1LSPRx"])

    @L1LSPRx.setter
    def L1LSPRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1LSPRx"], value)

    @property
    def L1LSPTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 LSP Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1LSPTx"])

    @L1LSPTx.setter
    def L1LSPTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1LSPTx"], value)

    @property
    def L1Neighbors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Neighbors
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1Neighbors"])

    @L1Neighbors.setter
    def L1Neighbors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1Neighbors"], value)

    @property
    def L1PSNPRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 PSNP Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1PSNPRx"])

    @L1PSNPRx.setter
    def L1PSNPRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1PSNPRx"], value)

    @property
    def L1PSNPTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 PSNP Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1PSNPTx"])

    @L1PSNPTx.setter
    def L1PSNPTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1PSNPTx"], value)

    @property
    def L1PTPHellosRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 PTP Hellos Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1PTPHellosRx"])

    @L1PTPHellosRx.setter
    def L1PTPHellosRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1PTPHellosRx"], value)

    @property
    def L1PTPHellosTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 PTP Hellos Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1PTPHellosTx"])

    @L1PTPHellosTx.setter
    def L1PTPHellosTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1PTPHellosTx"], value)

    @property
    def L1SessConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Sess. Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1SessConfigured"])

    @L1SessConfigured.setter
    def L1SessConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1SessConfigured"], value)

    @property
    def L1SessUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Sess. Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1SessUp"])

    @L1SessUp.setter
    def L1SessUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1SessUp"], value)

    @property
    def L1SessionFlapCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Session Flap Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1SessionFlapCount"])

    @L1SessionFlapCount.setter
    def L1SessionFlapCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1SessionFlapCount"], value)

    @property
    def L2CSNPRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 CSNP Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2CSNPRx"])

    @L2CSNPRx.setter
    def L2CSNPRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2CSNPRx"], value)

    @property
    def L2CSNPTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 CSNP Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2CSNPTx"])

    @L2CSNPTx.setter
    def L2CSNPTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2CSNPTx"], value)

    @property
    def L2DBSize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 DB Size
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2DBSize"])

    @L2DBSize.setter
    def L2DBSize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2DBSize"], value)

    @property
    def L2FullStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 Full State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2FullStateCount"])

    @L2FullStateCount.setter
    def L2FullStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2FullStateCount"], value)

    @property
    def L2HellosRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 Hellos Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2HellosRx"])

    @L2HellosRx.setter
    def L2HellosRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2HellosRx"], value)

    @property
    def L2HellosTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 Hellos Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2HellosTx"])

    @L2HellosTx.setter
    def L2HellosTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2HellosTx"], value)

    @property
    def L2InitStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 Init State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2InitStateCount"])

    @L2InitStateCount.setter
    def L2InitStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2InitStateCount"], value)

    @property
    def L2LSPRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 LSP Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2LSPRx"])

    @L2LSPRx.setter
    def L2LSPRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2LSPRx"], value)

    @property
    def L2LSPTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 LSP Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2LSPTx"])

    @L2LSPTx.setter
    def L2LSPTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2LSPTx"], value)

    @property
    def L2Neighbors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 Neighbors
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2Neighbors"])

    @L2Neighbors.setter
    def L2Neighbors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2Neighbors"], value)

    @property
    def L2PSNPRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 PSNP Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2PSNPRx"])

    @L2PSNPRx.setter
    def L2PSNPRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2PSNPRx"], value)

    @property
    def L2PSNPTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 PSNP Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2PSNPTx"])

    @L2PSNPTx.setter
    def L2PSNPTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2PSNPTx"], value)

    @property
    def L2PTPHellosRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 PTP Hellos Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2PTPHellosRx"])

    @L2PTPHellosRx.setter
    def L2PTPHellosRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2PTPHellosRx"], value)

    @property
    def L2PTPHellosTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 PTP Hellos Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2PTPHellosTx"])

    @L2PTPHellosTx.setter
    def L2PTPHellosTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2PTPHellosTx"], value)

    @property
    def L2SessConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 Sess. Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2SessConfigured"])

    @L2SessConfigured.setter
    def L2SessConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2SessConfigured"], value)

    @property
    def L2SessUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 Sess. Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2SessUp"])

    @L2SessUp.setter
    def L2SessUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2SessUp"], value)

    @property
    def L2SessionFlapCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L2 Session Flap Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["L2SessionFlapCount"])

    @L2SessionFlapCount.setter
    def L2SessionFlapCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L2SessionFlapCount"], value)

    @property
    def MGROUPCSNPsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: M-GROUP CSNPs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MGROUPCSNPsRx"])

    @MGROUPCSNPsRx.setter
    def MGROUPCSNPsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MGROUPCSNPsRx"], value)

    @property
    def MGROUPCSNPsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: M-GROUP CSNPs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MGROUPCSNPsTx"])

    @MGROUPCSNPsTx.setter
    def MGROUPCSNPsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MGROUPCSNPsTx"], value)

    @property
    def MGROUPLSPRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: M-GROUP LSP Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MGROUPLSPRx"])

    @MGROUPLSPRx.setter
    def MGROUPLSPRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MGROUPLSPRx"], value)

    @property
    def MGROUPLSPTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: M-GROUP LSP Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MGROUPLSPTx"])

    @MGROUPLSPTx.setter
    def MGROUPLSPTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MGROUPLSPTx"], value)

    @property
    def MGROUPPSNPsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: M-GROUP PSNPs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MGROUPPSNPsRx"])

    @MGROUPPSNPsRx.setter
    def MGROUPPSNPsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MGROUPPSNPsRx"], value)

    @property
    def MGROUPPSNPsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: M-GROUP PSNPs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MGROUPPSNPsTx"])

    @MGROUPPSNPsTx.setter
    def MGROUPPSNPsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MGROUPPSNPsTx"], value)

    @property
    def MacGroupRecordsLearned(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MAC Group Records Learned
        """
        return self._get_attribute(self._SDM_ATT_MAP["MacGroupRecordsLearned"])

    @MacGroupRecordsLearned.setter
    def MacGroupRecordsLearned(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MacGroupRecordsLearned"], value)

    @property
    def MulticastIPv4GroupRecordRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Multicast IPv4 Group Record Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastIPv4GroupRecordRx"])

    @MulticastIPv4GroupRecordRx.setter
    def MulticastIPv4GroupRecordRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastIPv4GroupRecordRx"], value)

    @property
    def MulticastIPv4GroupRecordTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Multicast IPv4 Group Record Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastIPv4GroupRecordTx"])

    @MulticastIPv4GroupRecordTx.setter
    def MulticastIPv4GroupRecordTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastIPv4GroupRecordTx"], value)

    @property
    def MulticastIPv6GroupRecordRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Multicast IPv6 Group Record Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastIPv6GroupRecordRx"])

    @MulticastIPv6GroupRecordRx.setter
    def MulticastIPv6GroupRecordRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastIPv6GroupRecordRx"], value)

    @property
    def MulticastIPv6GroupRecordTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Multicast IPv6 Group Record Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastIPv6GroupRecordTx"])

    @MulticastIPv6GroupRecordTx.setter
    def MulticastIPv6GroupRecordTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastIPv6GroupRecordTx"], value)

    @property
    def MulticastMACGroupRecordRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Multicast MAC Group Record Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastMACGroupRecordRx"])

    @MulticastMACGroupRecordRx.setter
    def MulticastMACGroupRecordRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastMACGroupRecordRx"], value)

    @property
    def MulticastMACGroupRecordTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Multicast MAC Group Record Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastMACGroupRecordTx"])

    @MulticastMACGroupRecordTx.setter
    def MulticastMACGroupRecordTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastMACGroupRecordTx"], value)

    @property
    def PortName(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Name
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortName"])

    @PortName.setter
    def PortName(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortName"], value)

    @property
    def RateControlBlockedSendingLSPMGROUP(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rate Control Blocked Sending LSP/MGROUP
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RateControlBlockedSendingLSPMGROUP"]
        )

    @RateControlBlockedSendingLSPMGROUP.setter
    def RateControlBlockedSendingLSPMGROUP(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RateControlBlockedSendingLSPMGROUP"], value
        )

    @property
    def RbchannelEchoReplyRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RBChannel Echo Reply Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RbchannelEchoReplyRx"])

    @RbchannelEchoReplyRx.setter
    def RbchannelEchoReplyRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RbchannelEchoReplyRx"], value)

    @property
    def RbchannelEchoReplyTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RBChannel Echo Reply Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RbchannelEchoReplyTx"])

    @RbchannelEchoReplyTx.setter
    def RbchannelEchoReplyTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RbchannelEchoReplyTx"], value)

    @property
    def RbchannelEchoRequestRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RBChannel Echo Request Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RbchannelEchoRequestRx"])

    @RbchannelEchoRequestRx.setter
    def RbchannelEchoRequestRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RbchannelEchoRequestRx"], value)

    @property
    def RbchannelEchoRequestTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RBChannel Echo Request Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RbchannelEchoRequestTx"])

    @RbchannelEchoRequestTx.setter
    def RbchannelEchoRequestTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RbchannelEchoRequestTx"], value)

    @property
    def RbchannelErrNotifRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RBChannel ErrNotif Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RbchannelErrNotifRx"])

    @RbchannelErrNotifRx.setter
    def RbchannelErrNotifRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RbchannelErrNotifRx"], value)

    @property
    def RbchannelErrNotifTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RBChannel ErrNotif Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RbchannelErrNotifTx"])

    @RbchannelErrNotifTx.setter
    def RbchannelErrNotifTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RbchannelErrNotifTx"], value)

    @property
    def RbchannelErrorRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RBChannel Error Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RbchannelErrorRx"])

    @RbchannelErrorRx.setter
    def RbchannelErrorRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RbchannelErrorRx"], value)

    @property
    def RbchannelErrorTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RBChannel Error Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RbchannelErrorTx"])

    @RbchannelErrorTx.setter
    def RbchannelErrorTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RbchannelErrorTx"], value)

    @property
    def RbchannelFramesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RBChannel Frames Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RbchannelFramesRx"])

    @RbchannelFramesRx.setter
    def RbchannelFramesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RbchannelFramesRx"], value)

    @property
    def RbchannelFramesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RBChannel Frames Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RbchannelFramesTx"])

    @RbchannelFramesTx.setter
    def RbchannelFramesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RbchannelFramesTx"], value)

    @property
    def RbridgesLearned(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RBridges Learned
        """
        return self._get_attribute(self._SDM_ATT_MAP["RbridgesLearned"])

    @RbridgesLearned.setter
    def RbridgesLearned(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RbridgesLearned"], value)

    @property
    def UnicastMACGroupRecordRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unicast MAC Group Record Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastMACGroupRecordRx"])

    @UnicastMACGroupRecordRx.setter
    def UnicastMACGroupRecordRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastMACGroupRecordRx"], value)

    @property
    def UnicastMACGroupRecordTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unicast MAC Group Record Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastMACGroupRecordTx"])

    @UnicastMACGroupRecordTx.setter
    def UnicastMACGroupRecordTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastMACGroupRecordTx"], value)

    @property
    def UnicastMACRangesLearned(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unicast MAC Ranges Learned
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnicastMACRangesLearned"])

    @UnicastMACRangesLearned.setter
    def UnicastMACRangesLearned(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnicastMACRangesLearned"], value)

    def update(
        self,
        Ipv4GroupRecordsLearned=None,
        Ipv6GroupRecordsLearned=None,
        L1CSNPRx=None,
        L1CSNPTx=None,
        L1DBSize=None,
        L1FullStateCount=None,
        L1HellosRx=None,
        L1HellosTx=None,
        L1InitStateCount=None,
        L1LSPRx=None,
        L1LSPTx=None,
        L1Neighbors=None,
        L1PSNPRx=None,
        L1PSNPTx=None,
        L1PTPHellosRx=None,
        L1PTPHellosTx=None,
        L1SessConfigured=None,
        L1SessUp=None,
        L1SessionFlapCount=None,
        L2CSNPRx=None,
        L2CSNPTx=None,
        L2DBSize=None,
        L2FullStateCount=None,
        L2HellosRx=None,
        L2HellosTx=None,
        L2InitStateCount=None,
        L2LSPRx=None,
        L2LSPTx=None,
        L2Neighbors=None,
        L2PSNPRx=None,
        L2PSNPTx=None,
        L2PTPHellosRx=None,
        L2PTPHellosTx=None,
        L2SessConfigured=None,
        L2SessUp=None,
        L2SessionFlapCount=None,
        MGROUPCSNPsRx=None,
        MGROUPCSNPsTx=None,
        MGROUPLSPRx=None,
        MGROUPLSPTx=None,
        MGROUPPSNPsRx=None,
        MGROUPPSNPsTx=None,
        MacGroupRecordsLearned=None,
        MulticastIPv4GroupRecordRx=None,
        MulticastIPv4GroupRecordTx=None,
        MulticastIPv6GroupRecordRx=None,
        MulticastIPv6GroupRecordTx=None,
        MulticastMACGroupRecordRx=None,
        MulticastMACGroupRecordTx=None,
        PortName=None,
        RateControlBlockedSendingLSPMGROUP=None,
        RbchannelEchoReplyRx=None,
        RbchannelEchoReplyTx=None,
        RbchannelEchoRequestRx=None,
        RbchannelEchoRequestTx=None,
        RbchannelErrNotifRx=None,
        RbchannelErrNotifTx=None,
        RbchannelErrorRx=None,
        RbchannelErrorTx=None,
        RbchannelFramesRx=None,
        RbchannelFramesTx=None,
        RbridgesLearned=None,
        UnicastMACGroupRecordRx=None,
        UnicastMACGroupRecordTx=None,
        UnicastMACRangesLearned=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> IsisAggregatedStatistics
        """Updates isisAggregatedStatistics resource on the server.

        Args
        ----
        - Ipv4GroupRecordsLearned (bool): IPv4 Group Records Learned
        - Ipv6GroupRecordsLearned (bool): IPv6 Group Records Learned
        - L1CSNPRx (bool): L1 CSNP Rx
        - L1CSNPTx (bool): L1 CSNP Tx
        - L1DBSize (bool): L1 DB Size
        - L1FullStateCount (bool): L1 Full State Count
        - L1HellosRx (bool): L1 Hellos Rx
        - L1HellosTx (bool): L1 Hellos Tx
        - L1InitStateCount (bool): L1 Init State Count
        - L1LSPRx (bool): L1 LSP Rx
        - L1LSPTx (bool): L1 LSP Tx
        - L1Neighbors (bool): L1 Neighbors
        - L1PSNPRx (bool): L1 PSNP Rx
        - L1PSNPTx (bool): L1 PSNP Tx
        - L1PTPHellosRx (bool): L1 PTP Hellos Rx
        - L1PTPHellosTx (bool): L1 PTP Hellos Tx
        - L1SessConfigured (bool): L1 Sess. Configured
        - L1SessUp (bool): L1 Sess. Up
        - L1SessionFlapCount (bool): L1 Session Flap Count
        - L2CSNPRx (bool): L2 CSNP Rx
        - L2CSNPTx (bool): L2 CSNP Tx
        - L2DBSize (bool): L2 DB Size
        - L2FullStateCount (bool): L2 Full State Count
        - L2HellosRx (bool): L2 Hellos Rx
        - L2HellosTx (bool): L2 Hellos Tx
        - L2InitStateCount (bool): L2 Init State Count
        - L2LSPRx (bool): L2 LSP Rx
        - L2LSPTx (bool): L2 LSP Tx
        - L2Neighbors (bool): L2 Neighbors
        - L2PSNPRx (bool): L2 PSNP Rx
        - L2PSNPTx (bool): L2 PSNP Tx
        - L2PTPHellosRx (bool): L2 PTP Hellos Rx
        - L2PTPHellosTx (bool): L2 PTP Hellos Tx
        - L2SessConfigured (bool): L2 Sess. Configured
        - L2SessUp (bool): L2 Sess. Up
        - L2SessionFlapCount (bool): L2 Session Flap Count
        - MGROUPCSNPsRx (bool): M-GROUP CSNPs Rx
        - MGROUPCSNPsTx (bool): M-GROUP CSNPs Tx
        - MGROUPLSPRx (bool): M-GROUP LSP Rx
        - MGROUPLSPTx (bool): M-GROUP LSP Tx
        - MGROUPPSNPsRx (bool): M-GROUP PSNPs Rx
        - MGROUPPSNPsTx (bool): M-GROUP PSNPs Tx
        - MacGroupRecordsLearned (bool): MAC Group Records Learned
        - MulticastIPv4GroupRecordRx (bool): Multicast IPv4 Group Record Rx
        - MulticastIPv4GroupRecordTx (bool): Multicast IPv4 Group Record Tx
        - MulticastIPv6GroupRecordRx (bool): Multicast IPv6 Group Record Rx
        - MulticastIPv6GroupRecordTx (bool): Multicast IPv6 Group Record Tx
        - MulticastMACGroupRecordRx (bool): Multicast MAC Group Record Rx
        - MulticastMACGroupRecordTx (bool): Multicast MAC Group Record Tx
        - PortName (bool): Port Name
        - RateControlBlockedSendingLSPMGROUP (bool): Rate Control Blocked Sending LSP/MGROUP
        - RbchannelEchoReplyRx (bool): RBChannel Echo Reply Rx
        - RbchannelEchoReplyTx (bool): RBChannel Echo Reply Tx
        - RbchannelEchoRequestRx (bool): RBChannel Echo Request Rx
        - RbchannelEchoRequestTx (bool): RBChannel Echo Request Tx
        - RbchannelErrNotifRx (bool): RBChannel ErrNotif Rx
        - RbchannelErrNotifTx (bool): RBChannel ErrNotif Tx
        - RbchannelErrorRx (bool): RBChannel Error Rx
        - RbchannelErrorTx (bool): RBChannel Error Tx
        - RbchannelFramesRx (bool): RBChannel Frames Rx
        - RbchannelFramesTx (bool): RBChannel Frames Tx
        - RbridgesLearned (bool): RBridges Learned
        - UnicastMACGroupRecordRx (bool): Unicast MAC Group Record Rx
        - UnicastMACGroupRecordTx (bool): Unicast MAC Group Record Tx
        - UnicastMACRangesLearned (bool): Unicast MAC Ranges Learned

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Ipv4GroupRecordsLearned=None,
        Ipv6GroupRecordsLearned=None,
        L1CSNPRx=None,
        L1CSNPTx=None,
        L1DBSize=None,
        L1FullStateCount=None,
        L1HellosRx=None,
        L1HellosTx=None,
        L1InitStateCount=None,
        L1LSPRx=None,
        L1LSPTx=None,
        L1Neighbors=None,
        L1PSNPRx=None,
        L1PSNPTx=None,
        L1PTPHellosRx=None,
        L1PTPHellosTx=None,
        L1SessConfigured=None,
        L1SessUp=None,
        L1SessionFlapCount=None,
        L2CSNPRx=None,
        L2CSNPTx=None,
        L2DBSize=None,
        L2FullStateCount=None,
        L2HellosRx=None,
        L2HellosTx=None,
        L2InitStateCount=None,
        L2LSPRx=None,
        L2LSPTx=None,
        L2Neighbors=None,
        L2PSNPRx=None,
        L2PSNPTx=None,
        L2PTPHellosRx=None,
        L2PTPHellosTx=None,
        L2SessConfigured=None,
        L2SessUp=None,
        L2SessionFlapCount=None,
        MGROUPCSNPsRx=None,
        MGROUPCSNPsTx=None,
        MGROUPLSPRx=None,
        MGROUPLSPTx=None,
        MGROUPPSNPsRx=None,
        MGROUPPSNPsTx=None,
        MacGroupRecordsLearned=None,
        MulticastIPv4GroupRecordRx=None,
        MulticastIPv4GroupRecordTx=None,
        MulticastIPv6GroupRecordRx=None,
        MulticastIPv6GroupRecordTx=None,
        MulticastMACGroupRecordRx=None,
        MulticastMACGroupRecordTx=None,
        PortName=None,
        RateControlBlockedSendingLSPMGROUP=None,
        RbchannelEchoReplyRx=None,
        RbchannelEchoReplyTx=None,
        RbchannelEchoRequestRx=None,
        RbchannelEchoRequestTx=None,
        RbchannelErrNotifRx=None,
        RbchannelErrNotifTx=None,
        RbchannelErrorRx=None,
        RbchannelErrorTx=None,
        RbchannelFramesRx=None,
        RbchannelFramesTx=None,
        RbridgesLearned=None,
        UnicastMACGroupRecordRx=None,
        UnicastMACGroupRecordTx=None,
        UnicastMACRangesLearned=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> IsisAggregatedStatistics
        """Finds and retrieves isisAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisAggregatedStatistics resources from the server.

        Args
        ----
        - Ipv4GroupRecordsLearned (bool): IPv4 Group Records Learned
        - Ipv6GroupRecordsLearned (bool): IPv6 Group Records Learned
        - L1CSNPRx (bool): L1 CSNP Rx
        - L1CSNPTx (bool): L1 CSNP Tx
        - L1DBSize (bool): L1 DB Size
        - L1FullStateCount (bool): L1 Full State Count
        - L1HellosRx (bool): L1 Hellos Rx
        - L1HellosTx (bool): L1 Hellos Tx
        - L1InitStateCount (bool): L1 Init State Count
        - L1LSPRx (bool): L1 LSP Rx
        - L1LSPTx (bool): L1 LSP Tx
        - L1Neighbors (bool): L1 Neighbors
        - L1PSNPRx (bool): L1 PSNP Rx
        - L1PSNPTx (bool): L1 PSNP Tx
        - L1PTPHellosRx (bool): L1 PTP Hellos Rx
        - L1PTPHellosTx (bool): L1 PTP Hellos Tx
        - L1SessConfigured (bool): L1 Sess. Configured
        - L1SessUp (bool): L1 Sess. Up
        - L1SessionFlapCount (bool): L1 Session Flap Count
        - L2CSNPRx (bool): L2 CSNP Rx
        - L2CSNPTx (bool): L2 CSNP Tx
        - L2DBSize (bool): L2 DB Size
        - L2FullStateCount (bool): L2 Full State Count
        - L2HellosRx (bool): L2 Hellos Rx
        - L2HellosTx (bool): L2 Hellos Tx
        - L2InitStateCount (bool): L2 Init State Count
        - L2LSPRx (bool): L2 LSP Rx
        - L2LSPTx (bool): L2 LSP Tx
        - L2Neighbors (bool): L2 Neighbors
        - L2PSNPRx (bool): L2 PSNP Rx
        - L2PSNPTx (bool): L2 PSNP Tx
        - L2PTPHellosRx (bool): L2 PTP Hellos Rx
        - L2PTPHellosTx (bool): L2 PTP Hellos Tx
        - L2SessConfigured (bool): L2 Sess. Configured
        - L2SessUp (bool): L2 Sess. Up
        - L2SessionFlapCount (bool): L2 Session Flap Count
        - MGROUPCSNPsRx (bool): M-GROUP CSNPs Rx
        - MGROUPCSNPsTx (bool): M-GROUP CSNPs Tx
        - MGROUPLSPRx (bool): M-GROUP LSP Rx
        - MGROUPLSPTx (bool): M-GROUP LSP Tx
        - MGROUPPSNPsRx (bool): M-GROUP PSNPs Rx
        - MGROUPPSNPsTx (bool): M-GROUP PSNPs Tx
        - MacGroupRecordsLearned (bool): MAC Group Records Learned
        - MulticastIPv4GroupRecordRx (bool): Multicast IPv4 Group Record Rx
        - MulticastIPv4GroupRecordTx (bool): Multicast IPv4 Group Record Tx
        - MulticastIPv6GroupRecordRx (bool): Multicast IPv6 Group Record Rx
        - MulticastIPv6GroupRecordTx (bool): Multicast IPv6 Group Record Tx
        - MulticastMACGroupRecordRx (bool): Multicast MAC Group Record Rx
        - MulticastMACGroupRecordTx (bool): Multicast MAC Group Record Tx
        - PortName (bool): Port Name
        - RateControlBlockedSendingLSPMGROUP (bool): Rate Control Blocked Sending LSP/MGROUP
        - RbchannelEchoReplyRx (bool): RBChannel Echo Reply Rx
        - RbchannelEchoReplyTx (bool): RBChannel Echo Reply Tx
        - RbchannelEchoRequestRx (bool): RBChannel Echo Request Rx
        - RbchannelEchoRequestTx (bool): RBChannel Echo Request Tx
        - RbchannelErrNotifRx (bool): RBChannel ErrNotif Rx
        - RbchannelErrNotifTx (bool): RBChannel ErrNotif Tx
        - RbchannelErrorRx (bool): RBChannel Error Rx
        - RbchannelErrorTx (bool): RBChannel Error Tx
        - RbchannelFramesRx (bool): RBChannel Frames Rx
        - RbchannelFramesTx (bool): RBChannel Frames Tx
        - RbridgesLearned (bool): RBridges Learned
        - UnicastMACGroupRecordRx (bool): Unicast MAC Group Record Rx
        - UnicastMACGroupRecordTx (bool): Unicast MAC Group Record Tx
        - UnicastMACRangesLearned (bool): Unicast MAC Ranges Learned

        Returns
        -------
        - self: This instance with matching isisAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
