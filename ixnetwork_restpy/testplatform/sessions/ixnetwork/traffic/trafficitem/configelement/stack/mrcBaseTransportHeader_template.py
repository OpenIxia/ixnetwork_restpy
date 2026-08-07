from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MrcBaseTransportHeader(Base):
    __slots__ = ()
    _SDM_NAME = "mrcBaseTransportHeader"
    _SDM_ATT_MAP = {
        "BaseTransportHeaderOpCodeOptions": "mrcBaseTransportHeader.baseTransportHeader.opCodeOptions-1",
        "BaseTransportHeaderMigReq": "mrcBaseTransportHeader.baseTransportHeader.migReq-2",
        "BaseTransportHeaderSe": "mrcBaseTransportHeader.baseTransportHeader.se-3",
        "BaseTransportHeaderPadCount": "mrcBaseTransportHeader.baseTransportHeader.padCount-4",
        "BaseTransportHeaderTransportHeaderVersion": "mrcBaseTransportHeader.baseTransportHeader.transportHeaderVersion-5",
        "BaseTransportHeaderPartitionKey": "mrcBaseTransportHeader.baseTransportHeader.partitionKey-6",
        "BaseTransportHeaderRes1": "mrcBaseTransportHeader.baseTransportHeader.res1-7",
        "BaseTransportHeaderDestQp": "mrcBaseTransportHeader.baseTransportHeader.destQp-8",
        "BaseTransportHeaderAckReq": "mrcBaseTransportHeader.baseTransportHeader.ackReq-9",
        "BaseTransportHeaderRes2": "mrcBaseTransportHeader.baseTransportHeader.res2-10",
        "BaseTransportHeaderRtx": "mrcBaseTransportHeader.baseTransportHeader.rtx-11",
        "BaseTransportHeaderTsethPresent": "mrcBaseTransportHeader.baseTransportHeader.tsethPresent-12",
        "BaseTransportHeaderRes3": "mrcBaseTransportHeader.baseTransportHeader.res3-13",
        "BaseTransportHeaderPsn": "mrcBaseTransportHeader.baseTransportHeader.psn-14",
    }

    def __init__(self, parent, list_op=False):
        super(MrcBaseTransportHeader, self).__init__(parent, list_op)

    @property
    def BaseTransportHeaderOpCodeOptions(self):
        """
        Display Name: OpCode
        Default Value: 198
        Value Format: decimal
        Available enum values: RDMA WRITE First, 198, RDMA WRITE Middle, 199, RDMA WRITE Last, 200, RDMA WRITE Last with Immediate, 201, RDMA WRITE Only, 202, RDMA WRITE Only with Immediate, 203, Acknowledge, 209, Endpoint Request, 216, Endpoint Response, 217, Reliability SACK, 220, Reliability NACK, 221, Reliability PROBE Request, 222
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderOpCodeOptions"]),
        )

    @property
    def BaseTransportHeaderMigReq(self):
        """
        Display Name: MigReq
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderMigReq"])
        )

    @property
    def BaseTransportHeaderSe(self):
        """
        Display Name: Solicited Event
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderSe"])
        )

    @property
    def BaseTransportHeaderPadCount(self):
        """
        Display Name: Pad Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderPadCount"])
        )

    @property
    def BaseTransportHeaderTransportHeaderVersion(self):
        """
        Display Name: Transport Header Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["BaseTransportHeaderTransportHeaderVersion"]
            ),
        )

    @property
    def BaseTransportHeaderPartitionKey(self):
        """
        Display Name: Partition Key
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderPartitionKey"]),
        )

    @property
    def BaseTransportHeaderRes1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderRes1"])
        )

    @property
    def BaseTransportHeaderDestQp(self):
        """
        Display Name: Destination QP
        Default Value: 0xFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderDestQp"])
        )

    @property
    def BaseTransportHeaderAckReq(self):
        """
        Display Name: AckReq
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderAckReq"])
        )

    @property
    def BaseTransportHeaderRes2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderRes2"])
        )

    @property
    def BaseTransportHeaderRtx(self):
        """
        Display Name: Retransmit
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderRtx"])
        )

    @property
    def BaseTransportHeaderTsethPresent(self):
        """
        Display Name: TSETH Present
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderTsethPresent"]),
        )

    @property
    def BaseTransportHeaderRes3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderRes3"])
        )

    @property
    def BaseTransportHeaderPsn(self):
        """
        Display Name: Packet Sequence Number (PSN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderPsn"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
