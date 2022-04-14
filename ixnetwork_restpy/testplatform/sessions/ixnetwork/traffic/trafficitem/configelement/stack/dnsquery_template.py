from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Dnsquery(Base):
    __slots__ = ()
    _SDM_NAME = "dns_query"
    _SDM_ATT_MAP = {
        "HeaderTid": "dns_query.header.tid-1",
        "DnsflagsQRBit": "dns_query.header.dnsflags.QRBit-2",
        "DnsflagsOpcode": "dns_query.header.dnsflags.opcode-3",
        "DnsflagsAABit": "dns_query.header.dnsflags.AABit-4",
        "DnsflagsTCBit": "dns_query.header.dnsflags.TCBit-5",
        "DnsflagsRDBit": "dns_query.header.dnsflags.RDBit-6",
        "DnsflagsRABit": "dns_query.header.dnsflags.RABit-7",
        "DnsflagsZBit": "dns_query.header.dnsflags.ZBit-8",
        "DnsflagsADBit": "dns_query.header.dnsflags.ADBit-9",
        "DnsflagsCDBit": "dns_query.header.dnsflags.CDBit-10",
        "DnsflagsRcode": "dns_query.header.dnsflags.rcode-11",
        "HeaderQCount": "dns_query.header.QCount-12",
        "HeaderACount": "dns_query.header.ACount-13",
        "HeaderAuthCount": "dns_query.header.AuthCount-14",
        "HeaderInfoCount": "dns_query.header.InfoCount-15",
        "QueriesLength": "dns_query.header.queries.length-16",
        "QueriesName": "dns_query.header.queries.Name-17",
        "QueriesType": "dns_query.header.queries.Type-18",
        "QueriesClass": "dns_query.header.queries.Class-19",
    }

    def __init__(self, parent, list_op=False):
        super(Dnsquery, self).__init__(parent, list_op)

    @property
    def HeaderTid(self):
        """
        Display Name: Transaction ID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderTid"]))

    @property
    def DnsflagsQRBit(self):
        """
        Display Name: QR
        Default Value: 1
        Value Format: decimal
        Available enum values: Query, 0, Response, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DnsflagsQRBit"]))

    @property
    def DnsflagsOpcode(self):
        """
        Display Name: OpCode
        Default Value: 0
        Value Format: decimal
        Available enum values: Query, 0, Inverse Query, 1, Status, 2, Notify, 4, Update, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DnsflagsOpcode"])
        )

    @property
    def DnsflagsAABit(self):
        """
        Display Name: AA
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DnsflagsAABit"]))

    @property
    def DnsflagsTCBit(self):
        """
        Display Name: TC
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DnsflagsTCBit"]))

    @property
    def DnsflagsRDBit(self):
        """
        Display Name: RD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DnsflagsRDBit"]))

    @property
    def DnsflagsRABit(self):
        """
        Display Name: RA
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DnsflagsRABit"]))

    @property
    def DnsflagsZBit(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DnsflagsZBit"]))

    @property
    def DnsflagsADBit(self):
        """
        Display Name: AD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DnsflagsADBit"]))

    @property
    def DnsflagsCDBit(self):
        """
        Display Name: CD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DnsflagsCDBit"]))

    @property
    def DnsflagsRcode(self):
        """
        Display Name: RCODE
        Default Value: 0
        Value Format: decimal
        Available enum values: No Error, 0, Format Error, 1, Server Failure, 2, Non-Existent Domain, 3, Not Implemented, 4, Query Refused, 5, YXDomain, 6, YXRRSet, 7, NXRRSet, 8, NotAuth, 9, NotZone, 10, Bad OPT Version, 16, TSIG Signature failure, 16, BADKEY, 17, BADTIME, 18, BADMODE, 19, BADNAME, 20, BADALG, 21
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DnsflagsRcode"]))

    @property
    def HeaderQCount(self):
        """
        Display Name: Query Count
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderQCount"]))

    @property
    def HeaderACount(self):
        """
        Display Name: Answer Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderACount"]))

    @property
    def HeaderAuthCount(self):
        """
        Display Name: Authority Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderAuthCount"])
        )

    @property
    def HeaderInfoCount(self):
        """
        Display Name: Additional Info Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderInfoCount"])
        )

    @property
    def QueriesLength(self):
        """
        Display Name: Name Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["QueriesLength"]))

    @property
    def QueriesName(self):
        """
        Display Name: NAME
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["QueriesName"]))

    @property
    def QueriesType(self):
        """
        Display Name: TYPE
        Default Value: 1
        Value Format: decimal
        Available enum values: A, 1, AAAA, 28, CNAME, 5, DNAME, 39, DNSKEY, 48
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["QueriesType"]))

    @property
    def QueriesClass(self):
        """
        Display Name: CLASS
        Default Value: 1
        Value Format: decimal
        Available enum values: Internet(IN), 1, Chaos(CH), 3, Hesiod(HS), 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["QueriesClass"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
