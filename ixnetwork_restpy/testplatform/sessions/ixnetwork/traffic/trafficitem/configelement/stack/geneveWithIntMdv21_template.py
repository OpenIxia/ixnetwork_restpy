from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class GeneveWithIntMdv21(Base):
    __slots__ = ()
    _SDM_NAME = "geneveWithIntMdv21"
    _SDM_ATT_MAP = {
        "HeaderVersion": "geneveWithIntMdv21.header.version-1",
        "HeaderOptionslength": "geneveWithIntMdv21.header.optionslength-2",
        "HeaderFlags": "geneveWithIntMdv21.header.flags-3",
        "HeaderProtocol": "geneveWithIntMdv21.header.protocol-4",
        "HeaderVni": "geneveWithIntMdv21.header.vni-5",
        "HeaderReserved8": "geneveWithIntMdv21.header.reserved8-6",
        "TelemetryOptionclass": "geneveWithIntMdv21.header.tlv.telemetry.optionclass-7",
        "TelemetryOptiontype": "geneveWithIntMdv21.header.tlv.telemetry.optiontype-8",
        "TelemetryReserved03": "geneveWithIntMdv21.header.tlv.telemetry.reserved03-9",
        "TelemetryLength0": "geneveWithIntMdv21.header.tlv.telemetry.length0-10",
        "OptiondataVersion": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.version-11",
        "OptiondataDiscard": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.discard-12",
        "OptiondataExceeded": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.exceeded-13",
        "OptiondataMtuexceeded": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.mtuexceeded-14",
        "OptiondataReserved12": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.reserved12-15",
        "OptiondataHopml": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.hopml-16",
        "OptiondataRemaininghopcount": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.remaininghopcount-17",
        "InstbitmapNodeid": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.instbitmap.nodeid-18",
        "InstbitmapIngressegressinterfaceid": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.instbitmap.ingressegressinterfaceid-19",
        "InstbitmapHoplatency": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.instbitmap.hoplatency-20",
        "InstbitmapQueue": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.instbitmap.queue-21",
        "InstbitmapIngresstimestamp": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.instbitmap.ingresstimestamp-22",
        "InstbitmapEgresstimestamp": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.instbitmap.egresstimestamp-23",
        "InstbitmapIngressegressinterfaceidwide": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.instbitmap.ingressegressinterfaceidwide-24",
        "InstbitmapEgressinterfacetxutil": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.instbitmap.egressinterfacetxutil-25",
        "InstbitmapBuffer": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.instbitmap.buffer-26",
        "InstbitmapReserved06": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.instbitmap.reserved06-27",
        "InstbitmapChecksumcomplement": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.instbitmap.checksumcomplement-28",
        "OptiondataDomainspecificid": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.domainspecificid-29",
        "OptiondataDsinstruction": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.dsinstruction-30",
        "OptiondataDsflags": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.dsflags-31",
        "IntmetadatastackNid": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.nid-32",
        "Ingressegressinterfaceid32Iifid": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.ingressegressinterfaceid32.iifid-33",
        "Ingressegressinterfaceid32Eifid": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.ingressegressinterfaceid32.eifid-34",
        "IntmetadatastackHl": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.hl-35",
        "QueueidoccupancyQid": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.queueidoccupancy.qid-36",
        "QueueidoccupancyQo": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.queueidoccupancy.qo-37",
        "IntmetadatastackIt": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.it-38",
        "IntmetadatastackEt": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.et-39",
        "Ingressegressinterfaceid64Iifid32": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.ingressegressinterfaceid64.iifid32-40",
        "Ingressegressinterfaceid64Eifid32": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.ingressegressinterfaceid64.eifid32-41",
        "IntmetadatastackEiftu32": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.eiftu32-42",
        "BufferidoccupancyBid": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.bufferidoccupancy.bid-43",
        "BufferidoccupancyBo": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.bufferidoccupancy.bo-44",
        "IntmetadatastackReservedmeta": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.reservedmeta-45",
        "IntmetadatastackDefault": "geneveWithIntMdv21.header.tlv.telemetry.optiondata.intmetadatastack.-46",
    }

    def __init__(self, parent, list_op=False):
        super(GeneveWithIntMdv21, self).__init__(parent, list_op)

    @property
    def HeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def HeaderOptionslength(self):
        """
        Display Name: Options Length (x4 octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderOptionslength"])
        )

    @property
    def HeaderFlags(self):
        """
        Display Name: Flags
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderFlags"]))

    @property
    def HeaderProtocol(self):
        """
        Display Name: Protocol Type
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderProtocol"])
        )

    @property
    def HeaderVni(self):
        """
        Display Name: VNI
        Default Value: 1000
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVni"]))

    @property
    def HeaderReserved8(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved8"])
        )

    @property
    def TelemetryOptionclass(self):
        """
        Display Name: Option Class
        Default Value: 0x0103
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TelemetryOptionclass"])
        )

    @property
    def TelemetryOptiontype(self):
        """
        Display Name: Option Type
        Default Value: 1
        Value Format: decimal
        Available enum values: INT-MD, 1, INT-Destination, 2, INT-MX, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TelemetryOptiontype"])
        )

    @property
    def TelemetryReserved03(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TelemetryReserved03"])
        )

    @property
    def TelemetryLength0(self):
        """
        Display Name: Length (x4 octets)
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TelemetryLength0"])
        )

    @property
    def OptiondataVersion(self):
        """
        Display Name: Version
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataVersion"])
        )

    @property
    def OptiondataDiscard(self):
        """
        Display Name: Discard (D)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataDiscard"])
        )

    @property
    def OptiondataExceeded(self):
        """
        Display Name: Max Hop Count Exceeded (E)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataExceeded"])
        )

    @property
    def OptiondataMtuexceeded(self):
        """
        Display Name: MTU Exceeded (M)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataMtuexceeded"])
        )

    @property
    def OptiondataReserved12(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataReserved12"])
        )

    @property
    def OptiondataHopml(self):
        """
        Display Name: Hop Metadata Length (x4 bytes)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataHopml"])
        )

    @property
    def OptiondataRemaininghopcount(self):
        """
        Display Name: Remaining Hop Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataRemaininghopcount"])
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
    def OptiondataDomainspecificid(self):
        """
        Display Name: Domain Specific ID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataDomainspecificid"])
        )

    @property
    def OptiondataDsinstruction(self):
        """
        Display Name: DS Instruction
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataDsinstruction"])
        )

    @property
    def OptiondataDsflags(self):
        """
        Display Name: DS Flags
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataDsflags"])
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
