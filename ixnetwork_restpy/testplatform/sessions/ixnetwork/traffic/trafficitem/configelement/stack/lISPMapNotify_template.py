from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LISPMapNotify(Base):
    __slots__ = ()
    _SDM_NAME = "lISPMapNotify"
    _SDM_ATT_MAP = {
        "HeaderType": "lISPMapNotify.header.type-1",
        "HeaderReserved": "lISPMapNotify.header.reserved-2",
        "HeaderRecordcount": "lISPMapNotify.header.recordcount-3",
        "HeaderNonce": "lISPMapNotify.header.nonce-4",
        "HeaderKeyid": "lISPMapNotify.header.keyid-5",
        "HeaderAuthdatalen": "lISPMapNotify.header.authdatalen-6",
        "HeaderAuthdata": "lISPMapNotify.header.authdata-7",
        "RecordTtl": "lISPMapNotify.header.eidrecord.record.ttl-8",
        "RecordLoccnt": "lISPMapNotify.header.eidrecord.record.loccnt-9",
        "RecordEIDmasklen": "lISPMapNotify.header.eidrecord.record.eIDmasklen-10",
        "RecordACT": "lISPMapNotify.header.eidrecord.record.aCT-11",
        "RecordA": "lISPMapNotify.header.eidrecord.record.a-12",
        "RecordRecreserved": "lISPMapNotify.header.eidrecord.record.recreserved-13",
        "RecordRsvd": "lISPMapNotify.header.eidrecord.record.rsvd-14",
        "RecordMapvernumber": "lISPMapNotify.header.eidrecord.record.mapvernumber-15",
        "Ipv4eidEidipv4afi": "lISPMapNotify.header.eidrecord.record.eidafiprefix.ipv4eid.eidipv4afi-16",
        "Ipv4eidEidprefix": "lISPMapNotify.header.eidrecord.record.eidafiprefix.ipv4eid.eidprefix-17",
        "Ipv6eidEidipv6afi": "lISPMapNotify.header.eidrecord.record.eidafiprefix.ipv6eid.eidipv6afi-18",
        "Ipv6eidEidprefix": "lISPMapNotify.header.eidrecord.record.eidafiprefix.ipv6eid.eidprefix-19",
        "AfiAfi": "lISPMapNotify.header.eidrecord.record.eidafiprefix.afi.afi-20",
        "AfiRsvd1": "lISPMapNotify.header.eidrecord.record.eidafiprefix.afi.rsvd1-21",
        "AfiFlags": "lISPMapNotify.header.eidrecord.record.eidafiprefix.afi.flags-22",
        "AfiType": "lISPMapNotify.header.eidrecord.record.eidafiprefix.afi.type-23",
        "AfiRsvd2": "lISPMapNotify.header.eidrecord.record.eidafiprefix.afi.rsvd2-24",
        "AfiLength": "lISPMapNotify.header.eidrecord.record.eidafiprefix.afi.length-25",
        "AfiInstanceid": "lISPMapNotify.header.eidrecord.record.eidafiprefix.afi.instanceid-26",
        "EidafiprefixIpv4eidEidipv4afi": "lISPMapNotify.header.eidrecord.record.eidafiprefix.afi.eidafiprefix.ipv4eid.eidipv4afi-27",
        "EidafiprefixIpv4eidEidprefix": "lISPMapNotify.header.eidrecord.record.eidafiprefix.afi.eidafiprefix.ipv4eid.eidprefix-28",
        "EidafiprefixIpv6eidEidipv6afi": "lISPMapNotify.header.eidrecord.record.eidafiprefix.afi.eidafiprefix.ipv6eid.eidipv6afi-29",
        "EidafiprefixIpv6eidEidprefix": "lISPMapNotify.header.eidrecord.record.eidafiprefix.afi.eidafiprefix.ipv6eid.eidprefix-30",
        "LocatorPriority": "lISPMapNotify.header.eidrecord.record.locatorrecords.locator.priority-31",
        "LocatorWeight": "lISPMapNotify.header.eidrecord.record.locatorrecords.locator.weight-32",
        "LocatorMpriority": "lISPMapNotify.header.eidrecord.record.locatorrecords.locator.mpriority-33",
        "LocatorMweight": "lISPMapNotify.header.eidrecord.record.locatorrecords.locator.mweight-34",
        "LocatorUnusedflags": "lISPMapNotify.header.eidrecord.record.locatorrecords.locator.unusedflags-35",
        "LocatorL": "lISPMapNotify.header.eidrecord.record.locatorrecords.locator.l-36",
        "LocatorLocp": "lISPMapNotify.header.eidrecord.record.locatorrecords.locator.locp-37",
        "LocatorR": "lISPMapNotify.header.eidrecord.record.locatorrecords.locator.r-38",
        "Ipv4locLocipv4afi": "lISPMapNotify.header.eidrecord.record.locatorrecords.locator.locafiprefix.ipv4loc.locipv4afi-39",
        "Ipv4locLocprefix": "lISPMapNotify.header.eidrecord.record.locatorrecords.locator.locafiprefix.ipv4loc.locprefix-40",
        "Ipv6locLocipv6afi": "lISPMapNotify.header.eidrecord.record.locatorrecords.locator.locafiprefix.ipv6loc.locipv6afi-41",
        "Ipv6locLocprefix": "lISPMapNotify.header.eidrecord.record.locatorrecords.locator.locafiprefix.ipv6loc.locprefix-42",
    }

    def __init__(self, parent, list_op=False):
        super(LISPMapNotify, self).__init__(parent, list_op)

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0x4
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

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
