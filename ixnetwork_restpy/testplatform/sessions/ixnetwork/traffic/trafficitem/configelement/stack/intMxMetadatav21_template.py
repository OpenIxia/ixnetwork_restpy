from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IntMxMetadatav21(Base):
    __slots__ = ()
    _SDM_NAME = "intMxMetadatav21"
    _SDM_ATT_MAP = {
        "IntMxMetadataVersion": "intMxMetadatav21.intMxMetadata.version-1",
        "IntMxMetadataDiscard": "intMxMetadatav21.intMxMetadata.discard-2",
        "IntMxMetadataReserved27": "intMxMetadatav21.intMxMetadata.reserved27-3",
        "InstbitmapNodeid": "intMxMetadatav21.intMxMetadata.instbitmap.nodeid-4",
        "InstbitmapIngressegressinterfaceid": "intMxMetadatav21.intMxMetadata.instbitmap.ingressegressinterfaceid-5",
        "InstbitmapHoplatency": "intMxMetadatav21.intMxMetadata.instbitmap.hoplatency-6",
        "InstbitmapQueue": "intMxMetadatav21.intMxMetadata.instbitmap.queue-7",
        "InstbitmapIngresstimestamp": "intMxMetadatav21.intMxMetadata.instbitmap.ingresstimestamp-8",
        "InstbitmapEgresstimestamp": "intMxMetadatav21.intMxMetadata.instbitmap.egresstimestamp-9",
        "InstbitmapIngressegressinterfaceidwide": "intMxMetadatav21.intMxMetadata.instbitmap.ingressegressinterfaceidwide-10",
        "InstbitmapEgressinterfacetxutil": "intMxMetadatav21.intMxMetadata.instbitmap.egressinterfacetxutil-11",
        "InstbitmapBuffer": "intMxMetadatav21.intMxMetadata.instbitmap.buffer-12",
        "InstbitmapReserved07": "intMxMetadatav21.intMxMetadata.instbitmap.reserved07-13",
        "IntMxMetadataDomainspecificid": "intMxMetadatav21.intMxMetadata.domainspecificid-14",
        "IntMxMetadataDsinstruction": "intMxMetadatav21.intMxMetadata.dsinstruction-15",
        "IntMxMetadataDsflags": "intMxMetadatav21.intMxMetadata.dsflags-16",
    }

    def __init__(self, parent, list_op=False):
        super(IntMxMetadatav21, self).__init__(parent, list_op)

    @property
    def IntMxMetadataVersion(self):
        """
        Display Name: Version
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMxMetadataVersion"])
        )

    @property
    def IntMxMetadataDiscard(self):
        """
        Display Name: Discard (D)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMxMetadataDiscard"])
        )

    @property
    def IntMxMetadataReserved27(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMxMetadataReserved27"])
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
    def InstbitmapReserved07(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstbitmapReserved07"])
        )

    @property
    def IntMxMetadataDomainspecificid(self):
        """
        Display Name: Domain Specific ID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IntMxMetadataDomainspecificid"]),
        )

    @property
    def IntMxMetadataDsinstruction(self):
        """
        Display Name: DS Instruction
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMxMetadataDsinstruction"])
        )

    @property
    def IntMxMetadataDsflags(self):
        """
        Display Name: DS Flags
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntMxMetadataDsflags"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
