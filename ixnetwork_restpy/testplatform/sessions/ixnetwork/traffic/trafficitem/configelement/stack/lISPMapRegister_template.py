from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LISPMapRegister(Base):
    __slots__ = ()
    _SDM_NAME = "lISPMapRegister"
    _SDM_ATT_MAP = {
        "HeaderType": "lISPMapRegister.header.type-1",
        "HeaderP": "lISPMapRegister.header.p-2",
        "HeaderReserved": "lISPMapRegister.header.reserved-3",
        "HeaderM": "lISPMapRegister.header.m-4",
        "HeaderRecordcount": "lISPMapRegister.header.recordcount-5",
        "HeaderNonce": "lISPMapRegister.header.nonce-6",
        "HeaderKeyid": "lISPMapRegister.header.keyid-7",
        "HeaderAuthdatalen": "lISPMapRegister.header.authdatalen-8",
        "HeaderAuthdata": "lISPMapRegister.header.authdata-9",
        "RecordTtl": "lISPMapRegister.header.eidrecord.record.ttl-10",
        "RecordLoccnt": "lISPMapRegister.header.eidrecord.record.loccnt-11",
        "RecordEIDmasklen": "lISPMapRegister.header.eidrecord.record.eIDmasklen-12",
        "RecordACT": "lISPMapRegister.header.eidrecord.record.aCT-13",
        "RecordA": "lISPMapRegister.header.eidrecord.record.a-14",
        "RecordRecreserved": "lISPMapRegister.header.eidrecord.record.recreserved-15",
        "RecordRsvd": "lISPMapRegister.header.eidrecord.record.rsvd-16",
        "RecordMapvernumber": "lISPMapRegister.header.eidrecord.record.mapvernumber-17",
        "Ipv4eidEidipv4afi": "lISPMapRegister.header.eidrecord.record.eidafiprefix.ipv4eid.eidipv4afi-18",
        "Ipv4eidEidprefix": "lISPMapRegister.header.eidrecord.record.eidafiprefix.ipv4eid.eidprefix-19",
        "Ipv6eidEidipv6afi": "lISPMapRegister.header.eidrecord.record.eidafiprefix.ipv6eid.eidipv6afi-20",
        "Ipv6eidEidprefix": "lISPMapRegister.header.eidrecord.record.eidafiprefix.ipv6eid.eidprefix-21",
        "AfiAfi": "lISPMapRegister.header.eidrecord.record.eidafiprefix.afi.afi-22",
        "AfiRsvd1": "lISPMapRegister.header.eidrecord.record.eidafiprefix.afi.rsvd1-23",
        "AfiFlags": "lISPMapRegister.header.eidrecord.record.eidafiprefix.afi.flags-24",
        "AfiType": "lISPMapRegister.header.eidrecord.record.eidafiprefix.afi.type-25",
        "AfiRsvd2": "lISPMapRegister.header.eidrecord.record.eidafiprefix.afi.rsvd2-26",
        "AfiLength": "lISPMapRegister.header.eidrecord.record.eidafiprefix.afi.length-27",
        "AfiInstanceid": "lISPMapRegister.header.eidrecord.record.eidafiprefix.afi.instanceid-28",
        "EidafiprefixIpv4eidEidipv4afi": "lISPMapRegister.header.eidrecord.record.eidafiprefix.afi.eidafiprefix.ipv4eid.eidipv4afi-29",
        "EidafiprefixIpv4eidEidprefix": "lISPMapRegister.header.eidrecord.record.eidafiprefix.afi.eidafiprefix.ipv4eid.eidprefix-30",
        "EidafiprefixIpv6eidEidipv6afi": "lISPMapRegister.header.eidrecord.record.eidafiprefix.afi.eidafiprefix.ipv6eid.eidipv6afi-31",
        "EidafiprefixIpv6eidEidprefix": "lISPMapRegister.header.eidrecord.record.eidafiprefix.afi.eidafiprefix.ipv6eid.eidprefix-32",
        "LocatorPriority": "lISPMapRegister.header.eidrecord.record.locatorrecords.locator.priority-33",
        "LocatorWeight": "lISPMapRegister.header.eidrecord.record.locatorrecords.locator.weight-34",
        "LocatorMpriority": "lISPMapRegister.header.eidrecord.record.locatorrecords.locator.mpriority-35",
        "LocatorMweight": "lISPMapRegister.header.eidrecord.record.locatorrecords.locator.mweight-36",
        "LocatorUnusedflags": "lISPMapRegister.header.eidrecord.record.locatorrecords.locator.unusedflags-37",
        "LocatorL": "lISPMapRegister.header.eidrecord.record.locatorrecords.locator.l-38",
        "LocatorLocp": "lISPMapRegister.header.eidrecord.record.locatorrecords.locator.locp-39",
        "LocatorR": "lISPMapRegister.header.eidrecord.record.locatorrecords.locator.r-40",
        "Ipv4locLocipv4afi": "lISPMapRegister.header.eidrecord.record.locatorrecords.locator.locafiprefix.ipv4loc.locipv4afi-41",
        "Ipv4locLocprefix": "lISPMapRegister.header.eidrecord.record.locatorrecords.locator.locafiprefix.ipv4loc.locprefix-42",
        "Ipv6locLocipv6afi": "lISPMapRegister.header.eidrecord.record.locatorrecords.locator.locafiprefix.ipv6loc.locipv6afi-43",
        "Ipv6locLocprefix": "lISPMapRegister.header.eidrecord.record.locatorrecords.locator.locafiprefix.ipv6loc.locprefix-44",
    }

    def __init__(self, parent, list_op=False):
        super(LISPMapRegister, self).__init__(parent, list_op)

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0x3
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
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderM(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderM"]))

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
    def HeaderKeyid(self):
        """
        Display Name: Key ID
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderKeyid"]))

    @property
    def HeaderAuthdatalen(self):
        """
        Display Name: Auth Data Length
        Default Value: 0x0014
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderAuthdatalen"])
        )

    @property
    def HeaderAuthdata(self):
        """
        Display Name: Auth Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderAuthdata"])
        )

    @property
    def RecordTtl(self):
        """
        Display Name: Record TTL
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
    def RecordRsvd(self):
        """
        Display Name: Rsvd
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RecordRsvd"]))

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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
