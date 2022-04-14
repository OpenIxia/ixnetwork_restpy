from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class JpegVideoFormat(Base):
    __slots__ = ()
    _SDM_NAME = "jpegVideoFormat"
    _SDM_ATT_MAP = {
        "JpegMainHeaderTypeSpecific": "jpegVideoFormat.header.jpegMainHeader.typeSpecific-1",
        "JpegMainHeaderFragmentOffset": "jpegVideoFormat.header.jpegMainHeader.fragmentOffset-2",
        "JpegMainHeaderType": "jpegVideoFormat.header.jpegMainHeader.type-3",
        "JpegMainHeaderQtable": "jpegVideoFormat.header.jpegMainHeader.qtable-4",
        "JpegMainHeaderWidth": "jpegVideoFormat.header.jpegMainHeader.width-5",
        "JpegMainHeaderHeight": "jpegVideoFormat.header.jpegMainHeader.height-6",
        "RestartMarkerHeaderRestartInterval": "jpegVideoFormat.header.jpegPayloadData.restartMarkerHeader.restartInterval-7",
        "RestartMarkerHeaderFirst": "jpegVideoFormat.header.jpegPayloadData.restartMarkerHeader.first-8",
        "RestartMarkerHeaderLast": "jpegVideoFormat.header.jpegPayloadData.restartMarkerHeader.last-9",
        "RestartMarkerHeaderRestartCount": "jpegVideoFormat.header.jpegPayloadData.restartMarkerHeader.restartCount-10",
        "QuantizationTableHeaderMbz": "jpegVideoFormat.header.jpegPayloadData.quantizationTableHeader.mbz-11",
        "QuantizationTableHeaderPrecision": "jpegVideoFormat.header.jpegPayloadData.quantizationTableHeader.precision-12",
        "QuantizationTableHeaderLength": "jpegVideoFormat.header.jpegPayloadData.quantizationTableHeader.length-13",
        "QuantizationTableHeaderData": "jpegVideoFormat.header.jpegPayloadData.quantizationTableHeader.data-14",
    }

    def __init__(self, parent, list_op=False):
        super(JpegVideoFormat, self).__init__(parent, list_op)

    @property
    def JpegMainHeaderTypeSpecific(self):
        """
        Display Name: Type Specific
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["JpegMainHeaderTypeSpecific"])
        )

    @property
    def JpegMainHeaderFragmentOffset(self):
        """
        Display Name: Fragment offset
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["JpegMainHeaderFragmentOffset"])
        )

    @property
    def JpegMainHeaderType(self):
        """
        Display Name: Type
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["JpegMainHeaderType"])
        )

    @property
    def JpegMainHeaderQtable(self):
        """
        Display Name: Q
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["JpegMainHeaderQtable"])
        )

    @property
    def JpegMainHeaderWidth(self):
        """
        Display Name: Width
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["JpegMainHeaderWidth"])
        )

    @property
    def JpegMainHeaderHeight(self):
        """
        Display Name: Height
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["JpegMainHeaderHeight"])
        )

    @property
    def RestartMarkerHeaderRestartInterval(self):
        """
        Display Name: Restart Interval
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RestartMarkerHeaderRestartInterval"]
            ),
        )

    @property
    def RestartMarkerHeaderFirst(self):
        """
        Display Name: F
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RestartMarkerHeaderFirst"])
        )

    @property
    def RestartMarkerHeaderLast(self):
        """
        Display Name: L
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RestartMarkerHeaderLast"])
        )

    @property
    def RestartMarkerHeaderRestartCount(self):
        """
        Display Name: Restart Count
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RestartMarkerHeaderRestartCount"]),
        )

    @property
    def QuantizationTableHeaderMbz(self):
        """
        Display Name: MBZ
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["QuantizationTableHeaderMbz"])
        )

    @property
    def QuantizationTableHeaderPrecision(self):
        """
        Display Name: Precision
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["QuantizationTableHeaderPrecision"]),
        )

    @property
    def QuantizationTableHeaderLength(self):
        """
        Display Name: Length
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["QuantizationTableHeaderLength"]),
        )

    @property
    def QuantizationTableHeaderData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["QuantizationTableHeaderData"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
