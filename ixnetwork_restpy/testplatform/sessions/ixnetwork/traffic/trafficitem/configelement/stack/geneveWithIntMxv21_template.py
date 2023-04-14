from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class GeneveWithIntMxv21(Base):
    __slots__ = ()
    _SDM_NAME = "geneveWithIntMxv21"
    _SDM_ATT_MAP = {
        "HeaderVersion": "geneveWithIntMxv21.header.version-1",
        "HeaderOptionslength": "geneveWithIntMxv21.header.optionslength-2",
        "HeaderFlags": "geneveWithIntMxv21.header.flags-3",
        "HeaderProtocol": "geneveWithIntMxv21.header.protocol-4",
        "HeaderVni": "geneveWithIntMxv21.header.vni-5",
        "HeaderReserved8": "geneveWithIntMxv21.header.reserved8-6",
        "TelemetryOptionclass": "geneveWithIntMxv21.header.tlv.telemetry.optionclass-7",
        "TelemetryOptiontype": "geneveWithIntMxv21.header.tlv.telemetry.optiontype-8",
        "TelemetryReserved03": "geneveWithIntMxv21.header.tlv.telemetry.reserved03-9",
        "TelemetryLength0": "geneveWithIntMxv21.header.tlv.telemetry.length0-10",
        "OptiondataVersion": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.version-11",
        "OptiondataDiscard": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.discard-12",
        "OptiondataReserved27": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.reserved27-13",
        "InstbitmapNodeid": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.instbitmap.nodeid-14",
        "InstbitmapIngressegressinterfaceid": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.instbitmap.ingressegressinterfaceid-15",
        "InstbitmapHoplatency": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.instbitmap.hoplatency-16",
        "InstbitmapQueue": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.instbitmap.queue-17",
        "InstbitmapIngresstimestamp": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.instbitmap.ingresstimestamp-18",
        "InstbitmapEgresstimestamp": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.instbitmap.egresstimestamp-19",
        "InstbitmapIngressegressinterfaceidwide": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.instbitmap.ingressegressinterfaceidwide-20",
        "InstbitmapEgressinterfacetxutil": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.instbitmap.egressinterfacetxutil-21",
        "InstbitmapBuffer": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.instbitmap.buffer-22",
        "InstbitmapReserved07": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.instbitmap.reserved07-23",
        "OptiondataDomainspecificid": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.domainspecificid-24",
        "OptiondataDsinstruction": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.dsinstruction-25",
        "OptiondataDsflags": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.dsflags-26",
        "OptiondataDatalength": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.datalength-27",
        "OptiondataMetadata": "geneveWithIntMxv21.header.tlv.telemetry.optiondata.metadata-28",
    }

    def __init__(self, parent, list_op=False):
        super(GeneveWithIntMxv21, self).__init__(parent, list_op)

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
        Default Value: 3
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
    def OptiondataReserved27(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataReserved27"])
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
    def OptiondataDatalength(self):
        """
        Display Name: Length of Metadata (x4 bytes)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataDatalength"])
        )

    @property
    def OptiondataMetadata(self):
        """
        Display Name: Metadata
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataMetadata"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
