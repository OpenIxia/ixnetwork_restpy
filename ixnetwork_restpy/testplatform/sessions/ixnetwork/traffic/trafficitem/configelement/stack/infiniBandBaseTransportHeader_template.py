from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class InfiniBandBaseTransportHeader(Base):
    __slots__ = ()
    _SDM_NAME = "infiniBandBaseTransportHeader"
    _SDM_ATT_MAP = {
        "BaseTransportHeaderOpCodeOptions": "infiniBandBaseTransportHeader.baseTransportHeader.opCodeOptions-1",
        "BaseTransportHeaderSe": "infiniBandBaseTransportHeader.baseTransportHeader.se-2",
        "BaseTransportHeaderMigReq": "infiniBandBaseTransportHeader.baseTransportHeader.migReq-3",
        "BaseTransportHeaderPadCount": "infiniBandBaseTransportHeader.baseTransportHeader.padCount-4",
        "BaseTransportHeaderTransportHeaderVersion": "infiniBandBaseTransportHeader.baseTransportHeader.transportHeaderVersion-5",
        "BaseTransportHeaderPartitionKey": "infiniBandBaseTransportHeader.baseTransportHeader.partitionKey-6",
        "BaseTransportHeaderFecnRes": "infiniBandBaseTransportHeader.baseTransportHeader.fecnRes-7",
        "BaseTransportHeaderBecnRes": "infiniBandBaseTransportHeader.baseTransportHeader.becnRes-8",
        "BaseTransportHeaderResv6": "infiniBandBaseTransportHeader.baseTransportHeader.resv6-9",
        "BaseTransportHeaderDestQp": "infiniBandBaseTransportHeader.baseTransportHeader.destQp-10",
        "BaseTransportHeaderAckReq": "infiniBandBaseTransportHeader.baseTransportHeader.ackReq-11",
        "BaseTransportHeaderResv7": "infiniBandBaseTransportHeader.baseTransportHeader.resv7-12",
        "BaseTransportHeaderPsn": "infiniBandBaseTransportHeader.baseTransportHeader.psn-13",
    }

    def __init__(self, parent, list_op=False):
        super(InfiniBandBaseTransportHeader, self).__init__(parent, list_op)

    @property
    def BaseTransportHeaderOpCodeOptions(self):
        """
        Display Name: OpCode
        Default Value: 6
        Value Format: decimal
        Available enum values: Reliable Connection (RC) - SEND First, 0, Reliable Connection (RC) - SEND Middle, 1, Reliable Connection (RC) - SEND Last, 2, Reliable Connection (RC) - SEND Last with Immediate, 3, Reliable Connection (RC) - SEND Only, 4, Reliable Connection (RC) - SEND Only with Immediate, 5, Reliable Connection (RC) - RDMA WRITE First, 6, Reliable Connection (RC) - RDMA WRITE Middle, 7, Reliable Connection (RC) - RDMA WRITE Last, 8, Reliable Connection (RC) - RDMA WRITE Last with Immediate, 9, Reliable Connection (RC) - RDMA WRITE Only, 10, Reliable Connection (RC) - RDMA WRITE Only with Immediate, 11, Reliable Connection (RC) - RDMA READ Request, 12, Reliable Connection (RC) - RDMA READ response First, 13, Reliable Connection (RC) - RDMA READ response Middle, 14, Reliable Connection (RC) - RDMA READ response Last, 15, Reliable Connection (RC) - RDMA READ response Only, 16, Reliable Connection (RC) - Acknowledge, 17, Reliable Connection (RC) - ATOMIC Acknowledge, 18, Reliable Connection (RC) - CmpSwap, 19, Reliable Connection (RC) - FetchAdd, 20, Reliable Connection (RC) - Reserve, 21, Reliable Connection (RC) - SEND Last with Invalidate, 22, Reliable Connection (RC) - SEND Last Only with Invalidate, 23, Unreliable Connection (UC) - SEND First, 32, Unreliable Connection (UC) - SEND Middle, 33, Unreliable Connection (UC) - SEND Last, 34, Unreliable Connection (UC) - SEND Last with Immediate, 35, Unreliable Connection (UC) - SEND Only, 36, Unreliable Connection (UC) - SEND Only with Immediate, 37, Unreliable Connection (UC) - RDMA WRITE First, 38, Unreliable Connection (UC) - RDMA WRITE Middle, 39, Unreliable Connection (UC) - RDMA WRITE Last, 40, Unreliable Connection (UC) - RDMA WRITE Last with Immediate, 41, Unreliable Connection (UC) - RDMA WRITE Only, 42, Unreliable Connection (UC) - RDMA WRITE Only with Immediate, 43, Reliable Datagram (RD) - SEND First, 64, Reliable Datagram (RD) - SEND Middle, 65, Reliable Datagram (RD) - SEND Last, 66, Reliable Datagram (RD) - SEND Last with Immediate, 67, Reliable Datagram (RD) - SEND Only, 68, Reliable Datagram (RD) - SEND Only with Immediate, 69, Reliable Datagram (RD) - RDMA WRITE First, 70, Reliable Datagram (RD) - RDMA WRITE Middle, 71, Reliable Datagram (RD) - RDMA WRITE Last, 72, Reliable Datagram (RD) - RDMA WRITE Last with Immediate, 73, Reliable Datagram (RD) - RDMA WRITE Only, 74, Reliable Datagram (RD) - RDMA WRITE Only with Immediate, 75, Reliable Datagram (RD) - RDMA READ Request, 76, Reliable Datagram (RD) - RDMA READ response First, 77, Reliable Datagram (RD) - RDMA READ response Middle, 78, Reliable Datagram (RD) - RDMA READ response Last, 79, Reliable Datagram (RD) - RDMA READ response Only, 80, Reliable Datagram (RD) - Acknowledge, 81, Reliable Datagram (RD) - ATOMIC Acknowledge, 82, Reliable Datagram (RD) - CmpSwap, 83, Reliable Datagram (RD) - FetchAdd, 84, Reliable Datagram (RD) - RESYNC, 85, Unreliable Datagram (UD) - SEND only, 100, Unreliable Datagram (UD) - SEND only with Immediate, 101, CNP, 129
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderOpCodeOptions"]),
        )

    @property
    def BaseTransportHeaderSe(self):
        """
        Display Name: Solicited Event (SE)
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderSe"])
        )

    @property
    def BaseTransportHeaderMigReq(self):
        """
        Display Name: MiGREQ (M)
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderMigReq"])
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
        Display Name: Transport Header Version (TVer)
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
        Display Name: Partition Key (P_Key)
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderPartitionKey"]),
        )

    @property
    def BaseTransportHeaderFecnRes(self):
        """
        Display Name: FECN/RES1
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderFecnRes"])
        )

    @property
    def BaseTransportHeaderBecnRes(self):
        """
        Display Name: BECN/RES1
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderBecnRes"])
        )

    @property
    def BaseTransportHeaderResv6(self):
        """
        Display Name: Reserve 6 (Resv6)
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderResv6"])
        )

    @property
    def BaseTransportHeaderDestQp(self):
        """
        Display Name: Destination QP (DestQP)
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
        Display Name: AckReq (A)
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderAckReq"])
        )

    @property
    def BaseTransportHeaderResv7(self):
        """
        Display Name: Reserve 7 (Resv7)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderResv7"])
        )

    @property
    def BaseTransportHeaderPsn(self):
        """
        Display Name: Packet Sequence Number (PSN)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseTransportHeaderPsn"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
