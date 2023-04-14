from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IntMdMetadatav21(Base):
    __slots__ = ()
    _SDM_NAME = "intMdMetadatav21"
    _SDM_ATT_MAP = {
        "IntMdMetadataVersion": "intMdMetadatav21.intMdMetadata.version-1",
        "IntMdMetadataDiscard": "intMdMetadatav21.intMdMetadata.discard-2",
        "IntMdMetadataExceeded": "intMdMetadatav21.intMdMetadata.exceeded-3",
        "IntMdMetadataMtuexceeded": "intMdMetadatav21.intMdMetadata.mtuexceeded-4",
        "IntMdMetadataReserved12": "intMdMetadatav21.intMdMetadata.reserved12-5",
        "IntMdMetadataHopml": "intMdMetadatav21.intMdMetadata.hopml-6",
        "IntMdMetadataRemaininghopcount": "intMdMetadatav21.intMdMetadata.remaininghopcount-7",
        "InstbitmapNodeid": "intMdMetadatav21.intMdMetadata.instbitmap.nodeid-8",
        "InstbitmapIngressegressinterfaceid": "intMdMetadatav21.intMdMetadata.instbitmap.ingressegressinterfaceid-9",
        "InstbitmapHoplatency": "intMdMetadatav21.intMdMetadata.instbitmap.hoplatency-10",
        "InstbitmapQueue": "intMdMetadatav21.intMdMetadata.instbitmap.queue-11",
        "InstbitmapIngresstimestamp": "intMdMetadatav21.intMdMetadata.instbitmap.ingresstimestamp-12",
        "InstbitmapEgresstimestamp": "intMdMetadatav21.intMdMetadata.instbitmap.egresstimestamp-13",
        "InstbitmapIngressegressinterfaceidwide": "intMdMetadatav21.intMdMetadata.instbitmap.ingressegressinterfaceidwide-14",
        "InstbitmapEgressinterfacetxutil": "intMdMetadatav21.intMdMetadata.instbitmap.egressinterfacetxutil-15",
        "InstbitmapBuffer": "intMdMetadatav21.intMdMetadata.instbitmap.buffer-16",
        "InstbitmapReserved06": "intMdMetadatav21.intMdMetadata.instbitmap.reserved06-17",
        "InstbitmapChecksumcomplement": "intMdMetadatav21.intMdMetadata.instbitmap.checksumcomplement-18",
        "IntMdMetadataDomainspecificid": "intMdMetadatav21.intMdMetadata.domainspecificid-19",
        "IntMdMetadataDsinstruction": "intMdMetadatav21.intMdMetadata.dsinstruction-20",
        "IntMdMetadataDsflags": "intMdMetadatav21.intMdMetadata.dsflags-21",
        "IntmetadatastackNid": "intMdMetadatav21.intMdMetadata.intmetadatastack.nid-22",
        "Ingressegressinterfaceid32Iifid": "intMdMetadatav21.intMdMetadata.intmetadatastack.ingressegressinterfaceid32.iifid-23",
        "Ingressegressinterfaceid32Eifid": "intMdMetadatav21.intMdMetadata.intmetadatastack.ingressegressinterfaceid32.eifid-24",
        "IntmetadatastackHl": "intMdMetadatav21.intMdMetadata.intmetadatastack.hl-25",
        "QueueidoccupancyQid": "intMdMetadatav21.intMdMetadata.intmetadatastack.queueidoccupancy.qid-26",
        "QueueidoccupancyQo": "intMdMetadatav21.intMdMetadata.intmetadatastack.queueidoccupancy.qo-27",
        "IntmetadatastackIt": "intMdMetadatav21.intMdMetadata.intmetadatastack.it-28",
        "IntmetadatastackEt": "intMdMetadatav21.intMdMetadata.intmetadatastack.et-29",
        "Ingressegressinterfaceid64Iifid32": "intMdMetadatav21.intMdMetadata.intmetadatastack.ingressegressinterfaceid64.iifid32-30",
        "Ingressegressinterfaceid64Eifid32": "intMdMetadatav21.intMdMetadata.intmetadatastack.ingressegressinterfaceid64.eifid32-31",
        "IntmetadatastackEiftu32": "intMdMetadatav21.intMdMetadata.intmetadatastack.eiftu32-32",
        "BufferidoccupancyBid": "intMdMetadatav21.intMdMetadata.intmetadatastack.bufferidoccupancy.bid-33",
        "BufferidoccupancyBo": "intMdMetadatav21.intMdMetadata.intmetadatastack.bufferidoccupancy.bo-34",
        "IntmetadatastackReservedmeta": "intMdMetadatav21.intMdMetadata.intmetadatastack.reservedmeta-35",
        "IntmetadatastackDefault": "intMdMetadatav21.intMdMetadata.intmetadatastack.-36",
    }

    def __init__(self, parent, list_op=False):
        super(IntMdMetadatav21, self).__init__(parent, list_op)

    @property
    def IntMdMetadataVersion(self):
        """
        Display Name: Version
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMdMetadataVersion"])
        )

    @property
    def IntMdMetadataDiscard(self):
        """
        Display Name: Discard (D)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMdMetadataDiscard"])
        )

    @property
    def IntMdMetadataExceeded(self):
        """
        Display Name: Max Hop Count Exceeded (E)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMdMetadataExceeded"])
        )

    @property
    def IntMdMetadataMtuexceeded(self):
        """
        Display Name: MTU Exceeded (M)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMdMetadataMtuexceeded"])
        )

    @property
    def IntMdMetadataReserved12(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMdMetadataReserved12"])
        )

    @property
    def IntMdMetadataHopml(self):
        """
        Display Name: Hop Metadata Length (x4 bytes)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMdMetadataHopml"])
        )

    @property
    def IntMdMetadataRemaininghopcount(self):
        """
        Display Name: Remaining Hop Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IntMdMetadataRemaininghopcount"]),
        )

    @property
    def InstbitmapNodeid(self):
        """
        Display Name: Node ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstbitmapNodeid"])
        )

    @property
    def InstbitmapIngressegressinterfaceid(self):
        """
        Display Name: Level 1 Ingress-Egress Interface ID(short)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["InstbitmapIngressegressinterfaceid"]
            ),
        )

    @property
    def InstbitmapHoplatency(self):
        """
        Display Name: Hop Latency
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstbitmapHoplatency"])
        )

    @property
    def InstbitmapQueue(self):
        """
        Display Name: Queue ID and Occupancy
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstbitmapQueue"])
        )

    @property
    def InstbitmapIngresstimestamp(self):
        """
        Display Name: Ingress Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstbitmapIngresstimestamp"])
        )

    @property
    def InstbitmapEgresstimestamp(self):
        """
        Display Name: Egress Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstbitmapEgresstimestamp"])
        )

    @property
    def InstbitmapIngressegressinterfaceidwide(self):
        """
        Display Name: Level 2 Ingress-Egress Interface ID(wide)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["InstbitmapIngressegressinterfaceidwide"]
            ),
        )

    @property
    def InstbitmapEgressinterfacetxutil(self):
        """
        Display Name: Egress Interface TX Utilization
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["InstbitmapEgressinterfacetxutil"]),
        )

    @property
    def InstbitmapBuffer(self):
        """
        Display Name: Buffer ID and Occupancy
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstbitmapBuffer"])
        )

    @property
    def InstbitmapReserved06(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstbitmapReserved06"])
        )

    @property
    def InstbitmapChecksumcomplement(self):
        """
        Display Name: Checksum Complement
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstbitmapChecksumcomplement"])
        )

    @property
    def IntMdMetadataDomainspecificid(self):
        """
        Display Name: Domain Specific ID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IntMdMetadataDomainspecificid"]),
        )

    @property
    def IntMdMetadataDsinstruction(self):
        """
        Display Name: DS Instruction
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMdMetadataDsinstruction"])
        )

    @property
    def IntMdMetadataDsflags(self):
        """
        Display Name: DS Flags
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMdMetadataDsflags"])
        )

    @property
    def IntmetadatastackNid(self):
        """
        Display Name: Node ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadatastackNid"])
        )

    @property
    def Ingressegressinterfaceid32Iifid(self):
        """
        Display Name: Ingress Interface ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ingressegressinterfaceid32Iifid"]),
        )

    @property
    def Ingressegressinterfaceid32Eifid(self):
        """
        Display Name: Egress Interface ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ingressegressinterfaceid32Eifid"]),
        )

    @property
    def IntmetadatastackHl(self):
        """
        Display Name: Hop Latency
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadatastackHl"])
        )

    @property
    def QueueidoccupancyQid(self):
        """
        Display Name: Queue ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["QueueidoccupancyQid"])
        )

    @property
    def QueueidoccupancyQo(self):
        """
        Display Name: Queue Occupancy
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["QueueidoccupancyQo"])
        )

    @property
    def IntmetadatastackIt(self):
        """
        Display Name: Ingress Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadatastackIt"])
        )

    @property
    def IntmetadatastackEt(self):
        """
        Display Name: Egress Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadatastackEt"])
        )

    @property
    def Ingressegressinterfaceid64Iifid32(self):
        """
        Display Name: Ingress Interface ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ingressegressinterfaceid64Iifid32"]),
        )

    @property
    def Ingressegressinterfaceid64Eifid32(self):
        """
        Display Name: Egress Interface ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ingressegressinterfaceid64Eifid32"]),
        )

    @property
    def IntmetadatastackEiftu32(self):
        """
        Display Name: Egress Interface TX Utilization
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadatastackEiftu32"])
        )

    @property
    def BufferidoccupancyBid(self):
        """
        Display Name: Buffer ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BufferidoccupancyBid"])
        )

    @property
    def BufferidoccupancyBo(self):
        """
        Display Name: Buffer Occupancy
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BufferidoccupancyBo"])
        )

    @property
    def IntmetadatastackReservedmeta(self):
        """
        Display Name: Reserved
        Default Value: 0xFFFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadatastackReservedmeta"])
        )

    @property
    def IntmetadatastackDefault(self):
        """
        Display Name: Checksum Complement
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadatastackDefault"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
