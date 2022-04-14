from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Intmetadata(Base):
    __slots__ = ()
    _SDM_NAME = "intmetadata"
    _SDM_ATT_MAP = {
        "IntmetadataVersion": "intmetadata.intmetadata.version-1",
        "IntmetadataReplication": "intmetadata.intmetadata.replication-2",
        "IntmetadataCopy": "intmetadata.intmetadata.copy-3",
        "IntmetadataExceeded": "intmetadata.intmetadata.exceeded-4",
        "IntmetadataMtuexceeded": "intmetadata.intmetadata.mtuexceeded-5",
        "IntmetadataReserved10": "intmetadata.intmetadata.reserved10-6",
        "IntmetadataHopml": "intmetadata.intmetadata.hopml-7",
        "IntmetadataRemaininghopcount": "intmetadata.intmetadata.remaininghopcount-8",
        "InstbitmapSwitchid": "intmetadata.intmetadata.instbitmap.switchid-9",
        "InstbitmapIngressegressportid": "intmetadata.intmetadata.instbitmap.ingressegressportid-10",
        "InstbitmapHoplatency": "intmetadata.intmetadata.instbitmap.hoplatency-11",
        "InstbitmapQueue": "intmetadata.intmetadata.instbitmap.queue-12",
        "InstbitmapIngresstimestamp": "intmetadata.intmetadata.instbitmap.ingresstimestamp-13",
        "InstbitmapEgresstimestamp": "intmetadata.intmetadata.instbitmap.egresstimestamp-14",
        "InstbitmapIngressegressportidwide": "intmetadata.intmetadata.instbitmap.ingressegressportidwide-15",
        "InstbitmapEgressporttxutil": "intmetadata.intmetadata.instbitmap.egressporttxutil-16",
        "InstbitmapReserved07": "intmetadata.intmetadata.instbitmap.reserved07-17",
        "InstbitmapChecksumcomplement": "intmetadata.intmetadata.instbitmap.checksumcomplement-18",
        "IntmetadataReserved16": "intmetadata.intmetadata.reserved16-19",
        "IntmetadatastackSid": "intmetadata.intmetadata.intmetadatastack.sid-20",
        "Ingressegressportid32Ipid": "intmetadata.intmetadata.intmetadatastack.ingressegressportid32.ipid-21",
        "Ingressegressportid32Epid": "intmetadata.intmetadata.intmetadatastack.ingressegressportid32.epid-22",
        "IntmetadatastackHl": "intmetadata.intmetadata.intmetadatastack.hl-23",
        "QueueidoccupancyQid": "intmetadata.intmetadata.intmetadatastack.queueidoccupancy.qid-24",
        "QueueidoccupancyQo": "intmetadata.intmetadata.intmetadatastack.queueidoccupancy.qo-25",
        "IntmetadatastackIt": "intmetadata.intmetadata.intmetadatastack.it-26",
        "IntmetadatastackEt": "intmetadata.intmetadata.intmetadatastack.et-27",
        "Ingressegressportid64Ipid32": "intmetadata.intmetadata.intmetadatastack.ingressegressportid64.ipid32-28",
        "Ingressegressportid64Epid32": "intmetadata.intmetadata.intmetadatastack.ingressegressportid64.epid32-29",
        "IntmetadatastackEptu32": "intmetadata.intmetadata.intmetadatastack.eptu32-30",
        "IntmetadatastackReservedmeta": "intmetadata.intmetadata.intmetadatastack.reservedmeta-31",
        "IntmetadatastackDefault": "intmetadata.intmetadata.intmetadatastack.-32",
    }

    def __init__(self, parent, list_op=False):
        super(Intmetadata, self).__init__(parent, list_op)

    @property
    def IntmetadataVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadataVersion"])
        )

    @property
    def IntmetadataReplication(self):
        """
        Display Name: Replication
        Default Value: 0
        Value Format: decimal
        Available enum values: No replication requested, 0, Port Level replication requested, 1, Next hop level replication requested, 2, Port-level and Next-hop-level replication requested, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadataReplication"])
        )

    @property
    def IntmetadataCopy(self):
        """
        Display Name: Copy
        Default Value: 0
        Value Format: decimal
        Available enum values: Original Packet, 0, Replicated Packet, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadataCopy"])
        )

    @property
    def IntmetadataExceeded(self):
        """
        Display Name: Max Hop Count Exceeded
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadataExceeded"])
        )

    @property
    def IntmetadataMtuexceeded(self):
        """
        Display Name: MTU Exceeded
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadataMtuexceeded"])
        )

    @property
    def IntmetadataReserved10(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadataReserved10"])
        )

    @property
    def IntmetadataHopml(self):
        """
        Display Name: Hop Metadata Length (x4 bytes)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadataHopml"])
        )

    @property
    def IntmetadataRemaininghopcount(self):
        """
        Display Name: Remaining Hop Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadataRemaininghopcount"])
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
    def IntmetadataReserved16(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IntmetadataReserved16"])
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
