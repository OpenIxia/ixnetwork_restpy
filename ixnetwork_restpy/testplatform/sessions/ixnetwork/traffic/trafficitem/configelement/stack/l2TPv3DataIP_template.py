from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2TPv3DataIP(Base):
    __slots__ = ()
    _SDM_NAME = "l2TPv3DataIP"
    _SDM_ATT_MAP = {
        "SessionHeaderSessionId": "l2TPv3DataIP.dataHeader.sessionHeader.sessionId-1",
        "CookieCookie64": "l2TPv3DataIP.dataHeader.sessionHeader.cookie.cookie64-2",
        "CookieCookie32": "l2TPv3DataIP.dataHeader.sessionHeader.cookie.cookie32-3",
        "CustomCookieLength": "l2TPv3DataIP.dataHeader.sessionHeader.cookie.customCookie.length-4",
        "CustomCookieData": "l2TPv3DataIP.dataHeader.sessionHeader.cookie.customCookie.data-5",
        "L2SublayerReserved": "l2TPv3DataIP.dataHeader.l2Sublayer.reserved-6",
        "L2SublayerSequenceBit": "l2TPv3DataIP.dataHeader.l2Sublayer.sequenceBit-7",
        "L2SublayerReserved": "l2TPv3DataIP.dataHeader.l2Sublayer.reserved-8",
        "L2SublayerSequenceNumber": "l2TPv3DataIP.dataHeader.l2Sublayer.sequenceNumber-9",
    }

    def __init__(self, parent, list_op=False):
        super(L2TPv3DataIP, self).__init__(parent, list_op)

    @property
    def SessionHeaderSessionId(self):
        """
        Display Name: Session ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SessionHeaderSessionId"])
        )

    @property
    def CookieCookie64(self):
        """
        Display Name: 64-bit cookie
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CookieCookie64"])
        )

    @property
    def CookieCookie32(self):
        """
        Display Name: 32-bit cookie
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CookieCookie32"])
        )

    @property
    def CustomCookieLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CustomCookieLength"])
        )

    @property
    def CustomCookieData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CustomCookieData"])
        )

    @property
    def L2SublayerReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L2SublayerReserved"])
        )

    @property
    def L2SublayerSequenceBit(self):
        """
        Display Name: Sequence bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Invalid sequence number, 0, Valid sequence number, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L2SublayerSequenceBit"])
        )

    @property
    def L2SublayerReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L2SublayerReserved"])
        )

    @property
    def L2SublayerSequenceNumber(self):
        """
        Display Name: Sequence number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["L2SublayerSequenceNumber"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
