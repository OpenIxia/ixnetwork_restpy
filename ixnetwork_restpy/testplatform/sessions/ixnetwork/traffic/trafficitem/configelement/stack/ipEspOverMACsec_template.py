from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IpEspOverMACsec(Base):
    __slots__ = ()
    _SDM_NAME = "ipEspOverMACsec"
    _SDM_ATT_MAP = {
        "HeaderSpi": "ipEspOverMACsec.header.spi-1",
        "HeaderSn": "ipEspOverMACsec.header.sn-2",
        "EncryptedDataLength": "ipEspOverMACsec.header.encryptedData.length-3",
        "EncryptedDataData": "ipEspOverMACsec.header.encryptedData.data-4",
        "PaddingLength": "ipEspOverMACsec.header.padding.length-5",
        "PaddingData": "ipEspOverMACsec.header.padding.data-6",
        "HeaderPadLength": "ipEspOverMACsec.header.padLength-7",
        "HeaderNextHeader": "ipEspOverMACsec.header.nextHeader-8",
        "HeaderEsn": "ipEspOverMACsec.header.esn-9",
        "HeaderIcv": "ipEspOverMACsec.header.icv-10",
    }

    def __init__(self, parent, list_op=False):
        super(IpEspOverMACsec, self).__init__(parent, list_op)

    @property
    def HeaderSpi(self):
        """
        Display Name: Security Paramaters Index
        Default Value: 0x1ff
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSpi"]))

    @property
    def HeaderSn(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSn"]))

    @property
    def EncryptedDataLength(self):
        """
        Display Name: Length (Bytes)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EncryptedDataLength"])
        )

    @property
    def EncryptedDataData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EncryptedDataData"])
        )

    @property
    def PaddingLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PaddingLength"]))

    @property
    def PaddingData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PaddingData"]))

    @property
    def HeaderPadLength(self):
        """
        Display Name: PadLength
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPadLength"])
        )

    @property
    def HeaderNextHeader(self):
        """
        Display Name: Next Header
        Default Value: 59
        Value Format: decimal
        Available enum values: HOPOPT, 0, ICMP, 1, IGMP, 2, GGP, 3, IP, 4, ST, 5, TCP, 6, CBT, 7, EGP, 8, IGP, 9, BBN-RCC-MON, 10, NVP-II, 11, PUP, 12, ARGUS, 13, EMCON, 14, XNET, 15, CHAOS, 16, UDP, 17, MUX, 18, DCN-MEAS, 19, HMP, 20, PRM, 21, XNS-IDP, 22, TRUNK-1, 23, TRUNK-2, 24, LEAF-1, 25, LEAF-2, 26, RDP, 27, IRTP, 28, ISO-TP4, 29, NETBLT, 30, MFE-NSP, 31, MERIT-INP, 32, SEP, 33, 3PC, 34, IDPR, 35, XTP, 36, DDP, 37, IDPR-CMTP, 38, TP++, 39, IL, 40, IPv6, 41, SDRP, 42, IPv6-Route, 43, IPv6-Frag, 44, IDRP, 45, RSVP, 46, GRE, 47, MHRP, 48, BNA, 49, ESP, 50, AH, 51, I-NLSP, 52, SWIPE, 53, NARP, 54, MOBILE, 55, TLSP, 56, SKIP, 57, IPv6-ICMP, 58, IPv6-NoNxt, 59, IPv6-Opts, 60, Any host internal protocol, 61, CFTP, 62, Any local network, 63, SAT-EXPAK, 64, KRYPTOLAN, 65, RVD, 66, IPPC, 67, Any distributed file system, 68, SAT-MON, 69, VISA, 70, IPCV, 71, CPNX, 72, CPHB, 73, WSN, 74, PVP, 75, BR-SAT-MON, 76, SUN-ND, 77, WB-MON, 78, WB-EXPAK, 79, ISO-IP, 80, VMTP, 81, SECURE-VMTP, 82, VINES, 83, TTP, 84, NSFNET-IGP, 85, DGP, 86, TCF, 87, EIGRP, 88, OSPFIGP, 89, Sprite-RPC, 90, LARP, 91, MTP, 92, AX.25, 93, IPIP, 94, MICP, 95, SCC-SP, 96, ETHERIP, 97, ENCAP, 98, Any private encryption, 99, GMTP, 100, IFMP, 101, PNNI, 102, PIM, 103, ARIS, 104, SCPS, 105, QNX, 106, A/N, 107, IPComp, 108, SNP, 109, Compaq-Peer, 110, IPX-in-IP, 111, VRRP, 112, PGM, 113, Any 0-hop protocol, 114, L2TP, 115, DDX, 116, IATP, 117, STP, 118, SRP, 119, UTI, 120, SMP, 121, SM, 122, PTP, 123, ISIS over IPv4, 124, FIRE, 125, CRTP, 126, CRUDP, 127, SSCOPMCE, 128, IPLT, 129, SPS, 130, PIPE, 131, SCTP, 132, FC, 133, RSVP-E2E-IGNORE, 134, Mobility Header, 135, UDPLite, 136, MPLS-in-IP, 137, Unassigned, 138, Unassigned, 139, Unassigned, 140, Unassigned, 141, Unassigned, 142, Unassigned, 143, Unassigned, 144, Unassigned, 145, Unassigned, 146, Unassigned, 147, Unassigned, 148, Unassigned, 149, Unassigned, 150, Unassigned, 151, Unassigned, 152, Unassigned, 153, Unassigned, 154, Unassigned, 155, Unassigned, 156, Unassigned, 157, Unassigned, 158, Unassigned, 159, Unassigned, 160, Unassigned, 161, Unassigned, 162, Unassigned, 163, Unassigned, 164, Unassigned, 165, Unassigned, 166, Unassigned, 167, Unassigned, 168, Unassigned, 169, Unassigned, 170, Unassigned, 171, Unassigned, 172, Unassigned, 173, Unassigned, 174, Unassigned, 175, Unassigned, 176, Unassigned, 177, Unassigned, 178, Unassigned, 179, Unassigned, 180, Unassigned, 181, Unassigned, 182, Unassigned, 183, Unassigned, 184, Unassigned, 185, Unassigned, 186, Unassigned, 187, Unassigned, 188, Unassigned, 189, Unassigned, 190, Unassigned, 191, Unassigned, 192, Unassigned, 193, Unassigned, 194, Unassigned, 195, Unassigned, 196, Unassigned, 197, Unassigned, 198, Unassigned, 199, Unassigned, 200, Unassigned, 201, Unassigned, 202, Unassigned, 203, Unassigned, 204, Unassigned, 205, Unassigned, 206, Unassigned, 207, Unassigned, 208, Unassigned, 209, Unassigned, 210, Unassigned, 211, Unassigned, 212, Unassigned, 213, Unassigned, 214, Unassigned, 215, Unassigned, 216, Unassigned, 217, Unassigned, 218, Unassigned, 219, Unassigned, 220, Unassigned, 221, Unassigned, 222, Unassigned, 223, Unassigned, 224, Unassigned, 225, Unassigned, 226, Unassigned, 227, Unassigned, 228, Unassigned, 229, Unassigned, 230, Unassigned, 231, Unassigned, 232, Unassigned, 233, Unassigned, 234, Unassigned, 235, Unassigned, 236, Unassigned, 237, Unassigned, 238, Unassigned, 239, Unassigned, 240, Unassigned, 241, Unassigned, 242, Unassigned, 243, Unassigned, 244, Unassigned, 245, Unassigned, 246, Unassigned, 247, Unassigned, 248, Unassigned, 249, Unassigned, 250, Unassigned, 251, Unassigned, 252, Unassigned, 253, Unassigned, 254, Reserved, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderNextHeader"])
        )

    @property
    def HeaderEsn(self):
        """
        Display Name: Extended Sequence Number (ESN)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderEsn"]))

    @property
    def HeaderIcv(self):
        """
        Display Name: Integrity Check Value (ICV)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderIcv"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
