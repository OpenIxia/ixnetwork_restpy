from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LISPMapRequest(Base):
    __slots__ = ()
    _SDM_NAME = "lISPMapRequest"
    _SDM_ATT_MAP = {
        "HeaderType": "lISPMapRequest.header.type-1",
        "HeaderA": "lISPMapRequest.header.a-2",
        "HeaderM": "lISPMapRequest.header.M-3",
        "HeaderP": "lISPMapRequest.header.p-4",
        "HeaderS": "lISPMapRequest.header.S-5",
        "HeaderReserved": "lISPMapRequest.header.reserved-6",
        "HeaderIRC_RLOC_Count": "lISPMapRequest.header.IRC_RLOC_Count-7",
        "HeaderRecordcount": "lISPMapRequest.header.recordcount-8",
        "HeaderNonce": "lISPMapRequest.header.nonce-9",
        "Ipv4sourceeidSourceeidipv4afi": "lISPMapRequest.header.Source_EID_AFI_Address.ipv4sourceeid.sourceeidipv4afi-10",
        "Ipv4sourceeidSourceeidprefix": "lISPMapRequest.header.Source_EID_AFI_Address.ipv4sourceeid.sourceeidprefix-11",
        "Ipv6sourceeidSourceeidipv6afi": "lISPMapRequest.header.Source_EID_AFI_Address.ipv6sourceeid.sourceeidipv6afi-12",
        "Ipv6sourceeidSourceeidprefix": "lISPMapRequest.header.Source_EID_AFI_Address.ipv6sourceeid.sourceeidprefix-13",
        "AfiAfi": "lISPMapRequest.header.Source_EID_AFI_Address.afi.afi-14",
        "AfiRsvd1": "lISPMapRequest.header.Source_EID_AFI_Address.afi.rsvd1-15",
        "AfiFlags": "lISPMapRequest.header.Source_EID_AFI_Address.afi.flags-16",
        "AfiType": "lISPMapRequest.header.Source_EID_AFI_Address.afi.type-17",
        "AfiRsvd2": "lISPMapRequest.header.Source_EID_AFI_Address.afi.rsvd2-18",
        "AfiLength": "lISPMapRequest.header.Source_EID_AFI_Address.afi.length-19",
        "AfiInstanceid": "lISPMapRequest.header.Source_EID_AFI_Address.afi.instanceid-20",
        "Ipv4eidEidipv4afi": "lISPMapRequest.header.Source_EID_AFI_Address.afi.eidafiprefix.ipv4eid.eidipv4afi-21",
        "Ipv4eidEidprefix": "lISPMapRequest.header.Source_EID_AFI_Address.afi.eidafiprefix.ipv4eid.eidprefix-22",
        "Ipv6eidEidipv6afi": "lISPMapRequest.header.Source_EID_AFI_Address.afi.eidafiprefix.ipv6eid.eidipv6afi-23",
        "Ipv6eidEidprefix": "lISPMapRequest.header.Source_EID_AFI_Address.afi.eidafiprefix.ipv6eid.eidprefix-24",
        "Ipv4itrrlocItrrlocipv4afi": "lISPMapRequest.header.ITR_RLOC_AFI_Address.ipv4itrrloc.itrrlocipv4afi-25",
        "Ipv4itrrlocItrrlocaddress": "lISPMapRequest.header.ITR_RLOC_AFI_Address.ipv4itrrloc.itrrlocaddress-26",
        "Ipv6itrrlocItrrlocipv6afi": "lISPMapRequest.header.ITR_RLOC_AFI_Address.ipv6itrrloc.itrrlocipv6afi-27",
        "Ipv6itrrlocItrrlocaddress": "lISPMapRequest.header.ITR_RLOC_AFI_Address.ipv6itrrloc.itrrlocaddress-28",
        "RecordRecreserved": "lISPMapRequest.header.EID Record.record.recreserved-29",
        "RecordEIDmasklen": "lISPMapRequest.header.EID Record.record.eIDmasklen-30",
        "EidafiprefixIpv4eidEidipv4afi": "lISPMapRequest.header.EID Record.record.eidafiprefix.ipv4eid.eidipv4afi-31",
        "EidafiprefixIpv4eidEidprefix": "lISPMapRequest.header.EID Record.record.eidafiprefix.ipv4eid.eidprefix-32",
        "EidafiprefixIpv6eidEidipv6afi": "lISPMapRequest.header.EID Record.record.eidafiprefix.ipv6eid.eidipv6afi-33",
        "EidafiprefixIpv6eidEidprefix": "lISPMapRequest.header.EID Record.record.eidafiprefix.ipv6eid.eidprefix-34",
        "EidafiprefixAfiAfi": "lISPMapRequest.header.EID Record.record.eidafiprefix.afi.afi-35",
        "EidafiprefixAfiRsvd1": "lISPMapRequest.header.EID Record.record.eidafiprefix.afi.rsvd1-36",
        "EidafiprefixAfiFlags": "lISPMapRequest.header.EID Record.record.eidafiprefix.afi.flags-37",
        "EidafiprefixAfiType": "lISPMapRequest.header.EID Record.record.eidafiprefix.afi.type-38",
        "EidafiprefixAfiRsvd2": "lISPMapRequest.header.EID Record.record.eidafiprefix.afi.rsvd2-39",
        "EidafiprefixAfiLength": "lISPMapRequest.header.EID Record.record.eidafiprefix.afi.length-40",
        "EidafiprefixAfiInstanceid": "lISPMapRequest.header.EID Record.record.eidafiprefix.afi.instanceid-41",
        "AfiEidafiprefixIpv4eidEidipv4afi": "lISPMapRequest.header.EID Record.record.eidafiprefix.afi.eidafiprefix.ipv4eid.eidipv4afi-42",
        "AfiEidafiprefixIpv4eidEidprefix": "lISPMapRequest.header.EID Record.record.eidafiprefix.afi.eidafiprefix.ipv4eid.eidprefix-43",
        "AfiEidafiprefixIpv6eidEidipv6afi": "lISPMapRequest.header.EID Record.record.eidafiprefix.afi.eidafiprefix.ipv6eid.eidipv6afi-44",
        "AfiEidafiprefixIpv6eidEidprefix": "lISPMapRequest.header.EID Record.record.eidafiprefix.afi.eidafiprefix.ipv6eid.eidprefix-45",
        "RecordTtl": "lISPMapRequest.header.Map-Reply Record.Record.ttl-46",
        "RecordLoccnt": "lISPMapRequest.header.Map-Reply Record.Record.loccnt-47",
        "RecordEIDmasklen": "lISPMapRequest.header.Map-Reply Record.Record.eIDmasklen-48",
        "RecordACT": "lISPMapRequest.header.Map-Reply Record.Record.aCT-49",
        "RecordA": "lISPMapRequest.header.Map-Reply Record.Record.a-50",
        "RecordRecreserved": "lISPMapRequest.header.Map-Reply Record.Record.recreserved-51",
        "RecordMapvernumber": "lISPMapRequest.header.Map-Reply Record.Record.mapvernumber-52",
        "RecordEidafiprefixIpv4eidEidipv4afi": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.ipv4eid.eidipv4afi-53",
        "RecordEidafiprefixIpv4eidEidprefix": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.ipv4eid.eidprefix-54",
        "RecordEidafiprefixIpv6eidEidipv6afi": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.ipv6eid.eidipv6afi-55",
        "RecordEidafiprefixIpv6eidEidprefix": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.ipv6eid.eidprefix-56",
        "RecordEidafiprefixAfiAfi": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.afi.afi-57",
        "RecordEidafiprefixAfiRsvd1": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.afi.rsvd1-58",
        "RecordEidafiprefixAfiFlags": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.afi.flags-59",
        "RecordEidafiprefixAfiType": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.afi.type-60",
        "RecordEidafiprefixAfiRsvd2": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.afi.rsvd2-61",
        "RecordEidafiprefixAfiLength": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.afi.length-62",
        "RecordEidafiprefixAfiInstanceid": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.afi.instanceid-63",
        "EidafiprefixAfiEidafiprefixIpv4eidEidipv4afi": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.afi.eidafiprefix.ipv4eid.eidipv4afi-64",
        "EidafiprefixAfiEidafiprefixIpv4eidEidprefix": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.afi.eidafiprefix.ipv4eid.eidprefix-65",
        "EidafiprefixAfiEidafiprefixIpv6eidEidipv6afi": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.afi.eidafiprefix.ipv6eid.eidipv6afi-66",
        "EidafiprefixAfiEidafiprefixIpv6eidEidprefix": "lISPMapRequest.header.Map-Reply Record.Record.eidafiprefix.afi.eidafiprefix.ipv6eid.eidprefix-67",
        "LocatorPriority": "lISPMapRequest.header.Map-Reply Record.Record.locatorrecords.locator.priority-68",
        "LocatorWeight": "lISPMapRequest.header.Map-Reply Record.Record.locatorrecords.locator.weight-69",
        "LocatorMpriority": "lISPMapRequest.header.Map-Reply Record.Record.locatorrecords.locator.mpriority-70",
        "LocatorMweight": "lISPMapRequest.header.Map-Reply Record.Record.locatorrecords.locator.mweight-71",
        "LocatorUnusedflags": "lISPMapRequest.header.Map-Reply Record.Record.locatorrecords.locator.unusedflags-72",
        "LocatorL": "lISPMapRequest.header.Map-Reply Record.Record.locatorrecords.locator.l-73",
        "LocatorLocp": "lISPMapRequest.header.Map-Reply Record.Record.locatorrecords.locator.locp-74",
        "LocatorR": "lISPMapRequest.header.Map-Reply Record.Record.locatorrecords.locator.r-75",
        "Ipv4locLocipv4afi": "lISPMapRequest.header.Map-Reply Record.Record.locatorrecords.locator.locafiprefix.ipv4loc.locipv4afi-76",
        "Ipv4locLocprefix": "lISPMapRequest.header.Map-Reply Record.Record.locatorrecords.locator.locafiprefix.ipv4loc.locprefix-77",
        "Ipv6locLocipv6afi": "lISPMapRequest.header.Map-Reply Record.Record.locatorrecords.locator.locafiprefix.ipv6loc.locipv6afi-78",
        "Ipv6locLocprefix": "lISPMapRequest.header.Map-Reply Record.Record.locatorrecords.locator.locafiprefix.ipv6loc.locprefix-79",
        "HeaderMapping_Protocol_Data": "lISPMapRequest.header.Mapping_Protocol_Data-80",
    }

    def __init__(self, parent, list_op=False):
        super(LISPMapRequest, self).__init__(parent, list_op)

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderA(self):
        """
        Display Name: A
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderA"]))

    @property
    def HeaderM(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderM"]))

    @property
    def HeaderP(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderP"]))

    @property
    def HeaderS(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderS"]))

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderIRC_RLOC_Count(self):
        """
        Display Name: IRC
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderIRC_RLOC_Count"])
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
    def Ipv4sourceeidSourceeidipv4afi(self):
        """
        Display Name: IPv4 AFI
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv4sourceeidSourceeidipv4afi"]),
        )

    @property
    def Ipv4sourceeidSourceeidprefix(self):
        """
        Display Name: IPv4 Source EID Prefix
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4sourceeidSourceeidprefix"])
        )

    @property
    def Ipv6sourceeidSourceeidipv6afi(self):
        """
        Display Name: IPv6 AFI
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv6sourceeidSourceeidipv6afi"]),
        )

    @property
    def Ipv6sourceeidSourceeidprefix(self):
        """
        Display Name: IPv6 Source EID Prefix
        Default Value: 00::00
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6sourceeidSourceeidprefix"])
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
    def Ipv4itrrlocItrrlocipv4afi(self):
        """
        Display Name: IPv4 AFI
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4itrrlocItrrlocipv4afi"])
        )

    @property
    def Ipv4itrrlocItrrlocaddress(self):
        """
        Display Name: IPv4 EID Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4itrrlocItrrlocaddress"])
        )

    @property
    def Ipv6itrrlocItrrlocipv6afi(self):
        """
        Display Name: IPv6 AFI
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6itrrlocItrrlocipv6afi"])
        )

    @property
    def Ipv6itrrlocItrrlocaddress(self):
        """
        Display Name: IPv6 EID Prefix
        Default Value: 00::00
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6itrrlocItrrlocaddress"])
        )

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
    def EidafiprefixAfiAfi(self):
        """
        Display Name: AFI
        Default Value: 16387
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EidafiprefixAfiAfi"])
        )

    @property
    def EidafiprefixAfiRsvd1(self):
        """
        Display Name: Rsvd1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EidafiprefixAfiRsvd1"])
        )

    @property
    def EidafiprefixAfiFlags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EidafiprefixAfiFlags"])
        )

    @property
    def EidafiprefixAfiType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EidafiprefixAfiType"])
        )

    @property
    def EidafiprefixAfiRsvd2(self):
        """
        Display Name: Rsvd2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EidafiprefixAfiRsvd2"])
        )

    @property
    def EidafiprefixAfiLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EidafiprefixAfiLength"])
        )

    @property
    def EidafiprefixAfiInstanceid(self):
        """
        Display Name: InstanceID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EidafiprefixAfiInstanceid"])
        )

    @property
    def AfiEidafiprefixIpv4eidEidipv4afi(self):
        """
        Display Name: IPv4 AFI
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AfiEidafiprefixIpv4eidEidipv4afi"]),
        )

    @property
    def AfiEidafiprefixIpv4eidEidprefix(self):
        """
        Display Name: IPv4 EID Prefix
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AfiEidafiprefixIpv4eidEidprefix"]),
        )

    @property
    def AfiEidafiprefixIpv6eidEidipv6afi(self):
        """
        Display Name: IPv6 AFI
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AfiEidafiprefixIpv6eidEidipv6afi"]),
        )

    @property
    def AfiEidafiprefixIpv6eidEidprefix(self):
        """
        Display Name: IPv6 EID Prefix
        Default Value: 00::00
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AfiEidafiprefixIpv6eidEidprefix"]),
        )

    @property
    def RecordTtl(self):
        """
        Display Name: ttl
        Default Value: 1440
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
    def RecordEidafiprefixIpv4eidEidipv4afi(self):
        """
        Display Name: IPv4 AFI
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RecordEidafiprefixIpv4eidEidipv4afi"]
            ),
        )

    @property
    def RecordEidafiprefixIpv4eidEidprefix(self):
        """
        Display Name: IPv4 EID Prefix
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RecordEidafiprefixIpv4eidEidprefix"]
            ),
        )

    @property
    def RecordEidafiprefixIpv6eidEidipv6afi(self):
        """
        Display Name: IPv6 AFI
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RecordEidafiprefixIpv6eidEidipv6afi"]
            ),
        )

    @property
    def RecordEidafiprefixIpv6eidEidprefix(self):
        """
        Display Name: IPv6 EID Prefix
        Default Value: 00::00
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RecordEidafiprefixIpv6eidEidprefix"]
            ),
        )

    @property
    def RecordEidafiprefixAfiAfi(self):
        """
        Display Name: AFI
        Default Value: 16387
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RecordEidafiprefixAfiAfi"])
        )

    @property
    def RecordEidafiprefixAfiRsvd1(self):
        """
        Display Name: Rsvd1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RecordEidafiprefixAfiRsvd1"])
        )

    @property
    def RecordEidafiprefixAfiFlags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RecordEidafiprefixAfiFlags"])
        )

    @property
    def RecordEidafiprefixAfiType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RecordEidafiprefixAfiType"])
        )

    @property
    def RecordEidafiprefixAfiRsvd2(self):
        """
        Display Name: Rsvd2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RecordEidafiprefixAfiRsvd2"])
        )

    @property
    def RecordEidafiprefixAfiLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RecordEidafiprefixAfiLength"])
        )

    @property
    def RecordEidafiprefixAfiInstanceid(self):
        """
        Display Name: InstanceID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RecordEidafiprefixAfiInstanceid"]),
        )

    @property
    def EidafiprefixAfiEidafiprefixIpv4eidEidipv4afi(self):
        """
        Display Name: IPv4 AFI
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EidafiprefixAfiEidafiprefixIpv4eidEidipv4afi"]
            ),
        )

    @property
    def EidafiprefixAfiEidafiprefixIpv4eidEidprefix(self):
        """
        Display Name: IPv4 EID Prefix
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EidafiprefixAfiEidafiprefixIpv4eidEidprefix"]
            ),
        )

    @property
    def EidafiprefixAfiEidafiprefixIpv6eidEidipv6afi(self):
        """
        Display Name: IPv6 AFI
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EidafiprefixAfiEidafiprefixIpv6eidEidipv6afi"]
            ),
        )

    @property
    def EidafiprefixAfiEidafiprefixIpv6eidEidprefix(self):
        """
        Display Name: IPv6 EID Prefix
        Default Value: 00::00
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EidafiprefixAfiEidafiprefixIpv6eidEidprefix"]
            ),
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
