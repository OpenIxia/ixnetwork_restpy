from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MrcEndpointResponseHeader(Base):
    __slots__ = ()
    _SDM_NAME = "mrcEndpointResponseHeader"
    _SDM_ATT_MAP = {
        "EndpointResponseHeaderEethType": "mrcEndpointResponseHeader.endpointResponseHeader.eethType-1",
        "EndpointResponseHeaderNxt": "mrcEndpointResponseHeader.endpointResponseHeader.nxt-2",
        "EndpointResponseHeaderRes1": "mrcEndpointResponseHeader.endpointResponseHeader.res1-3",
        "EndpointResponseHeaderOp": "mrcEndpointResponseHeader.endpointResponseHeader.op-4",
        "EndpointResponseHeaderRes2": "mrcEndpointResponseHeader.endpointResponseHeader.res2-5",
        "EndpointResponseHeaderRes3": "mrcEndpointResponseHeader.endpointResponseHeader.res3-6",
        "EndpointResponseHeaderRes4": "mrcEndpointResponseHeader.endpointResponseHeader.res4-7",
        "EndpointResponseHeaderRes5": "mrcEndpointResponseHeader.endpointResponseHeader.res5-8",
        "EndpointResponseHeaderRes6": "mrcEndpointResponseHeader.endpointResponseHeader.res6-9",
        "EndpointResponseHeaderRes7": "mrcEndpointResponseHeader.endpointResponseHeader.res7-10",
        "EndpointResponseHeaderTxTimestamp": "mrcEndpointResponseHeader.endpointResponseHeader.txTimestamp-11",
        "EndpointResponseHeaderRes8": "mrcEndpointResponseHeader.endpointResponseHeader.res8-12",
        "EndpointResponseHeaderRes9": "mrcEndpointResponseHeader.endpointResponseHeader.res9-13",
    }

    def __init__(self, parent, list_op=False):
        super(MrcEndpointResponseHeader, self).__init__(parent, list_op)

    @property
    def EndpointResponseHeaderEethType(self):
        """
        Display Name: Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderEethType"]),
        )

    @property
    def EndpointResponseHeaderNxt(self):
        """
        Display Name: Next Header
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderNxt"])
        )

    @property
    def EndpointResponseHeaderRes1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderRes1"])
        )

    @property
    def EndpointResponseHeaderOp(self):
        """
        Display Name: Endpoint Operation
        Default Value: 0
        Value Format: decimal
        Available enum values: Port Status Update, 0, EV Probe, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderOp"])
        )

    @property
    def EndpointResponseHeaderRes2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderRes2"])
        )

    @property
    def EndpointResponseHeaderRes3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderRes3"])
        )

    @property
    def EndpointResponseHeaderRes4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderRes4"])
        )

    @property
    def EndpointResponseHeaderRes5(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderRes5"])
        )

    @property
    def EndpointResponseHeaderRes6(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderRes6"])
        )

    @property
    def EndpointResponseHeaderRes7(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderRes7"])
        )

    @property
    def EndpointResponseHeaderTxTimestamp(self):
        """
        Display Name: TX Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderTxTimestamp"]),
        )

    @property
    def EndpointResponseHeaderRes8(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderRes8"])
        )

    @property
    def EndpointResponseHeaderRes9(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointResponseHeaderRes9"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
