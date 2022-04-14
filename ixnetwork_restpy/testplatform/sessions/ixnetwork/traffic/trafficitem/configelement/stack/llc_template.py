from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Llc(Base):
    __slots__ = ()
    _SDM_NAME = "llc"
    _SDM_ATT_MAP = {
        "HeaderDsap": "llc.header.dsap-1",
        "HeaderSsap": "llc.header.ssap-2",
        "HeaderControlField": "llc.header.controlField-3",
    }

    def __init__(self, parent, list_op=False):
        super(Llc, self).__init__(parent, list_op)

    @property
    def HeaderDsap(self):
        """
        Display Name: DSAP
        Default Value: 0x42
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderDsap"]))

    @property
    def HeaderSsap(self):
        """
        Display Name: SSAP
        Default Value: 0x42
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSsap"]))

    @property
    def HeaderControlField(self):
        """
        Display Name: Control field
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderControlField"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
