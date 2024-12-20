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


class PortStatistics(Base):
    """Represents stats of Port Statistics
    The PortStatistics class encapsulates a required portStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "portStatistics"
    _SDM_ATT_MAP = {
        "Aal5FramesRx": "aal5FramesRx",
        "Aal5FramesRxRate": "aal5FramesRxRate",
        "Aal5FramesTx": "aal5FramesTx",
        "Aal5FramesTxRate": "aal5FramesTxRate",
        "Aal5PayloadBytesRx": "aal5PayloadBytesRx",
        "Aal5PayloadBytesRxRate": "aal5PayloadBytesRxRate",
        "Aal5PayloadBytesTx": "aal5PayloadBytesTx",
        "Aal5PayloadBytesTxRate": "aal5PayloadBytesTxRate",
        "ActiveFECMode": "activeFECMode",
        "AlignmentErrors": "alignmentErrors",
        "AlignmentErrorsRate": "alignmentErrorsRate",
        "AsynchronousFramesSent": "asynchronousFramesSent",
        "AsynchronousFramesSentRate": "asynchronousFramesSentRate",
        "AtmCellsRx": "atmCellsRx",
        "AtmCellsRxRate": "atmCellsRxRate",
        "AtmCellsTx": "atmCellsTx",
        "AtmCellsTxRate": "atmCellsTxRate",
        "AtmUnregisteredCellsRx": "atmUnregisteredCellsRx",
        "AtmUnregisteredCellsRxRate": "atmUnregisteredCellsRxRate",
        "AvailableSeconds": "availableSeconds",
        "BackgroundBlockErrors": "backgroundBlockErrors",
        "BackgroundBlockErrorsRate": "backgroundBlockErrorsRate",
        "BackgroundChipTemperatureC": "backgroundChipTemperatureC",
        "BadPacketRxBroadcast": "badPacketRxBroadcast",
        "BadPacketRxMulticast": "badPacketRxMulticast",
        "BadTagICVDiscardedBroadcast": "badTagICVDiscardedBroadcast",
        "BadTagICVDiscardedMulticast": "badTagICVDiscardedMulticast",
        "BertBitsReceived": "bertBitsReceived",
        "BertBitsSent": "bertBitsSent",
        "BitErrorsReceived": "bitErrorsReceived",
        "BitErrorsSent": "bitErrorsSent",
        "BitsReceived": "bitsReceived",
        "BitsReceivedRate": "bitsReceivedRate",
        "BitsSent": "bitsSent",
        "BitsSentRate": "bitsSentRate",
        "BlockErrorState": "blockErrorState",
        "ByteAlignmentError": "byteAlignmentError",
        "ByteAlignmentErrorRate": "byteAlignmentErrorRate",
        "BytesRx": "bytesRx",
        "BytesRxRate": "bytesRxRate",
        "BytesSentTransmitDuration": "bytesSentTransmitDuration",
        "BytesTx": "bytesTx",
        "BytesTxRate": "bytesTxRate",
        "CaptureChipTemperatureC": "captureChipTemperatureC",
        "CaptureFilterUDS4": "captureFilterUDS4",
        "CaptureFilterUDS4Rate": "captureFilterUDS4Rate",
        "CaptureTriggerUDS3": "captureTriggerUDS3",
        "CaptureTriggerUDS3Rate": "captureTriggerUDS3Rate",
        "CentralChipTemperatureC": "centralChipTemperatureC",
        "CodeError": "codeError",
        "CodeErrorRate": "codeErrorRate",
        "CollisionFrames": "collisionFrames",
        "CollisionFramesRate": "collisionFramesRate",
        "Collisions": "collisions",
        "CollisionsRate": "collisionsRate",
        "ControlFramesRx": "controlFramesRx",
        "ControlFramesTx": "controlFramesTx",
        "CorrectedHCSErrorCount": "correctedHCSErrorCount",
        "CorrectedHCSErrorCountRate": "correctedHCSErrorCountRate",
        "CpuIdle": "cpuIdle",
        "CpuLoadAvg15Minutes": "cpuLoadAvg15Minutes",
        "CpuLoadAvg1Minute": "cpuLoadAvg1Minute",
        "CpuLoadAvg5Minutes": "cpuLoadAvg5Minutes",
        "CpuRxFrameSize1024to2047": "cpuRxFrameSize1024to2047",
        "CpuRxFrameSize128to255": "cpuRxFrameSize128to255",
        "CpuRxFrameSize2048to4095": "cpuRxFrameSize2048to4095",
        "CpuRxFrameSize256to511": "cpuRxFrameSize256to511",
        "CpuRxFrameSize4096andabove": "cpuRxFrameSize4096andabove",
        "CpuRxFrameSize512to1023": "cpuRxFrameSize512to1023",
        "CpuRxFrameSize64to127": "cpuRxFrameSize64to127",
        "CpuRxFrameSizelessthan64": "cpuRxFrameSizelessthan64",
        "CpuTxFrameSize1024to2047": "cpuTxFrameSize1024to2047",
        "CpuTxFrameSize128to255": "cpuTxFrameSize128to255",
        "CpuTxFrameSize2048to4095": "cpuTxFrameSize2048to4095",
        "CpuTxFrameSize256to511": "cpuTxFrameSize256to511",
        "CpuTxFrameSize4096andabove": "cpuTxFrameSize4096andabove",
        "CpuTxFrameSize512to1023": "cpuTxFrameSize512to1023",
        "CpuTxFrameSize64to127": "cpuTxFrameSize64to127",
        "CpuTxFrameSizelessthan64": "cpuTxFrameSizelessthan64",
        "CrcErrors": "crcErrors",
        "CrcErrorsRate": "crcErrorsRate",
        "CumulativeServiceDisruptionTimems": "cumulativeServiceDisruptionTimems",
        "CumulativeServiceDisruptionTimemsRate": "cumulativeServiceDisruptionTimemsRate",
        "CustomOrderedSetsReceived": "customOrderedSetsReceived",
        "CustomOrderedSetsReceivedRate": "customOrderedSetsReceivedRate",
        "CustomOrderedSetsSent": "customOrderedSetsSent",
        "CustomOrderedSetsSentRate": "customOrderedSetsSentRate",
        "DataIntegrityErrors": "dataIntegrityErrors",
        "DataIntegrityErrorsRate": "dataIntegrityErrorsRate",
        "DataIntegrityFramesRate": "dataIntegrityFramesRate",
        "DataIntegrityFramesRx": "dataIntegrityFramesRx",
        "DeskewBitErrorsReceived": "deskewBitErrorsReceived",
        "DeskewBitErrorsReceivedRate": "deskewBitErrorsReceivedRate",
        "DeskewBitErrorsSent": "deskewBitErrorsSent",
        "DeskewBitErrorsSentRate": "deskewBitErrorsSentRate",
        "DeskewErrorFreeFramesReceived": "deskewErrorFreeFramesReceived",
        "DeskewErrorFreeFramesReceivedRate": "deskewErrorFreeFramesReceivedRate",
        "DeskewErrorFreeFramesSent": "deskewErrorFreeFramesSent",
        "DeskewErrorFreeFramesSentRate": "deskewErrorFreeFramesSentRate",
        "DeskewErroredFramesReceived": "deskewErroredFramesReceived",
        "DeskewErroredFramesReceivedRate": "deskewErroredFramesReceivedRate",
        "DeskewErroredFramesSent": "deskewErroredFramesSent",
        "DeskewErroredFramesSentRate": "deskewErroredFramesSentRate",
        "DeskewLossOfFrame": "deskewLossOfFrame",
        "DeskewLossOfFrameRate": "deskewLossOfFrameRate",
        "Dhcpv4ACKsReceived": "dhcpv4ACKsReceived",
        "Dhcpv4AddressesLearned": "dhcpv4AddressesLearned",
        "Dhcpv4DiscoveredMessagesSent": "dhcpv4DiscoveredMessagesSent",
        "Dhcpv4EnabledInterfaces": "dhcpv4EnabledInterfaces",
        "Dhcpv4NACKsReceived": "dhcpv4NACKsReceived",
        "Dhcpv4OffersReceived": "dhcpv4OffersReceived",
        "Dhcpv4ReleasesSent": "dhcpv4ReleasesSent",
        "Dhcpv4RequestsSent": "dhcpv4RequestsSent",
        "DisparityErrors": "disparityErrors",
        "DisparityErrorsRate": "disparityErrorsRate",
        "DmaChipTemperatureC": "dmaChipTemperatureC",
        "DribbleErrors": "dribbleErrors",
        "DribbleErrorsRate": "dribbleErrorsRate",
        "DroppedFrames": "droppedFrames",
        "DroppedFramesRate": "droppedFramesRate",
        "DuplexMode": "duplexMode",
        "ElapsedTestTime": "elapsedTestTime",
        "ElapsedTestTimeRate": "elapsedTestTimeRate",
        "Encoding": "encoding",
        "EncryptedByteRx": "encryptedByteRx",
        "EncryptedByteTx": "encryptedByteTx",
        "EncryptedPacketRx": "encryptedPacketRx",
        "EncryptedPacketTx": "encryptedPacketTx",
        "EndofStreamDelimiterError": "endofStreamDelimiterError",
        "EofBigErrorFrameCount": "eofBigErrorFrameCount",
        "EofLateFrameCount": "eofLateFrameCount",
        "EofLateMaximumByteCount": "eofLateMaximumByteCount",
        "EofLateMinimumByteCount": "eofLateMinimumByteCount",
        "ErrorFreeSeconds": "errorFreeSeconds",
        "ErroredBlocks": "erroredBlocks",
        "ErroredBlocksRate": "erroredBlocksRate",
        "ErroredSeconds": "erroredSeconds",
        "EthernetCRC": "ethernetCRC",
        "EthernetCRCRate": "ethernetCRCRate",
        "EthernetOAMEventNotificationPDUsReceived": "ethernetOAMEventNotificationPDUsReceived",
        "EthernetOAMInformationPDUsReceived": "ethernetOAMInformationPDUsReceived",
        "EthernetOAMInformationPDUsSent": "ethernetOAMInformationPDUsSent",
        "EthernetOAMLoopbackControlPDUsReceived": "ethernetOAMLoopbackControlPDUsReceived",
        "EthernetOAMOrganisationPDUsReceived": "ethernetOAMOrganisationPDUsReceived",
        "EthernetOAMUnsupportedPDUsReceived": "ethernetOAMUnsupportedPDUsReceived",
        "EthernetOAMVariableRequestPDUsReceived": "ethernetOAMVariableRequestPDUsReceived",
        "EthernetOAMVariableResponseReceived": "ethernetOAMVariableResponseReceived",
        "ExcessiveCollisionFrames": "excessiveCollisionFrames",
        "ExcessiveCollisionFramesRate": "excessiveCollisionFramesRate",
        "FcFECCorrectedBlockCount": "fcFECCorrectedBlockCount",
        "FcFECCorrectedBlockCountRate": "fcFECCorrectedBlockCountRate",
        "FcFECCorrectedErrorBits": "fcFECCorrectedErrorBits",
        "FcFECCorrectedErrorBitsRate": "fcFECCorrectedErrorBitsRate",
        "FcFECUncorrectedBlockCount": "fcFECUncorrectedBlockCount",
        "FcFECUncorrectedBlockCountRate": "fcFECUncorrectedBlockCountRate",
        "FdiscSent": "fdiscSent",
        "FdiscSuccessful": "fdiscSuccessful",
        "FecCodewordswith0errors": "fecCodewordswith0errors",
        "FecCodewordswith0errorsRate": "fecCodewordswith0errorsRate",
        "FecCodewordswith10errors": "fecCodewordswith10errors",
        "FecCodewordswith10errorsRate": "fecCodewordswith10errorsRate",
        "FecCodewordswith11errors": "fecCodewordswith11errors",
        "FecCodewordswith11errorsRate": "fecCodewordswith11errorsRate",
        "FecCodewordswith12errors": "fecCodewordswith12errors",
        "FecCodewordswith12errorsRate": "fecCodewordswith12errorsRate",
        "FecCodewordswith13errors": "fecCodewordswith13errors",
        "FecCodewordswith13errorsRate": "fecCodewordswith13errorsRate",
        "FecCodewordswith14errors": "fecCodewordswith14errors",
        "FecCodewordswith14errorsRate": "fecCodewordswith14errorsRate",
        "FecCodewordswith15errors": "fecCodewordswith15errors",
        "FecCodewordswith15errorsRate": "fecCodewordswith15errorsRate",
        "FecCodewordswith1error": "fecCodewordswith1error",
        "FecCodewordswith1errorRate": "fecCodewordswith1errorRate",
        "FecCodewordswith2errors": "fecCodewordswith2errors",
        "FecCodewordswith2errorsRate": "fecCodewordswith2errorsRate",
        "FecCodewordswith3errors": "fecCodewordswith3errors",
        "FecCodewordswith3errorsRate": "fecCodewordswith3errorsRate",
        "FecCodewordswith4errors": "fecCodewordswith4errors",
        "FecCodewordswith4errorsRate": "fecCodewordswith4errorsRate",
        "FecCodewordswith5errors": "fecCodewordswith5errors",
        "FecCodewordswith5errorsRate": "fecCodewordswith5errorsRate",
        "FecCodewordswith6errors": "fecCodewordswith6errors",
        "FecCodewordswith6errorsRate": "fecCodewordswith6errorsRate",
        "FecCodewordswith7errors": "fecCodewordswith7errors",
        "FecCodewordswith7errorsRate": "fecCodewordswith7errorsRate",
        "FecCodewordswith8errors": "fecCodewordswith8errors",
        "FecCodewordswith8errorsRate": "fecCodewordswith8errorsRate",
        "FecCodewordswith9errors": "fecCodewordswith9errors",
        "FecCodewordswith9errorsRate": "fecCodewordswith9errorsRate",
        "FecCorrected0sCount": "fecCorrected0sCount",
        "FecCorrected0sCountRate": "fecCorrected0sCountRate",
        "FecCorrected1sCount": "fecCorrected1sCount",
        "FecCorrected1sCountRate": "fecCorrected1sCountRate",
        "FecCorrectedBitsCount": "fecCorrectedBitsCount",
        "FecCorrectedBitsCountRate": "fecCorrectedBitsCountRate",
        "FecCorrectedBytesCount": "fecCorrectedBytesCount",
        "FecCorrectedBytesCountRate": "fecCorrectedBytesCountRate",
        "FecCorrectedCodewords": "fecCorrectedCodewords",
        "FecCorrectedCodewordsRate": "fecCorrectedCodewordsRate",
        "FecFrameLossRatio": "fecFrameLossRatio",
        "FecMaxSymbolErrors": "fecMaxSymbolErrors",
        "FecTotalBitErrors": "fecTotalBitErrors",
        "FecTotalBitErrorsRate": "fecTotalBitErrorsRate",
        "FecTotalCodewords": "fecTotalCodewords",
        "FecTotalCodewordsRate": "fecTotalCodewordsRate",
        "FecTranscodingUncorrectableEvents": "fecTranscodingUncorrectableEvents",
        "FecTranscodingUncorrectableEventsRate": "fecTranscodingUncorrectableEventsRate",
        "FecUncorrectableCodewords": "fecUncorrectableCodewords",
        "FecUncorrectableCodewordsRate": "fecUncorrectableCodewordsRate",
        "FecUncorrectableSubrowCount": "fecUncorrectableSubrowCount",
        "FecUncorrectableSubrowCountRate": "fecUncorrectableSubrowCountRate",
        "FirecodeFECSync": "firecodeFECSync",
        "FivebDecodeError": "fivebDecodeError",
        "FlogiSent": "flogiSent",
        "FlogiSuccessful": "flogiSuccessful",
        "FlogoSent": "flogoSent",
        "FlowControlFrames": "flowControlFrames",
        "FlowControlFramesRate": "flowControlFramesRate",
        "FomBoardTemperatureC": "fomBoardTemperatureC",
        "FomInternalTemperatureC": "fomInternalTemperatureC",
        "FomPortTemperatureC": "fomPortTemperatureC",
        "Fragments": "fragments",
        "FragmentsRate": "fragmentsRate",
        "FramerAbort": "framerAbort",
        "FramerAbortRate": "framerAbortRate",
        "FramerMaxLength": "framerMaxLength",
        "FramerMaxLengthRate": "framerMaxLengthRate",
        "FramerMinLength": "framerMinLength",
        "FramerMinLengthRate": "framerMinLengthRate",
        "FramesReceivedwithCodingErrors": "framesReceivedwithCodingErrors",
        "FramesReceivedwithCodingErrorsRate": "framesReceivedwithCodingErrorsRate",
        "FramesReceivedwithEerrorCharacter": "framesReceivedwithEerrorCharacter",
        "FramesReceivedwithEerrorCharacterRate": "framesReceivedwithEerrorCharacterRate",
        "FramesTx": "framesTx",
        "FramesTxRate": "framesTxRate",
        "FreeMemory": "freeMemory",
        "FrontendChipTemperatureC": "frontendChipTemperatureC",
        "HostConfigStatus": "hostConfigStatus",
        "HostDataPathState": "hostDataPathState",
        "HostLaneCount": "hostLaneCount",
        "HostToMediaLane": "hostToMediaLane",
        "HostTxCDRLOL": "hostTxCDRLOL",
        "HostTxLOS": "hostTxLOS",
        "IdleCellsRx": "idleCellsRx",
        "IdleCellsRxRate": "idleCellsRxRate",
        "InputSignalStrengthdBm": "inputSignalStrengthdBm",
        "InsertionState": "insertionState",
        "InvalidEOF": "invalidEOF",
        "InvalidEOFRate": "invalidEOFRate",
        "InvalidICVAcceptedBroadcast": "invalidICVAcceptedBroadcast",
        "InvalidICVAcceptedMulticast": "invalidICVAcceptedMulticast",
        "InvalidICVDiscardedBroadcast": "invalidICVDiscardedBroadcast",
        "InvalidICVDiscardedMulticast": "invalidICVDiscardedMulticast",
        "Ipv4ChecksumErrors": "ipv4ChecksumErrors",
        "Ipv4ChecksumErrorsRate": "ipv4ChecksumErrorsRate",
        "Ipv4PacketsReceived": "ipv4PacketsReceived",
        "Ipv4PacketsReceivedRate": "ipv4PacketsReceivedRate",
        "KernelTimestamp": "kernelTimestamp",
        "L1BitsReceived": "l1BitsReceived",
        "L1BitsReceivedRate": "l1BitsReceivedRate",
        "L1BitsSent": "l1BitsSent",
        "L1BitsSentRate": "l1BitsSentRate",
        "L1LineRateReceivePercent": "l1LineRateReceivePercent",
        "L1LineRateTransmitPercent": "l1LineRateTransmitPercent",
        "LastServiceDisruptionTimems": "lastServiceDisruptionTimems",
        "LateCollisions": "lateCollisions",
        "LateCollisionsRate": "lateCollisionsRate",
        "LatencyChipTemperatureC": "latencyChipTemperatureC",
        "LineAIS": "lineAIS",
        "LineAISAlarmedSeconds": "lineAISAlarmedSeconds",
        "LineBIPB2": "lineBIPB2",
        "LineBIPB2Rate": "lineBIPB2Rate",
        "LineBIPErroredSeconds": "lineBIPErroredSeconds",
        "LineErrorFrames": "lineErrorFrames",
        "LineErrorFramesRate": "lineErrorFramesRate",
        "LineErrors": "lineErrors",
        "LineErrorsRate": "lineErrorsRate",
        "LineRDI": "lineRDI",
        "LineRDIUnavailableSeconds": "lineRDIUnavailableSeconds",
        "LineREIErroredSeconds": "lineREIErroredSeconds",
        "LineREIFEBE": "lineREIFEBE",
        "LineREIFEBERate": "lineREIFEBERate",
        "LineSpeed": "lineSpeed",
        "LinkFaultState": "linkFaultState",
        "LinkState": "linkState",
        "LocalFaults": "localFaults",
        "LocalOrderedSetsReceived": "localOrderedSetsReceived",
        "LocalOrderedSetsReceivedRate": "localOrderedSetsReceivedRate",
        "LocalOrderedSetsSent": "localOrderedSetsSent",
        "LocalOrderedSetsSentRate": "localOrderedSetsSentRate",
        "MaxServiceDisruptionTimems": "maxServiceDisruptionTimems",
        "MediaLaneCount": "mediaLaneCount",
        "MediaRxCDRLOL": "mediaRxCDRLOL",
        "MediaRxLOS": "mediaRxLOS",
        "MediaRxOpticalPower": "mediaRxOpticalPower",
        "MediaTxBiasCurrent": "mediaTxBiasCurrent",
        "MediaTxOpticalPower": "mediaTxOpticalPower",
        "MinServiceDisruptionTimems": "minServiceDisruptionTimems",
        "MisdirectedPacketCount": "misdirectedPacketCount",
        "MisdirectedPacketCountRate": "misdirectedPacketCountRate",
        "NonMACsecPacketRx": "nonMACsecPacketRx",
        "NonMACsecPacketTx": "nonMACsecPacketTx",
        "NportidsAcquired": "nportidsAcquired",
        "NportsEnabled": "nportsEnabled",
        "NsRegSent": "nsRegSent",
        "NsRegSuccessful": "nsRegSuccessful",
        "NumberofMismatched0s": "numberofMismatched0s",
        "NumberofMismatched0sRate": "numberofMismatched0sRate",
        "NumberofMismatched1s": "numberofMismatched1s",
        "NumberofMismatched1sRate": "numberofMismatched1sRate",
        "NumberofRRDYsReceived": "numberofRRDYsReceived",
        "NumberofRRDYsReceivedRate": "numberofRRDYsReceivedRate",
        "NumberofRRDYsSent": "numberofRRDYsSent",
        "NumberofRRDYsSentRate": "numberofRRDYsSentRate",
        "OutofWindowRxBroadcast": "outofWindowRxBroadcast",
        "OutofWindowRxMulticast": "outofWindowRxMulticast",
        "OverlayChipTemperatureC": "overlayChipTemperatureC",
        "Oversize": "oversize",
        "OversizeRate": "oversizeRate",
        "OversizeandCRCErrors": "oversizeandCRCErrors",
        "OversizeandCRCErrorsRate": "oversizeandCRCErrorsRate",
        "PathAIS": "pathAIS",
        "PathAISAlarmedSeconds": "pathAISAlarmedSeconds",
        "PathAISUnavailableSeconds": "pathAISUnavailableSeconds",
        "PathBIPB3": "pathBIPB3",
        "PathBIPB3Rate": "pathBIPB3Rate",
        "PathBIPErroredSeconds": "pathBIPErroredSeconds",
        "PathLOP": "pathLOP",
        "PathPLMC2": "pathPLMC2",
        "PathRDI": "pathRDI",
        "PathRDIUnavailableSeconds": "pathRDIUnavailableSeconds",
        "PathREIErroredSeconds": "pathREIErroredSeconds",
        "PathREIFEBE": "pathREIFEBE",
        "PathREIFEBERate": "pathREIFEBERate",
        "PauseAcknowledge": "pauseAcknowledge",
        "PauseAcknowledgeRate": "pauseAcknowledgeRate",
        "PauseEndFrames": "pauseEndFrames",
        "PauseEndFramesRate": "pauseEndFramesRate",
        "PauseOverwrite": "pauseOverwrite",
        "PauseOverwriteRate": "pauseOverwriteRate",
        "PcsIllegalCodes": "pcsIllegalCodes",
        "PcsIllegalCodesRate": "pcsIllegalCodesRate",
        "PcsIllegalIdle": "pcsIllegalIdle",
        "PcsIllegalIdleRate": "pcsIllegalIdleRate",
        "PcsIllegalOrderedSet": "pcsIllegalOrderedSet",
        "PcsIllegalOrderedSetRate": "pcsIllegalOrderedSetRate",
        "PcsIllegalSOF": "pcsIllegalSOF",
        "PcsIllegalSOFRate": "pcsIllegalSOFRate",
        "PcsLocalFaults": "pcsLocalFaults",
        "PcsLocalFaultsRate": "pcsLocalFaultsRate",
        "PcsOutofOrderData": "pcsOutofOrderData",
        "PcsOutofOrderDataRate": "pcsOutofOrderDataRate",
        "PcsOutofOrderEOF": "pcsOutofOrderEOF",
        "PcsOutofOrderEOFRate": "pcsOutofOrderEOFRate",
        "PcsOutofOrderOrderedSet": "pcsOutofOrderOrderedSet",
        "PcsOutofOrderOrderedSetRate": "pcsOutofOrderOrderedSetRate",
        "PcsOutofOrderSOF": "pcsOutofOrderSOF",
        "PcsOutofOrderSOFRate": "pcsOutofOrderSOFRate",
        "PcsRemoteFaults": "pcsRemoteFaults",
        "PcsRemoteFaultsRate": "pcsRemoteFaultsRate",
        "PcsSyncErrors": "pcsSyncErrors",
        "PcsSyncErrorsRate": "pcsSyncErrorsRate",
        "PercentCPULoad": "percentCPULoad",
        "PfcPriority0BufferMaxDepth": "pfcPriority0BufferMaxDepth",
        "PfcPriority0PacketDrop": "pfcPriority0PacketDrop",
        "PfcPriority0PacketDropRate": "pfcPriority0PacketDropRate",
        "PfcPriority0PauseRatioPercent": "pfcPriority0PauseRatioPercent",
        "PfcPriority0PauseStart": "pfcPriority0PauseStart",
        "PfcPriority0PauseStartResent": "pfcPriority0PauseStartResent",
        "PfcPriority0PauseStop": "pfcPriority0PauseStop",
        "PfcPriority1BufferMaxDepth": "pfcPriority1BufferMaxDepth",
        "PfcPriority1PacketDrop": "pfcPriority1PacketDrop",
        "PfcPriority1PacketDropRate": "pfcPriority1PacketDropRate",
        "PfcPriority1PauseRatioPercent": "pfcPriority1PauseRatioPercent",
        "PfcPriority1PauseStart": "pfcPriority1PauseStart",
        "PfcPriority1PauseStartResent": "pfcPriority1PauseStartResent",
        "PfcPriority1PauseStop": "pfcPriority1PauseStop",
        "PfcPriority2BufferMaxDepth": "pfcPriority2BufferMaxDepth",
        "PfcPriority2PacketDrop": "pfcPriority2PacketDrop",
        "PfcPriority2PacketDropRate": "pfcPriority2PacketDropRate",
        "PfcPriority2PauseRatioPercent": "pfcPriority2PauseRatioPercent",
        "PfcPriority2PauseStart": "pfcPriority2PauseStart",
        "PfcPriority2PauseStartResent": "pfcPriority2PauseStartResent",
        "PfcPriority2PauseStop": "pfcPriority2PauseStop",
        "PfcPriority3BufferMaxDepth": "pfcPriority3BufferMaxDepth",
        "PfcPriority3PacketDrop": "pfcPriority3PacketDrop",
        "PfcPriority3PacketDropRate": "pfcPriority3PacketDropRate",
        "PfcPriority3PauseRatioPercent": "pfcPriority3PauseRatioPercent",
        "PfcPriority3PauseStart": "pfcPriority3PauseStart",
        "PfcPriority3PauseStartResent": "pfcPriority3PauseStartResent",
        "PfcPriority3PauseStop": "pfcPriority3PauseStop",
        "PfcPriority4BufferMaxDepth": "pfcPriority4BufferMaxDepth",
        "PfcPriority4PacketDrop": "pfcPriority4PacketDrop",
        "PfcPriority4PacketDropRate": "pfcPriority4PacketDropRate",
        "PfcPriority4PauseRatioPercent": "pfcPriority4PauseRatioPercent",
        "PfcPriority4PauseStart": "pfcPriority4PauseStart",
        "PfcPriority4PauseStartResent": "pfcPriority4PauseStartResent",
        "PfcPriority4PauseStop": "pfcPriority4PauseStop",
        "PfcPriority5BufferMaxDepth": "pfcPriority5BufferMaxDepth",
        "PfcPriority5PacketDrop": "pfcPriority5PacketDrop",
        "PfcPriority5PacketDropRate": "pfcPriority5PacketDropRate",
        "PfcPriority5PauseRatioPercent": "pfcPriority5PauseRatioPercent",
        "PfcPriority5PauseStart": "pfcPriority5PauseStart",
        "PfcPriority5PauseStartResent": "pfcPriority5PauseStartResent",
        "PfcPriority5PauseStop": "pfcPriority5PauseStop",
        "PfcPriority6BufferMaxDepth": "pfcPriority6BufferMaxDepth",
        "PfcPriority6PacketDrop": "pfcPriority6PacketDrop",
        "PfcPriority6PacketDropRate": "pfcPriority6PacketDropRate",
        "PfcPriority6PauseRatioPercent": "pfcPriority6PauseRatioPercent",
        "PfcPriority6PauseStart": "pfcPriority6PauseStart",
        "PfcPriority6PauseStartResent": "pfcPriority6PauseStartResent",
        "PfcPriority6PauseStop": "pfcPriority6PauseStop",
        "PfcPriority7BufferMaxDepth": "pfcPriority7BufferMaxDepth",
        "PfcPriority7PacketDrop": "pfcPriority7PacketDrop",
        "PfcPriority7PacketDropRate": "pfcPriority7PacketDropRate",
        "PfcPriority7PauseRatioPercent": "pfcPriority7PauseRatioPercent",
        "PfcPriority7PauseStart": "pfcPriority7PauseStart",
        "PfcPriority7PauseStartResent": "pfcPriority7PauseStartResent",
        "PfcPriority7PauseStop": "pfcPriority7PauseStop",
        "PgidOverflow": "pgidOverflow",
        "PgidOverflowRate": "pgidOverflowRate",
        "PhyChipTemperatureC": "phyChipTemperatureC",
        "PlcaBeaconCount": "plcaBeaconCount",
        "PlcaBeaconCountRate": "plcaBeaconCountRate",
        "PlcaBeaconReceivedBeforeTransmitOpportunity": "plcaBeaconReceivedBeforeTransmitOpportunity",
        "PlcaCorruptedTransmitCount": "plcaCorruptedTransmitCount",
        "PlcaCorruptedTransmitCountRate": "plcaCorruptedTransmitCountRate",
        "PlcaEmptyCycleStatus": "plcaEmptyCycleStatus",
        "PlcaTransmitOpportunityCount": "plcaTransmitOpportunityCount",
        "PlcaTransmitOpportunityCountRate": "plcaTransmitOpportunityCountRate",
        "Plcasymboldetected": "plcasymboldetected",
        "PlmInternalTemperature1C": "plmInternalTemperature1C",
        "PlmInternalTemperature2C": "plmInternalTemperature2C",
        "PlmInternalTemperature3C": "plmInternalTemperature3C",
        "PlogiReceived": "plogiReceived",
        "PlogiSent": "plogiSent",
        "PlogiSuccessful": "plogiSuccessful",
        "PlogoReceived": "plogoReceived",
        "PlogoSent": "plogoSent",
        "PortCPUDoDStatus": "portCPUDoDStatus",
        "PortCPUFramesReceived": "portCPUFramesReceived",
        "PortCPUFramesSent": "portCPUFramesSent",
        "PortCPUFramesSentRate": "portCPUFramesSentRate",
        "PortCPUStatus": "portCPUStatus",
        "PortChipTemperatureC": "portChipTemperatureC",
        "PortName": "portName",
        "PrbsBerRatio": "prbsBerRatio",
        "PrbsBitsReceived": "prbsBitsReceived",
        "PrbsBitsReceivedRate": "prbsBitsReceivedRate",
        "PrbsErroredBits": "prbsErroredBits",
        "PrbsErroredBitsRate": "prbsErroredBitsRate",
        "PrbsFramesReceived": "prbsFramesReceived",
        "PrbsFramesReceivedRate": "prbsFramesReceivedRate",
        "PrbsFramesWithHeaderError": "prbsFramesWithHeaderError",
        "PrbsFramesWithHeaderErrorRate": "prbsFramesWithHeaderErrorRate",
        "PreFECBitErrorRatio": "preFECBitErrorRatio",
        "ProtectedByteRx": "protectedByteRx",
        "ProtectedByteTx": "protectedByteTx",
        "ProtectedPacketRx": "protectedPacketRx",
        "ProtectedPacketTx": "protectedPacketTx",
        "ProtocolServerVlanDroppedFrames": "protocolServerVlanDroppedFrames",
        "PtpAnnounceMessagesReceived": "ptpAnnounceMessagesReceived",
        "PtpAnnounceMessagesSent": "ptpAnnounceMessagesSent",
        "PtpDelayReqMessagesReceived": "ptpDelayReqMessagesReceived",
        "PtpDelayReqMessagesSent": "ptpDelayReqMessagesSent",
        "PtpDelayRespMessagesReceived": "ptpDelayRespMessagesReceived",
        "PtpDelayRespMessagesSent": "ptpDelayRespMessagesSent",
        "PtpFollowUpMessagesReceived": "ptpFollowUpMessagesReceived",
        "PtpFollowUpMessagesSent": "ptpFollowUpMessagesSent",
        "PtpSyncMessagesReceived": "ptpSyncMessagesReceived",
        "PtpSyncMessagesSent": "ptpSyncMessagesSent",
        "RamDiskUtilization": "ramDiskUtilization",
        "ReceiveArpReply": "receiveArpReply",
        "ReceiveArpRequest": "receiveArpRequest",
        "ReceiveInTransmitOpportunity": "receiveInTransmitOpportunity",
        "ReceiveNeighborAdvertisements": "receiveNeighborAdvertisements",
        "ReceiveNeighborSolicitation": "receiveNeighborSolicitation",
        "ReceivePingReply": "receivePingReply",
        "ReceivePingRequest": "receivePingRequest",
        "RemoteBuffertoBufferCreditCount": "remoteBuffertoBufferCreditCount",
        "RemoteBuffertoBufferCreditValue": "remoteBuffertoBufferCreditValue",
        "RemoteFaults": "remoteFaults",
        "RemoteOrderedSetsReceived": "remoteOrderedSetsReceived",
        "RemoteOrderedSetsReceivedRate": "remoteOrderedSetsReceivedRate",
        "RemoteOrderedSetsSent": "remoteOrderedSetsSent",
        "RemoteOrderedSetsSentRate": "remoteOrderedSetsSentRate",
        "Rocev2BadiCRCCount": "rocev2BadiCRCCount",
        "Rocev2OpCodeErrorCount": "rocev2OpCodeErrorCount",
        "RsFECCorrectedCodewordCount": "rsFECCorrectedCodewordCount",
        "RsFECCorrectedCodewordCountRate": "rsFECCorrectedCodewordCountRate",
        "RsFECUncorrectedCodewordCount": "rsFECUncorrectedCodewordCount",
        "RsFECUncorrectedCodewordCountRate": "rsFECUncorrectedCodewordCountRate",
        "Rx0FpgaTemperatureC": "rx0FpgaTemperatureC",
        "Rx1FpgaTemperatureC": "rx1FpgaTemperatureC",
        "RxBadPacketforBroadcastRate": "rxBadPacketforBroadcastRate",
        "RxBadPacketforMulticastRate": "rxBadPacketforMulticastRate",
        "RxBadTagPacketorICVDiscardedPacketforBroadcastRate": "rxBadTagPacketorICVDiscardedPacketforBroadcastRate",
        "RxBadTagPacketorICVDiscardedPacketforMulticastRate": "rxBadTagPacketorICVDiscardedPacketforMulticastRate",
        "RxBytesDecryptedBroadcast": "rxBytesDecryptedBroadcast",
        "RxBytesDecryptedMulticast": "rxBytesDecryptedMulticast",
        "RxBytesDecryptedforBroadcastRate": "rxBytesDecryptedforBroadcastRate",
        "RxBytesDecryptedforMulticastRate": "rxBytesDecryptedforMulticastRate",
        "RxBytesValidatedBroadcast": "rxBytesValidatedBroadcast",
        "RxBytesValidatedMulticast": "rxBytesValidatedMulticast",
        "RxBytesValidatedforBroadcastRate": "rxBytesValidatedforBroadcastRate",
        "RxBytesValidatedforMulticastRate": "rxBytesValidatedforMulticastRate",
        "RxEncryptedByteCountRate": "rxEncryptedByteCountRate",
        "RxEncryptedPacketCountRate": "rxEncryptedPacketCountRate",
        "RxFPExpressCRCTypeErrorCount": "rxFPExpressCRCTypeErrorCount",
        "RxFPExpressCRCTypeErrorCountRate": "rxFPExpressCRCTypeErrorCountRate",
        "RxFPFragCountError": "rxFPFragCountError",
        "RxFPFragCountErrorRate": "rxFPFragCountErrorRate",
        "RxFPInvalidCRCTypeErrorCount": "rxFPInvalidCRCTypeErrorCount",
        "RxFPInvalidCRCTypeErrorCountRate": "rxFPInvalidCRCTypeErrorCountRate",
        "RxFPReassemblyGoodCount": "rxFPReassemblyGoodCount",
        "RxFPReassemblyGoodCountRate": "rxFPReassemblyGoodCountRate",
        "RxFPRespondmPacketCRCErrorCount": "rxFPRespondmPacketCRCErrorCount",
        "RxFPRespondmPacketCRCErrorCountRate": "rxFPRespondmPacketCRCErrorCountRate",
        "RxFPRespondmPacketCount": "rxFPRespondmPacketCount",
        "RxFPRespondmPacketCountRate": "rxFPRespondmPacketCountRate",
        "RxFPSMDC0mPacketCRCErrorCount": "rxFPSMDC0mPacketCRCErrorCount",
        "RxFPSMDC0mPacketCRCErrorCountRate": "rxFPSMDC0mPacketCRCErrorCountRate",
        "RxFPSMDC0mPacketCount": "rxFPSMDC0mPacketCount",
        "RxFPSMDC0mPacketCountRate": "rxFPSMDC0mPacketCountRate",
        "RxFPSMDC1mPacketCRCErrorCount": "rxFPSMDC1mPacketCRCErrorCount",
        "RxFPSMDC1mPacketCRCErrorCountRate": "rxFPSMDC1mPacketCRCErrorCountRate",
        "RxFPSMDC1mPacketCount": "rxFPSMDC1mPacketCount",
        "RxFPSMDC1mPacketCountRate": "rxFPSMDC1mPacketCountRate",
        "RxFPSMDC2mPacketCRCErrorCount": "rxFPSMDC2mPacketCRCErrorCount",
        "RxFPSMDC2mPacketCRCErrorCountRate": "rxFPSMDC2mPacketCRCErrorCountRate",
        "RxFPSMDC2mPacketCount": "rxFPSMDC2mPacketCount",
        "RxFPSMDC2mPacketCountRate": "rxFPSMDC2mPacketCountRate",
        "RxFPSMDC3mPacketCRCErrorCount": "rxFPSMDC3mPacketCRCErrorCount",
        "RxFPSMDC3mPacketCRCErrorCountRate": "rxFPSMDC3mPacketCRCErrorCountRate",
        "RxFPSMDC3mPacketCount": "rxFPSMDC3mPacketCount",
        "RxFPSMDC3mPacketCountRate": "rxFPSMDC3mPacketCountRate",
        "RxFPSMDCCRCCalcErrorCount": "rxFPSMDCCRCCalcErrorCount",
        "RxFPSMDCCRCCalcErrorCountRate": "rxFPSMDCCRCCalcErrorCountRate",
        "RxFPSMDCFrameCountError": "rxFPSMDCFrameCountError",
        "RxFPSMDCFrameCountErrorRate": "rxFPSMDCFrameCountErrorRate",
        "RxFPSMDCTerminationErrorCount": "rxFPSMDCTerminationErrorCount",
        "RxFPSMDCTerminationErrorCountRate": "rxFPSMDCTerminationErrorCountRate",
        "RxFPSMDRNotTransmittedCount": "rxFPSMDRNotTransmittedCount",
        "RxFPSMDRNotTransmittedCountRate": "rxFPSMDRNotTransmittedCountRate",
        "RxFPSMDS0mPacketCRCErrorCount": "rxFPSMDS0mPacketCRCErrorCount",
        "RxFPSMDS0mPacketCRCErrorCountRate": "rxFPSMDS0mPacketCRCErrorCountRate",
        "RxFPSMDS0mPacketCount": "rxFPSMDS0mPacketCount",
        "RxFPSMDS0mPacketCountRate": "rxFPSMDS0mPacketCountRate",
        "RxFPSMDS1mPacketCRCErrorCount": "rxFPSMDS1mPacketCRCErrorCount",
        "RxFPSMDS1mPacketCRCErrorCountRate": "rxFPSMDS1mPacketCRCErrorCountRate",
        "RxFPSMDS1mPacketCount": "rxFPSMDS1mPacketCount",
        "RxFPSMDS1mPacketCountRate": "rxFPSMDS1mPacketCountRate",
        "RxFPSMDS2mPacketCRCErrorCount": "rxFPSMDS2mPacketCRCErrorCount",
        "RxFPSMDS2mPacketCRCErrorCountRate": "rxFPSMDS2mPacketCRCErrorCountRate",
        "RxFPSMDS2mPacketCount": "rxFPSMDS2mPacketCount",
        "RxFPSMDS2mPacketCountRate": "rxFPSMDS2mPacketCountRate",
        "RxFPSMDS3mPacketCRCErrorCount": "rxFPSMDS3mPacketCRCErrorCount",
        "RxFPSMDS3mPacketCRCErrorCountRate": "rxFPSMDS3mPacketCRCErrorCountRate",
        "RxFPSMDS3mPacketCount": "rxFPSMDS3mPacketCount",
        "RxFPSMDS3mPacketCountRate": "rxFPSMDS3mPacketCountRate",
        "RxFPSMDSFrameCountError": "rxFPSMDSFrameCountError",
        "RxFPSMDSFrameCountErrorRate": "rxFPSMDSFrameCountErrorRate",
        "RxFPSMDSStartProtocolError": "rxFPSMDSStartProtocolError",
        "RxFPSMDSStartProtocolErrorRate": "rxFPSMDSStartProtocolErrorRate",
        "RxFPSMDSTerminationErrorCount": "rxFPSMDSTerminationErrorCount",
        "RxFPSMDSTerminationErrorCountRate": "rxFPSMDSTerminationErrorCountRate",
        "RxFPSMDVNotReceivedCount": "rxFPSMDVNotReceivedCount",
        "RxFPSMDVNotReceivedCountRate": "rxFPSMDVNotReceivedCountRate",
        "RxFPUnexpectedSMDRCount": "rxFPUnexpectedSMDRCount",
        "RxFPUnexpectedSMDRCountRate": "rxFPUnexpectedSMDRCountRate",
        "RxFPVerifyProtocolError": "rxFPVerifyProtocolError",
        "RxFPVerifyProtocolErrorRate": "rxFPVerifyProtocolErrorRate",
        "RxFPVerifymPacketCRCErrorCount": "rxFPVerifymPacketCRCErrorCount",
        "RxFPVerifymPacketCRCErrorCountRate": "rxFPVerifymPacketCRCErrorCountRate",
        "RxFPVerifymPacketCount": "rxFPVerifymPacketCount",
        "RxFPVerifymPacketCountRate": "rxFPVerifymPacketCountRate",
        "RxFpgaTemperatureC": "rxFpgaTemperatureC",
        "RxInvalidICVDiscardedPacketforBroadcastRate": "rxInvalidICVDiscardedPacketforBroadcastRate",
        "RxInvalidICVDiscardedPacketforMulticastRate": "rxInvalidICVDiscardedPacketforMulticastRate",
        "RxInvalidICVPacketforBroadcastRate": "rxInvalidICVPacketforBroadcastRate",
        "RxInvalidICVPacketforMulticastRate": "rxInvalidICVPacketforMulticastRate",
        "RxNonMACsecPacketCountRate": "rxNonMACsecPacketCountRate",
        "RxOpticalPowerHighAlarm": "rxOpticalPowerHighAlarm",
        "RxOpticalPowerHighWarn": "rxOpticalPowerHighWarn",
        "RxOpticalPowerLimitFlag": "rxOpticalPowerLimitFlag",
        "RxOpticalPowerLowAlarm": "rxOpticalPowerLowAlarm",
        "RxOpticalPowerLowWarn": "rxOpticalPowerLowWarn",
        "RxOutofWindowPacketorOutofWindowDiscardedPacketforBroadcastRate": "rxOutofWindowPacketorOutofWindowDiscardedPacketforBroadcastRate",
        "RxOutofWindowPacketorOutofWindowDiscardedPacketforMulticastRate": "rxOutofWindowPacketorOutofWindowDiscardedPacketforMulticastRate",
        "RxPausePriorityGroup0Frames": "rxPausePriorityGroup0Frames",
        "RxPausePriorityGroup0FramesRate": "rxPausePriorityGroup0FramesRate",
        "RxPausePriorityGroup1Frames": "rxPausePriorityGroup1Frames",
        "RxPausePriorityGroup1FramesRate": "rxPausePriorityGroup1FramesRate",
        "RxPausePriorityGroup2Frames": "rxPausePriorityGroup2Frames",
        "RxPausePriorityGroup2FramesRate": "rxPausePriorityGroup2FramesRate",
        "RxPausePriorityGroup3Frames": "rxPausePriorityGroup3Frames",
        "RxPausePriorityGroup3FramesRate": "rxPausePriorityGroup3FramesRate",
        "RxPausePriorityGroup4Frames": "rxPausePriorityGroup4Frames",
        "RxPausePriorityGroup4FramesRate": "rxPausePriorityGroup4FramesRate",
        "RxPausePriorityGroup5Frames": "rxPausePriorityGroup5Frames",
        "RxPausePriorityGroup5FramesRate": "rxPausePriorityGroup5FramesRate",
        "RxPausePriorityGroup6Frames": "rxPausePriorityGroup6Frames",
        "RxPausePriorityGroup6FramesRate": "rxPausePriorityGroup6FramesRate",
        "RxPausePriorityGroup7Frames": "rxPausePriorityGroup7Frames",
        "RxPausePriorityGroup7FramesRate": "rxPausePriorityGroup7FramesRate",
        "RxProtectedByteCountRate": "rxProtectedByteCountRate",
        "RxProtectedPacketCountRate": "rxProtectedPacketCountRate",
        "RxRateKbps": "rxRateKbps",
        "RxRateMbps": "rxRateMbps",
        "RxRatebps": "rxRatebps",
        "RxRoCEACKFrameCount": "rxRoCEACKFrameCount",
        "RxRoCEACKFrameCountRate": "rxRoCEACKFrameCountRate",
        "RxRoCECNPFrameCount": "rxRoCECNPFrameCount",
        "RxRoCECNPFrameCountRate": "rxRoCECNPFrameCountRate",
        "RxRoCEECNFrameCount": "rxRoCEECNFrameCount",
        "RxRoCEECNFrameCountRate": "rxRoCEECNFrameCountRate",
        "RxRoCENAKFrameCount": "rxRoCENAKFrameCount",
        "RxRoCENAKFrameCountRate": "rxRoCENAKFrameCountRate",
        "RxRoCEOpcodeErrorCountRate": "rxRoCEOpcodeErrorCountRate",
        "RxRoCEPrePFCCNPFrameCount": "rxRoCEPrePFCCNPFrameCount",
        "RxRoCEPrePFCCNPFrameCountRate": "rxRoCEPrePFCCNPFrameCountRate",
        "RxRoCEiCRCErrorCountRate": "rxRoCEiCRCErrorCountRate",
        "RxSharedStat1": "rxSharedStat1",
        "RxSharedStat1Rate": "rxSharedStat1Rate",
        "RxSharedStat2": "rxSharedStat2",
        "RxSharedStat2Rate": "rxSharedStat2Rate",
        "RxUnknownSCIDiscardedPacketorUnusedSADiscardedPacketRate": "rxUnknownSCIDiscardedPacketorUnusedSADiscardedPacketRate",
        "RxUnknownSCIPacketorUnusedSAPacketRate": "rxUnknownSCIPacketorUnusedSAPacketRate",
        "RxUnvalidatedPacketCountRate": "rxUnvalidatedPacketCountRate",
        "RxValidPacketforBroadcastRate": "rxValidPacketforBroadcastRate",
        "RxValidPacketforMulticastRate": "rxValidPacketforMulticastRate",
        "ScheduledCellsTx": "scheduledCellsTx",
        "ScheduledCellsTxRate": "scheduledCellsTxRate",
        "ScheduledFramesTx": "scheduledFramesTx",
        "ScheduledFramesTxRate": "scheduledFramesTxRate",
        "ScheduledTransmitDuration": "scheduledTransmitDuration",
        "ScheduledTxRoCEACKFrameCount": "scheduledTxRoCEACKFrameCount",
        "ScheduledTxRoCEACKFrameCountRate": "scheduledTxRoCEACKFrameCountRate",
        "ScheduledTxRoCECNPFrameCount": "scheduledTxRoCECNPFrameCount",
        "ScheduledTxRoCECNPFrameCountRate": "scheduledTxRoCECNPFrameCountRate",
        "ScheduledTxRoCENAKFrameCount": "scheduledTxRoCENAKFrameCount",
        "ScheduledTxRoCENAKFrameCountRate": "scheduledTxRoCENAKFrameCountRate",
        "SchedulerChipTemperatureC": "schedulerChipTemperatureC",
        "SectionBIPB1": "sectionBIPB1",
        "SectionBIPB1Rate": "sectionBIPB1Rate",
        "SectionBIPErroredSeconds": "sectionBIPErroredSeconds",
        "SectionBIPSeverelyErroredSeconds": "sectionBIPSeverelyErroredSeconds",
        "SectionLOF": "sectionLOF",
        "SectionLOS": "sectionLOS",
        "SectionLOSSeconds": "sectionLOSSeconds",
        "SequenceErrors": "sequenceErrors",
        "SequenceErrorsRate": "sequenceErrorsRate",
        "SequenceFrames": "sequenceFrames",
        "SequenceFramesRate": "sequenceFramesRate",
        "SeverelyErroredSeconds": "severelyErroredSeconds",
        "SofBigErrorFrameCount": "sofBigErrorFrameCount",
        "SofEarlyFrameCount": "sofEarlyFrameCount",
        "SofEarlyMaximumByteCount": "sofEarlyMaximumByteCount",
        "SofEarlyMinimumByteCount": "sofEarlyMinimumByteCount",
        "StatelessBitsReceived": "statelessBitsReceived",
        "StatelessBitsSent": "statelessBitsSent",
        "StatelessBytesReceived": "statelessBytesReceived",
        "StatelessBytesReceivedRate": "statelessBytesReceivedRate",
        "StatelessBytesRxRate": "statelessBytesRxRate",
        "StatelessBytesSent": "statelessBytesSent",
        "StatelessBytesSentRate": "statelessBytesSentRate",
        "StatelessBytesTxRate": "statelessBytesTxRate",
        "StatelessFramesSent": "statelessFramesSent",
        "StatelessFramesSentRate": "statelessFramesSentRate",
        "StatelessRxRateKbps": "statelessRxRateKbps",
        "StatelessRxRateMbps": "statelessRxRateMbps",
        "StatelessRxRatebps": "statelessRxRatebps",
        "StatelessTxRateKbps": "statelessTxRateKbps",
        "StatelessTxRateMbps": "statelessTxRateMbps",
        "StatelessTxRatebps": "statelessTxRatebps",
        "Status": "status",
        "SupplyVoltageHighAlarm": "supplyVoltageHighAlarm",
        "SupplyVoltageHighWarn": "supplyVoltageHighWarn",
        "SupplyVoltageLimitFlag": "supplyVoltageLimitFlag",
        "SupplyVoltageLowAlarm": "supplyVoltageLowAlarm",
        "SupplyVoltageLowWarn": "supplyVoltageLowWarn",
        "TcpChecksumErrors": "tcpChecksumErrors",
        "TcpChecksumErrorsRate": "tcpChecksumErrorsRate",
        "TcpPacketsReceived": "tcpPacketsReceived",
        "TcpPacketsReceivedRate": "tcpPacketsReceivedRate",
        "TemperatureHighAlarm": "temperatureHighAlarm",
        "TemperatureHighWarn": "temperatureHighWarn",
        "TemperatureLimitFlag": "temperatureLimitFlag",
        "TemperatureLowAlarm": "temperatureLowAlarm",
        "TemperatureLowWarn": "temperatureLowWarn",
        "TotalMemory": "totalMemory",
        "TransceiverTemperatureC": "transceiverTemperatureC",
        "TransmitArpGratuitous": "transmitArpGratuitous",
        "TransmitArpGratuitousRate": "transmitArpGratuitousRate",
        "TransmitArpReply": "transmitArpReply",
        "TransmitArpRequest": "transmitArpRequest",
        "TransmitArpReverse": "transmitArpReverse",
        "TransmitArpReverseRate": "transmitArpReverseRate",
        "TransmitDurationClearedonStartTx": "transmitDurationClearedonStartTx",
        "TransmitNeighborAdvertisements": "transmitNeighborAdvertisements",
        "TransmitNeighborSolicitation": "transmitNeighborSolicitation",
        "TransmitPingReply": "transmitPingReply",
        "TransmitPingRequest": "transmitPingRequest",
        "Tx0FpgaTemperatureC": "tx0FpgaTemperatureC",
        "TxBiasCurrentHighAlarm": "txBiasCurrentHighAlarm",
        "TxBiasCurrentHighWarn": "txBiasCurrentHighWarn",
        "TxBiasCurrentLimitFlag": "txBiasCurrentLimitFlag",
        "TxBiasCurrentLowAlarm": "txBiasCurrentLowAlarm",
        "TxBiasCurrentLowWarn": "txBiasCurrentLowWarn",
        "TxEncryptedByteCountRate": "txEncryptedByteCountRate",
        "TxEncryptedPacketCountRate": "txEncryptedPacketCountRate",
        "TxFpgaTemperatureC": "txFpgaTemperatureC",
        "TxNonMACsecPacketCountRate": "txNonMACsecPacketCountRate",
        "TxOpticalPowerHighAlarm": "txOpticalPowerHighAlarm",
        "TxOpticalPowerHighWarn": "txOpticalPowerHighWarn",
        "TxOpticalPowerLimitFlag": "txOpticalPowerLimitFlag",
        "TxOpticalPowerLowAlarm": "txOpticalPowerLowAlarm",
        "TxOpticalPowerLowWarn": "txOpticalPowerLowWarn",
        "TxProtectedByteCountRate": "txProtectedByteCountRate",
        "TxProtectedPacketCountRate": "txProtectedPacketCountRate",
        "TxRateKbps": "txRateKbps",
        "TxRateMbps": "txRateMbps",
        "TxRatebps": "txRatebps",
        "UdpChecksumErrors": "udpChecksumErrors",
        "UdpChecksumErrorsRate": "udpChecksumErrorsRate",
        "UdpPacketsReceived": "udpPacketsReceived",
        "UdpPacketsReceivedRate": "udpPacketsReceivedRate",
        "UnavailableSeconds": "unavailableSeconds",
        "UncorrectedHCSErrorCount": "uncorrectedHCSErrorCount",
        "UncorrectedHCSErrorCountRate": "uncorrectedHCSErrorCountRate",
        "Undersize": "undersize",
        "UndersizeRate": "undersizeRate",
        "UnexpectedPLCABeaconReceived": "unexpectedPLCABeaconReceived",
        "UnknownSCISAAccepted": "unknownSCISAAccepted",
        "UnknownSCISADiscarded": "unknownSCISADiscarded",
        "UnvalidatedPacketRx": "unvalidatedPacketRx",
        "UserDefinedStat1": "userDefinedStat1",
        "UserDefinedStat1Rate": "userDefinedStat1Rate",
        "UserDefinedStat2": "userDefinedStat2",
        "UserDefinedStat2Rate": "userDefinedStat2Rate",
        "UserDefinedStat5": "userDefinedStat5",
        "UserDefinedStat5Rate": "userDefinedStat5Rate",
        "UserDefinedStat6": "userDefinedStat6",
        "UserDefinedStat6Rate": "userDefinedStat6Rate",
        "UserDefinedStatByteCount1": "userDefinedStatByteCount1",
        "UserDefinedStatByteCount1Rate": "userDefinedStatByteCount1Rate",
        "UserDefinedStatByteCount2": "userDefinedStatByteCount2",
        "UserDefinedStatByteCount2Rate": "userDefinedStatByteCount2Rate",
        "ValidFramesRx": "validFramesRx",
        "ValidFramesRxRate": "validFramesRxRate",
        "ValidPacketRxBroadcast": "validPacketRxBroadcast",
        "ValidPacketRxMulticast": "validPacketRxMulticast",
        "ValidStatelessFramesReceived": "validStatelessFramesReceived",
        "ValidStatelessFramesReceivedRate": "validStatelessFramesReceivedRate",
        "VlanTaggedFrames": "vlanTaggedFrames",
        "VlanTaggedFramesRate": "vlanTaggedFramesRate",
        "WindowClosedFrameCount": "windowClosedFrameCount",
        "WindowValidFrameCount": "windowValidFrameCount",
        "WindowViolationFrameCount": "windowViolationFrameCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PortStatistics, self).__init__(parent, list_op)

    @property
    def Aal5FramesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: AAL5 Frames Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Aal5FramesRx"])

    @Aal5FramesRx.setter
    def Aal5FramesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Aal5FramesRx"], value)

    @property
    def Aal5FramesRxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: AAL5 Frames Rx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["Aal5FramesRxRate"])

    @Aal5FramesRxRate.setter
    def Aal5FramesRxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Aal5FramesRxRate"], value)

    @property
    def Aal5FramesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: AAL5 Frames Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Aal5FramesTx"])

    @Aal5FramesTx.setter
    def Aal5FramesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Aal5FramesTx"], value)

    @property
    def Aal5FramesTxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: AAL5 Frames Tx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["Aal5FramesTxRate"])

    @Aal5FramesTxRate.setter
    def Aal5FramesTxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Aal5FramesTxRate"], value)

    @property
    def Aal5PayloadBytesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: AAL5 Payload Bytes Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Aal5PayloadBytesRx"])

    @Aal5PayloadBytesRx.setter
    def Aal5PayloadBytesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Aal5PayloadBytesRx"], value)

    @property
    def Aal5PayloadBytesRxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: AAL5 Payload Bytes Rx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["Aal5PayloadBytesRxRate"])

    @Aal5PayloadBytesRxRate.setter
    def Aal5PayloadBytesRxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Aal5PayloadBytesRxRate"], value)

    @property
    def Aal5PayloadBytesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: AAL5 Payload Bytes Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Aal5PayloadBytesTx"])

    @Aal5PayloadBytesTx.setter
    def Aal5PayloadBytesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Aal5PayloadBytesTx"], value)

    @property
    def Aal5PayloadBytesTxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: AAL5 Payload Bytes Tx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["Aal5PayloadBytesTxRate"])

    @Aal5PayloadBytesTxRate.setter
    def Aal5PayloadBytesTxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Aal5PayloadBytesTxRate"], value)

    @property
    def ActiveFECMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Active FEC Mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActiveFECMode"])

    @ActiveFECMode.setter
    def ActiveFECMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ActiveFECMode"], value)

    @property
    def AlignmentErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Alignment Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["AlignmentErrors"])

    @AlignmentErrors.setter
    def AlignmentErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AlignmentErrors"], value)

    @property
    def AlignmentErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Alignment Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["AlignmentErrorsRate"])

    @AlignmentErrorsRate.setter
    def AlignmentErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AlignmentErrorsRate"], value)

    @property
    def AsynchronousFramesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Asynchronous Frames Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["AsynchronousFramesSent"])

    @AsynchronousFramesSent.setter
    def AsynchronousFramesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AsynchronousFramesSent"], value)

    @property
    def AsynchronousFramesSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Asynchronous Frames Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["AsynchronousFramesSentRate"])

    @AsynchronousFramesSentRate.setter
    def AsynchronousFramesSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AsynchronousFramesSentRate"], value)

    @property
    def AtmCellsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ATM Cells Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AtmCellsRx"])

    @AtmCellsRx.setter
    def AtmCellsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AtmCellsRx"], value)

    @property
    def AtmCellsRxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ATM Cells Rx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["AtmCellsRxRate"])

    @AtmCellsRxRate.setter
    def AtmCellsRxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AtmCellsRxRate"], value)

    @property
    def AtmCellsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ATM Cells Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AtmCellsTx"])

    @AtmCellsTx.setter
    def AtmCellsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AtmCellsTx"], value)

    @property
    def AtmCellsTxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ATM Cells Tx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["AtmCellsTxRate"])

    @AtmCellsTxRate.setter
    def AtmCellsTxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AtmCellsTxRate"], value)

    @property
    def AtmUnregisteredCellsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ATM Unregistered Cells Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AtmUnregisteredCellsRx"])

    @AtmUnregisteredCellsRx.setter
    def AtmUnregisteredCellsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AtmUnregisteredCellsRx"], value)

    @property
    def AtmUnregisteredCellsRxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ATM Unregistered Cells Rx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["AtmUnregisteredCellsRxRate"])

    @AtmUnregisteredCellsRxRate.setter
    def AtmUnregisteredCellsRxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AtmUnregisteredCellsRxRate"], value)

    @property
    def AvailableSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Available Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableSeconds"])

    @AvailableSeconds.setter
    def AvailableSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AvailableSeconds"], value)

    @property
    def BackgroundBlockErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Background Block Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["BackgroundBlockErrors"])

    @BackgroundBlockErrors.setter
    def BackgroundBlockErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BackgroundBlockErrors"], value)

    @property
    def BackgroundBlockErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Background Block Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["BackgroundBlockErrorsRate"])

    @BackgroundBlockErrorsRate.setter
    def BackgroundBlockErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BackgroundBlockErrorsRate"], value)

    @property
    def BackgroundChipTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Background Chip Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["BackgroundChipTemperatureC"])

    @BackgroundChipTemperatureC.setter
    def BackgroundChipTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BackgroundChipTemperatureC"], value)

    @property
    def BadPacketRxBroadcast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bad Packet Rx Broadcast
        """
        return self._get_attribute(self._SDM_ATT_MAP["BadPacketRxBroadcast"])

    @BadPacketRxBroadcast.setter
    def BadPacketRxBroadcast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BadPacketRxBroadcast"], value)

    @property
    def BadPacketRxMulticast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bad Packet Rx Multicast
        """
        return self._get_attribute(self._SDM_ATT_MAP["BadPacketRxMulticast"])

    @BadPacketRxMulticast.setter
    def BadPacketRxMulticast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BadPacketRxMulticast"], value)

    @property
    def BadTagICVDiscardedBroadcast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bad Tag/ICV Discarded Broadcast
        """
        return self._get_attribute(self._SDM_ATT_MAP["BadTagICVDiscardedBroadcast"])

    @BadTagICVDiscardedBroadcast.setter
    def BadTagICVDiscardedBroadcast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BadTagICVDiscardedBroadcast"], value)

    @property
    def BadTagICVDiscardedMulticast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bad Tag/ICV Discarded Multicast
        """
        return self._get_attribute(self._SDM_ATT_MAP["BadTagICVDiscardedMulticast"])

    @BadTagICVDiscardedMulticast.setter
    def BadTagICVDiscardedMulticast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BadTagICVDiscardedMulticast"], value)

    @property
    def BertBitsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: BERT Bits Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["BertBitsReceived"])

    @BertBitsReceived.setter
    def BertBitsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BertBitsReceived"], value)

    @property
    def BertBitsSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: BERT Bits Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["BertBitsSent"])

    @BertBitsSent.setter
    def BertBitsSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BertBitsSent"], value)

    @property
    def BitErrorsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bit Errors Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["BitErrorsReceived"])

    @BitErrorsReceived.setter
    def BitErrorsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BitErrorsReceived"], value)

    @property
    def BitErrorsSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bit Errors Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["BitErrorsSent"])

    @BitErrorsSent.setter
    def BitErrorsSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BitErrorsSent"], value)

    @property
    def BitsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bits Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["BitsReceived"])

    @BitsReceived.setter
    def BitsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BitsReceived"], value)

    @property
    def BitsReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bits Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["BitsReceivedRate"])

    @BitsReceivedRate.setter
    def BitsReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BitsReceivedRate"], value)

    @property
    def BitsSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bits Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["BitsSent"])

    @BitsSent.setter
    def BitsSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BitsSent"], value)

    @property
    def BitsSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bits Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["BitsSentRate"])

    @BitsSentRate.setter
    def BitsSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BitsSentRate"], value)

    @property
    def BlockErrorState(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Block Error State
        """
        return self._get_attribute(self._SDM_ATT_MAP["BlockErrorState"])

    @BlockErrorState.setter
    def BlockErrorState(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BlockErrorState"], value)

    @property
    def ByteAlignmentError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Byte Alignment Error
        """
        return self._get_attribute(self._SDM_ATT_MAP["ByteAlignmentError"])

    @ByteAlignmentError.setter
    def ByteAlignmentError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ByteAlignmentError"], value)

    @property
    def ByteAlignmentErrorRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Byte Alignment Error Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["ByteAlignmentErrorRate"])

    @ByteAlignmentErrorRate.setter
    def ByteAlignmentErrorRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ByteAlignmentErrorRate"], value)

    @property
    def BytesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bytes Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BytesRx"])

    @BytesRx.setter
    def BytesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BytesRx"], value)

    @property
    def BytesRxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bytes Rx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["BytesRxRate"])

    @BytesRxRate.setter
    def BytesRxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BytesRxRate"], value)

    @property
    def BytesSentTransmitDuration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bytes Sent / Transmit Duration
        """
        return self._get_attribute(self._SDM_ATT_MAP["BytesSentTransmitDuration"])

    @BytesSentTransmitDuration.setter
    def BytesSentTransmitDuration(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BytesSentTransmitDuration"], value)

    @property
    def BytesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bytes Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BytesTx"])

    @BytesTx.setter
    def BytesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BytesTx"], value)

    @property
    def BytesTxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Bytes Tx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["BytesTxRate"])

    @BytesTxRate.setter
    def BytesTxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["BytesTxRate"], value)

    @property
    def CaptureChipTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Capture Chip Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["CaptureChipTemperatureC"])

    @CaptureChipTemperatureC.setter
    def CaptureChipTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CaptureChipTemperatureC"], value)

    @property
    def CaptureFilterUDS4(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Capture Filter (UDS 4)
        """
        return self._get_attribute(self._SDM_ATT_MAP["CaptureFilterUDS4"])

    @CaptureFilterUDS4.setter
    def CaptureFilterUDS4(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CaptureFilterUDS4"], value)

    @property
    def CaptureFilterUDS4Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Capture Filter (UDS 4) Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["CaptureFilterUDS4Rate"])

    @CaptureFilterUDS4Rate.setter
    def CaptureFilterUDS4Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CaptureFilterUDS4Rate"], value)

    @property
    def CaptureTriggerUDS3(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Capture Trigger (UDS 3)
        """
        return self._get_attribute(self._SDM_ATT_MAP["CaptureTriggerUDS3"])

    @CaptureTriggerUDS3.setter
    def CaptureTriggerUDS3(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CaptureTriggerUDS3"], value)

    @property
    def CaptureTriggerUDS3Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Capture Trigger (UDS 3) Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["CaptureTriggerUDS3Rate"])

    @CaptureTriggerUDS3Rate.setter
    def CaptureTriggerUDS3Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CaptureTriggerUDS3Rate"], value)

    @property
    def CentralChipTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Central Chip Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["CentralChipTemperatureC"])

    @CentralChipTemperatureC.setter
    def CentralChipTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CentralChipTemperatureC"], value)

    @property
    def CodeError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Code Error
        """
        return self._get_attribute(self._SDM_ATT_MAP["CodeError"])

    @CodeError.setter
    def CodeError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CodeError"], value)

    @property
    def CodeErrorRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Code Error Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["CodeErrorRate"])

    @CodeErrorRate.setter
    def CodeErrorRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CodeErrorRate"], value)

    @property
    def CollisionFrames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Collision Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["CollisionFrames"])

    @CollisionFrames.setter
    def CollisionFrames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CollisionFrames"], value)

    @property
    def CollisionFramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Collision Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["CollisionFramesRate"])

    @CollisionFramesRate.setter
    def CollisionFramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CollisionFramesRate"], value)

    @property
    def Collisions(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Collisions
        """
        return self._get_attribute(self._SDM_ATT_MAP["Collisions"])

    @Collisions.setter
    def Collisions(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Collisions"], value)

    @property
    def CollisionsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Collisions Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["CollisionsRate"])

    @CollisionsRate.setter
    def CollisionsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CollisionsRate"], value)

    @property
    def ControlFramesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Control Frames Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlFramesRx"])

    @ControlFramesRx.setter
    def ControlFramesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlFramesRx"], value)

    @property
    def ControlFramesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Control Frames Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlFramesTx"])

    @ControlFramesTx.setter
    def ControlFramesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlFramesTx"], value)

    @property
    def CorrectedHCSErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Corrected HCS Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["CorrectedHCSErrorCount"])

    @CorrectedHCSErrorCount.setter
    def CorrectedHCSErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CorrectedHCSErrorCount"], value)

    @property
    def CorrectedHCSErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Corrected HCS Error Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["CorrectedHCSErrorCountRate"])

    @CorrectedHCSErrorCountRate.setter
    def CorrectedHCSErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CorrectedHCSErrorCountRate"], value)

    @property
    def CpuIdle(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Idle
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuIdle"])

    @CpuIdle.setter
    def CpuIdle(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuIdle"], value)

    @property
    def CpuLoadAvg15Minutes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Load Avg (15 Minutes)
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuLoadAvg15Minutes"])

    @CpuLoadAvg15Minutes.setter
    def CpuLoadAvg15Minutes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuLoadAvg15Minutes"], value)

    @property
    def CpuLoadAvg1Minute(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Load Avg (1 Minute)
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuLoadAvg1Minute"])

    @CpuLoadAvg1Minute.setter
    def CpuLoadAvg1Minute(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuLoadAvg1Minute"], value)

    @property
    def CpuLoadAvg5Minutes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Load Avg (5 Minutes)
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuLoadAvg5Minutes"])

    @CpuLoadAvg5Minutes.setter
    def CpuLoadAvg5Minutes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuLoadAvg5Minutes"], value)

    @property
    def CpuRxFrameSize1024to2047(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Rx Frame Size 1024 to 2047
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuRxFrameSize1024to2047"])

    @CpuRxFrameSize1024to2047.setter
    def CpuRxFrameSize1024to2047(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuRxFrameSize1024to2047"], value)

    @property
    def CpuRxFrameSize128to255(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Rx Frame Size 128 to 255
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuRxFrameSize128to255"])

    @CpuRxFrameSize128to255.setter
    def CpuRxFrameSize128to255(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuRxFrameSize128to255"], value)

    @property
    def CpuRxFrameSize2048to4095(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Rx Frame Size 2048 to 4095
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuRxFrameSize2048to4095"])

    @CpuRxFrameSize2048to4095.setter
    def CpuRxFrameSize2048to4095(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuRxFrameSize2048to4095"], value)

    @property
    def CpuRxFrameSize256to511(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Rx Frame Size 256 to 511
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuRxFrameSize256to511"])

    @CpuRxFrameSize256to511.setter
    def CpuRxFrameSize256to511(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuRxFrameSize256to511"], value)

    @property
    def CpuRxFrameSize4096andabove(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Rx Frame Size 4096 and above
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuRxFrameSize4096andabove"])

    @CpuRxFrameSize4096andabove.setter
    def CpuRxFrameSize4096andabove(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuRxFrameSize4096andabove"], value)

    @property
    def CpuRxFrameSize512to1023(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Rx Frame Size 512 to 1023
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuRxFrameSize512to1023"])

    @CpuRxFrameSize512to1023.setter
    def CpuRxFrameSize512to1023(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuRxFrameSize512to1023"], value)

    @property
    def CpuRxFrameSize64to127(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Rx Frame Size 64 to 127
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuRxFrameSize64to127"])

    @CpuRxFrameSize64to127.setter
    def CpuRxFrameSize64to127(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuRxFrameSize64to127"], value)

    @property
    def CpuRxFrameSizelessthan64(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Rx Frame Size less than 64
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuRxFrameSizelessthan64"])

    @CpuRxFrameSizelessthan64.setter
    def CpuRxFrameSizelessthan64(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuRxFrameSizelessthan64"], value)

    @property
    def CpuTxFrameSize1024to2047(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Tx Frame Size 1024 to 2047
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuTxFrameSize1024to2047"])

    @CpuTxFrameSize1024to2047.setter
    def CpuTxFrameSize1024to2047(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuTxFrameSize1024to2047"], value)

    @property
    def CpuTxFrameSize128to255(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Tx Frame Size 128 to 255
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuTxFrameSize128to255"])

    @CpuTxFrameSize128to255.setter
    def CpuTxFrameSize128to255(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuTxFrameSize128to255"], value)

    @property
    def CpuTxFrameSize2048to4095(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Tx Frame Size 2048 to 4095
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuTxFrameSize2048to4095"])

    @CpuTxFrameSize2048to4095.setter
    def CpuTxFrameSize2048to4095(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuTxFrameSize2048to4095"], value)

    @property
    def CpuTxFrameSize256to511(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Tx Frame Size 256 to 511
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuTxFrameSize256to511"])

    @CpuTxFrameSize256to511.setter
    def CpuTxFrameSize256to511(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuTxFrameSize256to511"], value)

    @property
    def CpuTxFrameSize4096andabove(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Tx Frame Size 4096 and above
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuTxFrameSize4096andabove"])

    @CpuTxFrameSize4096andabove.setter
    def CpuTxFrameSize4096andabove(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuTxFrameSize4096andabove"], value)

    @property
    def CpuTxFrameSize512to1023(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Tx Frame Size 512 to 1023
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuTxFrameSize512to1023"])

    @CpuTxFrameSize512to1023.setter
    def CpuTxFrameSize512to1023(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuTxFrameSize512to1023"], value)

    @property
    def CpuTxFrameSize64to127(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Tx Frame Size 64 to 127
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuTxFrameSize64to127"])

    @CpuTxFrameSize64to127.setter
    def CpuTxFrameSize64to127(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuTxFrameSize64to127"], value)

    @property
    def CpuTxFrameSizelessthan64(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CPU Tx Frame Size less than 64
        """
        return self._get_attribute(self._SDM_ATT_MAP["CpuTxFrameSizelessthan64"])

    @CpuTxFrameSizelessthan64.setter
    def CpuTxFrameSizelessthan64(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CpuTxFrameSizelessthan64"], value)

    @property
    def CrcErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CRC Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["CrcErrors"])

    @CrcErrors.setter
    def CrcErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CrcErrors"], value)

    @property
    def CrcErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CRC Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["CrcErrorsRate"])

    @CrcErrorsRate.setter
    def CrcErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CrcErrorsRate"], value)

    @property
    def CumulativeServiceDisruptionTimems(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Cumulative Service Disruption Time (ms)
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["CumulativeServiceDisruptionTimems"]
        )

    @CumulativeServiceDisruptionTimems.setter
    def CumulativeServiceDisruptionTimems(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["CumulativeServiceDisruptionTimems"], value
        )

    @property
    def CumulativeServiceDisruptionTimemsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Cumulative Service Disruption Time (ms) Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["CumulativeServiceDisruptionTimemsRate"]
        )

    @CumulativeServiceDisruptionTimemsRate.setter
    def CumulativeServiceDisruptionTimemsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["CumulativeServiceDisruptionTimemsRate"], value
        )

    @property
    def CustomOrderedSetsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Custom Ordered Sets Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomOrderedSetsReceived"])

    @CustomOrderedSetsReceived.setter
    def CustomOrderedSetsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomOrderedSetsReceived"], value)

    @property
    def CustomOrderedSetsReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Custom Ordered Sets Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomOrderedSetsReceivedRate"])

    @CustomOrderedSetsReceivedRate.setter
    def CustomOrderedSetsReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomOrderedSetsReceivedRate"], value)

    @property
    def CustomOrderedSetsSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Custom Ordered Sets Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomOrderedSetsSent"])

    @CustomOrderedSetsSent.setter
    def CustomOrderedSetsSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomOrderedSetsSent"], value)

    @property
    def CustomOrderedSetsSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Custom Ordered Sets Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomOrderedSetsSentRate"])

    @CustomOrderedSetsSentRate.setter
    def CustomOrderedSetsSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomOrderedSetsSentRate"], value)

    @property
    def DataIntegrityErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Data Integrity Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataIntegrityErrors"])

    @DataIntegrityErrors.setter
    def DataIntegrityErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataIntegrityErrors"], value)

    @property
    def DataIntegrityErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Data Integrity Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataIntegrityErrorsRate"])

    @DataIntegrityErrorsRate.setter
    def DataIntegrityErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataIntegrityErrorsRate"], value)

    @property
    def DataIntegrityFramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Data Integrity Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataIntegrityFramesRate"])

    @DataIntegrityFramesRate.setter
    def DataIntegrityFramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataIntegrityFramesRate"], value)

    @property
    def DataIntegrityFramesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Data Integrity Frames Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataIntegrityFramesRx"])

    @DataIntegrityFramesRx.setter
    def DataIntegrityFramesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataIntegrityFramesRx"], value)

    @property
    def DeskewBitErrorsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Bit Errors Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewBitErrorsReceived"])

    @DeskewBitErrorsReceived.setter
    def DeskewBitErrorsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewBitErrorsReceived"], value)

    @property
    def DeskewBitErrorsReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Bit Errors Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewBitErrorsReceivedRate"])

    @DeskewBitErrorsReceivedRate.setter
    def DeskewBitErrorsReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewBitErrorsReceivedRate"], value)

    @property
    def DeskewBitErrorsSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Bit Errors Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewBitErrorsSent"])

    @DeskewBitErrorsSent.setter
    def DeskewBitErrorsSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewBitErrorsSent"], value)

    @property
    def DeskewBitErrorsSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Bit Errors Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewBitErrorsSentRate"])

    @DeskewBitErrorsSentRate.setter
    def DeskewBitErrorsSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewBitErrorsSentRate"], value)

    @property
    def DeskewErrorFreeFramesReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Error Free Frames Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewErrorFreeFramesReceived"])

    @DeskewErrorFreeFramesReceived.setter
    def DeskewErrorFreeFramesReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewErrorFreeFramesReceived"], value)

    @property
    def DeskewErrorFreeFramesReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Error Free Frames Received Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["DeskewErrorFreeFramesReceivedRate"]
        )

    @DeskewErrorFreeFramesReceivedRate.setter
    def DeskewErrorFreeFramesReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["DeskewErrorFreeFramesReceivedRate"], value
        )

    @property
    def DeskewErrorFreeFramesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Error Free Frames Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewErrorFreeFramesSent"])

    @DeskewErrorFreeFramesSent.setter
    def DeskewErrorFreeFramesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewErrorFreeFramesSent"], value)

    @property
    def DeskewErrorFreeFramesSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Error Free Frames Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewErrorFreeFramesSentRate"])

    @DeskewErrorFreeFramesSentRate.setter
    def DeskewErrorFreeFramesSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewErrorFreeFramesSentRate"], value)

    @property
    def DeskewErroredFramesReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Errored Frames Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewErroredFramesReceived"])

    @DeskewErroredFramesReceived.setter
    def DeskewErroredFramesReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewErroredFramesReceived"], value)

    @property
    def DeskewErroredFramesReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Errored Frames Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewErroredFramesReceivedRate"])

    @DeskewErroredFramesReceivedRate.setter
    def DeskewErroredFramesReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewErroredFramesReceivedRate"], value)

    @property
    def DeskewErroredFramesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Errored Frames Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewErroredFramesSent"])

    @DeskewErroredFramesSent.setter
    def DeskewErroredFramesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewErroredFramesSent"], value)

    @property
    def DeskewErroredFramesSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Errored Frames Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewErroredFramesSentRate"])

    @DeskewErroredFramesSentRate.setter
    def DeskewErroredFramesSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewErroredFramesSentRate"], value)

    @property
    def DeskewLossOfFrame(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Loss Of Frame
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewLossOfFrame"])

    @DeskewLossOfFrame.setter
    def DeskewLossOfFrame(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewLossOfFrame"], value)

    @property
    def DeskewLossOfFrameRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Deskew Loss Of Frame Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DeskewLossOfFrameRate"])

    @DeskewLossOfFrameRate.setter
    def DeskewLossOfFrameRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DeskewLossOfFrameRate"], value)

    @property
    def Dhcpv4ACKsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DHCPv4 ACKs Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcpv4ACKsReceived"])

    @Dhcpv4ACKsReceived.setter
    def Dhcpv4ACKsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcpv4ACKsReceived"], value)

    @property
    def Dhcpv4AddressesLearned(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DHCPv4 Addresses Learned
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcpv4AddressesLearned"])

    @Dhcpv4AddressesLearned.setter
    def Dhcpv4AddressesLearned(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcpv4AddressesLearned"], value)

    @property
    def Dhcpv4DiscoveredMessagesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DHCPv4 Discovered Messages Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcpv4DiscoveredMessagesSent"])

    @Dhcpv4DiscoveredMessagesSent.setter
    def Dhcpv4DiscoveredMessagesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcpv4DiscoveredMessagesSent"], value)

    @property
    def Dhcpv4EnabledInterfaces(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DHCPv4 Enabled Interfaces
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcpv4EnabledInterfaces"])

    @Dhcpv4EnabledInterfaces.setter
    def Dhcpv4EnabledInterfaces(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcpv4EnabledInterfaces"], value)

    @property
    def Dhcpv4NACKsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DHCPv4 NACKs Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcpv4NACKsReceived"])

    @Dhcpv4NACKsReceived.setter
    def Dhcpv4NACKsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcpv4NACKsReceived"], value)

    @property
    def Dhcpv4OffersReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DHCPv4 Offers Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcpv4OffersReceived"])

    @Dhcpv4OffersReceived.setter
    def Dhcpv4OffersReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcpv4OffersReceived"], value)

    @property
    def Dhcpv4ReleasesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DHCPv4 Releases Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcpv4ReleasesSent"])

    @Dhcpv4ReleasesSent.setter
    def Dhcpv4ReleasesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcpv4ReleasesSent"], value)

    @property
    def Dhcpv4RequestsSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DHCPv4 Requests Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["Dhcpv4RequestsSent"])

    @Dhcpv4RequestsSent.setter
    def Dhcpv4RequestsSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Dhcpv4RequestsSent"], value)

    @property
    def DisparityErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disparity Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisparityErrors"])

    @DisparityErrors.setter
    def DisparityErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisparityErrors"], value)

    @property
    def DisparityErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disparity Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisparityErrorsRate"])

    @DisparityErrorsRate.setter
    def DisparityErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisparityErrorsRate"], value)

    @property
    def DmaChipTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: DMA Chip Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["DmaChipTemperatureC"])

    @DmaChipTemperatureC.setter
    def DmaChipTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DmaChipTemperatureC"], value)

    @property
    def DribbleErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Dribble Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["DribbleErrors"])

    @DribbleErrors.setter
    def DribbleErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DribbleErrors"], value)

    @property
    def DribbleErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Dribble Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DribbleErrorsRate"])

    @DribbleErrorsRate.setter
    def DribbleErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DribbleErrorsRate"], value)

    @property
    def DroppedFrames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Dropped Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["DroppedFrames"])

    @DroppedFrames.setter
    def DroppedFrames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DroppedFrames"], value)

    @property
    def DroppedFramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Dropped Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["DroppedFramesRate"])

    @DroppedFramesRate.setter
    def DroppedFramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DroppedFramesRate"], value)

    @property
    def DuplexMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Duplex Mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["DuplexMode"])

    @DuplexMode.setter
    def DuplexMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DuplexMode"], value)

    @property
    def ElapsedTestTime(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Elapsed Test Time
        """
        return self._get_attribute(self._SDM_ATT_MAP["ElapsedTestTime"])

    @ElapsedTestTime.setter
    def ElapsedTestTime(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ElapsedTestTime"], value)

    @property
    def ElapsedTestTimeRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Elapsed Test Time Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["ElapsedTestTimeRate"])

    @ElapsedTestTimeRate.setter
    def ElapsedTestTimeRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ElapsedTestTimeRate"], value)

    @property
    def Encoding(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Encoding
        """
        return self._get_attribute(self._SDM_ATT_MAP["Encoding"])

    @Encoding.setter
    def Encoding(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Encoding"], value)

    @property
    def EncryptedByteRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Encrypted Byte Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EncryptedByteRx"])

    @EncryptedByteRx.setter
    def EncryptedByteRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EncryptedByteRx"], value)

    @property
    def EncryptedByteTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Encrypted Byte Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EncryptedByteTx"])

    @EncryptedByteTx.setter
    def EncryptedByteTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EncryptedByteTx"], value)

    @property
    def EncryptedPacketRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Encrypted Packet Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EncryptedPacketRx"])

    @EncryptedPacketRx.setter
    def EncryptedPacketRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EncryptedPacketRx"], value)

    @property
    def EncryptedPacketTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Encrypted Packet Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EncryptedPacketTx"])

    @EncryptedPacketTx.setter
    def EncryptedPacketTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EncryptedPacketTx"], value)

    @property
    def EndofStreamDelimiterError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: End-of-Stream Delimiter Error
        """
        return self._get_attribute(self._SDM_ATT_MAP["EndofStreamDelimiterError"])

    @EndofStreamDelimiterError.setter
    def EndofStreamDelimiterError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EndofStreamDelimiterError"], value)

    @property
    def EofBigErrorFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: EOF Big Error Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["EofBigErrorFrameCount"])

    @EofBigErrorFrameCount.setter
    def EofBigErrorFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EofBigErrorFrameCount"], value)

    @property
    def EofLateFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: EOF Late Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["EofLateFrameCount"])

    @EofLateFrameCount.setter
    def EofLateFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EofLateFrameCount"], value)

    @property
    def EofLateMaximumByteCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: EOF Late Maximum Byte Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["EofLateMaximumByteCount"])

    @EofLateMaximumByteCount.setter
    def EofLateMaximumByteCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EofLateMaximumByteCount"], value)

    @property
    def EofLateMinimumByteCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: EOF Late Minimum Byte Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["EofLateMinimumByteCount"])

    @EofLateMinimumByteCount.setter
    def EofLateMinimumByteCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EofLateMinimumByteCount"], value)

    @property
    def ErrorFreeSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Error Free Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorFreeSeconds"])

    @ErrorFreeSeconds.setter
    def ErrorFreeSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErrorFreeSeconds"], value)

    @property
    def ErroredBlocks(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Blocks
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErroredBlocks"])

    @ErroredBlocks.setter
    def ErroredBlocks(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErroredBlocks"], value)

    @property
    def ErroredBlocksRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Blocks Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErroredBlocksRate"])

    @ErroredBlocksRate.setter
    def ErroredBlocksRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErroredBlocksRate"], value)

    @property
    def ErroredSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Errored Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErroredSeconds"])

    @ErroredSeconds.setter
    def ErroredSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErroredSeconds"], value)

    @property
    def EthernetCRC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ethernet CRC
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetCRC"])

    @EthernetCRC.setter
    def EthernetCRC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetCRC"], value)

    @property
    def EthernetCRCRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ethernet CRC Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetCRCRate"])

    @EthernetCRCRate.setter
    def EthernetCRCRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetCRCRate"], value)

    @property
    def EthernetOAMEventNotificationPDUsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ethernet OAM Event Notification PDUs Received
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EthernetOAMEventNotificationPDUsReceived"]
        )

    @EthernetOAMEventNotificationPDUsReceived.setter
    def EthernetOAMEventNotificationPDUsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EthernetOAMEventNotificationPDUsReceived"], value
        )

    @property
    def EthernetOAMInformationPDUsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ethernet OAM Information PDUs Received
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EthernetOAMInformationPDUsReceived"]
        )

    @EthernetOAMInformationPDUsReceived.setter
    def EthernetOAMInformationPDUsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EthernetOAMInformationPDUsReceived"], value
        )

    @property
    def EthernetOAMInformationPDUsSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ethernet OAM Information PDUs Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetOAMInformationPDUsSent"])

    @EthernetOAMInformationPDUsSent.setter
    def EthernetOAMInformationPDUsSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EthernetOAMInformationPDUsSent"], value)

    @property
    def EthernetOAMLoopbackControlPDUsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ethernet OAM Loopback Control PDUs Received
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EthernetOAMLoopbackControlPDUsReceived"]
        )

    @EthernetOAMLoopbackControlPDUsReceived.setter
    def EthernetOAMLoopbackControlPDUsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EthernetOAMLoopbackControlPDUsReceived"], value
        )

    @property
    def EthernetOAMOrganisationPDUsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ethernet OAM Organisation PDUs Received
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EthernetOAMOrganisationPDUsReceived"]
        )

    @EthernetOAMOrganisationPDUsReceived.setter
    def EthernetOAMOrganisationPDUsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EthernetOAMOrganisationPDUsReceived"], value
        )

    @property
    def EthernetOAMUnsupportedPDUsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ethernet OAM Unsupported PDUs Received
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EthernetOAMUnsupportedPDUsReceived"]
        )

    @EthernetOAMUnsupportedPDUsReceived.setter
    def EthernetOAMUnsupportedPDUsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EthernetOAMUnsupportedPDUsReceived"], value
        )

    @property
    def EthernetOAMVariableRequestPDUsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ethernet OAM Variable Request PDUs Received
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EthernetOAMVariableRequestPDUsReceived"]
        )

    @EthernetOAMVariableRequestPDUsReceived.setter
    def EthernetOAMVariableRequestPDUsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EthernetOAMVariableRequestPDUsReceived"], value
        )

    @property
    def EthernetOAMVariableResponseReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ethernet OAM Variable Response Received
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EthernetOAMVariableResponseReceived"]
        )

    @EthernetOAMVariableResponseReceived.setter
    def EthernetOAMVariableResponseReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EthernetOAMVariableResponseReceived"], value
        )

    @property
    def ExcessiveCollisionFrames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Excessive Collision Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExcessiveCollisionFrames"])

    @ExcessiveCollisionFrames.setter
    def ExcessiveCollisionFrames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExcessiveCollisionFrames"], value)

    @property
    def ExcessiveCollisionFramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Excessive Collision Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExcessiveCollisionFramesRate"])

    @ExcessiveCollisionFramesRate.setter
    def ExcessiveCollisionFramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExcessiveCollisionFramesRate"], value)

    @property
    def FcFECCorrectedBlockCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FC-FEC Corrected Block Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcFECCorrectedBlockCount"])

    @FcFECCorrectedBlockCount.setter
    def FcFECCorrectedBlockCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcFECCorrectedBlockCount"], value)

    @property
    def FcFECCorrectedBlockCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FC-FEC Corrected Block Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcFECCorrectedBlockCountRate"])

    @FcFECCorrectedBlockCountRate.setter
    def FcFECCorrectedBlockCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcFECCorrectedBlockCountRate"], value)

    @property
    def FcFECCorrectedErrorBits(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FC-FEC Corrected Error Bits
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcFECCorrectedErrorBits"])

    @FcFECCorrectedErrorBits.setter
    def FcFECCorrectedErrorBits(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcFECCorrectedErrorBits"], value)

    @property
    def FcFECCorrectedErrorBitsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FC-FEC Corrected Error Bits Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcFECCorrectedErrorBitsRate"])

    @FcFECCorrectedErrorBitsRate.setter
    def FcFECCorrectedErrorBitsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcFECCorrectedErrorBitsRate"], value)

    @property
    def FcFECUncorrectedBlockCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FC-FEC Uncorrected Block Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcFECUncorrectedBlockCount"])

    @FcFECUncorrectedBlockCount.setter
    def FcFECUncorrectedBlockCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcFECUncorrectedBlockCount"], value)

    @property
    def FcFECUncorrectedBlockCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FC-FEC Uncorrected Block Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FcFECUncorrectedBlockCountRate"])

    @FcFECUncorrectedBlockCountRate.setter
    def FcFECUncorrectedBlockCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FcFECUncorrectedBlockCountRate"], value)

    @property
    def FdiscSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Fdisc Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["FdiscSent"])

    @FdiscSent.setter
    def FdiscSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FdiscSent"], value)

    @property
    def FdiscSuccessful(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Fdisc Successful
        """
        return self._get_attribute(self._SDM_ATT_MAP["FdiscSuccessful"])

    @FdiscSuccessful.setter
    def FdiscSuccessful(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FdiscSuccessful"], value)

    @property
    def FecCodewordswith0errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 0 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith0errors"])

    @FecCodewordswith0errors.setter
    def FecCodewordswith0errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith0errors"], value)

    @property
    def FecCodewordswith0errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 0 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith0errorsRate"])

    @FecCodewordswith0errorsRate.setter
    def FecCodewordswith0errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith0errorsRate"], value)

    @property
    def FecCodewordswith10errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 10 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith10errors"])

    @FecCodewordswith10errors.setter
    def FecCodewordswith10errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith10errors"], value)

    @property
    def FecCodewordswith10errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 10 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith10errorsRate"])

    @FecCodewordswith10errorsRate.setter
    def FecCodewordswith10errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith10errorsRate"], value)

    @property
    def FecCodewordswith11errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 11 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith11errors"])

    @FecCodewordswith11errors.setter
    def FecCodewordswith11errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith11errors"], value)

    @property
    def FecCodewordswith11errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 11 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith11errorsRate"])

    @FecCodewordswith11errorsRate.setter
    def FecCodewordswith11errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith11errorsRate"], value)

    @property
    def FecCodewordswith12errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 12 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith12errors"])

    @FecCodewordswith12errors.setter
    def FecCodewordswith12errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith12errors"], value)

    @property
    def FecCodewordswith12errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 12 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith12errorsRate"])

    @FecCodewordswith12errorsRate.setter
    def FecCodewordswith12errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith12errorsRate"], value)

    @property
    def FecCodewordswith13errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 13 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith13errors"])

    @FecCodewordswith13errors.setter
    def FecCodewordswith13errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith13errors"], value)

    @property
    def FecCodewordswith13errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 13 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith13errorsRate"])

    @FecCodewordswith13errorsRate.setter
    def FecCodewordswith13errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith13errorsRate"], value)

    @property
    def FecCodewordswith14errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 14 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith14errors"])

    @FecCodewordswith14errors.setter
    def FecCodewordswith14errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith14errors"], value)

    @property
    def FecCodewordswith14errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 14 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith14errorsRate"])

    @FecCodewordswith14errorsRate.setter
    def FecCodewordswith14errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith14errorsRate"], value)

    @property
    def FecCodewordswith15errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 15 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith15errors"])

    @FecCodewordswith15errors.setter
    def FecCodewordswith15errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith15errors"], value)

    @property
    def FecCodewordswith15errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 15 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith15errorsRate"])

    @FecCodewordswith15errorsRate.setter
    def FecCodewordswith15errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith15errorsRate"], value)

    @property
    def FecCodewordswith1error(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 1 error
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith1error"])

    @FecCodewordswith1error.setter
    def FecCodewordswith1error(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith1error"], value)

    @property
    def FecCodewordswith1errorRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 1 error Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith1errorRate"])

    @FecCodewordswith1errorRate.setter
    def FecCodewordswith1errorRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith1errorRate"], value)

    @property
    def FecCodewordswith2errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 2 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith2errors"])

    @FecCodewordswith2errors.setter
    def FecCodewordswith2errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith2errors"], value)

    @property
    def FecCodewordswith2errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 2 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith2errorsRate"])

    @FecCodewordswith2errorsRate.setter
    def FecCodewordswith2errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith2errorsRate"], value)

    @property
    def FecCodewordswith3errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 3 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith3errors"])

    @FecCodewordswith3errors.setter
    def FecCodewordswith3errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith3errors"], value)

    @property
    def FecCodewordswith3errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 3 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith3errorsRate"])

    @FecCodewordswith3errorsRate.setter
    def FecCodewordswith3errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith3errorsRate"], value)

    @property
    def FecCodewordswith4errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 4 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith4errors"])

    @FecCodewordswith4errors.setter
    def FecCodewordswith4errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith4errors"], value)

    @property
    def FecCodewordswith4errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 4 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith4errorsRate"])

    @FecCodewordswith4errorsRate.setter
    def FecCodewordswith4errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith4errorsRate"], value)

    @property
    def FecCodewordswith5errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 5 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith5errors"])

    @FecCodewordswith5errors.setter
    def FecCodewordswith5errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith5errors"], value)

    @property
    def FecCodewordswith5errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 5 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith5errorsRate"])

    @FecCodewordswith5errorsRate.setter
    def FecCodewordswith5errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith5errorsRate"], value)

    @property
    def FecCodewordswith6errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 6 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith6errors"])

    @FecCodewordswith6errors.setter
    def FecCodewordswith6errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith6errors"], value)

    @property
    def FecCodewordswith6errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 6 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith6errorsRate"])

    @FecCodewordswith6errorsRate.setter
    def FecCodewordswith6errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith6errorsRate"], value)

    @property
    def FecCodewordswith7errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 7 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith7errors"])

    @FecCodewordswith7errors.setter
    def FecCodewordswith7errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith7errors"], value)

    @property
    def FecCodewordswith7errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 7 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith7errorsRate"])

    @FecCodewordswith7errorsRate.setter
    def FecCodewordswith7errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith7errorsRate"], value)

    @property
    def FecCodewordswith8errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 8 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith8errors"])

    @FecCodewordswith8errors.setter
    def FecCodewordswith8errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith8errors"], value)

    @property
    def FecCodewordswith8errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 8 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith8errorsRate"])

    @FecCodewordswith8errorsRate.setter
    def FecCodewordswith8errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith8errorsRate"], value)

    @property
    def FecCodewordswith9errors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 9 errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith9errors"])

    @FecCodewordswith9errors.setter
    def FecCodewordswith9errors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith9errors"], value)

    @property
    def FecCodewordswith9errorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Codewords with 9 errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCodewordswith9errorsRate"])

    @FecCodewordswith9errorsRate.setter
    def FecCodewordswith9errorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCodewordswith9errorsRate"], value)

    @property
    def FecCorrected0sCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Corrected 0s Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCorrected0sCount"])

    @FecCorrected0sCount.setter
    def FecCorrected0sCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCorrected0sCount"], value)

    @property
    def FecCorrected0sCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Corrected 0s Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCorrected0sCountRate"])

    @FecCorrected0sCountRate.setter
    def FecCorrected0sCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCorrected0sCountRate"], value)

    @property
    def FecCorrected1sCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Corrected 1s Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCorrected1sCount"])

    @FecCorrected1sCount.setter
    def FecCorrected1sCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCorrected1sCount"], value)

    @property
    def FecCorrected1sCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Corrected 1s Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCorrected1sCountRate"])

    @FecCorrected1sCountRate.setter
    def FecCorrected1sCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCorrected1sCountRate"], value)

    @property
    def FecCorrectedBitsCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Corrected Bits Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCorrectedBitsCount"])

    @FecCorrectedBitsCount.setter
    def FecCorrectedBitsCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCorrectedBitsCount"], value)

    @property
    def FecCorrectedBitsCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Corrected Bits Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCorrectedBitsCountRate"])

    @FecCorrectedBitsCountRate.setter
    def FecCorrectedBitsCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCorrectedBitsCountRate"], value)

    @property
    def FecCorrectedBytesCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Corrected Bytes Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCorrectedBytesCount"])

    @FecCorrectedBytesCount.setter
    def FecCorrectedBytesCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCorrectedBytesCount"], value)

    @property
    def FecCorrectedBytesCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Corrected Bytes Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCorrectedBytesCountRate"])

    @FecCorrectedBytesCountRate.setter
    def FecCorrectedBytesCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCorrectedBytesCountRate"], value)

    @property
    def FecCorrectedCodewords(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Corrected Codewords
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCorrectedCodewords"])

    @FecCorrectedCodewords.setter
    def FecCorrectedCodewords(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCorrectedCodewords"], value)

    @property
    def FecCorrectedCodewordsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Corrected Codewords Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecCorrectedCodewordsRate"])

    @FecCorrectedCodewordsRate.setter
    def FecCorrectedCodewordsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecCorrectedCodewordsRate"], value)

    @property
    def FecFrameLossRatio(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Frame Loss Ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecFrameLossRatio"])

    @FecFrameLossRatio.setter
    def FecFrameLossRatio(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecFrameLossRatio"], value)

    @property
    def FecMaxSymbolErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Max Symbol Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecMaxSymbolErrors"])

    @FecMaxSymbolErrors.setter
    def FecMaxSymbolErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecMaxSymbolErrors"], value)

    @property
    def FecTotalBitErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Total Bit Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecTotalBitErrors"])

    @FecTotalBitErrors.setter
    def FecTotalBitErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecTotalBitErrors"], value)

    @property
    def FecTotalBitErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Total Bit Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecTotalBitErrorsRate"])

    @FecTotalBitErrorsRate.setter
    def FecTotalBitErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecTotalBitErrorsRate"], value)

    @property
    def FecTotalCodewords(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Total Codewords
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecTotalCodewords"])

    @FecTotalCodewords.setter
    def FecTotalCodewords(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecTotalCodewords"], value)

    @property
    def FecTotalCodewordsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Total Codewords Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecTotalCodewordsRate"])

    @FecTotalCodewordsRate.setter
    def FecTotalCodewordsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecTotalCodewordsRate"], value)

    @property
    def FecTranscodingUncorrectableEvents(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Transcoding Uncorrectable Events
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FecTranscodingUncorrectableEvents"]
        )

    @FecTranscodingUncorrectableEvents.setter
    def FecTranscodingUncorrectableEvents(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FecTranscodingUncorrectableEvents"], value
        )

    @property
    def FecTranscodingUncorrectableEventsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Transcoding Uncorrectable Events Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FecTranscodingUncorrectableEventsRate"]
        )

    @FecTranscodingUncorrectableEventsRate.setter
    def FecTranscodingUncorrectableEventsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FecTranscodingUncorrectableEventsRate"], value
        )

    @property
    def FecUncorrectableCodewords(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Uncorrectable Codewords
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecUncorrectableCodewords"])

    @FecUncorrectableCodewords.setter
    def FecUncorrectableCodewords(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecUncorrectableCodewords"], value)

    @property
    def FecUncorrectableCodewordsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Uncorrectable Codewords Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecUncorrectableCodewordsRate"])

    @FecUncorrectableCodewordsRate.setter
    def FecUncorrectableCodewordsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecUncorrectableCodewordsRate"], value)

    @property
    def FecUncorrectableSubrowCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Uncorrectable Subrow Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecUncorrectableSubrowCount"])

    @FecUncorrectableSubrowCount.setter
    def FecUncorrectableSubrowCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecUncorrectableSubrowCount"], value)

    @property
    def FecUncorrectableSubrowCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FEC Uncorrectable Subrow Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FecUncorrectableSubrowCountRate"])

    @FecUncorrectableSubrowCountRate.setter
    def FecUncorrectableSubrowCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FecUncorrectableSubrowCountRate"], value)

    @property
    def FirecodeFECSync(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Fire code FEC Sync
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirecodeFECSync"])

    @FirecodeFECSync.setter
    def FirecodeFECSync(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirecodeFECSync"], value)

    @property
    def FivebDecodeError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 5B Decode Error
        """
        return self._get_attribute(self._SDM_ATT_MAP["FivebDecodeError"])

    @FivebDecodeError.setter
    def FivebDecodeError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FivebDecodeError"], value)

    @property
    def FlogiSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flogi Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlogiSent"])

    @FlogiSent.setter
    def FlogiSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlogiSent"], value)

    @property
    def FlogiSuccessful(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flogi Successful
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlogiSuccessful"])

    @FlogiSuccessful.setter
    def FlogiSuccessful(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlogiSuccessful"], value)

    @property
    def FlogoSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flogo Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlogoSent"])

    @FlogoSent.setter
    def FlogoSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlogoSent"], value)

    @property
    def FlowControlFrames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Control Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowControlFrames"])

    @FlowControlFrames.setter
    def FlowControlFrames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowControlFrames"], value)

    @property
    def FlowControlFramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flow Control Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowControlFramesRate"])

    @FlowControlFramesRate.setter
    def FlowControlFramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowControlFramesRate"], value)

    @property
    def FomBoardTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Fom Board Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["FomBoardTemperatureC"])

    @FomBoardTemperatureC.setter
    def FomBoardTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FomBoardTemperatureC"], value)

    @property
    def FomInternalTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Fom Internal Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["FomInternalTemperatureC"])

    @FomInternalTemperatureC.setter
    def FomInternalTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FomInternalTemperatureC"], value)

    @property
    def FomPortTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Fom Port Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["FomPortTemperatureC"])

    @FomPortTemperatureC.setter
    def FomPortTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FomPortTemperatureC"], value)

    @property
    def Fragments(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Fragments
        """
        return self._get_attribute(self._SDM_ATT_MAP["Fragments"])

    @Fragments.setter
    def Fragments(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Fragments"], value)

    @property
    def FragmentsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Fragments Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FragmentsRate"])

    @FragmentsRate.setter
    def FragmentsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FragmentsRate"], value)

    @property
    def FramerAbort(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Framer Abort
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramerAbort"])

    @FramerAbort.setter
    def FramerAbort(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramerAbort"], value)

    @property
    def FramerAbortRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Framer Abort Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramerAbortRate"])

    @FramerAbortRate.setter
    def FramerAbortRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramerAbortRate"], value)

    @property
    def FramerMaxLength(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Framer Max Length
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramerMaxLength"])

    @FramerMaxLength.setter
    def FramerMaxLength(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramerMaxLength"], value)

    @property
    def FramerMaxLengthRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Framer Max Length Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramerMaxLengthRate"])

    @FramerMaxLengthRate.setter
    def FramerMaxLengthRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramerMaxLengthRate"], value)

    @property
    def FramerMinLength(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Framer Min Length
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramerMinLength"])

    @FramerMinLength.setter
    def FramerMinLength(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramerMinLength"], value)

    @property
    def FramerMinLengthRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Framer Min Length Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramerMinLengthRate"])

    @FramerMinLengthRate.setter
    def FramerMinLengthRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramerMinLengthRate"], value)

    @property
    def FramesReceivedwithCodingErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Frames Received with Coding Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesReceivedwithCodingErrors"])

    @FramesReceivedwithCodingErrors.setter
    def FramesReceivedwithCodingErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesReceivedwithCodingErrors"], value)

    @property
    def FramesReceivedwithCodingErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Frames Received with Coding Errors Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FramesReceivedwithCodingErrorsRate"]
        )

    @FramesReceivedwithCodingErrorsRate.setter
    def FramesReceivedwithCodingErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FramesReceivedwithCodingErrorsRate"], value
        )

    @property
    def FramesReceivedwithEerrorCharacter(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Frames Received with /E/ error Character
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FramesReceivedwithEerrorCharacter"]
        )

    @FramesReceivedwithEerrorCharacter.setter
    def FramesReceivedwithEerrorCharacter(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FramesReceivedwithEerrorCharacter"], value
        )

    @property
    def FramesReceivedwithEerrorCharacterRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Frames Received with /E/ error Character Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["FramesReceivedwithEerrorCharacterRate"]
        )

    @FramesReceivedwithEerrorCharacterRate.setter
    def FramesReceivedwithEerrorCharacterRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["FramesReceivedwithEerrorCharacterRate"], value
        )

    @property
    def FramesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Frames Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesTx"])

    @FramesTx.setter
    def FramesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesTx"], value)

    @property
    def FramesTxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Frames Tx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["FramesTxRate"])

    @FramesTxRate.setter
    def FramesTxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FramesTxRate"], value)

    @property
    def FreeMemory(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Free Memory
        """
        return self._get_attribute(self._SDM_ATT_MAP["FreeMemory"])

    @FreeMemory.setter
    def FreeMemory(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FreeMemory"], value)

    @property
    def FrontendChipTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: FrontEnd Chip Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrontendChipTemperatureC"])

    @FrontendChipTemperatureC.setter
    def FrontendChipTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrontendChipTemperatureC"], value)

    @property
    def HostConfigStatus(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Host Config Status
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostConfigStatus"])

    @HostConfigStatus.setter
    def HostConfigStatus(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HostConfigStatus"], value)

    @property
    def HostDataPathState(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Host Data Path State
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostDataPathState"])

    @HostDataPathState.setter
    def HostDataPathState(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HostDataPathState"], value)

    @property
    def HostLaneCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Host Lane Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostLaneCount"])

    @HostLaneCount.setter
    def HostLaneCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HostLaneCount"], value)

    @property
    def HostToMediaLane(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Host To Media Lane
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostToMediaLane"])

    @HostToMediaLane.setter
    def HostToMediaLane(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HostToMediaLane"], value)

    @property
    def HostTxCDRLOL(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Host Tx CDR LOL
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostTxCDRLOL"])

    @HostTxCDRLOL.setter
    def HostTxCDRLOL(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HostTxCDRLOL"], value)

    @property
    def HostTxLOS(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Host Tx LOS
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostTxLOS"])

    @HostTxLOS.setter
    def HostTxLOS(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HostTxLOS"], value)

    @property
    def IdleCellsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Idle Cells Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IdleCellsRx"])

    @IdleCellsRx.setter
    def IdleCellsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IdleCellsRx"], value)

    @property
    def IdleCellsRxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Idle Cells Rx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["IdleCellsRxRate"])

    @IdleCellsRxRate.setter
    def IdleCellsRxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IdleCellsRxRate"], value)

    @property
    def InputSignalStrengthdBm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Input Signal Strength (dBm)
        """
        return self._get_attribute(self._SDM_ATT_MAP["InputSignalStrengthdBm"])

    @InputSignalStrengthdBm.setter
    def InputSignalStrengthdBm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InputSignalStrengthdBm"], value)

    @property
    def InsertionState(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Insertion State
        """
        return self._get_attribute(self._SDM_ATT_MAP["InsertionState"])

    @InsertionState.setter
    def InsertionState(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InsertionState"], value)

    @property
    def InvalidEOF(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Invalid EOF
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidEOF"])

    @InvalidEOF.setter
    def InvalidEOF(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidEOF"], value)

    @property
    def InvalidEOFRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Invalid EOF Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidEOFRate"])

    @InvalidEOFRate.setter
    def InvalidEOFRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidEOFRate"], value)

    @property
    def InvalidICVAcceptedBroadcast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Invalid ICV Accepted Broadcast
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidICVAcceptedBroadcast"])

    @InvalidICVAcceptedBroadcast.setter
    def InvalidICVAcceptedBroadcast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidICVAcceptedBroadcast"], value)

    @property
    def InvalidICVAcceptedMulticast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Invalid ICV Accepted Multicast
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidICVAcceptedMulticast"])

    @InvalidICVAcceptedMulticast.setter
    def InvalidICVAcceptedMulticast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidICVAcceptedMulticast"], value)

    @property
    def InvalidICVDiscardedBroadcast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Invalid ICV Discarded Broadcast
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidICVDiscardedBroadcast"])

    @InvalidICVDiscardedBroadcast.setter
    def InvalidICVDiscardedBroadcast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidICVDiscardedBroadcast"], value)

    @property
    def InvalidICVDiscardedMulticast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Invalid ICV Discarded Multicast
        """
        return self._get_attribute(self._SDM_ATT_MAP["InvalidICVDiscardedMulticast"])

    @InvalidICVDiscardedMulticast.setter
    def InvalidICVDiscardedMulticast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["InvalidICVDiscardedMulticast"], value)

    @property
    def Ipv4ChecksumErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Checksum Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4ChecksumErrors"])

    @Ipv4ChecksumErrors.setter
    def Ipv4ChecksumErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4ChecksumErrors"], value)

    @property
    def Ipv4ChecksumErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Checksum Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4ChecksumErrorsRate"])

    @Ipv4ChecksumErrorsRate.setter
    def Ipv4ChecksumErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4ChecksumErrorsRate"], value)

    @property
    def Ipv4PacketsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Packets Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4PacketsReceived"])

    @Ipv4PacketsReceived.setter
    def Ipv4PacketsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4PacketsReceived"], value)

    @property
    def Ipv4PacketsReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: IPv4 Packets Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ipv4PacketsReceivedRate"])

    @Ipv4PacketsReceivedRate.setter
    def Ipv4PacketsReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ipv4PacketsReceivedRate"], value)

    @property
    def KernelTimestamp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Kernel Timestamp
        """
        return self._get_attribute(self._SDM_ATT_MAP["KernelTimestamp"])

    @KernelTimestamp.setter
    def KernelTimestamp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["KernelTimestamp"], value)

    @property
    def L1BitsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Bits Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1BitsReceived"])

    @L1BitsReceived.setter
    def L1BitsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1BitsReceived"], value)

    @property
    def L1BitsReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Bits Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1BitsReceivedRate"])

    @L1BitsReceivedRate.setter
    def L1BitsReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1BitsReceivedRate"], value)

    @property
    def L1BitsSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Bits Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1BitsSent"])

    @L1BitsSent.setter
    def L1BitsSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1BitsSent"], value)

    @property
    def L1BitsSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Bits Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1BitsSentRate"])

    @L1BitsSentRate.setter
    def L1BitsSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1BitsSentRate"], value)

    @property
    def L1LineRateReceivePercent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Line Rate Receive (%)
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1LineRateReceivePercent"])

    @L1LineRateReceivePercent.setter
    def L1LineRateReceivePercent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1LineRateReceivePercent"], value)

    @property
    def L1LineRateTransmitPercent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: L1 Line Rate Transmit (%)
        """
        return self._get_attribute(self._SDM_ATT_MAP["L1LineRateTransmitPercent"])

    @L1LineRateTransmitPercent.setter
    def L1LineRateTransmitPercent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["L1LineRateTransmitPercent"], value)

    @property
    def LastServiceDisruptionTimems(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Last Service Disruption Time (ms)
        """
        return self._get_attribute(self._SDM_ATT_MAP["LastServiceDisruptionTimems"])

    @LastServiceDisruptionTimems.setter
    def LastServiceDisruptionTimems(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LastServiceDisruptionTimems"], value)

    @property
    def LateCollisions(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Late Collisions
        """
        return self._get_attribute(self._SDM_ATT_MAP["LateCollisions"])

    @LateCollisions.setter
    def LateCollisions(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LateCollisions"], value)

    @property
    def LateCollisionsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Late Collisions Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["LateCollisionsRate"])

    @LateCollisionsRate.setter
    def LateCollisionsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LateCollisionsRate"], value)

    @property
    def LatencyChipTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Latency Chip Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyChipTemperatureC"])

    @LatencyChipTemperatureC.setter
    def LatencyChipTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyChipTemperatureC"], value)

    @property
    def LineAIS(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line AIS
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineAIS"])

    @LineAIS.setter
    def LineAIS(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineAIS"], value)

    @property
    def LineAISAlarmedSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line AIS Alarmed Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineAISAlarmedSeconds"])

    @LineAISAlarmedSeconds.setter
    def LineAISAlarmedSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineAISAlarmedSeconds"], value)

    @property
    def LineBIPB2(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line BIP (B2)
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineBIPB2"])

    @LineBIPB2.setter
    def LineBIPB2(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineBIPB2"], value)

    @property
    def LineBIPB2Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line BIP (B2) Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineBIPB2Rate"])

    @LineBIPB2Rate.setter
    def LineBIPB2Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineBIPB2Rate"], value)

    @property
    def LineBIPErroredSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line BIP Errored Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineBIPErroredSeconds"])

    @LineBIPErroredSeconds.setter
    def LineBIPErroredSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineBIPErroredSeconds"], value)

    @property
    def LineErrorFrames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line Error Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineErrorFrames"])

    @LineErrorFrames.setter
    def LineErrorFrames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineErrorFrames"], value)

    @property
    def LineErrorFramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line Error Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineErrorFramesRate"])

    @LineErrorFramesRate.setter
    def LineErrorFramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineErrorFramesRate"], value)

    @property
    def LineErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineErrors"])

    @LineErrors.setter
    def LineErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineErrors"], value)

    @property
    def LineErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineErrorsRate"])

    @LineErrorsRate.setter
    def LineErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineErrorsRate"], value)

    @property
    def LineRDI(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line RDI
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineRDI"])

    @LineRDI.setter
    def LineRDI(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineRDI"], value)

    @property
    def LineRDIUnavailableSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line RDI Unavailable Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineRDIUnavailableSeconds"])

    @LineRDIUnavailableSeconds.setter
    def LineRDIUnavailableSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineRDIUnavailableSeconds"], value)

    @property
    def LineREIErroredSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line REI Errored Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineREIErroredSeconds"])

    @LineREIErroredSeconds.setter
    def LineREIErroredSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineREIErroredSeconds"], value)

    @property
    def LineREIFEBE(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line REI (FEBE)
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineREIFEBE"])

    @LineREIFEBE.setter
    def LineREIFEBE(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineREIFEBE"], value)

    @property
    def LineREIFEBERate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line REI (FEBE) Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineREIFEBERate"])

    @LineREIFEBERate.setter
    def LineREIFEBERate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineREIFEBERate"], value)

    @property
    def LineSpeed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Line Speed
        """
        return self._get_attribute(self._SDM_ATT_MAP["LineSpeed"])

    @LineSpeed.setter
    def LineSpeed(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LineSpeed"], value)

    @property
    def LinkFaultState(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Link Fault State
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkFaultState"])

    @LinkFaultState.setter
    def LinkFaultState(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkFaultState"], value)

    @property
    def LinkState(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Link State
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkState"])

    @LinkState.setter
    def LinkState(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkState"], value)

    @property
    def LocalFaults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Local Faults
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalFaults"])

    @LocalFaults.setter
    def LocalFaults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LocalFaults"], value)

    @property
    def LocalOrderedSetsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Local Ordered Sets Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalOrderedSetsReceived"])

    @LocalOrderedSetsReceived.setter
    def LocalOrderedSetsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LocalOrderedSetsReceived"], value)

    @property
    def LocalOrderedSetsReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Local Ordered Sets Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalOrderedSetsReceivedRate"])

    @LocalOrderedSetsReceivedRate.setter
    def LocalOrderedSetsReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LocalOrderedSetsReceivedRate"], value)

    @property
    def LocalOrderedSetsSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Local Ordered Sets Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalOrderedSetsSent"])

    @LocalOrderedSetsSent.setter
    def LocalOrderedSetsSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LocalOrderedSetsSent"], value)

    @property
    def LocalOrderedSetsSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Local Ordered Sets Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalOrderedSetsSentRate"])

    @LocalOrderedSetsSentRate.setter
    def LocalOrderedSetsSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LocalOrderedSetsSentRate"], value)

    @property
    def MaxServiceDisruptionTimems(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Max Service Disruption Time (ms)
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxServiceDisruptionTimems"])

    @MaxServiceDisruptionTimems.setter
    def MaxServiceDisruptionTimems(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxServiceDisruptionTimems"], value)

    @property
    def MediaLaneCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Media Lane Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaLaneCount"])

    @MediaLaneCount.setter
    def MediaLaneCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MediaLaneCount"], value)

    @property
    def MediaRxCDRLOL(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Media Rx CDR LOL
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaRxCDRLOL"])

    @MediaRxCDRLOL.setter
    def MediaRxCDRLOL(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MediaRxCDRLOL"], value)

    @property
    def MediaRxLOS(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Media Rx LOS
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaRxLOS"])

    @MediaRxLOS.setter
    def MediaRxLOS(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MediaRxLOS"], value)

    @property
    def MediaRxOpticalPower(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Media Rx Optical Power
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaRxOpticalPower"])

    @MediaRxOpticalPower.setter
    def MediaRxOpticalPower(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MediaRxOpticalPower"], value)

    @property
    def MediaTxBiasCurrent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Media Tx Bias Current
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaTxBiasCurrent"])

    @MediaTxBiasCurrent.setter
    def MediaTxBiasCurrent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MediaTxBiasCurrent"], value)

    @property
    def MediaTxOpticalPower(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Media Tx Optical Power
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaTxOpticalPower"])

    @MediaTxOpticalPower.setter
    def MediaTxOpticalPower(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MediaTxOpticalPower"], value)

    @property
    def MinServiceDisruptionTimems(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Min Service Disruption Time (ms)
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinServiceDisruptionTimems"])

    @MinServiceDisruptionTimems.setter
    def MinServiceDisruptionTimems(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinServiceDisruptionTimems"], value)

    @property
    def MisdirectedPacketCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Misdirected Packet Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["MisdirectedPacketCount"])

    @MisdirectedPacketCount.setter
    def MisdirectedPacketCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MisdirectedPacketCount"], value)

    @property
    def MisdirectedPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Misdirected Packet Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["MisdirectedPacketCountRate"])

    @MisdirectedPacketCountRate.setter
    def MisdirectedPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MisdirectedPacketCountRate"], value)

    @property
    def NonMACsecPacketRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Non-MACsec Packet Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["NonMACsecPacketRx"])

    @NonMACsecPacketRx.setter
    def NonMACsecPacketRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NonMACsecPacketRx"], value)

    @property
    def NonMACsecPacketTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Non-MACsec Packet Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["NonMACsecPacketTx"])

    @NonMACsecPacketTx.setter
    def NonMACsecPacketTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NonMACsecPacketTx"], value)

    @property
    def NportidsAcquired(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NPortIds Acquired
        """
        return self._get_attribute(self._SDM_ATT_MAP["NportidsAcquired"])

    @NportidsAcquired.setter
    def NportidsAcquired(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NportidsAcquired"], value)

    @property
    def NportsEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NPorts Enabled
        """
        return self._get_attribute(self._SDM_ATT_MAP["NportsEnabled"])

    @NportsEnabled.setter
    def NportsEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NportsEnabled"], value)

    @property
    def NsRegSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NS Reg Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["NsRegSent"])

    @NsRegSent.setter
    def NsRegSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NsRegSent"], value)

    @property
    def NsRegSuccessful(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NS Reg Successful
        """
        return self._get_attribute(self._SDM_ATT_MAP["NsRegSuccessful"])

    @NsRegSuccessful.setter
    def NsRegSuccessful(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NsRegSuccessful"], value)

    @property
    def NumberofMismatched0s(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Number of Mismatched 0's
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberofMismatched0s"])

    @NumberofMismatched0s.setter
    def NumberofMismatched0s(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberofMismatched0s"], value)

    @property
    def NumberofMismatched0sRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Number of Mismatched 0's Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberofMismatched0sRate"])

    @NumberofMismatched0sRate.setter
    def NumberofMismatched0sRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberofMismatched0sRate"], value)

    @property
    def NumberofMismatched1s(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Number of Mismatched 1's
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberofMismatched1s"])

    @NumberofMismatched1s.setter
    def NumberofMismatched1s(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberofMismatched1s"], value)

    @property
    def NumberofMismatched1sRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Number of Mismatched 1's Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberofMismatched1sRate"])

    @NumberofMismatched1sRate.setter
    def NumberofMismatched1sRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberofMismatched1sRate"], value)

    @property
    def NumberofRRDYsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Number of R_RDYs Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberofRRDYsReceived"])

    @NumberofRRDYsReceived.setter
    def NumberofRRDYsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberofRRDYsReceived"], value)

    @property
    def NumberofRRDYsReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Number of R_RDYs Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberofRRDYsReceivedRate"])

    @NumberofRRDYsReceivedRate.setter
    def NumberofRRDYsReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberofRRDYsReceivedRate"], value)

    @property
    def NumberofRRDYsSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Number of R_RDYs Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberofRRDYsSent"])

    @NumberofRRDYsSent.setter
    def NumberofRRDYsSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberofRRDYsSent"], value)

    @property
    def NumberofRRDYsSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Number of R_RDYs Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberofRRDYsSentRate"])

    @NumberofRRDYsSentRate.setter
    def NumberofRRDYsSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberofRRDYsSentRate"], value)

    @property
    def OutofWindowRxBroadcast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Out of Window Rx Broadcast
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutofWindowRxBroadcast"])

    @OutofWindowRxBroadcast.setter
    def OutofWindowRxBroadcast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutofWindowRxBroadcast"], value)

    @property
    def OutofWindowRxMulticast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Out of Window Rx Multicast
        """
        return self._get_attribute(self._SDM_ATT_MAP["OutofWindowRxMulticast"])

    @OutofWindowRxMulticast.setter
    def OutofWindowRxMulticast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OutofWindowRxMulticast"], value)

    @property
    def OverlayChipTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Overlay Chip Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverlayChipTemperatureC"])

    @OverlayChipTemperatureC.setter
    def OverlayChipTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverlayChipTemperatureC"], value)

    @property
    def Oversize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Oversize
        """
        return self._get_attribute(self._SDM_ATT_MAP["Oversize"])

    @Oversize.setter
    def Oversize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Oversize"], value)

    @property
    def OversizeRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Oversize Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["OversizeRate"])

    @OversizeRate.setter
    def OversizeRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OversizeRate"], value)

    @property
    def OversizeandCRCErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Oversize and CRC Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["OversizeandCRCErrors"])

    @OversizeandCRCErrors.setter
    def OversizeandCRCErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OversizeandCRCErrors"], value)

    @property
    def OversizeandCRCErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Oversize and CRC Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["OversizeandCRCErrorsRate"])

    @OversizeandCRCErrorsRate.setter
    def OversizeandCRCErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OversizeandCRCErrorsRate"], value)

    @property
    def PathAIS(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path AIS
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathAIS"])

    @PathAIS.setter
    def PathAIS(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathAIS"], value)

    @property
    def PathAISAlarmedSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path AIS Alarmed Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathAISAlarmedSeconds"])

    @PathAISAlarmedSeconds.setter
    def PathAISAlarmedSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathAISAlarmedSeconds"], value)

    @property
    def PathAISUnavailableSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path AIS Unavailable Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathAISUnavailableSeconds"])

    @PathAISUnavailableSeconds.setter
    def PathAISUnavailableSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathAISUnavailableSeconds"], value)

    @property
    def PathBIPB3(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path BIP (B3)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathBIPB3"])

    @PathBIPB3.setter
    def PathBIPB3(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathBIPB3"], value)

    @property
    def PathBIPB3Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path BIP (B3) Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathBIPB3Rate"])

    @PathBIPB3Rate.setter
    def PathBIPB3Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathBIPB3Rate"], value)

    @property
    def PathBIPErroredSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path BIP Errored Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathBIPErroredSeconds"])

    @PathBIPErroredSeconds.setter
    def PathBIPErroredSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathBIPErroredSeconds"], value)

    @property
    def PathLOP(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path LOP
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathLOP"])

    @PathLOP.setter
    def PathLOP(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathLOP"], value)

    @property
    def PathPLMC2(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path PLM (C2)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathPLMC2"])

    @PathPLMC2.setter
    def PathPLMC2(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathPLMC2"], value)

    @property
    def PathRDI(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path RDI
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathRDI"])

    @PathRDI.setter
    def PathRDI(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathRDI"], value)

    @property
    def PathRDIUnavailableSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path RDI Unavailable Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathRDIUnavailableSeconds"])

    @PathRDIUnavailableSeconds.setter
    def PathRDIUnavailableSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathRDIUnavailableSeconds"], value)

    @property
    def PathREIErroredSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path REI Errored Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathREIErroredSeconds"])

    @PathREIErroredSeconds.setter
    def PathREIErroredSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathREIErroredSeconds"], value)

    @property
    def PathREIFEBE(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path REI (FEBE)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathREIFEBE"])

    @PathREIFEBE.setter
    def PathREIFEBE(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathREIFEBE"], value)

    @property
    def PathREIFEBERate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Path REI (FEBE) Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PathREIFEBERate"])

    @PathREIFEBERate.setter
    def PathREIFEBERate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PathREIFEBERate"], value)

    @property
    def PauseAcknowledge(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Pause Acknowledge
        """
        return self._get_attribute(self._SDM_ATT_MAP["PauseAcknowledge"])

    @PauseAcknowledge.setter
    def PauseAcknowledge(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PauseAcknowledge"], value)

    @property
    def PauseAcknowledgeRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Pause Acknowledge Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PauseAcknowledgeRate"])

    @PauseAcknowledgeRate.setter
    def PauseAcknowledgeRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PauseAcknowledgeRate"], value)

    @property
    def PauseEndFrames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Pause End Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["PauseEndFrames"])

    @PauseEndFrames.setter
    def PauseEndFrames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PauseEndFrames"], value)

    @property
    def PauseEndFramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Pause End Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PauseEndFramesRate"])

    @PauseEndFramesRate.setter
    def PauseEndFramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PauseEndFramesRate"], value)

    @property
    def PauseOverwrite(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Pause Overwrite
        """
        return self._get_attribute(self._SDM_ATT_MAP["PauseOverwrite"])

    @PauseOverwrite.setter
    def PauseOverwrite(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PauseOverwrite"], value)

    @property
    def PauseOverwriteRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Pause Overwrite Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PauseOverwriteRate"])

    @PauseOverwriteRate.setter
    def PauseOverwriteRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PauseOverwriteRate"], value)

    @property
    def PcsIllegalCodes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Illegal Codes
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsIllegalCodes"])

    @PcsIllegalCodes.setter
    def PcsIllegalCodes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsIllegalCodes"], value)

    @property
    def PcsIllegalCodesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Illegal Codes Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsIllegalCodesRate"])

    @PcsIllegalCodesRate.setter
    def PcsIllegalCodesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsIllegalCodesRate"], value)

    @property
    def PcsIllegalIdle(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Illegal Idle
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsIllegalIdle"])

    @PcsIllegalIdle.setter
    def PcsIllegalIdle(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsIllegalIdle"], value)

    @property
    def PcsIllegalIdleRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Illegal Idle Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsIllegalIdleRate"])

    @PcsIllegalIdleRate.setter
    def PcsIllegalIdleRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsIllegalIdleRate"], value)

    @property
    def PcsIllegalOrderedSet(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Illegal Ordered Set
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsIllegalOrderedSet"])

    @PcsIllegalOrderedSet.setter
    def PcsIllegalOrderedSet(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsIllegalOrderedSet"], value)

    @property
    def PcsIllegalOrderedSetRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Illegal Ordered Set Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsIllegalOrderedSetRate"])

    @PcsIllegalOrderedSetRate.setter
    def PcsIllegalOrderedSetRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsIllegalOrderedSetRate"], value)

    @property
    def PcsIllegalSOF(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Illegal SOF
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsIllegalSOF"])

    @PcsIllegalSOF.setter
    def PcsIllegalSOF(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsIllegalSOF"], value)

    @property
    def PcsIllegalSOFRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Illegal SOF Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsIllegalSOFRate"])

    @PcsIllegalSOFRate.setter
    def PcsIllegalSOFRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsIllegalSOFRate"], value)

    @property
    def PcsLocalFaults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Local Faults
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsLocalFaults"])

    @PcsLocalFaults.setter
    def PcsLocalFaults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsLocalFaults"], value)

    @property
    def PcsLocalFaultsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Local Faults Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsLocalFaultsRate"])

    @PcsLocalFaultsRate.setter
    def PcsLocalFaultsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsLocalFaultsRate"], value)

    @property
    def PcsOutofOrderData(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Out of Order Data
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsOutofOrderData"])

    @PcsOutofOrderData.setter
    def PcsOutofOrderData(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsOutofOrderData"], value)

    @property
    def PcsOutofOrderDataRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Out of Order Data Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsOutofOrderDataRate"])

    @PcsOutofOrderDataRate.setter
    def PcsOutofOrderDataRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsOutofOrderDataRate"], value)

    @property
    def PcsOutofOrderEOF(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Out of Order EOF
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsOutofOrderEOF"])

    @PcsOutofOrderEOF.setter
    def PcsOutofOrderEOF(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsOutofOrderEOF"], value)

    @property
    def PcsOutofOrderEOFRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Out of Order EOF Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsOutofOrderEOFRate"])

    @PcsOutofOrderEOFRate.setter
    def PcsOutofOrderEOFRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsOutofOrderEOFRate"], value)

    @property
    def PcsOutofOrderOrderedSet(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Out of Order Ordered Set
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsOutofOrderOrderedSet"])

    @PcsOutofOrderOrderedSet.setter
    def PcsOutofOrderOrderedSet(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsOutofOrderOrderedSet"], value)

    @property
    def PcsOutofOrderOrderedSetRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Out of Order Ordered Set Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsOutofOrderOrderedSetRate"])

    @PcsOutofOrderOrderedSetRate.setter
    def PcsOutofOrderOrderedSetRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsOutofOrderOrderedSetRate"], value)

    @property
    def PcsOutofOrderSOF(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Out of Order SOF
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsOutofOrderSOF"])

    @PcsOutofOrderSOF.setter
    def PcsOutofOrderSOF(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsOutofOrderSOF"], value)

    @property
    def PcsOutofOrderSOFRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Out of Order SOF Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsOutofOrderSOFRate"])

    @PcsOutofOrderSOFRate.setter
    def PcsOutofOrderSOFRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsOutofOrderSOFRate"], value)

    @property
    def PcsRemoteFaults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Remote Faults
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsRemoteFaults"])

    @PcsRemoteFaults.setter
    def PcsRemoteFaults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsRemoteFaults"], value)

    @property
    def PcsRemoteFaultsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Remote Faults Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsRemoteFaultsRate"])

    @PcsRemoteFaultsRate.setter
    def PcsRemoteFaultsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsRemoteFaultsRate"], value)

    @property
    def PcsSyncErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Sync Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsSyncErrors"])

    @PcsSyncErrors.setter
    def PcsSyncErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsSyncErrors"], value)

    @property
    def PcsSyncErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PCS Sync Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PcsSyncErrorsRate"])

    @PcsSyncErrorsRate.setter
    def PcsSyncErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PcsSyncErrorsRate"], value)

    @property
    def PercentCPULoad(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: %CPU Load
        """
        return self._get_attribute(self._SDM_ATT_MAP["PercentCPULoad"])

    @PercentCPULoad.setter
    def PercentCPULoad(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PercentCPULoad"], value)

    @property
    def PfcPriority0BufferMaxDepth(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 0 Buffer Max Depth
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority0BufferMaxDepth"])

    @PfcPriority0BufferMaxDepth.setter
    def PfcPriority0BufferMaxDepth(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority0BufferMaxDepth"], value)

    @property
    def PfcPriority0PacketDrop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 0 Packet Drop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority0PacketDrop"])

    @PfcPriority0PacketDrop.setter
    def PfcPriority0PacketDrop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority0PacketDrop"], value)

    @property
    def PfcPriority0PacketDropRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 0 Packet Drop Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority0PacketDropRate"])

    @PfcPriority0PacketDropRate.setter
    def PfcPriority0PacketDropRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority0PacketDropRate"], value)

    @property
    def PfcPriority0PauseRatioPercent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 0 Pause Ratio(%)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority0PauseRatioPercent"])

    @PfcPriority0PauseRatioPercent.setter
    def PfcPriority0PauseRatioPercent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority0PauseRatioPercent"], value)

    @property
    def PfcPriority0PauseStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 0 Pause Start
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority0PauseStart"])

    @PfcPriority0PauseStart.setter
    def PfcPriority0PauseStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority0PauseStart"], value)

    @property
    def PfcPriority0PauseStartResent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 0 Pause Start Resent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority0PauseStartResent"])

    @PfcPriority0PauseStartResent.setter
    def PfcPriority0PauseStartResent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority0PauseStartResent"], value)

    @property
    def PfcPriority0PauseStop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 0 Pause Stop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority0PauseStop"])

    @PfcPriority0PauseStop.setter
    def PfcPriority0PauseStop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority0PauseStop"], value)

    @property
    def PfcPriority1BufferMaxDepth(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 1 Buffer Max Depth
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority1BufferMaxDepth"])

    @PfcPriority1BufferMaxDepth.setter
    def PfcPriority1BufferMaxDepth(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority1BufferMaxDepth"], value)

    @property
    def PfcPriority1PacketDrop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 1 Packet Drop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority1PacketDrop"])

    @PfcPriority1PacketDrop.setter
    def PfcPriority1PacketDrop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority1PacketDrop"], value)

    @property
    def PfcPriority1PacketDropRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 1 Packet Drop Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority1PacketDropRate"])

    @PfcPriority1PacketDropRate.setter
    def PfcPriority1PacketDropRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority1PacketDropRate"], value)

    @property
    def PfcPriority1PauseRatioPercent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 1 Pause Ratio(%)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority1PauseRatioPercent"])

    @PfcPriority1PauseRatioPercent.setter
    def PfcPriority1PauseRatioPercent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority1PauseRatioPercent"], value)

    @property
    def PfcPriority1PauseStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 1 Pause Start
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority1PauseStart"])

    @PfcPriority1PauseStart.setter
    def PfcPriority1PauseStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority1PauseStart"], value)

    @property
    def PfcPriority1PauseStartResent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 1 Pause Start Resent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority1PauseStartResent"])

    @PfcPriority1PauseStartResent.setter
    def PfcPriority1PauseStartResent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority1PauseStartResent"], value)

    @property
    def PfcPriority1PauseStop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 1 Pause Stop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority1PauseStop"])

    @PfcPriority1PauseStop.setter
    def PfcPriority1PauseStop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority1PauseStop"], value)

    @property
    def PfcPriority2BufferMaxDepth(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 2 Buffer Max Depth
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority2BufferMaxDepth"])

    @PfcPriority2BufferMaxDepth.setter
    def PfcPriority2BufferMaxDepth(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority2BufferMaxDepth"], value)

    @property
    def PfcPriority2PacketDrop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 2 Packet Drop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority2PacketDrop"])

    @PfcPriority2PacketDrop.setter
    def PfcPriority2PacketDrop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority2PacketDrop"], value)

    @property
    def PfcPriority2PacketDropRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 2 Packet Drop Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority2PacketDropRate"])

    @PfcPriority2PacketDropRate.setter
    def PfcPriority2PacketDropRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority2PacketDropRate"], value)

    @property
    def PfcPriority2PauseRatioPercent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 2 Pause Ratio(%)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority2PauseRatioPercent"])

    @PfcPriority2PauseRatioPercent.setter
    def PfcPriority2PauseRatioPercent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority2PauseRatioPercent"], value)

    @property
    def PfcPriority2PauseStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 2 Pause Start
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority2PauseStart"])

    @PfcPriority2PauseStart.setter
    def PfcPriority2PauseStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority2PauseStart"], value)

    @property
    def PfcPriority2PauseStartResent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 2 Pause Start Resent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority2PauseStartResent"])

    @PfcPriority2PauseStartResent.setter
    def PfcPriority2PauseStartResent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority2PauseStartResent"], value)

    @property
    def PfcPriority2PauseStop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 2 Pause Stop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority2PauseStop"])

    @PfcPriority2PauseStop.setter
    def PfcPriority2PauseStop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority2PauseStop"], value)

    @property
    def PfcPriority3BufferMaxDepth(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 3 Buffer Max Depth
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority3BufferMaxDepth"])

    @PfcPriority3BufferMaxDepth.setter
    def PfcPriority3BufferMaxDepth(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority3BufferMaxDepth"], value)

    @property
    def PfcPriority3PacketDrop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 3 Packet Drop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority3PacketDrop"])

    @PfcPriority3PacketDrop.setter
    def PfcPriority3PacketDrop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority3PacketDrop"], value)

    @property
    def PfcPriority3PacketDropRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 3 Packet Drop Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority3PacketDropRate"])

    @PfcPriority3PacketDropRate.setter
    def PfcPriority3PacketDropRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority3PacketDropRate"], value)

    @property
    def PfcPriority3PauseRatioPercent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 3 Pause Ratio(%)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority3PauseRatioPercent"])

    @PfcPriority3PauseRatioPercent.setter
    def PfcPriority3PauseRatioPercent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority3PauseRatioPercent"], value)

    @property
    def PfcPriority3PauseStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 3 Pause Start
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority3PauseStart"])

    @PfcPriority3PauseStart.setter
    def PfcPriority3PauseStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority3PauseStart"], value)

    @property
    def PfcPriority3PauseStartResent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 3 Pause Start Resent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority3PauseStartResent"])

    @PfcPriority3PauseStartResent.setter
    def PfcPriority3PauseStartResent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority3PauseStartResent"], value)

    @property
    def PfcPriority3PauseStop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 3 Pause Stop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority3PauseStop"])

    @PfcPriority3PauseStop.setter
    def PfcPriority3PauseStop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority3PauseStop"], value)

    @property
    def PfcPriority4BufferMaxDepth(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 4 Buffer Max Depth
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority4BufferMaxDepth"])

    @PfcPriority4BufferMaxDepth.setter
    def PfcPriority4BufferMaxDepth(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority4BufferMaxDepth"], value)

    @property
    def PfcPriority4PacketDrop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 4 Packet Drop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority4PacketDrop"])

    @PfcPriority4PacketDrop.setter
    def PfcPriority4PacketDrop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority4PacketDrop"], value)

    @property
    def PfcPriority4PacketDropRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 4 Packet Drop Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority4PacketDropRate"])

    @PfcPriority4PacketDropRate.setter
    def PfcPriority4PacketDropRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority4PacketDropRate"], value)

    @property
    def PfcPriority4PauseRatioPercent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 4 Pause Ratio(%)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority4PauseRatioPercent"])

    @PfcPriority4PauseRatioPercent.setter
    def PfcPriority4PauseRatioPercent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority4PauseRatioPercent"], value)

    @property
    def PfcPriority4PauseStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 4 Pause Start
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority4PauseStart"])

    @PfcPriority4PauseStart.setter
    def PfcPriority4PauseStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority4PauseStart"], value)

    @property
    def PfcPriority4PauseStartResent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 4 Pause Start Resent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority4PauseStartResent"])

    @PfcPriority4PauseStartResent.setter
    def PfcPriority4PauseStartResent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority4PauseStartResent"], value)

    @property
    def PfcPriority4PauseStop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 4 Pause Stop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority4PauseStop"])

    @PfcPriority4PauseStop.setter
    def PfcPriority4PauseStop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority4PauseStop"], value)

    @property
    def PfcPriority5BufferMaxDepth(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 5 Buffer Max Depth
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority5BufferMaxDepth"])

    @PfcPriority5BufferMaxDepth.setter
    def PfcPriority5BufferMaxDepth(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority5BufferMaxDepth"], value)

    @property
    def PfcPriority5PacketDrop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 5 Packet Drop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority5PacketDrop"])

    @PfcPriority5PacketDrop.setter
    def PfcPriority5PacketDrop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority5PacketDrop"], value)

    @property
    def PfcPriority5PacketDropRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 5 Packet Drop Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority5PacketDropRate"])

    @PfcPriority5PacketDropRate.setter
    def PfcPriority5PacketDropRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority5PacketDropRate"], value)

    @property
    def PfcPriority5PauseRatioPercent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 5 Pause Ratio(%)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority5PauseRatioPercent"])

    @PfcPriority5PauseRatioPercent.setter
    def PfcPriority5PauseRatioPercent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority5PauseRatioPercent"], value)

    @property
    def PfcPriority5PauseStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 5 Pause Start
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority5PauseStart"])

    @PfcPriority5PauseStart.setter
    def PfcPriority5PauseStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority5PauseStart"], value)

    @property
    def PfcPriority5PauseStartResent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 5 Pause Start Resent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority5PauseStartResent"])

    @PfcPriority5PauseStartResent.setter
    def PfcPriority5PauseStartResent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority5PauseStartResent"], value)

    @property
    def PfcPriority5PauseStop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 5 Pause Stop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority5PauseStop"])

    @PfcPriority5PauseStop.setter
    def PfcPriority5PauseStop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority5PauseStop"], value)

    @property
    def PfcPriority6BufferMaxDepth(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 6 Buffer Max Depth
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority6BufferMaxDepth"])

    @PfcPriority6BufferMaxDepth.setter
    def PfcPriority6BufferMaxDepth(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority6BufferMaxDepth"], value)

    @property
    def PfcPriority6PacketDrop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 6 Packet Drop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority6PacketDrop"])

    @PfcPriority6PacketDrop.setter
    def PfcPriority6PacketDrop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority6PacketDrop"], value)

    @property
    def PfcPriority6PacketDropRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 6 Packet Drop Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority6PacketDropRate"])

    @PfcPriority6PacketDropRate.setter
    def PfcPriority6PacketDropRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority6PacketDropRate"], value)

    @property
    def PfcPriority6PauseRatioPercent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 6 Pause Ratio(%)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority6PauseRatioPercent"])

    @PfcPriority6PauseRatioPercent.setter
    def PfcPriority6PauseRatioPercent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority6PauseRatioPercent"], value)

    @property
    def PfcPriority6PauseStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 6 Pause Start
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority6PauseStart"])

    @PfcPriority6PauseStart.setter
    def PfcPriority6PauseStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority6PauseStart"], value)

    @property
    def PfcPriority6PauseStartResent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 6 Pause Start Resent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority6PauseStartResent"])

    @PfcPriority6PauseStartResent.setter
    def PfcPriority6PauseStartResent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority6PauseStartResent"], value)

    @property
    def PfcPriority6PauseStop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 6 Pause Stop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority6PauseStop"])

    @PfcPriority6PauseStop.setter
    def PfcPriority6PauseStop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority6PauseStop"], value)

    @property
    def PfcPriority7BufferMaxDepth(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 7 Buffer Max Depth
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority7BufferMaxDepth"])

    @PfcPriority7BufferMaxDepth.setter
    def PfcPriority7BufferMaxDepth(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority7BufferMaxDepth"], value)

    @property
    def PfcPriority7PacketDrop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 7 Packet Drop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority7PacketDrop"])

    @PfcPriority7PacketDrop.setter
    def PfcPriority7PacketDrop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority7PacketDrop"], value)

    @property
    def PfcPriority7PacketDropRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 7 Packet Drop Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority7PacketDropRate"])

    @PfcPriority7PacketDropRate.setter
    def PfcPriority7PacketDropRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority7PacketDropRate"], value)

    @property
    def PfcPriority7PauseRatioPercent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 7 Pause Ratio(%)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority7PauseRatioPercent"])

    @PfcPriority7PauseRatioPercent.setter
    def PfcPriority7PauseRatioPercent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority7PauseRatioPercent"], value)

    @property
    def PfcPriority7PauseStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 7 Pause Start
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority7PauseStart"])

    @PfcPriority7PauseStart.setter
    def PfcPriority7PauseStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority7PauseStart"], value)

    @property
    def PfcPriority7PauseStartResent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 7 Pause Start Resent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority7PauseStartResent"])

    @PfcPriority7PauseStartResent.setter
    def PfcPriority7PauseStartResent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority7PauseStartResent"], value)

    @property
    def PfcPriority7PauseStop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PFC Priority 7 Pause Stop
        """
        return self._get_attribute(self._SDM_ATT_MAP["PfcPriority7PauseStop"])

    @PfcPriority7PauseStop.setter
    def PfcPriority7PauseStop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PfcPriority7PauseStop"], value)

    @property
    def PgidOverflow(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PGID Overflow
        """
        return self._get_attribute(self._SDM_ATT_MAP["PgidOverflow"])

    @PgidOverflow.setter
    def PgidOverflow(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PgidOverflow"], value)

    @property
    def PgidOverflowRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PGID Overflow Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PgidOverflowRate"])

    @PgidOverflowRate.setter
    def PgidOverflowRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PgidOverflowRate"], value)

    @property
    def PhyChipTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PHY Chip Temperature (C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PhyChipTemperatureC"])

    @PhyChipTemperatureC.setter
    def PhyChipTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PhyChipTemperatureC"], value)

    @property
    def PlcaBeaconCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PLCA Beacon Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlcaBeaconCount"])

    @PlcaBeaconCount.setter
    def PlcaBeaconCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlcaBeaconCount"], value)

    @property
    def PlcaBeaconCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PLCA Beacon Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlcaBeaconCountRate"])

    @PlcaBeaconCountRate.setter
    def PlcaBeaconCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlcaBeaconCountRate"], value)

    @property
    def PlcaBeaconReceivedBeforeTransmitOpportunity(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PLCA Beacon Received Before Transmit Opportunity
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["PlcaBeaconReceivedBeforeTransmitOpportunity"]
        )

    @PlcaBeaconReceivedBeforeTransmitOpportunity.setter
    def PlcaBeaconReceivedBeforeTransmitOpportunity(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["PlcaBeaconReceivedBeforeTransmitOpportunity"], value
        )

    @property
    def PlcaCorruptedTransmitCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PLCA Corrupted Transmit Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlcaCorruptedTransmitCount"])

    @PlcaCorruptedTransmitCount.setter
    def PlcaCorruptedTransmitCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlcaCorruptedTransmitCount"], value)

    @property
    def PlcaCorruptedTransmitCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PLCA Corrupted Transmit Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlcaCorruptedTransmitCountRate"])

    @PlcaCorruptedTransmitCountRate.setter
    def PlcaCorruptedTransmitCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlcaCorruptedTransmitCountRate"], value)

    @property
    def PlcaEmptyCycleStatus(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PLCA Empty Cycle Status
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlcaEmptyCycleStatus"])

    @PlcaEmptyCycleStatus.setter
    def PlcaEmptyCycleStatus(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlcaEmptyCycleStatus"], value)

    @property
    def PlcaTransmitOpportunityCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PLCA Transmit Opportunity Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlcaTransmitOpportunityCount"])

    @PlcaTransmitOpportunityCount.setter
    def PlcaTransmitOpportunityCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlcaTransmitOpportunityCount"], value)

    @property
    def PlcaTransmitOpportunityCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PLCA Transmit Opportunity Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["PlcaTransmitOpportunityCountRate"]
        )

    @PlcaTransmitOpportunityCountRate.setter
    def PlcaTransmitOpportunityCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["PlcaTransmitOpportunityCountRate"], value
        )

    @property
    def Plcasymboldetected(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: PLCA symbol detected
        """
        return self._get_attribute(self._SDM_ATT_MAP["Plcasymboldetected"])

    @Plcasymboldetected.setter
    def Plcasymboldetected(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Plcasymboldetected"], value)

    @property
    def PlmInternalTemperature1C(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Plm Internal Temperature 1(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlmInternalTemperature1C"])

    @PlmInternalTemperature1C.setter
    def PlmInternalTemperature1C(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlmInternalTemperature1C"], value)

    @property
    def PlmInternalTemperature2C(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Plm Internal Temperature 2(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlmInternalTemperature2C"])

    @PlmInternalTemperature2C.setter
    def PlmInternalTemperature2C(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlmInternalTemperature2C"], value)

    @property
    def PlmInternalTemperature3C(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Plm Internal Temperature 3(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlmInternalTemperature3C"])

    @PlmInternalTemperature3C.setter
    def PlmInternalTemperature3C(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlmInternalTemperature3C"], value)

    @property
    def PlogiReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Plogi Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlogiReceived"])

    @PlogiReceived.setter
    def PlogiReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlogiReceived"], value)

    @property
    def PlogiSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Plogi Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlogiSent"])

    @PlogiSent.setter
    def PlogiSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlogiSent"], value)

    @property
    def PlogiSuccessful(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Plogi Successful
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlogiSuccessful"])

    @PlogiSuccessful.setter
    def PlogiSuccessful(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlogiSuccessful"], value)

    @property
    def PlogoReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Plogo Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlogoReceived"])

    @PlogoReceived.setter
    def PlogoReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlogoReceived"], value)

    @property
    def PlogoSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Plogo Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PlogoSent"])

    @PlogoSent.setter
    def PlogoSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PlogoSent"], value)

    @property
    def PortCPUDoDStatus(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port CPU DoD Status
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortCPUDoDStatus"])

    @PortCPUDoDStatus.setter
    def PortCPUDoDStatus(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortCPUDoDStatus"], value)

    @property
    def PortCPUFramesReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port CPU Frames Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortCPUFramesReceived"])

    @PortCPUFramesReceived.setter
    def PortCPUFramesReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortCPUFramesReceived"], value)

    @property
    def PortCPUFramesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port CPU Frames Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortCPUFramesSent"])

    @PortCPUFramesSent.setter
    def PortCPUFramesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortCPUFramesSent"], value)

    @property
    def PortCPUFramesSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port CPU Frames Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortCPUFramesSentRate"])

    @PortCPUFramesSentRate.setter
    def PortCPUFramesSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortCPUFramesSentRate"], value)

    @property
    def PortCPUStatus(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port CPU Status
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortCPUStatus"])

    @PortCPUStatus.setter
    def PortCPUStatus(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortCPUStatus"], value)

    @property
    def PortChipTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Chip Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortChipTemperatureC"])

    @PortChipTemperatureC.setter
    def PortChipTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortChipTemperatureC"], value)

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
    def PrbsBerRatio(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prbs Ber Ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrbsBerRatio"])

    @PrbsBerRatio.setter
    def PrbsBerRatio(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrbsBerRatio"], value)

    @property
    def PrbsBitsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prbs Bits Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrbsBitsReceived"])

    @PrbsBitsReceived.setter
    def PrbsBitsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrbsBitsReceived"], value)

    @property
    def PrbsBitsReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prbs Bits Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrbsBitsReceivedRate"])

    @PrbsBitsReceivedRate.setter
    def PrbsBitsReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrbsBitsReceivedRate"], value)

    @property
    def PrbsErroredBits(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prbs Errored Bits
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrbsErroredBits"])

    @PrbsErroredBits.setter
    def PrbsErroredBits(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrbsErroredBits"], value)

    @property
    def PrbsErroredBitsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prbs Errored Bits Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrbsErroredBitsRate"])

    @PrbsErroredBitsRate.setter
    def PrbsErroredBitsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrbsErroredBitsRate"], value)

    @property
    def PrbsFramesReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prbs Frames Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrbsFramesReceived"])

    @PrbsFramesReceived.setter
    def PrbsFramesReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrbsFramesReceived"], value)

    @property
    def PrbsFramesReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prbs Frames Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrbsFramesReceivedRate"])

    @PrbsFramesReceivedRate.setter
    def PrbsFramesReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrbsFramesReceivedRate"], value)

    @property
    def PrbsFramesWithHeaderError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prbs Frames With Header Error
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrbsFramesWithHeaderError"])

    @PrbsFramesWithHeaderError.setter
    def PrbsFramesWithHeaderError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrbsFramesWithHeaderError"], value)

    @property
    def PrbsFramesWithHeaderErrorRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Prbs Frames With Header Error Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrbsFramesWithHeaderErrorRate"])

    @PrbsFramesWithHeaderErrorRate.setter
    def PrbsFramesWithHeaderErrorRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrbsFramesWithHeaderErrorRate"], value)

    @property
    def PreFECBitErrorRatio(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: pre FEC Bit Error Ratio
        """
        return self._get_attribute(self._SDM_ATT_MAP["PreFECBitErrorRatio"])

    @PreFECBitErrorRatio.setter
    def PreFECBitErrorRatio(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PreFECBitErrorRatio"], value)

    @property
    def ProtectedByteRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Protected Byte Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtectedByteRx"])

    @ProtectedByteRx.setter
    def ProtectedByteRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtectedByteRx"], value)

    @property
    def ProtectedByteTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Protected Byte Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtectedByteTx"])

    @ProtectedByteTx.setter
    def ProtectedByteTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtectedByteTx"], value)

    @property
    def ProtectedPacketRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Protected Packet Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtectedPacketRx"])

    @ProtectedPacketRx.setter
    def ProtectedPacketRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtectedPacketRx"], value)

    @property
    def ProtectedPacketTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Protected Packet Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtectedPacketTx"])

    @ProtectedPacketTx.setter
    def ProtectedPacketTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtectedPacketTx"], value)

    @property
    def ProtocolServerVlanDroppedFrames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Protocol Server Vlan Dropped Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolServerVlanDroppedFrames"])

    @ProtocolServerVlanDroppedFrames.setter
    def ProtocolServerVlanDroppedFrames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtocolServerVlanDroppedFrames"], value)

    @property
    def PtpAnnounceMessagesReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ptp Announce Messages Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["PtpAnnounceMessagesReceived"])

    @PtpAnnounceMessagesReceived.setter
    def PtpAnnounceMessagesReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PtpAnnounceMessagesReceived"], value)

    @property
    def PtpAnnounceMessagesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ptp Announce Messages Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PtpAnnounceMessagesSent"])

    @PtpAnnounceMessagesSent.setter
    def PtpAnnounceMessagesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PtpAnnounceMessagesSent"], value)

    @property
    def PtpDelayReqMessagesReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ptp Delay_Req Messages Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["PtpDelayReqMessagesReceived"])

    @PtpDelayReqMessagesReceived.setter
    def PtpDelayReqMessagesReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PtpDelayReqMessagesReceived"], value)

    @property
    def PtpDelayReqMessagesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ptp Delay_Req Messages Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PtpDelayReqMessagesSent"])

    @PtpDelayReqMessagesSent.setter
    def PtpDelayReqMessagesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PtpDelayReqMessagesSent"], value)

    @property
    def PtpDelayRespMessagesReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ptp Delay_Resp Messages Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["PtpDelayRespMessagesReceived"])

    @PtpDelayRespMessagesReceived.setter
    def PtpDelayRespMessagesReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PtpDelayRespMessagesReceived"], value)

    @property
    def PtpDelayRespMessagesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ptp Delay_Resp Messages Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PtpDelayRespMessagesSent"])

    @PtpDelayRespMessagesSent.setter
    def PtpDelayRespMessagesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PtpDelayRespMessagesSent"], value)

    @property
    def PtpFollowUpMessagesReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ptp Follow_Up Messages Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["PtpFollowUpMessagesReceived"])

    @PtpFollowUpMessagesReceived.setter
    def PtpFollowUpMessagesReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PtpFollowUpMessagesReceived"], value)

    @property
    def PtpFollowUpMessagesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ptp Follow_Up Messages Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PtpFollowUpMessagesSent"])

    @PtpFollowUpMessagesSent.setter
    def PtpFollowUpMessagesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PtpFollowUpMessagesSent"], value)

    @property
    def PtpSyncMessagesReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ptp Sync Messages Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["PtpSyncMessagesReceived"])

    @PtpSyncMessagesReceived.setter
    def PtpSyncMessagesReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PtpSyncMessagesReceived"], value)

    @property
    def PtpSyncMessagesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Ptp Sync Messages Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["PtpSyncMessagesSent"])

    @PtpSyncMessagesSent.setter
    def PtpSyncMessagesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PtpSyncMessagesSent"], value)

    @property
    def RamDiskUtilization(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RAM Disk Utilization
        """
        return self._get_attribute(self._SDM_ATT_MAP["RamDiskUtilization"])

    @RamDiskUtilization.setter
    def RamDiskUtilization(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RamDiskUtilization"], value)

    @property
    def ReceiveArpReply(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Receive Arp Reply
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceiveArpReply"])

    @ReceiveArpReply.setter
    def ReceiveArpReply(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReceiveArpReply"], value)

    @property
    def ReceiveArpRequest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Receive Arp Request
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceiveArpRequest"])

    @ReceiveArpRequest.setter
    def ReceiveArpRequest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReceiveArpRequest"], value)

    @property
    def ReceiveInTransmitOpportunity(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Receive In Transmit Opportunity
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceiveInTransmitOpportunity"])

    @ReceiveInTransmitOpportunity.setter
    def ReceiveInTransmitOpportunity(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReceiveInTransmitOpportunity"], value)

    @property
    def ReceiveNeighborAdvertisements(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Receive Neighbor Advertisements
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceiveNeighborAdvertisements"])

    @ReceiveNeighborAdvertisements.setter
    def ReceiveNeighborAdvertisements(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReceiveNeighborAdvertisements"], value)

    @property
    def ReceiveNeighborSolicitation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Receive Neighbor Solicitation
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceiveNeighborSolicitation"])

    @ReceiveNeighborSolicitation.setter
    def ReceiveNeighborSolicitation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReceiveNeighborSolicitation"], value)

    @property
    def ReceivePingReply(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Receive Ping Reply
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceivePingReply"])

    @ReceivePingReply.setter
    def ReceivePingReply(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReceivePingReply"], value)

    @property
    def ReceivePingRequest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Receive Ping Request
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceivePingRequest"])

    @ReceivePingRequest.setter
    def ReceivePingRequest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReceivePingRequest"], value)

    @property
    def RemoteBuffertoBufferCreditCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Remote Buffer-to-Buffer Credit Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteBuffertoBufferCreditCount"])

    @RemoteBuffertoBufferCreditCount.setter
    def RemoteBuffertoBufferCreditCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RemoteBuffertoBufferCreditCount"], value)

    @property
    def RemoteBuffertoBufferCreditValue(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Remote Buffer-to-Buffer Credit Value
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteBuffertoBufferCreditValue"])

    @RemoteBuffertoBufferCreditValue.setter
    def RemoteBuffertoBufferCreditValue(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RemoteBuffertoBufferCreditValue"], value)

    @property
    def RemoteFaults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Remote Faults
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteFaults"])

    @RemoteFaults.setter
    def RemoteFaults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RemoteFaults"], value)

    @property
    def RemoteOrderedSetsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Remote Ordered Sets Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteOrderedSetsReceived"])

    @RemoteOrderedSetsReceived.setter
    def RemoteOrderedSetsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RemoteOrderedSetsReceived"], value)

    @property
    def RemoteOrderedSetsReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Remote Ordered Sets Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteOrderedSetsReceivedRate"])

    @RemoteOrderedSetsReceivedRate.setter
    def RemoteOrderedSetsReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RemoteOrderedSetsReceivedRate"], value)

    @property
    def RemoteOrderedSetsSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Remote Ordered Sets Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteOrderedSetsSent"])

    @RemoteOrderedSetsSent.setter
    def RemoteOrderedSetsSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RemoteOrderedSetsSent"], value)

    @property
    def RemoteOrderedSetsSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Remote Ordered Sets Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RemoteOrderedSetsSentRate"])

    @RemoteOrderedSetsSentRate.setter
    def RemoteOrderedSetsSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RemoteOrderedSetsSentRate"], value)

    @property
    def Rocev2BadiCRCCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RoCEv2 Bad iCRC Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["Rocev2BadiCRCCount"])

    @Rocev2BadiCRCCount.setter
    def Rocev2BadiCRCCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Rocev2BadiCRCCount"], value)

    @property
    def Rocev2OpCodeErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RoCEv2 OpCode Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["Rocev2OpCodeErrorCount"])

    @Rocev2OpCodeErrorCount.setter
    def Rocev2OpCodeErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Rocev2OpCodeErrorCount"], value)

    @property
    def RsFECCorrectedCodewordCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RS-FEC Corrected Codeword Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsFECCorrectedCodewordCount"])

    @RsFECCorrectedCodewordCount.setter
    def RsFECCorrectedCodewordCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsFECCorrectedCodewordCount"], value)

    @property
    def RsFECCorrectedCodewordCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RS-FEC Corrected Codeword Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsFECCorrectedCodewordCountRate"])

    @RsFECCorrectedCodewordCountRate.setter
    def RsFECCorrectedCodewordCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsFECCorrectedCodewordCountRate"], value)

    @property
    def RsFECUncorrectedCodewordCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RS-FEC Uncorrected Codeword Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsFECUncorrectedCodewordCount"])

    @RsFECUncorrectedCodewordCount.setter
    def RsFECUncorrectedCodewordCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsFECUncorrectedCodewordCount"], value)

    @property
    def RsFECUncorrectedCodewordCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RS-FEC Uncorrected Codeword Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RsFECUncorrectedCodewordCountRate"]
        )

    @RsFECUncorrectedCodewordCountRate.setter
    def RsFECUncorrectedCodewordCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RsFECUncorrectedCodewordCountRate"], value
        )

    @property
    def Rx0FpgaTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx0 Fpga Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Rx0FpgaTemperatureC"])

    @Rx0FpgaTemperatureC.setter
    def Rx0FpgaTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Rx0FpgaTemperatureC"], value)

    @property
    def Rx1FpgaTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx1 Fpga Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Rx1FpgaTemperatureC"])

    @Rx1FpgaTemperatureC.setter
    def Rx1FpgaTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Rx1FpgaTemperatureC"], value)

    @property
    def RxBadPacketforBroadcastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Bad Packet for Broadcast Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxBadPacketforBroadcastRate"])

    @RxBadPacketforBroadcastRate.setter
    def RxBadPacketforBroadcastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxBadPacketforBroadcastRate"], value)

    @property
    def RxBadPacketforMulticastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Bad Packet for Multicast Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxBadPacketforMulticastRate"])

    @RxBadPacketforMulticastRate.setter
    def RxBadPacketforMulticastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxBadPacketforMulticastRate"], value)

    @property
    def RxBadTagPacketorICVDiscardedPacketforBroadcastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Bad Tag Packet or ICV Discarded Packet for Broadcast Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxBadTagPacketorICVDiscardedPacketforBroadcastRate"]
        )

    @RxBadTagPacketorICVDiscardedPacketforBroadcastRate.setter
    def RxBadTagPacketorICVDiscardedPacketforBroadcastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxBadTagPacketorICVDiscardedPacketforBroadcastRate"],
            value,
        )

    @property
    def RxBadTagPacketorICVDiscardedPacketforMulticastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Bad Tag Packet or ICV Discarded Packet for Multicast Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxBadTagPacketorICVDiscardedPacketforMulticastRate"]
        )

    @RxBadTagPacketorICVDiscardedPacketforMulticastRate.setter
    def RxBadTagPacketorICVDiscardedPacketforMulticastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxBadTagPacketorICVDiscardedPacketforMulticastRate"],
            value,
        )

    @property
    def RxBytesDecryptedBroadcast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Bytes Decrypted Broadcast
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxBytesDecryptedBroadcast"])

    @RxBytesDecryptedBroadcast.setter
    def RxBytesDecryptedBroadcast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxBytesDecryptedBroadcast"], value)

    @property
    def RxBytesDecryptedMulticast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Bytes Decrypted Multicast
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxBytesDecryptedMulticast"])

    @RxBytesDecryptedMulticast.setter
    def RxBytesDecryptedMulticast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxBytesDecryptedMulticast"], value)

    @property
    def RxBytesDecryptedforBroadcastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Bytes Decrypted for Broadcast Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxBytesDecryptedforBroadcastRate"]
        )

    @RxBytesDecryptedforBroadcastRate.setter
    def RxBytesDecryptedforBroadcastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxBytesDecryptedforBroadcastRate"], value
        )

    @property
    def RxBytesDecryptedforMulticastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Bytes Decrypted for Multicast Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxBytesDecryptedforMulticastRate"]
        )

    @RxBytesDecryptedforMulticastRate.setter
    def RxBytesDecryptedforMulticastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxBytesDecryptedforMulticastRate"], value
        )

    @property
    def RxBytesValidatedBroadcast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Bytes Validated Broadcast
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxBytesValidatedBroadcast"])

    @RxBytesValidatedBroadcast.setter
    def RxBytesValidatedBroadcast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxBytesValidatedBroadcast"], value)

    @property
    def RxBytesValidatedMulticast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Bytes Validated Multicast
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxBytesValidatedMulticast"])

    @RxBytesValidatedMulticast.setter
    def RxBytesValidatedMulticast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxBytesValidatedMulticast"], value)

    @property
    def RxBytesValidatedforBroadcastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Bytes Validated for Broadcast Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxBytesValidatedforBroadcastRate"]
        )

    @RxBytesValidatedforBroadcastRate.setter
    def RxBytesValidatedforBroadcastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxBytesValidatedforBroadcastRate"], value
        )

    @property
    def RxBytesValidatedforMulticastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Bytes Validated for Multicast Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxBytesValidatedforMulticastRate"]
        )

    @RxBytesValidatedforMulticastRate.setter
    def RxBytesValidatedforMulticastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxBytesValidatedforMulticastRate"], value
        )

    @property
    def RxEncryptedByteCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Encrypted Byte Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxEncryptedByteCountRate"])

    @RxEncryptedByteCountRate.setter
    def RxEncryptedByteCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxEncryptedByteCountRate"], value)

    @property
    def RxEncryptedPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Encrypted Packet Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxEncryptedPacketCountRate"])

    @RxEncryptedPacketCountRate.setter
    def RxEncryptedPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxEncryptedPacketCountRate"], value)

    @property
    def RxFPExpressCRCTypeErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Express CRC Type Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPExpressCRCTypeErrorCount"])

    @RxFPExpressCRCTypeErrorCount.setter
    def RxFPExpressCRCTypeErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPExpressCRCTypeErrorCount"], value)

    @property
    def RxFPExpressCRCTypeErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Express CRC Type Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPExpressCRCTypeErrorCountRate"]
        )

    @RxFPExpressCRCTypeErrorCountRate.setter
    def RxFPExpressCRCTypeErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPExpressCRCTypeErrorCountRate"], value
        )

    @property
    def RxFPFragCountError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Frag Count Error
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPFragCountError"])

    @RxFPFragCountError.setter
    def RxFPFragCountError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPFragCountError"], value)

    @property
    def RxFPFragCountErrorRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Frag Count Error Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPFragCountErrorRate"])

    @RxFPFragCountErrorRate.setter
    def RxFPFragCountErrorRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPFragCountErrorRate"], value)

    @property
    def RxFPInvalidCRCTypeErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Invalid CRC Type Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPInvalidCRCTypeErrorCount"])

    @RxFPInvalidCRCTypeErrorCount.setter
    def RxFPInvalidCRCTypeErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPInvalidCRCTypeErrorCount"], value)

    @property
    def RxFPInvalidCRCTypeErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Invalid CRC Type Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPInvalidCRCTypeErrorCountRate"]
        )

    @RxFPInvalidCRCTypeErrorCountRate.setter
    def RxFPInvalidCRCTypeErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPInvalidCRCTypeErrorCountRate"], value
        )

    @property
    def RxFPReassemblyGoodCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Reassembly Good Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPReassemblyGoodCount"])

    @RxFPReassemblyGoodCount.setter
    def RxFPReassemblyGoodCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPReassemblyGoodCount"], value)

    @property
    def RxFPReassemblyGoodCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Reassembly Good Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPReassemblyGoodCountRate"])

    @RxFPReassemblyGoodCountRate.setter
    def RxFPReassemblyGoodCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPReassemblyGoodCountRate"], value)

    @property
    def RxFPRespondmPacketCRCErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Respond mPacket CRC Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPRespondmPacketCRCErrorCount"])

    @RxFPRespondmPacketCRCErrorCount.setter
    def RxFPRespondmPacketCRCErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPRespondmPacketCRCErrorCount"], value)

    @property
    def RxFPRespondmPacketCRCErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Respond mPacket CRC Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPRespondmPacketCRCErrorCountRate"]
        )

    @RxFPRespondmPacketCRCErrorCountRate.setter
    def RxFPRespondmPacketCRCErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPRespondmPacketCRCErrorCountRate"], value
        )

    @property
    def RxFPRespondmPacketCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Respond mPacket Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPRespondmPacketCount"])

    @RxFPRespondmPacketCount.setter
    def RxFPRespondmPacketCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPRespondmPacketCount"], value)

    @property
    def RxFPRespondmPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Respond mPacket Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPRespondmPacketCountRate"])

    @RxFPRespondmPacketCountRate.setter
    def RxFPRespondmPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPRespondmPacketCountRate"], value)

    @property
    def RxFPSMDC0mPacketCRCErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C0 mPacket CRC Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDC0mPacketCRCErrorCount"])

    @RxFPSMDC0mPacketCRCErrorCount.setter
    def RxFPSMDC0mPacketCRCErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDC0mPacketCRCErrorCount"], value)

    @property
    def RxFPSMDC0mPacketCRCErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C0 mPacket CRC Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPSMDC0mPacketCRCErrorCountRate"]
        )

    @RxFPSMDC0mPacketCRCErrorCountRate.setter
    def RxFPSMDC0mPacketCRCErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPSMDC0mPacketCRCErrorCountRate"], value
        )

    @property
    def RxFPSMDC0mPacketCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C0 mPacket Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDC0mPacketCount"])

    @RxFPSMDC0mPacketCount.setter
    def RxFPSMDC0mPacketCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDC0mPacketCount"], value)

    @property
    def RxFPSMDC0mPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C0 mPacket Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDC0mPacketCountRate"])

    @RxFPSMDC0mPacketCountRate.setter
    def RxFPSMDC0mPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDC0mPacketCountRate"], value)

    @property
    def RxFPSMDC1mPacketCRCErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C1 mPacket CRC Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDC1mPacketCRCErrorCount"])

    @RxFPSMDC1mPacketCRCErrorCount.setter
    def RxFPSMDC1mPacketCRCErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDC1mPacketCRCErrorCount"], value)

    @property
    def RxFPSMDC1mPacketCRCErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C1 mPacket CRC Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPSMDC1mPacketCRCErrorCountRate"]
        )

    @RxFPSMDC1mPacketCRCErrorCountRate.setter
    def RxFPSMDC1mPacketCRCErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPSMDC1mPacketCRCErrorCountRate"], value
        )

    @property
    def RxFPSMDC1mPacketCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C1 mPacket Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDC1mPacketCount"])

    @RxFPSMDC1mPacketCount.setter
    def RxFPSMDC1mPacketCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDC1mPacketCount"], value)

    @property
    def RxFPSMDC1mPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C1 mPacket Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDC1mPacketCountRate"])

    @RxFPSMDC1mPacketCountRate.setter
    def RxFPSMDC1mPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDC1mPacketCountRate"], value)

    @property
    def RxFPSMDC2mPacketCRCErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C2 mPacket CRC Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDC2mPacketCRCErrorCount"])

    @RxFPSMDC2mPacketCRCErrorCount.setter
    def RxFPSMDC2mPacketCRCErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDC2mPacketCRCErrorCount"], value)

    @property
    def RxFPSMDC2mPacketCRCErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C2 mPacket CRC Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPSMDC2mPacketCRCErrorCountRate"]
        )

    @RxFPSMDC2mPacketCRCErrorCountRate.setter
    def RxFPSMDC2mPacketCRCErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPSMDC2mPacketCRCErrorCountRate"], value
        )

    @property
    def RxFPSMDC2mPacketCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C2 mPacket Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDC2mPacketCount"])

    @RxFPSMDC2mPacketCount.setter
    def RxFPSMDC2mPacketCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDC2mPacketCount"], value)

    @property
    def RxFPSMDC2mPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C2 mPacket Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDC2mPacketCountRate"])

    @RxFPSMDC2mPacketCountRate.setter
    def RxFPSMDC2mPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDC2mPacketCountRate"], value)

    @property
    def RxFPSMDC3mPacketCRCErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C3 mPacket CRC Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDC3mPacketCRCErrorCount"])

    @RxFPSMDC3mPacketCRCErrorCount.setter
    def RxFPSMDC3mPacketCRCErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDC3mPacketCRCErrorCount"], value)

    @property
    def RxFPSMDC3mPacketCRCErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C3 mPacket CRC Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPSMDC3mPacketCRCErrorCountRate"]
        )

    @RxFPSMDC3mPacketCRCErrorCountRate.setter
    def RxFPSMDC3mPacketCRCErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPSMDC3mPacketCRCErrorCountRate"], value
        )

    @property
    def RxFPSMDC3mPacketCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C3 mPacket Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDC3mPacketCount"])

    @RxFPSMDC3mPacketCount.setter
    def RxFPSMDC3mPacketCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDC3mPacketCount"], value)

    @property
    def RxFPSMDC3mPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C3 mPacket Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDC3mPacketCountRate"])

    @RxFPSMDC3mPacketCountRate.setter
    def RxFPSMDC3mPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDC3mPacketCountRate"], value)

    @property
    def RxFPSMDCCRCCalcErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C CRC Calc Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDCCRCCalcErrorCount"])

    @RxFPSMDCCRCCalcErrorCount.setter
    def RxFPSMDCCRCCalcErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDCCRCCalcErrorCount"], value)

    @property
    def RxFPSMDCCRCCalcErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C CRC Calc Error Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDCCRCCalcErrorCountRate"])

    @RxFPSMDCCRCCalcErrorCountRate.setter
    def RxFPSMDCCRCCalcErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDCCRCCalcErrorCountRate"], value)

    @property
    def RxFPSMDCFrameCountError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C Frame Count Error
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDCFrameCountError"])

    @RxFPSMDCFrameCountError.setter
    def RxFPSMDCFrameCountError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDCFrameCountError"], value)

    @property
    def RxFPSMDCFrameCountErrorRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C Frame Count Error Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDCFrameCountErrorRate"])

    @RxFPSMDCFrameCountErrorRate.setter
    def RxFPSMDCFrameCountErrorRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDCFrameCountErrorRate"], value)

    @property
    def RxFPSMDCTerminationErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C Termination Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDCTerminationErrorCount"])

    @RxFPSMDCTerminationErrorCount.setter
    def RxFPSMDCTerminationErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDCTerminationErrorCount"], value)

    @property
    def RxFPSMDCTerminationErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-C Termination Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPSMDCTerminationErrorCountRate"]
        )

    @RxFPSMDCTerminationErrorCountRate.setter
    def RxFPSMDCTerminationErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPSMDCTerminationErrorCountRate"], value
        )

    @property
    def RxFPSMDRNotTransmittedCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-R Not Transmitted Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDRNotTransmittedCount"])

    @RxFPSMDRNotTransmittedCount.setter
    def RxFPSMDRNotTransmittedCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDRNotTransmittedCount"], value)

    @property
    def RxFPSMDRNotTransmittedCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-R Not Transmitted Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDRNotTransmittedCountRate"])

    @RxFPSMDRNotTransmittedCountRate.setter
    def RxFPSMDRNotTransmittedCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDRNotTransmittedCountRate"], value)

    @property
    def RxFPSMDS0mPacketCRCErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S0 mPacket CRC Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDS0mPacketCRCErrorCount"])

    @RxFPSMDS0mPacketCRCErrorCount.setter
    def RxFPSMDS0mPacketCRCErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDS0mPacketCRCErrorCount"], value)

    @property
    def RxFPSMDS0mPacketCRCErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S0 mPacket CRC Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPSMDS0mPacketCRCErrorCountRate"]
        )

    @RxFPSMDS0mPacketCRCErrorCountRate.setter
    def RxFPSMDS0mPacketCRCErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPSMDS0mPacketCRCErrorCountRate"], value
        )

    @property
    def RxFPSMDS0mPacketCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S0 mPacket Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDS0mPacketCount"])

    @RxFPSMDS0mPacketCount.setter
    def RxFPSMDS0mPacketCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDS0mPacketCount"], value)

    @property
    def RxFPSMDS0mPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S0 mPacket Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDS0mPacketCountRate"])

    @RxFPSMDS0mPacketCountRate.setter
    def RxFPSMDS0mPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDS0mPacketCountRate"], value)

    @property
    def RxFPSMDS1mPacketCRCErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S1 mPacket CRC Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDS1mPacketCRCErrorCount"])

    @RxFPSMDS1mPacketCRCErrorCount.setter
    def RxFPSMDS1mPacketCRCErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDS1mPacketCRCErrorCount"], value)

    @property
    def RxFPSMDS1mPacketCRCErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S1 mPacket CRC Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPSMDS1mPacketCRCErrorCountRate"]
        )

    @RxFPSMDS1mPacketCRCErrorCountRate.setter
    def RxFPSMDS1mPacketCRCErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPSMDS1mPacketCRCErrorCountRate"], value
        )

    @property
    def RxFPSMDS1mPacketCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S1 mPacket Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDS1mPacketCount"])

    @RxFPSMDS1mPacketCount.setter
    def RxFPSMDS1mPacketCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDS1mPacketCount"], value)

    @property
    def RxFPSMDS1mPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S1 mPacket Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDS1mPacketCountRate"])

    @RxFPSMDS1mPacketCountRate.setter
    def RxFPSMDS1mPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDS1mPacketCountRate"], value)

    @property
    def RxFPSMDS2mPacketCRCErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S2 mPacket CRC Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDS2mPacketCRCErrorCount"])

    @RxFPSMDS2mPacketCRCErrorCount.setter
    def RxFPSMDS2mPacketCRCErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDS2mPacketCRCErrorCount"], value)

    @property
    def RxFPSMDS2mPacketCRCErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S2 mPacket CRC Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPSMDS2mPacketCRCErrorCountRate"]
        )

    @RxFPSMDS2mPacketCRCErrorCountRate.setter
    def RxFPSMDS2mPacketCRCErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPSMDS2mPacketCRCErrorCountRate"], value
        )

    @property
    def RxFPSMDS2mPacketCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S2 mPacket Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDS2mPacketCount"])

    @RxFPSMDS2mPacketCount.setter
    def RxFPSMDS2mPacketCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDS2mPacketCount"], value)

    @property
    def RxFPSMDS2mPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S2 mPacket Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDS2mPacketCountRate"])

    @RxFPSMDS2mPacketCountRate.setter
    def RxFPSMDS2mPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDS2mPacketCountRate"], value)

    @property
    def RxFPSMDS3mPacketCRCErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S3 mPacket CRC Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDS3mPacketCRCErrorCount"])

    @RxFPSMDS3mPacketCRCErrorCount.setter
    def RxFPSMDS3mPacketCRCErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDS3mPacketCRCErrorCount"], value)

    @property
    def RxFPSMDS3mPacketCRCErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S3 mPacket CRC Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPSMDS3mPacketCRCErrorCountRate"]
        )

    @RxFPSMDS3mPacketCRCErrorCountRate.setter
    def RxFPSMDS3mPacketCRCErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPSMDS3mPacketCRCErrorCountRate"], value
        )

    @property
    def RxFPSMDS3mPacketCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S3 mPacket Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDS3mPacketCount"])

    @RxFPSMDS3mPacketCount.setter
    def RxFPSMDS3mPacketCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDS3mPacketCount"], value)

    @property
    def RxFPSMDS3mPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S3 mPacket Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDS3mPacketCountRate"])

    @RxFPSMDS3mPacketCountRate.setter
    def RxFPSMDS3mPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDS3mPacketCountRate"], value)

    @property
    def RxFPSMDSFrameCountError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S Frame Count Error
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDSFrameCountError"])

    @RxFPSMDSFrameCountError.setter
    def RxFPSMDSFrameCountError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDSFrameCountError"], value)

    @property
    def RxFPSMDSFrameCountErrorRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S Frame Count Error Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDSFrameCountErrorRate"])

    @RxFPSMDSFrameCountErrorRate.setter
    def RxFPSMDSFrameCountErrorRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDSFrameCountErrorRate"], value)

    @property
    def RxFPSMDSStartProtocolError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S Start Protocol Error
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDSStartProtocolError"])

    @RxFPSMDSStartProtocolError.setter
    def RxFPSMDSStartProtocolError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDSStartProtocolError"], value)

    @property
    def RxFPSMDSStartProtocolErrorRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S Start Protocol Error Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDSStartProtocolErrorRate"])

    @RxFPSMDSStartProtocolErrorRate.setter
    def RxFPSMDSStartProtocolErrorRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDSStartProtocolErrorRate"], value)

    @property
    def RxFPSMDSTerminationErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S Termination Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDSTerminationErrorCount"])

    @RxFPSMDSTerminationErrorCount.setter
    def RxFPSMDSTerminationErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDSTerminationErrorCount"], value)

    @property
    def RxFPSMDSTerminationErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-S Termination Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPSMDSTerminationErrorCountRate"]
        )

    @RxFPSMDSTerminationErrorCountRate.setter
    def RxFPSMDSTerminationErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPSMDSTerminationErrorCountRate"], value
        )

    @property
    def RxFPSMDVNotReceivedCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-V Not Received Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDVNotReceivedCount"])

    @RxFPSMDVNotReceivedCount.setter
    def RxFPSMDVNotReceivedCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDVNotReceivedCount"], value)

    @property
    def RxFPSMDVNotReceivedCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP SMD-V Not Received Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPSMDVNotReceivedCountRate"])

    @RxFPSMDVNotReceivedCountRate.setter
    def RxFPSMDVNotReceivedCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPSMDVNotReceivedCountRate"], value)

    @property
    def RxFPUnexpectedSMDRCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Unexpected SMD-R Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPUnexpectedSMDRCount"])

    @RxFPUnexpectedSMDRCount.setter
    def RxFPUnexpectedSMDRCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPUnexpectedSMDRCount"], value)

    @property
    def RxFPUnexpectedSMDRCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Unexpected SMD-R Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPUnexpectedSMDRCountRate"])

    @RxFPUnexpectedSMDRCountRate.setter
    def RxFPUnexpectedSMDRCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPUnexpectedSMDRCountRate"], value)

    @property
    def RxFPVerifyProtocolError(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Verify Protocol Error
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPVerifyProtocolError"])

    @RxFPVerifyProtocolError.setter
    def RxFPVerifyProtocolError(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPVerifyProtocolError"], value)

    @property
    def RxFPVerifyProtocolErrorRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Verify Protocol Error Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPVerifyProtocolErrorRate"])

    @RxFPVerifyProtocolErrorRate.setter
    def RxFPVerifyProtocolErrorRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPVerifyProtocolErrorRate"], value)

    @property
    def RxFPVerifymPacketCRCErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Verify mPacket CRC Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPVerifymPacketCRCErrorCount"])

    @RxFPVerifymPacketCRCErrorCount.setter
    def RxFPVerifymPacketCRCErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPVerifymPacketCRCErrorCount"], value)

    @property
    def RxFPVerifymPacketCRCErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Verify mPacket CRC Error Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxFPVerifymPacketCRCErrorCountRate"]
        )

    @RxFPVerifymPacketCRCErrorCountRate.setter
    def RxFPVerifymPacketCRCErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxFPVerifymPacketCRCErrorCountRate"], value
        )

    @property
    def RxFPVerifymPacketCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Verify mPacket Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPVerifymPacketCount"])

    @RxFPVerifymPacketCount.setter
    def RxFPVerifymPacketCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPVerifymPacketCount"], value)

    @property
    def RxFPVerifymPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx FP Verify mPacket Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFPVerifymPacketCountRate"])

    @RxFPVerifymPacketCountRate.setter
    def RxFPVerifymPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFPVerifymPacketCountRate"], value)

    @property
    def RxFpgaTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Fpga Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxFpgaTemperatureC"])

    @RxFpgaTemperatureC.setter
    def RxFpgaTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxFpgaTemperatureC"], value)

    @property
    def RxInvalidICVDiscardedPacketforBroadcastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Invalid ICV Discarded Packet for Broadcast Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxInvalidICVDiscardedPacketforBroadcastRate"]
        )

    @RxInvalidICVDiscardedPacketforBroadcastRate.setter
    def RxInvalidICVDiscardedPacketforBroadcastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxInvalidICVDiscardedPacketforBroadcastRate"], value
        )

    @property
    def RxInvalidICVDiscardedPacketforMulticastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Invalid ICV Discarded Packet for Multicast Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxInvalidICVDiscardedPacketforMulticastRate"]
        )

    @RxInvalidICVDiscardedPacketforMulticastRate.setter
    def RxInvalidICVDiscardedPacketforMulticastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxInvalidICVDiscardedPacketforMulticastRate"], value
        )

    @property
    def RxInvalidICVPacketforBroadcastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Invalid ICV Packet for Broadcast Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxInvalidICVPacketforBroadcastRate"]
        )

    @RxInvalidICVPacketforBroadcastRate.setter
    def RxInvalidICVPacketforBroadcastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxInvalidICVPacketforBroadcastRate"], value
        )

    @property
    def RxInvalidICVPacketforMulticastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Invalid ICV Packet for Multicast Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxInvalidICVPacketforMulticastRate"]
        )

    @RxInvalidICVPacketforMulticastRate.setter
    def RxInvalidICVPacketforMulticastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxInvalidICVPacketforMulticastRate"], value
        )

    @property
    def RxNonMACsecPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx NonMACsec Packet Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxNonMACsecPacketCountRate"])

    @RxNonMACsecPacketCountRate.setter
    def RxNonMACsecPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxNonMACsecPacketCountRate"], value)

    @property
    def RxOpticalPowerHighAlarm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Optical Power High Alarm
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxOpticalPowerHighAlarm"])

    @RxOpticalPowerHighAlarm.setter
    def RxOpticalPowerHighAlarm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxOpticalPowerHighAlarm"], value)

    @property
    def RxOpticalPowerHighWarn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Optical Power High Warn
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxOpticalPowerHighWarn"])

    @RxOpticalPowerHighWarn.setter
    def RxOpticalPowerHighWarn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxOpticalPowerHighWarn"], value)

    @property
    def RxOpticalPowerLimitFlag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Optical Power Limit Flag
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxOpticalPowerLimitFlag"])

    @RxOpticalPowerLimitFlag.setter
    def RxOpticalPowerLimitFlag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxOpticalPowerLimitFlag"], value)

    @property
    def RxOpticalPowerLowAlarm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Optical Power Low Alarm
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxOpticalPowerLowAlarm"])

    @RxOpticalPowerLowAlarm.setter
    def RxOpticalPowerLowAlarm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxOpticalPowerLowAlarm"], value)

    @property
    def RxOpticalPowerLowWarn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Optical Power Low Warn
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxOpticalPowerLowWarn"])

    @RxOpticalPowerLowWarn.setter
    def RxOpticalPowerLowWarn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxOpticalPowerLowWarn"], value)

    @property
    def RxOutofWindowPacketorOutofWindowDiscardedPacketforBroadcastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Out of Window Packet or Out of Window Discarded Packet for Broadcast Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP[
                "RxOutofWindowPacketorOutofWindowDiscardedPacketforBroadcastRate"
            ]
        )

    @RxOutofWindowPacketorOutofWindowDiscardedPacketforBroadcastRate.setter
    def RxOutofWindowPacketorOutofWindowDiscardedPacketforBroadcastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP[
                "RxOutofWindowPacketorOutofWindowDiscardedPacketforBroadcastRate"
            ],
            value,
        )

    @property
    def RxOutofWindowPacketorOutofWindowDiscardedPacketforMulticastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Out of Window Packet or Out of Window Discarded Packet for Multicast Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP[
                "RxOutofWindowPacketorOutofWindowDiscardedPacketforMulticastRate"
            ]
        )

    @RxOutofWindowPacketorOutofWindowDiscardedPacketforMulticastRate.setter
    def RxOutofWindowPacketorOutofWindowDiscardedPacketforMulticastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP[
                "RxOutofWindowPacketorOutofWindowDiscardedPacketforMulticastRate"
            ],
            value,
        )

    @property
    def RxPausePriorityGroup0Frames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 0 Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup0Frames"])

    @RxPausePriorityGroup0Frames.setter
    def RxPausePriorityGroup0Frames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup0Frames"], value)

    @property
    def RxPausePriorityGroup0FramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 0 Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup0FramesRate"])

    @RxPausePriorityGroup0FramesRate.setter
    def RxPausePriorityGroup0FramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup0FramesRate"], value)

    @property
    def RxPausePriorityGroup1Frames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 1 Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup1Frames"])

    @RxPausePriorityGroup1Frames.setter
    def RxPausePriorityGroup1Frames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup1Frames"], value)

    @property
    def RxPausePriorityGroup1FramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 1 Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup1FramesRate"])

    @RxPausePriorityGroup1FramesRate.setter
    def RxPausePriorityGroup1FramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup1FramesRate"], value)

    @property
    def RxPausePriorityGroup2Frames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 2 Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup2Frames"])

    @RxPausePriorityGroup2Frames.setter
    def RxPausePriorityGroup2Frames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup2Frames"], value)

    @property
    def RxPausePriorityGroup2FramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 2 Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup2FramesRate"])

    @RxPausePriorityGroup2FramesRate.setter
    def RxPausePriorityGroup2FramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup2FramesRate"], value)

    @property
    def RxPausePriorityGroup3Frames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 3 Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup3Frames"])

    @RxPausePriorityGroup3Frames.setter
    def RxPausePriorityGroup3Frames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup3Frames"], value)

    @property
    def RxPausePriorityGroup3FramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 3 Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup3FramesRate"])

    @RxPausePriorityGroup3FramesRate.setter
    def RxPausePriorityGroup3FramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup3FramesRate"], value)

    @property
    def RxPausePriorityGroup4Frames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 4 Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup4Frames"])

    @RxPausePriorityGroup4Frames.setter
    def RxPausePriorityGroup4Frames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup4Frames"], value)

    @property
    def RxPausePriorityGroup4FramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 4 Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup4FramesRate"])

    @RxPausePriorityGroup4FramesRate.setter
    def RxPausePriorityGroup4FramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup4FramesRate"], value)

    @property
    def RxPausePriorityGroup5Frames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 5 Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup5Frames"])

    @RxPausePriorityGroup5Frames.setter
    def RxPausePriorityGroup5Frames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup5Frames"], value)

    @property
    def RxPausePriorityGroup5FramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 5 Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup5FramesRate"])

    @RxPausePriorityGroup5FramesRate.setter
    def RxPausePriorityGroup5FramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup5FramesRate"], value)

    @property
    def RxPausePriorityGroup6Frames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 6 Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup6Frames"])

    @RxPausePriorityGroup6Frames.setter
    def RxPausePriorityGroup6Frames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup6Frames"], value)

    @property
    def RxPausePriorityGroup6FramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 6 Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup6FramesRate"])

    @RxPausePriorityGroup6FramesRate.setter
    def RxPausePriorityGroup6FramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup6FramesRate"], value)

    @property
    def RxPausePriorityGroup7Frames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 7 Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup7Frames"])

    @RxPausePriorityGroup7Frames.setter
    def RxPausePriorityGroup7Frames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup7Frames"], value)

    @property
    def RxPausePriorityGroup7FramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Pause Priority Group 7 Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup7FramesRate"])

    @RxPausePriorityGroup7FramesRate.setter
    def RxPausePriorityGroup7FramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxPausePriorityGroup7FramesRate"], value)

    @property
    def RxProtectedByteCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Protected Byte Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxProtectedByteCountRate"])

    @RxProtectedByteCountRate.setter
    def RxProtectedByteCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxProtectedByteCountRate"], value)

    @property
    def RxProtectedPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Protected Packet Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxProtectedPacketCountRate"])

    @RxProtectedPacketCountRate.setter
    def RxProtectedPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxProtectedPacketCountRate"], value)

    @property
    def RxRateKbps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx. Rate (Kbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRateKbps"])

    @RxRateKbps.setter
    def RxRateKbps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRateKbps"], value)

    @property
    def RxRateMbps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx. Rate (Mbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRateMbps"])

    @RxRateMbps.setter
    def RxRateMbps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRateMbps"], value)

    @property
    def RxRatebps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx. Rate (bps)
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRatebps"])

    @RxRatebps.setter
    def RxRatebps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRatebps"], value)

    @property
    def RxRoCEACKFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx RoCE ACK Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRoCEACKFrameCount"])

    @RxRoCEACKFrameCount.setter
    def RxRoCEACKFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRoCEACKFrameCount"], value)

    @property
    def RxRoCEACKFrameCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx RoCE ACK Frame Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRoCEACKFrameCountRate"])

    @RxRoCEACKFrameCountRate.setter
    def RxRoCEACKFrameCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRoCEACKFrameCountRate"], value)

    @property
    def RxRoCECNPFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx RoCE CNP Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRoCECNPFrameCount"])

    @RxRoCECNPFrameCount.setter
    def RxRoCECNPFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRoCECNPFrameCount"], value)

    @property
    def RxRoCECNPFrameCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx RoCE CNP Frame Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRoCECNPFrameCountRate"])

    @RxRoCECNPFrameCountRate.setter
    def RxRoCECNPFrameCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRoCECNPFrameCountRate"], value)

    @property
    def RxRoCEECNFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx RoCE ECN Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRoCEECNFrameCount"])

    @RxRoCEECNFrameCount.setter
    def RxRoCEECNFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRoCEECNFrameCount"], value)

    @property
    def RxRoCEECNFrameCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx RoCE ECN Frame Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRoCEECNFrameCountRate"])

    @RxRoCEECNFrameCountRate.setter
    def RxRoCEECNFrameCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRoCEECNFrameCountRate"], value)

    @property
    def RxRoCENAKFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx RoCE NAK Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRoCENAKFrameCount"])

    @RxRoCENAKFrameCount.setter
    def RxRoCENAKFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRoCENAKFrameCount"], value)

    @property
    def RxRoCENAKFrameCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx RoCE NAK Frame Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRoCENAKFrameCountRate"])

    @RxRoCENAKFrameCountRate.setter
    def RxRoCENAKFrameCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRoCENAKFrameCountRate"], value)

    @property
    def RxRoCEOpcodeErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx RoCE Opcode Error Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRoCEOpcodeErrorCountRate"])

    @RxRoCEOpcodeErrorCountRate.setter
    def RxRoCEOpcodeErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRoCEOpcodeErrorCountRate"], value)

    @property
    def RxRoCEPrePFCCNPFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx RoCE Pre-PFC CNP Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRoCEPrePFCCNPFrameCount"])

    @RxRoCEPrePFCCNPFrameCount.setter
    def RxRoCEPrePFCCNPFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRoCEPrePFCCNPFrameCount"], value)

    @property
    def RxRoCEPrePFCCNPFrameCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx RoCE Pre-PFC CNP Frame Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRoCEPrePFCCNPFrameCountRate"])

    @RxRoCEPrePFCCNPFrameCountRate.setter
    def RxRoCEPrePFCCNPFrameCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRoCEPrePFCCNPFrameCountRate"], value)

    @property
    def RxRoCEiCRCErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx RoCE iCRC Error Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxRoCEiCRCErrorCountRate"])

    @RxRoCEiCRCErrorCountRate.setter
    def RxRoCEiCRCErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxRoCEiCRCErrorCountRate"], value)

    @property
    def RxSharedStat1(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Shared Stat 1
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxSharedStat1"])

    @RxSharedStat1.setter
    def RxSharedStat1(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxSharedStat1"], value)

    @property
    def RxSharedStat1Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Shared Stat 1 Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxSharedStat1Rate"])

    @RxSharedStat1Rate.setter
    def RxSharedStat1Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxSharedStat1Rate"], value)

    @property
    def RxSharedStat2(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Shared Stat 2
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxSharedStat2"])

    @RxSharedStat2.setter
    def RxSharedStat2(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxSharedStat2"], value)

    @property
    def RxSharedStat2Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Shared Stat 2 Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxSharedStat2Rate"])

    @RxSharedStat2Rate.setter
    def RxSharedStat2Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxSharedStat2Rate"], value)

    @property
    def RxUnknownSCIDiscardedPacketorUnusedSADiscardedPacketRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Unknown SCI Discarded Packet or Unused SA Discarded Packet Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP[
                "RxUnknownSCIDiscardedPacketorUnusedSADiscardedPacketRate"
            ]
        )

    @RxUnknownSCIDiscardedPacketorUnusedSADiscardedPacketRate.setter
    def RxUnknownSCIDiscardedPacketorUnusedSADiscardedPacketRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP[
                "RxUnknownSCIDiscardedPacketorUnusedSADiscardedPacketRate"
            ],
            value,
        )

    @property
    def RxUnknownSCIPacketorUnusedSAPacketRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Unknown SCI Packet or Unused SA Packet Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["RxUnknownSCIPacketorUnusedSAPacketRate"]
        )

    @RxUnknownSCIPacketorUnusedSAPacketRate.setter
    def RxUnknownSCIPacketorUnusedSAPacketRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["RxUnknownSCIPacketorUnusedSAPacketRate"], value
        )

    @property
    def RxUnvalidatedPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Unvalidated Packet Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxUnvalidatedPacketCountRate"])

    @RxUnvalidatedPacketCountRate.setter
    def RxUnvalidatedPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxUnvalidatedPacketCountRate"], value)

    @property
    def RxValidPacketforBroadcastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Valid Packet for Broadcast Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxValidPacketforBroadcastRate"])

    @RxValidPacketforBroadcastRate.setter
    def RxValidPacketforBroadcastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxValidPacketforBroadcastRate"], value)

    @property
    def RxValidPacketforMulticastRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Rx Valid Packet for Multicast Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxValidPacketforMulticastRate"])

    @RxValidPacketforMulticastRate.setter
    def RxValidPacketforMulticastRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxValidPacketforMulticastRate"], value)

    @property
    def ScheduledCellsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Scheduled Cells Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ScheduledCellsTx"])

    @ScheduledCellsTx.setter
    def ScheduledCellsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ScheduledCellsTx"], value)

    @property
    def ScheduledCellsTxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Scheduled Cells Tx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["ScheduledCellsTxRate"])

    @ScheduledCellsTxRate.setter
    def ScheduledCellsTxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ScheduledCellsTxRate"], value)

    @property
    def ScheduledFramesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Scheduled Frames Tx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ScheduledFramesTx"])

    @ScheduledFramesTx.setter
    def ScheduledFramesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ScheduledFramesTx"], value)

    @property
    def ScheduledFramesTxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Scheduled Frames Tx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["ScheduledFramesTxRate"])

    @ScheduledFramesTxRate.setter
    def ScheduledFramesTxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ScheduledFramesTxRate"], value)

    @property
    def ScheduledTransmitDuration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Scheduled Transmit Duration
        """
        return self._get_attribute(self._SDM_ATT_MAP["ScheduledTransmitDuration"])

    @ScheduledTransmitDuration.setter
    def ScheduledTransmitDuration(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ScheduledTransmitDuration"], value)

    @property
    def ScheduledTxRoCEACKFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Scheduled Tx RoCE ACK Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["ScheduledTxRoCEACKFrameCount"])

    @ScheduledTxRoCEACKFrameCount.setter
    def ScheduledTxRoCEACKFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ScheduledTxRoCEACKFrameCount"], value)

    @property
    def ScheduledTxRoCEACKFrameCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Scheduled Tx RoCE ACK Frame Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ScheduledTxRoCEACKFrameCountRate"]
        )

    @ScheduledTxRoCEACKFrameCountRate.setter
    def ScheduledTxRoCEACKFrameCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ScheduledTxRoCEACKFrameCountRate"], value
        )

    @property
    def ScheduledTxRoCECNPFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Scheduled Tx RoCE CNP Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["ScheduledTxRoCECNPFrameCount"])

    @ScheduledTxRoCECNPFrameCount.setter
    def ScheduledTxRoCECNPFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ScheduledTxRoCECNPFrameCount"], value)

    @property
    def ScheduledTxRoCECNPFrameCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Scheduled Tx RoCE CNP Frame Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ScheduledTxRoCECNPFrameCountRate"]
        )

    @ScheduledTxRoCECNPFrameCountRate.setter
    def ScheduledTxRoCECNPFrameCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ScheduledTxRoCECNPFrameCountRate"], value
        )

    @property
    def ScheduledTxRoCENAKFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Scheduled Tx RoCE NAK Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["ScheduledTxRoCENAKFrameCount"])

    @ScheduledTxRoCENAKFrameCount.setter
    def ScheduledTxRoCENAKFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ScheduledTxRoCENAKFrameCount"], value)

    @property
    def ScheduledTxRoCENAKFrameCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Scheduled Tx RoCE NAK Frame Count Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ScheduledTxRoCENAKFrameCountRate"]
        )

    @ScheduledTxRoCENAKFrameCountRate.setter
    def ScheduledTxRoCENAKFrameCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ScheduledTxRoCENAKFrameCountRate"], value
        )

    @property
    def SchedulerChipTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Scheduler Chip Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["SchedulerChipTemperatureC"])

    @SchedulerChipTemperatureC.setter
    def SchedulerChipTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SchedulerChipTemperatureC"], value)

    @property
    def SectionBIPB1(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Section BIP (B1)
        """
        return self._get_attribute(self._SDM_ATT_MAP["SectionBIPB1"])

    @SectionBIPB1.setter
    def SectionBIPB1(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SectionBIPB1"], value)

    @property
    def SectionBIPB1Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Section BIP (B1) Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["SectionBIPB1Rate"])

    @SectionBIPB1Rate.setter
    def SectionBIPB1Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SectionBIPB1Rate"], value)

    @property
    def SectionBIPErroredSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Section BIP Errored Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["SectionBIPErroredSeconds"])

    @SectionBIPErroredSeconds.setter
    def SectionBIPErroredSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SectionBIPErroredSeconds"], value)

    @property
    def SectionBIPSeverelyErroredSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Section BIP Severely Errored Seconds
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["SectionBIPSeverelyErroredSeconds"]
        )

    @SectionBIPSeverelyErroredSeconds.setter
    def SectionBIPSeverelyErroredSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["SectionBIPSeverelyErroredSeconds"], value
        )

    @property
    def SectionLOF(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Section LOF
        """
        return self._get_attribute(self._SDM_ATT_MAP["SectionLOF"])

    @SectionLOF.setter
    def SectionLOF(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SectionLOF"], value)

    @property
    def SectionLOS(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Section LOS
        """
        return self._get_attribute(self._SDM_ATT_MAP["SectionLOS"])

    @SectionLOS.setter
    def SectionLOS(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SectionLOS"], value)

    @property
    def SectionLOSSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Section LOS Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["SectionLOSSeconds"])

    @SectionLOSSeconds.setter
    def SectionLOSSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SectionLOSSeconds"], value)

    @property
    def SequenceErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sequence Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["SequenceErrors"])

    @SequenceErrors.setter
    def SequenceErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SequenceErrors"], value)

    @property
    def SequenceErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sequence Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["SequenceErrorsRate"])

    @SequenceErrorsRate.setter
    def SequenceErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SequenceErrorsRate"], value)

    @property
    def SequenceFrames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sequence Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["SequenceFrames"])

    @SequenceFrames.setter
    def SequenceFrames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SequenceFrames"], value)

    @property
    def SequenceFramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sequence Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["SequenceFramesRate"])

    @SequenceFramesRate.setter
    def SequenceFramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SequenceFramesRate"], value)

    @property
    def SeverelyErroredSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Severely Errored Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["SeverelyErroredSeconds"])

    @SeverelyErroredSeconds.setter
    def SeverelyErroredSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SeverelyErroredSeconds"], value)

    @property
    def SofBigErrorFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: SOF Big Error Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["SofBigErrorFrameCount"])

    @SofBigErrorFrameCount.setter
    def SofBigErrorFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SofBigErrorFrameCount"], value)

    @property
    def SofEarlyFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: SOF Early Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["SofEarlyFrameCount"])

    @SofEarlyFrameCount.setter
    def SofEarlyFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SofEarlyFrameCount"], value)

    @property
    def SofEarlyMaximumByteCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: SOF Early Maximum Byte Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["SofEarlyMaximumByteCount"])

    @SofEarlyMaximumByteCount.setter
    def SofEarlyMaximumByteCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SofEarlyMaximumByteCount"], value)

    @property
    def SofEarlyMinimumByteCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: SOF Early Minimum Byte Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["SofEarlyMinimumByteCount"])

    @SofEarlyMinimumByteCount.setter
    def SofEarlyMinimumByteCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SofEarlyMinimumByteCount"], value)

    @property
    def StatelessBitsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Bits Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessBitsReceived"])

    @StatelessBitsReceived.setter
    def StatelessBitsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessBitsReceived"], value)

    @property
    def StatelessBitsSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Bits Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessBitsSent"])

    @StatelessBitsSent.setter
    def StatelessBitsSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessBitsSent"], value)

    @property
    def StatelessBytesReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Bytes Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessBytesReceived"])

    @StatelessBytesReceived.setter
    def StatelessBytesReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessBytesReceived"], value)

    @property
    def StatelessBytesReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Bytes Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessBytesReceivedRate"])

    @StatelessBytesReceivedRate.setter
    def StatelessBytesReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessBytesReceivedRate"], value)

    @property
    def StatelessBytesRxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Bytes Rx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessBytesRxRate"])

    @StatelessBytesRxRate.setter
    def StatelessBytesRxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessBytesRxRate"], value)

    @property
    def StatelessBytesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Bytes Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessBytesSent"])

    @StatelessBytesSent.setter
    def StatelessBytesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessBytesSent"], value)

    @property
    def StatelessBytesSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Bytes Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessBytesSentRate"])

    @StatelessBytesSentRate.setter
    def StatelessBytesSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessBytesSentRate"], value)

    @property
    def StatelessBytesTxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Bytes Tx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessBytesTxRate"])

    @StatelessBytesTxRate.setter
    def StatelessBytesTxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessBytesTxRate"], value)

    @property
    def StatelessFramesSent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Frames Sent
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessFramesSent"])

    @StatelessFramesSent.setter
    def StatelessFramesSent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessFramesSent"], value)

    @property
    def StatelessFramesSentRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Frames Sent Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessFramesSentRate"])

    @StatelessFramesSentRate.setter
    def StatelessFramesSentRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessFramesSentRate"], value)

    @property
    def StatelessRxRateKbps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Rx. Rate (Kbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessRxRateKbps"])

    @StatelessRxRateKbps.setter
    def StatelessRxRateKbps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessRxRateKbps"], value)

    @property
    def StatelessRxRateMbps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Rx. Rate (Mbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessRxRateMbps"])

    @StatelessRxRateMbps.setter
    def StatelessRxRateMbps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessRxRateMbps"], value)

    @property
    def StatelessRxRatebps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Rx. Rate (bps)
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessRxRatebps"])

    @StatelessRxRatebps.setter
    def StatelessRxRatebps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessRxRatebps"], value)

    @property
    def StatelessTxRateKbps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Tx. Rate (Kbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessTxRateKbps"])

    @StatelessTxRateKbps.setter
    def StatelessTxRateKbps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessTxRateKbps"], value)

    @property
    def StatelessTxRateMbps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Tx. Rate (Mbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessTxRateMbps"])

    @StatelessTxRateMbps.setter
    def StatelessTxRateMbps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessTxRateMbps"], value)

    @property
    def StatelessTxRatebps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Stateless Tx. Rate (bps)
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatelessTxRatebps"])

    @StatelessTxRatebps.setter
    def StatelessTxRatebps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatelessTxRatebps"], value)

    @property
    def Status(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Status
        """
        return self._get_attribute(self._SDM_ATT_MAP["Status"])

    @Status.setter
    def Status(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Status"], value)

    @property
    def SupplyVoltageHighAlarm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Supply Voltage High Alarm
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupplyVoltageHighAlarm"])

    @SupplyVoltageHighAlarm.setter
    def SupplyVoltageHighAlarm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupplyVoltageHighAlarm"], value)

    @property
    def SupplyVoltageHighWarn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Supply Voltage High Warn
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupplyVoltageHighWarn"])

    @SupplyVoltageHighWarn.setter
    def SupplyVoltageHighWarn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupplyVoltageHighWarn"], value)

    @property
    def SupplyVoltageLimitFlag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Supply Voltage Limit Flag
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupplyVoltageLimitFlag"])

    @SupplyVoltageLimitFlag.setter
    def SupplyVoltageLimitFlag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupplyVoltageLimitFlag"], value)

    @property
    def SupplyVoltageLowAlarm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Supply Voltage Low Alarm
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupplyVoltageLowAlarm"])

    @SupplyVoltageLowAlarm.setter
    def SupplyVoltageLowAlarm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupplyVoltageLowAlarm"], value)

    @property
    def SupplyVoltageLowWarn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Supply Voltage Low Warn
        """
        return self._get_attribute(self._SDM_ATT_MAP["SupplyVoltageLowWarn"])

    @SupplyVoltageLowWarn.setter
    def SupplyVoltageLowWarn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SupplyVoltageLowWarn"], value)

    @property
    def TcpChecksumErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: TCP Checksum Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpChecksumErrors"])

    @TcpChecksumErrors.setter
    def TcpChecksumErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcpChecksumErrors"], value)

    @property
    def TcpChecksumErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: TCP Checksum Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpChecksumErrorsRate"])

    @TcpChecksumErrorsRate.setter
    def TcpChecksumErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcpChecksumErrorsRate"], value)

    @property
    def TcpPacketsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: TCP Packets Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpPacketsReceived"])

    @TcpPacketsReceived.setter
    def TcpPacketsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcpPacketsReceived"], value)

    @property
    def TcpPacketsReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: TCP Packets Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["TcpPacketsReceivedRate"])

    @TcpPacketsReceivedRate.setter
    def TcpPacketsReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TcpPacketsReceivedRate"], value)

    @property
    def TemperatureHighAlarm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Temperature High Alarm
        """
        return self._get_attribute(self._SDM_ATT_MAP["TemperatureHighAlarm"])

    @TemperatureHighAlarm.setter
    def TemperatureHighAlarm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TemperatureHighAlarm"], value)

    @property
    def TemperatureHighWarn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Temperature High Warn
        """
        return self._get_attribute(self._SDM_ATT_MAP["TemperatureHighWarn"])

    @TemperatureHighWarn.setter
    def TemperatureHighWarn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TemperatureHighWarn"], value)

    @property
    def TemperatureLimitFlag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Temperature Limit Flag
        """
        return self._get_attribute(self._SDM_ATT_MAP["TemperatureLimitFlag"])

    @TemperatureLimitFlag.setter
    def TemperatureLimitFlag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TemperatureLimitFlag"], value)

    @property
    def TemperatureLowAlarm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Temperature Low Alarm
        """
        return self._get_attribute(self._SDM_ATT_MAP["TemperatureLowAlarm"])

    @TemperatureLowAlarm.setter
    def TemperatureLowAlarm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TemperatureLowAlarm"], value)

    @property
    def TemperatureLowWarn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Temperature Low Warn
        """
        return self._get_attribute(self._SDM_ATT_MAP["TemperatureLowWarn"])

    @TemperatureLowWarn.setter
    def TemperatureLowWarn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TemperatureLowWarn"], value)

    @property
    def TotalMemory(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Total Memory
        """
        return self._get_attribute(self._SDM_ATT_MAP["TotalMemory"])

    @TotalMemory.setter
    def TotalMemory(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TotalMemory"], value)

    @property
    def TransceiverTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Transceiver Temperature (C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransceiverTemperatureC"])

    @TransceiverTemperatureC.setter
    def TransceiverTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransceiverTemperatureC"], value)

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
    def TransmitArpGratuitousRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Transmit Arp Gratuitous Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitArpGratuitousRate"])

    @TransmitArpGratuitousRate.setter
    def TransmitArpGratuitousRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitArpGratuitousRate"], value)

    @property
    def TransmitArpReply(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Transmit Arp Reply
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitArpReply"])

    @TransmitArpReply.setter
    def TransmitArpReply(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitArpReply"], value)

    @property
    def TransmitArpRequest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Transmit Arp Request
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitArpRequest"])

    @TransmitArpRequest.setter
    def TransmitArpRequest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitArpRequest"], value)

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

    @property
    def TransmitArpReverseRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Transmit Arp Reverse Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitArpReverseRate"])

    @TransmitArpReverseRate.setter
    def TransmitArpReverseRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitArpReverseRate"], value)

    @property
    def TransmitDurationClearedonStartTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Transmit Duration(Cleared on Start Tx)
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["TransmitDurationClearedonStartTx"]
        )

    @TransmitDurationClearedonStartTx.setter
    def TransmitDurationClearedonStartTx(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["TransmitDurationClearedonStartTx"], value
        )

    @property
    def TransmitNeighborAdvertisements(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Transmit Neighbor Advertisements
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitNeighborAdvertisements"])

    @TransmitNeighborAdvertisements.setter
    def TransmitNeighborAdvertisements(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitNeighborAdvertisements"], value)

    @property
    def TransmitNeighborSolicitation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Transmit Neighbor Solicitation
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitNeighborSolicitation"])

    @TransmitNeighborSolicitation.setter
    def TransmitNeighborSolicitation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitNeighborSolicitation"], value)

    @property
    def TransmitPingReply(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Transmit Ping Reply
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitPingReply"])

    @TransmitPingReply.setter
    def TransmitPingReply(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitPingReply"], value)

    @property
    def TransmitPingRequest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Transmit Ping Request
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitPingRequest"])

    @TransmitPingRequest.setter
    def TransmitPingRequest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitPingRequest"], value)

    @property
    def Tx0FpgaTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx0 Fpga Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Tx0FpgaTemperatureC"])

    @Tx0FpgaTemperatureC.setter
    def Tx0FpgaTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Tx0FpgaTemperatureC"], value)

    @property
    def TxBiasCurrentHighAlarm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Bias Current High Alarm
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxBiasCurrentHighAlarm"])

    @TxBiasCurrentHighAlarm.setter
    def TxBiasCurrentHighAlarm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxBiasCurrentHighAlarm"], value)

    @property
    def TxBiasCurrentHighWarn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Bias Current High Warn
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxBiasCurrentHighWarn"])

    @TxBiasCurrentHighWarn.setter
    def TxBiasCurrentHighWarn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxBiasCurrentHighWarn"], value)

    @property
    def TxBiasCurrentLimitFlag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Bias Current Limit Flag
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxBiasCurrentLimitFlag"])

    @TxBiasCurrentLimitFlag.setter
    def TxBiasCurrentLimitFlag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxBiasCurrentLimitFlag"], value)

    @property
    def TxBiasCurrentLowAlarm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Bias Current Low Alarm
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxBiasCurrentLowAlarm"])

    @TxBiasCurrentLowAlarm.setter
    def TxBiasCurrentLowAlarm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxBiasCurrentLowAlarm"], value)

    @property
    def TxBiasCurrentLowWarn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Bias Current Low Warn
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxBiasCurrentLowWarn"])

    @TxBiasCurrentLowWarn.setter
    def TxBiasCurrentLowWarn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxBiasCurrentLowWarn"], value)

    @property
    def TxEncryptedByteCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Encrypted Byte Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxEncryptedByteCountRate"])

    @TxEncryptedByteCountRate.setter
    def TxEncryptedByteCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxEncryptedByteCountRate"], value)

    @property
    def TxEncryptedPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Encrypted Packet Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxEncryptedPacketCountRate"])

    @TxEncryptedPacketCountRate.setter
    def TxEncryptedPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxEncryptedPacketCountRate"], value)

    @property
    def TxFpgaTemperatureC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Fpga Temperature(C)
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxFpgaTemperatureC"])

    @TxFpgaTemperatureC.setter
    def TxFpgaTemperatureC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxFpgaTemperatureC"], value)

    @property
    def TxNonMACsecPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx NonMACsec Packet Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxNonMACsecPacketCountRate"])

    @TxNonMACsecPacketCountRate.setter
    def TxNonMACsecPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxNonMACsecPacketCountRate"], value)

    @property
    def TxOpticalPowerHighAlarm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Optical Power High Alarm
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxOpticalPowerHighAlarm"])

    @TxOpticalPowerHighAlarm.setter
    def TxOpticalPowerHighAlarm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxOpticalPowerHighAlarm"], value)

    @property
    def TxOpticalPowerHighWarn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Optical Power High Warn
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxOpticalPowerHighWarn"])

    @TxOpticalPowerHighWarn.setter
    def TxOpticalPowerHighWarn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxOpticalPowerHighWarn"], value)

    @property
    def TxOpticalPowerLimitFlag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Optical Power Limit Flag
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxOpticalPowerLimitFlag"])

    @TxOpticalPowerLimitFlag.setter
    def TxOpticalPowerLimitFlag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxOpticalPowerLimitFlag"], value)

    @property
    def TxOpticalPowerLowAlarm(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Optical Power Low Alarm
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxOpticalPowerLowAlarm"])

    @TxOpticalPowerLowAlarm.setter
    def TxOpticalPowerLowAlarm(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxOpticalPowerLowAlarm"], value)

    @property
    def TxOpticalPowerLowWarn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Optical Power Low Warn
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxOpticalPowerLowWarn"])

    @TxOpticalPowerLowWarn.setter
    def TxOpticalPowerLowWarn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxOpticalPowerLowWarn"], value)

    @property
    def TxProtectedByteCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Protected Byte Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxProtectedByteCountRate"])

    @TxProtectedByteCountRate.setter
    def TxProtectedByteCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxProtectedByteCountRate"], value)

    @property
    def TxProtectedPacketCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx Protected Packet Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxProtectedPacketCountRate"])

    @TxProtectedPacketCountRate.setter
    def TxProtectedPacketCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxProtectedPacketCountRate"], value)

    @property
    def TxRateKbps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx. Rate (Kbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxRateKbps"])

    @TxRateKbps.setter
    def TxRateKbps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxRateKbps"], value)

    @property
    def TxRateMbps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx. Rate (Mbps)
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxRateMbps"])

    @TxRateMbps.setter
    def TxRateMbps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxRateMbps"], value)

    @property
    def TxRatebps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Tx. Rate (bps)
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxRatebps"])

    @TxRatebps.setter
    def TxRatebps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxRatebps"], value)

    @property
    def UdpChecksumErrors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: UDP Checksum Errors
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpChecksumErrors"])

    @UdpChecksumErrors.setter
    def UdpChecksumErrors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpChecksumErrors"], value)

    @property
    def UdpChecksumErrorsRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: UDP Checksum Errors Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpChecksumErrorsRate"])

    @UdpChecksumErrorsRate.setter
    def UdpChecksumErrorsRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpChecksumErrorsRate"], value)

    @property
    def UdpPacketsReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: UDP Packets Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpPacketsReceived"])

    @UdpPacketsReceived.setter
    def UdpPacketsReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpPacketsReceived"], value)

    @property
    def UdpPacketsReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: UDP Packets Received Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["UdpPacketsReceivedRate"])

    @UdpPacketsReceivedRate.setter
    def UdpPacketsReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UdpPacketsReceivedRate"], value)

    @property
    def UnavailableSeconds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unavailable Seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnavailableSeconds"])

    @UnavailableSeconds.setter
    def UnavailableSeconds(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnavailableSeconds"], value)

    @property
    def UncorrectedHCSErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Uncorrected HCS Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["UncorrectedHCSErrorCount"])

    @UncorrectedHCSErrorCount.setter
    def UncorrectedHCSErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UncorrectedHCSErrorCount"], value)

    @property
    def UncorrectedHCSErrorCountRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Uncorrected HCS Error Count Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["UncorrectedHCSErrorCountRate"])

    @UncorrectedHCSErrorCountRate.setter
    def UncorrectedHCSErrorCountRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UncorrectedHCSErrorCountRate"], value)

    @property
    def Undersize(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Undersize
        """
        return self._get_attribute(self._SDM_ATT_MAP["Undersize"])

    @Undersize.setter
    def Undersize(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Undersize"], value)

    @property
    def UndersizeRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Undersize Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["UndersizeRate"])

    @UndersizeRate.setter
    def UndersizeRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UndersizeRate"], value)

    @property
    def UnexpectedPLCABeaconReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unexpected PLCA Beacon Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnexpectedPLCABeaconReceived"])

    @UnexpectedPLCABeaconReceived.setter
    def UnexpectedPLCABeaconReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnexpectedPLCABeaconReceived"], value)

    @property
    def UnknownSCISAAccepted(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unknown SCI/SA Accepted
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnknownSCISAAccepted"])

    @UnknownSCISAAccepted.setter
    def UnknownSCISAAccepted(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnknownSCISAAccepted"], value)

    @property
    def UnknownSCISADiscarded(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unknown SCI/SA Discarded
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnknownSCISADiscarded"])

    @UnknownSCISADiscarded.setter
    def UnknownSCISADiscarded(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnknownSCISADiscarded"], value)

    @property
    def UnvalidatedPacketRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Unvalidated Packet Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnvalidatedPacketRx"])

    @UnvalidatedPacketRx.setter
    def UnvalidatedPacketRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnvalidatedPacketRx"], value)

    @property
    def UserDefinedStat1(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: User Defined Stat 1
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDefinedStat1"])

    @UserDefinedStat1.setter
    def UserDefinedStat1(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDefinedStat1"], value)

    @property
    def UserDefinedStat1Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: User Defined Stat 1 Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDefinedStat1Rate"])

    @UserDefinedStat1Rate.setter
    def UserDefinedStat1Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDefinedStat1Rate"], value)

    @property
    def UserDefinedStat2(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: User Defined Stat 2
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDefinedStat2"])

    @UserDefinedStat2.setter
    def UserDefinedStat2(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDefinedStat2"], value)

    @property
    def UserDefinedStat2Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: User Defined Stat 2 Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDefinedStat2Rate"])

    @UserDefinedStat2Rate.setter
    def UserDefinedStat2Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDefinedStat2Rate"], value)

    @property
    def UserDefinedStat5(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: User Defined Stat 5
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDefinedStat5"])

    @UserDefinedStat5.setter
    def UserDefinedStat5(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDefinedStat5"], value)

    @property
    def UserDefinedStat5Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: User Defined Stat 5 Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDefinedStat5Rate"])

    @UserDefinedStat5Rate.setter
    def UserDefinedStat5Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDefinedStat5Rate"], value)

    @property
    def UserDefinedStat6(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: User Defined Stat 6
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDefinedStat6"])

    @UserDefinedStat6.setter
    def UserDefinedStat6(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDefinedStat6"], value)

    @property
    def UserDefinedStat6Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: User Defined Stat 6 Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDefinedStat6Rate"])

    @UserDefinedStat6Rate.setter
    def UserDefinedStat6Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDefinedStat6Rate"], value)

    @property
    def UserDefinedStatByteCount1(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: User Defined Stat Byte Count 1
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDefinedStatByteCount1"])

    @UserDefinedStatByteCount1.setter
    def UserDefinedStatByteCount1(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDefinedStatByteCount1"], value)

    @property
    def UserDefinedStatByteCount1Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: User Defined Stat Byte Count 1 Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDefinedStatByteCount1Rate"])

    @UserDefinedStatByteCount1Rate.setter
    def UserDefinedStatByteCount1Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDefinedStatByteCount1Rate"], value)

    @property
    def UserDefinedStatByteCount2(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: User Defined Stat Byte Count 2
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDefinedStatByteCount2"])

    @UserDefinedStatByteCount2.setter
    def UserDefinedStatByteCount2(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDefinedStatByteCount2"], value)

    @property
    def UserDefinedStatByteCount2Rate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: User Defined Stat Byte Count 2 Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["UserDefinedStatByteCount2Rate"])

    @UserDefinedStatByteCount2Rate.setter
    def UserDefinedStatByteCount2Rate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UserDefinedStatByteCount2Rate"], value)

    @property
    def ValidFramesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Valid Frames Rx.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ValidFramesRx"])

    @ValidFramesRx.setter
    def ValidFramesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ValidFramesRx"], value)

    @property
    def ValidFramesRxRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Valid Frames Rx. Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["ValidFramesRxRate"])

    @ValidFramesRxRate.setter
    def ValidFramesRxRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ValidFramesRxRate"], value)

    @property
    def ValidPacketRxBroadcast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Valid Packet Rx Broadcast
        """
        return self._get_attribute(self._SDM_ATT_MAP["ValidPacketRxBroadcast"])

    @ValidPacketRxBroadcast.setter
    def ValidPacketRxBroadcast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ValidPacketRxBroadcast"], value)

    @property
    def ValidPacketRxMulticast(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Valid Packet Rx Multicast
        """
        return self._get_attribute(self._SDM_ATT_MAP["ValidPacketRxMulticast"])

    @ValidPacketRxMulticast.setter
    def ValidPacketRxMulticast(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ValidPacketRxMulticast"], value)

    @property
    def ValidStatelessFramesReceived(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Valid Stateless Frames Received
        """
        return self._get_attribute(self._SDM_ATT_MAP["ValidStatelessFramesReceived"])

    @ValidStatelessFramesReceived.setter
    def ValidStatelessFramesReceived(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ValidStatelessFramesReceived"], value)

    @property
    def ValidStatelessFramesReceivedRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Valid Stateless Frames Received Rate
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["ValidStatelessFramesReceivedRate"]
        )

    @ValidStatelessFramesReceivedRate.setter
    def ValidStatelessFramesReceivedRate(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["ValidStatelessFramesReceivedRate"], value
        )

    @property
    def VlanTaggedFrames(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Vlan Tagged Frames
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanTaggedFrames"])

    @VlanTaggedFrames.setter
    def VlanTaggedFrames(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanTaggedFrames"], value)

    @property
    def VlanTaggedFramesRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Vlan Tagged Frames Rate
        """
        return self._get_attribute(self._SDM_ATT_MAP["VlanTaggedFramesRate"])

    @VlanTaggedFramesRate.setter
    def VlanTaggedFramesRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["VlanTaggedFramesRate"], value)

    @property
    def WindowClosedFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Window Closed Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["WindowClosedFrameCount"])

    @WindowClosedFrameCount.setter
    def WindowClosedFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["WindowClosedFrameCount"], value)

    @property
    def WindowValidFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Window Valid Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["WindowValidFrameCount"])

    @WindowValidFrameCount.setter
    def WindowValidFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["WindowValidFrameCount"], value)

    @property
    def WindowViolationFrameCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Window Violation Frame Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["WindowViolationFrameCount"])

    @WindowViolationFrameCount.setter
    def WindowViolationFrameCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["WindowViolationFrameCount"], value)

    def update(self, **kwargs):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> PortStatistics
        """Updates portStatistics resource on the server.

        Args
        ----
        - Aal5FramesRx (bool): AAL5 Frames Rx.
        - Aal5FramesRxRate (bool): AAL5 Frames Rx. Rate
        - Aal5FramesTx (bool): AAL5 Frames Tx.
        - Aal5FramesTxRate (bool): AAL5 Frames Tx. Rate
        - Aal5PayloadBytesRx (bool): AAL5 Payload Bytes Rx.
        - Aal5PayloadBytesRxRate (bool): AAL5 Payload Bytes Rx. Rate
        - Aal5PayloadBytesTx (bool): AAL5 Payload Bytes Tx.
        - Aal5PayloadBytesTxRate (bool): AAL5 Payload Bytes Tx. Rate
        - ActiveFECMode (bool): Active FEC Mode
        - AlignmentErrors (bool): Alignment Errors
        - AlignmentErrorsRate (bool): Alignment Errors Rate
        - AsynchronousFramesSent (bool): Asynchronous Frames Sent
        - AsynchronousFramesSentRate (bool): Asynchronous Frames Sent Rate
        - AtmCellsRx (bool): ATM Cells Rx.
        - AtmCellsRxRate (bool): ATM Cells Rx. Rate
        - AtmCellsTx (bool): ATM Cells Tx.
        - AtmCellsTxRate (bool): ATM Cells Tx. Rate
        - AtmUnregisteredCellsRx (bool): ATM Unregistered Cells Rx.
        - AtmUnregisteredCellsRxRate (bool): ATM Unregistered Cells Rx. Rate
        - AvailableSeconds (bool): Available Seconds
        - BackgroundBlockErrors (bool): Background Block Errors
        - BackgroundBlockErrorsRate (bool): Background Block Errors Rate
        - BackgroundChipTemperatureC (bool): Background Chip Temperature(C)
        - BadPacketRxBroadcast (bool): Bad Packet Rx Broadcast
        - BadPacketRxMulticast (bool): Bad Packet Rx Multicast
        - BadTagICVDiscardedBroadcast (bool): Bad Tag/ICV Discarded Broadcast
        - BadTagICVDiscardedMulticast (bool): Bad Tag/ICV Discarded Multicast
        - BertBitsReceived (bool): BERT Bits Received
        - BertBitsSent (bool): BERT Bits Sent
        - BitErrorsReceived (bool): Bit Errors Received
        - BitErrorsSent (bool): Bit Errors Sent
        - BitsReceived (bool): Bits Received
        - BitsReceivedRate (bool): Bits Received Rate
        - BitsSent (bool): Bits Sent
        - BitsSentRate (bool): Bits Sent Rate
        - BlockErrorState (bool): Block Error State
        - ByteAlignmentError (bool): Byte Alignment Error
        - ByteAlignmentErrorRate (bool): Byte Alignment Error Rate
        - BytesRx (bool): Bytes Rx.
        - BytesRxRate (bool): Bytes Rx. Rate
        - BytesSentTransmitDuration (bool): Bytes Sent / Transmit Duration
        - BytesTx (bool): Bytes Tx.
        - BytesTxRate (bool): Bytes Tx. Rate
        - CaptureChipTemperatureC (bool): Capture Chip Temperature(C)
        - CaptureFilterUDS4 (bool): Capture Filter (UDS 4)
        - CaptureFilterUDS4Rate (bool): Capture Filter (UDS 4) Rate
        - CaptureTriggerUDS3 (bool): Capture Trigger (UDS 3)
        - CaptureTriggerUDS3Rate (bool): Capture Trigger (UDS 3) Rate
        - CentralChipTemperatureC (bool): Central Chip Temperature(C)
        - CodeError (bool): Code Error
        - CodeErrorRate (bool): Code Error Rate
        - CollisionFrames (bool): Collision Frames
        - CollisionFramesRate (bool): Collision Frames Rate
        - Collisions (bool): Collisions
        - CollisionsRate (bool): Collisions Rate
        - ControlFramesRx (bool): Control Frames Rx
        - ControlFramesTx (bool): Control Frames Tx
        - CorrectedHCSErrorCount (bool): Corrected HCS Error Count
        - CorrectedHCSErrorCountRate (bool): Corrected HCS Error Count Rate
        - CpuIdle (bool): CPU Idle
        - CpuLoadAvg15Minutes (bool): CPU Load Avg (15 Minutes)
        - CpuLoadAvg1Minute (bool): CPU Load Avg (1 Minute)
        - CpuLoadAvg5Minutes (bool): CPU Load Avg (5 Minutes)
        - CpuRxFrameSize1024to2047 (bool): CPU Rx Frame Size 1024 to 2047
        - CpuRxFrameSize128to255 (bool): CPU Rx Frame Size 128 to 255
        - CpuRxFrameSize2048to4095 (bool): CPU Rx Frame Size 2048 to 4095
        - CpuRxFrameSize256to511 (bool): CPU Rx Frame Size 256 to 511
        - CpuRxFrameSize4096andabove (bool): CPU Rx Frame Size 4096 and above
        - CpuRxFrameSize512to1023 (bool): CPU Rx Frame Size 512 to 1023
        - CpuRxFrameSize64to127 (bool): CPU Rx Frame Size 64 to 127
        - CpuRxFrameSizelessthan64 (bool): CPU Rx Frame Size less than 64
        - CpuTxFrameSize1024to2047 (bool): CPU Tx Frame Size 1024 to 2047
        - CpuTxFrameSize128to255 (bool): CPU Tx Frame Size 128 to 255
        - CpuTxFrameSize2048to4095 (bool): CPU Tx Frame Size 2048 to 4095
        - CpuTxFrameSize256to511 (bool): CPU Tx Frame Size 256 to 511
        - CpuTxFrameSize4096andabove (bool): CPU Tx Frame Size 4096 and above
        - CpuTxFrameSize512to1023 (bool): CPU Tx Frame Size 512 to 1023
        - CpuTxFrameSize64to127 (bool): CPU Tx Frame Size 64 to 127
        - CpuTxFrameSizelessthan64 (bool): CPU Tx Frame Size less than 64
        - CrcErrors (bool): CRC Errors
        - CrcErrorsRate (bool): CRC Errors Rate
        - CumulativeServiceDisruptionTimems (bool): Cumulative Service Disruption Time (ms)
        - CumulativeServiceDisruptionTimemsRate (bool): Cumulative Service Disruption Time (ms) Rate
        - CustomOrderedSetsReceived (bool): Custom Ordered Sets Received
        - CustomOrderedSetsReceivedRate (bool): Custom Ordered Sets Received Rate
        - CustomOrderedSetsSent (bool): Custom Ordered Sets Sent
        - CustomOrderedSetsSentRate (bool): Custom Ordered Sets Sent Rate
        - DataIntegrityErrors (bool): Data Integrity Errors
        - DataIntegrityErrorsRate (bool): Data Integrity Errors Rate
        - DataIntegrityFramesRate (bool): Data Integrity Frames Rate
        - DataIntegrityFramesRx (bool): Data Integrity Frames Rx.
        - DeskewBitErrorsReceived (bool): Deskew Bit Errors Received
        - DeskewBitErrorsReceivedRate (bool): Deskew Bit Errors Received Rate
        - DeskewBitErrorsSent (bool): Deskew Bit Errors Sent
        - DeskewBitErrorsSentRate (bool): Deskew Bit Errors Sent Rate
        - DeskewErrorFreeFramesReceived (bool): Deskew Error Free Frames Received
        - DeskewErrorFreeFramesReceivedRate (bool): Deskew Error Free Frames Received Rate
        - DeskewErrorFreeFramesSent (bool): Deskew Error Free Frames Sent
        - DeskewErrorFreeFramesSentRate (bool): Deskew Error Free Frames Sent Rate
        - DeskewErroredFramesReceived (bool): Deskew Errored Frames Received
        - DeskewErroredFramesReceivedRate (bool): Deskew Errored Frames Received Rate
        - DeskewErroredFramesSent (bool): Deskew Errored Frames Sent
        - DeskewErroredFramesSentRate (bool): Deskew Errored Frames Sent Rate
        - DeskewLossOfFrame (bool): Deskew Loss Of Frame
        - DeskewLossOfFrameRate (bool): Deskew Loss Of Frame Rate
        - Dhcpv4ACKsReceived (bool): DHCPv4 ACKs Received
        - Dhcpv4AddressesLearned (bool): DHCPv4 Addresses Learned
        - Dhcpv4DiscoveredMessagesSent (bool): DHCPv4 Discovered Messages Sent
        - Dhcpv4EnabledInterfaces (bool): DHCPv4 Enabled Interfaces
        - Dhcpv4NACKsReceived (bool): DHCPv4 NACKs Received
        - Dhcpv4OffersReceived (bool): DHCPv4 Offers Received
        - Dhcpv4ReleasesSent (bool): DHCPv4 Releases Sent
        - Dhcpv4RequestsSent (bool): DHCPv4 Requests Sent
        - DisparityErrors (bool): Disparity Errors
        - DisparityErrorsRate (bool): Disparity Errors Rate
        - DmaChipTemperatureC (bool): DMA Chip Temperature(C)
        - DribbleErrors (bool): Dribble Errors
        - DribbleErrorsRate (bool): Dribble Errors Rate
        - DroppedFrames (bool): Dropped Frames
        - DroppedFramesRate (bool): Dropped Frames Rate
        - DuplexMode (bool): Duplex Mode
        - ElapsedTestTime (bool): Elapsed Test Time
        - ElapsedTestTimeRate (bool): Elapsed Test Time Rate
        - Encoding (bool): Encoding
        - EncryptedByteRx (bool): Encrypted Byte Rx
        - EncryptedByteTx (bool): Encrypted Byte Tx
        - EncryptedPacketRx (bool): Encrypted Packet Rx
        - EncryptedPacketTx (bool): Encrypted Packet Tx
        - EndofStreamDelimiterError (bool): End-of-Stream Delimiter Error
        - EofBigErrorFrameCount (bool): EOF Big Error Frame Count
        - EofLateFrameCount (bool): EOF Late Frame Count
        - EofLateMaximumByteCount (bool): EOF Late Maximum Byte Count
        - EofLateMinimumByteCount (bool): EOF Late Minimum Byte Count
        - ErrorFreeSeconds (bool): Error Free Seconds
        - ErroredBlocks (bool): Errored Blocks
        - ErroredBlocksRate (bool): Errored Blocks Rate
        - ErroredSeconds (bool): Errored Seconds
        - EthernetCRC (bool): Ethernet CRC
        - EthernetCRCRate (bool): Ethernet CRC Rate
        - EthernetOAMEventNotificationPDUsReceived (bool): Ethernet OAM Event Notification PDUs Received
        - EthernetOAMInformationPDUsReceived (bool): Ethernet OAM Information PDUs Received
        - EthernetOAMInformationPDUsSent (bool): Ethernet OAM Information PDUs Sent
        - EthernetOAMLoopbackControlPDUsReceived (bool): Ethernet OAM Loopback Control PDUs Received
        - EthernetOAMOrganisationPDUsReceived (bool): Ethernet OAM Organisation PDUs Received
        - EthernetOAMUnsupportedPDUsReceived (bool): Ethernet OAM Unsupported PDUs Received
        - EthernetOAMVariableRequestPDUsReceived (bool): Ethernet OAM Variable Request PDUs Received
        - EthernetOAMVariableResponseReceived (bool): Ethernet OAM Variable Response Received
        - ExcessiveCollisionFrames (bool): Excessive Collision Frames
        - ExcessiveCollisionFramesRate (bool): Excessive Collision Frames Rate
        - FcFECCorrectedBlockCount (bool): FC-FEC Corrected Block Count
        - FcFECCorrectedBlockCountRate (bool): FC-FEC Corrected Block Count Rate
        - FcFECCorrectedErrorBits (bool): FC-FEC Corrected Error Bits
        - FcFECCorrectedErrorBitsRate (bool): FC-FEC Corrected Error Bits Rate
        - FcFECUncorrectedBlockCount (bool): FC-FEC Uncorrected Block Count
        - FcFECUncorrectedBlockCountRate (bool): FC-FEC Uncorrected Block Count Rate
        - FdiscSent (bool): Fdisc Sent
        - FdiscSuccessful (bool): Fdisc Successful
        - FecCodewordswith0errors (bool): FEC Codewords with 0 errors
        - FecCodewordswith0errorsRate (bool): FEC Codewords with 0 errors Rate
        - FecCodewordswith10errors (bool): FEC Codewords with 10 errors
        - FecCodewordswith10errorsRate (bool): FEC Codewords with 10 errors Rate
        - FecCodewordswith11errors (bool): FEC Codewords with 11 errors
        - FecCodewordswith11errorsRate (bool): FEC Codewords with 11 errors Rate
        - FecCodewordswith12errors (bool): FEC Codewords with 12 errors
        - FecCodewordswith12errorsRate (bool): FEC Codewords with 12 errors Rate
        - FecCodewordswith13errors (bool): FEC Codewords with 13 errors
        - FecCodewordswith13errorsRate (bool): FEC Codewords with 13 errors Rate
        - FecCodewordswith14errors (bool): FEC Codewords with 14 errors
        - FecCodewordswith14errorsRate (bool): FEC Codewords with 14 errors Rate
        - FecCodewordswith15errors (bool): FEC Codewords with 15 errors
        - FecCodewordswith15errorsRate (bool): FEC Codewords with 15 errors Rate
        - FecCodewordswith1error (bool): FEC Codewords with 1 error
        - FecCodewordswith1errorRate (bool): FEC Codewords with 1 error Rate
        - FecCodewordswith2errors (bool): FEC Codewords with 2 errors
        - FecCodewordswith2errorsRate (bool): FEC Codewords with 2 errors Rate
        - FecCodewordswith3errors (bool): FEC Codewords with 3 errors
        - FecCodewordswith3errorsRate (bool): FEC Codewords with 3 errors Rate
        - FecCodewordswith4errors (bool): FEC Codewords with 4 errors
        - FecCodewordswith4errorsRate (bool): FEC Codewords with 4 errors Rate
        - FecCodewordswith5errors (bool): FEC Codewords with 5 errors
        - FecCodewordswith5errorsRate (bool): FEC Codewords with 5 errors Rate
        - FecCodewordswith6errors (bool): FEC Codewords with 6 errors
        - FecCodewordswith6errorsRate (bool): FEC Codewords with 6 errors Rate
        - FecCodewordswith7errors (bool): FEC Codewords with 7 errors
        - FecCodewordswith7errorsRate (bool): FEC Codewords with 7 errors Rate
        - FecCodewordswith8errors (bool): FEC Codewords with 8 errors
        - FecCodewordswith8errorsRate (bool): FEC Codewords with 8 errors Rate
        - FecCodewordswith9errors (bool): FEC Codewords with 9 errors
        - FecCodewordswith9errorsRate (bool): FEC Codewords with 9 errors Rate
        - FecCorrected0sCount (bool): FEC Corrected 0s Count
        - FecCorrected0sCountRate (bool): FEC Corrected 0s Count Rate
        - FecCorrected1sCount (bool): FEC Corrected 1s Count
        - FecCorrected1sCountRate (bool): FEC Corrected 1s Count Rate
        - FecCorrectedBitsCount (bool): FEC Corrected Bits Count
        - FecCorrectedBitsCountRate (bool): FEC Corrected Bits Count Rate
        - FecCorrectedBytesCount (bool): FEC Corrected Bytes Count
        - FecCorrectedBytesCountRate (bool): FEC Corrected Bytes Count Rate
        - FecCorrectedCodewords (bool): FEC Corrected Codewords
        - FecCorrectedCodewordsRate (bool): FEC Corrected Codewords Rate
        - FecFrameLossRatio (bool): FEC Frame Loss Ratio
        - FecMaxSymbolErrors (bool): FEC Max Symbol Errors
        - FecTotalBitErrors (bool): FEC Total Bit Errors
        - FecTotalBitErrorsRate (bool): FEC Total Bit Errors Rate
        - FecTotalCodewords (bool): FEC Total Codewords
        - FecTotalCodewordsRate (bool): FEC Total Codewords Rate
        - FecTranscodingUncorrectableEvents (bool): FEC Transcoding Uncorrectable Events
        - FecTranscodingUncorrectableEventsRate (bool): FEC Transcoding Uncorrectable Events Rate
        - FecUncorrectableCodewords (bool): FEC Uncorrectable Codewords
        - FecUncorrectableCodewordsRate (bool): FEC Uncorrectable Codewords Rate
        - FecUncorrectableSubrowCount (bool): FEC Uncorrectable Subrow Count
        - FecUncorrectableSubrowCountRate (bool): FEC Uncorrectable Subrow Count Rate
        - FirecodeFECSync (bool): Fire code FEC Sync
        - FivebDecodeError (bool): 5B Decode Error
        - FlogiSent (bool): Flogi Sent
        - FlogiSuccessful (bool): Flogi Successful
        - FlogoSent (bool): Flogo Sent
        - FlowControlFrames (bool): Flow Control Frames
        - FlowControlFramesRate (bool): Flow Control Frames Rate
        - FomBoardTemperatureC (bool): Fom Board Temperature(C)
        - FomInternalTemperatureC (bool): Fom Internal Temperature(C)
        - FomPortTemperatureC (bool): Fom Port Temperature(C)
        - Fragments (bool): Fragments
        - FragmentsRate (bool): Fragments Rate
        - FramerAbort (bool): Framer Abort
        - FramerAbortRate (bool): Framer Abort Rate
        - FramerMaxLength (bool): Framer Max Length
        - FramerMaxLengthRate (bool): Framer Max Length Rate
        - FramerMinLength (bool): Framer Min Length
        - FramerMinLengthRate (bool): Framer Min Length Rate
        - FramesReceivedwithCodingErrors (bool): Frames Received with Coding Errors
        - FramesReceivedwithCodingErrorsRate (bool): Frames Received with Coding Errors Rate
        - FramesReceivedwithEerrorCharacter (bool): Frames Received with /E/ error Character
        - FramesReceivedwithEerrorCharacterRate (bool): Frames Received with /E/ error Character Rate
        - FramesTx (bool): Frames Tx.
        - FramesTxRate (bool): Frames Tx. Rate
        - FreeMemory (bool): Free Memory
        - FrontendChipTemperatureC (bool): FrontEnd Chip Temperature(C)
        - HostConfigStatus (bool): Host Config Status
        - HostDataPathState (bool): Host Data Path State
        - HostLaneCount (bool): Host Lane Count
        - HostToMediaLane (bool): Host To Media Lane
        - HostTxCDRLOL (bool): Host Tx CDR LOL
        - HostTxLOS (bool): Host Tx LOS
        - IdleCellsRx (bool): Idle Cells Rx.
        - IdleCellsRxRate (bool): Idle Cells Rx. Rate
        - InputSignalStrengthdBm (bool): Input Signal Strength (dBm)
        - InsertionState (bool): Insertion State
        - InvalidEOF (bool): Invalid EOF
        - InvalidEOFRate (bool): Invalid EOF Rate
        - InvalidICVAcceptedBroadcast (bool): Invalid ICV Accepted Broadcast
        - InvalidICVAcceptedMulticast (bool): Invalid ICV Accepted Multicast
        - InvalidICVDiscardedBroadcast (bool): Invalid ICV Discarded Broadcast
        - InvalidICVDiscardedMulticast (bool): Invalid ICV Discarded Multicast
        - Ipv4ChecksumErrors (bool): IPv4 Checksum Errors
        - Ipv4ChecksumErrorsRate (bool): IPv4 Checksum Errors Rate
        - Ipv4PacketsReceived (bool): IPv4 Packets Received
        - Ipv4PacketsReceivedRate (bool): IPv4 Packets Received Rate
        - KernelTimestamp (bool): Kernel Timestamp
        - L1BitsReceived (bool): L1 Bits Received
        - L1BitsReceivedRate (bool): L1 Bits Received Rate
        - L1BitsSent (bool): L1 Bits Sent
        - L1BitsSentRate (bool): L1 Bits Sent Rate
        - L1LineRateReceivePercent (bool): L1 Line Rate Receive (%)
        - L1LineRateTransmitPercent (bool): L1 Line Rate Transmit (%)
        - LastServiceDisruptionTimems (bool): Last Service Disruption Time (ms)
        - LateCollisions (bool): Late Collisions
        - LateCollisionsRate (bool): Late Collisions Rate
        - LatencyChipTemperatureC (bool): Latency Chip Temperature(C)
        - LineAIS (bool): Line AIS
        - LineAISAlarmedSeconds (bool): Line AIS Alarmed Seconds
        - LineBIPB2 (bool): Line BIP (B2)
        - LineBIPB2Rate (bool): Line BIP (B2) Rate
        - LineBIPErroredSeconds (bool): Line BIP Errored Seconds
        - LineErrorFrames (bool): Line Error Frames
        - LineErrorFramesRate (bool): Line Error Frames Rate
        - LineErrors (bool): Line Errors
        - LineErrorsRate (bool): Line Errors Rate
        - LineRDI (bool): Line RDI
        - LineRDIUnavailableSeconds (bool): Line RDI Unavailable Seconds
        - LineREIErroredSeconds (bool): Line REI Errored Seconds
        - LineREIFEBE (bool): Line REI (FEBE)
        - LineREIFEBERate (bool): Line REI (FEBE) Rate
        - LineSpeed (bool): Line Speed
        - LinkFaultState (bool): Link Fault State
        - LinkState (bool): Link State
        - LocalFaults (bool): Local Faults
        - LocalOrderedSetsReceived (bool): Local Ordered Sets Received
        - LocalOrderedSetsReceivedRate (bool): Local Ordered Sets Received Rate
        - LocalOrderedSetsSent (bool): Local Ordered Sets Sent
        - LocalOrderedSetsSentRate (bool): Local Ordered Sets Sent Rate
        - MaxServiceDisruptionTimems (bool): Max Service Disruption Time (ms)
        - MediaLaneCount (bool): Media Lane Count
        - MediaRxCDRLOL (bool): Media Rx CDR LOL
        - MediaRxLOS (bool): Media Rx LOS
        - MediaRxOpticalPower (bool): Media Rx Optical Power
        - MediaTxBiasCurrent (bool): Media Tx Bias Current
        - MediaTxOpticalPower (bool): Media Tx Optical Power
        - MinServiceDisruptionTimems (bool): Min Service Disruption Time (ms)
        - MisdirectedPacketCount (bool): Misdirected Packet Count
        - MisdirectedPacketCountRate (bool): Misdirected Packet Count Rate
        - NonMACsecPacketRx (bool): Non-MACsec Packet Rx
        - NonMACsecPacketTx (bool): Non-MACsec Packet Tx
        - NportidsAcquired (bool): NPortIds Acquired
        - NportsEnabled (bool): NPorts Enabled
        - NsRegSent (bool): NS Reg Sent
        - NsRegSuccessful (bool): NS Reg Successful
        - NumberofMismatched0s (bool): Number of Mismatched 0's
        - NumberofMismatched0sRate (bool): Number of Mismatched 0's Rate
        - NumberofMismatched1s (bool): Number of Mismatched 1's
        - NumberofMismatched1sRate (bool): Number of Mismatched 1's Rate
        - NumberofRRDYsReceived (bool): Number of R_RDYs Received
        - NumberofRRDYsReceivedRate (bool): Number of R_RDYs Received Rate
        - NumberofRRDYsSent (bool): Number of R_RDYs Sent
        - NumberofRRDYsSentRate (bool): Number of R_RDYs Sent Rate
        - OutofWindowRxBroadcast (bool): Out of Window Rx Broadcast
        - OutofWindowRxMulticast (bool): Out of Window Rx Multicast
        - OverlayChipTemperatureC (bool): Overlay Chip Temperature(C)
        - Oversize (bool): Oversize
        - OversizeRate (bool): Oversize Rate
        - OversizeandCRCErrors (bool): Oversize and CRC Errors
        - OversizeandCRCErrorsRate (bool): Oversize and CRC Errors Rate
        - PathAIS (bool): Path AIS
        - PathAISAlarmedSeconds (bool): Path AIS Alarmed Seconds
        - PathAISUnavailableSeconds (bool): Path AIS Unavailable Seconds
        - PathBIPB3 (bool): Path BIP (B3)
        - PathBIPB3Rate (bool): Path BIP (B3) Rate
        - PathBIPErroredSeconds (bool): Path BIP Errored Seconds
        - PathLOP (bool): Path LOP
        - PathPLMC2 (bool): Path PLM (C2)
        - PathRDI (bool): Path RDI
        - PathRDIUnavailableSeconds (bool): Path RDI Unavailable Seconds
        - PathREIErroredSeconds (bool): Path REI Errored Seconds
        - PathREIFEBE (bool): Path REI (FEBE)
        - PathREIFEBERate (bool): Path REI (FEBE) Rate
        - PauseAcknowledge (bool): Pause Acknowledge
        - PauseAcknowledgeRate (bool): Pause Acknowledge Rate
        - PauseEndFrames (bool): Pause End Frames
        - PauseEndFramesRate (bool): Pause End Frames Rate
        - PauseOverwrite (bool): Pause Overwrite
        - PauseOverwriteRate (bool): Pause Overwrite Rate
        - PcsIllegalCodes (bool): PCS Illegal Codes
        - PcsIllegalCodesRate (bool): PCS Illegal Codes Rate
        - PcsIllegalIdle (bool): PCS Illegal Idle
        - PcsIllegalIdleRate (bool): PCS Illegal Idle Rate
        - PcsIllegalOrderedSet (bool): PCS Illegal Ordered Set
        - PcsIllegalOrderedSetRate (bool): PCS Illegal Ordered Set Rate
        - PcsIllegalSOF (bool): PCS Illegal SOF
        - PcsIllegalSOFRate (bool): PCS Illegal SOF Rate
        - PcsLocalFaults (bool): PCS Local Faults
        - PcsLocalFaultsRate (bool): PCS Local Faults Rate
        - PcsOutofOrderData (bool): PCS Out of Order Data
        - PcsOutofOrderDataRate (bool): PCS Out of Order Data Rate
        - PcsOutofOrderEOF (bool): PCS Out of Order EOF
        - PcsOutofOrderEOFRate (bool): PCS Out of Order EOF Rate
        - PcsOutofOrderOrderedSet (bool): PCS Out of Order Ordered Set
        - PcsOutofOrderOrderedSetRate (bool): PCS Out of Order Ordered Set Rate
        - PcsOutofOrderSOF (bool): PCS Out of Order SOF
        - PcsOutofOrderSOFRate (bool): PCS Out of Order SOF Rate
        - PcsRemoteFaults (bool): PCS Remote Faults
        - PcsRemoteFaultsRate (bool): PCS Remote Faults Rate
        - PcsSyncErrors (bool): PCS Sync Errors
        - PcsSyncErrorsRate (bool): PCS Sync Errors Rate
        - PercentCPULoad (bool): %CPU Load
        - PfcPriority0BufferMaxDepth (bool): PFC Priority 0 Buffer Max Depth
        - PfcPriority0PacketDrop (bool): PFC Priority 0 Packet Drop
        - PfcPriority0PacketDropRate (bool): PFC Priority 0 Packet Drop Rate
        - PfcPriority0PauseRatioPercent (bool): PFC Priority 0 Pause Ratio(%)
        - PfcPriority0PauseStart (bool): PFC Priority 0 Pause Start
        - PfcPriority0PauseStartResent (bool): PFC Priority 0 Pause Start Resent
        - PfcPriority0PauseStop (bool): PFC Priority 0 Pause Stop
        - PfcPriority1BufferMaxDepth (bool): PFC Priority 1 Buffer Max Depth
        - PfcPriority1PacketDrop (bool): PFC Priority 1 Packet Drop
        - PfcPriority1PacketDropRate (bool): PFC Priority 1 Packet Drop Rate
        - PfcPriority1PauseRatioPercent (bool): PFC Priority 1 Pause Ratio(%)
        - PfcPriority1PauseStart (bool): PFC Priority 1 Pause Start
        - PfcPriority1PauseStartResent (bool): PFC Priority 1 Pause Start Resent
        - PfcPriority1PauseStop (bool): PFC Priority 1 Pause Stop
        - PfcPriority2BufferMaxDepth (bool): PFC Priority 2 Buffer Max Depth
        - PfcPriority2PacketDrop (bool): PFC Priority 2 Packet Drop
        - PfcPriority2PacketDropRate (bool): PFC Priority 2 Packet Drop Rate
        - PfcPriority2PauseRatioPercent (bool): PFC Priority 2 Pause Ratio(%)
        - PfcPriority2PauseStart (bool): PFC Priority 2 Pause Start
        - PfcPriority2PauseStartResent (bool): PFC Priority 2 Pause Start Resent
        - PfcPriority2PauseStop (bool): PFC Priority 2 Pause Stop
        - PfcPriority3BufferMaxDepth (bool): PFC Priority 3 Buffer Max Depth
        - PfcPriority3PacketDrop (bool): PFC Priority 3 Packet Drop
        - PfcPriority3PacketDropRate (bool): PFC Priority 3 Packet Drop Rate
        - PfcPriority3PauseRatioPercent (bool): PFC Priority 3 Pause Ratio(%)
        - PfcPriority3PauseStart (bool): PFC Priority 3 Pause Start
        - PfcPriority3PauseStartResent (bool): PFC Priority 3 Pause Start Resent
        - PfcPriority3PauseStop (bool): PFC Priority 3 Pause Stop
        - PfcPriority4BufferMaxDepth (bool): PFC Priority 4 Buffer Max Depth
        - PfcPriority4PacketDrop (bool): PFC Priority 4 Packet Drop
        - PfcPriority4PacketDropRate (bool): PFC Priority 4 Packet Drop Rate
        - PfcPriority4PauseRatioPercent (bool): PFC Priority 4 Pause Ratio(%)
        - PfcPriority4PauseStart (bool): PFC Priority 4 Pause Start
        - PfcPriority4PauseStartResent (bool): PFC Priority 4 Pause Start Resent
        - PfcPriority4PauseStop (bool): PFC Priority 4 Pause Stop
        - PfcPriority5BufferMaxDepth (bool): PFC Priority 5 Buffer Max Depth
        - PfcPriority5PacketDrop (bool): PFC Priority 5 Packet Drop
        - PfcPriority5PacketDropRate (bool): PFC Priority 5 Packet Drop Rate
        - PfcPriority5PauseRatioPercent (bool): PFC Priority 5 Pause Ratio(%)
        - PfcPriority5PauseStart (bool): PFC Priority 5 Pause Start
        - PfcPriority5PauseStartResent (bool): PFC Priority 5 Pause Start Resent
        - PfcPriority5PauseStop (bool): PFC Priority 5 Pause Stop
        - PfcPriority6BufferMaxDepth (bool): PFC Priority 6 Buffer Max Depth
        - PfcPriority6PacketDrop (bool): PFC Priority 6 Packet Drop
        - PfcPriority6PacketDropRate (bool): PFC Priority 6 Packet Drop Rate
        - PfcPriority6PauseRatioPercent (bool): PFC Priority 6 Pause Ratio(%)
        - PfcPriority6PauseStart (bool): PFC Priority 6 Pause Start
        - PfcPriority6PauseStartResent (bool): PFC Priority 6 Pause Start Resent
        - PfcPriority6PauseStop (bool): PFC Priority 6 Pause Stop
        - PfcPriority7BufferMaxDepth (bool): PFC Priority 7 Buffer Max Depth
        - PfcPriority7PacketDrop (bool): PFC Priority 7 Packet Drop
        - PfcPriority7PacketDropRate (bool): PFC Priority 7 Packet Drop Rate
        - PfcPriority7PauseRatioPercent (bool): PFC Priority 7 Pause Ratio(%)
        - PfcPriority7PauseStart (bool): PFC Priority 7 Pause Start
        - PfcPriority7PauseStartResent (bool): PFC Priority 7 Pause Start Resent
        - PfcPriority7PauseStop (bool): PFC Priority 7 Pause Stop
        - PgidOverflow (bool): PGID Overflow
        - PgidOverflowRate (bool): PGID Overflow Rate
        - PhyChipTemperatureC (bool): PHY Chip Temperature (C)
        - PlcaBeaconCount (bool): PLCA Beacon Count
        - PlcaBeaconCountRate (bool): PLCA Beacon Count Rate
        - PlcaBeaconReceivedBeforeTransmitOpportunity (bool): PLCA Beacon Received Before Transmit Opportunity
        - PlcaCorruptedTransmitCount (bool): PLCA Corrupted Transmit Count
        - PlcaCorruptedTransmitCountRate (bool): PLCA Corrupted Transmit Count Rate
        - PlcaEmptyCycleStatus (bool): PLCA Empty Cycle Status
        - PlcaTransmitOpportunityCount (bool): PLCA Transmit Opportunity Count
        - PlcaTransmitOpportunityCountRate (bool): PLCA Transmit Opportunity Count Rate
        - Plcasymboldetected (bool): PLCA symbol detected
        - PlmInternalTemperature1C (bool): Plm Internal Temperature 1(C)
        - PlmInternalTemperature2C (bool): Plm Internal Temperature 2(C)
        - PlmInternalTemperature3C (bool): Plm Internal Temperature 3(C)
        - PlogiReceived (bool): Plogi Received
        - PlogiSent (bool): Plogi Sent
        - PlogiSuccessful (bool): Plogi Successful
        - PlogoReceived (bool): Plogo Received
        - PlogoSent (bool): Plogo Sent
        - PortCPUDoDStatus (bool): Port CPU DoD Status
        - PortCPUFramesReceived (bool): Port CPU Frames Received
        - PortCPUFramesSent (bool): Port CPU Frames Sent
        - PortCPUFramesSentRate (bool): Port CPU Frames Sent Rate
        - PortCPUStatus (bool): Port CPU Status
        - PortChipTemperatureC (bool): Port Chip Temperature(C)
        - PortName (bool): Port Name
        - PrbsBerRatio (bool): Prbs Ber Ratio
        - PrbsBitsReceived (bool): Prbs Bits Received
        - PrbsBitsReceivedRate (bool): Prbs Bits Received Rate
        - PrbsErroredBits (bool): Prbs Errored Bits
        - PrbsErroredBitsRate (bool): Prbs Errored Bits Rate
        - PrbsFramesReceived (bool): Prbs Frames Received
        - PrbsFramesReceivedRate (bool): Prbs Frames Received Rate
        - PrbsFramesWithHeaderError (bool): Prbs Frames With Header Error
        - PrbsFramesWithHeaderErrorRate (bool): Prbs Frames With Header Error Rate
        - PreFECBitErrorRatio (bool): pre FEC Bit Error Ratio
        - ProtectedByteRx (bool): Protected Byte Rx
        - ProtectedByteTx (bool): Protected Byte Tx
        - ProtectedPacketRx (bool): Protected Packet Rx
        - ProtectedPacketTx (bool): Protected Packet Tx
        - ProtocolServerVlanDroppedFrames (bool): Protocol Server Vlan Dropped Frames
        - PtpAnnounceMessagesReceived (bool): Ptp Announce Messages Received
        - PtpAnnounceMessagesSent (bool): Ptp Announce Messages Sent
        - PtpDelayReqMessagesReceived (bool): Ptp Delay_Req Messages Received
        - PtpDelayReqMessagesSent (bool): Ptp Delay_Req Messages Sent
        - PtpDelayRespMessagesReceived (bool): Ptp Delay_Resp Messages Received
        - PtpDelayRespMessagesSent (bool): Ptp Delay_Resp Messages Sent
        - PtpFollowUpMessagesReceived (bool): Ptp Follow_Up Messages Received
        - PtpFollowUpMessagesSent (bool): Ptp Follow_Up Messages Sent
        - PtpSyncMessagesReceived (bool): Ptp Sync Messages Received
        - PtpSyncMessagesSent (bool): Ptp Sync Messages Sent
        - RamDiskUtilization (bool): RAM Disk Utilization
        - ReceiveArpReply (bool): Receive Arp Reply
        - ReceiveArpRequest (bool): Receive Arp Request
        - ReceiveInTransmitOpportunity (bool): Receive In Transmit Opportunity
        - ReceiveNeighborAdvertisements (bool): Receive Neighbor Advertisements
        - ReceiveNeighborSolicitation (bool): Receive Neighbor Solicitation
        - ReceivePingReply (bool): Receive Ping Reply
        - ReceivePingRequest (bool): Receive Ping Request
        - RemoteBuffertoBufferCreditCount (bool): Remote Buffer-to-Buffer Credit Count
        - RemoteBuffertoBufferCreditValue (bool): Remote Buffer-to-Buffer Credit Value
        - RemoteFaults (bool): Remote Faults
        - RemoteOrderedSetsReceived (bool): Remote Ordered Sets Received
        - RemoteOrderedSetsReceivedRate (bool): Remote Ordered Sets Received Rate
        - RemoteOrderedSetsSent (bool): Remote Ordered Sets Sent
        - RemoteOrderedSetsSentRate (bool): Remote Ordered Sets Sent Rate
        - Rocev2BadiCRCCount (bool): RoCEv2 Bad iCRC Count
        - Rocev2OpCodeErrorCount (bool): RoCEv2 OpCode Error Count
        - RsFECCorrectedCodewordCount (bool): RS-FEC Corrected Codeword Count
        - RsFECCorrectedCodewordCountRate (bool): RS-FEC Corrected Codeword Count Rate
        - RsFECUncorrectedCodewordCount (bool): RS-FEC Uncorrected Codeword Count
        - RsFECUncorrectedCodewordCountRate (bool): RS-FEC Uncorrected Codeword Count Rate
        - Rx0FpgaTemperatureC (bool): Rx0 Fpga Temperature(C)
        - Rx1FpgaTemperatureC (bool): Rx1 Fpga Temperature(C)
        - RxBadPacketforBroadcastRate (bool): Rx Bad Packet for Broadcast Rate
        - RxBadPacketforMulticastRate (bool): Rx Bad Packet for Multicast Rate
        - RxBadTagPacketorICVDiscardedPacketforBroadcastRate (bool): Rx Bad Tag Packet or ICV Discarded Packet for Broadcast Rate
        - RxBadTagPacketorICVDiscardedPacketforMulticastRate (bool): Rx Bad Tag Packet or ICV Discarded Packet for Multicast Rate
        - RxBytesDecryptedBroadcast (bool): Rx Bytes Decrypted Broadcast
        - RxBytesDecryptedMulticast (bool): Rx Bytes Decrypted Multicast
        - RxBytesDecryptedforBroadcastRate (bool): Rx Bytes Decrypted for Broadcast Rate
        - RxBytesDecryptedforMulticastRate (bool): Rx Bytes Decrypted for Multicast Rate
        - RxBytesValidatedBroadcast (bool): Rx Bytes Validated Broadcast
        - RxBytesValidatedMulticast (bool): Rx Bytes Validated Multicast
        - RxBytesValidatedforBroadcastRate (bool): Rx Bytes Validated for Broadcast Rate
        - RxBytesValidatedforMulticastRate (bool): Rx Bytes Validated for Multicast Rate
        - RxEncryptedByteCountRate (bool): Rx Encrypted Byte Count Rate
        - RxEncryptedPacketCountRate (bool): Rx Encrypted Packet Count Rate
        - RxFPExpressCRCTypeErrorCount (bool): Rx FP Express CRC Type Error Count
        - RxFPExpressCRCTypeErrorCountRate (bool): Rx FP Express CRC Type Error Count Rate
        - RxFPFragCountError (bool): Rx FP Frag Count Error
        - RxFPFragCountErrorRate (bool): Rx FP Frag Count Error Rate
        - RxFPInvalidCRCTypeErrorCount (bool): Rx FP Invalid CRC Type Error Count
        - RxFPInvalidCRCTypeErrorCountRate (bool): Rx FP Invalid CRC Type Error Count Rate
        - RxFPReassemblyGoodCount (bool): Rx FP Reassembly Good Count
        - RxFPReassemblyGoodCountRate (bool): Rx FP Reassembly Good Count Rate
        - RxFPRespondmPacketCRCErrorCount (bool): Rx FP Respond mPacket CRC Error Count
        - RxFPRespondmPacketCRCErrorCountRate (bool): Rx FP Respond mPacket CRC Error Count Rate
        - RxFPRespondmPacketCount (bool): Rx FP Respond mPacket Count
        - RxFPRespondmPacketCountRate (bool): Rx FP Respond mPacket Count Rate
        - RxFPSMDC0mPacketCRCErrorCount (bool): Rx FP SMD-C0 mPacket CRC Error Count
        - RxFPSMDC0mPacketCRCErrorCountRate (bool): Rx FP SMD-C0 mPacket CRC Error Count Rate
        - RxFPSMDC0mPacketCount (bool): Rx FP SMD-C0 mPacket Count
        - RxFPSMDC0mPacketCountRate (bool): Rx FP SMD-C0 mPacket Count Rate
        - RxFPSMDC1mPacketCRCErrorCount (bool): Rx FP SMD-C1 mPacket CRC Error Count
        - RxFPSMDC1mPacketCRCErrorCountRate (bool): Rx FP SMD-C1 mPacket CRC Error Count Rate
        - RxFPSMDC1mPacketCount (bool): Rx FP SMD-C1 mPacket Count
        - RxFPSMDC1mPacketCountRate (bool): Rx FP SMD-C1 mPacket Count Rate
        - RxFPSMDC2mPacketCRCErrorCount (bool): Rx FP SMD-C2 mPacket CRC Error Count
        - RxFPSMDC2mPacketCRCErrorCountRate (bool): Rx FP SMD-C2 mPacket CRC Error Count Rate
        - RxFPSMDC2mPacketCount (bool): Rx FP SMD-C2 mPacket Count
        - RxFPSMDC2mPacketCountRate (bool): Rx FP SMD-C2 mPacket Count Rate
        - RxFPSMDC3mPacketCRCErrorCount (bool): Rx FP SMD-C3 mPacket CRC Error Count
        - RxFPSMDC3mPacketCRCErrorCountRate (bool): Rx FP SMD-C3 mPacket CRC Error Count Rate
        - RxFPSMDC3mPacketCount (bool): Rx FP SMD-C3 mPacket Count
        - RxFPSMDC3mPacketCountRate (bool): Rx FP SMD-C3 mPacket Count Rate
        - RxFPSMDCCRCCalcErrorCount (bool): Rx FP SMD-C CRC Calc Error Count
        - RxFPSMDCCRCCalcErrorCountRate (bool): Rx FP SMD-C CRC Calc Error Count Rate
        - RxFPSMDCFrameCountError (bool): Rx FP SMD-C Frame Count Error
        - RxFPSMDCFrameCountErrorRate (bool): Rx FP SMD-C Frame Count Error Rate
        - RxFPSMDCTerminationErrorCount (bool): Rx FP SMD-C Termination Error Count
        - RxFPSMDCTerminationErrorCountRate (bool): Rx FP SMD-C Termination Error Count Rate
        - RxFPSMDRNotTransmittedCount (bool): Rx FP SMD-R Not Transmitted Count
        - RxFPSMDRNotTransmittedCountRate (bool): Rx FP SMD-R Not Transmitted Count Rate
        - RxFPSMDS0mPacketCRCErrorCount (bool): Rx FP SMD-S0 mPacket CRC Error Count
        - RxFPSMDS0mPacketCRCErrorCountRate (bool): Rx FP SMD-S0 mPacket CRC Error Count Rate
        - RxFPSMDS0mPacketCount (bool): Rx FP SMD-S0 mPacket Count
        - RxFPSMDS0mPacketCountRate (bool): Rx FP SMD-S0 mPacket Count Rate
        - RxFPSMDS1mPacketCRCErrorCount (bool): Rx FP SMD-S1 mPacket CRC Error Count
        - RxFPSMDS1mPacketCRCErrorCountRate (bool): Rx FP SMD-S1 mPacket CRC Error Count Rate
        - RxFPSMDS1mPacketCount (bool): Rx FP SMD-S1 mPacket Count
        - RxFPSMDS1mPacketCountRate (bool): Rx FP SMD-S1 mPacket Count Rate
        - RxFPSMDS2mPacketCRCErrorCount (bool): Rx FP SMD-S2 mPacket CRC Error Count
        - RxFPSMDS2mPacketCRCErrorCountRate (bool): Rx FP SMD-S2 mPacket CRC Error Count Rate
        - RxFPSMDS2mPacketCount (bool): Rx FP SMD-S2 mPacket Count
        - RxFPSMDS2mPacketCountRate (bool): Rx FP SMD-S2 mPacket Count Rate
        - RxFPSMDS3mPacketCRCErrorCount (bool): Rx FP SMD-S3 mPacket CRC Error Count
        - RxFPSMDS3mPacketCRCErrorCountRate (bool): Rx FP SMD-S3 mPacket CRC Error Count Rate
        - RxFPSMDS3mPacketCount (bool): Rx FP SMD-S3 mPacket Count
        - RxFPSMDS3mPacketCountRate (bool): Rx FP SMD-S3 mPacket Count Rate
        - RxFPSMDSFrameCountError (bool): Rx FP SMD-S Frame Count Error
        - RxFPSMDSFrameCountErrorRate (bool): Rx FP SMD-S Frame Count Error Rate
        - RxFPSMDSStartProtocolError (bool): Rx FP SMD-S Start Protocol Error
        - RxFPSMDSStartProtocolErrorRate (bool): Rx FP SMD-S Start Protocol Error Rate
        - RxFPSMDSTerminationErrorCount (bool): Rx FP SMD-S Termination Error Count
        - RxFPSMDSTerminationErrorCountRate (bool): Rx FP SMD-S Termination Error Count Rate
        - RxFPSMDVNotReceivedCount (bool): Rx FP SMD-V Not Received Count
        - RxFPSMDVNotReceivedCountRate (bool): Rx FP SMD-V Not Received Count Rate
        - RxFPUnexpectedSMDRCount (bool): Rx FP Unexpected SMD-R Count
        - RxFPUnexpectedSMDRCountRate (bool): Rx FP Unexpected SMD-R Count Rate
        - RxFPVerifyProtocolError (bool): Rx FP Verify Protocol Error
        - RxFPVerifyProtocolErrorRate (bool): Rx FP Verify Protocol Error Rate
        - RxFPVerifymPacketCRCErrorCount (bool): Rx FP Verify mPacket CRC Error Count
        - RxFPVerifymPacketCRCErrorCountRate (bool): Rx FP Verify mPacket CRC Error Count Rate
        - RxFPVerifymPacketCount (bool): Rx FP Verify mPacket Count
        - RxFPVerifymPacketCountRate (bool): Rx FP Verify mPacket Count Rate
        - RxFpgaTemperatureC (bool): Rx Fpga Temperature(C)
        - RxInvalidICVDiscardedPacketforBroadcastRate (bool): Rx Invalid ICV Discarded Packet for Broadcast Rate
        - RxInvalidICVDiscardedPacketforMulticastRate (bool): Rx Invalid ICV Discarded Packet for Multicast Rate
        - RxInvalidICVPacketforBroadcastRate (bool): Rx Invalid ICV Packet for Broadcast Rate
        - RxInvalidICVPacketforMulticastRate (bool): Rx Invalid ICV Packet for Multicast Rate
        - RxNonMACsecPacketCountRate (bool): Rx NonMACsec Packet Count Rate
        - RxOpticalPowerHighAlarm (bool): Rx Optical Power High Alarm
        - RxOpticalPowerHighWarn (bool): Rx Optical Power High Warn
        - RxOpticalPowerLimitFlag (bool): Rx Optical Power Limit Flag
        - RxOpticalPowerLowAlarm (bool): Rx Optical Power Low Alarm
        - RxOpticalPowerLowWarn (bool): Rx Optical Power Low Warn
        - RxOutofWindowPacketorOutofWindowDiscardedPacketforBroadcastRate (bool): Rx Out of Window Packet or Out of Window Discarded Packet for Broadcast Rate
        - RxOutofWindowPacketorOutofWindowDiscardedPacketforMulticastRate (bool): Rx Out of Window Packet or Out of Window Discarded Packet for Multicast Rate
        - RxPausePriorityGroup0Frames (bool): Rx Pause Priority Group 0 Frames
        - RxPausePriorityGroup0FramesRate (bool): Rx Pause Priority Group 0 Frames Rate
        - RxPausePriorityGroup1Frames (bool): Rx Pause Priority Group 1 Frames
        - RxPausePriorityGroup1FramesRate (bool): Rx Pause Priority Group 1 Frames Rate
        - RxPausePriorityGroup2Frames (bool): Rx Pause Priority Group 2 Frames
        - RxPausePriorityGroup2FramesRate (bool): Rx Pause Priority Group 2 Frames Rate
        - RxPausePriorityGroup3Frames (bool): Rx Pause Priority Group 3 Frames
        - RxPausePriorityGroup3FramesRate (bool): Rx Pause Priority Group 3 Frames Rate
        - RxPausePriorityGroup4Frames (bool): Rx Pause Priority Group 4 Frames
        - RxPausePriorityGroup4FramesRate (bool): Rx Pause Priority Group 4 Frames Rate
        - RxPausePriorityGroup5Frames (bool): Rx Pause Priority Group 5 Frames
        - RxPausePriorityGroup5FramesRate (bool): Rx Pause Priority Group 5 Frames Rate
        - RxPausePriorityGroup6Frames (bool): Rx Pause Priority Group 6 Frames
        - RxPausePriorityGroup6FramesRate (bool): Rx Pause Priority Group 6 Frames Rate
        - RxPausePriorityGroup7Frames (bool): Rx Pause Priority Group 7 Frames
        - RxPausePriorityGroup7FramesRate (bool): Rx Pause Priority Group 7 Frames Rate
        - RxProtectedByteCountRate (bool): Rx Protected Byte Count Rate
        - RxProtectedPacketCountRate (bool): Rx Protected Packet Count Rate
        - RxRateKbps (bool): Rx. Rate (Kbps)
        - RxRateMbps (bool): Rx. Rate (Mbps)
        - RxRatebps (bool): Rx. Rate (bps)
        - RxRoCEACKFrameCount (bool): Rx RoCE ACK Frame Count
        - RxRoCEACKFrameCountRate (bool): Rx RoCE ACK Frame Count Rate
        - RxRoCECNPFrameCount (bool): Rx RoCE CNP Frame Count
        - RxRoCECNPFrameCountRate (bool): Rx RoCE CNP Frame Count Rate
        - RxRoCEECNFrameCount (bool): Rx RoCE ECN Frame Count
        - RxRoCEECNFrameCountRate (bool): Rx RoCE ECN Frame Count Rate
        - RxRoCENAKFrameCount (bool): Rx RoCE NAK Frame Count
        - RxRoCENAKFrameCountRate (bool): Rx RoCE NAK Frame Count Rate
        - RxRoCEOpcodeErrorCountRate (bool): Rx RoCE Opcode Error Count Rate
        - RxRoCEPrePFCCNPFrameCount (bool): Rx RoCE Pre-PFC CNP Frame Count
        - RxRoCEPrePFCCNPFrameCountRate (bool): Rx RoCE Pre-PFC CNP Frame Count Rate
        - RxRoCEiCRCErrorCountRate (bool): Rx RoCE iCRC Error Count Rate
        - RxSharedStat1 (bool): Rx Shared Stat 1
        - RxSharedStat1Rate (bool): Rx Shared Stat 1 Rate
        - RxSharedStat2 (bool): Rx Shared Stat 2
        - RxSharedStat2Rate (bool): Rx Shared Stat 2 Rate
        - RxUnknownSCIDiscardedPacketorUnusedSADiscardedPacketRate (bool): Rx Unknown SCI Discarded Packet or Unused SA Discarded Packet Rate
        - RxUnknownSCIPacketorUnusedSAPacketRate (bool): Rx Unknown SCI Packet or Unused SA Packet Rate
        - RxUnvalidatedPacketCountRate (bool): Rx Unvalidated Packet Count Rate
        - RxValidPacketforBroadcastRate (bool): Rx Valid Packet for Broadcast Rate
        - RxValidPacketforMulticastRate (bool): Rx Valid Packet for Multicast Rate
        - ScheduledCellsTx (bool): Scheduled Cells Tx.
        - ScheduledCellsTxRate (bool): Scheduled Cells Tx. Rate
        - ScheduledFramesTx (bool): Scheduled Frames Tx.
        - ScheduledFramesTxRate (bool): Scheduled Frames Tx. Rate
        - ScheduledTransmitDuration (bool): Scheduled Transmit Duration
        - ScheduledTxRoCEACKFrameCount (bool): Scheduled Tx RoCE ACK Frame Count
        - ScheduledTxRoCEACKFrameCountRate (bool): Scheduled Tx RoCE ACK Frame Count Rate
        - ScheduledTxRoCECNPFrameCount (bool): Scheduled Tx RoCE CNP Frame Count
        - ScheduledTxRoCECNPFrameCountRate (bool): Scheduled Tx RoCE CNP Frame Count Rate
        - ScheduledTxRoCENAKFrameCount (bool): Scheduled Tx RoCE NAK Frame Count
        - ScheduledTxRoCENAKFrameCountRate (bool): Scheduled Tx RoCE NAK Frame Count Rate
        - SchedulerChipTemperatureC (bool): Scheduler Chip Temperature(C)
        - SectionBIPB1 (bool): Section BIP (B1)
        - SectionBIPB1Rate (bool): Section BIP (B1) Rate
        - SectionBIPErroredSeconds (bool): Section BIP Errored Seconds
        - SectionBIPSeverelyErroredSeconds (bool): Section BIP Severely Errored Seconds
        - SectionLOF (bool): Section LOF
        - SectionLOS (bool): Section LOS
        - SectionLOSSeconds (bool): Section LOS Seconds
        - SequenceErrors (bool): Sequence Errors
        - SequenceErrorsRate (bool): Sequence Errors Rate
        - SequenceFrames (bool): Sequence Frames
        - SequenceFramesRate (bool): Sequence Frames Rate
        - SeverelyErroredSeconds (bool): Severely Errored Seconds
        - SofBigErrorFrameCount (bool): SOF Big Error Frame Count
        - SofEarlyFrameCount (bool): SOF Early Frame Count
        - SofEarlyMaximumByteCount (bool): SOF Early Maximum Byte Count
        - SofEarlyMinimumByteCount (bool): SOF Early Minimum Byte Count
        - StatelessBitsReceived (bool): Stateless Bits Received
        - StatelessBitsSent (bool): Stateless Bits Sent
        - StatelessBytesReceived (bool): Stateless Bytes Received
        - StatelessBytesReceivedRate (bool): Stateless Bytes Received Rate
        - StatelessBytesRxRate (bool): Stateless Bytes Rx. Rate
        - StatelessBytesSent (bool): Stateless Bytes Sent
        - StatelessBytesSentRate (bool): Stateless Bytes Sent Rate
        - StatelessBytesTxRate (bool): Stateless Bytes Tx. Rate
        - StatelessFramesSent (bool): Stateless Frames Sent
        - StatelessFramesSentRate (bool): Stateless Frames Sent Rate
        - StatelessRxRateKbps (bool): Stateless Rx. Rate (Kbps)
        - StatelessRxRateMbps (bool): Stateless Rx. Rate (Mbps)
        - StatelessRxRatebps (bool): Stateless Rx. Rate (bps)
        - StatelessTxRateKbps (bool): Stateless Tx. Rate (Kbps)
        - StatelessTxRateMbps (bool): Stateless Tx. Rate (Mbps)
        - StatelessTxRatebps (bool): Stateless Tx. Rate (bps)
        - Status (bool): Status
        - SupplyVoltageHighAlarm (bool): Supply Voltage High Alarm
        - SupplyVoltageHighWarn (bool): Supply Voltage High Warn
        - SupplyVoltageLimitFlag (bool): Supply Voltage Limit Flag
        - SupplyVoltageLowAlarm (bool): Supply Voltage Low Alarm
        - SupplyVoltageLowWarn (bool): Supply Voltage Low Warn
        - TcpChecksumErrors (bool): TCP Checksum Errors
        - TcpChecksumErrorsRate (bool): TCP Checksum Errors Rate
        - TcpPacketsReceived (bool): TCP Packets Received
        - TcpPacketsReceivedRate (bool): TCP Packets Received Rate
        - TemperatureHighAlarm (bool): Temperature High Alarm
        - TemperatureHighWarn (bool): Temperature High Warn
        - TemperatureLimitFlag (bool): Temperature Limit Flag
        - TemperatureLowAlarm (bool): Temperature Low Alarm
        - TemperatureLowWarn (bool): Temperature Low Warn
        - TotalMemory (bool): Total Memory
        - TransceiverTemperatureC (bool): Transceiver Temperature (C)
        - TransmitArpGratuitous (bool): Transmit Arp Gratuitous
        - TransmitArpGratuitousRate (bool): Transmit Arp Gratuitous Rate
        - TransmitArpReply (bool): Transmit Arp Reply
        - TransmitArpRequest (bool): Transmit Arp Request
        - TransmitArpReverse (bool): Transmit Arp Reverse
        - TransmitArpReverseRate (bool): Transmit Arp Reverse Rate
        - TransmitDurationClearedonStartTx (bool): Transmit Duration(Cleared on Start Tx)
        - TransmitNeighborAdvertisements (bool): Transmit Neighbor Advertisements
        - TransmitNeighborSolicitation (bool): Transmit Neighbor Solicitation
        - TransmitPingReply (bool): Transmit Ping Reply
        - TransmitPingRequest (bool): Transmit Ping Request
        - Tx0FpgaTemperatureC (bool): Tx0 Fpga Temperature(C)
        - TxBiasCurrentHighAlarm (bool): Tx Bias Current High Alarm
        - TxBiasCurrentHighWarn (bool): Tx Bias Current High Warn
        - TxBiasCurrentLimitFlag (bool): Tx Bias Current Limit Flag
        - TxBiasCurrentLowAlarm (bool): Tx Bias Current Low Alarm
        - TxBiasCurrentLowWarn (bool): Tx Bias Current Low Warn
        - TxEncryptedByteCountRate (bool): Tx Encrypted Byte Count Rate
        - TxEncryptedPacketCountRate (bool): Tx Encrypted Packet Count Rate
        - TxFpgaTemperatureC (bool): Tx Fpga Temperature(C)
        - TxNonMACsecPacketCountRate (bool): Tx NonMACsec Packet Count Rate
        - TxOpticalPowerHighAlarm (bool): Tx Optical Power High Alarm
        - TxOpticalPowerHighWarn (bool): Tx Optical Power High Warn
        - TxOpticalPowerLimitFlag (bool): Tx Optical Power Limit Flag
        - TxOpticalPowerLowAlarm (bool): Tx Optical Power Low Alarm
        - TxOpticalPowerLowWarn (bool): Tx Optical Power Low Warn
        - TxProtectedByteCountRate (bool): Tx Protected Byte Count Rate
        - TxProtectedPacketCountRate (bool): Tx Protected Packet Count Rate
        - TxRateKbps (bool): Tx. Rate (Kbps)
        - TxRateMbps (bool): Tx. Rate (Mbps)
        - TxRatebps (bool): Tx. Rate (bps)
        - UdpChecksumErrors (bool): UDP Checksum Errors
        - UdpChecksumErrorsRate (bool): UDP Checksum Errors Rate
        - UdpPacketsReceived (bool): UDP Packets Received
        - UdpPacketsReceivedRate (bool): UDP Packets Received Rate
        - UnavailableSeconds (bool): Unavailable Seconds
        - UncorrectedHCSErrorCount (bool): Uncorrected HCS Error Count
        - UncorrectedHCSErrorCountRate (bool): Uncorrected HCS Error Count Rate
        - Undersize (bool): Undersize
        - UndersizeRate (bool): Undersize Rate
        - UnexpectedPLCABeaconReceived (bool): Unexpected PLCA Beacon Received
        - UnknownSCISAAccepted (bool): Unknown SCI/SA Accepted
        - UnknownSCISADiscarded (bool): Unknown SCI/SA Discarded
        - UnvalidatedPacketRx (bool): Unvalidated Packet Rx
        - UserDefinedStat1 (bool): User Defined Stat 1
        - UserDefinedStat1Rate (bool): User Defined Stat 1 Rate
        - UserDefinedStat2 (bool): User Defined Stat 2
        - UserDefinedStat2Rate (bool): User Defined Stat 2 Rate
        - UserDefinedStat5 (bool): User Defined Stat 5
        - UserDefinedStat5Rate (bool): User Defined Stat 5 Rate
        - UserDefinedStat6 (bool): User Defined Stat 6
        - UserDefinedStat6Rate (bool): User Defined Stat 6 Rate
        - UserDefinedStatByteCount1 (bool): User Defined Stat Byte Count 1
        - UserDefinedStatByteCount1Rate (bool): User Defined Stat Byte Count 1 Rate
        - UserDefinedStatByteCount2 (bool): User Defined Stat Byte Count 2
        - UserDefinedStatByteCount2Rate (bool): User Defined Stat Byte Count 2 Rate
        - ValidFramesRx (bool): Valid Frames Rx.
        - ValidFramesRxRate (bool): Valid Frames Rx. Rate
        - ValidPacketRxBroadcast (bool): Valid Packet Rx Broadcast
        - ValidPacketRxMulticast (bool): Valid Packet Rx Multicast
        - ValidStatelessFramesReceived (bool): Valid Stateless Frames Received
        - ValidStatelessFramesReceivedRate (bool): Valid Stateless Frames Received Rate
        - VlanTaggedFrames (bool): Vlan Tagged Frames
        - VlanTaggedFramesRate (bool): Vlan Tagged Frames Rate
        - WindowClosedFrameCount (bool): Window Closed Frame Count
        - WindowValidFrameCount (bool): Window Valid Frame Count
        - WindowViolationFrameCount (bool): Window Violation Frame Count

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, **kwargs):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> PortStatistics
        """Finds and retrieves portStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve portStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all portStatistics resources from the server.

        Args
        ----
        - Aal5FramesRx (bool): AAL5 Frames Rx.
        - Aal5FramesRxRate (bool): AAL5 Frames Rx. Rate
        - Aal5FramesTx (bool): AAL5 Frames Tx.
        - Aal5FramesTxRate (bool): AAL5 Frames Tx. Rate
        - Aal5PayloadBytesRx (bool): AAL5 Payload Bytes Rx.
        - Aal5PayloadBytesRxRate (bool): AAL5 Payload Bytes Rx. Rate
        - Aal5PayloadBytesTx (bool): AAL5 Payload Bytes Tx.
        - Aal5PayloadBytesTxRate (bool): AAL5 Payload Bytes Tx. Rate
        - ActiveFECMode (bool): Active FEC Mode
        - AlignmentErrors (bool): Alignment Errors
        - AlignmentErrorsRate (bool): Alignment Errors Rate
        - AsynchronousFramesSent (bool): Asynchronous Frames Sent
        - AsynchronousFramesSentRate (bool): Asynchronous Frames Sent Rate
        - AtmCellsRx (bool): ATM Cells Rx.
        - AtmCellsRxRate (bool): ATM Cells Rx. Rate
        - AtmCellsTx (bool): ATM Cells Tx.
        - AtmCellsTxRate (bool): ATM Cells Tx. Rate
        - AtmUnregisteredCellsRx (bool): ATM Unregistered Cells Rx.
        - AtmUnregisteredCellsRxRate (bool): ATM Unregistered Cells Rx. Rate
        - AvailableSeconds (bool): Available Seconds
        - BackgroundBlockErrors (bool): Background Block Errors
        - BackgroundBlockErrorsRate (bool): Background Block Errors Rate
        - BackgroundChipTemperatureC (bool): Background Chip Temperature(C)
        - BadPacketRxBroadcast (bool): Bad Packet Rx Broadcast
        - BadPacketRxMulticast (bool): Bad Packet Rx Multicast
        - BadTagICVDiscardedBroadcast (bool): Bad Tag/ICV Discarded Broadcast
        - BadTagICVDiscardedMulticast (bool): Bad Tag/ICV Discarded Multicast
        - BertBitsReceived (bool): BERT Bits Received
        - BertBitsSent (bool): BERT Bits Sent
        - BitErrorsReceived (bool): Bit Errors Received
        - BitErrorsSent (bool): Bit Errors Sent
        - BitsReceived (bool): Bits Received
        - BitsReceivedRate (bool): Bits Received Rate
        - BitsSent (bool): Bits Sent
        - BitsSentRate (bool): Bits Sent Rate
        - BlockErrorState (bool): Block Error State
        - ByteAlignmentError (bool): Byte Alignment Error
        - ByteAlignmentErrorRate (bool): Byte Alignment Error Rate
        - BytesRx (bool): Bytes Rx.
        - BytesRxRate (bool): Bytes Rx. Rate
        - BytesSentTransmitDuration (bool): Bytes Sent / Transmit Duration
        - BytesTx (bool): Bytes Tx.
        - BytesTxRate (bool): Bytes Tx. Rate
        - CaptureChipTemperatureC (bool): Capture Chip Temperature(C)
        - CaptureFilterUDS4 (bool): Capture Filter (UDS 4)
        - CaptureFilterUDS4Rate (bool): Capture Filter (UDS 4) Rate
        - CaptureTriggerUDS3 (bool): Capture Trigger (UDS 3)
        - CaptureTriggerUDS3Rate (bool): Capture Trigger (UDS 3) Rate
        - CentralChipTemperatureC (bool): Central Chip Temperature(C)
        - CodeError (bool): Code Error
        - CodeErrorRate (bool): Code Error Rate
        - CollisionFrames (bool): Collision Frames
        - CollisionFramesRate (bool): Collision Frames Rate
        - Collisions (bool): Collisions
        - CollisionsRate (bool): Collisions Rate
        - ControlFramesRx (bool): Control Frames Rx
        - ControlFramesTx (bool): Control Frames Tx
        - CorrectedHCSErrorCount (bool): Corrected HCS Error Count
        - CorrectedHCSErrorCountRate (bool): Corrected HCS Error Count Rate
        - CpuIdle (bool): CPU Idle
        - CpuLoadAvg15Minutes (bool): CPU Load Avg (15 Minutes)
        - CpuLoadAvg1Minute (bool): CPU Load Avg (1 Minute)
        - CpuLoadAvg5Minutes (bool): CPU Load Avg (5 Minutes)
        - CpuRxFrameSize1024to2047 (bool): CPU Rx Frame Size 1024 to 2047
        - CpuRxFrameSize128to255 (bool): CPU Rx Frame Size 128 to 255
        - CpuRxFrameSize2048to4095 (bool): CPU Rx Frame Size 2048 to 4095
        - CpuRxFrameSize256to511 (bool): CPU Rx Frame Size 256 to 511
        - CpuRxFrameSize4096andabove (bool): CPU Rx Frame Size 4096 and above
        - CpuRxFrameSize512to1023 (bool): CPU Rx Frame Size 512 to 1023
        - CpuRxFrameSize64to127 (bool): CPU Rx Frame Size 64 to 127
        - CpuRxFrameSizelessthan64 (bool): CPU Rx Frame Size less than 64
        - CpuTxFrameSize1024to2047 (bool): CPU Tx Frame Size 1024 to 2047
        - CpuTxFrameSize128to255 (bool): CPU Tx Frame Size 128 to 255
        - CpuTxFrameSize2048to4095 (bool): CPU Tx Frame Size 2048 to 4095
        - CpuTxFrameSize256to511 (bool): CPU Tx Frame Size 256 to 511
        - CpuTxFrameSize4096andabove (bool): CPU Tx Frame Size 4096 and above
        - CpuTxFrameSize512to1023 (bool): CPU Tx Frame Size 512 to 1023
        - CpuTxFrameSize64to127 (bool): CPU Tx Frame Size 64 to 127
        - CpuTxFrameSizelessthan64 (bool): CPU Tx Frame Size less than 64
        - CrcErrors (bool): CRC Errors
        - CrcErrorsRate (bool): CRC Errors Rate
        - CumulativeServiceDisruptionTimems (bool): Cumulative Service Disruption Time (ms)
        - CumulativeServiceDisruptionTimemsRate (bool): Cumulative Service Disruption Time (ms) Rate
        - CustomOrderedSetsReceived (bool): Custom Ordered Sets Received
        - CustomOrderedSetsReceivedRate (bool): Custom Ordered Sets Received Rate
        - CustomOrderedSetsSent (bool): Custom Ordered Sets Sent
        - CustomOrderedSetsSentRate (bool): Custom Ordered Sets Sent Rate
        - DataIntegrityErrors (bool): Data Integrity Errors
        - DataIntegrityErrorsRate (bool): Data Integrity Errors Rate
        - DataIntegrityFramesRate (bool): Data Integrity Frames Rate
        - DataIntegrityFramesRx (bool): Data Integrity Frames Rx.
        - DeskewBitErrorsReceived (bool): Deskew Bit Errors Received
        - DeskewBitErrorsReceivedRate (bool): Deskew Bit Errors Received Rate
        - DeskewBitErrorsSent (bool): Deskew Bit Errors Sent
        - DeskewBitErrorsSentRate (bool): Deskew Bit Errors Sent Rate
        - DeskewErrorFreeFramesReceived (bool): Deskew Error Free Frames Received
        - DeskewErrorFreeFramesReceivedRate (bool): Deskew Error Free Frames Received Rate
        - DeskewErrorFreeFramesSent (bool): Deskew Error Free Frames Sent
        - DeskewErrorFreeFramesSentRate (bool): Deskew Error Free Frames Sent Rate
        - DeskewErroredFramesReceived (bool): Deskew Errored Frames Received
        - DeskewErroredFramesReceivedRate (bool): Deskew Errored Frames Received Rate
        - DeskewErroredFramesSent (bool): Deskew Errored Frames Sent
        - DeskewErroredFramesSentRate (bool): Deskew Errored Frames Sent Rate
        - DeskewLossOfFrame (bool): Deskew Loss Of Frame
        - DeskewLossOfFrameRate (bool): Deskew Loss Of Frame Rate
        - Dhcpv4ACKsReceived (bool): DHCPv4 ACKs Received
        - Dhcpv4AddressesLearned (bool): DHCPv4 Addresses Learned
        - Dhcpv4DiscoveredMessagesSent (bool): DHCPv4 Discovered Messages Sent
        - Dhcpv4EnabledInterfaces (bool): DHCPv4 Enabled Interfaces
        - Dhcpv4NACKsReceived (bool): DHCPv4 NACKs Received
        - Dhcpv4OffersReceived (bool): DHCPv4 Offers Received
        - Dhcpv4ReleasesSent (bool): DHCPv4 Releases Sent
        - Dhcpv4RequestsSent (bool): DHCPv4 Requests Sent
        - DisparityErrors (bool): Disparity Errors
        - DisparityErrorsRate (bool): Disparity Errors Rate
        - DmaChipTemperatureC (bool): DMA Chip Temperature(C)
        - DribbleErrors (bool): Dribble Errors
        - DribbleErrorsRate (bool): Dribble Errors Rate
        - DroppedFrames (bool): Dropped Frames
        - DroppedFramesRate (bool): Dropped Frames Rate
        - DuplexMode (bool): Duplex Mode
        - ElapsedTestTime (bool): Elapsed Test Time
        - ElapsedTestTimeRate (bool): Elapsed Test Time Rate
        - Encoding (bool): Encoding
        - EncryptedByteRx (bool): Encrypted Byte Rx
        - EncryptedByteTx (bool): Encrypted Byte Tx
        - EncryptedPacketRx (bool): Encrypted Packet Rx
        - EncryptedPacketTx (bool): Encrypted Packet Tx
        - EndofStreamDelimiterError (bool): End-of-Stream Delimiter Error
        - EofBigErrorFrameCount (bool): EOF Big Error Frame Count
        - EofLateFrameCount (bool): EOF Late Frame Count
        - EofLateMaximumByteCount (bool): EOF Late Maximum Byte Count
        - EofLateMinimumByteCount (bool): EOF Late Minimum Byte Count
        - ErrorFreeSeconds (bool): Error Free Seconds
        - ErroredBlocks (bool): Errored Blocks
        - ErroredBlocksRate (bool): Errored Blocks Rate
        - ErroredSeconds (bool): Errored Seconds
        - EthernetCRC (bool): Ethernet CRC
        - EthernetCRCRate (bool): Ethernet CRC Rate
        - EthernetOAMEventNotificationPDUsReceived (bool): Ethernet OAM Event Notification PDUs Received
        - EthernetOAMInformationPDUsReceived (bool): Ethernet OAM Information PDUs Received
        - EthernetOAMInformationPDUsSent (bool): Ethernet OAM Information PDUs Sent
        - EthernetOAMLoopbackControlPDUsReceived (bool): Ethernet OAM Loopback Control PDUs Received
        - EthernetOAMOrganisationPDUsReceived (bool): Ethernet OAM Organisation PDUs Received
        - EthernetOAMUnsupportedPDUsReceived (bool): Ethernet OAM Unsupported PDUs Received
        - EthernetOAMVariableRequestPDUsReceived (bool): Ethernet OAM Variable Request PDUs Received
        - EthernetOAMVariableResponseReceived (bool): Ethernet OAM Variable Response Received
        - ExcessiveCollisionFrames (bool): Excessive Collision Frames
        - ExcessiveCollisionFramesRate (bool): Excessive Collision Frames Rate
        - FcFECCorrectedBlockCount (bool): FC-FEC Corrected Block Count
        - FcFECCorrectedBlockCountRate (bool): FC-FEC Corrected Block Count Rate
        - FcFECCorrectedErrorBits (bool): FC-FEC Corrected Error Bits
        - FcFECCorrectedErrorBitsRate (bool): FC-FEC Corrected Error Bits Rate
        - FcFECUncorrectedBlockCount (bool): FC-FEC Uncorrected Block Count
        - FcFECUncorrectedBlockCountRate (bool): FC-FEC Uncorrected Block Count Rate
        - FdiscSent (bool): Fdisc Sent
        - FdiscSuccessful (bool): Fdisc Successful
        - FecCodewordswith0errors (bool): FEC Codewords with 0 errors
        - FecCodewordswith0errorsRate (bool): FEC Codewords with 0 errors Rate
        - FecCodewordswith10errors (bool): FEC Codewords with 10 errors
        - FecCodewordswith10errorsRate (bool): FEC Codewords with 10 errors Rate
        - FecCodewordswith11errors (bool): FEC Codewords with 11 errors
        - FecCodewordswith11errorsRate (bool): FEC Codewords with 11 errors Rate
        - FecCodewordswith12errors (bool): FEC Codewords with 12 errors
        - FecCodewordswith12errorsRate (bool): FEC Codewords with 12 errors Rate
        - FecCodewordswith13errors (bool): FEC Codewords with 13 errors
        - FecCodewordswith13errorsRate (bool): FEC Codewords with 13 errors Rate
        - FecCodewordswith14errors (bool): FEC Codewords with 14 errors
        - FecCodewordswith14errorsRate (bool): FEC Codewords with 14 errors Rate
        - FecCodewordswith15errors (bool): FEC Codewords with 15 errors
        - FecCodewordswith15errorsRate (bool): FEC Codewords with 15 errors Rate
        - FecCodewordswith1error (bool): FEC Codewords with 1 error
        - FecCodewordswith1errorRate (bool): FEC Codewords with 1 error Rate
        - FecCodewordswith2errors (bool): FEC Codewords with 2 errors
        - FecCodewordswith2errorsRate (bool): FEC Codewords with 2 errors Rate
        - FecCodewordswith3errors (bool): FEC Codewords with 3 errors
        - FecCodewordswith3errorsRate (bool): FEC Codewords with 3 errors Rate
        - FecCodewordswith4errors (bool): FEC Codewords with 4 errors
        - FecCodewordswith4errorsRate (bool): FEC Codewords with 4 errors Rate
        - FecCodewordswith5errors (bool): FEC Codewords with 5 errors
        - FecCodewordswith5errorsRate (bool): FEC Codewords with 5 errors Rate
        - FecCodewordswith6errors (bool): FEC Codewords with 6 errors
        - FecCodewordswith6errorsRate (bool): FEC Codewords with 6 errors Rate
        - FecCodewordswith7errors (bool): FEC Codewords with 7 errors
        - FecCodewordswith7errorsRate (bool): FEC Codewords with 7 errors Rate
        - FecCodewordswith8errors (bool): FEC Codewords with 8 errors
        - FecCodewordswith8errorsRate (bool): FEC Codewords with 8 errors Rate
        - FecCodewordswith9errors (bool): FEC Codewords with 9 errors
        - FecCodewordswith9errorsRate (bool): FEC Codewords with 9 errors Rate
        - FecCorrected0sCount (bool): FEC Corrected 0s Count
        - FecCorrected0sCountRate (bool): FEC Corrected 0s Count Rate
        - FecCorrected1sCount (bool): FEC Corrected 1s Count
        - FecCorrected1sCountRate (bool): FEC Corrected 1s Count Rate
        - FecCorrectedBitsCount (bool): FEC Corrected Bits Count
        - FecCorrectedBitsCountRate (bool): FEC Corrected Bits Count Rate
        - FecCorrectedBytesCount (bool): FEC Corrected Bytes Count
        - FecCorrectedBytesCountRate (bool): FEC Corrected Bytes Count Rate
        - FecCorrectedCodewords (bool): FEC Corrected Codewords
        - FecCorrectedCodewordsRate (bool): FEC Corrected Codewords Rate
        - FecFrameLossRatio (bool): FEC Frame Loss Ratio
        - FecMaxSymbolErrors (bool): FEC Max Symbol Errors
        - FecTotalBitErrors (bool): FEC Total Bit Errors
        - FecTotalBitErrorsRate (bool): FEC Total Bit Errors Rate
        - FecTotalCodewords (bool): FEC Total Codewords
        - FecTotalCodewordsRate (bool): FEC Total Codewords Rate
        - FecTranscodingUncorrectableEvents (bool): FEC Transcoding Uncorrectable Events
        - FecTranscodingUncorrectableEventsRate (bool): FEC Transcoding Uncorrectable Events Rate
        - FecUncorrectableCodewords (bool): FEC Uncorrectable Codewords
        - FecUncorrectableCodewordsRate (bool): FEC Uncorrectable Codewords Rate
        - FecUncorrectableSubrowCount (bool): FEC Uncorrectable Subrow Count
        - FecUncorrectableSubrowCountRate (bool): FEC Uncorrectable Subrow Count Rate
        - FirecodeFECSync (bool): Fire code FEC Sync
        - FivebDecodeError (bool): 5B Decode Error
        - FlogiSent (bool): Flogi Sent
        - FlogiSuccessful (bool): Flogi Successful
        - FlogoSent (bool): Flogo Sent
        - FlowControlFrames (bool): Flow Control Frames
        - FlowControlFramesRate (bool): Flow Control Frames Rate
        - FomBoardTemperatureC (bool): Fom Board Temperature(C)
        - FomInternalTemperatureC (bool): Fom Internal Temperature(C)
        - FomPortTemperatureC (bool): Fom Port Temperature(C)
        - Fragments (bool): Fragments
        - FragmentsRate (bool): Fragments Rate
        - FramerAbort (bool): Framer Abort
        - FramerAbortRate (bool): Framer Abort Rate
        - FramerMaxLength (bool): Framer Max Length
        - FramerMaxLengthRate (bool): Framer Max Length Rate
        - FramerMinLength (bool): Framer Min Length
        - FramerMinLengthRate (bool): Framer Min Length Rate
        - FramesReceivedwithCodingErrors (bool): Frames Received with Coding Errors
        - FramesReceivedwithCodingErrorsRate (bool): Frames Received with Coding Errors Rate
        - FramesReceivedwithEerrorCharacter (bool): Frames Received with /E/ error Character
        - FramesReceivedwithEerrorCharacterRate (bool): Frames Received with /E/ error Character Rate
        - FramesTx (bool): Frames Tx.
        - FramesTxRate (bool): Frames Tx. Rate
        - FreeMemory (bool): Free Memory
        - FrontendChipTemperatureC (bool): FrontEnd Chip Temperature(C)
        - HostConfigStatus (bool): Host Config Status
        - HostDataPathState (bool): Host Data Path State
        - HostLaneCount (bool): Host Lane Count
        - HostToMediaLane (bool): Host To Media Lane
        - HostTxCDRLOL (bool): Host Tx CDR LOL
        - HostTxLOS (bool): Host Tx LOS
        - IdleCellsRx (bool): Idle Cells Rx.
        - IdleCellsRxRate (bool): Idle Cells Rx. Rate
        - InputSignalStrengthdBm (bool): Input Signal Strength (dBm)
        - InsertionState (bool): Insertion State
        - InvalidEOF (bool): Invalid EOF
        - InvalidEOFRate (bool): Invalid EOF Rate
        - InvalidICVAcceptedBroadcast (bool): Invalid ICV Accepted Broadcast
        - InvalidICVAcceptedMulticast (bool): Invalid ICV Accepted Multicast
        - InvalidICVDiscardedBroadcast (bool): Invalid ICV Discarded Broadcast
        - InvalidICVDiscardedMulticast (bool): Invalid ICV Discarded Multicast
        - Ipv4ChecksumErrors (bool): IPv4 Checksum Errors
        - Ipv4ChecksumErrorsRate (bool): IPv4 Checksum Errors Rate
        - Ipv4PacketsReceived (bool): IPv4 Packets Received
        - Ipv4PacketsReceivedRate (bool): IPv4 Packets Received Rate
        - KernelTimestamp (bool): Kernel Timestamp
        - L1BitsReceived (bool): L1 Bits Received
        - L1BitsReceivedRate (bool): L1 Bits Received Rate
        - L1BitsSent (bool): L1 Bits Sent
        - L1BitsSentRate (bool): L1 Bits Sent Rate
        - L1LineRateReceivePercent (bool): L1 Line Rate Receive (%)
        - L1LineRateTransmitPercent (bool): L1 Line Rate Transmit (%)
        - LastServiceDisruptionTimems (bool): Last Service Disruption Time (ms)
        - LateCollisions (bool): Late Collisions
        - LateCollisionsRate (bool): Late Collisions Rate
        - LatencyChipTemperatureC (bool): Latency Chip Temperature(C)
        - LineAIS (bool): Line AIS
        - LineAISAlarmedSeconds (bool): Line AIS Alarmed Seconds
        - LineBIPB2 (bool): Line BIP (B2)
        - LineBIPB2Rate (bool): Line BIP (B2) Rate
        - LineBIPErroredSeconds (bool): Line BIP Errored Seconds
        - LineErrorFrames (bool): Line Error Frames
        - LineErrorFramesRate (bool): Line Error Frames Rate
        - LineErrors (bool): Line Errors
        - LineErrorsRate (bool): Line Errors Rate
        - LineRDI (bool): Line RDI
        - LineRDIUnavailableSeconds (bool): Line RDI Unavailable Seconds
        - LineREIErroredSeconds (bool): Line REI Errored Seconds
        - LineREIFEBE (bool): Line REI (FEBE)
        - LineREIFEBERate (bool): Line REI (FEBE) Rate
        - LineSpeed (bool): Line Speed
        - LinkFaultState (bool): Link Fault State
        - LinkState (bool): Link State
        - LocalFaults (bool): Local Faults
        - LocalOrderedSetsReceived (bool): Local Ordered Sets Received
        - LocalOrderedSetsReceivedRate (bool): Local Ordered Sets Received Rate
        - LocalOrderedSetsSent (bool): Local Ordered Sets Sent
        - LocalOrderedSetsSentRate (bool): Local Ordered Sets Sent Rate
        - MaxServiceDisruptionTimems (bool): Max Service Disruption Time (ms)
        - MediaLaneCount (bool): Media Lane Count
        - MediaRxCDRLOL (bool): Media Rx CDR LOL
        - MediaRxLOS (bool): Media Rx LOS
        - MediaRxOpticalPower (bool): Media Rx Optical Power
        - MediaTxBiasCurrent (bool): Media Tx Bias Current
        - MediaTxOpticalPower (bool): Media Tx Optical Power
        - MinServiceDisruptionTimems (bool): Min Service Disruption Time (ms)
        - MisdirectedPacketCount (bool): Misdirected Packet Count
        - MisdirectedPacketCountRate (bool): Misdirected Packet Count Rate
        - NonMACsecPacketRx (bool): Non-MACsec Packet Rx
        - NonMACsecPacketTx (bool): Non-MACsec Packet Tx
        - NportidsAcquired (bool): NPortIds Acquired
        - NportsEnabled (bool): NPorts Enabled
        - NsRegSent (bool): NS Reg Sent
        - NsRegSuccessful (bool): NS Reg Successful
        - NumberofMismatched0s (bool): Number of Mismatched 0's
        - NumberofMismatched0sRate (bool): Number of Mismatched 0's Rate
        - NumberofMismatched1s (bool): Number of Mismatched 1's
        - NumberofMismatched1sRate (bool): Number of Mismatched 1's Rate
        - NumberofRRDYsReceived (bool): Number of R_RDYs Received
        - NumberofRRDYsReceivedRate (bool): Number of R_RDYs Received Rate
        - NumberofRRDYsSent (bool): Number of R_RDYs Sent
        - NumberofRRDYsSentRate (bool): Number of R_RDYs Sent Rate
        - OutofWindowRxBroadcast (bool): Out of Window Rx Broadcast
        - OutofWindowRxMulticast (bool): Out of Window Rx Multicast
        - OverlayChipTemperatureC (bool): Overlay Chip Temperature(C)
        - Oversize (bool): Oversize
        - OversizeRate (bool): Oversize Rate
        - OversizeandCRCErrors (bool): Oversize and CRC Errors
        - OversizeandCRCErrorsRate (bool): Oversize and CRC Errors Rate
        - PathAIS (bool): Path AIS
        - PathAISAlarmedSeconds (bool): Path AIS Alarmed Seconds
        - PathAISUnavailableSeconds (bool): Path AIS Unavailable Seconds
        - PathBIPB3 (bool): Path BIP (B3)
        - PathBIPB3Rate (bool): Path BIP (B3) Rate
        - PathBIPErroredSeconds (bool): Path BIP Errored Seconds
        - PathLOP (bool): Path LOP
        - PathPLMC2 (bool): Path PLM (C2)
        - PathRDI (bool): Path RDI
        - PathRDIUnavailableSeconds (bool): Path RDI Unavailable Seconds
        - PathREIErroredSeconds (bool): Path REI Errored Seconds
        - PathREIFEBE (bool): Path REI (FEBE)
        - PathREIFEBERate (bool): Path REI (FEBE) Rate
        - PauseAcknowledge (bool): Pause Acknowledge
        - PauseAcknowledgeRate (bool): Pause Acknowledge Rate
        - PauseEndFrames (bool): Pause End Frames
        - PauseEndFramesRate (bool): Pause End Frames Rate
        - PauseOverwrite (bool): Pause Overwrite
        - PauseOverwriteRate (bool): Pause Overwrite Rate
        - PcsIllegalCodes (bool): PCS Illegal Codes
        - PcsIllegalCodesRate (bool): PCS Illegal Codes Rate
        - PcsIllegalIdle (bool): PCS Illegal Idle
        - PcsIllegalIdleRate (bool): PCS Illegal Idle Rate
        - PcsIllegalOrderedSet (bool): PCS Illegal Ordered Set
        - PcsIllegalOrderedSetRate (bool): PCS Illegal Ordered Set Rate
        - PcsIllegalSOF (bool): PCS Illegal SOF
        - PcsIllegalSOFRate (bool): PCS Illegal SOF Rate
        - PcsLocalFaults (bool): PCS Local Faults
        - PcsLocalFaultsRate (bool): PCS Local Faults Rate
        - PcsOutofOrderData (bool): PCS Out of Order Data
        - PcsOutofOrderDataRate (bool): PCS Out of Order Data Rate
        - PcsOutofOrderEOF (bool): PCS Out of Order EOF
        - PcsOutofOrderEOFRate (bool): PCS Out of Order EOF Rate
        - PcsOutofOrderOrderedSet (bool): PCS Out of Order Ordered Set
        - PcsOutofOrderOrderedSetRate (bool): PCS Out of Order Ordered Set Rate
        - PcsOutofOrderSOF (bool): PCS Out of Order SOF
        - PcsOutofOrderSOFRate (bool): PCS Out of Order SOF Rate
        - PcsRemoteFaults (bool): PCS Remote Faults
        - PcsRemoteFaultsRate (bool): PCS Remote Faults Rate
        - PcsSyncErrors (bool): PCS Sync Errors
        - PcsSyncErrorsRate (bool): PCS Sync Errors Rate
        - PercentCPULoad (bool): %CPU Load
        - PfcPriority0BufferMaxDepth (bool): PFC Priority 0 Buffer Max Depth
        - PfcPriority0PacketDrop (bool): PFC Priority 0 Packet Drop
        - PfcPriority0PacketDropRate (bool): PFC Priority 0 Packet Drop Rate
        - PfcPriority0PauseRatioPercent (bool): PFC Priority 0 Pause Ratio(%)
        - PfcPriority0PauseStart (bool): PFC Priority 0 Pause Start
        - PfcPriority0PauseStartResent (bool): PFC Priority 0 Pause Start Resent
        - PfcPriority0PauseStop (bool): PFC Priority 0 Pause Stop
        - PfcPriority1BufferMaxDepth (bool): PFC Priority 1 Buffer Max Depth
        - PfcPriority1PacketDrop (bool): PFC Priority 1 Packet Drop
        - PfcPriority1PacketDropRate (bool): PFC Priority 1 Packet Drop Rate
        - PfcPriority1PauseRatioPercent (bool): PFC Priority 1 Pause Ratio(%)
        - PfcPriority1PauseStart (bool): PFC Priority 1 Pause Start
        - PfcPriority1PauseStartResent (bool): PFC Priority 1 Pause Start Resent
        - PfcPriority1PauseStop (bool): PFC Priority 1 Pause Stop
        - PfcPriority2BufferMaxDepth (bool): PFC Priority 2 Buffer Max Depth
        - PfcPriority2PacketDrop (bool): PFC Priority 2 Packet Drop
        - PfcPriority2PacketDropRate (bool): PFC Priority 2 Packet Drop Rate
        - PfcPriority2PauseRatioPercent (bool): PFC Priority 2 Pause Ratio(%)
        - PfcPriority2PauseStart (bool): PFC Priority 2 Pause Start
        - PfcPriority2PauseStartResent (bool): PFC Priority 2 Pause Start Resent
        - PfcPriority2PauseStop (bool): PFC Priority 2 Pause Stop
        - PfcPriority3BufferMaxDepth (bool): PFC Priority 3 Buffer Max Depth
        - PfcPriority3PacketDrop (bool): PFC Priority 3 Packet Drop
        - PfcPriority3PacketDropRate (bool): PFC Priority 3 Packet Drop Rate
        - PfcPriority3PauseRatioPercent (bool): PFC Priority 3 Pause Ratio(%)
        - PfcPriority3PauseStart (bool): PFC Priority 3 Pause Start
        - PfcPriority3PauseStartResent (bool): PFC Priority 3 Pause Start Resent
        - PfcPriority3PauseStop (bool): PFC Priority 3 Pause Stop
        - PfcPriority4BufferMaxDepth (bool): PFC Priority 4 Buffer Max Depth
        - PfcPriority4PacketDrop (bool): PFC Priority 4 Packet Drop
        - PfcPriority4PacketDropRate (bool): PFC Priority 4 Packet Drop Rate
        - PfcPriority4PauseRatioPercent (bool): PFC Priority 4 Pause Ratio(%)
        - PfcPriority4PauseStart (bool): PFC Priority 4 Pause Start
        - PfcPriority4PauseStartResent (bool): PFC Priority 4 Pause Start Resent
        - PfcPriority4PauseStop (bool): PFC Priority 4 Pause Stop
        - PfcPriority5BufferMaxDepth (bool): PFC Priority 5 Buffer Max Depth
        - PfcPriority5PacketDrop (bool): PFC Priority 5 Packet Drop
        - PfcPriority5PacketDropRate (bool): PFC Priority 5 Packet Drop Rate
        - PfcPriority5PauseRatioPercent (bool): PFC Priority 5 Pause Ratio(%)
        - PfcPriority5PauseStart (bool): PFC Priority 5 Pause Start
        - PfcPriority5PauseStartResent (bool): PFC Priority 5 Pause Start Resent
        - PfcPriority5PauseStop (bool): PFC Priority 5 Pause Stop
        - PfcPriority6BufferMaxDepth (bool): PFC Priority 6 Buffer Max Depth
        - PfcPriority6PacketDrop (bool): PFC Priority 6 Packet Drop
        - PfcPriority6PacketDropRate (bool): PFC Priority 6 Packet Drop Rate
        - PfcPriority6PauseRatioPercent (bool): PFC Priority 6 Pause Ratio(%)
        - PfcPriority6PauseStart (bool): PFC Priority 6 Pause Start
        - PfcPriority6PauseStartResent (bool): PFC Priority 6 Pause Start Resent
        - PfcPriority6PauseStop (bool): PFC Priority 6 Pause Stop
        - PfcPriority7BufferMaxDepth (bool): PFC Priority 7 Buffer Max Depth
        - PfcPriority7PacketDrop (bool): PFC Priority 7 Packet Drop
        - PfcPriority7PacketDropRate (bool): PFC Priority 7 Packet Drop Rate
        - PfcPriority7PauseRatioPercent (bool): PFC Priority 7 Pause Ratio(%)
        - PfcPriority7PauseStart (bool): PFC Priority 7 Pause Start
        - PfcPriority7PauseStartResent (bool): PFC Priority 7 Pause Start Resent
        - PfcPriority7PauseStop (bool): PFC Priority 7 Pause Stop
        - PgidOverflow (bool): PGID Overflow
        - PgidOverflowRate (bool): PGID Overflow Rate
        - PhyChipTemperatureC (bool): PHY Chip Temperature (C)
        - PlcaBeaconCount (bool): PLCA Beacon Count
        - PlcaBeaconCountRate (bool): PLCA Beacon Count Rate
        - PlcaBeaconReceivedBeforeTransmitOpportunity (bool): PLCA Beacon Received Before Transmit Opportunity
        - PlcaCorruptedTransmitCount (bool): PLCA Corrupted Transmit Count
        - PlcaCorruptedTransmitCountRate (bool): PLCA Corrupted Transmit Count Rate
        - PlcaEmptyCycleStatus (bool): PLCA Empty Cycle Status
        - PlcaTransmitOpportunityCount (bool): PLCA Transmit Opportunity Count
        - PlcaTransmitOpportunityCountRate (bool): PLCA Transmit Opportunity Count Rate
        - Plcasymboldetected (bool): PLCA symbol detected
        - PlmInternalTemperature1C (bool): Plm Internal Temperature 1(C)
        - PlmInternalTemperature2C (bool): Plm Internal Temperature 2(C)
        - PlmInternalTemperature3C (bool): Plm Internal Temperature 3(C)
        - PlogiReceived (bool): Plogi Received
        - PlogiSent (bool): Plogi Sent
        - PlogiSuccessful (bool): Plogi Successful
        - PlogoReceived (bool): Plogo Received
        - PlogoSent (bool): Plogo Sent
        - PortCPUDoDStatus (bool): Port CPU DoD Status
        - PortCPUFramesReceived (bool): Port CPU Frames Received
        - PortCPUFramesSent (bool): Port CPU Frames Sent
        - PortCPUFramesSentRate (bool): Port CPU Frames Sent Rate
        - PortCPUStatus (bool): Port CPU Status
        - PortChipTemperatureC (bool): Port Chip Temperature(C)
        - PortName (bool): Port Name
        - PrbsBerRatio (bool): Prbs Ber Ratio
        - PrbsBitsReceived (bool): Prbs Bits Received
        - PrbsBitsReceivedRate (bool): Prbs Bits Received Rate
        - PrbsErroredBits (bool): Prbs Errored Bits
        - PrbsErroredBitsRate (bool): Prbs Errored Bits Rate
        - PrbsFramesReceived (bool): Prbs Frames Received
        - PrbsFramesReceivedRate (bool): Prbs Frames Received Rate
        - PrbsFramesWithHeaderError (bool): Prbs Frames With Header Error
        - PrbsFramesWithHeaderErrorRate (bool): Prbs Frames With Header Error Rate
        - PreFECBitErrorRatio (bool): pre FEC Bit Error Ratio
        - ProtectedByteRx (bool): Protected Byte Rx
        - ProtectedByteTx (bool): Protected Byte Tx
        - ProtectedPacketRx (bool): Protected Packet Rx
        - ProtectedPacketTx (bool): Protected Packet Tx
        - ProtocolServerVlanDroppedFrames (bool): Protocol Server Vlan Dropped Frames
        - PtpAnnounceMessagesReceived (bool): Ptp Announce Messages Received
        - PtpAnnounceMessagesSent (bool): Ptp Announce Messages Sent
        - PtpDelayReqMessagesReceived (bool): Ptp Delay_Req Messages Received
        - PtpDelayReqMessagesSent (bool): Ptp Delay_Req Messages Sent
        - PtpDelayRespMessagesReceived (bool): Ptp Delay_Resp Messages Received
        - PtpDelayRespMessagesSent (bool): Ptp Delay_Resp Messages Sent
        - PtpFollowUpMessagesReceived (bool): Ptp Follow_Up Messages Received
        - PtpFollowUpMessagesSent (bool): Ptp Follow_Up Messages Sent
        - PtpSyncMessagesReceived (bool): Ptp Sync Messages Received
        - PtpSyncMessagesSent (bool): Ptp Sync Messages Sent
        - RamDiskUtilization (bool): RAM Disk Utilization
        - ReceiveArpReply (bool): Receive Arp Reply
        - ReceiveArpRequest (bool): Receive Arp Request
        - ReceiveInTransmitOpportunity (bool): Receive In Transmit Opportunity
        - ReceiveNeighborAdvertisements (bool): Receive Neighbor Advertisements
        - ReceiveNeighborSolicitation (bool): Receive Neighbor Solicitation
        - ReceivePingReply (bool): Receive Ping Reply
        - ReceivePingRequest (bool): Receive Ping Request
        - RemoteBuffertoBufferCreditCount (bool): Remote Buffer-to-Buffer Credit Count
        - RemoteBuffertoBufferCreditValue (bool): Remote Buffer-to-Buffer Credit Value
        - RemoteFaults (bool): Remote Faults
        - RemoteOrderedSetsReceived (bool): Remote Ordered Sets Received
        - RemoteOrderedSetsReceivedRate (bool): Remote Ordered Sets Received Rate
        - RemoteOrderedSetsSent (bool): Remote Ordered Sets Sent
        - RemoteOrderedSetsSentRate (bool): Remote Ordered Sets Sent Rate
        - Rocev2BadiCRCCount (bool): RoCEv2 Bad iCRC Count
        - Rocev2OpCodeErrorCount (bool): RoCEv2 OpCode Error Count
        - RsFECCorrectedCodewordCount (bool): RS-FEC Corrected Codeword Count
        - RsFECCorrectedCodewordCountRate (bool): RS-FEC Corrected Codeword Count Rate
        - RsFECUncorrectedCodewordCount (bool): RS-FEC Uncorrected Codeword Count
        - RsFECUncorrectedCodewordCountRate (bool): RS-FEC Uncorrected Codeword Count Rate
        - Rx0FpgaTemperatureC (bool): Rx0 Fpga Temperature(C)
        - Rx1FpgaTemperatureC (bool): Rx1 Fpga Temperature(C)
        - RxBadPacketforBroadcastRate (bool): Rx Bad Packet for Broadcast Rate
        - RxBadPacketforMulticastRate (bool): Rx Bad Packet for Multicast Rate
        - RxBadTagPacketorICVDiscardedPacketforBroadcastRate (bool): Rx Bad Tag Packet or ICV Discarded Packet for Broadcast Rate
        - RxBadTagPacketorICVDiscardedPacketforMulticastRate (bool): Rx Bad Tag Packet or ICV Discarded Packet for Multicast Rate
        - RxBytesDecryptedBroadcast (bool): Rx Bytes Decrypted Broadcast
        - RxBytesDecryptedMulticast (bool): Rx Bytes Decrypted Multicast
        - RxBytesDecryptedforBroadcastRate (bool): Rx Bytes Decrypted for Broadcast Rate
        - RxBytesDecryptedforMulticastRate (bool): Rx Bytes Decrypted for Multicast Rate
        - RxBytesValidatedBroadcast (bool): Rx Bytes Validated Broadcast
        - RxBytesValidatedMulticast (bool): Rx Bytes Validated Multicast
        - RxBytesValidatedforBroadcastRate (bool): Rx Bytes Validated for Broadcast Rate
        - RxBytesValidatedforMulticastRate (bool): Rx Bytes Validated for Multicast Rate
        - RxEncryptedByteCountRate (bool): Rx Encrypted Byte Count Rate
        - RxEncryptedPacketCountRate (bool): Rx Encrypted Packet Count Rate
        - RxFPExpressCRCTypeErrorCount (bool): Rx FP Express CRC Type Error Count
        - RxFPExpressCRCTypeErrorCountRate (bool): Rx FP Express CRC Type Error Count Rate
        - RxFPFragCountError (bool): Rx FP Frag Count Error
        - RxFPFragCountErrorRate (bool): Rx FP Frag Count Error Rate
        - RxFPInvalidCRCTypeErrorCount (bool): Rx FP Invalid CRC Type Error Count
        - RxFPInvalidCRCTypeErrorCountRate (bool): Rx FP Invalid CRC Type Error Count Rate
        - RxFPReassemblyGoodCount (bool): Rx FP Reassembly Good Count
        - RxFPReassemblyGoodCountRate (bool): Rx FP Reassembly Good Count Rate
        - RxFPRespondmPacketCRCErrorCount (bool): Rx FP Respond mPacket CRC Error Count
        - RxFPRespondmPacketCRCErrorCountRate (bool): Rx FP Respond mPacket CRC Error Count Rate
        - RxFPRespondmPacketCount (bool): Rx FP Respond mPacket Count
        - RxFPRespondmPacketCountRate (bool): Rx FP Respond mPacket Count Rate
        - RxFPSMDC0mPacketCRCErrorCount (bool): Rx FP SMD-C0 mPacket CRC Error Count
        - RxFPSMDC0mPacketCRCErrorCountRate (bool): Rx FP SMD-C0 mPacket CRC Error Count Rate
        - RxFPSMDC0mPacketCount (bool): Rx FP SMD-C0 mPacket Count
        - RxFPSMDC0mPacketCountRate (bool): Rx FP SMD-C0 mPacket Count Rate
        - RxFPSMDC1mPacketCRCErrorCount (bool): Rx FP SMD-C1 mPacket CRC Error Count
        - RxFPSMDC1mPacketCRCErrorCountRate (bool): Rx FP SMD-C1 mPacket CRC Error Count Rate
        - RxFPSMDC1mPacketCount (bool): Rx FP SMD-C1 mPacket Count
        - RxFPSMDC1mPacketCountRate (bool): Rx FP SMD-C1 mPacket Count Rate
        - RxFPSMDC2mPacketCRCErrorCount (bool): Rx FP SMD-C2 mPacket CRC Error Count
        - RxFPSMDC2mPacketCRCErrorCountRate (bool): Rx FP SMD-C2 mPacket CRC Error Count Rate
        - RxFPSMDC2mPacketCount (bool): Rx FP SMD-C2 mPacket Count
        - RxFPSMDC2mPacketCountRate (bool): Rx FP SMD-C2 mPacket Count Rate
        - RxFPSMDC3mPacketCRCErrorCount (bool): Rx FP SMD-C3 mPacket CRC Error Count
        - RxFPSMDC3mPacketCRCErrorCountRate (bool): Rx FP SMD-C3 mPacket CRC Error Count Rate
        - RxFPSMDC3mPacketCount (bool): Rx FP SMD-C3 mPacket Count
        - RxFPSMDC3mPacketCountRate (bool): Rx FP SMD-C3 mPacket Count Rate
        - RxFPSMDCCRCCalcErrorCount (bool): Rx FP SMD-C CRC Calc Error Count
        - RxFPSMDCCRCCalcErrorCountRate (bool): Rx FP SMD-C CRC Calc Error Count Rate
        - RxFPSMDCFrameCountError (bool): Rx FP SMD-C Frame Count Error
        - RxFPSMDCFrameCountErrorRate (bool): Rx FP SMD-C Frame Count Error Rate
        - RxFPSMDCTerminationErrorCount (bool): Rx FP SMD-C Termination Error Count
        - RxFPSMDCTerminationErrorCountRate (bool): Rx FP SMD-C Termination Error Count Rate
        - RxFPSMDRNotTransmittedCount (bool): Rx FP SMD-R Not Transmitted Count
        - RxFPSMDRNotTransmittedCountRate (bool): Rx FP SMD-R Not Transmitted Count Rate
        - RxFPSMDS0mPacketCRCErrorCount (bool): Rx FP SMD-S0 mPacket CRC Error Count
        - RxFPSMDS0mPacketCRCErrorCountRate (bool): Rx FP SMD-S0 mPacket CRC Error Count Rate
        - RxFPSMDS0mPacketCount (bool): Rx FP SMD-S0 mPacket Count
        - RxFPSMDS0mPacketCountRate (bool): Rx FP SMD-S0 mPacket Count Rate
        - RxFPSMDS1mPacketCRCErrorCount (bool): Rx FP SMD-S1 mPacket CRC Error Count
        - RxFPSMDS1mPacketCRCErrorCountRate (bool): Rx FP SMD-S1 mPacket CRC Error Count Rate
        - RxFPSMDS1mPacketCount (bool): Rx FP SMD-S1 mPacket Count
        - RxFPSMDS1mPacketCountRate (bool): Rx FP SMD-S1 mPacket Count Rate
        - RxFPSMDS2mPacketCRCErrorCount (bool): Rx FP SMD-S2 mPacket CRC Error Count
        - RxFPSMDS2mPacketCRCErrorCountRate (bool): Rx FP SMD-S2 mPacket CRC Error Count Rate
        - RxFPSMDS2mPacketCount (bool): Rx FP SMD-S2 mPacket Count
        - RxFPSMDS2mPacketCountRate (bool): Rx FP SMD-S2 mPacket Count Rate
        - RxFPSMDS3mPacketCRCErrorCount (bool): Rx FP SMD-S3 mPacket CRC Error Count
        - RxFPSMDS3mPacketCRCErrorCountRate (bool): Rx FP SMD-S3 mPacket CRC Error Count Rate
        - RxFPSMDS3mPacketCount (bool): Rx FP SMD-S3 mPacket Count
        - RxFPSMDS3mPacketCountRate (bool): Rx FP SMD-S3 mPacket Count Rate
        - RxFPSMDSFrameCountError (bool): Rx FP SMD-S Frame Count Error
        - RxFPSMDSFrameCountErrorRate (bool): Rx FP SMD-S Frame Count Error Rate
        - RxFPSMDSStartProtocolError (bool): Rx FP SMD-S Start Protocol Error
        - RxFPSMDSStartProtocolErrorRate (bool): Rx FP SMD-S Start Protocol Error Rate
        - RxFPSMDSTerminationErrorCount (bool): Rx FP SMD-S Termination Error Count
        - RxFPSMDSTerminationErrorCountRate (bool): Rx FP SMD-S Termination Error Count Rate
        - RxFPSMDVNotReceivedCount (bool): Rx FP SMD-V Not Received Count
        - RxFPSMDVNotReceivedCountRate (bool): Rx FP SMD-V Not Received Count Rate
        - RxFPUnexpectedSMDRCount (bool): Rx FP Unexpected SMD-R Count
        - RxFPUnexpectedSMDRCountRate (bool): Rx FP Unexpected SMD-R Count Rate
        - RxFPVerifyProtocolError (bool): Rx FP Verify Protocol Error
        - RxFPVerifyProtocolErrorRate (bool): Rx FP Verify Protocol Error Rate
        - RxFPVerifymPacketCRCErrorCount (bool): Rx FP Verify mPacket CRC Error Count
        - RxFPVerifymPacketCRCErrorCountRate (bool): Rx FP Verify mPacket CRC Error Count Rate
        - RxFPVerifymPacketCount (bool): Rx FP Verify mPacket Count
        - RxFPVerifymPacketCountRate (bool): Rx FP Verify mPacket Count Rate
        - RxFpgaTemperatureC (bool): Rx Fpga Temperature(C)
        - RxInvalidICVDiscardedPacketforBroadcastRate (bool): Rx Invalid ICV Discarded Packet for Broadcast Rate
        - RxInvalidICVDiscardedPacketforMulticastRate (bool): Rx Invalid ICV Discarded Packet for Multicast Rate
        - RxInvalidICVPacketforBroadcastRate (bool): Rx Invalid ICV Packet for Broadcast Rate
        - RxInvalidICVPacketforMulticastRate (bool): Rx Invalid ICV Packet for Multicast Rate
        - RxNonMACsecPacketCountRate (bool): Rx NonMACsec Packet Count Rate
        - RxOpticalPowerHighAlarm (bool): Rx Optical Power High Alarm
        - RxOpticalPowerHighWarn (bool): Rx Optical Power High Warn
        - RxOpticalPowerLimitFlag (bool): Rx Optical Power Limit Flag
        - RxOpticalPowerLowAlarm (bool): Rx Optical Power Low Alarm
        - RxOpticalPowerLowWarn (bool): Rx Optical Power Low Warn
        - RxOutofWindowPacketorOutofWindowDiscardedPacketforBroadcastRate (bool): Rx Out of Window Packet or Out of Window Discarded Packet for Broadcast Rate
        - RxOutofWindowPacketorOutofWindowDiscardedPacketforMulticastRate (bool): Rx Out of Window Packet or Out of Window Discarded Packet for Multicast Rate
        - RxPausePriorityGroup0Frames (bool): Rx Pause Priority Group 0 Frames
        - RxPausePriorityGroup0FramesRate (bool): Rx Pause Priority Group 0 Frames Rate
        - RxPausePriorityGroup1Frames (bool): Rx Pause Priority Group 1 Frames
        - RxPausePriorityGroup1FramesRate (bool): Rx Pause Priority Group 1 Frames Rate
        - RxPausePriorityGroup2Frames (bool): Rx Pause Priority Group 2 Frames
        - RxPausePriorityGroup2FramesRate (bool): Rx Pause Priority Group 2 Frames Rate
        - RxPausePriorityGroup3Frames (bool): Rx Pause Priority Group 3 Frames
        - RxPausePriorityGroup3FramesRate (bool): Rx Pause Priority Group 3 Frames Rate
        - RxPausePriorityGroup4Frames (bool): Rx Pause Priority Group 4 Frames
        - RxPausePriorityGroup4FramesRate (bool): Rx Pause Priority Group 4 Frames Rate
        - RxPausePriorityGroup5Frames (bool): Rx Pause Priority Group 5 Frames
        - RxPausePriorityGroup5FramesRate (bool): Rx Pause Priority Group 5 Frames Rate
        - RxPausePriorityGroup6Frames (bool): Rx Pause Priority Group 6 Frames
        - RxPausePriorityGroup6FramesRate (bool): Rx Pause Priority Group 6 Frames Rate
        - RxPausePriorityGroup7Frames (bool): Rx Pause Priority Group 7 Frames
        - RxPausePriorityGroup7FramesRate (bool): Rx Pause Priority Group 7 Frames Rate
        - RxProtectedByteCountRate (bool): Rx Protected Byte Count Rate
        - RxProtectedPacketCountRate (bool): Rx Protected Packet Count Rate
        - RxRateKbps (bool): Rx. Rate (Kbps)
        - RxRateMbps (bool): Rx. Rate (Mbps)
        - RxRatebps (bool): Rx. Rate (bps)
        - RxRoCEACKFrameCount (bool): Rx RoCE ACK Frame Count
        - RxRoCEACKFrameCountRate (bool): Rx RoCE ACK Frame Count Rate
        - RxRoCECNPFrameCount (bool): Rx RoCE CNP Frame Count
        - RxRoCECNPFrameCountRate (bool): Rx RoCE CNP Frame Count Rate
        - RxRoCEECNFrameCount (bool): Rx RoCE ECN Frame Count
        - RxRoCEECNFrameCountRate (bool): Rx RoCE ECN Frame Count Rate
        - RxRoCENAKFrameCount (bool): Rx RoCE NAK Frame Count
        - RxRoCENAKFrameCountRate (bool): Rx RoCE NAK Frame Count Rate
        - RxRoCEOpcodeErrorCountRate (bool): Rx RoCE Opcode Error Count Rate
        - RxRoCEPrePFCCNPFrameCount (bool): Rx RoCE Pre-PFC CNP Frame Count
        - RxRoCEPrePFCCNPFrameCountRate (bool): Rx RoCE Pre-PFC CNP Frame Count Rate
        - RxRoCEiCRCErrorCountRate (bool): Rx RoCE iCRC Error Count Rate
        - RxSharedStat1 (bool): Rx Shared Stat 1
        - RxSharedStat1Rate (bool): Rx Shared Stat 1 Rate
        - RxSharedStat2 (bool): Rx Shared Stat 2
        - RxSharedStat2Rate (bool): Rx Shared Stat 2 Rate
        - RxUnknownSCIDiscardedPacketorUnusedSADiscardedPacketRate (bool): Rx Unknown SCI Discarded Packet or Unused SA Discarded Packet Rate
        - RxUnknownSCIPacketorUnusedSAPacketRate (bool): Rx Unknown SCI Packet or Unused SA Packet Rate
        - RxUnvalidatedPacketCountRate (bool): Rx Unvalidated Packet Count Rate
        - RxValidPacketforBroadcastRate (bool): Rx Valid Packet for Broadcast Rate
        - RxValidPacketforMulticastRate (bool): Rx Valid Packet for Multicast Rate
        - ScheduledCellsTx (bool): Scheduled Cells Tx.
        - ScheduledCellsTxRate (bool): Scheduled Cells Tx. Rate
        - ScheduledFramesTx (bool): Scheduled Frames Tx.
        - ScheduledFramesTxRate (bool): Scheduled Frames Tx. Rate
        - ScheduledTransmitDuration (bool): Scheduled Transmit Duration
        - ScheduledTxRoCEACKFrameCount (bool): Scheduled Tx RoCE ACK Frame Count
        - ScheduledTxRoCEACKFrameCountRate (bool): Scheduled Tx RoCE ACK Frame Count Rate
        - ScheduledTxRoCECNPFrameCount (bool): Scheduled Tx RoCE CNP Frame Count
        - ScheduledTxRoCECNPFrameCountRate (bool): Scheduled Tx RoCE CNP Frame Count Rate
        - ScheduledTxRoCENAKFrameCount (bool): Scheduled Tx RoCE NAK Frame Count
        - ScheduledTxRoCENAKFrameCountRate (bool): Scheduled Tx RoCE NAK Frame Count Rate
        - SchedulerChipTemperatureC (bool): Scheduler Chip Temperature(C)
        - SectionBIPB1 (bool): Section BIP (B1)
        - SectionBIPB1Rate (bool): Section BIP (B1) Rate
        - SectionBIPErroredSeconds (bool): Section BIP Errored Seconds
        - SectionBIPSeverelyErroredSeconds (bool): Section BIP Severely Errored Seconds
        - SectionLOF (bool): Section LOF
        - SectionLOS (bool): Section LOS
        - SectionLOSSeconds (bool): Section LOS Seconds
        - SequenceErrors (bool): Sequence Errors
        - SequenceErrorsRate (bool): Sequence Errors Rate
        - SequenceFrames (bool): Sequence Frames
        - SequenceFramesRate (bool): Sequence Frames Rate
        - SeverelyErroredSeconds (bool): Severely Errored Seconds
        - SofBigErrorFrameCount (bool): SOF Big Error Frame Count
        - SofEarlyFrameCount (bool): SOF Early Frame Count
        - SofEarlyMaximumByteCount (bool): SOF Early Maximum Byte Count
        - SofEarlyMinimumByteCount (bool): SOF Early Minimum Byte Count
        - StatelessBitsReceived (bool): Stateless Bits Received
        - StatelessBitsSent (bool): Stateless Bits Sent
        - StatelessBytesReceived (bool): Stateless Bytes Received
        - StatelessBytesReceivedRate (bool): Stateless Bytes Received Rate
        - StatelessBytesRxRate (bool): Stateless Bytes Rx. Rate
        - StatelessBytesSent (bool): Stateless Bytes Sent
        - StatelessBytesSentRate (bool): Stateless Bytes Sent Rate
        - StatelessBytesTxRate (bool): Stateless Bytes Tx. Rate
        - StatelessFramesSent (bool): Stateless Frames Sent
        - StatelessFramesSentRate (bool): Stateless Frames Sent Rate
        - StatelessRxRateKbps (bool): Stateless Rx. Rate (Kbps)
        - StatelessRxRateMbps (bool): Stateless Rx. Rate (Mbps)
        - StatelessRxRatebps (bool): Stateless Rx. Rate (bps)
        - StatelessTxRateKbps (bool): Stateless Tx. Rate (Kbps)
        - StatelessTxRateMbps (bool): Stateless Tx. Rate (Mbps)
        - StatelessTxRatebps (bool): Stateless Tx. Rate (bps)
        - Status (bool): Status
        - SupplyVoltageHighAlarm (bool): Supply Voltage High Alarm
        - SupplyVoltageHighWarn (bool): Supply Voltage High Warn
        - SupplyVoltageLimitFlag (bool): Supply Voltage Limit Flag
        - SupplyVoltageLowAlarm (bool): Supply Voltage Low Alarm
        - SupplyVoltageLowWarn (bool): Supply Voltage Low Warn
        - TcpChecksumErrors (bool): TCP Checksum Errors
        - TcpChecksumErrorsRate (bool): TCP Checksum Errors Rate
        - TcpPacketsReceived (bool): TCP Packets Received
        - TcpPacketsReceivedRate (bool): TCP Packets Received Rate
        - TemperatureHighAlarm (bool): Temperature High Alarm
        - TemperatureHighWarn (bool): Temperature High Warn
        - TemperatureLimitFlag (bool): Temperature Limit Flag
        - TemperatureLowAlarm (bool): Temperature Low Alarm
        - TemperatureLowWarn (bool): Temperature Low Warn
        - TotalMemory (bool): Total Memory
        - TransceiverTemperatureC (bool): Transceiver Temperature (C)
        - TransmitArpGratuitous (bool): Transmit Arp Gratuitous
        - TransmitArpGratuitousRate (bool): Transmit Arp Gratuitous Rate
        - TransmitArpReply (bool): Transmit Arp Reply
        - TransmitArpRequest (bool): Transmit Arp Request
        - TransmitArpReverse (bool): Transmit Arp Reverse
        - TransmitArpReverseRate (bool): Transmit Arp Reverse Rate
        - TransmitDurationClearedonStartTx (bool): Transmit Duration(Cleared on Start Tx)
        - TransmitNeighborAdvertisements (bool): Transmit Neighbor Advertisements
        - TransmitNeighborSolicitation (bool): Transmit Neighbor Solicitation
        - TransmitPingReply (bool): Transmit Ping Reply
        - TransmitPingRequest (bool): Transmit Ping Request
        - Tx0FpgaTemperatureC (bool): Tx0 Fpga Temperature(C)
        - TxBiasCurrentHighAlarm (bool): Tx Bias Current High Alarm
        - TxBiasCurrentHighWarn (bool): Tx Bias Current High Warn
        - TxBiasCurrentLimitFlag (bool): Tx Bias Current Limit Flag
        - TxBiasCurrentLowAlarm (bool): Tx Bias Current Low Alarm
        - TxBiasCurrentLowWarn (bool): Tx Bias Current Low Warn
        - TxEncryptedByteCountRate (bool): Tx Encrypted Byte Count Rate
        - TxEncryptedPacketCountRate (bool): Tx Encrypted Packet Count Rate
        - TxFpgaTemperatureC (bool): Tx Fpga Temperature(C)
        - TxNonMACsecPacketCountRate (bool): Tx NonMACsec Packet Count Rate
        - TxOpticalPowerHighAlarm (bool): Tx Optical Power High Alarm
        - TxOpticalPowerHighWarn (bool): Tx Optical Power High Warn
        - TxOpticalPowerLimitFlag (bool): Tx Optical Power Limit Flag
        - TxOpticalPowerLowAlarm (bool): Tx Optical Power Low Alarm
        - TxOpticalPowerLowWarn (bool): Tx Optical Power Low Warn
        - TxProtectedByteCountRate (bool): Tx Protected Byte Count Rate
        - TxProtectedPacketCountRate (bool): Tx Protected Packet Count Rate
        - TxRateKbps (bool): Tx. Rate (Kbps)
        - TxRateMbps (bool): Tx. Rate (Mbps)
        - TxRatebps (bool): Tx. Rate (bps)
        - UdpChecksumErrors (bool): UDP Checksum Errors
        - UdpChecksumErrorsRate (bool): UDP Checksum Errors Rate
        - UdpPacketsReceived (bool): UDP Packets Received
        - UdpPacketsReceivedRate (bool): UDP Packets Received Rate
        - UnavailableSeconds (bool): Unavailable Seconds
        - UncorrectedHCSErrorCount (bool): Uncorrected HCS Error Count
        - UncorrectedHCSErrorCountRate (bool): Uncorrected HCS Error Count Rate
        - Undersize (bool): Undersize
        - UndersizeRate (bool): Undersize Rate
        - UnexpectedPLCABeaconReceived (bool): Unexpected PLCA Beacon Received
        - UnknownSCISAAccepted (bool): Unknown SCI/SA Accepted
        - UnknownSCISADiscarded (bool): Unknown SCI/SA Discarded
        - UnvalidatedPacketRx (bool): Unvalidated Packet Rx
        - UserDefinedStat1 (bool): User Defined Stat 1
        - UserDefinedStat1Rate (bool): User Defined Stat 1 Rate
        - UserDefinedStat2 (bool): User Defined Stat 2
        - UserDefinedStat2Rate (bool): User Defined Stat 2 Rate
        - UserDefinedStat5 (bool): User Defined Stat 5
        - UserDefinedStat5Rate (bool): User Defined Stat 5 Rate
        - UserDefinedStat6 (bool): User Defined Stat 6
        - UserDefinedStat6Rate (bool): User Defined Stat 6 Rate
        - UserDefinedStatByteCount1 (bool): User Defined Stat Byte Count 1
        - UserDefinedStatByteCount1Rate (bool): User Defined Stat Byte Count 1 Rate
        - UserDefinedStatByteCount2 (bool): User Defined Stat Byte Count 2
        - UserDefinedStatByteCount2Rate (bool): User Defined Stat Byte Count 2 Rate
        - ValidFramesRx (bool): Valid Frames Rx.
        - ValidFramesRxRate (bool): Valid Frames Rx. Rate
        - ValidPacketRxBroadcast (bool): Valid Packet Rx Broadcast
        - ValidPacketRxMulticast (bool): Valid Packet Rx Multicast
        - ValidStatelessFramesReceived (bool): Valid Stateless Frames Received
        - ValidStatelessFramesReceivedRate (bool): Valid Stateless Frames Received Rate
        - VlanTaggedFrames (bool): Vlan Tagged Frames
        - VlanTaggedFramesRate (bool): Vlan Tagged Frames Rate
        - WindowClosedFrameCount (bool): Window Closed Frame Count
        - WindowValidFrameCount (bool): Window Valid Frame Count
        - WindowViolationFrameCount (bool): Window Violation Frame Count

        Returns
        -------
        - self: This instance with matching portStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of portStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the portStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
