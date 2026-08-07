from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ESUN(Base):
    __slots__ = ()
    _SDM_NAME = "ESUN"
    _SDM_ATT_MAP = {
        "Revision": "ESUN.header.Revision-1",
        "FlowLabelValid": "ESUN.header.flowLabelValid-2",
        "EhCoS": "ESUN.header.ehCoS-3",
        "EhECN": "ESUN.header.ehECN-4",
        "FlowLabel": "ESUN.header.flowLabel-5",
        "Ttl": "ESUN.header.ttl-6",
        "UserDefined": "ESUN.header.userDefined-7",
        "Reserved": "ESUN.header.reserved-8",
    }

    def __init__(self, parent, list_op=False):
        super(ESUN, self).__init__(parent, list_op)

    @property
    def Revision(self):
        """
        Display Name: Revision
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Revision"]))

    @property
    def FlowLabelValid(self):
        """
        Display Name: Flow Label Valid
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlowLabelValid"])
        )

    @property
    def EhCoS(self):
        """
        Display Name: EH-CoS
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EhCoS"]))

    @property
    def EhECN(self):
        """
        Display Name: EH-ECN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EhECN"]))

    @property
    def FlowLabel(self):
        """
        Display Name: Flow Label
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlowLabel"]))

    @property
    def Ttl(self):
        """
        Display Name: TTL
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ttl"]))

    @property
    def UserDefined(self):
        """
        Display Name: User Defined
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UserDefined"]))

    @property
    def Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
