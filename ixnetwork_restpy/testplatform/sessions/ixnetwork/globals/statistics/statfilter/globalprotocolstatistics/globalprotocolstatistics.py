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


class GlobalProtocolStatistics(Base):
    """Represents stats of Global Protocol Statistics
    The GlobalProtocolStatistics class encapsulates a required globalProtocolStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "globalProtocolStatistics"
    _SDM_ATT_MAP = {
        "ArpReplyRx": "arpReplyRx",
        "ArpReplyTx": "arpReplyTx",
        "ArpRequestRx": "arpRequestRx",
        "ArpRequestTx": "arpRequestTx",
        "BfdRoutersConfigured": "bfdRoutersConfigured",
        "BfdRoutersRunning": "bfdRoutersRunning",
        "BgpSessConfigured": "bgpSessConfigured",
        "BgpSessUp": "bgpSessUp",
        "CfmY1731PBBTEBridgesConfigured": "cfmY1731PBBTEBridgesConfigured",
        "ControlPacketRx": "controlPacketRx",
        "ControlPacketTx": "controlPacketTx",
        "EigrpIPv6RoutersConfigured": "eigrpIPv6RoutersConfigured",
        "EigrpIPv6RoutersRunning": "eigrpIPv6RoutersRunning",
        "EigrpRoutersConfigured": "eigrpRoutersConfigured",
        "EigrpRoutersRunning": "eigrpRoutersRunning",
        "ElmiStatus": "elmiStatus",
        "ElmiUNICConfigured": "elmiUNICConfigured",
        "ElmiUNICRunning": "elmiUNICRunning",
        "ElmiUNINConfigured": "elmiUNINConfigured",
        "ElmiUNINRunning": "elmiUNINRunning",
        "IgmpHostTotalFramesRx": "igmpHostTotalFramesRx",
        "IgmpHostTotalFramesTx": "igmpHostTotalFramesTx",
        "IgmpQuerierTotalFramesRx": "igmpQuerierTotalFramesRx",
        "IgmpQuerierTotalFramesTx": "igmpQuerierTotalFramesTx",
        "IsisFullL1Nbrs": "isisFullL1Nbrs",
        "IsisFullL2Nbrs": "isisFullL2Nbrs",
        "IsisL1SessConfigured": "isisL1SessConfigured",
        "IsisL1SessUp": "isisL1SessUp",
        "IsisL2SessConfigured": "isisL2SessConfigured",
        "IsisL2SessUp": "isisL2SessUp",
        "LdpBasicSessUp": "ldpBasicSessUp",
        "LdpTargetedSessConfigured": "ldpTargetedSessConfigured",
        "LdpTargetedSessUp": "ldpTargetedSessUp",
        "LispEIDsConfigured": "lispEIDsConfigured",
        "LispEIDsResolved": "lispEIDsResolved",
        "LispETRConfigured": "lispETRConfigured",
        "LispETRRunning": "lispETRRunning",
        "LispITRConfigured": "lispITRConfigured",
        "LispITRRunning": "lispITRRunning",
        "LispMSMRConfigured": "lispMSMRConfigured",
        "LispMSMRRunning": "lispMSMRRunning",
        "LispxTRConfigured": "lispxTRConfigured",
        "LispxTRRunning": "lispxTRRunning",
        "MldHostTotalFramesRx": "mldHostTotalFramesRx",
        "MldHostTotalFramesTx": "mldHostTotalFramesTx",
        "MldQuerierTotalFramesRx": "mldQuerierTotalFramesRx",
        "MldQuerierTotalFramesTx": "mldQuerierTotalFramesTx",
        "MplsoamBFDSessionCount": "mplsoamBFDSessionCount",
        "MplsoamBFDUpSessions": "mplsoamBFDUpSessions",
        "MplstpCCCVConfigured": "mplstpCCCVConfigured",
        "MplstpCCCVDown": "mplstpCCCVDown",
        "MplstpCCCVUp": "mplstpCCCVUp",
        "NeighborAdvertisementRx": "neighborAdvertisementRx",
        "NeighborAdvertisementTx": "neighborAdvertisementTx",
        "NeighborSolicitationRx": "neighborSolicitationRx",
        "NeighborSolicitationTx": "neighborSolicitationTx",
        "OamLinksConfigured": "oamLinksConfigured",
        "OamLinksRunning": "oamLinksRunning",
        "OpenflowSessConfigured": "openflowSessConfigured",
        "OpenflowSessConfiguredUp": "openflowSessConfiguredUp",
        "OpenflowSessLearnedUp": "openflowSessLearnedUp",
        "OspfFullNbrs": "ospfFullNbrs",
        "OspfSessionConfigured": "ospfSessionConfigured",
        "Ospfv3FullNbrs": "ospfv3FullNbrs",
        "Ospfv3SessConfigured": "ospfv3SessConfigured",
        "PimsmNbrsLearnt": "pimsmNbrsLearnt",
        "PimsmRtrsConfigured": "pimsmRtrsConfigured",
        "PimsmRtrsRunning": "pimsmRtrsRunning",
        "PingReplyRx": "pingReplyRx",
        "PingReplyTx": "pingReplyTx",
        "PingRequestRx": "pingRequestRx",
        "PingRequestTx": "pingRequestTx",
        "PortName": "portName",
        "RsvpEgressLSPsUp": "rsvpEgressLSPsUp",
        "RsvpIngressLSPsConfigured": "rsvpIngressLSPsConfigured",
        "RsvpIngressLSPsUp": "rsvpIngressLSPsUp",
        "StpBPDUsRx": "stpBPDUsRx",
        "StpBPDUsTx": "stpBPDUsTx",
        "TransmitArpGratuitous": "transmitArpGratuitous",
        "TransmitArpReverse": "transmitArpReverse",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(GlobalProtocolStatistics, self).__init__(parent, list_op)

    @property
    def ArpReplyRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Arp Reply Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpReplyRx"])

    @ArpReplyRx.setter
    def ArpReplyRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpReplyRx"], value)

    @property
    def ArpReplyTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Arp Reply Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpReplyTx"])

    @ArpReplyTx.setter
    def ArpReplyTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpReplyTx"], value)

    @property
    def ArpRequestRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Arp Request Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpRequestRx"])

    @ArpRequestRx.setter
    def ArpRequestRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpRequestRx"], value)

    @property
    def ArpRequestTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Arp Request Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ArpRequestTx"])

    @ArpRequestTx.setter
    def ArpRequestTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ArpRequestTx"], value)

    @property
    def BfdRoutersConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: BFD Routers Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["BfdRoutersConfigured"])

    @BfdRoutersConfigured.setter
    def BfdRoutersConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BfdRoutersConfigured"], value)

    @property
    def BfdRoutersRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: BFD Routers Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["BfdRoutersRunning"])

    @BfdRoutersRunning.setter
    def BfdRoutersRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BfdRoutersRunning"], value)

    @property
    def BgpSessConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: BGP Sess. Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["BgpSessConfigured"])

    @BgpSessConfigured.setter
    def BgpSessConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BgpSessConfigured"], value)

    @property
    def BgpSessUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: BGP Sess. Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["BgpSessUp"])

    @BgpSessUp.setter
    def BgpSessUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BgpSessUp"], value)

    @property
    def CfmY1731PBBTEBridgesConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CFM/Y.1731/PBB-TE Bridges Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["CfmY1731PBBTEBridgesConfigured"])

    @CfmY1731PBBTEBridgesConfigured.setter
    def CfmY1731PBBTEBridgesConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CfmY1731PBBTEBridgesConfigured"], value)

    @property
    def ControlPacketRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Control Packet Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlPacketRx"])

    @ControlPacketRx.setter
    def ControlPacketRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlPacketRx"], value)

    @property
    def ControlPacketTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Control Packet Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlPacketTx"])

    @ControlPacketTx.setter
    def ControlPacketTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlPacketTx"], value)

    @property
    def EigrpIPv6RoutersConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: EIGRP IPv6 Routers Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["EigrpIPv6RoutersConfigured"])

    @EigrpIPv6RoutersConfigured.setter
    def EigrpIPv6RoutersConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EigrpIPv6RoutersConfigured"], value)

    @property
    def EigrpIPv6RoutersRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: EIGRP IPv6 Routers Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["EigrpIPv6RoutersRunning"])

    @EigrpIPv6RoutersRunning.setter
    def EigrpIPv6RoutersRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EigrpIPv6RoutersRunning"], value)

    @property
    def EigrpRoutersConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: EIGRP Routers Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["EigrpRoutersConfigured"])

    @EigrpRoutersConfigured.setter
    def EigrpRoutersConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EigrpRoutersConfigured"], value)

    @property
    def EigrpRoutersRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: EIGRP Routers Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["EigrpRoutersRunning"])

    @EigrpRoutersRunning.setter
    def EigrpRoutersRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EigrpRoutersRunning"], value)

    @property
    def ElmiStatus(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ELMI Status
        """
        return self._get_attribute(self._SDM_ATT_MAP["ElmiStatus"])

    @ElmiStatus.setter
    def ElmiStatus(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ElmiStatus"], value)

    @property
    def ElmiUNICConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ELMI UNI-C Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["ElmiUNICConfigured"])

    @ElmiUNICConfigured.setter
    def ElmiUNICConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ElmiUNICConfigured"], value)

    @property
    def ElmiUNICRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ELMI UNI-C Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["ElmiUNICRunning"])

    @ElmiUNICRunning.setter
    def ElmiUNICRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ElmiUNICRunning"], value)

    @property
    def ElmiUNINConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ELMI UNI-N Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["ElmiUNINConfigured"])

    @ElmiUNINConfigured.setter
    def ElmiUNINConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ElmiUNINConfigured"], value)

    @property
    def ElmiUNINRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ELMI UNI-N Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["ElmiUNINRunning"])

    @ElmiUNINRunning.setter
    def ElmiUNINRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ElmiUNINRunning"], value)

    @property
    def IgmpHostTotalFramesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IGMP Host Total Frames Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["IgmpHostTotalFramesRx"])

    @IgmpHostTotalFramesRx.setter
    def IgmpHostTotalFramesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IgmpHostTotalFramesRx"], value)

    @property
    def IgmpHostTotalFramesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IGMP Host Total Frames Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["IgmpHostTotalFramesTx"])

    @IgmpHostTotalFramesTx.setter
    def IgmpHostTotalFramesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IgmpHostTotalFramesTx"], value)

    @property
    def IgmpQuerierTotalFramesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IGMP Querier Total Frames Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["IgmpQuerierTotalFramesRx"])

    @IgmpQuerierTotalFramesRx.setter
    def IgmpQuerierTotalFramesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IgmpQuerierTotalFramesRx"], value)

    @property
    def IgmpQuerierTotalFramesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IGMP Querier Total Frames Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["IgmpQuerierTotalFramesTx"])

    @IgmpQuerierTotalFramesTx.setter
    def IgmpQuerierTotalFramesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IgmpQuerierTotalFramesTx"], value)

    @property
    def IsisFullL1Nbrs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ISIS Full L1 Nbrs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsisFullL1Nbrs"])

    @IsisFullL1Nbrs.setter
    def IsisFullL1Nbrs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsisFullL1Nbrs"], value)

    @property
    def IsisFullL2Nbrs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ISIS Full L2 Nbrs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsisFullL2Nbrs"])

    @IsisFullL2Nbrs.setter
    def IsisFullL2Nbrs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsisFullL2Nbrs"], value)

    @property
    def IsisL1SessConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ISIS L1 Sess. Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsisL1SessConfigured"])

    @IsisL1SessConfigured.setter
    def IsisL1SessConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsisL1SessConfigured"], value)

    @property
    def IsisL1SessUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ISIS L1 Sess. Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsisL1SessUp"])

    @IsisL1SessUp.setter
    def IsisL1SessUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsisL1SessUp"], value)

    @property
    def IsisL2SessConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ISIS L2 Sess. Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsisL2SessConfigured"])

    @IsisL2SessConfigured.setter
    def IsisL2SessConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsisL2SessConfigured"], value)

    @property
    def IsisL2SessUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ISIS L2 Sess. Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsisL2SessUp"])

    @IsisL2SessUp.setter
    def IsisL2SessUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsisL2SessUp"], value)

    @property
    def LdpBasicSessUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LDP Basic Sess. Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["LdpBasicSessUp"])

    @LdpBasicSessUp.setter
    def LdpBasicSessUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LdpBasicSessUp"], value)

    @property
    def LdpTargetedSessConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LDP Targeted Sess. Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["LdpTargetedSessConfigured"])

    @LdpTargetedSessConfigured.setter
    def LdpTargetedSessConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LdpTargetedSessConfigured"], value)

    @property
    def LdpTargetedSessUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LDP Targeted Sess. Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["LdpTargetedSessUp"])

    @LdpTargetedSessUp.setter
    def LdpTargetedSessUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LdpTargetedSessUp"], value)

    @property
    def LispEIDsConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LISP EIDs Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["LispEIDsConfigured"])

    @LispEIDsConfigured.setter
    def LispEIDsConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LispEIDsConfigured"], value)

    @property
    def LispEIDsResolved(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LISP EIDs Resolved
        """
        return self._get_attribute(self._SDM_ATT_MAP["LispEIDsResolved"])

    @LispEIDsResolved.setter
    def LispEIDsResolved(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LispEIDsResolved"], value)

    @property
    def LispETRConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LISP ETR Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["LispETRConfigured"])

    @LispETRConfigured.setter
    def LispETRConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LispETRConfigured"], value)

    @property
    def LispETRRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LISP ETR Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["LispETRRunning"])

    @LispETRRunning.setter
    def LispETRRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LispETRRunning"], value)

    @property
    def LispITRConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LISP ITR Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["LispITRConfigured"])

    @LispITRConfigured.setter
    def LispITRConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LispITRConfigured"], value)

    @property
    def LispITRRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LISP ITR Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["LispITRRunning"])

    @LispITRRunning.setter
    def LispITRRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LispITRRunning"], value)

    @property
    def LispMSMRConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LISP MS/MR Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["LispMSMRConfigured"])

    @LispMSMRConfigured.setter
    def LispMSMRConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LispMSMRConfigured"], value)

    @property
    def LispMSMRRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LISP MS/MR Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["LispMSMRRunning"])

    @LispMSMRRunning.setter
    def LispMSMRRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LispMSMRRunning"], value)

    @property
    def LispxTRConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LISP xTR Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["LispxTRConfigured"])

    @LispxTRConfigured.setter
    def LispxTRConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LispxTRConfigured"], value)

    @property
    def LispxTRRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LISP xTR Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["LispxTRRunning"])

    @LispxTRRunning.setter
    def LispxTRRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LispxTRRunning"], value)

    @property
    def MldHostTotalFramesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MLD Host Total Frames Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MldHostTotalFramesRx"])

    @MldHostTotalFramesRx.setter
    def MldHostTotalFramesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MldHostTotalFramesRx"], value)

    @property
    def MldHostTotalFramesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MLD Host Total Frames Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MldHostTotalFramesTx"])

    @MldHostTotalFramesTx.setter
    def MldHostTotalFramesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MldHostTotalFramesTx"], value)

    @property
    def MldQuerierTotalFramesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MLD Querier Total Frames Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MldQuerierTotalFramesRx"])

    @MldQuerierTotalFramesRx.setter
    def MldQuerierTotalFramesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MldQuerierTotalFramesRx"], value)

    @property
    def MldQuerierTotalFramesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MLD Querier Total Frames Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MldQuerierTotalFramesTx"])

    @MldQuerierTotalFramesTx.setter
    def MldQuerierTotalFramesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MldQuerierTotalFramesTx"], value)

    @property
    def MplsoamBFDSessionCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MPLSOAM BFD Session Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsoamBFDSessionCount"])

    @MplsoamBFDSessionCount.setter
    def MplsoamBFDSessionCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsoamBFDSessionCount"], value)

    @property
    def MplsoamBFDUpSessions(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MPLSOAM BFD Up-Sessions
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsoamBFDUpSessions"])

    @MplsoamBFDUpSessions.setter
    def MplsoamBFDUpSessions(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsoamBFDUpSessions"], value)

    @property
    def MplstpCCCVConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MPLSTP CCCV Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplstpCCCVConfigured"])

    @MplstpCCCVConfigured.setter
    def MplstpCCCVConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplstpCCCVConfigured"], value)

    @property
    def MplstpCCCVDown(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MPLSTP CCCV Down
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplstpCCCVDown"])

    @MplstpCCCVDown.setter
    def MplstpCCCVDown(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplstpCCCVDown"], value)

    @property
    def MplstpCCCVUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MPLSTP CCCV Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplstpCCCVUp"])

    @MplstpCCCVUp.setter
    def MplstpCCCVUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplstpCCCVUp"], value)

    @property
    def NeighborAdvertisementRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Neighbor Advertisement Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NeighborAdvertisementRx"])

    @NeighborAdvertisementRx.setter
    def NeighborAdvertisementRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NeighborAdvertisementRx"], value)

    @property
    def NeighborAdvertisementTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Neighbor Advertisement Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NeighborAdvertisementTx"])

    @NeighborAdvertisementTx.setter
    def NeighborAdvertisementTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NeighborAdvertisementTx"], value)

    @property
    def NeighborSolicitationRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Neighbor Solicitation Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NeighborSolicitationRx"])

    @NeighborSolicitationRx.setter
    def NeighborSolicitationRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NeighborSolicitationRx"], value)

    @property
    def NeighborSolicitationTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Neighbor Solicitation Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NeighborSolicitationTx"])

    @NeighborSolicitationTx.setter
    def NeighborSolicitationTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NeighborSolicitationTx"], value)

    @property
    def OamLinksConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OAM Links Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["OamLinksConfigured"])

    @OamLinksConfigured.setter
    def OamLinksConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OamLinksConfigured"], value)

    @property
    def OamLinksRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OAM Links Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["OamLinksRunning"])

    @OamLinksRunning.setter
    def OamLinksRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OamLinksRunning"], value)

    @property
    def OpenflowSessConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OpenFlow Sess. Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["OpenflowSessConfigured"])

    @OpenflowSessConfigured.setter
    def OpenflowSessConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OpenflowSessConfigured"], value)

    @property
    def OpenflowSessConfiguredUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OpenFlow Sess. Configured Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["OpenflowSessConfiguredUp"])

    @OpenflowSessConfiguredUp.setter
    def OpenflowSessConfiguredUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OpenflowSessConfiguredUp"], value)

    @property
    def OpenflowSessLearnedUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OpenFlow Sess. Learned Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["OpenflowSessLearnedUp"])

    @OpenflowSessLearnedUp.setter
    def OpenflowSessLearnedUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OpenflowSessLearnedUp"], value)

    @property
    def OspfFullNbrs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OSPF Full Nbrs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OspfFullNbrs"])

    @OspfFullNbrs.setter
    def OspfFullNbrs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OspfFullNbrs"], value)

    @property
    def OspfSessionConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OSPF Session Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["OspfSessionConfigured"])

    @OspfSessionConfigured.setter
    def OspfSessionConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OspfSessionConfigured"], value)

    @property
    def Ospfv3FullNbrs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OSPFv3 Full Nbrs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ospfv3FullNbrs"])

    @Ospfv3FullNbrs.setter
    def Ospfv3FullNbrs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ospfv3FullNbrs"], value)

    @property
    def Ospfv3SessConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: OSPFv3 Sess. Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ospfv3SessConfigured"])

    @Ospfv3SessConfigured.setter
    def Ospfv3SessConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ospfv3SessConfigured"], value)

    @property
    def PimsmNbrsLearnt(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PIMSM Nbrs. Learnt
        """
        return self._get_attribute(self._SDM_ATT_MAP["PimsmNbrsLearnt"])

    @PimsmNbrsLearnt.setter
    def PimsmNbrsLearnt(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PimsmNbrsLearnt"], value)

    @property
    def PimsmRtrsConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PIMSM Rtrs. Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["PimsmRtrsConfigured"])

    @PimsmRtrsConfigured.setter
    def PimsmRtrsConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PimsmRtrsConfigured"], value)

    @property
    def PimsmRtrsRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PIMSM Rtrs. Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["PimsmRtrsRunning"])

    @PimsmRtrsRunning.setter
    def PimsmRtrsRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PimsmRtrsRunning"], value)

    @property
    def PingReplyRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ping Reply Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PingReplyRx"])

    @PingReplyRx.setter
    def PingReplyRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PingReplyRx"], value)

    @property
    def PingReplyTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ping Reply Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PingReplyTx"])

    @PingReplyTx.setter
    def PingReplyTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PingReplyTx"], value)

    @property
    def PingRequestRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ping Request Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PingRequestRx"])

    @PingRequestRx.setter
    def PingRequestRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PingRequestRx"], value)

    @property
    def PingRequestTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ping Request Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PingRequestTx"])

    @PingRequestTx.setter
    def PingRequestTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PingRequestTx"], value)

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
    def RsvpEgressLSPsUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RSVP Egress LSPs Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsvpEgressLSPsUp"])

    @RsvpEgressLSPsUp.setter
    def RsvpEgressLSPsUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsvpEgressLSPsUp"], value)

    @property
    def RsvpIngressLSPsConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RSVP Ingress LSPs Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsvpIngressLSPsConfigured"])

    @RsvpIngressLSPsConfigured.setter
    def RsvpIngressLSPsConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsvpIngressLSPsConfigured"], value)

    @property
    def RsvpIngressLSPsUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RSVP Ingress LSPs Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsvpIngressLSPsUp"])

    @RsvpIngressLSPsUp.setter
    def RsvpIngressLSPsUp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsvpIngressLSPsUp"], value)

    @property
    def StpBPDUsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: STP BPDUs Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["StpBPDUsRx"])

    @StpBPDUsRx.setter
    def StpBPDUsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StpBPDUsRx"], value)

    @property
    def StpBPDUsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: STP BPDUs Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["StpBPDUsTx"])

    @StpBPDUsTx.setter
    def StpBPDUsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StpBPDUsTx"], value)

    @property
    def TransmitArpGratuitous(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Transmit Arp Gratuitous
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitArpGratuitous"])

    @TransmitArpGratuitous.setter
    def TransmitArpGratuitous(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitArpGratuitous"], value)

    @property
    def TransmitArpReverse(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Transmit Arp Reverse
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitArpReverse"])

    @TransmitArpReverse.setter
    def TransmitArpReverse(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitArpReverse"], value)

    def update(
        self,
        ArpReplyRx=None,
        ArpReplyTx=None,
        ArpRequestRx=None,
        ArpRequestTx=None,
        BfdRoutersConfigured=None,
        BfdRoutersRunning=None,
        BgpSessConfigured=None,
        BgpSessUp=None,
        CfmY1731PBBTEBridgesConfigured=None,
        ControlPacketRx=None,
        ControlPacketTx=None,
        EigrpIPv6RoutersConfigured=None,
        EigrpIPv6RoutersRunning=None,
        EigrpRoutersConfigured=None,
        EigrpRoutersRunning=None,
        ElmiStatus=None,
        ElmiUNICConfigured=None,
        ElmiUNICRunning=None,
        ElmiUNINConfigured=None,
        ElmiUNINRunning=None,
        IgmpHostTotalFramesRx=None,
        IgmpHostTotalFramesTx=None,
        IgmpQuerierTotalFramesRx=None,
        IgmpQuerierTotalFramesTx=None,
        IsisFullL1Nbrs=None,
        IsisFullL2Nbrs=None,
        IsisL1SessConfigured=None,
        IsisL1SessUp=None,
        IsisL2SessConfigured=None,
        IsisL2SessUp=None,
        LdpBasicSessUp=None,
        LdpTargetedSessConfigured=None,
        LdpTargetedSessUp=None,
        LispEIDsConfigured=None,
        LispEIDsResolved=None,
        LispETRConfigured=None,
        LispETRRunning=None,
        LispITRConfigured=None,
        LispITRRunning=None,
        LispMSMRConfigured=None,
        LispMSMRRunning=None,
        LispxTRConfigured=None,
        LispxTRRunning=None,
        MldHostTotalFramesRx=None,
        MldHostTotalFramesTx=None,
        MldQuerierTotalFramesRx=None,
        MldQuerierTotalFramesTx=None,
        MplsoamBFDSessionCount=None,
        MplsoamBFDUpSessions=None,
        MplstpCCCVConfigured=None,
        MplstpCCCVDown=None,
        MplstpCCCVUp=None,
        NeighborAdvertisementRx=None,
        NeighborAdvertisementTx=None,
        NeighborSolicitationRx=None,
        NeighborSolicitationTx=None,
        OamLinksConfigured=None,
        OamLinksRunning=None,
        OpenflowSessConfigured=None,
        OpenflowSessConfiguredUp=None,
        OpenflowSessLearnedUp=None,
        OspfFullNbrs=None,
        OspfSessionConfigured=None,
        Ospfv3FullNbrs=None,
        Ospfv3SessConfigured=None,
        PimsmNbrsLearnt=None,
        PimsmRtrsConfigured=None,
        PimsmRtrsRunning=None,
        PingReplyRx=None,
        PingReplyTx=None,
        PingRequestRx=None,
        PingRequestTx=None,
        PortName=None,
        RsvpEgressLSPsUp=None,
        RsvpIngressLSPsConfigured=None,
        RsvpIngressLSPsUp=None,
        StpBPDUsRx=None,
        StpBPDUsTx=None,
        TransmitArpGratuitous=None,
        TransmitArpReverse=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> GlobalProtocolStatistics
        """Updates globalProtocolStatistics resource on the server.

        Args
        ----
        - ArpReplyRx (bool): Arp Reply Rx.
        - ArpReplyTx (bool): Arp Reply Tx.
        - ArpRequestRx (bool): Arp Request Rx.
        - ArpRequestTx (bool): Arp Request Tx.
        - BfdRoutersConfigured (bool): BFD Routers Configured
        - BfdRoutersRunning (bool): BFD Routers Running
        - BgpSessConfigured (bool): BGP Sess. Configured
        - BgpSessUp (bool): BGP Sess. Up
        - CfmY1731PBBTEBridgesConfigured (bool): CFM/Y.1731/PBB-TE Bridges Configured
        - ControlPacketRx (bool): Control Packet Rx.
        - ControlPacketTx (bool): Control Packet Tx.
        - EigrpIPv6RoutersConfigured (bool): EIGRP IPv6 Routers Configured
        - EigrpIPv6RoutersRunning (bool): EIGRP IPv6 Routers Running
        - EigrpRoutersConfigured (bool): EIGRP Routers Configured
        - EigrpRoutersRunning (bool): EIGRP Routers Running
        - ElmiStatus (bool): ELMI Status
        - ElmiUNICConfigured (bool): ELMI UNI-C Configured
        - ElmiUNICRunning (bool): ELMI UNI-C Running
        - ElmiUNINConfigured (bool): ELMI UNI-N Configured
        - ElmiUNINRunning (bool): ELMI UNI-N Running
        - IgmpHostTotalFramesRx (bool): IGMP Host Total Frames Rx
        - IgmpHostTotalFramesTx (bool): IGMP Host Total Frames Tx
        - IgmpQuerierTotalFramesRx (bool): IGMP Querier Total Frames Rx
        - IgmpQuerierTotalFramesTx (bool): IGMP Querier Total Frames Tx
        - IsisFullL1Nbrs (bool): ISIS Full L1 Nbrs.
        - IsisFullL2Nbrs (bool): ISIS Full L2 Nbrs.
        - IsisL1SessConfigured (bool): ISIS L1 Sess. Configured
        - IsisL1SessUp (bool): ISIS L1 Sess. Up
        - IsisL2SessConfigured (bool): ISIS L2 Sess. Configured
        - IsisL2SessUp (bool): ISIS L2 Sess. Up
        - LdpBasicSessUp (bool): LDP Basic Sess. Up
        - LdpTargetedSessConfigured (bool): LDP Targeted Sess. Configured
        - LdpTargetedSessUp (bool): LDP Targeted Sess. Up
        - LispEIDsConfigured (bool): LISP EIDs Configured
        - LispEIDsResolved (bool): LISP EIDs Resolved
        - LispETRConfigured (bool): LISP ETR Configured
        - LispETRRunning (bool): LISP ETR Running
        - LispITRConfigured (bool): LISP ITR Configured
        - LispITRRunning (bool): LISP ITR Running
        - LispMSMRConfigured (bool): LISP MS/MR Configured
        - LispMSMRRunning (bool): LISP MS/MR Running
        - LispxTRConfigured (bool): LISP xTR Configured
        - LispxTRRunning (bool): LISP xTR Running
        - MldHostTotalFramesRx (bool): MLD Host Total Frames Rx
        - MldHostTotalFramesTx (bool): MLD Host Total Frames Tx
        - MldQuerierTotalFramesRx (bool): MLD Querier Total Frames Rx
        - MldQuerierTotalFramesTx (bool): MLD Querier Total Frames Tx
        - MplsoamBFDSessionCount (bool): MPLSOAM BFD Session Count
        - MplsoamBFDUpSessions (bool): MPLSOAM BFD Up-Sessions
        - MplstpCCCVConfigured (bool): MPLSTP CCCV Configured
        - MplstpCCCVDown (bool): MPLSTP CCCV Down
        - MplstpCCCVUp (bool): MPLSTP CCCV Up
        - NeighborAdvertisementRx (bool): Neighbor Advertisement Rx.
        - NeighborAdvertisementTx (bool): Neighbor Advertisement Tx.
        - NeighborSolicitationRx (bool): Neighbor Solicitation Rx.
        - NeighborSolicitationTx (bool): Neighbor Solicitation Tx.
        - OamLinksConfigured (bool): OAM Links Configured
        - OamLinksRunning (bool): OAM Links Running
        - OpenflowSessConfigured (bool): OpenFlow Sess. Configured
        - OpenflowSessConfiguredUp (bool): OpenFlow Sess. Configured Up
        - OpenflowSessLearnedUp (bool): OpenFlow Sess. Learned Up
        - OspfFullNbrs (bool): OSPF Full Nbrs.
        - OspfSessionConfigured (bool): OSPF Session Configured
        - Ospfv3FullNbrs (bool): OSPFv3 Full Nbrs.
        - Ospfv3SessConfigured (bool): OSPFv3 Sess. Configured
        - PimsmNbrsLearnt (bool): PIMSM Nbrs. Learnt
        - PimsmRtrsConfigured (bool): PIMSM Rtrs. Configured
        - PimsmRtrsRunning (bool): PIMSM Rtrs. Running
        - PingReplyRx (bool): Ping Reply Rx.
        - PingReplyTx (bool): Ping Reply Tx.
        - PingRequestRx (bool): Ping Request Rx.
        - PingRequestTx (bool): Ping Request Tx.
        - PortName (bool): Port Name
        - RsvpEgressLSPsUp (bool): RSVP Egress LSPs Up
        - RsvpIngressLSPsConfigured (bool): RSVP Ingress LSPs Configured
        - RsvpIngressLSPsUp (bool): RSVP Ingress LSPs Up
        - StpBPDUsRx (bool): STP BPDUs Rx
        - StpBPDUsTx (bool): STP BPDUs Tx
        - TransmitArpGratuitous (bool): Transmit Arp Gratuitous
        - TransmitArpReverse (bool): Transmit Arp Reverse

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ArpReplyRx=None,
        ArpReplyTx=None,
        ArpRequestRx=None,
        ArpRequestTx=None,
        BfdRoutersConfigured=None,
        BfdRoutersRunning=None,
        BgpSessConfigured=None,
        BgpSessUp=None,
        CfmY1731PBBTEBridgesConfigured=None,
        ControlPacketRx=None,
        ControlPacketTx=None,
        EigrpIPv6RoutersConfigured=None,
        EigrpIPv6RoutersRunning=None,
        EigrpRoutersConfigured=None,
        EigrpRoutersRunning=None,
        ElmiStatus=None,
        ElmiUNICConfigured=None,
        ElmiUNICRunning=None,
        ElmiUNINConfigured=None,
        ElmiUNINRunning=None,
        IgmpHostTotalFramesRx=None,
        IgmpHostTotalFramesTx=None,
        IgmpQuerierTotalFramesRx=None,
        IgmpQuerierTotalFramesTx=None,
        IsisFullL1Nbrs=None,
        IsisFullL2Nbrs=None,
        IsisL1SessConfigured=None,
        IsisL1SessUp=None,
        IsisL2SessConfigured=None,
        IsisL2SessUp=None,
        LdpBasicSessUp=None,
        LdpTargetedSessConfigured=None,
        LdpTargetedSessUp=None,
        LispEIDsConfigured=None,
        LispEIDsResolved=None,
        LispETRConfigured=None,
        LispETRRunning=None,
        LispITRConfigured=None,
        LispITRRunning=None,
        LispMSMRConfigured=None,
        LispMSMRRunning=None,
        LispxTRConfigured=None,
        LispxTRRunning=None,
        MldHostTotalFramesRx=None,
        MldHostTotalFramesTx=None,
        MldQuerierTotalFramesRx=None,
        MldQuerierTotalFramesTx=None,
        MplsoamBFDSessionCount=None,
        MplsoamBFDUpSessions=None,
        MplstpCCCVConfigured=None,
        MplstpCCCVDown=None,
        MplstpCCCVUp=None,
        NeighborAdvertisementRx=None,
        NeighborAdvertisementTx=None,
        NeighborSolicitationRx=None,
        NeighborSolicitationTx=None,
        OamLinksConfigured=None,
        OamLinksRunning=None,
        OpenflowSessConfigured=None,
        OpenflowSessConfiguredUp=None,
        OpenflowSessLearnedUp=None,
        OspfFullNbrs=None,
        OspfSessionConfigured=None,
        Ospfv3FullNbrs=None,
        Ospfv3SessConfigured=None,
        PimsmNbrsLearnt=None,
        PimsmRtrsConfigured=None,
        PimsmRtrsRunning=None,
        PingReplyRx=None,
        PingReplyTx=None,
        PingRequestRx=None,
        PingRequestTx=None,
        PortName=None,
        RsvpEgressLSPsUp=None,
        RsvpIngressLSPsConfigured=None,
        RsvpIngressLSPsUp=None,
        StpBPDUsRx=None,
        StpBPDUsTx=None,
        TransmitArpGratuitous=None,
        TransmitArpReverse=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> GlobalProtocolStatistics
        """Finds and retrieves globalProtocolStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve globalProtocolStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all globalProtocolStatistics resources from the server.

        Args
        ----
        - ArpReplyRx (bool): Arp Reply Rx.
        - ArpReplyTx (bool): Arp Reply Tx.
        - ArpRequestRx (bool): Arp Request Rx.
        - ArpRequestTx (bool): Arp Request Tx.
        - BfdRoutersConfigured (bool): BFD Routers Configured
        - BfdRoutersRunning (bool): BFD Routers Running
        - BgpSessConfigured (bool): BGP Sess. Configured
        - BgpSessUp (bool): BGP Sess. Up
        - CfmY1731PBBTEBridgesConfigured (bool): CFM/Y.1731/PBB-TE Bridges Configured
        - ControlPacketRx (bool): Control Packet Rx.
        - ControlPacketTx (bool): Control Packet Tx.
        - EigrpIPv6RoutersConfigured (bool): EIGRP IPv6 Routers Configured
        - EigrpIPv6RoutersRunning (bool): EIGRP IPv6 Routers Running
        - EigrpRoutersConfigured (bool): EIGRP Routers Configured
        - EigrpRoutersRunning (bool): EIGRP Routers Running
        - ElmiStatus (bool): ELMI Status
        - ElmiUNICConfigured (bool): ELMI UNI-C Configured
        - ElmiUNICRunning (bool): ELMI UNI-C Running
        - ElmiUNINConfigured (bool): ELMI UNI-N Configured
        - ElmiUNINRunning (bool): ELMI UNI-N Running
        - IgmpHostTotalFramesRx (bool): IGMP Host Total Frames Rx
        - IgmpHostTotalFramesTx (bool): IGMP Host Total Frames Tx
        - IgmpQuerierTotalFramesRx (bool): IGMP Querier Total Frames Rx
        - IgmpQuerierTotalFramesTx (bool): IGMP Querier Total Frames Tx
        - IsisFullL1Nbrs (bool): ISIS Full L1 Nbrs.
        - IsisFullL2Nbrs (bool): ISIS Full L2 Nbrs.
        - IsisL1SessConfigured (bool): ISIS L1 Sess. Configured
        - IsisL1SessUp (bool): ISIS L1 Sess. Up
        - IsisL2SessConfigured (bool): ISIS L2 Sess. Configured
        - IsisL2SessUp (bool): ISIS L2 Sess. Up
        - LdpBasicSessUp (bool): LDP Basic Sess. Up
        - LdpTargetedSessConfigured (bool): LDP Targeted Sess. Configured
        - LdpTargetedSessUp (bool): LDP Targeted Sess. Up
        - LispEIDsConfigured (bool): LISP EIDs Configured
        - LispEIDsResolved (bool): LISP EIDs Resolved
        - LispETRConfigured (bool): LISP ETR Configured
        - LispETRRunning (bool): LISP ETR Running
        - LispITRConfigured (bool): LISP ITR Configured
        - LispITRRunning (bool): LISP ITR Running
        - LispMSMRConfigured (bool): LISP MS/MR Configured
        - LispMSMRRunning (bool): LISP MS/MR Running
        - LispxTRConfigured (bool): LISP xTR Configured
        - LispxTRRunning (bool): LISP xTR Running
        - MldHostTotalFramesRx (bool): MLD Host Total Frames Rx
        - MldHostTotalFramesTx (bool): MLD Host Total Frames Tx
        - MldQuerierTotalFramesRx (bool): MLD Querier Total Frames Rx
        - MldQuerierTotalFramesTx (bool): MLD Querier Total Frames Tx
        - MplsoamBFDSessionCount (bool): MPLSOAM BFD Session Count
        - MplsoamBFDUpSessions (bool): MPLSOAM BFD Up-Sessions
        - MplstpCCCVConfigured (bool): MPLSTP CCCV Configured
        - MplstpCCCVDown (bool): MPLSTP CCCV Down
        - MplstpCCCVUp (bool): MPLSTP CCCV Up
        - NeighborAdvertisementRx (bool): Neighbor Advertisement Rx.
        - NeighborAdvertisementTx (bool): Neighbor Advertisement Tx.
        - NeighborSolicitationRx (bool): Neighbor Solicitation Rx.
        - NeighborSolicitationTx (bool): Neighbor Solicitation Tx.
        - OamLinksConfigured (bool): OAM Links Configured
        - OamLinksRunning (bool): OAM Links Running
        - OpenflowSessConfigured (bool): OpenFlow Sess. Configured
        - OpenflowSessConfiguredUp (bool): OpenFlow Sess. Configured Up
        - OpenflowSessLearnedUp (bool): OpenFlow Sess. Learned Up
        - OspfFullNbrs (bool): OSPF Full Nbrs.
        - OspfSessionConfigured (bool): OSPF Session Configured
        - Ospfv3FullNbrs (bool): OSPFv3 Full Nbrs.
        - Ospfv3SessConfigured (bool): OSPFv3 Sess. Configured
        - PimsmNbrsLearnt (bool): PIMSM Nbrs. Learnt
        - PimsmRtrsConfigured (bool): PIMSM Rtrs. Configured
        - PimsmRtrsRunning (bool): PIMSM Rtrs. Running
        - PingReplyRx (bool): Ping Reply Rx.
        - PingReplyTx (bool): Ping Reply Tx.
        - PingRequestRx (bool): Ping Request Rx.
        - PingRequestTx (bool): Ping Request Tx.
        - PortName (bool): Port Name
        - RsvpEgressLSPsUp (bool): RSVP Egress LSPs Up
        - RsvpIngressLSPsConfigured (bool): RSVP Ingress LSPs Configured
        - RsvpIngressLSPsUp (bool): RSVP Ingress LSPs Up
        - StpBPDUsRx (bool): STP BPDUs Rx
        - StpBPDUsTx (bool): STP BPDUs Tx
        - TransmitArpGratuitous (bool): Transmit Arp Gratuitous
        - TransmitArpReverse (bool): Transmit Arp Reverse

        Returns
        -------
        - self: This instance with matching globalProtocolStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of globalProtocolStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the globalProtocolStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
