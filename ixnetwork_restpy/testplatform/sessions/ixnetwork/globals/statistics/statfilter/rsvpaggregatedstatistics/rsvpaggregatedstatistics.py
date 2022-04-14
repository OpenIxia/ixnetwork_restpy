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


class RsvpAggregatedStatistics(Base):
    """Represents stats of RSVP Aggregated Statistics
    The RsvpAggregatedStatistics class encapsulates a required rsvpAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "rsvpAggregatedStatistics"
    _SDM_ATT_MAP = {
        "AcksRx": "acksRx",
        "AcksTx": "acksTx",
        "BundleMessagesRx": "bundleMessagesRx",
        "BundleMessagesTx": "bundleMessagesTx",
        "DownStateCount": "downStateCount",
        "EgressLSPsUp": "egressLSPsUp",
        "EgressOutofOrderMsgsRx": "egressOutofOrderMsgsRx",
        "EgressSubLSPsUp": "egressSubLSPsUp",
        "HellosRx": "hellosRx",
        "HellosTx": "hellosTx",
        "IngressLSPsConfigured": "ingressLSPsConfigured",
        "IngressLSPsUp": "ingressLSPsUp",
        "IngressSubLSPsConfigured": "ingressSubLSPsConfigured",
        "IngressSubLSPsUp": "ingressSubLSPsUp",
        "NacksRx": "nacksRx",
        "NacksTx": "nacksTx",
        "NumberofPathReOptimizations": "numberofPathReOptimizations",
        "OwnGracefulRestarts": "ownGracefulRestarts",
        "PathERRsRx": "pathERRsRx",
        "PathERRsTx": "pathERRsTx",
        "PathLifetimeExpirations": "pathLifetimeExpirations",
        "PathReevaluationRequestTx": "pathReevaluationRequestTx",
        "PathSentStateCount": "pathSentStateCount",
        "PathTearsRx": "pathTearsRx",
        "PathTearsTx": "pathTearsTx",
        "PathsRx": "pathsRx",
        "PathsTx": "pathsTx",
        "PathswithRecoveryLabelRx": "pathswithRecoveryLabelRx",
        "PathswithRecoveryLabelTx": "pathswithRecoveryLabelTx",
        "PeerGracefulRestarts": "peerGracefulRestarts",
        "PortName": "portName",
        "RateControlBlockedLSPSetup": "rateControlBlockedLSPSetup",
        "ResvCONFsRx": "resvCONFsRx",
        "ResvCONFsTx": "resvCONFsTx",
        "ResvERRsRx": "resvERRsRx",
        "ResvERRsTx": "resvERRsTx",
        "ResvLifetimeExpirations": "resvLifetimeExpirations",
        "ResvTearsRx": "resvTearsRx",
        "ResvTearsTx": "resvTearsTx",
        "ResvsRx": "resvsRx",
        "ResvsTx": "resvsTx",
        "SessionFlapCount": "sessionFlapCount",
        "SrefreshsRx": "srefreshsRx",
        "SrefreshsTx": "srefreshsTx",
        "UnrecoveredRESVsDeleted": "unrecoveredRESVsDeleted",
        "UpStateCount": "upStateCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(RsvpAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def AcksRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ACKs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["AcksRx"])

    @AcksRx.setter
    def AcksRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AcksRx"], value)

    @property
    def AcksTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ACKs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["AcksTx"])

    @AcksTx.setter
    def AcksTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AcksTx"], value)

    @property
    def BundleMessagesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bundle Messages Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["BundleMessagesRx"])

    @BundleMessagesRx.setter
    def BundleMessagesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BundleMessagesRx"], value)

    @property
    def BundleMessagesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bundle Messages Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["BundleMessagesTx"])

    @BundleMessagesTx.setter
    def BundleMessagesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BundleMessagesTx"], value)

    @property
    def DownStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Down State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownStateCount"])

    @DownStateCount.setter
    def DownStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DownStateCount"], value)

    @property
    def EgressLSPsUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Egress LSPs Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["EgressLSPsUp"])

    @EgressLSPsUp.setter
    def EgressLSPsUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EgressLSPsUp"], value)

    @property
    def EgressOutofOrderMsgsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Egress Out of Order Msgs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EgressOutofOrderMsgsRx"])

    @EgressOutofOrderMsgsRx.setter
    def EgressOutofOrderMsgsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EgressOutofOrderMsgsRx"], value)

    @property
    def EgressSubLSPsUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Egress SubLSPs Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["EgressSubLSPsUp"])

    @EgressSubLSPsUp.setter
    def EgressSubLSPsUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EgressSubLSPsUp"], value)

    @property
    def HellosRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: HELLOs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HellosRx"])

    @HellosRx.setter
    def HellosRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HellosRx"], value)

    @property
    def HellosTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: HELLOs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HellosTx"])

    @HellosTx.setter
    def HellosTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HellosTx"], value)

    @property
    def IngressLSPsConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ingress LSPs Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["IngressLSPsConfigured"])

    @IngressLSPsConfigured.setter
    def IngressLSPsConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IngressLSPsConfigured"], value)

    @property
    def IngressLSPsUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ingress LSPs Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["IngressLSPsUp"])

    @IngressLSPsUp.setter
    def IngressLSPsUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IngressLSPsUp"], value)

    @property
    def IngressSubLSPsConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ingress SubLSPs Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["IngressSubLSPsConfigured"])

    @IngressSubLSPsConfigured.setter
    def IngressSubLSPsConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IngressSubLSPsConfigured"], value)

    @property
    def IngressSubLSPsUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ingress SubLSPs Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["IngressSubLSPsUp"])

    @IngressSubLSPsUp.setter
    def IngressSubLSPsUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IngressSubLSPsUp"], value)

    @property
    def NacksRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NACKs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["NacksRx"])

    @NacksRx.setter
    def NacksRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NacksRx"], value)

    @property
    def NacksTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NACKs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["NacksTx"])

    @NacksTx.setter
    def NacksTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NacksTx"], value)

    @property
    def NumberofPathReOptimizations(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Number of Path Re-Optimizations
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberofPathReOptimizations"])

    @NumberofPathReOptimizations.setter
    def NumberofPathReOptimizations(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberofPathReOptimizations"], value)

    @property
    def OwnGracefulRestarts(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Own Graceful-Restarts
        """
        return self._get_attribute(self._SDM_ATT_MAP["OwnGracefulRestarts"])

    @OwnGracefulRestarts.setter
    def OwnGracefulRestarts(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OwnGracefulRestarts"], value)

    @property
    def PathERRsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path-ERRs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathERRsRx"])

    @PathERRsRx.setter
    def PathERRsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathERRsRx"], value)

    @property
    def PathERRsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path-ERRs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathERRsTx"])

    @PathERRsTx.setter
    def PathERRsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathERRsTx"], value)

    @property
    def PathLifetimeExpirations(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PATH Lifetime Expirations
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathLifetimeExpirations"])

    @PathLifetimeExpirations.setter
    def PathLifetimeExpirations(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathLifetimeExpirations"], value)

    @property
    def PathReevaluationRequestTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path Re-evaluation Request Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathReevaluationRequestTx"])

    @PathReevaluationRequestTx.setter
    def PathReevaluationRequestTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathReevaluationRequestTx"], value)

    @property
    def PathSentStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path Sent State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathSentStateCount"])

    @PathSentStateCount.setter
    def PathSentStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathSentStateCount"], value)

    @property
    def PathTearsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path Tears Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathTearsRx"])

    @PathTearsRx.setter
    def PathTearsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathTearsRx"], value)

    @property
    def PathTearsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path Tears Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathTearsTx"])

    @PathTearsTx.setter
    def PathTearsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathTearsTx"], value)

    @property
    def PathsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Paths Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathsRx"])

    @PathsRx.setter
    def PathsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathsRx"], value)

    @property
    def PathsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Paths Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathsTx"])

    @PathsTx.setter
    def PathsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathsTx"], value)

    @property
    def PathswithRecoveryLabelRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Paths with Recovery-Label Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathswithRecoveryLabelRx"])

    @PathswithRecoveryLabelRx.setter
    def PathswithRecoveryLabelRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathswithRecoveryLabelRx"], value)

    @property
    def PathswithRecoveryLabelTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Paths with Recovery-Label Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathswithRecoveryLabelTx"])

    @PathswithRecoveryLabelTx.setter
    def PathswithRecoveryLabelTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathswithRecoveryLabelTx"], value)

    @property
    def PeerGracefulRestarts(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Peer Graceful-Restarts
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerGracefulRestarts"])

    @PeerGracefulRestarts.setter
    def PeerGracefulRestarts(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PeerGracefulRestarts"], value)

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
    def RateControlBlockedLSPSetup(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rate Control Blocked LSP Setup
        """
        return self._get_attribute(self._SDM_ATT_MAP["RateControlBlockedLSPSetup"])

    @RateControlBlockedLSPSetup.setter
    def RateControlBlockedLSPSetup(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RateControlBlockedLSPSetup"], value)

    @property
    def ResvCONFsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RESV-CONFs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResvCONFsRx"])

    @ResvCONFsRx.setter
    def ResvCONFsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResvCONFsRx"], value)

    @property
    def ResvCONFsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RESV-CONFs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResvCONFsTx"])

    @ResvCONFsTx.setter
    def ResvCONFsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResvCONFsTx"], value)

    @property
    def ResvERRsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RESV-ERRs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResvERRsRx"])

    @ResvERRsRx.setter
    def ResvERRsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResvERRsRx"], value)

    @property
    def ResvERRsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RESV-ERRs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResvERRsTx"])

    @ResvERRsTx.setter
    def ResvERRsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResvERRsTx"], value)

    @property
    def ResvLifetimeExpirations(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RESV Lifetime Expirations
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResvLifetimeExpirations"])

    @ResvLifetimeExpirations.setter
    def ResvLifetimeExpirations(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResvLifetimeExpirations"], value)

    @property
    def ResvTearsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RESV Tears Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResvTearsRx"])

    @ResvTearsRx.setter
    def ResvTearsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResvTearsRx"], value)

    @property
    def ResvTearsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RESV Tears Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResvTearsTx"])

    @ResvTearsTx.setter
    def ResvTearsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResvTearsTx"], value)

    @property
    def ResvsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RESVs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResvsRx"])

    @ResvsRx.setter
    def ResvsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResvsRx"], value)

    @property
    def ResvsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RESVs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResvsTx"])

    @ResvsTx.setter
    def ResvsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ResvsTx"], value)

    @property
    def SessionFlapCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Session Flap Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionFlapCount"])

    @SessionFlapCount.setter
    def SessionFlapCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessionFlapCount"], value)

    @property
    def SrefreshsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: SREFRESHs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrefreshsRx"])

    @SrefreshsRx.setter
    def SrefreshsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrefreshsRx"], value)

    @property
    def SrefreshsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: SREFRESHs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrefreshsTx"])

    @SrefreshsTx.setter
    def SrefreshsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrefreshsTx"], value)

    @property
    def UnrecoveredRESVsDeleted(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: UnRecovered RESVs Deleted
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnrecoveredRESVsDeleted"])

    @UnrecoveredRESVsDeleted.setter
    def UnrecoveredRESVsDeleted(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnrecoveredRESVsDeleted"], value)

    @property
    def UpStateCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Up State Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpStateCount"])

    @UpStateCount.setter
    def UpStateCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpStateCount"], value)

    def update(
        self,
        AcksRx=None,
        AcksTx=None,
        BundleMessagesRx=None,
        BundleMessagesTx=None,
        DownStateCount=None,
        EgressLSPsUp=None,
        EgressOutofOrderMsgsRx=None,
        EgressSubLSPsUp=None,
        HellosRx=None,
        HellosTx=None,
        IngressLSPsConfigured=None,
        IngressLSPsUp=None,
        IngressSubLSPsConfigured=None,
        IngressSubLSPsUp=None,
        NacksRx=None,
        NacksTx=None,
        NumberofPathReOptimizations=None,
        OwnGracefulRestarts=None,
        PathERRsRx=None,
        PathERRsTx=None,
        PathLifetimeExpirations=None,
        PathReevaluationRequestTx=None,
        PathSentStateCount=None,
        PathTearsRx=None,
        PathTearsTx=None,
        PathsRx=None,
        PathsTx=None,
        PathswithRecoveryLabelRx=None,
        PathswithRecoveryLabelTx=None,
        PeerGracefulRestarts=None,
        PortName=None,
        RateControlBlockedLSPSetup=None,
        ResvCONFsRx=None,
        ResvCONFsTx=None,
        ResvERRsRx=None,
        ResvERRsTx=None,
        ResvLifetimeExpirations=None,
        ResvTearsRx=None,
        ResvTearsTx=None,
        ResvsRx=None,
        ResvsTx=None,
        SessionFlapCount=None,
        SrefreshsRx=None,
        SrefreshsTx=None,
        UnrecoveredRESVsDeleted=None,
        UpStateCount=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> RsvpAggregatedStatistics
        """Updates rsvpAggregatedStatistics resource on the server.

        Args
        ----
        - AcksRx (bool): ACKs Rx
        - AcksTx (bool): ACKs Tx
        - BundleMessagesRx (bool): Bundle Messages Rx
        - BundleMessagesTx (bool): Bundle Messages Tx
        - DownStateCount (bool): Down State Count
        - EgressLSPsUp (bool): Egress LSPs Up
        - EgressOutofOrderMsgsRx (bool): Egress Out of Order Msgs Rx
        - EgressSubLSPsUp (bool): Egress SubLSPs Up
        - HellosRx (bool): HELLOs Rx
        - HellosTx (bool): HELLOs Tx
        - IngressLSPsConfigured (bool): Ingress LSPs Configured
        - IngressLSPsUp (bool): Ingress LSPs Up
        - IngressSubLSPsConfigured (bool): Ingress SubLSPs Configured
        - IngressSubLSPsUp (bool): Ingress SubLSPs Up
        - NacksRx (bool): NACKs Rx
        - NacksTx (bool): NACKs Tx
        - NumberofPathReOptimizations (bool): Number of Path Re-Optimizations
        - OwnGracefulRestarts (bool): Own Graceful-Restarts
        - PathERRsRx (bool): Path-ERRs Rx
        - PathERRsTx (bool): Path-ERRs Tx
        - PathLifetimeExpirations (bool): PATH Lifetime Expirations
        - PathReevaluationRequestTx (bool): Path Re-evaluation Request Tx
        - PathSentStateCount (bool): Path Sent State Count
        - PathTearsRx (bool): Path Tears Rx
        - PathTearsTx (bool): Path Tears Tx
        - PathsRx (bool): Paths Rx
        - PathsTx (bool): Paths Tx
        - PathswithRecoveryLabelRx (bool): Paths with Recovery-Label Rx
        - PathswithRecoveryLabelTx (bool): Paths with Recovery-Label Tx
        - PeerGracefulRestarts (bool): Peer Graceful-Restarts
        - PortName (bool): Port Name
        - RateControlBlockedLSPSetup (bool): Rate Control Blocked LSP Setup
        - ResvCONFsRx (bool): RESV-CONFs Rx
        - ResvCONFsTx (bool): RESV-CONFs Tx
        - ResvERRsRx (bool): RESV-ERRs Rx
        - ResvERRsTx (bool): RESV-ERRs Tx
        - ResvLifetimeExpirations (bool): RESV Lifetime Expirations
        - ResvTearsRx (bool): RESV Tears Rx
        - ResvTearsTx (bool): RESV Tears Tx
        - ResvsRx (bool): RESVs Rx
        - ResvsTx (bool): RESVs Tx
        - SessionFlapCount (bool): Session Flap Count
        - SrefreshsRx (bool): SREFRESHs Rx
        - SrefreshsTx (bool): SREFRESHs Tx
        - UnrecoveredRESVsDeleted (bool): UnRecovered RESVs Deleted
        - UpStateCount (bool): Up State Count

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AcksRx=None,
        AcksTx=None,
        BundleMessagesRx=None,
        BundleMessagesTx=None,
        DownStateCount=None,
        EgressLSPsUp=None,
        EgressOutofOrderMsgsRx=None,
        EgressSubLSPsUp=None,
        HellosRx=None,
        HellosTx=None,
        IngressLSPsConfigured=None,
        IngressLSPsUp=None,
        IngressSubLSPsConfigured=None,
        IngressSubLSPsUp=None,
        NacksRx=None,
        NacksTx=None,
        NumberofPathReOptimizations=None,
        OwnGracefulRestarts=None,
        PathERRsRx=None,
        PathERRsTx=None,
        PathLifetimeExpirations=None,
        PathReevaluationRequestTx=None,
        PathSentStateCount=None,
        PathTearsRx=None,
        PathTearsTx=None,
        PathsRx=None,
        PathsTx=None,
        PathswithRecoveryLabelRx=None,
        PathswithRecoveryLabelTx=None,
        PeerGracefulRestarts=None,
        PortName=None,
        RateControlBlockedLSPSetup=None,
        ResvCONFsRx=None,
        ResvCONFsTx=None,
        ResvERRsRx=None,
        ResvERRsTx=None,
        ResvLifetimeExpirations=None,
        ResvTearsRx=None,
        ResvTearsTx=None,
        ResvsRx=None,
        ResvsTx=None,
        SessionFlapCount=None,
        SrefreshsRx=None,
        SrefreshsTx=None,
        UnrecoveredRESVsDeleted=None,
        UpStateCount=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> RsvpAggregatedStatistics
        """Finds and retrieves rsvpAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rsvpAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rsvpAggregatedStatistics resources from the server.

        Args
        ----
        - AcksRx (bool): ACKs Rx
        - AcksTx (bool): ACKs Tx
        - BundleMessagesRx (bool): Bundle Messages Rx
        - BundleMessagesTx (bool): Bundle Messages Tx
        - DownStateCount (bool): Down State Count
        - EgressLSPsUp (bool): Egress LSPs Up
        - EgressOutofOrderMsgsRx (bool): Egress Out of Order Msgs Rx
        - EgressSubLSPsUp (bool): Egress SubLSPs Up
        - HellosRx (bool): HELLOs Rx
        - HellosTx (bool): HELLOs Tx
        - IngressLSPsConfigured (bool): Ingress LSPs Configured
        - IngressLSPsUp (bool): Ingress LSPs Up
        - IngressSubLSPsConfigured (bool): Ingress SubLSPs Configured
        - IngressSubLSPsUp (bool): Ingress SubLSPs Up
        - NacksRx (bool): NACKs Rx
        - NacksTx (bool): NACKs Tx
        - NumberofPathReOptimizations (bool): Number of Path Re-Optimizations
        - OwnGracefulRestarts (bool): Own Graceful-Restarts
        - PathERRsRx (bool): Path-ERRs Rx
        - PathERRsTx (bool): Path-ERRs Tx
        - PathLifetimeExpirations (bool): PATH Lifetime Expirations
        - PathReevaluationRequestTx (bool): Path Re-evaluation Request Tx
        - PathSentStateCount (bool): Path Sent State Count
        - PathTearsRx (bool): Path Tears Rx
        - PathTearsTx (bool): Path Tears Tx
        - PathsRx (bool): Paths Rx
        - PathsTx (bool): Paths Tx
        - PathswithRecoveryLabelRx (bool): Paths with Recovery-Label Rx
        - PathswithRecoveryLabelTx (bool): Paths with Recovery-Label Tx
        - PeerGracefulRestarts (bool): Peer Graceful-Restarts
        - PortName (bool): Port Name
        - RateControlBlockedLSPSetup (bool): Rate Control Blocked LSP Setup
        - ResvCONFsRx (bool): RESV-CONFs Rx
        - ResvCONFsTx (bool): RESV-CONFs Tx
        - ResvERRsRx (bool): RESV-ERRs Rx
        - ResvERRsTx (bool): RESV-ERRs Tx
        - ResvLifetimeExpirations (bool): RESV Lifetime Expirations
        - ResvTearsRx (bool): RESV Tears Rx
        - ResvTearsTx (bool): RESV Tears Tx
        - ResvsRx (bool): RESVs Rx
        - ResvsTx (bool): RESVs Tx
        - SessionFlapCount (bool): Session Flap Count
        - SrefreshsRx (bool): SREFRESHs Rx
        - SrefreshsTx (bool): SREFRESHs Tx
        - UnrecoveredRESVsDeleted (bool): UnRecovered RESVs Deleted
        - UpStateCount (bool): Up State Count

        Returns
        -------
        - self: This instance with matching rsvpAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rsvpAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rsvpAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
