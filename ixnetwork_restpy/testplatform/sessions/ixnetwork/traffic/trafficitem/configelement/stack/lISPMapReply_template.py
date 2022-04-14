from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LISPMapReply(Base):
    __slots__ = ()
    _SDM_NAME = "lISPMapReply"
    _SDM_ATT_MAP = {
        "HeaderType": "lISPMapReply.header.type-1",
        "HeaderP": "lISPMapReply.header.p-2",
        "HeaderE": "lISPMapReply.header.E-3",
        "HeaderReserved": "lISPMapReply.header.reserved-4",
        "HeaderRecordcount": "lISPMapReply.header.recordcount-5",
        "HeaderNonce": "lISPMapReply.header.nonce-6",
        "RecordTtl": "lISPMapReply.header.eidrecord.record.ttl-7",
        "RecordLoccnt": "lISPMapReply.header.eidrecord.record.loccnt-8",
        "RecordEIDmasklen": "lISPMapReply.header.eidrecord.record.eIDmasklen-9",
        "RecordACT": "lISPMapReply.header.eidrecord.record.aCT-10",
        "RecordA": "lISPMapReply.header.eidrecord.record.a-11",
        "RecordRecreserved": "lISPMapReply.header.eidrecord.record.recreserved-12",
        "RecordMapvernumber": "lISPMapReply.header.eidrecord.record.mapvernumber-13",
        "Ipv4eidEidipv4afi": "lISPMapReply.header.eidrecord.record.eidafiprefix.ipv4eid.eidipv4afi-14",
        "Ipv4eidEidprefix": "lISPMapReply.header.eidrecord.record.eidafiprefix.ipv4eid.eidprefix-15",
        "Ipv6eidEidipv6afi": "lISPMapReply.header.eidrecord.record.eidafiprefix.ipv6eid.eidipv6afi-16",
        "Ipv6eidEidprefix": "lISPMapReply.header.eidrecord.record.eidafiprefix.ipv6eid.eidprefix-17",
        "AfiAfi": "lISPMapReply.header.eidrecord.record.eidafiprefix.afi.afi-18",
        "AfiRsvd1": "lISPMapReply.header.eidrecord.record.eidafiprefix.afi.rsvd1-19",
        "AfiFlags": "lISPMapReply.header.eidrecord.record.eidafiprefix.afi.flags-20",
        "AfiType": "lISPMapReply.header.eidrecord.record.eidafiprefix.afi.type-21",
        "AfiRsvd2": "lISPMapReply.header.eidrecord.record.eidafiprefix.afi.rsvd2-22",
        "AfiLength": "lISPMapReply.header.eidrecord.record.eidafiprefix.afi.length-23",
        "AfiInstanceid": "lISPMapReply.header.eidrecord.record.eidafiprefix.afi.instanceid-24",
        "EidafiprefixIpv4eidEidipv4afi": "lISPMapReply.header.eidrecord.record.eidafiprefix.afi.eidafiprefix.ipv4eid.eidipv4afi-25",
        "EidafiprefixIpv4eidEidprefix": "lISPMapReply.header.eidrecord.record.eidafiprefix.afi.eidafiprefix.ipv4eid.eidprefix-26",
        "EidafiprefixIpv6eidEidipv6afi": "lISPMapReply.header.eidrecord.record.eidafiprefix.afi.eidafiprefix.ipv6eid.eidipv6afi-27",
        "EidafiprefixIpv6eidEidprefix": "lISPMapReply.header.eidrecord.record.eidafiprefix.afi.eidafiprefix.ipv6eid.eidprefix-28",
        "LocatorPriority": "lISPMapReply.header.eidrecord.record.locatorrecords.locator.priority-29",
        "LocatorWeight": "lISPMapReply.header.eidrecord.record.locatorrecords.locator.weight-30",
        "LocatorMpriority": "lISPMapReply.header.eidrecord.record.locatorrecords.locator.mpriority-31",
        "LocatorMweight": "lISPMapReply.header.eidrecord.record.locatorrecords.locator.mweight-32",
        "LocatorUnusedflags": "lISPMapReply.header.eidrecord.record.locatorrecords.locator.unusedflags-33",
        "LocatorL": "lISPMapReply.header.eidrecord.record.locatorrecords.locator.l-34",
        "LocatorLocp": "lISPMapReply.header.eidrecord.record.locatorrecords.locator.locp-35",
        "LocatorR": "lISPMapReply.header.eidrecord.record.locatorrecords.locator.r-36",
        "Ipv4locLocipv4afi": "lISPMapReply.header.eidrecord.record.locatorrecords.locator.locafiprefix.ipv4loc.locipv4afi-37",
        "Ipv4locLocprefix": "lISPMapReply.header.eidrecord.record.locatorrecords.locator.locafiprefix.ipv4loc.locprefix-38",
        "Ipv6locLocipv6afi": "lISPMapReply.header.eidrecord.record.locatorrecords.locator.locafiprefix.ipv6loc.locipv6afi-39",
        "Ipv6locLocprefix": "lISPMapReply.header.eidrecord.record.locatorrecords.locator.locafiprefix.ipv6loc.locprefix-40",
        "HeaderMapping_Protocol_Data": "lISPMapReply.header.Mapping_Protocol_Data-41",
    }

    def __init__(self, parent, list_op=False):
        super(LISPMapReply, self).__init__(parent, list_op)

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0x2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderP(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderP"]))

    @property
    def HeaderE(self):
        """
        Display Name: E
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderE"]))

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderRecordcount(self):
        """
        Display Name: Record Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRecordcount"])
        )

    @property
    def HeaderNonce(self):
        """
        Display Name: Nonce
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderNonce"]))

    @property
    def RecordTtl(self):
        """
        Display Name: ttl
        Default Value: 1441
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RecordTtl"]))

    @property
    def RecordLoccnt(self):
        """
        Display Name: Locator Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RecordLoccnt"]))

    @property
    def RecordEIDmasklen(self):
        """
        Display Name: EID Mask Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RecordEIDmasklen"])
        )

    @property
    def RecordACT(self):
        """
        Display Name: ACT
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RecordACT"]))

    @property
    def RecordA(self):
        """
        Display Name: A
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RecordA"]))

    @property
    def RecordRecreserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RecordRecreserved"])
        )

    @property
    def RecordMapvernumber(self):
        """
        Display Name: Map Version Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RecordMapvernumber"])
        )

    @property
    def Ipv4eidEidipv4afi(self):
        """
        Display Name: IPv4 AFI
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4eidEidipv4afi"])
        )

    @property
    def Ipv4eidEidprefix(self):
        """
        Display Name: IPv4 EID Prefix
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4eidEidprefix"])
        )

    @property
    def Ipv6eidEidipv6afi(self):
        """
        Display Name: IPv6 AFI
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6eidEidipv6afi"])
        )

    @property
    def Ipv6eidEidprefix(self):
        """
        Display Name: IPv6 EID Prefix
        Default Value: 00::00
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6eidEidprefix"])
        )

    @property
    def AfiAfi(self):
        """
        Display Name: AFI
        Default Value: 16387
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AfiAfi"]))

    @property
    def AfiRsvd1(self):
        """
        Display Name: Rsvd1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AfiRsvd1"]))

    @property
    def AfiFlags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AfiFlags"]))

    @property
    def AfiType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AfiType"]))

    @property
    def AfiRsvd2(self):
        """
        Display Name: Rsvd2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AfiRsvd2"]))

    @property
    def AfiLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AfiLength"]))

    @property
    def AfiInstanceid(self):
        """
        Display Name: InstanceID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AfiInstanceid"]))

    @property
    def EidafiprefixIpv4eidEidipv4afi(self):
        """
        Display Name: IPv4 AFI
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EidafiprefixIpv4eidEidipv4afi"]),
        )

    @property
    def EidafiprefixIpv4eidEidprefix(self):
        """
        Display Name: IPv4 EID Prefix
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EidafiprefixIpv4eidEidprefix"])
        )

    @property
    def EidafiprefixIpv6eidEidipv6afi(self):
        """
        Display Name: IPv6 AFI
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EidafiprefixIpv6eidEidipv6afi"]),
        )

    @property
    def EidafiprefixIpv6eidEidprefix(self):
        """
        Display Name: IPv6 EID Prefix
        Default Value: 00::00
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EidafiprefixIpv6eidEidprefix"])
        )

    @property
    def LocatorPriority(self):
        """
        Display Name: Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocatorPriority"])
        )

    @property
    def LocatorWeight(self):
        """
        Display Name: Weight
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LocatorWeight"]))

    @property
    def LocatorMpriority(self):
        """
        Display Name: M Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocatorMpriority"])
        )

    @property
    def LocatorMweight(self):
        """
        Display Name: M Weight
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocatorMweight"])
        )

    @property
    def LocatorUnusedflags(self):
        """
        Display Name: Unused Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocatorUnusedflags"])
        )

    @property
    def LocatorL(self):
        """
        Display Name: L
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LocatorL"]))

    @property
    def LocatorLocp(self):
        """
        Display Name: p
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LocatorLocp"]))

    @property
    def LocatorR(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LocatorR"]))

    @property
    def Ipv4locLocipv4afi(self):
        """
        Display Name: IPv4 AFI
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4locLocipv4afi"])
        )

    @property
    def Ipv4locLocprefix(self):
        """
        Display Name: IPv4 Locator Prefix
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4locLocprefix"])
        )

    @property
    def Ipv6locLocipv6afi(self):
        """
        Display Name: IPv6 AFI
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6locLocipv6afi"])
        )

    @property
    def Ipv6locLocprefix(self):
        """
        Display Name: IPv6 Locator Prefix
        Default Value: 00::00
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6locLocprefix"])
        )

    @property
    def HeaderMapping_Protocol_Data(self):
        """
        Display Name: Mapping Protocol Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMapping_Protocol_Data"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
