from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MrcEndpointRequestHeader(Base):
    __slots__ = ()
    _SDM_NAME = "mrcEndpointRequestHeader"
    _SDM_ATT_MAP = {
        "EndpointRequestHeaderErthType": "mrcEndpointRequestHeader.endpointRequestHeader.erthType-1",
        "EndpointRequestHeaderNxt": "mrcEndpointRequestHeader.endpointRequestHeader.nxt-2",
        "EndpointRequestHeaderRes1": "mrcEndpointRequestHeader.endpointRequestHeader.res1-3",
        "EndpointRequestHeaderOp": "mrcEndpointRequestHeader.endpointRequestHeader.op-4",
        "EndpointRequestHeaderRes2": "mrcEndpointRequestHeader.endpointRequestHeader.res2-5",
        "EndpointRequestHeaderVendorInfo": "mrcEndpointRequestHeader.endpointRequestHeader.vendorInfo-6",
        "EndpointRequestHeaderPortStatusMask": "mrcEndpointRequestHeader.endpointRequestHeader.portStatusMask-7",
        "EndpointRequestHeaderRes3": "mrcEndpointRequestHeader.endpointRequestHeader.res3-8",
        "EndpointRequestHeaderTxTimestamp": "mrcEndpointRequestHeader.endpointRequestHeader.txTimestamp-9",
        "EndpointRequestHeaderTsr": "mrcEndpointRequestHeader.endpointRequestHeader.tsr-10",
        "EndpointRequestHeaderRes4": "mrcEndpointRequestHeader.endpointRequestHeader.res4-11",
        "EndpointRequestHeaderFtype": "mrcEndpointRequestHeader.endpointRequestHeader.ftype-12",
    }

    def __init__(self, parent, list_op=False):
        super(MrcEndpointRequestHeader, self).__init__(parent, list_op)

    @property
    def EndpointRequestHeaderErthType(self):
        """
        Display Name: Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EndpointRequestHeaderErthType"]),
        )

    @property
    def EndpointRequestHeaderNxt(self):
        """
        Display Name: Next Header
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointRequestHeaderNxt"])
        )

    @property
    def EndpointRequestHeaderRes1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointRequestHeaderRes1"])
        )

    @property
    def EndpointRequestHeaderOp(self):
        """
        Display Name: Endpoint Operation
        Default Value: 0
        Value Format: decimal
        Available enum values: Port Status Update, 0, EV Probe, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointRequestHeaderOp"])
        )

    @property
    def EndpointRequestHeaderRes2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointRequestHeaderRes2"])
        )

    @property
    def EndpointRequestHeaderVendorInfo(self):
        """
        Display Name: Vendor Info
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EndpointRequestHeaderVendorInfo"]),
        )

    @property
    def EndpointRequestHeaderPortStatusMask(self):
        """
        Display Name: Port Status Mask
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EndpointRequestHeaderPortStatusMask"]
            ),
        )

    @property
    def EndpointRequestHeaderRes3(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointRequestHeaderRes3"])
        )

    @property
    def EndpointRequestHeaderTxTimestamp(self):
        """
        Display Name: TX Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EndpointRequestHeaderTxTimestamp"]),
        )

    @property
    def EndpointRequestHeaderTsr(self):
        """
        Display Name: Timestamp Resolution
        Default Value: 0
        Value Format: decimal
        Available enum values: 128ns, 0, Implementation defined, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointRequestHeaderTsr"])
        )

    @property
    def EndpointRequestHeaderRes4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointRequestHeaderRes4"])
        )

    @property
    def EndpointRequestHeaderFtype(self):
        """
        Display Name: TSETH Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointRequestHeaderFtype"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
