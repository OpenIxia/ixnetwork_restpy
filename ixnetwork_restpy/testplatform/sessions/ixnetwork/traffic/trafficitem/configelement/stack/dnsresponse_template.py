from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Dnsresponse(Base):
    __slots__ = ()
    _SDM_NAME = "dns_response"
    _SDM_ATT_MAP = {
        "HeaderTid": "dns_response.header.tid-1",
        "DnsflagsQRBit": "dns_response.header.dnsflags.QRBit-2",
        "DnsflagsOpcode": "dns_response.header.dnsflags.opcode-3",
        "DnsflagsAABit": "dns_response.header.dnsflags.AABit-4",
        "DnsflagsTCBit": "dns_response.header.dnsflags.TCBit-5",
        "DnsflagsRDBit": "dns_response.header.dnsflags.RDBit-6",
        "DnsflagsRABit": "dns_response.header.dnsflags.RABit-7",
        "DnsflagsZBit": "dns_response.header.dnsflags.ZBit-8",
        "DnsflagsADBit": "dns_response.header.dnsflags.ADBit-9",
        "DnsflagsCDBit": "dns_response.header.dnsflags.CDBit-10",
        "DnsflagsRcode": "dns_response.header.dnsflags.rcode-11",
        "HeaderQCount": "dns_response.header.QCount-12",
        "HeaderACount": "dns_response.header.ACount-13",
        "HeaderAuthCount": "dns_response.header.AuthCount-14",
        "HeaderInfoCount": "dns_response.header.InfoCount-15",
        "QueriesLength": "dns_response.header.queries.length-16",
        "QueriesName": "dns_response.header.queries.Name-17",
        "QueriesType": "dns_response.header.queries.Type-18",
        "QueriesClass": "dns_response.header.queries.Class-19",
        "AnswersLength": "dns_response.header.rrtype.answers.length-20",
        "AnswersName": "dns_response.header.rrtype.answers.Name-21",
        "AnswersType": "dns_response.header.rrtype.answers.Type-22",
        "AnswersClass": "dns_response.header.rrtype.answers.Class-23",
        "AnswersTtl": "dns_response.header.rrtype.answers.Ttl-24",
        "AnswersRdlen": "dns_response.header.rrtype.answers.rdlen-25",
        "AnswersRdata": "dns_response.header.rrtype.answers.rdata-26",
        "AuthnameserversLength": "dns_response.header.rrtype.authnameservers.length-27",
        "AuthnameserversName": "dns_response.header.rrtype.authnameservers.Name-28",
        "AuthnameserversType": "dns_response.header.rrtype.authnameservers.Type-29",
        "AuthnameserversClass": "dns_response.header.rrtype.authnameservers.Class-30",
        "AuthnameserversTtl": "dns_response.header.rrtype.authnameservers.Ttl-31",
        "AuthnameserversRdlen": "dns_response.header.rrtype.authnameservers.rdlen-32",
        "AuthnameserversRdata": "dns_response.header.rrtype.authnameservers.rdata-33",
        "AdditionalinfoLength": "dns_response.header.rrtype.additionalinfo.length-34",
        "AdditionalinfoName": "dns_response.header.rrtype.additionalinfo.Name-35",
        "AdditionalinfoType": "dns_response.header.rrtype.additionalinfo.Type-36",
        "AdditionalinfoClass": "dns_response.header.rrtype.additionalinfo.Class-37",
        "AdditionalinfoTtl": "dns_response.header.rrtype.additionalinfo.Ttl-38",
        "AdditionalinfoRdlen": "dns_response.header.rrtype.additionalinfo.rdlen-39",
        "AdditionalinfoRdata": "dns_response.header.rrtype.additionalinfo.rdata-40",
    }

    def __init__(self, parent, list_op=False):
        super(Dnsresponse, self).__init__(parent, list_op)

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

    @property
    def AnswersLength(self):
        """
        Display Name: Name Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AnswersLength"]))

    @property
    def AnswersName(self):
        """
        Display Name: NAME
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AnswersName"]))

    @property
    def AnswersType(self):
        """
        Display Name: TYPE
        Default Value: 1
        Value Format: decimal
        Available enum values: A, 1, AAAA, 28, CNAME, 5, DNAME, 39, DNSKEY, 48
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AnswersType"]))

    @property
    def AnswersClass(self):
        """
        Display Name: CLASS
        Default Value: 1
        Value Format: decimal
        Available enum values: Internet(IN), 1, Chaos(CH), 3, Hesiod(HS), 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AnswersClass"]))

    @property
    def AnswersTtl(self):
        """
        Display Name: TTL
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AnswersTtl"]))

    @property
    def AnswersRdlen(self):
        """
        Display Name: RDLENGTH
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AnswersRdlen"]))

    @property
    def AnswersRdata(self):
        """
        Display Name: RDATA
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AnswersRdata"]))

    @property
    def AuthnameserversLength(self):
        """
        Display Name: Name Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthnameserversLength"])
        )

    @property
    def AuthnameserversName(self):
        """
        Display Name: NAME
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthnameserversName"])
        )

    @property
    def AuthnameserversType(self):
        """
        Display Name: TYPE
        Default Value: 1
        Value Format: decimal
        Available enum values: A, 1, AAAA, 28, CNAME, 5, DNAME, 39, DNSKEY, 48
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthnameserversType"])
        )

    @property
    def AuthnameserversClass(self):
        """
        Display Name: CLASS
        Default Value: 1
        Value Format: decimal
        Available enum values: Internet(IN), 1, Chaos(CH), 3, Hesiod(HS), 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthnameserversClass"])
        )

    @property
    def AuthnameserversTtl(self):
        """
        Display Name: TTL
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthnameserversTtl"])
        )

    @property
    def AuthnameserversRdlen(self):
        """
        Display Name: RDLENGTH
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthnameserversRdlen"])
        )

    @property
    def AuthnameserversRdata(self):
        """
        Display Name: RDATA
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthnameserversRdata"])
        )

    @property
    def AdditionalinfoLength(self):
        """
        Display Name: Name Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdditionalinfoLength"])
        )

    @property
    def AdditionalinfoName(self):
        """
        Display Name: NAME
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdditionalinfoName"])
        )

    @property
    def AdditionalinfoType(self):
        """
        Display Name: TYPE
        Default Value: 1
        Value Format: decimal
        Available enum values: A, 1, AAAA, 28, CNAME, 5, DNAME, 39, DNSKEY, 48
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdditionalinfoType"])
        )

    @property
    def AdditionalinfoClass(self):
        """
        Display Name: CLASS
        Default Value: 1
        Value Format: decimal
        Available enum values: Internet(IN), 1, Chaos(CH), 3, Hesiod(HS), 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdditionalinfoClass"])
        )

    @property
    def AdditionalinfoTtl(self):
        """
        Display Name: TTL
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdditionalinfoTtl"])
        )

    @property
    def AdditionalinfoRdlen(self):
        """
        Display Name: RDLENGTH
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdditionalinfoRdlen"])
        )

    @property
    def AdditionalinfoRdata(self):
        """
        Display Name: RDATA
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdditionalinfoRdata"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
