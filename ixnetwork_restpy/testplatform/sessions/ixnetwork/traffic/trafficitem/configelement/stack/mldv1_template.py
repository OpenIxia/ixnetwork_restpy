from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Mldv1(Base):
    __slots__ = ()
    _SDM_NAME = 'mldv1'
    _SDM_ATT_MAP = {
        'HeaderType': 'mldv1 .header.type-1',
        'HeaderCode': 'mldv1 .header.code-2',
        'HeaderMldv1Checksum': 'mldv1 .header.mldv1Checksum-3',
        'MaximumResponseDelayValue': 'mldv1 .header.maximumResponseDelay.value-4',
        'MaximumResponseDelayValue': 'mldv1 .header.maximumResponseDelay.value-5',
        'MaximumResponseDelayValue': 'mldv1 .header.maximumResponseDelay.value-6',
        'HeaderReserved': 'mldv1 .header.reserved-7',
        'HeaderMulticastAddress': 'mldv1 .header.multicastAddress-8',
    }

    def __init__(self, parent, list_op=False):
        super(Mldv1, self).__init__(parent, list_op)

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 130
        Value Format: decimal
        Available enum values: Query, 130, Report, 131, Done, 132
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderType']))

    @property
    def HeaderCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderCode']))

    @property
    def HeaderMldv1Checksum(self):
        """
        Display Name: MLDv1 checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderMldv1Checksum']))

    @property
    def MaximumResponseDelayValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaximumResponseDelayValue']))

    @property
    def MaximumResponseDelayValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaximumResponseDelayValue']))

    @property
    def MaximumResponseDelayValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaximumResponseDelayValue']))

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderReserved']))

    @property
    def HeaderMulticastAddress(self):
        """
        Display Name: Multicast address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderMulticastAddress']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
