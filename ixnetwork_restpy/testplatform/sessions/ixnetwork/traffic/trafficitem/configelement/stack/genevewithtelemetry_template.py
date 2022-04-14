from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Genevewithtelemetry(Base):
    __slots__ = ()
    _SDM_NAME = "genevewithtelemetry"
    _SDM_ATT_MAP = {
        "HeaderVersion": "genevewithtelemetry.header.version-1",
        "HeaderOptionslength": "genevewithtelemetry.header.optionslength-2",
        "HeaderFlags": "genevewithtelemetry.header.flags-3",
        "HeaderProtocol": "genevewithtelemetry.header.protocol-4",
        "HeaderVni": "genevewithtelemetry.header.vni-5",
        "HeaderReserved8": "genevewithtelemetry.header.reserved8-6",
        "HeaderLength": "genevewithtelemetry.header.length-7",
        "TelemetryOptionclass": "genevewithtelemetry.header.tlv.telemetry.optionclass-8",
        "TelemetryOptiontype": "genevewithtelemetry.header.tlv.telemetry.optiontype-9",
        "TelemetryReserved03": "genevewithtelemetry.header.tlv.telemetry.reserved03-10",
        "TelemetryLength0": "genevewithtelemetry.header.tlv.telemetry.length0-11",
        "OptiondataVersion": "genevewithtelemetry.header.tlv.telemetry.optiondata.version-12",
        "OptiondataReplication": "genevewithtelemetry.header.tlv.telemetry.optiondata.replication-13",
        "OptiondataCopy": "genevewithtelemetry.header.tlv.telemetry.optiondata.copy-14",
        "OptiondataExceeded": "genevewithtelemetry.header.tlv.telemetry.optiondata.exceeded-15",
        "OptiondataMtuexceeded": "genevewithtelemetry.header.tlv.telemetry.optiondata.mtuexceeded-16",
        "OptiondataReserved10": "genevewithtelemetry.header.tlv.telemetry.optiondata.reserved10-17",
        "OptiondataHopml": "genevewithtelemetry.header.tlv.telemetry.optiondata.hopml-18",
        "OptiondataRemaininghopcount": "genevewithtelemetry.header.tlv.telemetry.optiondata.remaininghopcount-19",
        "InstbitmapSwitchid": "genevewithtelemetry.header.tlv.telemetry.optiondata.instbitmap.switchid-20",
        "InstbitmapIngressegressportid": "genevewithtelemetry.header.tlv.telemetry.optiondata.instbitmap.ingressegressportid-21",
        "InstbitmapHoplatency": "genevewithtelemetry.header.tlv.telemetry.optiondata.instbitmap.hoplatency-22",
        "InstbitmapQueue": "genevewithtelemetry.header.tlv.telemetry.optiondata.instbitmap.queue-23",
        "InstbitmapIngresstimestamp": "genevewithtelemetry.header.tlv.telemetry.optiondata.instbitmap.ingresstimestamp-24",
        "InstbitmapEgresstimestamp": "genevewithtelemetry.header.tlv.telemetry.optiondata.instbitmap.egresstimestamp-25",
        "InstbitmapIngressegressportidwide": "genevewithtelemetry.header.tlv.telemetry.optiondata.instbitmap.ingressegressportidwide-26",
        "InstbitmapEgressporttxutil": "genevewithtelemetry.header.tlv.telemetry.optiondata.instbitmap.egressporttxutil-27",
        "InstbitmapReserved07": "genevewithtelemetry.header.tlv.telemetry.optiondata.instbitmap.reserved07-28",
        "InstbitmapChecksumcomplement": "genevewithtelemetry.header.tlv.telemetry.optiondata.instbitmap.checksumcomplement-29",
        "OptiondataReserved16": "genevewithtelemetry.header.tlv.telemetry.optiondata.reserved16-30",
        "IntmetadatastackSid": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.sid-31",
        "Ingressegressportid32Ipid": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.ingressegressportid32.ipid-32",
        "Ingressegressportid32Epid": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.ingressegressportid32.epid-33",
        "IntmetadatastackHl": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.hl-34",
        "QueueidoccupancyQid": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.queueidoccupancy.qid-35",
        "QueueidoccupancyQo": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.queueidoccupancy.qo-36",
        "IntmetadatastackIt": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.it-37",
        "IntmetadatastackEt": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.et-38",
        "Ingressegressportid64Ipid32": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.ingressegressportid64.ipid32-39",
        "Ingressegressportid64Epid32": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.ingressegressportid64.epid32-40",
        "IntmetadatastackEptu32": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.eptu32-41",
        "IntmetadatastackReservedmeta": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.reservedmeta-42",
        "IntmetadatastackDefault": "genevewithtelemetry.header.tlv.telemetry.optiondata.intmetadatastack.-43",
    }

    def __init__(self, parent, list_op=False):
        super(Genevewithtelemetry, self).__init__(parent, list_op)

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
        Default Value: 0x6558
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
        Display Name: Reserved8
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved8"])
        )

    @property
    def HeaderLength(self):
        """
        Display Name: Length of data field
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength"]))

    @property
    def TelemetryOptionclass(self):
        """
        Display Name: Option Class
        Default Value: 0x00AB
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
        Available enum values: Hop-by-Hop, 1, Destination, 2
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
        Default Value: 31
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
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataVersion"])
        )

    @property
    def OptiondataReplication(self):
        """
        Display Name: Replication
        Default Value: 0
        Value Format: decimal
        Available enum values: No replication requested, 0, Port Level replication requested, 1, Next hop level replication requested, 2, Port-level and Next-hop-level replication requested, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataReplication"])
        )

    @property
    def OptiondataCopy(self):
        """
        Display Name: Copy
        Default Value: 0
        Value Format: decimal
        Available enum values: Original Packet, 0, Replicated Packet, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataCopy"])
        )

    @property
    def OptiondataExceeded(self):
        """
        Display Name: Max Hop Count Exceeded
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
        Display Name: MTU Exceeded
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataMtuexceeded"])
        )

    @property
    def OptiondataReserved10(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataReserved10"])
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
    def InstbitmapSwitchid(self):
        """
        Display Name: Switch ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstbitmapSwitchid"])
        )

    @property
    def InstbitmapIngressegressportid(self):
        """
        Display Name: Ingress-Egress Port ID(short)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["InstbitmapIngressegressportid"]),
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
    def InstbitmapIngressegressportidwide(self):
        """
        Display Name: Ingress-Egress Port ID(wide)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["InstbitmapIngressegressportidwide"]),
        )

    @property
    def InstbitmapEgressporttxutil(self):
        """
        Display Name: Egress Port TX Utilization
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InstbitmapEgressporttxutil"])
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
    def OptiondataReserved16(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptiondataReserved16"])
        )

    @property
    def IntmetadatastackSid(self):
        """
        Display Name: Switch Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadatastackSid"])
        )

    @property
    def Ingressegressportid32Ipid(self):
        """
        Display Name: Ingress Port ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ingressegressportid32Ipid"])
        )

    @property
    def Ingressegressportid32Epid(self):
        """
        Display Name: Egress Port Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ingressegressportid32Epid"])
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
    def Ingressegressportid64Ipid32(self):
        """
        Display Name: Ingress Port ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ingressegressportid64Ipid32"])
        )

    @property
    def Ingressegressportid64Epid32(self):
        """
        Display Name: Egress Port Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ingressegressportid64Epid32"])
        )

    @property
    def IntmetadatastackEptu32(self):
        """
        Display Name: Egress Port TX Utilization
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadatastackEptu32"])
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
