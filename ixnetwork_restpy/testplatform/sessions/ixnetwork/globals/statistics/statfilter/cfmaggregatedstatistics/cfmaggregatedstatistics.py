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


class CfmAggregatedStatistics(Base):
    """Represents stats of CFM Aggregated Statistics
    The CfmAggregatedStatistics class encapsulates a required cfmAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "cfmAggregatedStatistics"
    _SDM_ATT_MAP = {
        "AisRx": "aisRx",
        "AisTx": "aisTx",
        "BridgesConfigured": "bridgesConfigured",
        "BridgesRunning": "bridgesRunning",
        "CcmRx": "ccmRx",
        "CcmTx": "ccmTx",
        "CcmUnexpectedPeriod": "ccmUnexpectedPeriod",
        "DefectiveRMEPS": "defectiveRMEPS",
        "DmmRx": "dmmRx",
        "DmmTx": "dmmTx",
        "DmrRx": "dmrRx",
        "DmrTx": "dmrTx",
        "InvalidCCMRx": "invalidCCMRx",
        "InvalidLBMRx": "invalidLBMRx",
        "InvalidLBRRx": "invalidLBRRx",
        "InvalidLMRRx": "invalidLMRRx",
        "InvalidLTMRx": "invalidLTMRx",
        "InvalidLTRRx": "invalidLTRRx",
        "LbmRx": "lbmRx",
        "LbmTx": "lbmTx",
        "LbrRx": "lbrRx",
        "LbrTx": "lbrTx",
        "LckRx": "lckRx",
        "LckTx": "lckTx",
        "LmmRx": "lmmRx",
        "LmmTx": "lmmTx",
        "LmrRx": "lmrRx",
        "LmrTx": "lmrTx",
        "LrRespond": "lrRespond",
        "LtmRx": "ltmRx",
        "LtmTx": "ltmTx",
        "LtrRx": "ltrRx",
        "LtrTx": "ltrTx",
        "MasConfigured": "masConfigured",
        "MasRunning": "masRunning",
        "MepFNGDefect": "mepFNGDefect",
        "MepFNGDefectClearing": "mepFNGDefectClearing",
        "MepFNGDefectReported": "mepFNGDefectReported",
        "MepFNGReset": "mepFNGReset",
        "MepsConfigured": "mepsConfigured",
        "MepsRunning": "mepsRunning",
        "OnedmRx": "onedmRx",
        "OnedmTx": "onedmTx",
        "OutofSequenceCCMRx": "outofSequenceCCMRx",
        "PacketRx": "packetRx",
        "PacketTx": "packetTx",
        "PortName": "portName",
        "RdiRx": "rdiRx",
        "RdiTx": "rdiTx",
        "RemoteMEPs": "remoteMEPs",
        "RmepErrorDefect": "rmepErrorDefect",
        "RmepErrorNoDefect": "rmepErrorNoDefect",
        "RmepOk": "rmepOk",
        "SessionFlapCount": "sessionFlapCount",
        "TrunksConfigured": "trunksConfigured",
        "TrunksRunning": "trunksRunning",
        "TstOutofSequenceRx": "tstOutofSequenceRx",
        "TstOutofSequenceTx": "tstOutofSequenceTx",
        "TstPRBSBitErrorRx": "tstPRBSBitErrorRx",
        "TstRx": "tstRx",
        "TstTx": "tstTx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(CfmAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def AisRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: AIS Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["AisRx"])

    @AisRx.setter
    def AisRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AisRx"], value)

    @property
    def AisTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: AIS Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["AisTx"])

    @AisTx.setter
    def AisTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AisTx"], value)

    @property
    def BridgesConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bridges Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["BridgesConfigured"])

    @BridgesConfigured.setter
    def BridgesConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BridgesConfigured"], value)

    @property
    def BridgesRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bridges Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["BridgesRunning"])

    @BridgesRunning.setter
    def BridgesRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BridgesRunning"], value)

    @property
    def CcmRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CCM Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["CcmRx"])

    @CcmRx.setter
    def CcmRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CcmRx"], value)

    @property
    def CcmTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CCM Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["CcmTx"])

    @CcmTx.setter
    def CcmTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CcmTx"], value)

    @property
    def CcmUnexpectedPeriod(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CCM Unexpected Period
        """
        return self._get_attribute(self._SDM_ATT_MAP["CcmUnexpectedPeriod"])

    @CcmUnexpectedPeriod.setter
    def CcmUnexpectedPeriod(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CcmUnexpectedPeriod"], value)

    @property
    def DefectiveRMEPS(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Defective RMEPS
        """
        return self._get_attribute(self._SDM_ATT_MAP["DefectiveRMEPS"])

    @DefectiveRMEPS.setter
    def DefectiveRMEPS(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DefectiveRMEPS"], value)

    @property
    def DmmRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DMM Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmmRx"])

    @DmmRx.setter
    def DmmRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmmRx"], value)

    @property
    def DmmTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DMM Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmmTx"])

    @DmmTx.setter
    def DmmTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmmTx"], value)

    @property
    def DmrRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DMR Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmrRx"])

    @DmrRx.setter
    def DmrRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmrRx"], value)

    @property
    def DmrTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DMR Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmrTx"])

    @DmrTx.setter
    def DmrTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmrTx"], value)

    @property
    def InvalidCCMRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Invalid CCM Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidCCMRx"])

    @InvalidCCMRx.setter
    def InvalidCCMRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidCCMRx"], value)

    @property
    def InvalidLBMRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Invalid LBM Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidLBMRx"])

    @InvalidLBMRx.setter
    def InvalidLBMRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidLBMRx"], value)

    @property
    def InvalidLBRRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Invalid LBR Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidLBRRx"])

    @InvalidLBRRx.setter
    def InvalidLBRRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidLBRRx"], value)

    @property
    def InvalidLMRRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Invalid LMR Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidLMRRx"])

    @InvalidLMRRx.setter
    def InvalidLMRRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidLMRRx"], value)

    @property
    def InvalidLTMRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Invalid LTM Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidLTMRx"])

    @InvalidLTMRx.setter
    def InvalidLTMRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidLTMRx"], value)

    @property
    def InvalidLTRRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Invalid LTR Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidLTRRx"])

    @InvalidLTRRx.setter
    def InvalidLTRRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidLTRRx"], value)

    @property
    def LbmRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LBM Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LbmRx"])

    @LbmRx.setter
    def LbmRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LbmRx"], value)

    @property
    def LbmTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LBM Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LbmTx"])

    @LbmTx.setter
    def LbmTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LbmTx"], value)

    @property
    def LbrRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LBR Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LbrRx"])

    @LbrRx.setter
    def LbrRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LbrRx"], value)

    @property
    def LbrTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LBR Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LbrTx"])

    @LbrTx.setter
    def LbrTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LbrTx"], value)

    @property
    def LckRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LCK Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LckRx"])

    @LckRx.setter
    def LckRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LckRx"], value)

    @property
    def LckTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LCK Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LckTx"])

    @LckTx.setter
    def LckTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LckTx"], value)

    @property
    def LmmRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LMM Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmmRx"])

    @LmmRx.setter
    def LmmRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmmRx"], value)

    @property
    def LmmTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LMM Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmmTx"])

    @LmmTx.setter
    def LmmTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmmTx"], value)

    @property
    def LmrRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LMR Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmrRx"])

    @LmrRx.setter
    def LmrRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmrRx"], value)

    @property
    def LmrTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LMR Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LmrTx"])

    @LmrTx.setter
    def LmrTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LmrTx"], value)

    @property
    def LrRespond(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LR Respond
        """
        return self._get_attribute(self._SDM_ATT_MAP["LrRespond"])

    @LrRespond.setter
    def LrRespond(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LrRespond"], value)

    @property
    def LtmRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LTM Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LtmRx"])

    @LtmRx.setter
    def LtmRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LtmRx"], value)

    @property
    def LtmTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LTM Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LtmTx"])

    @LtmTx.setter
    def LtmTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LtmTx"], value)

    @property
    def LtrRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LTR Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LtrRx"])

    @LtrRx.setter
    def LtrRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LtrRx"], value)

    @property
    def LtrTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: LTR Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["LtrTx"])

    @LtrTx.setter
    def LtrTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LtrTx"], value)

    @property
    def MasConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MAs Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["MasConfigured"])

    @MasConfigured.setter
    def MasConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MasConfigured"], value)

    @property
    def MasRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MAs Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["MasRunning"])

    @MasRunning.setter
    def MasRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MasRunning"], value)

    @property
    def MepFNGDefect(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MEP FNG Defect
        """
        return self._get_attribute(self._SDM_ATT_MAP["MepFNGDefect"])

    @MepFNGDefect.setter
    def MepFNGDefect(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MepFNGDefect"], value)

    @property
    def MepFNGDefectClearing(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MEP FNG DefectClearing
        """
        return self._get_attribute(self._SDM_ATT_MAP["MepFNGDefectClearing"])

    @MepFNGDefectClearing.setter
    def MepFNGDefectClearing(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MepFNGDefectClearing"], value)

    @property
    def MepFNGDefectReported(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MEP FNG DefectReported
        """
        return self._get_attribute(self._SDM_ATT_MAP["MepFNGDefectReported"])

    @MepFNGDefectReported.setter
    def MepFNGDefectReported(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MepFNGDefectReported"], value)

    @property
    def MepFNGReset(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MEP FNG Reset
        """
        return self._get_attribute(self._SDM_ATT_MAP["MepFNGReset"])

    @MepFNGReset.setter
    def MepFNGReset(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MepFNGReset"], value)

    @property
    def MepsConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MEPs Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["MepsConfigured"])

    @MepsConfigured.setter
    def MepsConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MepsConfigured"], value)

    @property
    def MepsRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MEPs Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["MepsRunning"])

    @MepsRunning.setter
    def MepsRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MepsRunning"], value)

    @property
    def OnedmRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 1DM Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnedmRx"])

    @OnedmRx.setter
    def OnedmRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnedmRx"], value)

    @property
    def OnedmTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 1DM Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["OnedmTx"])

    @OnedmTx.setter
    def OnedmTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OnedmTx"], value)

    @property
    def OutofSequenceCCMRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Out of Sequence CCM Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutofSequenceCCMRx"])

    @OutofSequenceCCMRx.setter
    def OutofSequenceCCMRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutofSequenceCCMRx"], value)

    @property
    def PacketRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Packet Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketRx"])

    @PacketRx.setter
    def PacketRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketRx"], value)

    @property
    def PacketTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Packet Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketTx"])

    @PacketTx.setter
    def PacketTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PacketTx"], value)

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
    def RdiRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RDI Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RdiRx"])

    @RdiRx.setter
    def RdiRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RdiRx"], value)

    @property
    def RdiTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RDI Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RdiTx"])

    @RdiTx.setter
    def RdiTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RdiTx"], value)

    @property
    def RemoteMEPs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Remote MEPs
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteMEPs"])

    @RemoteMEPs.setter
    def RemoteMEPs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RemoteMEPs"], value)

    @property
    def RmepErrorDefect(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RMEP Error Defect
        """
        return self._get_attribute(self._SDM_ATT_MAP["RmepErrorDefect"])

    @RmepErrorDefect.setter
    def RmepErrorDefect(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RmepErrorDefect"], value)

    @property
    def RmepErrorNoDefect(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RMEP Error NoDefect
        """
        return self._get_attribute(self._SDM_ATT_MAP["RmepErrorNoDefect"])

    @RmepErrorNoDefect.setter
    def RmepErrorNoDefect(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RmepErrorNoDefect"], value)

    @property
    def RmepOk(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RMEP Ok
        """
        return self._get_attribute(self._SDM_ATT_MAP["RmepOk"])

    @RmepOk.setter
    def RmepOk(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RmepOk"], value)

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
    def TrunksConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Trunks Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrunksConfigured"])

    @TrunksConfigured.setter
    def TrunksConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrunksConfigured"], value)

    @property
    def TrunksRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Trunks Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrunksRunning"])

    @TrunksRunning.setter
    def TrunksRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrunksRunning"], value)

    @property
    def TstOutofSequenceRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: TST Out of Sequence Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstOutofSequenceRx"])

    @TstOutofSequenceRx.setter
    def TstOutofSequenceRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstOutofSequenceRx"], value)

    @property
    def TstOutofSequenceTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: TST Out of Sequence Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstOutofSequenceTx"])

    @TstOutofSequenceTx.setter
    def TstOutofSequenceTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstOutofSequenceTx"], value)

    @property
    def TstPRBSBitErrorRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: TST PRBS Bit Error Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstPRBSBitErrorRx"])

    @TstPRBSBitErrorRx.setter
    def TstPRBSBitErrorRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstPRBSBitErrorRx"], value)

    @property
    def TstRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: TST Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstRx"])

    @TstRx.setter
    def TstRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstRx"], value)

    @property
    def TstTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: TST Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["TstTx"])

    @TstTx.setter
    def TstTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TstTx"], value)

    def update(
        self,
        AisRx=None,
        AisTx=None,
        BridgesConfigured=None,
        BridgesRunning=None,
        CcmRx=None,
        CcmTx=None,
        CcmUnexpectedPeriod=None,
        DefectiveRMEPS=None,
        DmmRx=None,
        DmmTx=None,
        DmrRx=None,
        DmrTx=None,
        InvalidCCMRx=None,
        InvalidLBMRx=None,
        InvalidLBRRx=None,
        InvalidLMRRx=None,
        InvalidLTMRx=None,
        InvalidLTRRx=None,
        LbmRx=None,
        LbmTx=None,
        LbrRx=None,
        LbrTx=None,
        LckRx=None,
        LckTx=None,
        LmmRx=None,
        LmmTx=None,
        LmrRx=None,
        LmrTx=None,
        LrRespond=None,
        LtmRx=None,
        LtmTx=None,
        LtrRx=None,
        LtrTx=None,
        MasConfigured=None,
        MasRunning=None,
        MepFNGDefect=None,
        MepFNGDefectClearing=None,
        MepFNGDefectReported=None,
        MepFNGReset=None,
        MepsConfigured=None,
        MepsRunning=None,
        OnedmRx=None,
        OnedmTx=None,
        OutofSequenceCCMRx=None,
        PacketRx=None,
        PacketTx=None,
        PortName=None,
        RdiRx=None,
        RdiTx=None,
        RemoteMEPs=None,
        RmepErrorDefect=None,
        RmepErrorNoDefect=None,
        RmepOk=None,
        SessionFlapCount=None,
        TrunksConfigured=None,
        TrunksRunning=None,
        TstOutofSequenceRx=None,
        TstOutofSequenceTx=None,
        TstPRBSBitErrorRx=None,
        TstRx=None,
        TstTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> CfmAggregatedStatistics
        """Updates cfmAggregatedStatistics resource on the server.

        Args
        ----
        - AisRx (bool): AIS Rx
        - AisTx (bool): AIS Tx
        - BridgesConfigured (bool): Bridges Configured
        - BridgesRunning (bool): Bridges Running
        - CcmRx (bool): CCM Rx
        - CcmTx (bool): CCM Tx
        - CcmUnexpectedPeriod (bool): CCM Unexpected Period
        - DefectiveRMEPS (bool): Defective RMEPS
        - DmmRx (bool): DMM Rx
        - DmmTx (bool): DMM Tx
        - DmrRx (bool): DMR Rx
        - DmrTx (bool): DMR Tx
        - InvalidCCMRx (bool): Invalid CCM Rx
        - InvalidLBMRx (bool): Invalid LBM Rx
        - InvalidLBRRx (bool): Invalid LBR Rx
        - InvalidLMRRx (bool): Invalid LMR Rx
        - InvalidLTMRx (bool): Invalid LTM Rx
        - InvalidLTRRx (bool): Invalid LTR Rx
        - LbmRx (bool): LBM Rx
        - LbmTx (bool): LBM Tx
        - LbrRx (bool): LBR Rx
        - LbrTx (bool): LBR Tx
        - LckRx (bool): LCK Rx
        - LckTx (bool): LCK Tx
        - LmmRx (bool): LMM Rx
        - LmmTx (bool): LMM Tx
        - LmrRx (bool): LMR Rx
        - LmrTx (bool): LMR Tx
        - LrRespond (bool): LR Respond
        - LtmRx (bool): LTM Rx
        - LtmTx (bool): LTM Tx
        - LtrRx (bool): LTR Rx
        - LtrTx (bool): LTR Tx
        - MasConfigured (bool): MAs Configured
        - MasRunning (bool): MAs Running
        - MepFNGDefect (bool): MEP FNG Defect
        - MepFNGDefectClearing (bool): MEP FNG DefectClearing
        - MepFNGDefectReported (bool): MEP FNG DefectReported
        - MepFNGReset (bool): MEP FNG Reset
        - MepsConfigured (bool): MEPs Configured
        - MepsRunning (bool): MEPs Running
        - OnedmRx (bool): 1DM Rx
        - OnedmTx (bool): 1DM Tx
        - OutofSequenceCCMRx (bool): Out of Sequence CCM Rx
        - PacketRx (bool): Packet Rx
        - PacketTx (bool): Packet Tx
        - PortName (bool): Port Name
        - RdiRx (bool): RDI Rx
        - RdiTx (bool): RDI Tx
        - RemoteMEPs (bool): Remote MEPs
        - RmepErrorDefect (bool): RMEP Error Defect
        - RmepErrorNoDefect (bool): RMEP Error NoDefect
        - RmepOk (bool): RMEP Ok
        - SessionFlapCount (bool): Session Flap Count
        - TrunksConfigured (bool): Trunks Configured
        - TrunksRunning (bool): Trunks Running
        - TstOutofSequenceRx (bool): TST Out of Sequence Rx
        - TstOutofSequenceTx (bool): TST Out of Sequence Tx
        - TstPRBSBitErrorRx (bool): TST PRBS Bit Error Rx
        - TstRx (bool): TST Rx
        - TstTx (bool): TST Tx

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AisRx=None,
        AisTx=None,
        BridgesConfigured=None,
        BridgesRunning=None,
        CcmRx=None,
        CcmTx=None,
        CcmUnexpectedPeriod=None,
        DefectiveRMEPS=None,
        DmmRx=None,
        DmmTx=None,
        DmrRx=None,
        DmrTx=None,
        InvalidCCMRx=None,
        InvalidLBMRx=None,
        InvalidLBRRx=None,
        InvalidLMRRx=None,
        InvalidLTMRx=None,
        InvalidLTRRx=None,
        LbmRx=None,
        LbmTx=None,
        LbrRx=None,
        LbrTx=None,
        LckRx=None,
        LckTx=None,
        LmmRx=None,
        LmmTx=None,
        LmrRx=None,
        LmrTx=None,
        LrRespond=None,
        LtmRx=None,
        LtmTx=None,
        LtrRx=None,
        LtrTx=None,
        MasConfigured=None,
        MasRunning=None,
        MepFNGDefect=None,
        MepFNGDefectClearing=None,
        MepFNGDefectReported=None,
        MepFNGReset=None,
        MepsConfigured=None,
        MepsRunning=None,
        OnedmRx=None,
        OnedmTx=None,
        OutofSequenceCCMRx=None,
        PacketRx=None,
        PacketTx=None,
        PortName=None,
        RdiRx=None,
        RdiTx=None,
        RemoteMEPs=None,
        RmepErrorDefect=None,
        RmepErrorNoDefect=None,
        RmepOk=None,
        SessionFlapCount=None,
        TrunksConfigured=None,
        TrunksRunning=None,
        TstOutofSequenceRx=None,
        TstOutofSequenceTx=None,
        TstPRBSBitErrorRx=None,
        TstRx=None,
        TstTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> CfmAggregatedStatistics
        """Finds and retrieves cfmAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cfmAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cfmAggregatedStatistics resources from the server.

        Args
        ----
        - AisRx (bool): AIS Rx
        - AisTx (bool): AIS Tx
        - BridgesConfigured (bool): Bridges Configured
        - BridgesRunning (bool): Bridges Running
        - CcmRx (bool): CCM Rx
        - CcmTx (bool): CCM Tx
        - CcmUnexpectedPeriod (bool): CCM Unexpected Period
        - DefectiveRMEPS (bool): Defective RMEPS
        - DmmRx (bool): DMM Rx
        - DmmTx (bool): DMM Tx
        - DmrRx (bool): DMR Rx
        - DmrTx (bool): DMR Tx
        - InvalidCCMRx (bool): Invalid CCM Rx
        - InvalidLBMRx (bool): Invalid LBM Rx
        - InvalidLBRRx (bool): Invalid LBR Rx
        - InvalidLMRRx (bool): Invalid LMR Rx
        - InvalidLTMRx (bool): Invalid LTM Rx
        - InvalidLTRRx (bool): Invalid LTR Rx
        - LbmRx (bool): LBM Rx
        - LbmTx (bool): LBM Tx
        - LbrRx (bool): LBR Rx
        - LbrTx (bool): LBR Tx
        - LckRx (bool): LCK Rx
        - LckTx (bool): LCK Tx
        - LmmRx (bool): LMM Rx
        - LmmTx (bool): LMM Tx
        - LmrRx (bool): LMR Rx
        - LmrTx (bool): LMR Tx
        - LrRespond (bool): LR Respond
        - LtmRx (bool): LTM Rx
        - LtmTx (bool): LTM Tx
        - LtrRx (bool): LTR Rx
        - LtrTx (bool): LTR Tx
        - MasConfigured (bool): MAs Configured
        - MasRunning (bool): MAs Running
        - MepFNGDefect (bool): MEP FNG Defect
        - MepFNGDefectClearing (bool): MEP FNG DefectClearing
        - MepFNGDefectReported (bool): MEP FNG DefectReported
        - MepFNGReset (bool): MEP FNG Reset
        - MepsConfigured (bool): MEPs Configured
        - MepsRunning (bool): MEPs Running
        - OnedmRx (bool): 1DM Rx
        - OnedmTx (bool): 1DM Tx
        - OutofSequenceCCMRx (bool): Out of Sequence CCM Rx
        - PacketRx (bool): Packet Rx
        - PacketTx (bool): Packet Tx
        - PortName (bool): Port Name
        - RdiRx (bool): RDI Rx
        - RdiTx (bool): RDI Tx
        - RemoteMEPs (bool): Remote MEPs
        - RmepErrorDefect (bool): RMEP Error Defect
        - RmepErrorNoDefect (bool): RMEP Error NoDefect
        - RmepOk (bool): RMEP Ok
        - SessionFlapCount (bool): Session Flap Count
        - TrunksConfigured (bool): Trunks Configured
        - TrunksRunning (bool): Trunks Running
        - TstOutofSequenceRx (bool): TST Out of Sequence Rx
        - TstOutofSequenceTx (bool): TST Out of Sequence Tx
        - TstPRBSBitErrorRx (bool): TST PRBS Bit Error Rx
        - TstRx (bool): TST Rx
        - TstTx (bool): TST Tx

        Returns
        -------
        - self: This instance with matching cfmAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cfmAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cfmAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
