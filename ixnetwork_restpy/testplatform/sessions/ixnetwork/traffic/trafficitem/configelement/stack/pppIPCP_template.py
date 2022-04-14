from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PppIPCP(Base):
    __slots__ = ()
    _SDM_NAME = "pppIPCP"
    _SDM_ATT_MAP = {
        "HeaderCode": "pppIPCP.header.code-1",
        "HeaderIdFier": "pppIPCP.header.idFier-2",
        "HeaderLength11": "pppIPCP.header.length11-3",
        "ConfOptsType22": "pppIPCP.header.dataInIpcp.confOpts.type22-4",
        "ConfOptsLength7": "pppIPCP.header.dataInIpcp.confOpts.length7-5",
        "FurFldsIpCompProto11": "pppIPCP.header.dataInIpcp.confOpts.nxtFlds.furFlds.ipCompProto11-6",
        "FurFldsMaxSlt": "pppIPCP.header.dataInIpcp.confOpts.nxtFlds.furFlds.maxSlt-7",
        "FurFldsCompSlt": "pppIPCP.header.dataInIpcp.confOpts.nxtFlds.furFlds.compSlt-8",
        "LenVal11Length77": "pppIPCP.header.dataInIpcp.confOpts.nxtFlds.furFlds.lenVal11.length77-9",
        "LenVal11Val7": "pppIPCP.header.dataInIpcp.confOpts.nxtFlds.furFlds.lenVal11.val7-10",
        "IpAddrNextFieldIpAddr44": "pppIPCP.header.dataInIpcp.confOpts.nxtFlds.ipAddrNextField.ipAddr44-11",
        "PrimDnsAddr1PrimAddrDns": "pppIPCP.header.dataInIpcp.confOpts.nxtFlds.primDnsAddr1.primAddrDns-12",
        "PrimNbrsAddr1PrimAddrNbr": "pppIPCP.header.dataInIpcp.confOpts.nxtFlds.primNbrsAddr1.primAddrNbr-13",
        "SecDnsAddr1SecAddrDns": "pppIPCP.header.dataInIpcp.confOpts.nxtFlds.secDnsAddr1.secAddrDns-14",
        "SecNbnsAddr1SecAddrNbns": "pppIPCP.header.dataInIpcp.confOpts.nxtFlds.secNbnsAddr1.secAddrNbns-15",
        "LenVal12Length8": "pppIPCP.header.dataInIpcp.lenVal12.length8-16",
        "LenVal12Val8": "pppIPCP.header.dataInIpcp.lenVal12.val8-17",
    }

    def __init__(self, parent, list_op=False):
        super(PppIPCP, self).__init__(parent, list_op)

    @property
    def HeaderCode(self):
        """
        Display Name: Code
        Default Value: 1
        Value Format: decimal
        Available enum values: Configure-Request, 1, Configure-Ack, 2, Configure-Nak, 3, Configure-Reject, 4, Terminate-Request, 5, Terminate-Ack, 6, Code-Reject, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderCode"]))

    @property
    def HeaderIdFier(self):
        """
        Display Name: Identifier
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderIdFier"]))

    @property
    def HeaderLength11(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength11"])
        )

    @property
    def ConfOptsType22(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        Available enum values: IP-Compression-Protocol, 2, IP-Address, 3, Primary DNS Server Address, 129, Primary NBNS Server Address, 130, Secondary DNS Server Address, 131, Secondary NBNS Server Address, 132
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfOptsType22"])
        )

    @property
    def ConfOptsLength7(self):
        """
        Display Name: Length of TLV
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfOptsLength7"])
        )

    @property
    def FurFldsIpCompProto11(self):
        """
        Display Name: IP Compression Protocol
        Default Value: 45
        Value Format: decimal
        Available enum values: Van Jacobson Compressed TCP/IP, 45
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FurFldsIpCompProto11"])
        )

    @property
    def FurFldsMaxSlt(self):
        """
        Display Name: Max-Slot-Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FurFldsMaxSlt"]))

    @property
    def FurFldsCompSlt(self):
        """
        Display Name: Comp-Slot-Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FurFldsCompSlt"])
        )

    @property
    def LenVal11Length77(self):
        """
        Display Name: Length of data field
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LenVal11Length77"])
        )

    @property
    def LenVal11Val7(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LenVal11Val7"]))

    @property
    def IpAddrNextFieldIpAddr44(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpAddrNextFieldIpAddr44"])
        )

    @property
    def PrimDnsAddr1PrimAddrDns(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrimDnsAddr1PrimAddrDns"])
        )

    @property
    def PrimNbrsAddr1PrimAddrNbr(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrimNbrsAddr1PrimAddrNbr"])
        )

    @property
    def SecDnsAddr1SecAddrDns(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SecDnsAddr1SecAddrDns"])
        )

    @property
    def SecNbnsAddr1SecAddrNbns(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SecNbnsAddr1SecAddrNbns"])
        )

    @property
    def LenVal12Length8(self):
        """
        Display Name: Length of data field
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LenVal12Length8"])
        )

    @property
    def LenVal12Val8(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LenVal12Val8"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
