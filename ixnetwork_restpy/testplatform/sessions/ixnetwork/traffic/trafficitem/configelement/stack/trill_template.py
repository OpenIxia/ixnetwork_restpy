from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Trill(Base):
    __slots__ = ()
    _SDM_NAME = "trill"
    _SDM_ATT_MAP = {
        "Ver": "trill.trillHeader.ver-1",
        "Res": "trill.trillHeader.res-2",
        "Multdest": "trill.trillHeader.multdest-3",
        "Oplen": "trill.trillHeader.oplen-4",
        "Hpcnt": "trill.trillHeader.hpcnt-5",
        "Erbridge": "trill.trillHeader.erbridge-6",
        "Irbridge": "trill.trillHeader.irbridge-7",
        "Critical_sum_bitsChbhs": "trill.trillHeader.options.trill_extension_header.critical_sum_bits.chbhs-8",
        "Critical_sum_bitsCites": "trill.trillHeader.options.trill_extension_header.critical_sum_bits.cites-9",
        "Critical_sum_bitsCrsvs": "trill.trillHeader.options.trill_extension_header.critical_sum_bits.crsvs-10",
        "Trill_extension_headerChbh": "trill.trillHeader.options.trill_extension_header.chbh-11",
        "Trill_extension_headerNchbh": "trill.trillHeader.options.trill_extension_header.nchbh-12",
        "Trill_extension_headerCrsv": "trill.trillHeader.options.trill_extension_header.crsv-13",
        "Trill_extension_headerNcrsv": "trill.trillHeader.options.trill_extension_header.ncrsv-14",
        "Trill_extension_headerCite": "trill.trillHeader.options.trill_extension_header.cite-15",
        "Trill_extension_headerNcite": "trill.trillHeader.options.trill_extension_header.ncite-16",
    }

    def __init__(self, parent, list_op=False):
        super(Trill, self).__init__(parent, list_op)

    @property
    def Ver(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ver"]))

    @property
    def Res(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Res"]))

    @property
    def Multdest(self):
        """
        Display Name: Multi Destination
        Default Value: 0
        Value Format: decimal
        Available enum values: Nickname represents Unicast Mac, 0, Nickname represents Distribution Tree, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Multdest"]))

    @property
    def Oplen(self):
        """
        Display Name: Options Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Oplen"]))

    @property
    def Hpcnt(self):
        """
        Display Name: Hop Count
        Default Value: 63
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Hpcnt"]))

    @property
    def Erbridge(self):
        """
        Display Name: Egress RBridge Nickname
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Erbridge"]))

    @property
    def Irbridge(self):
        """
        Display Name: Ingress RBridge Nickname
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Irbridge"]))

    @property
    def Critical_sum_bitsChbhs(self):
        """
        Display Name: Critical Hop-by-Hop extension(s) Present Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Critical_sum_bitsChbhs"])
        )

    @property
    def Critical_sum_bitsCites(self):
        """
        Display Name: Critical Ingress-to-Egress extension(s) Present Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Critical_sum_bitsCites"])
        )

    @property
    def Critical_sum_bitsCrsvs(self):
        """
        Display Name: Critical reserved extension(s) Present Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Critical_sum_bitsCrsvs"])
        )

    @property
    def Trill_extension_headerChbh(self):
        """
        Display Name: Critical Hop-by-Hop extended Flag Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Trill_extension_headerChbh"])
        )

    @property
    def Trill_extension_headerNchbh(self):
        """
        Display Name: Non-critical Hop-by-Hop extended Flag Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Trill_extension_headerNchbh"])
        )

    @property
    def Trill_extension_headerCrsv(self):
        """
        Display Name: Critical Reserved extended Flag Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Trill_extension_headerCrsv"])
        )

    @property
    def Trill_extension_headerNcrsv(self):
        """
        Display Name: Non-critical Reserved extended Flag Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Trill_extension_headerNcrsv"])
        )

    @property
    def Trill_extension_headerCite(self):
        """
        Display Name: Critical Ingress-to-Egress extended Flag Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Trill_extension_headerCite"])
        )

    @property
    def Trill_extension_headerNcite(self):
        """
        Display Name: Non-critical Ingress-to-Egress extended Flag Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Trill_extension_headerNcite"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
