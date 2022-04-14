from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipNpivFdiscLsRjtFcf(Base):
    __slots__ = ()
    _SDM_NAME = "fipNpivFdiscLsRjtFcf"
    _SDM_ATT_MAP = {
        "HeaderFipVersion": "fipNpivFdiscLsRjtFcf.header.fipVersion-1",
        "HeaderFipReserved": "fipNpivFdiscLsRjtFcf.header.fipReserved-2",
        "FipOperationCodeFipVirtualLinkInstantiation": "fipNpivFdiscLsRjtFcf.header.fipOperation.fipOperationCode.fipVirtualLinkInstantiation-3",
        "FipOperationFipOperationReserved1": "fipNpivFdiscLsRjtFcf.header.fipOperation.fipOperationReserved1-4",
        "FipSubcodeFipSubcode02h": "fipNpivFdiscLsRjtFcf.header.fipOperation.fipSubcode.fipSubcode02h-5",
        "FipOperationFipDescriptorListLength": "fipNpivFdiscLsRjtFcf.header.fipOperation.fipDescriptorListLength-6",
        "FipOperationFipFp": "fipNpivFdiscLsRjtFcf.header.fipOperation.fipFp-7",
        "FipOperationFipSp": "fipNpivFdiscLsRjtFcf.header.fipOperation.fipSp-8",
        "FipOperationFipReserved2": "fipNpivFdiscLsRjtFcf.header.fipOperation.fipReserved2-9",
        "FipOperationFipABit": "fipNpivFdiscLsRjtFcf.header.fipOperation.fipABit-10",
        "FipOperationFipSBit": "fipNpivFdiscLsRjtFcf.header.fipOperation.fipSBit-11",
        "FipOperationFipFBit": "fipNpivFdiscLsRjtFcf.header.fipOperation.fipFBit-12",
        "FipNpivFdiscDescriptorFipNpivFdiscDescriptorType": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorType-13",
        "FipNpivFdiscDescriptorFipNpivFdiscDescriptorLength": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorLength-14",
        "FipNpivFdiscDescriptorFipNpivFdiscDescriptorReserved": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorReserved-15",
        "ExtendedLinkServicesExtendedLinkServiceInfo": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelRCtl.extendedLinkServices.extendedLinkServiceInfo-16",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelDId": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelDId-17",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelCsCtlPriority": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelCsCtlPriority-18",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSId": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelSId-19",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelType": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelType-20",
        "FCtlExchangeContext": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.exchangeContext-21",
        "FCtlSequenceContext": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.sequenceContext-22",
        "FCtlFirstSequence": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.firstSequence-23",
        "FCtlLastSequence": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.lastSequence-24",
        "FCtlEndSequence": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.endSequence-25",
        "FCtlEndConnection": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.endConnection-26",
        "FCtlCsCtlPriority": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.csCtlPriority-27",
        "FCtlSequenceInitiative": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.sequenceInitiative-28",
        "FCtlFcXidReassigned": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.fcXidReassigned-29",
        "FCtlFcInvalidateXid": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.fcInvalidateXid-30",
        "FCtlAckForm": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.ackForm-31",
        "FCtlFcDataCompression": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.fcDataCompression-32",
        "FCtlFcDataEncryption": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.fcDataEncryption-33",
        "FCtlRetransmittedSequence": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.retransmittedSequence-34",
        "FCtlUnidirectionalTransmit": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.unidirectionalTransmit-35",
        "FCtlContinueSeqCondition": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.continueSeqCondition-36",
        "FCtlAbortSeqCondition": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.abortSeqCondition-37",
        "FCtlRelativeOffsetPresent": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.relativeOffsetPresent-38",
        "FCtlExchangeReassembly": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.exchangeReassembly-39",
        "FCtlFillBytes": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelFCtl.fCtl.fillBytes-40",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSeqId": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelSeqId-41",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelDfCtl": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelDfCtl-42",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSeqCnt": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelSeqCnt-43",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelOxId": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelOxId-44",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelRxId": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelRxId-45",
        "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelParameter": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscFibreChannel.fipNpivFdiscDescriptorFibreChannelParameter-46",
        "FipNpivFdiscDescriptorFcElsCommandCodeFipNpivFdiscDescriptorFcElsCommandCodeLsRjt": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsAcceptReject.fipNpivFdiscDescriptorFcElsCommandCode.fipNpivFdiscDescriptorFcElsCommandCodeLsRjt-47",
        "FipNpivFdiscDescriptorFcElsAcceptRejectFipNpivFdiscDescriptorFcElsAcceptRejectReserved": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsAcceptReject.fipNpivFdiscDescriptorFcElsAcceptRejectReserved-48",
        "FipNpivFdiscDescriptorFcElsAcceptRejectFipNpivFdiscDescriptorFcElsLsRjtReasonCodes": "fipNpivFdiscLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipNpivFdiscDescriptor.fipNpivFdiscDescriptorFcEls.fipNpivFdiscDescriptorFcElsAcceptReject.fipNpivFdiscDescriptorFcElsLsRjtReasonCodes-49",
    }

    def __init__(self, parent, list_op=False):
        super(FipNpivFdiscLsRjtFcf, self).__init__(parent, list_op)

    @property
    def HeaderFipVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFipVersion"])
        )

    @property
    def HeaderFipReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFipReserved"])
        )

    @property
    def FipOperationCodeFipVirtualLinkInstantiation(self):
        """
        Display Name: Virtual Link Instantiation
        Default Value: 0x0002
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipOperationCodeFipVirtualLinkInstantiation"]
            ),
        )

    @property
    def FipOperationFipOperationReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FipOperationFipOperationReserved1"]),
        )

    @property
    def FipSubcodeFipSubcode02h(self):
        """
        Display Name: Subcode 02h
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipSubcodeFipSubcode02h"])
        )

    @property
    def FipOperationFipDescriptorListLength(self):
        """
        Display Name: FIP Descriptor List Length
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipOperationFipDescriptorListLength"]
            ),
        )

    @property
    def FipOperationFipFp(self):
        """
        Display Name: FP
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipFp"])
        )

    @property
    def FipOperationFipSp(self):
        """
        Display Name: SP
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipSp"])
        )

    @property
    def FipOperationFipReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipReserved2"])
        )

    @property
    def FipOperationFipABit(self):
        """
        Display Name: A bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipABit"])
        )

    @property
    def FipOperationFipSBit(self):
        """
        Display Name: S bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipSBit"])
        )

    @property
    def FipOperationFipFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipFBit"])
        )

    @property
    def FipNpivFdiscDescriptorFipNpivFdiscDescriptorType(self):
        """
        Display Name: FLOGI Descriptor Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipNpivFdiscDescriptorFipNpivFdiscDescriptorType"]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFipNpivFdiscDescriptorLength(self):
        """
        Display Name: FLOGI Descriptor Length
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipNpivFdiscDescriptorFipNpivFdiscDescriptorLength"]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFipNpivFdiscDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscDescriptorFipNpivFdiscDescriptorReserved"
                ]
            ),
        )

    @property
    def ExtendedLinkServicesExtendedLinkServiceInfo(self):
        """
        Display Name: Information
        Default Value: 35
        Value Format: decimal
        Available enum values: Solicited Data, 33, Request, 34, Reply, 35
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ExtendedLinkServicesExtendedLinkServiceInfo"]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelDId(self):
        """
        Display Name: D_ID
        Default Value: 00.00.01
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelDId"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelCsCtlPriority"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSId(self):
        """
        Display Name: S_ID
        Default Value: FF.FF.FE
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSId"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelType"
                ]
            ),
        )

    @property
    def FCtlExchangeContext(self):
        """
        Display Name: Exchange Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Originator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlExchangeContext"])
        )

    @property
    def FCtlSequenceContext(self):
        """
        Display Name: Sequence Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Initiator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlSequenceContext"])
        )

    @property
    def FCtlFirstSequence(self):
        """
        Display Name: First Sequence
        Default Value: 1
        Value Format: decimal
        Available enum values: Other, 0, First, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFirstSequence"])
        )

    @property
    def FCtlLastSequence(self):
        """
        Display Name: Last Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlLastSequence"])
        )

    @property
    def FCtlEndSequence(self):
        """
        Display Name: End Sequence
        Default Value: 1
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlEndSequence"])
        )

    @property
    def FCtlEndConnection(self):
        """
        Display Name: End Connection
        Default Value: 0
        Value Format: decimal
        Available enum values: Alive, 0, Pending, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlEndConnection"])
        )

    @property
    def FCtlCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority Enable
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority Enable, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlCsCtlPriority"])
        )

    @property
    def FCtlSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 1
        Value Format: decimal
        Available enum values: Hold, 0, Transfer, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlSequenceInitiative"])
        )

    @property
    def FCtlFcXidReassigned(self):
        """
        Display Name: FC XID Reassigned
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcXidReassigned"])
        )

    @property
    def FCtlFcInvalidateXid(self):
        """
        Display Name: FC Invalidate XID
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcInvalidateXid"])
        )

    @property
    def FCtlAckForm(self):
        """
        Display Name: ACK
        Default Value: 0
        Value Format: decimal
        Available enum values: No assistance provided, 0, ACK_1 Required, 1, reserved, 2, Ack_0 Required, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCtlAckForm"]))

    @property
    def FCtlFcDataCompression(self):
        """
        Display Name: FC Data Compression
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcDataCompression"])
        )

    @property
    def FCtlFcDataEncryption(self):
        """
        Display Name: FC Data Encryption
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcDataEncryption"])
        )

    @property
    def FCtlRetransmittedSequence(self):
        """
        Display Name: Retransmitted Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Original, 0, Retransmission, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlRetransmittedSequence"])
        )

    @property
    def FCtlUnidirectionalTransmit(self):
        """
        Display Name: Unidirectional Transmit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bi-directional, 0, Unidirectional, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlUnidirectionalTransmit"])
        )

    @property
    def FCtlContinueSeqCondition(self):
        """
        Display Name: Continue Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: No information, 0, Sequence to follow-immediately, 1, Squence to follow-soon, 2, Sequence to follow-delayed, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlContinueSeqCondition"])
        )

    @property
    def FCtlAbortSeqCondition(self):
        """
        Display Name: Abort Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x00, 0, 0x01, 1, 0x10, 2, 0x11, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlAbortSeqCondition"])
        )

    @property
    def FCtlRelativeOffsetPresent(self):
        """
        Display Name: Relative offset present
        Default Value: 0
        Value Format: decimal
        Available enum values: Parameter field defined, 0, Relative offset, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlRelativeOffsetPresent"])
        )

    @property
    def FCtlExchangeReassembly(self):
        """
        Display Name: Exchange Reassembly
        Default Value: 0
        Value Format: decimal
        Available enum values: off, 0, on, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlExchangeReassembly"])
        )

    @property
    def FCtlFillBytes(self):
        """
        Display Name: Fill Bytes
        Default Value: 0
        Value Format: decimal
        Available enum values: 0 bytes of fill, 0, 1 bytes of fill, 1, 2 bytes of fill, 2, 3 bytes of fill, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCtlFillBytes"]))

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSeqId(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSeqId"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelDfCtl(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelDfCtl"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSeqCnt(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelSeqCnt"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelOxId(self):
        """
        Display Name: OX_ID
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelOxId"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelRxId(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelRxId"
                ]
            ),
        )

    @property
    def FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelParameter(self):
        """
        Display Name: Parameter
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscFibreChannelFipNpivFdiscDescriptorFibreChannelParameter"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsCommandCodeFipNpivFdiscDescriptorFcElsCommandCodeLsRjt(
        self,
    ):
        """
        Display Name: LS_RJT
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscDescriptorFcElsCommandCodeFipNpivFdiscDescriptorFcElsCommandCodeLsRjt"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsAcceptRejectFipNpivFdiscDescriptorFcElsAcceptRejectReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscDescriptorFcElsAcceptRejectFipNpivFdiscDescriptorFcElsAcceptRejectReserved"
                ]
            ),
        )

    @property
    def FipNpivFdiscDescriptorFcElsAcceptRejectFipNpivFdiscDescriptorFcElsLsRjtReasonCodes(
        self,
    ):
        """
        Display Name: LS_RJT Reason Codes
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipNpivFdiscDescriptorFcElsAcceptRejectFipNpivFdiscDescriptorFcElsLsRjtReasonCodes"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
